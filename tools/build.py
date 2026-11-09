"""Gera as páginas do site AtomTuring em site/*.html.  Uso: python3 -I tools/build.py site"""
import json, os, sys
from urllib.parse import quote

OUT = sys.argv[1]
SITE = "https://atomturing.vercel.app"
WA = "https://wa.me/5511945498733?text=Ol%C3%A1%2C%20AtomTuring!%20Quero%20um%20or%C3%A7amento."
IG = "https://instagram.com/Atomturing"
MAIL = "contato.atomturing@gmail.com"
NB = '<span class="sr-only"> (abre em nova aba)</span>'
NAVP = [("computadores.html", "Computadores"), ("redes.html", "Redes e Wi‑Fi"), ("empresas.html", "Empresas"), ("como-funciona.html", "Como funciona"), ("orcamento.html", "Orçamento")]
MAN = json.load(open(os.path.join(OUT, "assets", "photos", "manifest.json")))


def pic(name, alt, sizes="100vw", eager=False, cls="", pos=""):
    w, h = MAN[name]
    w1 = min(1200, w)
    style = f' style="object-position:{pos}"' if pos else ""
    return (f'<img{f" class={cls}" if cls else ""} src="assets/photos/{name}-640.webp" srcset="assets/photos/{name}-640.webp 640w, assets/photos/{name}-1200.webp {w1}w" '
            f'sizes="{sizes}" width="{w1}" height="{round(h * w1 / w)}" alt="{alt}"{style}{"" if eager else " loading=lazy decoding=async"}>')


def og(name):
    return f"{SITE}/assets/photos/{name}-1200.webp"


LD = {"@context": "https://schema.org", "@type": "ProfessionalService", "name": "AtomTuring", "url": SITE + "/",
      "description": "Manutenção de computadores e redes: manutenção preventiva e corretiva, formatação, limpeza, troca de peças, rede cabeada, Wi-Fi e suporte para empresas.",
      "email": MAIL, "telephone": "+55 11 94549-8733", "taxID": "67.771.856/0001-31", "image": og("tecnico-pc"), "sameAs": [IG],
      "knowsAbout": ["Manutenção de computadores", "Formatação", "Redes cabeadas", "Wi-Fi", "Suporte técnico empresarial"]}


def head(file, title, desc, extra="", img="tecnico-pc"):
    url = SITE + "/" + ("" if file == "index.html" else file)
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0a1424">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="AtomTuring">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og(img)}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="preload" href="assets/fonts/display.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/sans.woff2" as="font" type="font/woff2" crossorigin>
<script>document.documentElement.classList.add("js")</script>
<link rel="stylesheet" href="css/site.css">
<script type="application/ld+json">{json.dumps(LD, ensure_ascii=False)}</script>
{extra}</head>
<body>
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
'''


def nav(cur):
    links = "".join(f'<a href="{h}"' + (' aria-current="page"' if h == cur else "") + f">{t}</a>" for h, t in NAVP)
    return f'''<header class="nav" id="top"><div class="wrap nav__in">
  <a class="nav__brand" href="index.html" aria-label="AtomTuring, página inicial"><img src="assets/logos/lockup-t-320.png" alt="AtomTuring" width="320" height="185"></a>
  <nav class="nav__links" id="menu" aria-label="Principal">{links}<a class="nav__ag" href="agendar.html">Agendar atendimento</a></nav>
  <a class="btn btn--sm nav__cta" href="agendar.html"{' aria-current="page"' if cur == "agendar.html" else ""}>Agendar</a>
  <button class="burger" type="button" aria-label="Abrir menu" aria-controls="menu" aria-expanded="false"><span></span><span></span></button>
