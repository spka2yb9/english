from lib import *
emit('bride', '白いドレスとブーケを持った花嫁のイラスト。ベールは後ろへ流している。', f"""
<circle cx="470" cy="100" r="56" class="coralp"/>
<g transform="translate(292 250)">
  <path d="M-56-16q56-30 112 0l20 96q-76 30-152 0z" fill="#f7f4ef" opacity=".9" stroke="{MUTED}" stroke-width="2"/>
</g>
{person(280,350,1.25,1,'violet','violet','hold','bob','smile')}
<g transform="translate(280 322)">
  <path d="M-38-64q38-14 76 0l44 92h-164z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M-28-36q28 12 56 0" fill="none" stroke="{MUTED}" stroke-width="3"/>
</g>
<g transform="translate(372 306)">
  <g class="coral o"><circle cx="-14" cy="-10" r="14"/><circle cx="14" cy="-14" r="14"/><circle cx="0" cy="10" r="14"/></g>
  <path d="M0 22v28" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
</g>
<path d="M80 370h420" class="a"/>
""", ground=True)
print(sheet(['bride']))
