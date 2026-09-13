# -*- coding: utf-8 -*-
"""第122回。身のまわりの物と、程度・様子の形容詞。形容詞は split() で左右比較。"""
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

# --- 物 ---------------------------------------------------------------------
add('lime', '緑のライムが半分に切られ、輪切りの断面が見えている', f'''
{table(320)}
<g transform="translate(200 250)">
  <ellipse rx="86" ry="76" class="green o"/>
  <path d="M0-76q-16-30 8-38 20 8 8 38z" class="greend o"/>
  <ellipse cx="-28" cy="-30" rx="20" ry="13" fill="#fffefd" opacity="0.5" transform="rotate(-30 -28 -30)"/>
</g>
<g transform="translate(400 250)">
  <circle r="82" class="green o"/>
  <circle r="70" fill="#dff0cf" class="o"/>
''' + ''.join(f'<path d="M0 0l{62*math.cos(i*0.785-0.35):.0f} {62*math.sin(i*0.785-0.35):.0f}A62 62 0 0 1 {62*math.cos(i*0.785+0.35):.0f} {62*math.sin(i*0.785+0.35):.0f}z" fill="#b6dc8e" stroke="#8fbf62" stroke-width="2"/>' for i in range(8)) + f'''
  <circle r="10" fill="#dff0cf" class="o"/>
</g>''', ground=False)

add('raspberry', 'つぶつぶが集まった赤いラズベリーの実', f'''
{table(320)}
<g transform="translate(300 250)">
  <g class="coral o">
''' + ''.join(f'<circle cx="{-52+ (i%5)*26}" cy="{-40+(i//5)*24}" r="17"/>' for i in range(10)) + f'''
''' + ''.join(f'<circle cx="{-40+i*26}" cy="10" r="16"/>' for i in range(4)) + f'''
''' + ''.join(f'<circle cx="{-26+i*26}" cy="40" r="14"/>' for i in range(3)) + f'''
    <circle cx="0" cy="66" r="12"/>
  </g>
  <g fill="{TONES['coral'][1]}" opacity="0.6">
''' + ''.join(f'<circle cx="{-56+ (i%5)*26}" cy="{-46+(i//5)*24}" r="5"/>' for i in range(10)) + f'''
  </g>
  <g class="green o">
    <path d="M-14-56q-46-14-56 8 34 22 56-8zM14-56q46-14 56 8-34 22-56-8zM0-64q-14-40 0-46 14 6 0 46z"/>
  </g>
</g>
<g class="coral o"><circle cx="470" cy="300" r="14"/><circle cx="500" cy="308" r="12"/></g>''', ground=False)

add('prawn', '殻とひげのついた大きなエビが皿の上にある', f'''
{table(320)}
<g transform="translate(300 254)">
  <ellipse rx="150" ry="34" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(290 220) rotate(-8)">
  <path d="M-90 20q-40-70 20-100 70-34 130 10 40 30 20 70-40 34-90 20z" class="coral o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="4">
    <path d="M-40-46q10 60 0 66M0-58q10 70 0 74M40-56q10 66 0 70"/>
  </g>
  <path d="M-90 20q-40 10-44 40 40 6 60-16z" class="corald o"/>
  <circle cx="86" cy="-38" r="6" fill="{INK}"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="3.5" stroke-linecap="round">
    <path d="M96-46q40-30 74-20M96-32q44-14 76 6"/>
  </g>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="4" stroke-linecap="round">
    <path d="M-30 34l-14 26M10 40l-8 28M50 36l6 28"/>
  </g>
</g>''', ground=False)

add('roast', 'オーブンで肉をこんがり焼いている', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<g transform="translate(300 220)">
  <path d="M-180-120h360v250h-360z" fill="#5a6270" class="o"/>
  <path d="M-150-90h300v190h-300z" fill="#2c333d" class="o"/>
  <path d="M-140-80h280v170h-280z" fill="#c8703a" opacity="0.4"/>
  <g fill="none" stroke="#9aa5b0" stroke-width="4"><path d="M-140 60h280"/></g>
  <g transform="translate(0 30)">
    <path d="M-80-30q60-40 140-10 26 30-10 52-70 20-120-8-16-22-10-34z" fill="#a8552c" class="o"/>
    <path d="M-56-24q50-26 106-4" fill="none" stroke="#7c3a1c" stroke-width="4"/>
    <g fill="#7c3a1c"><circle cx="-20" cy="8" r="6"/><circle cx="30" cy="14" r="5"/><circle cx="60" cy="0" r="5"/></g>
  </g>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{-110+i*44} -60v-16"/>' for i in range(6)) + f'''
  </g>
  <path d="M-180 130h360v20h-360z" fill="#8f9aa6" class="o"/>
  <g fill="{INK}"><circle cx="-120" cy="140" r="8"/><circle cx="-90" cy="140" r="8"/></g>
</g>''', ground=False)

add('radiator', '壁ぎわの暖房器が部屋を暖めている', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<path d="M0 330h600v70H0z" fill="#c9a464" class="o"/>
<g transform="translate(300 250)">
  <path d="M-170-90h340v170h-340z" fill="#e0e6ea" class="o"/>
  <g fill="#c8d0d8" class="o">
''' + ''.join(f'<rect x="{-152+i*34}" y="-74" width="22" height="138" rx="11"/>' for i in range(9)) + f'''
  </g>
  <path d="M-170-90h340v14h-340zM-170 66h340v14h-340z" fill="#b8bfc8" class="o"/>
  <path d="M-186 60h16v34h-16z" fill="#9aa5b0" class="o"/>
  <circle cx="182" cy="-40" r="18" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round" opacity="0.85">
''' + ''.join(f'<path d="M{160+i*56} 140q14-22 0-40t14-40"/>' for i in range(6)) + f'''
</g>''', ground=False)

add('ribbon', '包みに細長いリボンが結ばれて蝶結びになっている', f'''
{table(330)}
{box(300, 270, 200, 120, 34, 'teal')}
<g>
  <path d="M300 190v120M212 268h176" stroke="{TONES['coral'][0]}" stroke-width="20" fill="none"/>
</g>
<g transform="translate(300 194)">
  <path d="M-14 0q-70-46-84-6-10 34 40 32 30-2 44-26z" class="coral o"/>
  <path d="M14 0q70-46 84-6 10 34-40 32-30-2-44-26z" class="coral o"/>
  <path d="M-10 12q-24 50-56 60 42 8 62-46zM10 12q24 50 56 60-42 8-62-46z" class="corald o"/>
  <circle r="18" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 130l-120 50"/></g>''', arrow=True, ground=False)

