import { saveLead, json } from '../lib/leads.js';

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
    await saveLead({ ...b, source: b.source === 'scan' ? 'scan' : 'contact-form' });
    return json({ ok: true });
  } catch (e) {
    console.error('lead save failed', e?.message);
    return json({ ok: false, error: 'Could not save right now. Please email ryanjavaheri21@gmail.com.' }, 500);
  }
}
