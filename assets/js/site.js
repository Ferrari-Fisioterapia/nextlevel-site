(function(){
  var reduz=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  // origem do visitante: instagram, google, direto etc. (primeiro contato da sessão)
  var og=(function(){
    try{var k=sessionStorage.getItem('og');if(k)return k}catch(_){}
    var q=new URLSearchParams(location.search),o=q.get('utm_source')||q.get('origem')||'';
    if(!o&&document.referrer){try{
      var r=new URL(document.referrer).hostname.replace(/^www\./,'');
      if(r&&r.indexOf('nextlevelfitness.com.br')<0)o=/google\./.test(r)?'google':/bing\./.test(r)?'bing':/instagram\./.test(r)?'instagram':/facebook\.|fb\./.test(r)?'facebook':/duckduckgo\./.test(r)?'duckduckgo':r;
    }catch(_){}}
    o=(o||'direto').toLowerCase().replace(/[^a-z0-9._-]/g,'').slice(0,30)||'direto';
    try{sessionStorage.setItem('og',o)}catch(_){}
    return o;
  })();
  // revelar ao rolar
  var els=document.querySelectorAll('.rv');
  if('IntersectionObserver' in window && !reduz){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px',threshold:.08});
    els.forEach(function(el,i){el.style.transitionDelay=((i%4)*70)+'ms';io.observe(el)});
  }else{els.forEach(function(el){el.classList.add('on')})}
  // cabeçalho compacto e parallax leve no vídeo
  var h=document.querySelector('.s-header'),v=document.querySelector('.h-hero .fundo');
  var tick=false;
  function f(){tick=false;var y=window.scrollY||0;if(h)h.classList.toggle('mini',y>40);if(v&&!reduz&&y<900)v.style.transform='translate3d(0,'+(y*.18)+'px,0) scale(1.08)'}
  window.addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(f)}},{passive:true});f();
  // vídeo: pausa quando fora da tela ou com movimento reduzido
  if(v&&v.tagName==='VIDEO'){
    if(reduz){v.removeAttribute('autoplay');v.pause()}
    else if('IntersectionObserver' in window){new IntersectionObserver(function(es){es.forEach(function(e){e.isIntersecting?v.play().catch(function(){}):v.pause()})}).observe(v)}
  }
  // fecha o menu ao navegar
  var mn=document.getElementById('mn');
  if(mn)document.querySelectorAll('.s-nav a').forEach(function(a){a.addEventListener('click',function(){mn.checked=false})});
  // Google Analytics 4: só liga quando o ID de medição (G-XXXXXXX) for preenchido
  var GA_ID='G-56KHSPJ3QG';
  if(GA_ID){
    var gs=document.createElement('script');gs.async=true;gs.src='https://www.googletagmanager.com/gtag/js?id='+GA_ID;document.head.appendChild(gs);
    window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};
    gtag('js',new Date());gtag('set','user_properties',{origem:og});gtag('config',GA_ID);
  }
  // clique no direct do Instagram (o direct não aceita texto preenchido, então a origem vai só para o Analytics)
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a[href*="ig.me"]');if(!a)return;
    try{if(window.gtag)window.gtag('event','direct_click',{pagina:location.pathname,origem:og})}catch(_){}
  },true);
})();
