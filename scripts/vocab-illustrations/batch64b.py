"""第64回の描き直し: muscle, ours。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('muscle', '腕を曲げて力こぶが盛り上がるイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-140 60h80v-50h-80z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-60 60L60 60" fill="none" stroke="{SKIN}" stroke-width="56" stroke-linecap="round"/>
  <path d="M60 60L20-80" fill="none" stroke="{SKIN}" stroke-width="50" stroke-linecap="round"/>
  <circle cx="8" cy="-110" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <ellipse cx="-10" cy="14" rx="52" ry="38" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <g fill="none" stroke="{SKINL}" stroke-width="3"><path d="M-40 6q40-24 66 8"/></g>
</g>
<g class="corals" style="stroke-width:5"><path d="M240 200l-24-18M250 240h-28"/></g>
<circle cx="290" cy="274" r="66" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('ours', '私たちのものだと、二人と品をひと囲いにするイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','point','short','smile')}
{person(310,346,1.15,1,'coral','gold','point','bob','smile')}
{box(450,270,120,100,0,'gold')}
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="110" y="160" width="420" height="200" rx="18"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
