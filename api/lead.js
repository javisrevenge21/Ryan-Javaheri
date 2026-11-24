import { saveLead, saveRequest, json } from '../lib/leads.js';
import { timingSafeEqual } from 'node:crypto';

function fromVoiceAgent(request) {
  const want = process.env.VOICE_AGENT_SECRET || '';
  const got = request.headers.get('x-voice-agent-secret') || '';
  if (!want || got.length !== want.length) return false;
  return timingSafeEqual(Buffer.from(got), Buffer.from(want));
}

// Contact form submissions, and leads saved by the voice advisor during a call.
export async function POST(request) {
  let b;
  try {
    b = await request.json();
  } catch {
    return json({ ok: false, error: 'Bad request' }, 400);
  }
  if (b.company_url_hp) return json({ ok: true }); // honeypot: bots fill hidden fields
  if (fromVoiceAgent(request)) {
    try {
      if (b.kind === 'request') {
        if (!b.need) return json({ ok: false, error: 'need required' }, 400);
        await saveRequest({ ...b, page: 'voice-call' });
      } else {
        if (!b.name || (!b.email && !b.phone) || !b.need) return json({ ok: false, error: 'name, contact and need required' }, 400);
        await saveLead({ ...b, source: 'voice-call' });
      }
      return json({ ok: true });
    } catch (e) {
      console.error('voice lead save failed', e?.message);
      return json({ ok: false }, 500);
    }
  }
  if (!b.name || (!b.email && !b.phone) || !b.need) {
    return json({ ok: false, error: 'Please add your name, an email or phone, and what you need.' }, 400);
  }
  try {
    await saveLead({ ...b, source: ['scan', 'call-request'].includes(b.source) ? b.source : 'contact-form' });
    return json({ ok: true });
  } catch (e) {
    console.error('lead save failed', e?.message);
    return json({ ok: false, error: 'Could not save right now. Please email ryanjavaheri21@gmail.com.' }, 500);
  }
}
