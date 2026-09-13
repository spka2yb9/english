# -*- coding: utf-8 -*-
"""第120回の描き直し。pinch(手が雲に見えた)、knot(こぶだけで結び目に見えない)、
hem(ただの布)、flake(茶色い斑点)、burrow(動物がなめくじに見えた)。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))
def table(y=300):
    return (f'<path d="M40 {y}h520v20H40z" fill="#c9a464" class="o"/>'
            f'<path d="M80 {y+20}v60M520 {y+20}v60" stroke="#a0764a" stroke-width="14" stroke-linecap="round" fill="none"/>')

# 手のひらを描くと雲になる。親指と人差し指の2本だけを大きく描いて「つまむ」を見せる。
add('pinch', '親指と人差し指の先で塩をひとつまみしている', f'''
{table(340)}
<g transform="translate(280 170)">
  <path d="M-30 60q-46-10-52-56-6-46 26-70 26-20 46 4 14 18 2 44" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-10 62q40-18 46-64 6-44-24-58-26-12-40 12-10 20 4 42" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-8-18q-16 22-4 44" fill="none" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-52 40q-40 10-56 46" stroke="{SKIN}" stroke-width="30" stroke-linecap="round" fill="none"/>
  <path d="M-52 40q-40 10-56 46" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g fill="#fffefd" stroke="{MUTED}" stroke-width="1.8">
''' + ''.join(f'<circle cx="{264+ (i%4)*13}" cy="{248+i*13}" r="4"/>' for i in range(8)) + f'''
</g>
<g transform="translate(288 330)">
  <ellipse cy="-8" rx="76" ry="22" fill="#f0e6d0" class="o"/>
  <path d="M-76-8q0 34 76 34t76-34z" fill="#fffdf6" class="o"/>
  <g fill="#fffefd" stroke="{MUTED}" stroke-width="1.5">
    <circle cx="-30" cy="-8" r="5"/><circle cx="0" cy="-4" r="5"/><circle cx="30" cy="-10" r="5"/><circle cx="-8" cy="-14" r="4"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M440 190l-88 8"/></g>''', arrow=True, ground=False)

# こぶを描いても結び目にならない。2本の綱を交差させ、互いをくぐらせる。
add('knot', '二本のロープが交差してくぐり合い、固い結び目になっている', f'''
<g transform="translate(300 200)">
  <path d="M-270 90q90 10 140-40" fill="none" stroke="#c9a464" stroke-width="30" stroke-linecap="round"/>
  <path d="M270 90q-90 10-140-40" fill="none" stroke="#b08c50" stroke-width="30" stroke-linecap="round"/>
  <path d="M-130 50q-30-70 30-90t60 40" fill="none" stroke="#c9a464" stroke-width="30" stroke-linecap="round"/>
  <path d="M130 50q30-70-30-90t-60 40" fill="none" stroke="#b08c50" stroke-width="30" stroke-linecap="round"/>
  <path d="M-40 0q40 44 80 0" fill="none" stroke="#c9a464" stroke-width="30" stroke-linecap="round"/>
  <path d="M40 0q-40 44-80 0" fill="none" stroke="#b08c50" stroke-width="30" stroke-linecap="round" stroke-dasharray="34 40"/>
  <g fill="none" stroke="#a0764a" stroke-width="3">
    <path d="M-250 84h50M200 84h50M-96-38q20-18 40-6M96-38q-20-18-40-6"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 340v-90"/></g>''', arrow=True, ground=False)

# 「折り返して縫う」が見えないと ただの布。端を斜めに折り返して裏地を見せる。
add('hem', '布のすそを裏へ折り返し、その折り目を縫いとめている', f'''
{table(340)}
<g transform="translate(300 200)">
  <path d="M-170-100h340v170h-340z" class="bluep o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"><path d="M-170-50h340M-170 10h340"/></g>
  <path d="M-170 70h340v40h-340z" class="blued o"/>
  <path d="M-170 110h340l-40 34h-260z" class="blue o"/>
  <path d="M-170 70h340" stroke="{INK}" stroke-width="3" fill="none"/>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{-150+i*32} 92h18"/>' for i in range(10)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 380v-52"/></g>
<g transform="translate(470 130) rotate(40)">
  <path d="M0 0l-5-64 5-10 5 10z" fill="#c8d0d8" class="o"/>
  <ellipse cy="-54" rx="3.5" ry="7" fill="{INK}"/>
</g>
<path d="M456 176q34 20 60-4" fill="none" stroke="{TONES['gold'][0]}" stroke-width="4"/>''', arrow=True, ground=False)

# 斑点では「はがれ落ちる」が出ない。塗装がめくれ上がった縁と、落下中の薄片を描く。
add('flake', '壁の塗装がめくれ上がり、薄片になってはがれ落ちている', f'''
<path d="M0 0h600v400H0z" fill="#5c86ad"/>
<path d="M0 0h340v400H0z" fill="#f0e6d0"/>
<path d="M340 0q-40 60 10 120t-30 110 20 170" fill="#f0e6d0"/>
<path d="M340 0q-40 60 10 120t-30 110 20 170" fill="none" stroke="{INK}" stroke-width="2.5"/>
<g fill="#e0d4b8" stroke="{INK}" stroke-width="2">
  <path d="M340 60q46 24 34 56-40-8-34-56z"/>
  <path d="M320 240q50 16 44 52-44-4-44-52z"/>
</g>
<g fill="none" stroke="#d9cdb0" stroke-width="3">
  <path d="M60 80h200M60 160h180M60 240h210M60 320h170"/>
</g>
<g fill="#f0e6d0" class="o">
  <path d="M400 130l40 14-10 34-38-16z" transform="rotate(20 418 156)"/>
  <path d="M470 230l34 18-16 30-32-20z" transform="rotate(-30 486 254)"/>
  <path d="M420 320l30 16-14 28-28-18z" transform="rotate(12 434 342)"/>
  <path d="M520 90l26 14-12 24-24-16z" transform="rotate(40 532 110)"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M382 90q60 100 60 250"/></g>''', arrow=True, ground=False)

# 動物が横長のかたまりだけだと なめくじになる。頭・耳・足・尾を分けて描く。
add('burrow', '地面の下に掘られたトンネル状の巣穴と、その中のウサギ', f'''
<path d="M0 0h600v170H0z" fill="#dceaf4"/>
<path d="M0 170h600v230H0z" fill="#c9a464"/>
<path d="M0 158h600v14H0z" fill="#dfe8d8"/>
<path d="M0 158h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="#b08c50" stroke-width="3">
  <path d="M40 220h100M420 210h120M100 330h140M400 330h150"/>
</g>
<path d="M170 170q0 110 140 110t130-70" fill="none" stroke="#8b6437" stroke-width="70" stroke-linecap="round"/>
<path d="M170 170q0 110 140 110t130-70" fill="none" stroke="#f0e6d0" stroke-width="54" stroke-linecap="round"/>
<g transform="translate(316 262) scale(0.9)">
  <ellipse rx="52" ry="34" fill="#b8a48c" class="o"/>
  <circle cx="52" cy="-22" r="26" fill="#b8a48c" class="o"/>
  <path d="M42-46q-8-46 8-48 14 4 12 48zM66-46q8-44 22-40 8 10-8 42z" fill="#b8a48c" class="o"/>
  <path d="M46-44q-4-30 6-32 8 2 8 32zM68-44q6-28 16-26 4 8-6 28z" class="coralp"/>
  <circle cx="62" cy="-24" r="3.5" fill="{INK}"/>
  <circle cx="76" cy="-14" r="5" fill="{SKINL}"/>
  <g stroke="#8f7f68" stroke-width="9" stroke-linecap="round" fill="none"><path d="M-20 32v14M18 32v14"/></g>
  <circle cx="-56" cy="-14" r="14" fill="#e8e2d6" class="o"/>
</g>
<g fill="#a0764a" class="o">
  <path d="M136 158q34-32 76-16-34 24-76 16z"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M110 80q40 40 46 62"/></g>''', arrow=True, ground=False)

print(sheet(W, '/tmp/vocab-sheet2.html', 5))
