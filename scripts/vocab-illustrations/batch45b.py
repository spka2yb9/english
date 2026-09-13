"""第45回の描き直し: pilot, plead, polite, praise, precede, pregnant。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('pilot', '操縦席で計器をにぎり、飛行機を飛ばすパイロットのイラスト。', f"""
{plane(470,90,0.8,-8)}
<g transform="translate(240 260)">
  <path d="M-160-110h320v200h-320z" fill="#dfe6ea" class="o"/>
  <path d="M-130-80h300v90h-300z" fill="#cfe6f5" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><path d="M-130-20h300"/></g>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="3"><circle cx="60" cy="46" r="20"/><circle cx="120" cy="46" r="20"/></g>
  <g fill="none" stroke="{INK}" stroke-width="8"><path d="M-70 90v-40"/><path d="M-100 44h60"/></g>
</g>
{person(170,330,0.95,1,'blue','blue','reach','cap','smile')}
<path d="M60 350h480" class="a"/>
""", ground=True)

add('plead', '両手を合わせて、どうかとすがるように願うイラスト。', f"""
{person(220,346,1.25,1,'coral','blue','up','bob','sad')}
<g transform="translate(220 196)">
  <path d="M-22 30q-4-40 22-52 26 12 22 52z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M0-22v52" fill="none" stroke="{SKINL}" stroke-width="2"/>
</g>
{drop(290,250,0.8)}
{person(470,346,1.05,-1,'blue','blue','stand','short','neutral')}
<path d="M320 300h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('polite', '相手に向かって、ていねいに頭を下げるイラスト。', f"""
<g transform="translate(230 346) rotate(24)">{person(0,0,1.25,1,'blue','blue','stand','short','smile')}</g>
{person(470,346,1.15,-1,'coral','gold','stand','bob','smile')}
<path d="M300 250h70" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M110 180l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('praise', 'よくやったと星をつけて、ほめてもらうイラスト。', f"""
{person(210,346,1.3,1,'coral','blue','stand','bob','smile')}
<g transform="translate(210 140)"><path d="M0-40l14 28 30 4-22 21 6 30-28-15-28 15 6-30-22-21 30-4z" class="gold o"/></g>
{person(440,346,1.15,-1,'teal','gold','up','short','smile')}
<g class="golds" style="stroke-width:5"><path d="M370 200l-26-16M376 236h-30M368 270l-24 14"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('precede', '二両のうち前を走る車両を示したイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-250 40h500" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="20 14"/>
  <g class="tealp o"><rect x="-230" y="-70" width="180" height="100"/></g>
  <g class="coral o"><rect x="20" y="-80" width="200" height="110"/></g>
  <g fill="#e8f4fb" stroke="{INK}" stroke-width="3"><rect x="-200" y="-50" width="50" height="40"/><rect x="60" y="-56" width="50" height="40"/></g>
</g>
<path d="M540 220h30" class="a" marker-end="url(#ar)"/>
<circle cx="420" cy="235" r="70" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 330h480" class="a"/>
""", ground=True, arrow=True)

add('pregnant', 'おなかがふくらんだ人が、おなかに手をそえるイラスト。', f"""
<g transform="translate(300 340)">
  <path d="M-34-118q40-18 74 0l6 44q26 26 24 54-2 34-40 40h-70z" class="coral o"/>
  <ellipse cx="40" cy="-24" rx="44" ry="40" class="coral o"/>
  <path d="M44-52q34 10 34 40" fill="none" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
  <path d="M-34-92q-32 22-18 62" fill="none" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
  <circle cy="-150" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-32-160q4-34 32-34t32 34q-30-16-64 0z" fill="{HAIR}"/>
  <circle cx="-10" cy="-152" r="3.5" class="ink"/><circle cx="12" cy="-152" r="3.5" class="ink"/>
  <path d="M-6-138q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-16 18l-8 42M14 18l8 42" fill="none" stroke="{TONES['blue'][0]}" stroke-width="14" stroke-linecap="round"/>
</g>
<circle cx="340" cy="316" r="58" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 400h480" class="a"/>
""", ground=True)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
