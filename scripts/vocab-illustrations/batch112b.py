"""第112回の描き直し: disability。"""
from lib import *
W=[]
def add(slug,a,b,**k): W.append(emit(slug,a,b,**k))

add('disability', '車いすを使う人を示す記号のイラスト。', f"""
<g transform="translate(300 240)">
  <circle cx="-30" cy="-110" r="30" fill="{TONES['blue'][0]}"/>
  <path d="M-30-70v70h80" fill="none" stroke="{TONES['blue'][0]}" stroke-width="24" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M50 0l16 60" fill="none" stroke="{TONES['blue'][0]}" stroke-width="24" stroke-linecap="round"/>
  <circle cx="-6" cy="40" r="86" fill="none" stroke="{TONES['blue'][0]}" stroke-width="16"/>
  <path d="M-6 40h60" fill="none" stroke="{TONES['blue'][0]}" stroke-width="10"/>
  <path d="M30 100h50" fill="none" stroke="{TONES['blue'][0]}" stroke-width="20" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W, '/tmp/vocab-sheet2.html'))
