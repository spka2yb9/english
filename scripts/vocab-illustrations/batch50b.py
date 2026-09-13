"""第50回の描き直し: suitable, swallow。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('suitable', '穴の形にぴたりと合う積み木を入れるイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-230-50h460v100h-460z" fill="#dfe6ea" class="o"/>
  <path d="M-160-50h110v100h-110z" fill="#fffaf1"/>
  <path d="M-160-50h110v100h-110z" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M60-50h110v100H60z" fill="#fffaf1"/>
  <path d="M60-50h110v100H60z" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(140 160)"><path d="M-55-50h110v100h-110z" class="teal o"/></g>
<path d="M140 220v40" class="a" marker-end="url(#ar)"/>
<g transform="translate(415 300)"><path d="M-55-50h110v100h-110z" class="teal o"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M400 180l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('swallow', '口に入れたものが、のどを通って下へ落ちるイラスト。', f"""
<g transform="translate(280 200)">
  <path d="M-40-120q80-20 110 40 20 40-10 80t-40 60l-20 100h-60V60q-40-20-40-70 0-90 100-110z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="30" cy="-40" r="5" class="ink"/>
  <path d="M50 10q-30 20-56 6" fill="none" stroke="{SKINL}" stroke-width="4"/>
</g>
<g fill="none" stroke="{SKINL}" stroke-width="4" stroke-dasharray="9 8"><path d="M270 220v130"/></g>
<circle cx="270" cy="250" r="20" class="coral o"/>
<path d="M370 200v140" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
