"""第62回の描き直し: killing（flame の絶対座標ミス）。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('killing', 'ともっていた灯が消されて、命が絶たれることを示すイラスト。', f"""
{flame(180,220,1.3)}
<g transform="translate(180 330)"><path d="M-30-40h60l-8 60h-44z" fill="#f7e6bd" stroke="{INK}" stroke-width="3"/></g>
<g transform="translate(430 300)">
  <path d="M-30-10h60l-8 60h-44z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <g class="muted"><path d="M0-30q20-40 0-70"/></g>
</g>
<path d="M280 250h60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"><path d="M400 160l34 34M434 160l-34 34"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
