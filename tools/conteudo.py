"""Textos do site Next Level Fitness Community. Editar aqui e rodar `python3 tools/gerar.py`.
Regras: sem promessa de resultado, sem depoimento, sem preço, sem inventar fatos da comunidade (local, horários, vagas)."""

PILARES = [
    ("Hábitos que sustentam", "Constância vence motivação. A gente fala de rotina simples, sono, descanso e o que cabe na sua semana."),
    ("Movimento bem feito", "Técnica antes de carga. Explicamos o movimento de um jeito que dá para entender e repetir."),
    ("Treinar sem se lesionar", "Dor no treino merece atenção. Dicas de aquecimento, progressão e quando procurar um profissional."),
    ("Gente da comunidade", "Treinar junto é mais fácil de manter. Histórias, desafios em dupla e quem treina com a gente."),
]

PASSOS = [
    ("Chame no direct", "Mande uma mensagem para o perfil da comunidade no Instagram. Não precisa de apresentação formal."),
    ("Conte o que você treina", "Hyrox, CrossFit, corrida, academia ou ainda está começando. Qualquer nível é bem-vindo."),
    ("Receba as novidades", "A gente responde e avisa o que acontece na comunidade, incluindo o lançamento do membro fundador."),
]

HOME_FAQ = [
    ("O que é a Next Level Fitness Community?",
     "É uma comunidade para quem treina, de qualquer nível, em que técnica, hábitos e cuidado com o corpo andam junto com a rotina de treino. Ela nasceu no Instagram e tem este site como ponto de encontro."),
    ("Preciso ser atleta para participar?",
     "Não. A comunidade é para quem treina, seja Hyrox, CrossFit, corrida, academia ou o primeiro mês de treino."),
    ("Como eu entro?",
     "Chamando a comunidade no direct do Instagram. Conte o que você treina e o que procura, e a gente responde."),
    ("A Next Level substitui a avaliação de um profissional de saúde?",
     "Não. O conteúdo é informativo e educativo. Se você tem dor, lesão ou condição de saúde, procure um profissional para uma avaliação individual."),
    ("Quem está por trás da comunidade?",
     "A comunidade é criada pelo fisioterapeuta Ed Ferrari Jr (CREFITO-3/306266-F), que trabalha com reabilitação ortopédica e esportiva."),
    ("O que é o membro fundador?",
     "É quem constrói a comunidade desde o começo. O lançamento ainda não abriu: quem entra na lista de interesse é avisado primeiro, sem compromisso e sem garantia de vaga."),
]

