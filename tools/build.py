import os, sys
from urllib.parse import quote
OUT = sys.argv[1]
WA = "https://wa.me/5511945498733?text=Ol%C3%A1%2C%20AtomTuring!%20Quero%20um%20or%C3%A7amento."
IG = "https://instagram.com/Atomturing"
NB = '<span class="sr-only"> (abre em nova aba)</span>'
NAVP = [("index.html", "Início"), ("computadores.html", "Computadores"), ("redes.html", "Redes e Wi‑Fi"), ("empresas.html", "Empresas"), ("como-funciona.html", "Como funciona"), ("orcamento.html", "Orçamento")]
LD = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"ProfessionalService","name":"AtomTuring","description":"Manutenção de computadores e redes: manutenção preventiva e corretiva, formatação, limpeza, troca de peças, rede cabeada, Wi-Fi e pacote empresarial.","email":"contato.atomturing@gmail.com","telephone":"+55 11 94549-8733","taxID":"67.771.856/0001-31","sameAs":["https://instagram.com/Atomturing"]}</script>\n'
PACK = [("Suporte técnico", "Ajuda de quem entende, sempre que a equipe precisar."), ("Atendimento de emergência", "Quando algo importante para, a empresa sabe a quem chamar."), ("Gestão de equipamentos", "Controle do que a empresa tem e em que estado cada equipamento está."), ("Manutenção", "Preventiva e corretiva nos computadores. Peças cobradas à parte."), ("Limpeza", "Limpeza interna dos equipamentos, para evitar superaquecimento."), ("Acompanhamento técnico", "Rede, sistema e hardware acompanhados de perto.")]


def img(n, alt, eager=False, w=1400, h=933, cls=""):
    return f'<img{f" class={cls}" if cls else ""} src="assets/tech/{n}.jpg" width="{w}" height="{h}" alt="{alt}"{"" if eager else " loading=lazy"}>'


def head(title, desc, home=False):
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#04070d">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="AtomTuring">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="preload" href="assets/fonts/jbmono.woff2" as="font" type="font/woff2" crossorigin>
<script>document.documentElement.classList.add("js")</script>
<link rel="stylesheet" href="css/site.css">
{LD if home else ""}</head>
<body>
<canvas id="bg" aria-hidden="true"></canvas>
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
'''


def nav(cur):
    links = "".join(f'<a href="{h}"' + (' aria-current="page"' if h == cur else "") + f">{t}</a>" for h, t in NAVP)
    return f'''<header class="nav" id="top"><div class="nav__in">
  <a class="nav__brand" href="index.html" aria-label="AtomTuring, página inicial"><img src="assets/logos/lockup-t-320.png" alt="AtomTuring" width="320" height="185"></a>
  <nav class="nav__links" id="menu" aria-label="Principal">{links}<a class="nav__ag" href="agendar.html">Agendar atendimento</a></nav>
  <a class="btn btn--sm nav__cta" href="agendar.html"{' aria-current="page"' if cur == "agendar.html" else ""}>Agendar</a>
  <button class="burger" type="button" aria-label="Abrir menu" aria-controls="menu" aria-expanded="false"><span></span><span></span></button>
</div></header>
<main id="conteudo" tabindex="-1">
'''


def foot(sticky=True):
    s = f'<div class="sticky"><a class="btn" href="agendar.html">Agendar</a><a class="btn btn--ghost" href="{WA}" target="_blank" rel="noopener">WhatsApp{NB}</a></div>\n' if sticky else ""
    return f'''</main>
<footer class="foot"><div class="foot__in">
  <p class="foot__note">Orçamento sem compromisso. Valores do pacote empresarial sob consulta; peças cobradas à parte. WhatsApp (11) 94549-8733 ou Direct do Instagram @Atomturing.</p>
  <div class="foot__grid">
    <div><p class="foot__h">// páginas</p><ul><li><a href="index.html">Início</a></li><li><a href="computadores.html">Computadores</a></li><li><a href="redes.html">Redes e Wi‑Fi</a></li><li><a href="empresas.html">Empresas</a></li><li><a href="como-funciona.html">Como funciona</a></li></ul></div>
    <div><p class="foot__h">// serviços</p><ul><li>Manutenção preventiva e corretiva</li><li>Formatação e limpeza</li><li>Troca de peças</li><li>Rede cabeada e Wi‑Fi</li><li>Acompanhamento</li></ul></div>
    <div><p class="foot__h">// empresas</p><ul><li><a href="empresas.html">Pacote empresarial</a></li><li><a href="empresas.html#monte">Monte o seu pacote</a></li><li><a href="orcamento.html">Consultar valores</a></li></ul></div>
    <div><p class="foot__h">// contato</p><ul><li><a href="{WA}" target="_blank" rel="noopener">WhatsApp{NB}</a></li><li><a href="mailto:contato.atomturing@gmail.com">E-mail</a></li><li><a href="{IG}" target="_blank" rel="noopener">Instagram{NB}</a></li><li><a href="agendar.html">Agendar atendimento</a></li></ul></div>
  </div>
  <div class="foot__bar"><p>© 2026 AtomTuring. CNPJ 67.771.856/0001-31.</p><p><span>Fotos: Unsplash</span><a href="orcamento.html">Contato</a></p></div>