add('sneaker', 'ひもを通した布地の運動靴', f'''
{table(320)}
<g transform="translate(290 274)">
  <path d="M-140 26q-16-46 6-60 40-26 60-56 20-30 56-16 40 16 70 34 40 24 66 34 26 12 22 40-6 26-46 26z" fill="#fffdf6" class="o"/>
  <path d="M-146 26h380q6 20-14 22h-354q-16-4-12-22z" fill="#c8d0d8" class="o"/>
  <path d="M-40-42q40-44 66-30t46 34q-44 22-112-4z" class="tealp o"/>
  <g stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round">
    <path d="M-16-48l50 28M4-64l50 28M24-80l50 30"/>
  </g>
  <g fill="{INK}"><circle cx="-14" cy="-46" r="4"/><circle cx="6" cy="-62" r="4"/><circle cx="26" cy="-78" r="4"/>
    <circle cx="36" cy="-18" r="4"/><circle cx="56" cy="-34" r="4"/><circle cx="76" cy="-48" r="4"/></g>
  <path d="M74-88q30-24 46 6-24 18-46-6z" fill="#fffdf6" class="o"/>
  <path d="M160-4q40-16 74 4" fill="none" stroke="{TONES['teal'][0]}" stroke-width="8"/>
</g>''', ground=False)

add('staircase', '手すりのついた階段が上へ続いている', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<g fill="#c9a464" class="o">
''' + ''.join(f'<path d="M{60+i*70} {370-i*46}h{540-i*70}v{46}h-{540-i*70}z"/>' for i in range(7)) + f'''
</g>
<g fill="none" stroke="#8b6437" stroke-width="3">
''' + ''.join(f'<path d="M{60+i*70} {370-i*46}h{540-i*70}"/>' for i in range(7)) + f'''
</g>
<g>
  <path d="M50 340L470 64" fill="none" stroke="{BRN}" stroke-width="12" stroke-linecap="round"/>
  <g stroke="{BRN}" stroke-width="8" stroke-linecap="round" fill="none">
''' + ''.join(f'<path d="M{70+i*66} {370-i*44}v-{72}"/>' for i in range(6)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 130q90-40 200-40"/></g>''', arrow=True, ground=False)

add('submarine', '海の中を潜水艦が潜望鏡を出して進んでいる', f'''
<path d="M0 0h600v90H0z" fill="#dceaf4"/>
<path d="M0 90h600v310H0z" fill="#4d7fa4"/>
<path d="M0 90h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="#6f9cbd" stroke-width="4"><path d="M40 150h140M400 200h160M100 320h180"/></g>
<g transform="translate(300 240)">
  <path d="M-200 0q0-46 90-46h180q60 0 90 46-30 46-90 46h-180q-90 0-90-46z" fill="#5a6270" class="o"/>
  <path d="M-40-46h80v-40h-80z" fill="#5a6270" class="o"/>
  <path d="M-6-86h12v-70h-12z" fill="#4a5560" class="o"/>
  <path d="M-6-156h34v14H-6z" fill="#4a5560" class="o"/>
  <g fill="{TONES['gold'][1]}" class="o">
    <circle cx="-100" r="15"/><circle cx="-40" r="15"/><circle cx="20" r="15"/><circle cx="80" r="15"/>
  </g>
  <path d="M170-30q30 30 0 60" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g fill="#fffefd" opacity="0.5">
  <circle cx="140" cy="200" r="9"/><circle cx="120" cy="170" r="7"/><circle cx="152" cy="150" r="5"/>
</g>
<g fill="#3a6182"><path d="M0 380h600v20H0z"/></g>''', ground=False)

add('toolbox', 'ふたを開けた道具箱に工具が並んでいる', f'''
{table(330)}
<g transform="translate(300 260)">
  <path d="M-140-20h280v90q0 14-16 14h-248q-16 0-16-14z" class="coral o"/>
  <path d="M-140-20h280v-30h-280z" class="corald o"/>
  <path d="M-40-50q0-24 40-24t40 24" fill="none" stroke="{INK}" stroke-width="8"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"><path d="M-140 30h280"/></g>
</g>
<g transform="translate(190 200) rotate(-16)">
  <path d="M-8-60h16v90h-16z" fill="#8f9aa6" class="o"/>
  <path d="M-24 30h32v34q0 10-16 10t-16-10z" fill="{INK}"/>
</g>
<g transform="translate(300 190) rotate(6)">
  <path d="M-40-10h80v20h-80z" fill="{INK}"/>
  <path d="M-40-24h-30l-16 34 16 34h30z" fill="#9aa5b0" class="o"/>
  <path d="M40-16h34v32H40z" fill="#8f9aa6" class="o"/>
</g>
<g transform="translate(400 200) rotate(22)">
  <path d="M-10-60h20v80h-20z" fill="#c9a464" class="o"/>
  <path d="M-34 20h48v40q0 10-24 10t-24-10z" fill="#8f9aa6" class="o"/>
</g>''', ground=False)

add('trolley', 'スーパーの買い物カートに品物を入れて押している', f'''
{table(340)}
<g transform="translate(300 260)">
  <path d="M-110 0h200l-26 70h-150z" fill="none" stroke="{INK}" stroke-width="5"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
''' + ''.join(f'<path d="M{-96+i*32} 4l-8 62"/>' for i in range(7)) + ''.join(f'<path d="M-106 {14+i*18}h192"/>' for i in range(3)) + f'''
  </g>
  <path d="M90 0l40-70h34" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <path d="M-100 70l-14 20M76 70l14 20" stroke="{INK}" stroke-width="5" fill="none"/>
  <circle cx="-114" cy="98" r="14" fill="{INK}"/><circle cx="90" cy="98" r="14" fill="{INK}"/>
  <g class="o">
    <rect x="-90" y="-40" width="56" height="42" class="coralp"/>
    <rect x="-24" y="-32" width="46" height="34" class="tealp"/>
    <circle cx="52" cy="-20" r="22" class="goldp"/>
  </g>
</g>
{person(140, 340, 0.95, 1, 'teal', 'blue', 'reach', 'bun', 'smile')}''', ground=False)

