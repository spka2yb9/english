# -*- coding: utf-8 -*-
"""第124回。家族・車まわり・慣用表現。複数語の見出しはファイル名をハイフンでつなぐ。"""
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
    """家系図などに使う顔だけの小さな人。"""
    return (f'<g transform="translate({x} {y})">'
            f'<circle r="{r}" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>'
            f'<path d="{HAIRS[hair]}" transform="translate(0 {108-r*0.02:.0f}) scale({r/24:.2f})" fill="{HAIR}"/>'
            f'<circle cx="{-r*0.33:.0f}" cy="{-r*0.17:.0f}" r="2.4" fill="{INK}"/>'
            f'<circle cx="{r*0.33:.0f}" cy="{-r*0.17:.0f}" r="2.4" fill="{INK}"/>'
            f'<path d="M{-r*0.3:.0f} {r*0.35:.0f}q{r*0.3:.0f} {r*0.3:.0f} {r*0.6:.0f} 0" fill="none" stroke="{INK}" stroke-width="2"/>'
            f'<path d="M{-r*1.1:.0f} {r*1.5:.0f}q{r*1.1:.0f}-{r*0.6:.0f} {r*2.2:.0f} 0l-{r*0.3:.0f} {r*1.2:.0f}h-{r*1.6:.0f}z" fill="{TONES[shirt][0]}" class="o"/></g>')

