"""第47回の描き直し: relaxing, rescue, reserve, rude。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('relaxing', '木かげのいすで、お茶を手にくつろげる場のイラスト。', f"""
{sun(510,90,28)}
{tree(140,320,1.3)}
<g transform="translate(360 320)">
  <path d="M-90-30h180v26h-180z" class="goldd o"/>
  <path d="M-90-30h26v-90h-26z" class="goldd o"/>
  <path d="M-70-4h14v44h-14zM56-4h14v44H56z" class="goldd o"/>
</g>
<g transform="translate(390 250) scale(0.95)">{person(0,60,1.0,1,'teal','gold','stand','bob','smile')}</g>
<g transform="translate(300 240)">
  <path d="M-22-14h44v28h-44z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M22-8q16 0 16 12t-16 8" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
<g class="muted"><path d="M296 200q16-16 0-30M312 196q16-16 0-30"/></g>
<path d="M60 350h480" class="a"/>
""", ground=True)

add('rescue', '溺れている人に浮き輪を投げて助け出すイラスト。', f"""
<path d="M0 280h600v120H0z" class="bluep"/>
<g fill="none" stroke="#fffdf6" stroke-width="5" opacity=".8"><path d="M20 300q40-20 80 0t80 0t80 0t80 0t80 0t80 0"/></g>
<g transform="translate(450 270)">
  <circle cy="-6" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-30-16q-14-40 10-46M30-16q14-40-10-46" fill="none" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
  <path d="M-40 20q40-20 80 0" fill="none" stroke="#fffdf6" stroke-width="6"/>
</g>
{person(150,280,1.15,1,'coral','blue','up','short','neutral')}
<g transform="translate(330 200)">
  <circle r="44" fill="none" stroke="{TONES['coral'][0]}" stroke-width="18"/>
  <circle r="44" fill="none" stroke="#fffdf6" stroke-width="6" stroke-dasharray="24 24"/>
</g>
<path d="M200 200q60-40 90-20" fill="none" stroke="{MUTED}" stroke-width="3"/>
<path d="M380 210h40" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('reserve', '一つの席を取っておいて、予約の札を立てるイラスト。', f"""
<g transform="translate(300 310)">
  <g class="goldd o"><rect x="-250" y="-20" width="130" height="20"/><rect x="-70" y="-20" width="130" height="20"/><rect x="110" y="-20" width="130" height="20"/></g>
  <g class="goldd o"><rect x="-250" y="-90" width="20" height="70"/><rect x="-70" y="-90" width="20" height="70"/><rect x="110" y="-90" width="20" height="70"/></g>
</g>
{person(120,300,0.8,1,'teal','blue','stand','short','smile')}
{person(480,300,0.8,1,'coral','gold','stand','bob','smile')}
<g transform="translate(300 240)">
  <path d="M-6 30h12v-40h-12z" class="ink"/>
  <path d="M-60-40h120v40h-120z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-40" y="-28" width="80" height="10"/><rect x="-40" y="-12" width="50" height="8"/></g>
</g>
<circle cx="300" cy="280" r="76" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('rude', '相手に指を突きつけて、ぶしつけにふるまうイラスト。', f"""
{person(230,346,1.2,1,'coral','gold','point','bob','flat')}
{person(400,346,1.2,1,'teal','blue','stand','short','sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"><path d="M490 170l44 44M534 170l-44 44"/></g>
<path d="M320 220h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
