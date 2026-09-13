# -*- coding: utf-8 -*-
"""第133回。状態の変化と句動詞。"""
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


# --- 熟れる・腐る -------------------------------------------------------------
add('ripe', '青い実・食べごろの実・傷んだ実が並び、まん中が食べごろ', f'''
{table(340)}
<g transform="translate(140 250)"><circle r="60" class="green o"/><path d="M0-60q-12-24 6-30 16 6 6 30z" class="greend o"/></g>
<g transform="translate(300 250)"><circle r="66" class="coral o"/><path d="M0-66q-12-26 8-32 18 6 6 32z" class="greend o"/></g>
<g transform="translate(460 250)">
  <circle r="60" fill="#8b6f52" class="o"/>
  <g fill="#5b4a3c"><ellipse cx="-16" cy="10" rx="20" ry="14"/><ellipse cx="22" cy="-14" rx="14" ry="10"/></g>
</g>
<circle cx="300" cy="250" r="86" fill="none" stroke="{TONES['green'][0]}" stroke-width="5" stroke-dasharray="12 10"/>
{tick(300, 120, 0.7)}''', ground=False)

add('ripen', '緑だった実が日を浴びて赤く熟していく', f'''
{split()}
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
{table(360)}
<g transform="translate(150 240)">
  <circle r="70" class="green o"/>
  <path d="M0-70q-14-28 6-34 18 6 8 34z" class="greend o"/>
</g>
<g transform="translate(450 240)">
  <circle r="78" class="coral o"/>
  <path d="M0-78q-14-30 8-36 18 6 6 36z" class="greend o"/>
  <ellipse cx="-28" cy="-28" rx="16" ry="11" fill="#fffefd" opacity="0.4" transform="rotate(-30 -28 -28)"/>
</g>
{sun(300, 90, 34)}
<g class="a" marker-end="url(#ar)"><path d="M270 240h60"/></g>''', arrow=True, ground=False)

add('rotten', 'かびが生えて崩れかけた果物にハエが寄る', f'''
{table(340)}
<g transform="translate(280 260)">
  <path d="M-80-30q40-40 90-16 50 24 66 32-30 26-90 26t-66-42z" fill="#8b6f52" class="o"/>
  <g fill="#5b4a3c"><ellipse cx="-30" cy="0" rx="26" ry="16"/><ellipse cx="34" cy="8" rx="20" ry="12"/><ellipse cx="6" cy="-20" rx="16" ry="10"/></g>
  <g fill="#6f7a4a"><circle cx="-52" cy="-16" r="8"/><circle cx="20" cy="18" r="7"/></g>
</g>
<g fill="{INK}">
''' + ''.join(f'<g transform="translate({390+i*32} {160+(i%3)*30}) rotate({-20+i*22}) scale(0.6)"><ellipse rx="12" ry="8"/><ellipse cx="10" cy="-10" rx="12" ry="6" fill="#fffefd" stroke="{INK}" stroke-width="2" opacity="0.8"/></g>' for i in range(4)) + f'''
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" opacity="0.8">
  <path d="M180 190q14-24 0-44M240 176q14-26 0-48"/>
</g>
{cross(120, 140, 0.7)}''', ground=False)

add('seasonal', '同じ木が春夏秋冬で姿を変える', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
<path d="M0 300h600v100H0z" fill="#dfe8d8"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M150 40v340M300 40v340M450 40v340"/></g>
<g transform="translate(75 300)">
  <path d="M-8 0v-60h16V0z" fill="{BRN}" class="o"/>
  <circle cy="-84" r="34" class="coralp o"/>
</g>
<g transform="translate(225 300)">
  <path d="M-8 0v-60h16V0z" fill="{BRN}" class="o"/>
  <circle cy="-90" r="42" class="greenp o"/>
</g>
<g transform="translate(375 300)">
  <path d="M-8 0v-60h16V0z" fill="{BRN}" class="o"/>
  <circle cy="-86" r="38" class="goldp o"/>
  <g class="gold"><circle cx="-40" cy="-20" r="6"/><circle cx="36" cy="-10" r="6"/></g>
</g>
<g transform="translate(525 300)">
  <path d="M-8 0v-60h16V0z" fill="{BRN}" class="o"/>
  <g stroke="{BRN}" stroke-width="6" stroke-linecap="round" fill="none">
    <path d="M0-60l-30-30M0-60l30-30M0-70v-24"/>
  </g>
  <g fill="#fffefd"><circle cx="-20" cy="-96" r="6"/><circle cx="24" cy="-108" r="5"/></g>
</g>''', ground=False)

# --- 動きと液体 --------------------------------------------------------------
add('roam', '柵のない広い野をあてもなく歩き回る', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v170H0z" fill="#c9d8c0"/>
<path d="M0 230h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10">
  <path d="M80 380q60-90 150-40t120-70 160 30"/>
</g>
{person(300, 330, 1.0, 1, 'coral', 'green', 'walk', 'cap', 'smile', 'walk')}
{tree(80, 280, 0.8)}
{tree(520, 300, 1.0)}
{sun(500, 70, 30)}
<g fill="{TONES['green'][0]}" opacity="0.4">
''' + ''.join(f'<circle cx="{40+i*44}" cy="{300+(i%4)*22}" r="7"/>' for i in range(13)) + f'''
</g>''', ground=False)