# --- 家族と人 ----------------------------------------------------------------
add('ancestry', '家系図をさかのぼると何代も前の祖先にたどりつく', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g fill="none" stroke="{BRN}" stroke-width="4">
  <path d="M300 100v40M180 140h240M180 140v40M420 140v40"/>
  <path d="M120 220h120M360 220h120M120 220v40M240 220v40M360 220v40M480 220v40"/>
  <path d="M180 300h240M300 300v30"/>
  <path d="M180 260v40M420 260v40"/>
</g>
{head(300, 70, 26, 'gold', 'bun')}
{head(180, 190, 22, 'teal', 'short')}
{head(420, 190, 22, 'violet', 'bob')}
{head(120, 280, 19, 'coral', 'short')}
{head(240, 280, 19, 'green', 'bob')}
{head(360, 280, 19, 'blue', 'cap')}
{head(480, 280, 19, 'gold', 'bun')}
{head(300, 360, 19, 'coral', 'cap')}
<g class="a" marker-end="url(#ar)"><path d="M540 340V110"/></g>''', arrow=True, ground=False)

add('breadwinner', '一家のうちひとりが稼ぎ、家族の生活を支えている', f'''
{table(370)}
{person(150, 370, 1.05, 1, 'teal', 'blue', 'carry', 'short', 'neutral')}
<g transform="translate(190 280) rotate(-8)">
  <path d="M-46-30h92v60h-92z" class="gold o"/>
  <circle r="16" fill="none" stroke="{TONES['gold'][2]}" stroke-width="3"/>
</g>
{head(360, 300, 24, 'coral', 'bun')}
{head(440, 310, 20, 'green', 'bob')}
{head(510, 305, 20, 'violet', 'cap')}
<g class="a" marker-end="url(#ar)"><path d="M250 250q60-40 90-10"/></g>
{coin(300, 210, 20)}
{coin(266, 176, 16)}''', arrow=True, ground=False)

add('extended-family', '親子だけでなく祖父母やおじおばまで含む大家族', f'''
{table(380)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8">
  <ellipse cx="220" cy="250" rx="150" ry="110"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="14 10">
  <ellipse cx="300" cy="250" rx="270" ry="140"/>
</g>
{head(160, 220, 24, 'teal', 'short')}
{head(250, 220, 24, 'coral', 'bun')}
{head(150, 320, 19, 'gold', 'cap')}
{head(230, 322, 19, 'green', 'bob')}
{head(430, 210, 22, 'violet', 'bun')}
{head(510, 220, 22, 'blue', 'short')}
{head(440, 320, 19, 'coral', 'bob')}
{head(520, 318, 19, 'gold', 'cap')}
{head(60, 300, 19, 'green', 'short')}''', ground=False)

add('eyewitness', '事故を目の前で見た人が指さして証言する', f'''
{table(370)}
<g transform="translate(430 340) scale(0.75)">
  <path d="M-110 30h220v-46q0-16-16-16h-58l-34-38h-80l-24 38h-24q-16 0-16 16z" class="coral o"/>
  <circle cx="-64" cy="30" r="20" fill="{INK}"/><circle cx="64" cy="30" r="20" fill="{INK}"/>
  <path d="M110-10l40-20" stroke="{INK}" stroke-width="6" fill="none"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M500 210l24-24M540 260h30M480 270l-6 30"/>
</g>
{person(150, 370, 1.1, 1, 'teal', 'blue', 'point', 'bob', 'surprised')}
<g transform="translate(150 246)">
  <ellipse cx="-10" rx="14" ry="12" fill="#fffefd" class="o"/>
  <circle cx="-10" r="6" fill="{INK}"/>
  <ellipse cx="16" rx="14" ry="12" fill="#fffefd" class="o"/>
  <circle cx="16" r="6" fill="{INK}"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M230 250h150"/></g>''', ground=False)

add('famous', 'カメラとファンに囲まれた有名人', f'''
{table(370)}
{person(300, 370, 1.2, 1, 'coral', 'gold', 'up', 'bun', 'smile')}
<g>
''' + ''.join(f'''<g transform="translate({70+i*100} {300}) rotate({-14+i*7})">
  <path d="M-34-22h68v44h-68z" fill="#3b4450" class="o"/>
  <circle cx="6" r="14" fill="#8f9aa6" class="o"/><circle cx="6" r="7" fill="{INK}"/>
  <path d="M-30-22h20v-8h-20z" fill="#3b4450"/>
</g>''' for i in [0, 1, 3, 4]) + f'''
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{300+150*math.cos(3.6+i*0.35):.0f} {200+150*math.sin(3.6+i*0.35):.0f}l{22*math.cos(3.6+i*0.35):.0f} {22*math.sin(3.6+i*0.35):.0f}"/>' for i in range(9)) + f'''
</g>
<g fill="#fffefd">
  <circle cx="120" cy="150" r="16" opacity="0.9"/><circle cx="470" cy="140" r="14" opacity="0.9"/><circle cx="220" cy="110" r="12" opacity="0.9"/>
</g>''', ground=False)

# --- 車と家の設備 ------------------------------------------------------------
add('dashboard', '運転席の前に計器が並んだダッシュボード', f'''
<path d="M0 0h600v400H0z" fill="#3b4450"/>
<path d="M0 0h600v130H0z" fill="#dceaf4"/>
<path d="M0 130h600v40H0z" fill="#5a6270" class="o"/>
<g transform="translate(300 260)">
  <path d="M-290-90h580v190h-580z" fill="#4a5560" class="o"/>
  <circle cx="-110" cy="-10" r="66" fill="#2c333d" class="o"/>
  <circle cx="60" cy="-10" r="54" fill="#2c333d" class="o"/>
  <g fill="none" stroke="{TONES['gold'][1]}" stroke-width="3">
''' + ''.join(f'<path d="M{-110+52*math.cos(math.pi*(0.75+i*0.125)):.0f} {-10+52*math.sin(math.pi*(0.75+i*0.125)):.0f}l{10*math.cos(math.pi*(0.75+i*0.125)):.0f} {10*math.sin(math.pi*(0.75+i*0.125)):.0f}"/>' for i in range(11)) + f'''
''' + ''.join(f'<path d="M{60+42*math.cos(math.pi*(0.75+i*0.167)):.0f} {-10+42*math.sin(math.pi*(0.75+i*0.167)):.0f}l{9*math.cos(math.pi*(0.75+i*0.167)):.0f} {9*math.sin(math.pi*(0.75+i*0.167)):.0f}"/>' for i in range(9)) + f'''
  </g>
  <path d="M-110-10l30-42" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round" fill="none"/>
  <path d="M60-10l-26-34" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round" fill="none"/>
  <path d="M150-50h120v70H150z" fill="#2c333d" class="o"/>
  <g fill="{TONES['green'][0]}"><rect x="164" y="-36" width="14" height="42"/><rect x="186" y="-24" width="14" height="30"/><rect x="208" y="-40" width="14" height="46"/></g>
  <g fill="#2c333d" class="o"><circle cx="-230" cy="20" r="24"/><circle cx="-170" cy="20" r="24"/></g>
</g>
<g transform="translate(140 300)">
  <circle r="70" fill="none" stroke="{INK}" stroke-width="18"/>
  <path d="M-60 10h120M0 10v50" stroke="{INK}" stroke-width="12" fill="none"/>
</g>''', ground=False)

add('fill-up', 'ガソリンを入れてタンクを満タンにする', f'''
{table(370)}
<g transform="translate(390 330) scale(0.82)">
  <path d="M-130 30h260v-46q0-16-16-16h-70l-38-40H-84l-26 40h-20q-16 0-16 16z" class="teal o"/>
  <path d="M-80-32h100l30 40H-104z" fill="#dceaf4" class="o"/>
  <circle cx="-72" cy="30" r="22" fill="{INK}"/><circle cx="72" cy="30" r="22" fill="{INK}"/>
  <circle cx="-134" cy="-16" r="12" fill="#8f9aa6" class="o"/>
</g>
<g transform="translate(140 260)">
  <path d="M-60-90h120v190h-120z" fill="#c8d0d8" class="o"/>
  <path d="M-46-76h92v54h-92z" fill="#2c333d" class="o"/>
  <g fill="{TONES['green'][0]}"><rect x="-34" y="-64" width="16" height="30"/><rect x="-12" y="-64" width="16" height="30"/><rect x="14" y="-64" width="16" height="30"/></g>
  <path d="M60-30q40 0 40 30v50" fill="none" stroke="{INK}" stroke-width="9"/>
</g>
<g transform="translate(248 288) rotate(20)">
  <path d="M-30-16h50v32h-50z" class="coral o"/>
  <path d="M20-8h44v16H20z" fill="#8f9aa6" class="o"/>
</g>
<g transform="translate(470 170)">
  <circle r="52" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
''' + ''.join(f'<path d="M{42*math.cos(math.pi*(0.8+i*0.1)):.0f} {42*math.sin(math.pi*(0.8+i*0.1)):.0f}L{50*math.cos(math.pi*(0.8+i*0.1)):.0f} {50*math.sin(math.pi*(0.8+i*0.1)):.0f}"/>' for i in range(9)) + f'''
  </g>
  <path d="M0 0l34-24" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round" fill="none"/>
  <circle r="7" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 250v-30"/></g>''', arrow=True, ground=False)

add('gutter', '屋根の雨どいから雨水が流れ落ちている', f'''
<path d="M0 0h600v400H0z" fill="#cfd8e0"/>
{table(380)}
<g>
  <path d="M60 200L300 60l240 140z" fill="#a8552c" class="o"/>
  <path d="M60 200h480v50H60z" fill="#e8e2d6" class="o"/>
</g>
<g transform="translate(300 210)">
  <path d="M-250-14h500v20q0 14-16 14h-468q-16 0-16-14z" fill="#8f9aa6" class="o"/>
  <path d="M-250-14h500v8h-500z" fill="#b8bfc8"/>
</g>
<g>
  <path d="M228 232v148" stroke="#8f9aa6" stroke-width="24" fill="none"/>
  <path d="M228 232v148" stroke="{INK}" stroke-width="2.5" fill="none"/>
</g>
<g fill="{TONES['blue'][0]}">
''' + ''.join(f'<path d="M{240+i*46} {250+ (i%3)*30}q9 10 9 17t-9 8-9-8 9-17z"/>' for i in range(6)) + f'''
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
''' + ''.join(f'<path d="M{60+i*44} {60+(i%3)*30}l-12 34"/>' for i in range(11)) + f'''
</g>
<g fill="{TONES['blue'][1]}"><ellipse cx="228" cy="384" rx="60" ry="12"/></g>
<g class="a" marker-end="url(#ar)"><path d="M470 300l-190-70"/></g>''', arrow=True, ground=False)

add('draught', 'ドアのすきまから冷たい風が吹き込んでくる', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<path d="M0 360h600v40H0z" fill="#c9a464" class="o"/>
<g transform="translate(200 200)">
  <path d="M-120-180h240v360h-240z" fill="{BRN}" class="o"/>
  <path d="M-96-156h192v300h-192z" fill="#a0764a" class="o"/>
  <circle cx="70" cy="0" r="12" class="gold o"/>
</g>
<path d="M320 20h14v360h-14z" fill="#5a6270"/>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M340 120q60-20 110 0t110-14M340 200q60-20 110 0t110-14M340 280q60-20 110 0t110-14"/>
</g>
<g fill="{TONES['blue'][1]}" opacity="0.5"><path d="M320 20h280v360H320z"/></g>
{person(500, 360, 0.85, -1, 'coral', 'blue', 'hold', 'bob', 'sad')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M540 220q-16-14 0-26"/>
</g>''', ground=False)

add('firewall', 'ネットワークの前で壁が不正な通信をはじく', f'''
<path d="M0 0h600v400H0z" fill="#eef2f6"/>
<g transform="translate(300 200)">
  <path d="M-30-180h60v360h-60z" class="coral o"/>
  <g fill="{TONES['coral'][2]}">
''' + ''.join(f'<rect x="{-26 if i%2 else -4}" y="{-172+i*30}" width="26" height="24" rx="4"/>' for i in range(12)) + f'''
  </g>
</g>
<g transform="translate(120 200)">
  <path d="M-70-50h140v90h-140z" fill="#3b4450" class="o"/>
  <path d="M-60-40h120v70h-120z" fill="#dceaf4"/>
  <path d="M-30 40h60v14h-60z" fill="#5a6270"/>
</g>
<g transform="translate(490 130)">
  <circle r="40" class="greenp o"/>
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="3"><path d="M-40 0h80M0-40q26 40 0 80M0-40q-26 40 0 80"/></g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M440 130H210"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M470 290l-120 20"/>
</g>
{cross(340, 300, 0.8)}
<g transform="translate(500 300)">
  <path d="M-26-26h52v52h-52z" fill="{INK}"/>
  <path d="M-14-14l28 28M14-14l-28 28" stroke="#fffefd" stroke-width="5" fill="none"/>
</g>''', ground=False)

add('insulator', 'ゴムの層が電気を通さずに止めている', f'''
{table(340)}
<g transform="translate(300 230)">
  <path d="M-260-16h180v32h-180z" fill="#c8703a" class="o"/>
  <path d="M80-16h180v32H80z" fill="#c8703a" class="o"/>
  <path d="M-80-40h160v80h-160z" fill="#4a5560" class="o"/>
  <g fill="none" stroke="#6f7b88" stroke-width="3"><path d="M-60-40v80M-20-40v80M20-40v80M60-40v80"/></g>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M60 230l-20-24M40 230h-24M60 230l-20 24"/>
</g>
<g fill="{TONES['gold'][0]}">
  <path d="M120 200l24 22-16 6 20 22-40-22 16-8z"/>
</g>
{cross(300, 300, 0.9)}
<g class="a" marker-end="url(#ar)" stroke="{TONES['gold'][0]}"><path d="M60 170h150"/></g>''', ground=False)

# --- 台所と体 ----------------------------------------------------------------
add('grill', '網の上で肉に焼き目をつけている', f'''
{table(360)}
<g transform="translate(300 270)">
  <path d="M-160 30h320v20h-320z" fill="#5a6270" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="5">
''' + ''.join(f'<path d="M{-150+i*30} -20v50"/>' for i in range(11)) + f'''
    <path d="M-160-20h320"/>
  </g>
  <g class="o">
    <path d="M-110-46q50-24 96 0 12 26-16 34-56 12-88-8 0-18 8-26z" fill="#a8552c"/>
    <path d="M20-40q46-20 82 4 6 24-24 30-50 8-70-10 0-16 12-24z" fill="#a8552c"/>
  </g>
  <g fill="none" stroke="#5c2c14" stroke-width="4">
    <path d="M-100-20h80M10-14h70"/>
  </g>
</g>
{flame(240, 340, 0.5)}
{flame(360, 340, 0.5)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" opacity="0.8">
  <path d="M240 190q14-24 0-44M320 176q14-26 0-48M400 190q14-24 0-44"/>
</g>''', ground=False)

add('defrost', 'かちかちに凍った肉を電子レンジで解凍する', f'''
{split()}
{table(340)}
<g transform="translate(150 250)">
  <path d="M-80-40q50-30 110-4 16 34-16 46-60 16-100-10 0-20 6-32z" fill="#c8b0a0" class="o"/>
  <g fill="#e8f0f6" opacity="0.85"><path d="M-84-46h176v96h-176z"/></g>
  <g fill="none" stroke="#a8c4da" stroke-width="3.5" stroke-linecap="round">
''' + ''.join(f'<g transform="translate({-60+i*44} {-20+(i%2)*44})"><path d="M0-14v28M-12-7l24 14M-12 7l24-14"/></g>' for i in range(4)) + f'''
  </g>
</g>
<g transform="translate(450 250)">
  <path d="M-80-40q50-30 110-4 16 34-16 46-60 16-100-10 0-20 6-32z" fill="#c4604a" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" opacity="0.8">
    <path d="M-30-60q12-20 0-36M20-64q12-22 0-40"/>
  </g>
</g>
<g fill="{TONES['blue'][0]}"><path d="M420 316q9 10 9 17t-9 8-9-8 9-17z"/><path d="M470 322q8 9 8 15t-8 7-8-7 8-15z"/></g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('delicious', 'ひと口食べて目を輝かせている', f'''
{table(350)}
<g transform="translate(280 200)">
  <circle r="106" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-90-30q6-76 90-76t90 76q-44-34-90-34t-90 34z" fill="{HAIR}"/>
  <g fill="{INK}"><circle cx="-38" cy="-4" r="10"/><circle cx="38" cy="-4" r="10"/></g>
  <g fill="#fffefd"><circle cx="-42" cy="-8" r="4"/><circle cx="34" cy="-8" r="4"/></g>
  <path d="M-30 46q30 30 60 0q-30 16-60 0z" fill="{INK}" class="o"/>
  <path d="M-56-30q20-14 36-4M20-34q20-10 36 4" fill="none" stroke="{HAIR}" stroke-width="6" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M430 110l24-22M450 180h30M420 250l24 24M120 110l-24-22M100 180H70"/>
</g>
<g transform="translate(490 320)">
  <ellipse rx="70" ry="20" fill="#fffdf6" class="o"/>
  <path d="M-70 0q0 26 70 26t70-26z" fill="#fffdf6" class="o"/>
  <path d="M-36-10q30-24 66-2-32 20-66 2z" class="coral o"/>
</g>''', ground=False)

add('dice', '野菜をさいの目に細かく切りそろえる', f'''
{table(320)}
<g transform="translate(180 250)">
  <path d="M-70-30q50-26 106-4 14 36-18 48-58 14-96-12 0-20 8-32z" class="gold o"/>
  <path d="M-40-40q-10-30 6-34 14 6 8 34z" class="green o"/>
</g>
<g>
''' + ''.join(f'<rect x="{330+ (i%5)*30}" y="{230+(i//5)*30}" width="22" height="22" rx="3" class="gold o"/>' for i in range(10)) + f'''
</g>
<g transform="translate(290 180) rotate(-24)">
  <path d="M-100-24h140l30 24-30 22h-140z" fill="#dde3e8" class="o"/>
  <path d="M-140-10h44v20h-44q-10 0-10-10t10-10z" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 300h50"/></g>''', arrow=True, ground=False)

add('gush', 'こわれた管から水がどっと噴き出す', f'''
{table(370)}
<g transform="translate(160 250)">
  <path d="M-160-24h140v48h-140z" fill="#8f9aa6" class="o"/>
  <path d="M-26-30h20v60h-20z" fill="#6f7b88" class="o"/>
</g>
<path d="M136 250q100-70 220-30t170 130" fill="none" stroke="{TONES['blue'][1]}" stroke-width="52" stroke-linecap="round"/>
<path d="M136 250q100-70 220-30t170 130" fill="none" stroke="{TONES['blue'][0]}" stroke-width="26" stroke-linecap="round"/>
<g fill="{TONES['blue'][1]}" stroke="{TONES['blue'][0]}" stroke-width="2.5">
  <circle cx="300" cy="150" r="16"/><circle cx="400" cy="180" r="13"/><circle cx="480" cy="270" r="15"/><circle cx="230" cy="190" r="11"/>
</g>
<g fill="{TONES['blue'][1]}"><ellipse cx="470" cy="376" rx="110" ry="16"/></g>
<g class="a" marker-end="url(#ar)"><path d="M120 170q60-30 90 20"/></g>''', arrow=True, ground=False)

add('fragrance', '花からよい香りが立ちのぼっている', f'''
{table(360)}
<g transform="translate(300 300)">
  <path d="M-60-70h120l-14 70q-2 12-46 12t-46-12z" class="tealp o"/>
  <path d="M-60-70q0-16 60-16t60 16z" class="teal o"/>
</g>
<g transform="translate(300 190)">
  <path d="M-10 110V0" stroke="{TONES['green'][2]}" stroke-width="8" fill="none"/>
  <path d="M-10 60q-50-20-42-50 40 4 42 50z" class="greenp o"/>
  <g class="coralp o">
''' + ''.join(f'<ellipse cx="{-10+46*math.cos(j*1.2566):.0f}" cy="{46*math.sin(j*1.2566):.0f}" rx="32" ry="26" transform="rotate({j*72} {-10+46*math.cos(j*1.2566):.0f} {46*math.sin(j*1.2566):.0f})"/>' for j in range(5)) + f'''
  </g>
  <circle cx="-10" r="20" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-linecap="round" opacity="0.9">
  <path d="M200 130q26-40 0-70t26-60M290 100q26-44 0-76t26-56M380 130q26-40 0-70t26-60"/>
</g>
<g fill="{TONES['violet'][0]}" opacity="0.6">
  <circle cx="190" cy="70" r="6"/><circle cx="300" cy="40" r="6"/><circle cx="400" cy="70" r="6"/>
</g>''', ground=False)

# --- 音と動き ----------------------------------------------------------------
add('hiss', 'ヘビが舌を出してシューッと音を立てる', f'''
{table(360)}
<g transform="translate(260 300)">
  <path d="M-190 40q60-60 130-20t100-40 60-40" fill="none" stroke="{TONES['green'][0]}" stroke-width="34" stroke-linecap="round"/>
  <g transform="translate(100 -60)">
    <ellipse rx="34" ry="26" class="green o"/>
    <circle cx="14" cy="-8" r="4" fill="{INK}"/>
    <path d="M32 4l30 6-24 8 26 8-36 2z" class="corald o"/>
  </g>
  <g fill="{TONES['green'][2]}">
''' + ''.join(f'<circle cx="{-160+i*40}" cy="{34-(i%3)*14}" r="6"/>' for i in range(7)) + f'''
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M410 200q30 40 0 80M456 176q46 64 0 128M502 152q62 88 0 176"/>
</g>''', ground=False)

add('howl', 'オオカミが月に向かって長く遠ぼえする', f'''
<path d="M0 0h600v400H0z" fill="#2c3550"/>
<circle cx="470" cy="90" r="56" fill="#f0e6c0" class="o"/>
<g fill="#dcd0a8"><circle cx="452" cy="74" r="10"/><circle cx="486" cy="104" r="8"/><circle cx="490" cy="70" r="6"/></g>
<g fill="#fffefd"><circle cx="120" cy="60" r="4"/><circle cx="220" cy="110" r="3"/><circle cx="330" cy="50" r="3"/><circle cx="80" cy="150" r="3"/></g>
<path d="M0 340h600v60H0z" fill="#1c2130" class="o"/>
<g transform="translate(230 340)">
  <ellipse cx="-20" cy="-56" rx="80" ry="50" fill="#6f7b88" class="o"/>
  <path d="M30-90q40-30 60-90 26 30 6 80z" fill="#6f7b88" class="o"/>
  <path d="M66-158q-6-40 8-42 14 8 8 42zM90-166q10-36 24-30 6 12-10 34z" fill="#6f7b88" class="o"/>
  <path d="M84-176q40-20 56 6-40 20-56-6z" fill="#8f9aa6" class="o"/>
  <circle cx="72" cy="-160" r="3.5" fill="{INK}"/>
  <path d="M-90-70q-46-20-56 16 40 20 62 4z" fill="#6f7b88" class="o"/>
  <g stroke="#5a6270" stroke-width="12" stroke-linecap="round" fill="none"><path d="M-50-14v14M0-14v14M30-16v16"/></g>
</g>
<g fill="none" stroke="#f0e6c0" stroke-width="4" stroke-linecap="round" opacity="0.8">
  <path d="M340 160q40-30 0-60M370 180q60-44 0-100M400 200q80-58 0-140"/>
</g>''', ground=False)

add('fling', 'かばんを勢いよく部屋の隅へ放り投げる', f'''
{table(370)}
{person(160, 370, 1.15, 1, 'coral', 'blue', 'up', 'short', 'sad')}
<g transform="translate(420 200) rotate(30)">
  <path d="M-56-34h112v68h-112z" class="teal o"/>
  <path d="M-24-34q0-20 24-20t24 20" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g class="a" marker-end="url(#ar)" stroke-width="5"><path d="M220 190q120-80 220 20"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M130 180l-24-20M196 158l6-26"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M340 130l20-24M400 116l6-26"/>
</g>''', ground=False)

add('hold-on-to', '電車の手すりをしっかり握ってつかまっている', f'''
<path d="M0 0h600v400H0z" fill="#e8eef2"/>
<path d="M0 360h600v40H0z" fill="#8f9aa6" class="o"/>
<path d="M60 60h480v18H60z" fill="#8f9aa6" class="o"/>
<g>
  <path d="M300 78v70" stroke="{INK}" stroke-width="6" fill="none"/>
  <path d="M300 148q-40 0-40 34t40 34 40-34-40-34z" fill="none" stroke="{INK}" stroke-width="9"/>
</g>
{person(300, 360, 1.15, 1, 'coral', 'blue', 'up', 'bob', 'neutral')}
<g>
  <ellipse cx="300" cy="182" rx="30" ry="24" fill="{SKINL}"/>
  <ellipse cx="300" cy="182" rx="26" ry="20" fill="{SKIN}"/>
  <g fill="none" stroke="{SKINL}" stroke-width="2.5"><path d="M282 176h36M282 188h36"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M120 200h60M110 250h50M470 210h60M480 260h50"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M420 130l-90 44"/></g>''', arrow=True, ground=False)

add('disobey', '止まれと言われたのに走り出してしまう', f'''
{table(370)}
{person(160, 370, 1.05, 1, 'violet', 'blue', 'point', 'bun', 'sad')}
<g transform="translate(250 200)">
  <path d="M-46-40h92q12 0 12 12v40q0 12-12 12h-62l-22 16v-16q-10 0-10-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <path d="M-20-14h40v10h-40z" fill="{TONES['coral'][0]}"/>
  <circle r="24" cy="-4" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
{person(450, 370, 1.05, 1, 'coral', 'gold', 'walk', 'cap', 'smile', 'walk')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M360 250h50M350 300h40"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M330 160q100-40 190 60"/></g>''', ground=False)

add('idle', '働く機械の横で、止まったまま動かない機械', f'''
{split()}
{table(370)}
<g transform="translate(150 280)">
  <path d="M-80-60h160v120h-160z" fill="#8f9aa6" class="o"/>
  <circle cy="0" r="42" fill="#c8d0d8" class="o"/>
  <g fill="{INK}">
''' + ''.join(f'<rect x="-6" y="-52" width="12" height="20" rx="6" transform="rotate({i*45})"/>' for i in range(8)) + f'''
  </g>
  <circle r="10" fill="{INK}"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="4" stroke-linecap="round">
    <path d="M62-56q20 14 20 34M-62-56q-20 14-20 34"/>
  </g>
</g>
<g transform="translate(450 280)">
  <path d="M-80-60h160v120h-160z" fill="#9aa5b0" class="o"/>
  <circle cy="0" r="42" fill="#c8d0d8" class="o"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-6" y="-52" width="12" height="20" rx="6" transform="rotate({i*45})"/>' for i in range(8)) + f'''
  </g>
  <circle r="10" fill="{MUTED}"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M470 150q16-20 0-36M510 156q20-24 0-48"/>
</g>
{tick(150, 110, 0.75)}
{cross(450, 110, 0.75)}''', ground=False)

add('dazzle', '強いライトを浴びて目がくらむ', f'''
<path d="M0 0h600v400H0z" fill="#2c3550"/>
{table(380)}
<g transform="translate(470 160)">
  <circle r="70" fill="#fdf0d0" class="o"/>
  <circle r="44" fill="#fffefd"/>
  <path d="M70-56h50v112H70z" fill="#5a6270" class="o"/>
</g>
<g fill="#fdf0d0" opacity="0.45"><path d="M400 160L60 20v280z"/></g>
<g fill="none" stroke="#fdf0d0" stroke-width="5" stroke-linecap="round">
  <path d="M370 60l40-30M360 160h-40M370 270l40 30"/>
</g>
{person(180, 380, 1.15, -1, 'coral', 'blue', 'up', 'bob', 'sad')}
<g transform="translate(180 250)">
  <path d="M-30-6q14-16 28 0M2-6q14-16 28 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
</g>''', ground=False)

add('eruption', '火山が一気に噴き上げる瞬間', f'''
<path d="M0 0h600v400H0z" fill="#4a3540"/>
<path d="M0 400l180-230h60l180 230z" fill="#3b2f2a" class="o"/>
<path d="M180 170h60l-30-34z" fill="#3b2f2a"/>
<g class="coral o">
  <path d="M182 170q28-16 56 0-4 60-28 130-24-70-28-130z"/>
</g>
<g class="gold o">
  <path d="M194 168q16-10 32 0-2 40-16 84-14-44-16-84z"/>
</g>
<g fill="{MUTED}" opacity="0.9">
  <circle cx="210" cy="90" r="52"/><circle cx="290" cy="50" r="62"/><circle cx="380" cy="80" r="50"/><circle cx="140" cy="60" r="40"/>
</g>
<g fill="{TONES['coral'][0]}">
''' + ''.join(f'<circle cx="{100+i*46}" cy="{130+(i%5)*36}" r="{8-(i%4)*2}"/>' for i in range(11)) + f'''
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M240 200q60 40 90 200M200 200q-50 50-70 200"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['gold'][0]}" stroke-width="5"><path d="M210 130V60"/></g>''', ground=False)

add('demolition', '重機が古い建物を取り壊している', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
{table(370)}
<g>
  <path d="M60 370V150h180v220z" fill="#c8b8a0" class="o"/>
  <path d="M120 370V210h60v160z" fill="#a89880"/>
  <g fill="#a89880"><rect x="80" y="170" width="40" height="30"/><rect x="190" y="170" width="40" height="30"/></g>
  <path d="M240 370l40-150 50 150z" fill="#b8a890" class="o"/>
</g>
<g fill="#c8b8a0" class="o">
''' + ''.join(f'<path d="M{270+i*30} {320+(i%3)*20}l26 10-8 26-26-12z"/>' for i in range(5)) + f'''
</g>
<g transform="translate(470 300)">
  <path d="M-90 70h180v-40q0-14-14-14h-152q-14 0-14 14z" class="gold o"/>
  <circle cx="-50" cy="70" r="22" fill="{INK}"/><circle cx="50" cy="70" r="22" fill="{INK}"/>
  <path d="M-40 16h80v-40h-80z" fill="{TONES['gold'][2]}" class="o"/>
  <path d="M-30-24L-160-140" stroke="{TONES['gold'][2]}" stroke-width="18" stroke-linecap="round" fill="none"/>
  <path d="M-160-140l-40 30 30 26z" fill="#8f9aa6" class="o"/>
</g>
<g fill="{MUTED}" opacity="0.4"><ellipse cx="250" cy="360" rx="150" ry="34"/></g>''', ground=False)

add('excursion', 'バスに乗って日帰りの遠足に出かける', f'''
<path d="M0 0h600v250H0z" fill="#dceaf4"/>
<path d="M0 250h600v150H0z" fill="#dfe8d8"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M0 330h600v50H0z" fill="#8f9aa6" class="o"/>
<g transform="translate(320 330)">
  <path d="M-190 0h380v-130q0-16-16-16h-348q-16 0-16 16z" class="gold o"/>
  <g fill="#dceaf4" class="o">
''' + ''.join(f'<rect x="{-170+i*54}" y="-120" width="42" height="46" rx="6"/>' for i in range(6)) + f'''
  </g>
  <path d="M170-130h20v50h-20z" fill="#dceaf4" class="o"/>
  <circle cx="-120" cy="0" r="26" fill="{INK}"/><circle cx="120" cy="0" r="26" fill="{INK}"/>
  <circle cx="-120" cy="0" r="11" fill="#8f9aa6"/><circle cx="120" cy="0" r="11" fill="#8f9aa6"/>
</g>
<g>
''' + ''.join(f'<g transform="translate({164+i*54} {228})"><circle r="14" fill="{SKIN}" stroke="{SKINL}" stroke-width="2"/><path d="M-14-4q6-16 14-16t14 16z" fill="{HAIR}"/></g>' for i in range(6)) + f'''
</g>
{tree(70, 330, 1.0)}
{tree(540, 330, 0.9)}
{sun(120, 70, 34)}''', ground=False)

add('gown', 'すそが床まで届く長い式服を着ている', f'''
{table(380)}
{person(300, 380, 1.2, 1, 'violet', 'violet', 'stand', 'bun', 'smile')}
<g transform="translate(300 380)">
  <path d="M-40-142q40-20 80 0l60 142h-200z" class="violet o"/>
  <path d="M-40-142l-48 54 22 20 30-40M40-142l48 54-22 20-30-40" class="violet o"/>
  <g fill="none" stroke="{TONES['violet'][2]}" stroke-width="3"><path d="M-70-40q70 20 140 0M-86 0q86 24 172 0"/></g>
  <path d="M-20-142q20 14 40 0l-6 40h-28z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M170 200l-24-20M440 190l26-20"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 330l-90-20"/></g>''', arrow=True, ground=False)

add('cuff', 'シャツのそで口にボタンが二つついている', f'''
{table(340)}
<g transform="translate(300 220) rotate(-16)">
  <path d="M-200-56h200v112h-200z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-190-20h180M-190 20h180"/></g>
  <path d="M0-70h90v140H0z" fill="#e8eef2" class="o"/>
  <path d="M90-70h20v140H90z" fill="#dde3e8" class="o"/>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="2.5">
    <circle cx="46" cy="-24" r="12"/><circle cx="46" cy="24" r="12"/>
  </g>
  <g fill="{INK}"><circle cx="42" cy="-28" r="2"/><circle cx="50" cy="-20" r="2"/><circle cx="42" cy="20" r="2"/><circle cx="50" cy="28" r="2"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 130l-130 70"/></g>''', arrow=True, ground=False)

add('cushion', 'いすの上のクッションが体重を受けてへこむ', f'''
{table(370)}
<g transform="translate(200 300)">
  <path d="M-80-30q80-24 160 0 10 44-10 60-70 16-140 0-20-16-10-60z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M-70-10q70 20 140 0M-74 16q74 22 148 0"/></g>
</g>
<g transform="translate(430 310)">
  <path d="M-80-14q80-40 160 0 10 30-10 44-70 16-140 0-20-14-10-44z" class="coral o"/>
  <path d="M-40-24q40-16 80 0" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M430 200v40"/></g>
<g fill="{INK}" opacity="0.15"><ellipse cx="430" cy="272" rx="60" ry="16"/></g>''', arrow=True, ground=False)

add('dangerous', '「危険」の標識が立ち、崖の縁が崩れかけている', f'''
<path d="M0 0h600v260H0z" fill="#dceaf4"/>
<path d="M0 260h280v140H0z" fill="#c9d8c0" class="o"/>
<path d="M280 260q0 60-30 140h-30q40-80 30-140z" fill="#a8845c"/>
<path d="M0 380h600v20H0z" fill="#8f9aa6" opacity="0.4"/>
<g fill="#a8845c" class="o">
  <path d="M300 300l30 20-14 26-30-16z"/><path d="M340 340l24 16-10 22-26-14z"/>
</g>
<g transform="translate(150 200)">
  <path d="M0-70l70 120H-70z" class="gold o"/>
  <path d="M-6-24h12v40h-12z" fill="{INK}"/>
  <circle cy="30" r="6" fill="{INK}"/>
  <path d="M0 50v90" stroke="{BRN}" stroke-width="12" fill="none"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round" stroke-dasharray="20 16">
  <path d="M280 260v140"/>
</g>
{person(80, 340, 0.8, 1, 'teal', 'blue', 'stand', 'bob', 'sad')}''', ground=False)

add('inoculation', '腕に注射をして予防接種を受けている', f'''
{table(370)}
{sit(200, 370, 1.0, 1, 'coral', 'blue', 'bob', 'sad', 'down')}
{chair(200, 370, 0.95, 'gold', 1)}
<g>
  <path d="M244 268q60-6 90 12" stroke="{SKIN}" stroke-width="24" stroke-linecap="round" fill="none"/>
  <path d="M244 268q60-6 90 12" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g transform="translate(400 250) rotate(28)">
  <path d="M-60-14h110v28h-110z" fill="#e8f0f6" class="o"/>
  <path d="M-60-16h30v32h-30z" fill="{TONES['coral'][1]}"/>
  <path d="M50-6h30v12H50z" fill="#8f9aa6" class="o"/>
  <path d="M80-2h34v4H80z" fill="{INK}"/>
</g>
{person(470, 370, 0.95, -1, 'teal', 'teal', 'reach', 'bun', 'smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M300 200q-16-14 0-26"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M400 180l-60 60"/></g>''', arrow=True, ground=False)

add('infestation', '台所にアリが大量に湧いている', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
{table(230)}
<g transform="translate(300 200)">
  <path d="M-56-30h112v30h-112z" fill="#fde39a" class="o"/>
  <path d="M-56-30l14-14h112l-14 14z" fill="#fff2b8" class="o"/>
</g>
<g fill="{INK}">
''' + ''.join(f'''<g transform="translate({40+ (i%12)*46} {270+(i//12)*44}) rotate({-30+i*17}) scale(0.6)">
  <ellipse cx="-16" rx="10" ry="8"/><ellipse cx="2" rx="8" ry="7"/><ellipse cx="20" rx="12" ry="9"/>
  <g stroke="{INK}" stroke-width="2.5" fill="none"><path d="M0-7l-8-12M0 7l-8 12M8-7l4-12M8 7l4 12M-8-7l-10-10M-8 7l-10 10"/></g>
</g>''' for i in range(30)) + f'''
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M300 230v40"/></g>''', ground=False)

add('ingenuity', 'ありあわせの物を組み合わせて新しい仕掛けを作る', f'''
{table(340)}
<g transform="translate(300 240)">
  <circle cx="-90" r="46" fill="#8f9aa6" class="o"/>
  <g fill="{INK}">
''' + ''.join(f'<rect x="{-96}" y="-56" width="12" height="20" rx="6" transform="rotate({i*45} -90 0)"/>' for i in range(8)) + f'''
  </g>
  <circle cx="30" r="34" fill="#c8d0d8" class="o"/>
  <g fill="{INK}">
''' + ''.join(f'<rect x="{24}" y="-42" width="10" height="16" rx="5" transform="rotate({i*60} 30 0)"/>' for i in range(6)) + f'''
  </g>
  <path d="M64-8h60v16H64z" fill="#c9a464" class="o"/>
  <path d="M124-24h40v48h-40z" class="coral o"/>
  <path d="M-90-56v-40" stroke="{BRN}" stroke-width="8" fill="none"/>
  <circle cx="-90" cy="-104" r="18" class="gold o"/>
</g>
{person(120, 340, 0.9, 1, 'teal', 'blue', 'point', 'bun', 'smile')}
<g transform="translate(140 190)">
  <path d="M-30-26h60q10 0 10 10v28q0 10-10 10h-40l-16 14v-14q-14 0-14-10v-28q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M0-18q20 0 20 18t-10 16v8h-20v-8q-10 0-10-16t20-18z" fill="{TONES['gold'][0]}"/>
</g>''', ground=False)

add('gauge', '圧力計の針が目盛りのどこを指すか読み取る', f'''
{table(340)}
<g transform="translate(300 210)">
  <circle r="120" fill="#fffdf6" class="o"/>
  <circle r="104" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <g fill="none" stroke="{INK}" stroke-width="4">
''' + ''.join(f'<path d="M{88*math.cos(math.pi*(0.75+i*0.075)):.0f} {88*math.sin(math.pi*(0.75+i*0.075)):.0f}L{104*math.cos(math.pi*(0.75+i*0.075)):.0f} {104*math.sin(math.pi*(0.75+i*0.075)):.0f}"/>' for i in range(21)) + f'''
  </g>
  <path d="M-74-74A104 104 0 0 1 0-104" fill="none" stroke="{TONES['green'][0]}" stroke-width="10"/>
  <path d="M0-104A104 104 0 0 1 74-74" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10"/>
  <path d="M0 0l-52-62" stroke="{INK}" stroke-width="8" stroke-linecap="round" fill="none"/>
  <circle r="12" fill="{INK}"/>
  <path d="M-40 120h80v30h-80z" fill="#8f9aa6" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 130l-110 30"/></g>''', arrow=True, ground=False)

add('envy', '相手の大きなケーキを横目で見て、うらやましがる', f'''
{table(340)}
{person(180, 340, 1.05, 1, 'coral', 'blue', 'hold', 'bob', 'smile')}
<g transform="translate(220 250)">
  <path d="M-46-30h92v50q0 12-46 12t-46-12z" class="coralp o"/>
  <path d="M-46-30q0-16 46-16t46 16z" fill="#fde39a" class="o"/>
  <circle cx="0" cy="-40" r="10" class="coral o"/>
</g>
{person(450, 340, 1.05, -1, 'green', 'green', 'stand', 'bun', 'sad')}
<g transform="translate(470 260)">
  <ellipse rx="40" ry="14" fill="#fffdf6" class="o"/>
  <path d="M-16-6q16-12 32 0-16 8-32 0z" class="goldp o"/>
</g>
<g fill="{TONES['green'][0]}" opacity="0.45"><ellipse cx="450" cy="234" rx="34" ry="26"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M420 200l-24-18M400 250l-26-6"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M410 240l-140 10"/></g>''', ground=False)

add('emptiness', '中身のある箱と、何も入っていない箱', f'''
{split()}
{table(340)}
<g transform="translate(150 250)">
  <path d="M-90-40h180v90h-180z" fill="#c9a464" class="o"/>
  <path d="M-90-40l24-30h180l-24 30z" fill="#d9b877" class="o"/>
  <g class="o">
    <circle cx="-46" cy="-6" r="24" class="coralp"/><circle cx="10" cy="0" r="26" class="tealp"/><circle cx="60" cy="-8" r="22" class="goldp"/>
  </g>
</g>
<g transform="translate(450 250)">
  <path d="M-90-40h180v90h-180z" fill="#c9a464" class="o"/>
  <path d="M-90-40l24-30h180l-24 30z" fill="#e8d8b4"/>
  <path d="M-66-70l24 30v90M114-70l-24 30v90" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-66-70h180l-24 30h-180z" fill="#e8d8b4" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M400 230h100"/></g>''', ground=False)

add('conquest', '軍が城を落として旗を立てる', f'''
<path d="M0 0h600v260H0z" fill="#dceaf4"/>
{table(380)}
<path d="M0 300h600v100H0z" fill="#c9d8c0"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(360 300)">
  <path d="M-140 0v-150h280V0z" fill="#c8b8a0" class="o"/>
  <path d="M-160-150h60v-40h-60zM-40-150h80v-40h-80zM100-150h60v-40h-60z" fill="#c8b8a0" class="o"/>
  <path d="M-160-150h320v-14h-320z" fill="#b8a890"/>
  <g fill="#a89880"><rect x="-100" y="-110" width="40" height="50"/><rect x="60" y="-110" width="40" height="50"/></g>
  <path d="M-30-60h60V0h-60z" fill="#8b6437" class="o"/>
</g>
<g transform="translate(360 110)">
  <path d="M0 0v-90" stroke="{BRN}" stroke-width="8" stroke-linecap="round" fill="none"/>
  <path d="M4-90q60 10 96-10 6 40-4 58-48 14-92 4z" class="coral o"/>
</g>
{person(120, 380, 0.9, 1, 'teal', 'blue', 'up', 'cap', 'smile')}
{person(200, 380, 0.9, 1, 'teal', 'blue', 'up', 'cap', 'smile')}
<g class="a" marker-end="url(#ar)" stroke-width="5"><path d="M250 260h60"/></g>''', ground=False)

add('calibre', '力量の違う二人が同じ課題に取り組んだ結果', f'''
{split()}
{table(370)}
{person(150, 370, 1.05, 1, 'blue', 'blue', 'reach', 'short', 'sad')}
<g transform="translate(150 250)">
  <path d="M-60-40h120v70h-120z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-40-20q30 20 50-6t40 16"/></g>
</g>
<g fill="{TONES['coral'][0]}"><path d="M110 300l40 40M150 300l-40 40"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M110 300l40 40M150 300l-40 40"/></g>
{person(450, 370, 1.05, 1, 'coral', 'blue', 'reach', 'bun', 'smile')}
<g transform="translate(450 250)">
  <path d="M-60-40h120v70h-120z" class="paper"/>
  <g fill="{INK}"><rect x="-44" y="-24" width="88" height="9" rx="4.5"/><rect x="-44" y="-4" width="70" height="9" rx="4.5"/><rect x="-44" y="16" width="80" height="9" rx="4.5"/></g>
</g>
{tick(450, 320, 0.8)}''', ground=False)

add('chromosome', 'X字形の染色体が並んでいる', f'''
<path d="M0 0h600v400H0z" fill="#eef4f8"/>
<g>
''' + ''.join(f'''<g transform="translate({80+ (i%6)*90} {130+(i//6)*140}) scale({0.9-(i%3)*0.12})">
  <path d="M-34-70q20 40 0 60-20-20 0-60zM34-70q-20 40 0 60 20-20 0-60z" fill="{TONES[["violet","teal","coral"][i%3]][0]}" class="o"/>
  <path d="M-34 70q20-40 0-60-20 20 0 60zM34 70q-20-40 0-60 20 20 0 60z" fill="{TONES[["violet","teal","coral"][i%3]][0]}" class="o"/>
  <circle r="14" fill="{TONES[["violet","teal","coral"][i%3]][2]}" class="o"/>
</g>''' for i in range(10)) + f'''
</g>
<g transform="translate(490 300)">
  <circle r="70" fill="none" stroke="{INK}" stroke-width="9"/>
  <path d="M50 50l50 50" stroke="{INK}" stroke-width="12" stroke-linecap="round" fill="none"/>
</g>''', ground=False)

add('clumsiness', '皿を落としてつまずいてしまう', f'''
{table(370)}
{person(240, 370, 1.15, 1, 'coral', 'blue', 'up', 'bob', 'surprised')}
<g fill="#fffdf6" class="o">
  <ellipse cx="380" cy="180" rx="42" ry="12" transform="rotate(30 380 180)"/>
  <ellipse cx="430" cy="250" rx="38" ry="11" transform="rotate(-20 430 250)"/>
</g>
<g fill="#fffdf6" class="o">
  <path d="M420 350l40 10-14 20-36-14z"/><path d="M470 340l34 16-20 18-30-20z"/><path d="M380 366l30 8-10 16-28-10z"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M180 180l-24-20M300 160l6-26M470 300l24-16"/>
</g>
<g transform="translate(160 350) rotate(-20)">
  <path d="M-40-8h80v16h-80z" fill="#c9a464" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M330 170q80 40 90 150"/></g>''', arrow=True, ground=False)

add('demographic', '年齢層ごとの人数を棒グラフで示す', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(300 300)">
  <path d="M-250 0h500v6h-500z" fill="{INK}"/>
  <path d="M-250-240v240h6v-240z" fill="{INK}"/>
  <g class="teal o">
    <rect x="-220" y="-70" width="70" height="70"/><rect x="-130" y="-140" width="70" height="140"/>
    <rect x="-40" y="-210" width="70" height="210"/><rect x="50" y="-160" width="70" height="160"/>
    <rect x="140" y="-90" width="70" height="90"/>
  </g>
</g>
<g>
''' + ''.join(f'{head(85+i*90, 350, 16, ["coral","gold","teal","violet","green"][i], ["cap","short","bob","bun","short"][i])}' for i in range(5)) + f'''
</g>''', ground=False)

add('draw-the-line', 'ここまでは許すが、その先は認めないと線を引く', f'''
{table(380)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"><path d="M320 40v340"/></g>
<g>
''' + ''.join(f'<g transform="translate({80+i*70} {300})"><path d="M-24-24h48v48h-48z" class="greenp o"/>{tick(0, 0, 0.4)}</g>' for i in range(3)) + f'''
''' + ''.join(f'<g transform="translate({390+i*70} {300})"><path d="M-24-24h48v48h-48z" class="coralp o"/>{cross(0, 0, 0.4)}</g>' for i in range(3)) + f'''
</g>
{person(180, 380, 0.95, 1, 'teal', 'blue', 'point', 'bun', 'neutral')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M240 200h60"/></g>''', ground=False)

add('get-the-hang-of', '最初は転んでいたのが、こつをつかんで乗れるようになる', f'''
{split()}
{table(370)}
<g transform="translate(150 340) rotate(-30)">
  <circle cx="-40" r="34" fill="none" stroke="{INK}" stroke-width="6"/>
  <circle cx="40" r="34" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M-40 0l30-40h40l10 40M0-40v-20h24" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
{person(180, 380, 0.8, 1, 'coral', 'blue', 'up', 'bob', 'sad')}
{cross(150, 120, 0.7)}
<g transform="translate(450 330)">
  <circle cx="-46" cy="30" r="34" fill="none" stroke="{INK}" stroke-width="6"/>
  <circle cx="46" cy="30" r="34" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M-46 30l30-40h40l22 40M0-10v-24h26" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M-16-10l-14-24" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
{person(450, 300, 0.75, 1, 'coral', 'blue', 'reach', 'bob', 'smile')}
{tick(450, 120, 0.7)}''', ground=False)

add('go-the-extra-mile', '決められた距離を走り終えてから、さらに先まで走る', f'''
{table(370)}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="16 12"><path d="M300 60v320"/></g>
<g transform="translate(300 100)">
  <path d="M-6-40h12v40h-12z" fill="{INK}"/>
  <path d="M6-40h56v30H6z" class="coral o"/>
</g>
<path d="M40 370h520" fill="none" stroke="#8f9aa6" stroke-width="20"/>
{person(430, 368, 1.1, 1, 'teal', 'coral', 'walk', 'cap', 'smile', 'walk')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M330 250h50M320 300h40"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M330 200h200"/></g>
<g fill="{MUTED}">
''' + ''.join(f'<ellipse cx="{80+i*40}" cy="{386-(i%2)*12}" rx="10" ry="14" transform="rotate(10 {80+i*40} 380)"/>' for i in range(5)) + f'''
</g>''', ground=False)

add('eternity', '砂時計の砂が果てしなく落ち続けている', f'''
<path d="M0 0h600v400H0z" fill="#2f3550"/>
<g transform="translate(300 200)">
  <path d="M-110-160h220v24h-220zM-110 136h220v24h-220z" fill="#c9a464" class="o"/>
  <path d="M-90-136h180q0 90-90 136 90 46 90 136h-180q0-90 90-136-90-46-90-136z" fill="#e8f0f6" class="o" opacity="0.85"/>
  <path d="M-70-124h140q-6 66-70 106-64-40-70-106z" fill="{TONES['gold'][0]}"/>
  <path d="M-4-16h8v90h-8z" fill="{TONES['gold'][0]}"/>
  <path d="M-52 124q10-52 52-70 42 18 52 70z" fill="{TONES['gold'][0]}"/>
  <path d="M-90-160v320M90-160v320" stroke="#c9a464" stroke-width="12" stroke-linecap="round" fill="none"/>
</g>
<g fill="none" stroke="{TONES['gold'][1]}" stroke-width="5" stroke-linecap="round">
  <path d="M470 200q-40-50 0-90 40 40 0 90zM470 200q40 50 0 90-40-40 0-90z"/>
</g>
<g fill="#fffefd"><circle cx="100" cy="80" r="4"/><circle cx="500" cy="90" r="3"/><circle cx="120" cy="320" r="3"/></g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
