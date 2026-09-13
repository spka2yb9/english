# -*- coding: utf-8 -*-
"""第139回。d-/e- の形容詞と身のまわりの名詞。"""
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
def doc(x, y, w=100, h=130, lines=4):
    g = [f'<g transform="translate({x} {y})"><path d="M{-w/2} {-h/2}h{w}v{h}h{-w}z" class="paper"/>']
    for i in range(lines):
        g.append(f'<rect x="{-w/2+14}" y="{-h/2+22+i*(h-50)/max(lines,1):.0f}" width="{w-28-(i%3)*16}" height="8" rx="4" fill="{MUTED}"/>')
    g.append('</g>')
    return ''.join(g)
def head(x, y, r=22, shirt='teal', hair='short'):
    return (f'<g transform="translate({x} {y})">'
            f'<circle r="{r}" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>'
            f'<path d="{HAIRS[hair]}" transform="translate(0 108) scale({r/24:.2f})" fill="{HAIR}"/>'
            f'<circle cx="{-r*0.33:.0f}" cy="{-r*0.17:.0f}" r="2.4" fill="{INK}"/>'
            f'<circle cx="{r*0.33:.0f}" cy="{-r*0.17:.0f}" r="2.4" fill="{INK}"/>'
            f'<path d="M{-r*0.3:.0f} {r*0.35:.0f}q{r*0.3:.0f} {r*0.3:.0f} {r*0.6:.0f} 0" fill="none" stroke="{INK}" stroke-width="2"/>'
            f'<path d="M{-r*1.1:.0f} {r*1.5:.0f}q{r*1.1:.0f}-{r*0.6:.0f} {r*2.2:.0f} 0l-{r*0.3:.0f} {r*1.2:.0f}h-{r*1.6:.0f}z" fill="{TONES[shirt][0]}" class="o"/></g>')
def word(x, y, n=5, w=26, cls=None, bad=-1):
    """文字は描けないので、語を四角の並びで表す。bad の位置だけ形を崩す。"""
    g = [f'<g transform="translate({x} {y})">']
    for i in range(n):
        cx = -(n-1)*w/2 + i*w
        if i == bad:
            g.append(f'<rect x="{cx-9}" y="-11" width="18" height="22" rx="4" fill="{TONES["coral"][0]}" transform="rotate(18 {cx} 0)"/>')
        else:
            g.append(f'<rect x="{cx-9}" y="-11" width="18" height="22" rx="4" fill="{cls or INK}"/>')
    g.append('</g>')
    return ''.join(g)


# --- 物 ---------------------------------------------------------------------
add('cursor', '画面の文字の入る位置を示す点滅する縦棒', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-200-150h400v300h-400z" fill="#3b4450" class="o"/>
  <path d="M-180-130h360v260h-360z" fill="#fffefd"/>
  <g fill="{INK}">
''' + ''.join(f'<rect x="-150" y="{-96+i*40}" width="{200-(i%3)*50}" height="14" rx="7"/>' for i in range(4)) + f'''
  </g>
  <path d="M-150 50h130v14h-130z" fill="{INK}"/>
  <path d="M-14 40h8v34h-8z" fill="{TONES['coral'][0]}"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3" stroke-dasharray="6 6"><path d="M-30 30h40M-30 84h40"/></g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M470 340l-180-80"/></g>''', arrow=True, ground=False)

add('daisy', '白い花びらと黄色い芯の小さな花', f'''
<path d="M0 0h600v300H0z" fill="#dceaf4"/>
<path d="M0 300h600v100H0z" fill="#c9d8c0"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g>
''' + ''.join(f'''<g transform="translate({130+i*115} 300)">
  <path d="M-6 0v-110h12V0z" class="greend o"/>
  <path d="M-6-60q-46-22-38-48 40 4 38 48z" class="greenp o"/>
  <g transform="translate(0 -140)">
    <g fill="#fffdf6" class="o">''' + ''.join(f'<ellipse cx="{34*math.cos(j*0.785):.0f}" cy="{34*math.sin(j*0.785):.0f}" rx="20" ry="11" transform="rotate({j*45} {34*math.cos(j*0.785):.0f} {34*math.sin(j*0.785):.0f})"/>' for j in range(8)) + f'''</g>
    <circle r="17" class="gold o"/>
  </g>
</g>''' for i in range(4)) + f'''
</g>
{sun(520, 70, 30)}''', ground=False)

add('denim', '青い厚手の生地で作った作業ズボン', f'''
{table(340)}
<g transform="translate(300 210)">
  <path d="M-80-90h160v50l-20 170h-56l-4-116-4 116h-56l-20-170z" fill="#4a6a94" class="o"/>
  <path d="M-80-40h160" fill="none" stroke="#39537a" stroke-width="3"/>
  <path d="M-80-90h160v-16h-160z" fill="#39537a" class="o"/>
  <g fill="none" stroke="{TONES['gold'][1]}" stroke-width="3" stroke-dasharray="8 6">
    <path d="M-70-84h140M-70 116h30M40 116h30M-70-30h140"/>
  </g>
  <g fill="none" stroke="{TONES['gold'][1]}" stroke-width="3">
    <path d="M-56-60h34v30h-34zM22-60h34v30H22z"/>
  </g>
  <circle cy="-76" r="7" fill="{TONES['gold'][0]}"/>
</g>''', ground=False)

add('diesel', '給油ノズルから黒い印の燃料を入れる', f'''
{table(380)}
<g transform="translate(180 260)">
  <path d="M-70-90h140v190h-140z" fill="#c8d0d8" class="o"/>
  <path d="M-56-76h112v54h-112z" fill="#2c333d" class="o"/>
  <g fill="{TONES['green'][0]}"><rect x="-40" y="-64" width="18" height="30"/><rect x="-16" y="-64" width="18" height="30"/></g>
  <path d="M-40 20h80v40h-80z" fill="{INK}" class="o"/>
  <path d="M70-20q40 0 40 30v50" fill="none" stroke="{INK}" stroke-width="9"/>
</g>
<g transform="translate(320 300) rotate(-16)">
  <path d="M-34-16h58v32h-58z" fill="{INK}"/>
  <path d="M24-9h50v18H24z" fill="#8f9aa6" class="o"/>
</g>
<g transform="translate(470 320)">
  <path d="M-70 40h140v-56q0-20-20-20h-42l-30-34h-28q-20 0-20 20v90z" class="teal o"/>
  <circle cx="-40" cy="40" r="22" fill="{INK}"/><circle cx="40" cy="40" r="22" fill="{INK}"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" opacity="0.8">
  <path d="M540 250q14-24 0-44"/>
</g>''', ground=False)

add('diploma', '課程を修めた証しに渡される証書', f'''
{table(380)}
<g transform="translate(300 210) rotate(-3)">
  <path d="M-170-120h340v240h-340z" fill="#f6ecd4" class="o"/>
  <path d="M-150-100h300v200h-300z" fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"/>
  <rect x="-100" y="-70" width="200" height="20" rx="10" fill="{INK}"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-110" y="{-24+i*30}" width="{220-(i%3)*50}" height="11" rx="5.5"/>' for i in range(3)) + f'''
  </g>
  <circle cx="100" cy="72" r="28" class="coral o"/>
  <path d="M-120 66q40-24 70 0" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"/>
</g>
{person(510, 380, 0.8, -1, 'violet', 'gold', 'reach', 'bun', 'smile')}''', ground=False)

add('dormitory', '学生が一部屋ずつ暮らす寮の建物', f'''
<path d="M0 0h600v300H0z" fill="#dceaf4"/>
<path d="M0 300h600v100H0z" fill="#c9d8c0"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 300)">
  <path d="M-180 0v-250h360V0z" fill="#e0d6c0" class="o"/>
  <path d="M-196-250h392v-24h-392z" fill="#c0b6a0" class="o"/>
  <g class="bluep o">
