# -*- coding: utf-8 -*-
"""第116回の描き直し。淡すぎて形が読めない5点を描き起こす。"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))

add('pasta', '皿に山盛りの黄色い麺にトマトソースがかかっている', f'''
<g>
  <ellipse cx="300" cy="256" rx="190" ry="62" fill="#fffefd" class="o"/>
  <ellipse cx="300" cy="250" rx="150" ry="46" fill="#efe9dc"/>
</g>
<g fill="none" stroke="#e8c25c" stroke-width="13" stroke-linecap="round">
  <path d="M186 246q46-56 114-36t116 30"/>
  <path d="M192 262q52-38 108-20t114 20"/>
  <path d="M198 230q44-50 102-30t108 26"/>
  <path d="M210 276q48-24 92-10t102 12"/>
</g>
<g fill="none" stroke="#c99a2e" stroke-width="4" stroke-linecap="round">
  <path d="M186 246q46-56 114-36t116 30"/>
  <path d="M198 230q44-50 102-30t108 26"/>
</g>
<g class="coral o">
  <path d="M244 216q56-30 110 0 26 20-14 34-52 14-88 0-30-16-8-34z"/>
</g>
<g fill="{TONES['coral'][2]}"><circle cx="284" cy="226" r="5"/><circle cx="322" cy="232" r="5"/></g>
<g class="green o"><path d="M338 208q16-16 30-4-8 18-30 4z"/></g>
<path d="M96 316h408" class="a"/>''', ground=False)

add('pork', '骨のついた豚肉のかたまりが一切れ', f'''
<g transform="translate(310 214)">
  <path d="M-90 40q-34-66 20-100 56-36 130-14 62 18 56 66-6 48-84 56-84 8-122-8z" fill="#efa79e" class="o"/>
  <path d="M-62 26q-22-48 24-72 46-24 108-6 50 14 44 46-6 32-70 38-70 6-106-6z" fill="#e08a80"/>
  <path d="M60-44q34-8 52 10-16 22-52 12z" fill="#fdf0e4" class="o"/>
  <path d="M-90 40q-40-8-46-34-6-26 22-34l30 10z" fill="#fdf8ec" class="o"/>
  <path d="M-104 16q-20-6-18-18t18-14" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<path d="M120 292h380" class="a"/>''', ground=False)

add('ginger', 'こぶが枝分かれしたしょうがの根、切り口が黄色い', f'''
<g transform="translate(300 216)">
  <path d="M-130 24q-20-52 30-64 46-12 70 8 30-46 80-28 46 16 36 56-10 38-62 38-46 0-72-16-34 22-82 6z" fill="#d8b878" class="o"/>
  <path d="M62-52q34-46 70-22 30 18 6 50-24 30-58 8z" fill="#e0c48a" class="o"/>
  <path d="M-104 40q-28 38 6 54 30 14 44-16z" fill="#c9a464" class="o"/>
  <g fill="none" stroke="#a8873f" stroke-width="4">
    <path d="M-66-14q22 22 50 12M22-26q20 20 48 8M-44 34q28 14 56 0M-14-40q18 14 36 6"/>
  </g>
  <ellipse cx="-118" cy="14" rx="16" ry="26" fill="#f2dda2" class="o" transform="rotate(-20 -118 14)"/>
</g>
<path d="M140 306h320" class="a"/>''', ground=False)

add('pear', '首が細く下がふくらんだ黄緑色の洋なし', f'''
<g transform="translate(300 216)">
  <path d="M0-116q26 0 26 30 0 28-16 48 52 24 52 84 0 68-62 68t-62-68q0-60 52-84-16-20-16-48 0-30 26-30z" fill="#c9d95e" class="o"/>
  <path d="M0-116q26 0 26 30 0 28-16 48 52 24 52 84 0 68-62 68z" fill="#b6c848"/>
  <path d="M-28 20q-18 36 4 66" fill="none" stroke="#e8f0a8" stroke-width="10" stroke-linecap="round"/>
  <path d="M0-116v-28" stroke="#8b6437" stroke-width="8" stroke-linecap="round" fill="none"/>
  <path d="M6-136q36-18 44 12-32 12-44-12z" class="green o"/>
</g>
<path d="M190 320h220" class="a"/>''', ground=False)

add('dough', 'こね台の上のパン生地を両手で押している', f'''
<path d="M60 290h480v34H60z" fill="#c99a63" class="o"/>
<g>
  <path d="M160 290q-24-108 140-108t140 108z" fill="#f6ead2" class="o"/>
  <g fill="none" stroke="#ddceac" stroke-width="5">
    <path d="M224 262q36-26 76-6t76-16"/>
  </g>
</g>
<g>
  <path d="M186 200l-42-40q-10-10 2-20t22 0l44 40z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <ellipse cx="216" cy="212" rx="46" ry="32" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M414 200l42-40q10-10-2-20t-22 0l-44 40z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <ellipse cx="384" cy="212" rx="46" ry="32" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 148v34M360 148v34"/></g>
<g fill="#f6ead2" stroke="{INK}" stroke-width="2">
  <circle cx="126" cy="282" r="10"/><circle cx="478" cy="284" r="8"/>
</g>''', arrow=True, ground=False)

print(sheet(W, '/tmp/vocab-sheet2.html', 3))