add('tutorial', '少人数で先生を囲んで教わっている', f'''
{table(360)}
<g transform="translate(300 290)">
  <ellipse rx="180" ry="46" fill="#c9a464" class="o"/>
</g>
{sit(150, 350, 0.85, 1, 'coral', 'blue', 'bob', 'smile', 'lap')}
{sit(450, 350, 0.85, -1, 'gold', 'green', 'short', 'smile', 'lap')}
{person(300, 300, 0.9, 1, 'teal', 'violet', 'point', 'bun', 'smile')}
<g transform="translate(300 190)">
  <path d="M-90-56h180v90h-180z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}"><rect x="-70" y="-40" width="90" height="9" rx="4.5"/><rect x="-70" y="-20" width="120" height="9" rx="4.5"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M-70 8h70"/></g>
</g>''', ground=False)

add('prefix', '語の前に un- がついて意味が反対になる', f'''
<g transform="translate(300 160)">
  <path d="M-150-50h300v100h-300z" class="paper"/>
  <rect x="-110" y="-16" width="200" height="24" rx="12" fill="{INK}"/>
</g>
<g transform="translate(300 300)">
  <path d="M-230-50h460v100h-460z" class="paper"/>
  <rect x="-190" y="-16" width="90" height="24" rx="12" class="coral"/>
  <rect x="-86" y="-16" width="200" height="24" rx="12" fill="{INK}"/>
  <path d="M-190 22h90" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 216v40"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M120 260l-40 40"/></g>''', arrow=True, ground=False)

add('pavement', '車道のわきの舗装された歩道を歩いている', f'''
<path d="M0 250h600v150H0z" fill="#6f7b88"/>
<g fill="none" stroke="#fffefd" stroke-width="6" stroke-dasharray="34 30"><path d="M0 330h600"/></g>
<path d="M0 210h600v50H0z" fill="#d6cec0" class="o"/>
<path d="M0 250h600v14H0z" fill="#b0a898"/>
<g fill="none" stroke="#b0a898" stroke-width="3">
''' + ''.join(f'<path d="M{50+i*70} 210v40"/>' for i in range(9)) + f'''
</g>
{person(220, 234, 0.72, 1, 'coral', 'blue', 'walk', 'bob', 'smile', 'walk')}
{person(380, 234, 0.72, -1, 'teal', 'violet', 'walk', 'short', 'smile', 'walk')}
<g fill="#dfe8d8"><path d="M0 150h600v60H0z"/></g>
<path d="M0 210h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
{tree(90, 210, 0.7)}
{tree(510, 210, 0.7)}
<g class="a" marker-end="url(#ar)"><path d="M120 110v70"/></g>''', arrow=True, ground=False)

add('shortcut', '遠回りの道と、原っぱを突っ切る近道が並んでいる', f'''
<path d="M0 0h600v400H0z" fill="#dfe8d8"/>
<path d="M90 340q0-190 210-190t210 190" fill="none" stroke="#8f9aa6" stroke-width="34"/>
<g fill="none" stroke="#fffefd" stroke-width="4" stroke-dasharray="22 20"><path d="M90 340q0-190 210-190t210 190"/></g>
<path d="M96 340h410" fill="none" stroke="#c9a464" stroke-width="20" stroke-dasharray="18 14"/>
<g fill="{TONES['green'][0]}" opacity="0.5">
''' + ''.join(f'<circle cx="{130+i*44}" cy="{300+(i%3)*20}" r="7"/>' for i in range(9)) + f'''
</g>
{person(96, 340, 0.85, 1, 'coral', 'blue', 'walk', 'bob', 'smile', 'walk')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M170 320h300"/></g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}" stroke-width="4"><path d="M140 250q40-90 160-84"/></g>''', arrow=True, ground=False)

add('nurse', '看護師が患者の腕に包帯を巻いている', f'''
{table(370)}
<g transform="translate(380 300)">
  <path d="M-140-40h280v70h-280z" fill="#fffdf6" class="o"/>
  <path d="M-140-40h280v-16h-280z" fill="{TONES['blue'][1]}" class="o"/>
  <path d="M-150 30v40M130 30v40" stroke="#8f9aa6" stroke-width="10" fill="none"/>
</g>
{sit(400, 300, 0.85, -1, 'gold', 'blue', 'short', 'sad', 'down')}
{person(180, 370, 1.0, 1, 'teal', 'teal', 'reach', 'bob', 'smile')}
<g transform="translate(180 246)">
  <path d="M-26-22h52v14h-52z" fill="#fffdf6" class="o"/>
  <path d="M-6-20h12v-10h-12z" class="coral"/>
</g>
<g>
  <path d="M240 250q50-16 90 6" stroke="{SKIN}" stroke-width="22" stroke-linecap="round" fill="none"/>
  <path d="M240 250q50-16 90 6" stroke="{SKINL}" stroke-width="2.5" fill="none"/>
  <g fill="none" stroke="#fffefd" stroke-width="9" stroke-linecap="round">
    <path d="M276 240l-6 22M292 240l-6 24M308 244l-6 22"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 170l-20 50"/></g>''', arrow=True, ground=False)

# --- 動作 -------------------------------------------------------------------
add('peek', 'カーテンのすきまから外をこっそりのぞいている', f'''
<path d="M0 0h600v400H0z" fill="#5b6a86"/>
<g>
  <path d="M0 0h250v400H0zM600 0H350v400h250z" class="violetd o"/>
  <g fill="none" stroke="{TONES['violet'][2]}" stroke-width="4">
''' + ''.join(f'<path d="M{20+i*40} 0v400"/>' for i in range(6)) + ''.join(f'<path d="M{370+i*40} 0v400"/>' for i in range(6)) + f'''
  </g>
</g>
<path d="M250 0h100v400H250z" fill="#dceaf4"/>
{sun(300, 90, 34)}
{tree(300, 330, 0.7)}
<g transform="translate(258 200)">
  <ellipse rx="42" ry="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <ellipse cx="10" rx="24" ry="24" fill="#fffefd" class="o"/>
  <circle cx="16" r="12" fill="{INK}"/>
  <path d="M-14-32q26-14 46-2" fill="none" stroke="{HAIR}" stroke-width="7" stroke-linecap="round"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 120l110 60"/></g>''', arrow=True, ground=False)

