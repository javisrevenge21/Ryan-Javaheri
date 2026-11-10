from pages import head, nav, tail, PERSON, SITE, EMAIL, faq_schema, faq_html, breadcrumb, cta_band


def page(path, title, desc, h1, intro, body, crumbs, faqs=None, article=None, cta=True):
    graph = [PERSON, breadcrumb(crumbs)]
    if faqs:
        graph.append(faq_schema(faqs))
    if article:
        graph.append({
            "@type": "Article",
            "headline": h1,
            "description": desc,
            "author": {"@id": SITE + "/#ryan"},
            "publisher": {"@id": SITE + "/#ryan"},
            "datePublished": article,
            "dateModified": article,
            "mainEntityOfPage": SITE + path,
            "image": SITE + "/og-image.png",
        })
    schema = {"@context": "https://schema.org", "@graph": graph}
    crumb_html = " › ".join(
        [f'<a href="{u}">{n}</a>' for n, u in crumbs[:-1]] + [crumbs[-1][0]]
    )
    faq_block = ""
    if faqs:
        faq_block = f'<h2>Frequently asked questions</h2><div class="faq">{faq_html(faqs)}</div>'
    html = head(title, desc, path, schema=schema, og_type="article" if article else "website")
    html += nav("en")
    html += f"""<main id="main">
<header class="page-hero"><div class="inner">
<p class="crumbs">{crumb_html}</p>
<h1>{h1}</h1>
<p>{intro}</p>
</div></header>
<article class="prose">
{body}
{faq_block}
</article>
{cta_band() if cta else '<div style="height:60px"></div>'}
</main>
"""
    html += tail()
    return html


HOME = ("Home", "/")