</div></header>
<main id="conteudo" tabindex="-1">
'''


CREDITS = "Fotografias: Valentin Lacoste, Ritupon Baishya, Zoshua Colah, Yuriy Vertikov, Jordan Harrison e Jakub Żerdzicki, via Unsplash."
FAB = f'<a class="fab" href="{WA}" target="_blank" rel="noopener" aria-label="Chamar no WhatsApp (abre em nova aba)"><svg viewBox="0 0 32 32" width="28" height="28" aria-hidden="true"><path fill="#fff" d="M16 3C9 3 3.3 8.600 3.300 15.600c0 2.300.6 4.400 1.700 6.300L3 29l7.300-1.900a12.700 12.700 0 0 0 5.700 1.400c7 0 12.700-5.600 12.700-12.600S23 3 16 3Zm0 23.100c-1.800 0-3.600-.5-5.100-1.400l-.4-.2-4.300 1.100 1.200-4.200-.3-.4a10.300 10.300 0 0 1-1.600-5.500C5.500 9.800 10.200 5.200 16 5.200s10.500 4.600 10.500 10.400S21.800 26.100 16 26.100Zm5.800-7.800c-.3-.2-1.900-.9-2.200-1-.3-.1-.5-.2-.7.200-.2.300-.8 1-1 1.200-.2.200-.4.200-.7.100-.3-.2-1.400-.5-2.600-1.600-1-.9-1.600-1.900-1.800-2.300-.2-.3 0-.5.100-.7l.5-.6c.1-.2.200-.3.300-.5.100-.2.100-.4 0-.6l-1-2.300c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.100-.9.400-.3.300-1.200 1.200-1.200 2.800s1.200 3.300 1.400 3.500c.2.200 2.400 3.700 5.800 5.100 3.400 1.400 3.400 1 4 .9.6-.1 1.900-.8 2.200-1.500.3-.8.3-1.400.2-1.500-.1-.2-.3-.3-.6-.4Z"/></svg></a>\n'


def foot():
    return f'''</main>
<footer class="foot"><div class="wrap">
  <div class="foot__top">
    <div class="foot__brand"><img src="assets/logos/lockup-t-320.png" alt="AtomTuring" width="320" height="185" loading="lazy"><p>Manutenção de computadores, redes e Wi‑Fi. Suporte para você e para a sua empresa.</p></div>
    <nav class="foot__col" aria-label="Páginas"><h2>Páginas</h2><ul><li><a href="index.html">Início</a></li><li><a href="computadores.html">Computadores</a></li><li><a href="redes.html">Redes e Wi‑Fi</a></li><li><a href="empresas.html">Empresas</a></li><li><a href="como-funciona.html">Como funciona</a></li></ul></nav>
    <div class="foot__col"><h2>Serviços</h2><ul><li>Manutenção preventiva e corretiva</li><li>Formatação e limpeza</li><li>Troca de peças</li><li>Rede cabeada e Wi‑Fi</li><li>Pacote empresarial</li></ul></div>
    <div class="foot__col"><h2>Contato</h2><ul><li><a href="{WA}" target="_blank" rel="noopener">WhatsApp (11) 94549-8733{NB}</a></li><li><a href="{IG}" target="_blank" rel="noopener">Instagram @Atomturing{NB}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="agendar.html">Agendar atendimento</a></li></ul></div>
  </div>
  <div class="foot__bar"><p>© 2026 AtomTuring · CNPJ 67.771.856/0001-31</p><p>{CREDITS}</p></div>
</div></footer>
{FAB}<script src="js/site.js" defer></script>
</body>
</html>
'''


def btns(items, dark=False):
    out = ""
    for k, (h, t) in enumerate(items):
        ext = h.startswith("http")
        cls = "btn" if k == 0 else "btn btn--line" if dark else "tlink"
        arrow = ' <span aria-hidden="true">→</span>' if cls == "tlink" else ""
        out += f'<a class="{cls}" href="{h}"' + (' target="_blank" rel="noopener"' if ext else "") + f">{t}{NB if ext else ''}{arrow}</a>"
    return f'<div class="btns">{out}</div>'


def ems(t):
    parts = t.split("*")
    return "".join(f"<em>{p}</em>" if i % 2 else p for i, p in enumerate(parts))


def pagehead(title, lead, items, photo=None, alt="", pos=""):
    ph = f'<figure class="pagehead__ph rv">{pic(photo, alt, "(min-width:1000px) 40vw, 100vw", True, pos=pos)}</figure>' if photo else ""
    return f'''<section class="pagehead{" pagehead--solo" if not photo else ""}"><div class="wrap pagehead__in">
  <div class="pagehead__txt"><h1>{ems(title)}</h1><p class="lead">{lead}</p>{btns(items, True)}</div>{ph}
