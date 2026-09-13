# -*- coding: utf-8 -*-
"""第134回。身のまわりの名詞と、置き換え・裏づけの動詞。"""
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


# --- 身のまわりの名詞 ---------------------------------------------------------
add('suitcase', '取っ手と車輪のついた四角い旅行かばん', f'''
{table(360)}
<g transform="translate(300 250)">
  <path d="M-110-80h220v170h-220z" class="teal o"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="5"><path d="M-110 0h220M-60-80v170M60-80v170"/></g>
  <path d="M-40-80v-30h80v30" fill="none" stroke="{INK}" stroke-width="9"/>
  <path d="M-6-110h12v-40h-12z" fill="#8f9aa6" class="o"/>
  <path d="M-30-152h60v14h-60z" fill="#8f9aa6" class="o"/>
  <circle cx="-70" cy="102" r="14" fill="{INK}"/><circle cx="70" cy="102" r="14" fill="{INK}"/>
  <path d="M-114 20h228v18h-228z" fill="{TONES['teal'][2]}"/>
</g>''', ground=False)

add('sunflower', '大きな黄色い花が太陽のほうを向いている', f'''
<path d="M0 0h600v300H0z" fill="#dceaf4"/>
<path d="M0 300h600v100H0z" fill="#c9d8c0"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
{sun(510, 80, 34)}
<g transform="translate(250 300)">
  <path d="M-10 0v-160h20V0z" class="greend o"/>
  <path d="M-10-70q-60-24-50-56 54 6 50 56zM10-110q60-24 70 6-52 26-70-6z" class="greenp o"/>
  <g transform="translate(0 -190)">
    <g class="gold o">
''' + ''.join(f'<ellipse cx="{64*math.cos(i*0.393):.0f}" cy="{64*math.sin(i*0.393):.0f}" rx="34" ry="17" transform="rotate({i*22.5} {64*math.cos(i*0.393):.0f} {64*math.sin(i*0.393):.0f})"/>' for i in range(16)) + f'''
    </g>
    <circle r="46" fill="#7a5b3c" class="o"/>
    <g fill="#5b4a3c">
''' + ''.join(f'<circle cx="{-30+ (i%6)*12}" cy="{-30+(i//6)*12}" r="4"/>' for i in range(36)) + f'''
    </g>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M330 110h110"/></g>''', arrow=True, ground=False)

add('supermarket', '棚とレジの並ぶ大きな食料品店', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<path d="M0 40h600v50H0z" class="teal o"/>
<g fill="#fffefd"><rect x="200" y="54" width="200" height="22" rx="11"/></g>
<g>
  <path d="M40 130h180v180H40zM380 130h180v180H380z" fill="#dde3e8" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
''' + ''.join(f'<path d="M40 {180+i*50}h180M380 {180+i*50}h180"/>' for i in range(3)) + f'''
  </g>
  <g class="o">
''' + ''.join(f'<rect x="{56+ (i%4)*42}" y="{140+(i//4)*50}" width="30" height="34" class="{["coralp","tealp","goldp","violetp"][i%4]}"/>' for i in range(12)) + f'''
''' + ''.join(f'<rect x="{396+ (i%4)*42}" y="{140+(i//4)*50}" width="30" height="34" class="{["goldp","violetp","coralp","tealp"][i%4]}"/>' for i in range(12)) + f'''
  </g>
</g>
<g transform="translate(300 330)">
  <path d="M-90-30h180v50h-180z" fill="#c9a464" class="o"/>
  <path d="M-90-30h180v-14h-180z" fill="#a0764a"/>
</g>
{person(300, 300, 0.62, 1, 'teal', 'blue', 'stand', 'bun', 'smile')}
{person(150, 380, 0.62, 1, 'coral', 'blue', 'walk', 'short', 'smile', 'walk')}''', ground=False)

add('surname', '書類の姓の欄だけが囲まれている', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-190-140h380v280h-380z" class="paper"/>
  <g>
''' + ''.join(f'''<g transform="translate(0 {-90+i*56})">
  <rect x="-160" y="-8" width="66" height="16" rx="8" fill="{MUTED}"/>
  <path d="M-80 12h240" stroke="{MUTED}" stroke-width="3"/>
  <rect x="-70" y="-8" width="{140-i*30}" height="16" rx="8" fill="{INK}"/>
</g>''' for i in range(4)) + f'''
  </g>
  <path d="M-170-112h340v46h-340z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M520 350l-190-250"/></g>''', arrow=True, ground=False)

