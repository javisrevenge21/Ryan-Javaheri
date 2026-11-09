"""Translated homepages. Each language gets /<code>/ with the same layout.
To add a language: add it to LANGS in pages.py, add a block here, add widget strings in assets/agent.js."""
from pages import head, nav, tail, PERSON, SITE, EMAIL, faq_schema, faq_html, RTL
import portfolio

T = {}

T["es"] = dict(
    title="Ryan Javaheri — Consultor de IA, Agentes de IA y Sitios Web | Los Ángeles",
    desc="Consultor de IA en Los Ángeles: sitios web preparados para IA, agentes de admisión 24/7 y visibilidad en IA (LLMO) para que ChatGPT, Gemini y Perplexity te recomienden.",
    future="futuro abogado.", touch="Contáctame",
    kicker="Asesor de IA en línea 24/7, en tu idioma",
    h1a="Sé el nombre que", h1b="la IA recomienda.",
    sub="Construyo sitios web preparados para IA, agentes de admisión con IA y estrategia de visibilidad, para que cuando tus clientes pregunten a ChatGPT, Gemini o Perplexity a quién contratar, la respuesta seas tú.",
    who="Ryan Javaheri · Consultor de IA y desarrollador web · USC · Los Ángeles",
    cta1="Escaneo de IA gratis", cta2="Habla con mi asesor de IA →",
    s_eye="Servicios", s_h="Lo que construyo para ti.",
    services=[("Visibilidad en IA (LLMO)", "Que ChatGPT y Gemini recomienden tu negocio."),
              ("Agentes de admisión con IA", "Chat y voz que responden 24/7 y te entregan clientes potenciales."),
              ("Sitios web preparados para IA", "Rápidos, modernos y claros para personas y para la IA."),
              ("Para despachos de abogados", "Visibilidad, admisión, reclutamiento y relaciones públicas.")],
    m_eye="El método",
    steps=[("Base", "Vemos qué dice la IA de ti hoy."), ("Entender", "Las preguntas reales de tus clientes."),
           ("Implementar", "Sitio, schema, contenido y llms.txt."), ("Lanzar agentes", "Admisión con IA en web y teléfono."),
           ("Desarrollar", "Revisión mensual y crecimiento continuo.")],
    a_eye="Sobre mí",
    a_p="Trabajo con Siamak Consulting, donde aprendo LLMO y estrategia de IA directamente de Siamak Kalhor, y construyo sitios web y agentes de IA para clientes. Estudio relaciones públicas y derecho empresarial en USC.",
    faq=[("¿Qué es LLMO?", "LLMO (optimización para modelos de lenguaje) hace que tu negocio sea fácil de entender, verificar y recomendar para asistentes como ChatGPT, Claude, Gemini y Perplexity."),
         ("¿Qué hace un agente de admisión con IA?", "Responde preguntas 24/7 en el idioma del visitante, recoge su nombre, contacto y lo que necesita, y te lo envía. El asesor de este sitio es un ejemplo en vivo."),
         ("¿Cuánto cuesta?", "Cada proyecto se cotiza después de una breve llamada. Cuéntale a mi asesor de IA lo que necesitas y te envío una cotización.")],
    faq_h="Preguntas frecuentes", p_eye="Portafolio", port="Ver todo lo que he creado",
    c_eye="Contacto", c_h="Construyamos algo.", c_p="Cuéntame sobre tu negocio. Leo cada mensaje y respondo personalmente.",
    f=("Nombre *", "Correo *", "Empresa", "Teléfono", "¿Qué necesitas? *", "Enviar a Ryan", "¡Gracias! Te contactaré personalmente."),
)

T["fa"] = dict(
    title="رایان جواهری — مشاور هوش مصنوعی، ایجنت‌های هوش مصنوعی و طراحی وب‌سایت | لس‌آنجلس",
    desc="مشاور هوش مصنوعی در لس‌آنجلس: وب‌سایت‌های آماده برای هوش مصنوعی، ایجنت‌های پذیرش ۲۴ ساعته و دیده‌شدن در پاسخ‌های ChatGPT، Gemini و Perplexity.",
    future="وکیل آینده.", touch="در تماس باشید",
    kicker="مشاور هوش مصنوعی ۲۴/۷ آنلاین، به زبان شما",
    h1a="نامی باشید که", h1b="هوش مصنوعی پیشنهاد می‌دهد.",
    sub="من وب‌سایت‌های آماده برای هوش مصنوعی، ایجنت‌های پذیرش هوشمند و استراتژی دیده‌شدن می‌سازم تا وقتی مشتریان از ChatGPT، Gemini یا Perplexity می‌پرسند چه کسی را استخدام کنند، پاسخ شما باشید.",
    who="رایان جواهری · مشاور هوش مصنوعی و سازنده وب‌سایت · USC · لس‌آنجلس",
    cta1="اسکن رایگان هوش مصنوعی", cta2="با مشاور هوش مصنوعی من صحبت کنید ←",
    s_eye="خدمات", s_h="آنچه برای شما می‌سازم.",
    services=[("دیده‌شدن در هوش مصنوعی (LLMO)", "کسب‌وکاری باشید که ChatGPT و Gemini پیشنهاد می‌دهند."),
              ("ایجنت‌های پذیرش هوشمند", "چت و صدا که ۲۴ ساعته پاسخ می‌دهند و مشتری بالقوه را به شما می‌سپارند."),
              ("وب‌سایت آماده برای هوش مصنوعی", "سریع، مدرن و قابل فهم برای انسان و هوش مصنوعی."),
              ("برای دفاتر حقوقی", "دیده‌شدن، پذیرش، جذب نیرو و روابط عمومی.")],
    m_eye="روش کار",
    steps=[("پایه", "بررسی اینکه هوش مصنوعی امروز درباره شما چه می‌گوید."), ("درک", "سؤال‌های واقعی مشتریان شما."),
           ("اجرا", "وب‌سایت، اسکیما، محتوا و llms.txt."), ("راه‌اندازی ایجنت", "پذیرش هوشمند در وب و تلفن."),
           ("توسعه", "بررسی ماهانه و رشد مداوم.")],
    a_eye="درباره من",
    a_p="من با Siamak Consulting کار می‌کنم و LLMO و استراتژی هوش مصنوعی را مستقیماً از سیامک کلهر یاد می‌گیرم و برای مشتریان وب‌سایت و ایجنت هوش مصنوعی می‌سازم. در USC روابط عمومی و حقوق تجارت می‌خوانم.",
    faq=[("LLMO چیست؟", "LLMO یعنی بهینه‌سازی برای مدل‌های زبانی بزرگ: کسب‌وکار شما را برای ChatGPT، Claude، Gemini و Perplexity قابل فهم، قابل تأیید و قابل پیشنهاد می‌کند."),
         ("ایجنت پذیرش هوشمند چه کار می‌کند؟", "به سؤال‌ها ۲۴ ساعته و به زبان بازدیدکننده پاسخ می‌دهد، نام، راه تماس و نیاز او را می‌گیرد و برای شما می‌فرستد. مشاور همین سایت یک نمونه زنده است."),
         ("هزینه چقدر است؟", "هر پروژه پس از یک تماس کوتاه قیمت‌گذاری می‌شود. نیاز خود را به مشاور هوش مصنوعی من بگویید تا برایتان پیشنهاد قیمت بفرستم.")],
    faq_h="سؤالات متداول", p_eye="نمونه‌کارها", port="همه کارهایم را ببینید",
    c_eye="تماس", c_h="بیایید چیزی بسازیم.", c_p="درباره کسب‌وکارتان بگویید. همه پیام‌ها را می‌خوانم و شخصاً پاسخ می‌دهم.",
    f=("نام *", "ایمیل *", "شرکت", "تلفن", "به چه چیزی نیاز دارید؟ *", "ارسال برای رایان", "ممنون! شخصاً با شما تماس می‌گیرم."),
)