add('scatter', '種を手から広くまき散らす', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v170H0z" fill="#a8845c"/>
<path d="M0 230h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
{person(140, 350, 1.05, 1, 'gold', 'blue', 'reach', 'cap', 'smile')}
{hand(230, 200, 1)}
<g fill="#6b4c28">
''' + ''.join(f'<ellipse cx="{280+ (i%9)*34}" cy="{160+(i//9)*54}" rx="7" ry="5" transform="rotate({i*23} {280+(i%9)*34} {160+(i//9)*54})"/>' for i in range(27)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 180q90-40 200 20"/></g>''', arrow=True, ground=False)

add('seep', '水がひび割れからじわじわしみ出てくる', f'''
<path d="M0 0h600v400H0z" fill="#c8b8a0"/>
<g fill="none" stroke="#b0a088" stroke-width="3">
''' + ''.join(f'<path d="M0 {60+i*70}h600"/>' for i in range(5)) + f'''
</g>
<path d="M300 40q-20 60 10 110t-16 100 20 150" fill="none" stroke="#8f7f68" stroke-width="8"/>
<g fill="{TONES['blue'][1]}" opacity="0.85">
  <path d="M280 120q60 20 40 70t-20 90 30 120h-70q-30-100 0-160t-10-120z"/>
</g>
<g fill="{TONES['blue'][0]}">
  <path d="M300 200q10 12 10 20t-10 8-10-8 10-20z"/>
  <path d="M290 280q9 11 9 18t-9 7-9-7 9-18z"/>
  <path d="M310 340q9 11 9 18t-9 7-9-7 9-18z"/>
</g>
<g fill="{TONES['blue'][1]}"><ellipse cx="300" cy="388" rx="90" ry="12"/></g>
<g class="a" marker-end="url(#ar)"><path d="M460 140l-120 80"/></g>''', arrow=True, ground=False)

add('solidify', '溶けていたろうが冷えて固まる', f'''
{split()}
{table(340)}
<g transform="translate(150 280)">
  <path d="M-90 0q40-40 90-20 50 20 90 20-40 26-90 26t-90-26z" fill="#f0d8a8" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" opacity="0.7">
    <path d="M-30-40q12-20 0-36M30-46q12-22 0-40"/>
  </g>
</g>
<g transform="translate(450 250)">
  <path d="M-56-60h112v110h-112z" fill="#f0d8a8" class="o"/>
  <path d="M-56-60l14-16h112l-14 16z" fill="#f6e6c4" class="o"/>
  <path d="M56-60l14-16v110l-14 16z" fill="#e0c890" class="o"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M300 130v-30M286 112h28M292 104l16 16M308 104l-16 16"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 260h60"/></g>''', arrow=True, ground=False)

add('stagger', '足元がふらついてよろよろ歩く', f'''
{table(380)}
<g transform="translate(300 380) rotate(-14)">
  <path d="M-12-8l-40 26M12-8l30 30" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-27-78q27-14 54 0l-8 72h-38z" class="coral o"/>
  <path d="M-22-70l-40 14M22-70l40 20" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cy="-108" r="25" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="scale(1.04)" fill="{HAIR}"/>
  <path d="M-14-108q8-8 16 0M-2-108q8-8 16 0" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <path d="M-8-90h16" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8">
  <path d="M60 384q60-30 110 0t110 0 110 0 110 0"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M420 200q30 20 40 44M460 160q34 24 44 50"/>
</g>''', ground=False)

add('stagnate', '流れの止まった水が濁ってよどむ', f'''
{split()}
<path d="M0 0h600v170H0z" fill="#dceaf4"/>
<path d="M0 170h300v230H0z" fill="#5b8caa"/>
<path d="M300 170h300v230H300z" fill="#6b7a5e"/>
<path d="M0 170h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="#a8c8dd" stroke-width="5">
  <path d="M20 230q40-24 80 0t80 0 80 0M20 300q40-24 80 0t80 0 80 0M20 360q40-24 80 0t80 0 80 0"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="#a8c8dd" stroke-width="5"><path d="M60 120h180"/></g>
<g fill="none" stroke="#566349" stroke-width="4">
  <path d="M330 240h230M330 310h230"/>
</g>
<g class="greend o" opacity="0.9">
  <ellipse cx="390" cy="260" rx="46" ry="16"/><ellipse cx="500" cy="330" rx="52" ry="18"/><ellipse cx="440" cy="380" rx="40" ry="14"/>
</g>
{cross(430, 120, 0.7)}''', ground=False)