</div></footer>
{s}<script src="js/site.js" defer></script>
</body>
</html>
'''


def btns(items):
    out = ""
    for k, (h, t) in enumerate(items):
        ext = h.startswith("http")
        out += f'<a class="btn{" btn--ghost" if k else ""}" href="{h}"' + (' target="_blank" rel="noopener"' if ext else "") + f">{t}{NB if ext else ''}</a>"
    return f'<div class="btns">{out}</div>'


def h(tag, text, cls=""):
    return f'<{tag}{f" class={cls}" if cls else ""}><span class="c" aria-hidden="true">//</span> {text}</{tag}>'


def top(title, lead, items, photo=None, alt=""):
    ph = f'<figure class="frame rv">{img(photo, alt, True)}</figure>' if photo else ""
    return f'<section class="top dark{" top--solo" if not photo else ""}"><div class="wrap top__in"><div class="top__txt rv">{h("h1", title)}<p class="lead">{lead}</p>{btns(items)}</div>{ph}</div></section>\n'


def split(title, lead, items, extra=""):
    its = "".join(f'<div class="it"><h3>{t}</h3><p>{d}</p></div>' for t, d in items)
    ld = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<section class="light"><div class="wrap split"><div class="split__h rv">{h("h2", title)}{ld}</div><div class="split__b rv">{its}{extra}</div></div></section>\n'


def close(title):
    return f'<section class="close dark"><div class="wrap rv">{h("h2", title)}<p class="lead">Orçamento sem compromisso. Confirmamos o horário pelo WhatsApp.</p>{btns([("agendar.html", "Agendar atendimento"), (WA, "Chamar no WhatsApp")])}</div></section>\n'


PROBS = [
    ("Computador lento ou travando", "Otimização do sistema e limpeza interna. Se for preciso, formatação.", "Atualização e otimização,Limpeza,Formatação", "pc-lento", "Placa de circuito azul escura com contatos dourados", "Computadores"),
    ("Esquenta e faz barulho", "Limpeza interna de ventoinhas e coolers para baixar a temperatura.", "Limpeza", "calor", "Placa eletrônica azul-turquesa com componentes", "Computadores"),
    ("Peça com defeito", "Diagnóstico, instalação e teste. Você aprova a peça antes.", "Troca de peças", "peca", "Chips e componentes sobre uma placa azul", "Computadores"),
    ("Wi‑Fi fraco ou caindo", "Configuração do roteador e otimização do sinal onde você usa.", "Wi-Fi", "wifi", "Fibras ópticas com pontos de luz azul", "Redes e Wi‑Fi"),
    ("Rede bagunçada", "Instalação e configuração de rede cabeada, com cabos e pontos no lugar.", "Rede cabeada", "cabos", "Fios de luz azul sobre fundo escuro", "Redes e Wi‑Fi"),
    ("Preciso para minha empresa", "Pacote mensal fechado com suporte, emergência e gestão de equipamentos. Valores sob consulta.", "Pacote empresarial", "dados", "Malha de rede azul com pontos conectados", "Empresas"),
]
N = len(PROBS)
plist = "".join(f'<li><button type="button" data-i="{k}"{" aria-current=true" if k == 0 else ""}><span class="c" aria-hidden="true">{k + 1:02d}</span> {t}</button></li>' for k, (t, d, g, ph, al, tag) in enumerate(PROBS))
pimgs = "".join(f'<img src="assets/tech/{ph}.jpg" width="1400" height="933" alt="{al}"{"" if k == 0 else " loading=lazy"} data-i="{k}"{" class=on" if k == 0 else ""}>' for k, (t, d, g, ph, al, tag) in enumerate(PROBS))
pticks = "".join(f'<i data-i="{k}"{" class=on" if k == 0 else ""}></i>' for k in range(N))
pdata = "".join(f'<template data-i="{k}"><h3 class="pin__t"><span class="c" aria-hidden="true">&gt;</span> {t}</h3><p class="pin__s">{d}</p></template>' for k, (t, d, g, ph, al, tag) in enumerate(PROBS))
import json
pjson = json.dumps([{"t": t, "d": d, "g": g, "p": ph, "tag": tag} for t, d, g, ph, al, tag in PROBS], ensure_ascii=False)

pin = f'''<section class="pin dark" id="solucoes" style="--n:{N}" aria-label="Escolha o seu problema">
  <div class="pin__stage"><div class="wrap pin__grid">
    <div class="pin__l">
      {h("h2", "O que está acontecendo?")}
      <ul class="pin__list" id="plist">{plist}</ul>
      <div class="pin__d" aria-live="polite"><h3 class="pin__t" id="pt"><span class="c" aria-hidden="true">&gt;</span> {PROBS[0][0]}</h3><p class="pin__s" id="ps">{PROBS[0][1]}</p>
      <p class="pin__tag"><span id="ptag">{PROBS[0][5]}</span></p>
      <div class="btns"><a class="btn" id="pgo" href="agendar.html?s={quote(PROBS[0][2])}#agendar">Agendar este atendimento</a></div></div>
    </div>
    <div class="pin__m"><div class="pin__img">{pimgs}<span class="pin__scan" aria-hidden="true"></span><span class="pin__cap" id="pcap" aria-hidden="true">{PROBS[0][5]}</span></div><div class="pin__ticks" aria-hidden="true">{pticks}</div></div>
    <span class="pin__wire" id="wire" aria-hidden="true"></span>
  </div></div>
