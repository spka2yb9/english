# -*- coding: utf-8 -*-
"""第143回。i-/j-/l-/m- の形容詞と身のまわりの名詞。"""
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
add('jumper', '頭からかぶって着る毛糸のセーター', f'''
{table(340)}
<g transform="translate(300 220)">
  <path d="M-90-60q90-34 180 0l-16 130h-148z" class="coralp o"/>
  <path d="M-90-60l-56 56 30 30 40-44M90-60l56 56-30 30-40-44" class="coralp o"/>
  <path d="M-34-70q34-16 68 0-34 20-68 0z" class="corald o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3">
''' + ''.join(f'<path d="M-84 {-20+i*24}q84 24 168 0"/>' for i in range(4)) + f'''
  </g>
  <path d="M-88 66h176v18h-176z" class="corald o"/>
</g>''', ground=False)

add('lamb', '毛のふわふわした子羊', f'''
<path d="M0 0h600v260H0z" fill="#dceaf4"/>
<path d="M0 260h600v140H0z" fill="#c9d8c0"/>
<path d="M0 260h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 290)">
  <g fill="#fffdf6" class="o">
''' + ''.join(f'<circle cx="{-60+ (i%5)*32}" cy="{-40+(i//5)*30}" r="30"/>' for i in range(10)) + f'''
  </g>
  <ellipse cx="86" cy="-56" rx="30" ry="26" fill="#e8e2d6" class="o"/>
  <path d="M62-76q-20-16-8-26 14-2 18 20zM110-78q18-16 28-8 2 12-16 20z" fill="#e8e2d6" class="o"/>
  <circle cx="94" cy="-60" r="4" fill="{INK}"/>
  <g stroke="{MUTED}" stroke-width="10" stroke-linecap="round" fill="none">
    <path d="M-40 6v22M0 8v20M40 6v22"/>
  </g>
</g>''', ground=False)

add('lily', '大きく反り返った花びらの白い花', f'''
<path d="M0 0h600v300H0z" fill="#dceaf4"/>
<path d="M0 300h600v100H0z" fill="#c9d8c0"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 300)">
  <path d="M-8 0v-160h16V0z" class="greend o"/>
  <path d="M-8-70q-60-24-54-60 54 6 54 60zM8-110q60-26 70 4-52 28-70-4z" class="greenp o"/>
  <g transform="translate(0 -200)">
    <g fill="#fffdf6" class="o">
''' + ''.join(f'<path d="M0 10q-26-70 0-96 26 26 0 96z" transform="rotate({i*60})"/>' for i in range(6)) + f'''
    </g>
    <g stroke="{TONES['gold'][2]}" stroke-width="4" stroke-linecap="round" fill="none">
      <path d="M0 6v-34M0 6l-22-26M0 6l22-26"/>
    </g>
    <g fill="{TONES['gold'][0]}"><circle cy="-34" r="6"/><circle cx="-24" cy="-24" r="6"/><circle cx="24" cy="-24" r="6"/></g>
  </g>
</g>''', ground=False)

add('mammal', '毛があり、乳で子を育てる動物', f'''
<path d="M0 0h600v260H0z" fill="#dceaf4"/>
<path d="M0 260h600v140H0z" fill="#c9d8c0"/>
<path d="M0 260h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(240 300)">
  <ellipse cy="-40" rx="90" ry="52" fill="#c8a070" class="o"/>
  <circle cx="76" cy="-84" r="34" fill="#c8a070" class="o"/>
  <path d="M56-108q-10-40 6-40 14 6 10 40zM94-108q10-38 26-30 6 12-10 32z" fill="#a8804c" class="o"/>
  <circle cx="86" cy="-88" r="4" fill="{INK}"/>
  <path d="M-90-44q-46-24-58 8 40 26 60 8z" fill="#a8804c" class="o"/>
  <g stroke="#a8804c" stroke-width="12" stroke-linecap="round" fill="none"><path d="M-40 8v22M20 8v22"/></g>
</g>
<g transform="translate(400 320) scale(0.55)">
  <ellipse cy="-40" rx="90" ry="52" fill="#c8a070" class="o"/>
  <circle cx="76" cy="-84" r="34" fill="#c8a070" class="o"/>
  <circle cx="86" cy="-88" r="4" fill="{INK}"/>
  <g stroke="#a8804c" stroke-width="12" stroke-linecap="round" fill="none"><path d="M-40 8v22M20 8v22"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M340 280h40"/></g>
<g transform="translate(500 180)">
  <path d="M-30-20h60v40h-60z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-30-6h60"/></g>
</g>''', ground=False)

add('mango', '皮が赤黄色で、中が濃い黄色の果物', f'''
{table(330)}
<g transform="translate(200 250)">
  <path d="M0-80q70 20 76 76t-76 56q-82 0-76-56T0-80z" fill="#e8983a" class="o"/>
  <path d="M-40-56q40-30 80 0-40 20-80 0z" class="coral o"/>
  <path d="M0-80v-16" stroke="{TONES['green'][2]}" stroke-width="6" fill="none"/>
</g>
<g transform="translate(430 260)">
  <path d="M-70 0q0-70 70-70t70 70-70 60-70-60z" fill="#e8983a" class="o"/>
  <path d="M-56 0q0-56 56-56t56 56-56 48-56-48z" fill="#f0c04a" class="o"/>
  <ellipse ry="34" rx="20" fill="#e8d8a8" class="o"/>
</g>''', ground=False)