add('stiffen', '柔らかかった布が糊でぴんと固くなる', f'''
{split()}
{table(340)}
<g transform="translate(150 250)">
  <path d="M-80-40q80-30 160 0 10 60-16 76-64 16-128 0-26-16-16-76z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3"><path d="M-64 0q64 20 128 0"/></g>
</g>
<g transform="translate(450 250)">
  <path d="M-80-40h160v80h-160z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3"><path d="M-64 0h128"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
    <path d="M-96-56l-20-16M96-56l20-16M-96 56l-20 16M96 56l20 16"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('stabilise', '揺れていた棒が支えを得て止まる', f'''
{split()}
{table(380)}
<g transform="translate(150 380) rotate(-16)">
  <path d="M-16-200h32v200h-32z" fill="#c9a464" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M100 150q-20 20 0 40M210 140q20 20 0 40"/>
</g>
<g transform="translate(450 380)">
  <path d="M-16-200h32v200h-32z" fill="#c9a464" class="o"/>
  <path d="M-16-90l-70 90h70zM16-90l70 90H16z" fill="#8b6437" class="o"/>
</g>
{tick(450, 130, 0.7)}
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('soothe', 'ひりひりする腕に薬をぬって痛みを和らげる', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-100 20q60-30 200 0" stroke="{SKIN}" stroke-width="60" stroke-linecap="round" fill="none"/>
  <path d="M-100 20q60-30 200 0" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
  <g class="coral o" opacity="0.8"><ellipse cx="20" cy="10" rx="46" ry="26"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
    <path d="M-10-40l-14-24M50-44l14-24"/>
  </g>
</g>
<g transform="translate(450 250)">
  <path d="M-100 20q60-30 200 0" stroke="{SKIN}" stroke-width="60" stroke-linecap="round" fill="none"/>
  <path d="M-100 20q60-30 200 0" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
  <g class="coral o" opacity="0.25"><ellipse cx="20" cy="10" rx="26" ry="16"/></g>
</g>
<g transform="translate(300 130)">
  <path d="M-24-40h48v70q0 12-24 12t-24-12z" fill="#e8f0f6" class="o"/>
  <path d="M-12-40v-12h24v12z" class="green o"/>
  <path d="M-18-10h36v34q0 8-18 8t-18-8z" fill="{TONES['green'][1]}"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('slippery', 'ぬれた床で足が滑る', f'''
{table(380)}
<g transform="translate(300 360)">
  <ellipse rx="200" ry="26" fill="{TONES['blue'][1]}" class="o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"><ellipse rx="130" ry="14"/></g>
</g>
<g transform="translate(300 350) rotate(-24)">
  <path d="M-12-8l-56 20M12-8l40 30" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-27-78q27-14 54 0l-8 72h-38z" class="coral o"/>
  <path d="M-22-70l-40-20M22-70l42-16" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cy="-108" r="25" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="scale(1.04)" fill="{HAIR}"/>
  <circle cx="-8" cy="-104" r="2.4" fill="{INK}"/><circle cx="8" cy="-104" r="2.4" fill="{INK}"/>
  <circle cy="-90" r="5" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
<g transform="translate(130 240)">
  <path d="M0-50l60 100H-60z" class="gold o"/>
  <path d="M-4-14h8v30h-8z" fill="{INK}"/>
  <circle cy="32" r="5" fill="{INK}"/>
</g>''', ground=False)

# --- 句動詞 -----------------------------------------------------------------
add('round-up', '散らばった羊を一か所に寄せ集める', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v170H0z" fill="#c9d8c0"/>
<path d="M0 230h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="{BRN}" stroke-width="6" stroke-dasharray="14 12"><ellipse cx="420" cy="300" rx="130" ry="80"/></g>
<g>
''' + ''.join(f'''<g transform="translate({350+ (i%3)*70} {270+(i//3)*54}) scale(0.6)">
  <ellipse rx="60" ry="42" fill="#fffdf6" class="o"/>
  <circle cx="52" cy="-24" r="26" fill="#e8e2d6" class="o"/>
  <circle cx="62" cy="-28" r="4" fill="{INK}"/>
  <g stroke="{MUTED}" stroke-width="9" stroke-linecap="round" fill="none"><path d="M-24 40v16M18 40v16"/></g>
</g>''' for i in range(6)) + f'''
</g>
{person(120, 340, 1.0, 1, 'teal', 'blue', 'reach', 'cap', 'smile')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M200 250q80-60 140 10"/></g>''', ground=False)

add('run-down', '使いっぱなしで電池の残りがなくなる', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g>
''' + ''.join(f'''<g transform="translate({100+i*130} 200)">
  <path d="M-50-90h100v180h-100z" fill="#fffefd" class="o"/>
  <path d="M-20-100h40v10h-40z" fill="{INK}"/>
  <path d="M-40 {80-i*44}h80v{-(80-i*44)+80}z" fill="none"/>
  <path d="M-40 {-i*44+36}h80v{44+i*44}h-80z" fill="{[TONES['green'][0], TONES['green'][0], TONES['gold'][0], TONES['coral'][0]][i]}"/>
</g>''' for i in range(4)) + f'''
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M90 340h430"/></g>''', ground=False)

add('seize-on', '相手の言葉じりに飛びついて取り上げる', f'''
{table(380)}
{person(150, 380, 1.0, 1, 'teal', 'blue', 'point', 'short', 'neutral')}
{person(450, 380, 1.05, -1, 'coral', 'blue', 'reach', 'bun', 'smile')}
<g transform="translate(250 170)">
  <path d="M-70-34h140q12 0 12 12v34q0 12-12 12h-96l-20 16v-16q-12 0-12-12v-34q0-12 12-12z" fill="#fffefd" class="o"/>
  {word(-16, -4, 4, 26, MUTED)}
  <rect x="44" y="-11" width="22" height="22" rx="4" class="coral"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M400 230l-90-40"/></g>
<circle cx="306" cy="166" r="34" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"/>''', ground=False)

add('settle-for', '欲しかった品をあきらめ、小さい方で手を打つ', f'''
{table(380)}
<g transform="translate(160 250)">
  <path d="M-70-70h140v140h-140z" class="goldp o"/>
  <path d="M-70-70l16-20h140l-16 20z" fill="{TONES['gold'][1]}" class="o"/>
</g>
{cross(160, 250, 1.2)}
<g transform="translate(430 290)">
  <path d="M-40-40h80v80h-80z" class="tealp o"/>
  <path d="M-40-40l10-14h80l-10 14z" fill="{TONES['teal'][1]}" class="o"/>
</g>
{person(540, 380, 0.9, -1, 'coral', 'blue', 'reach', 'bun', 'neutral')}
<g class="a" marker-end="url(#ar)" stroke="{MUTED}" stroke-width="5"><path d="M250 150q90-60 170 60"/></g>''', ground=False)

add('shake-off', 'まとわりつく追手を振り切って逃げる', f'''
{table(380)}
{person(430, 380, 1.1, 1, 'coral', 'blue', 'walk', 'cap', 'neutral', 'walk')}
<g opacity="0.45">{person(200, 380, 1.0, 1, 'blue', 'blue', 'walk', 'short', 'sad', 'walk')}</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><path d="M240 300q80-40 140 0"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="6"><path d="M480 200h90"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M330 240h50M320 290h40"/>
</g>
{cross(200, 200, 0.6)}''', ground=False)

add('shortlist', '大勢の応募者から数人だけを最終候補に残す', f'''
{split()}
{table(380)}
<g>
''' + ''.join(head(70+ (i%4)*46, 200+(i//4)*70, 18, ['teal','coral','gold','violet'][i%4], ['short','bob','bun','cap'][i%4]) for i in range(12)) + f'''
</g>
<g>
{head(400, 250, 24, 'coral', 'bob')}
{head(480, 250, 24, 'teal', 'short')}
{head(560, 250, 24, 'gold', 'bun')}
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="5" stroke-dasharray="12 10">
  <path d="M350 180h260v160H350z"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('scoop', 'アイスをすくって丸く盛る', f'''
{table(340)}
<g transform="translate(330 300)">
  <path d="M-70-30h140l-16 60q-2 12-54 12t-54-12z" fill="#e8f0f6" class="o"/>
  <circle cx="-24" cy="-46" r="34" fill="#f6e0c8" class="o"/>
  <circle cx="30" cy="-52" r="32" class="coralp o"/>
  <circle cx="4" cy="-88" r="30" class="goldp o"/>
</g>
<g transform="translate(160 200) rotate(30)">
  <path d="M-8-70h16v90h-16z" fill="#8f9aa6" class="o"/>
  <path d="M-34 20q0-30 34-30t34 30q0 26-34 26t-34-26z" fill="#c8d0d8" class="o"/>
  <path d="M-24 20q0-20 24-20t24 20" fill="#f6e0c8" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 250q50 20 60 40"/></g>''', arrow=True, ground=False)

add('saddle', '馬の背に鞍を置いて締める', f'''
<path d="M0 0h600v260H0z" fill="#dceaf4"/>
<path d="M0 260h600v140H0z" fill="#dfe8d8"/>
<path d="M0 260h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(320 290)">
  <path d="M-120 0q-10-52 40-62h100q46 6 56 48-40 24-104 24-76 0-92-10z" fill="#a0764a" class="o"/>
  <path d="M92-52q40-38 58-66 22 16 8 58l-24 42z" fill="#a0764a" class="o"/>
  <path d="M146-116q-8-32 6-34 12 8 6 34zM168-122q10-28 20-22 4 10-8 28z" fill="#a0764a" class="o"/>
  <path d="M152-82l28 8-28 10z" fill="#8b6437" class="o"/>
  <circle cx="140" cy="-98" r="4" fill="{INK}"/>
  <path d="M-120 0q-44-16-54-56 44 6 62 42z" fill="#6b4c28" class="o"/>
  <g stroke="#8b6437" stroke-width="13" stroke-linecap="round" fill="none">
    <path d="M-70 14l-40 40M-26 18l-6 52M40 16l40 40M76 12l6 54"/>
  </g>
</g>
<g transform="translate(280 224)">
  <path d="M-56 10q-14-40 20-46 36-6 72 0 34 6 20 46-56 14-112 0z" fill="#7a5b3c" class="o"/>
  <path d="M-56 10q-30 4-30 20 30 8 30-8zM56 10q30 4 30 20-30 8-30-8z" fill="#7a5b3c" class="o"/>
  <path d="M-20 20v50h30v-14h-24" fill="none" stroke="#5b4a3c" stroke-width="6"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 130v50"/></g>''', arrow=True, ground=False)

# --- 調べる・示す -------------------------------------------------------------
add('scrutinise', '書類を虫めがねで一行ずつ細かく調べる', f'''
{table(380)}
<g transform="translate(280 210) rotate(-3)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-130" y="{-108+i*40}" width="{260-(i%3)*60}" height="10" rx="5"/>' for i in range(6)) + f'''
  </g>
</g>
<g transform="translate(340 240)">
  <circle r="86" fill="#eef6fb" class="o" opacity="0.9"/>
  <g fill="{INK}"><rect x="-60" y="-24" width="120" height="16" rx="8"/><rect x="-60" y="8" width="90" height="16" rx="8"/></g>
  <circle r="86" fill="none" stroke="#8f9aa6" stroke-width="12"/>
  <path d="M62 62l56 56" stroke="{INK}" stroke-width="16" stroke-linecap="round" fill="none"/>
</g>
{person(90, 380, 0.8, 1, 'violet', 'blue', 'stand', 'bun', 'neutral')}''', ground=False)

add('ascertain', '目盛りを読んで事実を確かめる', f'''
{table(380)}
<g transform="translate(250 210)">
  <path d="M-120-30h240v60h-240z" class="goldp o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">
''' + ''.join(f'<path d="M{-110+i*22} -30v{18 if i%5 else 30}"/>' for i in range(11)) + f'''
  </g>
</g>
<g transform="translate(200 150)">
  <path d="M-70-30h140v40h-140z" class="tealp o"/>
</g>
<g transform="translate(460 200)">
  <circle r="60" fill="#eef6fb" class="o" opacity="0.9"/>
  <circle r="60" fill="none" stroke="#8f9aa6" stroke-width="11"/>
  <path d="M44 44l44 44" stroke="{INK}" stroke-width="14" stroke-linecap="round" fill="none"/>
</g>
<g transform="translate(300 330)">
  <path d="M-60-24h120v48h-120z" class="paper"/>
  {tick(0, 0, 0.4)}
</g>''', ground=False)

add('delineate', 'ぼんやりした形の輪郭をはっきりなぞって示す', f'''
{split()}
{table(380)}
<g transform="translate(150 240)">
  <path d="M-80 40q-30-60 10-90 50-36 110-14 50 20 50 60 0 40-70 46-80 6-100-2z" fill="{TONES['teal'][1]}" opacity="0.55"/>
</g>
<g transform="translate(450 240)">
  <path d="M-80 40q-30-60 10-90 50-36 110-14 50 20 50 60 0 40-70 46-80 6-100-2z" fill="{TONES['teal'][1]}"/>
  <path d="M-80 40q-30-60 10-90 50-36 110-14 50 20 50 60 0 40-70 46-80 6-100-2z" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<g transform="translate(530 330) rotate(30)">
  <path d="M0-70l10 22v60h-20V-48z" class="teal o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 240h60"/></g>''', arrow=True, ground=False)

add('elucidate', 'もつれた線をほどいて筋道をはっきりさせる', f'''
{split()}
{table(380)}
<g transform="translate(150 240)">
  <path d="M-90 40q40-90 90-30t-60 20 90-70 40 80-100-40 60 40" fill="none" stroke="{TONES['violet'][0]}" stroke-width="7"/>
</g>
<g transform="translate(450 240)">
  <g class="a" marker-end="url(#ar)" stroke="{TONES['violet'][0]}" stroke-width="6">
    <path d="M-90 40h180"/>
  </g>
  <g fill="{TONES['violet'][0]}"><circle cx="-90" cy="40" r="9"/><circle cx="-30" cy="40" r="9"/><circle cx="30" cy="40" r="9"/></g>
</g>
{person(540, 380, 0.8, -1, 'teal', 'blue', 'point', 'bun', 'smile')}
<g class="a" marker-end="url(#ar)"><path d="M270 240h60"/></g>''', arrow=True, ground=False)

add('enlighten', '知らなかった人に教えて頭の中が明るくなる', f'''
{split()}
{table(380)}
{person(150, 380, 1.05, 1, 'blue', 'blue', 'think', 'short', 'neutral')}
<g transform="translate(220 200)">
  <path d="M-34-30h68q10 0 10 10v30q0 10-10 10h-46l-16 14v-14q-16 0-16-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M-14-18q0-14 14-14t14 14-14 12v8" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>
  <circle cy="14" r="3.5" fill="{MUTED}"/>
</g>
{person(450, 380, 1.05, 1, 'coral', 'blue', 'up', 'short', 'smile')}
<g transform="translate(450 200)">
  <circle r="34" class="goldp o"/>
  <path d="M0-18q18 0 18 16t-10 16v8h-16v-8q-10 0-10-16t18-16z" class="gold"/>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{48*math.cos(i*0.785):.0f} {48*math.sin(i*0.785):.0f}l{16*math.cos(i*0.785):.0f} {16*math.sin(i*0.785):.0f}"/>' for i in range(8)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 280h60"/></g>''', arrow=True, ground=False)

add('entail', '家を買うと税や修理費も必ずついてくる', f'''
{table(380)}
{building(160, 320, 0.9, 'coral')}
<g class="a" marker-end="url(#ar)" stroke-width="5"><path d="M250 280h70"/></g>
<g>
''' + ''.join(f'''<g transform="translate({420+ (i%2)*0} {170+i*80})">
  <path d="M-90-30h180v60h-180z" class="goldp o"/>
  <rect x="-64" y="-8" width="{110-i*20}" height="16" rx="8" fill="{MUTED}"/>
</g>''' for i in range(3)) + f'''
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M330 280v-110h20M330 280h20M330 280v80h20"/></g>''', ground=False)

add('extrapolate', '手前の点の並びから、先の値を推し量る', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(300 230)">
  <path d="M-250 130h500v6h-500z" fill="{INK}"/>
  <path d="M-250-170v300h6v-300z" fill="{INK}"/>
  <path d="M-230 100l50-24 50-30 50-36" fill="none" stroke="{TONES['teal'][0]}" stroke-width="7" stroke-linejoin="round"/>
  <g fill="{TONES['teal'][2]}">
''' + ''.join(f'<circle cx="{-230+i*50}" cy="{100-i*30}" r="8"/>' for i in range(4)) + f'''
  </g>
  <path d="M-80 10l160-96" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="14 10"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="8 6">
    <circle cx="80" cy="-86" r="20"/>
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M-80-170v300"/></g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M300 340q60-40 120-30"/></g>''', arrow=True, ground=False)

add('hypothesise', 'まだ確かめていない説を立てて図に書く', f'''
{table(380)}
<g transform="translate(340 200)">
  <path d="M-170-140h340v280h-340z" fill="#e8f0e4" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10">
    <circle cx="-80" cy="-50" r="44"/><circle cx="60" cy="-30" r="52"/><circle cx="-10" cy="70" r="40"/>
    <path d="M-40-40h60M40 20l-40 20"/>
  </g>
  <path d="M110-118q0-24 22-24t22 24-22 20v12" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/>
  <circle cx="132" cy="-52" r="5" fill="{MUTED}"/>
</g>
{person(110, 380, 0.9, 1, 'teal', 'blue', 'reach', 'bun', 'neutral')}''', ground=False)

add('affirm', '手を挙げてはっきりそうだと言い切る', f'''
{table(380)}
{person(300, 380, 1.25, 1, 'teal', 'blue', 'up', 'short', 'neutral')}
<g transform="translate(450 180)">
  <path d="M-56-40h112q12 0 12 12v40q0 12-12 12h-72l-22 16v-16q-18 0-18-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  {tick(0, -4, 0.45)}
</g>
{hand(230, 200, -1)}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M170 250l-24-18M400 300l24-16"/>
</g>''', ground=False)

add('absolve', '調べのすえ責任なしと認められて肩の荷が下りる', f'''
{split()}
{table(380)}
{person(150, 380, 1.05, 1, 'blue', 'blue', 'stand', 'short', 'sad')}
<g transform="translate(150 250)">
  <path d="M-56-40h112v56h-112z" fill="#9aa5b0" class="o"/>
  <path d="M-40-40q0-24 40-24t40 24" fill="none" stroke="#7d8894" stroke-width="7"/>
</g>
{person(450, 380, 1.05, 1, 'coral', 'blue', 'up', 'short', 'smile')}
<g transform="translate(300 120)">
  {doc(0, 0, 110, 120, 3)}
  {tick(0, 34, 0.4)}
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}"><path d="M270 300h60"/></g>''', ground=False)

add('aggravate', 'もともとの傷を引っかいてさらに悪くする', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-100 20q60-30 200 0" stroke="{SKIN}" stroke-width="60" stroke-linecap="round" fill="none"/>
  <path d="M-100 20q60-30 200 0" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-10 6q26-14 44 4" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
<g transform="translate(450 250)">
  <path d="M-100 20q60-30 200 0" stroke="{SKIN}" stroke-width="60" stroke-linecap="round" fill="none"/>
  <path d="M-100 20q60-30 200 0" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
  <g class="coral o"><ellipse cx="10" cy="8" rx="52" ry="28"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
    <path d="M-20-40l-14-26M40-44l16-26M80-14l30-14"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('necessitate', '雨が降ったので傘が必ず要る', f'''
<path d="M0 0h600v400H0z" fill="#c8d2da"/>
{table(380)}
{cloud(200, 90, 1.3, 'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{100+i*38} {170+(i%3)*40}l-14 40"/>' for i in range(7)) + f'''
</g>
<g class="a" marker-end="url(#ar)" stroke-width="6"><path d="M370 220h70"/></g>
<g transform="translate(510 250)">
  <path d="M-70 0q0-70 70-70t70 70q-36-24-70-24t-70 24z" class="coral o"/>
  <path d="M0 0v80q0 18 20 18" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <path d="M0-70v-16" stroke="{INK}" stroke-width="5" fill="none"/>
</g>
{tick(510, 130, 0.6)}''', ground=False)

add('predispose', '同じ寒さでも、疲れた人のほうが風邪をひきやすい', f'''
{split()}
{table(380)}
{person(150, 380, 1.05, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(450, 380, 1.05, 1, 'teal', 'blue', 'stand', 'short', 'sad')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M400 240q-16 12-16 28M500 236q16 12 16 28"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M60 120v-30M46 102h28M52 94l16 16M68 94l-16 16M360 120v-30M346 102h28M352 94l16 16M368 94l-16 16"/>
</g>
<g fill="{TONES['coral'][0]}" opacity="0.6"><circle cx="450" cy="250" r="46"/></g>
{cross(560, 150, 0.5)}
{tick(250, 150, 0.5)}''', ground=False)

add('esteem', 'まわりから高く評価されて壇上に立つ', f'''
{table(380)}
<g transform="translate(300 360)">
  <path d="M-60-60h120v60h-120z" class="goldp o"/>
  <path d="M-180-30h120v30h-120zM60-30h120v30H60z" fill="#dde3e8" class="o"/>
</g>
{person(300, 300, 1.05, 1, 'coral', 'gold', 'up', 'bun', 'smile')}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{300+130*math.cos(3.5+i*0.45):.0f} {200+130*math.sin(3.5+i*0.45):.0f}l{20*math.cos(3.5+i*0.45):.0f} {20*math.sin(3.5+i*0.45):.0f}"/>' for i in range(8)) + f'''
</g>
{head(90, 350, 20, 'teal', 'short')}
{head(510, 350, 20, 'violet', 'bob')}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="3" stroke-dasharray="8 7">
  <path d="M130 320q60-40 130-40M470 320q-60-40-130-40"/>
</g>''', ground=False)

add('poise', '本を頭に載せてまっすぐ落ち着いて立つ', f'''
{table(380)}
{person(300, 380, 1.25, 1, 'violet', 'blue', 'stand', 'bun', 'smile')}
<g transform="translate(300 208)">
  <path d="M-56-16h112v20h-112z" class="teal o"/>
  <path d="M-56 4h112v10h-112z" fill="#fffdf6" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M300 180v200"/></g>
<g class="a" marker-end="url(#ar)"><path d="M470 220l-110-10"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="4"><path d="M240 370h20v-20"/></g>''', arrow=True, ground=False)

add('foreground', 'ぼやけた背景の前に主役を大きく出す', f'''
<path d="M0 0h600v300H0z" fill="#dceaf4"/>
<path d="M0 300h600v100H0z" fill="#dfe8d8"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g opacity="0.3">
  {building(150, 300, 0.7, 'teal')}
  {building(470, 300, 0.7, 'blue')}
  {tree(300, 300, 0.8)}
</g>
{person(300, 380, 1.35, 1, 'coral', 'blue', 'up', 'bun', 'smile')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M470 150l-90 130"/></g>''', ground=False)

add('revolt', '民衆が旗を掲げて権力に反旗をひるがえす', f'''
{table(380)}
<g transform="translate(470 330)">
  <path d="M-70 50v-120h140v120z" fill="#8f9aa6" class="o"/>
  <path d="M-80-70h160v-20h-160z" fill="#7d8894" class="o"/>
  <path d="M-30-40h60v90h-60z" fill="#6f7b88" class="o"/>
</g>
{person(140, 380, 1.05, 1, 'coral', 'blue', 'up', 'cap', 'neutral')}
{person(230, 380, 1.0, 1, 'gold', 'blue', 'up', 'bob', 'neutral')}
{person(310, 380, 1.0, 1, 'teal', 'blue', 'up', 'short', 'neutral')}
<g transform="translate(190 200)">
  <path d="M0 100V-40" stroke="{BRN}" stroke-width="8" stroke-linecap="round" fill="none"/>
  <path d="M4-40q56 10 94-10 6 40-4 58-46 14-90 4z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M360 200h80"/></g>''', ground=False)

add('sightseeing', '観光名所をまわって写真を撮る', f'''
<path d="M0 0h600v270H0z" fill="#dceaf4"/>
<path d="M0 270h600v130H0z" fill="#dfe8d8"/>
<path d="M0 270h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
{sun(80, 70, 30)}
<g transform="translate(420 270)">
  <path d="M-70 0l30-190h20l30 190z" fill="#c8b8a0" class="o"/>
  <path d="M-46-140h72M-38-90h56" stroke="#a89880" stroke-width="6" fill="none"/>
  <path d="M-10-200h20v20h-20z" class="coral o"/>
</g>
{person(180, 370, 1.05, 1, 'coral', 'blue', 'hold', 'bun', 'smile')}
<g transform="translate(220 260)">
  <path d="M-40-26h80v52h-80z" fill="#3b4450" class="o"/>
  <circle cx="6" r="16" fill="#8f9aa6" class="o"/><circle cx="6" r="8" fill="{INK}"/>
  <path d="M-36-26h22v-8h-22z" fill="#3b4450"/>
</g>
<g fill="#fffefd"><circle cx="300" cy="200" r="14" opacity="0.9"/></g>''', ground=False)

add('souvenir', '旅先で買った記念の小物を並べる', f'''
{table(340)}
<g transform="translate(160 260)">
  <circle r="46" fill="#e8f0f6" class="o" opacity="0.9"/>
  <path d="M-46 20h92q0 20-46 20t-46-20z" fill="#8f9aa6" class="o"/>
  <path d="M-14 14l14-40 14 40z" fill="#fffdf6" class="o"/>
  <g fill="#fffefd"><circle cx="-16" cy="-6" r="3"/><circle cx="14" cy="-16" r="3"/><circle cx="6" cy="6" r="3"/></g>
</g>
<g transform="translate(300 270)">
  <path d="M-40-40h80v70h-80z" class="coralp o"/>
  <path d="M-40-40l10-14h80l-10 14z" fill="{TONES['coral'][1]}" class="o"/>
  <circle cx="0" cy="-4" r="16" class="coral o"/>
</g>
<g transform="translate(440 250)">
  <path d="M-30-50h60v70q0 12-30 12t-30-12z" fill="#c9a464" class="o"/>
  <path d="M-14-50v-14h28v14z" fill="#8b6437"/>
  <path d="M-22-16h44v30q0 8-22 8t-22-8z" class="goldp"/>
</g>
{person(540, 340, 0.75, -1, 'teal', 'blue', 'reach', 'bun', 'smile')}''', ground=False)

add('slipper', 'かかとのない室内履きが玄関にそろえてある', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<path d="M0 260h600v140H0z" fill="#c9a464" class="o"/>
<g transform="translate(220 320)">
  <path d="M-70 20q-16-30 10-40 50-18 110-4 26 6 22 26-6 18-60 20-66 2-82-2z" class="violetp o"/>
  <path d="M-50-10q40-30 80-6 6 16-26 20-46 4-54-14z" class="violet o"/>
</g>
<g transform="translate(390 340)">
  <path d="M-70 20q-16-30 10-40 50-18 110-4 26 6 22 26-6 18-60 20-66 2-82-2z" class="violetp o"/>
  <path d="M-50-10q40-30 80-6 6 16-26 20-46 4-54-14z" class="violet o"/>
</g>
<path d="M0 250h600v14H0z" fill="#a0764a"/>''', ground=False)

add('spelling', '語を一字ずつ並べて書き表す', f'''
{table(380)}
<g transform="translate(300 190)">
  <path d="M-220-110h440v220h-440z" class="paper"/>
  {word(0, -50, 6, 46, INK)}
  <g fill="none" stroke="{MUTED}" stroke-width="3">
''' + ''.join(f'<path d="M{-140+i*46} 10h30"/>' for i in range(6)) + f'''
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3" stroke-dasharray="6 5">
''' + ''.join(f'<path d="M{-137+i*46} -74v100"/>' for i in range(7)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 330h240"/></g>''', arrow=True, ground=False)

add('so-far', '目盛りの途中まで進んで、そこまでの分を示す', f'''
{table(380)}
<g transform="translate(300 230)">
  <path d="M-230-30h460v60h-460z" fill="#e0d6c0" class="o"/>
  <path d="M-230-30h280v60h-280z" class="teal o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">
''' + ''.join(f'<path d="M{-230+i*46} -30v{16 if i%2 else 30}"/>' for i in range(11)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['teal'][0]}" stroke-width="5"><path d="M70 320h280"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M350 320h180"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M350 150v130"/></g>''', ground=False)

add('sterilisation', '器具を高温で処理して菌をなくす', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-90-16h180v32h-180z" fill="#dde3e8" class="o"/>
  <g fill="{INK}" opacity="0.6">
''' + ''.join(f'<circle cx="{-70+i*30}" cy="{-36+(i%3)*14}" r="8"/>' for i in range(6)) + f'''
  </g>
</g>
<g transform="translate(450 250)">
  <path d="M-90-16h180v32h-180z" fill="#dde3e8" class="o"/>
  <path d="M-120-60h240v130h-240z" fill="none" stroke="{INK}" stroke-width="5"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
    <path d="M-70 40q14-24 0-44M0 44q14-26 0-48M70 40q14-24 0-44"/>
  </g>
</g>
{tick(450, 130, 0.6)}
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('restate', '伝わらなかったことを別の形で言い直す', f'''
{table(380)}
{person(140, 380, 1.05, 1, 'teal', 'blue', 'point', 'bun', 'neutral')}
{person(460, 380, 1.05, -1, 'coral', 'blue', 'stand', 'short', 'neutral')}
<g transform="translate(250 150)">
  <path d="M-70-34h140q12 0 12 12v34q0 12-12 12h-96l-20 16v-16q-12 0-12-12v-34q0-12 12-12z" fill="#fffefd" class="o" opacity="0.5"/>
  {word(0, -4, 5, 26, MUTED)}
</g>
<g transform="translate(280 270)">
  <path d="M-70-34h140q12 0 12 12v34q0 12-12 12h-96l-20 16v-16q-12 0-12-12v-34q0-12 12-12z" fill="#fffefd" class="o"/>
  {word(0, -4, 5, 26, INK)}
</g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}"><path d="M400 200q40 40 0 76"/></g>
<g transform="translate(460 200)">
  <path d="M-16-24q0-20 16-20t16 20-16 16v10" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/>
  <circle cy="20" r="4.5" fill="{MUTED}"/>
</g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