</div></section>
'''


def rows(title, lead, items, cls=""):
    its = "".join(f'<div class="row"><h3>{t}</h3><p>{d}</p></div>' for t, d in items)
    ld = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<section class="sec {cls}"><div class="wrap split"><div class="split__h rv"><h2>{ems(title)}</h2>{ld}</div><div class="rows rv">{its}</div></div></section>\n'


def cta(title="Vamos resolver o seu problema?"):
    return f'''<section class="cta"><canvas class="rain" aria-hidden="true" data-rain></canvas><img class="cta__mark" src="assets/logos/simbolo-520.png" alt="" aria-hidden="true" width="520" height="401" loading="lazy"><div class="wrap cta__in rv">
  <h2>{ems(title)}</h2>
  <div class="cta__side"><p>Orçamento sem compromisso. Confirmamos o horário pelo WhatsApp.</p>
  <div class="btns"><a class="btn btn--paper" href="{WA}" target="_blank" rel="noopener">Pedir orçamento no WhatsApp{NB}</a><a class="btn btn--line" href="agendar.html">Agendar atendimento</a></div></div>
</div></section>
'''


def faq_block(items):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)


# ---------- conteúdo ----------
PROBS = [
    ("Computador lento ou travando", "Otimização do sistema e limpeza interna. Se for preciso, formatação.", "Atualização e otimização,Limpeza,Formatação", "parafuso", "Mãos de um técnico com chave de precisão abrindo um notebook", "50% 45%"),
    ("Superaquecimento e ruído", "Limpeza interna de ventoinhas e coolers para baixar a temperatura.", "Limpeza", "notebook-interno", "Interior de um notebook com ventoinha e bateria à mostra", "50% 12%"),
    ("Peça com defeito", "Diagnóstico, instalação e teste. Você aprova a peça antes.", "Troca de peças", "bateria", "Mãos trocando a bateria de um notebook aberto sobre a bancada", "50% 50%"),
    ("Wi‑Fi fraco ou caindo", "Configuração do roteador e otimização do sinal onde você usa.", "Wi-Fi", "wifi-roteador", "Roteador preto com antenas ao lado de um nó mesh branco", "50% 55%"),
    ("Rede desorganizada", "Instalação e configuração de rede cabeada, com cabos e pontos no lugar.", "Rede cabeada", "rack-servidores", "Rack com switches e cabos de rede organizados", "50% 35%"),
    ("Suporte para empresas", "Pacote mensal fechado com suporte, emergência e gestão de equipamentos. Valores sob consulta.", "Pacote empresarial", "reuniao", "Dois profissionais conversando diante de um computador em um escritório", "40% 50%"),
]
plist = ""
for k, (t, d, g, ph, al, pos) in enumerate(PROBS):
    plist += (f'<li class="prob{" is-on" if k == 0 else ""}" data-i="{k}"><h3><button type="button" id="pb{k}" aria-expanded="{"true" if k == 0 else "false"}" aria-controls="pp{k}"><span class="prob__n" aria-hidden="true">{k + 1:02d}</span><span class="prob__t">{t}</span></button></h3>'
              f'<div class="prob__p" id="pp{k}" role="region" aria-labelledby="pb{k}"><div><p>{d}</p>'
              f'<a class="tlink" href="agendar.html?s={quote(g)}#agendar">Agendar este atendimento <span aria-hidden="true">→</span></a>'
              f'<div class="prob__m">{pic(ph, al, "(min-width:1000px) 0px, 100vw", pos=pos)}</div></div></div></li>')
pimgs = "".join(pic(ph, al, "(min-width:1000px) 46vw, 0px", False, cls="on" if k == 0 else "", pos=pos).replace("<img", f'<img data-i="{k}"', 1) for k, (t, d, g, ph, al, pos) in enumerate(PROBS))

hero = f'''<section class="hero"><canvas class="rain" aria-hidden="true" data-rain></canvas><div class="wrap hero__in">
  <div class="hero__txt">
    <h1>Computadores e redes <em>funcionando</em> como deveriam.</h1>
    <p class="lead">Manutenção preventiva e corretiva, formatação, limpeza e troca de peças. Rede cabeada, Wi‑Fi e suporte técnico para você e para a sua empresa.</p>
    <div class="btns"><a class="btn" href="{WA}" target="_blank" rel="noopener">Pedir orçamento{NB}</a><a class="btn btn--line" href="#servicos">Conhecer os serviços</a></div>
    <p class="hero__note">Orçamento sem compromisso · WhatsApp <a href="{WA}" target="_blank" rel="noopener">(11) 94549-8733{NB}</a></p>
  </div>
  <figure class="hero__ph">{pic("tecnico-pc", "Técnico de óculos limpando e montando o interior de um computador desktop", "(min-width:1000px) 44vw, 92vw", True, pos="38% 45%")}</figure>