add('mayonnaise', 'チューブから白いソースをしぼり出す', f'''
{table(330)}
<g transform="translate(220 220) rotate(150)">
  <path d="M-40-70h80v130q0 16-40 16t-40-16z" fill="#fffdf6" class="o"/>
  <path d="M-40-70q0-30 40-30t40 30z" fill="#fffdf6" class="o"/>
  <path d="M-14-100v-24h28v24z" class="blued o"/>
  <path d="M-30-30h60v60h-60z" class="bluep o"/>
</g>
<path d="M300 230q30 26 34 56" fill="none" stroke="#f6f0dc" stroke-width="14" stroke-linecap="round"/>
<path d="M300 230q30 26 34 56" fill="none" stroke="#ded8c0" stroke-width="2.5"/>
<g transform="translate(400 300)">
  <ellipse rx="110" ry="28" fill="#fffdf6" class="o"/>
  <path d="M-110 0q0 34 110 34t110-34z" fill="#fffdf6" class="o"/>
  <g class="green o"><ellipse cx="-40" cy="-10" rx="34" ry="16"/><ellipse cx="30" cy="-6" rx="30" ry="14"/></g>
  <path d="M-50-14q60-16 110 6" fill="none" stroke="#f6f0dc" stroke-width="9" stroke-linecap="round"/>
</g>''', ground=False)

add('microscope', 'のぞいて小さなものを大きく見る器械', f'''
{table(380)}
<g transform="translate(300 250)">
  <path d="M-90 120h180v20h-180z" fill="#5a6270" class="o"/>
  <path d="M-16 120V0h32v120z" fill="#8f9aa6" class="o"/>
  <path d="M-16 0q-54-40-54-104t72-92v50q-34 12-34 44t34 46z" fill="#8f9aa6" class="o"/>
  <path d="M-16-146h72v40h-72z" fill="#5a6270" class="o"/>
  <path d="M40-106h26v46H40z" fill="#c8d0d8" class="o"/>
  <path d="M-90 60h180v18h-180z" fill="#c8d0d8" class="o"/>
  <circle cx="14" cy="66" r="12" fill="{TONES['coral'][1]}" class="o"/>
  <circle cx="-56" cy="10" r="18" fill="#c8d0d8" class="o"/>
</g>''', ground=False)

add('midday', '太陽が真上に来る、真昼の時刻', f'''
<path d="M0 0h600v300H0z" fill="#dceaf4"/>
<path d="M0 300h600v100H0z" fill="#c9d8c0"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
{sun(300, 80, 48)}
{tree(140, 300, 1.0)}
{person(300, 300, 0.85, 1, 'coral', 'blue', 'stand', 'cap', 'smile')}
<g fill="{INK}" opacity="0.18"><ellipse cx="300" cy="306" rx="34" ry="10"/></g>
<g transform="translate(480 190)">
  <circle r="60" fill="#fffdf6" class="o"/>
  <g fill="{INK}">
''' + ''.join(f'<rect x="-4" y="-50" width="8" height="14" rx="4" transform="rotate({i*30})"/>' for i in range(12)) + f'''
  </g>
  <path d="M0 0v-40" stroke="{INK}" stroke-width="7" stroke-linecap="round" fill="none"/>
  <path d="M0 0v-46" stroke="{INK}" stroke-width="4" stroke-linecap="round" fill="none"/>
  <circle r="6" fill="{INK}"/>
</g>''', ground=False)

add('mint', 'すっとする香りの緑の葉', f'''
{table(340)}
<g transform="translate(280 250)">
  <path d="M-6 60v-90h12v90z" class="greend o"/>
  <g class="green o">
    <path d="M-6-30q-56-24-50-64 52 4 50 64zM6-56q56-24 66 8-52 26-66-8z"/>
    <path d="M-6-70q-46-24-38-58 44 6 38 58zM6-96q46-22 56 8-44 24-56-8z"/>
  </g>
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="3">
    <path d="M-30-56q-14-14-18-26M32-40q16-12 22-24"/>
  </g>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-linecap="round" opacity="0.9">
  <path d="M420 200q26-40 0-70t26-56M470 220q26-44 0-76t26-56"/>
</g>
<g fill="{TONES['blue'][0]}">
  <path d="M130 210v-30M116 192h28M122 184l16 16M138 184l-16 16"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M130 210v-30M116 192h28M122 184l16 16M138 184l-16 16"/>
</g>''', ground=False)

