"""THE PORTFOLIO: every website and project Ryan builds, newest first.

Standing rule (see CLAUDE.md): whenever Ryan builds a new website, app, agent or other project,
add an entry at the TOP of this list in the same change, then run `python3 tools/build.py`.
It appears automatically on the homepage portfolio section and on /portfolio/.

Fields:
  tag   short label (status, course code, or type)
  name  project name
  desc  one sentence on what it is
  url   link (absolute for other domains, /path/ for pages on this site, "#agent" opens the AI advisor)
  label link text shown on the card
  kind  "Website", "AI agent", "App", "Course project", ...
  date  when it was built or launched (YYYY-MM or YYYY)
"""

PORTFOLIO = [
    dict(tag="AI agent · Live", name="AI Intake Advisor", kind="AI agent", date="2026-11",
         desc="The chat and voice agent on this site: answers questions 24/7 in any language and sends every lead to a private inbox.",
         url="#agent", label="Try it now ›"),
    dict(tag="Website · Live", name="ryanjavaheri.com", kind="Website", date="2026-11",
         desc="This site: an AI consulting site with a free AI visibility scan, Spanish and Farsi pages, and full structured data for AI search.",
         url="/", label="ryanjavaheri.com ›"),
    dict(tag="Relaunching soon", name="JAVISREVENGE", kind="Website", date="2026",
         desc="An independent web project, currently offline while a new version is finished.",
         url="https://javisrevenge.com/", label="javisrevenge.com ›"),
    dict(tag="Coming soon", name="ClassRoutes", kind="App", date="2026",
         desc="A class-planning platform for community college and university students: major and minor planning, transfer planning, and professor and course lookup.",
         url="https://classroutes.com/", label="classroutes.com ›"),
    dict(tag="PR 444", name="Beyond the Spotlight", kind="Course project", date="2026",
         desc="A long-form feature on how athletes and celebrities build, protect, and repair their public image.",
         url="/pr444/", label="ryanjavaheri.com/pr444 ›"),
    dict(tag="PR 351A", name="Public Relations Portfolio", kind="Course project", date="2026",
         desc="My public relations writing and campaign work from USC Annenberg.",
         url="/pr351a/", label="ryanjavaheri.com/pr351a ›"),
    dict(tag="JOUR 330", name="Photojournalism", kind="Course project", date="2026",
         desc="Photo essays, assignments, and visual storytelling from JOUR 330 at USC Annenberg.",
         url="/jour330/", label="ryanjavaheri.com/jour330 ›"),
]


def card(p):
    if p["url"] == "#agent":
        attrs = 'href="#" data-open-agent=""'
    elif p["url"].startswith("http"):
        attrs = f'href="{p["url"]}" target="_blank" rel="noopener"'
    else:
        attrs = f'href="{p["url"]}"'
    return (f'<a class="card site-card" {attrs}>\n<span class="site-tag">{p["tag"]}</span>\n'
            f'<h3>{p["name"]}</h3>\n<p>{p["desc"]}</p>\n<span class="site-url">{p["label"]}</span>\n</a>')


def cards(items=None):
    return "\n".join(card(p) for p in (items or PORTFOLIO))


def schema_items(site):
    out = []
    for i, p in enumerate(PORTFOLIO):
        url = p["url"]
        if url == "#agent":
            url = site + "/"
        elif url.startswith("/"):
            url = site + url
        out.append({"@type": "ListItem", "position": i + 1, "item": {
            "@type": "CreativeWork", "name": p["name"], "description": p["desc"], "url": url,
            "creator": {"@id": site + "/#ryan"}, "dateCreated": p["date"], "genre": p["kind"]}})
    return out
