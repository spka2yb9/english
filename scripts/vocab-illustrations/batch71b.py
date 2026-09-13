"""第71回の描き直し: worth（天びんと品の配置を整えた）。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('worth', '品と代金が天びんで釣り合うイラスト。', f"""
<g transform="translate(300 150)">
  <path d="M-8-50h16v70h-16z" class="ink"/>
  <path d="M-180 20h360" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-180 20v50M180 20v50" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-240 70h120v10h-120zM120 70h120v10h-120z" class="ink"/>
</g>
{box(180,190,120,80,24,'teal')}
<g transform="translate(420 200)">
  <circle r="26" class="goldd o"/><circle cx="-30" cy="14" r="26" class="goldd o"/><circle cx="30" cy="14" r="26" class="goldd o"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M280 330h40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
