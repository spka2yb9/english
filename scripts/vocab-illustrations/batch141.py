# -*- coding: utf-8 -*-
"""第141回。g-/h- の形容詞と身のまわりの名詞。"""
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
add('galaxy', '渦を巻いて広がる無数の星の集まり', f'''
<path d="M0 0h600v400H0z" fill="#181d2a"/>
<g transform="translate(300 200)">
  <g fill="none" stroke="#7d8fd0" stroke-width="18" stroke-linecap="round" opacity="0.55">
    <path d="M0 0q90-70 190-30M0 0q-90 70-190 30M0 0q40 90-40 150M0 0q-40-90 40-150"/>
  </g>
  <circle r="46" fill="#fdf0d0" class="o"/>
  <circle r="80" fill="#fdf0d0" opacity="0.2"/>
</g>
<g fill="#fffefd">
''' + ''.join(f'<circle cx="{300+ (i*97 % 520) - 260}" cy="{200 + (i*61 % 340) - 170}" r="{2 + i % 3}"/>' for i in range(40)) + f'''
</g>''', ground=False)

add('germ', '顕微鏡でしか見えない小さな菌', f'''
{table(380)}
<g transform="translate(170 250)">
  <path d="M-50 120h100v20h-100z" fill="#5a6270" class="o"/>
  <path d="M-14 120V20h28v100z" fill="#8f9aa6" class="o"/>
  <path d="M-14 20q-40-30-40-80t54-70v40q-26 10-26 34t26 36z" fill="#8f9aa6" class="o"/>
  <path d="M-14-116h60v34h-60z" fill="#5a6270" class="o"/>
  <path d="M-50 60h100v14h-100z" fill="#c8d0d8" class="o"/>
</g>
<g transform="translate(430 200)">
  <circle r="110" fill="{TONES['coral'][1]}" class="o"/>
  <g class="coral o">
''' + ''.join(f'<circle cx="{-40+ (i%3)*44}" cy="{-30+(i//3)*44}" r="20"/>' for i in range(6)) + f'''
  </g>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="3" stroke-linecap="round">
''' + ''.join(f'<path d="M{-40+(i%3)*44} {-50-(i//3)*0}l{-8+(i%3)*8} -12"/>' for i in range(3)) + f'''
  </g>
</g>''', ground=False)

add('gorilla', '胸の厚い黒い類人猿が腰を下ろしている', f'''
<path d="M0 0h600v260H0z" fill="#cfe0d4"/>
<path d="M0 260h600v140H0z" fill="#c9d8c0"/>
<path d="M0 260h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 300)">
  <path d="M-90 40q-30-110 20-150 70-40 140 0 50 40 20 150-90 26-180 0z" fill="#3d3a3a" class="o"/>
  <path d="M-46 30q46-40 92 0 6 34-46 40t-46-40z" fill="#5b5757"/>
  <circle cy="-136" r="62" fill="#3d3a3a" class="o"/>
  <path d="M-46-160q6-40 46-40t46 40q-20 60-46 66-26-6-46-66z" fill="#3d3a3a"/>
  <ellipse cy="-120" rx="44" ry="36" fill="#7a6f68"/>
  <circle cx="-16" cy="-134" r="5" fill="{INK}"/><circle cx="16" cy="-134" r="5" fill="{INK}"/>
  <g fill="{INK}"><circle cx="-8" cy="-110" r="4"/><circle cx="8" cy="-110" r="4"/></g>
  <path d="M-14-92q14 8 28 0" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-62-140q-22 0-22 18t22 18zM62-140q22 0 22 18t-22 18z" fill="#3d3a3a" class="o"/>
  <path d="M-90-20q-56 10-70 60 50 26 80-14z" fill="#3d3a3a" class="o"/>
  <path d="M90-20q56 10 70 60-50 26-80-14z" fill="#3d3a3a" class="o"/>
</g>''', ground=False)

add('grapefruit', '半分に切った断面が赤い大きな柑橘', f'''
{table(320)}
<g transform="translate(190 240)">
  <circle r="86" class="gold o"/>
  <path d="M0-86q-16-30 8-38 20 8 8 38z" class="greend o"/>
  <ellipse cx="-30" cy="-30" rx="18" ry="12" fill="#fffefd" opacity="0.45" transform="rotate(-30 -30 -30)"/>
</g>
<g transform="translate(420 250)">
  <circle r="94" class="gold o"/>
  <circle r="80" fill="#f6d0c0" class="o"/>
''' + ''.join(f'<path d="M0 0l{72*math.cos(i*0.785-0.35):.0f} {72*math.sin(i*0.785-0.35):.0f}A72 72 0 0 1 {72*math.cos(i*0.785+0.35):.0f} {72*math.sin(i*0.785+0.35):.0f}z" fill="#e89a86" stroke="#d0806c" stroke-width="2"/>' for i in range(8)) + f'''
  <circle r="12" fill="#f6d0c0" class="o"/>
</g>''', ground=False)

