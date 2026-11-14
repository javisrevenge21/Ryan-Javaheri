import { track } from '@vercel/analytics/server';

// Counts a business event (a scan, a call request) in Vercel Web Analytics.
// Runs on the server, so it counts every scan and call request, whatever the
// visitor chose in the cookie banner. It sends no name, email or other details.
// Pinned to @vercel/analytics 1.6.1: that version posts the event to the site
// the visitor is on (www.ryanjavaheri.com). Version 2 posts to the deployment's
// vercel.app address, which is behind Vercel login on this project.
// Never lets a counting problem break the form.
export async function countEvent(name, props, request) {
  try {
    await track(name, props, { request });
  } catch (e) {
    console.error('analytics event failed', e?.message);
  }
}