''' + ''.join(f'<rect x="{-150+ (i%5)*66}" y="{-220+(i//5)*70}" width="44" height="50"/>' for i in range(15)) + f'''
  </g>
  <path d="M-30 0v-60h60V0z" fill="{BRN}" class="o"/>
</g>
{head(160, 250, 16, 'coral', 'bob')}
{head(360, 180, 16, 'teal', 'short')}
{head(440, 320, 16, 'gold', 'cap')}''', ground=False)

add('ecosystem', '植物と虫と鳥がつながって一つの輪をなす', f'''
<path d="M0 0h600v250H0z" fill="#dceaf4"/>
<path d="M0 250h600v150H0z" fill="#c9d8c0"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
{tree(120, 300, 1.1)}
<g transform="translate(300 300)">
  <path d="M-6 0v-70h12V0z" class="greend o"/>
  <g class="coralp o">
''' + ''.join(f'<ellipse cx="{28*math.cos(j*1.2566):.0f}" cy="{-90+28*math.sin(j*1.2566):.0f}" rx="20" ry="16" transform="rotate({j*72} {28*math.cos(j*1.2566):.0f} {-90+28*math.sin(j*1.2566):.0f})"/>' for j in range(5)) + f'''
  </g>
  <circle cy="-90" r="13" class="gold o"/>
</g>
<g transform="translate(400 170) scale(0.5)">
  <ellipse rx="40" ry="26" class="gold o"/>
  <g fill="{INK}"><path d="M-18-24q10 48 0 48zM6-26q10 52 0 52z"/></g>
  <circle cx="-34" cy="-4" r="16" fill="{INK}"/>
  <ellipse cx="4" cy="-30" rx="30" ry="14" fill="#fffefd" stroke="{INK}" stroke-width="3" opacity="0.85" transform="rotate(-22 4 -30)"/>
</g>
<g transform="translate(490 250)">
  <ellipse rx="40" ry="28" class="teal o"/>
  <circle cx="34" cy="-20" r="20" class="teal o"/>
  <path d="M50-24l20 6-20 8z" class="corald o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="4" stroke-dasharray="10 8">
  <path d="M180 200q60-70 170-50M420 200q50 20 50 40M470 300q-140 60-300 20"/>
</g>''', ground=False)

add('electrician', '電気工が配線を直す', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<g transform="translate(400 180)">
  <path d="M-70-70h140v140h-140z" fill="#c8d0d8" class="o"/>
  <path d="M-56-56h112v112h-112z" fill="#8f9aa6" class="o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6">
    <path d="M-40-30h80M-40 0h80M-40 30h80"/>
  </g>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="6">
    <path d="M70-30q40 0 40 40t-40 40"/>
  </g>
</g>
{person(180, 380, 1.1, 1, 'gold', 'blue', 'reach', 'cap', 'neutral')}
<g transform="translate(270 250) rotate(20)">
  <path d="M-40-10h80v20h-80z" fill="{TONES['gold'][0]}"/>
  <path d="M40-6h34v12H40z" fill="#8f9aa6" class="o"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M330 130l24-24M350 90l6-26"/>
</g>''', ground=False)