add('splash', '水たまりを踏んで水しぶきが飛び散る', f'''
<path d="M0 0h600v400H0z" fill="#cfd8e0"/>
{table(370)}
<g transform="translate(300 350)">
  <ellipse rx="170" ry="34" fill="{TONES['blue'][1]}" class="o"/>
  <ellipse rx="120" ry="20" fill="{TONES['blue'][0]}" opacity="0.4"/>
</g>
<g fill="{TONES['blue'][1]}" stroke="{TONES['blue'][0]}" stroke-width="2.5">
''' + ''.join(f'<ellipse cx="{300+140*math.cos(3.6+i*0.42):.0f}" cy="{330-90*abs(math.sin(0.5+i*0.42)):.0f}" rx="{16-abs(i-4)*2}" ry="{22-abs(i-4)*2}" transform="rotate({-70+i*20} {300+140*math.cos(3.6+i*0.42):.0f} {330-90*abs(math.sin(0.5+i*0.42)):.0f})"/>' for i in range(9)) + f'''
</g>
<g fill="{TONES['blue'][0]}">
  <circle cx="170" cy="200" r="9"/><circle cx="240" cy="150" r="7"/><circle cx="380" cy="140" r="8"/><circle cx="450" cy="196" r="9"/>
</g>
{person(300, 348, 1.0, 1, 'coral', 'blue', 'up', 'cap', 'smile', 'walk')}''', ground=False)

add('spend', '財布からお金を出して買い物の代金を払っている', f'''
{table(320)}
{person(160, 320, 1.0, 1, 'teal', 'blue', 'give', 'bob', 'smile')}
{person(470, 320, 1.0, -1, 'coral', 'violet', 'give', 'short', 'smile')}
<g transform="translate(230 250) rotate(-10)">
  <path d="M-46-30h92v60h-92z" fill="#a0764a" class="o"/>
  <path d="M-46-30h92v-10h-92z" fill="#8b6437"/>
  <circle cx="30" r="9" class="gold o"/>
</g>
<g transform="translate(330 236) rotate(8)">
  <path d="M-56-26h112v52h-112z" class="greenp o"/>
  <circle r="16" fill="none" stroke="{TONES['green'][2]}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="2.5"><path d="M-46-16h20M30 16h20"/></g>
</g>
{coin(390, 290, 17)}
{coin(420, 300, 15)}
<g class="a" marker-end="url(#ar)"><path d="M250 180q80-30 150 10"/></g>''', arrow=True, ground=False)

add('subdivide', '四つに分けた区画をさらに細かく分ける', f'''
{split()}
<g transform="translate(150 200)">
  <path d="M-110-110h220v220h-220z" fill="#e8f0e4" class="o"/>
  <path d="M0-110v220M-110 0h220" stroke="{INK}" stroke-width="4" fill="none"/>
</g>
<g transform="translate(450 200)">
  <path d="M-110-110h220v220h-220z" fill="#e8f0e4" class="o"/>
  <path d="M0-110v220M-110 0h220" stroke="{INK}" stroke-width="4" fill="none"/>
  <g stroke="{TONES['coral'][0]}" stroke-width="3" fill="none">
    <path d="M-55-110v220M55-110v220M-110-55h220M-110 55h220"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('instigate', 'ひとりが二人をあおって争いを起こさせる', f'''
{table(360)}
{person(180, 350, 1.0, 1, 'blue', 'blue', 'point', 'short', 'sad')}
{person(420, 350, 1.0, -1, 'gold', 'green', 'point', 'bun', 'sad')}
<g fill="{TONES['coral'][0]}">
  <path d="M280 200l24-20-8 26 30-8-24 22 24 22-30-8 8 26-24-20-24 20 8-26-30 8 24-22-24-22 30 8-8-26z"/>
</g>
{person(300, 350, 0.9, 1, 'violet', 'violet', 'up', 'cap', 'smile')}
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-linecap="round" stroke-dasharray="8 7">
  <path d="M270 270q-40-20-60-40M330 270q40-20 60-40"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['violet'][0]}"><path d="M300 130v40"/></g>''', arrow=True, ground=False)

add('resurface', '沈んでいた潜水士が水面に再び顔を出す', f'''
<path d="M0 0h600v170H0z" fill="#dceaf4"/>
<path d="M0 170h600v230H0z" fill="#5b8caa"/>
<path d="M0 170h600" stroke="{INK}" stroke-width="3" fill="none"/>
<g fill="none" stroke="#8fb8d4" stroke-width="4"><path d="M40 230h120M420 260h150"/></g>
<g transform="translate(300 150)">
  <circle cy="10" r="42" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-42-4q0-46 42-46t42 46q-22-22-42-22t-42 22z" fill="{HAIR}"/>
  <circle cx="-14" cy="10" r="4" fill="{INK}"/><circle cx="14" cy="10" r="4" fill="{INK}"/>
  <path d="M-12 26q12 12 24 0" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="none" stroke="#fffefd" stroke-width="4" opacity="0.9">
  <ellipse cx="300" cy="176" rx="70" ry="14"/><ellipse cx="300" cy="176" rx="110" ry="24"/>
</g>
<g fill="#fffefd" opacity="0.6">
  <circle cx="250" cy="250" r="10"/><circle cx="270" cy="300" r="8"/><circle cx="240" cy="340" r="6"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M440 330v-160"/></g>''', arrow=True, ground=False)

# --- 形容詞（左右比較・場面） ---------------------------------------------------
add('aimless', '的をねらう矢と、あてもなくさまよう足あと', f'''
{split()}
<g transform="translate(150 200)">
  <circle r="90" fill="#fffdf6" class="o"/>
  <circle r="66" class="coralp o"/><circle r="42" fill="#fffdf6" class="o"/><circle r="18" class="coral o"/>
  <path d="M-160-70L-10-6" stroke="{BRN}" stroke-width="7" fill="none"/>
  <path d="M-10-6l-30-4 10-16z" fill="{INK}"/>
</g>
<g transform="translate(450 200)">
  <g fill="{MUTED}">
''' + ''.join(f'<ellipse cx="{-90+i*24+ (0 if i%2 else 14)}" cy="{60-i*16+ (0 if i%3 else 20)}" rx="10" ry="15" transform="rotate({i*40} {-90+i*24}, {60-i*16})"/>' for i in range(9)) + f'''
  </g>
  <path d="M-100 80q40-60 20-90t40-50 30 60 40-40" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>
  <text>?</text>
  <path d="M40-110q0-24 22-24t22 24-22 20v14" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle cx="62" cy="-56" r="4.5" fill="{INK}"/>
</g>''', ground=False)