T["he"] = dict(
    title="ריאן ג'ואהרי — יועץ בינה מלאכותית, סוכני AI ואתרים | לוס אנג'לס",
    desc="יועץ בינה מלאכותית בלוס אנג'לס: אתרים מוכנים ל-AI, סוכני קליטה 24/7 ונראות בתשובות של ChatGPT, Gemini ו-Perplexity.",
    future="עורך דין לעתיד.", touch="צרו קשר",
    kicker="יועץ AI זמין 24/7, בשפה שלכם",
    h1a="היו השם", h1b="שה-AI ממליץ עליו.",
    sub="אני בונה אתרים מוכנים ל-AI, סוכני קליטה חכמים ואסטרטגיית נראות, כך שכשלקוחות שואלים את ChatGPT, Gemini או Perplexity את מי לשכור, התשובה היא אתם.",
    who="ריאן ג'ואהרי · יועץ AI ובונה אתרים · USC · לוס אנג'לס",
    cta1="סריקת AI חינם", cta2="דברו עם יועץ ה-AI שלי ←",
    s_eye="שירותים", s_h="מה אני בונה בשבילכם.",
    services=[("נראות ב-AI (LLMO)", "היו העסק ש-ChatGPT ו-Gemini ממליצים עליו."),
              ("סוכני קליטה חכמים", "צ'אט וקול שעונים 24/7 ומעבירים אליכם את הפנייה."),
              ("אתרים מוכנים ל-AI", "מהירים, מודרניים וברורים לאנשים ול-AI."),
              ("למשרדי עורכי דין", "נראות, קליטת פניות, גיוס ויחסי ציבור.")],
    m_eye="השיטה",
    steps=[("בסיס", "בודקים מה ה-AI אומר עליכם היום."), ("הבנה", "השאלות האמיתיות של הלקוחות שלכם."),
           ("יישום", "אתר, סכמה, תוכן ו-llms.txt."), ("השקת סוכנים", "קליטה חכמה באתר ובטלפון."),
           ("פיתוח", "בדיקה חודשית וצמיחה מתמדת.")],
    a_eye="עליי",
    a_p="אני עובד עם Siamak Consulting, לומד LLMO ואסטרטגיית AI ישירות מסיאמק קלהור, ובונה אתרים וסוכני AI ללקוחות. אני לומד יחסי ציבור ומשפט עסקי ב-USC.",
    faq=[("מה זה LLMO?", "LLMO (אופטימיזציה למודלי שפה גדולים) הופכת את העסק שלכם לקל להבנה, לאימות ולהמלצה עבור ChatGPT, Claude, Gemini ו-Perplexity."),
         ("מה עושה סוכן קליטה חכם?", "הוא עונה לשאלות 24/7 בשפת המבקר, אוסף שם, פרטי קשר ומה הוא צריך, ושולח לכם. היועץ באתר הזה הוא דוגמה חיה."),
         ("כמה זה עולה?", "כל פרויקט מתומחר אחרי שיחה קצרה. ספרו ליועץ ה-AI שלי מה אתם צריכים ואשלח הצעת מחיר.")],
    faq_h="שאלות נפוצות", p_eye="תיק עבודות", port="כל מה שבניתי",
    c_eye="צור קשר", c_h="בואו נבנה משהו.", c_p="ספרו לי על העסק שלכם. אני קורא כל הודעה ועונה אישית.",
    f=("שם *", "אימייל *", "חברה", "טלפון", "מה אתם צריכים? *", "שליחה לריאן", "תודה! אחזור אליכם אישית."),
)