add('duty-free', '空港で税のかからない品を買う', f'''
<path d="M0 0h600v400H0z" fill="#e8eef2"/>
{table(380)}
<g transform="translate(300 150)">
  <path d="M-180-50h360v70h-360z" class="teal o"/>
  <g fill="#fffefd"><rect x="-140" y="-30" width="180" height="20" rx="10"/><rect x="60" y="-30" width="80" height="20" rx="10"/></g>
</g>
<g transform="translate(300 300)">
  <path d="M-200-40h400v40h-400z" fill="#c9a464" class="o"/>
  <g class="o">
    <rect x="-160" y="-100" width="46" height="60" class="tealp"/>
    <rect x="-100" y="-90" width="46" height="50" class="coralp"/>
    <rect x="-40" y="-104" width="46" height="64" class="goldp"/>
    <rect x="20" y="-92" width="46" height="52" class="violetp"/>
  </g>
</g>
<g transform="translate(470 240)">
  <circle r="46" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
  <path d="M-30 30L30-30" stroke="{TONES['coral'][0]}" stroke-width="8" fill="none"/>
  <g fill="{MUTED}"><rect x="-24" y="-9" width="48" height="18" rx="9"/></g>
</g>
{person(120, 380, 0.85, 1, 'coral', 'blue', 'reach', 'bun', 'smile')}''', ground=False)

