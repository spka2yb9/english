"""第61回の描き直し: generic, gentleman。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('generic', '銘柄の印がある品と、印のないふつうの品を比べたイラスト。', f"""
{box(170,250,150,120,28,'teal')}
<g fill="#fffdf6">
  <path d="M160 240l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z"/>
</g>
<g transform="translate(430 250)">
  <path d="M-80-70h160v150h-160z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-50-30h100M-50 0h70"/></g>
</g>
<path d="M300 250h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M420 360l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('gentleman', '帽子を手に取って、ていねいに礼をする紳士のイラスト。', f"""
<g transform="translate(240 346) rotate(20)">{person(0,0,1.3,1,'blue','blue','carry','short','smile')}</g>
<g transform="translate(300 214) rotate(20)">
  <path d="M-50-6h100v14h-100z" class="ink"/>
  <path d="M-32-54h64v48h-64z" class="ink"/>
  <path d="M-32-20h64v10h-64z" class="coralp o"/>
</g>
{person(470,346,1.15,-1,'coral','gold','stand','bob','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M110 190l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
