#!/usr/bin/env python3
"""Gera o site da Next Level Fitness (home, membro fundador, sitemap e robots). Uso: python3 tools/gerar.py"""
import json, os
BASE = "https://www.nextlevelfitness.com.br"
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DM = "https://ig.me/m/nextlevelfitness.community"
IG = "https://www.instagram.com/nextlevelfitness.community/"
DATA = "2026-10-18"


def head(titulo, desc, caminho, ld):
    u = BASE + caminho
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{titulo}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{u}">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Next Level Fitness">
<meta property="og:url" content="{u}"><meta property="og:title" content="{titulo}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}/assets/img/foto-dupla.webp">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="/assets/fonts/BarlowCondensed-800i.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/Barlow-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="icon" href="/assets/img/logo.png">
<link rel="stylesheet" href="/css/site.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<header class="s-header"><div class="s-wide">
<a class="s-brand" href="/"><img src="/assets/img/logo.png" alt="Logo da Next Level Fitness" width="42" height="42">Next Level</a>
<nav class="s-nav" aria-label="Principal"><a href="/#pilares">Comunidade</a><a href="/membro-fundador/">Membro fundador</a><a class="s-btn small" href="{DM}">Chamar no direct</a></nav>
</div></header>
"""


def foot():
    return f"""<footer class="s-footer"><div class="s-wide"><div class="cols">
<div class="assin"><img src="/assets/img/logo.png" alt="" width="42" height="42">Next Level Fitness</div>
<div><a href="/#pilares">Comunidade</a><a href="/membro-fundador/">Membro fundador</a><a href="{IG}">Instagram</a><a href="{DM}">Chamar no direct</a></div>
<div>Criada por <a href="https://www.edferrarijr.com" style="display:inline">Ed Ferrari Jr</a>,<br>fisioterapeuta CREFITO-3/306266-F</div>
</div>
<p class="s-note">Conteúdo informativo, sem substituir a avaliação de um profissional de saúde. Cada pessoa responde de um jeito ao treino. © 2026 Next Level Fitness.</p>
</div></footer>
</body>
</html>
"""


PILARES = [
    ("Hábitos que sustentam", "Constância vence motivação. A gente fala de rotina simples, sono, descanso e o que cabe na sua semana."),
    ("Movimento bem feito", "Técnica antes de carga. Explicamos o movimento de um jeito que dá para entender e repetir."),
    ("Treinar sem se lesionar", "Dor no treino merece atenção. Dicas de aquecimento, progressão e quando procurar um profissional."),
    ("Gente da comunidade", "Treinar junto é mais fácil de manter. Histórias, desafios em dupla e quem treina com a gente."),
]


def home():
    titulo = "Next Level Fitness | Comunidade de treino"
    desc = "Comunidade para treinar junto, com constância, técnica e cuidado com a lesão. Chame no direct e conheça o membro fundador."
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": BASE + "/#org", "name": "Next Level Fitness", "url": BASE + "/", "logo": BASE + "/assets/img/logo.png",
         "sameAs": [IG], "founder": {"@type": "Person", "name": "Ed Ferrari Jr", "url": "https://www.edferrarijr.com/"}},
        {"@type": "WebSite", "@id": BASE + "/#site", "url": BASE + "/", "name": "Next Level Fitness", "inLanguage": "pt-BR"}]}
    cards = "".join(f'<div class="cartao"><span class="n">{i:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(PILARES, 1))
    return "/", head(titulo, desc, "/", ld) + f"""<main>
<section class="h-hero"><img class="fundo" src="/assets/img/foto-dupla.webp" alt="" width="1800" height="1200" fetchpriority="high"><div class="s-wide">
<span class="rotulo">Comunidade de treino</span><div class="faixas"></div>
<h1>Treinar é só o <span class="tarja"><span>começo</span></span></h1>
<p class="lead">A gente treina junto, com constância, técnica e cuidado com a lesão. Movimento, conexão e superação.</p>
<div class="acoes"><a class="s-btn" href="{DM}">Chamar no direct</a><a class="s-btn vazado" href="/membro-fundador/">Membro fundador</a></div>
</div></section>

<section class="h-sec" id="pilares"><div class="s-wide"><span class="rotulo">O que a gente faz</span><h2>Quatro coisas que sustentam o treino.</h2>
<p class="suave">Conteúdo e comunidade em torno do que faz alguém treinar por anos, e não só por semanas.</p>
<div class="pilares">{cards}</div></div></section>

<section class="h-sec clara"><div class="s-wrap s-main"><span class="rotulo">Quem está por trás</span><h2>Ciência aplicada, na linguagem de quem treina.</h2>
<p>A Next Level Fitness é uma comunidade para quem treina, de qualquer nível, onde técnica e cuidado com o corpo andam junto com a rotina. Ela é criada por <a href="https://www.edferrarijr.com">Ed Ferrari Jr</a>, fisioterapeuta ortopédico e esportivo (CREFITO-3/306266-F).</p></div></section>

<section class="h-sec"><div class="s-wide"><div class="s-cta"><span class="rotulo" style="color:#fff">Quer fazer parte?</span><h2>Chame no direct.</h2>
<p>Conte o que você treina e o que procura. A gente responde e avisa as novidades, incluindo o lançamento do membro fundador.</p>
<a class="s-btn" href="{DM}">Chamar no direct</a></div></div></section>
</main>
""" + foot()


def fundador():
    titulo = "Membro fundador | Next Level Fitness"
    desc = "O lançamento do membro fundador da Next Level Fitness ainda não abriu. Entre na lista de interesse chamando no direct."
    ld = {"@context": "https://schema.org", "@type": "WebPage", "name": titulo, "url": BASE + "/membro-fundador/", "inLanguage": "pt-BR"}
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


def escrever(c, h):
    p = os.path.join(RAIZ, c.strip("/"))
    os.makedirs(p, exist_ok=True)
    open(os.path.join(p, "index.html"), "w", encoding="utf-8").write(h)


if __name__ == "__main__":
    urls = []
    for f in (home, fundador):
        c, h = f(); escrever(c, h); urls.append(c)
    itens = "".join(f"  <url><loc>{BASE}{c}</loc><lastmod>{DATA}</lastmod></url>\n" for c in urls)
    open(os.path.join(RAIZ, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{itens}</urlset>\n')
    open(os.path.join(RAIZ, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    print(len(urls), "páginas")