# Modalidades: páginas-guia (conteúdo educativo, sem promessa de resultado)
MODALIDADES = {
    "hyrox": {
        "nome": "Hyrox", "foto": "sled", "pos": "50% 60%",
        "titulo": "Hyrox: como funciona a prova e como se preparar | Next Level Fitness Community",
        "desc": "Guia de Hyrox para quem treina: formato da prova, as oito estações, erros comuns de iniciante e cuidados para treinar sem se lesionar.",
        "h1": "Hyrox, do <em>primeiro</em> km à última estação",
        "intro": "Hyrox é uma prova de fitness que combina corrida e estações funcionais. Esta página explica o formato e o que costuma pesar em quem vai fazer a primeira.",
        "blocos": [
            ("Como é a prova", [
                "A prova tem oito rodadas: cada uma começa com 1 km de corrida e termina em uma estação de esforço funcional. Ao todo são 8 km de corrida e 8 estações, feitas em sequência e contra o relógio.",
                "As estações, na ordem: SkiErg (1.000 m), Sled Push (50 m), Sled Pull (50 m), Burpee Broad Jump (80 m), remo (1.000 m), Farmers Carry (200 m), Sandbag Lunges (100 m) e Wall Balls (100 repetições). As cargas mudam conforme a categoria."]),
            ("O que costuma pesar para quem está começando", [
                ("lista", [
                    "Ritmo da corrida: sair rápido demais no começo cobra o preço nas últimas estações.",
                    "Troca entre corrida e estação: o corpo sai de um esforço de força e já precisa correr de novo.",
                    "Sled e lunges com sandbag: exigem técnica, e o volume acumulado cansa quadril, joelho e tornozelo.",
                    "Falta de simulação: treinar corrida e estações separadas, sem nunca juntar."])]),
            ("Como a comunidade enxerga a preparação", [
                "Constância e progressão pesam mais do que um treino heroico. Aumente carga e volume aos poucos, simule partes da prova antes da prova inteira e respeite os dias de descanso.",
                "Se uma dor aparece e não passa, não ignore. Em Hyrox, as regiões que mais pedem atenção costumam ser joelho, quadril, lombar e ombro. Procure um profissional para avaliar antes que atrapalhe o treino."]),
        ],
        "faq": [
            ("Quantos quilômetros de corrida tem no Hyrox?", "São 8 km no total, em 8 trechos de 1 km, cada um seguido de uma estação."),
            ("Preciso ser corredor para fazer Hyrox?", "Não precisa ser corredor de elite, mas a corrida representa boa parte da prova. Vale incluir treino de corrida na rotina com progressão gradual."),
            ("Dá para treinar Hyrox em comunidade?", "Dá, e ajuda a manter a constância. Treinar em dupla ou grupo também facilita simular a prova."),
        ],
    },
    "crossfit": {
        "nome": "CrossFit", "foto": "crossfit-barra", "pos": "50% 40%",
        "titulo": "CrossFit: como começar e treinar com segurança | Next Level Fitness Community",
        "desc": "Guia de CrossFit para quem treina: o que é, como funciona o treino do dia, adaptação de movimentos e cuidados com ombro, lombar e joelho.",
        "h1": "CrossFit com <em>técnica</em> e constância",
        "intro": "CrossFit reúne movimentos funcionais variados em treinos de intensidade alta. Aqui vai o que ajuda a começar e a manter o treino por anos.",
        "blocos": [
            ("O que é o treino", [
                "O treino costuma misturar levantamento de peso, ginástica e condicionamento (corrida, remo, bike). Em geral há aquecimento, uma parte de técnica ou força e o treino do dia, conhecido como WOD."]),
            ("Escalonar é parte do treino", [
                "Adaptar carga, repetições ou o próprio movimento mantém o treino seguro e permite praticar a técnica. Quem escalona bem evolui com mais constância do que quem insiste em carga que ainda não domina.",
                ("lista", [
                    "Domine o padrão do movimento antes de aumentar a carga.",
                    "Aumente peso e volume de forma gradual.",
                    "Priorize o descanso entre as sessões mais intensas."])]),
            ("Regiões que pedem atenção", [
                "Ombro (movimentos overhead e ginásticos), lombar (levantamentos) e joelho (agachamentos e saltos) costumam receber bastante carga. Dor que se repete, piora durante o treino ou muda a forma de executar o movimento merece avaliação profissional."]),
        ],
        "faq": [
            ("CrossFit serve para iniciante?", "Pode servir, desde que os movimentos sejam adaptados ao nível de cada pessoa e a progressão seja gradual."),
            ("Quantas vezes por semana treinar?", "Depende do seu histórico, da sua recuperação e da sua rotina. O ideal é uma frequência que você consiga sustentar, com dias de descanso."),
            ("Senti dor no ombro no treino, o que faço?", "Reduza ou ajuste os movimentos que provocam a dor e procure um fisioterapeuta ou médico se ela persistir ou piorar."),
        ],
    },
    "athx": {
        "nome": "ATHX", "foto": "sandbag", "pos": "50% 30%",
        "titulo": "ATHX: o que é a competição híbrida de fitness | Next Level Fitness Community",
        "desc": "Entenda o ATHX: competição híbrida de fitness criada no Reino Unido, com zonas de força, resistência e metcon. Formato, origem e como se preparar.",
        "h1": "ATHX: <em>força</em>, resistência e metcon",
        "intro": "ATHX é uma competição de fitness híbrido criada no Reino Unido. O formato mistura levantamento, corrida, remo e circuitos funcionais.",
        "blocos": [
            ("O que é", [
                "O formato original foi descrito como uma competição contínua de cerca de duas horas e meia, dividida em seis zonas, que os atletas percorrem em sequência. A prova avalia três frentes: força (levantamentos com barra), resistência (corrida e remo) e metcon (circuito funcional).",
                "O ATHX surgiu no Reino Unido em 2023. Em dezembro de 2025, a organização anunciou parceria global com a adidas. No Brasil, o Wodnation Sprint, realizado em Valinhos (SP) em junho de 2026, foi apresentado como evento inspirado nesse formato."]),
            ("O que pesa na preparação", [
                ("lista", [
                    "Base de força com técnica: levantamentos com barra pedem padrão de movimento consistente.",
                    "Capacidade aeróbia: corrida e remo em volume exigem constância de treino.",
                    "Transições: passar de força para resistência e de volta é parte do desafio.",
                    "Recuperação: competições longas pedem planejamento de descanso e carga."])]),
            ("Aviso", [
                "A Next Level Fitness Community não é afiliada à ATHX nem à adidas. Regras, formatos e datas mudam: confira sempre o site oficial da organização."]),
        ],
        "fontes": [
            ("ATHX Games: what it is and how it works (Velites)", "https://ca.velitessport.com/blogs/news/athx-games"),
            ("ATHX Games, global expansion and adidas partnership (Athletech News)", "https://athletechnews.com/athx-games-global-expansion-adidas-partnership/"),
            ("Wodnation Sprint em Valinhos (Correio da Manhã)", "https://www.correiodamanha.com.br/nacional/sao-paulo/campinas/regiao-de-campinas/2026/05/285966-valinhos-sedia-o-wodnation-sprint-campeonato-fitness-inedito-no-brasil.html"),
        ],
        "faq": [
            ("O que significa Metcon?", "É a abreviação de metabolic conditioning, um circuito funcional de condicionamento, feito em intensidade alta."),
            ("O ATHX tem o mesmo formato do Hyrox?", "Não. O Hyrox tem formato fixo de 8 km de corrida com 8 estações. O ATHX é dividido em zonas que misturam força, resistência e metcon."),
            ("A Next Level é organizadora do ATHX?", "Não. A comunidade apenas conversa sobre a modalidade e ajuda quem treina a se preparar."),
        ],
    },
    "corrida": {
        "nome": "Corrida", "foto": "corrida-laranja", "pos": "50% 50%",
        "titulo": "Corrida para quem treina: como progredir sem se lesionar | Next Level Fitness Community",
        "desc": "Guia de corrida para quem treina funcional, Hyrox ou academia: como encaixar a corrida na rotina, progredir aos poucos e cuidar de joelho e tornozelo.",
        "h1": "Corrida sem <em>pressa</em> de se machucar",
        "intro": "Muita gente que treina funcional ou Hyrox precisa correr mais. Esta página reúne o que ajuda a encaixar a corrida na rotina com segurança.",
        "blocos": [
            ("Como encaixar a corrida na rotina", [
                ("lista", [
                    "Comece com volumes que você consiga repetir com conforto e aumente aos poucos.",
                    "Alterne corrida e caminhada se estiver retomando.",
                    "Evite somar corrida nova e aumento de carga de força na mesma semana.",
                    "Dê espaço para descanso entre as sessões mais intensas."])]),
            ("Calçado, superfície e técnica", [
                "Tênis confortável, superfícies variadas e cadência natural ajudam a distribuir a carga. Não existe técnica única que sirva para todo mundo: observe como o seu corpo responde."]),
            ("Quando procurar um profissional", [
                "Dor que persiste por vários dias, que piora ao correr, que muda o seu jeito de correr ou que vem com inchaço merece avaliação de um fisioterapeuta ou médico do esporte."]),
        ],
        "faq": [
            ("Quanto posso aumentar a corrida por semana?", "Não há número único. O aumento gradual, com bom descanso e sem dor crescente, é uma referência mais segura do que seguir uma regra fixa."),
            ("Corrida atrapalha o ganho de força?", "Depende do volume e da organização da semana. Planejar os dias de corrida e de força ajuda a equilibrar os dois."),
            ("Tenho dor no joelho ao correr. Devo parar?", "Reduza o volume e procure um profissional para avaliar, principalmente se a dor se repete ou piora."),
        ],
    },
}

