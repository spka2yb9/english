# -*- coding: utf-8 -*-
"""第172回の描き直し2。infectious の髪の位置、iron out のアイロン、miss the point の矢の位置。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def target(x, y, r=90):
    return ''.join(f'<circle cx="{x}" cy="{y}" r="{r-i*r/3:.0f}" class="{c} o"/>'
                   for i, c in enumerate(['coralp', 'coral', 'corald']))

def yawn(x, y, r=40, hair='short'):
    s = r / 24
    return (f'<g transform="translate({x} {y})">'
            f'<circle r="{r}" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>'
            f'<path d="{HAIRS[hair]}" transform="translate(0 {108*s:.0f}) scale({s:.2f})" fill="{HAIR}"/>'
            f'<path d="M{-r*0.42:.0f} {-r*0.18:.0f}l{r*0.26:.0f} {r*0.1:.0f}M{r*0.42:.0f} {-r*0.18:.0f}l{-r*0.26:.0f} {r*0.1:.0f}" '
            f'fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
            f'<ellipse cy="{r*0.44:.0f}" rx="{r*0.28:.0f}" ry="{r*0.34:.0f}" class="ink"/></g>')

add('infectious', '一人のあくびが、隣へ、その隣へと次々にうつっていく',
    '感染性の、(感情が)人にうつる＝infectious。', f'''
{''.join(yawn(100 + i * 133, 230, 46, h) for i, h in enumerate(['short', 'bob', 'bun', 'cap']))}
{''.join(f'<path d="M154+{i*133} 0" fill="none"/>' for i in range(0))}
{''.join(f'<path d="M{154+i*133} 174q34-42 76 0" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>' for i in range(3))}
{''.join(f'<path d="M{100+i*133} 168q12-18 0-36" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(4))}''', arrow=True)

add('iron out', 'しわの寄った布にアイロンをかけると、通ったあとが平らになる',
    '(問題を)片づける、調整する＝iron out。', f'''
{table(352)}
<g transform="translate(300 300)">
  <path d="M-260-54h520v54h-520z" fill="#fffefd" class="o"/></g>
<path d="M350 272q34-32 68 0t68 0 68 0" fill="none" stroke="{MUTED}" stroke-width="6"/>
<path d="M40 272h230" fill="none" stroke="{MUTED}" stroke-width="6"/>
<g transform="translate(290 220)">
  <path d="M-130 66q-14-30 24-32h216q14 18-4 32z" class="teald o"/>
  <path d="M-104 34h214q20-46-20-56h-160q-38 8-34 56z" class="teal o"/>
  <path d="M-74-22h150v-24h-150z" class="teald o"/>
  <path d="M-58-46q60-52 118 0" fill="none" stroke="{INK}" stroke-width="14" stroke-linecap="round"/></g>
{''.join(f'<path d="M{150+i*30} {180-i*12}q16-18 0-34" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}
{tick(100, 200, 0.6)}''')

add('miss the point', '放った矢が的から大きく外れ、何もない所に刺さっている',
    '論点を取り違える＝miss the point。', f'''
{target(220, 240, 96)}
{person(110, 350, 1.0, 1, 'teal', 'blue', 'point', 'short', 'smile')}
<g transform="translate(470 140) rotate(28)">
  <path d="M-140 0h140" stroke="{BRN}" stroke-width="7" fill="none" stroke-linecap="round"/>
  <path d="M0 0l-28-15v30z" class="ink"/>
  <path d="M-140 0l-22-15M-140 0l-22 15" stroke="{CRL}" stroke-width="6" fill="none" stroke-linecap="round"/></g>
<path d="M160 320q170-190 280-160" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>
{cross(500, 250, 0.6)}
{ring(220, 240, 20, True, 'teal')}''')

finish(__file__)
