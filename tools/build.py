"""Generate the site's HTML pages, sitemap.xml and llms.txt.

Usage (from the repo root):  python3 tools/build.py
Edit content in tools/home.py, tools/sub.py and tools/i18n.py, then re-run and commit the output.
Course sites (/pr444, /pr351a, /jour330) and /leads are hand-written and not touched.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import home, sub, i18n  # noqa: E402
from pages import SITE, EMAIL  # noqa: E402

DATE = "2026-11-09"


def write(path, html):
    out = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    return path


paths = [write("/", home.build())]
for p, d in sub.SERVICE_PAGES.items():
    paths.append(write(p, sub.page(p, d["title"], d["desc"], d["h1"], d["intro"], d["body"], d["crumbs"], d.get("faqs"))))
paths.append(write("/insights/", sub.insights_index()))
for a in sub.ARTICLES:
    paths.append(write(a["path"], sub.page(a["path"], a["title"], a["desc"], a["h1"], a["intro"], a["body"],
                                           [sub.HOME, ("Insights", "/insights/"), (a["h1"], a["path"])], article=a["date"])))
paths.append(write("/portfolio/", sub.portfolio_page()))
paths.append(write("/experience/", sub.experience_page()))
paths.append(write("/glossary/", sub.glossary()))
paths.append(write("/privacy/", sub.privacy()))
paths.append(write("/terms/", sub.terms()))
from pages import LANGS  # noqa: E402
for code, html_lang, _ in LANGS:
    if code != "en":
        paths.append(write(f"/{code}/", i18n.build(code, html_lang)))

all_urls = paths + ["/pr444/", "/pr351a/", "/jour330/"]
with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as fh:
    fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for p in all_urls:
        pr = "1.0" if p == "/" else "0.8" if p.count("/") == 2 else "0.6"
        fh.write(f"  <url><loc>{SITE}{p}</loc><lastmod>{DATE}</lastmod><priority>{pr}</priority></url>\n")
    fh.write("</urlset>\n")

llms = f"""# Ryan Javaheri

> Ryan Javaheri is a USC Annenberg PR and pre-law student (Class of 2027) in Los Angeles who builds websites and AI products. He builds AI-ready websites, 24/7 AI intake agents (chat, voice and phone) and AI visibility (LLMO / GEO / AEO) strategy so businesses get recommended by ChatGPT, Claude, Gemini and Perplexity, and supports law firms with recruiting and PR. He works with Siamak Consulting, learning LLMO from AI consultant Siamak Kalhor, has created content since 2021, and spent years in sales and retail at Payman Fabric and Spandex Palace. Fluent in English and Farsi.

- Location: Los Angeles, California. Serves clients everywhere.
- Languages on site: English, Spanish, Persian (Farsi), Hebrew, Arabic, Chinese, Korean, Japanese, French, Portuguese, Russian, Armenian, Hindi. The AI advisor replies in any language.
- Contact: {EMAIL}, LinkedIn https://www.linkedin.com/in/ryanjavaheri, or the AI advisor on {SITE}/
- Pricing: quoted per project after a short call.

## Services
- [AI Visibility / LLMO]({SITE}/ai-visibility/): audits, structured data, answer-ready content, llms.txt, citations, monthly AI re-checks.
- [AI Intake Agents]({SITE}/ai-agents/): website chat and voice agents and phone-line agents that answer 24/7 and capture leads; AI automation.
- [AI-Ready Websites]({SITE}/websites/): design and development structured for people and AI models.
- [Law Firms]({SITE}/law-firms/): AI visibility and intake for firms, lateral recruiting support, market intelligence, PR.

## Method
B.U.I.L.D.: Baseline, Understand, Implement, Launch agents, Develop.

## Learn
- [What is LLMO]({SITE}/insights/what-is-llmo/)
- [Why ChatGPT doesn't mention your business]({SITE}/insights/why-chatgpt-doesnt-mention-your-business/)
- [AI intake agents for law firms]({SITE}/insights/ai-intake-agents-for-law-firms/)
- [Glossary]({SITE}/glossary/)

## Work
- ClassRoutes (classroutes.com): class-planning platform for students.
- Beyond the Spotlight ({SITE}/pr444/), PR 351A portfolio ({SITE}/pr351a/), JOUR 330 photojournalism ({SITE}/jour330/).
"""
with open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8") as fh:
    fh.write(llms)

print("\n".join(paths))