add('guidebook', '見どころと地図が載った旅行の案内書', f'''
{table(360)}
<g transform="translate(300 230) rotate(-4)">
  <path d="M-140-120h280v240h-280z" fill="#fffdf6" class="o"/>
  <path d="M0-120v240" stroke="{INK}" stroke-width="3" fill="none"/>
  <g transform="translate(-70 -20)">
    <path d="M-56-70h112v100h-112z" fill="#f0e6d0" class="o"/>
    <path d="M-40 20q40-50 80 0" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"/>
    <path d="M6-24l14 24h-28z" class="coral o"/>
  </g>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="20" y="{-86+i*30}" width="{100-(i%3)*24}" height="10" rx="5"/>' for i in range(6)) + f'''
  </g>
  <path d="M-146-120h20v240h-20z" class="coral o"/>
</g>''', ground=False)

add('hacker', '他人の仕組みに勝手に入り込む人', f'''
<path d="M0 0h600v400H0z" fill="#1c2530"/>
<g transform="translate(360 200)">
  <path d="M-160-120h320v220h-320z" fill="#3b4450" class="o"/>
  <path d="M-140-100h280v180h-280z" fill="#0f2a1e"/>
  <g fill="{TONES['green'][0]}">
''' + ''.join(f'<rect x="{-120+ (i%3)*20}" y="{-80+i*22}" width="{160-(i%4)*40}" height="10" rx="5"/>' for i in range(7)) + f'''
  </g>
  <path d="M-40 100h80v14h-80z" fill="#5a6270"/>
</g>
{person(120, 380, 1.0, 1, 'violet', 'blue', 'reach', 'cap', 'neutral')}
<g fill="{INK}" opacity="0.35"><path d="M40 200h160v180H40z"/></g>
<g transform="translate(210 170)">
  <path d="M-30-20h60v40h-60z" fill="#c8d0d8" class="o"/>
  <path d="M-16-20v-16q0-14 16-14t16 14v16" fill="none" stroke="#c8d0d8" stroke-width="6"/>
  <path d="M-6 24l24-24" stroke="{TONES['coral'][0]}" stroke-width="6" fill="none"/>
</g>''', ground=False)

add('hallway', '部屋と部屋をつなぐ細長い廊下', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<path d="M0 400V60h180l60 90v180zM600 400V60H420l-60 90v180z" fill="#e0d6c0" class="o"/>
<path d="M240 400h120V150H240z" fill="#c9a464" class="o"/>
<g fill="none" stroke="#a0764a" stroke-width="3">
''' + ''.join(f'<path d="M{240- i*0} {200+i*50}h120"/>' for i in range(4)) + f'''
</g>
<g fill="{BRN}" class="o">
  <path d="M60 330V180h50v150zM540 330V180h-50v150z"/>
</g>
<g fill="{TONES['gold'][0]}"><circle cx="100" cy="260" r="7"/><circle cx="500" cy="260" r="7"/></g>
{person(300, 330, 0.65, 1, 'coral', 'blue', 'walk', 'bob', 'smile', 'walk')}
<g class="a" marker-end="url(#ar)"><path d="M300 120v90"/></g>''', arrow=True, ground=False)

add('handkerchief', 'たたんだ小さな布で額の汗をふく', f'''
{table(340)}
<g transform="translate(180 260) rotate(-10)">
  <path d="M-70-70h140v140h-140z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3">
    <path d="M-70-30h140M-70 30h140M-30-70v140M30-70v140"/>
  </g>
</g>
<g transform="translate(430 220)">
  <circle r="90" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-78-26q6-64 78-64t78 64q-38-30-78-30t-78 30z" fill="{HAIR}"/>
  <circle cx="-32" cy="4" r="6" fill="{INK}"/><circle cx="32" cy="4" r="6" fill="{INK}"/>
  <path d="M-18 44q18 12 36 0" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-70-46h140v20h-140z" fill="#fffdf6" class="o" transform="rotate(-6 0 -36)"/>
</g>
<g fill="{TONES['blue'][0]}"><path d="M520 150q9 10 9 17t-9 8-9-8 9-17z"/></g>''', ground=False)

add('heartbeat', '心臓の動きが波形になって画面に出る', f'''
<path d="M0 0h600v400H0z" fill="#1c2530"/>
<g transform="translate(300 200)">
  <path d="M-250-120h500v240h-500z" fill="#0f2028" class="o"/>
  <path d="M-230 0h80l20-50 26 100 24-70 20 20h100l20-50 26 100 24-70 20 20h60" fill="none" stroke="{TONES['green'][0]}" stroke-width="5" stroke-linejoin="round"/>
</g>
<g transform="translate(120 120)">
  <path d="M0-30q26-26 46 0 14 26-46 66-60-40-46-66 20-26 46 0z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M180 90q16-16 0-32M200 100q26-26 0-52"/>
</g>''', ground=False)

