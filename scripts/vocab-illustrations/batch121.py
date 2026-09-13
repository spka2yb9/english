# -*- coding: utf-8 -*-
"""第121回。家まわりの設備・書類・様子を表す形容詞。形容詞は反対の場面を左右に並べて見せる。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))
BRN='#8b6437'
def table(y=300):
    return (f'<path d="M40 {y}h520v20H40z" fill="#c9a464" class="o"/>'
            f'<path d="M80 {y+20}v60M520 {y+20}v60" stroke="#a0764a" stroke-width="14" stroke-linecap="round" fill="none"/>')
def split():
    """左右を比べる語のための仕切り線。"""
    return f'<path d="M300 20v360" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9" fill="none"/>'
def finger(d, w=34):
    return (f'<path d="{d}" fill="none" stroke="{SKINL}" stroke-width="{w+5}" stroke-linecap="round"/>'
            f'<path d="{d}" fill="none" stroke="{SKIN}" stroke-width="{w}" stroke-linecap="round"/>')

# --- 家の設備 ---------------------------------------------------------------
add('faucet', '流しの上の蛇口から水が出ている', f'''
<path d="M0 0h600v400H0z" fill="#e8eef2"/>
<g fill="none" stroke="#cfd8e0" stroke-width="2.5">
''' + ''.join(f'<path d="M0 {40+i*44}h600"/>' for i in range(4)) + ''.join(f'<path d="M{50+i*100} 0v190"/>' for i in range(6)) + f'''
</g>
<g transform="translate(300 300)">
  <path d="M-180-40h360v90q0 20-24 20h-312q-24 0-24-20z" fill="#c8d0d8" class="o"/>
  <path d="M-150-30h300v70q0 14-20 14h-260q-20 0-20-14z" fill="#e0e6ea" class="o"/>
  <circle cy="30" r="16" fill="#9aa5b0" class="o"/>
</g>
<g transform="translate(300 190)">
  <path d="M-14-70h28v40h-28z" fill="#b8bfc8" class="o"/>
  <path d="M-14-70q0-40 60-40h50v26h-40q-42 0-42 32z" fill="#c8d0d8" class="o"/>
  <path d="M-46-24h64q10 0 10 12t-10 12h-64q-10 0-10-12t10-12z" fill="#9aa5b0" class="o"/>
  <path d="M-70-30q-20-14-20-30h30q0 16-10 30z" fill="#b8bfc8" class="o"/>
</g>
<g fill="{TONES['blue'][1]}" stroke="{TONES['blue'][0]}" stroke-width="2">
  <path d="M286 194h28v106h-28z"/>
</g>
<g fill="{TONES['blue'][0]}"><circle cx="278" cy="290" r="5"/><circle cx="324" cy="278" r="4"/></g>''', ground=False)

add('countertop', '台所の調理台の広い天板の上に道具が並んでいる', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<g transform="translate(300 250)">
  <path d="M-280 0h560v26h-560z" fill="#5a6270" class="o"/>
  <path d="M-280 26h560v130h-560z" fill="#c9a464" class="o"/>
  <g fill="none" stroke="#a0764a" stroke-width="3"><path d="M-100 26v130M100 26v130"/></g>
  <g fill="#8b6437"><circle cx="-60" cy="60" r="8"/><circle cx="60" cy="60" r="8"/></g>
</g>
<g transform="translate(180 234)">
  <path d="M-40-30h80v30h-80z" fill="#fffdf6" class="o"/>
  <path d="M-30-30q0-24 30-24t30 24" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g transform="translate(320 232)">
  <path d="M-46-24h92l-8 24h-76z" fill="#9aa5b0" class="o"/>
  <path d="M-46-24q0-16 46-16t46 16z" fill="#b8bfc8" class="o"/>
</g>
<g transform="translate(450 222) rotate(-12)">
  <path d="M-56-6h96q22 0 22 8t-22 8h-96z" fill="#dde3e8" class="o"/>
  <path d="M-96-7h44v14h-44q-8 0-8-7t8-7z" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 160v70"/></g>''', arrow=True, ground=False)

add('dishwasher', '食器洗い機を開けて中に皿を並べている', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<g transform="translate(280 200)">
  <path d="M-130-160h260v300h-260z" fill="#c8d0d8" class="o"/>
  <path d="M-110-140h220v230h-220z" fill="#8f9aa6" class="o"/>
  <g fill="#e0e6ea">
''' + ''.join(f'<rect x="{-96+i*30}" y="-120" width="20" height="70" rx="10"/>' for i in range(7)) + f'''
  </g>
  <g fill="#e0e6ea">
''' + ''.join(f'<circle cx="{-80+i*40}" cy="20" r="22"/>' for i in range(5)) + f'''
  </g>
  <path d="M-130 100h260v40h-260z" fill="#b8bfc8" class="o"/>
  <g fill="{INK}"><circle cx="-70" cy="120" r="7"/><circle cx="-40" cy="120" r="7"/></g>
</g>
<g fill="{TONES['blue'][1]}" opacity="0.6"><circle cx="240" cy="140" r="18"/><circle cx="300" cy="120" r="14"/><circle cx="340" cy="150" r="16"/></g>
<path d="M150 340h360v20H150z" fill="#c9a464" class="o"/>''', ground=False)

add('microwave', '電子レンジの中で皿が回りながら温まっている', f'''
{table(340)}
<g transform="translate(290 240)">
  <path d="M-180-90h360v170h-360z" fill="#5a6270" class="o"/>
  <path d="M-160-70h230v130h-230z" fill="#2c333d" class="o"/>
  <g fill="none" stroke="#4a5560" stroke-width="2">
''' + ''.join(f'<path d="M{-156+i*20} -70v130"/>' for i in range(12)) + ''.join(f'<path d="M-160 {-64+i*20}h230"/>' for i in range(7)) + f'''
  </g>
  <g transform="translate(-46 26)">
    <ellipse rx="66" ry="18" fill="#e0e6ea" class="o"/>
    <path d="M-40-24h80v16q0 8-40 8t-40-8z" fill="#fde39a" class="o"/>
  </g>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
    <path d="M-70-16q12-18 0-34M-46-22q12-18 0-34M-22-16q12-18 0-34"/>
  </g>
  <path d="M90-60h72v50H90z" fill="#1c2530" class="o"/>
  <g fill="{TONES['green'][0]}"><rect x="98" y="-46" width="10" height="20"/><rect x="114" y="-46" width="10" height="20"/><rect x="134" y="-46" width="10" height="20"/></g>
  <g fill="#8f9aa6"><circle cx="126" cy="26" r="26" class="o"/></g>
  <path d="M126 26v-18" stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none"/>
</g>''', ground=False)

add('dustbin', 'ふたのついたごみ箱にごみを捨てている', f'''
{table(360)}
<g transform="translate(280 330)">
  <path d="M-70-140h140l-16 140q-2 14-54 14t-54-14z" fill="#6f7b88" class="o"/>
  <g fill="none" stroke="#4a5560" stroke-width="4">
    <path d="M-64-100h128M-58-56h116M-52-14h104"/>
  </g>
  <path d="M-82-152h164v14h-164z" fill="#8f9aa6" class="o"/>
  <path d="M-82-152q0-16 82-16t82 16z" fill="#9aa5b0" class="o"/>
  <rect x="-14" y="-186" width="28" height="18" rx="9" fill="{INK}"/>
</g>
<g transform="translate(420 180) rotate(24)">
  <path d="M-40-30q40-24 80 0 8 40-20 60-40 10-62-16-8-26 2-44z" fill="#e8e2d6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-20-10h44M-14 16h34"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M400 240q-40 30-70 50"/></g>''', arrow=True, ground=False)

add('jug', '取っ手と注ぎ口のついた水差しから水を注いでいる', f'''
{table(330)}
<g transform="translate(240 250) rotate(28)">
  <path d="M-56-70h112l-14 130q-2 14-42 14t-42-14z" fill="{TONES['blue'][1]}" class="o"/>
  <path d="M-56-70h112v-14h-112z" fill="{TONES['blue'][0]}" class="o"/>
  <path d="M56-70l34-16-8 22-26 10z" fill="{TONES['blue'][1]}" class="o"/>
  <path d="M-56-44q-40 0-40 34t40 34" fill="none" stroke="{TONES['blue'][0]}" stroke-width="12"/>
  <path d="M-46-30h92l-10 84q-2 10-36 10t-36-10z" fill="{TONES['blue'][0]}" opacity="0.5"/>
</g>
<path d="M320 216q30 40 26 84" fill="none" stroke="{TONES['blue'][0]}" stroke-width="14" stroke-linecap="round"/>
<g transform="translate(400 300)">
  <path d="M-40-70h80l-8 70q-2 10-32 10t-32-10z" fill="#e8f0f6" class="o"/>
  <path d="M-34-24h68l-6 24q-2 8-28 8t-28-8z" fill="{TONES['blue'][1]}"/>
</g>''', ground=False)

add('doorway', 'ドアのない戸口の枠を人がくぐろうとしている', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<g fill="none" stroke="#d6cfc0" stroke-width="3">
''' + ''.join(f'<path d="M{40+i*80} 0v400"/>' for i in range(7)) + f'''
</g>
<g transform="translate(300 200)">
  <path d="M-140-160h280v340h-280z" fill="{BRN}" class="o"/>
  <path d="M-108-130h216v310h-216z" fill="#4a4436"/>
  <path d="M-108-130h216v310h-216z" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-140-160h280v26h-280z" fill="#a0764a" class="o"/>
</g>
{person(300, 380, 1.0, 1, 'coral', 'blue', 'walk', 'bob', 'smile', 'walk')}
<g class="a" marker-end="url(#ar)"><path d="M480 60l-100 40"/></g>
<g class="a" marker-end="url(#ar)"><path d="M120 60l100 40"/></g>''', arrow=True, ground=False)

add('driveway', '家の前から道路まで車を乗り入れる私道が伸びている', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
<path d="M0 200h600v200H0z" fill="#dfe8d8"/>
<path d="M0 200h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M0 340h600v60H0z" fill="#8f9aa6" class="o"/>
<path d="M230 210h140l90 130H140z" fill="#c8d0d8" class="o"/>
<g fill="none" stroke="#9aa5b0" stroke-width="3"><path d="M258 250h84M232 296h136"/></g>
{building(300, 210, 0.9, 'coral')}
<g transform="translate(300 300) scale(0.8)">
  <path d="M-90 30h180v-40q0-14-14-14h-152q-14 0-14 14z" fill="{TONES['teal'][0]}" class="o"/>
  <path d="M-64-24h128l-22-32h-84z" fill="#dceaf4" class="o"/>
  <circle cx="-56" cy="30" r="18" fill="{INK}"/><circle cx="56" cy="30" r="18" fill="{INK}"/>
</g>
{tree(80, 340, 0.9)}
<g class="a" marker-end="url(#ar)"><path d="M480 240l-90 90"/></g>''', ground=False)

add('hood', 'パーカーのフードをかぶっている', f'''
<g transform="translate(290 240)">
  <path d="M-150 160q-20-190 150-190t150 190z" class="teal o"/>
  <path d="M-126-30q0-130 126-130T126-30q-30 40-126 40T-126-30z" class="teald o"/>
  <path d="M-96-24q0-104 96-104t96 104q-40-44-96-44t-96 44z" fill="{TONES['teal'][1]}"/>
  <ellipse cy="-6" rx="82" ry="72" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="-30" cy="-16" r="6" fill="{INK}"/><circle cx="30" cy="-16" r="6" fill="{INK}"/>
  <path d="M-24 26q24 20 48 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <path d="M-40 66q-20 40-14 94M40 66q20 40 14 94" fill="none" stroke="#fffdf6" stroke-width="7" stroke-linecap="round"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M520 120l-90 40"/></g>''', arrow=True)

add('magnet', 'U字の磁石が鉄のくぎを引き寄せている', f'''
{table(320)}
<g transform="translate(220 240)">
  <path d="M-70 40V-10q0-70 70-70t70 70v50h-46V-10q0-24-24-24t-24 24v50z" class="coral o"/>
  <path d="M-70 40h46v34h-46zM46 40h46v34H46z" fill="#c8d0d8" class="o"/>
</g>
<g fill="#9aa5b0" class="o">
''' + ''.join(f'<g transform="translate({330+i*36} {250+(i%3)*36-30}) rotate({-14+i*10})"><path d="M-30-4h50l14 4-14 4h-50z"/><circle cx="-32" r="7"/></g>' for i in range(5)) + f'''
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7">
  <path d="M320 264q60-30 130-20M320 220q60 20 130 10"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M420 320l-90-20"/></g>''', arrow=True, ground=False)

add('aisle', 'スーパーの棚と棚の間の通路を歩いている', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<path d="M180 140h240l90 260H90z" fill="#c8d0d8" class="o"/>
<g fill="none" stroke="#9aa5b0" stroke-width="3"><path d="M200 200h200M170 270h260M130 350h340"/></g>
<g>
  <path d="M0 60h180v340H0z" fill="#dde3e8" class="o"/>
  <path d="M600 60H420v340h180z" fill="#dde3e8" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
''' + ''.join(f'<path d="M0 {110+i*70}h180M420 {110+i*70}h180"/>' for i in range(4)) + f'''
  </g>
  <g class="o">
''' + ''.join(f'<rect x="{16+ (i%4)*40}" y="{80+(i//4)*70}" width="26" height="26" class="{["coralp","tealp","goldp","violetp"][i%4]}"/>' for i in range(16)) + ''.join(f'<rect x="{436+ (i%4)*40}" y="{80+(i//4)*70}" width="26" height="26" class="{["tealp","goldp","violetp","coralp"][i%4]}"/>' for i in range(16)) + f'''
  </g>
</g>
{person(300, 380, 0.85, 1, 'coral', 'blue', 'walk', 'bun', 'smile', 'walk')}
<g class="a" marker-end="url(#ar)"><path d="M240 120h120"/></g>''', arrow=True, ground=False)

add('motorway', '何車線もある高速道路を車が走っている', f'''
<path d="M0 0h600v170H0z" fill="#dceaf4"/>
<path d="M0 170h600v230H0z" fill="#dfe8d8"/>
<path d="M0 170h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M0 400l150-190h300l150 190z" fill="#6f7b88" class="o"/>
<g fill="none" stroke="#fffefd" stroke-width="5" stroke-dasharray="30 26">
  <path d="M256 210L160 400M344 210l96 190"/>
</g>
<path d="M290 210L250 400M310 210l40 190" fill="none" stroke="{TONES['gold'][0]}" stroke-width="4"/>
<g transform="translate(190 340) scale(0.7)">
  <path d="M-90 30h180v-40q0-14-14-14h-152q-14 0-14 14z" class="coral o"/>
  <path d="M-64-24h128l-22-32h-84z" fill="#dceaf4" class="o"/>
  <circle cx="-56" cy="30" r="18" fill="{INK}"/><circle cx="56" cy="30" r="18" fill="{INK}"/>
</g>
<g transform="translate(410 300) scale(0.55)">
  <path d="M-90 30h180v-40q0-14-14-14h-152q-14 0-14 14z" class="teal o"/>
  <path d="M-64-24h128l-22-32h-84z" fill="#dceaf4" class="o"/>
  <circle cx="-56" cy="30" r="18" fill="{INK}"/><circle cx="56" cy="30" r="18" fill="{INK}"/>
</g>
<g transform="translate(500 150)">
  <path d="M-70-50h140v70h-140z" class="green o"/>
  <g fill="#fffefd"><rect x="-50" y="-34" width="70" height="10" rx="5"/><rect x="-50" y="-14" width="50" height="10" rx="5"/></g>
  <path d="M0 20v40" stroke="{MUTED}" stroke-width="8" fill="none"/>
</g>''', ground=False)

add('boarding', '搭乗券を見せて飛行機に乗り込んでいる', f'''
<path d="M0 0h600v400H0z" fill="#e8eef2"/>
{table(340)}
<g transform="translate(430 190)">
  <path d="M-160 60h300q40 0 40 40t-40 40h-300z" fill="#dde3e8" class="o"/>
  <path d="M-160 60v80h-30v-80z" fill="#c8d0d8" class="o"/>
  <path d="M140 60q40-70 100-70v210q-60 0-100-60z" fill="#c8d0d8" class="o"/>
  <g fill="{TONES['blue'][1]}" class="o">
''' + ''.join(f'<circle cx="{-120+i*50}" cy="100" r="14"/>' for i in range(5)) + f'''
  </g>
</g>
{person(180, 340, 1.0, 1, 'coral', 'blue', 'give', 'bob', 'smile')}
<g transform="translate(260 268) rotate(-14)">
  <path d="M-44-28h88v56h-44l-44-14z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}"><rect x="-34" y="-16" width="46" height="8" rx="4"/><rect x="-34" y="0" width="34" height="8" rx="4"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="4 4"><path d="M14-28v56"/></g>
</g>
<g transform="translate(120 260)">
  <path d="M-30-40h60v70q0 12-30 12t-30-12z" class="teal o"/>
  <path d="M-8-40v-16h16v16z" fill="{INK}"/>
</g>''', ground=False)

add('baggage', '空港のベルトコンベアを荷物が流れてくる', f'''
<path d="M0 0h600v400H0z" fill="#e8eef2"/>
<g transform="translate(300 300)">
  <path d="M-280 0h560v50h-560z" fill="#4a5560" class="o"/>
  <path d="M-280 0q0-24 30-24h500q30 0 30 24z" fill="#6f7b88" class="o"/>
  <g fill="#8f9aa6"><circle cx="-200" cy="24" r="12"/><circle cx="-60" cy="24" r="12"/><circle cx="80" cy="24" r="12"/><circle cx="220" cy="24" r="12"/></g>
</g>
<g transform="translate(150 236)">
  <path d="M-50-44h100v88h-100z" class="teal o"/>
  <path d="M-8-44v-18h16v18z" fill="{INK}"/>
  <path d="M-50 0h100" fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"/>
</g>
<g transform="translate(300 246)">
  <path d="M-56-34h112v68h-112z" class="coral o"/>
  <path d="M-24-34q0-20 24-20t24 20" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
{box(450, 250, 90, 62, 20, 'gold')}
<g class="a" marker-end="url(#ar)"><path d="M120 180h180"/></g>''', arrow=True, ground=False)

add('conductor', 'タクトを振ってオーケストラを指揮している', f'''
{table(360)}
{person(300, 330, 1.2, 1, 'violet', 'blue', 'up', 'short', 'smile')}
<path d="M270 200l-40-46" stroke="#c9a464" stroke-width="6" stroke-linecap="round" fill="none"/>
<g transform="translate(300 350)">
  <path d="M-70-30h140v40h-140z" fill="#8b6437" class="o"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="4">
''' + ''.join(f'<g transform="translate({80+i*130} {230}) scale(0.5)"><path d="M-30 60V-30q0-16 60-30v20q-40 12-40 26v74z" fill="{TONES["gold"][0]}" stroke="{INK}" stroke-width="5"/><ellipse cx="-48" cy="60" rx="26" ry="18" fill="{TONES["gold"][0]}"/></g>' for i in range(2)) + f'''
</g>
<g fill="{INK}">
  <g transform="translate(120 130)"><ellipse rx="12" ry="9" transform="rotate(-20)"/><path d="M10-4v-40h4v40z"/></g>
  <g transform="translate(470 150)"><ellipse rx="12" ry="9" transform="rotate(-20)"/><path d="M10-4v-40h4v40z"/></g>
  <g transform="translate(400 90)"><ellipse rx="12" ry="9" transform="rotate(-20)"/><path d="M10-4v-40h4v40z"/></g>
</g>''', ground=False)

# --- 書類と仕事 --------------------------------------------------------------
add('form', '名前や住所の欄に記入する申込用紙', f'''
{table(340)}
<g transform="translate(280 200)">
  <path d="M-160-150h320v300h-320z" class="paper"/>
  <rect x="-130" y="-124" width="150" height="16" rx="8" fill="{INK}"/>
  <g>
''' + ''.join(f'<g><rect x="-130" y="{-80+i*50}" width="60" height="10" rx="5" fill="{MUTED}"/><path d="M-56 {-64+i*50}h186" stroke="{MUTED}" stroke-width="3"/></g>' for i in range(5)) + f'''
  </g>
  <path d="M-50-70q30-16 50 0t46-6" fill="none" stroke="{TONES['blue'][0]}" stroke-width="3.5"/>
  <path d="M-50-20q26-14 44 2t50-8" fill="none" stroke="{TONES['blue'][0]}" stroke-width="3.5"/>
</g>
<g transform="translate(450 250) rotate(34)">
  <path d="M0-90l14 30v90h-28V-60z" class="blue o"/>
  <path d="M-14 30h28v40l-14 24-14-24z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-6 70h12l-6 24z" fill="{INK}"/>
</g>''', ground=False)

add('handwriting', '手書きの文字が紙の上に並んでいる', f'''
{table(350)}
<g transform="translate(290 190)">
  <path d="M-180-140h360v290h-360z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2"><path d="M-150-100h300M-150-50h300M-150 0h300M-150 50h300M-150 100h300"/></g>
  <g fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round">
''' + ''.join(f'<path d="M{-150+i*54} -108q10 22 0 14t14-6 6 8 12-16 8 14 14-4"/>' for i in range(6)) + f'''
''' + ''.join(f'<path d="M{-150+i*54} -58q12 20 0 12t16-4 4 6 14-14 6 12 12-2"/>' for i in range(5)) + f'''
''' + ''.join(f'<path d="M{-150+i*54} -8q10 22 0 14t14-6 6 8 12-16 8 14 14-4"/>' for i in range(6)) + f'''
''' + ''.join(f'<path d="M{-150+i*54} 42q12 20 0 12t16-4 4 6 14-14 6 12 12-2"/>' for i in range(4)) + f'''
  </g>
</g>
<g transform="translate(452 300) rotate(28)">
  <path d="M0-80l12 26v80h-24V-54z" class="teal o"/>
  <path d="M-12 26h24v36l-12 22-12-22z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>''', ground=False)

add('blog', '画面に日付つきの記事が上から新しい順に並んでいる', f'''
{table(360)}
<g transform="translate(300 190)">
  <path d="M-220-150h440v270h-440z" fill="#3b4450" class="o"/>
  <path d="M-200-130h400v230h-400z" fill="#fffefd"/>
  <path d="M-200-130h400v34h-400z" class="teal"/>
  <g fill="#fffefd"><circle cx="-180" cy="-113" r="7"/><rect x="-160" y="-119" width="80" height="12" rx="6"/></g>
''' + ''.join(f'''<g transform="translate(0 {-76+i*58})">
    <rect x="-186" y="-8" width="46" height="10" rx="5" fill="{TONES['coral'][0]}"/>
    <rect x="-130" y="-12" width="150" height="14" rx="7" fill="{INK}"/>
    <rect x="-130" y="10" width="{300-i*40}" height="8" rx="4" fill="{MUTED}"/>
  </g>''' for i in range(3)) + f'''
  <path d="M-60 130h120v20h-120z" fill="#5a6270" class="o"/>
</g>''', ground=False)

add('internship', '学生が職場で先輩に教わりながら実務を経験している', f'''
{table(340)}
<g transform="translate(300 268)">
  <path d="M-200-20h400v20h-400z" fill="#c9a464" class="o"/>
</g>
{sit(200, 320, 0.95, 1, 'coral', 'blue', 'bob', 'smile', 'lap')}
{person(400, 320, 1.0, -1, 'teal', 'violet', 'point', 'short', 'smile')}
{chair(200, 320, 0.9, 'gold', 1)}
<g transform="translate(280 220)">
  <path d="M-60-40h120v70h-120z" fill="#3b4450" class="o"/>
  <path d="M-52-32h104v54h-104z" fill="#dceaf4"/>
  <g fill="{MUTED}"><rect x="-40" y="-22" width="60" height="7" rx="3.5"/><rect x="-40" y="-8" width="76" height="7" rx="3.5"/><rect x="-40" y="6" width="46" height="7" rx="3.5"/></g>
  <path d="M-30 30h60v10h-60z" fill="#5a6270"/>
</g>
<g transform="translate(160 210)">
  <path d="M-34-24h68v48h-34l-34-10z" fill="#fffefd" class="o"/>
  <g fill="{TONES['coral'][0]}"><rect x="-24" y="-12" width="36" height="7" rx="3.5"/></g>
</g>''', ground=False)

add('interviewer', '面接する側が質問し、応募者が答えている', f'''
{table(360)}
<g transform="translate(300 280)">
  <path d="M-220-20h440v22h-440z" fill="#c9a464" class="o"/>
  <path d="M-180 2v60M180 2v60" stroke="#a0764a" stroke-width="14" stroke-linecap="round" fill="none"/>
</g>
{sit(180, 340, 0.95, 1, 'teal', 'blue', 'short', 'smile', 'lap')}
{sit(420, 340, 0.95, -1, 'coral', 'violet', 'bob', 'neutral', 'lap')}
<g transform="translate(190 246) rotate(-8)">
  <path d="M-40-26h80v52h-80z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}"><rect x="-30" y="-16" width="52" height="7" rx="3.5"/><rect x="-30" y="-2" width="40" height="7" rx="3.5"/><rect x="-30" y="12" width="48" height="7" rx="3.5"/></g>
</g>
<g transform="translate(300 150)">
  <path d="M-56-40h112q14 0 14 14v44q0 14-14 14h-80l-26 20v-20q-14 0-14-14v-44q0-14 14-14z" fill="#fffefd" class="o"/>
  <path d="M-14-24q0-16 16-16t16 16-16 14v10" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <circle cx="2" cy="16" r="3.5" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 210v-60"/></g>''', arrow=True, ground=False)

add('diet', '毎日の食事の内容が皿の上に並んでいる', f'''
{table(330)}
<g transform="translate(300 250)">
  <circle r="130" fill="#fffdf6" class="o"/>
  <circle r="112" fill="none" stroke="{MUTED}" stroke-width="2.5"/>
  <path d="M0 0L0-112A112 112 0 0 1 97 56z" class="greenp o"/>
  <path d="M0 0L97 56A112 112 0 0 1-97 56z" class="goldp o"/>
  <path d="M0 0L-97 56A112 112 0 0 1 0-112z" class="coralp o"/>
  <g class="o">
    <circle cx="46" cy="-46" r="16" class="green"/><circle cx="16" cy="-64" r="13" class="green"/>
    <ellipse cx="0" cy="60" rx="30" ry="18" class="gold"/>
    <path d="M-56 6q30-24 44 4-26 26-44-4z" class="coral"/>
  </g>
</g>
<g transform="translate(500 280)">
  <path d="M-8-70h16v100h-16z" fill="#c8d0d8" class="o"/>
  <path d="M-24-70q0 24 8 24M0-70v24M24-70q0 24-8 24" fill="none" stroke="#c8d0d8" stroke-width="6" stroke-linecap="round"/>
</g>''', ground=False)

add('exercise', '腕立て伏せをして体を動かしている', f'''
{table(360)}
<g transform="translate(300 300)">
  <path d="M-190 40h380v18h-380z" class="tealp o"/>
  <g transform="translate(-20 0)">
    <path d="M-90 30q0-20 20-30l90-40 60 20q20 8 20 26" fill="none" stroke="{TONES['coral'][0]}" stroke-width="26" stroke-linecap="round"/>
    <circle cx="106" cy="-32" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <path d="M84-52q6-24 26-22 18 2 20 22z" fill="{HAIR}"/>
    <circle cx="116" cy="-34" r="3" fill="{INK}"/>
    <path d="M104-20q12 8 20 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
    <path d="M76-16v46M-70 4v26" fill="none" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
    <path d="M-88 30h30M62 30h30" fill="none" stroke="{TONES['blue'][0]}" stroke-width="14" stroke-linecap="round"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M420 220v50"/></g>
<g class="a" marker-end="url(#ar)"><path d="M420 270v-50"/></g>
<g fill="{TONES['blue'][0]}"><path d="M420 150q8 8 8 13t-8 5-8-5 8-13z"/></g>''', arrow=True, ground=False)

# --- 動作 -------------------------------------------------------------------
add('clutch', 'かばんを胸にぎゅっと抱きしめている', f'''
{person(300, 340, 1.25, 1, 'teal', 'blue', 'hold', 'bob', 'sad')}
<g transform="translate(300 240)">
  <path d="M-56-34h112v68h-112z" class="coral o"/>
  <path d="M-24-34q0-20 24-20t24 20" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M-56 0h112" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"/>
</g>
<path d="M244 246q40-26 90-4" fill="none" stroke="{SKIN}" stroke-width="18" stroke-linecap="round"/>
<path d="M244 246q40-26 90-4" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M200 200l-24-16M420 196l24-18M186 250h-28"/>
</g>''')

add('condense', '長い文章がぎゅっと短くまとめられている', f'''
{split()}
<g transform="translate(150 200)">
  <path d="M-110-150h220v300h-220z" class="paper"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-88" y="{-124+i*30}" width="{176-(i%3)*30}" height="9" rx="4.5"/>' for i in range(9)) + f'''
  </g>
</g>
<g transform="translate(450 200)">
  <path d="M-110-70h220v140h-220z" class="paper"/>
  <g fill="{INK}">
    <rect x="-88" y="-46" width="176" height="11" rx="5.5"/>
    <rect x="-88" y="-18" width="150" height="11" rx="5.5"/>
    <rect x="-88" y="10" width="166" height="11" rx="5.5"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>
<g class="a" marker-end="url(#ar)"><path d="M420 110l-40 40M480 110l40 40M420 290l-40-40M480 290l40-40"/></g>''', arrow=True, ground=False)

add('dehydrate', 'みずみずしい果物が乾いてしなびていく', f'''
{split()}
{table(330)}
<g transform="translate(150 240)">
  <circle r="76" class="coral o"/>
  <path d="M0-76q-16-30 6-40 20 6 10 40z" class="green o"/>
  <ellipse cx="-26" cy="-26" rx="20" ry="14" fill="#fffefd" opacity="0.6" transform="rotate(-30 -26 -26)"/>
</g>
<g fill="{TONES['blue'][0]}">
  <path d="M240 190q9 10 9 17t-9 8-9-8 9-17z"/><path d="M254 240q8 9 8 15t-8 7-8-7 8-15z"/>
</g>
<g transform="translate(450 260)">
  <path d="M-50-40q40-30 76-4 22 40-10 62-46 18-72-14-8-28 6-44z" class="corald o"/>
  <g fill="none" stroke="#8b3a2c" stroke-width="4">
    <path d="M-30-24q14 30-2 54M6-34q10 40-6 64M36-20q6 30-8 48"/>
  </g>
  <path d="M-4-38q-10-24 4-32 14 6 6 32z" class="greend o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('marinate', '肉をたれに漬け込んで冷蔵庫に入れる', f'''
{table(340)}
<g transform="translate(300 250)">
  <path d="M-130-70h260v130q0 16-130 16t-130-16z" fill="#e8f0f6" class="o" opacity="0.85"/>
  <path d="M-124-20h248v40q0 14-124 14t-124-14z" fill="#a8763c"/>
  <path d="M-124-20h248" stroke="#8b5a2c" stroke-width="3" fill="none"/>
  <g class="o">
    <path d="M-80-30q40-26 76 0 12 34-24 44-50 8-62-18 0-18 10-26z" fill="#c4604a"/>
    <path d="M20-14q34-20 62 4 8 28-24 34-44 4-46-18 0-14 8-20z" fill="#c4604a"/>
  </g>
  <path d="M-130-70h260v-14h-260z" fill="#c8d0d8" class="o"/>
  <g fill="{TONES['green'][0]}"><ellipse cx="-40" cy="14" rx="14" ry="7"/><ellipse cx="66" cy="20" rx="12" ry="6"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M120 190q60-40 180-40t180 40"/></g>
<g class="a" marker-end="url(#ar)"><path d="M300 120v40"/></g>''', arrow=True, ground=False)

add('obstruct', '倒れた木が道をふさいで車が通れない', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v170H0z" fill="#dfe8d8"/>
<path d="M0 230h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M0 400l140-170h320l140 170z" fill="#8f9aa6" class="o"/>
<g fill="none" stroke="#fffefd" stroke-width="5" stroke-dasharray="26 24"><path d="M300 230v170"/></g>
<g transform="translate(300 300) rotate(-8)">
  <path d="M-260-26h520v52h-520z" fill="{BRN}" class="o"/>
  <g fill="none" stroke="#6b4c28" stroke-width="4"><path d="M-240-10h480M-240 10h480"/></g>
  <g class="greenp o">
    <circle cx="-240" cy="-56" r="46"/><circle cx="-170" cy="-40" r="36"/><circle cx="250" cy="-50" r="42"/>
  </g>
</g>
<g transform="translate(300 190) scale(0.62)">
  <path d="M-90 30h180v-40q0-14-14-14h-152q-14 0-14 14z" class="coral o"/>
  <path d="M-64-24h128l-22-32h-84z" fill="#dceaf4" class="o"/>
  <circle cx="-56" cy="30" r="18" fill="{INK}"/><circle cx="56" cy="30" r="18" fill="{INK}"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round">
  <path d="M470 130l50 50M520 130l-50 50"/>
</g>''', ground=False)

add('pound', 'こぶしでドアをどんどんと強く叩いている', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<g transform="translate(360 200)">
  <path d="M-120-170h240v340h-240z" fill="{BRN}" class="o"/>
  <path d="M-92-142h184v130h-184zM-92 12h184v130h-184z" fill="#a0764a" class="o"/>
  <circle cx="-96" cy="10" r="12" fill="{TONES['gold'][0]}" class="o"/>
</g>
<g transform="translate(200 190)">
  <ellipse rx="54" ry="46" fill="{SKINL}"/>
  <ellipse rx="50" ry="42" fill="{SKIN}"/>
  <g fill="none" stroke="{SKINL}" stroke-width="3">
    <path d="M-30-14h60M-30 4h60M-24 22h48"/>
  </g>
  <path d="M-50 10q-40 6-60 34" stroke="{SKINL}" stroke-width="34" stroke-linecap="round" fill="none"/>
  <path d="M-50 10q-40 6-60 34" stroke="{SKIN}" stroke-width="29" stroke-linecap="round" fill="none"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M264 130q20-16 40 0M256 190h40M264 250q20 16 40 0"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 100l50 50"/></g>''', arrow=True, ground=False)

add('transplant', '苗を掘り上げて別の場所に植え替えている', f'''
<path d="M0 0h600v250H0z" fill="#dceaf4"/>
<path d="M0 250h600v150H0z" fill="#c9a464"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M0 238h600v14H0z" fill="#dfe8d8"/>
<g transform="translate(140 260)">
  <path d="M-56 0q0 40 56 40t56-40z" fill="#8b6437" class="o"/>
  <g fill="none" stroke="#6b4c28" stroke-width="3"><path d="M-30 6q10 26 0 30M20 8q-8 24 2 28"/></g>
</g>
<g transform="translate(340 200)">
  <path d="M-40 60q0-30 40-30t40 30q-10 26-40 26t-40-26z" fill="#8b6437" class="o"/>
  <path d="M-6 30V-40h12v70z" class="greend o"/>
  <path d="M-6-10q-50-20-40-50 40 4 40 50zM6-40q50-20 60 10-40 14-60-10z" class="greenp o"/>
  <g fill="none" stroke="#6b4c28" stroke-width="4" stroke-linecap="round">
    <path d="M0 60q-20 26-30 30M0 60q20 26 30 30M0 60v34"/>
  </g>
</g>
<g transform="translate(520 280)">
  <path d="M-56-16q0 40 56 40t56-40z" fill="#6b4c28" class="o"/>
  <path d="M-56-16q10-16 56-16t56 16z" fill="#8b6437"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M200 150q120-70 260 60"/></g>''', arrow=True, ground=False)

add('hop', '片足でぴょんと跳んでいる', f'''
{table(360)}
<g transform="translate(230 300)">
  <g opacity="0.35">
    {person(0, 60, 1.0, 1, 'teal', 'blue', 'stand', 'cap', 'smile')}
  </g>
</g>
<g transform="translate(390 250)">
  <path d="M-12-8l-30 40" fill="none" stroke="{TONES['blue'][2]}" stroke-width="11" stroke-linecap="round"/>
  <path d="M12-8l6 20-20 24" fill="none" stroke="{TONES['blue'][2]}" stroke-width="11" stroke-linecap="round"/>
  <path d="M-25-78q25-13 50 0l-8 72h-34z" fill="{TONES['teal'][0]}" class="o"/>
  <path d="M-22-70l-26-35-5-17M22-70l26-35 5-17" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
  <circle cx="0" cy="-108" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['cap']}" fill="{TONES['blue'][0]}" stroke="{TONES['blue'][0]}" stroke-width="2"/>
  <circle cx="-8" cy="-104" r="2.2" fill="{INK}"/><circle cx="8" cy="-104" r="2.2" fill="{INK}"/>
  <path d="M-8-94q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 250q70-90 150-40"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3"><ellipse cx="230" cy="362" rx="40" ry="9"/></g>''', arrow=True, ground=False)

add('giggle', '口をおさえて高い声でくすくす笑っている', f'''
{face(240, 200, 100, 'grin')}
{hand(250, 260, 1)}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M370 120q16-16 32 0M370 170q16-16 32 0M370 220q16-16 32 0"/>
</g>
<g transform="translate(470 170)">
  <path d="M-40-30h80q10 0 10 10v40q0 10-10 10h-56l-20 16v-16q-14 0-14-10v-40q0-10 10-10z" fill="#fffefd" class="o"/>
  <g fill="{TONES['gold'][0]}"><circle cx="-16" cy="0" r="6"/><circle cx="4" cy="0" r="6"/><circle cx="24" cy="0" r="6"/></g>
</g>''')

add('furnish', '空だった部屋に家具を入れて整えている', f'''
{split()}
<g transform="translate(150 200)">
  <path d="M-110-140h220v280h-220z" fill="#f0eee6" class="o"/>
  <path d="M-110 90h220v50h-220z" fill="#c9a464" class="o"/>
  <path d="M-60-90h60v70h-60z" fill="#dceaf4" class="o"/>
</g>
<g transform="translate(450 200)">
  <path d="M-110-140h220v280h-220z" fill="#f0eee6" class="o"/>
  <path d="M-110 90h220v50h-220z" fill="#c9a464" class="o"/>
  <path d="M-64-90h60v70h-60z" fill="#dceaf4" class="o"/>
  <g transform="translate(-30 66)">
    <path d="M-66-40h132v40h-132z" class="coral o"/>
    <path d="M-66-40q0-24 20-24h92q20 0 20 24z" class="coralp o"/>
    <path d="M-66-6h132v10h-132z" class="corald o"/>
  </g>
  <g transform="translate(66 74)">
    <path d="M-30-8h60v8h-60z" fill="{BRN}" class="o"/>
    <path d="M-24 0v16M24 0v16" stroke="#a0764a" stroke-width="6" fill="none"/>
  </g>
  <g transform="translate(60 -50)">
    <path d="M-24-14h48l8 30h-64z" class="goldp o"/>
    <path d="M0 16v40" stroke="{INK}" stroke-width="4" fill="none"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('expel', '生徒が校門の外へ追い出されている', f'''
{table(360)}
<g>
  <path d="M0 60h240v300H0z" fill="#e8e2d6" class="o"/>
  <g class="tealp o">
''' + ''.join(f'<rect x="{24+ (i%3)*72}" y="{100+(i//3)*90}" width="48" height="52"/>' for i in range(9)) + f'''
  </g>
  <path d="M240 120h30v240h-30z" fill="{BRN}" class="o"/>
</g>
{person(400, 360, 1.05, -1, 'coral', 'blue', 'walk', 'bob', 'sad', 'walk')}
{person(200, 360, 0.95, 1, 'teal', 'violet', 'point', 'short', 'neutral')}
<g class="a" marker-end="url(#ar)" stroke-width="6"><path d="M300 200h200"/></g>''', ground=False)

# --- 様子を表す形容詞 ---------------------------------------------------------
add('barren', '草も木も生えない、石だらけの荒れた土地', f'''
<path d="M0 0h600v220H0z" fill="#e6d9bc"/>
<path d="M0 220h600v180H0z" fill="#cbb98f" class="o"/>
<g fill="none" stroke="#b0a077" stroke-width="4">
  <path d="M40 270q80-20 160 0t170-10M60 330q100-16 200 6t250-14"/>
</g>
<g fill="#a89878" class="o">
  <ellipse cx="140" cy="300" rx="30" ry="18"/><ellipse cx="380" cy="266" rx="22" ry="14"/><ellipse cx="480" cy="340" rx="34" ry="20"/>
</g>
<g>
  <path d="M280 260V150h12v110z" fill="#8b7a5c" class="o"/>
  <g stroke="#8b7a5c" stroke-width="7" stroke-linecap="round" fill="none">
    <path d="M286 200l-40-40M286 176l44-34M286 220l34 20"/>
  </g>
</g>
<g fill="none" stroke="#c9b892" stroke-width="3">
  <path d="M60 190q60-14 120 0M340 176q80-16 160 0"/>
</g>
{sun(500, 80, 36)}''', ground=False)

add('fertile', '黒々とした土から作物が勢いよく育っている', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v170H0z" fill="#5b4a3c" class="o"/>
<g fill="none" stroke="#463a2e" stroke-width="4">
  <path d="M0 280h600M0 330h600"/>
</g>
<g>
''' + ''.join(f'''<g transform="translate({70+i*95} 240)">
  <path d="M-7 0v-70h14V0z" class="greend o"/>
  <path d="M-7-40q-50-24-40-56 42 6 40 56zM7-64q50-24 60 4-40 22-60-4z" class="greenp o"/>
  <path d="M-7-14q-44-20-36-46 36 4 36 46z" class="greenp o"/>
  <circle cy="-84" r="18" class="{"coral" if i%2 else "gold"} o"/>
</g>''' for i in range(6)) + f'''
</g>
{sun(510, 70, 34)}''', ground=False)

add('cosy', '小さな部屋で毛布にくるまり暖炉のそばにいる', f'''
<path d="M0 0h600v400H0z" fill="#3f3630"/>
<path d="M0 340h600v60H0z" fill="#6b4c28" class="o"/>
<g transform="translate(440 250)">
  <path d="M-110-130h220v210h-220z" fill="#7a5b3c" class="o"/>
  <path d="M-80-90h160v140h-160z" fill="#2c2420" class="o"/>
  {flame(0, 40, 0.9)}
  <g fill="#8b6437"><path d="M-60 40h120v14h-120z"/></g>
</g>
<g fill="{TONES['gold'][1]}" opacity="0.25"><path d="M330 250l-260 90V160z"/></g>
{sit(180, 340, 1.0, 1, 'coral', 'blue', 'bun', 'smile', 'lap')}
<g transform="translate(180 300)">
  <path d="M-64-40q64-24 128 0 8 50-14 70-50 16-104-2-16-26-10-68z" class="violetp o"/>
  <g fill="none" stroke="{TONES['violet'][0]}" stroke-width="3"><path d="M-50-10h108M-46 16h100"/></g>
</g>
<g transform="translate(280 258)">
  <path d="M-24-16h40v34q0 8-20 8t-20-8z" fill="#fffdf6" class="o"/>
  <path d="M16-8q20 0 20 12t-20 12" fill="none" stroke="{INK}" stroke-width="5"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-linecap="round"><path d="M-12-28q10-14 0-24M6-28q10-14 0-24"/></g>
</g>''', ground=False)

add('dim', '明るい照明とうす暗い照明が並べて示されている', f'''
{split()}
<g transform="translate(150 200)">
  <path d="M0-150v40" stroke="{INK}" stroke-width="5" fill="none"/>
  <path d="M-56-110h112l-20 44h-72z" fill="#c8d0d8" class="o"/>
  <circle cy="-52" r="24" class="gold o"/>
  <g fill="{TONES['gold'][1]}" opacity="0.55"><path d="M0-52l-130 220h260z"/></g>
  <g class="golds"><path d="M-56-40l-24 14M56-40l24 14M0-16v20"/></g>
</g>
<g transform="translate(450 200)">
  <path d="M0-150v40" stroke="{INK}" stroke-width="5" fill="none"/>
  <path d="M-56-110h112l-20 44h-72z" fill="#8f9aa6" class="o"/>
  <circle cy="-52" r="24" fill="#b0a880" class="o"/>
  <g fill="#8f9aa6" opacity="0.3"><path d="M0-52l-70 130h140z"/></g>
</g>
<path d="M300 20v360" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9" fill="none"/>
<path d="M300 0h300v400H300z" fill="#2c333d" opacity="0.55"/>
<g class="a" marker-end="url(#ar)" stroke="#fffefd"><path d="M270 350h60"/></g>''', arrow=True, ground=False)

add('gloomy', '雨の暗い部屋でうつむいて座っている', f'''
<path d="M0 0h600v400H0z" fill="#4a5560"/>
<path d="M0 350h600v50H0z" fill="#3b4450"/>
<g transform="translate(430 180)">
  <path d="M-90-120h180v240h-180z" fill="#5b6a86" class="o"/>
  <path d="M-70-100h140v200h-140z" fill="#6f7f96"/>
  <path d="M0-100v200M-70 0h140" stroke="#4a5560" stroke-width="6" fill="none"/>
  <g fill="none" stroke="#8fa0b6" stroke-width="3" stroke-linecap="round">
''' + ''.join(f'<path d="M{-56+i*22} {-84+(i%3)*40}l-10 30"/>' for i in range(6)) + f'''
  </g>
</g>
{sit(180, 350, 1.05, 1, 'violet', 'blue', 'bob', 'sad', 'down')}
<g transform="translate(180 290)"><path d="M-30 0q30 20 60 0" fill="none" stroke="{MUTED}" stroke-width="3"/></g>
{chair(180, 350, 1.0, 'gold', 1)}
<g fill="{MUTED}" opacity="0.35"><ellipse cx="300" cy="200" rx="300" ry="220"/></g>''', ground=False)

add('conspicuous', '灰色の人の列にひとりだけ真っ赤な人が立って目立つ', f'''
{table(360)}
<g opacity="0.85">
''' + ''.join(person(80+i*90, 340, 0.8, 1, 'blue', 'blue', 'stand', 'short', 'neutral') for i in [0,1,3,4,5]) + f'''
</g>
<g fill="{MUTED}" opacity="0.45">
''' + ''.join(f'<rect x="{40+i*90}" y="200" width="80" height="150"/>' for i in [0,1,3,4,5]) + f'''
</g>
{person(350, 340, 1.05, 1, 'coral', 'coral', 'up', 'bun', 'smile')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M470 110l-90 60"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round" opacity="0.8">
  <circle cx="350" cy="250" r="130" stroke-dasharray="12 12"/>
</g>''', ground=False)

add('deafening', '耳をふさぎたくなるほどの大音量が鳴っている', f'''
{table(360)}
<g transform="translate(160 240)">
  <path d="M-70-120h140v240h-140z" fill="#3b4450" class="o"/>
  <circle cy="-50" r="46" fill="#5a6270" class="o"/><circle cy="-50" r="20" fill="#2c333d"/>
  <circle cy="56" r="30" fill="#5a6270" class="o"/><circle cy="56" r="13" fill="#2c333d"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round">
  <path d="M250 180q40 60 0 120M300 150q66 90 0 180M350 120q92 120 0 240"/>
</g>
{person(500, 360, 1.05, -1, 'teal', 'blue', 'up', 'bob', 'sad')}
<g fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5">
  <ellipse cx="470" cy="238" rx="18" ry="22"/><ellipse cx="530" cy="238" rx="18" ry="22"/>
</g>''', ground=False)

add('hectic', '机の上が書類と電話であふれ、目が回るほど忙しい', f'''
{table(340)}
{sit(300, 340, 1.05, 1, 'coral', 'blue', 'bun', 'sad', 'up')}
<g transform="translate(300 300)">
  <path d="M-240-30h480v30h-480z" fill="#c9a464" class="o"/>
</g>
<g>
''' + ''.join(f'<g transform="translate({110+i*30} {250-(i%4)*14}) rotate({-20+i*9})"><path d="M-30-40h60v80h-60z" class="paper"/><g fill="{MUTED}"><rect x="-20" y="-26" width="40" height="6" rx="3"/><rect x="-20" y="-12" width="30" height="6" rx="3"/></g></g>' for i in range(4)) + f'''
</g>
<g>
''' + ''.join(f'<g transform="translate({420+i*28} {248-(i%3)*16}) rotate({14-i*10})"><path d="M-30-40h60v80h-60z" class="paper"/><g fill="{MUTED}"><rect x="-20" y="-26" width="40" height="6" rx="3"/><rect x="-20" y="-12" width="34" height="6" rx="3"/></g></g>' for i in range(4)) + f'''
</g>
<g transform="translate(300 200)">
  <path d="M-40 20q-20-60 40-60t40 60z" fill="{INK}"/>
  <path d="M-46 20h92v14h-92z" fill="{INK}"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M200 130q20-16 40 0M370 120q20-16 40 0M250 90h30M420 160h30"/>
</g>''', ground=False)

add('jealous', '仲よくしている二人を横から悔しそうに見ている', f'''
{table(360)}
{person(180, 350, 1.0, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(280, 350, 1.0, -1, 'coral', 'violet', 'stand', 'bob', 'smile')}
<g fill="{TONES['coral'][0]}">
  <path d="M230 200q-16-22 0-30 16-8 20 10 4-18 20-10 16 8 0 30l-20 22z"/>
</g>
{person(470, 350, 1.0, -1, 'gold', 'green', 'stand', 'bun', 'sad')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M440 216q-20-14 0-26M416 250l-24-10M420 190l-24 4"/>
</g>
<g fill="{TONES['green'][0]}" opacity="0.5"><ellipse cx="470" cy="242" rx="34" ry="26"/></g>
<g class="a" marker-end="url(#ar)"><path d="M430 250l-100-20"/></g>''', arrow=True, ground=False)

add('selfish', 'お菓子を全部自分のほうへ抱え込んで分けない', f'''
{table(320)}
{person(400, 320, 1.1, -1, 'coral', 'blue', 'hold', 'short', 'neutral')}
<g transform="translate(360 250)">
  <g class="gold o">
''' + ''.join(f'<circle cx="{-40+ (i%4)*28}" cy="{(i//4)*26}" r="17"/>' for i in range(8)) + f'''
  </g>
  <path d="M-80 40q60-40 130 0" fill="none" stroke="{SKIN}" stroke-width="20" stroke-linecap="round"/>
  <path d="M-80 40q60-40 130 0" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
</g>
{person(150, 320, 1.0, 1, 'teal', 'violet', 'reach', 'bob', 'sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M240 240l40 40M280 240l-40 40"/>
</g>''', ground=False)

add('luminous', '暗い中で文字盤が自分から光っている時計', f'''
<path d="M0 0h600v400H0z" fill="#232b3a"/>
<g transform="translate(300 200)">
  <g fill="{TONES['green'][1]}" opacity="0.18"><circle r="170"/></g>
  <g fill="{TONES['green'][1]}" opacity="0.25"><circle r="130"/></g>
  <circle r="104" fill="#1b222e" stroke="#5a6270" stroke-width="8"/>
  <circle r="92" fill="#232b3a"/>
  <g fill="#9fe8b0">
''' + ''.join(f'<rect x="-5" y="-84" width="10" height="20" rx="5" transform="rotate({i*30})"/>' for i in range(12)) + f'''
  </g>
  <path d="M0 0v-62" stroke="#9fe8b0" stroke-width="8" stroke-linecap="round" fill="none"/>
  <path d="M0 0l44 30" stroke="#9fe8b0" stroke-width="7" stroke-linecap="round" fill="none"/>
  <circle r="8" fill="#9fe8b0"/>
</g>
<g fill="none" stroke="#9fe8b0" stroke-width="4" stroke-linecap="round" opacity="0.6">
  <path d="M470 90l30-26M500 200h40M470 310l30 26M130 90l-30-26M100 200H60M130 310l-30 26"/>
</g>''', ground=False)

add('brisk', '背筋を伸ばして足早にきびきび歩いている', f'''
{table(360)}
{person(330, 360, 1.2, 1, 'teal', 'blue', 'walk', 'cap', 'smile', 'walk')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M110 200h90M90 250h70M120 300h84"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M440 220q16-18 0-32M470 230q24-26 0-52"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3"><ellipse cx="300" cy="366" rx="46" ry="8"/></g>
<g class="a" marker-end="url(#ar)" stroke-width="5"><path d="M200 130h240"/></g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