</div></section>
'''

pledge = '''<section class="pledge" aria-label="Nosso combinado"><div class="wrap pledge__in">
  <p><strong>Orçamento sem compromisso</strong><span>Você sabe o valor antes de decidir.</span></p>
  <p><strong>Você aprova a peça</strong><span>Nada é trocado sem a sua aprovação.</span></p>
  <p><strong>Horário combinado</strong><span>Confirmamos pelo WhatsApp.</span></p>
  <p><strong>Valores e prazos claros</strong><span>Combinados antes do serviço.</span></p>
</div></section>
'''

espec = f'''<section class="sec" id="especialidades"><div class="wrap">
  <div class="sechead rv"><h2>Problemas que <em>resolvemos</em>.</h2><p class="lead">Escolha o que está acontecendo e veja como a AtomTuring resolve.</p></div>
  <div class="espec rv"><ul class="probs" id="probs">{plist}</ul><div class="espec__ph" aria-hidden="true">{pimgs}</div></div>
</div></section>
'''

SV_C = [("Manutenção preventiva e corretiva", "Revisamos antes de dar problema e corrigimos quando algo falha."), ("Formatação e otimização", "Sistema limpo, instalado e rápido de novo."), ("Limpeza interna", "Ventoinhas, coolers e componentes limpos. Menos calor, menos barulho."), ("Substituição de peças", "Diagnóstico, instalação e teste, com a sua aprovação antes.")]
SV_R = [("Instalação de rede cabeada", "Cabos e pontos de rede instalados e organizados."), ("Otimização de sinal", "O Wi‑Fi chegando bem onde você realmente usa."), ("Configuração de equipamentos", "Roteadores, switches e demais equipamentos configurados."), ("Suporte e acompanhamento", "Alguém para chamar quando a rede der problema.")]
SV_E = ["Suporte técnico", "Atendimento de emergência", "Gestão de equipamentos", "Pacotes de acompanhamento mensal"]
dl = lambda it: "".join(f"<div><dt>{t}</dt><dd>{d}</dd></div>" for t, d in it)
servicos = f'''<section class="sec sec--tint" id="servicos"><div class="wrap">
  <div class="sechead rv"><h2>Computadores, redes e <em>Wi‑Fi</em>.</h2><p class="lead">Do notebook que trava ao Wi‑Fi que cai. Para empresas, há um pacote mensal logo mais abaixo.</p></div>
  <div class="svc svc--a">
    <figure class="svc__ph rv">{pic("estacao", "Profissional trabalhando em um notebook ligado a monitores numa estação de trabalho", "(min-width:1000px) 42vw, 100vw", pos="62% 50%")}</figure>
    <div class="svc__tx rv"><h3 class="svc__t">Computadores</h3><p class="lead">Notebooks e desktops com manutenção de verdade, por dentro e por fora.</p><dl class="dl">{dl(SV_C)}</dl>
    {btns([("computadores.html", "Ver serviços de computadores"), ("agendar.html?s=Manuten%C3%A7%C3%A3o%20preventiva%20e%20corretiva#agendar", "Agendar atendimento")])}</div>
  </div>
</div></section>
<section class="band band--dark" aria-labelledby="h-redes"><canvas class="rain" aria-hidden="true" data-rain></canvas><div class="wrap band__in">
  <div class="band__tx rv"><h2 id="h-redes">Redes e <em>Wi‑Fi</em></h2><p class="lead">Conexão estável, organizada e configurada para o uso real da casa ou da empresa.</p>
  <dl class="dl dl--d">{dl(SV_R)}</dl>
  {btns([("agendar.html?s=Rede%20cabeada%2CWi-Fi#agendar", "Agendar atendimento"), ("redes.html", "Ver serviços de redes")], True)}</div>
  <figure class="band__ph rv">{pic("roteador-portas", "Traseira de um roteador com portas de rede amarelas e cabo conectado", "(min-width:1000px) 40vw, 100vw", pos="45% 50%")}</figure>
</div></section>

