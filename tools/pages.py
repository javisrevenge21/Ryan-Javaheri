"""Shared layout for ryanjavaheri.com. Run `python3 tools/build.py` after editing content."""
import json

SITE = "https://ryanjavaheri.com"
EMAIL = "ryanjavaheri21@gmail.com"
YEAR = "2026"

SERVICES = [
    ("/ai-visibility/", "AI Visibility (LLMO)", "Become the business AI recommends."),
    ("/ai-agents/", "AI Intake Agents", "Chat and voice agents that answer and capture leads 24/7."),
    ("/websites/", "AI-Ready Websites", "Fast sites that people and AI models both understand."),
    ("/law-firms/", "For Law Firms", "AI, recruiting and PR support for firms."),
]


def nav(lang="en", here=""):
    if lang == "en":
        menu = "".join(
            f'<a href="{u}">{t}<small>{d}</small></a>' for u, t, d in SERVICES
        )
        return f"""<a class="skip" href="#main">Skip to content</a>
<div class="progress" id="progress"></div>
<nav class="site" aria-label="Main">
<div class="nav-inner">
<a class="brand" href="/">Ryan Javaheri <span>· AI</span></a>
<button class="burger" aria-label="Menu" aria-expanded="false">☰</button>
<div class="nav-links">
<div class="dd"><button type="button" aria-expanded="false">Services</button><div class="dd-menu">{menu}<a href="/#method">The B.U.I.L.D. method<small>How every project runs</small></a></div></div>
<a href="/#work">Work</a>
<div class="dd"><button type="button" aria-expanded="false">Learn</button><div class="dd-menu"><a href="/insights/">Insights<small>Articles on AI visibility</small></a><a href="/glossary/">Glossary<small>LLMO, GEO, AEO and more</small></a><a href="/#faq">FAQ<small>Quick answers</small></a></div></div>
<a href="/#about">About</a>
<a href="/#contact">Contact</a>
<span class="lang"><a href="/" aria-current="page">EN</a><a href="/es/" hreflang="es">ES</a><a href="/fa/" hreflang="fa">فا</a></span>
<a class="nav-cta" href="/#scan">Free AI scan</a>
</div>
</div>
</nav>"""
    labels = {
        "es": ("Servicios", "Método", "Contacto", "Escaneo gratis"),
        "fa": ("خدمات", "روش کار", "تماس", "اسکن رایگان"),
    }[lang]
    cur = {"es": ("", ' aria-current="page"', ""), "fa": ("", "", ' aria-current="page"')}[lang]
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="progress" id="progress"></div>
<nav class="site" aria-label="Main">
<div class="nav-inner">
<a class="brand" href="/{lang}/">Ryan Javaheri <span>· AI</span></a>
<button class="burger" aria-label="Menu" aria-expanded="false">☰</button>
<div class="nav-links">
<a href="#services">{labels[0]}</a>
<a href="#method">{labels[1]}</a>
<a href="#contact">{labels[2]}</a>
<span class="lang"><a href="/" hreflang="en"{cur[0]}>EN</a><a href="/es/" hreflang="es"{cur[1]}>ES</a><a href="/fa/" hreflang="fa"{cur[2]}>فا</a></span>
<a class="nav-cta" href="/#scan">{labels[3]}</a>
</div>
</div>
</nav>"""


def footer(lang="en"):
    return f"""<footer class="site">