T["ar"] = dict(
    title="رايان جواهري — مستشار ذكاء اصطناعي ووكلاء ذكاء اصطناعي ومواقع ويب | لوس أنجلوس",
    desc="مستشار ذكاء اصطناعي في لوس أنجلوس: مواقع جاهزة للذكاء الاصطناعي، ووكلاء استقبال على مدار الساعة، وظهور في إجابات ChatGPT وGemini وPerplexity.",
    future="محامي المستقبل.", touch="تواصل معي",
    kicker="مستشار ذكاء اصطناعي متاح 24/7 بلغتك",
    h1a="كن الاسم", h1b="الذي يوصي به الذكاء الاصطناعي.",
    sub="أبني مواقع جاهزة للذكاء الاصطناعي ووكلاء استقبال أذكياء واستراتيجية ظهور، حتى عندما يسأل العملاء ChatGPT أو Gemini أو Perplexity عمّن يوظفون، تكون أنت الإجابة.",
    who="رايان جواهري · مستشار ذكاء اصطناعي ومطوّر مواقع · USC · لوس أنجلوس",
    cta1="فحص مجاني بالذكاء الاصطناعي", cta2="تحدث مع مستشاري الذكي ←",
    s_eye="الخدمات", s_h="ما أبنيه لك.",
    services=[("الظهور في الذكاء الاصطناعي (LLMO)", "كن النشاط التجاري الذي يوصي به ChatGPT وGemini."),
              ("وكلاء الاستقبال الأذكياء", "دردشة وصوت يجيبان على مدار الساعة ويسلّمانك العميل المحتمل."),
              ("مواقع جاهزة للذكاء الاصطناعي", "سريعة وعصرية وواضحة للناس وللذكاء الاصطناعي."),
              ("لمكاتب المحاماة", "الظهور والاستقبال والتوظيف والعلاقات العامة.")],
    m_eye="المنهج",
    steps=[("الأساس", "نرى ماذا يقول الذكاء الاصطناعي عنك اليوم."), ("الفهم", "الأسئلة الحقيقية لعملائك."),
           ("التنفيذ", "الموقع والمخطط والمحتوى وllms.txt."), ("إطلاق الوكلاء", "استقبال ذكي على الموقع والهاتف."),
           ("التطوير", "فحص شهري ونمو مستمر.")],
    a_eye="عني",
    a_p="أعمل مع Siamak Consulting، وأتعلم LLMO واستراتيجية الذكاء الاصطناعي مباشرة من سيامك كلهر، وأبني مواقع ووكلاء ذكاء اصطناعي للعملاء. أدرس العلاقات العامة وقانون الأعمال في جامعة USC.",
    faq=[("ما هو LLMO؟", "LLMO (تحسين نماذج اللغة الكبيرة) يجعل نشاطك التجاري سهل الفهم والتحقق والتوصية من ChatGPT وClaude وGemini وPerplexity."),
         ("ماذا يفعل وكيل الاستقبال الذكي؟", "يجيب عن الأسئلة على مدار الساعة بلغة الزائر، ويجمع الاسم ووسيلة التواصل وما يحتاجه، ثم يرسلها إليك. المستشار في هذا الموقع مثال حي."),
         ("كم التكلفة؟", "يُسعَّر كل مشروع بعد مكالمة قصيرة. أخبر مستشاري الذكي بما تحتاجه وسأرسل لك عرض سعر.")],
    faq_h="الأسئلة الشائعة", p_eye="الأعمال", port="كل ما بنيته",
    c_eye="تواصل", c_h="لنبنِ شيئًا معًا.", c_p="أخبرني عن نشاطك التجاري. أقرأ كل رسالة وأرد شخصيًا.",
    f=("الاسم *", "البريد الإلكتروني *", "الشركة", "الهاتف", "ماذا تحتاج؟ *", "أرسل إلى رايان", "شكرًا! سأتواصل معك شخصيًا."),
)

T["zh"] = dict(
    title="Ryan Javaheri — AI 顾问、AI 智能体与网站建设 | 洛杉矶",
    desc="洛杉矶 AI 顾问：打造适配 AI 的网站、全天候 AI 接待智能体，并提升你在 ChatGPT、Gemini 和 Perplexity 回答中的曝光。",
    future="未来的律师。", touch="联系我",
    kicker="AI 顾问 24/7 在线，支持你的语言",
    h1a="成为", h1b="AI 推荐的名字。",
    sub="我为你打造适配 AI 的网站、AI 接待智能体和 AI 曝光策略，让客户在问 ChatGPT、Gemini 或 Perplexity 该找谁时，答案就是你。",
    who="Ryan Javaheri · AI 顾问与网站开发者 · 南加州大学 · 洛杉矶",
    cta1="免费 AI 扫描", cta2="和我的 AI 顾问聊聊 →",
    s_eye="服务", s_h="我为你打造什么。",
    services=[("AI 曝光（LLMO）", "成为 ChatGPT 和 Gemini 推荐的商家。"),
              ("AI 接待智能体", "文字与语音全天候应答，并把潜在客户交给你。"),
              ("适配 AI 的网站", "快速、现代，人和 AI 都能看懂。"),
              ("律师事务所", "曝光、接待、招聘与公关。")],
    m_eye="方法",
    steps=[("基线", "了解 AI 现在如何描述你。"), ("理解", "客户真正会问的问题。"),
           ("实施", "网站、结构化数据、内容与 llms.txt。"), ("上线智能体", "网站和电话上的 AI 接待。"),
           ("发展", "每月复查，持续增长。")],
    a_eye="关于我",
    a_p="我在 Siamak Consulting 工作，直接向 Siamak Kalhor 学习 LLMO 和 AI 策略，并为客户打造网站和 AI 智能体。我在南加州大学（USC）学习公共关系和商法。",
    faq=[("什么是 LLMO？", "LLMO（大语言模型优化）让你的业务更容易被 ChatGPT、Claude、Gemini 和 Perplexity 理解、核实和推荐。"),
         ("AI 接待智能体能做什么？", "它以访客的语言全天候回答问题，收集姓名、联系方式和需求，并发送给你。本网站的顾问就是一个实时示例。"),
         ("费用是多少？", "每个项目在简短沟通后报价。告诉我的 AI 顾问你的需求，我会发送报价。")],
    faq_h="常见问题", p_eye="作品集", port="查看我的全部作品",
    c_eye="联系", c_h="一起打造点什么吧。", c_p="介绍一下你的业务。每条消息我都会亲自阅读并回复。",
    f=("姓名 *", "邮箱 *", "公司", "电话", "你需要什么？ *", "发送给 Ryan", "谢谢！我会亲自与你联系。"),
)