</section>
<script id="pdata" type="application/json">{pjson}</script>
'''

hero = f'''<section class="hero dark"><div class="wrap hero__in">
  <div class="hero__txt">
    <h1 class="code rise"><span class="c" aria-hidden="true">$</span> Problema com <span class="word" id="word" data-words="o computador|o notebook|o Wi‑Fi|a rede|a internet">o computador</span>?<span class="cur" aria-hidden="true"></span></h1>
    <p class="lead rise">Manutenção de computadores e redes. Veja a solução para o seu caso e agende o atendimento. Orçamento sem compromisso.</p>
    <div class="btns rise"><a class="btn" href="agendar.html">Agendar atendimento</a><a class="btn btn--ghost" href="#solucoes">Ver a solução</a></div>
  </div>
  <div class="orbit rise" aria-label="Serviços ligados à AtomTuring">
    <svg class="orbit__svg" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"><line x1="50" y1="50" x2="15" y2="17"/><line x1="50" y1="50" x2="85" y2="17"/><line x1="50" y1="50" x2="15" y2="83"/><line x1="50" y1="50" x2="85" y2="83"/><circle cx="50" cy="50" r="30"/><circle cx="50" cy="50" r="42"/></svg>
    <img class="orbit__logo" src="assets/logos/simbolo-520.png" width="520" height="401" alt="Símbolo da AtomTuring">
    <a class="node n1" href="computadores.html">Computadores</a><a class="node n2" href="redes.html">Redes</a><a class="node n3" href="agendar.html?s=Wi-Fi#agendar">Wi‑Fi</a><a class="node n4" href="empresas.html">Empresas</a>
  </div>
