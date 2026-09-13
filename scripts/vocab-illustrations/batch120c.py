# -*- coding: utf-8 -*-
"""第120回の描き直し2回目。pinch と knot はやり方を変える。"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))
def table(y=300):
    return (f'<path d="M40 {y}h520v20H40z" fill="#c9a464" class="o"/>'
            f'<path d="M80 {y+20}v60M520 {y+20}v60" stroke="#a0764a" stroke-width="14" stroke-linecap="round" fill="none"/>')
def finger(d, w=34):
    """線で指を描く。太い肌色の下に少し太い縁色を敷いて輪郭にする。"""
    return (f'<path d="{d}" fill="none" stroke="{SKINL}" stroke-width="{w+5}" stroke-linecap="round"/>'
            f'<path d="{d}" fill="none" stroke="{SKIN}" stroke-width="{w}" stroke-linecap="round"/>')

# 手のひら全体を形で描くと雲になる。親指と人差し指だけを線で描き、先端を合わせる。
add('pinch', '親指と人差し指の先を合わせて塩をひとつまみしている', f'''
{table(346)}
<g>
  <ellipse cx="380" cy="180" rx="72" ry="58" fill="{SKINL}"/>
  <ellipse cx="380" cy="180" rx="68" ry="54" fill="{SKIN}"/>
  {finger('M356 216L302 250', 40)}
  {finger('M416 214L310 246', 34)}
  <circle cx="303" cy="249" r="19" fill="{SKINL}"/>
  <circle cx="303" cy="249" r="15" fill="{SKIN}"/>
  <circle cx="309" cy="245" r="16" fill="{SKINL}"/>
  <circle cx="309" cy="245" r="12" fill="{SKIN}"/>
  <path d="M430 150q40 6 44 40" fill="none" stroke="{SKINL}" stroke-width="30" stroke-linecap="round"/>
  <path d="M430 150q40 6 44 40" fill="none" stroke="{SKIN}" stroke-width="25" stroke-linecap="round"/>
</g>
<g fill="#fffefd" stroke="{MUTED}" stroke-width="1.8">
''' + ''.join(f'<circle cx="{300+ (i%3)*11 - 8}" cy="{276+i*11}" r="4"/>' for i in range(7)) + f'''
</g>
<g transform="translate(292 340)">
  <ellipse cy="-8" rx="80" ry="22" fill="#f0e6d0" class="o"/>
  <path d="M-80-8q0 34 80 34t80-34z" fill="#fffdf6" class="o"/>
  <g fill="#fffefd" stroke="{MUTED}" stroke-width="1.5">
    <circle cx="-34" cy="-8" r="5"/><circle cx="0" cy="-4" r="5"/><circle cx="34" cy="-10" r="5"/><circle cx="-10" cy="-15" r="4"/><circle cx="20" cy="-14" r="4"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M140 210l130 26"/></g>''', arrow=True, ground=False)

# 縄一本では結び目に見えない。荷物を縛った縄の交点に結び目とほどけた両端を描く。
add('knot', '荷物を縛った縄が交わるところで固く結ばれ、両端が垂れている', f'''
{table(340)}
<g transform="translate(300 240)">
  <path d="M-140-70h280v130h-280z" fill="#d9c49a" class="o"/>
  <path d="M-140-70l30-30h280l-30 30z" fill="#e8d8b4" class="o"/>
  <path d="M140-70l30-30v130l-30 30z" fill="#c0a877" class="o"/>
  <path d="M-24-70h48v130h-48z" fill="#a0764a"/>
  <path d="M-24-100h48l-30 30h-48z" fill="#b08c50"/>
  <path d="M-140 4h280" stroke="#a0764a" stroke-width="18" fill="none"/>
  <path d="M140 4l30-30" stroke="#a0764a" stroke-width="18" fill="none"/>
</g>
<g transform="translate(276 168)">
  <path d="M-56-8q-14 22 6 34 24 14 46-4 22 18 46 4 20-12 6-34-16-20-52-20t-52 20z" fill="#b08c50" class="o"/>
  <path d="M-30 4q30 26 60 0" fill="none" stroke="#8b6437" stroke-width="4"/>
  <path d="M-16 24q-14 44-56 56" fill="none" stroke="#a0764a" stroke-width="16" stroke-linecap="round"/>
  <path d="M18 24q18 44 62 50" fill="none" stroke="#a0764a" stroke-width="16" stroke-linecap="round"/>
  <g fill="none" stroke="#8b6437" stroke-width="3">
    <path d="M-58 74l-12 6M76 70l12 6"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M440 96l-120 46"/></g>''', arrow=True, ground=False)

print(sheet(W, '/tmp/vocab-sheet3.html', 5))
