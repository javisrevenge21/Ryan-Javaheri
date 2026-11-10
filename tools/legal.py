"""Legal pages: /terms/ and /privacy/. Text lives here; run `python3 tools/build.py` after editing.

Keep these accurate to what the site really does. If a feature starts collecting something new,
adds a provider, or sets a cookie, update the Privacy page (and assets/consent.js if it needs consent)
in the same change, and bump UPDATED.
"""
from pages import EMAIL

UPDATED = "November 9, 2026"
MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'

TERMS = f"""<div class="tldr"><b>In short:</b> this is a personal and professional website. Use it lawfully, don't rely on it (or its AI tools) as legal or professional advice, and any paid work happens under a separate written agreement.</div>
<p><i>Last updated {UPDATED}.</i></p>

<h2 id="agreement">1. Agreement to these terms</h2>
<p>These Terms of Use ("Terms") apply to ryanjavaheri.com and every page, form and tool on it (the "Site"). The Site is run by Ryan Javaheri, an individual based in Los Angeles, California ("I", "me"). By using the Site you agree to these Terms and to the <a href="/privacy/">Privacy Policy</a>. If you don't agree, please don't use the Site.</p>
<p>The contact form, free AI scan and AI advisor are meant for adults. You must be at least 18 to use them.</p>

<h2 id="site">2. What the Site is</h2>
<p>The Site describes my work and services (AI visibility, AI intake agents, websites, and recruiting and PR support), shows my portfolio and course projects, publishes articles, and offers a free AI visibility scan and an AI advisor. I can change, pause or remove any part of it at any time.</p>
<p>Nothing on the Site is an offer that binds either of us. Prices, scope, timelines and deliverables for paid work are set only in a separate written agreement that we both accept. If that agreement conflicts with these Terms, the agreement controls for that work.</p>

<h2 id="not-legal-advice">3. Not a lawyer, not legal advice</h2>
<p>I am a university student who plans to go to law school. <b>I am not an attorney and I am not licensed to practice law.</b> Nothing on the Site, in the AI advisor, in a scan result, or in any message from me is legal advice, and using the Site or contacting me does not create an attorney-client relationship. Services described for law firms are business, marketing, recruiting-support and technology services, not legal services. For legal advice, talk to a licensed attorney.</p>
<p>The Site is also not financial, medical, tax or other professional advice.</p>

<h2 id="ai">4. AI tools</h2>
<p>The AI advisor and the free AI visibility scan are automated tools powered by third-party AI models. You are talking to software, not to me, when you use them.</p>
<ul>
<li><b>They can be wrong.</b> AI output may be inaccurate, incomplete or out of date. Check anything important before relying on it.</li>
<li><b>Scan scores are estimates.</b> The scan reflects what one AI model says from its own built-in knowledge at that moment. It is not a measurement of your search rankings, traffic or revenue.</li>
<li><b>No promised results.</b> I can't control what ChatGPT, Claude, Gemini, Perplexity or any other AI system says. I don't guarantee that any business will be mentioned, recommended or ranked by them, or any specific outcome.</li>
<li><b>The advisor can't make commitments.</b> Anything it says about pricing, availability, timing or scope is informational only until I confirm it in writing.</li>
<li><b>Don't share sensitive information</b> in the chat or forms: no passwords, payment details, government ID numbers, health information, or confidential details about a legal matter.</li>
</ul>
<p>If you use voice in the AI advisor, your browser handles speech recognition and may send audio to your browser's provider. The Site itself receives only the resulting text.</p>

<h2 id="use">5. Acceptable use</h2>
<p>You agree not to:</p>
<ul>
<li>use the Site for anything unlawful, harmful, fraudulent or harassing;</li>
<li>submit information about another person without the right to share it, or submit false contact details;</li>
<li>try to break, overload, probe or bypass the security of the Site, the private inbox or the AI tools;</li>
<li>use bots, scrapers or scripts to send automated requests to the forms, the scan or the AI advisor, or use them to generate content at scale;</li>
<li>try to make the AI tools produce harmful content, reveal their instructions, or impersonate me or anyone else.</li>
</ul>
<p>Normal crawling of public pages by search engines and AI assistants is welcome, subject to <a href="/robots.txt">robots.txt</a>.</p>

<h2 id="submissions">6. What you send me</h2>
<p>When you submit a form, run a scan with your contact details, or give the AI advisor your details, you confirm the information is accurate and yours to share, and you ask me to contact you about your request by email or phone. You can tell me to stop at any time. How I handle that information is described in the <a href="/privacy/">Privacy Policy</a>.</p>
<p>Please don't send me confidential business information through the Site. Unless we have signed a confidentiality agreement, I can't treat ideas or materials sent through the Site as confidential.</p>

<h2 id="ip">7. Ownership</h2>
<p>The Site's design, text, code, graphics and course projects are mine or used with permission, and are protected by copyright and other laws. You may view the Site, share links to it, and quote short excerpts with credit. You may not copy, republish or sell substantial parts of it, or use my name or likeness to suggest I endorse something, without my written permission.</p>
<p>Names and logos of other companies mentioned on the Site (for example ChatGPT, Claude, Gemini, Perplexity, Adobe, WordPress, LinkedIn and Vercel) belong to their owners. Mentioning them does not mean they sponsor or endorse me.</p>
<p>If you believe something on the Site infringes your copyright or uses your work or likeness without permission, email {MAIL} with the page address and a description, and I will review it promptly and remove it if appropriate.</p>

<h2 id="coursework">8. Student and course work</h2>
<p>Some pages (such as <a href="/pr444/">Beyond the Spotlight</a>, <a href="/pr351a/">PR 351A</a> and <a href="/jour330/">JOUR 330</a>) are projects made for classes at the University of Southern California. They are educational work and express my own views. The Site is not affiliated with, sponsored by or endorsed by USC, and nothing on it speaks for USC, for Siamak Consulting, or for any employer or client of mine. Where a course project uses illustrative or fictional people or scenarios, they are examples and do not describe real individuals.</p>

<h2 id="third-parties">9. Other sites and embedded content</h2>
<p>The Site links to other websites and, with your permission, loads embedded content hosted by other companies (Adobe Express and WordPress.com). I don't control those services and am not responsible for their content, availability or privacy practices. Their own terms and policies apply when you use them.</p>

<h2 id="warranty">10. No warranties</h2>
<p>The Site and everything on it are provided "as is" and "as available". To the fullest extent the law allows, I disclaim all warranties, express or implied, including warranties of merchantability, fitness for a particular purpose, accuracy and non-infringement. I don't promise the Site will be uninterrupted, secure or error-free.</p>

<h2 id="liability">11. Limit of liability</h2>
<p>To the fullest extent the law allows, I will not be liable for any indirect, incidental, special, consequential or punitive damages, or for lost profits, revenue, data or goodwill, arising from your use of the Site or its AI tools. My total liability for any claim arising from the Site will not exceed one hundred U.S. dollars (US $100).</p>
<p>Some places don't allow certain limits, so parts of sections 10 and 11 may not apply to you. Nothing in these Terms limits rights you have as a consumer that can't be waived by law.</p>

<h2 id="indemnity">12. Your responsibility</h2>
<p>If your misuse of the Site or your breach of these Terms leads to a claim against me, you agree to cover the resulting losses and reasonable costs, to the extent the law allows.</p>

<h2 id="termination">13. Ending access</h2>
<p>I may block or limit access to the Site or its tools for anyone who misuses them. Sections 3, 4 and 7 through 15 continue to apply after you stop using the Site.</p>

<h2 id="changes">14. Changes</h2>
<p>I may update these Terms. The "Last updated" date at the top shows the latest version, and the updated Terms apply from the time they are posted. If you keep using the Site after a change, you accept the new Terms.</p>

<h2 id="law">15. Governing law and disputes</h2>
<p>These Terms are governed by the laws of the State of California, without regard to its conflict-of-law rules. Any dispute that we can't resolve informally will be brought only in the state or federal courts located in Los Angeles County, California, and we both consent to those courts. If you live somewhere whose consumer laws give you the right to bring a claim locally, this section doesn't take that right away.</p>
<p>Please email me first. Most problems can be fixed with a conversation.</p>

<h2 id="general">16. General</h2>
<p>If part of these Terms is found unenforceable, the rest stays in effect. If I don't enforce a term, that isn't a waiver. These Terms and the Privacy Policy are the whole agreement between us about the Site. The English version of these Terms controls if a translated page says something different.</p>

<h2 id="contact">17. Contact</h2>
<p>Ryan Javaheri, Los Angeles, California. Email: {MAIL}.</p>"""