'''

STEPS5 = [("Entendimento do problema", "Você conta o que está acontecendo, pelo WhatsApp, Direct ou formulário."), ("Diagnóstico e avaliação", "Avaliamos o equipamento ou a rede para achar a causa real, sem chutar."), ("Orçamento", "Apresentamos o valor antes de qualquer serviço. Você decide, sem compromisso."), ("Execução do serviço", "Manutenção, limpeza, formatação, troca de peças ou configuração da rede."), ("Acompanhamento", "Suporte depois do serviço e acompanhamento contínuo para quem precisa.")]
steps = lambda: "".join(f'<li><span class="step__n" aria-hidden="true">{i + 1}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(STEPS5))
metodo = f'''<section class="sec" id="como"><div class="wrap split">
  <div class="split__h split__h--sticky rv"><h2>Do chamado ao <em>acompanhamento</em>.</h2><p class="lead">Cinco etapas, na ordem. Você sabe em que ponto está e o que vem a seguir.</p>{btns([("agendar.html", "Agendar atendimento"), ("como-funciona.html", "Ver perguntas frequentes")])}</div>
  <ol class="steps rv">{steps()}</ol>
</div></section>
'''

PACK = [("Suporte técnico", "Ajuda de quem entende, sempre que a equipe precisar."), ("Atendimento de emergência", "Quando algo importante para, a empresa sabe a quem chamar."), ("Gestão de equipamentos", "Controle do que a empresa tem e em que estado cada equipamento está."), ("Manutenção", "Preventiva e corretiva nos computadores. Peças cobradas à parte."), ("Limpeza", "Limpeza interna dos equipamentos, para evitar superaquecimento."), ("Acompanhamento técnico", "Rede, sistema e hardware acompanhados de perto.")]
empr = f'''<section class="corp" id="empresas"><div class="wrap corp__in">
  <figure class="corp__ph rv">{pic("tecnico-datacenter", "Técnico conectando cabos em um rack de servidores", "(min-width:1000px) 34vw, 100vw", pos="55% 50%")}</figure>
  <div class="corp__tx rv">
    <h2>Tecnologia da empresa <em>sob controle</em>.</h2>
    <p class="lead">Um pacote mensal fechado: a empresa deixa de correr atrás de problemas e passa a contar com suporte, acompanhamento e gestão dos equipamentos.</p>
    <ul class="ticks">{"".join(f"<li><strong>{t}</strong><span>{d}</span></li>" for t, d in PACK[:5])}</ul>
    <p class="note">Valores sob consulta, sem preço fixo. Cada empresa recebe uma proposta.</p>
    <div class="btns"><a class="btn btn--paper" href="{WA}" target="_blank" rel="noopener">Consultar valores{NB}</a><a class="tlink tlink--d" href="empresas.html">Conhecer o pacote <span aria-hidden="true">→</span></a></div>
  </div>
