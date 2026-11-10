import portfolio
import me
from me import LINKEDIN
from pages import head, nav, tail, PERSON, SITE, EMAIL, faq_schema, faq_html

FAQ = [
    ("What is LLMO?",
     "LLMO (Large Language Model Optimization) is the work of making a business easy for AI assistants like ChatGPT, Claude, Gemini and Perplexity to understand, trust and recommend. It covers structured data, clear answer-style content, consistent business information across the web, and citations from trusted sources."),
    ("Why doesn't ChatGPT mention my business?",
     "Usually because AI models can't find clear, consistent, trustworthy information about you. If your website doesn't plainly say who you serve, where, and what you do, and other sites don't confirm it, models pick a competitor they understand better. The free scan shows where you stand."),
    ("What does an AI intake agent do?",
     "It answers visitors' questions 24/7 in their own language, then collects their name, contact details and what they need, and sends it to you. The advisor on this site is a live example: click the button at the bottom right and try it."),
    ("Who is Ryan Javaheri?",
     "Ryan Javaheri is a Los Angeles AI consultant and website builder. He studies public relations and business law at USC and works with Siamak Consulting, learning LLMO strategy from AI consultant Siamak Kalhor while building websites and AI agents for clients."),
    ("Do you work with law firms?",
     "Yes. Law firms are a main focus: AI visibility so firms show up in AI answers, intake agents that pre-qualify inquiries, and support with lateral recruiting, market intelligence and PR."),
    ("How much does a project cost?",
     "Every project is quoted after a short call, based on scope. Tell my AI advisor or the contact form what you need and I'll send a clear quote."),
    ("Can the AI agent answer phone calls too?",
     "Yes. The same intake agent can be connected to a phone number so it answers calls, takes messages and books follow-ups. The web version on this site also supports voice: press Talk in the advisor."),
]

ANSWER = ("<b>Ryan Javaheri</b> is a Los Angeles AI consultant who builds <b>AI-ready websites</b> and "
          "<b>24/7 AI intake agents</b> that answer questions and capture leads. He works with Siamak Consulting on "
          "LLMO, so firms show up when clients ask AI for a recommendation, and he brings a USC background in "
          "public relations and business law.")


