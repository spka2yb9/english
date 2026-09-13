# -*- coding: utf-8 -*-
"""第140回。e-/f- の形容詞と身のまわりの名詞。"""
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
add('fin', '魚の背と尾についた薄いひれ', f'''
<path d="M0 0h600v120H0z" fill="#dceaf4"/>
<path d="M0 120h600v280H0z" fill="#7aa8c4"/>
<path d="M0 120h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 250)">
  <path d="M-110 0q40-60 110-60t100 60q-30 60-100 60t-110-60z" fill="#b8c8d4" class="o"/>
  <path d="M100 0l70-40v80z" fill="#8fa4b4" class="o"/>
  <path d="M-10-56q10-60 50-70-6 46-20 68z" fill="#8fa4b4" class="o"/>
  <path d="M-20 52q0 50 34 64-24-30-20-62z" fill="#8fa4b4" class="o"/>
  <circle cx="-60" cy="-12" r="7" fill="{INK}"/>
  <path d="M-40 10q30 14 60 0" fill="none" stroke="#8fa4b4" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 90l100 60"/></g>
<g class="a" marker-end="url(#ar)"><path d="M470 60l-90 90"/></g>''', arrow=True, ground=False)

add('fireplace', '部屋の壁にある、火をたく炉', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<path d="M0 350h600v50H0z" fill="#c9a464" class="o"/>
<g transform="translate(300 240)">
  <path d="M-160-130h320v240h-320z" fill="#c8b8a0" class="o"/>
  <g fill="none" stroke="#a89880" stroke-width="3">
''' + ''.join(f'<path d="M-160 {-100+i*46}h320"/>' for i in range(5)) + f'''
  </g>
  <path d="M-100-60h200v170h-200z" fill="#2c2420" class="o"/>
  <path d="M-176-130h352v-26h-352z" fill="#a89880" class="o"/>
  {flame(0, 80, 1.0)}
  <g fill="#8b6437"><path d="M-70 96h140v14h-140z"/></g>
</g>
<g fill="{TONES['gold'][1]}" opacity="0.25"><path d="M300 240l-240 130h480z"/></g>''', ground=False)

add('flute', '横に構えて穴をふさぎ息を吹き込む笛', f'''
{table(380)}
<g transform="translate(300 240) rotate(-6)">
  <path d="M-200-12h400v24h-400z" fill="#c8d0d8" class="o"/>
  <path d="M-200-14h30v28h-30z" fill="#8f9aa6" class="o"/>
  <path d="M170-16h30v32h-30z" fill="#8f9aa6" class="o"/>
  <g fill="#8f9aa6" class="o">
''' + ''.join(f'<circle cx="{-120+i*44}" r="11"/>' for i in range(7)) + f'''
  </g>
  <ellipse cx="-150" ry="8" rx="12" fill="{INK}"/>
</g>
{hand(220, 320, 1)}
{hand(400, 320, -1)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M480 160q26 30 0 60M516 136q40 52 0 104"/>
</g>''', ground=False)

add('exchange-rate', '通貨どうしを交換する比率が表に出ている', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-200-140h400v280h-400z" fill="#3b4450" class="o"/>
  <path d="M-180-120h360v240h-360z" fill="#1c2530"/>
  <g>
''' + ''.join(f'''<g transform="translate(0 {-80+i*56})">
  <rect x="-150" y="-11" width="70" height="22" rx="8" fill="{TONES['gold'][0]}"/>
  <path d="M-60 0h30" stroke="{MUTED}" stroke-width="4"/>
  <rect x="-14" y="-11" width="70" height="22" rx="8" fill="{TONES['teal'][0]}"/>
  <rect x="80" y="-11" width="70" height="22" rx="8" fill="{TONES['green'][0]}"/>
</g>''' for i in range(3)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['gold'][0]}"><path d="M120 340h100"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['teal'][0]}"><path d="M220 366H120"/></g>''', ground=False)

add('fossil-fuel', '地中の化石からできた石炭と石油を燃やす', f'''
<path d="M0 0h600v170H0z" fill="#dceaf4"/>
<path d="M0 170h600v230H0z" fill="#a8845c"/>
<path d="M0 158h600v14H0z" fill="#dfe8d8"/>
<path d="M0 158h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="#8f6f4a" stroke-width="3"><path d="M0 240h600M0 320h600"/></g>
<g transform="translate(160 290)">
  <path d="M-70 40q-20-50 20-70 50-24 90 6 20 40-20 60-60 20-90 4z" fill="#2c2420" class="o"/>
  <g fill="#4a4038"><path d="M-30-14l24 10-18 18z"/><path d="M20 6l20 8-14 14z"/></g>
</g>
<g transform="translate(400 300)">
  <path d="M-60 30q-16-50 16-64 44-18 74 8 14 34-20 48-52 14-70 8z" fill="#3b3228" class="o"/>
  <ellipse cx="20" cy="0" rx="24" ry="14" fill="#5a4a3c"/>
</g>
{flame(500, 130, 0.7)}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M420 240q40-60 60-70"/></g>''', ground=False)

add('freelance', '会社に属さず、いくつもの相手と契約して働く', f'''
{table(380)}
{person(300, 380, 1.1, 1, 'coral', 'blue', 'reach', 'bun', 'smile')}
<g transform="translate(300 250)">
  <path d="M-70-46h140v92h-140z" fill="#3b4450" class="o"/>
  <path d="M-60-36h120v72h-120z" fill="#dceaf4"/>
</g>
<g>
''' + ''.join(f'<g transform="translate({[110,110,490,490][i]} {[150,320,150,320][i]})"><path d="M-60-36h120v72h-120z" fill="#e0d6c0" class="o"/><path d="M-60-36h120v-14h-120z" class="{["teal","coral","gold","violet"][i]} o"/></g>' for i in range(4)) + f'''
</g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8">
  <path d="M230 220l-70-40M230 300l-70 30M370 220l70-40M370 300l70 30"/>
</g>''', ground=False)

add('alteration', '仕立て直しですそを詰めて形を変える', f'''
{split()}
{table(380)}
<g transform="translate(150 200)">
  <path d="M-70-90h140v50l-16 190h-48l-2-100-2 100h-48l-16-190z" class="bluep o"/>
  <path d="M-70-40h140" fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><path d="M-56 110h112"/></g>
</g>
<g transform="translate(450 200)">
  <path d="M-70-90h140v50l-10 130h-48l-2-70-2 70h-48l-10-130z" class="bluep o"/>
  <path d="M-70-40h140" fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-dasharray="10 6"><path d="M-46 76h92"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

# --- e- の形容詞 ---------------------------------------------------------------
add('enviable', 'みんなが欲しがる、うらやましい賞', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-40 44h80v18h-80z" class="gold o"/>
  <path d="M-40 44l-10-70 30 26 20-40 20 40 30-26-10 70z" class="gold o"/>
  <circle cy="-10" r="12" class="corald"/>
</g>
<circle cx="300" cy="200" r="120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
{head(90, 320, 22, 'teal', 'short')}
{head(200, 350, 22, 'gold', 'bun')}
{head(400, 350, 22, 'violet', 'cap')}
{head(510, 320, 22, 'green', 'bob')}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7">
  <path d="M120 290l100-40M230 320l50-40M370 320l-50-40M480 290l-100-40"/>
</g>''', ground=False)

add('envious', '人の持ち物を見て、うらやましさで顔がくもる', f'''
{table(380)}
{person(180, 380, 1.1, 1, 'coral', 'blue', 'hold', 'bun', 'smile')}
<g transform="translate(220 270)">
  <path d="M-40-30h80v60h-80z" class="goldp o"/>
  <path d="M-40-30l10-14h80l-10 14z" fill="{TONES['gold'][1]}" class="o"/>
</g>
{person(450, 380, 1.15, -1, 'green', 'green', 'stand', 'short', 'sad')}
<g fill="{TONES['green'][0]}" opacity="0.45"><ellipse cx="450" cy="250" rx="36" ry="28"/></g>
<g transform="translate(450 250)">
  <path d="M-24-8q12-10 20 0M2-8q12-10 20 0" fill="none" stroke="{HAIR}" stroke-width="4" stroke-linecap="round" transform="translate(-2 0)"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M410 250l-130 10"/></g>
<circle cx="450" cy="270" r="90" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('equitable', '働いた分に応じて、公平に分ける', f'''
{split()}
{table(380)}
<g transform="translate(150 260)">
''' + ''.join(coin(-50+i*50, -20, 18) for i in range(3)) + f'''
''' + ''.join(coin(-50+i*50, -56, 18) for i in range(3)) + f'''
</g>
{head(110, 340, 20, 'teal', 'short')}
{head(190, 340, 20, 'coral', 'bob')}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M150 200v-40"/></g>
<g transform="translate(450 260)">
''' + ''.join(coin(-50+i*50, -20, 18) for i in range(3)) + f'''
''' + ''.join(coin(-50+i*50, -56, 18) for i in range(3)) + f'''
</g>
{head(410 , 340, 20, 'teal', 'short')}
{head(490, 340, 20, 'coral', 'bob')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="5" stroke-dasharray="10 8"><path d="M450 180v-40"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="6"><path d="M410 200h80"/></g>
<circle cx="450" cy="270" r="120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('erratic', '一定しない、上下にばらばらな動き', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(300 220)">
  <path d="M-250 140h500v6h-500z" fill="{INK}"/>
  <path d="M-250-160v300h6v-300z" fill="{INK}"/>
  <path d="M-230 40l40-100 40 130 40-150 40 90 40-70 40 140 40-120 40 80 40-50" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linejoin="round"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M-244 0h490"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M60 340h480"/></g>''', arrow=True, ground=False)

add('erroneous', '一か所だけ計算が誤っている答え', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <g>
''' + ''.join(f'''<g transform="translate(0 {-96+i*54})">
  <rect x="-140" y="-9" width="150" height="18" rx="9" fill="{MUTED}"/>
  <rect x="40" y="-9" width="{90-(i%3)*20}" height="18" rx="9" fill="{INK if i!=2 else TONES['coral'][0]}"/>
</g>''' for i in range(4)) + f'''
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5">
    <path d="M30 -4l100 44M130 -4L30 40"/>
  </g>
</g>
{cross(500, 130, 0.6)}''', ground=False)

add('evasive', '尋ねられても目をそらしてはっきり答えない', f'''
{table(380)}
{person(150, 380, 1.05, 1, 'teal', 'blue', 'point', 'bun', 'neutral')}
{person(440, 380, 1.15, -1, 'violet', 'blue', 'stand', 'short', 'neutral')}
<g transform="translate(250 170)">
  <path d="M-50-40h100q12 0 12 12v40q0 12-12 12h-66l-20 16v-16q-14 0-14-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <path d="M-16-24q0-18 16-18t16 18-16 14v10" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle cy="18" r="4.5" fill="{INK}"/>
</g>
<g transform="translate(410 250)">
  <path d="M50-34H-50q-12 0-12 12v34q0 12 12 12h66l20 16v-16q14 0 14-12v-34q0-12-12-12z" fill="#fffefd" class="o" opacity="0.65"/>
  <g fill="{MUTED}" opacity="0.7"><rect x="-40" y="-8" width="60" height="14" rx="7"/></g>
</g>
<g transform="translate(440 245)">
  <ellipse cx="-14" rx="13" ry="10" fill="#fffefd" class="o"/><circle cx="-20" r="5" fill="{INK}"/>
  <ellipse cx="14" rx="13" ry="10" fill="#fffefd" class="o"/><circle cx="8" r="5" fill="{INK}"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M470 250l70-40"/></g>''', ground=False)

add('eventful', '一日のうちに次々と出来事が起きる', f'''
{table(380)}
<g transform="translate(300 220)">
  <path d="M-250-10h500v20h-500z" fill="#e0d6c0" class="o"/>
</g>
<g>
''' + ''.join(f'''<g transform="translate({100+i*100} {220})">
  <circle r="18" class="{["coral","teal","gold","violet","green"][i]} o"/>
  <path d="M0-18v{-40-(i%2)*30}" stroke="{INK}" stroke-width="3" fill="none"/>
  <g transform="translate(0 {-72-(i%2)*30})">
    <path d="M-34-24h68v48h-68z" class="paper"/>
    <rect x="-22" y="-7" width="{44-(i%3)*10}" height="14" rx="7" fill="{MUTED}"/>
  </g>
</g>''' for i in range(5)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M60 300h480"/></g>''', arrow=True, ground=False)

add('evocative', '一枚の古い写真が昔の記憶を呼び起こす', f'''
{table(380)}
{person(140, 380, 1.05, 1, 'teal', 'blue', 'hold', 'bun', 'smile')}
<g transform="translate(200 270) rotate(-10)">
  <path d="M-50-40h100v80h-100z" fill="#fffdf6" class="o"/>
  <path d="M-40-30h80v54h-80z" fill="#e0d6c0" class="o"/>
  <circle cx="-16" cy="-12" r="11" class="goldp"/>
  <path d="M-36 24l24-30 18 20 20-26 30 36z" class="greenp"/>
</g>
<g fill="{MUTED}" opacity="0.7">
''' + ''.join(f'<circle cx="{290+i*30}" cy="{200-i*32}" r="{8+i*4}"/>' for i in range(3)) + f'''
</g>
<g transform="translate(450 150)">
  <path d="M-100-70h200v140h-200z" fill="#fffefd" class="o" opacity="0.9"/>
  {sun(60, -40, 20)}
  {tree(-50, 50, 0.7)}
  {person(30, 56, 0.4, 1, 'coral', 'blue', 'up', 'cap', 'smile')}
</g>''', ground=False)

add('excusable', '一度きりの小さな遅刻は大目に見られる', f'''
{table(380)}
{person(180, 380, 1.05, 1, 'coral', 'blue', 'up', 'bob', 'sad')}
{person(450, 380, 1.05, -1, 'teal', 'blue', 'reach', 'short', 'smile')}
<g transform="translate(140 200)">
  <circle r="48" fill="#fffdf6" class="o"/>
  <path d="M0 0v-30M0 0l22 14" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round" fill="none"/>
  <circle r="6" fill="{INK}"/>
</g>
<g transform="translate(330 180)">
  <path d="M-50-36h100q12 0 12 12v36q0 12-12 12h-64l-20 16v-16q-12 0-12-12v-36q0-12 12-12z" fill="#fffefd" class="o"/>
  {tick(0, -4, 0.38)}
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M240 300h140"/></g>''', ground=False)

add('exempt', '全員に課される料金から、一人だけ外される', f'''
{table(380)}
<g>
''' + ''.join(f'<g transform="translate({110+i*100} 250)">{head(0, 0, 24, "blue", ["short","bob","bun","cap"][i%4])}<g transform="translate(0 70)">{coin(0, 0, 18)}</g></g>' for i in range(4)) + f'''
</g>
<g transform="translate(510 250)">
  {head(0, 0, 24, 'coral', 'bun')}
  <g transform="translate(0 70)">
    <circle r="18" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 6"/>
    {cross(0, 0, 0.4)}
  </g>
</g>
<circle cx="510" cy="290" r="82" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('exhaustive', '一つも飛ばさず全項目を確かめ尽くす', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-180-150h360v300h-360z" class="paper"/>
  <g>
''' + ''.join(f'''<g transform="translate(0 {-116+i*46})">
  <rect x="-150" y="-14" width="28" height="28" rx="5" fill="none" stroke="{INK}" stroke-width="3"/>
  <rect x="-108" y="-8" width="{230-(i%3)*40}" height="14" rx="7" fill="{MUTED}"/>
</g>''' for i in range(6)) + f'''
  </g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
''' + ''.join(f'<path d="M-144 {-116+i*46}l8 10 18-22"/>' for i in range(6)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M520 70v260"/></g>''', ground=False)

add('expansive', '窓の外に広々とした景色が開ける', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<g transform="translate(300 200)">
  <path d="M-260-170h520v340h-520z" fill="{BRN}" class="o"/>
  <path d="M-230-140h460v280h-460z" fill="#dceaf4"/>
  <path d="M-230 60h460v80h-460z" fill="#c9d8c0"/>
  <path d="M-230 60h460" stroke="{INK}" stroke-width="2.5" fill="none"/>
  <path d="M-230 20l100-70 80 50 90-70 100 80 90-50v40z" fill="#9aa5b0" class="o"/>
  {sun(150, -90, 26)}
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 350h230"/></g>
<g class="a" marker-end="url(#ar)"><path d="M300 350H70"/></g>''', arrow=True, ground=False)

add('expressive', '顔と手で気持ちがよく伝わる', f'''
{split()}
{table(380)}
{person(150, 380, 1.15, 1, 'blue', 'blue', 'stand', 'short', 'neutral')}
<g transform="translate(150 250)">
  <path d="M-14 16h28" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
</g>
{person(450, 380, 1.15, 1, 'coral', 'blue', 'up', 'bun', 'smile')}
<g transform="translate(450 250)">
  <path d="M-16 12q16 16 32 0z" fill="{INK}" class="o"/>
  <path d="M-26-14q12-10 22 0M4-14q12-10 22 0" fill="none" stroke="{HAIR}" stroke-width="4" stroke-linecap="round"/>
</g>
{hand(380, 190, -1)}
{hand(520, 190, 1)}''', ground=False)

add('factual', '思ったことではなく、確かめた事実を書く', f'''
{split()}
{table(380)}
<g transform="translate(150 220)">
  {doc(0, 0, 180, 220, 5)}
  <path d="M-70 90q40-24 66 0" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<g transform="translate(150 90)">
  <path d="M-40-30h80q10 0 10 10v30q0 10-10 10h-52l-18 14v-14q-10 0-10-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M0-16q18 0 18 16t-10 16v6h-16v-6q-10 0-10-16t18-16z" fill="{MUTED}"/>
</g>
<g transform="translate(450 220)">
  {doc(0, 0, 180, 220, 5)}
</g>
<g transform="translate(450 90)">
  <path d="M-40-30h80q10 0 10 10v30q0 10-10 10h-52l-18 14v-14q-10 0-10-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  {tick(0, -4, 0.32)}
</g>
<circle cx="450" cy="220" r="130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('fearless', '高い所でも平気で足を踏み出す', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
<path d="M0 260h240v140H0z" fill="#a8845c" class="o"/>
<path d="M420 260h180v140H420z" fill="#a8845c" class="o"/>
<path d="M240 250h180v20H240z" fill="#c9a464" class="o"/>
{person(330, 250, 1.0, 1, 'coral', 'blue', 'walk', 'cap', 'smile', 'walk')}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M240 290v90M420 290v90"/></g>
{tick(120, 150, 0.7)}
{sun(520, 70, 28)}''', ground=False)

add('feeble', '力なく、うまく押し開けられない', f'''
{split()}
{table(380)}
{person(150, 380, 1.05, 1, 'coral', 'blue', 'reach', 'bun', 'sad')}
<g transform="translate(250 250)">
  <path d="M-30-120h60v240h-60z" fill="{BRN}" class="o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}" stroke-width="3"><path d="M210 250h20"/></g>
{person(450, 380, 1.05, 1, 'teal', 'blue', 'reach', 'cap', 'neutral')}
<g transform="translate(550 250) rotate(14)">
  <path d="M-30-120h60v240h-60z" fill="{BRN}" class="o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="6"><path d="M505 250h55"/></g>
<circle cx="150" cy="270" r="120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('ferocious', 'きばをむいてうなる、どう猛な獣', f'''
<path d="M0 0h600v260H0z" fill="#dceaf4"/>
<path d="M0 260h600v140H0z" fill="#c9d8c0"/>
<path d="M0 260h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 250)">
  <ellipse cx="-40" cy="10" rx="110" ry="60" fill="#a0764a" class="o"/>
  <circle cx="80" cy="-30" r="60" fill="#a0764a" class="o"/>
  <path d="M46-70q-14-40 4-44 18 8 14 44zM106-74q16-38 34-28 8 14-14 32z" fill="#a0764a" class="o"/>
  <path d="M126-24l30 8-30 12z" fill="#8b6437" class="o"/>
  <path d="M50-46q14-10 24 0M86-46q14-10 24 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <circle cx="62" cy="-38" r="4" fill="{INK}"/><circle cx="98" cy="-38" r="4" fill="{INK}"/>
  <path d="M50 0q30 26 60 0-8 26-30 26T50 0z" fill="{INK}" class="o"/>
  <g fill="#fffdf6"><path d="M56 4l8 18 8-18zM86 4l8 20 8-20z"/></g>
  <path d="M-150 0q-46-14-56-52 46 4 66 42z" fill="#8b6437" class="o"/>
  <g stroke="#8b6437" stroke-width="14" stroke-linecap="round" fill="none"><path d="M-90 60v22M-30 62v20M20 58v24"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M470 170q30 40 0 80M510 140q46 70 0 140"/>
</g>''', ground=False)

add('feudal', '領主が城から土地と農民を治める仕組み', f'''
<path d="M0 0h600v260H0z" fill="#dceaf4"/>
<path d="M0 260h600v140H0z" fill="#c9d8c0"/>
<path d="M0 260h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 260)">
  <path d="M-110 0v-130h220V0z" fill="#c8b8a0" class="o"/>
  <path d="M-130-130h50v-40h-50zM-30-130h60v-40h-60zM80-130h50v-40h-50z" fill="#c8b8a0" class="o"/>
  <path d="M-30-60h60V0h-60z" fill="#8b6437" class="o"/>
  <path d="M-10-210h10v40h-10z" fill="{BRN}"/>
  <path d="M0-210q40 8 60-6 4 26-2 38-30 8-58 2z" class="coral o"/>
</g>
{head(300, 200, 22, 'violet', 'bun')}
{head(120, 330, 20, 'gold', 'cap')}
{head(200, 350, 20, 'green', 'short')}
{head(410, 350, 20, 'teal', 'bob')}
{head(490, 330, 20, 'coral', 'cap')}
<g class="a" marker-end="url(#ar)" stroke="{MUTED}" stroke-width="4">
  <path d="M250 250l-110 50M270 260l-60 60M350 260l60 60M370 250l110 50"/>
</g>''', ground=False)

add('feverish', '額に手を当てると熱く、汗が出て顔が赤い', f'''
{table(380)}
<g transform="translate(240 210)">
  <circle r="100" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-86-30q6-66 86-66t86 66q-40-30-86-30t-86 30z" fill="{HAIR}"/>
  <g class="coral" opacity="0.5"><circle cx="-52" cy="24" r="20"/><circle cx="52" cy="24" r="20"/></g>
  <path d="M-46 0q14 12 28 0M18 0q14 12 28 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <path d="M-18 52h36" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <path d="M-70-46h56v14h-56z" fill="#fffdf6" class="o" transform="rotate(-8 -42 -40)"/>
</g>
<g fill="{TONES['blue'][0]}">
  <path d="M140 150q9 10 9 17t-9 8-9-8 9-17z"/><path d="M330 140q9 10 9 17t-9 8-9-8 9-17z"/>
</g>
{thermometer(470, 300, 0.95, 0.6)}''', ground=False)

add('figurative', '「山ほど」の言葉を、本当の山ではなく比喩で使う', f'''
{split()}
{table(380)}
<g transform="translate(150 300)">
  <path d="M-110 0l90-140 50 60 60-70 90 150z" fill="#9aa5b0" class="o"/>
  <path d="M-20-140l-24 34h48z" fill="#fffefd" class="o"/>
</g>
<g transform="translate(450 300)">
  <g class="teal o">
''' + ''.join(f'<rect x="{-70+ (i%5)*30}" y="{-20-(i//5)*30}" width="24" height="28"/>' for i in range(14)) + f'''
  </g>
</g>
<g transform="translate(300 110)">
  <path d="M-90-40h180q12 0 12 12v40q0 12-12 12h-120l-24 16v-16q-12 0-12-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  {word(0, -4, 4, 30, INK)}
</g>
<circle cx="450" cy="290" r="120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('finite', '数え切れない砂と、数え切れる石', f'''
{split()}
{table(380)}
<g fill="#e0c48a">
''' + ''.join(f'<circle cx="{40+ (i%14)*18}" cy="{240+(i//14)*22}" r="6"/>' for i in range(70)) + f'''
</g>
<g class="o">
''' + ''.join(f'<ellipse cx="{370+ (i%3)*70}" cy="{260+(i//3)*70}" rx="30" ry="22" fill="{MUTED}"/>' for i in range(6)) + f'''
</g>
<circle cx="450" cy="300" r="140" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}"><path d="M40 160h220"/></g>''', ground=False)

add('flammable', '火が近づくとすぐ燃え上がる印のついた缶', f'''
{table(380)}
<g transform="translate(320 280)">
  <path d="M-70-90h140v150q0 18-70 18t-70-18z" class="coral o"/>
  <path d="M-70-90h140v-16h-140z" class="corald o"/>
  <path d="M-24-106h48v-16h-48z" fill="{INK}"/>
  <g transform="translate(0 -20)">
    <path d="M0-40l40 70h-80z" fill="#fffdf6" class="o"/>
    {flame(0, 22, 0.28)}
  </g>
</g>
{flame(130, 300, 0.8)}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M190 240h50"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M470 200l24-22M490 260h26"/>
</g>''', ground=False)

add('flawless', '傷ひとつない皿と、欠けた皿', f'''
{split()}
{table(380)}
<g transform="translate(450 260)">
  <circle r="90" fill="#fffdf6" class="o"/>
  <circle r="66" fill="none" stroke="{MUTED}" stroke-width="3"/>
</g>
<circle cx="450" cy="260" r="120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g transform="translate(150 260)">
  <path d="M-90 0a90 90 0 1 1 180 0 90 90 0 1 1-180 0z" fill="#fffdf6" class="o"/>
  <path d="M60-70l34 16-30 20 26 22-40 6z" fill="#fffaf1" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-40 40l30 24" stroke="{MUTED}" stroke-width="4" fill="none"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><circle cx="150" cy="260" r="120"/></g>''', ground=False)

add('flimsy', 'ぺらぺらの薄い箱がつぶれ、厚い箱はつぶれない', f'''
{split()}
{table(380)}
<g transform="translate(150 300)">
  <path d="M-80-20q80-30 160 0 6 30-14 40-66 12-132 0-20-10-14-40z" fill="#e8dcc0" class="o"/>
  <g fill="none" stroke="#c8bc9c" stroke-width="3"><path d="M-60 4q60 16 120 0"/></g>
</g>
{hand(150, 180, 1)}
<circle cx="150" cy="290" r="110" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g transform="translate(450 290)">
  <path d="M-80-60h160v90h-160z" fill="#c9a464" class="o"/>
  <path d="M-80-60l16-20h160l-16 20z" fill="#d9b877" class="o"/>
  <path d="M80-60l16-20v90l-16 20z" fill="#a0764a" class="o"/>
</g>
{hand(450, 170, 1)}''', ground=False)

add('forceful', '身ぶりを交えて力強く言い切る', f'''
{table(380)}
{person(240, 380, 1.25, 1, 'coral', 'blue', 'up', 'short', 'neutral')}
{hand(160, 200, -1)}
<g transform="translate(430 190)">
  <path d="M-90-50l18 18-18 18 18 18-18 18h180l-18-18 18-18-18-18 18-18z" fill="#fffefd" class="o"/>
  <g fill="{INK}"><rect x="-56" y="-10" width="112" height="20" rx="10"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M140 300l-30 20M330 290l30 20"/>
</g>''', ground=False)

add('formative', '子どものころの経験が人柄をかたちづくる', f'''
{table(380)}
{person(140, 380, 0.8, 1, 'coral', 'blue', 'stand', 'cap', 'smile')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="6"><path d="M220 260h100"/></g>
{person(430, 380, 1.25, 1, 'coral', 'blue', 'stand', 'short', 'smile')}
<g>
''' + ''.join(f'''<g transform="translate({140+ (i%2)*0} {170-i*60})">
  <path d="M-60-24h120v48h-120z" fill="#fffefd" class="o"/>
  <rect x="-42" y="-8" width="{84-i*18}" height="16" rx="8" fill="{MUTED}"/>
</g>''' for i in range(2)) + f'''
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M140 200v60"/></g>
<circle cx="140" cy="300" r="90" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('fragrant', 'せっけんからよい香りが立ちのぼる', f'''
{table(380)}
<g transform="translate(230 290)">
  <path d="M-70-40h140v70q0 14-70 14t-70-14z" class="violetp o"/>
  <path d="M-70-40q70-24 140 0" fill="none" stroke="{TONES['violet'][0]}" stroke-width="4"/>
  <g class="violet o"><path d="M-20-16q20-14 40 0-20 16-40 0z"/></g>
</g>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-linecap="round" opacity="0.9">
  <path d="M180 210q26-40 0-70t26-60M240 190q26-44 0-76t26-56M300 210q26-40 0-70t26-60"/>
</g>
{person(470, 380, 1.05, -1, 'teal', 'blue', 'stand', 'bun', 'smile')}
<g transform="translate(450 250)">
  <path d="M-24-6q12-12 22 0M2-6q12-12 22 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round" transform="translate(-2 0)"/>
</g>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="3" stroke-dasharray="7 7"><path d="M330 220h80"/></g>''', ground=False)

add('frantic', '出発前に部屋じゅうを引っかき回して探す', f'''
{table(380)}
{person(300, 380, 1.2, 1, 'coral', 'blue', 'up', 'short', 'surprised')}
<g>
''' + ''.join(f'<g transform="translate({100+ (i%6)*80} {180+(i//6)*80}) rotate({-40+i*24})">{doc(0, 0, 56, 70, 2)}</g>' for i in range(9)) + f'''
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M180 240l-26-22M420 236l26-22M170 300l-30 8M430 296l30 8"/>
</g>
<g transform="translate(510 130)">
  <circle r="44" fill="#fffdf6" class="o"/>
  <path d="M0 0v-30M0 0l20 12" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round" fill="none"/>
</g>''', ground=False)

# --- -al / -ive の形容詞 --------------------------------------------------------
add('deductive', '一般の決まりから、この一件の答えを導く', f'''
{table(380)}
<g transform="translate(300 120)">
  <path d="M-200-50h400v90h-400z" class="tealp o"/>
  {word(0, -6, 6, 40, TONES['teal'][2])}
</g>
<g class="a" marker-end="url(#ar)" stroke-width="6"><path d="M300 180v50"/></g>
<g transform="translate(300 300)">
  <path d="M-90-50h180v90h-180z" class="coralp o"/>
  {word(0, -6, 3, 34, TONES['coral'][2])}
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M60 210h480"/></g>''', arrow=True, ground=False)

add('departmental', '会社がいくつもの部署に分かれている', f'''
{table(380)}
<g transform="translate(300 240)">
  <path d="M-250-140h500v260h-500z" fill="#e0d6c0" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="4"><path d="M-84-140v260M84-140v260M-250-20h500"/></g>
  <g class="o">
    <rect x="-240" y="-130" width="150" height="20" class="tealp"/>
    <rect x="-74" y="-130" width="150" height="20" class="coralp"/>
    <rect x="94" y="-130" width="150" height="20" class="goldp"/>
  </g>
</g>
{head(160, 190, 20, 'teal', 'short')}
{head(300, 190, 20, 'coral', 'bun')}
{head(450, 190, 20, 'gold', 'cap')}
{head(160, 300, 20, 'teal', 'bob')}
{head(300, 300, 20, 'coral', 'short')}
{head(450, 300, 20, 'gold', 'bun')}''', ground=False)

add('dimensional', '線・面・立体と、次元が一つずつ増える', f'''
{table(380)}
<g transform="translate(120 260)">
  <path d="M-70 0h140" stroke="{TONES['teal'][0]}" stroke-width="10" stroke-linecap="round" fill="none"/>
</g>
<g transform="translate(300 260)">
  <path d="M-70-60h140v120h-140z" class="tealp o"/>
</g>
<g transform="translate(480 260)">
  <path d="M-60-40h120v100h-120z" class="tealp o"/>
  <path d="M-60-40l24-30h120l-24 30z" fill="{TONES['teal'][1]}" class="o"/>
  <path d="M60-40l24-30v100l-24 30z" class="teal o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M200 150h50M380 150h50"/></g>''', arrow=True, ground=False)

add('elemental', '火と水と風と土、自然の根源の力', f'''
<path d="M0 0h600v400H0z" fill="#2f3550"/>
<g transform="translate(150 140)">{flame(0, 30, 0.7)}</g>
<g transform="translate(450 140)">
  <path d="M0-50c30 30 30 56 0 72s-30-42 0-72z" fill="{TONES['blue'][0]}" class="o" transform="scale(1.6)"/>
</g>
<g transform="translate(150 300)">
  <g fill="none" stroke="#c8d4dc" stroke-width="6" stroke-linecap="round">
    <path d="M-60-20q60-24 110 0t-30 30M-60 20q60-24 110 0"/>
  </g>
</g>
<g transform="translate(450 300)">
  <path d="M-70 30q-20-50 20-70 50-24 90 6 20 40-20 60-60 20-90 4z" fill="#a8845c" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M300 60v290M60 220h480"/></g>''', ground=False)

add('emotive', '同じ知らせでも、言い方一つで胸に迫る', f'''
{split()}
{table(380)}
<g transform="translate(150 230)">
  {doc(0, 0, 170, 200, 4)}
</g>
{head(150, 380, 22, 'blue', 'short')}
<g transform="translate(450 200)">
  <path d="M-90-60h180q14 0 14 14v60q0 14-14 14h-120l-26 20v-20q-14 0-14-14v-60q0-14 14-14z" fill="#fffefd" class="o"/>
  <g fill="{TONES['coral'][0]}"><rect x="-64" y="-24" width="128" height="18" rx="9"/><rect x="-64" y="4" width="90" height="18" rx="9"/></g>
</g>
{head(450, 380, 22, 'coral', 'bun')}
<g fill="{TONES['coral'][0]}">
  <path d="M450 320q-14-20 0-28 14-6 18 10 4-16 18-10 14 8 0 28l-18 20z"/>
</g>
<circle cx="450" cy="240" r="140" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('antitrust', '一社の独占をやめさせ、競争できる形に戻す', f'''
{split()}
{table(380)}
<g transform="translate(150 280)">
  <path d="M-90 0v-160h180V0z" fill="#8f9aa6" class="o"/>
  <g class="bluep o">
''' + ''.join(f'<rect x="{-64+ (i%3)*46}" y="{-140+(i//3)*50}" width="30" height="34"/>' for i in range(9)) + f'''
  </g>
</g>
{cross(150, 130, 0.7)}
<g transform="translate(450 280)">
''' + ''.join(f'<g transform="translate({-90+i*90} 0)"><path d="M-36 0v-90h72V0z" fill="#c8d0d8" class="o"/><path d="M-24-70h20v24h-20z" class="bluep o"/></g>' for i in range(3)) + f'''
</g>
{tick(450, 130, 0.7)}
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', ground=False)

add('consequential', '一つのつまずきが大きな結果につながる', f'''
{table(380)}
<g transform="translate(120 300)">
  <path d="M-14-40h28v80h-28z" fill="#c8d0d8" class="o"/>
</g>
<g>
''' + ''.join(f'<g transform="translate({210+i*90} {300}) rotate({8+i*8})"><path d="M-{16+i*4}-{50+i*20}h{32+i*8}v{100+i*40}h-{32+i*8}z" fill="#c8d0d8" class="o"/></g>' for i in range(4)) + f'''
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M120 180h380"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M60 380h500"/></g>''', ground=False)

# --- 連語 -------------------------------------------------------------------
add('essential-to', '水は植物が育つのに欠かせない', f'''
{split()}
<path d="M0 0h600v240H0z" fill="#dceaf4"/>
<path d="M0 240h600v160H0z" fill="#a8845c"/>
<path d="M0 240h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(150 240)">
  <path d="M-6 0v-40h12V0z" fill="#8b7a5c"/>
  <path d="M-6-28q-24-14-20-28 22 4 20 28z" fill="#a89878" class="o"/>
</g>
{cross(150, 130, 0.6)}
<g transform="translate(450 240)">
  <path d="M-8 0v-120h16V0z" class="greend o"/>
  <path d="M-8-70q-56-24-48-56 50 6 48 56zM8-100q56-24 66 6-46 26-66-6z" class="greenp o"/>
</g>
<g fill="{TONES['blue'][0]}">
''' + ''.join(f'<path d="M{410+i*30} {100+ (i%2)*26}q9 10 9 17t-9 8-9-8 9-17z"/>' for i in range(3)) + f'''
</g>
{tick(450, 130, 0.6)}''', ground=False)

add('familiar-with', '何度も使った道具なので、手が覚えている', f'''
{split()}
{table(380)}
{person(150, 380, 1.05, 1, 'blue', 'blue', 'reach', 'short', 'sad')}
<g transform="translate(150 270)">
  <path d="M-40-30h80v60h-80z" fill="#c8d0d8" class="o"/>
</g>
<g transform="translate(150 150)">
  <path d="M-34-28h68q10 0 10 10v28q0 10-10 10h-44l-16 14v-14q-18 0-18-10v-28q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M-14-16q0-14 14-14t14 14-14 12v8" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>
  <circle cy="14" r="3.5" fill="{MUTED}"/>
</g>
{person(450, 380, 1.05, 1, 'coral', 'blue', 'reach', 'bun', 'smile')}
<g transform="translate(450 270)">
  <path d="M-40-30h80v60h-80z" fill="#c8d0d8" class="o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="4" stroke-dasharray="10 8"><path d="M370 200q80-40 160 0"/></g>
{tick(450, 150, 0.5)}''', ground=False)

add('for-now', 'とりあえずの応急の当て木で、あとで直す', f'''
{table(380)}
<g transform="translate(300 260)">
  <path d="M-180-14h360v28h-360z" fill="#c9a464" class="o"/>
  <path d="M-14-14h28v28h-28z" fill="{TONES['coral'][0]}"/>
</g>
<g transform="translate(300 260) rotate(6)">
  <path d="M-70-30h140v60h-140z" fill="none" stroke="{BRN}" stroke-width="8"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="8" stroke-linecap="round">
  <path d="M230 220h140M230 300h140"/>
</g>
<g transform="translate(480 150)">
  <circle r="44" fill="#fffdf6" class="o"/>
  <path d="M0 0v-28M0 0l20 12" stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M440 200q40 60 0 100"/></g>''', ground=False)

add('in-the-long-run', '短い目では損だが、長い目では得になる', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(300 240)">
  <path d="M-250 120h500v6h-500z" fill="{INK}"/>
  <path d="M-250-180v300h6v-300z" fill="{INK}"/>
  <path d="M-230 40l60 60 60 20 60-60 60-90 60-100" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linejoin="round"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M-244 40h490M-110-180v300"/></g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}" stroke-width="4"><path d="M70 340h110"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M200 340h330"/></g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