SERVICE_PAGES = {
    "/ai-visibility/": dict(
        title="AI Visibility & LLMO Consultant in Los Angeles | Ryan Javaheri",
        desc="Get your business named in ChatGPT, Gemini, Claude and Perplexity answers. LLMO, GEO and AEO from Los Angeles AI consultant Ryan Javaheri.",
        h1="AI Visibility (LLMO): become the business AI recommends.",
        intro="When a customer asks an AI assistant who to hire, it names a few businesses. I make sure yours is one of them.",
        crumbs=[HOME, ("AI Visibility", "/ai-visibility/")],
        body="""<div class="tldr"><b>In short:</b> LLMO (Large Language Model Optimization) makes your business easy for AI models to find, understand, verify and recommend. It works alongside SEO, not instead of it.</div>
<h2>What's included</h2>
<ul>
<li><b>AI visibility audit.</b> What ChatGPT, Claude, Gemini and Perplexity say about you today, and what they say about your competitors.</li>
<li><b>Entity clarity.</b> One consistent description of who you are, what you do and where, on your site and across the web.</li>
<li><b>Structured data.</b> Schema.org markup (Organization, Person, LocalBusiness, Service, FAQ) so machines read your facts without guessing.</li>
<li><b>Answer-ready content.</b> Pages that answer the exact questions customers ask AI, written to be quoted.</li>
<li><b>llms.txt and crawl access.</b> A plain summary file for AI systems, and making sure AI crawlers can actually read your site.</li>
<li><b>Citations and trust.</b> Listings, profiles, reviews and mentions that let models confirm you're real and reputable.</li>
<li><b>Monthly re-checks.</b> Track how AI answers change and keep improving.</li>
</ul>
<h2>How it's different from SEO</h2>
<p>SEO competes for a ranked list of links. AI assistants usually give one synthesized answer and name a handful of sources. That rewards clarity, consistency and trust more than keyword volume. Good LLMO usually improves SEO too, because both depend on clear, credible content.</p>
<h2>Who it's for</h2>
<p>Law firms, local service businesses, professional practices, e-commerce brands and personal brands that win when someone asks "who's the best ___ near me?"</p>
<p>I learned this approach working with <a href="https://siamakconsulting.com/" target="_blank" rel="noopener">Siamak Consulting</a> and apply the same principles here, starting with the B.U.I.L.D. method: Baseline, Understand, Implement, Launch agents, Develop.</p>""",
        faqs=[
            ("How long does LLMO take to work?", "Some changes, like fixing structured data and site clarity, can show up as soon as AI tools re-read your site. Building trust signals and citations compounds over months. I re-check AI answers monthly so you can see progress."),
            ("Can you guarantee ChatGPT will recommend me?", "No one honestly can. AI answers vary by question, user and model. What I can do is remove the reasons AI skips you and build the signals models rely on, then measure the change."),
            ("Do I still need SEO?", "Yes. Search engines still drive traffic and many AI tools use search results as sources. LLMO and SEO reinforce each other."),
        ],
    ),
    "/ai-agents/": dict(
        title="AI Intake Agents for Websites & Phone Lines | Ryan Javaheri",
        desc="AI chat and voice intake agents that answer customer questions 24/7, in any language, and send you qualified leads. Built by Ryan Javaheri in Los Angeles.",
        h1="AI intake agents that answer 24/7 and hand you the lead.",
        intro="An assistant that knows your business, answers questions in the visitor's language, and collects what you need to follow up, on your website or your phone line.",
        crumbs=[HOME, ("AI Intake Agents", "/ai-agents/")],
        body="""<div class="tldr"><b>Try one now:</b> the advisor at the bottom right of this page is a live example. Ask it anything, press <b>Talk</b> to use your voice, or leave your details and watch it hand them to me.</div>
<h2>What an intake agent does</h2>
<ul>
<li><b>Answers questions</b> about your services, process, location and hours, using only facts you approve.</li>
<li><b>Takes a proper intake:</b> name, contact details, what they need, timeline, and anything else you ask for.</li>
<li><b>Sends you the lead</b> with the full conversation, to a private inbox, email or your CRM.</li>
<li><b>Speaks their language.</b> It replies in whatever language the visitor uses.</li>
<li><b>Knows its limits.</b> It never invents prices or gives legal, medical or financial advice. It escalates to you.</li>
</ul>
<h2>Web, voice and phone</h2>
<p><b>Website chat:</b> a chat widget like mine, styled to your brand. <b>Voice on the web:</b> visitors can just talk to it. <b>Phone line:</b> the same agent can answer a real phone number, take messages and book callbacks, so after-hours calls stop going to voicemail.</p>
<h2 id="automation">Automation around it</h2>
<p>An agent is most useful when the next step happens automatically: the lead lands in your CRM, the right person gets a text, the customer gets a confirmation email, and a follow-up goes out if nobody replies. I connect those pieces with the tools you already use.</p>""",
        faqs=[
            ("Will the agent pretend to be a human?", "No. My agents say they're an AI assistant for your business. Honesty builds trust, and many jurisdictions expect it."),
            ("What does it cost to run?", "Running costs are usually small and depend on volume. You get a clear quote covering the build and monthly running costs before we start."),
            ("Can it work for a law firm without giving legal advice?", "Yes. It answers general questions about the firm, collects the facts of the inquiry, and routes it to an attorney. It's instructed never to give legal advice."),
        ],
    ),
    "/websites/": dict(
        title="AI-Ready Website Design & Development | Ryan Javaheri, Los Angeles",
        desc="Fast, modern websites built so customers convert and AI models understand your business: schema, answer-ready pages, lead capture and an optional AI agent.",
        h1="Websites built for people and for AI.",
        intro="A beautiful site that loads fast, turns visitors into leads, and is structured so AI assistants can read and recommend you.",
        crumbs=[HOME, ("AI-Ready Websites", "/websites/")],
        body="""<h2>What "AI-ready" means</h2>
<ul>
<li><b>Clear positioning on every page:</b> who you serve, where, and what you do, in plain words.</li>
<li><b>Structured data</b> for your business, people, services, reviews and FAQs.</li>
<li><b>Answer pages</b> for the questions customers actually ask, with short, quotable answers.</li>
<li><b>llms.txt, sitemap and clean crawl access</b> for search engines and AI crawlers.</li>
<li><b>Fast and accessible</b> on phones, with motion that respects reduced-motion settings.</li>
<li><b>Lead capture built in:</b> forms, a free-check offer, and optionally an AI intake agent.</li>
<li><b>Multilingual</b> when your customers speak more than one language.</li>
</ul>
<h2>Sites I've built</h2>
<p>This site, <a href="https://classroutes.com/">ClassRoutes</a>, and several long-form and portfolio sites for USC Annenberg courses, including <a href="/pr444/">Beyond the Spotlight</a>. See them all in the <a href="/#work">portfolio</a>.</p>
<h2>How a build runs</h2>
<ol><li>A short call and a scan of where you stand.</li><li>Structure and copy: the pages and answers your customers need.</li><li>Design and build, with a private preview link to review.</li><li>Launch, schema checks and an AI visibility baseline.</li><li>Optional monthly care: content, AI re-checks and improvements.</li></ol>""",
        faqs=[
            ("Can you redesign my existing site?", "Yes. I can rebuild it, or keep your platform and add the AI-ready structure, pages and lead capture on top."),
            ("Who owns the site?", "You do. The domain, code and content are yours."),
        ],
    ),
    "/law-firms/": dict(
        title="AI, Intake, Recruiting & PR for Law Firms | Ryan Javaheri",
        desc="Help law firms get named in AI answers, answer every inquiry with a 24/7 AI intake agent, and support lateral recruiting, market intelligence and PR.",
        h1="Law firms: be the firm AI recommends, and never miss an inquiry.",
        intro="AI visibility and intake for firms, backed by a USC education in business law and public relations, plus hands-on recruiting and PR support.",
        crumbs=[HOME, ("Law Firms", "/law-firms/")],
        body="""<h2>Get named when clients ask AI</h2>
<p>People increasingly ask AI assistants things like "best employment lawyer in Los Angeles." I make sure your practice areas, attorneys, locations and credentials are clear and consistent, marked up with structured data, and backed by answer-ready pages, so models can recommend you with confidence.</p>
<h2>24/7 intake without legal advice</h2>
<p>An AI intake agent answers general questions about your firm, collects the facts of the matter and contact details, flags urgency, and routes it to the right attorney. It is instructed never to give legal advice. Read more in <a href="/insights/ai-intake-agents-for-law-firms/">AI intake agents for law firms</a>.</p>
<h2>Talent and recruiting support</h2>
<ul>
<li>Support lateral attorney recruitment and connect with top legal talent</li>
<li>Market intelligence on firm culture, compensation and growth trajectories</li>
<li>Recruitment and retention strategies that build lasting pipelines</li>
<li>Early-talent relationships with promising law students</li>
</ul>
<h2 id="pr">PR and positioning</h2>
<p>Positioning, messaging and media relations that attract the right clients and candidates, and protect your reputation when it matters. My PR training at USC Annenberg shapes how I write every page and agent script.</p>""",
        faqs=[
            ("Are you a lawyer?", "No. I'm a pre-law student studying public relations and business law at USC. I don't give legal advice; I help firms with visibility, intake, recruiting and communications."),
            ("Is AI intake compliant with attorney advertising rules?", "Rules vary by state. The agent is set up to identify itself as AI, avoid legal advice and avoid promising outcomes, and your firm reviews and approves its knowledge and wording before launch."),
        ],
    ),
}