add('draw', '両者が同じ点で引き分けになる', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-10 0h20v170h-20z" fill="#8f9aa6" class="o"/>
  <path d="M-70 170h140v20h-140z" fill="#8f9aa6" class="o"/>
  <path d="M-200-8h400v16h-400z" fill="#b8bfc8" class="o"/>
  <circle r="16" fill="#8f9aa6" class="o"/>
  <path d="M-190 8v40M190 8v40" stroke="{INK}" stroke-width="3" fill="none"/>
</g>
<g transform="translate(110 248)">
  <path d="M-56 0q0 30 56 30t56-30z" class="tealp o"/>
  <ellipse ry="10" rx="56" class="tealp o"/>
  <circle cy="-16" r="22" class="teal o"/>
</g>
<g transform="translate(490 248)">
  <path d="M-56 0q0 30 56 30t56-30z" class="coralp o"/>
  <ellipse ry="10" rx="56" class="coralp o"/>
  <circle cy="-16" r="22" class="coral o"/>
</g>
<g fill="{INK}">
  <rect x="256" y="306" width="88" height="16" rx="8"/>
  <rect x="256" y="336" width="88" height="16" rx="8"/>
</g>''', ground=False)

add('drip', '蛇口からしずくが一滴ずつ落ちる', f'''
<path d="M0 0h600v400H0z" fill="#e8eef2"/>
<g transform="translate(300 150)">
  <path d="M-14-60h28v40h-28z" fill="#b8bfc8" class="o"/>
  <path d="M-14-60q0-34 50-34h44v24h-36q-36 0-36 26z" fill="#c8d0d8" class="o"/>
  <path d="M-40-20h52q10 0 10 12t-10 12h-52q-10 0-10-12t10-12z" fill="#9aa5b0" class="o"/>
</g>
<g fill="{TONES['blue'][0]}">
  <path d="M266 190q10 12 10 20t-10 8-10-8 10-20z"/>
  <path d="M264 260q9 11 9 18t-9 7-9-7 9-18z"/>
  <path d="M266 320q9 11 9 18t-9 7-9-7 9-18z"/>
</g>
<g transform="translate(280 370)">
  <path d="M-160-20h320v40h-320z" fill="#c8d0d8" class="o"/>
  <ellipse cy="-20" rx="60" ry="12" fill="{TONES['blue'][1]}" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M400 180v170"/></g>''', ground=False)

add('dash', '合図と同時に短い距離を全力で駆け出す', f'''
{table(380)}
<path d="M0 340h600v40H0z" fill="#c8703a" class="o"/>
<g fill="none" stroke="#fffefd" stroke-width="4"><path d="M0 360h600"/></g>
{person(380, 360, 1.2, 1, 'coral', 'blue', 'walk', 'cap', 'neutral', 'walk')}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round">
  <path d="M120 240h130M100 290h100M140 330h120"/>
</g>
<g transform="translate(80 160)">
  <path d="M-30-30h60v60h-60z" fill="#5a6270" class="o"/>
  <path d="M0-30v-30" stroke="{INK}" stroke-width="5" fill="none"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M130 150q26 26 0 52M160 130q40 46 0 92"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M450 220h110"/></g>''', ground=False)

# --- d- の形容詞 ---------------------------------------------------------------
add('deceitful', '本当は知っているのに知らないふりをする', f'''
{table(380)}
{person(200, 380, 1.15, 1, 'violet', 'blue', 'up', 'short', 'smile')}
<g transform="translate(330 160)">
  <path d="M-60-40h120q12 0 12 12v40q0 12-12 12h-80l-20 16v-16q-12 0-12-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <path d="M-30-16l60 40M30-16l-60 40" stroke="{MUTED}" stroke-width="6" fill="none"/>
</g>
<g transform="translate(330 290)">
  <path d="M-60-36h120q12 0 12 12v36q0 12-12 12h-80l-20 16v-16q-12 0-12-12v-36q0-12 12-12z" fill="#fffefd" class="o" opacity="0.85"/>
  <g fill="{TONES['coral'][0]}"><rect x="-40" y="-8" width="80" height="16" rx="8"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 6"><path d="M270 240v40"/></g>
{cross(510, 200, 0.7)}''', ground=False)

add('deceptive', '浅く見える池が、実はとても深い', f'''
<path d="M0 0h600v170H0z" fill="#dceaf4"/>
<path d="M0 170h600v230H0z" fill="#7aa8c4"/>
<path d="M0 170h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="#a8c8dd" stroke-width="4"><path d="M40 210h200M360 210h200"/></g>
<path d="M0 400V330h140l60-140h200l60 140h140v70z" fill="#5b7a94" class="o"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M40 240h520"/></g>
{person(120, 170, 0.85, 1, 'coral', 'blue', 'up', 'bob', 'smile')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M300 200v130"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M400 120l24-20M430 90l6-24"/>
</g>''', ground=False)

add('definitive', 'いくつもの案を経て、これで決まりという最終版', f'''
{table(380)}
<g>
''' + ''.join(f'<g transform="translate({120+i*70} {250}) rotate({-14+i*8})" opacity="0.45">{doc(0, 0, 90, 110, 3)}</g>' for i in range(3)) + f'''
</g>
<g transform="translate(430 240)">
  {doc(0, 0, 150, 190, 4)}
  <circle cx="46" cy="62" r="26" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M300 150h90"/></g>
{tick(430, 110, 0.6)}''', ground=False)

add('derogatory', '相手をけなす言葉を投げつける', f'''
{table(380)}
{person(170, 380, 1.1, 1, 'violet', 'blue', 'point', 'short', 'sad')}
{person(450, 380, 1.05, -1, 'coral', 'blue', 'stand', 'bob', 'sad')}
<g transform="translate(310 180)">
  <path d="M-80-46l16 16-16 16 16 16-16 16h160l-16-16 16-16-16-16 16-16z" fill="#fffefd" class="o"/>
  <g fill="{TONES['coral'][0]}"><rect x="-46" y="-9" width="92" height="18" rx="9"/></g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M250 270h130"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M410 250q-14 10-14 26"/>
</g>''', ground=False)

add('descriptive', '見たままを細かく書き写す', f'''
{table(380)}
<g transform="translate(160 230)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <circle cx="-30" cy="-30" r="30" class="goldp o"/>
  <path d="M-80 70L-20-10l30 34 40-54 50 100z" class="greenp o"/>
</g>
<g transform="translate(430 220)">
  {doc(0, 0, 180, 230, 6)}
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 220h50"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M270 300h70"/></g>''', arrow=True, ground=False)

add('desolate', '住む人のいない、荒れ果てた家と土地', f'''
<path d="M0 0h600v250H0z" fill="#b6bcc2"/>
<path d="M0 250h600v150H0z" fill="#9a9d94" class="o"/>
<g fill="none" stroke="#868a80" stroke-width="4"><path d="M0 300q140-20 300 0t300-14M0 350q160-16 300 8t300-16"/></g>
<g transform="translate(300 250)">
  <path d="M-90 0v-90h180V0z" fill="#a89880" class="o"/>
  <path d="M-104-90L0-140l104 50z" fill="#8f8574" class="o"/>
  <path d="M-60-70h40v40h-40z" fill="#5a5a52"/>
  <path d="M10-50h40V0H10z" fill="#5a5a52"/>
  <path d="M-40-30l30 30M40-70l-30 30" stroke="#7d7d72" stroke-width="4" fill="none"/>
</g>
<g fill="#7f8378"><path d="M470 250v-40h6v40zM484 250v-56h6v56z"/></g>
<g fill="#868a80" class="o"><ellipse cx="130" cy="320" rx="30" ry="16"/></g>''', ground=False)

add('despicable', '弱い立場の人からお金を取り上げる', f'''
{table(380)}
{person(200, 380, 1.15, 1, 'violet', 'blue', 'reach', 'short', 'neutral')}
{person(440, 380, 0.9, -1, 'coral', 'blue', 'up', 'bob', 'sad')}
{coin(320, 250, 22)}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M400 210H290"/></g>
{cross(520, 150, 0.8)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M480 260l24-18M500 310h26"/>
</g>''', ground=False)

add('detrimental', '毎日のたばこが体に悪い影響を与える', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-90-14h140v28h-140z" fill="#fffdf6" class="o"/>
  <path d="M50-14h40v28H50z" class="corald o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" opacity="0.8">
    <path d="M-100-20q-14-24 0-44M-70-30q-14-26 0-48"/>
  </g>
</g>
<g transform="translate(450 250)">
  <path d="M0-70q40-40 70 0 20 40-70 100-90-60-70-100 30-40 70 0z" fill="#c8a0a0" class="o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="5">
    <path d="M-40 0l30 20-20 20"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M270 250h60"/></g>
{cross(450, 130, 0.6)}''', ground=False)

add('devious', 'まっすぐ行かず、裏の道を回って手に入れる', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v170H0z" fill="#c9d8c0"/>
<path d="M0 230h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(500 300)">
  <path d="M-50-50h100v100h-100z" class="goldp o"/>
  <path d="M-50-50l12-16h100l-12 16z" fill="{TONES['gold'][1]}" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="14 12"><path d="M120 300h300"/></g>
{cross(270, 300, 0.6)}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M120 320q40-160 190-140t130 90"/></g>
{person(90, 380, 0.9, 1, 'violet', 'blue', 'walk', 'cap', 'neutral', 'walk')}''', ground=False)

add('devoid', '中身がまったくなく、からっぽの器', f'''
{split()}
{table(340)}
<g transform="translate(150 260)">
  <path d="M-80-60h160v90q0 18-80 18t-80-18z" fill="#e8f0f6" class="o"/>
  <path d="M-70-20h140v50q0 12-70 12t-70-12z" fill="{TONES['blue'][0]}"/>
  <path d="M-70-20h140" stroke="{TONES['blue'][2]}" stroke-width="3" fill="none"/>
</g>
<g transform="translate(450 260)">
  <path d="M-80-60h160v90q0 18-80 18t-80-18z" fill="#e8f0f6" class="o"/>
  <path d="M-80-60h160" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>
{cross(450, 130, 0.7)}
<g class="a" marker-end="url(#ar)"><path d="M270 260h60"/></g>''', arrow=True, ground=False)

add('diligent', '毎日欠かさず机に向かって積み上げる', f'''
{table(380)}
{sit(200, 380, 1.1, 1, 'teal', 'blue', 'bun', 'neutral', 'lap')}
{chair(200, 380, 1.05, 'gold', 1)}
<g transform="translate(250 290)">{doc(0, 0, 120, 90, 3)}</g>
<g transform="translate(430 300)">
  <path d="M-120-20h240v20h-240z" fill="#c9a464" class="o"/>
  <g class="teal o">
''' + ''.join(f'<rect x="{-100+i*40}" y="{-40-i*20}" width="32" height="{20+i*20}"/>' for i in range(5)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M330 160h180"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M330 200h180"/></g>''', ground=False)

add('disgraceful', 'みんなの前でごみを投げ捨てて非難される', f'''
{table(380)}
{person(200, 380, 1.1, 1, 'violet', 'blue', 'up', 'short', 'neutral')}
<g transform="translate(320 300) rotate(24)">
  <path d="M-30-24q30-20 60 0 6 26-16 34-32 6-48-10-4-16 4-24z" fill="#e8e2d6" class="o"/>
</g>
<g transform="translate(430 340)">
  <path d="M-50-40h100l-10 70q-2 12-40 12t-40-12z" fill="#6f7b88" class="o"/>
  <path d="M-58-40h116v-12h-116z" fill="#8f9aa6" class="o"/>
</g>
{cross(320, 240, 0.5)}
{head(90, 300, 20, 'coral', 'bob')}
{head(540, 250, 20, 'teal', 'short')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M120 250l-24-18M510 200l-24-18"/>
</g>''', ground=False)

add('dispensable', 'なくても困らない品と、欠かせない品', f'''
{split()}
{table(380)}
<g transform="translate(150 270)">
  <path d="M-50-40h100v80h-100z" class="goldp o"/>
</g>
{cross(150, 150, 0.7)}
<g transform="translate(450 270)">
  <path d="M-50-40h100v80h-100z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="6"><circle cx="450" cy="270" r="76" stroke-dasharray="12 10"/></g>
{tick(450, 150, 0.7)}''', ground=False)

add('disposable', '一度使って捨てるコップと、洗って使うコップ', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-40-50h80l-10 90q-2 12-30 12t-30-12z" fill="#fffdf6" class="o"/>
  <path d="M-36-20h72" fill="none" stroke="{MUTED}" stroke-width="3"/>
</g>
<g transform="translate(150 350)">
  <path d="M-40-30h80l-8 50q-2 10-32 10t-32-10z" fill="#6f7b88" class="o"/>
  <path d="M-46-30h92v-10h-92z" fill="#8f9aa6" class="o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M150 320v-20"/></g>
<g transform="translate(450 250)">
  <path d="M-40-50h80v90q0 12-40 12t-40-12z" fill="#e8f0f6" class="o"/>
  <path d="M40-30q34 0 34 22t-34 22" fill="none" stroke="{INK}" stroke-width="7"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}"><path d="M520 320q40-60 0-120"/></g>''', ground=False)

add('divisive', 'ひとつの案が人を二つに割ってしまう', f'''
{table(380)}
<g transform="translate(300 130)">
  {doc(0, 0, 140, 100, 3)}
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-dasharray="16 12"><path d="M300 200v180"/></g>
{head(110, 280, 24, 'teal', 'short')}
{head(190, 320, 24, 'gold', 'bun')}
{head(410, 280, 24, 'coral', 'bob')}
{head(490, 320, 24, 'violet', 'cap')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M250 230l-80 30"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M350 230l80 30"/></g>''', ground=False)

add('dormant', '冬の間、活動を止めて眠っている種', f'''
{split()}
<path d="M0 0h600v200H0z" fill="#dfe4ea"/>
<path d="M0 200h600v200H0z" fill="#a8845c"/>
<path d="M0 188h600v14H0z" fill="#e8f0f6"/>
<path d="M0 188h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(150 280)">
  <ellipse rx="34" ry="24" fill="#6b4c28" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
''' + ''.join(f'<path d="M{200+i*24} {180-i*24}q16 0 16 12t-16 12h18"/>' for i in range(3)) + f'''
</g>
<path d="M300 0h300v200H300z" fill="#dceaf4"/>
<path d="M300 188h300v14H300z" fill="#c9d8c0"/>
<g transform="translate(450 280)">
  <ellipse rx="34" ry="24" fill="#6b4c28" class="o"/>
  <path d="M0-24v-70" stroke="{TONES['green'][2]}" stroke-width="8" fill="none"/>
  <path d="M0-60q-50-24-42-52 44 6 42 52zM0-88q46-24 56 4-40 24-56-4z" class="greenp o"/>
</g>
{sun(540, 70, 26)}
<g class="a" marker-end="url(#ar)"><path d="M270 300h60"/></g>''', ground=False)

add('drastic', '少し切るのではなく、根元からばっさり切る', f'''
{split()}
{table(380)}
<g transform="translate(150 380)">
  <path d="M-20 0v-140h40V0z" fill="{BRN}" class="o"/>
  <g class="greenp o"><circle cx="-40" cy="-180" r="46"/><circle cx="26" cy="-200" r="52"/><circle cx="70" cy="-166" r="40"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><path d="M-90-210h180"/></g>
</g>
<g transform="translate(450 380)">
  <path d="M-20 0v-50h40V0z" fill="{BRN}" class="o"/>
  <ellipse cy="-50" rx="20" ry="8" fill="#c9a464" class="o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><path d="M-90-50h180"/></g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M270 200h60"/></g>''', ground=False)

add('drowsy', '本を持ったまま目が半分閉じてうとうとする', f'''
{table(380)}
{sit(260, 380, 1.15, 1, 'blue', 'blue', 'short', 'neutral', 'lap')}
{chair(260, 380, 1.05, 'gold', 1)}
<g transform="translate(310 280) rotate(14)">
  <path d="M-56-40h112v80h-112z" fill="#fffefd" class="o"/>
  <path d="M0-40v80" stroke="{INK}" stroke-width="3" fill="none"/>
</g>
<g transform="translate(260 250) rotate(10)">
  <path d="M-30-6q14 12 28 0M2-6q14 12 28 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round" transform="translate(-6 0)"/>
</g>
<g fill="{MUTED}">
''' + ''.join(f'<path d="M{360+i*40} {200-i*40}q18 0 18 14t-18 14h20" fill="none" stroke="{MUTED}" stroke-width="{4+i}"/>' for i in range(3)) + f'''
</g>''', ground=False)

add('dubious', '差し出された話に半信半疑で眉を寄せる', f'''
{table(380)}
{person(430, 380, 1.05, -1, 'gold', 'blue', 'give', 'short', 'smile')}
{person(180, 380, 1.15, 1, 'teal', 'blue', 'stand', 'bun', 'neutral')}
<g transform="translate(180 250)">
  <path d="M-24-14q12-10 22 0" fill="none" stroke="{HAIR}" stroke-width="5" stroke-linecap="round"/>
  <path d="M4-18q12-6 22 4" fill="none" stroke="{HAIR}" stroke-width="5" stroke-linecap="round"/>
  <path d="M-10 22q10 6 20-2" fill="none" stroke="{INK}" stroke-width="3.5"/>
</g>
<g transform="translate(320 250)">{doc(0, 0, 110, 130, 3)}</g>
<g transform="translate(150 150)">
  <path d="M-36-30h72q10 0 10 10v30q0 10-10 10h-46l-18 14v-14q-18 0-18-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M-14-18q0-14 14-14t14 14-14 12v8" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <circle cy="14" r="3.5" fill="{INK}"/>
</g>''', ground=False)

# --- e- の形容詞 ---------------------------------------------------------------
add('ecstatic', '知らせを聞いて跳び上がって狂喜する', f'''
<path d="M0 0h600v400H0z" fill="#fff6e0"/>
{table(380)}
<g transform="translate(300 320)">
  <path d="M-12-8l-36 30M12-8l38 26" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-27-78q27-14 54 0l-8 72h-38z" class="coral o"/>
  <path d="M-22-70l-34-34M22-70l34-34" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cy="-108" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['bun']}" transform="translate(0 4) scale(1.06)" fill="{HAIR}"/>
  <circle cx="-9" cy="-104" r="2.4" fill="{INK}"/><circle cx="9" cy="-104" r="2.4" fill="{INK}"/>
  <path d="M-14-92q14 18 28 0z" fill="{INK}" class="o"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="6" stroke-linecap="round">
''' + ''.join(f'<path d="M{300+160*math.cos(3.4+i*0.42):.0f} {230+160*math.sin(3.4+i*0.42):.0f}l{24*math.cos(3.4+i*0.42):.0f} {24*math.sin(3.4+i*0.42):.0f}"/>' for i in range(9)) + f'''
</g>
<g class="o">
''' + ''.join(f'<circle cx="{100+i*90}" cy="{70+(i%3)*36}" r="11" class="{["coral","teal","violet","gold"][i%4]}"/>' for i in range(6)) + f'''
</g>''', ground=False)

add('elated', '足取りが軽く、宙に浮くように喜ぶ', f'''
<path d="M0 0h600v400H0z" fill="#fff6e0"/>
{table(380)}
{person(300, 320, 1.15, 1, 'teal', 'gold', 'up', 'cap', 'smile')}
<g fill="none" stroke="{MUTED}" stroke-width="3"><ellipse cx="300" cy="374" rx="50" ry="9"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['gold'][0]}" stroke-width="5"><path d="M300 360v-40"/></g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M190 220l-24-20M410 216l24-20M170 280l-30-6M430 276l30-6"/>
</g>
<g fill="{TONES['gold'][1]}" opacity="0.5"><ellipse cx="300" cy="240" rx="130" ry="120"/></g>''', ground=False)

add('enraged', '顔を真っ赤にして激しく怒る', f'''
{table(380)}
{person(300, 380, 1.25, 1, 'coral', 'blue', 'up', 'short', 'sad')}
<g transform="translate(300 245)">
  <circle r="30" class="coral" opacity="0.45"/>
  <path d="M-26-16q14-10 24 0M2-16q14-10 24 0" fill="none" stroke="{HAIR}" stroke-width="5" stroke-linecap="round" transform="translate(-2 0)"/>
  <path d="M-12 14q12 12 24 0z" fill="{INK}" class="o"/>
</g>
<g fill="{MUTED}" opacity="0.85">
''' + ''.join(f'<circle cx="{244-i*22}" cy="{200-i*24}" r="{8+i*3}"/>' for i in range(3)) + f'''
''' + ''.join(f'<circle cx="{356+i*22}" cy="{200-i*24}" r="{8+i*3}"/>' for i in range(3)) + f'''
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M170 190l-30-26M430 186l30-26M160 280l-34-8M440 276l34-8"/>
</g>''', ground=False)

add('edgy', '落ち着かず、指をかんでそわそわする', f'''
{table(380)}
{sit(300, 380, 1.15, 1, 'violet', 'blue', 'short', 'sad', 'up')}
{chair(300, 380, 1.05, 'gold', 1)}
<g transform="translate(300 250)">
  <path d="M-24-8q12-12 22 0M2-8q12-12 22 0" fill="none" stroke="{HAIR}" stroke-width="4.5" stroke-linecap="round" transform="translate(-2 0)"/>
  <path d="M-8 20h16" fill="none" stroke="{INK}" stroke-width="3.5"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M200 240q-14 10-14 26M400 236q14 10 14 26M190 300q-20 8-24 22M410 296q20 8 24 22"/>
</g>
<g transform="translate(470 200)">
  <circle r="44" fill="#fffdf6" class="o"/>
  <path d="M0 0v-28M0 0l20 12" stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none"/>
</g>
<g fill="{TONES['blue'][0]}"><path d="M240 224q9 10 9 17t-9 8-9-8 9-17z"/></g>''', ground=False)

add('edible', '食べられるきのこと、食べられないきのこ', f'''
{split()}
{table(380)}
<g transform="translate(150 300)">
  <path d="M-24-40h48l-6 40q-2 12-18 12t-18-12z" fill="#f0e6d0" class="o"/>
  <path d="M-70-40q0-56 70-56t70 56z" fill="#c8934a" class="o"/>
  <g fill="#a8763a"><circle cx="-30" cy="-58" r="8"/><circle cx="20" cy="-66" r="7"/></g>
</g>
{tick(150, 150, 0.7)}
<g transform="translate(450 300)">
  <path d="M-24-40h48l-6 40q-2 12-18 12t-18-12z" fill="#f0e6d0" class="o"/>
  <path d="M-70-40q0-56 70-56t70 56z" class="violet o"/>
  <g fill="#fffdf6"><circle cx="-30" cy="-58" r="9"/><circle cx="20" cy="-66" r="8"/><circle cx="46" cy="-50" r="7"/></g>
</g>
{cross(450, 150, 0.7)}''', ground=False)

add('effortless', '力まずに軽々と持ち上げる', f'''
{split()}
{table(380)}
{person(150, 380, 1.05, 1, 'blue', 'blue', 'up', 'short', 'sad')}
<g fill="{INK}"><g transform="translate(150 230)"><rect x="-56" y="-10" width="112" height="20" rx="8"/><rect x="-80" y="-30" width="24" height="60" rx="10"/><rect x="56" y="-30" width="24" height="60" rx="10"/></g></g>
<g fill="{TONES['blue'][0]}"><path d="M104 264q9 10 9 17t-9 8-9-8 9-17z"/></g>
{person(450, 380, 1.05, 1, 'coral', 'blue', 'up', 'cap', 'smile')}
<g fill="{INK}"><g transform="translate(450 230)"><rect x="-56" y="-10" width="112" height="20" rx="8"/><rect x="-80" y="-30" width="24" height="60" rx="10"/><rect x="56" y="-30" width="24" height="60" rx="10"/></g></g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M540 260l-24-18M550 310h-26"/>
</g>''', ground=False)

add('elastic', '引っぱると伸び、放すと元に戻るゴム', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <ellipse rx="50" ry="34" fill="none" stroke="{TONES['coral'][0]}" stroke-width="16"/>
</g>
<g transform="translate(450 250)">
  <ellipse rx="120" ry="20" fill="none" stroke="{TONES['coral'][0]}" stroke-width="11"/>
</g>
{hand(340, 250, -1)}
{hand(560, 250, 1)}
<g class="a" marker-end="url(#ar)" stroke="{MUTED}"><path d="M270 250h60"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}"><path d="M480 340q60-40 0-60"/></g>''', arrow=True, ground=False)

add('eminent', '大勢の中でだれもが知る、名の通った人', f'''
{table(380)}
<g>
''' + ''.join(head(70+ (i%5)*54, 300+(i//5)*60, 18, 'blue', ['short','bob','bun','cap'][i%4]) for i in range(8)) + f'''
</g>
{person(430, 380, 1.15, 1, 'coral', 'gold', 'up', 'bun', 'smile')}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{430+140*math.cos(3.4+i*0.44):.0f} {240+140*math.sin(3.4+i*0.44):.0f}l{20*math.cos(3.4+i*0.44):.0f} {20*math.sin(3.4+i*0.44):.0f}"/>' for i in range(8)) + f'''
</g>
<g transform="translate(430 130)">
  <path d="M-40-14h80v14h-80z" class="gold o"/>
  <path d="M-40-14l-8-44 22 20 18-30 18 30 22-20-8 44z" class="gold o"/>
</g>''', ground=False)

add('emphatic', '首を強く横に振ってきっぱり断る', f'''
{table(380)}
{person(300, 380, 1.2, 1, 'teal', 'blue', 'up', 'short', 'neutral')}
<g transform="translate(300 240)">
  <path d="M-14 16h28" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <path d="M-26-16q14-10 24 0M2-16q14-10 24 0" fill="none" stroke="{HAIR}" stroke-width="5" stroke-linecap="round" transform="translate(-2 0)"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M250 190h-70"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M350 190h70"/></g>
<g transform="translate(470 300)">
  <path d="M-50-36h100q12 0 12 12v36q0 12-12 12h-64l-20 16v-16q-12 0-12-12v-36q0-12 12-12z" fill="#fffefd" class="o"/>
  {cross(0, -4, 0.35)}
</g>''', ground=False)

add('climatic', '長い年月の平均から見た、その土地の気候', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(300 250)">
  <path d="M-250 100h500v6h-500z" fill="{INK}"/>
  <path d="M-250-180v280h6v-280z" fill="{INK}"/>
  <path d="M-230 40q60-90 120-100t120 60 110-40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
  <g class="blue o">
''' + ''.join(f'<rect x="{-220+i*44}" y="{40+ (i%4)*-14}" width="30" height="{60-(i%4)*-14}"/>' for i in range(11)) + f'''
  </g>
</g>
{sun(80, 70, 26)}
{cloud(480, 80, 0.9, 'blue')}
<g class="a" marker-end="url(#ar)"><path d="M70 340h460"/></g>''', arrow=True, ground=False)

add('diagnostic', '検査の結果から原因を突き止める', f'''
{table(380)}
<g transform="translate(200 220)">
  <path d="M-120-120h240v240h-240z" fill="#2c3542" class="o"/>
  <g fill="#c8d4dc" opacity="0.9">
    <path d="M-26-100h52v36q0 16-16 22v100q0 16 16 22v36h-52v-36q16-6 16-22V-42q0-16-16-22z"/>
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M-26 34l52 14"/></g>
  <circle cy="40" r="40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"/>
</g>
{person(470, 380, 1.0, -1, 'teal', 'teal', 'point', 'bun', 'neutral')}
<g transform="translate(430 190)">
  {doc(0, 0, 120, 130, 3)}
  {tick(0, 42, 0.35)}
</g>''', ground=False)

# --- 慣用表現 ----------------------------------------------------------------
add('depend-on', '橋の一本の綱にすべてがかかっている', f'''
<path d="M0 0h600v250H0z" fill="#dceaf4"/>
<path d="M0 250h600v150H0z" fill="#c9d8c0"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M0 300h140v100H0zM460 300h140v100H460z" fill="#a8845c" class="o"/>
<path d="M140 300h320v20H140z" fill="#c9a464" class="o"/>
<g fill="none" stroke="{BRN}" stroke-width="8"><path d="M140 300q160 60 320 0"/></g>
<g fill="none" stroke="{BRN}" stroke-width="5">
''' + ''.join(f'<path d="M{170+i*40} {300+ int(60*(1-((i*40-160)/160)**2)*0.45)}v-{int(60*(1-((i*40-160)/160)**2)*0.45)}"/>' for i in range(8)) + f'''
</g>
{person(300, 300, 0.85, 1, 'coral', 'blue', 'walk', 'cap', 'neutral', 'walk')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M300 180v60"/></g>''', ground=False)

add('in-brief', '長い報告を、要点だけの短い形で伝える', f'''
{split()}
{table(380)}
<g transform="translate(150 220)">
  <path d="M-100-130h200v260h-200z" class="paper"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-76" y="{-104+i*26}" width="{152-(i%3)*40}" height="9" rx="4.5"/>' for i in range(9)) + f'''
  </g>
</g>
<g transform="translate(450 220)">
  <path d="M-100-50h200v100h-200z" class="paper"/>
  <g fill="{INK}">
    <rect x="-76" y="-26" width="152" height="14" rx="7"/>
    <rect x="-76" y="2" width="110" height="14" rx="7"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 220h60"/></g>
{person(560, 380, 0.7, -1, 'teal', 'blue', 'point', 'bun', 'smile')}''', arrow=True, ground=False)

add('in-practice', '図面のうえの計画と、実際にやってみた結果', f'''
{split()}
{table(380)}
<g transform="translate(150 230)">
  <path d="M-110-120h220v240h-220z" fill="#e1edfb" class="o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3">
    <path d="M-70 90V-40l70-50 70 50v130z"/><path d="M-30 90V30h30v60M20 20h40v40H20z"/>
''' + ''.join(f'<path d="M{-100+i*24} -110v220"/>' for i in range(9)) + f'''
  </g>
</g>
<g transform="translate(450 300)">
  <path d="M-90 0v-90h180V0z" fill="#fffdf6" class="o"/>
  <path d="M-104-90L0-140l104 50z" class="coral o"/>
  <path d="M-20-50h40V0h-40z" class="corald o"/>
  <path d="M-60-64h34v28h-34z" class="bluep o"/>
  <path d="M40-70l24 20" stroke="{TONES['coral'][0]}" stroke-width="4" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
