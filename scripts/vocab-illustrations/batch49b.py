"""第49回の描き直し: skin。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('skin', '腕の表面をおおう肌を、虫めがねで見るイラスト。', f"""
<g transform="translate(280 260)">
  <path d="M-190-40q30-30 90-30h130q40 0 40 40t-40 40h-130q-60 0-90-30z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M70-70q60 0 60 40t-60 40" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-190-40q30-24 90-24" fill="none" stroke="#ffffff" opacity=".5" stroke-width="6"/>
</g>
<g transform="translate(360 160) rotate(24)">
  <circle r="66" fill="#fdece0" stroke="{INK}" stroke-width="8"/>
  <g fill="{SKINL}" opacity=".55"><circle cx="-24" cy="-14" r="6"/><circle cx="6" cy="10" r="6"/><circle cx="26" cy="-22" r="6"/><circle cx="-8" cy="-34" r="5"/><circle cx="34" cy="18" r="5"/></g>
  <path d="M0 66v70" fill="none" stroke="{INK}" stroke-width="16"/>
</g>
<path d="M160 340h-40" class="a" marker-end="url(#ar)" transform="rotate(180 140 340)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
