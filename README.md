# Site da Next Level Fitness

Site estático pronto para subir num repositório novo e ligar à Vercel. Gerado por `python3 tools/gerar.py`.
Páginas: home e /membro-fundador/ (lista de interesse, sem prometer vagas). Estilo no design system da Next Level (css/site.css).

## Como publicar
1. Crie um repositório vazio no GitHub (ex.: `nextlevel-site`) e libere o app do Claude nele.
2. Copie o conteúdo desta pasta para a raiz do repositório e faça o commit.
3. Na Vercel, importe o repositório (sem build) e adicione o domínio `nextlevelfitness.com.br` (e `www`).
4. Confirme se o site atual do domínio tem páginas que precisam continuar existindo (ex.: /membro-fundador, que já está na bio do Instagram: esta versão mantém esse endereço).

## Antes de publicar, o Ed confirma
- Endereço principal com ou sem www (o código usa www).
- Texto "Quem está por trás" e os 4 pilares.
- Contato: usa o direct do Instagram (ig.me). Se preferir WhatsApp, trocar `DM` em tools/gerar.py.
