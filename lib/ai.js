// Try models in order. Free-tier AI Gateway accounts can't use every model, so if one is
// refused we move to the next. Set AI_GATEWAY_MODEL in Vercel to force a specific model.
const DEFAULTS = [
  'anthropic/claude-haiku-5.5',
  'anthropic/claude-haiku-4.5',
  'openai/gpt-5-mini',
  'google/gemini-2.5-flash',
  'openai/gpt-4.1-mini',
  'google/gemini-2.5-flash-lite',
  'meta/llama-3.3-70b',
];

const accessError = (e) =>
  /free tier|do not have access|not available|not found|unsupported|permission|forbidden|403|404/i.test(
    `${e?.message || ''} ${e?.statusCode || ''}`,
  );

let lastGood = null; // remembered per warm instance

export async function withModel(run) {
  const list = [...new Set([process.env.AI_GATEWAY_MODEL, lastGood, ...DEFAULTS].filter(Boolean))];
  let err;
  for (const model of list) {
    try {
      const out = await run(model);
      if (lastGood !== model) console.log('ai model in use:', model);
      lastGood = model;
      return out;
    } catch (e) {
      err = e;
      if (!accessError(e)) throw e;
      console.warn('model refused, trying next:', model, '-', e?.message?.slice(0, 120));
    }
  }
  throw err;
}