</div></section>
'''

FAQ = [("O que a AtomTuring faz?", "Manutenção preventiva e corretiva, formatação, limpeza, troca de peças e otimização do sistema de computadores. Instalação e configuração de rede cabeada, otimização de sinal Wi-Fi e suporte técnico. E acompanhamento contínuo."), ("Quem paga as peças?", "Nós fazemos a troca. O custo da peça fica por conta da empresa."), ("Atendem empresas?", "Sim. O suporte é pensado para você e sua empresa, inclusive com pacote mensal."), ("Quanto custa e quanto tempo leva?", "Depende do serviço. Valores e prazos são combinados no orçamento, que é sem compromisso."), ("Como peço um orçamento?", "Pelo WhatsApp (11) 94549-8733, pelo Direct do Instagram @Atomturing, por e-mail ou pelo formulário da página de orçamento.")]
home = (head("index.html", "AtomTuring — Manutenção de computadores, redes e Wi‑Fi", "Manutenção preventiva e corretiva, formatação, limpeza, troca de peças, rede cabeada e Wi-Fi. Suporte técnico para você e para a sua empresa. Orçamento sem compromisso.")
        + nav("index.html") + hero + pledge + espec + servicos + metodo + empr + cta() + foot())

comp = (head("computadores.html", "Manutenção de computadores e notebooks — AtomTuring", "Manutenção preventiva e corretiva, formatação, limpeza interna, troca de peças e otimização do sistema para computadores e notebooks.", img="pc-interno")
        + nav("computadores.html")
        + pagehead("Manutenção de *computadores* e notebooks", "Manutenção preventiva e corretiva, formatação, limpeza, troca de peças e otimização do sistema.", [(WA, "Pedir orçamento"), ("agendar.html", "Agendar atendimento")], "pc-interno", "Mãos de um técnico dentro de um computador, com cabos azuis e placa-mãe à mostra", "50% 50%")
        + rows("O que está *incluso*.", "Tudo o que fazemos nos computadores e notebooks.", [("Manutenção preventiva e corretiva", "Revisamos antes de dar problema e corrigimos quando algo falha."), ("Limpeza interna", "Limpeza de ventoinhas, coolers e componentes. Menos calor, menos barulho."), ("Formatação", "Sistema limpo, instalado e pronto para usar."), ("Otimização do sistema", "Ajustes para o computador voltar a responder sem travar."), ("Troca de peças", "Diagnóstico, instalação e teste. O custo da peça fica por conta da empresa."), ("Configuração", "Programas, contas e periféricos instalados do jeito que você usa.")])
        + f'<section class="sec sec--tint"><div class="wrap duo"><figure class="duo__ph rv">{pic("parafuso", "Mãos de um técnico com chave de precisão abrindo um notebook", "(min-width:1000px) 44vw, 100vw", pos="50% 45%")}</figure><div class="rv"><h2>Antes de <em>trocar</em> qualquer peça.</h2><dl class="dl dl--one">{dl([("Diagnóstico primeiro", "Avaliamos o equipamento para achar a causa real do problema."), ("Você aprova a peça", "Diagnóstico, instalação e teste, com a sua aprovação antes."), ("Orçamento sem compromisso", "Você sabe o valor antes de decidir."), ("Acompanhamento", "Suporte depois do serviço, para você e para a sua empresa.")])}</dl></div></div></section>\n'
        + f'<section class="sec"><div class="wrap split"><div class="split__h rv"><h2>Dúvidas sobre <em>computadores</em>.</h2></div><div class="faq rv">{faq_block(FAQ[0:2] + FAQ[3:5])}</div></div></section>\n'
        + cta("Computador com problema? Vamos *ver* isso.") + foot())

redes = (head("redes.html", "Redes, Wi‑Fi e rede cabeada — AtomTuring", "Instalação e configuração de rede cabeada, otimização de sinal Wi-Fi, configuração de equipamentos e suporte técnico.", img="wifi-roteador")
         + nav("redes.html")
         + pagehead("Redes e *Wi‑Fi* que funcionam", "Instalação e configuração de rede cabeada, otimização de sinal Wi-Fi e suporte técnico.", [("agendar.html?s=Rede%20cabeada%2CWi-Fi#agendar", "Agendar atendimento"), (WA, "Pedir orçamento")], "wifi-roteador", "Roteador preto com antenas ao lado de um nó mesh branco", "50% 55%")
         + rows("O que está *acontecendo* com a sua rede?", "", [("O Wi‑Fi cai ou está fraco", "Configuração do roteador e otimização do sinal Wi-Fi."), ("Cabos bagunçados ou sem ponto de rede", "Instalação, organização e configuração da rede cabeada."), ("A rede vive instável", "Suporte técnico e acompanhamento para achar e corrigir a causa."), ("Equipamentos novos para configurar", "Roteadores, switches e demais equipamentos configurados e testados.")])
         + f'<section class="sec sec--tint"><div class="wrap duo"><figure class="duo__ph rv">{pic("roteador-portas", "Traseira de um roteador com portas de rede amarelas e cabo conectado", "(min-width:1000px) 44vw, 100vw", pos="45% 50%")}</figure><div class="rv"><h2>Como a gente <em>resolve</em>.</h2><dl class="dl dl--one">{dl(SV_R)}</dl></div></div></section>\n'
         + f'<section class="sec"><div class="wrap split"><div class="split__h rv"><h2>Dúvidas sobre <em>redes</em>.</h2></div><div class="faq rv">{faq_block(FAQ[0:1] + FAQ[2:5])}</div></div></section>\n'
         + cta("Sua rede merece *estabilidade*.") + foot())

FAQ_E = [("Quanto custa o pacote?", "Sob consulta. O valor depende do que a empresa precisa e de quantos equipamentos tem. Não há preço fixo."), ("As peças estão inclusas?", "Não. As peças são à parte: a AtomTuring faz a troca e o custo da peça fica por conta da empresa."), ("O que acontece em uma emergência?", "O atendimento de emergência faz parte do pacote. Fale pelo WhatsApp (11) 94549-8733."), ("O que é a gestão de equipamentos?", "É o controle dos equipamentos da empresa: o que existe, em que estado está e quando precisa de manutenção.")]
pk_opts = "".join(f'<label><input type="checkbox" name="item" value="{t}" checked><span>{t}</span></label>' for t, _ in PACK)
empresas = (head("empresas.html", "Pacote empresarial de suporte técnico — AtomTuring", "Pacote mensal fechado de suporte técnico, atendimento de emergência, gestão de equipamentos, manutenção, limpeza e acompanhamento para empresas. Valores sob consulta.", img="tecnico-datacenter")
            + nav("empresas.html")
            + pagehead("Pacote empresarial: a TI da empresa *sob controle*", "Uma mensalidade fechada para a empresa contar com suporte, acompanhamento e gestão de equipamentos. Valores sob consulta.", [(WA, "Consultar valores"), ("#monte", "Montar o meu pacote")], "tecnico-datacenter", "Técnico conectando cabos em um rack de servidores", "50% 40%")
            + rows("O que está *incluso*.", "A empresa paga uma mensalidade fechada e recebe auxílio, suporte e acompanhamento. Peças são cobradas à parte.", PACK)
            + f'''<section class="sec sec--tint" id="monte"><div class="wrap formgrid">
  <div class="rv"><h2>Monte o seu <em>pacote</em>.</h2><p class="lead">Marque o que a sua empresa precisa, diga quantos equipamentos tem e consulte os valores pelo WhatsApp. Cada empresa recebe uma proposta.</p></div>
  <form class="form rv" id="pkg" novalidate><fieldset class="f"><legend>O que a empresa precisa?</legend><div class="opts">{pk_opts}</div></fieldset>
  <label class="f"><span>Quantos equipamentos a empresa tem?</span><select name="qtd"><option value="">Prefiro informar na conversa</option><option>1 a 5</option><option>6 a 15</option><option>16 a 50</option><option>Mais de 50</option></select></label>
  <button class="btn" type="submit">Consultar valores no WhatsApp</button><p class="status" role="status" aria-live="polite" hidden></p></form></div></section>
