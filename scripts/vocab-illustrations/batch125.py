# -*- coding: utf-8 -*-
"""第125回。店・水回り・re- の動詞。re- の語は「一度目 → 二度目」を左右に置く。"""
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
    return f'<path d="M300 20v360" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9" fill="none"/>'
def coin(x, y, r=20):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" class="gold o"/>'
            f'<circle cx="{x}" cy="{y}" r="{r*0.62}" fill="none" stroke="{TONES["gold"][2]}" stroke-width="2.5"/>')
def cross(x, y, s=1):
    return (f'<g fill="none" stroke="{TONES["coral"][0]}" stroke-width="{9*s}" stroke-linecap="round">'
            f'<path d="M{x-26*s} {y-26*s}l{52*s} {52*s}M{x+26*s} {y-26*s}l{-52*s} {52*s}"/></g>')
def tick(x, y, s=1):
    return (f'<g fill="none" stroke="{TONES["green"][0]}" stroke-width="{9*s}" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M{x-30*s} {y}l{22*s} {24*s} {42*s}-{52*s}"/></g>')
def head(x, y, r=22, shirt='teal', hair='short'):
    return (f'<g transform="translate({x} {y})">'
            f'<circle r="{r}" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>'
            f'<path d="{HAIRS[hair]}" transform="translate(0 108) scale({r/24:.2f})" fill="{HAIR}"/>'
            f'<circle cx="{-r*0.33:.0f}" cy="{-r*0.17:.0f}" r="2.4" fill="{INK}"/>'
            f'<circle cx="{r*0.33:.0f}" cy="{-r*0.17:.0f}" r="2.4" fill="{INK}"/>'
            f'<path d="M{-r*0.3:.0f} {r*0.35:.0f}q{r*0.3:.0f} {r*0.3:.0f} {r*0.6:.0f} 0" fill="none" stroke="{INK}" stroke-width="2"/>'
            f'<path d="M{-r*1.1:.0f} {r*1.5:.0f}q{r*1.1:.0f}-{r*0.6:.0f} {r*2.2:.0f} 0l-{r*0.3:.0f} {r*1.2:.0f}h-{r*1.6:.0f}z" fill="{TONES[shirt][0]}" class="o"/></g>')
def screen(x, y, w=200, h=140):
    return (f'<g transform="translate({x} {y})">'
            f'<path d="M{-w/2-14} {-h/2-14}h{w+28}v{h+28}h{-w-28}z" fill="#3b4450" class="o"/>'
            f'<path d="M{-w/2} {-h/2}h{w}v{h}h{-w}z" fill="#fffefd"/>'
            f'<path d="M-34 {h/2+14}h68v14h-68z" fill="#5a6270"/></g>')

# --- 店と仕事 ---------------------------------------------------------------
add('inventory', '棚の品を一つずつ数えて在庫を記録する', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(200 200)">
  <path d="M-140-170h280v340h-140z" fill="#e0d6c0" class="o"/>
  <path d="M-140-170h280v340h-280z" fill="#e0d6c0" class="o"/>
  <g fill="none" stroke="{BRN}" stroke-width="6"><path d="M-140-80h280M-140 10h280M-140 100h280"/></g>
  <g class="o">
''' + ''.join(f'<rect x="{-124+ (i%6)*46}" y="{-146+(i//6)*90}" width="34" height="60" class="{["coralp","tealp","goldp","violetp","greenp","bluep"][i%6]}"/>' for i in range(18)) + f'''
  </g>
</g>
{person(470, 340, 1.0, -1, 'teal', 'blue', 'hold', 'bun', 'neutral')}
<g transform="translate(440 250) rotate(10)">
  <path d="M-40-56h80v112h-80z" fill="#fffefd" class="o"/>
  <path d="M-20-56v-12h40v12z" fill="#8f9aa6" class="o"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-28" y="{-38+i*22}" width="{50-(i%2)*14}" height="7" rx="3.5"/>' for i in range(4)) + f'''
  </g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
''' + ''.join(f'<path d="M28 {-36+i*22}l6 7 12-14"/>' for i in range(3)) + f'''
  </g>
</g>''', ground=False)

add('labourer', '工事現場で重い袋を運ぶ肉体労働者', f'''
<path d="M0 0h600v260H0z" fill="#dceaf4"/>
{table(370)}
<path d="M0 300h600v100H0z" fill="#c8b8a0"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="#a89880" class="o">
  <path d="M400 300v-140h140v140z"/>
  <g fill="none" stroke="#8f7f68" stroke-width="4"><path d="M400 200h140M400 250h140M470 160v140"/></g>
</g>
{person(220, 300, 1.2, 1, 'gold', 'blue', 'carry', 'cap', 'neutral', 'walk')}
<g transform="translate(240 180)">
  <path d="M-56-30q56-24 112 0 10 40-16 56-46 12-84 0-20-18-12-56z" fill="#c9a464" class="o"/>
  <g fill="none" stroke="#a0764a" stroke-width="3"><path d="M-46 0q46 16 92 0"/></g>
</g>
<g fill="{TONES['blue'][0]}"><path d="M170 210q9 10 9 17t-9 8-9-8 9-17z"/></g>
<g fill="{TONES['gold'][0]}" class="o"><path d="M60 300q0-40 50-40t50 40z"/></g>''', ground=False)

add('optician', '眼鏡店で度を合わせた眼鏡を選んでいる', f'''
<path d="M0 0h600v400H0z" fill="#e8eef2"/>
{table(370)}
<g transform="translate(150 200)">
  <path d="M-110-140h220v280h-220z" fill="#e0d6c0" class="o"/>
  <g fill="none" stroke="{BRN}" stroke-width="5"><path d="M-110-50h220M-110 40h220"/></g>
  <g>
''' + ''.join(f'''<g transform="translate({-64+ (i%3)*64} {-90+(i//3)*90})">
  <circle cx="-16" r="14" fill="none" stroke="{TONES[["teal","coral","violet","gold","blue","green"][i%6]][0]}" stroke-width="4"/>
  <circle cx="16" r="14" fill="none" stroke="{TONES[["teal","coral","violet","gold","blue","green"][i%6]][0]}" stroke-width="4"/>
  <path d="M-2 0h4M-30-4l-14-8M30-4l14-8" stroke="{TONES[["teal","coral","violet","gold","blue","green"][i%6]][0]}" stroke-width="4" fill="none"/>
</g>''' for i in range(9)) + f'''
  </g>
</g>
{person(400, 370, 1.1, 1, 'coral', 'blue', 'hold', 'bob', 'smile')}
<g transform="translate(400 246)">
  <circle cx="-16" r="14" fill="none" stroke="{INK}" stroke-width="4"/>
  <circle cx="16" r="14" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-2 0h4M-30-4l-12-6M30-4l12-6" stroke="{INK}" stroke-width="4" fill="none"/>
</g>
{person(510, 370, 1.0, -1, 'teal', 'teal', 'reach', 'bun', 'smile')}''', ground=False)

add('narrator', '物語の外から声で話を語る人', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(400 200)">
  <path d="M-170-140h340v280h-340z" fill="#dceaf4" class="o"/>
  {tree(-100, 100, 0.9)}
  <path d="M40 100V20h90v80z" fill="#fffdf6" class="o"/>
  <path d="M28 20L85-24l57 44z" class="coral o"/>
  {sun(120, -90, 26)}
</g>
{person(110, 340, 1.1, 1, 'violet', 'blue', 'point', 'bun', 'smile')}
<g transform="translate(170 200)">
  <path d="M-30-40h90q12 0 12 12v40q0 12-12 12h-60l-20 16v-16q-22 0-22-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}"><rect x="-16" y="-18" width="60" height="8" rx="4"/><rect x="-16" y="-2" width="44" height="8" rx="4"/><rect x="-16" y="14" width="52" height="8" rx="4"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M250 210h60"/></g>''', ground=False)

