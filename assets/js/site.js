(function(){
  var reduz=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
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
})();
