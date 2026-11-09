(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const WA = 'https://wa.me/5511945498733?text=';
  const MAIL = 'contato.atomturing@gmail.com';

  // menu no celular
  const nav = $('#top'), burger = $('.burger');
  if (burger) {
    const close = (focus) => { nav.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); burger.setAttribute('aria-label', 'Abrir menu'); document.body.style.overflow = ''; if (focus) burger.focus(); };
    burger.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open);
      burger.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
      document.body.style.overflow = open ? 'hidden' : '';
    });
    $$('.nav__links a').forEach((a) => a.addEventListener('click', () => close(false)));
    addEventListener('keydown', (e) => { if (e.key === 'Escape' && nav.classList.contains('open')) close(true); });
    matchMedia('(min-width:1001px)').addEventListener('change', (m) => { if (m.matches) close(false); });
  }

  // problemas: um item aberto por vez, foto acompanha
  const probs = $('#probs');
  if (probs) {
    const items = $$('.prob', probs), imgs = $$('.espec__ph img');
    const open = (i) => {
      items.forEach((li, k) => { const on = k === i; li.classList.toggle('is-on', on); $('button', li).setAttribute('aria-expanded', on); });
      imgs.forEach((im, k) => im.classList.toggle('on', k === i));
    };
    items.forEach((li, k) => $('button', li).addEventListener('click', () => open(k)));
  }

  // botão do WhatsApp no celular: só aparece depois que o visitante rola um pouco
  const fab = $('.fab');
  if (fab) {
    const upd = () => fab.classList.toggle('is-on', scrollY > 520);
    addEventListener('scroll', upd, { passive: true }); upd();
  }

  // entrada suave dos blocos (sem script, tudo aparece)
  const rv = $$('.rv');
  if (!still && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: 0.12, rootMargin: '0px 0px -5% 0px' });
    rv.forEach((el) => io.observe(el));
  } else rv.forEach((el) => el.classList.add('in'));

  // formulários
  const status = (form, html) => { const s = $('.status', form); s.innerHTML = html; s.hidden = false; };
  const needName = (form, errId) => {
    const nome = form.nome.value.trim(), err = $('#' + errId);
    err.hidden = !!nome;
    form.nome.setAttribute('aria-invalid', nome ? 'false' : 'true');
    if (!nome) form.nome.focus();
    return nome;
  };
  const wanted = () => (new URLSearchParams(location.search).get('s') || '').split(',');
  const picked = (form) => $$('input[name=s]:checked', form).map((x) => x.value);

  const form = $('#form');
  if (form) {
    $$('#opts input').forEach((o) => { o.checked = wanted().includes(o.value); });
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const nome = needName(form, 'err'); if (!nome) return;
      const serv = picked(form);
      const body = ['Olá, AtomTuring!', '', `Meu nome é ${nome}.`, form.tel.value.trim() && `Telefone: ${form.tel.value.trim()}`, serv.length && `Preciso de: ${serv.join(', ')}.`, form.msg.value.trim() && `Detalhes: ${form.msg.value.trim()}`].filter(Boolean).join('\n');
      const href = `mailto:${MAIL}?subject=${encodeURIComponent('Orçamento' + (serv.length ? ' — ' + serv.join(', ') : ''))}&body=${encodeURIComponent(body)}`;
      status(form, `Abrindo o seu e-mail com a mensagem pronta. Se nada abrir, escreva para <a class="tl" href="${href}">${MAIL}</a> ou chame no WhatsApp.`);
      location.href = href;
    });
  }

  const ag = $('#ag');
  if (ag) {
    $$('#aopts input').forEach((o) => { o.checked = wanted().includes(o.value); });
    const d = new Date(); d.setMinutes(d.getMinutes() - d.getTimezoneOffset());
    ag.dia.min = d.toISOString().slice(0, 10);
    ag.addEventListener('submit', (e) => {
      e.preventDefault();
      const nome = needName(ag, 'aerr'); if (!nome) return;
      const serv = picked(ag);
      const dia = ag.dia.value && ag.dia.value.split('-').reverse().join('/');
      const per = $('input[name=per]:checked', ag).value;
      const txt = ['Olá, AtomTuring! Quero agendar um atendimento.', `Meu nome é ${nome}.`, serv.length && `Preciso de: ${serv.join(', ')}.`, dia && `Melhor dia: ${dia}.`, per !== 'Combinar na conversa' && `Período: ${per}.`, ag.msg.value.trim() && `Detalhes: ${ag.msg.value.trim()}`].filter(Boolean).join('\n');
      const href = WA + encodeURIComponent(txt);
      status(ag, `Abrindo o WhatsApp com a sua mensagem. Se não abrir, <a class="tl" href="${href}" target="_blank" rel="noopener">toque aqui</a>.`);
      window.open(href, '_blank', 'noopener');
    });
  }

  const pk = $('#pkg');
  if (pk) {
    pk.addEventListener('submit', (e) => {
      e.preventDefault();
      const itens = $$('input[name=item]:checked', pk).map((i) => i.value);
      const txt = ['Olá, AtomTuring! Quero consultar valores do pacote empresarial.', itens.length && `Itens: ${itens.join(', ')}.`, pk.qtd.value && `Equipamentos: ${pk.qtd.value}.`].filter(Boolean).join('\n');
      const href = WA + encodeURIComponent(txt);
      status(pk, `Abrindo o WhatsApp com os itens escolhidos. Se não abrir, <a class="tl" href="${href}" target="_blank" rel="noopener">toque aqui</a>.`);
      window.open(href, '_blank', 'noopener');
    });
  }
})();