add('bleak', '木も家もない、灰色の風の吹く荒れ野', f'''
<path d="M0 0h600v230H0z" fill="#b6bcc2"/>
<path d="M0 230h600v170H0z" fill="#9a9d94" class="o"/>
<g fill="none" stroke="#868a80" stroke-width="4">
  <path d="M0 280q120-20 300 0t300-14M0 340q140-16 300 8t300-16"/>
</g>
<g>
  <path d="M240 240V120h10v120z" fill="#6f6f66" class="o"/>
  <g stroke="#6f6f66" stroke-width="6" stroke-linecap="round" fill="none">
    <path d="M245 170l-40-34M245 190l44-40"/>
  </g>
</g>
<g fill="none" stroke="#c8ccd0" stroke-width="4" stroke-linecap="round">
  <path d="M40 120q90-24 180 0t180-10M60 180q80-20 160 0"/>
</g>
<g fill="#868a80" class="o"><ellipse cx="440" cy="300" rx="30" ry="16"/><ellipse cx="120" cy="330" rx="24" ry="13"/></g>
<g fill="#7f8378"><path d="M400 240v-20h6v20zM412 240v-30h6v30z"/></g>''', ground=False)

add('eccentric', '普通の服の列に、傘とシルクハットの変わった人がいる', f'''
{table(360)}
''' + ''.join(person(90+i*100, 350, 0.9, 1, 'blue', 'blue', 'stand', 'short', 'neutral') for i in [0,1,3,4]) + f'''
{person(390, 350, 1.0, 1, 'violet', 'gold', 'hold', 'bun', 'smile')}
<g transform="translate(390 232)">
  <path d="M-40 0h80v10h-80z" fill="{INK}"/>
  <path d="M-24-56h48v56h-48z" fill="{INK}"/>
  <path d="M-24-40h48v10h-48z" class="coral"/>
</g>
<g transform="translate(452 250)">
  <path d="M-56 0q0-46 56-46t56 46q-16-14-32-14t-24 8q-14-12-30-8T-56 0z" class="gold o"/>
  <path d="M0 0v76q0 14 16 14" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <path d="M0-46v-14" stroke="{INK}" stroke-width="4" fill="none"/>
</g>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M340 190l-24-20M420 160l10-26"/>
</g>''', ground=False)

add('fitted', 'ぶかぶかの服と、体にぴったり合った服', f'''
{split()}
{person(150, 340, 1.1, 1, 'teal', 'blue', 'stand', 'short', 'sad')}
<g transform="translate(150 250)">
  <path d="M-70-40q70-26 140 0l-14 100h-112z" class="tealp o"/>
  <path d="M-70-40l-40 44M70-40l40 44" stroke="{TONES['teal'][1]}" stroke-width="26" stroke-linecap="round" fill="none"/>
</g>
{person(450, 340, 1.1, 1, 'coral', 'blue', 'stand', 'short', 'smile')}
<g transform="translate(450 260)">
  <path d="M-30-52q30-14 60 0l-8 84h-44z" class="coral o"/>
  <path d="M-28-46l-20 34M28-46l20 34" stroke="{TONES['coral'][0]}" stroke-width="13" stroke-linecap="round" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M400 240h-40"/></g>
<g class="a" marker-end="url(#ar)"><path d="M500 240h40"/></g>''', ground=False)

add('formidable', '小さな人の前に立ちはだかる巨大な相手', f'''
{table(360)}
<g transform="translate(410 360)">
  <path d="M-120 0v-190q0-70 120-70t120 70V0z" class="teald o" transform="scale(0.85 1)"/>
  <circle cx="0" cy="-286" r="60" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-58-300q6-56 58-56 50 0 56 56-28-24-56-14-26-20-58 14z" fill="{HAIR}"/>
  <circle cx="-22" cy="-292" r="5" fill="{INK}"/><circle cx="22" cy="-292" r="5" fill="{INK}"/>
  <path d="M-20-260h40" stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none"/>
  <path d="M-32-306q18-10 30 0M2-306q18-10 30 0" fill="none" stroke="{HAIR}" stroke-width="6" stroke-linecap="round"/>
  <path d="M-102-190l-40 100M102-190l40 100" stroke="{SKIN}" stroke-width="30" stroke-linecap="round" fill="none"/>
</g>
{person(150, 360, 0.85, 1, 'coral', 'blue', 'up', 'bob', 'sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M96 226l-22-16M204 220l22-18"/>
</g>
<g fill="{INK}" opacity="0.12"><path d="M240 360l150-260 170 260z"/></g>''', ground=False)

add('fruitful', '手をかけた木がたわわに実をつけている', f'''
<path d="M0 0h600v250H0z" fill="#dceaf4"/>
{table(360)}
<path d="M0 300h600v100H0z" fill="#dfe8d8"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 300)">
  <path d="M-24 0h48v-90h-48z" fill="{BRN}" class="o"/>
  <g class="greenp o">
    <circle cx="-90" cy="-150" r="62"/><circle cx="0" cy="-190" r="72"/><circle cx="90" cy="-150" r="62"/><circle cx="0" cy="-118" r="58"/>
  </g>
  <g class="coral o">
''' + ''.join(f'<circle cx="{-120+i*30}" cy="{-190+ (i%4)*32}" r="15"/>' for i in range(9)) + f'''
  </g>
</g>
<g class="coral o"><circle cx="130" cy="330" r="16"/><circle cx="170" cy="342" r="14"/><circle cx="450" cy="336" r="15"/></g>
{sun(510, 70, 32)}''', ground=False)