T["ko"] = dict(
    title="라이언 자바헤리 — AI 컨설턴트, AI 에이전트 & 웹사이트 | 로스앤젤레스",
    desc="로스앤젤레스 AI 컨설턴트: AI 친화적 웹사이트, 24시간 AI 상담 에이전트, ChatGPT·Gemini·Perplexity 답변 노출 전략.",
    future="미래의 변호사.", touch="연락하기",
    kicker="AI 상담사 24시간 온라인, 원하는 언어로",
    h1a="AI가 추천하는", h1b="이름이 되세요.",
    sub="AI 친화적 웹사이트, AI 상담 에이전트, AI 노출 전략을 만들어 고객이 ChatGPT, Gemini, Perplexity에 누구에게 맡길지 물을 때 그 답이 당신이 되도록 합니다.",
    who="라이언 자바헤리 · AI 컨설턴트 & 웹 빌더 · USC · 로스앤젤레스",
    cta1="무료 AI 스캔", cta2="AI 상담사와 대화하기 →",
    s_eye="서비스", s_h="제가 만들어 드리는 것.",
    services=[("AI 노출 (LLMO)", "ChatGPT와 Gemini가 추천하는 비즈니스가 되세요."),
              ("AI 상담 에이전트", "채팅과 음성으로 24시간 응답하고 잠재 고객을 전달합니다."),
              ("AI 친화적 웹사이트", "빠르고 현대적이며 사람과 AI 모두 이해하기 쉬운 사이트."),
              ("로펌을 위한 서비스", "노출, 상담 접수, 채용, PR.")],
    m_eye="방법론",
    steps=[("기준점", "지금 AI가 당신에 대해 뭐라고 하는지 확인."), ("이해", "고객의 실제 질문 파악."),
           ("실행", "웹사이트, 스키마, 콘텐츠, llms.txt."), ("에이전트 출시", "웹과 전화에서 AI 상담."),
           ("발전", "매월 점검과 꾸준한 성장.")],
    a_eye="소개",
    a_p="Siamak Consulting에서 일하며 시아막 칼호르에게 LLMO와 AI 전략을 직접 배우고, 고객을 위한 웹사이트와 AI 에이전트를 만듭니다. USC에서 홍보학과 비즈니스 법을 공부하고 있습니다.",
    faq=[("LLMO란 무엇인가요?", "LLMO(대규모 언어 모델 최적화)는 ChatGPT, Claude, Gemini, Perplexity가 당신의 비즈니스를 쉽게 이해하고 확인하고 추천하도록 만드는 작업입니다."),
         ("AI 상담 에이전트는 무엇을 하나요?", "방문자의 언어로 24시간 질문에 답하고 이름, 연락처, 필요한 내용을 받아 전달합니다. 이 사이트의 상담사가 실제 예시입니다."),
         ("비용은 얼마인가요?", "모든 프로젝트는 짧은 통화 후 견적을 드립니다. AI 상담사에게 필요한 것을 알려 주시면 견적을 보내드립니다.")],
    faq_h="자주 묻는 질문", p_eye="포트폴리오", port="제가 만든 모든 작업 보기",
    c_eye="연락", c_h="함께 만들어 봐요.", c_p="비즈니스에 대해 알려 주세요. 모든 메시지를 직접 읽고 답장합니다.",
    f=("이름 *", "이메일 *", "회사", "전화번호", "무엇이 필요하신가요? *", "라이언에게 보내기", "감사합니다! 직접 연락드리겠습니다."),
)

T["ja"] = dict(
    title="ライアン・ジャヴァヘリ — AIコンサルタント・AIエージェント・Web制作 | ロサンゼルス",
    desc="ロサンゼルスのAIコンサルタント。AI対応のWebサイト、24時間対応のAI受付エージェント、ChatGPT・Gemini・Perplexityでの露出を支援します。",
    future="未来の弁護士。", touch="お問い合わせ",
    kicker="AIアドバイザーが24時間、あなたの言語で対応",
    h1a="AIが勧める", h1b="名前になろう。",
    sub="AI対応のWebサイト、AI受付エージェント、AI露出戦略をつくり、お客様がChatGPT、Gemini、Perplexityに誰に頼むべきか尋ねたとき、その答えがあなたになるようにします。",
    who="ライアン・ジャヴァヘリ · AIコンサルタント & Web制作 · USC · ロサンゼルス",
    cta1="無料AIスキャン", cta2="AIアドバイザーと話す →",
    s_eye="サービス", s_h="あなたのためにつくるもの。",
    services=[("AI露出（LLMO）", "ChatGPTやGeminiが推薦するビジネスに。"),
              ("AI受付エージェント", "チャットと音声で24時間対応し、見込み客をお届けします。"),
              ("AI対応Webサイト", "高速でモダン、人にもAIにも分かりやすいサイト。"),
              ("法律事務所向け", "露出、受付、採用、PR。")],
    m_eye="メソッド",
    steps=[("現状把握", "AIが今あなたをどう語るかを確認。"), ("理解", "お客様の本当の質問を把握。"),
           ("実装", "サイト、スキーマ、コンテンツ、llms.txt。"), ("エージェント導入", "Webと電話でのAI受付。"),
           ("成長", "毎月の確認と継続的な改善。")],
    a_eye="私について",
    a_p="Siamak Consultingで、シアマク・カルホールから直接LLMOとAI戦略を学びながら、お客様のWebサイトやAIエージェントを制作しています。USCで広報とビジネス法を学んでいます。",
    faq=[("LLMOとは？", "LLMO（大規模言語モデル最適化）は、ChatGPT、Claude、Gemini、Perplexityがあなたのビジネスを理解・確認・推薦しやすくする取り組みです。"),
         ("AI受付エージェントは何をしますか？", "訪問者の言語で24時間質問に答え、名前・連絡先・ご要望を受け取ってあなたに届けます。このサイトのアドバイザーが実例です。"),
         ("費用は？", "各プロジェクトは短い通話の後にお見積もりします。AIアドバイザーにご要望を伝えていただければ、お見積もりをお送りします。")],
    faq_h="よくある質問", p_eye="ポートフォリオ", port="これまでの制作実績を見る",
    c_eye="お問い合わせ", c_h="一緒につくりましょう。", c_p="あなたのビジネスについて教えてください。すべてのメッセージを読み、私が直接返信します。",
    f=("お名前 *", "メールアドレス *", "会社名", "電話番号", "ご要望 *", "ライアンに送信", "ありがとうございます！私から直接ご連絡します。"),
)