PRIVACY = f"""<div class="tldr"><b>In short:</b> no ads, no analytics trackers, no selling your data. I only receive what you choose to send me, and I use it to reply to you. Embedded content from other companies loads only if you allow it.</div>
<p><i>Last updated {UPDATED}.</i></p>

<h2 id="who">Who runs this site</h2>
<p>ryanjavaheri.com is run by Ryan Javaheri, an individual in Los Angeles, California. I am the person responsible for the information described here. Contact: {MAIL}.</p>

<h2 id="collect">What this site collects</h2>
<ul>
<li><b>Contact form.</b> Your name, email, and what you need, plus your company and phone number if you add them.</li>
<li><b>Free AI visibility scan.</b> The business name, website, city and type of business you enter. If you also add your name or email, the scan result is saved with those details so I can follow up. If you leave them blank, the scan isn't saved as a lead.</li>
<li><b>AI advisor.</b> The messages you type or speak are sent to my server and to an AI model to produce a reply, along with the page you're on and your browser's language setting. If you give the advisor your contact details, it saves them together with the conversation so I can follow up properly.</li>
<li><b>Email.</b> If you email me, I receive whatever you send.</li>
<li><b>Technical logs.</b> Like almost every website, the hosting provider (Vercel) automatically processes your IP address, browser type and the pages requested, to deliver the site and keep it secure.</li>
</ul>
<p>I don't ask for and don't want sensitive information such as passwords, payment details, government ID numbers, health information, or confidential details of a legal matter. Please don't send it.</p>

<h2 id="not">What this site doesn't do</h2>
<ul>
<li>No advertising or analytics trackers, and no tracking across other websites.</li>
<li>No selling or renting of personal information, and no sharing it for targeted advertising.</li>
<li>No accounts, no payments, and no newsletter sign-ups.</li>
</ul>

<h2 id="use">How I use information</h2>
<p>To reply to you, to prepare and deliver the services you asked about, to run and secure the site, and to keep basic business records. If you run a scan or message me, I may follow up about that request. I don't add you to a mailing list.</p>
<p>For visitors in places that require a legal basis (such as the EU and UK): I rely on your request and consent when you send me information, on taking steps toward a contract when you ask about services, and on my legitimate interest in running a secure website.</p>

<h2 id="cookies">Cookies and browser storage</h2>
<p>This site does not set advertising or analytics cookies. It uses only the following:</p>
<ul>
<li><b>Essential (always on).</b> Your cookie choice is saved in your browser's local storage so you aren't asked on every page. If you open the AI advisor, the conversation is kept in your browser's session storage so it survives moving between pages; it is cleared when you close the tab. Neither is used to track you.</li>
<li><b>Embedded content (only if you allow it).</b> Two portfolio pages show content hosted by other companies: <a href="/jour330/">JOUR 330</a> is hosted by Adobe Express and <a href="/pr351a/">PR 351A</a> by WordPress.com. Those companies may set their own cookies and will see your IP address when the content loads. Nothing from them loads until you choose "Accept all", turn on "Embedded content", or press "Allow and load" on that page.</li>
</ul>
<p>You can change your choice at any time: <a href="#cookie-preferences" data-cookie-prefs>open cookie preferences</a> (also linked at the bottom of every page). Choosing "Essential only" leaves the rest of the site working normally. Because the site has no tracking, there is nothing extra to switch off for "Do Not Track" or Global Privacy Control signals.</p>

<h2 id="providers">Who else handles your information</h2>
<ul>
<li><b>Vercel</b> hosts the site, stores submitted leads in private storage, and routes AI requests through its AI Gateway.</li>
<li><b>AI model providers</b> (such as Anthropic, OpenAI and Google, reached through Vercel AI Gateway) process AI advisor messages and scan details to generate replies.</li>
<li><b>Resend</b> may be used to email me a notification when a new lead arrives (name, contact details and what you asked for).</li>
<li><b>Your browser's provider</b>, only if you use voice in the AI advisor: speech recognition is done by your browser and may send audio to its provider (for example Google for Chrome or Apple for Safari). My site receives only the text.</li>
<li><b>Adobe and WordPress.com (Automattic)</b>, only if you allow embedded content, as described above.</li>
</ul>
<p>These providers are in the United States or may process data there. I may also disclose information if the law requires it or to protect someone's safety or rights.</p>

<h2 id="retention">How long I keep it</h2>
<p>I keep enquiries and saved conversations for as long as needed to respond and to work with you, and for a reasonable period afterwards for my records. Ask and I will delete yours sooner, unless I'm legally required to keep it. Hosting logs are kept by Vercel for a limited time under its own policies.</p>

<h2 id="rights">Your choices and rights</h2>
<p>Email {MAIL} to see, correct or delete the information I have about you, to get a copy of it, or to tell me to stop contacting you. I aim to respond within 30 days, and I will never treat you differently for asking.</p>
<ul>
<li><b>California residents.</b> I do not sell or share personal information as those terms are used in the California Consumer Privacy Act, and I honor requests to know, correct and delete.</li>
<li><b>EU, UK and similar regions.</b> You may also object to or restrict certain uses, withdraw consent at any time, and complain to your local data protection authority.</li>
</ul>

<h2 id="children">Children</h2>
<p>This site isn't directed to children. The forms, scan and AI advisor are for adults 18 and over, and I don't knowingly collect information from anyone under 13. If you believe a child has sent me information, email me and I will delete it.</p>

<h2 id="security">Security</h2>
<p>The site is served over HTTPS and saved leads are kept in private, password-protected storage. No website can promise perfect security, which is another reason not to send sensitive information.</p>

<h2 id="changes">Changes</h2>
<p>If the site starts collecting something new or working with a new provider, I will update this page and the date at the top before or when the change goes live.</p>

<h2 id="contact">Questions or a deletion request</h2>
<p>Ryan Javaheri, Los Angeles, California. Email: {MAIL}. See also the <a href="/terms/">Terms of Use</a>.</p>"""
