(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* Mobile menu + dropdowns */
  var burger = $('.burger'), links = $('.nav-links');
  if (burger && links) burger.addEventListener('click', function () {
    var open = links.classList.toggle('open');
    burger.setAttribute('aria-expanded', open);
    burger.textContent = open ? '✕' : '☰';
  });
  $$('.dd > button').forEach(function (b) {
    b.addEventListener('click', function () {
      var dd = b.parentNode, open = dd.classList.toggle('open');
      b.setAttribute('aria-expanded', open);
    });
  });
  $$('.nav-links a').forEach(function (a) {
    a.addEventListener('click', function () { if (links) links.classList.remove('open'); if (burger) burger.textContent = '☰'; });
  });

  /* Reveals */
  var els = $$('.reveal, .stagger, [data-play]');
  if ('IntersectionObserver' in window) {
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); } });
    }, { threshold: 0.12 });
    els.forEach(function (el) { obs.observe(el); });
  } else els.forEach(function (el) { el.classList.add('visible'); });

  /* Forms: contact / lead */
  $$('form[data-lead]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = $('.f-msg', form), btn = $('button[type=submit]', form);
      var data = {}; new FormData(form).forEach(function (v, k) { data[k] = v; });
      data.page = location.pathname; data.language = document.documentElement.lang;
      btn.disabled = true; msg.className = 'f-msg'; msg.textContent = '…';
      fetch('/api/lead', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) { return r.json(); })
        .then(function (d) {
          if (d.ok) { msg.className = 'f-msg ok'; msg.textContent = form.getAttribute('data-ok') || 'Thanks! Ryan will reach out personally.'; form.reset(); }
          else { msg.className = 'f-msg bad'; msg.textContent = d.error || 'Something went wrong.'; }
        })
        .catch(function () { msg.className = 'f-msg bad'; msg.textContent = 'Network error. Email ryanjavaheri21@gmail.com.'; })
        .then(function () { btn.disabled = false; });
    });
  });

  /* Book the 30-minute call from the scan results.
     If #scanResult has data-booking-url (set BOOKING_URL in tools/home.py), show a link to it.
     Otherwise show a short form: the visitor suggests times and it's saved as a 'call-request' lead. */
  var attr = function (t) { return String(t || '').replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); };
  function bookingBlock(data, score) {
    var url = ($('#scanResult') || document.body).getAttribute('data-booking-url') || '';
    var head = '<div class="book" id="book"><h4>Book your 30-minute call</h4>' +
      '<p>Go through these results with me and get a plan to raise your score.</p>';
    if (/^https:\/\//.test(url)) {
      return head + '<a class="btn btn-light" href="' + attr(url) + '" target="_blank" rel="noopener" style="margin-top:10px">Pick a time ›</a></div>';
    }
    return head +
      '<form class="book-form" novalidate>' +
      '<div class="fgrid">' +
      '<div><label class="f" for="b-n">Name *</label><input class="f-in" id="b-n" name="name" required maxlength="120" value="' + attr(data.name) + '"></div>' +
      '<div><label class="f" for="b-e">Email *</label><input class="f-in" id="b-e" name="email" type="email" required maxlength="200" value="' + attr(data.email) + '"></div>' +
      '<div class="full"><label class="f" for="b-t">Times that work for you *</label><input class="f-in" id="b-t" name="times" required maxlength="300" placeholder="e.g. Tue or Wed after 2pm, Fri morning"></div>' +
      '</div>' +
      '<div class="hp" aria-hidden="true"><input name="company_url_hp" tabindex="-1" autocomplete="off"></div>' +
      '<button class="btn btn-light" type="submit" style="margin-top:14px;width:100%">Request my call</button>' +
      '<p class="f-msg" aria-live="polite"></p>' +
      '<p class="f-note">I’ll email you to confirm a time. Your details only go to Ryan. See the <a href="/terms/" style="color:#a1a1a6">Terms</a> and <a href="/privacy/" style="color:#a1a1a6">Privacy Policy</a>.</p>' +
      '</form></div>';
  }
  function wireBooking(out, data, r, score) {
    var form = $('.book-form', out);
    if (!form) return;
    var tz = '';
    try { tz = Intl.DateTimeFormat().resolvedOptions().timeZone || ''; } catch (e) {}
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = $('.f-msg', form), btn = $('button[type=submit]', form);
      var f = {}; new FormData(form).forEach(function (v, k) { f[k] = String(v).trim(); });
      if (!f.name || !f.email || !f.times) { msg.className = 'f-msg bad'; msg.textContent = 'Add your name, email and a few times that work.'; return; }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f.email)) { msg.className = 'f-msg bad'; msg.textContent = 'Check your email address.'; return; }
      btn.disabled = true; msg.className = 'f-msg'; msg.textContent = '…';
      fetch('/api/lead', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          source: 'call-request',
          company_url_hp: f.company_url_hp,
          name: f.name, email: f.email,
          company: data.business, website: data.website,
          need: '30-minute call after the free AI scan (score ' + score + ')',
          details: 'Times that work: ' + f.times + (tz ? ' (time zone: ' + tz + ')' : ''),
          timeline: f.times,
          page: '/#scan', language: document.documentElement.lang,
          extra: { scan: r, city: data.city, category: data.category, timeZone: tz }
        })
      })
        .then(function (res) { return res.json(); })
        .then(function (d) {
          if (d.ok) {
            form.innerHTML = '<p class="f-msg ok">Thanks, ' + attr(f.name.split(' ')[0]) + '! I’ll email you at ' + attr(f.email) + ' to confirm a time.</p>';
          } else { msg.className = 'f-msg bad'; msg.textContent = d.error || 'Something went wrong.'; btn.disabled = false; }
        })
        .catch(function () { msg.className = 'f-msg bad'; msg.textContent = 'Network error. Email ryanjavaheri21@gmail.com.'; btn.disabled = false; });
    });
  }

  /* Free AI visibility scan */
  var scan = $('#scanForm');
  if (scan) scan.addEventListener('submit', function (e) {
    e.preventDefault();
    var btn = $('button[type=submit]', scan), msg = $('.f-msg', scan), out = $('#scanResult');
    var data = {}; new FormData(scan).forEach(function (v, k) { data[k] = v; });
    btn.disabled = true; btn.textContent = 'Scanning AI answers…'; msg.textContent = '';
    fetch('/api/scan', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
      .then(function (r) { return r.json(); })
      .then(function (d) {
        if (!d.result) { msg.className = 'f-msg bad'; msg.textContent = d.error || 'Scan failed.'; return; }
        var r = d.result, s = Math.round(r.score);
        var esc = function (t) { var x = document.createElement('div'); x.textContent = t; return x.innerHTML; };
        out.innerHTML =
          '<div class="score"><div class="ring" style="--p:' + s + '"><b>' + s + '</b></div><div><b style="color:#fff;font-size:18px">AI visibility score</b><p>' +
          (r.recognized === 'yes' ? 'AI models recognize you.' : r.recognized === 'partly' ? 'AI models only partly recognize you.' : "AI models don't recognize you yet. That's what we fix.") + '</p></div></div>' +
          '<h4>What an AI model says about you today</h4><p>' + esc(r.whatAiSays) + '</p>' +
          '<h4>Questions your customers ask AI</h4><ul>' + r.likelyQuestions.map(function (q) { return '<li>' + esc(q) + '</li>'; }).join('') + '</ul>' +
          '<h4>Quick wins</h4><ul>' + r.quickWins.map(function (q) { return '<li>' + esc(q) + '</li>'; }).join('') + '</ul>' +
          '<p style="margin-top:16px;font-size:13px;color:#86868b!important">Snapshot from one AI model’s built-in knowledge. A full audit checks ChatGPT, Claude, Gemini and Perplexity with live search.</p>' +
          bookingBlock(data, s);
        out.classList.add('show');
        wireBooking(out, data, r, s);
        if (data.email) { msg.className = 'f-msg ok'; msg.textContent = 'Ryan got your scan and will send a full audit.'; }
      })
      .catch(function () { msg.className = 'f-msg bad'; msg.textContent = 'Network error.'; })
      .then(function () { btn.disabled = false; btn.textContent = 'Run my free scan'; });
  });

  /* AI answer typing mockup */
  var ans = $('#aiAnswer');
  if (ans) {
    var full = ans.getAttribute('data-text');
    if (reduced) ans.innerHTML = full;
    else {
      var plain = full.replace(/<[^>]+>/g, '');
      var i = 0;
      var caret = '<span class="caret"></span>';
      var tick = function () {
        i += 2;
        if (i >= plain.length) { ans.innerHTML = full; $('#aiSources') && ($('#aiSources').style.opacity = 1); return; }
        // map plain index back onto html, keeping tags intact
        var out = '', n = 0, inTag = false;
        for (var k = 0; k < full.length && n < i; k++) {
          var c = full[k];
          if (c === '<') inTag = true;
          out += c;
          if (!inTag) n++;
          if (c === '>') inTag = false;
        }
        if ((out.match(/<b>/g) || []).length > (out.match(/<\/b>/g) || []).length) out += '</b>';
        ans.innerHTML = out + caret;
        setTimeout(tick, 22);
      };
      var started = false, startTyping = function () { if (!started) { started = true; setTimeout(tick, 1300); } };
      var host = ans.closest('[data-play]');
      if (host && 'IntersectionObserver' in window) {
        var io = new IntersectionObserver(function (en) { if (en[0].isIntersecting) { startTyping(); io.disconnect(); } }, { threshold: 0.3 });
        io.observe(host);
      } else startTyping();
    }
  }

  var nav = $('nav.site'), progress = $('#progress');
  var heroContent = $('#heroContent'), orbs = $$('.intro-wrap .orb'), cue = $('#scrollCue');
  var list = $('#scrubList'), words = [];
  var track = $('#slideshowTrack'), slides = track ? $('#slideshowStage').children : [], dots = track ? $('#slideDots').children : [];

  if (!reduced) {
    $$('[data-split]').forEach(function (h1) {
      var nodes = Array.prototype.slice.call(h1.childNodes), idx = 0, base = h1.closest('[data-play]') ? 0.15 : 0.08;
      h1.innerHTML = '';
      nodes.forEach(function (node) {
        if (node.nodeType === 1 && node.tagName === 'BR') { h1.appendChild(document.createElement('br')); return; }
        var target = h1, text = node.textContent;
        if (node.nodeType === 1) { target = node.cloneNode(false); h1.appendChild(target); }
        text.replace(/\n/g, '').split(' ').forEach(function (word, wi) {
          if (wi > 0) { target.appendChild(document.createTextNode(' ')); idx++; }
          if (!word) return;
          var w = document.createElement('span');
          w.style.display = 'inline-block'; w.style.whiteSpace = 'nowrap';
          word.split('').forEach(function (c) {
            var s = document.createElement('span');
            s.className = 'ch';
            s.textContent = c;
            s.style.animationDelay = (base + idx++ * 0.035) + 's';
            w.appendChild(s);
          });
          target.appendChild(w);
        });
      });
    });
    if (list) {
      $$('li', list).forEach(function (li) {
        li.innerHTML = li.textContent.split(' ').map(function (w) { return '<span class="w" style="opacity:0.18">' + w + '</span>'; }).join(' ');
      });
      words = $$('.w', list);
    }
    $$('.card').forEach(function (card) {
      card.addEventListener('mousemove', function (e) {
        var b = card.getBoundingClientRect();
        var rx = ((e.clientY - b.top) / b.height - 0.5) * -5;
        var ry = ((e.clientX - b.left) / b.width - 0.5) * 5;
        card.style.transform = 'translateY(-8px) scale(1.015) rotateX(' + rx + 'deg) rotateY(' + ry + 'deg)';
      });
      card.addEventListener('mouseleave', function () { card.style.transform = ''; });
    });
  }

  var ticking = false;
  function update() {
    ticking = false;
    var y = window.scrollY, vh = window.innerHeight;
    if (nav) nav.classList.toggle('scrolled', y > 10);
    if (progress) {
      var max = document.documentElement.scrollHeight - vh;
      progress.style.transform = 'scaleX(' + (max > 0 ? y / max : 0) + ')';
    }
    if (reduced) return;
    if (heroContent) {
      var h = Math.min(y / 600, 1);
      heroContent.style.transform = 'translateY(' + y * 0.25 + 'px)';
      heroContent.style.opacity = 1 - h * 0.8;
    }
    if (cue) cue.style.visibility = y > 60 ? 'hidden' : '';
    orbs.forEach(function (o) { o.style.transform = 'translateY(' + y * parseFloat(o.dataset.speed || 0.3) + 'px)'; });
    if (words.length) {
      var r = list.getBoundingClientRect();
      var p = Math.max(0, Math.min(1, (vh * 0.85 - r.top) / (r.height + vh * 0.35)));
      var lit = Math.floor(p * words.length);
      for (var i = 0; i < words.length; i++) words[i].style.opacity = i < lit ? 1 : 0.18;
    }
    if (track && !window.matchMedia('(max-width: 700px)').matches) {
      var tr = track.getBoundingClientRect();
      var total = track.offsetHeight - vh;
      var sp = Math.max(0, Math.min(1, -tr.top / total));
      var pos = sp * (slides.length - 1);
      for (var j = 0; j < slides.length; j++) {
        var d = pos - j, a = Math.abs(d);
        slides[j].style.opacity = Math.max(0, 1 - a * 1.15);
        slides[j].style.transform = 'translateX(' + (-d * 110) + 'px) translateY(' + (Math.min(a, 1) * 18) + 'px) scale(' + (1 - Math.min(a, 1) * 0.07) + ') rotateY(' + (-d * 7) + 'deg)';
        slides[j].style.zIndex = 10 - Math.round(a);
      }
      var active = Math.round(pos);
      for (var k = 0; k < dots.length; k++) dots[k].classList.toggle('on', k === active);
    }
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  update();
})();