<section class="sec"><div class="wrap split"><div class="split__h rv"><h2>Dúvidas sobre o <em>pacote</em>.</h2></div><div class="faq rv">{faq_block(FAQ_E)}</div></div></section>
''' + cta("Vamos montar o pacote da *sua* empresa?") + foot())

faq_ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}, ensure_ascii=False) + "</script>\n"
como = (head("como-funciona.html", "Como funciona o atendimento — AtomTuring", "Veja como a AtomTuring cuida do seu computador e da sua rede: entendimento, diagnóstico, orçamento, execução e acompanhamento.", faq_ld, img="estacao")
        + nav("como-funciona.html")
        + pagehead("Como funciona o *atendimento*", "Um processo simples, do primeiro contato ao suporte contínuo.", [("agendar.html", "Agendar atendimento"), (WA, "Pedir orçamento")])
        + f'<section class="sec"><div class="wrap split"><div class="split__h rv"><h2>Cinco etapas, <em>na ordem</em>.</h2></div><ol class="steps rv">{steps()}</ol></div></section>\n'
        + f'<section class="sec sec--tint"><div class="wrap split"><div class="split__h rv"><h2>Dúvidas <em>comuns</em>.</h2></div><div class="faq rv">{faq_block(FAQ)}</div></div></section>\n'
        + cta() + foot())

OPTS = ["Manutenção preventiva e corretiva", "Limpeza", "Formatação", "Atualização e otimização", "Troca de peças", "Configuração", "Rede cabeada", "Wi-Fi", "Acompanhamento", "Pacote empresarial"]
opts = "".join(f'<label><input type="checkbox" name="s" value="{o}"><span>{o}</span></label>' for o in OPTS)
orc = (head("orcamento.html", "Orçamento sem compromisso — AtomTuring", "Peça um orçamento sem compromisso pelo WhatsApp, Direct do Instagram, e-mail ou formulário.") + nav("orcamento.html") + f'''
<section class="sec sec--form" id="formulario"><div class="wrap formgrid">
  <div>
    <h1>Peça o seu <em>orçamento</em>.</h1>
    <p class="lead">Sem compromisso. Fale pelo WhatsApp ou pelo Direct do Instagram. Se preferir, envie o formulário: abrimos o seu e-mail com a mensagem pronta.</p>
    <div class="btns"><a class="btn" href="{WA}" target="_blank" rel="noopener">Chamar no WhatsApp{NB}</a><a class="tlink" href="agendar.html">Agendar atendimento <span aria-hidden="true">→</span></a></div>
    <dl class="contacts">
      <div><dt>WhatsApp</dt><dd><a href="{WA}" target="_blank" rel="noopener">(11) 94549-8733{NB}</a></dd></div>
      <div><dt>Instagram (Direct)</dt><dd><a href="{IG}" target="_blank" rel="noopener">@Atomturing{NB}</a></dd></div>
      <div><dt>E-mail</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd></div>
      <div><dt>CNPJ</dt><dd>67.771.856/0001-31</dd></div>
    </dl>
  </div>
  <form class="form" id="form" novalidate>
    <label class="f"><span>Seu nome</span><input type="text" name="nome" autocomplete="name" required aria-required="true" aria-describedby="err"></label>
    <label class="f"><span>Telefone ou WhatsApp</span><input type="tel" name="tel" autocomplete="tel" inputmode="tel"></label>
    <fieldset class="f"><legend>O que você precisa?</legend><div class="opts" id="opts">{opts}</div></fieldset>
    <label class="f"><span>Detalhes</span><textarea name="msg" rows="4" placeholder="Modelo do equipamento, o que acontece, onde fica a rede…"></textarea></label>
    <p class="err" id="err" role="alert" hidden>Escreva seu nome para continuar.</p>
    <button class="btn" type="submit">Enviar por e-mail</button><p class="status" role="status" aria-live="polite" hidden></p>
  </form>
