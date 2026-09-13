# -*- coding: utf-8 -*-
"""第186回の描き直し。lilac が壊れていた。hoop は禁止記号に見えたので差し替える。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def blossom(x, y, n=9):
    return ''.join(
        f'<circle cx="{x - 20 + (j % 3) * 20}" cy="{y - 20 + (j // 3) * 18}" r="11" '
        f'fill="#b79ad8" stroke="{VIOD}" stroke-width="1.5"/>' for j in range(n))

add('lilac', '房になった薄紫の花をつけた低木が、庭のすみに咲く',
    'ライラック＝lilac。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
<g transform="translate(300 300)">
  <path d="M-8 0v-80h16V0z" class="goldd"/>
  <path d="M0-70l-70-56M0-70l70-60M0-90v-56" fill="none" stroke="{BRN}" stroke-width="7"/>
  {''.join(f'<ellipse cx="{x}" cy="{y}" rx="20" ry="11" class="green o" transform="rotate({r} {x} {y})"/>' for x, y, r in [(-54, -62, -20), (54, -66, 20), (-18, -34, -10), (22, -40, 14)])}</g>
{blossom(230, 158)}
{blossom(370, 154)}
{blossom(300, 128)}
{''.join(f'<path d="M{100 + i * 400} 250v-60" stroke="{BRN}" stroke-width="8" fill="none"/>' for i in range(2))}''')

add('hoop', 'バスケットの輪に網が下がり、ボールが上から通り抜ける',
    '輪、(バスケットの)リング＝hoop。', f'''
<path d="M0 330h600v70H0z" class="ground"/>
<g transform="translate(340 200)">
  <path d="M-30-110h180v140h-180z" fill="#fffefd" class="o"/>
  <path d="M20-70h80v60H20z" fill="none" stroke="{CRL}" stroke-width="5"/>
  <path d="M-30 30h180v14h-180z" fill="#9aa7b1"/>
  <path d="M150-40h40v190h-40z" fill="{MUTED}"/>
  <ellipse cx="-40" cy="30" rx="70" ry="14" fill="none" stroke="{CRL}" stroke-width="9"/>
  {''.join(f'<path d="M{-40 + int(68*math.cos(math.radians(a)))} {30 + int(13*math.sin(math.radians(a)))}q{int(6*math.cos(math.radians(a)))} 40 {int(-14*math.cos(math.radians(a)))} 62" fill="none" stroke="#fffefd" stroke-width="3"/>' for a in range(0, 360, 30))}</g>
<g transform="translate(300 130)">
  <circle r="34" class="gold o"/>
  <path d="M-34 0h68M0-34v68" fill="none" stroke="{GLDD}" stroke-width="3"/></g>
{arc(300, 90, 300, 200, 0, MUTED, True, 5)}''', arrow=True)

finish(__file__)
