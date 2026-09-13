# -*- coding: utf-8 -*-
"""第137回。職業と身のまわりの物、b- の形容詞。"""
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


# --- 職業・人 ----------------------------------------------------------------
add('butcher', '肉屋が包丁で肉を切り分ける', f'''
<path d="M0 0h600v400H0z" fill="#e8eef2"/>
{table(330)}
<g transform="translate(300 240)">
  <path d="M-200-40h400v40h-400z" fill="#c8d0d8" class="o"/>
  <path d="M-180-100h360v60h-360z" fill="#fffdf6" class="o"/>
  <g class="o">
    <path d="M-140-90q40-24 76 0 6 22-24 26-46 4-52-26z" fill="#c4604a"/>
    <path d="M-30-88q44-22 80 4 4 22-28 24-48 2-52-28z" fill="#c4604a"/>
    <path d="M80-86q40-20 74 4 2 20-26 22-44 2-48-26z" fill="#c4604a"/>
  </g>
</g>
{person(150, 330, 1.05, 1, 'teal', 'teal', 'reach', 'bun', 'smile')}
<g transform="translate(240 220) rotate(-16)">
  <path d="M-70-26h100l30 26-30 20h-100z" fill="#dde3e8" class="o"/>
  <path d="M-110-10h44v20h-44q-8 0-8-10t8-10z" fill="{INK}"/>
</g>
<g transform="translate(430 200)">
  <path d="M-60-16h120v32h-120z" class="coral o"/>
</g>''', ground=False)

add('carpenter', '大工がのこぎりで板を切る', f'''
{table(360)}
<g transform="translate(300 300)">
  <path d="M-200-30h400v30h-400z" fill="#c9a464" class="o"/>
  <path d="M-160 0v60M160 0v60" stroke="#a0764a" stroke-width="14" stroke-linecap="round" fill="none"/>
</g>
<g transform="translate(320 250) rotate(-6)">
  <path d="M-160-20h320v40h-320z" fill="#d9b877" class="o"/>
  <g fill="none" stroke="#b08c50" stroke-width="3"><path d="M-160 0h320"/></g>
</g>
{person(130, 360, 1.05, 1, 'gold', 'blue', 'reach', 'cap', 'neutral')}
<g transform="translate(250 200) rotate(24)">
  <path d="M-30-10h40v20h-40z" fill="{INK}"/>
  <path d="M10-16h150l-10 32H10z" fill="#dde3e8" class="o"/>
  <g fill="{INK}">
''' + ''.join(f'<path d="M{20+i*16} 16l8 12 8-12z"/>' for i in range(8)) + f'''
  </g>
</g>
<g fill="#d9b877">
''' + ''.join(f'<path d="M{380+i*30} {310+(i%3)*16}q12-14 22 0-10 12-22 0z"/>' for i in range(4)) + f'''
</g>''', ground=False)

add('cashier', 'レジ係が代金を受け取っておつりを返す', f'''
{table(380)}
<g transform="translate(300 290)">
  <path d="M-200-20h400v30h-400z" fill="#c9a464" class="o"/>
</g>
<g transform="translate(340 240)">
  <path d="M-70-50h140v50h-140z" fill="#5a6270" class="o"/>
  <path d="M-56-40h112v30h-112z" fill="#2c333d"/>
  <g fill="{TONES['green'][0]}"><rect x="-40" y="-32" width="16" height="14"/><rect x="-18" y="-32" width="16" height="14"/><rect x="4" y="-32" width="16" height="14"/></g>
  <path d="M-80 0h160v50h-160z" fill="#8f9aa6" class="o"/>
  <g fill="#c8d0d8"><rect x="-64" y="12" width="128" height="26" rx="4"/></g>
</g>
{person(140, 380, 1.0, 1, 'teal', 'teal', 'give', 'bun', 'smile')}
{person(510, 380, 1.0, -1, 'coral', 'blue', 'give', 'short', 'smile')}
{coin(240, 190, 18)}
<g class="a" marker-end="url(#ar)"><path d="M300 150q60-40 120 0"/></g>''', arrow=True, ground=False)

# --- 物 ---------------------------------------------------------------------
add('beak', '鳥の口が固くとがったくちばしになっている', f'''
{table(350)}
<g transform="translate(280 250)">
  <ellipse rx="80" ry="60" class="gold o"/>
  <circle cx="70" cy="-36" r="42" class="gold o"/>
  <circle cx="82" cy="-42" r="5" fill="{INK}"/>
  <path d="M-76-16q-46-30-56 10 42 28 62 10z" class="goldd o"/>
  <g stroke="{TONES['gold'][2]}" stroke-width="8" stroke-linecap="round" fill="none"><path d="M-20 58v20M20 58v20"/></g>
</g>
<g transform="translate(390 208)">
  <path d="M0-16l70 14-70 18z" class="corald o"/>
  <path d="M0-2h64" fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M520 120l-80 70"/></g>''', arrow=True, ground=False)

