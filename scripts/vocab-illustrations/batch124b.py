# -*- coding: utf-8 -*-
"""第124回の描き直し。chromosome(葉に見えた)、gown(円すいに見えた)、cuff(白い箱に見えた)。"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))
def table(y=300):
    return (f'<path d="M40 {y}h520v20H40z" fill="#c9a464" class="o"/>'
            f'<path d="M80 {y+20}v60M520 {y+20}v60" stroke="#a0764a" stroke-width="14" stroke-linecap="round" fill="none"/>')

# 曲線4本だと葉になる。太い棒2本を交差させ、真ん中をくびれさせて X を作る。
add('chromosome', '中央がくびれたX字形の染色体が並んでいる', f'''
<path d="M0 0h600v400H0z" fill="#eef4f8"/>
<g>
''' + ''.join(f'''<g transform="translate({110+ (i%4)*130} {130+(i//4)*150}) scale({1.0-(i%3)*0.1})">
  <path d="M-46-90q26 0 34 26l14 46-14 46q-8 26-34 26-16 0-16-18l24-54-24-54q0-18 16-18z"
        fill="{TONES[["violet","teal","coral","gold"][i%4]][0]}" class="o"/>
  <path d="M46-90q-26 0-34 26L-2-18l14 46q8 26 34 26 16 0 16-18L38-18l24-54q0-18-16-18z"
        fill="{TONES[["violet","teal","coral","gold"][i%4]][0]}" class="o"/>
  <ellipse cy="-18" rx="20" ry="13" fill="{TONES[["violet","teal","coral","gold"][i%4]][2]}" class="o"/>
</g>''' for i in range(8)) + f'''
</g>
<g transform="translate(500 320)">
  <circle r="66" fill="none" stroke="{INK}" stroke-width="9"/>
  <path d="M48 48l44 44" stroke="{INK}" stroke-width="12" stroke-linecap="round" fill="none"/>
</g>''', ground=False)

# 三角に塗ると円すいになる。人の形を残したまま、すそだけを床まで長く広げる。
add('gown', 'すそが床まで届く長い式服を着て立っている', f'''
{table(380)}
<g transform="translate(300 380)">
  <path d="M-30-176q30-16 60 0l14 60 46 116h-180l46-116z" class="violet o"/>
  <path d="M-30-176l-52 46 20 26 32-38M30-176l52 46-20 26-32-38" class="violet o"/>
  <g fill="none" stroke="{TONES['violet'][2]}" stroke-width="3">
    <path d="M-52-56q52 18 104 0M-72-8q72 22 144 0"/>
  </g>
  <path d="M-18-178q18 12 36 0l-4 26h-28z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <circle cy="-208" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['bun']}" transform="translate(0 -100)" fill="{HAIR}" stroke="{HAIR}" stroke-width="2"/>
  <circle cx="-9" cy="-204" r="2.4" fill="{INK}"/><circle cx="9" cy="-204" r="2.4" fill="{INK}"/>
  <path d="M-9-193q9 8 18 0" fill="none" stroke="{INK}" stroke-width="2"/>
  <path d="M-82-130l-26 40M82-130l26 40" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M160 190l-24-20M450 180l26-20"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M480 330l-110-14"/></g>''', arrow=True, ground=False)

# そで口だけ切り出すと白い箱になる。腕を通し、手首の位置が分かるようにする。
add('cuff', 'シャツのそで口が手首を包み、ボタンが二つついている', f'''
{table(340)}
<g transform="translate(300 220) rotate(-14)">
  <path d="M-230-58h190v116h-190z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-220-20h170M-220 20h170"/></g>
  <path d="M-40-72h96v144h-96z" fill="#e8eef2" class="o"/>
  <path d="M-40-72h96v10h-96zM-40 62h96v10h-96z" fill="#cfd8e0"/>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="2.5">
    <circle cx="8" cy="-26" r="13"/><circle cx="8" cy="26" r="13"/>
  </g>
  <g fill="{INK}"><circle cx="4" cy="-30" r="2"/><circle cx="12" cy="-22" r="2"/><circle cx="4" cy="22" r="2"/><circle cx="12" cy="30" r="2"/></g>
  <path d="M56-44h60q16 0 16 44t-16 44H56z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <ellipse cx="152" rx="46" ry="42" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <g fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5">
    <rect x="180" y="-32" width="46" height="17" rx="8.5"/><rect x="184" y="-9" width="48" height="17" rx="8.5"/><rect x="180" y="14" width="42" height="17" rx="8.5"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 100v60"/></g>''', arrow=True, ground=False)

print(sheet(W, '/tmp/vocab-sheet2.html', 5))