# Filtros do blog. Artigo novo: "data" (AAAA-MM-DD) põe no topo; "temas" usa estas chaves.
TEMAS = {"hyrox": "Hyrox", "crossfit": "CrossFit", "athx": "ATHX", "corrida": "Corrida",
         "prevencao": "Prevenção de lesão", "habitos": "Hábitos", "radar": "Radar"}

ARTIGOS = {
    "como-comecar-no-hyrox": {
        "titulo": "Primeira prova de Hyrox: 5 passos para começar sem se perder",
        "temas": ["hyrox", "prevencao"],
        "desc": "Guia para a primeira prova de Hyrox: formato, estações, ritmo, treino em dupla e cuidados para não se lesionar no caminho.",
        "foto": "costas-sled", "pos": "50% 40%", "tag": "Hyrox",
        "corpo": [
            ("p", "Hyrox é uma prova com 8 km de corrida dividida em oito trechos de 1 km, cada um seguido de uma estação funcional. Se você nunca fez, o primeiro passo é entender o formato e escolher como quer preparar."),
            ("h2", "1. Conheça as estações"),
            ("p", "SkiErg, Sled Push, Sled Pull, Burpee Broad Jump, remo, Farmers Carry, Sandbag Lunges e Wall Balls. Algumas pedem técnica específica, e vale praticar cada uma separadamente antes de juntar tudo."),
            ("h2", "2. Controle o ritmo"),
            ("p", "O erro mais comum é largar rápido demais. A prova é longa, e o cansaço das últimas estações cobra o ritmo dos primeiros quilômetros. Treine em um ritmo que você consiga sustentar."),
            ("h2", "3. Simule partes da prova"),
            ("p", "Em vez de treinar corrida e estações em dias separados o tempo todo, inclua blocos que juntam as duas coisas, como 1 km de corrida seguido de uma estação. Aumente o número de rodadas aos poucos."),
            ("h2", "4. Cuide das articulações"),
            ("p", "Sled, lunges com sandbag e corrida acumulam carga em joelho, quadril e tornozelo. Aumente o volume aos poucos, reserve dias de descanso e não ignore a dor que se repete."),
            ("h2", "5. Treinar junto ajuda"),
            ("p", "Em dupla ou em grupo, fica mais fácil manter a constância e simular a prova. É o que a comunidade faz no dia a dia."),
        ],
        "relacionados": ["hyrox", "corrida"],
    },
    "constancia-vence-motivacao": {
        "titulo": "Constância vence motivação: 5 jeitos de manter o treino quando a vontade some",
        "temas": ["habitos"],
        "desc": "Como montar uma rotina de treino que você consiga manter: metas pequenas, horários fixos, descanso planejado e apoio da comunidade.",
        "foto": "corrida-bw", "pos": "50% 50%", "tag": "Hábitos",
        "corpo": [
            ("p", "Motivação vai e volta. O que sustenta o treino por meses e anos é rotina. Aqui vão ideias simples para montar uma que caiba na sua semana."),
            ("h2", "Comece menor do que você acha que deveria"),
            ("p", "Uma meta que você cumpre quase sempre vale mais do que uma meta grande que você abandona na segunda semana. Duas ou três sessões por semana, bem encaixadas, já constroem o hábito."),
            ("h2", "Defina horários e deixe a roupa pronta"),
            ("p", "Quanto menos decisões no dia, mais fácil treinar. Combine o horário com você mesmo e prepare o que precisa na véspera."),
            ("h2", "Planeje o descanso"),
            ("p", "Dormir bem e reservar dias mais leves fazem parte do treino. Quem descansa com planejamento costuma manter a regularidade por mais tempo."),
            ("h2", "Treine com gente"),
            ("p", "Combinar com alguém, ou fazer parte de uma comunidade, aumenta a chance de ir mesmo nos dias de menos vontade."),
            ("h2", "Tenha um plano para o dia ruim"),
            ("p", "Decida antes o que fazer quando faltar tempo ou energia: uma sessão curta, uma caminhada, um treino mais leve. Fazer um pouco, nesses dias, mantém o hábito vivo."),
        ],
        "relacionados": ["crossfit", "corrida"],
    },
    "dor-no-treino-quando-procurar-um-profissional": {
        "titulo": "Dor no treino: 5 sinais de que é hora de procurar um profissional",
        "temas": ["prevencao", "crossfit", "hyrox"],
        "desc": "Nem toda dor no treino é lesão, mas algumas pedem avaliação. Veja sinais de atenção e o que fazer enquanto não consegue consulta.",
        "foto": "barra-mulher", "pos": "50% 25%", "tag": "Lesão",
        "corpo": [
            ("p", "Desconforto muscular depois de um treino novo é comum. Já a dor que se repete, piora ou muda a forma como você se move merece atenção. Este texto é informativo e não substitui uma avaliação individual."),
            ("h2", "Sinais de que vale procurar um profissional"),
            ("ul", [
                "Dor que dura vários dias e não melhora com repouso relativo.",
                "Dor que piora durante o treino ou aparece em repouso e à noite.",
                "Inchaço, formigamento ou sensação de falta de força.",
                "Dor que faz você mudar o jeito de se movimentar.",
                "Dor depois de uma queda, torção ou pancada."]),
            ("h2", "O que costuma ajudar enquanto isso"),
            ("p", "Reduzir ou ajustar o que provoca a dor, mantendo o movimento que for confortável, costuma ser mais útil do que parar tudo ou forçar. Se tiver dúvida, não ignore: a avaliação ajuda a entender a causa."),
            ("h2", "Prevenção começa na progressão"),
            ("p", "Aumentar carga e volume aos poucos, variar estímulos e respeitar o descanso reduzem a chance de sobrecarga. Técnica e planejamento valem mais do que treino heroico."),
            ("p", "Se você precisa de avaliação, procure um fisioterapeuta ou médico do esporte. O criador da comunidade, Ed Ferrari Jr, é fisioterapeuta ortopédico e esportivo e atende em Campinas (SP). Veja mais em edferrarijr.com."),
        ],
        "relacionados": ["crossfit", "hyrox"],
    },
    "como-aquecer-antes-do-treino": {
        "titulo": "Como aquecer antes do treino (e os 4 erros mais comuns)",
        "temas": ["prevencao", "crossfit", "habitos"],
        "desc": "Aquecimento antes de treinar: por que ele ajuda, o que incluir (geral e específico) e erros comuns de quem pula essa etapa.",
        "foto": "sandbag-dupla", "pos": "50% 30%", "tag": "Movimento",
        "corpo": [
            ("p", "Aquecer é preparar o corpo para o que vem. Um aquecimento simples já ajuda a entrar no treino com mais conforto e atenção ao movimento."),
            ("h2", "Parte geral"),
            ("p", "Alguns minutos de movimento leve, como caminhada, bike, remo leve ou polichinelo, elevam a frequência cardíaca e deixam o corpo mais disposto."),
            ("h2", "Parte específica"),
            ("p", "Faça séries leves dos movimentos do treino do dia. Se vai agachar, agache com pouca carga primeiro. Se vai fazer movimentos overhead, mobilize o ombro e a coluna torácica antes."),
            ("h2", "Erros comuns"),
            ("ul", [
                "Pular o aquecimento por falta de tempo.",
                "Gastar tanto tempo que chega cansado ao treino.",
                "Alongar de forma intensa antes de um treino de força ou corrida e perder a ativação.",
                "Usar sempre o mesmo aquecimento, sem relação com o treino."]),
            ("p", "Não existe aquecimento único e ideal para todo mundo. Observe como você se sente e ajuste com a ajuda de quem acompanha o seu treino."),
        ],
        "relacionados": ["crossfit", "hyrox"],
    },
    "hyrox-tampa-2026-proxima-etapa": {
        "data": "2026-10-21",
        "titulo": "Hyrox Tampa 2026: a próxima etapa do circuito, de 22 a 25 de outubro",
        "temas": ["hyrox", "radar"],
        "desc": "Depois de São Paulo, o Hyrox segue para Tampa (EUA), de 22 a 25 de outubro de 2026. Veja o que se sabe da etapa e o que dá para aprender com o calendário da temporada.",
        "foto": "sled", "pos": "50% 40%", "tag": "Radar",
        "corpo": [
            ("p", "O circuito do Hyrox não para: depois da etapa de São Paulo, a próxima parada é Tampa, na Flórida (EUA). A página oficial do evento, no <a href=\"https://hyrox.com/event/hyrox-tampa/\" rel=\"noopener\" target=\"_blank\">site do Hyrox</a>, marca a prova de 22 a 25 de outubro de 2026."),
            ("h2", "O que se sabe até agora"),
            ("ul", [
                "Data: de 22 a 25 de outubro de 2026, em quatro dias de evento.",
                "Local: Tampa Convention Center, no centro da cidade, segundo as informações públicas do evento.",
                "Brasil: a temporada 2026/2027 foi aberta em São Paulo, em 17 de outubro, no Distrito Anhembi, com provas individuais, em duplas e em revezamento."]),
            ("h2", "Por que acompanhar o calendário"),
            ("p", "Olhar o calendário de outras etapas ajuda a planejar a sua própria temporada: escolher uma prova-alvo, trabalhar para trás o período de preparação e combinar com a dupla ou o grupo de treino. Quem treina em comunidade costuma manter melhor a regularidade."),
            ("h2", "Viajar para competir"),
            ("p", "Se a sua prova exige viagem, chegue com antecedência, hidrate-se e evite estrear tênis, estratégia de ritmo ou alimentação na semana da competição. Voos longos e muitas horas sentado cobram lombar e quadril, então levante e se movimente durante o trajeto."),
            ("p", "Quer entender o formato da prova antes de escolher a sua? Leia <a href=\"/blog/como-comecar-no-hyrox/\">Como começar no Hyrox</a> e veja a <a href=\"/hyrox/\">página de Hyrox da comunidade</a>."),
            ("p", "Este texto é um resumo independente do calendário oficial e não tem vínculo com a organização do Hyrox. Confira sempre datas e regras no site oficial do evento."),
        ],
        "relacionados": ["hyrox", "athx"],
    },
    "athx-final-2026-lisboa": {
        "data": "2026-10-22",
        "titulo": "ATHX 2026: a final será em Lisboa, de 27 a 29 de novembro",
        "temas": ["athx", "radar"],
        "desc": "O ATHX marcou a final de 2026 para Lisboa, de 27 a 29 de novembro. Veja o que o site oficial informa, as próximas etapas e como acompanhar com a comunidade.",
        "foto": "overhead", "pos": "50% 30%", "tag": "Radar",
        "corpo": [
            ("p", "O ATHX, competição híbrida com etapas em várias cidades, já tem local e data para a final de 2026. Segundo o <a href=\"https://athxgames.com/finals-qualification/2026\" rel=\"noopener\" target=\"_blank\">site oficial</a>, ela acontece de 27 a 29 de novembro, no Lisbon Exhibition and Congress Centre, em Lisboa."),
            ("h2", "O que se sabe"),
            ("ul", [
                "Final: de 27 a 29 de novembro de 2026, em Lisboa.",
                "Classificação: as vagas são conquistadas nas etapas disputadas ao longo de 2026.",
                "Próximas etapas no calendário oficial: Amsterdam e Los Angeles, ambas em 7 de novembro.",
                "Formato: cerca de 2 horas e meia em seis zonas, segundo o ATHX."]),
            ("h2", "Por que acompanhar"),
            ("p", "Conhecer o formato e o calendário ajuda a escolher uma meta para a sua temporada, seja a primeira prova híbrida, seja uma vaga em etapa. Treinar em dupla ou em grupo torna mais fácil manter a constância durante a preparação."),
            ("p", "Quer entender como o ATHX se compara a outras provas? Veja a <a href=\"/athx/\">página de ATHX da comunidade</a> e leia <a href=\"/blog/como-comecar-no-hyrox/\">Como começar no Hyrox</a>."),
            ("p", "Este texto é um resumo independente do que consta no site oficial do ATHX e não tem vínculo com a organização. Confira sempre datas e regras no site oficial."),
        ],
        "relacionados": ["athx", "hyrox"],
    },
    "hyrox-rio-de-janeiro-2026": {
        "data": "2026-10-26",
        "titulo": "Hyrox Rio de Janeiro 2026: a etapa brasileira volta ao Riocentro",
        "temas": ["hyrox", "radar"],
        "desc": "O Hyrox Rio de Janeiro 2026 será no Riocentro, em novembro. Veja o que o site oficial informa e como transformar a etapa em meta para o seu grupo de treino.",
        "foto": "sled", "pos": "50% 40%", "tag": "Radar",
        "corpo": [
            ("p", "O Brasil entra de novo no calendário do Hyrox. Segundo a <a href=\"https://hyrox.com/event/hyrox-rio-de-janeiro/\" rel=\"noopener\" target=\"_blank\">página oficial do evento</a>, a etapa do Rio de Janeiro da temporada 26/27 acontece em novembro de 2026, no Riocentro, na Barra Olímpica."),
            ("h2", "O que se sabe"),
            ("ul", [
                "Local: Riocentro, Av. Salvador Allende, 6555, Barra Olímpica, Rio de Janeiro.",
                "Data: a página indica o dia 21 de novembro de 2026.",
                "Programação: o Hyrox informa que os detalhes são provisórios e podem mudar.",
                "Edição anterior: a etapa de 2025 foi no mesmo endereço."]),
            ("h2", "Por que fazer dessa etapa uma meta"),
            ("p", "Ter uma data no calendário organiza o treino. Quem vai competir em dupla ou em grupo costuma manter mais a constância, dividir as estações e treinar as transições entre corrida e força, que são o coração da prova."),
            ("p", "Quer entender o formato? Veja a <a href=\"/hyrox/\">página de Hyrox da comunidade</a> e leia <a href=\"/blog/como-comecar-no-hyrox/\">Como começar no Hyrox</a>. Antes de viajar, confira data e horário da sua divisão no site oficial."),
            ("p", "Este texto é um resumo independente do que consta no site oficial do Hyrox e não tem vínculo com a organização."),
        ],
        "relacionados": ["hyrox", "athx"],
    },
}
