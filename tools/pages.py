"""Shared layout for ryanjavaheri.com. Run `python3 tools/build.py` after editing content."""
import json

SITE = "https://ryanjavaheri.com"
EMAIL = "ryanjavaheri21@gmail.com"
YEAR = "2026"

# code, <html lang>, native name. Order = order in the language menu.
LANGS = [
    ("en", "en", "English"), ("es", "es", "Español"), ("fa", "fa", "فارسی"), ("he", "he", "עברית"),
    ("ar", "ar", "العربية"), ("zh", "zh-Hans", "中文"), ("ko", "ko", "한국어"), ("ja", "ja", "日本語"),
    ("fr", "fr", "Français"), ("pt", "pt", "Português"), ("ru", "ru", "Русский"), ("hy", "hy", "Հայերեն"),
    ("hi", "hi", "हिन्दी"),
]
RTL = {"fa", "he", "ar"}
NAV_T = {
    "es": ("Servicios", "Portafolio", "Método", "Contacto", "Escaneo gratis"),
    "fa": ("خدمات", "نمونه‌کارها", "روش کار", "تماس", "اسکن رایگان"),
    "he": ("שירותים", "תיק עבודות", "השיטה", "צור קשר", "סריקה חינם"),
    "ar": ("الخدمات", "الأعمال", "المنهج", "تواصل", "فحص مجاني"),
    "zh": ("服务", "作品集", "方法", "联系", "免费扫描"),
    "ko": ("서비스", "포트폴리오", "방법론", "연락", "무료 스캔"),
    "ja": ("サービス", "ポートフォリオ", "メソッド", "お問い合わせ", "無料スキャン"),
    "fr": ("Services", "Portfolio", "Méthode", "Contact", "Scan gratuit"),
    "pt": ("Serviços", "Portfólio", "Método", "Contato", "Análise grátis"),
    "ru": ("Услуги", "Портфолио", "Метод", "Контакты", "Бесплатный анализ"),
    "hy": ("Ծառայություններ", "Պորտֆոլիո", "Մեթոդ", "Կապ", "Անվճար ստուգում"),
    "hi": ("सेवाएँ", "पोर्टफ़ोलियो", "तरीका", "संपर्क", "मुफ़्त स्कैन"),
}


def lang_menu(cur="en"):
    name = dict((c, n) for c, _, n in LANGS)[cur]
    links = "".join(
        f'<a href="{"/" if c == "en" else "/" + c + "/"}" hreflang="{h}" lang="{h}"{" aria-current=\"page\"" if c == cur else ""}>{n}</a>'
        for c, h, n in LANGS
    )
    return f'<div class="dd lang-dd"><button type="button" aria-expanded="false" aria-label="Language">🌐 {name}</button><div class="dd-menu lang-menu">{links}</div></div>'


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
<a href="/portfolio/">Portfolio</a>
<a href="/experience/">Experience</a>
<div class="dd"><button type="button" aria-expanded="false">Learn</button><div class="dd-menu"><a href="/insights/">Insights<small>Articles on AI visibility</small></a><a href="/glossary/">Glossary<small>LLMO, GEO, AEO and more</small></a><a href="/#faq">FAQ<small>Quick answers</small></a></div></div>
<a href="/#about">About</a>
<a href="/#contact">Contact</a>
{lang_menu("en")}
<a class="nav-cta" href="/#scan">Free AI scan</a>
</div>
</div>
</nav>"""
    labels = NAV_T[lang]
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="progress" id="progress"></div>
<nav class="site" aria-label="Main">
<div class="nav-inner">
<a class="brand" href="/{lang}/" dir="ltr">Ryan Javaheri <span>· AI</span></a>
<button class="burger" aria-label="Menu" aria-expanded="false">☰</button>
<div class="nav-links">
<a href="#services">{labels[0]}</a>
<a href="#portfolio">{labels[1]}</a>
<a href="#method">{labels[2]}</a>
<a href="#contact">{labels[3]}</a>
{lang_menu(lang)}
<a class="nav-cta" href="/#scan">{labels[4]}</a>
</div>
</div>
</nav>"""


