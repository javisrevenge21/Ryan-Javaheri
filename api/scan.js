import { generateText, Output } from 'ai';
import { z } from 'zod';
import { saveLead, json } from '../lib/leads.js';
import { withModel } from '../lib/ai.js';
import { countEvent } from '../lib/analytics.js';

const schema = z.object({
  recognized: z
    .enum(['yes', 'partly', 'no'])
    .describe('Whether you, the model, recognize this specific business from your own knowledge'),
  whatAiSays: z
    .string()
    .describe(
      'In 2-3 sentences, what you would currently tell a user who asked about this business. If you do not recognize it, say so plainly. Never invent facts.',
    ),
  score: z
    .number()
    .min(0)
    .max(100)
    .describe('Estimated AI visibility score 0-100. Unrecognized local businesses should score low.'),
  likelyQuestions: z
    .array(z.string())
    .min(3)
    .max(5)
    .describe('Questions real customers of this kind of business ask AI assistants'),
  quickWins: z
    .array(z.string())
    .min(3)
    .max(5)
    .describe('Specific, practical steps to become the answer AI gives (schema, FAQ content, listings, reviews, llms.txt, etc.)'),
});

export async function POST(request) {
  let b;
  try {
    b = await request.json();
  } catch {
    return json({ error: 'Bad request' }, 400);
  }
  if (b.company_url_hp) return json({ error: 'Bad request' }, 400);
  const business = String(b.business || '').trim().slice(0, 120);
  const website = String(b.website || '').trim().slice(0, 200);
  const city = String(b.city || '').trim().slice(0, 80);
  const category = String(b.category || '').trim().slice(0, 80);
  if (!business) return json({ error: 'Add your business name.' }, 400);

  try {
    const { output } = await withModel((model) => generateText({
      model,
      output: Output.object({ schema }),
      maxOutputTokens: 2000,
      system:
        'You are an AI visibility auditor. Answer only from your own built-in knowledge (no browsing). Be honest: if you do not recognize a business, say so; that is the most useful finding. Never fabricate details, reviews or rankings about a business.',
      prompt: `Business: ${business}\nWebsite: ${website || 'not given'}\nCity/area: ${city || 'not given'}\nType of business: ${category || 'not given'}\n\nRun an AI visibility check for this business.`,
    }));

    if (b.email || b.phone) {
      await saveLead({
        source: 'scan',
        name: b.name,
        email: b.email,
        phone: b.phone,
        company: business,
        website,
        need: `Free AI visibility scan (${category || 'business'} in ${city || 'unknown area'}). Score ${Math.round(output.score)}.`,
        details: output.whatAiSays,
        page: '/#scan',
        extra: { scan: output },
      }).catch((e) => console.error('scan lead save failed', e?.message));
    }

    await countEvent('Scan', { withContact: Boolean(b.email || b.phone) }, request);

    return json({ result: output });
  } catch (e) {
    console.error('scan error', e?.message);
    return json({ error: 'The scan is busy right now. Leave your email and Ryan will run it for you.' }, 500);
  }
}
