# -*- coding: utf-8 -*-
"""第182回の描き直し。backyard に屋根を足し、tuesday の剣を太くする。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def week_strip(n, y=330, cls='coral'):
    g = []
    for i in range(7):
        x = 90 + i * 60
        c = TONES[cls][0] if i == n - 1 else '#fffefd'
        g.append(f'<rect x="{x}" y="{y}" width="52" height="44" rx="6" fill="{c}" stroke="{INK}" stroke-width="2.5"/>')
    return ''.join(g)

add('backyard', '家の裏手にある、柵で囲まれた芝生の庭',
    '裏庭＝backyard。', f'''
<path d="M0 250h600v150H0z" class="greenp"/>
<g transform="translate(130 250)">
  <path d="M-110 0v-110h220V0z" fill="#fffefd" class="o"/>
  <path d="M-126-110L0-190l126 80z" class="corald o"/>
  <path d="M-40 0v-70h80V0z" class="coral o"/>
  <path d="M52-84h44v36h-44z" class="coralp o"/></g>
{''.join(f'<path d="M{300+i*50} 300v-70" stroke="{BRN}" stroke-width="11" fill="none" stroke-linecap="round"/>' for i in range(6))}
<path d="M290 250h270M290 278h270" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>
{tree(430, 250, 0.7)}
{''.join(flower(200 + i * 50, 340, 0.5, c) for i, c in enumerate(['coral', 'gold']))}''')

add('tuesday', '7マスの週の帯の2つ目が塗られ、上に軍神の剣が置かれる',
    '火曜日＝Tuesday。軍神ティール(Tiw)の日が語源です。', f'''
<g transform="translate(300 175)">
  <path d="M-26-120h52v150h-52z" fill="#c3cbd1" class="o"/>
  <path d="M-26 30h52l-26 44z" fill="#c3cbd1" class="o"/>
  <path d="M0-120v150" fill="none" stroke="#9aa7b1" stroke-width="4"/>
  <path d="M-80-134h160v26h-160z" class="goldd o"/>
  <path d="M-16-108h32v-40h-32z" fill="{BRN}" class="o"/>
  <circle cx="0" cy="-158" r="16" class="gold o"/></g>
{week_strip(2)}''')

finish(__file__)
