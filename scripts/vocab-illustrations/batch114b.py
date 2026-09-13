# -*- coding: utf-8 -*-
"""第114回の描き直し。銃の台尻の接続、木陰の人影、フードの人物を描き起こす。"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib import *

W = []

W.append(emit('rifle', 'ライフル銃が壁の銃架に横向きに掛けられている', f'''
<g>
  <rect x="50" y="66" width="500" height="248" rx="10" fill="#f3ece1" stroke="{INK}" stroke-width="2.5"/>
  <path d="M50 148h500M50 232h500M180 66v82M330 148v84M470 66v82" stroke="{MUTED}" stroke-width="2" fill="none"/>
  <g transform="translate(300 190)">
    <path d="M-206-6h150v12h-150z" fill="{INK}"/>
    <path d="M-206-7h150v5h-150z" fill="{MUTED}"/>
    <path d="M-222-8h16v16h-16z" fill="{MUTED}" stroke="{INK}" stroke-width="2"/>
    <path d="M-56-16h96v34h-96z" fill="#8b6437" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>
    <path d="M40-16q30 0 46 16 20 24 24 52 2 14-10 18-14 4-26-8-16-16-24-38-6-18-10-40z" fill="#a0764a" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>
    <path d="M-4 18v22q0 12 12 12h22" fill="none" stroke="{INK}" stroke-width="3.5"/>
    <path d="M4 24v16" stroke="{INK}" stroke-width="4.5" stroke-linecap="round"/>
    <path d="M-8 18l-24 40q-4 8 4 8h20z" fill="#8b6437" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>
    <rect x="-40" y="-42" width="84" height="18" rx="9" fill="{INK}"/>
    <path d="M-28-24v10M32-24v10" stroke="{INK}" stroke-width="5"/>
    <circle cx="-34" cy="-33" r="7" fill="{TONES['blue'][1]}" stroke="{INK}" stroke-width="2"/>
  </g>
  <path d="M116 206q0 30 28 30h20q28 0 28-30" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <path d="M382 206q0 30 28 30h20q28 0 28-30" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
</g>''', ground=False))

W.append(emit('guerrilla', '森の木の陰から二人の兵がのぞき、道を通る軍用車をうかがっている', f'''
<path d="M0 244h600v62H0z" fill="#d9d2c4"/>
<path d="M0 244h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M40 276h58M138 276h58M236 276h58M334 276h58M432 276h58M530 276h50" stroke="#fffefd" stroke-width="6"/>
<g>
  <rect x="366" y="180" width="146" height="64" rx="8" fill="{TONES['green'][2]}" class="o"/>
  <path d="M366 180h-62l-24 32v32h86z" fill="{TONES['green'][0]}" class="o"/>
  <rect x="312" y="194" width="38" height="24" rx="4" fill="{TONES['blue'][1]}" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="336" cy="244" r="24" fill="{INK}"/><circle cx="336" cy="244" r="10" fill="{MUTED}"/>
  <circle cx="468" cy="244" r="24" fill="{INK}"/><circle cx="468" cy="244" r="10" fill="{MUTED}"/>
</g>
<g>
  <path d="M96 306V190" stroke="#7a5b3c" stroke-width="30" stroke-linecap="round"/>
  <path d="M240 306V206" stroke="#7a5b3c" stroke-width="24" stroke-linecap="round"/>
</g>
<g stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
  <path d="M116 306q-4-64 20-64 22 0 22 64z" fill="#46583f"/>
  <circle cx="140" cy="222" r="20" fill="{SKIN}"/>
  <path d="M120 220q0-24 20-24t20 24q-8-8-20-8t-20 8z" fill="#46583f"/>
  <path d="M132 224h16" stroke="{INK}" stroke-width="3" fill="none"/>
  <path d="M158 258l50-16" stroke="#46583f" stroke-width="13" stroke-linecap="round" fill="none"/>
  <path d="M196 232h56v9h-56z" fill="{INK}" stroke="none"/>
  <path d="M252 236l14-4v9l-14 2z" fill="{MUTED}" stroke="none"/>
</g>
<g stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
  <path d="M254 306q-4-52 17-52 19 0 19 52z" fill="#3f5039"/>
  <circle cx="272" cy="238" r="17" fill="{SKIN}"/>
  <path d="M255 236q0-20 17-20t17 20q-7-7-17-7t-17 7z" fill="#3f5039"/>
  <path d="M266 240h13" stroke="{INK}" stroke-width="3" fill="none"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="2.5" stroke-dasharray="7 8" stroke-linecap="round">
  <path d="M164 216l138 2"/>
</g>
<g fill="{TONES['green'][1]}" stroke="{INK}" stroke-width="2.5">
  <path d="M96 190q-56-6-56-46 0-34 56-30 56-4 56 30 0 40-56 46z"/>
  <path d="M240 206q-46-6-46-38 0-28 46-24 46-4 46 24 0 32-46 38z"/>
</g>''', ground=False))

W.append(emit('terrorist', 'フードをかぶった人影が建物のわきに鞄を置いて足早に立ち去ろうとしている', f'''
{building(478, 306, 1.05, 'blue')}
<g>
  <rect x="244" y="234" width="118" height="72" rx="10" fill="#5b4a3c" class="o"/>
  <path d="M272 234v-18q0-12 12-12h38q12 0 12 12v18" fill="none" stroke="{INK}" stroke-width="4.5"/>
  <path d="M244 262h118" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="303" cy="282" r="13" class="coral o"/>
  <path d="M303 269v-9M292 291l-11 9M314 291l11 9M290 282h-12M328 282h-12" stroke="{TONES['coral'][2]}" stroke-width="3.5" stroke-linecap="round" fill="none"/>
</g>
<g stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
  <path d="M132 306l-24-34 30-14 18 30z" fill="#2c333d"/>
  <path d="M196 306l14-40-30-12-16 36z" fill="#2c333d"/>
  <path d="M124 250q-16-64 8-88 12-12 30-12t30 12q24 24 8 88z" fill="#3b4450"/>
  <path d="M136 168q-8-34 10-48 9-7 20-7t20 7q18 14 10 48-16-12-30-12t-30 12z" fill="#2c333d"/>
  <path d="M148 168q14-11 28 0 2 14-14 14t-14-14z" fill="{MUTED}" stroke="none"/>
  <path d="M190 208l44 28" stroke="#3b4450" stroke-width="16" stroke-linecap="round" fill="none"/>
  <path d="M124 214l-40 20" stroke="#3b4450" stroke-width="16" stroke-linecap="round" fill="none"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 9" stroke-linecap="round" marker-end="url(#ar)">
  <path d="M84 268l-46 22"/>
</g>''', ground=True, arrow=True))

print(sheet(W, '/tmp/vocab-sheet2.html', 3))