ARTICLES = [
    dict(
        path="/insights/what-is-llmo/",
        date="2026-11-09",
        kicker="Guide",
        title="What Is LLMO? A Plain-English Guide | Ryan Javaheri",
        desc="LLMO (Large Language Model Optimization) explained: how AI assistants decide which businesses to recommend, and practical steps to become one of them.",
        h1="What is LLMO, and why it matters now",
        intro="How AI assistants decide which businesses to name, and what you can do about it.",
        body="""<div class="tldr"><b>Short answer:</b> LLMO (Large Language Model Optimization) is making your business easy for AI assistants to understand, verify and recommend. Think of it as SEO for answers instead of links.</div>
<h2>Why this matters</h2>
<p>More and more people skip the search results and ask an assistant directly: "Who's a good immigration lawyer in Glendale?" or "Where can I buy upholstery fabric in LA?" The assistant gives one short answer that names a few businesses. If you're not in it, you're invisible for that customer.</p>
<h2>How an AI model decides who to name</h2>
<p>Models build answers from what they learned in training plus, increasingly, sources they retrieve live. In both cases they favor businesses that are:</p>
<ul>
<li><b>Clear:</b> it's obvious what you do, for whom, and where.</li>
<li><b>Consistent:</b> your name, services and location match everywhere they appear.</li>
<li><b>Corroborated:</b> other trusted sites, listings and reviews confirm you.</li>
<li><b>Quotable:</b> your pages contain short, direct answers the model can lift.</li>
</ul>
<h2>LLMO vs. SEO vs. GEO vs. AEO</h2>
<p><b>SEO</b> optimizes for ranked search results. <b>AEO</b> (Answer Engine Optimization) targets direct answers like featured snippets and voice answers. <b>GEO</b> (Generative Engine Optimization) and <b>LLMO</b> both target AI-generated answers. In practice, the work overlaps heavily, and the best strategy does all of it from one foundation of clear, trustworthy content. See the <a href="/glossary/">glossary</a> for more terms.</p>
<h2>Five things you can do this month</h2>
<ol>
<li>Write one sentence that says exactly what you do, for whom, and where, and put it on your homepage.</li>
<li>Add structured data (schema.org) for your business and services.</li>
<li>Publish an FAQ that answers the questions customers really ask, in two or three sentences each.</li>
<li>Make your name, address, phone and services identical on Google, Yelp, LinkedIn and industry directories.</li>
<li>Add an llms.txt file summarizing your business for AI systems.</li>
</ol>
<p>Want to know where you stand? <a href="/#scan">Run the free AI visibility scan</a>.</p>""",
    ),
    dict(
        path="/insights/why-chatgpt-doesnt-mention-your-business/",
        date="2026-11-09",
        kicker="Diagnosis",
        title="Why Doesn't ChatGPT Mention My Business? 5 Reasons | Ryan Javaheri",
        desc="The five most common reasons AI assistants like ChatGPT skip a business, and how to fix each one.",
        h1="Why ChatGPT doesn't mention your business",
        intro="The five most common reasons, and the fix for each.",
        body="""<div class="tldr"><b>Short answer:</b> AI assistants recommend businesses they can clearly understand and confirm. If your information is vague, inconsistent, hidden or uncorroborated, they pick someone else.</div>
<h2>1. Your site doesn't say what you do plainly</h2>
<p>Clever taglines don't help a model. "Building tomorrow, today" tells it nothing. <b>Fix:</b> lead with a literal sentence: "Family law firm in Pasadena handling divorce, custody and support."</p>
<h2>2. Your details don't match across the web</h2>
<p>Different business names, old addresses or mismatched services on listings make models unsure you're one entity. <b>Fix:</b> audit and align every listing and profile.</p>
<h2>3. Nobody else vouches for you</h2>
<p>Models lean on corroboration: reviews, directories, press, associations, partner sites. <b>Fix:</b> build a steady set of trustworthy mentions and reviews.</p>
<h2>4. Your answers are buried</h2>
<p>If the answer to "do you handle X in Y?" lives on page six of a PDF, it might as well not exist. <b>Fix:</b> FAQ and service pages with short, direct answers, marked up with FAQ schema.</p>
<h2>5. AI tools can't read your site</h2>
<p>Heavy scripts, blocked crawlers or content inside images can hide you. <b>Fix:</b> make sure key content is real text, crawlers aren't blocked, and you publish a sitemap and llms.txt.</p>
<p>The <a href="/#scan">free scan</a> gives you a quick read on where you stand, and my <a href="/ai-visibility/">AI visibility service</a> fixes all five.</p>""",
    ),
    dict(
        path="/insights/ai-intake-agents-for-law-firms/",
        date="2026-11-09",
        kicker="Law firms",
        title="AI Intake Agents for Law Firms: How They Work | Ryan Javaheri",
        desc="How law firms use AI intake agents to answer every inquiry 24/7, collect the facts, and route qualified matters to attorneys without giving legal advice.",
        h1="AI intake agents for law firms",
        intro="Answer every inquiry, even at 2 a.m., without giving legal advice.",
        body="""<div class="tldr"><b>Short answer:</b> an AI intake agent greets potential clients on your website or phone line, answers general questions about the firm, collects the key facts and contact details, and sends a clean summary to the right attorney.</div>
<h2>The problem it solves</h2>
<p>Many potential clients reach out after hours, and many move on if nobody answers quickly. An intake agent means every inquiry gets a prompt, professional response.</p>
<h2>What a good legal intake agent does</h2>
<ul>
<li>Identifies itself as an AI assistant for the firm.</li>
<li>Answers general questions: practice areas, locations, languages, how consultations work.</li>
<li>Collects the essentials: name, contact, type of matter, key dates, urgency.</li>
<li>Flags urgent matters and conflicts information for staff review.</li>
<li>Never gives legal advice, predicts outcomes, or promises representation.</li>
<li>Works in the client's language.</li>
</ul>
<h2>What attorneys get</h2>
<p>A short summary of each inquiry with the full conversation attached, delivered to email, a private inbox or the firm's CRM, so the first call starts informed.</p>
<h2>Getting started</h2>
<p>Try the advisor on this site to see how it feels, then read about <a href="/ai-agents/">AI intake agents</a> or <a href="/law-firms/">my work with law firms</a>.</p>""",
    ),
]

