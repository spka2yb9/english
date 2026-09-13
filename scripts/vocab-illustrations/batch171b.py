# -*- coding: utf-8 -*-
"""第171回の描き直し。fragmentation の破片が出ていなかった。hawk も描き直す。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

add('fragmentation', '一枚だった板が砕けて、大小の破片に散らばる',
    '断片化、分裂＝fragmentation。', f'''
{split()}
<g transform="translate(150 200)"><path d="M-100-80h200v160h-200z" class="teal o"/></g>
{''.join(f'<g transform="translate({x} {y}) rotate({r})"><path d="{p}" class="teal o"/></g>'
         for x, y, r, p in [(390, 130, 12, 'M-40-30h60l10 40-50 20z'),
                            (480, 190, -24, 'M-30-24h44l6 34-40 14z'),
                            (396, 244, 30, 'M-26-20h36l8 30-36 12z'),
                            (506, 110, -14, 'M-20-16h28l6 24-28 10z'),
                            (476, 300, 20, 'M-24-18h32l6 26-32 10z'),
                            (368, 324, -30, 'M-18-14h24l4 20-24 8z')])}
{arc(260, 160, 320, 170, 44, MUTED, True, 4)}''', arrow=True)

add('hawk', '幅の広い翼を張り、かぎ状のくちばしを持つタカが空を舞う',
    'タカ、(政治の)強硬派＝hawk。', f'''
{''.join(cloud(110 + i * 240, 80, 0.9, 'blue') for i in range(2))}
<g transform="translate(300 220)">
  <path d="M-26-16q-56-64-172-76 48 44 66 62-56 10-84 44 84-18 152 4z" fill="#8b6437" class="o"/>
  <path d="M26-16q56-64 172-76-48 44-66 62 56 10 84 44-84-18-152 4z" fill="#8b6437" class="o"/>
  <path d="M-26 40q26 62 52 0z" fill="#a0764a" class="o"/>
  <ellipse rx="30" ry="46" fill="#a0764a" class="o"/>
  {''.join(f'<path d="M{-18+i*12} -14q6 16 0 32" fill="none" stroke="#6a5040" stroke-width="2.5"/>' for i in range(4))}
  <circle cx="0" cy="-58" r="24" fill="#a0764a" class="o"/>
  <path d="M18-64q22 2 20 14-12 10-20 2z" class="gold o"/>
  <circle cx="8" cy="-68" r="4" class="ink"/>
  <path d="M-12 84l-12 26M12 84l12 26" stroke="{GLDD}" stroke-width="7" fill="none" stroke-linecap="round"/></g>''')

finish(__file__)
