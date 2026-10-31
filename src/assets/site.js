(()=>{
const $=s=>document.querySelector(s)||document.createElement('div'),$$=s=>[...document.querySelectorAll(s)];
const pad=n=>String(n).padStart(2,'0');

/* pièces déchirées : bords irréguliers générés une fois */
function rnd(seed){return()=>{seed=(seed*16807)%2147483647;return seed/2147483647}}
$$('.torn').forEach((el,k)=>{
 const r=rnd(k*97+13),n=18,a=1.8,pts=[];
 for(let i=0;i<=n;i++)pts.push(`${(i*100/n).toFixed(1)}% ${(r()*a).toFixed(2)}%`);
 for(let i=n;i>=0;i--)pts.push(`${(i*100/n).toFixed(1)}% ${(100-r()*a).toFixed(2)}%`);
 el.style.setProperty('--clip',`polygon(${pts.join(',')})`);
});

/* apparitions + surligneur + jauge */
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}}),{threshold:.15});
const observe=()=>$$('.pose:not(.on),mark:not(.on),#gauge:not(.on)').forEach(el=>io.observe(el));

/* page courante : repère dans le menu */
const cur=document.body.dataset.page;
$$('nav.main a').forEach(a=>a.dataset.route===cur?a.setAttribute('aria-current','page'):a.removeAttribute('aria-current'));
// ancres internes (sommaire, grille) sans casser la navigation
document.addEventListener('click',e=>{const a=e.target.closest('a[href^="#"]:not([href^="#/"])');if(a&&a.getAttribute('href').length>1){const t=document.getElementById(a.getAttribute('href').slice(1));if(t){e.preventDefault();t.scrollIntoView({behavior:'smooth'})}}});

/* la règle défile avec la page, l'indicateur suit la lecture, l'en-tête se range */
let lastY=0,ticking=false;
function onScroll(){
 const y=scrollY,max=document.documentElement.scrollHeight-innerHeight,root=document.documentElement.style;
 root.setProperty('--shift',((y*.4)%60).toFixed(1));
 root.setProperty('--prog',max>0?Math.min(1,y/max).toFixed(3):0);
 const top=$('#top');
 if(y>lastY+6&&y>180)top.classList.add('hide');else if(y<lastY-6||y<180)top.classList.remove('hide');
 lastY=y;ticking=false;
 const secs=['s1','s2','s3','s4','s5','s6'].map(i=>document.getElementById(i));
 if(!$('#v-article').classList.contains('on'))return;
 let cur=secs[0];secs.forEach(s=>{if(s.getBoundingClientRect().top<220)cur=s});
 $$('#toc a').forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+cur.id));
}
addEventListener('scroll',()=>{if(!ticking){requestAnimationFrame(onScroll);ticking=true}},{passive:true});

/* brèves : rendues au build, ici seulement le filtre */
$$('[data-f]').forEach(c=>c.onclick=()=>{
 $$('[data-f]').forEach(x=>x.setAttribute('aria-pressed',x===c));
 $$('.breve').forEach(b=>b.hidden=!(c.dataset.f==='tout'||b.dataset.cat===c.dataset.f));
});

const R={bases:['Les bases'],anecdote:['Anecdote'],benchmark:['Benchmark'],actu:["L'actu pesée"],outil:['Outil testé']};
$('#aChips').innerHTML=`<button class="chip" aria-pressed="true" data-r="tout">Tout</button>`+Object.entries(R).filter(([k])=>$$('#gridArt .card[data-r="'+k+'"]').length).map(([k,v])=>`<button class="chip" aria-pressed="false" data-r="${k}">${v[0]}</button>`).join('');
let rub='tout';
const qr=(location.search.match(/[?&]r=(\w+)/)||[])[1];
function filt(){
 const q=$('#q').value.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').trim(),v=$('#onlyVid').checked;let n=0;
 $$('#gridArt .card').forEach(c=>{const ok=(rub==='tout'||c.dataset.r===rub)&&(!v||c.dataset.v==='1')&&(!q||q.split(/\s+/).every(w=>c.dataset.q.includes(w)));c.hidden=!ok;n+=ok});
 $('#empty').hidden=n>0;
}
function setRub(r){rub=r;$$('#aChips .chip').forEach(x=>x.setAttribute('aria-pressed',x.dataset.r===r));filt()}
$$('#aChips .chip').forEach(c=>c.onclick=()=>setRub(c.dataset.r));
if(qr)setRub(qr);
$('#q').oninput=filt;$('#onlyVid').onchange=filt;