add('bestseller', '書店の一番よく売れる棚に平積みされた本', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
{table(380)}
<g transform="translate(300 300)">
  <path d="M-220-20h440v30h-440z" fill="#c9a464" class="o"/>
</g>
<g>
''' + ''.join(f'<g transform="translate({300+i*3} {266-i*22})"><path d="M-90-14h180v28h-180z" class="coral o"/><path d="M-90-14h180v6h-180z" fill="#fffdf6"/></g>' for i in range(4)) + f'''
</g>
<g transform="translate(300 130)">
  <path d="M-110-40h220v50h-220z" class="gold o"/>
  <rect x="-80" y="-24" width="160" height="18" rx="9" fill="#fffefd"/>
  <path d="M0 10l7 14 15 2-11 12 3 16-14-8-14 8 3-16-11-12 15-2z" class="goldd"/>
</g>
{person(510, 380, 0.8, -1, 'teal', 'blue', 'reach', 'bun', 'smile')}''', ground=False)

add('blender', '刃の回るミキサーで果物を混ぜてジュースにする', f'''
{table(360)}
<g transform="translate(300 250)">
  <path d="M-70-110h140l-16 130h-108z" fill="#e8f0f6" class="o" opacity="0.9"/>
  <path d="M-56-70h112l-10 86q-2 12-46 12t-46-12z" class="coralp"/>
  <path d="M-56-70h112" stroke="{TONES['coral'][0]}" stroke-width="3" fill="none"/>
  <path d="M-70-110h140v-16h-140z" fill="#c8d0d8" class="o"/>
  <path d="M70-90q26 0 26 20t-26 20" fill="none" stroke="#c8d0d8" stroke-width="9"/>
  <path d="M-60 20h120v60q0 14-60 14t-60-14z" fill="#5a6270" class="o"/>
  <circle cx="30" cy="52" r="14" fill="#8f9aa6" class="o"/>
  <g fill="#8f9aa6" class="o">
    <path d="M-20 8q30-14 40 6-30 14-40-6z" transform="rotate(20 0 8)"/>
    <path d="M20 8q-30-14-40 6 30 14 40-6z" transform="rotate(-20 0 8)"/>
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M420 200q26 20 0 40M450 180q40 30 0 80"/>
</g>''', ground=False)

add('blouse', '襟とボタンのある女性用の上着', f'''
{table(340)}
<g transform="translate(300 220)">
  <path d="M-90-70q90-36 180 0l-16 140h-148z" class="violetp o"/>
  <path d="M-90-70l-50 50 26 26 34-40M90-70l50 50-26 26-34-40" class="violetp o"/>
  <path d="M-30-84h60l-30 44z" fill="#fffaf1"/>
  <path d="M-30-84l30 44-40-30zM30-84l-30 44 40-30z" class="violet o"/>
  <g fill="{TONES['violet'][2]}">
''' + ''.join(f'<circle cx="0" cy="{-20+i*30}" r="6"/>' for i in range(4)) + f'''
  </g>
  <path d="M0-40v112" stroke="{TONES['violet'][0]}" stroke-width="2.5" fill="none"/>
</g>''', ground=False)

add('cardigan', '前をボタンで開け閉めする毛糸の上着', f'''
{table(340)}
<g transform="translate(300 220)">
  <path d="M-90-70q90-34 180 0l-16 140h-148z" class="goldp o"/>
  <path d="M-90-70l-50 50 26 26 34-40M90-70l50 50-26 26-34-40" class="goldp o"/>
  <path d="M-20-78h40l-6 148h-28z" fill="#fffaf1"/>
  <path d="M-20-78l-14 148h20l8-148zM20-78l14 148h-20l-8-148z" class="gold o"/>
  <g fill="{TONES['gold'][2]}">
''' + ''.join(f'<circle cx="-24" cy="{-44+i*34}" r="6"/>' for i in range(4)) + f'''
  </g>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="2.5">
''' + ''.join(f'<path d="M-86 {-30+i*30}q30 14 60 0"/>' for i in range(4)) + f'''
  </g>
</g>''', ground=False)

add('bracelet', '手首にはめる輪の飾り', f'''
{table(380)}
<g transform="translate(300 240) rotate(-16)">
  <path d="M-160-30h180q20 0 20 30t-20 30h-180z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <ellipse cx="40" ry="46" rx="20" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <g fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5">
    <rect x="56" y="-34" width="60" height="18" rx="9"/><rect x="60" y="-10" width="64" height="18" rx="9"/><rect x="56" y="14" width="56" height="18" rx="9"/>
  </g>
  <ellipse cx="-40" ry="42" rx="16" fill="none" stroke="{TONES['gold'][0]}" stroke-width="12"/>
  <circle cx="-40" cy="-44" r="9" class="coral o"/>
  <circle cx="-40" cy="44" r="9" class="teal o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 130l60 60"/></g>''', arrow=True, ground=False)

add('cello', '床に立てて弓で弾く大きな弦楽器', f'''
{table(380)}
<g transform="translate(300 250)">
  <path d="M-60 90q-70 0-70-60t70-60q40 0 46 30 6 30 0 60-6 30-46 30z" fill="#a8552c" class="o"/>
  <path d="M60 90q70 0 70-60t-70-60q-42 0-48 30-6 30 0 60 6 30 48 30z" fill="#a8552c" class="o"/>
  <path d="M-24 0q-10 12 0 24M-24 24q10 12 20 0" fill="none" stroke="#7c3a1c" stroke-width="4"/>
  <path d="M-20-70h40v-100h-40z" fill="#5b4a3c" class="o"/>
  <path d="M-24-170h48v-30h-48z" fill="#a8552c" class="o"/>
  <g fill="none" stroke="#e8dcc0" stroke-width="2.5">
''' + ''.join(f'<path d="M{-12+i*8} 70v-240"/>' for i in range(4)) + f'''
  </g>
  <path d="M-6 90h12v50h-12z" fill="#8f9aa6" class="o"/>
</g>
<g transform="translate(420 210) rotate(-70)">
  <path d="M-100-5h200v10h-200z" fill="#c9a464" class="o"/>
</g>''', ground=False)

add('cathedral', '塔とバラ窓のある大きな石造りの聖堂', f'''
<path d="M0 0h600v300H0z" fill="#dceaf4"/>
<path d="M0 300h600v100H0z" fill="#c9d8c0"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 300)">
  <path d="M-140 0v-200h280V0z" fill="#d6cdba" class="o"/>
  <path d="M-140-200h280l-140-70z" fill="#c0b6a0" class="o"/>
  <path d="M-190 0v-160h50V0zM190 0v-160h-50V0z" fill="#d6cdba" class="o"/>
  <path d="M-190-160l25-70 25 70zM190-160l-25-70-25 70z" fill="#c0b6a0" class="o"/>
  <circle cy="-140" r="42" class="bluep o"/>
  <g fill="none" stroke="{TONES['blue'][2]}" stroke-width="4">
