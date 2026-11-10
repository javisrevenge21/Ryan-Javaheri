import { put, list, get } from '@vercel/blob';
import { randomUUID, timingSafeEqual, createHash } from 'node:crypto';

const PREFIX = 'leads/';

const clean = (v, max = 2000) =>
  typeof v === 'string' ? v.trim().slice(0, max) : v == null ? '' : String(v).slice(0, max);

export async function saveLead(input) {
  const now = new Date();
  const lead = {
    id: randomUUID(),
    createdAt: now.toISOString(),
    source: clean(input.source, 40) || 'unknown',
    name: clean(input.name, 120),
    email: clean(input.email, 200),
    phone: clean(input.phone, 60),
    company: clean(input.company, 200),
    website: clean(input.website, 300),
    need: clean(input.need, 2000),
    details: clean(input.details, 4000),
    timeline: clean(input.timeline, 200),
    language: clean(input.language, 40),
    page: clean(input.page, 300),
    transcript: Array.isArray(input.transcript)
      ? input.transcript.slice(-40).map((m) => ({ role: m.role, content: clean(m.content, 2000) }))
      : undefined,
    extra: input.extra && typeof input.extra === 'object' ? input.extra : undefined,
  };
  const stamp = now.toISOString().replace(/[:.]/g, '-');
  await put(`${PREFIX}${stamp}-${lead.id}.json`, JSON.stringify(lead, null, 2), {
    access: 'private',
    contentType: 'application/json',
    addRandomSuffix: false,
  });
  await notify(lead).catch((e) => console.error('lead notify failed', e?.message));
  return lead;
}

// A need the AI advisor couldn't match to any catalog product. Saved to the same private
// inbox (/leads) with source "unmet-request", so Ryan sees what to build next.
export async function saveRequest(input) {
  return saveLead({
    source: 'unmet-request',
    name: 'Product request',
    need: input.need,
    details: [input.industry && `Industry: ${clean(input.industry, 200)}`, input.closest_product && `Closest product: ${clean(input.closest_product, 120)}`]
      .filter(Boolean)
      .join(' | '),
    language: input.language,
    page: input.page,
    transcript: input.transcript,
  });
}

// Optional email alert. Works once RESEND_API_KEY and LEAD_NOTIFY_EMAIL are set in Vercel.
async function notify(lead) {
  const key = process.env.RESEND_API_KEY;
  const to = process.env.LEAD_NOTIFY_EMAIL;
  if (!key || !to) return;
  const isRequest = lead.source === 'unmet-request';
  const lines = [
    isRequest
      ? 'A visitor asked the AI advisor for something no catalog product covers yet.'
      : `New lead from ryanjavaheri.com (${lead.source})`,
    '',
    `Name: ${lead.name || '-'}`,
    `Email: ${lead.email || '-'}`,
    `Phone: ${lead.phone || '-'}`,
    `Company: ${lead.company || '-'}`,
    `Website: ${lead.website || '-'}`,
    `Timeline: ${lead.timeline || '-'}`,
    '',
    `Need: ${lead.need || '-'}`,
    lead.details ? `Details: ${lead.details}` : '',
    lead.extra?.products?.length ? `Interested in: ${lead.extra.products.join(', ')}` : '',
    lead.transcript?.length
      ? ['', 'Conversation:', ...lead.transcript.map((m) => `${m.role === 'user' ? 'Visitor' : 'Advisor'}: ${m.content}`)].join('\n')
      : '',
  ];
  await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      from: process.env.LEAD_FROM_EMAIL || 'Ryan AI Advisor <onboarding@resend.dev>',
      to: [to],
      subject: isRequest
        ? `Product request to build: ${lead.need.slice(0, 70)}`
        : `New lead: ${lead.name || 'website visitor'} - ${lead.need.slice(0, 60)}`,
      text: lines.join('\n'),
      reply_to: lead.email || undefined,
    }),
  });
}

export async function listLeads(limit = 200) {
  const { blobs } = await list({ prefix: PREFIX, limit: 1000 });
  blobs.sort((a, b) => (a.pathname < b.pathname ? 1 : -1));
  const out = [];
  for (const b of blobs.slice(0, limit)) {
    try {
      const res = await get(b.pathname, { access: 'private' });
      const text = await new Response(res.stream).text();
      out.push(JSON.parse(text));
    } catch (e) {
      console.error('read lead failed', b.pathname, e?.message);
    }
  }
  return out;
}

export function passwordOk(given) {
  const real = process.env.LEADS_PASSWORD;
  if (!real || !given) return false;
  const a = createHash('sha256').update(String(given)).digest();
  const b = createHash('sha256').update(real).digest();
  return timingSafeEqual(a, b);
}

export const json = (data, status = 200) =>
  new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' },
  });
