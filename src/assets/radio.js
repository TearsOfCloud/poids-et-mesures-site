/* Radio P&M : lecteur calé sur l'heure de Paris.
   Tout l'audio est fabriqué à l'avance. La grille (grille.json) dit quel segment
   passe à quelle seconde ; ici on calcule seulement « où en est l'antenne ». */
(()=>{
const s=document.currentScript,root=s.src.replace(/assets\/radio\.js.*$/,'');
const $=q=>document.querySelector(q),$$=q=>[...document.querySelectorAll(q)];
const pad=n=>String(n).padStart(2,'0');
const FMT={
 journal:['Journal','p-journal','#FFD60A'],titres:['Titres','p-titres','#FFE878'],bases:['Les bases','p-bases','#9FC0DA'],
 anecdote:['Anecdote','p-anecdote','#F7A48F'],outil:['L\'outil testé','p-outil','#8FD9B6'],dossier:['Dossier','p-dossier','#F7F2E4'],musique:['Musique','p-musique','#C9C6BD']};
const esc=t=>String(t).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
let G=null,audio=null,playing=false,curIdx=-1;

/* secondes écoulées depuis minuit, heure de Paris */
function nowSec(){
 const p=new Intl.DateTimeFormat('fr-FR',{timeZone:'Europe/Paris',hour:'2-digit',minute:'2-digit',second:'2-digit',hour12:false}).formatToParts(new Date());
 const g=t=>+p.find(x=>x.type===t).value;
 return (g('hour')%24)*3600+g('minute')*60+g('second');
}
function locate(t){
 const pl=G.plan;let lo=0,hi=pl.length-1;
 while(lo<hi){const mid=(lo+hi+1)>>1;if(pl[mid][1]<=t)lo=mid;else hi=mid-1}
 return {i:lo,off:Math.max(0,t-pl[lo][1])};
}
const seg=i=>G.segments[G.plan[i%G.plan.length][0]];
const hm=sec=>{sec=Math.floor(sec)%86400;return pad(Math.floor(sec/3600))+':'+pad(Math.floor(sec%3600/60))};

/* lecture */
function load(i,off){
 const sg=seg(i);curIdx=i;
 audio.src=G.base+sg.fichier;
 audio.onloadedmetadata=()=>{try{audio.currentTime=Math.min(off,Math.max(0,audio.duration-1))}catch(_){}};
 return audio.play();
}
function syncAndPlay(){
 const {i,off}=locate(nowSec());
 return load(i,off);
}
function setUi(on){
 playing=on;document.body.classList.toggle('playing',on);
 $$('.dial .core').forEach(c=>c.textContent=on?'❚❚':'▶');
 const b=$('#mpp');if(b){b.textContent=on?'❚❚':'▶';b.setAttribute('aria-label',on?'Pause':'Lecture')}
 $$('.btn.y[data-play]').forEach(x=>x.textContent=on?'Pause':'Écouter en direct');
 if(on&&$('#mini'))$('#mini').classList.add('show');
}
function toggle(){
 if(playing){audio.pause();setUi(false);return}
 setUi(true);
 syncAndPlay().catch(()=>setUi(false));
}

/* affichage */
function render(){
 const t=nowSec(),{i,off}=locate(t),sg=seg(i),f=FMT[sg.format]||FMT.musique;
 const rest=Math.max(0,Math.round(sg.duree-off));
 $$('.nowTitle').forEach(e=>e.textContent=sg.titre);
 $$('.nowProg').forEach(e=>e.style.setProperty('--p',Math.min(100,off/sg.duree*100)+'%'));
 const pill=$('.nowPill');if(pill){pill.className='pill nowPill '+f[1];pill.textContent=f[0]}
 $$('.nowRest').forEach(e=>e.textContent=`Encore ${Math.floor(rest/60)} min ${pad(rest%60)}`);
 $$('.clockTxt').forEach(e=>e.textContent=hm(t));
 const nxt=[1,2,3].map(k=>{const sg2=seg(i+k),st=G.plan[(i+k)%G.plan.length][1],f2=FMT[sg2.format]||FMT.musique;
  return `<li><span class="mono">${hm(st)}</span><span class="pill ${f2[1]}">${f2[0]}</span><span>${esc(sg2.titre)}</span></li>`}).join('');
 ['#suivreHome','#suivreRadio'].forEach(q=>{const e=$(q);if(e)e.innerHTML=nxt});
 const mt=$('#mini .t strong');if(mt)mt.textContent=sg.titre;
 /* si l'antenne a changé de segment pendant la lecture (ou la mise en veille) : on se recale */
 if(playing&&audio&&i!==curIdx&&audio.ended!==false&&audio.readyState===0)syncAndPlay().catch(()=>{});
 const rows=$$('#grilleJour .slot');rows.forEach(r=>r.classList.toggle('now',+r.dataset.i===i));
}
function grille(){
 const box=$('#grilleJour');if(!box)return;
 const t=nowSec(),{i}=locate(t),out=[];
 for(let k=0;k<G.plan.length&&out.length<14;k++){
  const idx=(i+k)%G.plan.length,sg=seg(idx);
  if(sg.format==='musique')continue;
  const f=FMT[sg.format],st=G.plan[idx][1];
  out.push(`<div class="slot" style="--k:${f[2]}" data-k="${sg.format}" data-i="${idx}"><span class="mono">${hm(st)}</span><span class="pill ${f[1]}">${f[0]}</span><div><b>${esc(sg.titre)}</b>${sg.texte?`<button class="lire">Lire le texte</button><div class="script">${esc(sg.texte).replace(/\n\n/g,'<br><br>')}</div>`:''}${sg.demo?'<span class="mono c-gris" style="display:block;margin-top:4px">Segment de démonstration</span>':''}</div><span></span></div>`);
 }
 box.innerHTML=out.join('');
 const hdr=$('#grille h2');if(hdr)hdr.innerHTML='Au programme <em>maintenant</em>';
}

fetch(root+'assets/radio/grille.json').then(r=>r.json()).then(g=>{
 G=g;G.base=new URL(G.base,root+'assets/radio/').href;
 window.__radio=true;
 audio=new Audio();audio.preload='auto';window.__radioAudio=audio;
 audio.addEventListener('ended',()=>{if(playing)syncAndPlay().catch(()=>setUi(false))});
 audio.addEventListener('error',()=>{if(playing)setTimeout(()=>syncAndPlay().catch(()=>setUi(false)),2000)});
 /* nos clics passent avant ceux de la maquette */
 document.addEventListener('click',e=>{if(e.target.closest('[data-play]')){e.preventDefault();e.stopImmediatePropagation();toggle()}},true);
 const mp=$('#mpp');if(mp)mp.onclick=toggle;
 const mx=$('#mx');if(mx)mx.onclick=()=>{if(playing)toggle();$('#mini').classList.remove('show')};
 $$('.btn.y[data-play]').forEach(x=>x.textContent='Écouter en direct');
 const lab=$('.r-hero .mono');if(lab)lab.textContent='Webradio · en test';
 const dial=$('.r-now .head .mono');if(dial)dial.lastChild.textContent='À l\'antenne';
 const nm=$('.note-maq');if(nm)nm.textContent='Phase de test : trois segments seulement (journal, mot pesé, anecdote) tournent en boucle, avec une musique de démonstration. Tout ce qui est dit est déjà publié et sourcé sur le site. La voix et la musique sont générées par IA.';
 setUi(false);render();grille();setInterval(render,1000);
}).catch(()=>{});
})();
