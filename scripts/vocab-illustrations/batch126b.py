# -*- coding: utf-8 -*-
"""第126回の描き直し。spur は馬と乗り手が重なって読めなかった。拍車そのものを主役にする。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))

add('spur', 'かかとの拍車を馬の腹に当てて、一気に速く走らせる', f'''
<path d="M0 0h600v290H0z" fill="#dceaf4"/>
<path d="M0 290h600v110H0z" fill="#dfe8d8"/>
<path d="M0 290h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(210 250) scale(0.62)">
  <path d="M-120 0q-10-52 40-62h100q46 6 56 48-40 24-104 24-76 0-92-10z" fill="#a0764a" class="o"/>
  <path d="M92-52q40-38 58-66 22 16 8 58l-24 42z" fill="#a0764a" class="o"/>
  <path d="M146-116q-8-32 6-34 12 8 6 34zM168-122q10-28 20-22 4 10-8 28z" fill="#a0764a" class="o"/>
  <path d="M152-82l28 8-28 10z" fill="#8b6437" class="o"/>
  <circle cx="140" cy="-98" r="4" fill="{INK}"/>
  <path d="M-120 0q-44-16-54-56 44 6 62 42z" fill="#6b4c28" class="o"/>
  <g stroke="#8b6437" stroke-width="13" stroke-linecap="round" fill="none">
    <path d="M-70 14l-50 34M-26 18l4 52M40 16l46 36M76 12l-8 54"/>
  </g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M60 170h50M40 210h40M70 250h50"/>
</g>
<g class="a" marker-end="url(#ar)" stroke-width="5"><path d="M300 190h90"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M240 240q100 40 170 20"/></g>
<g transform="translate(450 290)">
  <path d="M-44-160h56v130l60 26q10 4 10 14h-126z" fill="#5b4a3c" class="o"/>
  <path d="M-44-160h56v24h-56z" fill="#7a6450"/>
  <path d="M-46 10h128v-14H-46z" fill="{INK}"/>
  <g transform="translate(-58 -22)">
    <path d="M0-8h22v16H0z" fill="#b8bfc8" class="o"/>
    <circle cx="-22" r="20" fill="none" stroke="#b8bfc8" stroke-width="7"/>
    <g fill="#b8bfc8" stroke="{INK}" stroke-width="1.5">
''' + ''.join(f'<rect x="-25" y="-32" width="6" height="14" rx="3" transform="rotate({i*45} -22 0)"/>' for i in range(8)) + f'''
    </g>
    <circle cx="-22" r="5" fill="{INK}"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M330 350l60-40"/></g>''', arrow=True, ground=False)

print(sheet(W, '/tmp/vocab-sheet2.html', 5))
