"""第42回の描き直し: literally, lonely, loose, lower, manager, manipulate。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('literally', '紙に書かれた矢印の道を、そのまま歩いている人のイラスト。', f"""
<g transform="translate(160 200)">
  <path d="M-90-80h180v160h-180z" class="paper"/>
  <path d="M-60 40l0-60h100" fill="none" stroke="{INK}" stroke-width="8"/>
  <path d="M20-20l30 0M40-32l14 12-14 12" fill="none" stroke="{INK}" stroke-width="8"/>
</g>
<path d="M310 300h60V210h110" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" marker-end="url(#ar)"/>
{person(300,346,0.95,1,'teal','blue','walk','short','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M480 320l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('lonely', '遠くの集まりから離れて、一人きりで立っているイラスト。', f"""
<g opacity=".35">{person(470,330,0.7,-1,'coral','gold','stand','bob','smile')}{person(520,330,0.7,-1,'gold','blue','stand','short','smile')}</g>
{person(170,346,1.2,1,'violet','blue','stand','short','sad')}
<path d="M250 300h150" class="muted"/>
{drop(206,246,0.8)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('loose', 'ねじがゆるんで、板とのあいだにすきまができたイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-200-30h400v70h-400z" class="goldp o"/>
  <g transform="translate(-100 -30)">
    <circle r="20" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
    <path d="M-10 0h20" fill="none" stroke="{INK}" stroke-width="4"/>
  </g>
  <g transform="translate(110 -80) rotate(14)">
    <circle r="20" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
    <path d="M-10 0h20" fill="none" stroke="{INK}" stroke-width="4"/>
    <path d="M-6 20h12v34h-12z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  </g>
  <g class="corals" style="stroke-width:4"><path d="M150-70q22 10 22 30M150-96q40 16 40 56"/></g>
</g>
<path d="M370 200v-40" class="a" marker-end="url(#ar)"/>
<path d="M60 350h480" class="a"/>
""", ground=True, arrow=True)

add('lower', '高い位置にあった箱を、下へ下げるイラスト。', f"""
<g transform="translate(200 150)" opacity=".4"><path d="M-60-30h120v60h-120z" class="tealp o"/></g>
<g transform="translate(200 300)"><path d="M-60-30h120v60h-120z" class="teal o"/></g>
<path d="M200 190v70" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M280 150h180M280 300h180"/></g>
<path d="M420 160v120" class="a" marker-end="url(#ar)"/>
<path d="M60 350h480" class="a"/>
""", ground=True, arrow=True)

add('manager', '書類を手にして、働く人たちに指示を出す責任者のイラスト。', f"""
{person(160,346,1.25,1,'blue','blue','point','short','neutral')}
<g transform="translate(112 268) rotate(-12)">
  <path d="M-30-40h60v80h-60z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-18-20h36M-18 0h36M-18 20h24"/></g>
</g>
<g opacity=".85">{person(400,346,0.95,-1,'gold','blue','carry','cap','neutral')}{person(500,346,0.95,-1,'teal','gold','reach','bob','neutral')}</g>
<path d="M250 210h80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('manipulate', '糸を引いて、人形を思いどおりに動かしているイラスト。', f"""
{hand(300,110,1)}
<g fill="none" stroke="{INK}" stroke-width="3"><path d="M266 150l-24 80M334 150l24 80M300 150v58"/></g>
<g transform="translate(300 330)">
  <path d="M-32-70q32-14 64 0l-8 70h-48z" class="violet o"/>
  <path d="M-28-58l-30 22M28-58l30 22" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <path d="M-14 0l-14 40M14 0l14 40" fill="none" stroke="{TONES['violet'][2]}" stroke-width="12" stroke-linecap="round"/>
  <circle cx="0" cy="-98" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<path d="M400 130q40 20 40 60" class="a" marker-end="url(#ar)"/>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