</div></section>
'''

STEP3 = [("conversa", "Você conta o que acontece, pelo WhatsApp, Direct ou formulário."), ("agenda", "Manhã, tarde ou noite. Confirmamos o horário pelo WhatsApp."), ("resolve", "Diagnóstico, conserto e suporte depois do serviço. Orçamento antes de decidir.")]
steps = f'''<section class="steps"><div class="wrap">{h("h2", "Do problema ao computador funcionando.")}<div class="term3 rv">''' + "".join(f'<div class="term"><p class="term__b"><span class="c">$</span> {a}</p><p>{b}</p></div>' for a, b in STEP3) + '</div></div></section>\n'

def svc(tag, title, items, photo, alt, links):
    li = "".join(f"<li>{x}</li>" for x in items)
    return f'<article class="svc rv"><figure>{img(photo, alt)}</figure><div><h3>{title}</h3><ul class="ticks">{li}</ul>{btns(links)}</div></article>'

services = f'''<section class="dark svcs"><div class="wrap">{h("h2", "Serviços")}<div class="svc3">''' \
  + svc("computadores.png", "Computadores", ["Manutenção preventiva e corretiva", "Formatação e otimização", "Limpeza interna", "Troca de peças"], "peca", "Chips sobre placa azul", [("agendar.html?s=Manuten%C3%A7%C3%A3o%20preventiva%20e%20corretiva#agendar", "Agendar"), ("computadores.html", "Detalhes")]) \
  + svc("redes.png", "Redes e Wi‑Fi", ["Rede cabeada", "Otimização do sinal Wi‑Fi", "Suporte e acompanhamento"], "wifi", "Fibras ópticas azuis", [("agendar.html?s=Rede%20cabeada%2CWi-Fi#agendar", "Agendar"), ("redes.html", "Detalhes")]) \
  + svc("empresas.png", "Para empresas", ["Suporte e emergência", "Gestão de equipamentos", "Pacote mensal, valores sob consulta"], "dados", "Malha de rede azul", [(WA, "Consultar valores"), ("empresas.html", "Detalhes")]) + '</div></div></section>\n'

home = head("AtomTuring — Manutenção de computadores e redes", "Problema no computador, no Wi-Fi ou na rede? Veja a solução e agende o atendimento. Orçamento sem compromisso.", True) + nav("index.html") + hero + pin + steps + services + close("agendar --hoje") + foot()

comp = head("Computadores — AtomTuring", "Manutenção preventiva e corretiva, formatação, limpeza, troca de peças e otimização do sistema para computadores e notebooks.") + nav("computadores.html") \
  + top("Computadores e notebooks", "Manutenção preventiva e corretiva, formatação, limpeza, troca de peças e otimização do sistema.", [("agendar.html", "Agendar atendimento"), (WA, "Chamar no WhatsApp")], "pc-lento", "Placa de circuito azul escura") \
  + split("O que está incluso.", "Tudo o que fazemos nos computadores e notebooks.", [("Manutenção preventiva e corretiva", "Revisamos antes de dar problema e corrigimos quando algo falha."), ("Limpeza", "Limpeza interna de ventoinhas, coolers e componentes. Menos calor, menos barulho."), ("Formatação", "Sistema limpo, instalado e pronto para usar."), ("Otimização do sistema", "Ajustes para o computador voltar a responder sem travar."), ("Troca de peças", "Diagnóstico, instalação e teste. O custo da peça fica por conta da empresa."), ("Configuração", "Programas, contas e periféricos instalados do jeito que você usa.")]) \
  + close("agendar --computador") + foot()

redes = head("Redes e Wi-Fi — AtomTuring", "Instalação e configuração de rede cabeada, otimização de sinal Wi-Fi e suporte técnico.") + nav("redes.html") \
  + top("Redes e Wi‑Fi", "Instalação e configuração de rede cabeada, otimização de sinal Wi-Fi e suporte técnico.", [("agendar.html?s=Rede%20cabeada%2CWi-Fi#agendar", "Agendar atendimento"), (WA, "Chamar no WhatsApp")], "wifi", "Fibras ópticas com pontos de luz azul") \
  + split("O que está acontecendo com a sua rede?", "", [("O Wi‑Fi cai ou está fraco", "Configuração do roteador e otimização do sinal Wi-Fi."), ("Cabos bagunçados ou sem ponto de rede", "Instalação, organização e configuração da rede cabeada."), ("A rede vive instável", "Suporte técnico e acompanhamento para achar e corrigir a causa.")]) \
  + close("agendar --rede") + foot()

FAQ_E = [("Quanto custa o pacote?", "Sob consulta. O valor depende do que a empresa precisa e de quantos equipamentos tem. Não há preço fixo."), ("As peças estão inclusas?", "Não. As peças são à parte: a AtomTuring faz a troca e o custo da peça fica por conta da empresa."), ("O que acontece em uma emergência?", "O atendimento de emergência faz parte do pacote. Fale pelo WhatsApp (11) 94549-8733."), ("O que é a gestão de equipamentos?", "É o controle dos equipamentos da empresa: o que existe, em que estado está e quando precisa de manutenção.")]
faq_e = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ_E)
pk_opts = "".join(f'<label><input type="checkbox" name="item" value="{t}" checked><span>{t}</span></label>' for t, _ in PACK)
empresas = head("Pacote empresarial — AtomTuring", "Pacote mensal fechado de suporte, atendimento de emergência, gestão de equipamentos, manutenção, limpeza e acompanhamento técnico para empresas. Valores sob consulta.") + nav("empresas.html") \
  + top("Pacote empresarial", "Sua TI sob controle, todo mês. Valores sob consulta.", [(WA, "Consultar valores"), ("#monte", "Monte o seu pacote")], "dados", "Malha de rede azul com pontos conectados") \
  + split("O que está incluso.", "A empresa paga uma mensalidade fechada e recebe auxílio, suporte e acompanhamento. Peças são cobradas à parte.", PACK) + f'''
