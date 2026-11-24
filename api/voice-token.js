import { AccessToken, RoomConfiguration, RoomAgentDispatch } from 'livekit-server-sdk';
import { randomUUID } from 'node:crypto';
import { json } from '../lib/leads.js';

// Starts a voice call with Ryan's advisor (the LiveKit agent in /voice-agent).
// Returns a short-lived token for one fresh room; LiveKit dispatches the agent into it.
// Until LIVEKIT_URL, LIVEKIT_API_KEY and LIVEKIT_API_SECRET are set in Vercel this returns 503,
// and the site falls back to the browser's own voice.
export async function POST(request) {
  const url = process.env.LIVEKIT_URL;
  const key = process.env.LIVEKIT_API_KEY;
  const secret = process.env.LIVEKIT_API_SECRET;
  if (!url || !key || !secret) return json({ ok: false, error: 'voice-not-configured' }, 503);

  let b = {};
  try { b = await request.json(); } catch {}
  const page = typeof b.page === 'string' ? b.page.slice(0, 300) : '';

  const room = `web-${randomUUID()}`;
  const at = new AccessToken(key, secret, {
    identity: `visitor-${randomUUID().slice(0, 8)}`,
    name: 'Website visitor',
    ttl: '15m',
    metadata: JSON.stringify({ page }),
  });
  at.addGrant({ room, roomJoin: true, canPublish: true, canSubscribe: true, canPublishData: true });
  at.roomConfig = new RoomConfiguration({
    agents: [new RoomAgentDispatch({ agentName: 'ryan-advisor' })],
  });
  return json({ ok: true, url, room, token: await at.toJwt() });
}
