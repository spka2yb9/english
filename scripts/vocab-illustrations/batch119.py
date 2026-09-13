# -*- coding: utf-8 -*-
"""第119回。植物・地形・天気。植物は葉と幹の形で、地形は横から見た断面で描き分ける。"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib import *

W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))
GR='#dfe8d8'; SKY='#dceaf4'; BRN='#8b6437'
def land(y=300, fill=GR):
    return f'<path d="M0 {y}h600v{400-y}H0z" fill="{fill}"/><path d="M0 {y}h600" stroke="{INK}" stroke-width="2.5" fill="none"/>'
def sky():
    return f'<path d="M0 0h600v400H0z" fill="{SKY}"/>'

# --- 木と植物 ---------------------------------------------------------------
add('oak', 'どっしりした幹と丸い樹冠を持つカシの木、足元にどんぐり', f'''
{land(310)}
<g transform="translate(300 310)">
  <path d="M-30 0q6-90-14-130 24 10 30 40 8-40 32-52-16 34-10 62 10-30 34-38-22 30-16 58 8 92 4 60z" fill="{BRN}" class="o"/>
  <path d="M-30 0h60v-40h-60z" fill="{BRN}"/>
  <g class="greenp o">
    <circle cx="-70" cy="-150" r="56"/><circle cx="10" cy="-186" r="66"/>
    <circle cx="80" cy="-146" r="54"/><circle cx="-24" cy="-116" r="50"/><circle cx="48" cy="-104" r="44"/>
  </g>
</g>
<g transform="translate(160 292)">
  <ellipse ry="20" rx="14" fill="#c9a464" class="o"/>
  <path d="M-14-16h28v-12h-28z" fill="{BRN}" class="o"/>
</g>''', ground=False)

add('pine', '先のとがった三角形の樹形と細い葉を持つマツ', f'''
{land(312)}
<g transform="translate(300 312)">
  <path d="M-16 0h32v-56h-32z" fill="{BRN}" class="o"/>
  <g class="greend o">
    <path d="M0-240l-40 60h80zM0-206l-58 68h116zM0-166l-76 78h152zM0-120l-92 82h184z"/>
  </g>
</g>
<g transform="translate(474 296)">
  <ellipse ry="26" rx="16" fill="#a0764a" class="o"/>
  <g stroke="#7a5b3c" stroke-width="2.5" fill="none">
    <path d="M-16-8h32M-16 4h32M-16 16h32"/>
  </g>
</g>''', ground=False)

add('maple', '五つに分かれた手のひら形の葉を持つカエデが赤く色づいている', f'''
{land(310)}
<g transform="translate(300 310)">
  <path d="M-14 0h28v-70h-28z" fill="{BRN}" class="o"/>
  <g stroke="{BRN}" stroke-width="9" stroke-linecap="round" fill="none">
    <path d="M0-70l-50-40M0-70l50-40M0-90v-40"/>
  </g>
  <g class="coral o">
    <circle cx="-62" cy="-130" r="46"/><circle cx="6" cy="-166" r="54"/><circle cx="66" cy="-126" r="44"/>
  </g>
</g>
<g transform="translate(462 250) scale(1.5)">
  <path d="M0-30l10 14 18-8-8 18 16 6-18 10 8 16-20-6-6 20-6-20-20 6 8-16-18-10 16-6-8-18 18 8z" class="corald o"/>
  <path d="M0 6v24" stroke="{BRN}" stroke-width="3" fill="none"/>
</g>''', ground=False)

add('birch', '白い樹皮に黒い横線が入ったシラカバが並んでいる', f'''
{land(312)}
<g>
  <path d="M180 312V80h34v232zM280 312V60h30v252zM380 312V96h32v216z" fill="#f6f2e4" class="o"/>
  <g fill="{INK}">
''' + ''.join(f'<path d="M182 {110+i*36}h20v7h-20z"/><path d="M282 {94+i*36}h18v7h-18z"/><path d="M382 {122+i*36}h20v7h-20z"/>' for i in range(5)) + f'''
  </g>
</g>
<g class="greenp o">
  <ellipse cx="200" cy="70" rx="52" ry="34"/><ellipse cx="296" cy="48" rx="58" ry="36"/><ellipse cx="398" cy="84" rx="50" ry="32"/>
</g>''', ground=False)

add('willow', '細い枝が水辺に長く垂れ下がったヤナギ', f'''
<path d="M0 300h600v100H0z" fill="#cfe0ec"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(290 300)">
  <path d="M-18 0h36v-110h-36z" fill="{BRN}" class="o"/>
  <ellipse cy="-146" rx="120" ry="52" class="greenp o"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{-110+i*22} -128q{-8+i} 70 {4-i*0.4:.0f} {96+ (i%3)*24}"/>' for i in range(11)) + f'''
  </g>
</g>''', ground=False)

add('bamboo', '節のある緑の茎がまっすぐ伸びる竹', f'''
{land(316)}
<g>
''' + ''.join(f'<g><path d="M{200+i*70} 316V{60+i*20}h30v{256-i*20}z" class="green o"/>' + ''.join(f'<path d="M{200+i*70} {100+j*54}h30" stroke="{TONES["green"][2]}" stroke-width="5" fill="none"/>' for j in range(4)) + '</g>' for i in range(3)) + f'''
</g>
<g class="greend o">
  <path d="M230 128q-50-20-70 6 44 20 70-6zM260 182q52-22 72 4-46 22-72-4z"/>
  <path d="M300 96q-50-20-70 6 44 20 70-6zM370 160q52-22 72 4-46 22-72-4z"/>
  <path d="M370 118q-50-20-70 6 44 20 70-6z"/>
</g>''', ground=False)

add('cactus', 'とげにおおわれた腕のあるサボテンが砂漠に立っている', f'''
<path d="M0 306h600v94H0z" fill="#f0dfb8"/>
<path d="M0 306h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 306)">
  <path d="M-30 0h60v-190q0-30-30-30t-30 30z" class="green o"/>
  <path d="M-30-110q-56 0-56 46 0 40 32 40v-46q0-18 24-18z" class="green o"/>
  <path d="M30-140q56 0 56 46 0 40-32 40v-46q0-18-24-18z" class="green o"/>
  <g stroke="{TONES['green'][2]}" stroke-width="3" fill="none">
    <path d="M-12-200v190M12-200v190"/>
  </g>
  <g stroke="{INK}" stroke-width="2.5" stroke-linecap="round" fill="none">
''' + ''.join(f'<path d="M-30 {-30-i*32}l-10-6M30 {-30-i*32}l10-6"/>' for i in range(6)) + f'''
  </g>
  <circle cx="0" cy="-216" r="14" class="coral o"/>
</g>''', ground=False)

add('fern', '細かく切れ込んだ葉が弧を描いて広がるシダ', f'''
{land(310)}
<g transform="translate(300 310)">
''' + ''.join(f'''<g transform="rotate({-56+i*23})">
  <path d="M0 0q-6-100 0-170" fill="none" stroke="{TONES['green'][2]}" stroke-width="6" stroke-linecap="round"/>
  ''' + ''.join(f'<path d="M-1 {-30-j*22}q-22-6-30-18M1 {-30-j*22}q22-6 30-18" fill="none" stroke="{TONES["green"][0]}" stroke-width="4.5" stroke-linecap="round"/>' for j in range(6)) + '</g>' for i in range(5)) + f'''
</g>''', ground=False)

add('moss', '石の上に厚くふかふかと生えたコケ', f'''
{land(320)}
<g>
  <path d="M140 320q-20-120 160-120t160 120z" fill="#b8bfc8" class="o"/>
  <path d="M180 236q60-40 140-20" fill="none" stroke="#9aa3ad" stroke-width="6"/>
</g>
<g class="green o">
  <path d="M150 288q40-40 90-16 40-34 90-8 44-28 84 4 30 22 22 52H144q-14-20 6-32z"/>
</g>
<g fill="{TONES['green'][2]}">
  <circle cx="200" cy="272" r="9"/><circle cx="256" cy="256" r="8"/><circle cx="316" cy="262" r="9"/>
  <circle cx="376" cy="252" r="8"/><circle cx="424" cy="272" r="9"/><circle cx="284" cy="288" r="7"/>
</g>
<g stroke="{TONES['green'][2]}" stroke-width="3" stroke-linecap="round" fill="none">
  <path d="M212 262v-22M300 250v-24M392 244v-22"/>
</g>''', ground=False)

add('vine', 'つるが壁をはい上がって葉を広げている', f'''
<path d="M0 0h600v320H0z" fill="#e8e2d6"/>
<g stroke="{INK}" stroke-width="2" fill="none">
''' + ''.join(f'<path d="M0 {60+i*52}h600"/>' for i in range(5)) + f'''
</g>
{land(320, '#dfe8d8')}
<g fill="none" stroke="{TONES['green'][2]}" stroke-width="7" stroke-linecap="round">
  <path d="M300 320q-20-90 40-130t-10-120"/>
  <path d="M300 250q-60-16-80-70M330 180q60-10 84-60M320 120q-50-20-60-64"/>
</g>
<g class="greenp o">
  <path d="M216 176q-40-30-16-58 34 12 16 58zM418 116q40-30 16-58-34 12-16 58z"/>
  <path d="M256 52q-40-24-20-52 32 10 20 52zM306 300q-42-26-20-54 34 12 20 54z"/>
  <path d="M356 216q40-28 62-4-30 30-62 4z"/>
</g>
<g fill="none" stroke="{TONES['green'][2]}" stroke-width="4" stroke-linecap="round">
  <path d="M340 148q22-6 20-24M292 214q-24-4-24-22"/>
</g>''', ground=False)

add('shrub', '根元から枝分かれした背の低い木', f'''
{land(316)}
<g transform="translate(300 316)">
  <g stroke="{BRN}" stroke-width="10" stroke-linecap="round" fill="none">
    <path d="M0 0v-40M0-40l-40-40M0-40l40-40M0-40v-46M-40-80l-24-34M40-80l24-34"/>
  </g>
  <g class="greenp o">
    <ellipse cx="-66" cy="-124" rx="46" ry="36"/><ellipse cx="0" cy="-146" rx="52" ry="40"/>
    <ellipse cx="66" cy="-124" rx="46" ry="36"/><ellipse cx="-32" cy="-92" rx="40" ry="30"/>
    <ellipse cx="34" cy="-92" rx="40" ry="30"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 316v-70"/></g>''', arrow=True, ground=False)

add('hedge', '刈りそろえられた生け垣が庭を区切っている', f'''
{land(320)}
<g>
  <path d="M60 320V200q0-16 16-16h448q16 0 16 16v120z" class="green o"/>
  <g fill="{TONES['green'][2]}">
''' + ''.join(f'<circle cx="{84+i*36}" cy="{206+(i%3)*20}" r="9"/>' for i in range(13)) + f'''
  </g>
  <path d="M60 200q60-14 120 0t120 0 120 0 120 0" fill="none" stroke="{TONES['green'][2]}" stroke-width="4"/>
</g>
<g transform="translate(300 150) rotate(-20)">
  <g stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
    <path d="M-6-6L-96-40q-12-4-8-14t18-6L8-24z" fill="#cfd6dd"/>
    <path d="M-6 6L-96 40q-12 4-8 14t18 6L8 24z" fill="#8f9aa6"/>
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="12" stroke-linecap="round">
    <path d="M12-12q46-18 64 4t-16 32"/><path d="M12 12q46 18 64-4t-16-32"/>
  </g>
</g>''', ground=False)

add('trunk', '木の幹の太い部分だけが示されている', f'''
{land(318)}
<g transform="translate(300 318)">
  <path d="M-56 0q-6-120 10-180h92q16 60 10 180z" fill="{BRN}" class="o"/>
  <g fill="none" stroke="#6b4c28" stroke-width="4">
    <path d="M-34-10q-4-110 6-160M0-6q0-116 2-164M34-10q4-110-6-160"/>
  </g>
  <g class="greenp o">
    <circle cx="-60" cy="-210" r="50"/><circle cx="20" cy="-238" r="58"/><circle cx="76" cy="-200" r="46"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 250h-90"/></g>''', arrow=True, ground=False)

add('twig', '指ほどの細い小枝が折れている', f'''
{land(320)}
<g transform="translate(300 220) rotate(-12)">
  <g stroke="#a0764a" stroke-width="11" stroke-linecap="round" fill="none">
    <path d="M-160 0h150"/>
    <path d="M-90 0l-30-34M-40 0l-26 40M10 0l32-34"/>
  </g>
  <g stroke="#a0764a" stroke-width="11" stroke-linecap="round" fill="none" transform="translate(40 26) rotate(24)">
    <path d="M0 0h130M60 0l30-34M100 0l24 36"/>
  </g>
  <g class="greenp o">
    <path d="M-126-40q-30-24-12-44 26 10 12 44zM48-40q30-24 12-44-26 10-12 44z"/>
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M336 224l14-18M348 244l20-6"/>
</g>''', ground=False)

add('bud', '枝の先でまだ開いていないつぼみがふくらんでいる', f'''
{land(318)}
<g transform="translate(300 318)">
  <path d="M-10 0h20v-150h-20z" class="greend o"/>
  <g stroke="{TONES['green'][2]}" stroke-width="7" stroke-linecap="round" fill="none">
    <path d="M0-90l-56-30M0-120l56-34"/>
  </g>
  <g class="greenp o">
    <path d="M-56-120q-40-24-24-46 32 8 24 46zM56-154q40-24 24-46-32 8-24 46z"/>
  </g>
  <g transform="translate(0 -180)">
    <path d="M0-34q34 0 34 34t-34 40q-34-6-34-40 0-34 34-34z" class="coralp o"/>
    <path d="M-14 0q0-30 14-34 14 4 14 34-14 8-28 0z" class="coral o"/>
    <path d="M-30 24q-14 22 6 26 12-8 8-26zM30 24q14 22-6 26-12-8-8-26z" class="green o"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M450 128l-86 10"/></g>''', arrow=True, ground=False)

add('blossom', '枝いっぱいに桜のような花が咲いている', f'''
<g>
  <path d="M0 60q140 40 300 60t300 20" fill="none" stroke="{BRN}" stroke-width="16" stroke-linecap="round"/>
  <g stroke="{BRN}" stroke-width="8" stroke-linecap="round" fill="none">
    <path d="M160 82l-30 60M280 110l20 66M400 128l-24 62M480 136l30 54"/>
  </g>
</g>
<g>
''' + ''.join(f'''<g transform="translate({100+i*62} {96+(i%3)*44})">
  <g class="coralp o">''' + ''.join(f'<ellipse cx="{22*__import__("math").cos(j*1.2566):.0f}" cy="{22*__import__("math").sin(j*1.2566):.0f}" rx="16" ry="13"/>' for j in range(5)) + f'''</g>
  <circle r="8" class="gold o"/></g>''' for i in range(8)) + f'''
</g>
<g fill="{TONES['coral'][1]}">
  <ellipse cx="180" cy="330" rx="14" ry="10" transform="rotate(20 180 330)"/>
  <ellipse cx="320" cy="356" rx="14" ry="10" transform="rotate(-30 320 356)"/>
  <ellipse cx="440" cy="336" rx="14" ry="10" transform="rotate(10 440 336)"/>
</g>''', ground=False)

add('petal', '一枚の花びらが花から離れて落ちる', f'''
<g transform="translate(230 190)">
  <g class="violetp o">
''' + ''.join(f'<ellipse cx="{56*__import__("math").cos(j*1.2566):.0f}" cy="{56*__import__("math").sin(j*1.2566):.0f}" rx="40" ry="32" transform="rotate({j*72} {56*__import__("math").cos(j*1.2566):.0f} {56*__import__("math").sin(j*1.2566):.0f})"/>' for j in range(5)) + f'''
  </g>
  <circle r="24" class="gold o"/>
  <path d="M0 90v70" stroke="{TONES['green'][2]}" stroke-width="9" stroke-linecap="round" fill="none"/>
</g>
<g transform="translate(440 262) rotate(34)">
  <ellipse rx="48" ry="36" class="violet o"/>
  <path d="M-30 0q30-18 60 0" fill="none" stroke="{TONES['violet'][2]}" stroke-width="4"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M320 190q60 20 90 56"/></g>''', arrow=True, ground=False)

add('thorn', 'バラの茎に鋭いとげが並んでいる', f'''
<g transform="translate(300 210) rotate(16)">
  <path d="M-12-160h24v340h-24z" class="greend o"/>
  <g class="greend o">
''' + ''.join(f'<path d="M-12 {-110+i*54}l-36-26 6 30z"/><path d="M12 {-84+i*54}l36-26-6 30z"/>' for i in range(5)) + f'''
  </g>
  <g transform="translate(0 -190)">
    <g class="coral o">
''' + ''.join(f'<ellipse cx="{34*__import__("math").cos(j*1.05):.0f}" cy="{34*__import__("math").sin(j*1.05):.0f}" rx="26" ry="22"/>' for j in range(6)) + f'''
    </g>
    <circle r="18" class="corald o"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 220l-78-26"/></g>''', arrow=True, ground=False)

add('pollen', '花からミツバチが花粉を運んでいる', f'''
{land(320)}
<g transform="translate(200 200)">
  <g class="gold o">
''' + ''.join(f'<ellipse cx="{48*__import__("math").cos(j*1.05):.0f}" cy="{48*__import__("math").sin(j*1.05):.0f}" rx="34" ry="26" transform="rotate({j*60} {48*__import__("math").cos(j*1.05):.0f} {48*__import__("math").sin(j*1.05):.0f})"/>' for j in range(6)) + f'''
  </g>
  <circle r="28" class="goldd o"/>
  <path d="M0 76v44" stroke="{TONES['green'][2]}" stroke-width="10" stroke-linecap="round" fill="none"/>
</g>
<g fill="{TONES['gold'][0]}">
''' + ''.join(f'<circle cx="{262+i*26}" cy="{176+(i%4)*22}" r="{7-(i%3)}"/>' for i in range(9)) + f'''
</g>
<g transform="translate(470 214)">
  <ellipse rx="40" ry="26" class="gold o"/>
  <g fill="{INK}"><path d="M-18-24q10 48 0 48zM6-26q10 52 0 52z"/></g>
  <circle cx="-34" cy="-4" r="16" fill="{INK}"/>
  <g fill="#fffefd" stroke="{INK}" stroke-width="2" opacity="0.85">
    <ellipse cx="4" cy="-30" rx="30" ry="14" transform="rotate(-22 4 -30)"/>
  </g>
</g>''', ground=False)

add('sap', '幹の切り口から樹液がしたたっている', f'''
{land(320)}
<g transform="translate(300 320)">
  <path d="M-64 0q-8-140 12-210h104q20 70 12 210z" fill="{BRN}" class="o"/>
  <g fill="none" stroke="#6b4c28" stroke-width="4">
    <path d="M-36-14q-4-130 6-186M0-10q0-136 2-190M36-14q4-130-6-186"/>
  </g>
  <path d="M-58-130h50v22h-50z" fill="#e0c48a" class="o"/>
  <g class="golds" stroke-width="0"/>
</g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2">
  <path d="M244 212q10 12 10 20t-10 10-10-10 10-20z"/>
  <path d="M240 258q9 11 9 18t-9 9-9-9 9-18z"/>
</g>
<g transform="translate(236 300)">
  <path d="M-44-20h88v20q0 14-44 14t-44-14z" fill="{MUTED}" class="o"/>
  <ellipse cy="-20" rx="44" ry="12" fill="{TONES['gold'][0]}" class="o"/>
</g>''', ground=False)

add('bark', '木の幹の表面のごつごつした樹皮が近くから見えている', f'''
<path d="M0 0h600v400H0z" fill="#a0764a"/>
<g fill="none" stroke="#6b4c28" stroke-width="7" stroke-linecap="round">
''' + ''.join(f'<path d="M{40+i*52} 0q{-14+ (i%3)*14} 100 {6-(i%4)*6} 200t{-8+(i%3)*10} 200"/>' for i in range(11)) + f'''
</g>
<g fill="none" stroke="#c9a464" stroke-width="3">
''' + ''.join(f'<path d="M{62+i*52} 20q{-10+(i%3)*10} 100 {4-(i%4)*4} 200t{-6+(i%3)*8} 180"/>' for i in range(10)) + f'''
</g>
<g fill="#7a5b3c">
  <path d="M120 140q30-10 40 20-34 12-40-20zM320 240q28-14 42 14-32 16-42-14zM460 90q26-12 38 16-30 16-38-16z"/>
</g>''', ground=False)

# --- 地形 -------------------------------------------------------------------
add('meadow', '野の花が咲いた平らな草地が広がっている', f'''
{sky()}
<path d="M0 200q120-20 300-14t300 14v200H0z" fill="{GR}"/>
<path d="M0 200q120-20 300-14t300 14" fill="none" stroke="{INK}" stroke-width="2.5"/>
<g stroke="{TONES['green'][0]}" stroke-width="3" stroke-linecap="round" fill="none">
''' + ''.join(f'<path d="M{20+i*24} {400-(i%5)*10}v-{26+(i%4)*8}"/>' for i in range(24)) + f'''
</g>
<g>
''' + ''.join(f'<g transform="translate({50+i*54} {250+(i%5)*28})"><circle r="8" class="gold o"/>' + ''.join(f'<ellipse cx="{14*__import__("math").cos(j*1.256):.0f}" cy="{14*__import__("math").sin(j*1.256):.0f}" rx="8" ry="6" class="{"coralp" if i%2 else "violetp"} o"/>' for j in range(5)) + '</g>' for i in range(10)) + f'''
</g>
{sun(500, 70, 36)}''', ground=False)

add('swamp', '木が立ち枯れ、水がよどんだ沼地', f'''
<path d="M0 0h600v230H0z" fill="#c9d6c0"/>
<path d="M0 230h600v170H0z" fill="#6b7a5e"/>
<path d="M0 230h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="#566349" stroke-width="4">
  <path d="M40 268h140M300 300h180M120 340h200M400 258h150"/>
</g>
<g>
  <path d="M150 230V90h18v140zM370 230V60h20v170zM470 230V120h16v110z" fill="#5b4a3c" class="o"/>
  <g stroke="#5b4a3c" stroke-width="7" stroke-linecap="round" fill="none">
    <path d="M159 130l-40-30M159 160l44-24M380 100l-46-34M380 140l50-28M478 156l-36-24"/>
  </g>
</g>
<g class="greend o">
  <ellipse cx="80" cy="252" rx="46" ry="14"/><ellipse cx="250" cy="286" rx="52" ry="16"/><ellipse cx="520" cy="310" rx="44" ry="14"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3">
  <circle cx="200" cy="258" r="9"/><circle cx="330" cy="330" r="8"/><circle cx="440" cy="288" r="10"/>
</g>''', ground=False)

add('dune', '風で形の変わる砂の丘が連なっている', f'''
{sky()}
<path d="M0 250q100-70 200-20t180-40 220 20v190H0z" fill="#f0dfb8"/>
<path d="M0 250q100-70 200-20t180-40 220 20" fill="none" stroke="{INK}" stroke-width="2.5"/>
<path d="M0 320q140-40 300 10t300-16v86H0z" fill="#e0c48a"/>
<path d="M0 320q140-40 300 10t300-16" fill="none" stroke="{INK}" stroke-width="2.5"/>
<g fill="none" stroke="#c9a464" stroke-width="3">
  <path d="M40 300q80-20 160 6M280 268q70-24 140-4M340 356q90-18 170 4"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-linecap="round">
  <path d="M60 190q50-14 90 0M120 160q50-14 90 0"/>
</g>
{sun(500, 80, 34)}''', ground=False)

add('canyon', '川が岩を削ってできた深い峡谷', f'''
{sky()}
<g>
  <path d="M0 120h230l-70 240H0z" fill="#c8703a" class="o"/>
  <path d="M600 120H370l70 240h160z" fill="#c8703a" class="o"/>
  <path d="M0 120h230l-40 60H0zM600 120H370l40 60h190z" fill="#d88a54"/>
  <g fill="none" stroke="#a85a2c" stroke-width="4">
    <path d="M0 200h206M0 260h190M0 320h176M600 200H394M600 260H410M600 320H424"/>
  </g>
</g>
<path d="M160 360h280l-30-40H190z" fill="#8fb8d4" class="o"/>
<g fill="none" stroke="#c7dbea" stroke-width="4"><path d="M210 344h180"/></g>''', ground=False)

add('plateau', '頂上が平らに広がった台地', f'''
{sky()}
<path d="M0 400V330q0-16 60-30l40-130q6-20 40-20h320q34 0 40 20l40 130q60 14 60 30v70z" fill="#c99a63" class="o"/>
<path d="M140 150h320v20H140z" fill="#dcae72" class="o"/>
<g fill="none" stroke="#a0764a" stroke-width="4">
  <path d="M120 210h360M104 260h392M88 310h424"/>
</g>
<g class="greenp o">
  <ellipse cx="220" cy="146" rx="30" ry="14"/><ellipse cx="330" cy="142" rx="34" ry="14"/><ellipse cx="420" cy="148" rx="26" ry="12"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 96v40"/></g>
{sun(520, 70, 30)}''', arrow=True, ground=False)

add('ridge', '山の背が一本の線になって続く尾根', f'''
{sky()}
<path d="M0 400l120-190 90 90 100-160 110 130 80-70 100 200z" fill="#9aa5b0" class="o"/>
<path d="M0 400l120-190 90 90 100-160 110 130 80-70 100 200z" fill="none" stroke="{INK}" stroke-width="2.5"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round">
  <path d="M120 210l90 90 100-160 110 130 80-70"/>
</g>
<path d="M310 140l-30 44h60z" fill="#fffefd" class="o"/>
{person(392, 156, 0.34, 1, 'coral', 'blue', 'stand', 'cap', 'smile')}''', ground=False)

add('creek', '林の中を流れる浅い小川', f'''
<path d="M0 0h600v400H0z" fill="{GR}"/>
<path d="M240 0q-40 100 20 160t-30 140 40 100" fill="none" stroke="#8fb8d4" stroke-width="80" stroke-linecap="round"/>
<path d="M240 0q-40 100 20 160t-30 140 40 100" fill="none" stroke="#c7dbea" stroke-width="52" stroke-linecap="round"/>
<g fill="none" stroke="#8fb8d4" stroke-width="4">
  <path d="M230 90q30 14 40 0M258 190q30 14 40 0M226 290q30 14 40 0"/>
</g>
<g fill="{MUTED}" stroke="{INK}" stroke-width="2">
  <ellipse cx="212" cy="150" rx="20" ry="13"/><ellipse cx="288" cy="248" rx="17" ry="11"/><ellipse cx="240" cy="340" rx="18" ry="12"/>
</g>
{tree(90, 320, 1.0)}
{tree(470, 340, 1.2)}
{tree(540, 250, 0.7)}''', ground=False)

add('waterfall', '崖から水が落ちて下の池でしぶきを上げている', f'''
{sky()}
<g>
  <path d="M0 60h200v300H0z" fill="#9aa5b0" class="o"/>
  <path d="M600 60H400v300h200z" fill="#9aa5b0" class="o"/>
  <g fill="none" stroke="#7d8894" stroke-width="4">
    <path d="M0 130h192M0 200h190M0 270h188M600 130H408M600 200H410M600 270H412"/>
  </g>
</g>
<path d="M200 60h200v270H200z" fill="#c7dbea"/>
<g fill="none" stroke="#fffefd" stroke-width="6" stroke-linecap="round">
  <path d="M230 70v250M270 70v250M310 70v250M350 70v250M382 70v250"/>
</g>
<path d="M120 330h360v70H120z" fill="#8fb8d4"/>
<path d="M120 330h360" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="#fffefd" stroke="{INK}" stroke-width="2" opacity="0.9">
  <circle cx="230" cy="330" r="20"/><circle cx="286" cy="318" r="26"/><circle cx="344" cy="330" r="22"/><circle cx="392" cy="322" r="17"/>
</g>''', ground=False)

add('glacier', '谷をゆっくり流れ下る氷の川', f'''
{sky()}
<path d="M0 400V180l120-90 110 70 100-90 120 100 150-60v290z" fill="#b8c1ca" class="o"/>
<path d="M120 400q-20-160 60-230 40-34 100-6 60-30 120 20 60 50 40 216z" fill="#dfeaf2" class="o"/>
<g fill="none" stroke="#a8c4da" stroke-width="5">
  <path d="M150 380q60-30 130-6t130-8M158 320q60-26 120-4t126-8M176 250q54-22 104-2t106-6"/>
</g>
<g fill="#c7dbea" stroke="{INK}" stroke-width="2">
  <path d="M210 300l16-26 16 26zM320 250l14-24 14 24zM400 330l16-26 16 26z"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 130v40"/></g>''', arrow=True, ground=False)

add('iceberg', '海に浮かぶ氷山、水面下のほうが大きい', f'''
<path d="M0 0h600v190H0z" fill="{SKY}"/>
<path d="M0 190h600v210H0z" fill="#5b8caa"/>
<path d="M0 190h600" stroke="{INK}" stroke-width="3" fill="none"/>
<g>
  <path d="M230 190l70-110 90 110z" fill="#fffefd" class="o"/>
  <path d="M300 80l50 110h-50z" fill="#dfeaf2"/>
  <path d="M150 190h330q30 80-10 130-50 62-160 56-110-6-150-70-30-46-10-116z" fill="#c7dbea" class="o" opacity="0.9"/>
  <g fill="none" stroke="#9fc4dd" stroke-width="4">
    <path d="M200 240h240M180 300h280M220 350h190"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M74 130v52"/></g>
<g class="a" marker-end="url(#ar)"><path d="M74 240v130"/></g>''', arrow=True, ground=False)

# --- 天気 -------------------------------------------------------------------
add('breeze', '穏やかな風に木の葉と洗濯物がゆれている', f'''
{sky()}
{land(320)}
{tree(150, 320, 1.0)}
<g>
  <path d="M280 130h240" stroke="{INK}" stroke-width="4" fill="none"/>
  <path d="M300 130q6 70 30 74t26-74z" class="tealp o"/>
  <path d="M380 130q8 66 32 70t24-70z" class="coralp o"/>
  <path d="M460 130q6 60 28 64t22-64z" class="goldp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M40 170q60-16 100 0t100-4M40 220q60-16 100 0t100-4"/>
</g>
<g fill="{TONES['green'][0]}">
  <ellipse cx="250" cy="196" rx="12" ry="8" transform="rotate(20 250 196)"/>
  <ellipse cx="288" cy="240" rx="11" ry="7" transform="rotate(-20 288 240)"/>
</g>''', ground=False)

add('gale', '強風で傘が裏返り、木が大きくしなっている', f'''
<path d="M0 0h600v400H0z" fill="#c8d2da"/>
{land(330, '#c9d6c0')}
<g transform="translate(140 330) rotate(-24)">
  <path d="M-10 0h20v-160h-20z" fill="{BRN}" class="o"/>
  <g class="greenp o" transform="rotate(-16 0 -160)">
    <circle cx="-30" cy="-190" r="40"/><circle cx="26" cy="-206" r="44"/><circle cx="10" cy="-166" r="36"/>
  </g>
</g>
{person(360, 340, 0.95, 1, 'blue', 'blue', 'reach', 'short', 'sad')}
<g transform="translate(452 150) rotate(160)">
  <path d="M-80 0q0-70 80-70t80 70q-40-26-80-26T-80 0z" class="coral o"/>
  <path d="M0 0v90" stroke="{INK}" stroke-width="6" stroke-linecap="round" fill="none"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M20 120q80-24 150 0t150-8M20 190q80-24 150 0t150-8M20 260q70-22 130 0"/>
</g>''', ground=False)

add('thunder', '暗い雲から雷鳴がとどろいている', f'''
<path d="M0 0h600v400H0z" fill="#8f9aa6"/>
{land(340, '#6b7a5e')}
<g fill="#4a5560" stroke="{INK}" stroke-width="2.5">
  <path d="M110 190q-8-58 44-58 14-46 68-30 34-26 68 12 60-14 66 46 44 6 40 44H144q-32-2-34-14z"/>
</g>
<g fill="none" stroke="#fdf0d0" stroke-width="7" stroke-linecap="round">
  <path d="M170 230q-20 24-6 40M300 240q-24 26-8 44M430 226q-22 24-6 42"/>
</g>
<g fill="none" stroke="#fdf0d0" stroke-width="5" stroke-linecap="round" opacity="0.8">
  <path d="M120 252q40 18 90 6M340 268q50 16 100 0M200 300q60 18 120 2"/>
</g>
<g fill="{MUTED}" opacity="0.6">
  <ellipse cx="300" cy="300" rx="170" ry="30"/>
</g>''', ground=False)

add('lightning', '空から地上へ稲妻が一本走っている', f'''
<path d="M0 0h600v400H0z" fill="#3b4450"/>
{land(340, '#2c333d')}
<g fill="#4a5560" stroke="{INK}" stroke-width="2.5">
  <path d="M120 130q-8-54 42-54 14-42 66-28 32-24 66 12 56-14 62 42 42 6 38 42H152q-30-2-32-14z"/>
</g>
<path d="M290 150l-70 120h56l-46 110 130-150h-58l52-80z" fill="#fde39a" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>
<g fill="none" stroke="#fde39a" stroke-width="4" opacity="0.7" stroke-linecap="round">
  <path d="M440 170l-30 70h26l-22 60M140 200l-24 56h20l-18 46"/>
</g>''', ground=False)

add('sleet', '雨と雪が混ざったみぞれが降っている', f'''
<path d="M0 0h600v400H0z" fill="#b8c1ca"/>
{land(346, '#c9d6c0')}
{cloud(300, 90, 1.4, 'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
''' + ''.join(f'<path d="M{80+i*52} {180+(i%3)*46}l-12 34"/>' for i in range(10)) + f'''
</g>
<g fill="none" stroke="#fffefd" stroke-width="3" stroke-linecap="round">
''' + ''.join(f'<g transform="translate({108+i*52} {212+(i%4)*40})"><path d="M0-10v20M-9-5l18 10M-9 5l18-10"/></g>' for i in range(9)) + f'''
</g>''', ground=False)

add('frost', '朝の草と窓に白い霜が降りている', f'''
<path d="M0 0h600v400H0z" fill="#dfeaf2"/>
{land(300, '#cfe0ec')}
<g stroke="{TONES['green'][2]}" stroke-width="4" stroke-linecap="round" fill="none">
''' + ''.join(f'<path d="M{30+i*30} 400v-{50+(i%4)*20}"/>' for i in range(19)) + f'''
</g>
<g stroke="#fffefd" stroke-width="4" stroke-linecap="round" fill="none">
''' + ''.join(f'<path d="M{30+i*30} {350-(i%4)*20}v-{50+(i%4)*20}"/>' for i in range(19)) + f'''
</g>
<g fill="none" stroke="#fffefd" stroke-width="3.5" stroke-linecap="round">
''' + ''.join(f'<g transform="translate({110+i*100} {110+(i%2)*70})"><path d="M0-26v52M-22-13l44 26M-22 13l44-26"/><path d="M0-26l-8 10M0-26l8 10M0 26l-8-10M0 26l8-10"/></g>' for i in range(5)) + f'''
</g>''', ground=False)

add('dew', '朝の葉に水滴がいくつも乗っている', f'''
<path d="M0 0h600v400H0z" fill="#e8f0e4"/>
<g transform="translate(300 220)">
  <path d="M-200 60q-30-120 90-160 120-40 220 20 60 36 30 90-120 46-340 50z" class="greenp o"/>
  <path d="M-160 74q100-90 300-70" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="4">
    <path d="M-100 46q-14-40-4-70M-20 34q-8-44 6-74M60 30q-4-44 14-70M140 34q0-40 20-62"/>
  </g>
</g>
<g fill="#cfe0ec" stroke="{TONES['blue'][0]}" stroke-width="2.5">
  <ellipse cx="180" cy="200" rx="18" ry="16"/><ellipse cx="262" cy="176" rx="14" ry="12"/>
  <ellipse cx="340" cy="188" rx="20" ry="17"/><ellipse cx="420" cy="206" rx="15" ry="13"/>
  <ellipse cx="222" cy="248" rx="12" ry="10"/><ellipse cx="386" cy="252" rx="13" ry="11"/>
</g>
<g fill="#fffefd" opacity="0.9">
  <ellipse cx="174" cy="194" rx="6" ry="4"/><ellipse cx="334" cy="182" rx="6" ry="4"/><ellipse cx="416" cy="200" rx="5" ry="3"/>
</g>''', ground=False)

add('mist', '向こうが透けて見える薄いもやが川面に立っている', f'''
<path d="M0 0h600v400H0z" fill="#e2eaf0"/>
<path d="M0 290h600v110H0z" fill="#bcd4e4"/>
<g opacity="0.5">
  {tree(120, 290, 1.0)}
  {tree(470, 290, 0.85)}
</g>
<g opacity="0.35">
  <path d="M300 290V150h20v140z" fill="{BRN}"/>
  <circle cx="310" cy="130" r="46" class="greenp"/>
</g>
<g fill="#fffefd" opacity="0.75">
  <ellipse cx="160" cy="250" rx="150" ry="26"/><ellipse cx="400" cy="236" rx="170" ry="24"/>
  <ellipse cx="290" cy="286" rx="200" ry="26"/><ellipse cx="470" cy="300" rx="140" ry="20"/>
</g>''', ground=False)

add('fog', '濃い霧で前が見えず、車がライトをつけている', f'''
<path d="M0 0h600v400H0z" fill="#d2d8dd"/>
<path d="M0 320h600v80H0z" fill="#b8bfc5"/>
<g opacity="0.3">
  <path d="M100 320V160h16v160zM500 320V180h16v140z" fill="{MUTED}"/>
</g>
<g transform="translate(300 280)">
  <path d="M-110 40h220v-46q0-16-16-16h-188q-16 0-16 16z" fill="#6f7b88" class="o" opacity="0.8"/>
  <path d="M-74-22h148l-24-40h-100z" fill="#8f9aa6" class="o" opacity="0.8"/>
  <circle cx="-70" cy="40" r="20" fill="{INK}" opacity="0.8"/><circle cx="70" cy="40" r="20" fill="{INK}" opacity="0.8"/>
  <circle cx="-96" cy="6" r="12" class="goldp o"/><circle cx="96" cy="6" r="12" class="goldp o"/>
  <g fill="{TONES['gold'][1]}" opacity="0.5">
    <path d="M-96 6l-90-40v80zM96 6l90-40v80z"/>
  </g>
</g>
<g fill="#fffefd" opacity="0.8">
  <ellipse cx="150" cy="200" rx="190" ry="46"/><ellipse cx="440" cy="176" rx="180" ry="40"/>
  <ellipse cx="300" cy="268" rx="230" ry="36"/>
</g>''', ground=False)

add('drizzle', '細かい霧雨が静かに降り続いている', f'''
<path d="M0 0h600v400H0z" fill="#cfd8e0"/>
{land(340, '#c9d6c0')}
{cloud(300, 86, 1.5, 'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="2" stroke-linecap="round" opacity="0.9">
''' + ''.join(f'<path d="M{50+i*26} {170+(i%5)*34}v14"/>' for i in range(21)) + ''.join(f'<path d="M{62+i*26} {240+(i%4)*30}v12"/>' for i in range(20)) + f'''
</g>
{person(300, 340, 0.8, 1, 'coral', 'blue', 'stand', 'bob', 'neutral')}
<g>
  <path d="M240 210q0-60 60-60t60 60q-30-20-60-20t-60 20z" class="teal o"/>
  <path d="M300 210v80" stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none"/>
</g>''', ground=False)

add('downpour', 'どしゃぶりの雨が地面ではね返っている', f'''
<path d="M0 0h600v400H0z" fill="#8f9aa6"/>
{land(340, '#6b7a5e')}
<g fill="#4a5560" stroke="{INK}" stroke-width="2.5">
  <path d="M100 120q-8-56 44-56 14-44 68-28 34-26 68 12 60-14 66 44 44 6 40 42H134q-32-2-34-14z"/>
</g>
<g fill="none" stroke="#c7dbea" stroke-width="6" stroke-linecap="round">
''' + ''.join(f'<path d="M{40+i*38} {150+(i%3)*40}l-18 130"/>' for i in range(15)) + f'''
</g>
<g fill="none" stroke="#c7dbea" stroke-width="4" stroke-linecap="round">
''' + ''.join(f'<path d="M{50+i*46} 340q-10-20-2-30M{62+i*46} 340q10-20 2-30"/>' for i in range(12)) + f'''
</g>''', ground=False)

add('sunrise', '地平線から太陽が昇り、空が明るくなる', f'''
<path d="M0 0h600v300H0z" fill="#fbd9a8"/>
<path d="M0 0h600v120H0z" fill="#cfe0ec"/>
<path d="M0 120h600v60H0z" fill="#e6dfc4" opacity="0.7"/>
<path d="M0 300h600v100H0z" fill="#6b7a5e"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g>
  <path d="M180 300a120 120 0 0 1 240 0z" class="gold o"/>
  <g class="golds" stroke-width="6" stroke-linecap="round">
    <path d="M300 152v-46M170 210l-36-30M430 210l36-30M120 292H70M530 292h-50M204 176l-24-40M396 176l24-40"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M540 260v-90"/></g>''', arrow=True, ground=False)

add('sunset', '太陽が地平線に沈み、空がオレンジに染まる', f'''
<path d="M0 0h600v300H0z" fill="#f0a06a"/>
<path d="M0 0h600v110H0z" fill="#8f7ab0"/>
<path d="M0 110h600v70H0z" fill="#d98a70" opacity="0.8"/>
<path d="M0 300h600v100H0z" fill="#4a4436"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M190 300a110 110 0 0 1 220 0z" class="corald o"/>
<g fill="none" stroke="#c96f5a" stroke-width="5" opacity="0.8">
  <path d="M40 240h180M380 240h180M60 268h140M400 268h140"/>
</g>
<g fill="{INK}">
  <path d="M100 300V240h10v60zM120 300V220h10v80z"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M520 180v90"/></g>''', arrow=True, ground=False)

add('dusk', '日が沈んだあとの薄暗い時間、街灯がともる', f'''
<path d="M0 0h600v320H0z" fill="#5b6a86"/>
<path d="M0 0h600v130H0z" fill="#3b4a66"/>
<path d="M0 130h600v70H0z" fill="#7a7290" opacity="0.7"/>
<path d="M0 320h600v80H0z" fill="#333c33"/>
<path d="M0 320h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="#2c333d">
  <path d="M60 320V200h60v120zM160 320V160h70v160zM380 320V180h64v140zM480 320V220h56v100z"/>
</g>
<g fill="{TONES['gold'][1]}">
  <rect x="176" y="180" width="16" height="20"/><rect x="202" y="216" width="16" height="20"/>
  <rect x="396" y="200" width="16" height="20"/><rect x="496" y="242" width="16" height="20"/>
</g>
<g>
  <path d="M296 320V150h10v170z" fill="#2c333d"/>
  <circle cx="301" cy="140" r="20" class="goldp o"/>
  <g fill="{TONES['gold'][1]}" opacity="0.4"><path d="M301 140l-70 180h140z"/></g>
</g>
<g fill="#fdf0d0"><circle cx="500" cy="60" r="5"/><circle cx="440" cy="40" r="4"/><circle cx="550" cy="96" r="4"/></g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
