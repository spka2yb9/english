# -*- coding: utf-8 -*-
"""第128回の描き直し。dislodge(歯列が読めない)、dwindle(水が見えない)、quirk(癖が伝わらない)。"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))
def table(y=300):
    return (f'<path d="M40 {y}h520v20H40z" fill="#c9a464" class="o"/>'
            f'<path d="M80 {y+20}v60M520 {y+20}v60" stroke="#a0764a" stroke-width="14" stroke-linecap="round" fill="none"/>')

# 歯を並べても口に見えない。石が車輪にはさまり、棒でこじり出す場面に替える。
add('dislodge', '靴底の溝にはさまった小石を棒でこじって取り除く', f'''
{table(370)}
<g transform="translate(280 250) rotate(-14)">
  <path d="M-170 40q-20-50 10-66 50-28 100-56 40-22 80-6 50 20 90 44 30 18 24 48-10 26-70 26z" fill="#5b4a3c" class="o"/>
  <path d="M-176 40h316q8 24-16 26h-292q-18-4-8-26z" fill="#3d3229" class="o"/>
  <g fill="#2c241d">
''' + ''.join(f'<rect x="{-150+i*38}" y="42" width="24" height="22" rx="5"/>' for i in range(9)) + f'''
  </g>
  <g fill="none" stroke="#4a3d33" stroke-width="4">
    <path d="M-60-20q40-24 90-10M-20-52q40-20 80-4"/>
  </g>
</g>
<g transform="translate(310 316) rotate(-14)">
  <path d="M-22 0l26-20 24 16-8 26-30 4z" fill="{MUTED}" class="o"/>
</g>
<g transform="translate(430 150) rotate(52)">
  <path d="M-6-10h150v20H-6z" fill="#c9a464" class="o"/>
  <path d="M-30-12l24 2v20l-24 2z" fill="#8f9aa6" class="o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M200 130l-90 60"/></g>
<g fill="{MUTED}" class="o"><path d="M120 210l26 8-12 22-26-10z"/></g>''', ground=False)

# 水位が背景と同化した。水を濃い色にし、外枠を太くして残量をはっきり出す。
add('dwindle', 'たっぷりあった水が日ごとに減っていく', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g>
''' + ''.join(f'''<g transform="translate({90+i*105} 290)">
  <path d="M-46-140h92v140q0 18-46 18t-46-18z" fill="#fffefd" class="o"/>
  <path d="M-41 {-124+i*30}h82v{124-i*30}q0 14-41 14t-41-14z" fill="{TONES['blue'][0]}"/>
  <path d="M-41 {-124+i*30}h82" stroke="{TONES['blue'][2]}" stroke-width="4" fill="none"/>
  <path d="M-46-140h92v140q0 18-46 18t-46-18z" fill="none" stroke="{INK}" stroke-width="3"/>
</g>''' for i in range(5)) + f'''
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M80 90h440"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M40 370h520"/></g>''', ground=False)

# 「その人だけの癖」は一度きりでは伝わらない。同じ動作を三度くり返して見せる。
add('quirk', '座る前に必ず三回ノックする、その人だけの決まった癖', f'''
{table(380)}
<g transform="translate(420 200)">
  <path d="M-90-170h180v340h-180z" fill="#8b6437" class="o"/>
  <path d="M-66-146h132v292h-132z" fill="#a0764a" class="o"/>
  <circle cx="46" cy="10" r="12" class="gold o"/>
</g>
{person(200, 380, 1.15, 1, 'violet', 'blue', 'reach', 'bun', 'smile')}
<g>
  <ellipse cx="292" cy="220" rx="30" ry="24" fill="{SKINL}"/>
  <ellipse cx="292" cy="220" rx="26" ry="20" fill="{SKIN}"/>
  <g fill="none" stroke="{SKINL}" stroke-width="2.5"><path d="M274 214h36M274 226h36"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M330 190q26 30 0 60M356 168q40 52 0 104M382 146q54 74 0 148"/>
</g>
<g transform="translate(150 150)">
  <path d="M-56-34h112q12 0 12 12v38q0 12-12 12h-72l-22 16v-16q-18 0-18-12v-38q0-12 12-12z" fill="#fffefd" class="o"/>
  <g fill="{TONES['coral'][0]}"><circle cx="-24" y="0" r="8"/><circle cx="0" r="8"/><circle cx="24" r="8"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M150 200v40"/></g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet2.html', 5))
