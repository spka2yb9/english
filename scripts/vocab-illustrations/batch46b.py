"""第46回の描き直し: railway。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('railway', '遠くまで延びる二本のレールと枕木のイラスト。', f"""
<g fill="#b09274" stroke="{INK}" stroke-width="2">
  {''.join(f'<rect x="{300-(150-i*12)}" y="{376-i*30}" width="{2*(150-i*12)}" height="{16-i}"/>' for i in range(9))}
</g>
<path d="M110 392L262 130M490 392L338 130" fill="none" stroke="#8b98a6" stroke-width="14" stroke-linecap="round"/>
<path d="M140 392L272 130M460 392L328 130" fill="none" stroke="#c9d3dc" stroke-width="4"/>
<g class="green o" opacity=".8"><path d="M0 400q80-40 160-30v30zM600 400q-80-40-160-30v30z"/></g>
""", ground=False)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