T["fr"] = dict(
    title="Ryan Javaheri — Consultant IA, agents IA et sites web | Los Angeles",
    desc="Consultant IA à Los Angeles : sites web prêts pour l'IA, agents d'accueil IA 24h/24 et visibilité dans les réponses de ChatGPT, Gemini et Perplexity.",
    future="futur avocat.", touch="Me contacter",
    kicker="Conseiller IA en ligne 24h/24, dans votre langue",
    h1a="Soyez le nom", h1b="que l'IA recommande.",
    sub="Je crée des sites web prêts pour l'IA, des agents d'accueil IA et des stratégies de visibilité, pour que lorsque vos clients demandent à ChatGPT, Gemini ou Perplexity qui choisir, la réponse soit vous.",
    who="Ryan Javaheri · Consultant IA et créateur de sites · USC · Los Angeles",
    cta1="Scan IA gratuit", cta2="Parler à mon conseiller IA →",
    s_eye="Services", s_h="Ce que je construis pour vous.",
    services=[("Visibilité IA (LLMO)", "Devenez l'entreprise que ChatGPT et Gemini recommandent."),
              ("Agents d'accueil IA", "Chat et voix qui répondent 24h/24 et vous transmettent le contact."),
              ("Sites prêts pour l'IA", "Rapides, modernes, clairs pour les humains et pour l'IA."),
              ("Cabinets d'avocats", "Visibilité, accueil, recrutement et relations presse.")],
    m_eye="La méthode",
    steps=[("Base", "Voir ce que l'IA dit de vous aujourd'hui."), ("Comprendre", "Les vraies questions de vos clients."),
           ("Implémenter", "Site, schéma, contenu et llms.txt."), ("Lancer les agents", "Accueil IA sur le web et au téléphone."),
           ("Développer", "Vérification mensuelle et croissance continue.")],
    a_eye="À propos",
    a_p="Je travaille avec Siamak Consulting, où j'apprends le LLMO et la stratégie IA directement auprès de Siamak Kalhor, et je crée des sites et des agents IA pour les clients. J'étudie les relations publiques et le droit des affaires à USC.",
    faq=[("Qu'est-ce que le LLMO ?", "Le LLMO (optimisation pour les grands modèles de langage) rend votre entreprise facile à comprendre, vérifier et recommander pour ChatGPT, Claude, Gemini et Perplexity."),
         ("Que fait un agent d'accueil IA ?", "Il répond aux questions 24h/24 dans la langue du visiteur, recueille son nom, ses coordonnées et son besoin, puis vous les envoie. Le conseiller de ce site en est un exemple en direct."),
         ("Combien ça coûte ?", "Chaque projet fait l'objet d'un devis après un court appel. Dites à mon conseiller IA ce dont vous avez besoin et je vous enverrai un devis.")],
    faq_h="Questions fréquentes", p_eye="Portfolio", port="Voir tout ce que j'ai créé",
    c_eye="Contact", c_h="Construisons quelque chose.", c_p="Parlez-moi de votre entreprise. Je lis chaque message et je réponds personnellement.",
    f=("Nom *", "E-mail *", "Entreprise", "Téléphone", "De quoi avez-vous besoin ? *", "Envoyer à Ryan", "Merci ! Je vous recontacte personnellement."),
)

T["pt"] = dict(
    title="Ryan Javaheri — Consultor de IA, agentes de IA e sites | Los Angeles",
    desc="Consultor de IA em Los Angeles: sites prontos para IA, agentes de atendimento com IA 24/7 e visibilidade nas respostas do ChatGPT, Gemini e Perplexity.",
    future="futuro advogado.", touch="Fale comigo",
    kicker="Consultor de IA online 24/7, no seu idioma",
    h1a="Seja o nome", h1b="que a IA recomenda.",
    sub="Eu crio sites prontos para IA, agentes de atendimento com IA e estratégias de visibilidade, para que, quando seus clientes perguntarem ao ChatGPT, Gemini ou Perplexity quem contratar, a resposta seja você.",
    who="Ryan Javaheri · Consultor de IA e criador de sites · USC · Los Angeles",
    cta1="Análise de IA grátis", cta2="Fale com meu consultor de IA →",
    s_eye="Serviços", s_h="O que eu crio para você.",
    services=[("Visibilidade em IA (LLMO)", "Seja a empresa que o ChatGPT e o Gemini recomendam."),
              ("Agentes de atendimento com IA", "Chat e voz que respondem 24/7 e entregam o contato para você."),
              ("Sites prontos para IA", "Rápidos, modernos e claros para pessoas e para a IA."),
              ("Para escritórios de advocacia", "Visibilidade, atendimento, recrutamento e relações públicas.")],
    m_eye="O método",
    steps=[("Base", "Ver o que a IA diz sobre você hoje."), ("Entender", "As perguntas reais dos seus clientes."),
           ("Implementar", "Site, schema, conteúdo e llms.txt."), ("Lançar agentes", "Atendimento com IA na web e no telefone."),
           ("Desenvolver", "Revisão mensal e crescimento contínuo.")],
    a_eye="Sobre mim",
    a_p="Trabalho com a Siamak Consulting, onde aprendo LLMO e estratégia de IA diretamente com Siamak Kalhor, e crio sites e agentes de IA para clientes. Estudo relações públicas e direito empresarial na USC.",
    faq=[("O que é LLMO?", "LLMO (otimização para grandes modelos de linguagem) torna sua empresa fácil de entender, verificar e recomendar pelo ChatGPT, Claude, Gemini e Perplexity."),
         ("O que faz um agente de atendimento com IA?", "Ele responde perguntas 24/7 no idioma do visitante, coleta nome, contato e necessidade, e envia tudo para você. O consultor deste site é um exemplo ao vivo."),
         ("Quanto custa?", "Cada projeto é orçado após uma ligação curta. Conte ao meu consultor de IA o que você precisa e eu envio um orçamento.")],
    faq_h="Perguntas frequentes", p_eye="Portfólio", port="Ver tudo o que eu criei",
    c_eye="Contato", c_h="Vamos construir algo.", c_p="Conte sobre o seu negócio. Leio cada mensagem e respondo pessoalmente.",
    f=("Nome *", "E-mail *", "Empresa", "Telefone", "Do que você precisa? *", "Enviar para Ryan", "Obrigado! Vou entrar em contato pessoalmente."),
)