def build():
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            PERSON,
            {
                "@type": "ProfessionalService",
                "@id": SITE + "/#service",
                "name": "Ryan Javaheri, AI Consulting & Websites",
                "url": SITE + "/",
                "image": SITE + "/og-image.png",
                "email": EMAIL,
                "founder": {"@id": SITE + "/#ryan"},
                "areaServed": ["Los Angeles", "California", "United States", "Worldwide"],
                "address": {"@type": "PostalAddress", "addressLocality": "Los Angeles", "addressRegion": "CA", "addressCountry": "US"},
                "knowsLanguage": ["en", "es", "fa", "he", "ar", "zh", "ko", "ja", "fr", "pt", "ru", "hy", "hi"],
                "hasOfferCatalog": {
                    "@type": "OfferCatalog",
                    "name": "Services",
                    "itemListElement": [
                        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "url": SITE + u}}
                        for n, u in [
                            ("AI Visibility / LLMO", "/ai-visibility/"),
                            ("AI Intake Agents", "/ai-agents/"),
                            ("AI-Ready Websites", "/websites/"),
                            ("Law Firm AI, Recruiting and PR", "/law-firms/"),
                        ]
                    ],
                },
            },
            {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Ryan Javaheri", "publisher": {"@id": SITE + "/#ryan"}, "inLanguage": ["en", "es", "fa", "he", "ar", "zh-Hans", "ko", "ja", "fr", "pt", "ru", "hy", "hi"]},
            faq_schema(FAQ),
        ],
    }
    html = head(
        "Ryan Javaheri — AI Consultant, AI Agents & AI-Ready Websites | Los Angeles",
        "Los Angeles AI consultant building AI-ready websites, 24/7 AI intake agents and AI visibility (LLMO) so ChatGPT, Gemini and Perplexity recommend you. Free AI scan.",
        "/",
        schema=schema,
    )
    html += nav("en")
    SITES = portfolio.site_count()
    html += f"""
<main id="main">
<div class="intro-wrap">
<div class="orb orb-1" data-speed="0.25"></div>
<div class="orb orb-2" data-speed="0.45"></div>
<header class="intro">
<div class="intro-content" id="heroContent">
<h1 data-split>Ryan Javaheri</h1>
<p class="intro-sub">future lawyer.</p>
<a class="intro-cta" href="#contact">Get in touch</a>
</div>
<div class="scroll-cue" id="scrollCue" aria-hidden="true"></div>
</header>
</div>

<div class="hero-wrap" data-play>
<section class="hero" aria-label="AI consulting">
<div class="hero-content">
<span class="kicker"><i></i>AI advisor online 24/7, in any language</span>
<h2 class="h1" data-split>Be the name<br><span class="grad">AI recommends.</span></h2>
<p class="sub">I build AI-ready websites, AI intake agents and AI visibility strategy, so when customers ask ChatGPT, Gemini or Perplexity who to hire, the answer is you.</p>
<p class="who">Ryan Javaheri · USC Annenberg ’27 · PR &amp; Pre-Law · AI &amp; web development · English &amp; Farsi</p>
<div class="ctas">
<a class="btn btn-dark" href="#scan">Run your free AI scan</a>
<a class="btn btn-light" href="#" data-open-agent="">Talk to my AI advisor →</a>
</div>
<div class="stats">
<div><b>{SITES}</b><span>sites built</span></div>
<div><b>24/7</b><span>AI intake</span></div>
<div><b>13</b><span>languages</span></div>
<div><b>USC ’27</b><span>PR &amp; Pre-Law</span></div>
</div>
</div>
<div class="answer" aria-label="Illustrative AI answer">
<div class="answer-bar"><i></i><i></i><i></i><span>ai-answer.engine</span><em>EXAMPLE</em></div>
<div class="answer-q">Who can build an AI intake agent and website for my law firm in LA?</div>
<div class="answer-a"><span class="av" aria-hidden="true"></span><p id="aiAnswer" data-text="{ANSWER.replace('"', '&quot;')}"></p></div>
<div class="answer-src" id="aiSources" style="opacity:0;transition:opacity .6s"><span>ryanjavaheri.com</span><span>schema.org/Person</span><span>llms.txt</span></div>
<div class="answer-foot"><span>Illustrative answer: this is the goal for every client.</span><a href="#scan">Check yours →</a></div>
</div>
</section>
</div>

<div class="ticker" aria-hidden="true"><div class="ticker-track">
{''.join(f'<span>{t}</span>' for t in ['LLM Optimization','Generative Engine Optimization','Answer Engine Optimization','AI Intake Agents','Voice AI','Structured Data','llms.txt','AI-Ready Websites','AI Automation','Law Firm Marketing','Legal Recruiting','Public Relations','The B.U.I.L.D. Method']*2)}
</div></div>

<section class="block dark reveal" id="how">
<div class="inner">
<p class="eyebrow">How it works</p>
<h2>Search used to rank links.<br>AI just gives one answer.</h2>
<p class="lede">Your customers now ask an assistant "who should I hire?" and get a short answer naming a few businesses. Models name the ones they can understand, verify and trust. Everything I build is aimed at making that business you.</p>
<div class="how">
<div class="diagram" aria-hidden="true">
<svg viewBox="0 0 100 100"><defs><linearGradient id="lg" x1="0" x2="1"><stop offset="0" stop-color="#5b5bf7"/><stop offset="1" stop-color="#2dd4ff"/></linearGradient></defs>
<path d="M18 16 Q35 35 50 50"/><path d="M82 16 Q65 35 50 50"/><path d="M18 84 Q35 65 50 50"/><path d="M82 84 Q65 65 50 50"/></svg>
<span class="node" style="left:18%;top:16%">ChatGPT</span><span class="node" style="left:82%;top:16%">Claude</span>
<span class="node" style="left:18%;top:84%">Gemini</span><span class="node" style="left:82%;top:84%">Perplexity</span>
<span class="node you" style="left:50%;top:50%">Your brand</span>
</div>
<ul class="signals">
<li><b>Retrieval, not ranking</b>AI pulls a few sources it can read cleanly. Clear pages, schema and llms.txt get you into that set.</li>
<li><b>Engineered trust</b>Consistent name, services and location everywhere, plus citations and reviews, so models can verify you.</li>
<li><b>Compounding authority</b>Every answer-ready page and mention adds up. Early movers become the default answer.</li>
</ul>
</div>
<div class="qa"><h3>Why doesn't ChatGPT mention my business?</h3><p>Usually it can't find clear, consistent, trustworthy information about you. If your site doesn't plainly say who you serve, where, and what you do, and other sites don't confirm it, the model names a competitor it understands better. The fix is structural, and it's what I do.</p></div>
</div>
</section>

<section class="block alt" id="services">
<div class="inner">
<div class="reveal"><p class="eyebrow">Services</p>
<h2>What I build for you.</h2>
<p class="lede">Strategy and the hands-on build, from one person who does both.</p></div>
<div class="cards stagger">
<a class="card" href="/ai-visibility/"><div class="icon">✦</div><h3>AI Visibility (LLMO)</h3><p>Become the business ChatGPT, Gemini and Perplexity recommend.</p><ul><li>AI visibility audit</li><li>Schema &amp; llms.txt</li><li>Answer-ready content</li></ul><span class="more">Learn more ›</span></a>
<a class="card" href="/ai-agents/"><div class="icon">◉</div><h3>AI Intake Agents</h3><p>Chat and voice agents that answer 24/7 and hand you qualified leads.</p><ul><li>Website chat + voice</li><li>Phone-line agents</li><li>Any language</li></ul><span class="more">Learn more ›</span></a>
<a class="card" href="/websites/"><div class="icon">▲</div><h3>AI-Ready Websites</h3><p>Fast, modern sites built so people convert and AI models understand.</p><ul><li>Design &amp; build</li><li>SEO + AI structure</li><li>Lead capture built in</li></ul><span class="more">Learn more ›</span></a>
<a class="card" href="/ai-agents/#automation"><div class="icon">⚙</div><h3>AI Automation</h3><p>Leads, follow-ups, emails and calendars connected so nothing slips.</p><ul><li>Lead routing</li><li>Auto follow-up</li><li>CRM hookups</li></ul><span class="more">Learn more ›</span></a>
<a class="card" href="/law-firms/"><div class="icon">§</div><h3>Law Firm Growth</h3><p>AI visibility and intake for firms, plus recruiting and market intel.</p><ul><li>Lateral recruiting support</li><li>Market intelligence</li><li>Retention strategy</li></ul><span class="more">Learn more ›</span></a>
<a class="card" href="/law-firms/#pr"><div class="icon">❝</div><h3>PR &amp; Reputation</h3><p>Messaging and media relations that make the right people trust you.</p><ul><li>Positioning</li><li>Media relations</li><li>Reputation repair</li></ul><span class="more">Learn more ›</span></a>
</div>
</div>
</section>

<section class="block reveal" id="law">
<div class="inner">
<p class="eyebrow">For law firms</p>
<h2>What I can do for your firm.</h2>
<ul class="plus" id="scrubList">
<li>Get your firm named when clients ask AI who to hire</li>
<li>Answer and pre-qualify inquiries 24/7 with an AI intake agent</li>
<li>Support lateral attorney recruitment and connect you with top legal talent</li>
<li>Provide market intelligence on firm culture, compensation and growth</li>
<li>Position and market your firm to attract the right candidates and clients</li>
<li>Cultivate early talent and relationships with promising law students</li>
</ul>
</div>
</section>

<section class="block alt" id="industries">
<div class="inner">
<div class="reveal"><p class="eyebrow">Industries</p><h2>Who I work with.</h2></div>
<div class="cards stagger">
<a class="card" href="/law-firms/"><h3>Law firms</h3><p>Show up in AI answers for your practice area and city, and never miss an after-hours inquiry.</p></a>
<div class="card"><h3>Small business &amp; retail</h3><p>From fabric stores to local shops: a site that sells, listings AI trusts, and an assistant that answers customers.</p></div>
<div class="card"><h3>Professional practices</h3><p>Dental, medical, financial and real estate offices that win on trust and need clean intake.</p></div>
<div class="card"><h3>Personal brands</h3><p>Founders, creators and professionals who want AI to describe them accurately and well.</p></div>
</div>
</div>
</section>

<section class="block reveal" id="method">
<div class="inner">
<p class="eyebrow">The method</p>
<h2>B.U.I.L.D.</h2>
<p class="lede">Five steps every project follows, from finding out what AI says about you today to making you the default answer.</p>
<div class="steps stagger">
<div class="step"><span class="L">B</span><h3>Baseline</h3><p>Scan what ChatGPT, Gemini, Perplexity and search say about you now.</p></div>
<div class="step"><span class="L">U</span><h3>Understand</h3><p>Map the real questions your customers ask AI before they hire.</p></div>
<div class="step"><span class="L">I</span><h3>Implement</h3><p>Website, schema, answer-ready pages, listings and llms.txt.</p></div>
<div class="step"><span class="L">L</span><h3>Launch agents</h3><p>AI intake on web and phone that answers and captures leads.</p></div>
<div class="step"><span class="L">D</span><h3>Develop</h3><p>Re-check AI answers monthly and keep compounding authority.</p></div>
</div>
<div class="qa"><h3>What does an AI consultant actually do?</h3><p>An AI consultant finds where AI can grow a business and then makes it happen: getting the business recommended in AI answers, adding agents that handle intake and questions, and automating repetitive work. I do the strategy and the build myself.</p></div>
</div>
</section>

<section class="block alt reveal" id="about">
<div class="inner">
<p class="eyebrow">About</p>
<h2>Hi, I'm Ryan.</h2>
<div class="mentor">
<div class="mono" aria-hidden="true">RJ</div>
<div>
<blockquote>I enjoy turning a concept into something valuable that people actually use, whether that's a website, a video, or a store's online sales.</blockquote>
<p class="lede">I'm a PR major at USC Annenberg (Class of 2027) on the pre-law path. For over two years I worked in sales, retail and marketing at Payman Fabric and Spandex Palace in Los Angeles, selling in-store and online through Shopify, so I know how a small business runs from the inside and how much it matters to really listen to a customer.</p>
<p class="lede">I've been creating content since 2021, building audiences and systems for steady production. I build websites with HTML, CSS and JavaScript, and I now create and promote AI products. I'm learning LLMO and AI strategy directly from <a href="https://siamakconsulting.com/" target="_blank" rel="noopener">Siamak Kalhor</a> at Siamak Consulting. I'm fluent in English and Farsi.</p>
<p class="lede">Open to internships and roles in law, PR, marketing and tech.</p>
<div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:8px">
<a class="btn btn-light" href="#" data-open-agent="Tell me about Ryan's background">Ask my AI about me</a>
<a class="btn btn-light" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn ›</a>
</div>
</div>
</div>
</div>
</section>



<section class="block alt reveal" id="work">
<div class="inner" id="portfolio">
<p class="eyebrow">Portfolio</p>
<h2>Websites I have built.</h2>
<p>Every site and AI project I have built, in one place.</p>
<div class="cards stagger">
<!-- PORTFOLIO: generated from tools/portfolio.py. Add new projects there, newest first. -->
{portfolio.cards(portfolio.home_items())}
</div>
<a class="btn btn-light" href="/portfolio/" style="margin-top:30px">Full portfolio ›</a>
</div>
</section>

<section class="block reveal" id="insights">
<div class="inner">
<p class="eyebrow">Insights</p>
<h2>Notes on AI visibility.</h2>
<div class="cards stagger">
<a class="card post-card" href="/insights/what-is-llmo/"><div class="cover" data-k="LLMO"></div><span class="date">Guide</span><h3>What is LLMO, and why it matters now</h3><p>How AI assistants decide which businesses to name, and what you can do about it.</p></a>
<a class="card post-card" href="/insights/why-chatgpt-doesnt-mention-your-business/"><div class="cover v2" data-k="Why not me?"></div><span class="date">Diagnosis</span><h3>Why ChatGPT doesn't mention your business</h3><p>The five most common reasons, and the fix for each.</p></a>
<a class="card post-card" href="/insights/ai-intake-agents-for-law-firms/"><div class="cover v3" data-k="24/7 intake"></div><span class="date">Law firms</span><h3>AI intake agents for law firms</h3><p>Answer every inquiry, even at 2 a.m., without giving legal advice.</p></a>
</div>
<a class="btn btn-light" href="/insights/" style="margin-top:30px">All insights ›</a> <a class="btn btn-light" href="/glossary/" style="margin-top:30px">Glossary ›</a>
</div>
</section>

<section class="block dark" id="scan">
<div class="inner scan-grid">
<div class="reveal">
<p class="eyebrow">Free AI visibility scan</p>
<h2>See what AI says about you.</h2>
<p class="lede">Two minutes. You get a visibility score, what an AI model says about you today, the questions your customers ask, and quick wins. Leave your email and I'll follow up with a full audit across ChatGPT, Claude, Gemini and Perplexity.</p>
<ol class="scan-list"><li>Run the scan</li><li>Get your score and quick wins</li><li>Optional: a full audit and 30-minute call with me</li></ol>
</div>
<div class="formcard reveal">
<form id="scanForm">
<div class="fgrid">
<div class="full"><label class="f" for="s-b">Business name *</label><input class="f-in" id="s-b" name="business" required maxlength="120"></div>
<div><label class="f" for="s-w">Website</label><input class="f-in" id="s-w" name="website" placeholder="yourbusiness.com" maxlength="200"></div>
<div><label class="f" for="s-c">City / area</label><input class="f-in" id="s-c" name="city" placeholder="Los Angeles" maxlength="80"></div>
<div class="full"><label class="f" for="s-k">Type of business</label><input class="f-in" id="s-k" name="category" placeholder="e.g. personal injury law firm" maxlength="80"></div>
<div><label class="f" for="s-n">Your name</label><input class="f-in" id="s-n" name="name" maxlength="120"></div>
<div><label class="f" for="s-e">Email (for the full audit)</label><input class="f-in" id="s-e" name="email" type="email" maxlength="200"></div>
</div>
<div class="hp" aria-hidden="true"><input name="company_url_hp" tabindex="-1" autocomplete="off"></div>
<button class="btn btn-light" type="submit" style="margin-top:18px;width:100%">Run my free scan</button>
<p class="f-msg"></p>
<p class="f-note">Free. An AI model writes the result, so treat it as an estimate. Your details only go to Ryan. By running the scan you agree to the <a href="/terms/" style="color:#a1a1a6">Terms</a> and <a href="/privacy/" style="color:#a1a1a6">Privacy Policy</a>.</p>
</form>
<div class="result" id="scanResult" aria-live="polite"></div>
</div>
</div>
</section>

<section class="block reveal" id="faq">
<div class="inner">
<p class="eyebrow">FAQ</p>
<h2>Quick answers.</h2>
<div class="faq">{faq_html(FAQ)}</div>
</div>
</section>

<section class="block reveal" id="contact">
<div class="inner scan-grid">
<div>
<p class="eyebrow">Contact</p>
<h2>Let's build something.</h2>
<p class="lede">Tell me about your business and what you want AI to say about you. I read every message and reply personally.</p>
<p class="lede">Prefer to talk? <a href="#" data-open-agent="">My AI advisor</a> answers right now, by text or voice, or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div>
<div class="formcard">
<form data-lead data-ok="Thanks! I'll reach out personally, usually within a day.">
<div class="fgrid">
<div><label class="f" for="c-n">Name *</label><input class="f-in" id="c-n" name="name" required maxlength="120"></div>
<div><label class="f" for="c-e">Email *</label><input class="f-in" id="c-e" name="email" type="email" required maxlength="200"></div>
<div><label class="f" for="c-c">Company</label><input class="f-in" id="c-c" name="company" maxlength="200"></div>
<div><label class="f" for="c-p">Phone</label><input class="f-in" id="c-p" name="phone" type="tel" maxlength="60"></div>
<div class="full"><label class="f" for="c-m">What do you need? *</label><textarea class="f-in" id="c-m" name="need" required maxlength="2000" placeholder="AI visibility, a website, an AI agent, recruiting support…"></textarea></div>
</div>
<div class="hp" aria-hidden="true"><input name="company_url_hp" tabindex="-1" autocomplete="off"></div>
<button class="btn btn-dark" type="submit" style="margin-top:18px">Send to Ryan</button>
<p class="f-msg" aria-live="polite"></p>
</form>
</div>
</div>
</section>
</main>
"""
    html += tail("en")
    return html