add('furtive', '肩ごしに人目を気にしながらこっそり物を隠す', f'''
{table(360)}
<g transform="translate(320 360)">
  <path d="M-70-100h140v100h-140z" fill="#8f9aa6" class="o"/>
</g>
{person(230, 360, 1.05, 1, 'violet', 'blue', 'hold', 'cap', 'neutral')}
<g transform="translate(268 254) rotate(-16)">
  <path d="M-36-24h72v48h-72z" class="gold o"/>
  <path d="M-36 0h72" fill="none" stroke="{TONES['gold'][2]}" stroke-width="3"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7">
  <path d="M270 200q60-40 130-30"/>
</g>
<g transform="translate(430 190)">
  <ellipse rx="34" ry="24" fill="#fffefd" class="o"/>
  <circle r="14" fill="{INK}"/>
</g>
<g fill="{INK}" opacity="0.18"><path d="M100 200h140v160H100z"/></g>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M186 232l-22-14M290 224l20-18"/>
</g>''', ground=False)

add('grim', '口を固く結び、眉をひそめた険しい表情', f'''
<g transform="translate(300 200)">
  <circle r="130" fill="{SKIN}" stroke="{SKINL}" stroke-width="4"/>
  <path d="M-88-46q40-26 66-6M88-46q-40-26-66-6" fill="none" stroke="{HAIR}" stroke-width="12" stroke-linecap="round"/>
  <circle cx="-46" cy="-6" r="9" fill="{INK}"/><circle cx="46" cy="-6" r="9" fill="{INK}"/>
  <path d="M-44 62h88" stroke="{INK}" stroke-width="10" stroke-linecap="round" fill="none"/>
  <path d="M-52 84q52-14 104 0" fill="none" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-20-72q-14-20-34-24M20-72q14-20 34-24" fill="none" stroke="{SKINL}" stroke-width="3"/>
</g>
<g fill="{INK}" opacity="0.12"><path d="M0 0h600v400H0z"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M90 130l-40-20M90 270l-40 20M510 130l40-20M510 270l40 20"/>
</g>''', ground=False)

add('joyful', '両手を上げて跳び上がり、心から喜んでいる', f'''
<path d="M0 0h600v400H0z" fill="#fff6e0"/>
{table(370)}
{person(300, 330, 1.25, 1, 'coral', 'gold', 'up', 'bun', 'smile')}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="6" stroke-linecap="round">
''' + ''.join(f'<path d="M{300+170*math.cos(i*0.785):.0f} {200+170*math.sin(i*0.785):.0f}l{26*math.cos(i*0.785):.0f} {26*math.sin(i*0.785):.0f}"/>' for i in range(8)) + f'''
</g>
<g class="o">
''' + ''.join(f'<circle cx="{110+i*80}" cy="{80+(i%3)*40}" r="11" class="{["coral","teal","violet","gold"][i%4]}"/>' for i in range(6)) + f'''
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3"><ellipse cx="300" cy="374" rx="56" ry="9"/></g>''', ground=False)

add('laborious', '重い石を汗をかきながら一つずつ積み上げている', f'''
{table(370)}
{person(220, 370, 1.1, 1, 'gold', 'blue', 'carry', 'short', 'sad')}
<g transform="translate(250 268)">
  <path d="M-50-34h100v68h-100z" fill="#9aa5b0" class="o"/>
  <g fill="none" stroke="#7d8894" stroke-width="3"><path d="M-50 0h100M0-34v68"/></g>
</g>
<g fill="{TONES['blue'][0]}">
  <path d="M186 210q9 10 9 17t-9 8-9-8 9-17z"/><path d="M172 252q8 9 8 15t-8 7-8-7 8-15z"/>
</g>
<g transform="translate(450 300)">
  <g fill="#9aa5b0" class="o">
    <rect x="-70" y="30" width="70" height="40"/><rect x="4" y="30" width="70" height="40"/>
    <rect x="-34" y="-14" width="70" height="40"/><rect x="-70" y="-14" width="32" height="40"/><rect x="40" y="-14" width="32" height="40"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M320 240q70-30 96 20"/></g>''', arrow=True, ground=False)

add('lofty', 'はるか高くそびえる塔を見上げている', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
{table(370)}
<g transform="translate(340 370)">
  <path d="M-90 0l30-330h120L90 0z" fill="#e0d6c0" class="o"/>
  <g fill="{TONES['blue'][1]}" class="o">
''' + ''.join(f'<rect x="{-30+ (i%2)*30}" y="{-300+i*44}" width="24" height="34" rx="12"/>' for i in range(6)) + f'''
  </g>
  <path d="M-64-330h128l-64-56z" class="coral o"/>
  <path d="M0-386v-40" stroke="{INK}" stroke-width="5" fill="none"/>
  <path d="M0-426h40l-10 14 10 14H0z" class="gold o"/>
</g>
<g fill="#c9d8e4" opacity="0.7"><ellipse cx="180" cy="130" rx="90" ry="26"/><ellipse cx="470" cy="180" rx="80" ry="22"/></g>
{person(110, 370, 0.85, -1, 'teal', 'blue', 'up', 'bob', 'surprised')}
<g class="a" marker-end="url(#ar)"><path d="M180 300v-230"/></g>''', arrow=True, ground=False)

add('mountainous', '見わたすかぎり山が連なっている', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
<path d="M0 260l90-100 80 70 90-110 100 120 90-90 150 110v140H0z" fill="#b0bac4" class="o"/>
<path d="M0 320l110-90 90 70 110-90 120 100 170-70v160H0z" fill="#8f9aa6" class="o"/>
<g fill="#fffefd" class="o">
  <path d="M90 160l-30 42h60zM260 120l-32 44h64zM450 170l-30 42h60z"/>
</g>
<path d="M0 380h600v20H0z" fill="#6f7b88"/>
{sun(520, 70, 30)}
<g fill="none" stroke="#c9d8e4" stroke-width="4"><path d="M40 120q70-16 140 0M330 90q80-16 150 0"/></g>''', ground=False)