add('teaspoon', '茶さじで砂糖をひとさじすくう', f'''
{table(330)}
<g transform="translate(280 220) rotate(30)">
  <path d="M-6-70h12v110h-12z" fill="#c8d0d8" class="o"/>
  <ellipse cy="-84" rx="22" ry="30" fill="#c8d0d8" class="o"/>
  <ellipse cy="-84" rx="15" ry="22" fill="#fffdf6"/>
</g>
<g transform="translate(430 280)">
  <path d="M-56-40h112v56q0 12-56 12t-56-12z" fill="#e8f0f6" class="o"/>
  <path d="M-50-24h100v34q0 10-50 10t-50-10z" fill="#fffdf6"/>
  <g fill="#fffefd" stroke="{MUTED}" stroke-width="1.5">
''' + ''.join(f'<circle cx="{-34+ (i%5)*17}" cy="{-6+(i//5)*14}" r="4"/>' for i in range(10)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 130l60 40"/></g>''', arrow=True, ground=False)

add('teenager', '13歳から19歳までの年ごろの若者', f'''
{table(380)}
{person(300, 380, 1.2, 1, 'coral', 'blue', 'stand', 'bob', 'smile')}
<g transform="translate(300 130)">
  <path d="M-160-40h320q14 0 14 14v40q0 14-14 14h-220l-30 20v-20q-14 0-14-14v-40q0-14 14-14z" fill="#fffefd" class="o"/>
  {word(-60, -4, 2, 34, INK)}
  <path d="M-8-4h16v6h-16z" fill="{MUTED}"/>
  {word(66, -4, 2, 34, INK)}
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M300 190v40"/></g>
<g transform="translate(120 300)">
  <path d="M-40-26h80v52h-80z" fill="#3b4450" class="o"/>
  <path d="M-32-18h64v36h-32z" fill="#dceaf4"/>
  <path d="M-32-18h64v36h-64z" fill="#dceaf4"/>
</g>''', ground=False)

add('telescope', '長い筒をのぞいて遠くの星を見る', f'''
<path d="M0 0h600v400H0z" fill="#1e2338"/>
<g fill="#fffefd"><circle cx="440" cy="60" r="5"/><circle cx="510" cy="120" r="4"/><circle cx="380" cy="120" r="3"/><circle cx="480" cy="180" r="4"/><circle cx="550" cy="60" r="3"/></g>
<g transform="translate(400 100)">
  <circle r="24" class="goldp o"/>
  <g class="golds"><path d="M0-40v-14M0 40v14M-40 0h-14M40 0h14"/></g>
</g>
<g transform="translate(240 250) rotate(-34)">
  <path d="M-90-26h150v52h-150z" fill="#5a6270" class="o"/>
  <path d="M60-34h60v68H60z" fill="#8f9aa6" class="o"/>
  <path d="M-120-18h30v36h-30z" fill="#3b4450" class="o"/>
</g>
<g transform="translate(220 380)">
  <path d="M-6-100h12v100h-12z" fill="#8f9aa6" class="o"/>
  <path d="M0-20l-60 20h120z" fill="#8f9aa6" class="o"/>
</g>
{person(120, 380, 0.8, 1, 'teal', 'blue', 'reach', 'bun', 'smile')}''', ground=False)

add('timetable', '列車の発車時刻が並んだ表', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-200-150h400v300h-400z" class="paper"/>
  <path d="M-200-150h400v50h-400z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5">
''' + ''.join(f'<path d="M-200 {-58+i*48}h400"/>' for i in range(5)) + f'''
    <path d="M-60-100v250M80-100v250"/>
  </g>
  <g fill="{INK}">
''' + ''.join(f'<rect x="-180" y="{-88+i*48}" width="100" height="14" rx="7"/>' for i in range(5)) + f'''
  </g>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-46" y="{-88+i*48}" width="{110-(i%3)*20}" height="14" rx="7"/>' for i in range(5)) + f'''
  </g>
  <g fill="{TONES['coral'][0]}">
''' + ''.join(f'<rect x="96" y="{-88+i*48}" width="80" height="14" rx="7"/>' for i in range(5)) + f'''
  </g>
</g>''', ground=False)

add('toothbrush', '柄の先に毛の束がついた歯ブラシ', f'''
{table(340)}
<g transform="translate(300 240) rotate(-16)">
  <path d="M-160-14h220q20 0 20 14t-20 14h-220q-16 0-16-14t16-14z" class="teal o"/>
  <path d="M60-18h100q18 0 18 18t-18 18H60z" fill="#e8f0f6" class="o"/>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="2">
''' + ''.join(f'<rect x="{70+i*22}" y="-40" width="16" height="24" rx="4"/>' for i in range(5)) + f'''
  </g>
</g>
<g transform="translate(180 320)">
  <path d="M-40-40h80v40h-80z" fill="#e8f0f6" class="o"/>
</g>''', ground=False)

add('toothpaste', 'チューブから歯みがき粉をしぼり出す', f'''
{table(330)}
<g transform="translate(240 240) rotate(-14)">
  <path d="M-130-40h180q20 0 20 40t-20 40h-180z" fill="#e8f0f6" class="o"/>
  <path d="M-130-40l-30 80h30z" fill="#c8d0d8" class="o"/>
  <path d="M50-20h30v40H50z" class="teal o"/>
  <path d="M-90-16h120v32h-120z" class="tealp"/>
</g>
<path d="M330 220q40 10 50 40" fill="none" stroke="#e8f0f6" stroke-width="20" stroke-linecap="round"/>
<path d="M330 220q40 10 50 40" fill="none" stroke="{TONES['teal'][0]}" stroke-width="2.5"/>
<g transform="translate(430 300) rotate(-10)">
  <path d="M-90-10h160q16 0 16 10t-16 10h-160q-12 0-12-10t12-10z" class="coral o"/>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="2">
''' + ''.join(f'<rect x="{20+i*20}" y="-30" width="14" height="22" rx="4"/>' for i in range(4)) + f'''
  </g>
</g>''', ground=False)

add('trousers', '二本の脚が分かれた長ズボン', f'''
{table(340)}
<g transform="translate(300 200)">
  <path d="M-80-90h160v50l-20 160h-56l-4-110-4 110h-56l-20-160z" class="bluep o"/>
  <path d="M-80-40h160" fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"/>
  <path d="M-80-90h160v-16h-160z" class="blue o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3">
    <path d="M-50-70h30v34h-30zM20-70h30v34H20z"/>
  </g>
  <circle cx="0" cy="-76" r="7" fill="{TONES['blue'][2]}"/>
</g>''', ground=False)

add('tulip', 'コップ形の花びらを持つチューリップが並ぶ', f'''
<path d="M0 0h600v300H0z" fill="#dceaf4"/>
<path d="M0 300h600v100H0z" fill="#c9d8c0"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g>
''' + ''.join(f'''<g transform="translate({120+i*90} 300)">
  <path d="M-7 0v-140h14V0z" class="greend o"/>
  <path d="M-7-70q-50-24-42-56 44 6 42 56zM7-100q50-24 60 6-44 24-60-6z" class="greenp o"/>
  <g transform="translate(0 -170)">
    <path d="M-34 0q0-40 34-40t34 40q0 40-34 40T-34 0z" fill="{[TONES['coral'][0], TONES['gold'][0], TONES['violet'][0], TONES['coral'][0], TONES['gold'][0]][i]}" class="o"/>
    <path d="M-34 0q10-30 34-30t34 30" fill="none" stroke="{[TONES['coral'][2], TONES['gold'][2], TONES['violet'][2], TONES['coral'][2], TONES['gold'][2]][i]}" stroke-width="4"/>
    <path d="M-12-26q12-14 24 0" fill="none" stroke="{[TONES['coral'][2], TONES['gold'][2], TONES['violet'][2], TONES['coral'][2], TONES['gold'][2]][i]}" stroke-width="4"/>
  </g>
</g>''' for i in range(5)) + f'''
</g>
{sun(520, 70, 30)}''', ground=False)

add('uncle', '家系図で親の兄弟にあたるおじの位置', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g fill="none" stroke="{BRN}" stroke-width="4">
  <path d="M300 90v30M170 120h260M170 120v40M430 120v40M300 210v40M240 250h120M240 250v30M360 250v30M170 210v40"/>
</g>
{head(300, 60, 24, 'gold', 'bun')}
{head(170, 190, 22, 'teal', 'short')}
{head(430, 190, 22, 'coral', 'bob')}
{head(240, 310, 19, 'green', 'cap')}
{head(360, 310, 19, 'violet', 'bob')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="10 8"><circle cx="170" cy="196" r="50"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['teal'][0]}"><path d="M60 320l70-80"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M430 250q-70 40-130 40"/></g>''', arrow=True, ground=False)

add('tailor', '仕立屋が体に合わせて服を仕立てる', f'''
{table(380)}
{person(420, 380, 1.15, 1, 'coral', 'blue', 'stand', 'bun', 'smile')}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5">
  <path d="M370 260q50 20 100 0"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="2">
''' + ''.join(f'<path d="M{376+i*18} 258v10"/>' for i in range(6)) + f'''
</g>
{person(160, 380, 1.05, -1, 'teal', 'teal', 'reach', 'short', 'neutral')}
<g transform="translate(230 250) rotate(20)">
  <g stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
    <path d="M-6-6l-60-22q-10-4-6-12t14-4L8-24z" fill="#cfd6dd"/>
    <path d="M-6 6l-60 22q-10 4-6 12t14 4L8 24z" fill="#8f9aa6"/>
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round">
    <path d="M12-12q30-12 42 4t-10 20"/><path d="M12 12q30 12 42-4t-10-20"/>
  </g>
</g>
<g transform="translate(90 300)">
  <path d="M-30-40h60v80h-60z" class="tealp o"/>
</g>''', ground=False)

add('trek', '重い荷を背負って山道を何日も歩く', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
<path d="M0 280l120-160 90 80 110-120 130 130 150-70v240H0z" fill="#9aa5b0" class="o"/>
<path d="M0 330h600v70H0z" fill="#c9d8c0"/>
<path d="M0 330h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="#fffefd" class="o"><path d="M320 100l-30 40h60z"/></g>
{person(220, 370, 1.1, 1, 'coral', 'green', 'walk', 'cap', 'neutral', 'walk')}
<g transform="translate(184 290)">
  <path d="M-34-50h68v86q0 14-34 14t-34-14z" class="teal o"/>
  <path d="M-34-50q34-16 68 0" fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"/>
</g>
<path d="M276 260v110" stroke="#a0764a" stroke-width="8" stroke-linecap="round" fill="none"/>
<g fill="{MUTED}">
''' + ''.join(f'<ellipse cx="{60+i*32}" cy="{384-(i%2)*10}" rx="9" ry="13" transform="rotate(12 {60+i*32} 380)"/>' for i in range(4)) + f'''
</g>
{sun(520, 70, 30)}''', ground=False)

add('thud', '重い本が床に落ちてドスンと鈍い音がする', f'''
{table(380)}
<g transform="translate(300 350) rotate(-8)">
  <path d="M-90-24h180v40h-180z" class="teal o"/>
  <path d="M-90-24h180v-8h-180z" fill="#fffdf6" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M160 320q-26 20-30 44M440 320q26 20 30 44M300 300v-30"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><path d="M300 100v190"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M120 360q-30 8-50 26M480 360q30 8 50 26"/>
</g>''', ground=False)

# --- 動詞 -------------------------------------------------------------------
add('straighten', '曲がった針金をまっすぐに伸ばす', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-90 40q30-70 60-20t50-60-40-40" fill="none" stroke="#8f9aa6" stroke-width="12" stroke-linecap="round"/>
</g>
<g transform="translate(450 250)">
  <path d="M-100 0h200" fill="none" stroke="#8f9aa6" stroke-width="12" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M330 250h240"/></g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('streamline', '曲がりくねった手続きを一直線に短くする', f'''
{split()}
{table(380)}
<g transform="translate(150 240)">
  <g class="a" marker-end="url(#ar)" stroke="{MUTED}" stroke-width="5">
    <path d="M-90-90q80 0 0 60t80 60 0 60h60"/>
  </g>
  <g fill="{MUTED}"><circle cx="-90" cy="-90" r="10"/><circle cx="-10" cy="-30" r="10"/><circle cx="-90" cy="30" r="10"/><circle cx="30" cy="90" r="10"/></g>
</g>
<g transform="translate(450 240)">
  <g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="6">
    <path d="M-100 0h200"/>
  </g>
  <g fill="{TONES['green'][0]}"><circle cx="-100" r="10"/><circle cx="0" r="10"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 340h60"/></g>''', ground=False)

add('subscribe', '毎月とどく雑誌を定期購読する', f'''
{table(380)}
<g transform="translate(180 240)">
  <path d="M-90-60h180v40h-180z" fill="#c9a464" class="o"/>
  <path d="M-90-20h180v90h-180z" fill="#d9b877" class="o"/>
  <path d="M-90-20q90 60 180 0" fill="none" stroke="#a0764a" stroke-width="4"/>
</g>
<g>
''' + ''.join(f'<g transform="translate({400+i*8} {180+i*54})">{doc(0, 0, 130, 46, 1)}</g>' for i in range(3)) + f'''
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M300 200h50M300 254h50M300 308h50"/></g>
<g transform="translate(300 110)">
  <circle r="34" fill="#fffdf6" class="o"/>
  <path d="M0 0v-22M0 0l14 10" stroke="{INK}" stroke-width="4" stroke-linecap="round" fill="none"/>
</g>''', ground=False)

add('substantiate', '主張のとなりに証拠の書類を並べて裏づける', f'''
{table(380)}
{person(120, 380, 1.0, 1, 'teal', 'blue', 'point', 'bun', 'neutral')}
<g transform="translate(240 160)">
  <path d="M-70-40h140q12 0 12 12v40q0 12-12 12h-96l-20 16v-16q-12 0-12-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  {word(0, 0, 5, 26, INK)}
</g>
<g>
''' + ''.join(f'<g transform="translate({420+ (i%2)*0} {200+i*90})">{doc(0, 0, 130, 76, 2)}{tick(46, 22, 0.3)}</g>' for i in range(2)) + f'''
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M330 220l-60-30"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M330 300l-70-100"/></g>''', ground=False)

add('supersede', '古い機種が新しい機種に置き換わる', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-90-70h180v130h-180z" fill="#c8b8a0" class="o"/>
  <path d="M-64-46h128v82h-128z" fill="#8f9aa6" class="o"/>
  <path d="M-40 60h80v30h-80z" fill="#a89880" class="o"/>
</g>
{cross(150, 250, 1.5)}
<g transform="translate(450 250)">
  <path d="M-110-70h220v130h-220z" fill="#3b4450" class="o"/>
  <path d="M-100-60h200v110h-200z" fill="#dceaf4"/>
  <path d="M-30 60h60v14h-60z" fill="#5a6270"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M270 130h60"/></g>''', ground=False)

add('supplant', 'いすに座っていた人を押しのけて別の人が座る', f'''
{table(380)}
{chair(300, 380, 1.1, 'gold', 1)}
{sit(300, 380, 1.1, 1, 'coral', 'blue', 'bun', 'smile', 'lap')}
<g opacity="0.4">{person(470, 380, 1.0, -1, 'blue', 'blue', 'walk', 'short', 'sad', 'walk')}</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M400 200h110"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['teal'][0]}" stroke-width="6"><path d="M150 200h100"/></g>
{person(110, 380, 0.9, 1, 'teal', 'blue', 'stand', 'cap', 'neutral')}''', ground=False)

add('surpass', '後から来た線が前の線を追い越して上に出る', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(300 230)">
  <path d="M-250 130h500v6h-500z" fill="{INK}"/>
  <path d="M-250-170v300h6v-300z" fill="{INK}"/>
  <path d="M-230 60l60-20 60-20 60-16 60-14" fill="none" stroke="{MUTED}" stroke-width="7" stroke-linejoin="round"/>
  <path d="M-230 120l60-40 60-60 60-50 60-40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linejoin="round"/>
  <circle cx="-70" cy="0" r="12" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M480 320v-130"/></g>''', ground=False)

add('symbolise', 'ハトの絵が平和という考えを表す', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <ellipse rx="60" ry="42" fill="#fffdf6" class="o"/>
  <circle cx="52" cy="-30" r="26" fill="#fffdf6" class="o"/>
  <path d="M74-36l24 8-24 10z" class="gold o"/>
  <circle cx="60" cy="-34" r="4" fill="{INK}"/>
  <path d="M-64 6l-30-18 32-10z" fill="#e8e2d6" class="o"/>
  <path d="M-14-14q40-22 60 6-36 26-60-6z" fill="#e8e2d6" class="o"/>
  <path d="M60-6q40 10 60-6" fill="none" stroke="{TONES['green'][2]}" stroke-width="5"/>
  <g class="greenp o"><ellipse cx="104" cy="-16" rx="16" ry="9" transform="rotate(-30 104 -16)"/></g>
</g>
<g transform="translate(450 250)">
  <path d="M-90-40h180v80h-180z" class="greenp o"/>
  {word(0, 0, 5, 30, TONES['green'][2])}
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('sympathise', '落ち込む相手の肩に手を置いて気持ちに寄り添う', f'''
{table(380)}
{sit(210, 380, 1.05, 1, 'blue', 'blue', 'bob', 'sad', 'down')}
{chair(210, 380, 1.0, 'gold', 1)}
{person(400, 380, 1.05, -1, 'coral', 'blue', 'reach', 'bun', 'neutral')}
<g>
  <path d="M340 260q-40-16-70-4" stroke="{SKINL}" stroke-width="26" stroke-linecap="round" fill="none"/>
  <path d="M340 260q-40-16-70-4" stroke="{SKIN}" stroke-width="21" stroke-linecap="round" fill="none"/>
</g>
<g fill="{TONES['blue'][0]}"><path d="M178 262q9 10 9 17t-9 8-9-8 9-17z"/></g>
<g fill="{TONES['coral'][0]}">
  <path d="M300 150q-14-20 0-28 14-6 18 10 4-16 18-10 14 8 0 28l-18 20z"/>
</g>''', ground=False)

add('tabulate', 'ばらばらの数字を行と列の表にまとめる', f'''
{split()}
{table(380)}
<g>
''' + ''.join(f'<g transform="translate({80+ (i%3)*70} {190+(i//3)*70}) rotate({-24+i*13})"><path d="M-30-18h60v36h-60z" class="paper"/><rect x="-20" y="-7" width="{40-(i%3)*10}" height="14" rx="7" fill="{MUTED}"/></g>' for i in range(6)) + f'''
</g>
<g transform="translate(450 240)">
  <path d="M-120-110h240v220h-240z" class="paper"/>
  <path d="M-120-110h240v46h-240z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5">
''' + ''.join(f'<path d="M-120 {-20+i*44}h240"/>' for i in range(3)) + f'''
    <path d="M-40-110v220M40-110v220"/>
  </g>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="{-104+ (i%3)*80}" y="{-52+(i//3)*44}" width="46" height="14" rx="7"/>' for i in range(9)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 240h60"/></g>''', arrow=True, ground=False)

add('thicken', 'さらさらのソースを煮つめてとろりと濃くする', f'''
{split()}
{table(340)}
<g transform="translate(150 260)">
  <path d="M-76-60h152l-14 90q-2 16-62 16t-62-16z" fill="#9aa5b0" class="o"/>
  <path d="M-68-20h136l-8 46q-2 12-60 12t-60-12z" fill="{TONES['gold'][1]}"/>
  <path d="M-68-20h136" stroke="{TONES['gold'][0]}" stroke-width="3" fill="none"/>
</g>
<g transform="translate(450 260)">
  <path d="M-76-60h152l-14 90q-2 16-62 16t-62-16z" fill="#9aa5b0" class="o"/>
  <path d="M-64 0h128l-6 30q-2 12-58 12t-58-12z" fill="{TONES['gold'][0]}"/>
  <path d="M-64 0q64 20 128 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"/>
</g>
{flame(450, 350, 0.35)}
<g class="a" marker-end="url(#ar)"><path d="M270 260h60"/></g>''', arrow=True, ground=False)

add('thwart', '転がってきた計画を手前でさえぎって止める', f'''
{table(380)}
<g transform="translate(160 250)">
  <circle r="46" class="coral o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"><circle r="26"/></g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M220 250h90"/></g>
<g transform="translate(360 250)">
  <path d="M-16-110h32v220h-32z" fill="#8f9aa6" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M320 200l-24-24M320 300l-24 24"/>
</g>
{person(500, 380, 0.95, -1, 'teal', 'blue', 'reach', 'cap', 'neutral')}''', ground=False)

add('toughen', '薄い板を厚く固くして強くする', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-100-10h200v20h-200z" fill="#c9a464" class="o"/>
  <path d="M-40 10q40 30 80 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="8 6"/>
</g>
<g transform="translate(450 250)">
  <path d="M-100-30h200v60h-200z" fill="#8b6437" class="o"/>
  <g fill="none" stroke="#6b4c28" stroke-width="3"><path d="M-100 0h200"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M450 150v40M450 350v-40"/>
</g>
{tick(560, 130, 0.5)}
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('transcribe', '録音を聞きながら文字に書き起こす', f'''
{table(380)}
<g transform="translate(140 250)">
  <path d="M-70-50h140v100h-140z" fill="#3b4450" class="o"/>
  <circle cx="-30" r="24" fill="#8f9aa6" class="o"/><circle cx="30" r="24" fill="#8f9aa6" class="o"/>
  <circle cx="-30" r="9" fill="{INK}"/><circle cx="30" r="9" fill="{INK}"/>
  <path d="M-30-24h60v-10h-60z" fill="#5a6270"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M230 200q26 30 0 60M266 176q40 52 0 108"/>
</g>
<g transform="translate(420 230) rotate(-4)">
  {doc(0, 0, 200, 240, 5)}
</g>
<g transform="translate(340 340) rotate(30)">
  <path d="M0-70l10 22v60h-20V-48z" class="teal o"/>
</g>''', ground=False)

add('truncate', '長すぎる棒の端を切り落として短くする', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-130-20h260v40h-260z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><path d="M200 180v140"/></g>
<g transform="translate(450 250)">
  <path d="M-130-20h180v40h-180z" class="tealp o"/>
  <path d="M50-20v40" stroke="{TONES['coral'][0]}" stroke-width="5" fill="none"/>
</g>
<g transform="translate(200 140) rotate(20)">
  <g stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
    <path d="M-6-6l-56-20q-10-4-6-12t14-4L8-24z" fill="#cfd6dd"/>
    <path d="M-6 6l-56 20q-10 4-6 12t14 4L8 24z" fill="#8f9aa6"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('typify', 'その集団の特徴をいちばんよく表す一つ', f'''
{table(380)}
<g>
''' + ''.join(f'<circle cx="{80+ (i%5)*54}" cy="{220+(i//5)*70}" r="24" class="tealp o"/>' for i in range(10)) + f'''
</g>
<g transform="translate(450 260)">
  <circle r="64" class="teal o"/>
  <circle r="84" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M300 140q80-40 130 20"/></g>''', ground=False)

add('uncover', 'かぶせてあった布を取って中身を明らかにする', f'''
{split()}
{table(380)}
<g transform="translate(150 260)">
  <path d="M-90 60q-20-100 90-100t90 100z" fill="#c8d0d8" class="o"/>
  <g fill="none" stroke="#a8b2bc" stroke-width="4"><path d="M-70 20q70 20 140 0"/></g>
</g>
<g transform="translate(450 300)">
  <path d="M-70-90h140v90h-140z" class="goldp o"/>
  <path d="M-70-90l16-20h140l-16 20z" fill="{TONES['gold'][1]}" class="o"/>
  <path d="M70-90l16-20v90l-16 20z" class="gold o"/>
</g>
<g transform="translate(500 160) rotate(24)">
  <path d="M-70 40q-16-50 20-60 50-14 100 4-10 50-60 60-40 6-60-4z" fill="#c8d0d8" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('underpin', '土台の柱が上の床を下から支える', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-200-40h400v50h-400z" fill="#c9a464" class="o"/>
  <g class="o"><rect x="-140" y="-90" width="70" height="50" class="tealp"/><rect x="-30" y="-100" width="70" height="60" class="coralp"/><rect x="80" y="-84" width="70" height="44" class="goldp"/></g>
</g>
<g fill="#8f9aa6" class="o">
''' + ''.join(f'<rect x="{170+i*90}" y="210" width="34" height="150"/>' for i in range(4)) + f'''
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5">
''' + ''.join(f'<path d="M{187+i*90} 340v-90"/>' for i in range(4)) + f'''
</g>''', ground=False)

add('reinterpret', '同じ絵を別の意味に読み直す', f'''
{split()}
{table(380)}
<g transform="translate(150 230)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <circle cy="-20" r="30" class="goldp o"/>
  <path d="M-50 60q40-70 90-20t50-40" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"/>
</g>
<g transform="translate(450 230)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <circle cy="-20" r="30" class="goldp o"/>
  <path d="M-50 60q40-70 90-20t50-40" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"/>
</g>
<g transform="translate(150 340)">
  <path d="M-70-24h140v48h-140z" fill="#fffefd" class="o"/>
  {word(0, 0, 3, 26, MUTED)}
</g>
<g transform="translate(450 340)">
  <path d="M-70-24h140v48h-140z" fill="#fffefd" class="o"/>
  {word(0, 0, 3, 26, TONES['coral'][0])}
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 230h60"/></g>''', arrow=True, ground=False)

add('presuppose', '答えを出す前に、正しいと決めてかかる', f'''
{table(380)}
{person(150, 380, 1.05, 1, 'teal', 'blue', 'think', 'bun', 'neutral')}
<g transform="translate(300 140)">
  <path d="M-90-50h180q14 0 14 14v50q0 14-14 14h-120l-26 20v-20q-14 0-14-14v-50q0-14 14-14z" fill="#fffefd" class="o"/>
  {word(-20, -10, 4, 28, INK)}
  {tick(60, 14, 0.35)}
</g>
<g transform="translate(440 300)">
  {doc(0, 0, 150, 170, 4)}
  <path d="M-56 70h112" stroke="{MUTED}" stroke-width="3" fill="none"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M330 220q60 30 70 70"/></g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}"><path d="M340 210q70 30 80 80"/></g>''', arrow=True, ground=False)

add('mismanage', '任された店の運営を誤って傾かせる', f'''
{split()}
{table(380)}
<g transform="translate(150 380)">
  <path d="M-80 0v-110h160V0z" fill="#fffdf6" class="o"/>
  <path d="M-92-110h184v-24h-184z" class="teal o"/>
  <path d="M-56-86h56v50h-56z" class="bluep o"/>
</g>
{tick(150, 130, 0.6)}
<g transform="translate(450 380) rotate(6)">
  <path d="M-80 0v-110h160V0z" fill="#e8e2d6" class="o"/>
  <path d="M-92-110h184v-24h-184z" fill="#9aa5b0" class="o"/>
  <path d="M-56-86h56v50h-56z" fill="#c8d0d8" class="o"/>
  <path d="M-40-70l40 30M0-70l-40 30" stroke="{TONES['coral'][0]}" stroke-width="4" fill="none"/>
</g>
{cross(450, 130, 0.6)}
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', ground=False)

add('ascribe', '作者不明だった絵を、この画家の作だと結びつける', f'''
{table(380)}
<g transform="translate(200 230)">
  <path d="M-110-110h220v220h-220z" fill="#fffdf6" class="o"/>
  <path d="M-90 80L-20-30l40 44 40-64 70 130z" class="greenp o"/>
  <circle cx="50" cy="-56" r="20" class="goldp o"/>
</g>
{head(470, 200, 34, 'violet', 'bun')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M330 250h90"/></g>
<g transform="translate(200 360)">
  <path d="M-60-16h120v32h-120z" fill="#fffefd" class="o"/>
  {word(0, 0, 3, 26, MUTED)}
</g>
<g transform="translate(470 320)">
  <path d="M-60-16h120v32h-120z" fill="#fffefd" class="o"/>
  {word(0, 0, 3, 26, INK)}
</g>''', ground=False)

# --- 形容詞・慣用表現 ---------------------------------------------------------
add('stylish', '飾り気のない服と、形も色も決まったおしゃれな服', f'''
{split()}
{table(380)}
{person(150, 380, 1.15, 1, 'blue', 'blue', 'stand', 'short', 'neutral')}
{person(450, 380, 1.15, 1, 'violet', 'gold', 'stand', 'bun', 'smile')}
<g transform="translate(450 250)">
  <path d="M-40-84q40-20 80 0l-6 30h-68z" class="violetd o"/>
  <circle cx="34" cy="-30" r="9" class="gold o"/>
</g>
<g transform="translate(450 224)">
  <path d="M-40-10h80v10h-80z" class="gold o"/>
  <path d="M-26-40h52v30h-52z" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M540 200l-24-18M552 260h-26"/>
</g>''', ground=False)

add('terrified', '目を見開き、口を開けてひどくおびえる', f'''
<g transform="translate(280 200)">
  <circle r="140" fill="{SKIN}" stroke="{SKINL}" stroke-width="4"/>
  <path d="M-96-56q30-26 56-8M40-64q30-16 56 8" fill="none" stroke="{HAIR}" stroke-width="8" stroke-linecap="round"/>
  <circle cx="-52" cy="-10" r="28" fill="#fffefd" class="o"/><circle cx="-52" cy="-10" r="12" fill="{INK}"/>
  <circle cx="52" cy="-10" r="28" fill="#fffefd" class="o"/><circle cx="52" cy="-10" r="12" fill="{INK}"/>
  <ellipse cy="76" rx="34" ry="40" fill="{INK}"/>
  <g fill="none" stroke="{SKINL}" stroke-width="3"><path d="M-110 30l-20-8M-106 60l-22 6M110 30l20-8M106 60l22 6"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M480 80l30-26M500 200h36M480 320l30 26M80 80L50 54M60 200H24"/>
</g>
<g fill="{TONES['blue'][0]}"><path d="M170 60q10 12 10 20t-10 8-10-8 10-20z"/><path d="M390 56q10 12 10 20t-10 8-10-8 10-20z"/></g>''', ground=False)

add('thankful', '両手を合わせてありがたく思う', f'''
<path d="M0 0h600v400H0z" fill="#fff6e0"/>
{table(380)}
{person(300, 380, 1.25, 1, 'coral', 'blue', 'hold', 'bun', 'smile')}
<g transform="translate(300 250)">
  <path d="M-34 10q34-40 68 0-34 26-68 0z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-30-6q30-34 60 0" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{300+150*math.cos(3.5+i*0.45):.0f} {220+150*math.sin(3.5+i*0.45):.0f}l{20*math.cos(3.5+i*0.45):.0f} {20*math.sin(3.5+i*0.45):.0f}"/>' for i in range(8)) + f'''
</g>
<g fill="{TONES['coral'][0]}">
  <path d="M300 130q-14-20 0-28 14-6 18 10 4-16 18-10 14 8 0 28l-18 20z"/>
</g>''', ground=False)

add('trendy', 'いま流行の形の服をみんなが着ている', f'''
{table(380)}
''' + ''.join(person(90+i*110, 380, 0.95, 1, 'violet', 'gold', 'stand', 'bun', 'smile') for i in range(5)) + f'''
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M300 130q26-24 52 0M300 130q-26-24-52 0"/>
</g>
<g transform="translate(300 90)">
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6">
    <path d="M-8-16v32M8-16v32M-18-6h36M-18 6h36"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M470 150l-120 60"/></g>''', ground=False)

add('such-as', '「果物」の例としてりんごとバナナを挙げる', f'''
{table(380)}
<g transform="translate(160 200)">
  <path d="M-90-40h180v80h-180z" class="tealp o"/>
  {word(0, 0, 4, 32, TONES['teal'][2])}
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h70"/></g>
<g transform="translate(400 180)"><circle r="42" class="coral o"/><path d="M0-42q-10-22 6-26 14 6 4 26z" class="greend o"/></g>
<g transform="translate(510 260)">
  <path d="M-40 20q-16-40 20-56 40-18 56 10-6 40-40 52-30 8-36-6z" class="gold o"/>
  <path d="M34-28l10-16" stroke="{TONES['gold'][2]}" stroke-width="6" stroke-linecap="round" fill="none"/>
</g>
<g transform="translate(390 300)">
  <path d="M-40 20q-16-40 20-56 40-18 56 10-6 40-40 52-30 8-36-6z" class="goldp o"/>
</g>''', arrow=True, ground=False)

add('take-part-in', 'みんなの輪に加わって一緒に活動する', f'''
{table(380)}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="12 10"><ellipse cx="330" cy="280" rx="160" ry="100"/></g>
{head(250, 240, 24, 'teal', 'short')}
{head(400, 235, 24, 'coral', 'bun')}
{head(240, 330, 24, 'gold', 'cap')}
{head(410, 330, 24, 'green', 'bob')}
{head(330, 285, 24, 'violet', 'short')}
{person(90, 380, 0.9, 1, 'blue', 'blue', 'walk', 'bob', 'smile', 'walk')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="6"><path d="M140 250h70"/></g>''', ground=False)

add('similar-to', '形は同じで色だけが違う二つ', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M0-90l80 140H-80z" class="teal o"/>
  <circle cy="20" r="20" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(450 250)">
  <path d="M0-90l80 140H-80z" class="coral o"/>
  <circle cy="20" r="20" fill="#fffdf6" class="o"/>
</g>
<g fill="{TONES['green'][0]}">
  <path d="M270 340q30-14 60 0" fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round"/>
  <path d="M270 366q30-14 60 0" fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round"/>
</g>''', ground=False)

add('trickle-down', '上の器からあふれた水が下の器へしたたり落ちる', f'''
{table(380)}
<g transform="translate(300 130)">
  <path d="M-70-40h140v50q0 14-70 14t-70-14z" class="goldp o"/>
  <ellipse cy="-40" rx="70" ry="16" fill="{TONES['blue'][1]}" class="o"/>
</g>
<g fill="{TONES['blue'][0]}">
  <path d="M240 200q10 12 10 20t-10 8-10-8 10-20z"/><path d="M360 210q9 11 9 18t-9 7-9-7 9-18z"/>
</g>
<g transform="translate(220 280)">
  <path d="M-50-30h100v40q0 12-50 12t-50-12z" class="tealp o"/>
  <ellipse cy="-30" rx="50" ry="12" fill="{TONES['blue'][1]}" class="o"/>
</g>
<g transform="translate(390 300)">
  <path d="M-44-26h88v34q0 10-44 10t-44-10z" class="violetp o"/>
  <ellipse cy="-26" rx="44" ry="10" fill="{TONES['blue'][1]}" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M500 140v200"/></g>''', arrow=True, ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
