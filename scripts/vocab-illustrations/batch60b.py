"""第60回の描き直し: film（person を translate 内で絶対座標指定していた）。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('film', 'カメラを回して人物の場面を撮るイラスト。', f"""
<g transform="translate(180 270)">
  <path d="M-80-50h160v100h-160z" fill="#2f4055"/>
  <path d="M80-20l60-36v92l-60-36z" fill="#2f4055"/>
  <circle cx="-30" cy="-70" r="26" fill="#41506a" stroke="{INK}" stroke-width="3"/>
  <circle cx="30" cy="-70" r="26" fill="#41506a" stroke="{INK}" stroke-width="3"/>
  <path d="M-40 50h80v50h-80z" fill="#41506a"/>
</g>
{person(450,346,1.15,-1,'coral','gold','up','bob','smile')}
<path d="M330 250h50" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:4"><path d="M120 160q-16-16 0-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