add('hostel', '二段ベッドの並ぶ安い宿に泊まる', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<path d="M0 350h600v50H0z" fill="#c9a464" class="o"/>
<g>
''' + ''.join(f'''<g transform="translate({130+i*160} 250)">
  <path d="M-70 100v-160h10v160zM70 100v-160h-10v160z" fill="#8f9aa6" class="o"/>
  <path d="M-70-10h140v26h-140z" class="bluep o"/>
  <path d="M-70 60h140v26h-140z" class="bluep o"/>
  <path d="M-70-20h44v10h-44zM-70 50h44v10h-44z" fill="#fffdf6" class="o"/>
</g>''' for i in range(3)) + f'''
</g>
<g transform="translate(300 90)">
  <path d="M-110-30h220v50h-220z" class="coral o"/>
  <g fill="#fffefd"><rect x="-80" y="-14" width="120" height="18" rx="9"/></g>
</g>''', ground=False)

add('humidity', '空気中の水分が多く、窓がくもる', f'''
<path d="M0 0h600v400H0z" fill="#dfe4ea"/>
<g transform="translate(300 200)">
  <path d="M-180-150h360v300h-360z" fill="{BRN}" class="o"/>
  <path d="M-150-120h300v240h-300z" fill="#c7d8e2"/>
  <path d="M0-120v240M-150 0h300" stroke="{BRN}" stroke-width="10" fill="none"/>
  <g fill="#fffefd" opacity="0.7">
''' + ''.join(f'<circle cx="{-120+ (i%8)*36}" cy="{-90+(i//8)*40}" r="{9+(i%3)*4}"/>' for i in range(24)) + f'''
  </g>
  <path d="M-100-60q0 60 20 90" fill="none" stroke="#fffefd" stroke-width="5" stroke-linecap="round"/>
</g>
<g transform="translate(510 300)">
  <circle r="56" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
''' + ''.join(f'<path d="M{44*math.cos(math.pi*(0.75+i*0.1)):.0f} {44*math.sin(math.pi*(0.75+i*0.1)):.0f}L{52*math.cos(math.pi*(0.75+i*0.1)):.0f} {52*math.sin(math.pi*(0.75+i*0.1)):.0f}"/>' for i in range(9)) + f'''
  </g>
  <path d="M0 0l34-18" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round" fill="none"/>
  <circle r="6" fill="{INK}"/>
</g>''', ground=False)

add('hyperlink', '文の一部を押すと別の場所へ飛ぶ', f'''
{table(380)}
<g transform="translate(240 190)">
  <path d="M-160-130h320v260h-320z" fill="#3b4450" class="o"/>
  <path d="M-140-110h280v220h-280z" fill="#fffefd"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-110" y="{-80+i*34}" width="{200-(i%3)*40}" height="12" rx="6"/>' for i in range(4)) + f'''
  </g>
  <rect x="-110" y="54" width="120" height="12" rx="6" fill="{TONES['blue'][0]}"/>
  <path d="M-112 72h124" stroke="{TONES['blue'][0]}" stroke-width="3" fill="none"/>
</g>
<g transform="translate(180 290)">
  <path d="M0 0l0 34 10-10 8 16 8-4-8-16h14z" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['blue'][0]}" stroke-width="5"><path d="M400 260q90-40 130 30"/></g>
<g transform="translate(530 340)">
  <path d="M-56-40h112v80h-112z" fill="#3b4450" class="o"/>
  <path d="M-46-30h92v60h-92z" fill="#dceaf4"/>
</g>''', ground=False)

add('frown', '眉を寄せてしかめ面をする', f'''
<g transform="translate(300 200)">
  <circle r="140" fill="{SKIN}" stroke="{SKINL}" stroke-width="4"/>
  <path d="M-100-40q40-26 68-4M100-40q-40-26-68-4" fill="none" stroke="{HAIR}" stroke-width="14" stroke-linecap="round"/>
  <circle cx="-48" cy="4" r="10" fill="{INK}"/><circle cx="48" cy="4" r="10" fill="{INK}"/>
  <path d="M-40 78q40-26 80 0" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
  <path d="M-14-58q14-16 28 0" fill="none" stroke="{SKINL}" stroke-width="4"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M520 90l-100 60"/></g>''', arrow=True, ground=False)

add('glow', '暗がりでやわらかくぼうっと光る', f'''
<path d="M0 0h600v400H0z" fill="#1e2338"/>
<g transform="translate(300 210)">
  <circle r="140" fill="{TONES['gold'][1]}" opacity="0.10"/>
  <circle r="100" fill="{TONES['gold'][1]}" opacity="0.16"/>
  <circle r="66" fill="{TONES['gold'][1]}" opacity="0.28"/>
  <circle r="40" fill="#fdf0d0" class="o"/>
  <path d="M-24-40h48v-30h-48z" fill="#8f9aa6" class="o"/>
</g>
<path d="M0 350h600v50H0z" fill="#2b3242"/>
{person(120, 350, 0.8, 1, 'teal', 'blue', 'reach', 'bun', 'smile')}''', ground=False)

# --- 形容詞 ------------------------------------------------------------------
add('frivolous', '大事な会議中にふざけて遊んでいる', f'''
{table(380)}
<g transform="translate(300 300)">
  <path d="M-240-30h480v40h-480z" fill="#c9a464" class="o"/>
</g>
{sit(140, 380, 0.95, 1, 'blue', 'blue', 'short', 'neutral', 'lap')}
{sit(460, 380, 0.95, -1, 'blue', 'blue', 'bun', 'neutral', 'lap')}
{sit(300, 380, 1.0, 1, 'coral', 'blue', 'cap', 'smile', 'up')}
<g fill="{TONES['coral'][0]}">
''' + ''.join(f'<circle cx="{280+i*24}" cy="{170-abs(i-1)*20}" r="13"/>' for i in range(3)) + f'''
</g>
<g transform="translate(180 200)">{doc(0, 0, 90, 60, 2)}</g>
{cross(470, 180, 0.6)}''', ground=False)

