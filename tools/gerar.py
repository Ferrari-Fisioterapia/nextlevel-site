#!/usr/bin/env python3
"""Gera o site Next Level Fitness Community (home, comunidade, modalidades, blog, membro fundador, 404, sitemap, robots).
Textos em tools/conteudo.py. Uso: python3 tools/gerar.py"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from conteudo import PILARES, PASSOS, HOME_FAQ, MODALIDADES, ARTIGOS, TEMAS

NOME = "Next Level Fitness Community"
BASE = "https://www.nextlevelfitness.com.br"
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DM = "https://ig.me/m/nextlevelfitness.community"
IG = "https://www.instagram.com/nextlevelfitness.community/"
ED = "https://www.edferrarijr.com"
DATA = "2026-10-18"
OG = BASE + "/assets/img/foto-dupla.webp"


def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def head(titulo, desc, caminho, ld, og=OG, robots="index, follow, max-image-preview:large"):
    u = BASE + caminho
    lds = "".join('<script type="application/ld+json">%s</script>\n' % json.dumps(x, ensure_ascii=False) for x in ld)
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(titulo)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#141414">
<link rel="canonical" href="{u}">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{NOME}">
<meta property="og:url" content="{u}"><meta property="og:title" content="{esc(titulo)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="/assets/fonts/BarlowCondensed-800i.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/Barlow-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="icon" href="/assets/img/logo.png">
<link rel="stylesheet" href="/css/site.css">
<script>document.documentElement.classList.add('js')</script>
<script src="/assets/js/site.js" defer></script>
{lds}</head>
<body>
<a class="pular" href="#conteudo">Pular para o conteúdo</a>
<header class="s-header"><div class="s-wide">
<a class="s-brand" href="/"><img src="/assets/img/logo.png" alt="Logo da {NOME}" width="42" height="42"><span>Next Level<small>Fitness Community</small></span></a>
<input type="checkbox" id="mn" class="mn-chk" aria-label="Abrir menu"><label for="mn" class="mn-btn" aria-hidden="true"><i></i></label>
<nav class="s-nav" aria-label="Principal"><a href="/comunidade/">Comunidade</a><a href="/hyrox/">Hyrox</a><a href="/crossfit/">CrossFit</a><a href="/athx/">ATHX</a><a href="/corrida/">Corrida</a><a href="/blog/">Blog</a><a class="s-btn small" href="{DM}">Chamar no direct</a></nav>
</div></header>
<div id="conteudo">
"""


def foot():
    return f"""</div>
<footer class="s-footer"><div class="s-wide"><div class="cols">
<div class="assin"><img src="/assets/img/logo.png" alt="" width="42" height="42"><span>Next Level<small>Fitness Community</small></span></div>
<div><strong>Comunidade</strong><a href="/comunidade/">Sobre</a><a href="/membro-fundador/">Membro fundador</a><a href="/blog/">Blog</a></div>
<div><strong>Modalidades</strong><a href="/hyrox/">Hyrox</a><a href="/crossfit/">CrossFit</a><a href="/athx/">ATHX</a><a href="/corrida/">Corrida</a></div>
<div><strong>Contato</strong><a href="{IG}">Instagram</a><a href="{DM}">Chamar no direct</a></div>
<div>Criada por <a href="{ED}" style="display:inline">Ed Ferrari Jr</a>,<br>fisioterapeuta CREFITO-3/306266-F</div>
</div>
<p class="s-note">Conteúdo informativo, sem substituir a avaliação de um profissional de saúde. Cada pessoa responde de um jeito ao treino. A Next Level Fitness Community não é afiliada a Hyrox, CrossFit, ATHX ou adidas; as marcas citadas pertencem a seus donos. © 2026 {NOME}.</p>
</div></footer>
<a class="barra-cta" href="{DM}">Chamar no direct</a>
</body>
</html>
"""


def foto(nome, alt, w, h, lazy=True, cls=""):
    la = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="/assets/img/{nome}.webp" alt="{esc(alt)}" width="{w}" height="{h}"{la}>'


def faq_html(itens):
    return "".join(f'<details class="faq rv"><summary>{esc(p)}</summary><p>{esc(r)}</p></details>' for p, r in itens)


