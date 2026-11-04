(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const WA = 'https://wa.me/5511945498733?text=';

  // menu no celular
  const top = $('#top'), burger = $('.burger');
  if (burger) {
    const close = () => { top.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); };
    burger.addEventListener('click', () => { const o = top.classList.toggle('open'); burger.setAttribute('aria-expanded', o); });
    $$('.nav__links a').forEach((a) => a.addEventListener('click', close));
    addEventListener('keydown', (e) => { if (e.key === 'Escape' && top.classList.contains('open')) { close(); burger.focus(); } });
  }

  // fundo: chuva de código azul + rede de pontos ligados
  const cv = $('#bg');
  if (cv) {
    const cx = cv.getContext('2d');
    const glyphs = '01<>{}[]/=+*#$%&;:ABCDEFabcdef0123456789'.split('');
    let W, H, cols, drops, nodes, size = 15, raf, mx = -999, my = -999;
    const init = () => {
      const dpr = Math.min(devicePixelRatio || 1, 2);
      W = innerWidth; H = innerHeight;
      cv.width = W * dpr; cv.height = H * dpr; cx.setTransform(dpr, 0, 0, dpr, 0, 0);
      cols = Math.ceil(W / size);
      drops = Array.from({ length: cols }, () => Math.random() * -H / size);
      const n = Math.round(Math.min(70, (W * H) / 26000));
      nodes = Array.from({ length: n }, () => ({ x: Math.random() * W, y: Math.random() * H, vx: (Math.random() - .5) * .35, vy: (Math.random() - .5) * .35 }));
      cx.fillStyle = '#04070d'; cx.fillRect(0, 0, W, H);
      drops = drops.map(() => Math.random() * H / size);
      for (let k = 0; k < 70; k++) rainStep();
    };
    const rainStep = () => {
      cx.fillStyle = 'rgba(4,7,13,.1)'; cx.fillRect(0, 0, W, H);
      cx.font = size + 'px JBMono, monospace';
      for (let i = 0; i < cols; i++) {
        const y = drops[i] * size;
        cx.fillStyle = Math.random() > .95 ? 'rgba(200,245,255,.95)' : 'rgba(30,125,255,.7)';
        cx.fillText(glyphs[(Math.random() * glyphs.length) | 0], i * size, y);
        if (y > H && Math.random() > .975) drops[i] = 0;
        drops[i] += .55;
      }
    };
    const frame = () => {
      rainStep();
      cx.lineWidth = 1;
      for (const a of nodes) {
        a.x += a.vx; a.y += a.vy;
        if (a.x < 0 || a.x > W) a.vx *= -1;
        if (a.y < 0 || a.y > H) a.vy *= -1;
        for (const b of nodes) {
          const d = Math.hypot(a.x - b.x, a.y - b.y);
          if (d < 130 && a < b) { cx.strokeStyle = `rgba(34,211,255,${(1 - d / 130) * .35})`; cx.beginPath(); cx.moveTo(a.x, a.y); cx.lineTo(b.x, b.y); cx.stroke(); }
        }
        const dm = Math.hypot(a.x - mx, a.y - my);
        if (dm < 160) { cx.strokeStyle = `rgba(34,211,255,${(1 - dm / 160) * .6})`; cx.beginPath(); cx.moveTo(a.x, a.y); cx.lineTo(mx, my); cx.stroke(); }
        cx.fillStyle = 'rgba(120,225,255,.85)'; cx.beginPath(); cx.arc(a.x, a.y, 1.6, 0, 6.3); cx.fill();
      }
      raf = requestAnimationFrame(frame);
    };
    init();
    addEventListener('resize', () => { cancelAnimationFrame(raf); init(); if (!still) frame(); });
    addEventListener('pointermove', (e) => { mx = e.clientX; my = e.clientY; }, { passive: true });
    document.addEventListener('visibilitychange', () => { cancelAnimationFrame(raf); if (!document.hidden && !still) frame(); });
    if (still) { frame(); cancelAnimationFrame(raf); } else frame();
  }

  // título que troca a palavra como dado decodificando
  const word = $('#word');
  if (word && !still) {
    const list = word.dataset.words.split('|'), pool = '01{}<>/#$%'.split('');
    let k = 0;
    const swap = () => {
      const to = list[(k = (k + 1) % list.length)];
      let t = 0;
      const id = setInterval(() => {
        t++;
        word.textContent = [...to].map((ch, i) => (i < t / 2 ? ch : ch === ' ' ? ' ' : pool[(Math.random() * pool.length) | 0])).join('');
        if (t / 2 >= to.length) { clearInterval(id); word.textContent = to; }
      }, 40);
    };
    setInterval(swap, 3200);
  }

  // seção fixa: rola a página, troca texto e foto no mesmo lugar
  const pin = $('#solucoes');
  if (pin) {
    const data = JSON.parse($('#pdata').textContent);
    const stage = $('.pin__stage', pin), imgs = $$('.pin__img img', pin), ticks = $$('.pin__ticks i', pin), btnsL = $$('#plist button');
    const pt = $('#pt'), ps = $('#ps'), ptag = $('#ptag'), pgo = $('#pgo'), pcap = $('#pcap'), wire = $('#wire'), grid = $('.pin__grid', pin), media = $('.pin__img', pin);
    let cur = -1;
    const place = () => {
      const b = btnsL[cur]; if (!b || getComputedStyle(b.parentElement.parentElement).display === 'none') { wire.style.opacity = 0; return; }
      const g = grid.getBoundingClientRect(), r = b.getBoundingClientRect(), m = media.getBoundingClientRect();
      wire.style.left = (r.right - g.left) + 'px'; wire.style.width = Math.max(0, m.left - r.right) + 'px'; wire.style.top = (r.top + r.height / 2 - g.top) + 'px'; wire.style.opacity = 1;
      pin.style.setProperty('--h', (m.height - 2) + 'px');
    };
    const show = (i) => {
      if (i === cur) return; cur = i; const d = data[i];
      imgs.forEach((im, k) => im.classList.toggle('on', k === i));
      ticks.forEach((t, k) => t.classList.toggle('on', k === i));
      btnsL.forEach((b, k) => b.setAttribute('aria-current', k === i));
      pt.innerHTML = '<span class="c" aria-hidden="true">&gt;</span> ' + d.t; ps.textContent = d.d; ptag.textContent = d.tag; pcap.textContent = d.p + '.jpg';
      pgo.href = 'agendar.html?s=' + encodeURIComponent(d.g) + '#agendar'; place();
    };
    const onScroll = () => {
      const rect = pin.getBoundingClientRect(), navH = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--nav')) || 56;
      const total = pin.offsetHeight - stage.offsetHeight;
      const p = Math.min(0.9999, Math.max(0, (navH - rect.top) / total));
      show(Math.floor(p * data.length));
    };
    btnsL.forEach((b, k) => b.addEventListener('click', () => {
      const total = pin.offsetHeight - stage.offsetHeight;
      scrollTo({ top: pin.getBoundingClientRect().top + scrollY - (parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--nav')) || 56) + (k + .5) / data.length * total, behavior: still ? 'auto' : 'smooth' });
    }));
    let tk = false;
    addEventListener('scroll', () => { if (!tk) { tk = true; requestAnimationFrame(() => { tk = false; onScroll(); }); } }, { passive: true });
    addEventListener('resize', () => { place(); onScroll(); });
    show(0); onScroll();
  }

  // formulário de orçamento -> e-mail pronto
  const form = $('#form');
  if (form) {
    const wanted = (new URLSearchParams(location.search).get('s') || '').split(',');
    $$('#opts input').forEach((o) => { o.checked = wanted.includes(o.value); });
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const nome = form.nome.value.trim(), err = $('#err');
      err.hidden = !!nome;
      form.nome.setAttribute('aria-invalid', nome ? 'false' : 'true');
      if (!nome) { form.nome.focus(); return; }
      const serv = $$('input[name=s]:checked', form).map((x) => x.value);
      const body = ['Olá, AtomTuring!', '', `Meu nome é ${nome}.`, form.tel.value.trim() && `Telefone: ${form.tel.value.trim()}`, serv.length && `Preciso de: ${serv.join(', ')}.`, form.msg.value.trim() && `Detalhes: ${form.msg.value.trim()}`].filter(Boolean).join('\n');
      location.href = `mailto:contato.atomturing@gmail.com?subject=${encodeURIComponent('Orçamento' + (serv.length ? ' — ' + serv.join(', ') : ''))}&body=${encodeURIComponent(body)}`;
    });
  }

  // agendamento -> WhatsApp com mensagem pronta
  const ag = $('#ag');
  if (ag) {
    const wanted = (new URLSearchParams(location.search).get('s') || '').split(',');
    $$('#aopts input').forEach((o) => { o.checked = wanted.includes(o.value); });
    const d = new Date(); d.setMinutes(d.getMinutes() - d.getTimezoneOffset());
    ag.dia.min = d.toISOString().slice(0, 10);
    ag.addEventListener('submit', (e) => {
      e.preventDefault();
      const nome = ag.nome.value.trim(), err = $('#aerr');
      err.hidden = !!nome;
      ag.nome.setAttribute('aria-invalid', nome ? 'false' : 'true');
      if (!nome) { ag.nome.focus(); return; }
      const serv = $$('input[name=s]:checked', ag).map((x) => x.value);
      const dia = ag.dia.value && ag.dia.value.split('-').reverse().join('/');
      const per = $('input[name=per]:checked', ag).value;
      const txt = ['Olá, AtomTuring! Quero agendar um atendimento.', `Meu nome é ${nome}.`, serv.length && `Preciso de: ${serv.join(', ')}.`, dia && `Melhor dia: ${dia}.`, per !== 'Combinar na conversa' && `Período: ${per}.`, ag.msg.value.trim() && `Detalhes: ${ag.msg.value.trim()}`].filter(Boolean).join('\n');
      window.open(WA + encodeURIComponent(txt), '_blank', 'noopener');
    });
  }

  // pacote empresarial -> WhatsApp (sem preço)
  const pk = $('#pkg');
  if (pk) {
    pk.addEventListener('submit', (e) => {
      e.preventDefault();
      const itens = $$('input[name=item]:checked', pk).map((i) => i.value);
      const txt = ['Olá, AtomTuring! Quero consultar valores do pacote empresarial.', itens.length && `Itens: ${itens.join(', ')}.`, pk.qtd.value && `Equipamentos: ${pk.qtd.value}.`].filter(Boolean).join('\n');
      window.open(WA + encodeURIComponent(txt), '_blank', 'noopener');
    });
  }

  // entrada dos blocos
  if (!still) {
    const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: 0.12 });
    $$('.rv').forEach((el) => io.observe(el));
  } else $$('.rv').forEach((el) => el.classList.add('in'));
})();
