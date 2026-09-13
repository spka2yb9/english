"""第51回の描き直し: trigger。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('trigger', 'ボタンを押したとたん、動きが始まるイラスト。', f"""
<g transform="translate(190 270)">
  <path d="M-90 60h180v-40h-180z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <ellipse cy="20" rx="70" ry="26" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <ellipse cy="-4" rx="56" ry="22" class="coral o"/>
</g>
{hand(190,150,1)}
<path d="M190 195v40" class="a" marker-end="url(#ar)"/>
<g transform="translate(450 230)">
  <path d="M0-90l26 62 68 6-50 46 14 68-58-34-58 34 14-68-50-46 68-6z" class="coralp o"/>
  <g class="corals" style="stroke-width:5"><path d="M-110-100l-24-20M110-100l24-20"/></g>
</g>
<path d="M300 230h50" class="a" marker-end="url(#ar)"/>
<path d="M60 336h480" class="a"/>
""", ground=True, arrow=True)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
