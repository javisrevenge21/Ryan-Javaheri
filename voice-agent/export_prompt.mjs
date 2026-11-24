// Copies the website advisor's knowledge (lib/profile.js, lib/catalog.js) into prompt.txt,
// so the voice agent says exactly what the chat advisor says.
// Run after changing lib/profile.js or lib/catalog.js:  node voice-agent/export_prompt.mjs
import { writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { SYSTEM_PROMPT } from '../lib/profile.js';

const out = fileURLToPath(new URL('./prompt.txt', import.meta.url));
writeFileSync(out, SYSTEM_PROMPT.trim() + '\n');
console.log(`wrote ${out} (${SYSTEM_PROMPT.length} chars)`);
