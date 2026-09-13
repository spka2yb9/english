"""第48回の描き直し: secret, silly。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('secret', '口もとに手を当てて、小声でないしょを打ち明けるイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','reach','short','smile')}
{hand(258,236,1)}
{person(430,346,1.15,-1,'coral','gold','stand','bob','surprised')}
<g transform="translate(330 200)">
  <path d="M-60-40h120v70h-120z" fill="#fffdf6" class="o"/>
  <path d="M-34 30l-14 32 42-32z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{MUTED}"><circle cx="-26" cy="-6" r="8"/><circle cx="0" cy="-6" r="8"/><circle cx="26" cy="-6" r="8"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('silly', 'よそ見をして壁にぶつかる、間の抜けたイラスト。', f"""
<g transform="translate(470 250)"><path d="M-30-140h60v240h-60z" fill="#c9d3dc" class="o"/></g>
<g transform="translate(330 346)">{person(0,0,1.3,1,'gold','blue','walk','short','smile')}</g>
<g class="corals" style="stroke-width:5"><path d="M410 200l24-14M414 240h28"/></g>
<g transform="translate(200 160)">
  <path d="M-60-50h120v80h-120z" fill="#fffdf6" class="o"/>
  <path d="M20 30l14 32-42-32z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><path d="M-14-24q0-24 20-24t20 24q0 14-14 18v12h-12v-18q12-4 12-14t-8-8-8 10z"/><rect x="0" y="20" width="10" height="10"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