/* radio : formats, heure type, grille */
const F={
 journal:{n:'Journal',c:'#FFD60A',p:'p-journal',d:'Chaque heure pile, 4 minutes : les faits du jour, avec leurs sources.',w:'Toutes les heures à :00'},
 titres:{n:'Titres',c:'#FFE878',p:'p-titres',d:'Moins d\'une minute pour faire le point.',w:':20 et :40'},
 bases:{n:'Les bases',c:'#9FC0DA',p:'p-bases',d:'Un mot ou un mécanisme de l\'IA expliqué simplement, en 2 minutes.',w:'Plusieurs fois par heure'},
 anecdote:{n:'Anecdote',c:'#F7A48F',p:'p-anecdote',d:'Une histoire vraie de la tech, et ce qu\'elle nous apprend.',w:'1 fois par heure'},
 outil:{n:'L\'outil testé',c:'#8FD9B6',p:'p-outil',d:'Un outil essayé pour de vrai : à quoi il sert, ses limites, comment l\'essayer.',w:'1 fois par heure'},
 dossier:{n:'Dossier',c:'#F7F2E4',p:'p-dossier',d:'5 à 8 minutes tirées d\'un article de fond du site.',w:'2 fois par heure'},
 musique:{n:'Musique',c:'#C9C6BD',p:'p-musique',d:'Musique générée par IA, entre les segments.',w:'Entre les segments'},
};
// déroulé type d'une heure : minute de début, durée, format, titre
const H=[[0,4,'journal','Le journal'],[4,2,'musique','Musique'],[6,2,'bases','Le mot pesé : hallucination'],[8,7,'dossier','Dossier : quand le robot engage l\'entreprise'],[15,3,'musique','Musique'],[18,2,'outil','L\'outil testé'],[20,1,'titres','Les titres'],[21,3,'anecdote','Anecdote : le chatbot d\'Air Canada'],[24,4,'musique','Musique'],[28,2,'bases','Les bases : un mot expliqué'],[30,8,'dossier','Dossier : un article du site'],[38,2,'musique','Musique'],[40,1,'titres','Les titres'],[41,3,'outil','L\'outil testé'],[44,4,'musique','Musique'],[48,3,'anecdote','Anecdote'],[51,5,'bases','Les bases'],[56,4,'musique','Musique']];
$('#heureBar').innerHTML=H.map(s=>`<span style="flex:${s[1]};background:${F[s[2]].c};${s[2]==='dossier'?'box-shadow:inset 0 0 0 2px #121316':''}" title=":${pad(s[0])} · ${F[s[2]].n}" data-m="${s[0]}"></span>`).join('');
$('#legend').innerHTML=Object.values(F).map(f=>`<span class="pill ${f.p}">${f.n}</span>`).join('');
$('#formats').innerHTML=['journal','bases','anecdote','outil','dossier','musique'].map((k,i)=>{const f=F[k];return `<div class="piece fmt pose" style="--k:${f.c};--r:${i%2?1:-1}deg"><span class="pill ${f.p}">${f.n}</span><h3>${f.n}</h3><p>${f.d}</p><div class="when mono">${f.w}</div></div>`}).join('');
const per=[['Le matin',6,10],['La journée',10,14],['L\'après-midi',14,19],['Le soir',19,24]];
const rdv=[[0,'journal'],[8,'dossier'],[21,'anecdote'],[30,'dossier'],[41,'outil'],[51,'bases']];
const hNow=new Date().getHours();
const pNow=Math.max(0,per.findIndex(p=>hNow>=p[1]&&hNow<p[2]));
let gh=`<div class="periodes" role="tablist">${per.map((p,i)=>`<button role="tab" data-per="${i}" aria-selected="${i===pNow}">${p[0]} · ${p[1]} h-${p[2]%24} h</button>`).join('')}</div>`;
per.forEach((p,pi)=>{gh+=`<div class="bloc" data-bloc="${pi}" ${pi===pNow?'':'hidden'}>`;
 for(let h=p[1];h<p[2];h++)rdv.forEach(([m,k])=>{const s=H.find(x=>x[0]===m);
  gh+=`<div class="slot" style="--k:${F[k].c}" data-k="${k}" data-t="${h*60+m}"><span class="mono">${pad(h)}:${pad(m)}</span><span class="pill ${F[k].p}">${F[k].n}</span><div><b>${k==='journal'?'Le journal de '+h+' h':s[3]}</b><button class="lire">Lire le texte</button><div class="script">Le texte du segment s'affichera ici dès que les premiers sons seront en ligne : pour lire au lieu d'écouter, et vérifier chaque phrase contre sa source.</div></div><button class="mini" data-play aria-label="Écouter ce segment">▶</button></div>`});gh+='</div>'});
