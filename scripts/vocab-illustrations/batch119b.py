# -*- coding: utf-8 -*-
"""第119回の描き直し。sap（板に見えた）、oak（どんぐりが小さすぎ）、bud（つぼみが小さすぎ）。"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))
GR='#dfe8d8'; BRN='#8b6437'
def land(y=300, fill=GR):
    return f'<path d="M0 {y}h600v{400-y}H0z" fill="{fill}"/><path d="M0 {y}h600" stroke="{INK}" stroke-width="2.5" fill="none"/>'

# 幹だけだと板に見えた。枝と葉を戻し、傷口と樽を大きくして「樹液を採る」場面にする。
add('sap', '木の幹の傷口から樹液がしたたり、下の桶にたまっている', f'''
{land(330)}
<g transform="translate(250 330)">
  <path d="M-58 0q-8-150 10-230h96q18 80 10 230z" fill="{BRN}" class="o"/>
  <g stroke="{BRN}" stroke-width="14" stroke-linecap="round" fill="none">
    <path d="M-30-200l-70-50M34-214l76-46"/>
  </g>
  <g class="greenp o">
    <circle cx="-116" cy="-268" r="44"/><circle cx="10" cy="-296" r="56"/><circle cx="126" cy="-274" r="46"/>
  </g>
  <g fill="none" stroke="#6b4c28" stroke-width="4">
    <path d="M-30-16q-4-140 6-200M4-12q0-146 2-204"/>
  </g>
  <path d="M-52-150h46v-32l-46 14z" fill="#e0c48a" class="o"/>
  <path d="M-52-150l-20 12" stroke="#c9a464" stroke-width="10" stroke-linecap="round" fill="none"/>
</g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2.5">
  <path d="M178 210q16 20 16 32t-16 16-16-16 16-32z"/>
  <path d="M176 274q12 15 12 24t-12 12-12-12 12-24z"/>
  <path d="M176 316q10 13 10 20t-10 10-10-10 10-20z"/>
</g>
<g transform="translate(176 366)">
  <path d="M-56-34h112l-10 34q-2 12-46 12t-46-12z" fill="#a0764a" class="o"/>
  <ellipse cy="-34" rx="56" ry="15" fill="{TONES['gold'][0]}" class="o"/>
  <g fill="none" stroke="#7a5b3c" stroke-width="3"><path d="M-52-16h104M-46 2h92"/></g>
</g>''', ground=False)

# どんぐりを大きく前に出し、樹冠を広く低くしてカシらしいどっしりした形にする。
add('oak', 'どっしりした太い幹と横に広がる樹冠のカシ、手前に大きなどんぐり', f'''
{land(322)}
<g transform="translate(280 322)">
  <path d="M-40 0q-6-90 8-134h64q14 44 8 134z" fill="{BRN}" class="o"/>
  <g stroke="{BRN}" stroke-width="16" stroke-linecap="round" fill="none">
    <path d="M-22-116l-66-42M28-124l70-38M2-130v-46"/>
  </g>
  <g class="greenp o">
    <circle cx="-120" cy="-180" r="60"/><circle cx="-34" cy="-218" r="70"/>
    <circle cx="66" cy="-200" r="62"/><circle cx="128" cy="-160" r="48"/>
    <circle cx="-70" cy="-142" r="52"/><circle cx="34" cy="-134" r="48"/>
  </g>
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="4">
    <path d="M-140-196q26-16 50 4M-16-238q28-14 52 8M76-214q26-14 48 8"/>
  </g>
</g>
<g transform="translate(494 300)">
  <path d="M-34 -18q0 66 34 78t34-78z" fill="#c9a464" class="o"/>
  <path d="M-38-52h76q10 0 10 16t-10 18h-76q-10 0-10-18t10-16z" fill="#8b6437" class="o"/>
  <path d="M0-52v-20" stroke="#6b4c28" stroke-width="7" stroke-linecap="round" fill="none"/>
  <g fill="none" stroke="#7a5b3c" stroke-width="2.5"><path d="M-34-42h68M-34-28h68"/></g>
</g>''', ground=False)

# つぼみを画面の主役の大きさにし、隣に開いた花を置いて「まだ開いていない」を対比で見せる。
add('bud', '枝の先でまだ開いていないふくらんだつぼみ、隣は開いた花', f'''
{land(330)}
<g transform="translate(230 330)">
  <path d="M-11 0h22v-190h-22z" class="greend o"/>
  <g class="greenp o">
    <path d="M-11-90q-60-34-38-66 48 12 38 66zM11-140q60-34 38-66-48 12-38 66z"/>
  </g>
  <g transform="translate(0 -246)">
    <path d="M0-58q52 4 52 52t-52 62q-52-14-52-62 0-48 52-52z" class="coralp o"/>
    <path d="M-20 44q-2-90 20-102 22 12 20 102-20 10-40 0z" class="coral o"/>
    <path d="M-46 42q-24 34 8 42 20-12 14-42zM46 42q24 34-8 42-20-12-14-42z" class="green o"/>
  </g>
</g>
<g transform="translate(452 330)">
  <path d="M-9 0h18v-150h-18z" class="greend o"/>
  <path d="M-9-70q-52-30-32-58 42 10 32 58z" class="greenp o"/>
  <g transform="translate(0 -190)">
    <g class="coralp o">
''' + ''.join(f'<ellipse cx="{46*__import__("math").cos(j*1.2566):.0f}" cy="{46*__import__("math").sin(j*1.2566):.0f}" rx="32" ry="26" transform="rotate({j*72} {46*__import__("math").cos(j*1.2566):.0f} {46*__import__("math").sin(j*1.2566):.0f})"/>' for j in range(5)) + f'''
    </g>
    <circle r="22" class="gold o"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M330 96h-52"/></g>''', arrow=True, ground=False)

print(sheet(W, '/tmp/vocab-sheet2.html', 5))
