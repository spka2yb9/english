"""第44回の描き直し: peace。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('peace', 'オリーブの枝をくわえて飛ぶ白いハトのイラスト。', f"""
<g transform="translate(270 210)">
  <ellipse rx="100" ry="60" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <circle cx="86" cy="-46" r="38" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <circle cx="100" cy="-54" r="5" class="ink"/>
  <path d="M120-40l34 8-34 14z" class="gold o"/>
  <path d="M-20-40q60-70 100-10-50 36-100 10z" fill="#eef4f8" stroke="{INK}" stroke-width="3"/>
  <path d="M-96 10l-90-40 20 46-30 34 92-14z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(410 200)">
  <path d="M0 0q60 20 96 60" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
  <g class="green o">
    <ellipse cx="34" cy="14" rx="22" ry="12" transform="rotate(28 34 14)"/>
    <ellipse cx="66" cy="36" rx="22" ry="12" transform="rotate(28 66 36)"/>
    <ellipse cx="94" cy="62" rx="22" ry="12" transform="rotate(28 94 62)"/>
  </g>
</g>
<path d="M120 340h360" class="a"/>
""", ground=True)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
