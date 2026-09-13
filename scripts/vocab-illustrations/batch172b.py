# -*- coding: utf-8 -*-
"""第172回の描き直し。infectious / interfere with / iron out / miss the point。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def target(x, y, r=90):
    return ''.join(f'<circle cx="{x}" cy="{y}" r="{r-i*r/3:.0f}" class="{c} o"/>'
                   for i, c in enumerate(['coralp', 'coral', 'corald']))

def yawn(x, y, r=40, hair='short'):
    return (f'<g transform="translate({x} {y})">'
            f'<circle r="{r}" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>'
            f'<path d="{HAIRS[hair]}" transform="translate(0 {r*4.5:.0f}) scale({r/24:.2f})" fill="{HAIR}"/>'
            f'<path d="M{-r*0.4:.0f} {-r*0.2:.0f}l{r*0.26:.0f} {r*0.1:.0f}M{r*0.4:.0f} {-r*0.2:.0f}l{-r*0.26:.0f} {r*0.1:.0f}" '
            f'fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
            f'<ellipse cy="{r*0.45:.0f}" rx="{r*0.3:.0f}" ry="{r*0.36:.0f}" class="ink"/></g>')

add('infectious', '一人のあくびが、隣へ、その隣へと次々にうつっていく',
    '感染性の、(感情が)人にうつる＝infectious。', f'''
{''.join(yawn(100 + i * 133, 230, 44, h) for i, h in enumerate(['short', 'bob', 'bun', 'cap']))}
{''.join(f'<path d="M{152+i*133} 176q34-42 76 0" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>' for i in range(3))}
{''.join(f'<path d="M{100+i*133} 170q10-18 0-34" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(4))}''', arrow=True)

add('interfere with', 'すんなり流れていた水路に石が投げこまれ、その先の流れが乱れる',
    '妨げる、じゃまをする＝interfere with。', f'''
<g transform="translate(300 250)">
  <path d="M-260-100h520v200h-520z" class="bluep o"/></g>
{''.join(f'<path d="M{50+i*40} {200+j*50}q20-16 40 0" fill="none" stroke="{BLU}" stroke-width="6"/>' for i in range(4) for j in range(3))}
{''.join(f'<path d="M{370+i*44} {194+ (i%3)*30 + j*46}q18-18 34 4t34-8" fill="none" stroke="{BLU}" stroke-width="6"/>' for i in range(3) for j in range(2))}
<g transform="translate(320 250) rotate(16)"><path d="M-54-48h108v96h-108z" fill="{STONE}" class="o"/></g>
{line(320, 50, 320, 168, MUTED, True, 6)}
{''.join(f'<path d="M{400+i*26} {150-i*12}l16-18" fill="none" stroke="{CRL}" stroke-width="5"/>' for i in range(3))}''', arrow=True)

add('iron out', 'しわの寄った布にアイロンをかけると、通ったあとが平らになる',
    '(問題を)片づける、調整する＝iron out。', f'''
{table(352)}
<g transform="translate(300 300)">
  <path d="M-260-50h520v50h-520z" fill="#fffefd" class="o"/></g>
<path d="M340 268q34-30 68 0t68 0 68 0" fill="none" stroke="{MUTED}" stroke-width="6"/>
<path d="M40 268h240" fill="none" stroke="{MUTED}" stroke-width="6"/>
<g transform="translate(300 214)">
  <path d="M-96 56h192l-36-80h-120z" class="teal o"/>
  <path d="M-96 56h192v14h-192z" class="teald o"/>
  <path d="M-70-24h140v-20h-140z" class="teald o"/>
  <path d="M-40-44q40-50 80 0" fill="none" stroke="{INK}" stroke-width="10"/></g>
{''.join(f'<path d="M{170+i*30} {170-i*10}q16-18 0-34" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}
{tick(110, 190, 0.6)}''')

add('miss the point', '放った矢が的から大きく外れ、何もない所に刺さっている',
    '論点を取り違える＝miss the point。', f'''
{target(230, 220, 100)}
{person(120, 350, 1.0, 1, 'teal', 'blue', 'point', 'short', 'smile')}
<g transform="translate(500 110) rotate(30)">
  <path d="M-150 0h150" stroke="{BRN}" stroke-width="7" fill="none" stroke-linecap="round"/>
  <path d="M0 0l-30-16v32z" class="ink"/>
  <path d="M-150 0l-24-16M-150 0l-24 16" stroke="{CRL}" stroke-width="6" fill="none" stroke-linecap="round"/></g>
<path d="M170 300q160-190 300-190" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>
{cross(540, 210, 0.6)}
{ring(230, 220, 22, True, 'teal')}''')

finish(__file__)