''' + ''.join(f'<path d="M0-140l{34*math.cos(i*0.785):.0f} {-140+34*math.sin(i*0.785):.0f}"/>' for i in range(8)) + f'''
  </g>
  <path d="M-40 0v-70q0-40 40-40t40 40V0z" fill="{BRN}" class="o"/>
  <path d="M-8-270h16v-30H-8z" fill="#c0b6a0"/>
  <path d="M-16-292h32v-10h-32z" fill="#c0b6a0"/>
</g>''', ground=False)

add('bull', '角と太い首を持つ雄牛', f'''
<path d="M0 0h600v250H0z" fill="#dceaf4"/>
<path d="M0 250h600v150H0z" fill="#c9d8c0"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 290)">
  <ellipse cy="-50" rx="130" ry="66" fill="#5b4a3c" class="o"/>
  <path d="M100-90q34-40 56-58l40 24q-24 26-52 60z" fill="#5b4a3c" class="o"/>
  <ellipse cx="196" cy="-142" rx="46" ry="34" fill="#5b4a3c" class="o" transform="rotate(-16 196 -142)"/>
  <path d="M226-158l26-4-14 26z" fill="#3d3229" class="o"/>
  <path d="M162-172q-30-30-6-46 20 12 20 40zM222-180q26-32 46-18-6 24-32 34z" fill="#e8dcc0" class="o"/>
  <circle cx="200" cy="-152" r="5" fill="{INK}"/>
  <path d="M-130-56q-46-14-58-52 46 4 66 42z" fill="#3d3229" class="o"/>
  <g stroke="#3d3229" stroke-width="18" stroke-linecap="round" fill="none">
    <path d="M-80 0v46M-30 4v42M50 0v46M96 0v46"/>
  </g>
  <circle cx="234" cy="-134" r="6" class="gold o"/>
</g>''', ground=False)

add('calf', 'ふくらはぎの筋肉と、そばにいる子牛', f'''
{table(380)}
<g transform="translate(180 250)">
  <path d="M-30-90h60v40q30 30 20 80t-50 50-50-50 20-80z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-40 30q40-40 80 0" fill="none" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-30 100h60v20h-60z" fill="{INK}"/>
</g>
<circle cx="180" cy="270" r="56" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10"/>
<g transform="translate(430 300) scale(0.7)">
  <ellipse cy="-50" rx="100" ry="56" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><ellipse cx="-30" cy="-56" rx="26" ry="18"/><ellipse cx="40" cy="-34" rx="20" ry="14"/></g>
  <circle cx="86" cy="-96" r="34" fill="#fffdf6" class="o"/>
  <path d="M60-118q-16-20-4-26 12-2 14 20zM106-120q14-20 24-12 4 12-14 20z" fill="#e8c9a0" class="o"/>
  <circle cx="96" cy="-100" r="4" fill="{INK}"/>
  <g stroke="#c9a464" stroke-width="12" stroke-linecap="round" fill="none"><path d="M-40 0v30M30 0v30"/></g>
</g>''', ground=False)

add('calorie', '食品の袋にエネルギー量が示されている', f'''
{table(340)}
<g transform="translate(230 240)">
  <path d="M-80-90h160v180h-160z" class="goldp o"/>
  <path d="M-80-90q80-26 160 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"/>
  <path d="M-60-40h120v90h-120z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><rect x="-44" y="-24" width="80" height="14" rx="7"/></g>
  {word(-4, 16, 3, 28, TONES['coral'][0])}
</g>
{flame(430, 300, 0.6)}
<g class="a" marker-end="url(#ar)"><path d="M330 250h60"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M120 150h360"/></g>''', arrow=True, ground=False)