def faq_ld(itens):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": p, "acceptedAnswer": {"@type": "Answer", "text": r}} for p, r in itens]}


def crumbs(itens):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i, "name": n, "item": BASE + c} for i, (n, c) in enumerate(itens, 1)]}


def org_ld():
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": BASE + "/#org", "name": NOME, "alternateName": "Next Level Fitness", "url": BASE + "/",
         "logo": BASE + "/assets/img/logo.png", "sameAs": [IG],
         "founder": {"@type": "Person", "name": "Ed Ferrari Jr", "url": ED + "/"}},
        {"@type": "WebSite", "@id": BASE + "/#site", "url": BASE + "/", "name": NOME, "inLanguage": "pt-BR", "publisher": {"@id": BASE + "/#org"}}]}


def cta_bloco(titulo="Chame no direct.", texto="Conte o que você treina e o que procura. A gente responde e avisa as novidades, incluindo o lançamento do membro fundador."):
    return f"""<section class="h-sec"><div class="s-wide"><div class="s-cta rv"><span class="rotulo" style="color:#fff">Quer fazer parte?</span><h2>{titulo}</h2>
<p>{texto}</p><a class="s-btn" href="{DM}">Chamar no direct</a></div></div></section>"""


def cards_modalidades():
    out = ""
    for slug, m in MODALIDADES.items():
        out += f"""<a class="mod rv" href="/{slug}/">{foto(m['foto'], 'Treino de ' + m['nome'], 900, 600)}<span class="mod-t">{m['nome']}</span><span class="mod-s">Guia da modalidade</span></a>"""
    return out


def temas(a):
    """Temas do artigo; sem o campo "temas", deduz pelo título e pela tag."""
    if a.get("temas"):
        return a["temas"]
    t = (a["titulo"] + " " + a.get("tag", "")).lower()
    achados = [k for k in ("hyrox", "crossfit", "athx", "corrida", "radar") if k in t]
    if any(x in t for x in ("dor", "lesão", "aquec")):
        achados.append("prevencao")
    return achados or ["habitos"]


def data_br(a):
    d = a.get("data", DATA)
    return f"{d[8:10]}/{d[5:7]}/{d[:4]}"


