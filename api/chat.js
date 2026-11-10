import { generateText, tool, isStepCount, Output } from 'ai';
import { waitUntil } from '@vercel/functions';
import { z } from 'zod';
import { SYSTEM_PROMPT } from '../lib/profile.js';
import { saveLead, saveRequest, json } from '../lib/leads.js';
import { withModel } from '../lib/ai.js';
import { PRODUCTS } from '../lib/catalog.js';

const PRODUCT_LIST = PRODUCTS.map((p) => `- ${p.name} (${p.category}): ${p.summary.split('. ')[0]}.`).join('\n');

const gapSchema = z.object({
  unmet: z.boolean().describe('true only if the latest visitor message asks for a product or service need that none of the products covers (fully or in part)'),
  need: z.string().describe('The uncovered need in one or two sentences, in English. Empty if unmet is false.'),
  industry: z.string().describe('Their industry or type of business, if known, else empty'),
  closest_product: z.string().describe('Closest product name if one partly fits, else empty'),
});

// Backstop: if the advisor didn't report a gap itself, double-check the latest message so no
// unmet request is lost. Runs after the reply is sent.
async function checkForGap(messages, reply) {
  const recent = messages.slice(-5).map((m) => `${m.role === 'user' ? 'Visitor' : 'Advisor'}: ${m.content}`).join('\n');
  const { output } = await withModel((model) => generateText({
    model,
    output: Output.object({ schema: gapSchema }),
    maxOutputTokens: 300,
    system:
      'You check a sales chat for needs that a fixed product list does not cover. Judge only the LATEST visitor message. Questions about the person Ryan, greetings, contact details, follow-ups about a product already recommended, and needs a product clearly covers are NOT unmet. A need only partly covered (e.g. wants phone answering but the product only does social media) IS unmet for the uncovered part.',
    prompt: `PRODUCTS:\n${PRODUCT_LIST}\n\nCONVERSATION (latest last):\n${recent}\nAdvisor reply just sent: ${reply}`,
  }));
  return output;
}

export async function POST(request) {
  let body;
  try {
    body = await request.json();
  } catch {
    return json({ error: 'Bad request' }, 400);
  }

  const messages = (Array.isArray(body.messages) ? body.messages : [])
    .filter((m) => m && (m.role === 'user' || m.role === 'assistant') && typeof m.content === 'string')
    .slice(-24)
    .map((m) => ({ role: m.role, content: m.content.slice(0, 2000) }));

  if (!messages.length || messages[messages.length - 1].role !== 'user') {
    return json({ error: 'No message' }, 400);
  }

  const page = typeof body.page === 'string' ? body.page.slice(0, 300) : '';
  const language = typeof body.language === 'string' ? body.language.slice(0, 20) : '';
  let leadSaved = false;

  const save_lead = tool({
    description:
      'Save the visitor as a lead so Ryan can follow up personally. Call once you have their name, at least one contact method (email or phone), and what they need.',
    inputSchema: z.object({
      name: z.string().describe("Visitor's name"),
      email: z.string().optional().describe('Email address, if given'),
      phone: z.string().optional().describe('Phone number, if given'),
      company: z.string().optional().describe('Company or organization, if given'),
      website: z.string().optional().describe('Their website, if given'),
      need: z.string().describe('What they need help with, in one or two sentences, in English'),
      details: z.string().optional().describe('Any other useful details, in English'),
      timeline: z.string().optional().describe('Timeline or urgency, if given'),
      language: z.string().optional().describe('Language the visitor is writing in'),
      products: z.array(z.string()).optional().describe("Names of Siamak's catalog products they are interested in, if any"),
    }),
    execute: async ({ products, ...input }) => {
      if (!input.email && !input.phone) {
        return { saved: false, reason: 'Need an email or phone number first.' };
      }
      await saveLead({
        ...input,
        source: 'ai-advisor',
        page,
        transcript: messages,
        extra: products?.length ? { products: products.slice(0, 5).map((p) => String(p).slice(0, 80)) } : undefined,
      });
      leadSaved = true;
      return { saved: true };
    },
  });

  let requestReported = false;
  const report_unmet_request = tool({
    description:
      "Report a need that no product in Siamak's catalog covers, so Ryan can consider building it. Call once per unmet need. Contact details are not required.",
    inputSchema: z.object({
      need: z.string().describe('What the visitor needs that no catalog product covers, in one or two sentences, in English'),
      industry: z.string().optional().describe('Their industry or type of business, if known'),
      closest_product: z.string().optional().describe('The closest catalog product, if any partly fits'),
      language: z.string().optional().describe('Language the visitor is writing in'),
    }),
    execute: async (input) => {
      if (requestReported) return { reported: true, note: 'Already reported in this reply.' };
      const saved = await saveRequest({ ...input, page, transcript: messages });
      console.log('unmet product request saved:', saved.id);
      requestReported = true;
      return { reported: true };
    },
  });

  try {
    const result = await withModel((model) => generateText({
      model,
      system:
        SYSTEM_PROMPT +
        (language ? `\nThe visitor's browser language is ${language}; still match the language they write in.` : ''),
      messages,
      tools: { save_lead, report_unmet_request },
      stopWhen: isStepCount(4),
      maxOutputTokens: 1200,
    }));
    const reply = (result.text || '').trim() || (leadSaved ? 'Thanks, Ryan has your details and will be in touch.' : 'Could you tell me a bit more about what you need?');
    if (!requestReported && messages[messages.length - 1].content.length >= 15) {
      waitUntil(
        checkForGap(messages, reply)
          .then(async (gap) => {
            if (!gap?.unmet || !gap.need) return;
            const saved = await saveRequest({ ...gap, language, page, transcript: [...messages, { role: 'assistant', content: reply }] });
            console.log('unmet product request saved (backstop):', saved.id);
          })
          .catch((e) => console.error('gap check failed', e?.message)),
      );
    }
    return json({ reply, leadSaved, requestReported });
  } catch (err) {
    console.error('chat error', err?.message);
    return json(
      {
        reply:
          "Sorry, I'm having trouble right now. You can email Ryan directly at ryanjavaheri21@gmail.com and he'll get back to you.",
        error: true,
      },
      200,
    );
  }
}
