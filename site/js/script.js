const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];

// menu no celular
const nav = $('.nav'), toggle = $('.nav__toggle');
if (toggle) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open);
  });
  $$('.nav__links a').forEach((a) => a.addEventListener('click', () => nav.classList.remove('open')));
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
    if (!nome) { form.nome.focus(); return; }
    const serv = $$('input[name=s]:checked', form).map((x) => x.value);
    const body = [
      'Olá, AtomTuring!', '',
      `Meu nome é ${nome}.`,
      form.tel.value.trim() && `Telefone: ${form.tel.value.trim()}`,
      serv.length && `Preciso de: ${serv.join(', ')}.`,
      form.msg.value.trim() && `Detalhes: ${form.msg.value.trim()}`,
    ].filter(Boolean).join('\n');
    const subj = `Orçamento${serv.length ? ' — ' + serv.join(', ') : ''}`;
    location.href = `mailto:contato.atomturing@gmail.com?subject=${encodeURIComponent(subj)}&body=${encodeURIComponent(body)}`;
  });
}