add('frugal', 'ぜいたくをせず、必要なものだけで暮らす', f'''
{split()}
{table(380)}
<g transform="translate(150 300)">
  <path d="M-110-20h220v30h-220z" fill="#c9a464" class="o"/>
''' + ''.join(f'<g transform="translate({-70+i*70} -50)"><ellipse rx="30" ry="10" fill="#fffdf6" class="o"/><path d="M-30 0q0 14 30 14t30-14z" fill="#fffdf6" class="o"/></g>' for i in range(3)) + f'''
</g>
{cross(150, 130, 0.6)}
<g transform="translate(450 300)">
  <path d="M-110-20h220v30h-220z" fill="#c9a464" class="o"/>
  <g transform="translate(0 -50)"><ellipse rx="34" ry="12" fill="#fffdf6" class="o"/><path d="M-34 0q0 16 34 16t34-16z" fill="#fffdf6" class="o"/></g>
</g>
{coin(520, 200, 20)}
{coin(556, 220, 17)}
<circle cx="450" cy="270" r="120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('futile', '底の抜けたバケツに水を注ぎ続ける', f'''
{table(380)}
<g transform="translate(300 260)">
  <path d="M-70-60h140l-14 100q-2 16-56 16t-56-16z" fill="#9aa5b0" class="o"/>
  <path d="M-70-60q0-34 70-34t70 34" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M-30 52h60v10h-60z" fill="#fffaf1"/>
</g>
<g transform="translate(300 130) rotate(30)">
  <path d="M-40-40h80l-10 60q-2 12-30 12t-30-12z" fill="#e8f0f6" class="o"/>
</g>
<g fill="{TONES['blue'][0]}">
  <path d="M300 190q10 12 10 20t-10 8-10-8 10-20z"/>
  <path d="M300 330q10 12 10 20t-10 8-10-8 10-20z"/>
</g>
<g fill="{TONES['blue'][1]}"><ellipse cx="300" cy="384" rx="80" ry="12"/></g>
{cross(480, 160, 0.7)}''', ground=False)

add('geographic', '山や川や国境を示した地図', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-220-150h440v300h-440z" fill="#f0e6d0" class="o"/>
  <path d="M-220 60q120-40 220 0t220-20v110h-440z" fill="#8fb8d4"/>
  <path d="M-220 60q120-40 220 0t220-20" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <g fill="#9aa5b0" class="o">
    <path d="M-160 20l60-100 50 60 60-80 70 120z"/>
  </g>
  <path d="M100-150v210" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 8"/>
  <g class="greenp o"><circle cx="150" cy="-60" r="26"/><circle cx="190" cy="-20" r="20"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="2">
''' + ''.join(f'<path d="M-220 {-110+i*50}h440"/>' for i in range(5)) + ''.join(f'<path d="M{-180+i*70} -150v300"/>' for i in range(6)) + f'''
  </g>
</g>''', ground=False)

add('glossy', 'つやのある表面と、つやのない表面', f'''
{split()}
{table(380)}
<g transform="translate(150 260)">
  <path d="M-90-70h180v140h-180z" fill="#b8a894" class="o"/>
</g>
<g transform="translate(450 260)">
  <path d="M-90-70h180v140h-180z" fill="#8f9aa6" class="o"/>
  <g fill="#fffefd" opacity="0.75">
    <path d="M-70-56l50 0-70 100v-60z"/>
    <path d="M10-56h30l-70 118h-16z"/>
  </g>
</g>
<circle cx="450" cy="260" r="120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><circle cx="150" cy="260" r="120"/></g>''', ground=False)

add('graceful', '軽やかに手足を伸ばして舞う', f'''
{table(380)}
<g transform="translate(300 380)">
  <path d="M-10-10l-60 8M10-10l50-40" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-26-84q26-14 52 0l-8 78h-36z" class="violet o"/>
  <path d="M-24-76l-56-30M24-76l56-46" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cy="-114" r="25" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['bun']}" transform="translate(0 -6) scale(1.04)" fill="{HAIR}"/>
  <circle cx="-8" cy="-110" r="2.4" fill="{INK}"/><circle cx="8" cy="-110" r="2.4" fill="{INK}"/>
  <path d="M-8-98q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2"/>
  <path d="M-26-6q26-16 52 0l30 6h-112z" class="violetp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8">
  <path d="M120 200q80-90 180-40t180-30"/>
</g>''', ground=False)

add('gracious', '客を招き入れて丁重にもてなす', f'''
{table(380)}
<g transform="translate(430 200)">
  <path d="M-110-160h220v320h-220z" fill="{BRN}" class="o"/>
  <path d="M-86-136h172v272h-172z" fill="#a0764a"/>
  <path d="M-86-136h172v272h-172z" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>
{person(250, 380, 1.1, 1, 'violet', 'gold', 'give', 'bun', 'smile')}
{person(430, 380, 0.95, -1, 'coral', 'blue', 'walk', 'short', 'smile', 'walk')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M330 200h80"/></g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M170 220l-24-18M190 280h-26"/>
</g>''', ground=False)

