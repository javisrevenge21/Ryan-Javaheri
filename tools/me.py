"""Ryan's background, taken from his LinkedIn profile (linkedin.com/in/ryanjavaheri).
Keep this in sync with LinkedIn. Used by the homepage Experience and Education sections."""

LINKEDIN = "https://www.linkedin.com/in/ryanjavaheri"

HEADLINE = "USC Annenberg ’27 | PR & Pre-Law | Sales, Content Creation & Web Development | English & Farsi"

# Newest first.
EXPERIENCE = [
    dict(title="AI Business Strategy Developer", org="Self-employed", when="Jun 2026 – Present · Remote",
         desc="Creating and promoting AI products: AI-ready websites, AI intake agents and AI visibility work, including projects with Siamak Consulting while learning LLMO from Siamak Kalhor."),
    dict(title="Style Advisor", org="Equinox", when="Nov 2026 – Present · Los Angeles",
         desc="Part-time, on-site sales and client service, building relationships with members through communication and personal attention."),
    dict(title="Content Creator", org="Instagram & YouTube · Self-employed", when="Nov 2021 – Present",
         desc="Built and grew content channels with short- and long-form video. Audience growth, storytelling, content systems and analytics, using automation to scale production, and helping others promote their products and ideas."),
    dict(title="Market & Retail Specialist", org="Payman Fabric Inc. & Spandex Palace", when="Sep 2023 – May 2026 · Los Angeles",
         desc="Started at 17 while still in high school. Sold in person and online through Shopify, helped design and promote the stores, and handled day-to-day customer service for two connected Los Angeles fabric businesses."),
    dict(title="President", org="Kol Torah Center", when="Apr 2021 – Jan 2023",
         desc="Led a Monday Jewish club for teens from Palisades Charter, Beverly Hills High and Milken, combining Jewish learning, basketball and social time. Later led the Persian Student Union at Palisades Charter (2023–2024)."),
    dict(title="Food Delivery Driver", org="Uber · Self-employed", when="Aug 2024 – Dec 2024",
         desc="Delivered orders on a flexible schedule while taking college classes, focused on on-time, accurate delivery and friendly service."),
]

EDUCATION = [
    dict(school="University of Southern California", sub="USC Annenberg · Class of 2027", when="Aug 2025 – Jun 2027",
         desc="PR / Pre-Law, Public Relations & Image Management, with a minor in Business Law."),
    dict(school="Santa Monica College & Citrus College", sub="History · 3.7 and 3.9 GPA", when="2024 – 2025",
         desc="Took classes at both colleges at the same time, carrying a heavy course load to finish credits early before transferring to USC."),
    dict(school="Palisades Charter High School", sub="High School Diploma", when="2020 – 2024",
         desc="President of the Kol Torah Center Jewish club (2021–2023) and leader of the Persian Student Union (2023–2024)."),
    dict(school="Colibri Real Estate", sub="Real estate pre-licensing", when="2024",
         desc="Completed the three pre-licensing courses for certification, with an A."),
    dict(school="Siamak Consulting", sub="AI consulting apprenticeship", when="2026 – Present",
         desc="Learning LLMO, AI strategy and client work hands-on from AI consultant Siamak Kalhor."),
]


def slides():
    n = len(EXPERIENCE)
    return "\n".join(
        f'<div class="slide"><p class="slide-num">{i + 1:02d} / {n:02d} · {e["when"]}</p><h3>{e["title"]}</h3>'
        f'<p class="slide-org">{e["org"]}</p><p>{e["desc"]}</p></div>'
        for i, e in enumerate(EXPERIENCE)
    )


def dots():
    return "".join('<span class="on"></span>' if i == 0 else "<span></span>" for i in range(len(EXPERIENCE)))


def track_height():
    return f"{100 + len(EXPERIENCE) * 60}vh"


def education_cards():
    return "\n".join(
        f'<div class="card"><span class="site-tag">{e["when"]}</span><h3>{e["school"]}</h3>'
        f'<p style="color:var(--black);font-weight:500;margin-bottom:8px">{e["sub"]}</p><p>{e["desc"]}</p></div>'
        for e in EDUCATION
    )