<div class="fcols">
<div><h4>Ryan Javaheri</h4><p>AI consultant and website builder in Los Angeles. AI visibility, AI intake agents and AI-ready websites, plus recruiting and PR support for law firms.</p></div>
<div><h4>Services</h4>{''.join(f'<a href="{u}">{t}</a>' for u, t, d in SERVICES)}<a href="/#scan">Free AI visibility scan</a></div>
<div><h4>Learn</h4><a href="/insights/">Insights</a><a href="/glossary/">Glossary</a><a href="/#faq">FAQ</a><a href="/llms.txt">llms.txt</a></div>
<div><h4>Contact</h4><a href="mailto:{EMAIL}">{EMAIL}</a><a href="#" data-open-agent="">Talk to my AI advisor</a><a href="/#contact">Start a project</a><a href="/es/">Español</a><a href="/fa/">فارسی</a></div>
</div>
<div class="fbottom"><span>&copy; {YEAR} Ryan Javaheri. Los Angeles, California. Serving clients everywhere.</span><span><a href="/privacy/">Privacy</a><a href="/#work">Portfolio</a></span></div>
</footer>"""


FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='22' fill='%23000000'/%3E%3Ctext x='50' y='50' font-family='Snell Roundhand,Brush Script MT,Segoe Script,cursive' font-size='56' font-style='italic' font-weight='700' fill='white' text-anchor='middle' dominant-baseline='central'%3ERJ%3C/text%3E%3C/svg%3E"


def head(title, desc, path, lang="en", schema=None, og_type="website", extra=""):
    url = SITE + path
    dir_attr = ' dir="rtl"' if lang == "fa" else ""
    alts = ""
    if path in ("/", "/es/", "/fa/"):
        alts = (
            f'<link rel="alternate" hreflang="en" href="{SITE}/">\n'
            f'<link rel="alternate" hreflang="es" href="{SITE}/es/">\n'
            f'<link rel="alternate" hreflang="fa" href="{SITE}/fa/">\n'
            f'<link rel="alternate" hreflang="x-default" href="{SITE}/">\n'
        )
    ld = ""
    if schema:
        ld = '<script type="application/ld+json">\n' + json.dumps(schema, ensure_ascii=False, indent=1) + "\n</script>\n"
    return f"""<!DOCTYPE html>
<html lang="{lang}"{dir_attr}>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="author" content="Ryan Javaheri">
<meta name="theme-color" content="#0b0b0d">
<meta name="geo.region" content="US-CA">
<meta name="geo.placename" content="Los Angeles">
<link rel="canonical" href="{url}">
{alts}<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Ryan Javaheri">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/og-image.png">
<link rel="icon" type="image/svg+xml" href="{FAVICON}">
<link rel="stylesheet" href="/assets/site.css">
{ld}{extra}</head>
<body>
"""


def tail(lang="en"):
    return f"""{footer(lang)}
<script src="/assets/site.js" defer></script>
<script src="/assets/agent.js" defer></script>
</body>
</html>
"""


PERSON = {
    "@type": "Person",
    "@id": SITE + "/#ryan",
    "name": "Ryan Javaheri",
    "url": SITE + "/",
    "image": SITE + "/og-image.png",
    "email": "mailto:" + EMAIL,
    "jobTitle": "AI Consultant & Website Builder",
    "description": "Los Angeles AI consultant and website builder. AI visibility (LLMO), AI intake agents and AI-ready websites, plus recruiting and PR support for law firms.",
    "address": {"@type": "PostalAddress", "addressLocality": "Los Angeles", "addressRegion": "CA", "addressCountry": "US"},
    "alumniOf": {"@type": "CollegeOrUniversity", "name": "University of Southern California", "url": "https://www.usc.edu/"},
    "knowsLanguage": ["English", "Persian"],
    "knowsAbout": ["Large Language Model Optimization (LLMO)", "Generative Engine Optimization (GEO)", "Answer Engine Optimization (AEO)", "AI agents", "Website development", "Structured data", "Legal recruiting", "Public relations", "Business law"],
    "worksFor": {"@type": "Organization", "name": "Siamak Consulting", "url": "https://siamakconsulting.com/"},
}


def breadcrumb(items):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items)
        ],
    }


def faq_schema(qas):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qas
        ],
    }


def faq_html(qas):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in qas)


def cta_band(title="Want to be the answer AI gives?", sub="Run the free scan, or tell my AI advisor what you need. I follow up personally."):
    return f"""<div class="cta-band reveal"><div><h2>{title}</h2><p>{sub}</p></div>
<div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-light" href="/#scan">Free AI scan</a><a class="btn btn-light" href="#" data-open-agent="">Ask my AI advisor</a></div></div>"""
