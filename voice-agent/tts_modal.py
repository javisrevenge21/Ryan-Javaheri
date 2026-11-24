"""Ryan's cloned voice, served from a Modal GPU.

Chatterbox Turbo (Resemble AI, MIT licence) speaks any text in the voice of a short
reference clip. The clip is NOT in this repo (the repo is public): it lives in the
Modal volume "ryan-voice" as /reference.wav. The deploy workflow puts it there from
the VOICE_REFERENCE_B64 repository secret.

Deploy:   pip install modal fastapi && modal deploy voice-agent/tts_modal.py
Needs:    Modal secret "ryan-voice-tts" with TTS_TOKEN (any long random string; the
          LiveKit agent sends it as a Bearer token so strangers can't use the GPU).

Endpoints (Modal prints their URLs on deploy):
  POST speak  {"text": "..."}  -> raw 16-bit mono PCM at 24 kHz (audio/pcm)
  GET  warm                    -> {"ok": true}; starts the GPU before the caller talks
"""

import os

import modal
from fastapi import Header  # installed next to modal wherever this file is deployed from

app = modal.App("ryan-voice-tts")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install("ffmpeg")
    .pip_install("chatterbox-tts==0.1.7", "fastapi[standard]")
)

hf_cache = modal.Volume.from_name("ryan-voice-hf-cache", create_if_missing=True)
voice_vol = modal.Volume.from_name("ryan-voice", create_if_missing=True)

SAMPLE_RATE = 24000
REFERENCE = "/voice/reference.wav"


@app.cls(
    gpu="L4",
    image=image,
    volumes={"/root/.cache/huggingface": hf_cache, "/voice": voice_vol},
    secrets=[modal.Secret.from_name("ryan-voice-tts")],
    scaledown_window=300,  # stay warm 5 minutes after the last sentence, then scale to zero
    timeout=600,
    max_containers=2,
)
@modal.concurrent(max_inputs=4)
class Voice:
    @modal.enter()
    def load(self):
        import torch

        device = "cuda" if torch.cuda.is_available() else "cpu"
        try:
            from chatterbox.tts_turbo import ChatterboxTurboTTS

            self.model = ChatterboxTurboTTS.from_pretrained(device=device)
        except Exception as e:  # fall back to the original model
            print("Turbo failed to load, using ChatterboxTTS:", e)
            from chatterbox.tts import ChatterboxTTS

            self.model = ChatterboxTTS.from_pretrained(device=device)
        if not os.path.exists(REFERENCE):
            raise RuntimeError("Missing /reference.wav in the Modal volume 'ryan-voice'.")
        self.model.prepare_conditionals(REFERENCE)
        hf_cache.commit()
        self.sr = self.model.sr

    def _authorized(self, auth):
        token = os.environ.get("TTS_TOKEN", "")
        return bool(token) and auth == f"Bearer {token}"

    @modal.fastapi_endpoint(method="POST")
    def speak(self, body: dict, authorization: str | None = Header(default=None)):
        from fastapi.responses import JSONResponse, Response
        import numpy as np

        if not self._authorized(authorization):
            return JSONResponse({"error": "unauthorized"}, status_code=401)
        text = str(body.get("text", "")).strip()[:600]
        if not text:
            return Response(b"", media_type="audio/pcm")
        wav = self.model.generate(text).squeeze(0).numpy()
        if self.sr != SAMPLE_RATE:
            import librosa

            wav = librosa.resample(wav, orig_sr=self.sr, target_sr=SAMPLE_RATE)
        pcm = (np.clip(wav, -1.0, 1.0) * 32767).astype("<i2").tobytes()
        return Response(pcm, media_type="audio/pcm", headers={"X-Sample-Rate": str(SAMPLE_RATE)})

    @modal.fastapi_endpoint(method="GET")
    def warm(self):
        return {"ok": True}
