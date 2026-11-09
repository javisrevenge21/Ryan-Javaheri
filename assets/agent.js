/* Ryan's AI intake advisor: chat + voice widget. Include with <script src="/assets/agent.js" defer></script> */
(function () {
  if (window.__rjAgent) return;
  window.__rjAgent = true;

  var lang = (document.documentElement.lang || navigator.language || 'en').toLowerCase();
  var T = {
    en: { open: 'Ask my AI advisor', title: "Ryan's AI Advisor", status: 'Online 24/7 · any language', ph: 'Type your question…', send: 'Send', hello: "Hi! I'm Ryan's AI advisor. Ask me anything about AI visibility, websites, AI agents, or working with Ryan. I can also take your details so Ryan can contact you personally.", talk: 'Talk', stop: 'Stop', listening: 'Listening…', saved: 'Saved. Ryan will follow up personally.', voiceOff: 'Voice not supported in this browser. Try Chrome or Safari.', note: 'AI assistant. Details you share go to Ryan.' },
    es: { open: 'Pregunta a mi asesor IA', title: 'Asesor IA de Ryan', status: 'En línea 24/7 · cualquier idioma', ph: 'Escribe tu pregunta…', send: 'Enviar', hello: '¡Hola! Soy el asesor de IA de Ryan. Pregúntame sobre visibilidad en IA, sitios web, agentes de IA o cómo trabajar con Ryan. También puedo tomar tus datos para que Ryan te contacte.', talk: 'Hablar', stop: 'Parar', listening: 'Escuchando…', saved: 'Guardado. Ryan te contactará personalmente.', voiceOff: 'La voz no funciona en este navegador. Prueba Chrome o Safari.', note: 'Asistente de IA. Tus datos llegan a Ryan.' },
    fa: { open: 'از مشاور هوش مصنوعی بپرسید', title: 'مشاور هوش مصنوعی رایان', status: 'آنلاین ۲۴/۷ · به هر زبانی', ph: 'سؤال خود را بنویسید…', send: 'ارسال', hello: 'سلام! من مشاور هوش مصنوعی رایان هستم. درباره دیده‌شدن در هوش مصنوعی، وب‌سایت، ایجنت‌های هوش مصنوعی یا همکاری با رایان بپرسید. می‌توانم اطلاعات شما را هم بگیرم تا رایان شخصاً تماس بگیرد.', talk: 'صحبت', stop: 'توقف', listening: 'در حال گوش دادن…', saved: 'ذخیره شد. رایان شخصاً با شما تماس می‌گیرد.', voiceOff: 'صدا در این مرورگر پشتیبانی نمی‌شود.', note: 'دستیار هوش مصنوعی. اطلاعات شما به رایان می‌رسد.' },
    he: {"open": "שאלו את יועץ ה-AI", "title": "יועץ ה-AI של ריאן", "status": "מחובר 24/7 · בכל שפה", "ph": "הקלידו שאלה…", "send": "שלח", "hello": "שלום! אני יועץ ה-AI של ריאן. שאלו אותי על נראות ב-AI, אתרים, סוכני AI או עבודה עם ריאן. אוכל גם לקחת את הפרטים שלכם כדי שריאן ייצור קשר אישית.", "talk": "דברו", "stop": "עצור", "listening": "מקשיב…", "saved": "נשמר. ריאן יחזור אליכם אישית.", "voiceOff": "קול לא נתמך בדפדפן הזה.", "note": "עוזר AI. הפרטים שתשתפו מגיעים לריאן."},
    ar: {"open": "اسأل مستشاري الذكي", "title": "مستشار رايان الذكي", "status": "متصل 24/7 · بأي لغة", "ph": "اكتب سؤالك…", "send": "إرسال", "hello": "مرحبًا! أنا مستشار رايان الذكي. اسألني عن الظهور في الذكاء الاصطناعي أو المواقع أو وكلاء الذكاء الاصطناعي أو العمل مع رايان. يمكنني أيضًا أخذ بياناتك ليتواصل معك رايان شخصيًا.", "talk": "تحدث", "stop": "إيقاف", "listening": "أستمع…", "saved": "تم الحفظ. سيتواصل رايان معك شخصيًا.", "voiceOff": "الصوت غير مدعوم في هذا المتصفح.", "note": "مساعد ذكاء اصطناعي. بياناتك تصل إلى رايان."},
    zh: {"open": "问问我的 AI 顾问", "title": "Ryan 的 AI 顾问", "status": "24/7 在线 · 支持任何语言", "ph": "输入你的问题…", "send": "发送", "hello": "你好！我是 Ryan 的 AI 顾问。可以问我关于 AI 曝光、网站、AI 智能体或与 Ryan 合作的任何问题。我也可以记录你的联系方式，让 Ryan 亲自联系你。", "talk": "语音", "stop": "停止", "listening": "正在聆听…", "saved": "已保存。Ryan 会亲自联系你。", "voiceOff": "此浏览器不支持语音。", "note": "AI 助手。你分享的信息将发送给 Ryan。"},
    ko: {"open": "AI 상담사에게 물어보기", "title": "라이언의 AI 상담사", "status": "24시간 온라인 · 모든 언어", "ph": "질문을 입력하세요…", "send": "보내기", "hello": "안녕하세요! 라이언의 AI 상담사입니다. AI 노출, 웹사이트, AI 에이전트, 라이언과의 협업에 대해 무엇이든 물어보세요. 연락처를 남기시면 라이언이 직접 연락드립니다.", "talk": "말하기", "stop": "중지", "listening": "듣는 중…", "saved": "저장되었습니다. 라이언이 직접 연락드립니다.", "voiceOff": "이 브라우저는 음성을 지원하지 않습니다.", "note": "AI 어시스턴트입니다. 공유한 정보는 라이언에게 전달됩니다."},
    ja: {"open": "AIアドバイザーに質問", "title": "ライアンのAIアドバイザー", "status": "24時間対応 · 多言語", "ph": "質問を入力してください…", "send": "送信", "hello": "こんにちは！ライアンのAIアドバイザーです。AI露出、Webサイト、AIエージェント、ライアンとの仕事について何でも聞いてください。連絡先をいただければライアンから直接ご連絡します。", "talk": "話す", "stop": "停止", "listening": "聞いています…", "saved": "保存しました。ライアンから直接ご連絡します。", "voiceOff": "このブラウザは音声に対応していません。", "note": "AIアシスタントです。共有した情報はライアンに届きます。"},
    fr: {"open": "Demandez à mon conseiller IA", "title": "Le conseiller IA de Ryan", "status": "En ligne 24h/24 · toutes langues", "ph": "Écrivez votre question…", "send": "Envoyer", "hello": "Bonjour ! Je suis le conseiller IA de Ryan. Posez-moi vos questions sur la visibilité IA, les sites web, les agents IA ou le travail avec Ryan. Je peux aussi prendre vos coordonnées pour que Ryan vous contacte personnellement.", "talk": "Parler", "stop": "Arrêter", "listening": "J'écoute…", "saved": "Enregistré. Ryan vous recontactera personnellement.", "voiceOff": "La voix n'est pas prise en charge par ce navigateur.", "note": "Assistant IA. Vos informations sont transmises à Ryan."},
    pt: {"open": "Pergunte ao meu consultor de IA", "title": "Consultor de IA do Ryan", "status": "Online 24/7 · qualquer idioma", "ph": "Digite sua pergunta…", "send": "Enviar", "hello": "Olá! Sou o consultor de IA do Ryan. Pergunte sobre visibilidade em IA, sites, agentes de IA ou como trabalhar com o Ryan. Também posso anotar seus dados para o Ryan entrar em contato pessoalmente.", "talk": "Falar", "stop": "Parar", "listening": "Ouvindo…", "saved": "Salvo. O Ryan vai entrar em contato pessoalmente.", "voiceOff": "Voz não suportada neste navegador.", "note": "Assistente de IA. Seus dados vão para o Ryan."},
    ru: {"open": "Спросите моего ИИ-консультанта", "title": "ИИ-консультант Райана", "status": "Онлайн 24/7 · любой язык", "ph": "Введите вопрос…", "send": "Отправить", "hello": "Здравствуйте! Я ИИ-консультант Райана. Спрашивайте о видимости в ИИ, сайтах, ИИ-агентах или работе с Райаном. Я также могу записать ваши контакты, чтобы Райан связался с вами лично.", "talk": "Говорить", "stop": "Стоп", "listening": "Слушаю…", "saved": "Сохранено. Райан свяжется с вами лично.", "voiceOff": "Голос не поддерживается в этом браузере.", "note": "ИИ-ассистент. Ваши данные получит Райан."},
    hy: {"open": "Հարցրեք իմ ԱԲ խորհրդատուին", "title": "Ռայանի ԱԲ խորհրդատուն", "status": "Առցանց 24/7 · ցանկացած լեզվով", "ph": "Գրեք ձեր հարցը…", "send": "Ուղարկել", "hello": "Բարև։ Ես Ռայանի ԱԲ խորհրդատուն եմ։ Հարցրեք ինձ ԱԲ-ում տեսանելիության, կայքերի, ԱԲ գործակալների կամ Ռայանի հետ աշխատելու մասին։ Կարող եմ նաև գրանցել ձեր տվյալները, որպեսզի Ռայանը անձամբ կապվի ձեզ հետ։", "talk": "Խոսել", "stop": "Կանգնեցնել", "listening": "Լսում եմ…", "saved": "Պահպանված է։ Ռայանը անձամբ կկապվի ձեզ հետ։", "voiceOff": "Ձայնը չի աջակցվում այս դիտարկիչում։", "note": "ԱԲ օգնական։ Ձեր տվյալները կստանա Ռայանը։"},
    hi: {"open": "मेरे AI सलाहकार से पूछें", "title": "रयान का AI सलाहकार", "status": "24/7 ऑनलाइन · किसी भी भाषा में", "ph": "अपना सवाल लिखें…", "send": "भेजें", "hello": "नमस्ते! मैं रयान का AI सलाहकार हूँ। AI विज़िबिलिटी, वेबसाइट, AI एजेंट या रयान के साथ काम करने के बारे में कुछ भी पूछें। मैं आपकी जानकारी भी ले सकता हूँ ताकि रयान आपसे ख़ुद संपर्क करें।", "talk": "बोलें", "stop": "रोकें", "listening": "सुन रहा हूँ…", "saved": "सेव हो गया। रयान आपसे ख़ुद संपर्क करेंगे।", "voiceOff": "इस ब्राउज़र में आवाज़ समर्थित नहीं है।", "note": "AI सहायक। आपकी जानकारी रयान तक पहुँचती है।"}
  };
  var L = T[lang.slice(0, 2)] || T.en;
  var rtl = /^(fa|he|ar)/.test(lang);

  var KEY = 'rj-agent-v1';
  var state = { open: false, messages: [] };
  try { var s = JSON.parse(sessionStorage.getItem(KEY) || 'null'); if (s && Array.isArray(s.messages)) state = s; } catch (e) {}
  function persist() { try { sessionStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {} }

  var css = '' +
    '.rja-btn{position:fixed;right:20px;bottom:20px;z-index:9998;display:flex;align-items:center;gap:10px;background:#0b0b0d;color:#fff;border:0;border-radius:999px;padding:12px 18px 12px 12px;font:600 15px/1 -apple-system,BlinkMacSystemFont,"SF Pro Text","Helvetica Neue",Arial,sans-serif;box-shadow:0 10px 40px rgba(0,0,0,.28);cursor:pointer;transition:transform .3s cubic-bezier(.16,1,.3,1)}' +
    '.rja-btn:hover{transform:translateY(-2px) scale(1.03)}' +
    '.rja-dot{width:30px;height:30px;border-radius:50%;background:radial-gradient(circle at 30% 30%,#7cf3ff,#2dd4ff 40%,#5b5bf7);position:relative}' +
    '.rja-dot:after{content:"";position:absolute;inset:-4px;border-radius:50%;border:2px solid rgba(45,212,255,.5);animation:rjaPulse 2s infinite}' +
    '@keyframes rjaPulse{0%{transform:scale(.9);opacity:1}100%{transform:scale(1.35);opacity:0}}' +
    '.rja-panel{position:fixed;right:20px;bottom:20px;z-index:9999;width:380px;max-width:calc(100vw - 24px);height:560px;max-height:calc(100vh - 40px);background:#fff;border-radius:22px;box-shadow:0 24px 80px rgba(0,0,0,.25);display:flex;flex-direction:column;overflow:hidden;font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text","Helvetica Neue",Arial,sans-serif;color:#1d1d1f;transform-origin:bottom right;animation:rjaIn .35s cubic-bezier(.16,1,.3,1)}' +
    '@keyframes rjaIn{from{opacity:0;transform:translateY(16px) scale(.96)}to{opacity:1;transform:none}}' +
    '.rja-head{background:#0b0b0d;color:#fff;padding:16px 16px 14px;display:flex;align-items:center;gap:12px}' +
    '.rja-head b{display:block;font-size:16px}.rja-head small{opacity:.7;font-size:12px}' +
    '.rja-x{margin-left:auto;background:rgba(255,255,255,.12);border:0;color:#fff;width:32px;height:32px;border-radius:50%;font-size:18px;cursor:pointer}' +
    '.rja-log{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:10px;background:#f5f5f7}' +
    '.rja-m{max-width:85%;padding:10px 14px;border-radius:18px;font-size:15px;line-height:1.4;white-space:pre-wrap;word-wrap:break-word}' +
    '.rja-a{background:#fff;align-self:flex-start;border-bottom-left-radius:6px;box-shadow:0 1px 3px rgba(0,0,0,.06)}' +
    '.rja-u{background:#0b0b0d;color:#fff;align-self:flex-end;border-bottom-right-radius:6px}' +
    '.rja-sys{align-self:center;font-size:12px;color:#1a7f37;background:#e8f7ed;padding:6px 12px;border-radius:999px}' +
    '.rja-typing span{display:inline-block;width:6px;height:6px;margin:0 2px;border-radius:50%;background:#86868b;animation:rjaB 1.2s infinite}' +
    '.rja-typing span:nth-child(2){animation-delay:.15s}.rja-typing span:nth-child(3){animation-delay:.3s}' +
    '@keyframes rjaB{0%,60%,100%{transform:none;opacity:.4}30%{transform:translateY(-4px);opacity:1}}' +
    '.rja-form{display:flex;gap:8px;padding:12px;border-top:1px solid #eee;background:#fff}' +
    '.rja-in{flex:1;border:1px solid #d2d2d7;border-radius:999px;padding:10px 14px;font-size:15px;outline:none;min-width:0}' +
    '.rja-in:focus{border-color:#0b0b0d}' +
    '.rja-send,.rja-mic{border:0;border-radius:999px;padding:0 14px;font-weight:600;font-size:14px;cursor:pointer}' +
    '.rja-send{background:#0b0b0d;color:#fff}.rja-mic{background:#f5f5f7;color:#1d1d1f}' +
    '.rja-mic.on{background:#ff3b30;color:#fff;animation:rjaGlow 1.2s infinite}' +
    '@keyframes rjaGlow{50%{box-shadow:0 0 0 6px rgba(255,59,48,.2)}}' +
    '.rja-note{font-size:11px;color:#86868b;text-align:center;padding:0 12px 10px;background:#fff}' +
    '.rja-rtl .rja-log,.rja-rtl .rja-form{direction:rtl}' +
    '@media (max-width:480px){.rja-panel{right:0;bottom:0;width:100vw;max-width:100vw;height:100%;max-height:100%;border-radius:0}.rja-btn .rja-lbl{display:none}.rja-btn{padding:10px}}' +
    '@media (prefers-reduced-motion:reduce){.rja-dot:after,.rja-panel{animation:none}}';
  var st = document.createElement('style');
  st.textContent = css;
  document.head.appendChild(st);

  var btn = document.createElement('button');
  btn.className = 'rja-btn';
  btn.type = 'button';
  btn.setAttribute('aria-label', L.open);
  btn.innerHTML = '<span class="rja-dot" aria-hidden="true"></span><span class="rja-lbl">' + L.open + '</span>';
  document.body.appendChild(btn);

  var panel, log, input, mic;
  var busy = false;

  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }

  function render() {
    log.innerHTML = '';
    log.appendChild(el('div', 'rja-m rja-a', L.hello));
    state.messages.forEach(function (m) {
      if (m.role === 'system') log.appendChild(el('div', 'rja-sys', m.content));
      else log.appendChild(el('div', 'rja-m ' + (m.role === 'user' ? 'rja-u' : 'rja-a'), m.content));
    });
    log.scrollTop = log.scrollHeight;
  }

  function openPanel() {
    state.open = true; persist();
    btn.style.display = 'none';
    if (panel) { panel.style.display = 'flex'; input.focus(); return; }
    panel = el('div', 'rja-panel' + (rtl ? ' rja-rtl' : ''));
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-label', L.title);
    var head = el('div', 'rja-head');
    head.innerHTML = '<span class="rja-dot" aria-hidden="true"></span><div><b></b><small></small></div>';
    head.querySelector('b').textContent = L.title;
    head.querySelector('small').textContent = L.status;
    var x = el('button', 'rja-x', '×'); x.type = 'button'; x.setAttribute('aria-label', 'Close');
    x.onclick = closePanel;
    head.appendChild(x);
    log = el('div', 'rja-log'); log.setAttribute('aria-live', 'polite');
    var form = el('form', 'rja-form');
    input = el('input', 'rja-in'); input.placeholder = L.ph; input.setAttribute('aria-label', L.ph); input.maxLength = 1500;
    mic = el('button', 'rja-mic', '🎙 ' + L.talk); mic.type = 'button'; mic.title = 'Voice conversation';
    var send = el('button', 'rja-send', L.send); send.type = 'submit';
    form.appendChild(input); form.appendChild(mic); form.appendChild(send);
    form.onsubmit = function (e) { e.preventDefault(); ask(input.value); };
    mic.onclick = toggleVoice;
    panel.appendChild(head); panel.appendChild(log); panel.appendChild(form);
    panel.appendChild(el('div', 'rja-note', L.note));
    document.body.appendChild(panel);
    render();
    input.focus();
  }

  function closePanel() {
    state.open = false; persist();
    stopVoice();
    if (panel) panel.style.display = 'none';
    btn.style.display = 'flex';
  }

  btn.onclick = openPanel;
  window.rjOpenAgent = function (prefill) { openPanel(); if (prefill) { input.value = prefill; input.focus(); } };
  document.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('[data-open-agent]');
    if (t) { e.preventDefault(); window.rjOpenAgent(t.getAttribute('data-open-agent') || ''); }
  });

  function ask(text) {
    text = (text || '').trim();
    if (!text || busy) return;
    input.value = '';
    state.messages.push({ role: 'user', content: text });
    persist(); render();
    busy = true;
    var typing = el('div', 'rja-m rja-a rja-typing'); typing.innerHTML = '<span></span><span></span><span></span>';
    log.appendChild(typing); log.scrollTop = log.scrollHeight;
    var history = state.messages.filter(function (m) { return m.role !== 'system'; });
    fetch('/api/chat', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages: history, page: location.pathname, language: navigator.language })
    }).then(function (r) { return r.json(); }).then(function (d) {
      state.messages.push({ role: 'assistant', content: d.reply || '…' });
      if (d.leadSaved) state.messages.push({ role: 'system', content: '✓ ' + L.saved });
      persist(); render();
      if (voiceOn) speak(d.reply);
    }).catch(function () {
      state.messages.push({ role: 'assistant', content: 'Connection problem. Email ryanjavaheri21@gmail.com and Ryan will reply.' });
      persist(); render();
    }).then(function () { busy = false; });
  }

  /* ---- Voice conversation: browser speech recognition + speech synthesis ---- */
  var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  var rec = null, voiceOn = false;
  var SPEECH = { es: 'es-ES', fa: 'fa-IR', he: 'he-IL', ar: 'ar-SA', zh: 'zh-CN', ko: 'ko-KR', ja: 'ja-JP', fr: 'fr-FR', pt: 'pt-BR', ru: 'ru-RU', hy: 'hy-AM', hi: 'hi-IN' };
  function speechLang() { return SPEECH[lang.slice(0, 2)] || navigator.language || 'en-US'; }
  function toggleVoice() { voiceOn ? stopVoice() : startVoice(); }
  function startVoice() {
    if (!SR || !window.speechSynthesis) { state.messages.push({ role: 'system', content: L.voiceOff }); render(); return; }
    voiceOn = true;
    mic.classList.add('on'); mic.textContent = '■ ' + L.stop;
    listen();
  }
  function stopVoice() {
    voiceOn = false;
    if (rec) { try { rec.abort(); } catch (e) {} rec = null; }
    if (window.speechSynthesis) window.speechSynthesis.cancel();
    if (mic) { mic.classList.remove('on'); mic.textContent = '🎙 ' + L.talk; }
    if (input) input.placeholder = L.ph;
  }
  function listen() {
    if (!voiceOn) return;
    rec = new SR();
    rec.lang = speechLang();
    rec.interimResults = true;
    rec.maxAlternatives = 1;
    input.placeholder = L.listening;
    var finalText = '';
    rec.onresult = function (e) {
      var t = '';
      for (var i = 0; i < e.results.length; i++) { t += e.results[i][0].transcript; if (e.results[i].isFinal) finalText = t; }
      input.value = t;
    };
    rec.onerror = function () {};
    rec.onend = function () {
      rec = null;
      var said = (finalText || input.value).trim();
      if (!voiceOn) return;
      if (said) ask(said); else setTimeout(listen, 300);
    };
    try { rec.start(); } catch (e) {}
  }
  function speak(text) {
    if (!window.speechSynthesis || !text) { listen(); return; }
    var u = new SpeechSynthesisUtterance(text);
    u.lang = speechLang();
    u.rate = 1.03;
    u.onend = function () { if (voiceOn) listen(); };
    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(u);
  }

  if (state.open) openPanel();
})();