T["ru"] = dict(
    title="Райан Джавахери — ИИ-консультант, ИИ-агенты и сайты | Лос-Анджелес",
    desc="ИИ-консультант в Лос-Анджелесе: сайты, готовые к ИИ, круглосуточные ИИ-агенты для приёма заявок и видимость в ответах ChatGPT, Gemini и Perplexity.",
    future="будущий юрист.", touch="Связаться",
    kicker="ИИ-консультант онлайн 24/7, на вашем языке",
    h1a="Станьте именем,", h1b="которое советует ИИ.",
    sub="Я создаю сайты, готовые к ИИ, ИИ-агентов для приёма заявок и стратегии видимости, чтобы, когда клиенты спрашивают ChatGPT, Gemini или Perplexity, к кому обратиться, ответом были вы.",
    who="Райан Джавахери · ИИ-консультант и веб-разработчик · USC · Лос-Анджелес",
    cta1="Бесплатный ИИ-анализ", cta2="Поговорить с моим ИИ-консультантом →",
    s_eye="Услуги", s_h="Что я создаю для вас.",
    services=[("Видимость в ИИ (LLMO)", "Станьте компанией, которую рекомендуют ChatGPT и Gemini."),
              ("ИИ-агенты для приёма заявок", "Чат и голос, которые отвечают 24/7 и передают вам клиента."),
              ("Сайты, готовые к ИИ", "Быстрые, современные, понятные людям и ИИ."),
              ("Для юридических фирм", "Видимость, приём заявок, подбор кадров и PR.")],
    m_eye="Метод",
    steps=[("Отправная точка", "Что ИИ говорит о вас сегодня."), ("Понимание", "Реальные вопросы ваших клиентов."),
           ("Внедрение", "Сайт, разметка, контент и llms.txt."), ("Запуск агентов", "ИИ-приём заявок на сайте и по телефону."),
           ("Развитие", "Ежемесячная проверка и постоянный рост.")],
    a_eye="Обо мне",
    a_p="Я работаю с Siamak Consulting, где изучаю LLMO и ИИ-стратегию напрямую у Сиамака Калхора, и создаю сайты и ИИ-агентов для клиентов. Изучаю связи с общественностью и деловое право в USC.",
    faq=[("Что такое LLMO?", "LLMO (оптимизация под большие языковые модели) делает ваш бизнес понятным, проверяемым и рекомендуемым для ChatGPT, Claude, Gemini и Perplexity."),
         ("Что делает ИИ-агент для приёма заявок?", "Он круглосуточно отвечает на вопросы на языке посетителя, собирает имя, контакты и запрос и передаёт их вам. Консультант на этом сайте — живой пример."),
         ("Сколько это стоит?", "Стоимость каждого проекта рассчитывается после короткого звонка. Расскажите моему ИИ-консультанту, что вам нужно, и я пришлю предложение.")],
    faq_h="Частые вопросы", p_eye="Портфолио", port="Все мои работы",
    c_eye="Контакты", c_h="Давайте создадим что-нибудь.", c_p="Расскажите о своём бизнесе. Я читаю каждое сообщение и отвечаю лично.",
    f=("Имя *", "Эл. почта *", "Компания", "Телефон", "Что вам нужно? *", "Отправить Райану", "Спасибо! Я свяжусь с вами лично."),
)