add('manual', '機械の使い方を手順ごとに説明した冊子', f'''
{table(380)}
<g transform="translate(300 210) rotate(-3)">
  <path d="M-150-140h300v280h-300z" fill="#fffdf6" class="o"/>
  <path d="M-150-140h40v280h-40z" class="teal o"/>
  <g>
''' + ''.join(f'''<g transform="translate(0 {-94+i*54})">
  <circle cx="-80" r="16" class="tealp o"/>
  <rect x="-54" y="-8" width="{170-(i%3)*30}" height="16" rx="8" fill="{MUTED}"/>
</g>''' for i in range(4)) + f'''
  </g>
  <g transform="translate(90 92)">
    <path d="M-30-24h60v48h-60z" fill="#c8d0d8" class="o"/>
    <circle r="12" fill="#8f9aa6"/>
  </g>
</g>''', ground=False)

# --- 形容詞 ------------------------------------------------------------------
add('idiomatic', '文法は正しいが、こなれた言い方は別にある', f'''
{split()}
{table(380)}
<g transform="translate(150 220)">
  <path d="M-110-40h220v80h-220z" fill="#fffefd" class="o"/>
  {word(0, 0, 5, 36, MUTED)}
</g>
{tick(150, 130, 0.5)}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M150 300v40"/></g>
<g transform="translate(450 220)">
  <path d="M-110-40h220v80h-220z" fill="#fffefd" class="o"/>
  {word(0, 0, 4, 40, TONES['teal'][0])}
</g>
<circle cx="450" cy="220" r="130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('interdependent', '互いに支え合って初めて立っていられる', f'''
{table(380)}
<g transform="translate(300 380)">
  <path d="M-160-20L-30-240h20L-140 0z" fill="#c9a464" class="o"/>
  <path d="M160-20L30-240H10L140 0z" fill="#c9a464" class="o"/>
  <path d="M-40-160h80v18h-80z" fill="#a0764a" class="o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M200 160l70 40"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M400 160l-70 40"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M40 380h520"/></g>''', ground=False)

add('intrinsic', '飾りを取り去っても残る、そのもの本来の価値', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-70 0l24-50h92l24 50-70 66z" class="tealp o"/>
  <g class="gold o"><circle cx="-70" cy="-70" r="16"/><circle cx="70" cy="-70" r="16"/><circle cy="-96" r="16"/></g>
  <path d="M-70-70q70-44 140 0" fill="none" stroke="{TONES['gold'][0]}" stroke-width="4"/>
</g>
<g transform="translate(450 250)">
  <path d="M-70 0l24-50h92l24 50-70 66z" class="tealp o"/>
</g>
<circle cx="450" cy="250" r="120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('inventive', '次々に新しい形を思いつく', f'''
{table(380)}
{person(120, 380, 1.0, 1, 'teal', 'blue', 'reach', 'bun', 'smile')}
<g>
''' + ''.join(f'''<g transform="translate({280+ (i%3)*110} {200+(i//3)*120})">
  <path d="M-46-40h92v80h-92z" class="paper"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4">
''' + ''.join([f'<path d="M-28 {-16+j*18}h56"/>' for j in range(2)]) + f'''</g>
  <circle cx="24" cy="-24" r="10" class="goldp o"/>
</g>''' for i in range(6)) + f'''
</g>
<g transform="translate(150 190)">
  <path d="M-34-28h68q10 0 10 10v28q0 10-10 10h-44l-16 14v-14q-18 0-18-10v-28q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M0-16q18 0 18 16t-10 16v6h-16v-6q-10 0-10-16t18-16z" class="gold"/>
</g>''', ground=False)

add('investigative', '手がかりを一つずつ調べて真相を追う', f'''
{table(380)}
<g transform="translate(300 210)">
  <path d="M-200-150h400v300h-400z" fill="#e8e2d6" class="o"/>
  <g>
''' + ''.join(f'<g transform="translate({-130+ (i%3)*130} {-90+(i//3)*90}) rotate({-14+i*9})">{doc(0, 0, 90, 100, 2)}</g>' for i in range(6)) + f'''
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4">
    <path d="M-130-90l130 0M0-90l130 90M-130 0l130 0"/>
  </g>
  <g fill="{TONES['coral'][0]}"><circle cx="-130" cy="-90" r="7"/><circle cx="0" cy="-90" r="7"/><circle cx="130" cy="0" r="7"/><circle cx="-130" cy="0" r="7"/></g>
</g>
<g transform="translate(470 300)">
  <circle r="46" fill="none" stroke="#8f9aa6" stroke-width="10"/>
  <path d="M32 32l34 34" stroke="{INK}" stroke-width="12" stroke-linecap="round" fill="none"/>
</g>''', ground=False)

add('irreplaceable', '同じものが二つとない、代えのきかない品', f'''
{split()}
{table(380)}
<g transform="translate(150 260)">
  <path d="M-50-50h100v100h-100z" class="tealp o"/>
</g>
<g transform="translate(150 140)">
  <path d="M-40-24h80v48h-80z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}"><path d="M210 190l-40 40"/></g>
<g transform="translate(450 260)">
  <path d="M-56-56q56-30 112 0 14 70-16 92-40 18-80 0-30-22-16-92z" class="corald o"/>
  <path d="M-30-40q30-16 60 0" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"/>
</g>
<g transform="translate(450 140)">
  <path d="M-40-24h80v48h-80z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 6"/>
  {cross(0, 0, 0.34)}
</g>
<circle cx="450" cy="260" r="110" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('irresistible', 'どうしても手が伸びてしまう、抗しがたい菓子', f'''
{table(340)}
<g transform="translate(400 270)">
  <ellipse rx="90" ry="24" fill="#fffdf6" class="o"/>
  <path d="M-90 0q0 30 90 30t90-30z" fill="#fffdf6" class="o"/>
  <g class="o">
    <circle cx="-40" cy="-14" r="24" fill="#c8934a"/><circle cx="4" cy="-20" r="22" fill="#c8934a"/><circle cx="44" cy="-12" r="20" fill="#c8934a"/>
  </g>
  <g fill="#6b4c28"><circle cx="-46" cy="-22" r="5"/><circle cx="10" cy="-28" r="5"/><circle cx="40" cy="-18" r="4"/></g>
</g>
{person(160, 340, 1.1, 1, 'coral', 'blue', 'reach', 'bun', 'smile')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M230 200h80"/></g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M480 170l24-22M500 230h26"/>
</g>''', ground=False)

add('irreversible', '割れたガラスはもう元に戻せない', f'''
{split()}
{table(380)}
<g transform="translate(150 260)">
  <path d="M-60-70h120v140h-120z" fill="#e8f0f6" class="o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"><path d="M-40-40h80M-40 30h80"/></g>
</g>
<g transform="translate(450 260)">
  <g fill="#e8f0f6" class="o">
    <path d="M-60-70h50l14 70-40 20z"/><path d="M-10-70h70v50l-50 20z"/>
    <path d="M-60 20l40-20 20 40-30 30z"/><path d="M10 0l50-20v90h-40z"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M270 200h60"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round">
  <path d="M330 330q-40 30-80 0"/>
</g>
{cross(300, 366, 0.5)}''', ground=False)

add('irritated', '小さなことが積もっていらいらする', f'''
{table(380)}
{sit(300, 380, 1.2, 1, 'coral', 'blue', 'short', 'sad', 'lap')}
{chair(300, 380, 1.1, 'gold', 1)}
<g transform="translate(300 250)">
  <path d="M-26-14q14-10 24 0M2-14q14-10 24 0" fill="none" stroke="{HAIR}" stroke-width="5" stroke-linecap="round" transform="translate(-2 0)"/>
  <path d="M-12 16h24" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M180 200l-26-22M420 196l26-22M170 270l-30-6M430 266l30-6"/>
</g>
<g transform="translate(120 300)">
  <circle r="34" fill="#fffdf6" class="o"/>
  <path d="M-24-24l-14-14M24-24l14-14" stroke="{INK}" stroke-width="6" stroke-linecap="round" fill="none"/>
  <circle cx="-24" cy="-30" r="9" class="coral o"/><circle cx="24" cy="-30" r="9" class="coral o"/>
</g>''', ground=False)

add('juicy', 'かじると果汁があふれ出る果物', f'''
{table(340)}
<g transform="translate(300 250)">
  <circle r="86" class="coral o"/>
  <path d="M50-64q40 6 46 40-46 12-64-16z" fill="#fffaf1"/>
  <path d="M52-62q34 6 40 34-40 10-56-12z" fill="#f6d0c0" class="o"/>
  <path d="M0-86q-14-28 8-34 18 6 6 34z" class="greend o"/>
</g>
<g fill="{TONES['coral'][1]}" stroke="{TONES['coral'][2]}" stroke-width="2">
''' + ''.join(f'<path d="M{380+i*30} {200+ (i%3)*30}q10 12 10 20t-10 8-10-8 10-20z"/>' for i in range(4)) + f'''
</g>
<g fill="{TONES['coral'][1]}"><ellipse cx="420" cy="326" rx="70" ry="12"/></g>''', ground=False)

add('justifiable', '身を守るためだった、と認められる行い', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-10 0h20v150h-20z" fill="#8f9aa6" class="o"/>
  <path d="M-60 150h120v20h-120z" fill="#8f9aa6" class="o"/>
  <path d="M-160-8h320v16h-320z" fill="#b8bfc8" class="o"/>
  <circle r="14" fill="#8f9aa6" class="o"/>
  <g class="tealp o"><path d="M-190 8q0 26 30 26t30-26z"/><ellipse cx="-160" ry="9" rx="30"/></g>
  <g class="tealp o"><path d="M130 8q0 26 30 26t30-26z"/><ellipse cx="160" ry="9" rx="30"/></g>
</g>
<g transform="translate(300 330)">
  {doc(0, 0, 130, 80, 2)}
  {tick(40, 20, 0.3)}
</g>
{tick(500, 150, 0.6)}''', ground=False)

add('knowledgeable', 'どんな質問にもすぐ答えが返ってくる', f'''
{table(380)}
{person(450, 380, 1.1, -1, 'violet', 'blue', 'up', 'bun', 'smile')}
{person(150, 380, 1.05, 1, 'coral', 'blue', 'up', 'short', 'neutral')}
<g transform="translate(230 160)">
  <path d="M-40-30h80q10 0 10 10v30q0 10-10 10h-52l-18 14v-14q-10 0-10-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M-18-18q0-16 18-16t18 16-18 14v8" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle cy="16" r="4.5" fill="{INK}"/>
</g>
<g transform="translate(390 250)">
  <path d="M40-34H-40q-12 0-12 12v34q0 12 12 12h56l20 16v-16q12 0 12-12v-34q0-12-12-12z" fill="#fffefd" class="o"/>
  {tick(0, -4, 0.34)}
</g>
<g>
''' + ''.join(f'<g transform="translate({530+ (i%2)*4} {350-i*22})"><path d="M-56-10h112v20h-112z" class="{["teal","coral","gold","violet"][i%4]} o"/></g>' for i in range(4)) + f'''
</g>''', ground=False)

add('laid-back', 'あくせくせず、のんびり構えている', f'''
{split()}
{table(380)}
{person(150, 380, 1.05, 1, 'blue', 'blue', 'up', 'short', 'sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M100 220l-24-18M200 216l24-18"/>
</g>
<g transform="translate(450 380)">
  <path d="M-90-30h180v30h-180z" class="gold o"/>
  <path d="M-90-30q0-46 90-46t90 46z" class="goldp o"/>
  <path d="M-30-6l-40 20M30-6l40 20" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-30-116q30-16 60 0l-8 86h-44z" class="coral o"/>
  <path d="M-28-106l-48 26M28-106l48 26" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cy="-146" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['cap']}" transform="translate(0 -38) scale(1.08)" fill="{TONES['blue'][0]}"/>
  <path d="M-16-148q10-8 18 0M-2-148q10-8 18 0" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <path d="M-10-132q10 10 20 0" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<circle cx="450" cy="290" r="130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('lasting', '年月がたっても変わらず残る', f'''
{table(380)}
<g>
''' + ''.join(f'''<g transform="translate({120+i*120} 260)">
  <path d="M-50 0v-70h100V0z" fill="#c8b8a0" class="o"/>
  <path d="M-60-70L0-110l60 40z" class="coral o"/>
  <path d="M-16-40h32V0h-32z" fill="#8b6437" class="o"/>
</g>''' for i in range(4)) + f'''
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M40 320h520"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M60 150h480"/></g>''', ground=False)

add('laughable', 'あまりにお粗末で、笑うしかない出来', f'''
{table(380)}
<g transform="translate(240 240)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="8" stroke-linecap="round">
    <path d="M-60-40q40 60 20-10t50 80M-40 50q60-40 100 20"/>
  </g>
  <circle cx="30" cy="-50" r="14" class="coralp"/>
</g>
{person(490, 380, 0.95, -1, 'teal', 'blue', 'up', 'bun', 'smile')}
<g transform="translate(490 250)">
  <path d="M-16 10q16 16 32 0z" fill="{INK}" class="o"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M400 200q16-16 32 0M400 250q16-16 32 0"/>
</g>''', ground=False)

add('lavish', '金に糸目をつけず、豪勢にふるまう', f'''
{table(380)}
<g transform="translate(300 300)">
  <path d="M-250-20h500v30h-500z" fill="#c9a464" class="o"/>
  <path d="M-250-30h500v10h-500z" class="corald o"/>
</g>
<g>
''' + ''.join(f'''<g transform="translate({100+i*90} 250)">
  <ellipse rx="42" ry="12" fill="#fffdf6" class="o"/>
  <path d="M-42 0q0 18 42 18t42-18z" fill="#fffdf6" class="o"/>
  <path d="M-24-12q24-16 48 0-24 14-48 0z" fill="{[TONES['coral'][0], TONES['gold'][0], TONES['green'][0], TONES['violet'][0], TONES['teal'][0], TONES['coral'][0]][i]}" class="o"/>
</g>''' for i in range(6)) + f'''
</g>
<g transform="translate(300 130)">
  <path d="M-70-30h140v14h-140z" class="gold o"/>
  <path d="M-70-30l-10-52 28 22 22-36 22 36 28-22-10 52z" class="gold o"/>
</g>
{coin(120, 350, 18)}
{coin(490, 350, 18)}''', ground=False)

add('lenient', '厳しく罰する側と、軽く済ませる側', f'''
{split()}
{table(380)}
{person(90, 380, 0.95, 1, 'violet', 'blue', 'point', 'short', 'sad')}
{person(220, 380, 0.9, -1, 'coral', 'blue', 'up', 'bob', 'sad')}
<g transform="translate(150 190)">
  <path d="M-50-30h100v60h-100z" fill="#fffefd" class="o"/>
  <g class="coral o"><rect x="-34" y="-14" width="68" height="28" rx="6"/></g>
</g>
{person(390, 380, 0.95, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{person(520, 380, 0.9, -1, 'coral', 'blue', 'stand', 'bob', 'smile')}
<g transform="translate(450 190)">
  <path d="M-50-30h100v60h-100z" fill="#fffefd" class="o"/>
  {tick(0, 0, 0.34)}
</g>
<circle cx="450" cy="280" r="130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('linguistic', 'ことばそのものを、音と形と意味に分けて調べる', f'''
{table(380)}
<g transform="translate(300 210)">
  <path d="M-200-150h400v300h-400z" class="paper"/>
  <g transform="translate(0 -100)">
    {word(0, 0, 6, 44, INK)}
  </g>
  <g class="a" marker-end="url(#ar)" stroke="{MUTED}" stroke-width="4">
    <path d="M-100-70l-40 50M0-70v50M100-70l40 50"/>
  </g>
  <g class="o">
    <rect x="-180" y="-14" width="90" height="50" class="tealp"/>
    <rect x="-46" y="-14" width="90" height="50" class="coralp"/>
    <rect x="90" y="-14" width="90" height="50" class="goldp"/>
  </g>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="{-166+i*136}" y="6" width="62" height="10" rx="5"/>' for i in range(3)) + f'''
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-160 90h320"/></g>
</g>''', arrow=True, ground=False)

add('literal', '「山」を比喩ではなく、本当の山として取る', f'''
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
<circle cx="150" cy="270" r="130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('lucid', 'こみ入った話が、澄んだ形で分かりやすくなる', f'''
{split()}
{table(380)}
<g transform="translate(150 240)">
  <path d="M-90 40q40-90 90-30t-60 20 90-70 40 80-100-40 60 40" fill="none" stroke="{MUTED}" stroke-width="7"/>
</g>
<g transform="translate(450 240)">
  <g fill="{INK}">
''' + ''.join(f'<rect x="-90" y="{-60+i*32}" width="{180-(i%3)*40}" height="16" rx="8"/>' for i in range(4)) + f'''
  </g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="4"><path d="M-110-70v150"/></g>
</g>
<circle cx="450" cy="240" r="130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g class="a" marker-end="url(#ar)"><path d="M270 240h60"/></g>''', arrow=True, ground=False)

add('ludicrous', '船に車輪をつけて坂を下ろうとする、ばかげた案', f'''
{table(380)}
<g transform="translate(300 260)">
  <path d="M-140 0h280l-34 60q-6 12-106 12T-110 60z" class="blue o"/>
  <path d="M-100-60h200v60h-200z" fill="#fffdf6" class="o"/>
  <path d="M60-110h16v50H60z" class="coral o"/>
  <circle cx="-90" cy="86" r="26" fill="{INK}"/><circle cx="90" cy="86" r="26" fill="{INK}"/>
</g>
{person(120, 380, 0.85, 1, 'teal', 'blue', 'up', 'bun', 'smile')}
<g transform="translate(500 160)">
  <path d="M-40-30h80q10 0 10 10v30q0 10-10 10h-52l-18 14v-14q-10 0-10-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M-16 4q16 16 32 0z" fill="{INK}" class="o"/>
</g>
{cross(120, 160, 0.6)}''', ground=False)

add('lukewarm', '熱くも冷たくもない、ぬるい湯', f'''
{table(340)}
<g transform="translate(160 260)">
  <path d="M-44-50h88l-10 84q-2 12-34 12t-34-12z" fill="#e8f0f6" class="o"/>
  <path d="M-38-20h76l-6 52q-2 10-32 10t-32-10z" fill="{TONES['coral'][0]}"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" opacity="0.8"><path d="M-16-64q10-18 0-32M14-68q10-20 0-36"/></g>
</g>
<g transform="translate(300 260)">
  <path d="M-44-50h88l-10 84q-2 12-34 12t-34-12z" fill="#e8f0f6" class="o"/>
  <path d="M-38-20h76l-6 52q-2 10-32 10t-32-10z" fill="#d8b0a0"/>
</g>
<g transform="translate(440 260)">
  <path d="M-44-50h88l-10 84q-2 12-34 12t-34-12z" fill="#e8f0f6" class="o"/>
  <path d="M-38-20h76l-6 52q-2 10-32 10t-32-10z" fill="{TONES['blue'][0]}"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
    <path d="M-10-72v-24M-22-84h24M-16-90l12 12M-4-90l-12 12"/>
  </g>
</g>
<circle cx="300" cy="270" r="86" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('luxurious', '広くて豪華な部屋に高価な調度が並ぶ', f'''
<path d="M0 0h600v400H0z" fill="#f6ecd4"/>
<path d="M0 340h600v60H0z" fill="#a0764a" class="o"/>
<g transform="translate(300 100)">
  <path d="M0-40v30" stroke="{TONES['gold'][2]}" stroke-width="5" fill="none"/>
  <path d="M-70-10h140l-20 40h-100z" class="gold o"/>
  <g fill="{TONES['gold'][1]}"><circle cx="-40" cy="46" r="10"/><circle cx="0" cy="54" r="10"/><circle cx="40" cy="46" r="10"/></g>
</g>
<g transform="translate(300 300)">
  <path d="M-160-40h320v70h-320z" class="corald o"/>
  <path d="M-160-40q0-70 160-70t160 70z" class="coral o"/>
  <path d="M-190-50h50v80h-50zM140-50h50v80h-50z" class="corald o"/>
</g>
<g transform="translate(110 300)">
  <path d="M-40-20h80v40h-80z" class="gold o"/>
  <path d="M-30-70h60v50h-60z" class="goldp o"/>
</g>
<g transform="translate(500 300)">
  <path d="M-30-90h60v110h-60z" class="tealp o"/>
  <path d="M-30-90q30-24 60 0" fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"/>
</g>''', ground=False)

add('majestic', '見上げるほど堂々とした山なみ', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
<path d="M0 400l140-260 90 110 130-190 120 180 120-100v260z" fill="#8f9aa6" class="o"/>
<g fill="#fffefd" class="o">
  <path d="M140-0l0 0z"/>
  <path d="M140 140l-34 50h68zM360 60l-38 56h76zM480 130l-30 44h60z"/>
</g>
<path d="M0 380h600v20H0z" fill="#6f7b88"/>
{sun(70, 70, 30)}
{person(300, 380, 0.7, 1, 'coral', 'blue', 'up', 'cap', 'surprised')}
<g class="a" marker-end="url(#ar)"><path d="M300 330v-160"/></g>''', arrow=True, ground=False)

add('malicious', 'わざと相手を困らせるために足をかける', f'''
{table(380)}
{person(180, 380, 1.1, 1, 'violet', 'blue', 'stand', 'short', 'neutral')}
<g transform="translate(280 370)">
  <path d="M-40-8h100v16h-100z" fill="{TONES['blue'][2]}"/>
</g>
<g transform="translate(430 330) rotate(24)">
  <path d="M-12-8l-30 30M12-8l32 26" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-27-78q27-14 54 0l-8 72h-38z" class="coral o"/>
  <path d="M-22-70l-36-16M22-70l36-16" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cy="-108" r="25" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['bob']}" transform="translate(0 4)" fill="{HAIR}"/>
  <circle cx="-8" cy="-104" r="2.4" fill="{INK}"/><circle cx="8" cy="-104" r="2.4" fill="{INK}"/>
  <circle cy="-90" r="5" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
<g transform="translate(180 250)">
  <path d="M-16-10q10-8 16 0M0-10q10-8 16 0" fill="none" stroke="{HAIR}" stroke-width="4" stroke-linecap="round"/>
  <path d="M-10 14q10 8 20-2" fill="none" stroke="{INK}" stroke-width="3.5"/>
</g>
{cross(540, 160, 0.6)}''', ground=False)

add('manageable', '山ほどあった仕事が、片づけられる量になる', f'''
{split()}
{table(380)}
<g>
''' + ''.join(f'<g transform="translate({80+ (i%4)*54} {230+(i//4)*70}) rotate({-24+i*11})">{doc(0, 0, 56, 70, 2)}</g>' for i in range(8)) + f'''
</g>
{cross(150, 130, 0.6)}
<g>
''' + ''.join(f'<g transform="translate({420+i*60} 280)">{doc(0, 0, 56, 70, 2)}</g>' for i in range(2)) + f'''
</g>
{tick(450, 130, 0.6)}
<g class="a" marker-end="url(#ar)"><path d="M270 300h60"/></g>''', arrow=True, ground=False)

add('manipulative', '糸を引いて、相手を思いどおりに動かす', f'''
{table(380)}
{person(140, 380, 1.05, 1, 'violet', 'blue', 'up', 'cap', 'neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="3">
  <path d="M200 220l180 40M210 240l160 60M220 200l170 20"/>
</g>
<g transform="translate(430 340)">
  <path d="M-12-10l-24 26M12-10l26 24" fill="none" stroke="{TONES['blue'][2]}" stroke-width="11" stroke-linecap="round"/>
  <path d="M-25-78q25-13 50 0l-8 72h-34z" class="coral o"/>
  <path d="M-22-70l-30-14M22-70l30-14" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
  <circle cy="-106" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['bob']}" transform="translate(0 2)" fill="{HAIR}"/>
  <circle cx="-8" cy="-102" r="2.2" fill="{INK}"/><circle cx="8" cy="-102" r="2.2" fill="{INK}"/>
  <path d="M-7-90h14" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
{cross(540, 150, 0.6)}''', ground=False)

add('marvellous', '思わず息をのむ、すばらしい眺め', f'''
<path d="M0 0h600v260H0z" fill="#f6c48a"/>
<path d="M0 0h600v100H0z" fill="#dceaf4"/>
<path d="M0 260h600v140H0z" fill="#c9d8c0"/>
<path d="M0 260h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M0 260l120-120 90 70 100-100 120 110 170-80v120z" fill="#9aa5b0" class="o"/>
{sun(490, 80, 40)}
{person(160, 340, 1.0, 1, 'coral', 'blue', 'up', 'bun', 'smile')}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M240 220l24-22M100 220l-24-22M250 290h26"/>
</g>''', ground=False)

add('maternal', '母親が赤ん坊を抱いてあやす', f'''
{table(380)}
{sit(300, 380, 1.2, 1, 'coral', 'blue', 'bun', 'smile', 'lap')}
{chair(300, 380, 1.1, 'gold', 1)}
<g transform="translate(320 290)">
  <path d="M-50-16q50-30 96 0 6 30-26 36-52 8-70-12z" fill="#fffdf6" class="o"/>
  <circle cx="-56" cy="-24" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(-56 84) scale(0.9)" fill="{HAIR}"/>
  <circle cx="-64" cy="-22" r="2.4" fill="{INK}"/><circle cx="-48" cy="-22" r="2.4" fill="{INK}"/>
  <path d="M-64-10q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
<g fill="{TONES['coral'][0]}">
  <path d="M180 200q-14-20 0-28 14-6 18 10 4-16 18-10 14 8 0 28l-18 20z"/>
</g>''', ground=False)

add('meagre', '皿にごくわずかしか盛られていない', f'''
{split()}
{table(380)}
<g transform="translate(150 280)">
  <ellipse rx="100" ry="26" fill="#fffdf6" class="o"/>
  <path d="M-100 0q0 32 100 32t100-32z" fill="#fffdf6" class="o"/>
  <g class="o"><ellipse cx="0" cy="-10" rx="14" ry="8" class="gold"/></g>
</g>
<circle cx="150" cy="280" r="120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g transform="translate(450 280)">
  <ellipse rx="100" ry="26" fill="#fffdf6" class="o"/>
  <path d="M-100 0q0 32 100 32t100-32z" fill="#fffdf6" class="o"/>
  <g class="o">
    <path d="M-60-16q60-34 120-4 4 24-30 28-70 4-90-24z" class="gold"/>
    <circle cx="-30" cy="-34" r="16" class="green"/><circle cx="30" cy="-38" r="14" class="coral"/>
  </g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><circle cx="450" cy="280" r="120"/></g>''', ground=False)

add('medicinal', '飲むと具合がよくなる、薬効のある草', f'''
{table(340)}
<g transform="translate(200 250)">
  <path d="M-6 60v-100h12v100z" class="greend o"/>
  <g class="green o">
    <path d="M-6-40q-56-24-48-60 52 6 48 60zM6-70q56-24 66 8-52 26-66-8z"/>
    <path d="M-6-80q-46-22-38-54 44 6 38 54z"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 250h60"/></g>
<g transform="translate(440 250)">
  <path d="M-40-60h80v90q0 14-40 14t-40-14z" fill="#e8f0f6" class="o"/>
  <path d="M-18-60v-14h36v14z" class="green o"/>
  <path d="M-32-24h64v46q0 10-32 10t-32-10z" fill="{TONES['green'][1]}"/>
  <path d="M-10 0h20M0-10v20" stroke="{TONES['green'][0]}" stroke-width="5" fill="none"/>
</g>
{tick(500, 150, 0.6)}''', arrow=True, ground=False)

add('mediocre', '飛び抜けてもいないし悪くもない、平凡な出来', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(300 300)">
  <path d="M-250 60h500v6h-500z" fill="{INK}"/>
  <g class="tealp o">
    <rect x="-220" y="-140" width="60" height="200"/>
    <rect x="-140" y="-180" width="60" height="240"/>
    <rect x="-20" y="-80" width="60" height="140"/>
    <rect x="80" y="-160" width="60" height="220"/>
    <rect x="160" y="-190" width="60" height="250"/>
  </g>
  <rect x="-20" y="-80" width="60" height="140" class="coral o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M-244-80h490"/></g>
</g>
<circle cx="310" cy="290" r="80" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('merciful', '罰を下せる立場にありながら、許してやる', f'''
{table(380)}
{person(180, 380, 1.15, 1, 'violet', 'gold', 'give', 'bun', 'neutral')}
{person(440, 380, 1.0, -1, 'coral', 'blue', 'up', 'short', 'sad')}
<g transform="translate(300 170)">
  <path d="M-56-36h112q12 0 12 12v36q0 12-12 12h-72l-20 16v-16q-18 0-18-12v-36q0-12 12-12z" fill="#fffefd" class="o"/>
  {tick(0, -4, 0.38)}
</g>
<g transform="translate(180 250)">
  <path d="M-30-30h60v50h-60z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 6"/>
  {cross(0, -4, 0.28)}
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M500 300h60"/></g>''', ground=False)

add('merciless', '倒れた相手にも手を緩めず攻め続ける', f'''
{table(380)}
{person(200, 380, 1.15, 1, 'violet', 'blue', 'up', 'short', 'neutral')}
<g transform="translate(430 370)">
  <path d="M-40-6h100v14h-100z" fill="{TONES['blue'][2]}"/>
  <path d="M-60-40q60-24 110 0l-10 34h-92z" class="coral o"/>
  <circle cx="-80" cy="-56" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(-80 52) scale(1.06)" fill="{HAIR}"/>
  <path d="M-92-58q8-8 16 0M-80-58q8-8 16 0" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M280 220h100"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M280 280h100"/></g>
{cross(120, 160, 0.6)}''', ground=False)

add('metallic', '光を鋭く反射する、金属の質感', f'''
{split()}
{table(380)}
<g transform="translate(150 260)">
  <path d="M-80-70h160v140h-160z" fill="#c8a070" class="o"/>
</g>
<g transform="translate(450 260)">
  <path d="M-80-70h160v140h-160z" fill="#9aa5b0" class="o"/>
  <g fill="#fffefd" opacity="0.8">
    <path d="M-60-56h34l-70 106v-56z"/>
    <path d="M10-56h26l-70 126h-20z"/>
  </g>
  <path d="M-80-70h160v140h-160z" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>
<circle cx="450" cy="260" r="120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
