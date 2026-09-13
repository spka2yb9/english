"""第9回の描き直し分。batch09.py のあとに実行する。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('slap', '開いた手のひらで、平たい面をぴしゃりと打つイラスト。', f"""
<circle cx="120" cy="100" r="56" class="coralp"/>
<g transform="translate(390 230)">
  <path d="M-30-130h140v260H-30z" class="goldp o"/>
  <path d="M-30-60h140M-30 10h140" fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"/>
</g>
{hand(280,230,1)}
<path d="M220 300h60" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:5">
  <path d="M350 160l-26-24M350 300l-26 24M336 230h-26"/>
</g>
""", ground=True, arrow=True)

add('split', '一本のまるたにくさびを打ち込んで、縦に二つへ割っているイラスト。', f"""
<circle cx="470" cy="100" r="54" class="goldp"/>
<g transform="translate(280 290)">
  <g transform="translate(-30 0)">
    <path d="M-160-50h130v100h-130z" class="goldp o"/>
    <ellipse cx="-160" cy="0" rx="18" ry="50" class="gold o"/>
    <path d="M-30-50v100" class="a"/>
  </g>
  <g transform="translate(30 0)">
    <path d="M30-50h130v100H30z" class="goldp o"/>
    <ellipse cx="160" cy="0" rx="18" ry="50" class="gold o"/>
    <path d="M30-50v100" class="a"/>
  </g>
</g>
<g transform="translate(280 196)">
  <path d="M-20-90h40v86l-20 30-20-30z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M150 350h-56"/><path d="M410 350h56"/></g>
""", ground=True, arrow=True)

add('tool', 'ハンマー・ドライバー・レンチなど、道具が並んだイラスト。', f"""
<g transform="translate(150 240) rotate(-10)">
  <path d="M-44-30h88v34h-88z" class="goldd o"/>
  <path d="M0 4v120" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"/>
</g>
<g transform="translate(300 250)">
  <path d="M-15-100h30v70h-30z" class="coral o"/>
  <path d="M-6-30h12v120h-12z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(450 250) rotate(12)">
  <path d="M-26-100q-16-26 4-38 20-12 40 0 20 12 6 38l-12 12h-26z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <circle cy="-120" r="13" fill="#fffaf1" stroke="{INK}" stroke-width="3"/>
  <path d="M-11-88h22v170h-22z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-22 70q22 14 44 0l-4 24h-36z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('bride', '白いドレスとブーケを持った花嫁のイラスト。', f"""
<circle cx="470" cy="100" r="56" class="coralp"/>
{person(280,350,1.25,1,'violet','violet','hold','bob','smile')}
<g transform="translate(280 322)">
  <path d="M-38-64q38-14 76 0l44 92h-164z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M-28-36q28 12 56 0" fill="none" stroke="{MUTED}" stroke-width="3"/>
</g>
<g transform="translate(280 240)">
  <path d="M-46-24q46-24 92 0l16 84q-62 26-124 0z" fill="#fffdf6" opacity=".45" stroke="{MUTED}" stroke-width="2"/>
</g>
<g transform="translate(372 306)">
  <g class="coral o"><circle cx="-14" cy="-10" r="14"/><circle cx="14" cy="-14" r="14"/><circle cx="0" cy="10" r="14"/></g>
  <path d="M0 22v28" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
</g>
<path d="M80 370h420" class="a"/>
""", ground=True)
print(' '.join(W)); print(sheet(W))