add('playwright', '劇作家が舞台のせりふを書いている', f'''
<path d="M0 0h600v400H0z" fill="#3b3550"/>
<g transform="translate(420 200)">
  <path d="M-160-120h320v260h-320z" fill="#2b2740" class="o"/>
  <path d="M-160-120h320v40h-320z" class="coral o"/>
  <path d="M-160-80h60v220h-60zM160-80h-60v220h60z" class="corald o"/>
  {person(-40, 130, 0.62, 1, 'gold', 'violet', 'up', 'bun', 'smile')}
  {person(60, 130, 0.62, -1, 'teal', 'blue', 'point', 'short', 'smile')}
  <g fill="{TONES['gold'][1]}" opacity="0.2"><path d="M0-80l-120 220h240z"/></g>
</g>
{person(110, 350, 1.0, 1, 'teal', 'blue', 'think', 'short', 'smile')}
<g transform="translate(150 250) rotate(-8)">
  <path d="M-50-60h100v120h-100z" class="paper"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="{-36+ (i%2)*12}" y="{-44+i*20}" width="{56-(i%2)*20}" height="7" rx="3.5"/>' for i in range(5)) + f'''
  </g>
</g>''', ground=False)

add('monastery', '石造りの修道院で修道士が静かに歩いている', f'''
<path d="M0 0h600v260H0z" fill="#dceaf4"/>
<path d="M0 260h600v140H0z" fill="#c9d8c0"/>
<path d="M0 260h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(320 260)">
  <path d="M-200 0v-160h400V0z" fill="#d6cdba" class="o"/>
  <path d="M-200-160h400v-20h-400z" fill="#c0b6a0"/>
  <g fill="#b8ad98" class="o">
''' + ''.join(f'<path d="M{-160+i*66} 0v-90q0-24 24-24t24 24V0z"/>' for i in range(6)) + f'''
  </g>
  <path d="M-40-180h80v-70q0-20-40-20t-40 20z" fill="#d6cdba" class="o"/>
  <path d="M-8-300h16v46h-16zM-24-284h48v14h-48z" fill="#c9a464" class="o"/>
  <circle cy="-220" r="20" class="bluep o"/>
</g>
{person(190, 330, 0.85, 1, 'violet', 'violet', 'stand', 'bun', 'neutral')}
<g transform="translate(190 246)">
  <path d="M-32 30q0-46 32-46t32 46q-32 16-64 0z" class="violetd o"/>
</g>
{tree(70, 340, 0.9)}
{tree(540, 350, 1.0)}''', ground=False)

# --- 家と水回り --------------------------------------------------------------
add('plumbing', '流しの下の配管を点検している', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<g transform="translate(300 140)">
  <path d="M-200-40h400v50h-400z" fill="#c8d0d8" class="o"/>
  <path d="M-120-30h240v40h-240z" fill="#e0e6ea" class="o"/>
  <path d="M-14-40h28v-60h-28z" fill="#b8bfc8" class="o"/>
  <path d="M-14-100q0-30 40-30h40v22h-32q-26 0-26 20z" fill="#c8d0d8" class="o"/>
</g>
<g fill="none" stroke="#9aa5b0" stroke-width="26" stroke-linecap="round" stroke-linejoin="round">
  <path d="M300 150v70q0 40-40 40t-40 40 40 40h180"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="2.5">
  <path d="M300 150v70q0 40-40 40t-40 40 40 40h180" stroke-width="2.5" fill="none"/>
</g>
<g fill="#7d8894" class="o">
  <rect x="286" y="212" width="28" height="20" rx="4"/><rect x="230" y="290" width="22" height="28" rx="4"/><rect x="410" y="326" width="28" height="22" rx="4"/>
</g>
<g fill="{TONES['blue'][0]}"><path d="M262 288q9 10 9 17t-9 8-9-8 9-17z"/></g>
{person(120, 360, 0.95, 1, 'gold', 'blue', 'reach', 'cap', 'neutral')}
<g transform="translate(180 300) rotate(20)">
  <path d="M-40-8h80v16h-80z" fill="{INK}"/>
  <path d="M40-16h34v32H40z" fill="#8f9aa6" class="o"/>
</g>''', ground=False)