add('greasy', '油が浮いてぎとぎとした料理', f'''
{table(340)}
<g transform="translate(300 270)">
  <ellipse rx="130" ry="34" fill="#fffdf6" class="o"/>
  <path d="M-130 0q0 40 130 40t130-40z" fill="#fffdf6" class="o"/>
  <path d="M-70-16q70-36 140-4 6 26-30 30-80 6-110-26z" fill="#c8934a" class="o"/>
  <g fill="{TONES['gold'][0]}" opacity="0.8">
''' + ''.join(f'<ellipse cx="{-60+i*36}" cy="{-4+(i%3)*10}" rx="{12-(i%3)*3}" ry="{8-(i%3)*2}"/>' for i in range(6)) + f'''
  </g>
</g>
<g fill="{TONES['gold'][0]}">
  <path d="M170 200q10 12 10 20t-10 8-10-8 10-20z"/>
</g>
{cross(470, 160, 0.7)}''', ground=False)

add('greenish', '完全な緑ではなく、緑がかった色', f'''
{table(380)}
<g class="o">
  <rect x="80" y="200" width="120" height="140" fill="{TONES['green'][0]}"/>
  <rect x="240" y="200" width="120" height="140" fill="#8fae86"/>
  <rect x="400" y="200" width="120" height="140" fill="#b8bfb0"/>
</g>
<circle cx="300" cy="270" r="96" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g class="a" marker-end="url(#ar)"><path d="M140 140h340"/></g>''', arrow=True, ground=False)

add('gullible', '見えすいたうそをすぐ信じ込む', f'''
{table(380)}
{person(180, 380, 1.1, 1, 'violet', 'blue', 'point', 'short', 'smile')}
{person(450, 380, 1.15, -1, 'coral', 'blue', 'up', 'bun', 'surprised')}
<g transform="translate(310 170)">
  <path d="M-70-40h140q12 0 12 12v40q0 12-12 12h-96l-22 16v-16q-12 0-12-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}"><rect x="-46" y="-16" width="92" height="9" rx="4.5"/><rect x="-46" y="4" width="60" height="9" rx="4.5"/></g>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M520 220l24-18M530 280h26"/>
</g>
<circle cx="450" cy="290" r="110" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('habitual', '毎朝きまって同じ時刻に同じことをする', f'''
{table(380)}
<g>
''' + ''.join(f'''<g transform="translate({110+i*130} 250)">
  <circle r="46" fill="#fffdf6" class="o"/>
  <path d="M0 0v-30M0 0l16 10" stroke="{INK}" stroke-width="4.5" stroke-linecap="round" fill="none"/>
  <circle r="5" fill="{INK}"/>
  <g transform="translate(0 80)">
    <ellipse rx="30" ry="10" fill="#fffdf6" class="o"/>
    <path d="M-30 0q0 14 30 14t30-14z" fill="#fffdf6" class="o"/>
  </g>
</g>''' for i in range(4)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M60 140h480"/></g>''', arrow=True, ground=False)

