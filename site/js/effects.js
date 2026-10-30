(() => {
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const WA = 'https://wa.me/5511945498733?text=';

  // ---- revelar com desfoque: separa o texto em palavras
  const splitWords = (el) => {
    let i = 0;
    const walk = (node) => {
      [...node.childNodes].forEach((n) => {
        if (n.nodeType === 3) {
          const frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach((part) => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.append(' '); return; }
            const s = document.createElement('span');
            s.className = 'w'; s.style.setProperty('--i', i++); s.textContent = part;
            frag.append(s);
          });
          n.replaceWith(frag);
        } else if (n.nodeType === 1 && n.tagName !== 'BR') walk(n);
      });
    };
    walk(el);
  };
  $$('.br').forEach(splitWords);

  // ---- texto "decodificando"
  const GLYPHS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#%&*';
  const scramble = (el) => {
    const finalText = el.dataset.text || el.textContent;
    el.dataset.text = finalText;
    if (still) { el.textContent = finalText; return; }
    const start = performance.now(), dur = 900;
    const tick = (t) => {
      const p = Math.min(1, (t - start) / dur);
      el.textContent = [...finalText].map((c, i) => (c === ' ' || i < p * finalText.length) ? c : GLYPHS[Math.random() * GLYPHS.length | 0]).join('');
      if (p < 1) requestAnimationFrame(tick); else el.textContent = finalText;
    };
    requestAnimationFrame(tick);
  };
  $$('[data-scramble]').forEach((el) => { el.dataset.text = el.textContent; if (!still) el.style.visibility = 'hidden'; });

  // ---- observador único para os efeitos de entrada
  const io = new IntersectionObserver((es) => {
    es.forEach((e) => {
      if (!e.isIntersecting) return;
      const el = e.target; io.unobserve(el);
      if (el.hasAttribute('data-scramble')) { el.style.visibility = ''; scramble(el); }
      else el.classList.add('in');
    });
  }, { threshold: 0.35, rootMargin: '0px 0px -8% 0px' });
  $$('.br, .hl, .ck[data-draw], [data-scramble]').forEach((el) => (still ? (el.hasAttribute('data-scramble') ? null : el.classList.add('in')) : io.observe(el)));

  // ---- marquee: duplica o conteúdo para o laço ficar contínuo
  $$('.marquee__track').forEach((t) => { t.innerHTML += t.innerHTML; t.setAttribute('aria-hidden', 'false'); });

  // ---- trilho com rolagem lateral (setas, barra, arrastar)
  $$('.rail-wrap').forEach((w) => {
    const rail = $$('.rail', w)[0], prev = $$('.rail-btn', w)[0], next = $$('.rail-btn', w)[1], bar = $$('.rail-bar i', w)[0];
    const step = () => rail.children[0].getBoundingClientRect().width + 16;
    const update = () => {
      const max = rail.scrollWidth - rail.clientWidth;
      const p = max > 0 ? rail.scrollLeft / max : 0, size = rail.clientWidth / rail.scrollWidth;
      bar.style.width = `${Math.max(12, size * 100)}%`;
      bar.style.transform = `translateX(${p * (100 / size - 100)}%)`;
      prev.disabled = rail.scrollLeft < 4; next.disabled = rail.scrollLeft > max - 4;
    };
    prev.onclick = () => rail.scrollBy({ left: -step(), behavior: still ? 'auto' : 'smooth' });
    next.onclick = () => rail.scrollBy({ left: step(), behavior: still ? 'auto' : 'smooth' });
    rail.addEventListener('scroll', () => requestAnimationFrame(update), { passive: true });
    addEventListener('resize', update); update();
    let down = false, sx = 0, sl = 0, moved = false;
    rail.addEventListener('pointerdown', (e) => { if (e.pointerType !== 'mouse') return; down = true; moved = false; sx = e.clientX; sl = rail.scrollLeft; });
    addEventListener('pointermove', (e) => { if (!down) return; const dx = e.clientX - sx; if (Math.abs(dx) > 4) { moved = true; rail.classList.add('drag'); } rail.scrollLeft = sl - dx; });
    addEventListener('pointerup', () => { if (!down) return; down = false; rail.classList.remove('drag'); });
    rail.addEventListener('click', (e) => { if (moved) { e.preventDefault(); moved = false; } }, true);
  });

  // ---- carimbo do rodapé: hora de São Paulo ao vivo
  const clock = document.getElementById('clock');
  if (clock) {
    const f = new Intl.DateTimeFormat('pt-BR', { timeZone: 'America/Sao_Paulo', hour: '2-digit', minute: '2-digit', second: '2-digit' });
    const tick = () => { clock.textContent = f.format(new Date()); };
    tick(); setInterval(tick, 1000);
  }

  // ---- atalhos de teclado: Alt+W (WhatsApp) e Alt+O (orçamento). Com Alt, para não atrapalhar quem digita ou usa leitor de tela (WCAG 2.1.4)
  const keys = { KeyW: ['w', () => window.open(WA + encodeURIComponent('Olá, AtomTuring! Quero um orçamento.'), '_blank', 'noopener')], KeyO: ['o', () => { location.href = 'orcamento.html'; }] };
  addEventListener('keydown', (e) => {
    if (!e.altKey || e.metaKey || e.ctrlKey || /input|textarea|select/i.test(e.target.tagName) || !keys[e.code]) return;
    e.preventDefault();
    $$('.kbd[data-key="' + keys[e.code][0] + '"]').forEach((el) => el.classList.add('on'));
    keys[e.code][1]();
  });
  addEventListener('keyup', () => $$('.kbd.on').forEach((el) => el.classList.remove('on')));

  // ---- monte o seu pacote -> mensagem de WhatsApp (sem preço)
  const pk = document.getElementById('pkg');
  if (pk) {
    pk.addEventListener('submit', (e) => {
      e.preventDefault();
      const itens = $$('input[name=item]:checked', pk).map((i) => i.value);
      const qtd = pk.qtd.value;
      const txt = ['Olá, AtomTuring! Quero consultar valores do pacote empresarial.',
        itens.length ? `Itens: ${itens.join(', ')}.` : '',
        qtd ? `Equipamentos: ${qtd}.` : ''].filter(Boolean).join('\n');
      window.open(WA + encodeURIComponent(txt), '_blank', 'noopener');
    });
  }
})();

// fundo do topo: leve paralaxe com o mouse
(() => {
  const hero = document.querySelector('.hero');
  if (!hero || matchMedia('(prefers-reduced-motion: reduce)').matches || !matchMedia('(hover: hover)').matches) return;
  hero.addEventListener('pointermove', (e) => {
    const r = hero.getBoundingClientRect();
    hero.style.setProperty('--mx', ((e.clientX - r.left) / r.width - 0.5) * 2);
    hero.style.setProperty('--my', ((e.clientY - r.top) / r.height - 0.5) * 2);
  });
  hero.addEventListener('pointerleave', () => { hero.style.setProperty('--mx', 0); hero.style.setProperty('--my', 0); });
})();
