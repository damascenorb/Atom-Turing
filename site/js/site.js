(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const WA = 'https://wa.me/5511945498733?text=';

  // menu no celular
  const top = $('#top'), burger = $('.burger');
  if (burger) {
    burger.addEventListener('click', () => { const o = top.classList.toggle('open'); burger.setAttribute('aria-expanded', o); });
    $$('.nav__links a').forEach((a) => a.addEventListener('click', () => { top.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); }));
    addEventListener('keydown', (e) => { if (e.key === 'Escape' && top.classList.contains('open')) { top.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); burger.focus(); } });
  }

  // galeria lateral: setas
  const rail = $('.rail');
  if (rail) {
    const [prev, next] = $$('.rail-btn');
    const step = () => rail.children[0].getBoundingClientRect().width + 20;
    const update = () => { prev.disabled = rail.scrollLeft < 4; next.disabled = rail.scrollLeft > rail.scrollWidth - rail.clientWidth - 4; };
    prev.onclick = () => rail.scrollBy({ left: -step(), behavior: still ? 'auto' : 'smooth' });
    next.onclick = () => rail.scrollBy({ left: step(), behavior: still ? 'auto' : 'smooth' });
    rail.addEventListener('scroll', () => requestAnimationFrame(update), { passive: true });
    addEventListener('resize', update); update();
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

  // movimento: entrada dos textos e leve paralaxe das fotos
  if (!still) {
    const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: 0.18, rootMargin: '0px 0px -6% 0px' });
    $$('.rv').forEach((el) => io.observe(el));
    const imgs = $$('.tile__img img');
    let tick = false;
    const par = () => {
      tick = false;
      const vh = innerHeight;
      imgs.forEach((im) => {
        const r = im.parentElement.getBoundingClientRect();
        if (r.bottom < -100 || r.top > vh + 100) return;
        const p = (r.top + r.height / 2 - vh / 2) / (vh / 2 + r.height / 2);
        im.style.setProperty('--py', (Math.max(-1, Math.min(1, p)) * -4.5).toFixed(2) + '%');
      });
    };
    addEventListener('scroll', () => { if (!tick) { tick = true; requestAnimationFrame(par); } }, { passive: true });
    addEventListener('resize', par); par();
  } else {
    $$('.rv').forEach((el) => el.classList.add('in'));
  }
})();