T["hy"] = dict(
    title="Ռայան Ջավահերի — ԱԲ խորհրդատու, ԱԲ գործակալներ և կայքեր | Լոս Անջելես",
    desc="ԱԲ խորհրդատու Լոս Անջելեսում. ԱԲ-ի համար պատրաստ կայքեր, 24/7 ԱԲ ընդունման գործակալներ և տեսանելիություն ChatGPT-ի, Gemini-ի և Perplexity-ի պատասխաններում։",
    future="ապագա իրավաբան։", touch="Կապ հաստատել",
    kicker="ԱԲ խորհրդատուն առցանց է 24/7, ձեր լեզվով",
    h1a="Եղեք այն անունը,", h1b="որը ԱԲ-ն խորհուրդ է տալիս։",
    sub="Ես ստեղծում եմ ԱԲ-ի համար պատրաստ կայքեր, ԱԲ ընդունման գործակալներ և տեսանելիության ռազմավարություն, որպեսզի երբ հաճախորդները ChatGPT-ին, Gemini-ին կամ Perplexity-ին հարցնեն՝ ում դիմել, պատասխանը լինեք դուք։",
    who="Ռայան Ջավահերի · ԱԲ խորհրդատու և կայքերի ստեղծող · USC · Լոս Անջելես",
    cta1="Անվճար ԱԲ ստուգում", cta2="Խոսեք իմ ԱԲ խորհրդատուի հետ →",
    s_eye="Ծառայություններ", s_h="Ինչ եմ ստեղծում ձեզ համար։",
    services=[("Տեսանելիություն ԱԲ-ում (LLMO)", "Դարձեք այն բիզնեսը, որը ChatGPT-ն ու Gemini-ն խորհուրդ են տալիս։"),
              ("ԱԲ ընդունման գործակալներ", "Չատ և ձայն, որոնք պատասխանում են 24/7 և հաճախորդին փոխանցում են ձեզ։"),
              ("ԱԲ-ի համար պատրաստ կայքեր", "Արագ, ժամանակակից, հասկանալի մարդկանց և ԱԲ-ի համար։"),
              ("Իրավաբանական ընկերությունների համար", "Տեսանելիություն, ընդունում, հավաքագրում և PR։")],
    m_eye="Մեթոդը",
    steps=[("Ելակետ", "Տեսնել, թե ինչ է ԱԲ-ն ասում ձեր մասին այսօր։"), ("Հասկանալ", "Ձեր հաճախորդների իրական հարցերը։"),
           ("Իրականացնել", "Կայք, սխեմա, բովանդակություն և llms.txt։"), ("Գործարկել գործակալներ", "ԱԲ ընդունում կայքում և հեռախոսով։"),
           ("Զարգացնել", "Ամսական ստուգում և կայուն աճ։")],
    a_eye="Իմ մասին",
    a_p="Ես աշխատում եմ Siamak Consulting-ի հետ, որտեղ LLMO և ԱԲ ռազմավարություն եմ սովորում անմիջապես Սիամակ Քալհորից, և հաճախորդների համար ստեղծում եմ կայքեր ու ԱԲ գործակալներ։ USC-ում սովորում եմ հասարակայնության հետ կապեր և բիզնես իրավունք։",
    faq=[("Ի՞նչ է LLMO-ն", "LLMO-ն (մեծ լեզվական մոդելների օպտիմալացում) ձեր բիզնեսը դարձնում է հեշտ հասկանալի, ստուգելի և խորհուրդ տրվող ChatGPT-ի, Claude-ի, Gemini-ի և Perplexity-ի համար։"),
         ("Ի՞նչ է անում ԱԲ ընդունման գործակալը", "Այն 24/7 պատասխանում է հարցերին այցելուի լեզվով, հավաքում է անունը, կոնտակտները և կարիքը ու ուղարկում ձեզ։ Այս կայքի խորհրդատուն կենդանի օրինակ է։"),
         ("Որքա՞ն արժե", "Յուրաքանչյուր նախագծի գինը որոշվում է կարճ զանգից հետո։ Ասեք իմ ԱԲ խորհրդատուին, թե ինչ է ձեզ պետք, և ես կուղարկեմ առաջարկ։")],
    faq_h="Հաճախ տրվող հարցեր", p_eye="Պորտֆոլիո", port="Տեսնել իմ բոլոր աշխատանքները",
    c_eye="Կապ", c_h="Եկեք ինչ-որ բան ստեղծենք։", c_p="Պատմեք ձեր բիզնեսի մասին։ Ես կարդում եմ յուրաքանչյուր հաղորդագրություն և անձամբ պատասխանում։",
    f=("Անուն *", "Էլ. փոստ *", "Ընկերություն", "Հեռախոս", "Ի՞նչ է ձեզ պետք *", "Ուղարկել Ռայանին", "Շնորհակալություն։ Անձամբ կկապվեմ ձեզ հետ։"),
)

T["hi"] = dict(
    title="रयान जवाहेरी — AI सलाहकार, AI एजेंट और वेबसाइट | लॉस एंजेलिस",
    desc="लॉस एंजेलिस के AI सलाहकार: AI-तैयार वेबसाइटें, 24/7 AI इनटेक एजेंट और ChatGPT, Gemini व Perplexity के जवाबों में आपकी पहचान।",
    future="भावी वकील।", touch="संपर्क करें",
    kicker="AI सलाहकार 24/7 ऑनलाइन, आपकी भाषा में",
    h1a="वह नाम बनिए", h1b="जिसकी AI सिफ़ारिश करे।",
    sub="मैं AI-तैयार वेबसाइटें, AI इनटेक एजेंट और AI विज़िबिलिटी रणनीति बनाता हूँ, ताकि जब ग्राहक ChatGPT, Gemini या Perplexity से पूछें कि किसे चुनें, तो जवाब आप हों।",
    who="रयान जवाहेरी · AI सलाहकार और वेब बिल्डर · USC · लॉस एंजेलिस",
    cta1="मुफ़्त AI स्कैन", cta2="मेरे AI सलाहकार से बात करें →",
    s_eye="सेवाएँ", s_h="मैं आपके लिए क्या बनाता हूँ।",
    services=[("AI विज़िबिलिटी (LLMO)", "वह व्यवसाय बनिए जिसकी ChatGPT और Gemini सिफ़ारिश करें।"),
              ("AI इनटेक एजेंट", "चैट और आवाज़ जो 24/7 जवाब दें और लीड आप तक पहुँचाएँ।"),
              ("AI-तैयार वेबसाइटें", "तेज़, आधुनिक और इंसानों व AI दोनों के लिए स्पष्ट।"),
              ("लॉ फ़र्म के लिए", "विज़िबिलिटी, इनटेक, भर्ती और PR।")],
    m_eye="तरीका",
    steps=[("आधार", "देखें कि आज AI आपके बारे में क्या कहता है।"), ("समझ", "आपके ग्राहकों के असली सवाल।"),
           ("अमल", "वेबसाइट, स्कीमा, कंटेंट और llms.txt।"), ("एजेंट लॉन्च", "वेब और फ़ोन पर AI इनटेक।"),
           ("विकास", "हर महीने जाँच और लगातार बढ़त।")],
    a_eye="मेरे बारे में",
    a_p="मैं Siamak Consulting के साथ काम करता हूँ, जहाँ सियामक कलहोर से सीधे LLMO और AI रणनीति सीख रहा हूँ, और ग्राहकों के लिए वेबसाइटें व AI एजेंट बनाता हूँ। मैं USC में जनसंपर्क और व्यावसायिक क़ानून पढ़ रहा हूँ।",
    faq=[("LLMO क्या है?", "LLMO (लार्ज लैंग्वेज मॉडल ऑप्टिमाइज़ेशन) आपके व्यवसाय को ChatGPT, Claude, Gemini और Perplexity के लिए समझने, जाँचने और सिफ़ारिश करने में आसान बनाता है।"),
         ("AI इनटेक एजेंट क्या करता है?", "यह विज़िटर की भाषा में 24/7 सवालों के जवाब देता है, नाम, संपर्क और ज़रूरत लेता है और आपको भेजता है। इस साइट का सलाहकार इसका जीता-जागता उदाहरण है।"),
         ("कितना ख़र्च आता है?", "हर प्रोजेक्ट की क़ीमत एक छोटी कॉल के बाद तय होती है। मेरे AI सलाहकार को अपनी ज़रूरत बताइए, मैं कोटेशन भेजूँगा।")],
    faq_h="अक्सर पूछे जाने वाले सवाल", p_eye="पोर्टफ़ोलियो", port="मेरा सारा काम देखें",
    c_eye="संपर्क", c_h="चलिए कुछ बनाते हैं।", c_p="अपने व्यवसाय के बारे में बताइए। मैं हर संदेश पढ़ता हूँ और ख़ुद जवाब देता हूँ।",
    f=("नाम *", "ईमेल *", "कंपनी", "फ़ोन", "आपको क्या चाहिए? *", "रयान को भेजें", "धन्यवाद! मैं ख़ुद आपसे संपर्क करूँगा।"),
)

