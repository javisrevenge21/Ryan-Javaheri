import { saveLead, json } from '../lib/leads.js';
import { countEvent } from '../lib/analytics.js';

// Contact form submissions.
export async function POST(request) {
  let b;
  try {
    b = await request.json();
  } catch {
    return json({ ok: false, error: 'Bad request' }, 400);
  }
  if (b.company_url_hp) return json({ ok: true }); // honeypot: bots fill hidden fields
  if (!b.name || (!b.email && !b.phone) || !b.need) {
    return json({ ok: false, error: 'Please add your name, an email or phone, and what you need.' }, 400);
  }
  try {
    const source = ['scan', 'call-request'].includes(b.source) ? b.source : 'contact-form';
    await saveLead({ ...b, source });
    await countEvent(source === 'call-request' ? 'Call request' : 'Lead', { source }, request);
    return json({ ok: true });
  } catch (e) {
    console.error('lead save failed', e?.message);
    return json({ ok: false, error: 'Could not save right now. Please email ryanjavaheri21@gmail.com.' }, 500);
  }
}