add('change', 'お札で払っておつりの小銭を受け取る', f'''
{table(340)}
{person(140, 340, 1.0, 1, 'teal', 'blue', 'give', 'bun', 'smile')}
{person(470, 340, 1.0, -1, 'coral', 'blue', 'give', 'short', 'smile')}
<g transform="translate(240 200) rotate(-8)">
  <path d="M-56-26h112v52h-112z" class="greenp o"/>
  <circle r="15" fill="none" stroke="{TONES['green'][2]}" stroke-width="3"/>
</g>
{coin(340, 270, 20)}
{coin(378, 288, 17)}
{coin(310, 296, 15)}
<g class="a" marker-end="url(#ar)"><path d="M200 150q90-40 170 0"/></g>
<g class="a" marker-end="url(#ar)"><path d="M400 320q-90 30-170 0"/></g>''', arrow=True, ground=False)

add('blink', '目を一瞬とじてすぐ開ける', f'''
{split()}
<g transform="translate(150 200)">
  <circle r="110" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-92-34q6-74 92-74t92 74q-44-34-92-34t-92 34z" fill="{HAIR}"/>
  <circle cx="-42" cy="-6" r="18" fill="#fffefd" class="o"/><circle cx="-42" cy="-6" r="8" fill="{INK}"/>
  <circle cx="42" cy="-6" r="18" fill="#fffefd" class="o"/><circle cx="42" cy="-6" r="8" fill="{INK}"/>
  <path d="M-22 54q22 16 44 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
</g>
<g transform="translate(450 200)">
  <circle r="110" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-92-34q6-74 92-74t92 74q-44-34-92-34t-92 34z" fill="{HAIR}"/>
  <path d="M-60-6q18 14 36 0M24-6q18 14 36 0" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <path d="M-22 54q22 16 44 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 340h60"/></g>
<g class="a" marker-end="url(#ar)"><path d="M330 366h-60"/></g>''', arrow=True, ground=False)

# --- b- の形容詞 ---------------------------------------------------------------
add('bearable', '重すぎて持てない荷と、なんとか持てる荷', f'''
{split()}
{table(380)}
{person(150, 380, 1.05, 1, 'coral', 'blue', 'up', 'short', 'sad')}
<g transform="translate(150 240)">
  <path d="M-80-40h160v70h-160z" fill="#9aa5b0" class="o"/>
</g>
{cross(150, 130, 0.6)}
{person(450, 380, 1.05, 1, 'coral', 'blue', 'up', 'short', 'neutral')}
<g transform="translate(450 250)">
  <path d="M-44-24h88v44h-88z" fill="#9aa5b0" class="o"/>
</g>
{tick(450, 130, 0.6)}''', ground=False)

add('belated', '誕生日を過ぎてから遅れて贈り物が届く', f'''
{table(380)}
<g transform="translate(180 200)">
  <path d="M-120-110h240v220h-240z" class="paper"/>
  <path d="M-120-110h240v40h-240z" class="coral o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5">
''' + ''.join(f'<path d="M{-120+i*48} -70v180"/>' for i in range(6)) + ''.join(f'<path d="M-120 {-24+i*44}h240"/>' for i in range(4)) + f'''
  </g>
  <circle cx="-24" cy="-46" r="20" class="coral o"/>
</g>
<g transform="translate(440 280)">
  <path d="M-60-40h120v80h-120z" class="teal o"/>
  <path d="M-60-40h120v-16h-120z" class="teald o"/>
  <path d="M-8-56h16v96h-16z" class="coral"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M240 150q120-60 190 60"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M156 340v40h300"/></g>''', ground=False)

add('biannual', '一年のうち二回だけ印がついている', f'''
{table(380)}
<g transform="translate(300 220)">
  <path d="M-260-30h520v60h-520z" fill="#e0d6c0" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">
''' + ''.join(f'<path d="M{-260+i*43} -30v{18 if i%2 else 30}"/>' for i in range(13)) + f'''
  </g>
  <circle cx="-130" r="24" class="coral o"/>
  <circle cx="130" r="24" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M40 130h520"/></g>
<g class="a" marker-end="url(#ar)"><path d="M560 130H40"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="8 6"><path d="M170 330v-70M430 330v-70"/></g>''', arrow=True, ground=False)

add('bilateral', '二つの国が向き合って両方から取り決める', f'''
{table(380)}
<g transform="translate(150 260)">
  <path d="M0 100V-60" stroke="{BRN}" stroke-width="8" stroke-linecap="round" fill="none"/>
  <path d="M4-60q60 10 96-10 6 40-4 58-46 14-92 4z" class="coral o"/>
</g>
<g transform="translate(450 260)">
  <path d="M0 100V-60" stroke="{BRN}" stroke-width="8" stroke-linecap="round" fill="none"/>
  <path d="M-4-60q-60 10-96-10-6 40 4 58 46 14 92 4z" class="teal o"/>
</g>
<g transform="translate(300 260)">
  {doc(0, 0, 130, 150, 3)}
  {tick(0, 44, 0.35)}
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 180h60"/></g>
<g class="a" marker-end="url(#ar)"><path d="M420 180h-60"/></g>''', arrow=True, ground=False)