</div></section>
''' + foot())

aper = "".join(f'<label><input type="radio" name="per" value="{o}"{" checked" if i == 0 else ""}><span>{o}</span></label>' for i, o in enumerate(["Combinar na conversa", "Manhã", "Tarde", "Noite"]))
agendar = (head("agendar.html", "Agendar atendimento — AtomTuring", "Escolha o serviço, o dia e o período. A mensagem segue pronta para o WhatsApp da AtomTuring e o orçamento é sem compromisso.") + nav("agendar.html") + f'''
<section class="sec sec--form" id="agendar"><div class="wrap formgrid">
  <div>
    <h1>Agende o seu <em>atendimento</em>.</h1>
    <p class="lead">Você escolhe o serviço e o melhor dia. Confirmamos o horário pelo WhatsApp e passamos o orçamento, sem compromisso.</p>
    <ol class="mini"><li>Escolha o serviço</li><li>Informe dia e período</li><li>Envie pelo WhatsApp</li></ol>
    <p class="note">O horário só vale depois da nossa resposta. Prefere conversar antes? <a class="tl" href="{WA}" target="_blank" rel="noopener">Chamar no WhatsApp{NB}</a></p>
  </div>
  <form class="form" id="ag" novalidate>
    <label class="f"><span>Seu nome</span><input type="text" name="nome" autocomplete="name" required aria-required="true" aria-describedby="aerr"></label>
    <fieldset class="f"><legend>O que você precisa?</legend><div class="opts" id="aopts">{opts}</div></fieldset>
    <label class="f"><span>Melhor dia</span><input type="date" name="dia"></label>
    <fieldset class="f"><legend>Período</legend><div class="opts">{aper}</div></fieldset>
    <label class="f"><span>Detalhes (opcional)</span><textarea name="msg" rows="3" placeholder="Modelo do equipamento, o que acontece, onde fica a rede…"></textarea></label>
    <p class="err" id="aerr" role="alert" hidden>Escreva seu nome para continuar.</p>
    <button class="btn" type="submit">Enviar pelo WhatsApp</button><p class="status" role="status" aria-live="polite" hidden></p>
  </form>
</div></section>
''' + foot())

PAGES = [("index.html", home), ("computadores.html", comp), ("redes.html", redes), ("empresas.html", empresas), ("como-funciona.html", como), ("orcamento.html", orc), ("agendar.html", agendar)]
for name, html in PAGES:
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{SITE}/{'' if n == 'index.html' else n}</loc></url>\n" for n, _ in PAGES) + "</urlset>\n")
open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
print("ok")
