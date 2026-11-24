"""Ryan's voice advisor: a LiveKit agent that takes intake calls in Ryan's cloned voice.

Pipeline:  caller audio -> Deepgram (speech to text) -> Groq (replies) -> Chatterbox on Modal (Ryan's voice)
The same agent answers website visitors (the Talk button) and, later, phone calls (a SIP number
pointed at LiveKit). What it knows comes from prompt.txt, exported from the site's lib/profile.js.

Environment (LiveKit Cloud agent secrets, or a local .env):
  LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET   set by LiveKit Cloud automatically when hosted there
  DEEPGRAM_API_KEY                                    speech to text
  GROQ_API_KEY                                        replies
  GROQ_MODEL            optional, default openai/gpt-oss-120b
  TTS_URL               the Modal "speak" endpoint URL
  TTS_WARM_URL          the Modal "warm" endpoint URL (optional)
  TTS_TOKEN             the same random string as in the Modal secret
  SITE_URL              optional, default https://www.ryanjavaheri.com
  VOICE_AGENT_SECRET    the same random string as in Vercel; lets the agent save leads to the site

Run locally:  python agent.py dev      Hosted:  LiveKit Cloud (see README.md)
"""

from __future__ import annotations

import asyncio
import logging
import os
import uuid
from pathlib import Path

import aiohttp
from livekit.agents import (
    DEFAULT_API_CONNECT_OPTIONS,
    Agent,
    AgentServer,
    AgentSession,
    APIConnectOptions,
    JobContext,
    JobProcess,
    RunContext,
    cli,
    function_tool,
    tts,
)
from livekit.plugins import deepgram, openai, silero

log = logging.getLogger("ryan-voice")

AGENT_NAME = "ryan-advisor"
SAMPLE_RATE = 24000
SITE_URL = os.environ.get("SITE_URL", "https://www.ryanjavaheri.com").rstrip("/")
MAX_CALL_MINUTES = int(os.environ.get("MAX_CALL_MINUTES", "15"))  # keeps one call from running up the GPU bill

VOICE_RULES = """
YOU ARE ON A LIVE VOICE CALL. These rules override the formatting rules above.
- Everything you write is spoken aloud in Ryan's cloned voice. Speak in short, natural sentences. One or two sentences per turn, then let the caller talk.
- At the start of the call, say that you're Ryan's AI assistant, speaking in a voice modeled on Ryan's. Never claim to be Ryan or any human.
- No markdown, lists, emoji or symbols. Say prices the way a person would ("two hundred forty-nine dollars a month").
- Don't read out full web addresses. Say the site name simply, like "scale dot siamak consulting dot com", and offer to have Ryan send the link by email.
- Speak English unless the caller speaks another language; then answer in theirs.
- To save details, ask for the caller's name and the best way to reach them, and read back an email address or phone number to confirm it before calling save_lead.
- When the caller is done, thank them and say goodbye.
"""


def load_instructions() -> str:
    base = (Path(__file__).parent / "prompt.txt").read_text(encoding="utf-8")
    return base + "\n" + VOICE_RULES


# ---------- Ryan's voice: Chatterbox on Modal ----------


class ChatterboxTTS(tts.TTS):
    """Sends one sentence at a time to the Modal GPU and plays back the PCM it returns.
    AgentSession splits replies into sentences for non-streaming TTS, so the caller hears
    the first sentence while the rest are still being made."""

    def __init__(self, url: str, token: str, http: aiohttp.ClientSession | None = None):
        super().__init__(
            capabilities=tts.TTSCapabilities(streaming=False),
            sample_rate=SAMPLE_RATE,
            num_channels=1,
        )
        self._url = url
        self._token = token
        self._http = http

    def _session(self) -> aiohttp.ClientSession:
        if self._http is None or self._http.closed:
            self._http = aiohttp.ClientSession()
        return self._http

    def synthesize(
        self, text: str, *, conn_options: APIConnectOptions = DEFAULT_API_CONNECT_OPTIONS
    ) -> "_ChatterboxStream":
        return _ChatterboxStream(tts=self, input_text=text, conn_options=conn_options)

    async def aclose(self) -> None:
        if self._http and not self._http.closed:
            await self._http.close()


class _ChatterboxStream(tts.ChunkedStream):
    async def _run(self, output_emitter: tts.AudioEmitter) -> None:
        t: ChatterboxTTS = self._tts  # type: ignore[assignment]
        output_emitter.initialize(
            request_id=str(uuid.uuid4()),
            sample_rate=SAMPLE_RATE,
            num_channels=1,
            mime_type="audio/pcm",
        )
        async with t._session().post(
            t._url,
            json={"text": self.input_text},
            headers={"Authorization": f"Bearer {t._token}"},
            timeout=aiohttp.ClientTimeout(total=60),
        ) as resp:
            resp.raise_for_status()
            async for chunk in resp.content.iter_chunked(4800):
                output_emitter.push(chunk)
        output_emitter.flush()


