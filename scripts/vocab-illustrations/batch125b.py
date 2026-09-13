# -*- coding: utf-8 -*-
"""第125回の描き直し。labourer は袋が顔にかぶさって別の物に見えた。肩に担がせる。"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))

add('labourer', '工事現場で重いセメント袋を肩に担いで運ぶ肉体労働者', f'''
<path d="M0 0h600v290H0z" fill="#dceaf4"/>
<path d="M0 290h600v110H0z" fill="#c8b8a0"/>
<path d="M0 290h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="#a89880" class="o">
  <path d="M400 290v-150h150v150z"/>
  <g fill="none" stroke="#8f7f68" stroke-width="4"><path d="M400 190h150M400 240h150M475 140v150"/></g>
</g>
<g stroke="#8f9aa6" stroke-width="9" fill="none">
  <path d="M420 140v-60h110v60M420 80l110 60M530 80L420 140"/>
</g>
<g transform="translate(220 290)">
  <path d="M-12-8l-28 34M12-8l30 30" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-26-78q26-14 52 0l-8 72h-36z" fill="{TONES['gold'][0]}" class="o"/>
  <path d="M-24-72l-24 40" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <path d="M22-74l30-26" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cx="0" cy="-108" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <circle cx="-8" cy="-104" r="2.2" fill="{INK}"/><circle cx="8" cy="-104" r="2.2" fill="{INK}"/>
  <path d="M-7-92h14" fill="none" stroke="{INK}" stroke-width="2"/>
  <path d="M-27-118q9-24 27-22 18 2 24 22z" class="gold o"/>
  <path d="M-32-118h64v8h-64z" class="goldd o"/>
</g>
<g transform="translate(330 128) rotate(-12)">
  <path d="M-70-30q70-24 140 0 12 40-16 54-58 14-110 0-22-16-14-54z" fill="#d9c9a8" class="o"/>
  <g fill="none" stroke="#b8a878" stroke-width="3"><path d="M-58 4q58 16 116 0"/></g>
  <rect x="-34" y="-16" width="68" height="16" rx="8" fill="{MUTED}"/>
</g>
<path d="M246 214l50-58" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
<g fill="{TONES['blue'][0]}"><path d="M172 214q9 10 9 17t-9 8-9-8 9-17z"/><path d="M160 250q8 9 8 15t-8 7-8-7 8-15z"/></g>
<g fill="{TONES['gold'][0]}" class="o"><path d="M60 290q0-44 52-44t52 44z"/></g>
<g fill="{MUTED}" opacity="0.4"><ellipse cx="220" cy="294" rx="60" ry="10"/></g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet2.html', 5))