add('patio', '家の裏の石だたみのテラスにいすと机がある', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v170H0z" fill="#c9d8c0"/>
<path d="M0 230h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M120 250h420l60 150H60z" fill="#d6cdba" class="o"/>
<g fill="none" stroke="#b8ad98" stroke-width="3">
  <path d="M104 300h432M84 350h472M240 250l-40 150M380 250l40 150"/>
</g>
<g transform="translate(60 190)">
  <path d="M-60 60v-150h180v150z" fill="#fffdf6" class="o"/>
  <path d="M-20-60h60v50h-60z" class="bluep o"/>
</g>
<g transform="translate(330 320)">
  <ellipse rx="90" ry="26" fill="#c9a464" class="o"/>
  <path d="M-10 26v50M-40 76h60" stroke="#a0764a" stroke-width="10" stroke-linecap="round" fill="none"/>
</g>
{chair(210, 350, 0.9, 'teal', 1)}
{chair(450, 350, 0.9, 'teal', -1)}
<g transform="translate(330 250)">
  <path d="M-6 44V-46h12v90z" fill="{BRN}"/>
  <path d="M-90-46h180q-30-40-90-40t-90 40z" class="coralp o"/>
</g>
{tree(540, 250, 0.8)}''', ground=False)

add('pier', '海に細長く突き出した桟橋', f'''
<path d="M0 0h600v210H0z" fill="#dceaf4"/>
<path d="M0 210h600v190H0z" fill="#7aa8c4"/>
<path d="M0 210h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="#a8c8dd" stroke-width="4"><path d="M40 300h140M420 340h160M60 370h150"/></g>
<g>
  <path d="M120 400v-140h360v40H180v100z" fill="#c9a464" class="o"/>
  <path d="M120 260h400v26H120z" fill="#d9b877" class="o"/>
  <g fill="none" stroke="#a0764a" stroke-width="3">
''' + ''.join(f'<path d="M{140+i*38} 260v26"/>' for i in range(10)) + f'''
  </g>
  <g stroke="#8b6437" stroke-width="14" stroke-linecap="round" fill="none">
''' + ''.join(f'<path d="M{170+i*76} 286v90"/>' for i in range(5)) + f'''
  </g>
  <g stroke="{INK}" stroke-width="5" fill="none">
''' + ''.join(f'<path d="M{160+i*76} 260v-40"/>' for i in range(5)) + f'''
    <path d="M160 224h306"/>
  </g>
</g>
{person(300, 258, 0.7, 1, 'coral', 'blue', 'stand', 'bob', 'smile')}
{sun(510, 80, 32)}''', ground=False)

add('kerb', '車道と歩道の境の一段高い縁石', f'''
<path d="M0 250h600v150H0z" fill="#6f7b88"/>
<g fill="none" stroke="#fffefd" stroke-width="6" stroke-dasharray="34 30"><path d="M0 340h600"/></g>
<path d="M0 210h600v40H0z" fill="#d6cec0" class="o"/>
<path d="M0 246h600v22H0z" fill="#b0a898" class="o"/>
<g fill="none" stroke="#9a9284" stroke-width="3">
''' + ''.join(f'<path d="M{50+i*70} 246v22"/>' for i in range(9)) + f'''
</g>
<g fill="#dfe8d8"><path d="M0 150h600v60H0z"/></g>
<path d="M0 210h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
{person(180, 240, 0.7, 1, 'coral', 'blue', 'stand', 'bob', 'smile')}
<g transform="translate(470 300) scale(0.6)">
  <path d="M-120 40h240v-56q0-20-20-20h-70l-40-40h-70q-20 0-20 20v76z" class="teal o"/>
  <circle cx="-70" cy="40" r="26" fill="{INK}"/><circle cx="70" cy="40" r="26" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M330 130l-40 110"/></g>''', arrow=True, ground=False)

add('sanitation', '下水管が汚水を運び、処理場できれいにする', f'''
<path d="M0 0h600v170H0z" fill="#dceaf4"/>
<path d="M0 170h600v230H0z" fill="#a8845c"/>
<path d="M0 158h600v14H0z" fill="#dfe8d8"/>
<path d="M0 158h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(120 158)">
  <path d="M-60 0v-90h120V0z" fill="#fffdf6" class="o"/>
  <path d="M-70-90L0-134l70 44z" class="coral o"/>
</g>
<path d="M120 170v70h280" fill="none" stroke="#8f9aa6" stroke-width="40" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M120 170v70h280" fill="none" stroke="{INK}" stroke-width="2.5"/>
<g fill="#6b7a5e"><circle cx="200" cy="240" r="9"/><circle cx="270" cy="240" r="7"/><circle cx="330" cy="240" r="8"/></g>
<g transform="translate(470 250)">
  <ellipse rx="100" ry="34" fill="#8f9aa6" class="o"/>
  <path d="M-100 0v70q0 34 100 34t100-34V0z" fill="#8f9aa6" class="o"/>
  <ellipse ry="26" rx="86" fill="{TONES['blue'][1]}" class="o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"><ellipse ry="14" rx="50"/></g>
</g>
{tick(470, 160, 0.8)}''', ground=False)

add('rinse', '洗剤の泡を水でしっかり流し落とす', f'''
<path d="M0 0h600v400H0z" fill="#e8eef2"/>
<g transform="translate(300 320)">
  <path d="M-190-40h380v70q0 16-20 16h-340q-20 0-20-16z" fill="#c8d0d8" class="o"/>
  <path d="M-160-30h320v50q0 12-16 12h-288q-16 0-16-12z" fill="#e0e6ea" class="o"/>
  <circle cy="26" r="14" fill="#9aa5b0" class="o"/>
</g>
<g transform="translate(300 200)">
  <path d="M-14-70h28v40h-28z" fill="#b8bfc8" class="o"/>
  <path d="M-14-70q0-40 60-40h50v26h-40q-42 0-42 32z" fill="#c8d0d8" class="o"/>
  <path d="M-46-24h64q10 0 10 12t-10 12h-64q-10 0-10-12t10-12z" fill="#9aa5b0" class="o"/>
</g>
<g fill="{TONES['blue'][1]}" stroke="{TONES['blue'][0]}" stroke-width="2"><path d="M282 194h32v100h-32z"/></g>
<g transform="translate(250 288) rotate(-16)">
  <ellipse rx="56" ry="16" fill="#fffdf6" class="o"/>
  <path d="M-56 0q0 24 56 24t56-24z" fill="#fffdf6" class="o"/>
</g>
<g fill="#fffefd" stroke="{MUTED}" stroke-width="2">
  <circle cx="200" cy="250" r="14"/><circle cx="176" cy="286" r="11"/><circle cx="222" cy="292" r="9"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M420 200v90"/></g>''', arrow=True, ground=False)

add('ripple', '池に石を落として同心円のさざ波が広がる', f'''
<path d="M0 0h600v130H0z" fill="#dceaf4"/>
<path d="M0 130h600v270H0z" fill="#7aa8c4"/>
<path d="M0 130h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="#c7dbea" stroke-width="5">
''' + ''.join(f'<ellipse cx="300" cy="250" rx="{50+i*54}" ry="{16+i*17}"/>' for i in range(5)) + f'''
</g>
<g fill="none" stroke="#a8c8dd" stroke-width="4">
''' + ''.join(f'<ellipse cx="300" cy="250" rx="{76+i*54}" ry="{25+i*17}"/>' for i in range(4)) + f'''
</g>
<g fill="{TONES['blue'][1]}" stroke="{TONES['blue'][0]}" stroke-width="2.5">
  <circle cx="290" cy="216" r="12"/><circle cx="320" cy="206" r="9"/>
</g>
<g fill="{MUTED}" class="o"><ellipse cx="180" cy="100" rx="18" ry="14" transform="rotate(-20 180 100)"/></g>
<g class="a" marker-end="url(#ar)"><path d="M180 118q60 60 108 122"/></g>''', arrow=True, ground=False)

add('precipitation', '一年の月ごとの降水量が棒グラフになっている', f'''
<path d="M0 0h600v400H0z" fill="#eef4f8"/>
<g transform="translate(300 320)">
  <path d="M-250 0h500v6h-500z" fill="{INK}"/>
  <path d="M-250-260v260h6v-260z" fill="{INK}"/>
  <g class="blue o">
''' + ''.join(f'<rect x="{-230+i*40}" y="{-(50+abs(6-i)*-8+ (i%4)*36)}" width="30" height="{50+abs(6-i)*-8+(i%4)*36}"/>' for i in range(12)) + f'''
  </g>
</g>
{cloud(140, 90, 1.2, 'blue')}
{cloud(430, 70, 1.0, 'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
''' + ''.join(f'<path d="M{90+i*32} {140+(i%3)*22}l-10 26"/>' for i in range(6)) + ''.join(f'<path d="M{390+i*32} {120+(i%3)*22}l-10 26"/>' for i in range(5)) + f'''
</g>''', ground=False)

# --- 食べ物・体 --------------------------------------------------------------
add('poultry', 'ニワトリとアヒルが並び、その肉が皿にある', f'''
{table(330)}
<g transform="translate(160 260)">
  <ellipse rx="56" ry="42" fill="#fffdf6" class="o"/>
  <circle cx="46" cy="-30" r="22" fill="#fffdf6" class="o"/>
  <path d="M34-48q4-20 12-12 6-14 12-2 6-10 10 6-4 16-18 16z" class="coral o"/>
  <path d="M64-28l18 6-18 8z" class="gold o"/>
  <circle cx="50" cy="-32" r="3" fill="{INK}"/>
  <g stroke="{TONES['gold'][2]}" stroke-width="6" stroke-linecap="round" fill="none"><path d="M-16 40v14M14 40v14"/></g>
</g>
<g transform="translate(310 268)">
  <ellipse rx="54" ry="36" fill="#f0e6d0" class="o"/>
  <circle cx="44" cy="-26" r="20" fill="#f0e6d0" class="o"/>
  <path d="M62-24l24 4-22 12z" class="gold o"/>
  <circle cx="48" cy="-28" r="3" fill="{INK}"/>
  <g stroke="{TONES['gold'][2]}" stroke-width="6" stroke-linecap="round" fill="none"><path d="M-14 34v14M12 34v14"/></g>
</g>
<g transform="translate(470 280)">
  <ellipse rx="80" ry="22" fill="#fffdf6" class="o"/>
  <path d="M-80 0q0 30 80 30t80-30z" fill="#fffdf6" class="o"/>
  <path d="M-40-14q40-30 80-6 6 22-24 26-46 4-56-20z" fill="#c8934a" class="o"/>
  <path d="M40-18l24-14" stroke="#e8dcc0" stroke-width="9" stroke-linecap="round" fill="none"/>
</g>''', ground=False)

add('salty', '塩をふった料理をなめて塩からさに顔をしかめる', f'''
{table(340)}
<g transform="translate(420 130) rotate(30)">
  <path d="M-22 0h44l-6 62q-2 10-16 10t-16-10z" fill="#fffdf6" class="o"/>
  <path d="M-22 0q0-18 22-18t22 18z" fill="#b8bfc8" class="o"/>
  <g fill="{INK}"><circle cx="-7" cy="-9" r="2.5"/><circle cx="7" cy="-9" r="2.5"/><circle cx="0" cy="-14" r="2.5"/></g>
</g>
<g fill="#fffefd" stroke="{MUTED}" stroke-width="1.5">
''' + ''.join(f'<circle cx="{360+ (i%4)*13}" cy="{200+i*15}" r="3.5"/>' for i in range(9)) + f'''
</g>
<g transform="translate(400 300)">
  <ellipse rx="80" ry="22" fill="#fffdf6" class="o"/>
  <path d="M-80 0q0 28 80 28t80-28z" fill="#fffdf6" class="o"/>
  <path d="M-40-12q40-24 80-2 4 20-24 24-46 4-56-22z" class="gold o"/>
</g>
<g transform="translate(180 220)">
  <circle r="94" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-64-20q28-24 50-2M14-22q28-24 50 2" fill="none" stroke="{HAIR}" stroke-width="7" stroke-linecap="round"/>
  <path d="M-40 6q14-14 28 0M12 6q14-14 28 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <path d="M-24 54q24-26 48 0-24-8-48 0z" fill="{INK}" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M90 130l-24-20M76 200H50M96 274l-24 22"/>
</g>''', ground=False)

add('puberty', '子どもの体が数年で大人の体つきに変わる', f'''
{split()}
{table(370)}
{person(150, 370, 0.8, 1, 'coral', 'blue', 'stand', 'bob', 'smile')}
{person(450, 370, 1.25, 1, 'coral', 'blue', 'stand', 'bob', 'smile')}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8">
  <path d="M40 258h520"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 200h120"/></g>
<g transform="translate(300 110)">
  <path d="M-70-40h140q12 0 12 12v44q0 12-12 12h-96l-22 16v-16q-12 0-12-12v-44q0-12 12-12z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}"><rect x="-46" y="-16" width="92" height="9" rx="4.5"/><rect x="-46" y="4" width="64" height="9" rx="4.5"/></g>
</g>''', arrow=True, ground=False)

add('organism', '顕微鏡の中で単細胞の生き物が動いている', f'''
{table(370)}
<g transform="translate(180 250)">
  <path d="M-50 120h100v20h-100z" fill="#5a6270" class="o"/>
  <path d="M-14 120V20h28v100z" fill="#8f9aa6" class="o"/>
  <path d="M-14 20q-40-30-40-80t54-70v40q-26 10-26 34t26 36z" fill="#8f9aa6" class="o"/>
  <path d="M-14-116h60v34h-60z" fill="#5a6270" class="o"/>
  <path d="M-50 60h100v14h-100z" fill="#c8d0d8" class="o"/>
</g>
<g transform="translate(430 200)">
  <circle r="120" fill="{TONES['green'][1]}" class="o"/>
  <g class="green o">
    <ellipse cx="-30" cy="-24" rx="46" ry="32" transform="rotate(-20 -30 -24)"/>
    <ellipse cx="42" cy="30" rx="38" ry="27" transform="rotate(24 42 30)"/>
    <ellipse cx="-20" cy="56" rx="30" ry="21" transform="rotate(-14 -20 56)"/>
  </g>
  <g fill="{TONES['green'][2]}"><circle cx="-30" cy="-24" r="12"/><circle cx="42" cy="30" r="10"/><circle cx="-20" cy="56" r="8"/></g>
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="3" stroke-linecap="round">
    <path d="M-70-40l-16-10M-4-52l-6-18M76 40l18 8M64 54l10 18"/>
  </g>
</g>''', ground=False)

add('reptile', 'うろこにおおわれ日なたで体を温めるトカゲ', f'''
<path d="M0 0h600v290H0z" fill="#dceaf4"/>
<path d="M0 290h600v110H0z" fill="#e0d6c0"/>
<path d="M0 290h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="#b8ad98" class="o"><ellipse cx="300" cy="320" rx="200" ry="40"/></g>
<g transform="translate(300 300)">
  <path d="M-160 0q0-30 60-30h100q50 0 60 20t-40 24h-120q-60 0-60-14z" class="green o"/>
  <ellipse cx="130" cy="-10" rx="46" ry="26" class="green o"/>
  <path d="M170-14l30 4-28 10z" class="corald o"/>
  <circle cx="140" cy="-18" r="5" fill="{INK}"/>
  <path d="M-160 0q-70 6-100-16 60-30 100 2z" class="green o"/>
  <g stroke="{TONES['green'][2]}" stroke-width="10" stroke-linecap="round" fill="none">
    <path d="M-80 12l-30 26M60 14l30 26M-40 12l-14 30M20 14l14 30"/>
  </g>
  <g fill="{TONES['green'][2]}">
''' + ''.join(f'<path d="M{-130+i*30} -22l14-14 14 14z"/>' for i in range(9)) + f'''
  </g>
</g>
{sun(500, 80, 40)}''', ground=False)

add('massage', '背中の筋肉を両手でもみほぐしている', f'''
{table(370)}
<g transform="translate(300 300)">
  <path d="M-200-30h400v30h-400z" fill="#fffdf6" class="o"/>
  <path d="M-180 0v40M180 0v40" stroke="#8f9aa6" stroke-width="12" stroke-linecap="round" fill="none"/>
</g>
<g transform="translate(300 250)">
  <path d="M-150-20q60-40 160-30 100 10 140 30-40 24-140 26-100 2-160-26z" fill="{TONES['teal'][0]}" class="o"/>
  <circle cx="-172" cy="-22" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-200-34q6-30 30-28 22 2 26 26z" fill="{HAIR}"/>
  <path d="M150-10q50 0 70 16-30 14-70 8z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
{hand(240, 190, 1)}
{hand(340, 190, -1)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M230 140q-16-14 0-26M350 136q16-14 0-26"/>
</g>''', ground=False)

# --- 動きと言葉 --------------------------------------------------------------
add('navigate', '地図と方位磁針を見ながら進む道を選ぶ', f'''
{table(370)}
<g transform="translate(230 220) rotate(-6)">
  <path d="M-160-110h320v220h-320z" fill="#f0e6d0" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    <path d="M-160-40h320M-160 40h320M-60-110v220M60-110v220"/>
  </g>
  <path d="M-130 80q60-70 140-40t120-90" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="14 10"/>
  <circle cx="-130" cy="80" r="10" class="coral o"/>
  <path d="M130-50l-14 26h28z" class="coral o"/>
  <g class="greenp o"><circle cx="-90" cy="-60" r="20"/><circle cx="90" cy="50" r="18"/></g>
</g>
<g transform="translate(470 300)">
  <circle r="66" fill="#fffdf6" class="o"/>
  <circle r="54" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M0-50l14 44-14 6-14-6z" class="coral o"/>
  <path d="M0 50l14-44-14-6-14 6z" fill="#fffefd" class="o"/>
  <circle r="7" fill="{INK}"/>
</g>''', ground=False)

add('ramble', '道をはずれて野原をあてもなくのんびり歩き回る', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v170H0z" fill="#dfe8d8"/>
<path d="M0 230h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M60 400q40-90 120-100t100-40 140 20 160-40" fill="none" stroke="#c9a464" stroke-width="18" stroke-dasharray="20 16"/>
<g fill="{TONES['green'][0]}" opacity="0.5">
''' + ''.join(f'<circle cx="{40+i*44}" cy="{300+(i%4)*26}" r="7"/>' for i in range(13)) + f'''
</g>
{person(280, 340, 1.05, 1, 'coral', 'green', 'walk', 'cap', 'smile', 'walk')}
<path d="M330 250v100" stroke="#a0764a" stroke-width="7" stroke-linecap="round" fill="none"/>
{tree(90, 260, 0.9)}
{tree(500, 280, 1.1)}
{sun(510, 70, 32)}
<g class="a" marker-end="url(#ar)" stroke="{MUTED}"><path d="M120 200q60-60 130-20t150-40"/></g>''', ground=False)

add('oversleep', '目覚ましが鳴ったのに気づかず寝過ごしてしまう', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
{table(380)}
<g transform="translate(300 300)">
  <path d="M-200-20h400v60h-400z" class="bluep o"/>
  <path d="M-210-60h100v40h-100z" fill="#fffdf6" class="o"/>
  <path d="M-220 40v40M200 40v40" stroke="{BRN}" stroke-width="14" stroke-linecap="round" fill="none"/>
  <circle cx="-160" cy="-46" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-190-58q6-30 30-28 24 2 28 28z" fill="{HAIR}"/>
  <path d="M-172-44q10-8 14 0M-152-44q10-8 14 0" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M-0 0"/>
</g>
<g transform="translate(120 200)">
  <circle r="60" fill="#fffdf6" class="o"/>
  <path d="M-42-42l-24-24M42-42l24-24" stroke="{INK}" stroke-width="10" stroke-linecap="round" fill="none"/>
  <circle cx="-42" cy="-52" r="16" class="coral o"/><circle cx="42" cy="-52" r="16" class="coral o"/>
  <path d="M0 0v-36M0 0l26 18" stroke="{INK}" stroke-width="6" stroke-linecap="round" fill="none"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M200 160q26 30 0 60M232 140q40 46 0 92"/>
</g>
<g fill="{MUTED}" opacity="0.8">
''' + ''.join(f'<path d="M{330+i*40} {160-i*30}q18 0 18 14t-18 14h20" fill="none" stroke="{MUTED}" stroke-width="{4+i}"/>' for i in range(3)) + f'''
</g>''', ground=False)

add('rehearse', '本番の前に舞台でせりふのけいこをする', f'''
<path d="M0 0h600v400H0z" fill="#3b3550"/>
<path d="M0 320h600v80H0z" fill="#5a4a3c" class="o"/>
<path d="M0 60h600v40H0z" class="corald o"/>
<path d="M0 100h70v220H0zM600 100h-70v220h70z" class="coral o"/>
{person(220, 320, 1.05, 1, 'teal', 'blue', 'up', 'bun', 'smile')}
{person(370, 320, 1.05, -1, 'gold', 'violet', 'point', 'short', 'smile')}
<g transform="translate(300 150)">
  <path d="M-70-40h140q12 0 12 12v40q0 12-12 12h-96l-22 18v-18q-12 0-12-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}"><rect x="-46" y="-16" width="92" height="9" rx="4.5"/><rect x="-46" y="4" width="60" height="9" rx="4.5"/></g>
</g>
{sit(520, 380, 0.8, -1, 'violet', 'blue', 'bob', 'neutral', 'lap')}
<g transform="translate(500 300) rotate(-10)">
  <path d="M-30-40h60v80h-60z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}"><rect x="-20" y="-26" width="40" height="6" rx="3"/><rect x="-20" y="-12" width="30" height="6" rx="3"/></g>
</g>''', ground=False)

add('memorise', '単語カードを見て内容を頭に入れる', f'''
{table(350)}
{sit(180, 350, 1.1, 1, 'coral', 'blue', 'bun', 'neutral', 'up')}
{chair(180, 350, 1.0, 'gold', 1)}
<g transform="translate(250 230) rotate(-12)">
  <path d="M-50-36h100v72h-100z" class="paper"/>
  <rect x="-32" y="-8" width="64" height="16" rx="8" fill="{INK}"/>
</g>
<g transform="translate(180 150)">
  <path d="M-70-40q0-40 70-40t70 40q0 40-70 40t-70-40z" fill="#fffefd" class="o" opacity="0.9"/>
  <rect x="-40" y="-48" width="80" height="16" rx="8" fill="{INK}"/>
  <circle cx="-64" cy="14" r="9" fill="#fffefd" class="o"/>
  <circle cx="-84" cy="34" r="6" fill="#fffefd" class="o"/>
</g>
<g>
''' + ''.join(f'<g transform="translate({420+i*10} {300+i*4}) rotate({-8+i*7})"><path d="M-50-34h100v68h-100z" class="paper"/><rect x="-32" y="-8" width="{56-i*8}" height="14" rx="7" fill="{MUTED}"/></g>' for i in range(3)) + f'''
</g>''', ground=False)

add('phrase', '単語がいくつか集まって一つの言い回しになる', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(300 120)">
''' + ''.join(f'<g transform="translate({-170+i*115} 0)"><path d="M-50-30h100v60h-100z" class="tealp o"/><rect x="-32" y="-8" width="64" height="16" rx="8" fill="{INK}"/></g>' for i in range(4)) + f'''
</g>
<g transform="translate(300 290)">
  <path d="M-250-40h500v80h-500z" class="goldp o"/>
  <g fill="{INK}">
''' + ''.join(f'<rect x="{-220+i*115}" y="-8" width="{64+ (i%2)*20}" height="16" rx="8"/>' for i in range(4)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 170v70"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M60 200h480"/></g>''', arrow=True, ground=False)

add('satire', '政治家を大げさに描いて皮肉る風刺画', f'''
{table(370)}
<g transform="translate(300 200)">
  <path d="M-190-150h380v300h-380z" class="paper"/>
  <g transform="translate(-40 20)">
    <ellipse cy="60" rx="60" ry="46" class="violet o"/>
    <circle cy="-30" r="64" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
    <path d="M-64-46q6-46 64-46t64 46q-34-24-64-16-30-14-64 16z" fill="{HAIR}"/>
    <circle cx="-22" cy="-30" r="6" fill="{INK}"/><circle cx="22" cy="-30" r="6" fill="{INK}"/>
    <path d="M-4-20q40 10 46-2 8 20-42 24z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <path d="M-20 14q24 14 44-2" fill="none" stroke="{INK}" stroke-width="4"/>
  </g>
  <g transform="translate(110 -60)">
    <path d="M-56-40h112q12 0 12 12v40q0 12-12 12h-76l-20 16v-16q-16 0-16-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
    <g fill="{MUTED}"><rect x="-38" y="-16" width="76" height="9" rx="4.5"/><rect x="-38" y="4" width="50" height="9" rx="4.5"/></g>
  </g>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
    <path d="M110 60q20-16 40 0M110 100q20-16 40 0"/>
  </g>
</g>''', ground=False)

add('lantern', '取っ手のついたランタンが暗がりを照らす', f'''
<path d="M0 0h600v400H0z" fill="#2c2f3d"/>
<path d="M0 360h600v40H0z" fill="#1e2129" class="o"/>
<g transform="translate(300 200)">
  <path d="M-46-70q0-40 46-40t46 40" fill="none" stroke="#8f9aa6" stroke-width="8"/>
  <path d="M-56-70h112v20h-112z" fill="#8f9aa6" class="o"/>
  <path d="M-46-50h92v120h-92z" fill="{TONES['gold'][1]}" class="o"/>
  <g fill="none" stroke="#8f9aa6" stroke-width="7"><path d="M-46-50v120M46-50v120"/></g>
  <path d="M-56 70h112v20h-112z" fill="#8f9aa6" class="o"/>
  {flame(0, 46, 0.42)}
</g>
<g fill="{TONES['gold'][1]}" opacity="0.22">
  <path d="M300 200l-260 200h520z"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M410 130l30-26M440 200h36M410 274l30 26M190 130l-30-26M160 200h-36M190 274l-30 26"/>
</g>''', ground=False)

add('lace', '細かい模様の透けたレース地の布', f'''
{table(340)}
<g transform="translate(300 210)">
  <path d="M-200-110h400v220h-400z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5">
''' + ''.join(f'<circle cx="{-170+ (i%9)*42}" cy="{-80+(i//9)*42}" r="16"/>' for i in range(45)) + f'''
  </g>
  <g fill="{MUTED}">
''' + ''.join(f'<circle cx="{-149+ (i%8)*42}" cy="{-59+(i//8)*42}" r="4"/>' for i in range(40)) + f'''
  </g>
  <path d="M-200 110q26-26 50 0t50 0 50 0 50 0 50 0 50 0 50 0 50 0" fill="none" stroke="{MUTED}" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 110l-100 60"/></g>''', arrow=True, ground=False)

add('sash', '肩から斜めにかけた飾り帯', f'''
{table(380)}
{person(300, 380, 1.35, 1, 'teal', 'blue', 'stand', 'bun', 'smile')}
<g transform="translate(300 290)">
  <path d="M-40-96q20-10 40 0l50 116q-40 14-80 0z" class="coral o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"><path d="M-26-60q26 8 52 0M-12-14q26 8 52 0"/></g>
  <circle cx="34" cy="34" r="16" class="gold o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 200l-120 40"/></g>''', arrow=True, ground=False)

add('pouch', '口をひもで縛る小さな袋', f'''
{table(330)}
<g transform="translate(240 250)">
  <path d="M-70-30q70-30 140 0 20 60-6 82-64 20-128 0-26-22-6-82z" class="gold o"/>
  <path d="M-70-30q70-24 140 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"/>
  <path d="M-56-40q56-22 112 0v14q-56-20-112 0z" class="goldd o"/>
  <path d="M-56-40q-30-14-40-40M56-40q30-14 40-40" fill="none" stroke="{BRN}" stroke-width="5" stroke-linecap="round"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="3"><path d="M-40 30q40 14 80 0"/></g>
</g>
{coin(430, 240, 20)}
{coin(468, 268, 17)}
{coin(410, 288, 15)}
<g class="a" marker-end="url(#ar)"><path d="M400 200l-100 20"/></g>''', arrow=True, ground=False)

# --- re- の動詞 ---------------------------------------------------------------
add('reconnect', '切れていた線をつなぎ直して通信が戻る', f'''
{split()}
{table(370)}
<g transform="translate(150 220)">
  <path d="M-120-14h80v28h-80z" fill="#8f9aa6" class="o"/>
  <path d="M40-14h80v28H40z" fill="#8f9aa6" class="o"/>
  <path d="M-40-8h14v16h-14zM26-8h14v16H26z" fill="{INK}"/>
</g>
{cross(150, 300, 0.8)}
<g transform="translate(450 220)">
  <path d="M-120-14h110v28h-110z" fill="#8f9aa6" class="o"/>
  <path d="M10-14h110v28H10z" fill="#8f9aa6" class="o"/>
  <path d="M-14-20h28v40h-28z" fill="{TONES['gold'][0]}" class="o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M450 170q-26-24 0-46M492 176q40-32 0-64M408 176q-40-32 0-64"/>
</g>
{tick(450, 300, 0.8)}''', ground=False)

add('reconsider', '一度出した結論を消して考え直す', f'''
{table(370)}
<g transform="translate(300 210) rotate(-4)">
  <path d="M-180-130h360v260h-360z" class="paper"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-140" y="{-100+i*30}" width="{280-(i%3)*50}" height="9" rx="4.5"/>' for i in range(4)) + f'''
  </g>
  <rect x="-140" y="40" width="180" height="14" rx="7" fill="{INK}"/>
  <path d="M-150 30h200" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round" fill="none"/>
  <path d="M-150 62h200" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round" fill="none"/>
  <rect x="-140" y="84" width="150" height="14" rx="7" class="green"/>
</g>
{person(110, 370, 0.9, 1, 'violet', 'blue', 'think', 'bun', 'neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M470 130q40 30 0 60" marker-end="url(#ar)"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 120q60 40 0 76"/></g>''', arrow=True, ground=False)

add('reinstall', 'いったん消したソフトを入れ直している', f'''
{split()}
{table(380)}
{screen(150, 200, 190, 130)}
<g transform="translate(150 200)">
  <g class="o">
''' + ''.join(f'<rect x="{-70+ (i%3)*50}" y="{-42+(i//3)*46}" width="34" height="34" rx="6" class="{["tealp","goldp","violetp"][i%3]}"/>' for i in range(6)) + f'''
  </g>
  {cross(50, 30, 0.5)}
</g>
{screen(450, 200, 190, 130)}
<g transform="translate(450 200)">
  <g class="o">
''' + ''.join(f'<rect x="{-70+ (i%3)*50}" y="{-42+(i//3)*46}" width="34" height="34" rx="6" class="{["tealp","goldp","violetp"][i%3]}"/>' for i in range(6)) + f'''
    <rect x="30" y="4" width="34" height="34" rx="6" class="coralp"/>
  </g>
  {tick(50, 66, 0.45)}
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 340h60"/></g>''', arrow=True, ground=False)

add('rename', 'ファイルの名前を書き換えて別の名にする', f'''
{split()}
{table(380)}
<g transform="translate(150 200)">
  <path d="M-70-100h100l40 40v160h-140z" class="paper"/>
  <path d="M30-100v40h40z" fill="#d6cec0" class="o"/>
  <rect x="-50" y="40" width="100" height="16" rx="8" fill="{INK}"/>
</g>
<g transform="translate(450 200)">
  <path d="M-70-100h100l40 40v160h-140z" class="paper"/>
  <path d="M30-100v40h40z" fill="#d6cec0" class="o"/>
  <rect x="-50" y="40" width="70" height="16" rx="8" class="coral"/>
  <path d="M-56 66h116" stroke="{TONES['coral'][0]}" stroke-width="3" fill="none"/>
</g>
<g transform="translate(510 290) rotate(30)">
  <path d="M0-70l12 26v70h-24V-44z" class="gold o"/>
  <path d="M-12 26h24v34l-12 20-12-20z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('reopen', '閉まっていた店がふたたび開く', f'''
{split()}
{table(380)}
<g transform="translate(150 380)">
  <path d="M-100 0v-140h200V0z" fill="#c8d0d8" class="o"/>
  <path d="M-114-140h228v-24h-228z" fill="#8f9aa6" class="o"/>
  <path d="M-70-110h140v90h-140z" fill="#6f7b88" class="o"/>
  <g fill="none" stroke="#5a6270" stroke-width="4">
''' + ''.join(f'<path d="M-70 {-100+i*16}h140"/>' for i in range(6)) + f'''
  </g>
</g>
{cross(150, 130, 0.8)}
<g transform="translate(450 380)">
  <path d="M-100 0v-140h200V0z" fill="#fffdf6" class="o"/>
  <path d="M-114-140h228v-24h-228z" class="coral o"/>
  <path d="M-80-110h70v70h-70z" class="bluep o"/>
  <path d="M14-110h64V0H14z" class="corald o"/>
  <path d="M-24-160h48v-30h-48z" class="gold o"/>
</g>
{tick(450, 130, 0.8)}
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('repay', '借りたお金を期日どおりに返す', f'''
{table(340)}
{person(160, 340, 1.0, 1, 'coral', 'blue', 'give', 'bob', 'smile')}
{person(460, 340, 1.0, -1, 'teal', 'violet', 'give', 'short', 'smile')}
<g transform="translate(300 220) rotate(-6)">
  <path d="M-60-28h120v56h-120z" class="greenp o"/>
  <circle r="17" fill="none" stroke="{TONES['green'][2]}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="2.5"><path d="M-50-18h22M28 18h22"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 180q70-40 140 0"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M370 300q-70 30-140 0"/></g>
<g transform="translate(300 320)">
  <path d="M-46-30h92v60h-92z" class="paper"/>
  <g fill="{MUTED}"><rect x="-32" y="-16" width="64" height="7" rx="3.5"/><rect x="-32" y="-2" width="44" height="7" rx="3.5"/></g>
  {tick(16, 16, 0.35)}
</g>''', arrow=True, ground=False)

add('reschedule', '予定表の日付を消して別の日に組み直す', f'''
{table(370)}
<g transform="translate(300 200)">
  <path d="M-190-140h380v280h-380z" class="paper"/>
  <path d="M-190-140h380v50h-380z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5">
''' + ''.join(f'<path d="M{-190+i*54} -90v230"/>' for i in range(8)) + ''.join(f'<path d="M-190 {-40+i*44}h380"/>' for i in range(5)) + f'''
  </g>
  <rect x="-176" y="-24" width="26" height="12" rx="6" class="coral"/>
  <path d="M-186-18h46" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round" fill="none"/>
  <rect x="14" y="68" width="26" height="12" rx="6" class="green"/>
  <circle cx="27" cy="74" r="24" fill="none" stroke="{TONES['green'][0]}" stroke-width="4"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M130 200q80-70 190 50"/></g>''', arrow=True, ground=False)

add('rift', '地面に大きな裂け目ができて二つに分かれる', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v170H0z" fill="#c9d8c0"/>
<path d="M0 230h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M270 230l20 40-24 40 30 50-20 40h70l-24-46 26-42-26-40 22-42z" fill="#5b4a3c" class="o"/>
<path d="M282 240l14 30-18 34 22 44-14 32h34l-16-38 20-38-20-34 16-30z" fill="#2f2820"/>
<g fill="none" stroke="#a89880" stroke-width="3">
  <path d="M120 300h130M360 320h130M100 360h150M360 380h140"/>
</g>
<g fill="#8f9aa6" class="o">
  <ellipse cx="140" cy="270" rx="20" ry="12"/><ellipse cx="450" cy="290" rx="16" ry="10"/>
</g>
{tree(80, 240, 0.8)}
{tree(520, 240, 0.8)}
<g class="a" marker-end="url(#ar)"><path d="M170 180h80"/></g>
<g class="a" marker-end="url(#ar)"><path d="M430 180h-80"/></g>''', arrow=True, ground=False)

add('livestream', 'カメラで撮った映像がそのまま画面に流れている', f'''
{table(380)}
<g transform="translate(140 250)">
  <path d="M-70-46h120v92h-120z" fill="#3b4450" class="o"/>
  <path d="M50-20l40-26v92l-40-26z" fill="#5a6270" class="o"/>
  <circle cx="-20" r="24" fill="#8f9aa6" class="o"/><circle cx="-20" r="12" fill="{INK}"/>
  <circle cx="-56" cy="-30" r="8" class="coral o"/>
  <path d="M-10 46v50M-50 96h80" stroke="{INK}" stroke-width="8" stroke-linecap="round" fill="none"/>
</g>
{screen(430, 200, 210, 140)}
<g transform="translate(430 200)">
  <path d="M-105-70h210v140h-210z" fill="#dceaf4"/>
  {person(0, 60, 0.5, 1, 'coral', 'blue', 'up', 'bun', 'smile')}
  <g transform="translate(-70 -50)">
    <circle r="12" class="coral"/>
    <path d="M20-8h56v16H20z" class="coral"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M250 220h60"/></g>''', ground=False)

add('lodge', '山あいの木造の宿に泊まる', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 190l120-90 90 60 110-80 130 90 150-60v220H0z" fill="#9aa5b0" class="o"/>
<path d="M0 300h600v100H0z" fill="#dfe8d8"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 300)">
  <path d="M-130 0v-110h260V0z" fill="#a0764a" class="o"/>
  <g fill="none" stroke="#8b6437" stroke-width="3"><path d="M-130-80h260M-130-50h260M-130-20h260"/></g>
  <path d="M-160-110L0-190l160 80z" fill="#7a5b3c" class="o"/>
  <path d="M-90-84h60v44h-60zM30-84h60v44h-60z" class="goldp o"/>
  <path d="M-24-40h48V0h-48z" fill="#6b4c28" class="o"/>
  <path d="M60-150h20v40H60z" fill="#5a6270" class="o"/>
</g>
<g fill="{MUTED}" opacity="0.7"><circle cx="376" cy="122" r="14"/><circle cx="396" cy="98" r="11"/><circle cx="410" cy="76" r="8"/></g>
{tree(90, 320, 1.1)}
{tree(520, 330, 1.2)}''', ground=False)

add('natural', '人工の造花と、野に咲く本物の花', f'''
{split()}
{table(370)}
<g transform="translate(150 250)">
  <path d="M-40-40h80v90q0 14-40 14t-40-14z" class="tealp o"/>
  <path d="M-6-40v-60h12v60z" class="green"/>
  <g class="coralp o">
''' + ''.join(f'<ellipse cx="{34*math.cos(j*1.2566):.0f}" cy="{-100+34*math.sin(j*1.2566):.0f}" rx="24" ry="19" transform="rotate({j*72} {34*math.cos(j*1.2566):.0f} {-100+34*math.sin(j*1.2566):.0f})"/>' for j in range(5)) + f'''
  </g>
  <circle cy="-100" r="15" class="gold o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-40 20h80"/></g>
</g>
<g fill="#dfe8d8"><path d="M300 300h300v100H300z"/></g>
<path d="M300 300h300" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(450 300)">
  <path d="M-6 0v-100h12V0z" class="greend o"/>
  <path d="M-6-50q-46-20-38-46 38 4 38 46z" class="greenp o"/>
  <g class="coralp o">
''' + ''.join(f'<ellipse cx="{34*math.cos(j*1.2566):.0f}" cy="{-136+34*math.sin(j*1.2566):.0f}" rx="24" ry="19" transform="rotate({j*72} {34*math.cos(j*1.2566):.0f} {-136+34*math.sin(j*1.2566):.0f})"/>' for j in range(5)) + f'''
  </g>
  <circle cy="-136" r="15" class="gold o"/>
</g>
<g fill="{TONES['green'][0]}" opacity="0.5">
''' + ''.join(f'<path d="M{330+i*36} 300v-{20+(i%3)*12}" stroke="{TONES["green"][0]}" stroke-width="3"/>' for i in range(8)) + f'''
</g>
{sun(540, 80, 26)}''', ground=False)

add('nonstop', '途中で止まらず目的地まで一気に行く便', f'''
{split()}
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
<g transform="translate(150 200)">
  <circle cx="-90" cy="80" r="16" class="teal o"/>
  <circle cx="0" cy="0" r="12" class="gold o"/>
  <circle cx="90" cy="-80" r="16" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M-76 66L-12-12M12-12l64-56"/></g>
</g>
<g transform="translate(450 200)">
  <circle cx="-90" cy="80" r="16" class="teal o"/>
  <circle cx="90" cy="-80" r="16" class="teal o"/>
  <g class="a" marker-end="url(#ar)" stroke-width="5"><path d="M-76 66L76-66"/></g>
</g>
{plane(450, 200, 0.42, -42, 'coral')}
<g class="a" marker-end="url(#ar)"><path d="M270 320h60"/></g>''', arrow=True, ground=False)

add('nuclear-family', '親と子どもだけの小さな家族', f'''
{table(380)}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="14 10">
  <ellipse cx="300" cy="260" rx="190" ry="120"/>
</g>
{head(220, 220, 28, 'teal', 'short')}
{head(380, 220, 28, 'coral', 'bun')}
{head(230, 320, 22, 'gold', 'cap')}
{head(370, 322, 22, 'green', 'bob')}
<g fill="{MUTED}" opacity="0.4">
  {head(70, 300, 18, 'violet', 'bun')}
  {head(530, 300, 18, 'blue', 'short')}
</g>''', ground=False)

add('personal', 'みんなの棚と、自分だけの引き出しに分かれている', f'''
{split()}
{table(380)}
<g transform="translate(150 220)">
  <path d="M-110-120h220v240h-220z" fill="#e0d6c0" class="o"/>
  <g fill="none" stroke="{BRN}" stroke-width="5"><path d="M-110-40h220M-110 40h220"/></g>
  <g class="o">
''' + ''.join(f'<rect x="{-92+ (i%4)*50}" y="{-104+(i//4)*80}" width="34" height="56" class="{["coralp","tealp","goldp","violetp"][i%4]}"/>' for i in range(12)) + f'''
  </g>
</g>
{head(80, 340, 18, 'coral', 'bob')}
{head(150, 344, 18, 'teal', 'short')}
{head(220, 340, 18, 'gold', 'bun')}
<g transform="translate(450 220)">
  <path d="M-100-120h200v240h-200z" fill="#c9a464" class="o"/>
  <g fill="none" stroke="#8b6437" stroke-width="4"><path d="M-100-40h200M-100 40h200"/></g>
  <g fill="{INK}"><circle cx="0" cy="-80" r="8"/><circle cx="0" cy="0" r="8"/><circle cx="0" cy="80" r="8"/></g>
  <g transform="translate(60 -80)">
    <path d="M-14-14h28v20h-28z" fill="{TONES['gold'][0]}" class="o"/>
    <path d="M-8-14q0-12 8-12t8 12" fill="none" stroke="{INK}" stroke-width="4"/>
  </g>
</g>
{head(450, 344, 18, 'violet', 'bun')}''', ground=False)

add('preheat', '料理を入れる前にオーブンを温めておく', f'''
{split()}
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<g transform="translate(150 210)">
  <path d="M-110-110h220v230h-220z" fill="#5a6270" class="o"/>
  <path d="M-88-88h176v160h-176z" fill="#2c333d" class="o"/>
  <path d="M-80-80h160v144h-160z" fill="#c8703a" opacity="0.4"/>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{-64+i*32} -58v-14"/>' for i in range(5)) + ''.join(f'<path d="M{-64+i*32} 50v-14"/>' for i in range(5)) + f'''
  </g>
  <g fill="{TONES['green'][0]}"><rect x="40" y="86" width="14" height="22"/><rect x="60" y="86" width="14" height="22"/></g>
</g>
<g transform="translate(450 210)">
  <path d="M-110-110h220v230h-220z" fill="#5a6270" class="o"/>
  <path d="M-88-88h176v160h-176z" fill="#2c333d" class="o"/>
  <path d="M-80-80h160v144h-160z" fill="#c8703a" opacity="0.4"/>
  <g transform="translate(0 10)">
    <path d="M-70-20h140v40h-140z" fill="#9aa5b0" class="o"/>
    <path d="M-50-40q50-24 100 0 8 24-14 34-46 10-80-4-10-14-6-30z" fill="#c8934a" class="o"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 210h60"/></g>''', arrow=True, ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
