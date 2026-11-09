from pages import head, nav, tail, PERSON, SITE, EMAIL, faq_schema, faq_html

T = {
    "es": dict(
        title="Ryan Javaheri — Consultor de IA, Agentes de IA y Sitios Web | Los Ángeles",
        desc="Consultor de IA en Los Ángeles: sitios web preparados para IA, agentes de admisión 24/7 y visibilidad en IA (LLMO) para que ChatGPT, Gemini y Perplexity te recomienden.",
        kicker="Asesor de IA en línea 24/7, en tu idioma",
        h1a="Sé el nombre que", h1b="la IA recomienda.",
        sub="Construyo sitios web preparados para IA, agentes de admisión con IA y estrategia de visibilidad, para que cuando tus clientes pregunten a ChatGPT, Gemini o Perplexity a quién contratar, la respuesta seas tú.",
        who="Ryan Javaheri · Consultor de IA y desarrollador web · USC · Los Ángeles",
        cta1="Escaneo de IA gratis", cta2="Habla con mi asesor de IA →",
        s_eye="Servicios", s_h="Lo que construyo para ti.",
        services=[
            ("Visibilidad en IA (LLMO)", "Que ChatGPT, Gemini y Perplexity recomienden tu negocio.", "/ai-visibility/"),
            ("Agentes de admisión con IA", "Chat y voz que responden 24/7 y te entregan clientes potenciales.", "/ai-agents/"),
            ("Sitios web preparados para IA", "Rápidos, modernos y fáciles de entender para personas y para la IA.", "/websites/"),
            ("Para despachos de abogados", "Visibilidad, admisión, reclutamiento y relaciones públicas.", "/law-firms/"),
        ],
        m_eye="El método", m_h="B.U.I.L.D.",
        steps=[("B", "Base", "Vemos qué dice la IA de ti hoy."), ("U", "Entender", "Las preguntas reales de tus clientes."), ("I", "Implementar", "Sitio, schema, contenido y llms.txt."), ("L", "Lanzar agentes", "Admisión con IA en web y teléfono."), ("D", "Desarrollar", "Revisión mensual y mejora continua.")],
        a_eye="Sobre mí", a_p="Trabajo con Siamak Consulting, donde aprendo LLMO y estrategia de IA directamente de Siamak Kalhor, y construyo sitios web y agentes de IA para clientes. Estudio relaciones públicas y derecho empresarial en USC.",
        faq=[
            ("¿Qué es LLMO?", "LLMO (optimización para modelos de lenguaje) es hacer que tu negocio sea fácil de entender, verificar y recomendar para asistentes como ChatGPT, Claude, Gemini y Perplexity."),
            ("¿Qué hace un agente de admisión con IA?", "Responde preguntas 24/7 en el idioma del visitante, recoge su nombre, contacto y lo que necesita, y te lo envía. El asesor de este sitio es un ejemplo en vivo."),
            ("¿Cuánto cuesta?", "Cada proyecto se cotiza después de una breve llamada. Cuéntale a mi asesor de IA lo que necesitas y te envío una cotización."),
        ],
        c_eye="Contacto", c_h="Construyamos algo.", c_p="Cuéntame sobre tu negocio. Leo cada mensaje y respondo personalmente.",
        f=("Nombre *", "Correo *", "Empresa", "Teléfono", "¿Qué necesitas? *", "Enviar a Ryan", "¡Gracias! Te contactaré personalmente."),
        faq_h="Preguntas frecuentes",
    ),
    "fa": dict(
        title="رایان جواهری — مشاور هوش مصنوعی، ایجنت‌های هوش مصنوعی و طراحی وب‌سایت | لس‌آنجلس",
        desc="مشاور هوش مصنوعی در لس‌آنجلس: وب‌سایت‌های آماده برای هوش مصنوعی، ایجنت‌های پذیرش ۲۴ ساعته و دیده‌شدن در پاسخ‌های ChatGPT، Gemini و Perplexity.",
        kicker="مشاور هوش مصنوعی ۲۴/۷ آنلاین، به زبان شما",
        h1a="نامی باشید که", h1b="هوش مصنوعی پیشنهاد می‌دهد.",
        sub="من وب‌سایت‌های آماده برای هوش مصنوعی، ایجنت‌های پذیرش هوشمند و استراتژی دیده‌شدن می‌سازم تا وقتی مشتریان از ChatGPT، Gemini یا Perplexity می‌پرسند چه کسی را استخدام کنند، پاسخ شما باشید.",
        who="رایان جواهری · مشاور هوش مصنوعی و سازنده وب‌سایت · USC · لس‌آنجلس",
        cta1="اسکن رایگان هوش مصنوعی", cta2="با مشاور هوش مصنوعی من صحبت کنید ←",
        s_eye="خدمات", s_h="آنچه برای شما می‌سازم.",
        services=[
            ("دیده‌شدن در هوش مصنوعی (LLMO)", "کسب‌وکاری باشید که ChatGPT و Gemini پیشنهاد می‌دهند.", "/ai-visibility/"),
            ("ایجنت‌های پذیرش هوشمند", "چت و صدا که ۲۴ ساعته پاسخ می‌دهند و مشتری بالقوه را به شما می‌سپارند.", "/ai-agents/"),
            ("وب‌سایت آماده برای هوش مصنوعی", "سریع، مدرن و قابل فهم برای انسان و هوش مصنوعی.", "/websites/"),
            ("برای دفاتر حقوقی", "دیده‌شدن، پذیرش، جذب نیرو و روابط عمومی.", "/law-firms/"),
        ],
        m_eye="روش کار", m_h="B.U.I.L.D.",
        steps=[("B", "پایه", "بررسی اینکه هوش مصنوعی امروز درباره شما چه می‌گوید."), ("U", "درک", "سؤال‌های واقعی مشتریان شما."), ("I", "اجرا", "وب‌سایت، اسکیما، محتوا و llms.txt."), ("L", "راه‌اندازی ایجنت", "پذیرش هوشمند در وب و تلفن."), ("D", "توسعه", "بررسی ماهانه و رشد مداوم.")],
        a_eye="درباره من", a_p="من با Siamak Consulting کار می‌کنم و LLMO و استراتژی هوش مصنوعی را مستقیماً از سیامک کلهر یاد می‌گیرم و برای مشتریان وب‌سایت و ایجنت هوش مصنوعی می‌سازم. در USC روابط عمومی و حقوق تجارت می‌خوانم.",
        faq=[
            ("LLMO چیست؟", "LLMO یعنی بهینه‌سازی برای مدل‌های زبانی بزرگ: کسب‌وکار شما را برای ChatGPT، Claude، Gemini و Perplexity قابل فهم، قابل تأیید و قابل پیشنهاد می‌کند."),
            ("ایجنت پذیرش هوشمند چه کار می‌کند؟", "به سؤال‌ها ۲۴ ساعته و به زبان بازدیدکننده پاسخ می‌دهد، نام، راه تماس و نیاز او را می‌گیرد و برای شما می‌فرستد. مشاور همین سایت یک نمونه زنده است."),
            ("هزینه چقدر است؟", "هر پروژه پس از یک تماس کوتاه قیمت‌گذاری می‌شود. نیاز خود را به مشاور هوش مصنوعی من بگویید تا برایتان پیشنهاد قیمت بفرستم."),
        ],
        c_eye="تماس", c_h="بیایید چیزی بسازیم.", c_p="درباره کسب‌وکارتان بگویید. همه پیام‌ها را می‌خوانم و شخصاً پاسخ می‌دهم.",
        f=("نام *", "ایمیل *", "شرکت", "تلفن", "به چه چیزی نیاز دارید؟ *", "ارسال برای رایان", "ممنون! شخصاً با شما تماس می‌گیرم."),
        faq_h="سؤالات متداول",
    ),
}