# ---------- The advisor ----------


async def post_to_site(payload: dict) -> bool:
    secret = os.environ.get("VOICE_AGENT_SECRET", "")
    if not secret:
        log.warning("VOICE_AGENT_SECRET not set; not saving %s", payload.get("kind"))
        return False
    async with aiohttp.ClientSession() as s:
        async with s.post(
            f"{SITE_URL}/api/lead",
            json=payload,
            headers={"x-voice-agent-secret": secret},
            timeout=aiohttp.ClientTimeout(total=15),
        ) as r:
            ok = r.status == 200
            if not ok:
                log.error("site refused %s: %s", payload.get("kind"), r.status)
            return ok


class Advisor(Agent):
    def __init__(self, channel: str) -> None:
        super().__init__(instructions=load_instructions())
        self.channel = channel  # "web" or "phone"

    def _transcript(self, ctx: RunContext) -> list[dict]:
        out = []
        for item in ctx.session.history.items:
            role = getattr(item, "role", None)
            text = getattr(item, "text_content", None)
            if role in ("user", "assistant") and text:
                out.append({"role": role, "content": text})
        return out[-40:]

    @function_tool()
    async def save_lead(
        self,
        ctx: RunContext,
        name: str,
        need: str,
        email: str = "",
        phone: str = "",
        company: str = "",
        timeline: str = "",
        products: str = "",
    ) -> str:
        """Save the caller's details so Ryan can follow up personally. Call once you have their
        name, at least one way to reach them (email or phone, read back and confirmed) and what they need.

        Args:
            name: the caller's name
            need: what they need, in a sentence or two (in English)
            email: their email address, if given
            phone: their phone number, if given
            company: their company or website, if given
            timeline: when they want it, if given
            products: catalog products they were interested in, comma-separated
        """
        ok = await post_to_site(
            {
                "kind": "lead",
                "name": name,
                "need": need,
                "email": email,
                "phone": phone,
                "company": company,
                "timeline": timeline,
                "details": f"Voice call ({self.channel})" + (f". Products: {products}" if products else ""),
                "transcript": self._transcript(ctx),
            }
        )
        return "Saved. Ryan has the details." if ok else "Saving failed; ask them to email ryanjavaheri21@gmail.com."

    @function_tool()
    async def report_unmet_request(
        self, ctx: RunContext, need: str, industry: str = "", closest_product: str = ""
    ) -> str:
        """Pass a need that none of the catalog products covers to Ryan, so he can build it.

        Args:
            need: the need, summarized in English
            industry: the caller's industry, if known
            closest_product: the closest product, if any partly fits
        """
        ok = await post_to_site(
            {
                "kind": "request",
                "need": need,
                "industry": industry,
                "closest_product": closest_product,
                "transcript": self._transcript(ctx),
            }
        )
        return "Passed on to Ryan." if ok else "Couldn't pass it on right now."


server = AgentServer()


def prewarm(proc: JobProcess) -> None:
    proc.userdata["vad"] = silero.VAD.load()


server.setup_fnc = prewarm


@server.rtc_session(agent_name=AGENT_NAME)
async def entrypoint(ctx: JobContext) -> None:
    channel = "phone" if ctx.room.name.startswith("call-") else "web"

    # Wake the GPU while the caller is still connecting.
    warm_url = os.environ.get("TTS_WARM_URL")
    if warm_url:
        async def _warm():
            try:
                async with aiohttp.ClientSession() as s:
                    await s.get(warm_url, timeout=aiohttp.ClientTimeout(total=120))
            except Exception as e:  # warming is best-effort
                log.info("warm-up failed: %s", e)

        asyncio.create_task(_warm())

    session = AgentSession(
        vad=ctx.proc.userdata["vad"],
        stt=deepgram.STT(model="nova-3", language="multi"),
        llm=openai.LLM(
            model=os.environ.get("GROQ_MODEL", "openai/gpt-oss-120b"),
            base_url="https://api.groq.com/openai/v1",
            api_key=os.environ["GROQ_API_KEY"],
        ),
        tts=ChatterboxTTS(url=os.environ["TTS_URL"], token=os.environ["TTS_TOKEN"]),
        preemptive_generation=True,
    )
    await session.start(agent=Advisor(channel), room=ctx.room)
    await session.generate_reply(
        instructions="Greet the caller warmly in one or two short sentences: say you're Ryan Javaheri's AI assistant, "
        "speaking in a voice modeled on Ryan's, and ask what they're looking for."
    )

    async def _time_limit():
        await asyncio.sleep(max(1, MAX_CALL_MINUTES - 1) * 60)
        await session.generate_reply(
            instructions="The call is about to reach its time limit. In one or two sentences, offer to save the caller's "
            "details so Ryan can follow up if you haven't already, then say goodbye."
        )
        await asyncio.sleep(60)
        ctx.shutdown(reason="call time limit")

    asyncio.create_task(_time_limit())


if __name__ == "__main__":
    cli.run_app(server)
