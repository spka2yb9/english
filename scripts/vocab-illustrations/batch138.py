# -*- coding: utf-8 -*-
"""第138回。c- の形容詞と身のまわりの名詞。"""
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


# --- 物・場面 ----------------------------------------------------------------
add('checkout', 'かごの品をレジ台に出して会計する', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
{table(380)}
<g transform="translate(300 300)">
  <path d="M-220-20h440v30h-440z" fill="#c9a464" class="o"/>
  <path d="M-220-30h240v10h-240z" fill="#8f9aa6"/>
  <g fill="#6f7b88">
''' + ''.join(f'<rect x="{-210+i*34}" y="-28" width="20" height="8" rx="4"/>' for i in range(7)) + f'''
  </g>
</g>
<g class="o">
  <rect x="120" y="240" width="46" height="34" class="coralp"/>
  <rect x="180" y="234" width="46" height="40" class="tealp"/>
  <circle cx="260" cy="256" r="20" class="goldp"/>
</g>
<g transform="translate(390 240)">
  <path d="M-60-46h120v46h-120z" fill="#5a6270" class="o"/>
  <path d="M-46-36h92v26h-92z" fill="#2c333d"/>
  <g fill="{TONES['green'][0]}"><rect x="-32" y="-30" width="14" height="12"/><rect x="-12" y="-30" width="14" height="12"/></g>
  <path d="M-70 0h140v42h-140z" fill="#8f9aa6" class="o"/>
</g>
{person(500, 380, 0.85, -1, 'teal', 'teal', 'reach', 'bun', 'smile')}
{person(80, 380, 0.85, 1, 'coral', 'blue', 'reach', 'short', 'smile')}''', ground=False)

add('checkup', '医者が聴診器で体を調べる定期検診', f'''
{table(380)}
{sit(220, 380, 1.05, 1, 'coral', 'blue', 'bob', 'neutral', 'down')}
<g transform="translate(200 320)">
  <path d="M-90-20h180v30h-180z" fill="#fffdf6" class="o"/>
  <path d="M-90-20h180v-10h-180z" fill="{TONES['blue'][1]}"/>
</g>
{person(430, 380, 1.05, -1, 'teal', 'teal', 'reach', 'short', 'smile')}
<g transform="translate(430 240)">
  <path d="M-30 0q-30 0-30 40t30 50" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M30 0q30 0 30 40t-30 50" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M-30 90q30 30 60 0" fill="none" stroke="{INK}" stroke-width="5"/>
  <circle cx="-40" cy="94" r="18" fill="#c8d0d8" class="o"/>
</g>
<g transform="translate(120 200)">
  {doc(0, 0, 110, 130, 3)}
  {tick(0, 40, 0.35)}
</g>''', ground=False)

add('chimney', '屋根から突き出た煙突から煙が出る', f'''
<path d="M0 0h600v300H0z" fill="#dceaf4"/>
<path d="M0 300h600v100H0z" fill="#c9d8c0"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 300)">
  <path d="M-120 0v-100h240V0z" fill="#fffdf6" class="o"/>
  <path d="M-140-100L0-180l140 80z" class="coral o"/>
  <path d="M-70-80h50v40h-50z" class="bluep o"/>
  <path d="M10-60h50v60H10z" class="corald o"/>
</g>
<g transform="translate(370 180)">
  <path d="M-26-60h52v70h-52z" fill="#a8552c" class="o"/>
  <path d="M-32-60h64v-14h-64z" fill="#8b3a1c" class="o"/>
</g>
<g fill="{MUTED}" opacity="0.8">
  <circle cx="380" cy="80" r="24"/><circle cx="420" cy="46" r="30"/><circle cx="470" cy="26" r="22"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M520 180l-110-20"/></g>''', arrow=True, ground=False)

