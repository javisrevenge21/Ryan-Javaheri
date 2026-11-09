import { generateText, tool, isStepCount } from 'ai';
import { z } from 'zod';
import { SYSTEM_PROMPT } from '../lib/profile.js';
import { saveLead, json } from '../lib/leads.js';

const MODEL = process.env.AI_GATEWAY_MODEL || 'anthropic/claude-haiku-5.5';

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
    }),
    execute: async (input) => {
      if (!input.email && !input.phone) {
        return { saved: false, reason: 'Need an email or phone number first.' };
      }
      await saveLead({ ...input, source: 'ai-advisor', page, transcript: messages });
      leadSaved = true;
      return { saved: true };
    },
  });

  try {
    const result = await generateText({
      model: MODEL,
      system:
        SYSTEM_PROMPT +
        (language ? `\nThe visitor's browser language is ${language}; still match the language they write in.` : ''),
      messages,
      tools: { save_lead },
      stopWhen: isStepCount(3),
      maxOutputTokens: 400,
    });
    const reply = (result.text || '').trim() || 'Thanks, Ryan has your details and will be in touch.';
    return json({ reply, leadSaved });
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