add('hasty', '確かめずに急いで書いて誤りを残す', f'''
{split()}
{table(380)}
<g transform="translate(150 230)">
  {doc(0, 0, 170, 210, 5)}
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4">
    <path d="M-40 60l40 20M0 60l-40 20"/>
  </g>
</g>
<g transform="translate(150 100)">
  <circle r="34" fill="#fffdf6" class="o"/>
  <path d="M0 0v-22M0 0l16 10" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round" fill="none"/>
</g>
<g transform="translate(450 230)">
  {doc(0, 0, 170, 210, 5)}
  {tick(30, 62, 0.4)}
</g>
<circle cx="150" cy="240" r="130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('hazardous', 'どくろの印のついた、危険な薬品', f'''
{table(380)}
<g transform="translate(300 260)">
  <path d="M-70-90h140v150q0 18-70 18t-70-18z" class="goldp o"/>
  <path d="M-70-90h140v-16h-140z" fill="#c8d0d8" class="o"/>
  <path d="M-24-106h48v-16h-48z" fill="{INK}"/>
  <g transform="translate(0 -20)">
    <path d="M0-44l46 80h-92z" fill="#fffdf6" class="o"/>
    <g fill="{INK}">
      <circle cx="0" cy="12" r="16"/>
      <path d="M-14 24h28v12h-28z"/>
    </g>
    <g fill="#fffdf6"><circle cx="-6" cy="8" r="4"/><circle cx="6" cy="8" r="4"/></g>
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M160 200l-26-22M440 196l26-22M150 300l-30 8M450 296l30 8"/>
</g>''', ground=False)

add('heroic', '燃える建物に飛び込んで人を助け出す', f'''
<path d="M0 0h600v400H0z" fill="#3b2a28"/>
<path d="M0 350h600v50H0z" fill="#2b201e" class="o"/>
<g transform="translate(400 350)">
  <path d="M-130 0v-190h260V0z" fill="#5a4a44" class="o"/>
  <g fill="#e8983a" class="o">
    <rect x="-100" y="-160" width="60" height="50"/><rect x="-20" y="-160" width="60" height="50"/>
    <rect x="-60" y="-80" width="60" height="50"/>
  </g>
</g>
{flame(360, 200, 1.1)}
{person(150, 350, 1.1, 1, 'coral', 'blue', 'carry', 'cap', 'neutral', 'walk')}
<g transform="translate(130 260)">
  <path d="M-46-16q46-24 92 0-30 30-92 0z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <circle cx="-52" cy="-24" r="20" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M220 160H80"/></g>''', ground=False)

add('heterogeneous', '形も色もばらばらのものが混ざっている', f'''
{split()}
{table(380)}
<g class="o">
  <circle cx="90" cy="220" r="26" class="coralp"/>
  <rect x="150" y="196" width="52" height="52" class="tealp"/>
  <path d="M240 196l30 52h-60z" class="goldp"/>
  <ellipse cx="110" cy="310" rx="32" ry="22" class="violetp"/>
  <rect x="170" y="284" width="44" height="52" rx="10" class="greenp"/>
  <circle cx="250" cy="310" r="22" class="bluep"/>
</g>
<g class="o">
''' + ''.join(f'<circle cx="{370+ (i%3)*70}" cy="{220+(i//3)*90}" r="30" class="tealp"/>' for i in range(6)) + f'''
</g>
<circle cx="170" cy="270" r="130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><circle cx="440" cy="270" r="130"/></g>''', ground=False)

add('homogeneous', 'まったく同じものだけがそろっている', f'''
{split()}
{table(380)}
<g class="o">
  <circle cx="90" cy="220" r="26" class="coralp"/>
  <rect x="150" y="196" width="52" height="52" class="tealp"/>
  <path d="M240 196l30 52h-60z" class="goldp"/>
  <ellipse cx="110" cy="310" rx="32" ry="22" class="violetp"/>
  <rect x="170" y="284" width="44" height="52" rx="10" class="greenp"/>
  <circle cx="250" cy="310" r="22" class="bluep"/>
</g>
<g class="o">
''' + ''.join(f'<circle cx="{370+ (i%3)*70}" cy="{220+(i//3)*90}" r="30" class="tealp"/>' for i in range(6)) + f'''
</g>
<circle cx="440" cy="270" r="130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><circle cx="170" cy="270" r="130"/></g>''', ground=False)

add('hideous', '見るにたえないほど醜い置き物', f'''
{table(340)}
<g transform="translate(300 250)">
  <path d="M-70 60q-40-50-10-90 20-30 10-60 30 20 50-10 10 40 40 30 20 40-10 70 30 30-10 60-40 20-70 0z" fill="#8a7a5c" class="o"/>
  <g fill="{INK}"><circle cx="-24" cy="-20" r="8"/><circle cx="30" cy="-6" r="6"/></g>
  <path d="M-20 24q30 20 50-6" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M-56-40l-24-16M60-56l26-10" stroke="#8a7a5c" stroke-width="10" stroke-linecap="round" fill="none"/>
</g>
{person(500, 380, 0.85, -1, 'teal', 'blue', 'up', 'bun', 'sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M130 170l-26-22M470 180l26-22"/>
</g>''', ground=False)

add('honourable', '負けを認めて正々堂々と手を差し出す', f'''
{table(380)}
{person(200, 380, 1.05, 1, 'teal', 'blue', 'give', 'short', 'neutral')}
{person(430, 380, 1.05, -1, 'coral', 'gold', 'give', 'bun', 'smile')}
<g>
  <path d="M268 260q40-14 76 0" stroke="{SKINL}" stroke-width="26" stroke-linecap="round" fill="none"/>
  <path d="M268 260q40-14 76 0" stroke="{SKIN}" stroke-width="21" stroke-linecap="round" fill="none"/>
</g>
<g transform="translate(500 220)">
  <path d="M-30-24h60v14h-60z" class="gold o"/>
  <path d="M-30-24l-8-42 22 18 16-28 16 28 22-18-8 42z" class="gold o"/>
</g>
<circle cx="200" cy="290" r="110" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('horrific', 'こわれた車と割れたガラス、ぞっとする事故現場', f'''
{table(380)}
<path d="M0 300h600v100H0z" fill="#6f7b88"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 330) rotate(-10)">
  <path d="M-130 30h260v-46q0-16-16-16h-64l-40-38H-84l-24 38h-22q-16 0-16 16z" class="coral o"/>
  <path d="M-84-32h96l30 38H-108z" fill="#c8d0d8" class="o"/>
  <path d="M-30-20l40 30M10-20l-40 30" stroke="{INK}" stroke-width="4" fill="none"/>
  <circle cx="-70" cy="30" r="22" fill="{INK}"/><circle cx="70" cy="30" r="22" fill="{INK}"/>
  <path d="M40-14q40-20 60 10-40 20-60-10z" fill="{TONES['coral'][2]}"/>
</g>
<g fill="#e8f0f6" class="o">
''' + ''.join(f'<path d="M{430+i*34} {350+(i%3)*16}l20 8-10 18-20-10z"/>' for i in range(4)) + f'''
</g>
{person(80, 380, 0.85, 1, 'teal', 'blue', 'up', 'bun', 'surprised')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M150 220l-26-22M60 200l-20-24"/>
</g>''', ground=False)

add('hospitable', '訪ねてきた客に温かい飲み物を出す', f'''
{table(380)}
{person(180, 380, 1.05, 1, 'teal', 'gold', 'give', 'bun', 'smile')}
{person(450, 380, 1.05, -1, 'coral', 'blue', 'give', 'short', 'smile')}
<g transform="translate(320 250)">
  <path d="M-40-40h80l-8 66q-2 12-32 12t-32-12z" fill="#e8f0f6" class="o"/>
  <path d="M40-24q34 0 34 22t-34 22" fill="none" stroke="{INK}" stroke-width="7"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" opacity="0.8">
    <path d="M-18-56q12-20 0-36M14-60q12-22 0-40"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 180q70-40 130 10"/></g>''', arrow=True, ground=False)

add('hygienic', '手を洗ってから調理する、清潔なやり方', f'''
{split()}
{table(380)}
<g transform="translate(150 260)">
  <path d="M-100 20q60-30 200 0" stroke="{SKIN}" stroke-width="56" stroke-linecap="round" fill="none"/>
  <path d="M-100 20q60-30 200 0" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
  <g fill="{INK}" opacity="0.55">
''' + ''.join(f'<circle cx="{-40+i*36}" cy="{10+(i%3)*14}" r="7"/>' for i in range(4)) + f'''
  </g>
</g>
{cross(150, 140, 0.6)}
<g transform="translate(450 260)">
  <path d="M-100 20q60-30 200 0" stroke="{SKIN}" stroke-width="56" stroke-linecap="round" fill="none"/>
  <path d="M-100 20q60-30 200 0" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
  <g fill="#fffefd" stroke="{MUTED}" stroke-width="2">
''' + ''.join(f'<circle cx="{-40+i*36}" cy="{-30-(i%3)*14}" r="{12-(i%3)*3}"/>' for i in range(4)) + f'''
  </g>
</g>
{tick(450, 140, 0.6)}''', ground=False)

add('hyperactive', 'じっとしていられず動き回り続ける', f'''
{table(380)}
{chair(150, 380, 1.0, 'gold', 1)}
<g opacity="0.3">{person(150, 380, 0.95, 1, 'coral', 'blue', 'stand', 'cap', 'smile')}</g>
{person(320, 380, 1.0, 1, 'coral', 'blue', 'walk', 'cap', 'smile', 'walk')}
{person(470, 340, 1.0, 1, 'coral', 'blue', 'up', 'cap', 'smile')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 8">
  <path d="M210 300q60-90 160-40t90-40"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M540 240l24-20M550 300h-26"/>
</g>''', ground=False)

add('hypersensitive', 'ごく軽く触れただけで大きく反応する', f'''
{split()}
{table(380)}
<g transform="translate(150 260)">
  <path d="M-100 20q60-24 200 0" stroke="{SKIN}" stroke-width="52" stroke-linecap="round" fill="none"/>
  <path d="M-100 20q60-24 200 0" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
</g>
{finger('M150 130L166 200', 24) if False else ''}
<g>
  <path d="M150 130l16 70" fill="none" stroke="{SKINL}" stroke-width="26" stroke-linecap="round"/>
  <path d="M150 130l16 70" fill="none" stroke="{SKIN}" stroke-width="21" stroke-linecap="round"/>
</g>
<g transform="translate(450 260)">
  <path d="M-100 20q60-24 200 0" stroke="{SKIN}" stroke-width="52" stroke-linecap="round" fill="none"/>
  <path d="M-100 20q60-24 200 0" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
  <g class="coral o" opacity="0.7"><ellipse cx="16" cy="12" rx="54" ry="30"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M400 200l-26-24M500 196l26-24M380 300l-30 10M520 296l30 10"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 260h60"/></g>''', arrow=True, ground=False)

add('hypocritical', '禁煙を説きながら自分は吸っている', f'''
{table(380)}
{person(300, 380, 1.2, 1, 'violet', 'blue', 'point', 'short', 'neutral')}
<g transform="translate(150 160)">
  <path d="M-60-40h120q12 0 12 12v40q0 12-12 12h-80l-20 16v-16q-12 0-12-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <g transform="translate(0 -4)">
    <path d="M-30-8h50v16h-50z" fill="#fffdf6" class="o"/>
    <path d="M20-8h14v16H20z" class="corald"/>
    <circle r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
    <path d="M-20 20L20-20" stroke="{TONES['coral'][0]}" stroke-width="5" fill="none"/>
  </g>
</g>
<g transform="translate(374 262) rotate(-16)">
  <path d="M-40-7h60v14h-60z" fill="#fffdf6" class="o"/>
  <path d="M20-7h16v14H20z" class="corald"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" opacity="0.8">
    <path d="M44-14q14-22 0-40"/>
  </g>
</g>
{cross(500, 150, 0.7)}''', ground=False)

add('hypothetical', '「もし〜だったら」という、実在しない話', f'''
{table(380)}
{person(140, 380, 1.05, 1, 'teal', 'blue', 'think', 'bun', 'neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><ellipse cx="400" cy="200" rx="170" ry="130"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8">
  <path d="M330 260v-90h140v90M330 170l70-50 70 50"/>
  <path d="M350 200h40v40h-40z"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3">
  <circle cx="230" cy="270" r="12"/><circle cx="270" cy="240" r="16"/>
</g>
<g transform="translate(540 90)">
  <path d="M-18-30q0-24 18-24t18 24-18 20v12" fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="26" r="5.5" fill="{MUTED}"/>
</g>''', ground=False)

add('iconic', 'ひと目でそれと分かる、誰もが知る形', f'''
<path d="M0 0h600v300H0z" fill="#dceaf4"/>
<path d="M0 300h600v100H0z" fill="#c9d8c0"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 300)">
  <path d="M-90 0l30-120h20l-14-60 24-40 24 40-14 60h20l30 120z" fill="#8f9aa6" class="o"/>
  <g fill="none" stroke="#6f7b88" stroke-width="4">
    <path d="M-60-120h120M-40-60h80"/>
  </g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M300 60v40"/></g>
{head(100, 340, 20, 'coral', 'bob')}
{head(500, 340, 20, 'teal', 'short')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="3" stroke-dasharray="8 7"><path d="M140 310l100-30M460 310l-100-30"/></g>
{tick(100, 200, 0.5)}
{tick(500, 200, 0.5)}''', ground=False)

add('idealistic', '現実の予算を見ずに、理想の案だけを描く', f'''
{split()}
{table(380)}
<g transform="translate(150 230)">
  <path d="M-110-120h220v240h-220z" fill="#e1edfb" class="o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4">
    <path d="M-80 100V-40l80-60 80 60v140z"/><path d="M-40 100V40h30v60M20 20h40v40H20z"/>
  </g>
  <circle cx="60" cy="-70" r="20" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"/>
</g>
<g transform="translate(450 230)">
  {doc(0, 0, 180, 220, 4)}
  <path d="M-60 70h130" stroke="{MUTED}" stroke-width="3" fill="none"/>
  <rect x="0" y="80" width="70" height="18" rx="9" class="coral"/>
</g>
<circle cx="150" cy="240" r="140" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('identifiable', '同じ服の中で、一人だけ名札があって見分けがつく', f'''
{table(380)}
''' + ''.join(person(90+i*100, 380, 0.9, 1, 'blue', 'blue', 'stand', 'short', 'neutral') for i in [0,1,3,4]) + f'''
{person(350, 380, 0.9, 1, 'blue', 'blue', 'stand', 'short', 'smile')}
<g transform="translate(350 280)">
  <path d="M-34-16h68v32h-68z" fill="#fffefd" class="o"/>
  {word(0, 0, 3, 18, INK)}
</g>
<circle cx="350" cy="300" r="90" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M500 130l-100 90"/></g>''', ground=False)

add('spatial', '物と物のあいだの距離や配置をつかむ', f'''
{table(380)}
<g transform="translate(300 240)">
  <path d="M-140-60h100v100h-100z" class="tealp o"/>
  <path d="M40-30h100v70H40z" class="coralp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 6">
    <path d="M-40-10h80M-90-60v-40M-90 40v40"/>
  </g>
  <g class="a" marker-end="url(#ar)"><path d="M-30-10h60M30-10h-60"/></g>
  <g class="a" marker-end="url(#ar)"><path d="M-90-70v-30M-90-100v30"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="2">
''' + ''.join(f'<path d="M60 {160+i*50}h480"/>' for i in range(5)) + ''.join(f'<path d="M{60+i*60} 160v200"/>' for i in range(9)) + f'''
</g>''', arrow=True, ground=False)

add('supplemental', '本体に足す、補いの一冊', f'''
{table(380)}
<g transform="translate(230 250)">
  <path d="M-100-120h200v240h-200z" fill="#fffdf6" class="o"/>
  <path d="M-100-120h34v240h-34z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">
''' + ''.join(f'<path d="M-56 {-92+i*26}h130"/>' for i in range(8)) + f'''
  </g>
</g>
<g transform="translate(430 300)">
  <path d="M-60-70h120v140h-120z" fill="#fffdf6" class="o"/>
  <path d="M-60-70h22v140h-22z" class="coral o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">
''' + ''.join(f'<path d="M-30 {-50+i*26}h80"/>' for i in range(4)) + f'''
  </g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M340 200h50M365 175v50"/>
</g>''', ground=False)

add('unsatisfactory', '求めた水準に届かず、やり直しになる', f'''
{table(380)}
<g transform="translate(300 220) rotate(-3)">
  {doc(0, 0, 200, 250, 5)}
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5">
    <path d="M-70-40l40 20M-30-40l-40 20M20 10l40 20M60 10l-40 20"/>
  </g>
  <circle cx="60" cy="86" r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M470 130q70 70 0 130"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M60 120h180"/></g>
{cross(120, 320, 0.6)}''', ground=False)

add('depressive', '気分が沈み、何もする気が起きない', f'''
<path d="M0 0h600v400H0z" fill="#5b6470"/>
{table(380)}
{sit(300, 380, 1.2, 1, 'blue', 'blue', 'bob', 'sad', 'down')}
{chair(300, 380, 1.1, 'blue', 1)}
<g transform="translate(300 250)">
  <path d="M-24-6q12 10 22 0M2-6q12 10 22 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round" transform="translate(-4 0)"/>
</g>
{cloud(300, 110, 1.4, 'blue')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{240+i*32} {170+(i%3)*22}l-10 30"/>' for i in range(5)) + f'''
</g>
<g fill="{MUTED}" opacity="0.35"><ellipse cx="300" cy="300" rx="180" ry="100"/></g>''', ground=False)

add('developmental', '子どもが段階を追って育っていく', f'''
{table(380)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M40 300h520"/></g>
<g transform="translate(110 300)">
  <ellipse cy="-20" rx="34" ry="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <circle cy="-56" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 52) scale(0.9)" fill="{HAIR}"/>
</g>
{person(250, 300, 0.6, 1, 'coral', 'blue', 'stand', 'cap', 'smile')}
{person(390, 300, 0.9, 1, 'coral', 'blue', 'stand', 'cap', 'smile')}
{person(520, 300, 1.2, 1, 'coral', 'blue', 'stand', 'short', 'smile')}
<g class="a" marker-end="url(#ar)"><path d="M60 350h480"/></g>''', arrow=True, ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
