/* Cookie consent for ryanjavaheri.com.
   - Shows a banner on first visit and a "Cookie preferences" dialog (footer link, or any [data-cookie-prefs]).
   - Category "embeds" gates third-party content (Adobe Express, WordPress.com). Nothing third-party loads before consent.
   - The choice is stored only in this browser (localStorage "rj-consent-v1").
   - Mark gated content as: <div data-embed-src="https://…" data-embed-host="Adobe Express" data-embed-title="…"></div>
   Include with <script src="/assets/consent.js" defer></script> */
(function () {
  if (window.rjConsent) return;

  var KEY = 'rj-consent-v1';
  var lang = (document.documentElement.lang || 'en').toLowerCase().slice(0, 2);
  var rtl = /^(fa|he|ar)$/.test(lang);

  var T = {
    en: { msg: 'This site only stores what it needs to work. With your permission it also loads embedded content from other companies (Adobe, WordPress.com), which may set their own cookies.', accept: 'Accept all', reject: 'Essential only', prefs: 'Preferences', title: 'Cookie preferences', ess: 'Essential', essd: 'Needed for the site to work: remembers this choice and keeps your AI advisor chat during your visit. Always on.', emb: 'Embedded content', embd: 'Loads portfolio pages hosted by Adobe Express and WordPress.com. Those companies may set cookies and see your IP address.', save: 'Save choices', terms: 'Terms', privacy: 'Privacy', form: 'By sending, you agree to the {t} and {p} Policy.' },
    es: { msg: 'Este sitio solo guarda lo necesario para funcionar. Con tu permiso también carga contenido integrado de otras empresas (Adobe, WordPress.com), que pueden instalar sus propias cookies.', accept: 'Aceptar todo', reject: 'Solo esenciales', prefs: 'Preferencias', title: 'Preferencias de cookies', ess: 'Esenciales', essd: 'Necesarias para que el sitio funcione: recuerdan esta elección y mantienen tu chat con el asesor de IA durante la visita. Siempre activas.', emb: 'Contenido integrado', embd: 'Carga páginas del portafolio alojadas en Adobe Express y WordPress.com. Esas empresas pueden instalar cookies y ver tu dirección IP.', save: 'Guardar', terms: 'Términos', privacy: 'Privacidad', form: 'Al enviar, aceptas los {t} y la política de {p}.' },
    fa: { msg: 'این سایت فقط آنچه برای کارکردن لازم است ذخیره می‌کند. با اجازهٔ شما محتوای جاسازی‌شده از شرکت‌های دیگر (Adobe و WordPress.com) نیز بارگذاری می‌شود که ممکن است کوکی‌های خودشان را ذخیره کنند.', accept: 'پذیرفتن همه', reject: 'فقط ضروری', prefs: 'تنظیمات', title: 'تنظیمات کوکی', ess: 'ضروری', essd: 'برای کارکرد سایت لازم است: این انتخاب را به خاطر می‌سپارد و گفت‌وگوی شما با مشاور هوش مصنوعی را در طول بازدید نگه می‌دارد. همیشه فعال.', emb: 'محتوای جاسازی‌شده', embd: 'صفحات نمونه‌کار میزبانی‌شده در Adobe Express و WordPress.com را بارگذاری می‌کند. این شرکت‌ها ممکن است کوکی ذخیره کنند و نشانی IP شما را ببینند.', save: 'ذخیره', terms: 'شرایط استفاده', privacy: 'حریم خصوصی', form: 'با ارسال، {t} و سیاست {p} را می‌پذیرید.' },
    he: { msg: 'האתר שומר רק את מה שנחוץ לפעולתו. באישורכם הוא טוען גם תוכן מוטמע מחברות אחרות (Adobe, WordPress.com), שעשויות לשמור קובצי Cookie משלהן.', accept: 'אישור הכול', reject: 'חיוניים בלבד', prefs: 'העדפות', title: 'העדפות קובצי Cookie', ess: 'חיוניים', essd: 'נדרשים לפעולת האתר: זוכרים את הבחירה הזו ושומרים את השיחה עם יועץ ה-AI במהלך הביקור. תמיד פעילים.', emb: 'תוכן מוטמע', embd: 'טוען עמודי תיק עבודות המתארחים ב-Adobe Express וב-WordPress.com. חברות אלה עשויות לשמור קובצי Cookie ולראות את כתובת ה-IP שלכם.', save: 'שמירה', terms: 'תנאי השימוש', privacy: 'פרטיות', form: 'בשליחה אתם מסכימים ל{t} ולמדיניות ה{p}.' },
    ar: { msg: 'هذا الموقع يخزّن فقط ما يحتاجه ليعمل. وبإذنك يحمّل أيضًا محتوى مضمّنًا من شركات أخرى (Adobe و WordPress.com) قد تضع ملفات تعريف ارتباط خاصة بها.', accept: 'قبول الكل', reject: 'الضروري فقط', prefs: 'التفضيلات', title: 'تفضيلات ملفات تعريف الارتباط', ess: 'ضرورية', essd: 'لازمة لعمل الموقع: تتذكر هذا الاختيار وتحفظ محادثتك مع المستشار الذكي أثناء زيارتك. مفعّلة دائمًا.', emb: 'المحتوى المضمّن', embd: 'يحمّل صفحات الأعمال المستضافة على Adobe Express و WordPress.com. قد تضع هذه الشركات ملفات تعريف ارتباط وترى عنوان IP الخاص بك.', save: 'حفظ', terms: 'الشروط', privacy: 'الخصوصية', form: 'بالإرسال، أنت توافق على {t} وسياسة {p}.' },
    zh: { msg: '本网站只存储运行所必需的内容。经您许可后，还会加载来自其他公司（Adobe、WordPress.com）的嵌入内容，这些公司可能会设置自己的 Cookie。', accept: '全部接受', reject: '仅必要项', prefs: '偏好设置', title: 'Cookie 偏好设置', ess: '必要', essd: '网站运行所必需：记住此选择，并在您访问期间保留与 AI 顾问的对话。始终开启。', emb: '嵌入内容', embd: '加载托管在 Adobe Express 和 WordPress.com 上的作品集页面。这些公司可能会设置 Cookie 并看到您的 IP 地址。', save: '保存选择', terms: '条款', privacy: '隐私政策', form: '发送即表示您同意{t}和{p}。' },
    ko: { msg: '이 사이트는 작동에 필요한 정보만 저장합니다. 동의하시면 다른 회사(Adobe, WordPress.com)의 임베드 콘텐츠도 불러오며, 해당 회사가 자체 쿠키를 설정할 수 있습니다.', accept: '모두 허용', reject: '필수만', prefs: '설정', title: '쿠키 설정', ess: '필수', essd: '사이트 작동에 필요합니다. 이 선택을 기억하고 방문 중 AI 상담사와의 대화를 유지합니다. 항상 켜져 있습니다.', emb: '임베드 콘텐츠', embd: 'Adobe Express와 WordPress.com에서 호스팅되는 포트폴리오 페이지를 불러옵니다. 해당 회사가 쿠키를 설정하고 IP 주소를 볼 수 있습니다.', save: '선택 저장', terms: '이용약관', privacy: '개인정보처리방침', form: '보내시면 {t} 및 {p}에 동의하는 것으로 간주됩니다.' },
    ja: { msg: 'このサイトは動作に必要な情報のみを保存します。許可いただいた場合に限り、他社（Adobe、WordPress.com）の埋め込みコンテンツも読み込みます。これらの会社が独自のCookieを設定することがあります。', accept: 'すべて許可', reject: '必須のみ', prefs: '設定', title: 'Cookieの設定', ess: '必須', essd: 'サイトの動作に必要です。この選択を記憶し、訪問中のAIアドバイザーとの会話を保持します。常に有効です。', emb: '埋め込みコンテンツ', embd: 'Adobe ExpressとWordPress.comでホストされているポートフォリオページを読み込みます。これらの会社がCookieを設定し、IPアドレスを取得することがあります。', save: '選択を保存', terms: '利用規約', privacy: 'プライバシーポリシー', form: '送信すると、{t}と{p}に同意したことになります。' },
    fr: { msg: 'Ce site ne stocke que ce qui est nécessaire à son fonctionnement. Avec votre accord, il charge aussi du contenu intégré d\'autres sociétés (Adobe, WordPress.com), qui peuvent déposer leurs propres cookies.', accept: 'Tout accepter', reject: 'Essentiels uniquement', prefs: 'Préférences', title: 'Préférences de cookies', ess: 'Essentiels', essd: 'Nécessaires au fonctionnement du site : mémorisent ce choix et conservent votre conversation avec le conseiller IA pendant la visite. Toujours actifs.', emb: 'Contenu intégré', embd: 'Charge les pages du portfolio hébergées par Adobe Express et WordPress.com. Ces sociétés peuvent déposer des cookies et voir votre adresse IP.', save: 'Enregistrer', terms: 'Conditions', privacy: 'Confidentialité', form: 'En envoyant, vous acceptez les {t} et la politique de {p}.' },
    pt: { msg: 'Este site guarda apenas o necessário para funcionar. Com a sua permissão, também carrega conteúdo incorporado de outras empresas (Adobe, WordPress.com), que podem definir os próprios cookies.', accept: 'Aceitar tudo', reject: 'Só essenciais', prefs: 'Preferências', title: 'Preferências de cookies', ess: 'Essenciais', essd: 'Necessários para o site funcionar: lembram esta escolha e mantêm a sua conversa com o consultor de IA durante a visita. Sempre ativos.', emb: 'Conteúdo incorporado', embd: 'Carrega páginas do portfólio hospedadas no Adobe Express e no WordPress.com. Essas empresas podem definir cookies e ver o seu endereço IP.', save: 'Salvar', terms: 'Termos', privacy: 'Privacidade', form: 'Ao enviar, você concorda com os {t} e a política de {p}.' },
    ru: { msg: 'Сайт хранит только то, что нужно для его работы. С вашего разрешения он также загружает встроенный контент других компаний (Adobe, WordPress.com), которые могут устанавливать свои cookie.', accept: 'Принять все', reject: 'Только необходимые', prefs: 'Настройки', title: 'Настройки cookie', ess: 'Необходимые', essd: 'Нужны для работы сайта: запоминают этот выбор и сохраняют чат с ИИ-консультантом на время визита. Всегда включены.', emb: 'Встроенный контент', embd: 'Загружает страницы портфолио, размещённые на Adobe Express и WordPress.com. Эти компании могут устанавливать cookie и видеть ваш IP-адрес.', save: 'Сохранить', terms: 'Условия', privacy: 'Конфиденциальность', form: 'Отправляя, вы принимаете {t} и политику «{p}».' },
    hy: { msg: 'Այս կայքը պահում է միայն այն, ինչ անհրաժեշտ է աշխատելու համար։ Ձեր թույլտվությամբ այն բեռնում է նաև այլ ընկերությունների (Adobe, WordPress.com) ներկառուցված բովանդակություն, որոնք կարող են տեղադրել իրենց cookie-ները։', accept: 'Ընդունել բոլորը', reject: 'Միայն անհրաժեշտները', prefs: 'Կարգավորումներ', title: 'Cookie-ների կարգավորումներ', ess: 'Անհրաժեշտ', essd: 'Պետք են կայքի աշխատանքի համար. հիշում են այս ընտրությունը և պահում են ԱԲ խորհրդատուի հետ զրույցը այցի ընթացքում։ Միշտ միացված են։', emb: 'Ներկառուցված բովանդակություն', embd: 'Բեռնում է Adobe Express-ում և WordPress.com-ում տեղակայված պորտֆոլիոյի էջերը։ Այդ ընկերությունները կարող են տեղադրել cookie-ներ և տեսնել ձեր IP հասցեն։', save: 'Պահպանել', terms: 'Պայմաններ', privacy: 'Գաղտնիություն', form: 'Ուղարկելով՝ դուք համաձայնում եք {t} և {p} քաղաքականությանը։' },
    hi: { msg: 'यह साइट केवल वही सहेजती है जो इसके काम करने के लिए ज़रूरी है। आपकी अनुमति से यह दूसरी कंपनियों (Adobe, WordPress.com) की एम्बेडेड सामग्री भी लोड करती है, जो अपनी कुकीज़ सेट कर सकती हैं।', accept: 'सभी स्वीकार करें', reject: 'केवल ज़रूरी', prefs: 'प्राथमिकताएँ', title: 'कुकी प्राथमिकताएँ', ess: 'ज़रूरी', essd: 'साइट के काम करने के लिए आवश्यक: यह चुनाव याद रखती हैं और आपकी विज़िट के दौरान AI सलाहकार से बातचीत बनाए रखती हैं। हमेशा चालू।', emb: 'एम्बेडेड सामग्री', embd: 'Adobe Express और WordPress.com पर होस्ट किए गए पोर्टफ़ोलियो पेज लोड करती है। ये कंपनियाँ कुकीज़ सेट कर सकती हैं और आपका IP पता देख सकती हैं।', save: 'सहेजें', terms: 'शर्तें', privacy: 'गोपनीयता', form: 'भेजकर आप {t} और {p} नीति से सहमत होते हैं।' }
  };
  var L = T[lang] || T.en;

  function read() {
    try {
      var c = JSON.parse(localStorage.getItem(KEY) || 'null');
      if (c && c.v === 1 && typeof c.embeds === 'boolean') return c;
    } catch (e) {}
    return null;
  }
  var choice = read();
  var listeners = [];

  function save(embeds) {
    choice = { v: 1, embeds: !!embeds, t: new Date().toISOString() };
    try { localStorage.setItem(KEY, JSON.stringify(choice)); } catch (e) {}
    hideBanner(); closeDialog();
    listeners.forEach(function (fn) { try { fn(choice); } catch (e) {} });
    renderEmbeds();
  }

  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function link(href, text) { var a = el('a', null, text); a.href = href; return a; }

  var css = '' +
    '.rjc,.rjc-dlg,.rjc-embed{font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text","Helvetica Neue",Arial,sans-serif;color:#1d1d1f;line-height:1.45;box-sizing:border-box}' +
    '.rjc *,.rjc-dlg *,.rjc-embed *{box-sizing:border-box}' +
    '.rjc{position:fixed;left:20px;bottom:20px;z-index:9990;width:440px;max-width:calc(100vw - 40px);background:#fff;border-radius:20px;box-shadow:0 18px 60px rgba(0,0,0,.22),0 0 0 1px rgba(0,0,0,.06);padding:20px;font-size:14px;animation:rjcIn .5s cubic-bezier(.16,1,.3,1)}' +
    '@keyframes rjcIn{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}' +
    '.rjc p{margin:0 0 6px}.rjc .rjc-links{font-size:12px;color:#6e6e73;margin-bottom:14px}.rjc a,.rjc-dlg a,.rjc-embed a{color:#1a5fd6}' +
    '.rjc-row{display:flex;gap:8px;flex-wrap:wrap}' +
    '.rjc-b{flex:1 1 auto;border:1px solid #0b0b0d;border-radius:999px;padding:10px 16px;font:600 14px/1.2 inherit;font-family:inherit;cursor:pointer;background:#0b0b0d;color:#fff;white-space:nowrap}' +
    '.rjc-b.alt{background:#fff;color:#0b0b0d}' +
    '.rjc-b.txt{flex:0 0 auto;background:none;border-color:transparent;color:#1d1d1f;text-decoration:underline;padding:10px 8px}' +
    '.rjc-b:focus-visible,.rjc-sw input:focus-visible+span{outline:2px solid #1a5fd6;outline-offset:2px}' +
    '.rjc-back{position:fixed;inset:0;z-index:10000;background:rgba(0,0,0,.45);display:flex;align-items:center;justify-content:center;padding:16px}' +
    '.rjc-dlg{background:#fff;border-radius:22px;width:520px;max-width:100%;max-height:calc(100vh - 32px);overflow:auto;padding:26px;font-size:14px;box-shadow:0 30px 90px rgba(0,0,0,.35)}' +
    '.rjc-dlg h2{font-size:22px;margin:0 0 6px;letter-spacing:-.01em}' +
    '.rjc-cat{display:flex;gap:16px;align-items:flex-start;justify-content:space-between;padding:16px 0;border-top:1px solid rgba(0,0,0,.08)}' +
    '.rjc-cat b{display:block;font-size:15px;margin-bottom:3px}.rjc-cat span.d{color:#6e6e73;font-size:13px}' +
    '.rjc-sw{position:relative;flex:0 0 auto;width:46px;height:28px;margin-top:2px}' +
    '.rjc-sw input{position:absolute;inset:0;opacity:0;width:100%;height:100%;margin:0;cursor:pointer}' +
    '.rjc-sw span{position:absolute;inset:0;border-radius:999px;background:#d2d2d7;transition:background .2s;pointer-events:none}' +
    '.rjc-sw span:after{content:"";position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.3);transition:transform .2s}' +
    '.rjc-sw input:checked+span{background:#0b0b0d}.rjc-sw input:checked+span:after{transform:translateX(18px)}' +
    '.rjc-sw input:disabled{cursor:not-allowed}.rjc-sw input:disabled+span{opacity:.45}' +
    '.rjc-dlg .rjc-row{margin-top:18px}' +
    '.rjc-embed{position:fixed;inset:0;display:flex;align-items:center;justify-content:center;padding:24px;background:#f5f5f7}' +
    '.rjc-embed>div{background:#fff;border-radius:22px;padding:32px;max-width:480px;box-shadow:0 10px 50px rgba(0,0,0,.1);font-size:16px}' +
    '.rjc-embed h1{font-size:24px;margin:0 0 10px;letter-spacing:-.01em}.rjc-embed p{margin:0 0 18px;color:#424245}.rjc-embed small{display:block;margin-top:16px;color:#6e6e73;font-size:12px}' +
    '.rjc-frame{position:fixed;top:0;left:0;width:100vw;height:100vh;height:100dvh;border:0;display:block}' +
    '.f-legal{font-size:12px;color:#86868b;margin-top:12px}.f-legal a{color:inherit;text-decoration:underline}' +
    '@media (max-width:560px){.rjc{left:12px;right:12px;bottom:78px;width:auto;max-width:none;padding:16px}.rjc-b{padding:10px 12px}}' +
    '@media (prefers-reduced-motion:reduce){.rjc{animation:none}.rjc-sw span,.rjc-sw span:after{transition:none}}';
  var st = document.createElement('style');
  st.textContent = css;
  document.head.appendChild(st);

  function legalLinks() {
    var p = el('p', 'rjc-links');
    p.appendChild(link('/privacy/', L.privacy));
    p.appendChild(document.createTextNode(' · '));
    p.appendChild(link('/terms/', L.terms));
    return p;
  }
  function button(text, cls, fn) { var b = el('button', 'rjc-b' + (cls ? ' ' + cls : ''), text); b.type = 'button'; b.onclick = fn; return b; }

  /* ---- Banner ---- */
  var banner = null;
  function showBanner() {
    if (banner) return;
    banner = el('div', 'rjc');
    banner.setAttribute('role', 'region');
    banner.setAttribute('aria-label', L.title);
    if (rtl) banner.dir = 'rtl';
    banner.appendChild(el('p', null, L.msg));
    banner.appendChild(legalLinks());
    var row = el('div', 'rjc-row');
    row.appendChild(button(L.accept, '', function () { save(true); }));
    row.appendChild(button(L.reject, 'alt', function () { save(false); }));
    row.appendChild(button(L.prefs, 'txt', openDialog));
    banner.appendChild(row);
    document.body.appendChild(banner);
  }
  function hideBanner() { if (banner) { banner.remove(); banner = null; } }

  /* ---- Preferences dialog ---- */
  var back = null, lastFocus = null;
  function cat(title, desc, checked, disabled) {
    var row = el('div', 'rjc-cat');
    var txt = el('div'); txt.appendChild(el('b', null, title)); txt.appendChild(el('span', 'd', desc));
    var sw = el('label', 'rjc-sw');
    var input = el('input'); input.type = 'checkbox'; input.checked = checked; input.disabled = !!disabled;
    input.setAttribute('aria-label', title);
    sw.appendChild(input); sw.appendChild(el('span'));
    row.appendChild(txt); row.appendChild(sw);
    return { row: row, input: input };
  }
  function openDialog() {
    if (back) return;
    lastFocus = document.activeElement;
    back = el('div', 'rjc-back');
    var dlg = el('div', 'rjc-dlg');
    dlg.setAttribute('role', 'dialog'); dlg.setAttribute('aria-modal', 'true'); dlg.setAttribute('aria-labelledby', 'rjc-title');
    if (rtl) dlg.dir = 'rtl';
    var h = el('h2', null, L.title); h.id = 'rjc-title';
    dlg.appendChild(h);
    dlg.appendChild(legalLinks());
    var ess = cat(L.ess, L.essd, true, true);
    var emb = cat(L.emb, L.embd, !!(choice && choice.embeds), false);
    dlg.appendChild(ess.row); dlg.appendChild(emb.row);
    var row = el('div', 'rjc-row');
    row.appendChild(button(L.save, '', function () { save(emb.input.checked); }));
    row.appendChild(button(L.accept, 'alt', function () { save(true); }));
    row.appendChild(button(L.reject, 'alt', function () { save(false); }));
    dlg.appendChild(row);
    back.appendChild(dlg);
    back.addEventListener('click', function (e) { if (e.target === back) closeDialog(); });
    back.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { closeDialog(); return; }
      if (e.key !== 'Tab') return;
      var f = dlg.querySelectorAll('a,button,input:not([disabled])');
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
    document.body.appendChild(back);
    emb.input.focus();
  }
  function closeDialog() {
    if (!back) return;
    back.remove(); back = null;
    if (lastFocus && lastFocus.focus) { try { lastFocus.focus(); } catch (e) {} }
  }

  /* ---- Third-party embeds: only load after consent ---- */
  function renderEmbeds() {
    var nodes = document.querySelectorAll('[data-embed-src]');
    for (var i = 0; i < nodes.length; i++) {
      var box = nodes[i];
      var src = box.getAttribute('data-embed-src');
      var host = box.getAttribute('data-embed-host') || 'another company';
      var title = box.getAttribute('data-embed-title') || document.title;
      if (choice && choice.embeds) {
        if (box.querySelector('iframe')) continue;
        box.textContent = '';
        var f = el('iframe', 'rjc-frame');
        f.src = src; f.title = title; f.setAttribute('allow', 'fullscreen'); f.setAttribute('allowfullscreen', '');
        box.appendChild(f);
      } else {
        if (box.querySelector('.rjc-embed')) continue;
        box.textContent = '';
        var wrap = el('div', 'rjc-embed'), card = el('div');
        card.appendChild(el('h1', null, title));
        card.appendChild(el('p', null, 'This page shows content hosted by ' + host + '. Loading it lets ' + host + ' set cookies and see your IP address. It only loads if you allow it.'));
        var row = el('div', 'rjc-row');
        row.appendChild(button('Allow and load', '', function () { save(true); }));
        var a = el('a', 'rjc-b alt', 'Open on ' + host); a.href = src; a.target = '_blank'; a.rel = 'noopener'; a.style.textDecoration = 'none'; a.style.textAlign = 'center';
        row.appendChild(a);
        card.appendChild(row);
        var sm = el('small');
        sm.appendChild(link('/', '← ryanjavaheri.com')); sm.appendChild(document.createTextNode(' · '));
        sm.appendChild(link('/privacy/#cookies', 'Privacy and cookies')); sm.appendChild(document.createTextNode(' · '));
        sm.appendChild(link('/terms/', 'Terms'));
        card.appendChild(sm);
        wrap.appendChild(card); box.appendChild(wrap);
      }
    }
    return nodes.length;
  }

  /* ---- Terms / Privacy line under forms that don't already have one ---- */
  function formNotes() {
    var forms = document.querySelectorAll('form[data-lead], #scanForm');
    for (var i = 0; i < forms.length; i++) {
      var form = forms[i];
      if (form.parentNode.querySelector('a[href="/terms/"]')) continue;
      var p = el('p', 'f-legal');
      var parts = L.form.split(/(\{t\}|\{p\})/);
      parts.forEach(function (s) {
        if (s === '{t}') p.appendChild(link('/terms/', L.terms));
        else if (s === '{p}') p.appendChild(link('/privacy/', L.privacy));
        else if (s) p.appendChild(document.createTextNode(s));
      });
      form.appendChild(p);
    }
  }

  window.rjConsent = {
    get: function () { return choice; },
    allowed: function (cat) { return cat === 'essential' || !!(choice && choice[cat]); },
    set: save,
    open: openDialog,
    onChange: function (fn) { listeners.push(fn); },
    labels: { terms: L.terms, privacy: L.privacy }
  };

  document.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('[data-cookie-prefs], a[href="#cookie-preferences"]');
    if (t) { e.preventDefault(); openDialog(); }
  });

  function start() {
    var embeds = renderEmbeds();
    formNotes();
    /* On a page that is only an embed, the placeholder already asks the question. */
    if (!choice && !(embeds && document.body.hasAttribute('data-embed-page'))) showBanner();
    if (location.hash === '#cookie-preferences') openDialog();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
