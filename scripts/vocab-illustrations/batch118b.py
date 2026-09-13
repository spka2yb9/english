# -*- coding: utf-8 -*-
"""第118回の描き直し。頭が二重になった wolf、たてがみが出なかった lion、
背景に沈んだ swan、小さすぎた mosquito。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))
GR = '#dfe8d8'
def grass(y=306):
    return (f'<path d="M0 {y}h600v{400-y}H0z" fill="{GR}"/><path d="M0 {y}h600" stroke="{INK}" stroke-width="2.5" fill="none"/>')

add('mosquito', '細い脚と針のような口を持つ蚊が大きく描かれている', f'''
<g transform="translate(300 330) rotate(-6)">
  <path d="M-250 26q-12-28 18-36l400-24q34-4 38 20t-32 28l-400 26q-14 2-24-14z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g transform="translate(300 170) rotate(16)">
  <ellipse cx="70" rx="100" ry="30" fill="#5b4a3c" class="o"/>
  <g fill="#3b3025">
    <path d="M20-26q12 52 0 52zM70-30q12 60 0 60zM120-26q12 52 0 52z"/>
  </g>
  <ellipse cx="-46" rx="40" ry="34" fill="#5b4a3c" class="o"/>
  <circle cx="-58" cy="-10" r="9" fill="{INK}"/>
  <path d="M-74 14l-88 82" stroke="#5b4a3c" stroke-width="9" stroke-linecap="round" fill="none"/>
  <g fill="#fffefd" stroke="{INK}" stroke-width="2.5" opacity="0.85">
    <ellipse cx="46" cy="-46" rx="100" ry="26" transform="rotate(-16 46 -46)"/>
    <ellipse cx="80" cy="-34" rx="86" ry="20" transform="rotate(-6 80 -34)"/>
  </g>
  <g stroke="#5b4a3c" stroke-width="5" stroke-linecap="round" fill="none">
    <path d="M0 26l-46 96M50 30l-8 106M104 24l60 100M0-26l-46-76M50-30l-8-86M104-24l60-80"/>
  </g>
</g>''', ground=False)

add('swan', '首がS字に曲がった白いハクチョウが水に浮かんでいる', f'''
<path d="M0 276h600v124H0z" fill="#9fc4dd"/>
<path d="M0 276h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="#7fb0ce" stroke-width="5">
  <path d="M40 316h130M330 340h150M120 366h190"/>
</g>
<g transform="translate(310 246)">
  <path d="M-140 34q-24-76 60-92 96-18 172 22 44 22 22 48-44 26-152 26-86 0-102-4z" fill="#fffefd" stroke="{INK}" stroke-width="3.5"/>
  <g fill="none" stroke="#d6dde4" stroke-width="4">
    <path d="M-70 6q60-26 140-6M-50 26q70-22 150-2"/>
  </g>
  <path d="M-44-52q34-46 0-78-34-32-78-4-32 20-16 48 16-26 44-14 30 14 18 48z" fill="#fffefd" stroke="{INK}" stroke-width="3.5"/>
  <circle cx="-126" cy="-116" r="7" fill="{INK}"/>
  <path d="M-140-110l-38 10 38 12z" class="gold o"/>
  <path d="M-142-118q-10-8 0-12" stroke="{INK}" stroke-width="3" fill="none"/>
</g>''', ground=False)

add('wolf', 'とがった耳と長い口を持つオオカミが遠ぼえしている', f'''
{grass(308)}
<g transform="translate(310 240)">
  <path d="M-70 0q0-42 60-42h74q56 0 56 46v46q0 20-20 20h-150q-20 0-20-20z" fill="#8f9aa6" class="o"/>
  <path d="M136 18q46-8 66-52 22 42-14 80-26 26-52 6z" fill="#8f9aa6" class="o"/>
  <path d="M-70 0q-30-24-28-58 2-32 34-34 28-2 34 22l12 46z" fill="#a6b0bb" class="o"/>
  <path d="M-92-58l-14-42 38 20zM-52-70l14-40 18 36z" fill="#a6b0bb" class="o"/>
  <path d="M-88-56l-6-22 18 10zM-50-66l8-20 10 18z" fill="#c8d0d8"/>
  <path d="M-70-38q-46-14-64-40 26-24 66-6z" fill="#a6b0bb" class="o"/>
  <circle cx="-70" cy="-44" r="6" fill="{INK}"/>
  <path d="M-130-72l-14-6 12-8z" fill="{INK}"/>
  <path d="M-118-58q-16 4-2 10" stroke="{INK}" stroke-width="3" fill="none"/>
  <g stroke="#6f7b88" stroke-width="14" stroke-linecap="round" fill="none">
    <path d="M-34 96v30M14 96v30M64 96v30M104 92v34"/>
  </g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M132 116q-18-10-16-26M100 142q-22-8-22-26"/>
</g>''', ground=False)

add('lion', 'ふさふさのたてがみに囲まれた顔を持つライオン', f'''
{grass(310)}
<g transform="translate(310 232)">
  <path d="M-20 12q0-38 60-38h56q48 0 48 42v46q0 18-18 18h-128q-18 0-18-18z" fill="#d8b878" class="o"/>
  <path d="M144 28q40 12 42 50-34 14-46-20z" fill="#d8b878" class="o"/>
  <path d="M182 70q22 6 18 26-22 4-24-16z" fill="#8b6437" class="o"/>
''' + '<g fill="#a0764a" stroke="' + INK + '" stroke-width="2.5">' + ''.join(
  f'<ellipse cx="{-60+92*math.cos(i*math.pi/7):.0f}" cy="{-26+92*math.sin(i*math.pi/7):.0f}" rx="26" ry="20" transform="rotate({i*180/7:.0f} {-60+92*math.cos(i*math.pi/7):.0f} {-26+92*math.sin(i*math.pi/7):.0f})"/>'
  for i in range(14)) + '</g>' + f'''
  <circle cx="-60" cy="-26" r="66" fill="#e0c48a" class="o"/>
  <circle cx="-82" cy="-42" r="7" fill="{INK}"/><circle cx="-38" cy="-42" r="7" fill="{INK}"/>
  <path d="M-60-16l-14 12h28z" fill="{INK}"/>
  <path d="M-60-4q-16 16-30 4M-60-4q16 16 30 4" fill="none" stroke="{INK}" stroke-width="3.5"/>
  <g stroke="{INK}" stroke-width="2" fill="none">
    <path d="M-92-8l-24-8M-92 0l-24 4M-28-8l24-8M-28 0l24 4"/>
  </g>
  <g stroke="#c9a464" stroke-width="14" stroke-linecap="round" fill="none">
    <path d="M4 100v30M52 100v30M100 100v30M140 96v34"/>
  </g>
</g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet2.html', 4))
