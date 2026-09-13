"""第55回の描き直し: cause（flame を translate 内で絶対座標指定していた）。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('cause', '火が原因となって、けむりと崩れという結果を生むイラスト。', f"""
{flame(170,250,1.4)}
<g transform="translate(450 260)">
  <g class="muted" opacity=".9"><path d="M-30-60q30-40 0-70M30-40q30-40 0-70"/></g>
  <path d="M-90 60h180v-50h-180z" fill="#b6bfc9" stroke="{INK}" stroke-width="3"/>
  <path d="M-60-20l40-40 30 40z" fill="#b6bfc9" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M250 240h100" class="a" marker-end="url(#ar)"/>
<path d="M60 326h480" class="a"/>
""", ground=True, arrow=True)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