$('#grilleJour').innerHTML=gh;
$('#gChips').innerHTML=`<button class="chip" aria-pressed="true" data-g="tout">Tout</button>`+['journal','bases','anecdote','outil','dossier'].map(k=>`<button class="chip" aria-pressed="false" data-g="${k}">${F[k].n}</button>`).join('');
$$('[data-g]').forEach(c=>c.onclick=()=>{$$('[data-g]').forEach(x=>x.setAttribute('aria-pressed',x===c));$$('#grilleJour .slot').forEach(s=>s.hidden=!(c.dataset.g==='tout'||s.dataset.k===c.dataset.g))});
$('#grilleJour').addEventListener('click',e=>{const t=e.target.closest('[data-per]');if(t){$$('[data-per]').forEach(x=>x.setAttribute('aria-selected',x===t));$$('.bloc').forEach(b=>b.hidden=b.dataset.bloc!==t.dataset.per);return}const b=e.target.closest('.lire');if(b){const s=b.closest('.slot');s.classList.toggle('open');b.textContent=s.classList.contains('open')?'Masquer le texte':'Lire le texte'}});

/* horloge + segment en cours, calculés sur l'heure réelle */
function tick(){
 const d=new Date(),h=d.getHours(),m=d.getMinutes(),sec=d.getSeconds();
 $('#clock').textContent=`${pad(h)}:${pad(m)}:${pad(sec)}`;
 const i=H.findIndex((s,j)=>m>=s[0]&&(j===H.length-1||m<H[j+1][0]));
 const s=H[i],el=(m-s[0])*60+sec,dur=s[1]*60,f=F[s[2]];
 const title=s[2]==='journal'?`Le journal de ${h} h`:s[3];
 $$('.nowTitle').forEach(e=>e.textContent=title);
 $$('.nowProg').forEach(e=>e.style.setProperty('--p',Math.min(100,el/dur*100)+'%'));
 $$('.clockTxt').forEach(e=>e.textContent=`${pad(h)}:${pad(m)}`);
 const pill=$('.nowPill');pill.className='pill nowPill '+f.p;pill.textContent=f.n;
 const rest=Math.max(0,dur-el);$('.nowRest').textContent=`Encore ${Math.floor(rest/60)} min ${pad(rest%60)}`;
 const li=[1,2,3].map(k=>{const n=H[(i+k)%H.length],hh=(i+k>=H.length)?(h+1)%24:h;return `<li><span class="mono">${pad(hh)}:${pad(n[0])}</span><span class="pill ${F[n[2]].p}">${F[n[2]].n}</span><span>${n[2]==='journal'?'Le journal de '+hh+' h':n[3]}</span></li>`}).join('');
 $('#suivreHome').innerHTML=li;$('#suivreRadio').innerHTML=li;
 $$('#heureBar span').forEach(b=>b.classList.toggle('now',+b.dataset.m===s[0]));
 const t=h*60+m;let best=null;
 $$('#grilleJour .slot').forEach(x=>{x.classList.remove('now');if(+x.dataset.t<=t)best=x});
 if(best)best.classList.add('now');
}
tick();setInterval(tick,1000);

/* écoute : pas encore de son, le lecteur le dit franchement */
document.addEventListener('click',e=>{if(e.target.closest('[data-play]')){e.preventDefault();$('#mini').classList.add('show')}});
$('#mx').onclick=()=>$('#mini').classList.remove('show');

$('#copy').onclick=e=>{try{navigator.clipboard.writeText(location.href)}catch(_){}e.target.textContent='Lien copié ✓';setTimeout(()=>e.target.textContent='Copier le lien',1800)};
$$('.terme').forEach(t=>t.onclick=()=>t.classList.toggle('open'));
$('#today').textContent=new Date().toLocaleDateString('fr-FR',{weekday:'long',day:'numeric',month:'long',year:'numeric'});

onScroll();observe();
})();
