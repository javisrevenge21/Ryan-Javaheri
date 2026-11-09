import { listLeads, passwordOk, json } from '../lib/leads.js';

// Private inbox data for /leads. Requires the LEADS_PASSWORD environment variable.
export async function POST(request) {
  if (!process.env.LEADS_PASSWORD) {
    return json(
      { error: 'Inbox is locked: add a LEADS_PASSWORD environment variable in Vercel, then redeploy.' },
      503,
    );
  }
  let b = {};
  try {
    b = await request.json();
  } catch {}
  if (!passwordOk(b.password)) {
    await new Promise((r) => setTimeout(r, 600));
    return json({ error: 'Wrong password.' }, 401);
  }
  try {
    return json({ leads: await listLeads() });
  } catch (e) {
    console.error('list leads failed', e?.message);
    return json({ error: 'Could not load leads.' }, 500);
  }
}