add('bland', '香辛料を入れないうすい味のスープ', f'''
{split()}
{table(340)}
<g transform="translate(150 260)">
  <path d="M-80-50h160l-14 80q-2 16-66 16t-66-16z" fill="#9aa5b0" class="o"/>
  <path d="M-70-20h140l-8 46q-2 12-62 12t-62-12z" fill="#e8dcc0"/>
</g>
<g transform="translate(450 260)">
  <path d="M-80-50h160l-14 80q-2 16-66 16t-66-16z" fill="#9aa5b0" class="o"/>
  <path d="M-70-20h140l-8 46q-2 12-62 12t-62-12z" fill="#c8703a"/>
  <g class="o"><circle cx="-30" cy="6" r="10" class="green"/><circle cx="20" cy="12" r="9" class="coral"/></g>
</g>
<g transform="translate(430 130) rotate(30)">
  <path d="M-18 0h36l-5 44q-2 8-13 8t-13-8z" fill="#fffdf6" class="o"/>
  <path d="M-18 0q0-14 18-14t18 14z" fill="#b8bfc8" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M120 150q-14 10-14 26"/>
</g>''', ground=False)

add('blatant', '「立入禁止」の札の真下で堂々と入っていく', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-90-70h180v90h-180z" class="coral o"/>
  <path d="M-60-30h120v16h-120z" fill="#fffefd"/>
  <path d="M0 20v40" stroke="{BRN}" stroke-width="10" fill="none"/>
</g>
{person(300, 380, 1.05, 1, 'violet', 'blue', 'walk', 'cap', 'smile', 'walk')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M380 320h130"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M300 260v90"/></g>
{cross(140, 200, 0.8)}''', ground=False)

add('blunt', '切れる刃と、まるくなって切れない刃', f'''
{split()}
{table(340)}
<g transform="translate(150 250) rotate(-10)">
  <path d="M-90-24h140l40 24-40 12h-140z" fill="#dde3e8" class="o"/>
  <path d="M-90 12h180" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M50-6h80q12 0 12 9t-12 9H50z" fill="{INK}"/>
</g>
<g transform="translate(450 250) rotate(-10)">
  <path d="M-90-24h140q20 8 20 18t-20 18h-140z" fill="#c8d0d8" class="o"/>
  <path d="M-90 12h170" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M50-6h80q12 0 12 9t-12 9H50z" fill="{INK}"/>
</g>
{tick(150, 130, 0.6)}
{cross(450, 130, 0.6)}''', ground=False)

add('blurred', 'はっきりした写真と、輪郭のぼやけた写真', f'''
{split()}
{table(380)}
<g transform="translate(150 230)">
  <path d="M-100-90h200v180h-200z" class="paper"/>
  <circle cx="-30" cy="-20" r="34" class="goldp o"/>
  <path d="M-70 60L-20-10l30 34 34-44 46 80z" class="greenp o"/>
</g>
<g transform="translate(450 230)">
  <path d="M-100-90h200v180h-200z" class="paper"/>
  <g opacity="0.5">
    <circle cx="-34" cy="-20" r="38" fill="{TONES['gold'][1]}"/>
    <circle cx="-26" cy="-20" r="38" fill="{TONES['gold'][1]}"/>
    <path d="M-74 60L-24-10l30 34 34-44 46 80z" fill="{TONES['green'][1]}"/>
    <path d="M-66 60L-16-10l30 34 34-44 46 80z" fill="{TONES['green'][1]}"/>
  </g>
</g>
{tick(150, 120, 0.6)}
{cross(450, 120, 0.6)}''', ground=False)

add('boastful', '小さな成果を大声で自慢して回る', f'''
{table(380)}
{person(200, 380, 1.15, 1, 'violet', 'gold', 'up', 'short', 'smile')}
<g transform="translate(200 290)">
  <path d="M-20-16h40v32h-40z" class="tealp o"/>
</g>
<g transform="translate(410 190)">
  <path d="M-120-70h240q14 0 14 14v80q0 14-14 14h-160l-28 20v-20q-14 0-14-14v-80q0-14 14-14z" fill="#fffefd" class="o"/>
  <path d="M-64-34h128v82h-128z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M120 210l-26-22M280 170l6-26"/>
</g>
{head(120, 350, 20, 'coral', 'bob')}''', ground=False)

add('boisterous', '子どもたちが元気に走り回って騒がしい', f'''
{table(380)}
''' + ''.join(person(90+i*110, 380, 0.85, 1 if i%2 else -1, ['coral','gold','teal','violet','green'][i%5], 'blue', 'up', ['cap','bob','short','bun'][i%4], 'smile', 'walk') for i in range(5)) + f'''
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{90+i*110} 210q20-24 40 0"/>' for i in range(5)) + f'''
</g>
<g class="o">
  <circle cx="300" cy="120" r="20" class="coral"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M120 300q100-60 200 0t180-40"/></g>''', ground=False)

add('bookish', '本ばかり読んでいて外へ出ない', f'''
{table(380)}
{sit(240, 380, 1.15, 1, 'teal', 'blue', 'bun', 'smile', 'lap')}
{chair(240, 380, 1.05, 'gold', 1)}
<g transform="translate(290 250) rotate(-12)">
  <path d="M-70-50h140v100h-140z" fill="#fffefd" class="o"/>
  <path d="M0-50v100" stroke="{INK}" stroke-width="3" fill="none"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="{-58+ (i%2)*62}" y="{-34+(i//2)*22}" width="46" height="7" rx="3.5"/>' for i in range(6)) + f'''
  </g>
</g>
<g>
''' + ''.join(f'<g transform="translate({470+ (i%2)*4} {360-i*26})"><path d="M-70-12h140v24h-140z" class="{["coral","teal","gold","violet"][i%4]} o"/></g>' for i in range(6)) + f'''
</g>
<g transform="translate(120 180)">
  <path d="M-50-40h100v80h-100z" fill="#dceaf4" class="o"/>
  {sun(20, -16, 14)}
</g>
{cross(120, 300, 0.5)}''', ground=False)

add('boundless', '見わたすかぎり果てのない空と海', f'''
<path d="M0 0h600v200H0z" fill="#dceaf4"/>
<path d="M0 200h600v200H0z" fill="#7aa8c4"/>
<path d="M0 200h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="#a8c8dd" stroke-width="4">
''' + ''.join(f'<path d="M0 {240+i*40}h600"/>' for i in range(4)) + f'''
</g>
{sun(500, 70, 34)}
<g class="a" marker-end="url(#ar)"><path d="M300 120h250"/></g>
<g class="a" marker-end="url(#ar)"><path d="M300 120H50"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 8"><path d="M40 120h520"/></g>
{person(300, 200, 0.7, 1, 'coral', 'blue', 'up', 'bob', 'smile')}''', arrow=True, ground=False)

add('breathless', '階段を上りきって息を切らす', f'''
{table(380)}
<g fill="#c9a464" class="o">
''' + ''.join(f'<path d="M{40+i*80} {380-i*44}h{520-i*80}v44h-{520-i*80}z"/>' for i in range(5)) + f'''
</g>
{person(430, 200, 1.0, 1, 'coral', 'blue', 'stand', 'cap', 'sad')}
<g transform="translate(430 90)">
  <ellipse rx="20" ry="16" fill="{INK}"/>
</g>
<g fill="{TONES['blue'][0]}">
  <path d="M380 120q9 10 9 17t-9 8-9-8 9-17z"/><path d="M488 116q9 10 9 17t-9 8-9-8 9-17z"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M350 160q-16 10-16 26M520 156q16 10 16 26"/>
</g>''', ground=False)

add('brittle', 'かたいが、たたくとぱりんと割れる', f'''
{split()}
{table(380)}
<g transform="translate(150 260)">
  <path d="M-70-70h140v140h-140z" fill="#e8f0f6" class="o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"><path d="M-50-40h100M-50 30h100"/></g>
</g>
<g transform="translate(450 260)">
  <g fill="#e8f0f6" class="o">
    <path d="M-70-70h60l10 70-40 20z"/><path d="M-10-70h80v50l-60 20z"/>
    <path d="M-70 20l40-20 20 40-30 30z"/><path d="M10 0l60-20v90h-46z"/>
  </g>
</g>
<g transform="translate(400 130) rotate(30)">
  <path d="M-10-60h20v70h-20z" fill="#c9a464" class="o"/>
  <path d="M-30 10h40v34q0 10-20 10t-20-10z" fill="#8f9aa6" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 260h60"/></g>''', arrow=True, ground=False)

add('bulky', '重くはないが大きくてかさばる荷物', f'''
{table(380)}
{person(180, 380, 1.05, 1, 'teal', 'blue', 'up', 'cap', 'sad')}
<g transform="translate(330 250)">
  <path d="M-130-110h260v220h-260z" class="goldp o"/>
  <path d="M-130-110l26-30h260l-26 30z" fill="{TONES['gold'][1]}" class="o"/>
  <path d="M130-110l26-30v220l-26 30z" class="gold o"/>
</g>
<g transform="translate(500 340)">
  <path d="M-40-20h80v40h-80z" fill="#c8d0d8" class="o"/>
  <path d="M-24-30h48v10h-48z" fill="#8f9aa6"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M200 120h260"/></g>
<g class="a" marker-end="url(#ar)"><path d="M460 120H200"/></g>''', arrow=True, ground=False)

add('bustling', '市場が人でにぎわって活気がある', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(300 130)">
  <path d="M-260-40h520v30h-520z" class="coral o"/>
  <g fill="{TONES['coral'][1]}">
''' + ''.join(f'<path d="M{-260+i*66} -10h33v24h-33z"/>' for i in range(8)) + f'''
  </g>
</g>
<g transform="translate(300 260)">
  <path d="M-250-20h500v30h-500z" fill="#c9a464" class="o"/>
  <g class="o">
''' + ''.join(f'<circle cx="{-210+i*60}" cy="-40" r="20" class="{["coralp","tealp","goldp","violetp","greenp"][i%5]}"/>' for i in range(8)) + f'''
  </g>
</g>
<g>
''' + ''.join(person(60+i*70, 380, 0.7, 1 if i%2 else -1, ['coral','teal','gold','violet','green','blue'][i%6], 'blue', 'walk', ['short','bob','bun','cap'][i%4], 'smile', 'walk') for i in range(8)) + f'''
</g>''', ground=False)

add('catastrophic', '津波で町がすっかり押し流される', f'''
<path d="M0 0h600v400H0z" fill="#8f9aa6"/>
<path d="M0 300h600v100H0z" fill="#6b7a86"/>
<path d="M0 300q60-140 180-120t120 60 160-140 140 80v220H0z" fill="#4d7fa4" class="o"/>
<g fill="none" stroke="#a8c8dd" stroke-width="6">
  <path d="M60 260q60-40 120 0M340 200q60-40 120 0"/>
</g>
<g fill="#c8b8a0" class="o" opacity="0.9">
  <path d="M120 340l40-10 10 40-40 8z" transform="rotate(20 140 350)"/>
  <path d="M330 360l46-14 12 40-46 12z" transform="rotate(-24 350 370)"/>
  <path d="M460 330l40-12 12 34-40 12z" transform="rotate(34 480 340)"/>
</g>
<g fill="{MUTED}" opacity="0.5"><circle cx="140" cy="70" r="44"/><circle cx="230" cy="46" r="52"/><circle cx="330" cy="70" r="42"/></g>
{cross(520, 90, 0.9)}''', ground=False)

add('ceremonial', '式のためだけに使う飾りの剣と敷物', f'''
{table(380)}
<g transform="translate(300 330)">
  <path d="M-200-20h400v40h-400z" class="corald o"/>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4"><path d="M-180-10h360M-180 10h360"/></g>
</g>
<g transform="translate(300 190) rotate(20)">
  <path d="M-8-120h16v170h-16z" fill="#dde3e8" class="o"/>
  <path d="M-8-120l8-24 8 24z" fill="#c8d0d8" class="o"/>
  <path d="M-40 50h80v14h-80z" class="gold o"/>
  <path d="M-10 64h20v40h-20z" fill="#8b6437" class="o"/>
  <circle cy="110" r="12" class="gold o"/>
</g>
{person(110, 380, 0.85, 1, 'violet', 'gold', 'stand', 'bun', 'neutral')}
{person(500, 380, 0.85, -1, 'violet', 'gold', 'stand', 'short', 'neutral')}''', ground=False)

add('changeable', '一日のうちに晴れと雨がころころ変わる', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
{table(380)}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M200 40v340M400 40v340"/></g>
{sun(100, 140, 34)}
{cloud(300, 130, 1.1, 'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
''' + ''.join(f'<path d="M{260+i*30} {190+(i%2)*24}l-10 30"/>' for i in range(4)) + f'''
</g>
{sun(500, 140, 34)}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M80 320h440"/></g>''', ground=False)

add('chaotic', '机の上も床も物であふれて大混乱になる', f'''
{table(340)}
<g>
''' + ''.join(f'<g transform="translate({80+ (i%6)*80} {200+(i//6)*70}) rotate({-40+i*23})">{doc(0, 0, 60, 76, 2)}</g>' for i in range(12)) + f'''
</g>
<g class="o">
  <rect x="130" y="330" width="50" height="34" class="tealp" transform="rotate(24 155 347)"/>
  <circle cx="420" cy="350" r="20" class="coralp"/>
  <rect x="300" y="340" width="44" height="30" class="goldp" transform="rotate(-20 322 355)"/>
</g>
{person(530, 380, 0.85, -1, 'blue', 'blue', 'up', 'bun', 'sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M480 240l-24-18M570 230l20-18"/>
</g>''', ground=False)

add('brightness', '同じ画面の明るさを上げ下げする', f'''
{split()}
{table(380)}
<g transform="translate(150 220)">
  <path d="M-110-90h220v170h-220z" fill="#3b4450" class="o"/>
  <path d="M-96-76h192v142h-192z" fill="#5a6270"/>
  <path d="M-30 80h60v14h-60z" fill="#5a6270"/>
</g>
<g transform="translate(450 220)">
  <path d="M-110-90h220v170h-220z" fill="#3b4450" class="o"/>
  <path d="M-96-76h192v142h-192z" fill="#fff6e0"/>
  <path d="M-30 80h60v14h-60z" fill="#5a6270"/>
  {sun(0, -10, 30)}
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['gold'][0]}" stroke-width="5"><path d="M270 340h60"/></g>''', ground=False)

add('buzz', 'ハチがブンブンと羽音を立てて飛ぶ', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
{table(380)}
<g transform="translate(250 200)">
  <ellipse rx="60" ry="40" class="gold o"/>
  <g fill="{INK}"><path d="M-26-36q14 72 0 72zM10-38q14 76 0 76z"/></g>
  <circle cx="-52" cy="-6" r="24" fill="{INK}"/>
  <path d="M52-10l24 6-24 8z" class="goldd o"/>
  <g fill="#fffefd" stroke="{INK}" stroke-width="2.5" opacity="0.85">
    <ellipse cx="6" cy="-46" rx="46" ry="20" transform="rotate(-22 6 -46)"/>
    <ellipse cx="-14" cy="-40" rx="40" ry="17" transform="rotate(-40 -14 -40)"/>
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M350 160q26 40 0 80M390 130q40 70 0 140M430 100q54 100 0 200"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M90 300q60-90 130-70"/></g>''', ground=False)

add('discontent', '待遇に不満で顔をしかめる人が並ぶ', f'''
{table(380)}
''' + ''.join(person(110+i*100, 380, 0.95, 1, 'blue', 'blue', 'stand', ['short','bob','bun','cap'][i%4], 'sad') for i in range(4)) + f'''
<g>
''' + ''.join(f'''<g transform="translate({110+i*100} 240)">
  <path d="M-16-8q10-10 18 0M2-8q10-10 18 0" fill="none" stroke="{HAIR}" stroke-width="4" stroke-linecap="round" transform="translate(-2 0)"/>
</g>''' for i in range(4)) + f'''
</g>
<g transform="translate(480 180)">
  <path d="M-60-40h120q12 0 12 12v40q0 12-12 12h-80l-20 16v-16q-12 0-12-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <path d="M-30 6q30-24 60 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>''', ground=False)

# --- 連語・慣用表現 -----------------------------------------------------------
add('as-far-as-i-know', '知っている範囲はここまで、と線を引く', f'''
{table(380)}
{person(140, 380, 1.05, 1, 'teal', 'blue', 'point', 'bun', 'neutral')}
<g transform="translate(380 250)">
  <path d="M-160-90h320v180h-320z" fill="#e8f0e4" class="o"/>
  <path d="M-160-90h190v180h-190z" class="tealp"/>
  <path d="M30-90v180" stroke="{TONES['coral'][0]}" stroke-width="6" fill="none"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="{-140+ (i%2)*90}" y="{-60+(i//2)*44}" width="70" height="12" rx="6"/>' for i in range(6)) + f'''
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"><path d="M50-60h100M50-16h100M50 28h100"/></g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M250 150l140 20"/></g>''', ground=False)

add('aware-of', '後ろの物音に気づいて振り返る', f'''
{table(380)}
{person(300, 380, 1.15, -1, 'teal', 'blue', 'stand', 'bun', 'surprised')}
<g transform="translate(480 300)">
  <path d="M-40-20h80v40h-80z" fill="#c8d0d8" class="o" transform="rotate(24)"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M400 230q-26 26 0 52M370 208q-40 46 0 96"/>
</g>
<g transform="translate(330 250)">
  <ellipse rx="14" ry="18" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M6 6q-10-12 0-20" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g transform="translate(160 190)">
  <path d="M-40-30h80q10 0 10 10v30q0 10-10 10h-52l-18 14v-14q-10 0-10-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M-6-16h12v22h-12z" fill="{INK}"/>
  <circle cy="16" r="4" fill="{INK}"/>
</g>''', ground=False)

add('be-supposed-to', '掲示のとおり、この時刻に来ることになっている', f'''
{table(380)}
<g transform="translate(200 200)">
  <path d="M-120-120h240v240h-240z" class="paper"/>
  <rect x="-90" y="-94" width="150" height="16" rx="8" fill="{INK}"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-90" y="{-50+i*36}" width="{180-(i%3)*40}" height="12" rx="6"/>' for i in range(4)) + f'''
  </g>
  <path d="M-120 100h240" stroke="{MUTED}" stroke-width="3" fill="none"/>
</g>
<g transform="translate(450 200)">
  <circle r="80" fill="#fffdf6" class="o"/>
  <g fill="{INK}">
''' + ''.join(f'<rect x="-4" y="-66" width="8" height="16" rx="4" transform="rotate({i*30})"/>' for i in range(12)) + f'''
  </g>
  <path d="M0 0v-48" stroke="{INK}" stroke-width="7" stroke-linecap="round" fill="none"/>
  <path d="M0 0l34 20" stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none"/>
  <circle r="7" fill="{INK}"/>
</g>
{person(450, 380, 0.8, 1, 'coral', 'blue', 'walk', 'cap', 'smile', 'walk')}
{tick(560, 130, 0.5)}''', ground=False)

add('belong-to', '名前の書かれたかばんが持ち主のもとにある', f'''
{table(380)}
{person(430, 380, 1.1, 1, 'coral', 'blue', 'hold', 'bun', 'smile')}
<g transform="translate(370 300)">
  <path d="M-56-36h112v72h-112z" class="teal o"/>
  <path d="M-24-36q0-18 24-18t24 18" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M-34-10h68v26h-68z" fill="#fffdf6" class="o"/>
  {word(0, 4, 3, 18, MUTED)}
</g>
<g transform="translate(160 200)">
  <path d="M-60-26h120v52h-120z" fill="#fffefd" class="o"/>
  {word(0, 0, 4, 26, INK)}
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M240 220l90 60"/></g>''', ground=False)

add('by-chance', '道でばったり知り合いに出会う', f'''
<path d="M0 0h600v250H0z" fill="#dceaf4"/>
<path d="M0 250h600v150H0z" fill="#dfe8d8"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M0 340h600v50H0z" fill="#c9a464" class="o"/>
{person(220, 380, 1.05, 1, 'teal', 'blue', 'walk', 'bun', 'surprised', 'walk')}
{person(380, 380, 1.05, -1, 'coral', 'blue', 'walk', 'short', 'surprised', 'walk')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M170 230l-24-22M430 226l24-22"/>
</g>
<g transform="translate(300 130)">
  <path d="M-16-30q0-24 16-24t16 24-16 20v12" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="30" r="5.5" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M60 300h130"/></g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M540 300H410"/></g>''', ground=False)

add('capable-of', '重い荷を持ち上げるだけの力がある', f'''
{table(380)}
{person(300, 380, 1.2, 1, 'coral', 'blue', 'up', 'cap', 'neutral')}
<g fill="{INK}">
  <g transform="translate(300 180)">
    <rect x="-70" y="-11" width="140" height="22" rx="8"/>
    <rect x="-100" y="-34" width="26" height="68" rx="10"/><rect x="74" y="-34" width="26" height="68" rx="10"/>
  </g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M180 250l-24-18M420 246l24-18"/>
</g>
{tick(500, 320, 0.7)}''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