def leitura(a):
    txt = " ".join(v if isinstance(v, str) else " ".join(v) for _, v in a["corpo"])
    return max(1, -(-len(re.sub(r"<[^>]+>", " ", txt).split()) // 200))


def recentes():
    """Slugs do mais novo para o mais antigo (sem "data" contam como DATA, na ordem do dicionário)."""
    return sorted(ARTIGOS, key=lambda s: ARTIGOS[s].get("data", DATA), reverse=True)


def cards_artigos(slugs, destaque=False):
    out = ""
    for i, s in enumerate(slugs):
        a = ARTIGOS[s]
        tt = temas(a)
        d = destaque and i == 0
        busca = esc(" ".join([a["titulo"], a["desc"], a.get("tag", "")] + [TEMAS[t] for t in tt]).lower())
        rot = ("Mais recente · " if d else "") + a["tag"]
        out += f"""<a class="post rv{' post-dest' if d else ''}" href="/blog/{s}/" data-temas="{' '.join(tt)}" data-busca="{busca}">{foto(a['foto'], a['titulo'], 900, 600, lazy=i > 1)}<span class="rotulo">{rot}</span><h3>{a['titulo']}</h3><p>{a['desc']}</p><span class="post-meta">{data_br(a)} · {leitura(a)} min de leitura</span></a>"""
    return out


def home():
    titulo = f"{NOME} | Treino em comunidade: Hyrox, CrossFit, ATHX e corrida"
    desc = "Comunidade para treinar junto, com constância, técnica e cuidado com a lesão. Guias de Hyrox, CrossFit, ATHX e corrida, e o lançamento do membro fundador."
    ld = [org_ld(), faq_ld(HOME_FAQ)]
    pil = "".join(f'<div class="cartao rv"><span class="n">{i:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(PILARES, 1))
    pas = "".join(f'<li class="rv"><span class="n">{i}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(PASSOS, 1))
    tick = "".join(f"<span>{x}</span>" for x in ["Hyrox", "CrossFit", "ATHX", "Corrida", "Movimento", "Conexão", "Superação", "Comunidade"]) * 2
    return "/", head(titulo, desc, "/", ld) + f"""<main>
<section class="h-hero"><video class="fundo" autoplay muted loop playsinline preload="metadata" poster="/assets/img/foto-dupla.webp" aria-hidden="true"><source src="/assets/video/hero.mp4" type="video/mp4"></video><div class="s-wide">
<span class="rotulo">{NOME}</span><div class="faixas"></div>
<h1>Treinar é só o <span class="tarja"><span>começo</span></span></h1>
<p class="lead">A gente treina junto, com constância, técnica e cuidado com a lesão. Movimento, conexão e superação.</p>
<div class="acoes"><a class="s-btn" href="{DM}">Chamar no direct</a><a class="s-btn vazado" href="/comunidade/">Conhecer a comunidade</a></div>
</div></section>
<div class="ticker" aria-hidden="true"><div>{tick}</div></div>

<section class="h-sec" id="comunidade"><div class="s-wide dupla"><div class="rv"><span class="rotulo">O que é</span><h2>Uma comunidade para quem treina de verdade.</h2>
<p>A {NOME} reúne quem treina Hyrox, CrossFit, corrida ou academia, de qualquer nível. A ideia é simples: treinar junto torna a rotina mais fácil de manter, e técnica e cuidado com o corpo evitam que a lesão tire você do jogo.</p>
<p><a class="s-btn" href="/comunidade/">Ler mais</a></p></div>
<div class="rv">{foto('foto-dupla', 'Dupla treinando junto', 1200, 800, cls='arredonda')}</div></div></section>

<section class="h-sec" id="pilares"><div class="s-wide"><span class="rotulo">O que a gente faz</span><h2>Quatro coisas que sustentam o treino.</h2>
<p class="suave">Conteúdo e comunidade em torno do que faz alguém treinar por anos, e não só por semanas.</p>
<div class="pilares">{pil}</div></div></section>

<section class="h-sec escura2" id="modalidades"><div class="s-wide"><span class="rotulo">Modalidades</span><h2>Guias para cada jeito de treinar.</h2>
<p class="suave">Conteúdo claro sobre o formato, o treino e os cuidados de cada modalidade.</p>
<div class="mods">{cards_modalidades()}</div></div></section>

<section class="h-sec"><div class="s-wide"><span class="rotulo">Como entrar</span><h2>Três passos, sem burocracia.</h2>
<ol class="passos">{pas}</ol></div></section>

<section class="h-sec clara"><div class="s-wrap s-main rv"><span class="rotulo">Quem está por trás</span><h2>Ciência aplicada, na linguagem de quem treina.</h2>
<p>A comunidade é criada por <a href="{ED}">Ed Ferrari Jr</a>, fisioterapeuta ortopédico e esportivo (CREFITO-3/306266-F). O foco é ajudar quem treina a ter constância, técnica e cuidado com o corpo.</p></div></section>

<section class="h-sec"><div class="s-wide"><span class="rotulo">Blog</span><h2>Para ler e aplicar no treino.</h2>
<div class="posts">{cards_artigos(recentes()[:3])}</div>
<p style="margin-top:28px"><a class="s-btn vazado" href="/blog/">Ver todos os artigos</a></p></div></section>

<section class="h-sec"><div class="s-wrap"><span class="rotulo">Perguntas frequentes</span><h2>Dúvidas comuns.</h2><div class="faqs">{faq_html(HOME_FAQ)}</div></div></section>
{cta_bloco()}
</main>
""" + foot()


def comunidade():
    titulo = f"Sobre a {NOME}: treinar em comunidade"
    desc = f"Conheça a {NOME}: o que é, em que acreditamos, como participar e quem criou. Treino com constância, técnica e cuidado com a lesão."
    ld = [org_ld(), crumbs([("Início", "/"), ("Comunidade", "/comunidade/")])]
    pil = "".join(f'<div class="cartao rv"><span class="n">{i:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(PILARES, 1))
    return "/comunidade/", head(titulo, desc, "/comunidade/", ld) + f"""<main>
<section class="pg-hero"><div class="s-wrap"><span class="rotulo">Comunidade</span><div class="faixas"></div>
<h1>Treinar é só o <span class="tarja"><span>começo</span></span></h1>
<p class="lead">A {NOME} nasceu para juntar quem treina e quer fazer isso por muito tempo.</p></div></section>
<section class="h-sec"><div class="s-wrap s-main">
<h2>Em que a gente acredita</h2>
<p>Treino é mais fácil de manter quando existe gente junto. E dura mais quando vem com técnica, descanso e atenção ao que o corpo diz. Por isso a comunidade fala de hábito, movimento e prevenção de lesão, além de acompanhar modalidades como Hyrox, CrossFit, ATHX e corrida.</p>
<h2>Para quem é</h2>
<p>Para quem treina, de qualquer nível: do primeiro mês de academia à preparação para uma prova. Não é preciso ser atleta.</p></div></section>
<section class="h-sec"><div class="s-wide"><span class="rotulo">Pilares</span><h2>O que sustenta a comunidade.</h2><div class="pilares">{pil}</div></div></section>
<section class="h-sec clara"><div class="s-wrap s-main"><span class="rotulo">Quem criou</span><h2>Ed Ferrari Jr</h2>
<p>Fisioterapeuta ortopédico e esportivo (CREFITO-3/306266-F), trabalha com reabilitação e retorno ao esporte. Conheça o trabalho clínico em <a href="{ED}">edferrarijr.com</a>.</p>
<p><a class="s-btn" href="/membro-fundador/">Membro fundador</a></p></div></section>
{cta_bloco()}
</main>
""" + foot()


def modalidade(slug):
    m = MODALIDADES[slug]
    ld = [org_ld(), faq_ld(m["faq"]), crumbs([("Início", "/"), (m["nome"], f"/{slug}/")]),
          {"@context": "https://schema.org", "@type": "Article", "headline": m["titulo"].split(" | ")[0], "description": m["desc"], "inLanguage": "pt-BR",
           "dateModified": DATA, "author": {"@type": "Person", "name": "Ed Ferrari Jr", "url": ED + "/"}, "publisher": {"@id": BASE + "/#org"},
           "image": f"{BASE}/assets/img/{m['foto']}.webp", "mainEntityOfPage": f"{BASE}/{slug}/"}]
    corpo = ""
    for h, paras in m["blocos"]:
        corpo += f"<h2>{h}</h2>"
        for p in paras:
            if isinstance(p, tuple):
                corpo += "<ul>" + "".join(f"<li>{esc(i)}</li>" for i in p[1]) + "</ul>"
            else:
                corpo += f"<p>{p}</p>"
    fontes = ""
    if m.get("fontes"):
        fontes = "<h2>Fontes</h2><ul>" + "".join(f'<li><a href="{u}" rel="nofollow noopener" target="_blank">{esc(t)}</a></li>' for t, u in m["fontes"]) + "</ul>"
    outras = "".join(f'<a class="s-btn vazado small" href="/{s}/">{x["nome"]}</a>' for s, x in MODALIDADES.items() if s != slug)
    rel = [s for s, a in ARTIGOS.items() if slug in a["relacionados"]]
    rel_html = f'<section class="h-sec"><div class="s-wide"><span class="rotulo">Para ler</span><h2>Artigos relacionados.</h2><div class="posts">{cards_artigos(rel)}</div></div></section>' if rel else ""
    return f"/{slug}/", head(m["titulo"], m["desc"], f"/{slug}/", ld, og=f"{BASE}/assets/img/{m['foto']}.webp") + f"""<main>
<section class="pg-hero com-foto"><div class="fundo-img" style="--pos:{m['pos']}">{foto(m['foto'], 'Treino de ' + m['nome'], 1600, 1000, lazy=False)}</div><div class="s-wide"><span class="rotulo">{m['nome']}</span><div class="faixas"></div>
<h1>{m['h1']}</h1><p class="lead">{m['intro']}</p><div class="acoes"><a class="s-btn" href="{DM}">Chamar no direct</a></div></div></section>
<section class="h-sec"><div class="s-wrap s-main">{corpo}{fontes}
<h2>Perguntas frequentes</h2><div class="faqs">{faq_html(m['faq'])}</div>
<p class="s-note">Conteúdo informativo, elaborado pela {NOME}. Não substitui avaliação individual de um profissional de saúde.</p>
<div class="outras"><span class="rotulo">Outras modalidades</span><div class="acoes">{outras}</div></div></div></section>
{rel_html}
{cta_bloco()}
</main>
""" + foot()


def artigo(slug):
    a = ARTIGOS[slug]
    c = f"/blog/{slug}/"
    ld = [org_ld(), crumbs([("Início", "/"), ("Blog", "/blog/"), (a["titulo"], c)]),
          {"@context": "https://schema.org", "@type": "BlogPosting", "headline": a["titulo"], "description": a["desc"], "inLanguage": "pt-BR",
           "datePublished": a.get("data", DATA), "dateModified": a.get("data", DATA), "image": f"{BASE}/assets/img/{a['foto']}.webp",
           "author": {"@type": "Person", "name": "Ed Ferrari Jr", "url": ED + "/"}, "publisher": {"@id": BASE + "/#org"}, "mainEntityOfPage": BASE + c}]
    corpo = ""
    for t, v in a["corpo"]:
        if t == "p": corpo += f"<p>{v}</p>"
        elif t == "h2": corpo += f"<h2>{v}</h2>"
        elif t == "ul": corpo += "<ul>" + "".join(f"<li>{esc(i)}</li>" for i in v) + "</ul>"
    rel = "".join(f'<a class="s-btn vazado small" href="/{s}/">{MODALIDADES[s]["nome"]}</a>' for s in a["relacionados"])
    tt = temas(a)
    chips = "".join(f'<a class="b-chip" href="/blog/?tema={t}">{TEMAS[t]}</a>' for t in tt)
    # continue lendo: mais temas em comum primeiro, depois os mais recentes
    outros = [s for s in recentes() if s != slug]
    outros.sort(key=lambda s: len(set(temas(ARTIGOS[s])) & set(tt)), reverse=True)
    return c, head(a["titulo"] + " | " + NOME, a["desc"], c, ld, og=f"{BASE}/assets/img/{a['foto']}.webp") + f"""<main>
<section class="pg-hero com-foto"><div class="fundo-img" style="--pos:{a['pos']}">{foto(a['foto'], a['titulo'], 1600, 1000, lazy=False)}</div><div class="s-wrap"><span class="rotulo">{a['tag']} · {data_br(a)} · {leitura(a)} min de leitura</span><div class="faixas"></div>
<h1 class="h1-menor">{a['titulo']}</h1><div class="b-chips">{chips}</div></div></section>
<article class="h-sec"><div class="s-wrap s-main">{corpo}
<div class="outras"><span class="rotulo">Veja também</span><div class="acoes">{rel}<a class="s-btn vazado small" href="/blog/">Todos os artigos</a></div></div>
<p class="s-note">Por Ed Ferrari Jr, fisioterapeuta (CREFITO-3/306266-F). Conteúdo informativo, sem substituir a avaliação de um profissional de saúde.</p></div></article>
<section class="h-sec" style="padding-top:0"><div class="s-wide"><span class="rotulo">Continue lendo</span><h2>Você também pode gostar</h2><div class="posts">{cards_artigos(outros[:3])}</div></div></section>
{cta_bloco()}
</main>
""" + foot()


def blog():
    titulo = f"Blog | {NOME}"
    desc = "Treino, prevenção de lesão, hábitos e notícias de Hyrox, CrossFit, ATHX e corrida, em linguagem de quem treina. Busque por tema ou palavra."
    lista = recentes()
    usados = {t for s in lista for t in temas(ARTIGOS[s])}
    chips = '<button type="button" class="b-chip on" data-tema="">Todos</button>' + "".join(
        f'<button type="button" class="b-chip" data-tema="{t}">{n}</button>' for t, n in TEMAS.items() if t in usados)
    ld = [org_ld(), crumbs([("Início", "/"), ("Blog", "/blog/")])]
    return "/blog/", head(titulo, desc, "/blog/", ld) + f"""<main>
<section class="pg-hero"><div class="s-wrap"><span class="rotulo">Blog</span><div class="faixas"></div><h1>Para ler e <span class="tarja"><span>aplicar</span></span></h1>
<p class="lead">Dúvidas de quem treina Hyrox, CrossFit, ATHX e corrida, respondidas sem enrolação, e as notícias do Radar.</p></div></section>
<section class="h-sec" style="padding-top:10px"><div class="s-wide">
<div class="b-filtros"><input class="b-busca" type="search" placeholder="Buscar: Hyrox, aquecimento, dor..." aria-label="Buscar no blog" autocomplete="off">
<div class="b-chips" role="group" aria-label="Filtrar por tema">{chips}</div>
<p class="b-vazio" hidden>Nenhum artigo encontrado. Tente outra palavra ou <a href="{DM}">mande a sua dúvida no direct</a>: ela pode virar o próximo artigo.</p></div>
<div class="posts" data-blog>{cards_artigos(lista, destaque=True)}</div></div></section>
{cta_bloco()}
</main>
""" + foot()


def fundador():
    titulo = f"Membro fundador | {NOME}"
    desc = f"O lançamento do membro fundador da {NOME} ainda não abriu. Entre na lista de interesse chamando no direct."
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": titulo, "url": BASE + "/membro-fundador/", "inLanguage": "pt-BR"},
          crumbs([("Início", "/"), ("Membro fundador", "/membro-fundador/")])]
    return "/membro-fundador/", head(titulo, desc, "/membro-fundador/", ld) + f"""<main class="s-main"><div class="s-wrap" style="padding-top:70px">
<span class="rotulo">Membro fundador</span><div class="faixas"></div>
<h1>Seja um dos <span class="tarja"><span>primeiros</span></span></h1>
<p style="font-size:1.25rem;color:var(--suave);margin:22px 0 10px">O membro fundador é quem constrói a comunidade com a gente desde o começo.</p>
<h2>Como está o lançamento</h2>
<p>O lançamento <strong>ainda não abriu</strong>. Quem entrar na lista de interesse é avisado primeiro, quando houver data e condições. Entrar na lista não é compromisso e não garante vaga.</p>
<h2>Como entrar na lista</h2>
<p>Chame a gente no direct do Instagram e escreva "quero ser avisado". Só isso.</p>
<p style="margin-top:26px"><a class="s-btn" href="{DM}">Entrar na lista pelo direct</a></p>
</div></main>
""" + foot()


def erro404():
    return "/404.html", head("Página não encontrada | " + NOME, "Página não encontrada.", "/404.html", [], robots="noindex") + f"""<main class="s-main"><div class="s-wrap" style="padding:90px 24px">
<span class="rotulo">Erro 404</span><div class="faixas"></div><h1>Essa página <span class="tarja"><span>não existe</span></span></h1>
<p style="margin:22px 0 28px">O endereço pode ter mudado. Volte ao início ou chame a comunidade no direct.</p>
<div class="acoes"><a class="s-btn" href="/">Voltar ao início</a><a class="s-btn vazado" href="{DM}">Chamar no direct</a></div></div></main>
""" + foot()


def escrever(c, h):
    if c.endswith(".html"):
        open(os.path.join(RAIZ, c.strip("/")), "w", encoding="utf-8").write(h)
        return
    p = os.path.join(RAIZ, c.strip("/"))
    os.makedirs(p, exist_ok=True)
    open(os.path.join(p, "index.html"), "w", encoding="utf-8").write(h)


if __name__ == "__main__":
    paginas = [home(), comunidade(), blog(), fundador()] + [modalidade(s) for s in MODALIDADES] + [artigo(s) for s in ARTIGOS]
    urls = []
    for c, h in paginas:
        escrever(c, h); urls.append(c)
    ultimo = {f"/blog/{k}/": v["data"] for k, v in ARTIGOS.items() if "data" in v}
    c, h = erro404(); escrever(c, h)
    prio = {"/": "1.0"}
    itens = "".join(f"  <url><loc>{BASE}{c}</loc><lastmod>{ultimo.get(c, DATA)}</lastmod><priority>{prio.get(c, '0.7')}</priority></url>\n" for c in urls)
    open(os.path.join(RAIZ, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{itens}</urlset>\n')
    open(os.path.join(RAIZ, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    print(len(urls), "páginas")