GLOSSARY = [
    ("LLMO (Large Language Model Optimization)", "Making a business easy for AI assistants to understand, verify and recommend."),
    ("GEO (Generative Engine Optimization)", "Optimizing content to appear in AI-generated answers from tools like ChatGPT, Gemini and Perplexity. Largely overlaps with LLMO."),
    ("AEO (Answer Engine Optimization)", "Structuring content so search and voice assistants can lift it as a direct answer."),
    ("SEO (Search Engine Optimization)", "Improving how a site ranks in traditional search results."),
    ("AI visibility", "How often, and how accurately, AI assistants mention your business when people ask relevant questions."),
    ("Entity", "A distinct thing a machine can identify, such as your business, a person or a place. AI visibility starts with being a clear entity."),
    ("Structured data / Schema", "Code (usually JSON-LD using schema.org vocabulary) that labels facts on a page, like business name, address, services and FAQs."),
    ("llms.txt", "A plain-text file at the root of a website that summarizes it for AI systems, similar in spirit to robots.txt."),
    ("Citation", "A mention of your business on another site, such as a directory, review site or article, that helps confirm you're real and reputable."),
    ("Grounding", "When an AI model bases its answer on specific retrieved sources rather than memory alone."),
    ("RAG (Retrieval-Augmented Generation)", "A technique where an AI system retrieves documents and uses them to write its answer."),
    ("AI agent", "Software that uses an AI model to take actions toward a goal, such as answering a customer and saving their details."),
    ("Intake agent", "An AI agent that greets inquiries, answers basic questions and collects information for a business to follow up."),
    ("Voice agent", "An AI agent that talks by voice, on a website or a phone line."),
    ("Hallucination", "When an AI model states something false with confidence. Good agents are restricted to approved facts to avoid it."),
    ("B.U.I.L.D. method", "Ryan Javaheri's five-step process: Baseline, Understand, Implement, Launch agents, Develop."),
]


