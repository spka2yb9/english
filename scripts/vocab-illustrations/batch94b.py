"""第94回の描き直し: thumb。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('thumb', '手の親指を立てたイラスト。', f"""
<g transform="translate(310 250)">
  <rect x="-90" y="-30" width="180" height="120" rx="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <g fill="none" stroke="{SKINL}" stroke-width="2.5"><path d="M-30 -30v120M20-30v120M62-30v120"/></g>
  <g transform="rotate(-10 -60 -20)">
    <rect x="-92" y="-140" width="60" height="130" rx="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="10 8"><ellipse cx="238" cy="150" rx="46" ry="72" transform="rotate(-10 238 150)"/></g>
<path d="M470 150H300" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

print(len(W), ' '.join(W))
print(sheet(W, '/tmp/vocab-sheet2.html'))
