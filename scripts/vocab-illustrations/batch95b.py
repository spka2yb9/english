"""第95回の描き直し: violence。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'

add('violence', '力にまかせて傷つける暴力のイラスト。', f"""
<g transform="translate(250 240)">
  <path d="M-200-34h130v68h-130z" class="teal o"/>
  <path d="M-80-40h40v80h-40z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <rect x="-46" y="-56" width="130" height="112" rx="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <g fill="none" stroke="{SKINL}" stroke-width="2.5"><path d="M-4-56v112M36-56v112M68-50v100"/></g>
  <path d="M-40-56q-20-30 6-44 22-12 34 12l6 28z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round">
  <path d="M370 180l46-34M382 240h56M370 300l46 34"/>
</g>
{xx(500,240,1.3)}
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W, '/tmp/vocab-sheet2.html'))