URLS = ["/ai-visibility/", "/ai-agents/", "/websites/", "/law-firms/"]


def build(lang, html_lang):
    t = T[lang]
    path = f"/{lang}/"
    schema = {"@context": "https://schema.org", "@graph": [PERSON, {"@type": "WebPage", "url": SITE + path, "name": t["title"], "inLanguage": html_lang, "about": {"@id": SITE + "/#ryan"}}, faq_schema(t["faq"])]}
    html = head(t["title"], t["desc"], path, lang=html_lang, schema=schema)
    html += nav(lang)
    cards = "".join(f'<a class="card" href="{u}"><h3>{n}</h3><p>{d}</p></a>' for (n, d), u in zip(t["services"], URLS))
    steps = "".join(f'<div class="step"><span class="L">{L}</span><h3>{n}</h3><p>{d}</p></div>' for L, (n, d) in zip("BUILD", t["steps"]))
    f = t["f"]
    html += f"""<main id="main">
<div class="intro-wrap">
<div class="orb orb-1" data-speed="0.25"></div><div class="orb orb-2" data-speed="0.45"></div>
<header class="intro"><div class="intro-content" id="heroContent">
<h1 data-split dir="ltr">Ryan Javaheri</h1>
<p class="intro-sub">{t["future"]}</p>
<a class="intro-cta" href="#contact">{t["touch"]}</a>
</div><div class="scroll-cue" id="scrollCue" aria-hidden="true"></div></header>
</div>
<div class="hero-wrap" data-play>
<section class="hero" style="grid-template-columns:1fr"><div class="hero-content">
<span class="kicker"><i></i>{t["kicker"]}</span>
<h2 class="h1">{t["h1a"]}<br><span class="grad">{t["h1b"]}</span></h2>
<p class="sub">{t["sub"]}</p><p class="who">{t["who"]}</p>
<div class="ctas"><a class="btn btn-dark" href="/#scan">{t["cta1"]}</a><a class="btn btn-light" href="#" data-open-agent="">{t["cta2"]}</a></div>
</div></section></div>
<section class="block alt" id="services"><div class="inner"><div class="reveal"><p class="eyebrow">{t["s_eye"]}</p><h2>{t["s_h"]}</h2></div><div class="cards stagger">{cards}</div></div></section>
<section class="block reveal" id="method"><div class="inner"><p class="eyebrow">{t["m_eye"]}</p><h2><bdi dir="ltr">B.U.I.L.D.</bdi></h2><div class="steps stagger">{steps}</div></div></section>
<section class="block alt reveal" id="about"><div class="inner"><p class="eyebrow">{t["a_eye"]}</p><p class="lede">{t["a_p"]}</p></div></section>
<section class="block reveal" id="portfolio"><div class="inner"><p class="eyebrow">{t["p_eye"]}</p><div class="cards stagger" dir="ltr" lang="en">{portfolio.cards(portfolio.home_items())}</div>
<a class="btn btn-light" href="/portfolio/" style="margin-top:30px">{t["port"]}</a></div></section>
<section class="block alt reveal" id="faq"><div class="inner"><h2>{t["faq_h"]}</h2><div class="faq">{faq_html(t["faq"])}</div></div></section>
<section class="block reveal" id="contact"><div class="inner scan-grid"><div><p class="eyebrow">{t["c_eye"]}</p><h2>{t["c_h"]}</h2><p class="lede">{t["c_p"]}</p><p class="lede"><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<div class="formcard"><form data-lead data-ok="{f[6]}"><div class="fgrid">
<div><label class="f" for="c-n">{f[0]}</label><input class="f-in" id="c-n" name="name" required maxlength="120"></div>
<div><label class="f" for="c-e">{f[1]}</label><input class="f-in" id="c-e" name="email" type="email" required maxlength="200" dir="ltr"></div>
<div><label class="f" for="c-c">{f[2]}</label><input class="f-in" id="c-c" name="company" maxlength="200"></div>
<div><label class="f" for="c-p">{f[3]}</label><input class="f-in" id="c-p" name="phone" type="tel" maxlength="60" dir="ltr"></div>
<div class="full"><label class="f" for="c-m">{f[4]}</label><textarea class="f-in" id="c-m" name="need" required maxlength="2000"></textarea></div>
</div><div class="hp" aria-hidden="true"><input name="company_url_hp" tabindex="-1" autocomplete="off"></div>
<button class="btn btn-dark" type="submit" style="margin-top:18px">{f[5]}</button><p class="f-msg" aria-live="polite"></p></form></div></div></section>
</main>
"""
    return html + tail(lang)
