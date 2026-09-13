# -*- coding: utf-8 -*-
"""第168回の描き直し。bachelor / barrister / adaptable。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

add('bachelor', '食卓に一人分の皿といすが一つだけあり、向かいのいすは空いたまま',
    '独身男性、学士＝bachelor。', f'''
{table(286)}
{chair(210, 286, 1.0, 'gold', 1)}
{sit(210, 286, 1.05, 1, 'blue', 'green', 'short', 'smile', 'lap')}
<g transform="translate(300 278)">
  <ellipse rx="58" ry="17" fill="#fffefd" class="o"/>
  <ellipse rx="32" ry="8" fill="none" stroke="{MUTED}" stroke-width="2.5"/></g>
<g opacity="0.28">{chair(470, 286, 1.0, 'gold', -1)}</g>
<g transform="translate(452 278)" opacity="0.3">
  <ellipse rx="58" ry="17" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9"/></g>
{ring(470, 210, 60, True)}''')

add('barrister', '白いかつらと黒いガウンをまとった弁護士が、法廷で書類を手に立つ',
    '法廷弁護士(英)＝barrister。', f'''
<path d="M0 60h600v246H0z" fill="#f4ead9"/>
{table(300)}
<g transform="translate(300 306)">
  <path d="M-70 0v-150q70-30 140 0V0z" fill="#2f3542" class="o"/>
  <path d="M-24-150q24 26 48 0l-16 60h-16z" fill="#fffefd" class="o"/>
  <path d="M-34-196q-14 26-8 48 4 16 18 14M34-196q14 26 8 48-4 16-18 14" fill="#f2f2f0" class="o"/>
  <circle cx="0" cy="-186" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-30-198q6-28 30-28t30 28q-16-14-30-8-16-8-30 8z" fill="#f2f2f0" class="o"/>
  <circle cx="-9" cy="-186" r="2.6" class="ink"/><circle cx="9" cy="-186" r="2.6" class="ink"/>
  <path d="M-8-174q8 7 16 0" fill="none" stroke="{INK}" stroke-width="2.2"/>
  <path d="M-70-150l-40 66M70-150l44 60" fill="none" stroke="#2f3542" stroke-width="14" stroke-linecap="round"/></g>
{doc(470, 236, 108, 136, 3)}
<g transform="translate(110 250)"><path d="M-40 40h80v14h-80z" fill="{BRN}" class="o"/>
  <path d="M-10 40v-46h20v46z" fill="{BRN}"/><path d="M-46-6h92l-46-34z" fill="{BRN}" class="o"/></g>''')

add('adaptable', '同じ粘土のかたまりが、四角い型にも丸い型にも収まって形を変える',
    '順応性のある、融通のきく＝adaptable。', f'''
<g transform="translate(300 86)">
  <path d="M-46 30q-26-24-10-48 14-22 44-24 32-2 46 22 16 26-10 50-34 20-70 0z" class="teal o"/></g>
<g transform="translate(150 260)">
  <path d="M-88-78h176v156h-176z" fill="#e8ddc9" class="o"/>
  <path d="M-54-46h108v92h-108z" fill="#fffaf1" class="o"/>
  <path d="M-48-40h96v80h-96z" class="teal o"/></g>
<g transform="translate(450 260)">
  <path d="M-88-78h176v156h-176z" fill="#e8ddc9" class="o"/>
  <circle r="52" fill="#fffaf1" class="o"/>
  <circle r="46" class="teal o"/></g>
{arc(258, 108, 176, 156, 40, MUTED, True, 4)}
{arc(342, 108, 424, 156, 40, MUTED, True, 4)}
{tick(150, 356, 0.6)}{tick(450, 356, 0.6)}''', arrow=True)

finish(__file__)