def insights_index():
    cards = "".join(
        f'<a class="card post-card" href="{a["path"]}"><div class="cover{" v" + str(i + 1) if i else ""}" data-k="{a["kicker"]}"></div><span class="date">{a["kicker"]} · {a["date"]}</span><h3>{a["h1"]}</h3><p>{a["intro"]}</p></a>'
        for i, a in enumerate(ARTICLES)
    )
    schema = {"@context": "https://schema.org", "@graph": [PERSON, breadcrumb([HOME, ("Insights", "/insights/")]), {
        "@type": "Blog", "name": "Insights by Ryan Javaheri", "url": SITE + "/insights/", "author": {"@id": SITE + "/#ryan"},
        "blogPost": [{"@type": "BlogPosting", "headline": a["h1"], "url": SITE + a["path"], "datePublished": a["date"]} for a in ARTICLES]}]}
    html = head("Insights on AI Visibility, LLMO & AI Agents | Ryan Javaheri",
                "Plain-English articles on LLMO, AI visibility, AI intake agents and AI-ready websites by Los Angeles AI consultant Ryan Javaheri.",
                "/insights/", schema=schema)
    html += nav("en")
    html += f"""<main id="main">
<header class="page-hero"><div class="inner"><p class="crumbs"><a href="/">Home</a> › Insights</p><h1>Insights.</h1><p>Plain-English notes on AI visibility, AI agents and building for the AI era.</p></div></header>
<section class="block"><div class="inner"><div class="cards stagger">{cards}</div></div></section>
{cta_band()}
</main>
"""
    return html + tail()


