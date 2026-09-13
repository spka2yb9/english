"""第73回の描き直し: aspect（box の絶対座標）, bat（暗い背景で影が見えなかった）。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('aspect', '立方体のうち、一つの面だけを示したイラスト。', f"""
{box(290,240,200,150,44,'teal')}
<g transform="translate(290 240)"><path d="M-100-75h200v150h-200z" class="coral o" opacity=".9"/></g>
<path d="M500 300h-80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('bat', '夜空を飛ぶコウモリのイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#2b3a52"/>
<g fill="#f3e3ae"><path d="M490 90a56 56 0 1 0 0 84 44 44 0 1 1 0-84z"/></g>
<g fill="#8b98a6" stroke="#c9d3dc" stroke-width="3">
  <ellipse cx="300" cy="210" rx="34" ry="46"/>
  <path d="M272 186l-46-34-30-40-14 56-46 24 46 24 14 56 30-40 46-34z"/>
  <path d="M328 186l46-34 30-40 14 56 46 24-46 24-14 56-30-40-46-34z"/>
  <path d="M284 172l-12-32 28 16zM316 172l12-32-28 16z"/>
</g>
<g fill="#f3c94f"><circle cx="290" cy="196" r="5"/><circle cx="310" cy="196" r="5"/></g>
<g fill="#fdf6e0"><circle cx="110" cy="120" r="4"/><circle cx="180" cy="320" r="4"/><circle cx="520" cy="300" r="4"/></g>
""", ground=False)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
