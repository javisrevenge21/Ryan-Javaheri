# Ryan's voice advisor

Live voice calls with the site's AI advisor, in an AI voice modeled on Ryan's, on our own stack
instead of ElevenLabs credits.

```
caller (Talk button, later a phone number)
   -> LiveKit Cloud (call audio)  -> agent.py
        Deepgram nova-3   speech to text
        Groq              replies (same catalog prompt as the chat advisor)
        Modal L4 GPU      Chatterbox Turbo, cloned voice (tts_modal.py)
   -> leads saved through /api/lead to the site's private inbox
```

| Part | File | Runs on |
|---|---|---|
| Voice server | `tts_modal.py` | Modal, scales to zero when idle |
| Call agent | `agent.py`, `prompt.txt` | LiveKit Cloud agent hosting |
| Talk button | `assets/agent.js`, `assets/vendor/livekit-client.umd.js` | the site |
| Call token | `api/voice-token.js` | Vercel |

Until the LiveKit keys are in Vercel, `/api/voice-token` returns 503 and the Talk button keeps using
the browser's own voice, so merging this changes nothing for visitors.

## Setup (one time)

1. Free accounts: modal.com, cloud.livekit.io, console.deepgram.com, console.groq.com.
2. GitHub repo > Settings > Secrets and variables > Actions, add the secrets listed at the top of
   `.github/workflows/voice-deploy.yml`.
3. Vercel project > Settings > Environment Variables: `LIVEKIT_URL`, `LIVEKIT_API_KEY`,
   `LIVEKIT_API_SECRET`, `VOICE_AGENT_SECRET` (same value as the GitHub secret).
4. Actions > Deploy voice advisor > Run workflow. After the first run, commit the
   `voice-agent/livekit.toml` it prints.
5. Redeploy the site so the new Vercel variables take effect.

## Phone number (later)

Buy a number from a SIP provider (Twilio or Telnyx), point it at a LiveKit SIP inbound trunk, and
add a dispatch rule that sends calls to agent `ryan-advisor` in rooms named `call-…`. The agent
already treats `call-` rooms as phone calls.

## Changing what the advisor says

Edit `lib/profile.js` or `lib/catalog.js`. The workflow re-exports `prompt.txt` and redeploys.
Locally: `node voice-agent/export_prompt.mjs`.

## Cost guard

Calls end after 15 minutes (`MAX_CALL_MINUTES`). The GPU stays warm 5 minutes after the last
sentence and runs at most 2 containers.