def footer(lang="en"):
    return f"""<footer class="site">
<div class="fcols">
<div><h4>Ryan Javaheri</h4><p>AI consultant and website builder in Los Angeles. AI visibility, AI intake agents and AI-ready websites, plus recruiting and PR support for law firms.</p></div>
<div><h4>Services</h4>{''.join(f'<a href="{u}">{t}</a>' for u, t, d in SERVICES)}<a href="/#scan">Free AI visibility scan</a></div>
<div><h4>Work</h4><a href="/portfolio/">Portfolio</a><a href="/experience/">Experience</a><a href="/pr444/">Beyond the Spotlight</a><a href="/pr351a/">PR 351A</a><a href="/jour330/">Photojournalism</a></div>
<div><h4>Learn</h4><a href="/insights/">Insights</a><a href="/glossary/">Glossary</a><a href="/#faq">FAQ</a><a href="/llms.txt">llms.txt</a></div>
<div><h4>Contact</h4><a href="mailto:{EMAIL}">{EMAIL}</a><a href="https://www.linkedin.com/in/ryanjavaheri" target="_blank" rel="noopener">LinkedIn</a><a href="#" data-open-agent="">Talk to my AI advisor</a><a href="/#contact">Start a project</a></div>
<div><h4>Languages</h4>{"".join(f'<a href="{"/" if c == "en" else "/" + c + "/"}" lang="{h}">{n}</a>' for c, h, n in LANGS)}</div>
</div>
<div class="fbottom"><span>&copy; {YEAR} Ryan Javaheri. Los Angeles, California. Serving clients everywhere.</span><span><a href="/privacy/">Privacy</a><a href="/portfolio/">Portfolio</a></span></div>
</footer>"""


FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='22' fill='%23000000'/%3E%3Ctext x='50' y='50' font-family='Snell Roundhand,Brush Script MT,Segoe Script,cursive' font-size='56' font-style='italic' font-weight='700' fill='white' text-anchor='middle' dominant-baseline='central'%3ERJ%3C/text%3E%3C/svg%3E"


def head(title, desc, path, lang="en", schema=None, og_type="website", extra=""):
    url = SITE + path
    dir_attr = ' dir="rtl"' if lang.split("-")[0] in RTL else ""
    alts = ""
    if path == "/" or path.strip("/") in [c for c, _, _ in LANGS]:
        alts = "".join(
            f'<link rel="alternate" hreflang="{h}" href="{SITE}{"/" if c == "en" else "/" + c + "/"}">\n' for c, h, _ in LANGS
        ) + f'<link rel="alternate" hreflang="x-default" href="{SITE}/">\n'

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
    "sameAs": ["https://www.linkedin.com/in/ryanjavaheri"],
    "jobTitle": "AI Business Strategy Developer & Website Builder",
    "description": "USC Annenberg PR and pre-law student (Class of 2027) in Los Angeles. Builds websites and AI products, creates content, and brings years of sales and small-business experience. Fluent in English and Farsi.",
    "address": {"@type": "PostalAddress", "addressLocality": "Los Angeles", "addressRegion": "CA", "addressCountry": "US"},
    "alumniOf": [
        {"@type": "CollegeOrUniversity", "name": "University of Southern California", "url": "https://www.usc.edu/"},
        {"@type": "CollegeOrUniversity", "name": "Santa Monica College"},
        {"@type": "CollegeOrUniversity", "name": "Citrus College"},
        {"@type": "HighSchool", "name": "Palisades Charter High School"},
    ],
    "knowsLanguage": ["English", "Persian"],
    "knowsAbout": ["Public relations", "Pre-law", "Business law", "Web development", "HTML", "CSS", "JavaScript", "Content creation", "Social media", "Sales", "Customer service", "Retail", "Shopify", "Large Language Model Optimization (LLMO)", "AI agents", "Structured data"],
    "worksFor": [
        {"@type": "Organization", "name": "Siamak Consulting", "url": "https://siamakconsulting.com/"},
        {"@type": "Organization", "name": "Equinox"},
    ],
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