<section class="light alt" id="monte"><div class="wrap formgrid"><div class="rv">{h("h2", "Monte o seu pacote.")}<p class="lead">Marque o que a sua empresa precisa, diga quantos equipamentos tem e consulte os valores pelo WhatsApp. Cada empresa recebe uma proposta.</p></div>
<form class="form" id="pkg"><fieldset class="f"><legend>O que a empresa precisa?</legend><div class="opts">{pk_opts}</div></fieldset><label class="f"><span>Quantos equipamentos a empresa tem?</span><select name="qtd"><option value="">Prefiro informar na conversa</option><option>1 a 5</option><option>6 a 15</option><option>16 a 50</option><option>Mais de 50</option></select></label><button class="btn" type="submit">Consultar valores no WhatsApp</button></form></div></section>
<section class="light"><div class="wrap split"><div class="split__h rv">{h("h2", "Dúvidas sobre o pacote.")}</div><div class="split__b rv"><div class="faq">{faq_e}</div></div></div></section>
''' + close("agendar --empresa") + foot()

STEPS = [("Conversa", "Você conta o que está acontecendo com o computador ou com a rede, pelo WhatsApp, Direct ou formulário."), ("Diagnóstico", "Avaliamos o equipamento e a rede para achar a causa real do problema."), ("Execução", "Manutenção, limpeza, formatação, troca de peças, otimização do sistema e configuração de rede."), ("Acompanhamento", "Suporte contínuo, monitoramento preventivo e assistência personalizada para você e sua empresa.")]
FAQ = [("O que a AtomTuring faz?", "Manutenção preventiva e corretiva, formatação, limpeza, troca de peças e otimização do sistema de computadores. Instalação e configuração de rede cabeada, otimização de sinal Wi-Fi e suporte técnico. E acompanhamento contínuo."), ("Quem paga as peças?", "Nós fazemos a troca. O custo da peça fica por conta da empresa."), ("Atendem empresas?", "Sim. O suporte é pensado para você e sua empresa, inclusive com pacote mensal."), ("Quanto custa e quanto tempo leva?", "Depende do serviço. Valores e prazos são combinados no orçamento, que é sem compromisso."), ("Como peço um orçamento?", "Pelo WhatsApp (11) 94549-8733, pelo Direct do Instagram @Atomturing, por e-mail ou pelo formulário da página de orçamento.")]
faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
como = head("Como funciona — AtomTuring", "Veja como a AtomTuring cuida do seu computador e da sua rede, da conversa ao suporte contínuo.") + nav("como-funciona.html") \
  + top("Como trabalhamos", "Um processo simples, do chamado ao suporte contínuo.", [("agendar.html", "Agendar atendimento"), (WA, "Chamar no WhatsApp")]) \
  + split("Quatro etapas.", "", STEPS) + f'<section class="light alt"><div class="wrap split"><div class="split__h rv">{h("h2", "Dúvidas comuns.")}</div><div class="split__b rv"><div class="faq">{faq}</div></div></div></section>\n' \
  + close("agendar --hoje") + foot()

OPTS = ["Manutenção preventiva e corretiva", "Limpeza", "Formatação", "Atualização e otimização", "Troca de peças", "Configuração", "Rede cabeada", "Wi-Fi", "Acompanhamento", "Pacote empresarial"]
opts = "".join(f'<label><input type="checkbox" name="s" value="{o}"><span>{o}</span></label>' for o in OPTS)
orc = head("Orçamento — AtomTuring", "Peça um orçamento sem compromisso pelo WhatsApp, Direct do Instagram, e-mail ou formulário.") + nav("orcamento.html") + f'''
<section class="light formpage" id="formulario"><div class="wrap formgrid">
  <div>
    {h("h1", "Peça seu orçamento.", "page-title")}
    <p class="lead">Orçamento sem compromisso. Fale pelo WhatsApp ou pelo Direct do Instagram. Se preferir, envie o formulário: abrimos o seu e-mail com a mensagem pronta.</p>
    <div class="btns"><a class="btn" href="{WA}" target="_blank" rel="noopener">Chamar no WhatsApp{NB}</a><a class="btn btn--ghost" href="agendar.html">Agendar atendimento</a></div>
    <dl class="contacts">
      <div><dt>WhatsApp</dt><dd><a href="{WA}" target="_blank" rel="noopener">(11) 94549-8733{NB}</a></dd></div>
      <div><dt>Instagram (Direct)</dt><dd><a href="{IG}" target="_blank" rel="noopener">@Atomturing{NB}</a></dd></div>
      <div><dt>E-mail</dt><dd><a href="mailto:contato.atomturing@gmail.com">contato.atomturing@gmail.com</a></dd></div>
      <div><dt>CNPJ</dt><dd>67.771.856/0001-31</dd></div>
    </dl>
  </div>
  <form class="form" id="form" novalidate>
    <label class="f"><span>Seu nome</span><input type="text" name="nome" autocomplete="name" required aria-required="true" aria-describedby="err"></label>
    <label class="f"><span>Telefone ou WhatsApp</span><input type="tel" name="tel" autocomplete="tel" inputmode="tel"></label>
    <fieldset class="f"><legend>O que você precisa?</legend><div class="opts" id="opts">{opts}</div></fieldset>
    <label class="f"><span>Detalhes</span><textarea name="msg" rows="4" placeholder="Modelo do equipamento, o que acontece, onde fica a rede…"></textarea></label>
    <p class="err" id="err" role="alert" hidden>Escreva seu nome para continuar.</p>
    <button class="btn" type="submit">Enviar por e-mail</button>
  </form>