add('populous', '広場が人でびっしり埋まっている', f'''
{table(380)}
<g>
''' + ''.join(person(40+ (i%9)*68, 200+ (i//9)*62, 0.42, 1 if i%2 else -1, ['teal','coral','gold','violet','blue','green'][i%6], ['blue','violet','green','blue','coral','gold'][i%6], 'stand', ['short','bob','bun','cap'][i%4], 'smile') for i in range(27)) + f'''
</g>
<g fill="{INK}" opacity="0.06"><path d="M0 180h600v220H0z"/></g>''', ground=False)

add('porous', 'スポンジが穴だらけで水を吸い込む', f'''
{table(340)}
<g transform="translate(300 250)">
  <path d="M-150-70h300v130h-300z" class="goldp o"/>
  <g fill="#e8d8a8">
''' + ''.join(f'<circle cx="{-128+ (i%9)*32}" cy="{-48+(i//9)*36}" r="{9+(i%4)*3}"/>' for i in range(27)) + f'''
  </g>
</g>
<g fill="{TONES['blue'][0]}">
''' + ''.join(f'<path d="M{200+i*40} 130q9 10 9 17t-9 8-9-8 9-17z"/>' for i in range(6)) + f'''
</g>
<g fill="{TONES['blue'][1]}" opacity="0.7"><path d="M150 250h300v60H150z"/></g>
<g class="a" marker-end="url(#ar)"><path d="M300 170v40"/></g>''', arrow=True, ground=False)

add('potent', '一滴だけで色が大きく変わる強い薬', f'''
{table(340)}
<g transform="translate(180 210)">
  <path d="M-24-70h48v40l24 60q4 10-6 10h-84q-10 0-6-10l24-60z" fill="#e8f0f6" class="o"/>
  <path d="M-24-70h48v-14h-48z" class="coral o"/>
  <path d="M-34 24h68l6 16q4 10-6 10h-68q-10 0-6-10z" class="corald"/>
</g>
<g fill="{TONES['coral'][0]}"><path d="M180 260q10 12 10 20t-10 8-10-8 10-20z"/></g>
<g transform="translate(400 260)">
  <path d="M-70-90h140l-20 120q-2 16-50 16t-50-16z" fill="#e8f0f6" class="o"/>
  <path d="M-58-30h116l-12 62q-2 12-46 12t-46-12z" class="corald"/>
  <path d="M-58-30h116" stroke="{TONES['coral'][2]}" stroke-width="3" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 220q70-20 100 10"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M480 130l24-20M500 190l30-4M470 240l26 24"/>
</g>''', arrow=True, ground=False)

add('prehistoric', '文字の記録がない時代、洞窟の壁に絵が描かれている', f'''
<path d="M0 0h600v400H0z" fill="#5b4a3c"/>
<path d="M0 0h600v400H0z" fill="none"/>
<g fill="#7a6450">
  <path d="M0 0h600v400H0z"/>
  <path d="M60 40q120-30 240 0t240-10" fill="none" stroke="#6b573f" stroke-width="6"/>
</g>
<g fill="#a8552c" class="o">
  <path d="M120 240q-20-60 40-70 70-12 90 30 40-10 50 20 6 40-40 46-90 10-140-26z"/>
  <path d="M150 246l-14 60M200 254l-6 54M260 250l14 56M300 236l24 50"/>
  <path d="M250 200q30-40 60-30-10 40-60 30z"/>
</g>
<g fill="none" stroke="#a8552c" stroke-width="10" stroke-linecap="round">
  <path d="M150 246l-14 60M200 254l-6 54M256 252l14 54M296 240l24 50"/>
</g>
<g fill="#6b3f22">
  <path d="M420 180q40-30 70 0 20 30-20 40-46 6-50-40z"/>
  <path d="M430 218l-10 50M470 224l6 46"/>
</g>
<g fill="none" stroke="#6b3f22" stroke-width="8" stroke-linecap="round"><path d="M430 218l-10 50M470 224l6 46"/></g>
<g fill="#c8703a">
''' + ''.join(f'<ellipse cx="{80+i*34}" cy="340" rx="14" ry="20" transform="rotate({-10+i*6} {80+i*34} 340)"/>' for i in range(6)) + f'''
</g>
<g fill="none" stroke="#3f3128" stroke-width="6" opacity="0.5">
  <path d="M0 60q80 40 40 120t20 180M600 40q-70 60-30 140t-30 180"/>
</g>''', ground=False)

add('scarce', 'たっぷりある棚と、ほとんど空の棚', f'''
{split()}
<g transform="translate(150 200)">
  <path d="M-110-140h220v280h-220z" fill="#e0d6c0" class="o"/>
  <g fill="none" stroke="{BRN}" stroke-width="6"><path d="M-110-60h220M-110 20h220M-110 100h220"/></g>
  <g class="o">
''' + ''.join(f'<rect x="{-96+ (i%5)*42}" y="{-114+(i//5)*80}" width="30" height="50" class="{["coralp","tealp","goldp","violetp","greenp"][i%5]}"/>' for i in range(15)) + f'''
  </g>
</g>
<g transform="translate(450 200)">
  <path d="M-110-140h220v280h-220z" fill="#e0d6c0" class="o"/>
  <g fill="none" stroke="{BRN}" stroke-width="6"><path d="M-110-60h220M-110 20h220M-110 100h220"/></g>
  <rect x="-96" y="-114" width="30" height="50" class="coralp o"/>
  <rect x="60" y="-34" width="30" height="50" class="tealp o"/>
</g>''', ground=False)

add('seamless', '継ぎ目のある布と、継ぎ目のない一枚布', f'''
{split()}
<g transform="translate(150 200)">
  <path d="M-110-120h110v240h-110z" class="tealp o"/>
  <path d="M0-120h110v240H0z" class="tealp o"/>
  <path d="M0-120v240" stroke="{INK}" stroke-width="4" fill="none"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
''' + ''.join(f'<path d="M-8 {-108+i*26}h16"/>' for i in range(9)) + f'''
  </g>
</g>
<g transform="translate(450 200)">
  <path d="M-110-120h220v240h-220z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3" opacity="0.5">
    <path d="M-110-60h220M-110 0h220M-110 60h220"/>
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M120 350l60 30M180 350l-60 30"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">
  <path d="M420 366l24 24 46-54"/>
</g>''', ground=False)

add('secluded', '林の奥に、人目につかない小さな家がひっそりある', f'''
<path d="M0 0h600v250H0z" fill="#cfe0d4"/>
<path d="M0 250h600v150H0z" fill="#c9d8c0"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
{building(300, 280, 0.7, 'coral')}
''' + ''.join(tree(30+i*70, 300+(i%3)*20, 1.1+(i%3)*0.2) for i in range(9)) + f'''
''' + ''.join(tree(60+i*90, 250, 0.9) for i in range(7)) + f'''
<g fill="{TONES['green'][2]}" opacity="0.14"><path d="M0 0h600v400H0z"/></g>
<g class="a" marker-end="url(#ar)"><path d="M120 80q100 60 160 130"/></g>''', arrow=True, ground=False)

add('shrill', 'ホイッスルが甲高い音を突き刺すように鳴らす', f'''
{table(370)}
<g transform="translate(200 200) rotate(-14)">
  <path d="M-70-30h110q30 0 30 30t-30 30H-70q-16 0-16-30t16-30z" fill="#c8d0d8" class="o"/>
  <path d="M-86-14h-40v28h40z" fill="#9aa5b0" class="o"/>
  <circle cx="10" cy="-12" r="10" fill="{INK}"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-linecap="round">
''' + ''.join(f'<path d="M{300+i*44} {200-70-i*20}L{310+i*44} {200+70+i*20}" stroke-width="{6-i}"/>' for i in range(5)) + f'''
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M300 120q60 80 0 160M340 96q76 104 0 208"/>
</g>
{person(520, 370, 0.9, -1, 'teal', 'blue', 'up', 'bob', 'sad')}
<g fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5">
  <ellipse cx="496" cy="256" rx="15" ry="19"/><ellipse cx="544" cy="256" rx="15" ry="19"/>
</g>''', ground=False)

add('smug', '腕を組んでひとりよがりに得意げな顔をしている', f'''
{table(370)}
{person(300, 370, 1.3, 1, 'violet', 'blue', 'hold', 'short', 'smile')}
<g transform="translate(300 258)">
  <path d="M-60 0q60-24 120 0" stroke="{SKIN}" stroke-width="20" stroke-linecap="round" fill="none"/>
  <path d="M-50 18q56-20 108 0" stroke="{SKIN}" stroke-width="18" stroke-linecap="round" fill="none"/>
  <path d="M-60 0q60-24 120 0M-50 18q56-20 108 0" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g transform="translate(300 226)">
  <path d="M-14 6q22 12 42-4" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <path d="M-24-16q14-10 26 0M14-16q14-10 26 0" fill="none" stroke="{HAIR}" stroke-width="5" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M400 170l24-18M420 220l30-6M180 170l-24-18M160 220l-30-6"/>
</g>''', ground=False)

add('soggy', '水を吸ってべちゃべちゃになったパンが崩れる', f'''
{table(330)}
<g transform="translate(180 250)">
  <path d="M-70-40h140v70q0 12-70 12t-70-12z" fill="#e8c98d" class="o"/>
  <path d="M-70-40q0-30 70-30t70 30z" fill="#f0dcae" class="o"/>
  <g fill="none" stroke="#c9a464" stroke-width="3"><path d="M-50-14h100M-46 12h92"/></g>
</g>
<g transform="translate(420 270)">
  <path d="M-80-24q40-30 90-10 50 20 60 44-20 26-90 24t-70-26 10-32z" fill="#c8b070" class="o"/>
  <g fill="#a8905a"><ellipse cx="-30" cy="6" rx="20" ry="10"/><ellipse cx="34" cy="16" rx="18" ry="9"/></g>
  <path d="M-80 20q60 26 150 8" fill="none" stroke="#a8905a" stroke-width="4"/>
</g>
<g fill="{TONES['blue'][0]}">
  <path d="M290 200q10 12 10 20t-10 8-10-8 10-20z"/><path d="M320 240q9 11 9 18t-9 7-9-7 9-18z"/>
</g>
<g fill="{TONES['blue'][1]}" opacity="0.8"><ellipse cx="420" cy="316" rx="110" ry="16"/></g>
<g class="a" marker-end="url(#ar)"><path d="M270 160q70-30 110 20"/></g>''', arrow=True, ground=False)

add('tedious', '同じ書類に延々と判を押し続けてうんざりしている', f'''
{table(330)}
{sit(180, 330, 1.0, 1, 'blue', 'blue', 'short', 'sad', 'lap')}
{chair(180, 330, 0.95, 'gold', 1)}
<g>
''' + ''.join(f'<g transform="translate({300+ (i%5)*54} {250+(i//5)*26})"><path d="M-26-34h52v68h-52z" class="paper"/><g fill="{MUTED}"><rect x="-18" y="-22" width="36" height="6" rx="3"/><rect x="-18" y="-8" width="28" height="6" rx="3"/></g><circle cx="8" cy="16" r="8" class="coral"/></g>' for i in range(10)) + f'''
</g>
<g transform="translate(260 210) rotate(10)">
  <path d="M-20-40h40v40h-40z" fill="#8b6437" class="o"/>
  <path d="M-30 0h60v16h-60z" fill="{INK}"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M130 200q-14-16 0-30M110 240l-24-8"/>
</g>
<g transform="translate(170 170)">
  <path d="M-30-26h60q10 0 10 10v26q0 10-10 10h-40l-16 14v-14q-14 0-14-10v-26q0-10 10-10z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}"><circle cx="-12" cy="-2" r="4"/><circle cx="0" cy="-2" r="4"/><circle cx="12" cy="-2" r="4"/></g>
</g>''', ground=False)

add('thrifty', '小銭を貯金箱に入れてこつこつためている', f'''
{table(330)}
<g transform="translate(320 250)">
  <ellipse rx="100" ry="70" class="coralp o"/>
  <circle cx="82" cy="-16" r="42" class="coralp o"/>
  <ellipse cx="118" cy="-8" rx="20" ry="16" class="coral o"/>
  <circle cx="112" cy="-12" r="3.5" fill="{INK}"/><circle cx="124" cy="-12" r="3.5" fill="{INK}"/>
  <circle cx="70" cy="-30" r="4" fill="{INK}"/>
  <path d="M60-46q-14-30 4-32 14 6 8 32z" class="coral o"/>
  <path d="M-90 10q-40 4-30 34 30 6 34-20z" class="coral o"/>
  <g stroke="{TONES['coral'][2]}" stroke-width="14" stroke-linecap="round" fill="none">
    <path d="M-50 66v20M20 68v20M70 60v20"/>
  </g>
  <path d="M-24-64h48v10h-48z" fill="{INK}"/>
</g>
{coin(300, 130, 22)}
{coin(200, 240, 18)}
{coin(170, 290, 16)}
<g class="a" marker-end="url(#ar)"><path d="M300 156v22"/></g>''', arrow=True, ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