add('chorus', '大勢が声をそろえて一斉に歌う', f'''
{table(380)}
<g>
''' + ''.join(head(90+ (i%6)*84, 250+(i//6)*70, 24, ['coral','teal','gold','violet','green','blue'][i%6], ['short','bob','bun','cap'][i%4]) for i in range(11)) + f'''
</g>
<g>
''' + ''.join(f'<g transform="translate({90+ (i%6)*84} {286+(i//6)*70})"><ellipse rx="11" ry="9" fill="{INK}"/></g>' for i in range(11)) + f'''
</g>
<g fill="{INK}">
  <g transform="translate(140 130)"><ellipse rx="13" ry="10" transform="rotate(-20)"/><path d="M11-5v-44h4v44z"/></g>
  <g transform="translate(300 100)"><ellipse rx="13" ry="10" transform="rotate(-20)"/><path d="M11-5v-44h4v44z"/></g>
  <g transform="translate(460 130)"><ellipse rx="13" ry="10" transform="rotate(-20)"/><path d="M11-5v-44h4v44z"/></g>
</g>''', ground=False)

add('cinnamon', '巻いた樹皮の棒と、粉になったシナモン', f'''
{table(330)}
<g transform="translate(200 250) rotate(-16)">
  <path d="M-80-22h160v44h-160z" fill="#a8552c" class="o"/>
  <ellipse cx="-80" rx="14" ry="22" fill="#8b3a1c" class="o"/>
  <ellipse cx="-80" rx="7" ry="12" fill="#c8703a"/>
  <g fill="none" stroke="#8b3a1c" stroke-width="3"><path d="M-40-22v44M0-22v44M40-22v44"/></g>
</g>
<g transform="translate(210 300) rotate(10)">
  <path d="M-70-16h140v32h-140z" fill="#a8552c" class="o"/>
  <ellipse cx="-70" rx="11" ry="16" fill="#8b3a1c" class="o"/>
</g>
<g transform="translate(430 290)">
  <ellipse rx="70" ry="20" fill="#fffdf6" class="o"/>
  <path d="M-70 0q0 24 70 24t70-24z" fill="#fffdf6" class="o"/>
  <path d="M-40-8q40-22 80 0-40 16-80 0z" fill="#a8552c" class="o"/>
</g>
<g fill="#a8552c">
''' + ''.join(f'<circle cx="{380+i*26}" cy="{240+ (i%3)*14}" r="4"/>' for i in range(5)) + f'''
</g>''', ground=False)

add('comet', '長い尾を引いて夜空を横切る星', f'''
<path d="M0 0h600v400H0z" fill="#1e2338"/>
<g fill="#fffefd"><circle cx="90" cy="330" r="4"/><circle cx="520" cy="330" r="3"/><circle cx="180" cy="80" r="3"/><circle cx="480" cy="60" r="4"/></g>
<g transform="translate(430 150)">
  <circle r="34" fill="#fdf0d0" class="o"/>
  <circle r="18" fill="#fffefd"/>
  <g fill="#fdf0d0" opacity="0.6">
    <path d="M-30-24L-330 60l300 0z"/>
  </g>
  <g fill="none" stroke="#fdf0d0" stroke-width="4" opacity="0.8" stroke-linecap="round">
    <path d="M-40-14L-320 30M-36 6L-300 70M-30 22L-250 96"/>
  </g>
</g>
<path d="M0 380h600v20H0z" fill="#2b3242"/>
{person(120, 380, 0.7, 1, 'teal', 'blue', 'up', 'bob', 'surprised')}''', ground=False)

add('commuter', '毎朝同じ電車で職場へ通う人たち', f'''
<path d="M0 0h600v400H0z" fill="#e8eef2"/>
<path d="M0 340h600v60H0z" fill="#8f9aa6" class="o"/>
<g transform="translate(300 250)">
  <path d="M-260-100h520v190h-520z" class="bluep o"/>
  <path d="M-260-100h520v-20h-520z" class="blue o"/>
  <g fill="#dceaf4" class="o">
''' + ''.join(f'<rect x="{-240+i*84}" y="-80" width="64" height="60" rx="6"/>' for i in range(6)) + f'''
  </g>
  <g fill="{INK}"><rect x="-90" y="0" width="180" height="90" rx="6"/></g>
  <g fill="none" stroke="#5a6270" stroke-width="4"><path d="M0 0v90"/></g>
</g>
<g>
''' + ''.join(f'{head(-198+ i*84 + 300, 220, 18, ["teal","coral","gold","violet","green","blue"][i%6], ["short","bob","bun","cap"][i%4])}' for i in range(6)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M60 120h180"/></g>
<g class="a" marker-end="url(#ar)"><path d="M540 120H360"/></g>''', ground=False)

add('consonant', '口を閉じて息をせき止めて出す音', f'''
{split()}
{table(380)}
<g transform="translate(150 230)">
  <path d="M-90-90q90-40 180 0 20 120-20 160-70 24-140 0-40-40-20-160z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-60 40h120" stroke="{INK}" stroke-width="10" stroke-linecap="round" fill="none"/>
  <path d="M-40 40q40-20 80 0" fill="none" stroke="{SKINL}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M110 300l60 40M170 300l-60 40"/>
</g>
<g transform="translate(450 230)">
  <path d="M-90-90q90-40 180 0 20 120-20 160-70 24-140 0-40-40-20-160z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <ellipse cy="44" rx="34" ry="30" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M450 320v50"/></g>''', ground=False)

add('coupon', '切り取って使う割引券', f'''
{table(340)}
<g transform="translate(280 240) rotate(-4)">
  <path d="M-160-70h320v140h-320z" class="goldp o"/>
  <path d="M60-70v140" fill="none" stroke="{INK}" stroke-width="3" stroke-dasharray="10 8"/>
  <g fill="{INK}"><rect x="-130" y="-40" width="150" height="18" rx="9"/></g>
  <g fill="{MUTED}"><rect x="-130" y="-8" width="110" height="12" rx="6"/><rect x="-130" y="16" width="130" height="12" rx="6"/></g>
  <path d="M90-24h60v48H90z" class="coral o"/>
  <circle cx="60" cy="-70" r="12" fill="#fffaf1"/>
  <circle cx="60" cy="70" r="12" fill="#fffaf1"/>
</g>
<g transform="translate(420 140) rotate(30)">
  <g stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
    <path d="M-6-6l-56-20q-10-4-6-12t14-4L8-24z" fill="#cfd6dd"/>
    <path d="M-6 6l-56 20q-10 4-6 12t14 4L8 24z" fill="#8f9aa6"/>
  </g>
</g>''', ground=False)

add('cricket', '細長い体と長い触角を持つコオロギ', f'''
<path d="M0 0h600v290H0z" fill="#dceaf4"/>
<path d="M0 290h600v110H0z" fill="#c9d8c0"/>
<path d="M0 290h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(280 250)">
  <ellipse rx="90" ry="40" fill="#5b6a3c" class="o"/>
  <ellipse cx="-70" cy="-14" rx="34" ry="26" fill="#5b6a3c" class="o"/>
  <circle cx="-84" cy="-20" r="5" fill="{INK}"/>
  <g fill="none" stroke="#3f4a28" stroke-width="4" stroke-linecap="round">
    <path d="M-96-34q-50-40-90-40M-96-26q-54-24-96-10"/>
  </g>
  <path d="M-40-20q60-24 110 4-50 30-110-4z" fill="#4a5730" class="o"/>
  <g stroke="#3f4a28" stroke-width="8" stroke-linecap="round" fill="none">
    <path d="M-40 34l-24 30M10 38l10 30"/>
    <path d="M50 30l40-30-10 60"/>
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M420 200q26 30 0 60M456 176q40 52 0 104"/>
</g>''', ground=False)

# --- c- の形容詞 ---------------------------------------------------------------
add('charitable', '募金箱にお金を入れて困った人を助ける', f'''
{table(380)}
<g transform="translate(300 290)">
  <path d="M-80-70h160v100q0 16-80 16t-80-16z" class="tealp o"/>
  <path d="M-26-70h52v-12h-52z" fill="{INK}"/>
  <path d="M0-30q22 0 22 20t-22 24q-22-4-22-24 0-20 22-20z" class="coral o"/>
</g>
{coin(300, 150, 22)}
{person(130, 380, 0.95, 1, 'coral', 'blue', 'reach', 'bun', 'smile')}
{person(480, 380, 0.9, -1, 'gold', 'blue', 'up', 'short', 'smile')}
<g class="a" marker-end="url(#ar)"><path d="M300 180v30"/></g>''', arrow=True, ground=False)

add('cheerless', '窓もなく灰色ばかりの、気の滅入る部屋', f'''
<path d="M0 0h600v400H0z" fill="#7d838c"/>
<path d="M0 340h600v60H0z" fill="#666c74" class="o"/>
<g fill="none" stroke="#6b717a" stroke-width="3">
''' + ''.join(f'<path d="M0 {60+i*70}h600"/>' for i in range(4)) + f'''
</g>
<g transform="translate(300 300)">
  <path d="M-60-40h120v40h-120z" fill="#8f959e" class="o"/>
  <path d="M-40 0v40M40 0v40" stroke="#6b717a" stroke-width="10" fill="none"/>
</g>
{chair(150, 340, 1.0, 'blue', 1)}
<g fill="#8f959e" opacity="0.5"><ellipse cx="470" cy="330" rx="46" ry="14"/></g>
<g transform="translate(470 160)">
  <circle r="34" fill="#8f959e" class="o"/>
  <path d="M-16-6q10-8 16 0M4-6q10-8 16 0" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>
  <path d="M-14 20q14-14 28 0" fill="none" stroke="{INK}" stroke-width="3.5"/>
</g>''', ground=False)

add('chewy', 'かむのに時間がかかる、もちもちしたパン', f'''
{table(340)}
<g transform="translate(400 270)">
  <path d="M-70-40q70-30 140 0 10 46-16 60-54 14-108 0-26-14-16-60z" fill="#e8c98d" class="o"/>
  <path d="M-30 20q30-40 60 0" fill="none" stroke="#c9a464" stroke-width="14" stroke-linecap="round"/>
</g>
<g transform="translate(180 210)">
  <circle r="94" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-80-26q6-66 80-66t80 66q-40-30-80-30t-80 30z" fill="{HAIR}"/>
  <path d="M-50 4q16-14 30 0M20 4q16-14 30 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <ellipse cy="46" rx="30" ry="20" fill="{INK}"/>
  <path d="M-40 46q40 30 80 0" fill="none" stroke="{SKINL}" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 140q40 40 0 76"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M290 300h50"/></g>''', arrow=True, ground=False)

add('coercive', '力ずくで無理やり署名させる', f'''
{table(380)}
{person(180, 380, 1.15, 1, 'violet', 'blue', 'reach', 'short', 'neutral')}
{sit(430, 380, 1.0, -1, 'coral', 'blue', 'bob', 'sad', 'lap')}
<g transform="translate(360 290)">{doc(0, 0, 120, 100, 2)}</g>
<g>
  <path d="M250 250q60-16 100 10" stroke="{SKINL}" stroke-width="26" stroke-linecap="round" fill="none"/>
  <path d="M250 250q60-16 100 10" stroke="{SKIN}" stroke-width="21" stroke-linecap="round" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M250 180h130"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M480 250l24-18M490 300h26"/>
</g>''', ground=False)

add('coherent', 'ばらばらの話が筋の通った一本の流れになる', f'''
{split()}
{table(380)}
<g transform="translate(150 240)">
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="{-90+ (i%3)*66}" y="{-60+(i//3)*54}" width="52" height="16" rx="8" transform="rotate({-24+i*11} {-64+(i%3)*66} {-52+(i//3)*54})"/>' for i in range(6)) + f'''
  </g>
</g>
<g transform="translate(450 240)">
  <g fill="{INK}">
''' + ''.join(f'<rect x="-90" y="{-70+i*32}" width="{180-(i%3)*40}" height="16" rx="8"/>' for i in range(5)) + f'''
  </g>
  <g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="4"><path d="M-110-70v150"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 240h60"/></g>''', arrow=True, ground=False)

add('cohesive', 'ばらけていた班がまとまって一つになる', f'''
{split()}
{table(380)}
{head(70, 210, 20, 'teal', 'short')}
{head(230, 180, 20, 'coral', 'bun')}
{head(110, 330, 20, 'gold', 'cap')}
{head(240, 320, 20, 'green', 'bob')}
{head(160, 250, 20, 'violet', 'short')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"><ellipse cx="450" cy="270" rx="130" ry="90"/></g>
{head(390, 240, 20, 'teal', 'short')}
{head(450, 230, 20, 'coral', 'bun')}
{head(510, 240, 20, 'gold', 'cap')}
{head(420, 315, 20, 'green', 'bob')}
{head(485, 315, 20, 'violet', 'short')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3" stroke-dasharray="6 5">
  <path d="M390 240h60M450 230h60M420 315h65M390 240l30 75M510 240l-25 75"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 140h60"/></g>''', arrow=True, ground=False)

add('commendable', '努力を認めて賞状を渡す', f'''
{table(380)}
{person(170, 380, 1.05, 1, 'violet', 'gold', 'give', 'bun', 'smile')}
{person(440, 380, 1.05, -1, 'coral', 'blue', 'give', 'short', 'smile')}
<g transform="translate(305 240) rotate(-6)">
  <path d="M-80-56h160v112h-160z" class="paper"/>
  <rect x="-56" y="-36" width="112" height="14" rx="7" fill="{INK}"/>
  <g fill="{MUTED}"><rect x="-56" y="-10" width="80" height="10" rx="5"/></g>
  <circle cx="46" cy="26" r="20" class="gold o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 170q70-40 130 10"/></g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M510 200l24-18M520 260h26"/>
</g>''', arrow=True, ground=False)

add('communicative', 'よく話し、身ぶりも交えて伝えようとする', f'''
{table(380)}
{person(200, 380, 1.15, 1, 'coral', 'blue', 'up', 'bun', 'smile')}
{person(470, 380, 1.0, -1, 'teal', 'blue', 'stand', 'short', 'smile')}
<g>
''' + ''.join(f'''<g transform="translate({330+ (i%2)*40} {130+i*70})">
  <path d="M-70-30h140q12 0 12 12v30q0 12-12 12h-96l-18 14v-14q-12 0-12-12v-30q0-12 12-12z" fill="#fffefd" class="o"/>
  {word(0, -4, 4, 26, INK)}
</g>''' for i in range(3)) + f'''
</g>
{hand(130, 250, -1)}''', ground=False)

add('compact', '大きな機械と、同じ働きをする小型の機械', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-100-100h200v200h-200z" fill="#8f9aa6" class="o"/>
  <circle cy="-30" r="40" fill="#c8d0d8" class="o"/>
  <g fill="{INK}">
''' + ''.join(f'<rect x="-6" y="-78" width="12" height="18" rx="6" transform="rotate({i*45} 0 -30)"/>' for i in range(8)) + f'''
  </g>
  <path d="M-60 50h120v40h-120z" fill="#6f7b88" class="o"/>
</g>
<g transform="translate(450 290)">
  <path d="M-50-50h100v100h-100z" fill="#8f9aa6" class="o"/>
  <circle cy="-14" r="20" fill="#c8d0d8" class="o"/>
  <g fill="{INK}">
''' + ''.join(f'<rect x="-4" y="-38" width="8" height="12" rx="4" transform="rotate({i*60} 0 -14)"/>' for i in range(6)) + f'''
  </g>
  <path d="M-30 22h60v22h-60z" fill="#6f7b88" class="o"/>
</g>
{tick(450, 130, 0.6)}
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('compassionate', 'うずくまる人のそばにひざをついて寄り添う', f'''
{table(380)}
<g transform="translate(400 380)">
  <path d="M-20-6l-50 6M20-6l50 6" fill="none" stroke="{TONES['blue'][2]}" stroke-width="13" stroke-linecap="round"/>
  <path d="M-34-64q34-16 68 0l-10 58h-48z" class="blue o"/>
  <circle cy="-96" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['bob']}" transform="translate(0 12) scale(1.06)" fill="{HAIR}"/>
  <path d="M-14-98q8-8 16 0M-2-98q8-8 16 0" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <path d="M-8-78q8-8 16 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>
<g transform="translate(200 380)">
  <path d="M-10-8l50 8" fill="none" stroke="{TONES['blue'][2]}" stroke-width="14" stroke-linecap="round"/>
  <path d="M-30-80q30-16 60 0l-10 74h-42z" class="coral o"/>
  <path d="M28-70q60-10 110 20" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
  <circle cy="-112" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['bun']}" transform="translate(0 -4) scale(1.08)" fill="{HAIR}"/>
  <circle cx="-9" cy="-108" r="2.4" fill="{INK}"/><circle cx="9" cy="-108" r="2.4" fill="{INK}"/>
  <path d="M-9-96q9 8 18 0" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
<g fill="{TONES['coral'][0]}">
  <path d="M300 220q-14-20 0-28 14-6 18 10 4-16 18-10 14 8 0 28l-18 20z"/>
</g>''', ground=False)

add('complacent', '一位のまま練習をやめて油断する', f'''
{table(380)}
{sit(280, 380, 1.15, 1, 'gold', 'blue', 'short', 'smile', 'lap')}
{chair(280, 380, 1.05, 'gold', 1)}
<g transform="translate(280 250)">
  <path d="M-16-6q10-8 18 0M0-6q10-8 18 0" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round" transform="translate(-2 0)"/>
</g>
<g transform="translate(150 220)">
  <path d="M-30-24h60v14h-60z" class="gold o"/>
  <path d="M-30-24l-6-40 20 18 16-28 16 28 20-18-6 40z" class="gold o"/>
</g>
<g transform="translate(470 250)">
  <path d="M-90 90h180v20h-180z" fill="{MUTED}"/>
  <g class="coral o"><rect x="-70" y="-40" width="40" height="130"/><rect x="-14" y="10" width="40" height="80"/><rect x="42" y="50" width="40" height="40"/></g>
  <g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M-60-60l120 120"/></g>
</g>''', ground=False)

add('composed', '慌てる人の横で落ち着いて手順どおり動く', f'''
{split()}
{table(380)}
{person(150, 380, 1.1, 1, 'blue', 'blue', 'up', 'short', 'sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M90 220l-26-22M210 216l26-22"/>
</g>
{person(450, 380, 1.1, 1, 'teal', 'blue', 'reach', 'bun', 'neutral')}
<g transform="translate(520 290)">
  <path d="M-40-30h80v60h-80z" fill="#e8f0f6" class="o"/>
  {tick(0, 0, 0.3)}
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M380 300v-80"/></g>
{cross(150, 130, 0.5)}
{tick(450, 130, 0.5)}''', ground=False)

add('compulsive', '同じ動作を止められずに何度も繰り返す', f'''
{table(380)}
{person(220, 380, 1.15, 1, 'violet', 'blue', 'reach', 'bun', 'sad')}
<g transform="translate(340 290)">
  <path d="M-60-30h120v60h-120z" fill="#c8d0d8" class="o"/>
  <circle cx="-20" r="12" fill="{INK}"/><circle cx="20" r="12" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5">
  <path d="M420 250q60 40 0 80"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5">
  <path d="M440 240q80 50 0 100"/>
</g>
<g transform="translate(190 180)">
  <path d="M-40-30h80q10 0 10 10v30q0 10-10 10h-52l-18 14v-14q-10 0-10-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <g fill="{TONES['coral'][0]}"><circle cx="-18" r="6"/><circle cx="0" r="6"/><circle cx="18" r="6"/></g>
</g>''', ground=False)

add('conceited', '鏡に映る自分に見とれてうぬぼれる', f'''
{table(380)}
<g transform="translate(400 230)">
  <path d="M-100-140h200v280h-200z" fill="#c8d0d8" class="o"/>
  <path d="M-84-124h168v248h-168z" fill="#e8f0f6"/>
  <g opacity="0.85">
    <circle cy="-40" r="46" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <path d="M-40-56q4-40 40-40t40 40q-20-16-40-10-20-12-40 10z" fill="{HAIR}"/>
    <circle cx="-14" cy="-40" r="4" fill="{INK}"/><circle cx="14" cy="-40" r="4" fill="{INK}"/>
    <path d="M-12-22q12 10 24 0" fill="none" stroke="{INK}" stroke-width="3"/>
  </g>
</g>
{person(170, 380, 1.1, -1, 'violet', 'blue', 'hold', 'short', 'smile')}
<g fill="{TONES['coral'][0]}">
  <path d="M270 200q-14-20 0-28 14-6 18 10 4-16 18-10 14 8 0 28l-18 20z"/>
</g>''', ground=False)

add('conceivable', 'ありえないことではなく、考えられる範囲にある', f'''
{table(380)}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="14 10"><ellipse cx="300" cy="240" rx="200" ry="120"/></g>
<g class="o">
''' + ''.join(f'<circle cx="{190+ (i%4)*74}" cy="{200+(i//4)*80}" r="26" class="tealp"/>' for i in range(8)) + f'''
</g>
<circle cx="486" cy="200" r="26" class="coral o"/>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M540 120l-46 50"/></g>
{tick(120, 140, 0.6)}''', ground=False)

add('concise', '長い説明を短く言い切る', f'''
{split()}
{table(380)}
<g transform="translate(150 220)">
  <path d="M-100-130h200v260h-200z" class="paper"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-76" y="{-104+i*28}" width="{152-(i%3)*40}" height="9" rx="4.5"/>' for i in range(8)) + f'''
  </g>
</g>
<g transform="translate(450 220)">
  <path d="M-100-60h200v120h-200z" class="paper"/>
  <g fill="{INK}">
    <rect x="-76" y="-32" width="152" height="14" rx="7"/>
    <rect x="-76" y="-4" width="120" height="14" rx="7"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 220h60"/></g>
{tick(450, 340, 0.5)}''', arrow=True, ground=False)

add('conclusive', '疑いようのない、決め手になる証拠', f'''
{table(380)}
<g transform="translate(300 210)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-130" y="{-104+i*34}" width="{260-(i%3)*60}" height="11" rx="5.5"/>' for i in range(5)) + f'''
  </g>
  <g transform="translate(70 80)">
    <circle r="46" fill="none" stroke="{TONES['green'][0]}" stroke-width="6"/>
    {tick(0, 0, 0.55)}
  </g>
  <g transform="translate(-100 76)">
    <path d="M-40-30h80v60h-80z" class="tealp o"/>
  </g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M520 130l-24-20M540 200h-26"/>
</g>''', ground=False)

add('concurrent', '二つの仕事が同じ期間に並んで進む', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-230-50h340v50h-340z" class="tealp o"/>
  <path d="M-160 30h330v50h-330z" class="coralp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8">
    <path d="M-160-70v170M110-70v170"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M140 340h270"/></g>
<g class="a" marker-end="url(#ar)"><path d="M410 340H140"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M40 120h520"/></g>''', arrow=True, ground=False)

add('condescending', 'しゃがんで、相手を子ども扱いして話す', f'''
{table(380)}
<g transform="translate(200 380)">
  <path d="M-6-10l-40 10M30-10l30 10" fill="none" stroke="{TONES['blue'][2]}" stroke-width="13" stroke-linecap="round"/>
  <path d="M-30-80q30-16 60 0l-10 74h-42z" class="violet o"/>
  <path d="M30-70q50 20 70 0" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
  <circle cy="-112" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 -4) scale(1.08)" fill="{HAIR}"/>
  <path d="M-16-114q10-8 18 0M0-114q10-8 18 0" fill="none" stroke="{HAIR}" stroke-width="4" stroke-linecap="round"/>
  <path d="M-9-96q9 8 18 0" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
{person(420, 380, 1.05, -1, 'coral', 'blue', 'stand', 'bun', 'sad')}
<g>
  <path d="M300 310q50-14 80 6" stroke="{SKINL}" stroke-width="24" stroke-linecap="round" fill="none"/>
  <path d="M300 310q50-14 80 6" stroke="{SKIN}" stroke-width="19" stroke-linecap="round" fill="none"/>
</g>
<g transform="translate(300 180)">
  <path d="M-60-36h120q12 0 12 12v36q0 12-12 12h-80l-18 16v-16q-12 0-12-12v-36q0-12 12-12z" fill="#fffefd" class="o"/>
  {word(0, -4, 3, 24, MUTED)}
</g>''', ground=False)

add('confidential', '「部外秘」と押された封をした書類', f'''
{table(380)}
<g transform="translate(300 210) rotate(-4)">
  <path d="M-160-140h320v280h-320z" class="paper"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-124" y="{-104+i*36}" width="{248-(i%3)*60}" height="11" rx="5.5"/>' for i in range(5)) + f'''
  </g>
  <g transform="rotate(-14)">
    <path d="M-130-30h260v70h-260z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
    <g fill="{TONES['coral'][0]}">
''' + ''.join(f'<rect x="{-100+i*46}" y="-11" width="34" height="26" rx="6"/>' for i in range(4)) + f'''
    </g>
  </g>
</g>
<g transform="translate(500 320)">
  <path d="M-40-30h80v60h-80z" fill="#c9a464" class="o"/>
  <circle r="12" fill="{INK}"/>
  <path d="M-16-30v-16q0-18 16-18t16 18v16" fill="none" stroke="#8f9aa6" stroke-width="7"/>
</g>''', ground=False)

add('conscientious', '仕上げた仕事を隅から隅まで見直す', f'''
{table(380)}
<g transform="translate(280 210) rotate(-3)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <g>
''' + ''.join(f'''<g transform="translate(0 {-100+i*46})">
  <rect x="-140" y="-14" width="28" height="28" rx="5" fill="none" stroke="{INK}" stroke-width="3"/>
  <rect x="-98" y="-8" width="{200-(i%3)*40}" height="14" rx="7" fill="{MUTED}"/>
</g>''' for i in range(5)) + f'''
  </g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
''' + ''.join(f'<path d="M-134 {-100+i*46}l8 10 18-22"/>' for i in range(5)) + f'''
  </g>
</g>
{person(520, 380, 0.85, -1, 'teal', 'blue', 'reach', 'bun', 'neutral')}
<g transform="translate(470 190)">
  <circle r="40" fill="none" stroke="#8f9aa6" stroke-width="9"/>
  <path d="M28 28l30 30" stroke="{INK}" stroke-width="11" stroke-linecap="round" fill="none"/>
</g>''', ground=False)

add('constructive', 'こわす批判ではなく、直す案を出す', f'''
{split()}
{table(380)}
<g transform="translate(150 280)">
  <g fill="#c8b8a0" class="o">
    <path d="M-70 0h40v-40h-40zM-20-10h40v-30h-40z"/>
    <path d="M30 0l30-20 10 20z"/>
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round">
    <path d="M-40-100l60 60M20-100l-60 60"/>
  </g>
</g>
<g transform="translate(450 280)">
  <path d="M-60 0v-70h120V0z" fill="#fffdf6" class="o"/>
  <path d="M-72-70L0-120l72 50z" class="coral o"/>
  <path d="M-16-40h32V0h-32z" class="corald o"/>
</g>
<g transform="translate(540 170) rotate(-20)">
  <path d="M-10-50h20v70h-20z" fill="#c9a464" class="o"/>
  <path d="M-28 20h40v34q0 10-20 10t-20-10z" fill="#8f9aa6" class="o"/>
</g>
{cross(150, 140, 0.6)}
{tick(450, 140, 0.6)}''', ground=False)

add('contagious', 'せきをした人から次々にうつっていく', f'''
{table(380)}
{person(120, 380, 0.95, 1, 'coral', 'blue', 'up', 'short', 'sad')}
<g fill="{TONES['coral'][0]}" opacity="0.55">
''' + ''.join(f'<circle cx="{190+i*26}" cy="{230+ (i%3)*22}" r="{9-(i%3)*2}"/>' for i in range(6)) + f'''
</g>
{person(330, 380, 0.95, 1, 'gold', 'blue', 'stand', 'bob', 'sad')}
<g fill="{TONES['coral'][0]}" opacity="0.55">
''' + ''.join(f'<circle cx="{400+i*26}" cy="{240+ (i%3)*22}" r="{9-(i%3)*2}"/>' for i in range(4)) + f'''
</g>
{person(520, 380, 0.95, 1, 'teal', 'blue', 'stand', 'cap', 'sad')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M170 160h140M380 160h100"/></g>''', ground=False)

add('contemplative', '窓辺で静かに物思いにふける', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<g transform="translate(430 200)">
  <path d="M-130-150h260v300h-260z" fill="{BRN}" class="o"/>
  <path d="M-104-124h208v248h-208z" fill="#dceaf4"/>
  <path d="M0-124v248M-104 0h208" stroke="{BRN}" stroke-width="10" fill="none"/>
  {tree(-56, 100, 0.7)}
  {sun(60, -70, 22)}
</g>
{sit(160, 380, 1.15, 1, 'violet', 'blue', 'bun', 'neutral', 'lap')}
{chair(160, 380, 1.05, 'gold', 1)}
<g transform="translate(160 250)">
  <path d="M-24-6q14-10 24 0M0-6q14-10 24 0" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round" transform="translate(-4 0)"/>
</g>
<g fill="{MUTED}" opacity="0.7">
''' + ''.join(f'<circle cx="{230+i*30}" cy="{190-i*30}" r="{7+i*4}"/>' for i in range(3)) + f'''
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M320 110q40-30 80-20"/></g>''', ground=False)

add('continental', '海に囲まれた島ではなく、地続きの大きな陸', f'''
{split()}
<path d="M0 0h600v400H0z" fill="#7aa8c4"/>
<g transform="translate(150 220)">
  <path d="M-60 40q-30-50 10-80 50-34 90 0 30 30 0 80-50 24-100 0z" fill="#c9d8c0" class="o"/>
</g>
<g fill="none" stroke="#a8c8dd" stroke-width="4"><path d="M40 320h220M60 360h180"/></g>
<g transform="translate(460 220)">
  <path d="M-160 160q-60-140 30-200 120-80 220 0 70 60 30 180-120 60-280 20z" fill="#c9d8c0" class="o"/>
  <g fill="none" stroke="#a8bfa0" stroke-width="4"><path d="M-100-60q80 40 180 0M-120 40q120 50 240 0"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M330 90h230"/></g>
<g class="a" marker-end="url(#ar)"><path d="M560 90H330"/></g>''', ground=False)

add('contradictory', '同じ件について正反対の二つの報告がある', f'''
{split()}
{table(380)}
<g transform="translate(150 240)">
  {doc(0, 0, 170, 200, 4)}
  {tick(0, 66, 0.5)}
</g>
<g transform="translate(450 240)">
  {doc(0, 0, 170, 200, 4)}
  {cross(0, 66, 0.5)}
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M270 130l60 40M330 130l-60 40"/>
</g>''', ground=False)

add('counterproductive', '急ごうとして手を出し、かえって遅くなる', f'''
{split()}
{table(380)}
<g transform="translate(150 260)">
  <g class="teal o">
''' + ''.join(f'<rect x="{-60+ (i%3)*44}" y="{-30-(i//3)*44}" width="34" height="34"/>' for i in range(6)) + f'''
  </g>
</g>
{tick(150, 130, 0.6)}
<g transform="translate(450 300)">
  <g class="teal o">
''' + ''.join(f'<rect x="{-70+ (i%4)*40}" y="{-20+(i//4)*0}" width="34" height="34" transform="rotate({-30+i*18} {-53+(i%4)*40} 0)"/>' for i in range(6)) + f'''
  </g>
</g>
{hand(450, 170, 1)}
{cross(450, 130, 0.6)}
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', ground=False)

add('courteous', 'ドアを押さえて相手を先に通す', f'''
{table(380)}
<g transform="translate(400 200)">
  <path d="M-110-160h220v320h-220z" fill="{BRN}" class="o"/>
  <path d="M-86-136h172v272h-172z" fill="#4a4436"/>
  <path d="M-86-136h172v272h-172z" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>
{person(230, 380, 1.05, 1, 'teal', 'blue', 'reach', 'short', 'smile')}
{person(430, 380, 0.95, 1, 'coral', 'blue', 'walk', 'bun', 'smile', 'walk')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M470 300h80"/></g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M150 220l-24-18M170 280h-26"/>
</g>''', ground=False)

add('cramped', '広い部屋と、机で身動きの取れない狭い部屋', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-110-120h220v240h-220z" fill="#f0eee6" class="o"/>
  <path d="M-60 60h120v40h-120z" fill="#c9a464" class="o"/>
</g>
{sit(150, 340, 0.75, 1, 'teal', 'blue', 'bun', 'smile', 'lap')}
<g transform="translate(450 250)">
  <path d="M-110-120h220v240h-220z" fill="#f0eee6" class="o"/>
  <path d="M-110-60h90v40h-90zM20-60h90v40H20zM-110 20h90v40h-90zM20 20h90v40H20z" fill="#c9a464" class="o"/>
</g>
{sit(450, 300, 0.6, 1, 'coral', 'blue', 'bob', 'sad', 'lap')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M390 190h40M510 190h-40"/></g>''', ground=False)

add('cryptic', '何を指すのか分からない謎めいた記号の走り書き', f'''
{table(380)}
<g transform="translate(280 210) rotate(-4)">
  <path d="M-160-130h320v260h-320z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round">
    <path d="M-110-80q30-30 50 0t40-20M20-90l40 40-40 20M90-80v50M-110-10h50l-20 40M0 0q30 30 0 50t50 0M100-10l-30 50h50"/>
  </g>
</g>
{person(500, 380, 0.85, -1, 'teal', 'blue', 'up', 'bun', 'neutral')}
<g transform="translate(520 190)">
  <path d="M-18-30q0-24 18-24t18 24-18 20v12" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="26" r="5.5" fill="{INK}"/>
</g>''', ground=False)

add('cumbersome', '長すぎる棒が引っかかって扱いにくい', f'''
{table(380)}
{person(200, 380, 1.05, 1, 'coral', 'blue', 'up', 'cap', 'sad')}
<g transform="translate(340 220) rotate(-8)">
  <path d="M-220-14h440v28h-440z" fill="#c9a464" class="o"/>
</g>
<g transform="translate(560 200)">
  <path d="M-30-140h60v300h-60z" fill="{BRN}" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M500 160l24-24M520 220h26"/>
</g>
<g transform="translate(60 200)">
  <path d="M-30-140h60v300h-60z" fill="{BRN}" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M130 170l-24-24M120 230h-26"/>
</g>''', ground=False)

add('cumulative', '毎日少しずつ足した分が積み上がる', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(300 300)">
  <path d="M-250 60h500v6h-500z" fill="{INK}"/>
  <path d="M-250-240v300h6v-300z" fill="{INK}"/>
  <g class="teal o">
''' + ''.join(f'<rect x="{-220+i*60}" y="{-i*36}" width="46" height="{60+i*36}"/>' for i in range(7)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M100 130L480 60"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M50 360h500"/></g>''', ground=False)

# --- 連語 -------------------------------------------------------------------
add('by-and-large', '細かい例外はあるが、全体としてはうまくいっている', f'''
{table(380)}
<g class="o">
''' + ''.join(f'<circle cx="{80+ (i%7)*76}" cy="{200+(i//7)*80}" r="26" class="greenp"/>' for i in range(13)) + f'''
  <circle cx="384" cy="280" r="26" class="coralp"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
''' + ''.join(f'<path d="M{68+ (i%7)*76} {200+(i//7)*80}l8 10 16-20"/>' for i in [0,1,2,3,4,5,6,7,8,10,11,12]) + f'''
</g>
{cross(384, 280, 0.4)}
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M80 130h440"/></g>''', ground=False)

add('by-means-of', 'はしごという手段を使って上に届く', f'''
{table(380)}
<g transform="translate(430 240)">
  <path d="M-120-140h240v300h-240z" fill="#c8b8a0" class="o"/>
  <path d="M-60-100h60v50h-60z" class="bluep o"/>
</g>
<g transform="translate(300 260) rotate(-16)">
  <path d="M-14-140h14v280h-14zM50-140h14v280H50z" fill="#c9a464" class="o"/>
  <g fill="#a0764a">
''' + ''.join(f'<rect x="0" y="{-120+i*48}" width="50" height="14"/>' for i in range(6)) + f'''
  </g>
</g>
{person(150, 380, 0.95, 1, 'coral', 'blue', 'up', 'cap', 'smile')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M120 250V130"/></g>''', ground=False)

add('curious-about', '箱の中が気になってのぞき込む', f'''
{table(380)}
<g transform="translate(380 320)">
  <path d="M-90-50h180v90h-180z" class="gold o"/>
  <path d="M-90-50l20-24h180l-20 24z" fill="{TONES['gold'][1]}" class="o"/>
  <path d="M-70-74l-30-30M110-74l30-30" fill="none" stroke="{TONES['gold'][2]}" stroke-width="8"/>
</g>
{person(180, 380, 1.05, 1, 'teal', 'blue', 'reach', 'bun', 'surprised')}
<g transform="translate(240 250)">
  <ellipse cx="-6" rx="14" ry="12" fill="#fffefd" class="o"/><circle cx="0" r="6" fill="{INK}"/>
  <ellipse cx="26" rx="14" ry="12" fill="#fffefd" class="o"/><circle cx="32" r="6" fill="{INK}"/>
</g>
<g transform="translate(160 160)">
  <path d="M-18-30q0-24 18-24t18 24-18 20v12" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="26" r="5.5" fill="{INK}"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M290 250l60 20"/></g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