</div></section>
''' + foot(False)

aper = "".join(f'<label><input type="radio" name="per" value="{o}"{" checked" if i == 0 else ""}><span>{o}</span></label>' for i, o in enumerate(["Combinar na conversa", "Manhã", "Tarde", "Noite"]))
agendar = head("Agendar atendimento — AtomTuring", "Escolha o serviço, o dia e o período. A mensagem segue pronta para o WhatsApp da AtomTuring e o orçamento é sem compromisso.") + nav("agendar.html") + f'''
<section class="light formpage" id="agendar"><div class="wrap formgrid">
  <div>
    {h("h1", "Agende seu atendimento.", "page-title")}
    <p class="lead">Você escolhe o serviço e o melhor dia. Confirmamos o horário pelo WhatsApp e passamos o orçamento, sem compromisso.</p>
    <ul class="plain"><li><span class="c">$</span> escolha o serviço</li><li><span class="c">$</span> informe dia e período</li><li><span class="c">$</span> envie pelo WhatsApp</li></ul>
    <p class="note-s">O horário só vale depois da nossa resposta. Prefere conversar antes? <a class="tl" href="{WA}" target="_blank" rel="noopener">Chamar no WhatsApp{NB}</a></p>
  </div>
  <form class="form" id="ag" novalidate>
    <label class="f"><span>Seu nome</span><input type="text" name="nome" autocomplete="name" required aria-required="true" aria-describedby="aerr"></label>
    <fieldset class="f"><legend>O que você precisa?</legend><div class="opts" id="aopts">{opts}</div></fieldset>
    <label class="f"><span>Melhor dia</span><input type="date" name="dia"></label>
    <fieldset class="f"><legend>Período</legend><div class="opts">{aper}</div></fieldset>
    <label class="f"><span>Detalhes (opcional)</span><textarea name="msg" rows="3" placeholder="Modelo do equipamento, o que acontece, onde fica a rede…"></textarea></label>
    <p class="err" id="aerr" role="alert" hidden>Escreva seu nome para continuar.</p>
    <button class="btn" type="submit">Enviar pelo WhatsApp</button>
  </form>
</div></section>
''' + foot(False)

for name, html in [("index.html", home), ("computadores.html", comp), ("redes.html", redes), ("empresas.html", empresas), ("como-funciona.html", como), ("orcamento.html", orc), ("agendar.html", agendar)]:
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
print("ok")