def glossary():
    dl = "".join(f"<dt id=\"{t.split(' ')[0].lower().strip('()')}\">{t}</dt><dd>{d}</dd>" for t, d in GLOSSARY)
    schema = {"@context": "https://schema.org", "@graph": [PERSON, breadcrumb([HOME, ("Glossary", "/glossary/")]), {
        "@type": "DefinedTermSet", "name": "AI Visibility Glossary", "url": SITE + "/glossary/",
        "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t, "description": d} for t, d in GLOSSARY]}]}
    html = head("AI Visibility Glossary: LLMO, GEO, AEO & More | Ryan Javaheri",
                "Definitions of LLMO, GEO, AEO, structured data, llms.txt, AI agents and other AI visibility terms.",
                "/glossary/", schema=schema)
    html += nav("en")
    html += f"""<main id="main" class="glossary">
<header class="page-hero"><div class="inner"><p class="crumbs"><a href="/">Home</a> › Glossary</p><h1>The AI visibility glossary.</h1><p>{len(GLOSSARY)} terms, explained simply.</p></div></header>
<dl>{dl}</dl>
{cta_band()}
</main>
"""
    return html + tail()


def privacy():
    import legal
    return page("/privacy/", "Privacy Policy | Ryan Javaheri", "What ryanjavaheri.com collects through its forms, free AI scan and AI advisor, how cookies work, and your choices.",
                "Privacy Policy", "Plain language: what this site collects, why, and how to control it.", legal.PRIVACY, [HOME, ("Privacy", "/privacy/")], cta=False)


def terms():
    import legal
    return page("/terms/", "Terms of Use | Ryan Javaheri", "The terms for using ryanjavaheri.com, its free AI scan and AI advisor, including the no-legal-advice and AI disclaimers.",
                "Terms of Use", "The rules for using this site and its AI tools.", legal.TERMS, [HOME, ("Terms", "/terms/")], cta=False)


def portfolio_page():
    import portfolio
    kinds = []
    for p in portfolio.PORTFOLIO:
        if p["kind"] not in kinds:
            kinds.append(p["kind"])
    schema = {"@context": "https://schema.org", "@graph": [PERSON, breadcrumb([HOME, ("Portfolio", "/portfolio/")]), {
        "@type": "CollectionPage", "name": "Portfolio of Ryan Javaheri", "url": SITE + "/portfolio/",
        "about": {"@id": SITE + "/#ryan"},
        "mainEntity": {"@type": "ItemList", "itemListElement": portfolio.schema_items(SITE)}}]}
    html = head("Portfolio — Websites, AI Agents & Projects by Ryan Javaheri",
                "Every website, AI agent and project built by Ryan Javaheri: client sites, AI intake agents, ClassRoutes and USC Annenberg work.",
                "/portfolio/", schema=schema)
    html += nav("en")
    groups = ""
    for k in kinds:
        items = [p for p in portfolio.PORTFOLIO if p["kind"] == k]
        groups += f'<div class="reveal" style="margin-top:50px"><p class="eyebrow">{k}{"s" if not k.endswith("s") else ""}</p></div><div class="cards stagger" style="margin-top:10px">{portfolio.cards(items)}</div>'
    html += f"""<main id="main">
<header class="page-hero"><div class="inner"><p class="crumbs"><a href="/">Home</a> › Portfolio</p><h1>Everything I've built.</h1><p>{len(portfolio.PORTFOLIO)} websites, AI agents and projects, newest first. Every new build gets added here.</p></div></header>
<section class="block alt" style="padding-top:40px"><div class="inner">{groups}</div></section>
{cta_band("Want something built?", "Websites, AI agents and AI visibility. Tell my AI advisor what you need.")}
</main>
"""
    return html + tail()


def experience_page():
    import me
    schema = {"@context": "https://schema.org", "@graph": [PERSON, breadcrumb([HOME, ("Experience", "/experience/")])]}
    html = head("Experience — Ryan Javaheri", "Ryan Javaheri's experience: AI business strategy, Equinox, content creation, Payman Fabric and Spandex Palace, Kol Torah Center and more.", "/experience/", schema=schema)
    html += nav("en")
    html += f"""<main id="main">
<section id="experience">
<div class="slideshow-track" id="slideshowTrack" style="height:{me.track_height()}">
<div class="slideshow-sticky">
<div class="slideshow-head">
<p class="eyebrow">Experience</p>
<h2>Experience.</h2>
<p style="font-size:19px;color:#333;max-width:700px;">AI and web work, content creation, and years of real sales and small-business experience.</p>
</div>
<div class="slideshow-stage" id="slideshowStage">
{me.slides()}
</div>
<div class="slide-dots" id="slideDots">{me.dots()}</div>
<p class="slideshow-hint">Keep scrolling</p>
</div>
</div>
</section>
{cta_band("Want to work together?", "Ask my AI advisor or send a message. I reply personally.")}
</main>
"""
    return html + tail()