def build(lang):
    t = T[lang]
    path = f"/{lang}/"
    schema = {"@context": "https://schema.org", "@graph": [PERSON, {"@type": "WebPage", "url": SITE + path, "name": t["title"], "inLanguage": lang, "about": {"@id": SITE + "/#ryan"}}, faq_schema(t["faq"])]}
    html = head(t["title"], t["desc"], path, lang=lang, schema=schema)
    html += nav(lang)
    cards = "".join(f'<a class="card" href="{u}"><h3>{n}</h3><p>{d}</p></a>' for n, d, u in t["services"])
    steps = "".join(f'<div class="step"><span class="L">{L}</span><h3>{n}</h3><p>{d}</p></div>' for L, n, d in t["steps"])
    f = t["f"]
    html += f"""<main id="main">
<div class="hero-wrap"><div class="orb orb-1" data-speed="0.25"></div><div class="orb orb-2" data-speed="0.45"></div>
<header class="hero" style="grid-template-columns:1fr"><div class="hero-content" id="heroContent">
<span class="kicker"><i></i>{t["kicker"]}</span>
<h1>{t["h1a"]}<br><span class="grad">{t["h1b"]}</span></h1>
<p class="sub">{t["sub"]}</p><p class="who">{t["who"]}</p>
<div class="ctas"><a class="btn btn-dark" href="/#scan">{t["cta1"]}</a><a class="btn btn-light" href="#" data-open-agent="">{t["cta2"]}</a></div>
</div></header></div>
<section class="block alt" id="services"><div class="inner"><div class="reveal"><p class="eyebrow">{t["s_eye"]}</p><h2>{t["s_h"]}</h2></div><div class="cards stagger">{cards}</div></div></section>
<section class="block reveal" id="method"><div class="inner"><p class="eyebrow">{t["m_eye"]}</p><h2>{t["m_h"]}</h2><div class="steps stagger">{steps}</div></div></section>
<section class="block alt reveal" id="about"><div class="inner"><p class="eyebrow">{t["a_eye"]}</p><p class="lede">{t["a_p"]}</p></div></section>
<section class="block reveal" id="faq"><div class="inner"><h2>{t["faq_h"]}</h2><div class="faq">{faq_html(t["faq"])}</div></div></section>
<section class="block alt reveal" id="contact"><div class="inner scan-grid"><div><p class="eyebrow">{t["c_eye"]}</p><h2>{t["c_h"]}</h2><p class="lede">{t["c_p"]}</p><p class="lede"><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<div class="formcard"><form data-lead data-ok="{f[6]}"><div class="fgrid">
<div><label class="f" for="c-n">{f[0]}</label><input class="f-in" id="c-n" name="name" required maxlength="120"></div>
<div><label class="f" for="c-e">{f[1]}</label><input class="f-in" id="c-e" name="email" type="email" required maxlength="200"></div>
<div><label class="f" for="c-c">{f[2]}</label><input class="f-in" id="c-c" name="company" maxlength="200"></div>
<div><label class="f" for="c-p">{f[3]}</label><input class="f-in" id="c-p" name="phone" type="tel" maxlength="60"></div>
<div class="full"><label class="f" for="c-m">{f[4]}</label><textarea class="f-in" id="c-m" name="need" required maxlength="2000"></textarea></div>
</div><div class="hp" aria-hidden="true"><input name="company_url_hp" tabindex="-1" autocomplete="off"></div>
<button class="btn btn-dark" type="submit" style="margin-top:18px">{f[5]}</button><p class="f-msg" aria-live="polite"></p></form></div></div></section>
</main>
"""
    return html + tail(lang)
