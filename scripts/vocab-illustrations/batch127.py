# -*- coding: utf-8 -*-
"""第127回。家族・家の中・句動詞。句動詞は「前置詞の向き」を矢印でそのまま描く。"""
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
    return (f'<g transform="translate({x} {y})">'
            f'<circle r="{r}" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>'
            f'<path d="{HAIRS[hair]}" transform="translate(0 108) scale({r/24:.2f})" fill="{HAIR}"/>'
            f'<circle cx="{-r*0.33:.0f}" cy="{-r*0.17:.0f}" r="2.4" fill="{INK}"/>'
            f'<circle cx="{r*0.33:.0f}" cy="{-r*0.17:.0f}" r="2.4" fill="{INK}"/>'
            f'<path d="M{-r*0.3:.0f} {r*0.35:.0f}q{r*0.3:.0f} {r*0.3:.0f} {r*0.6:.0f} 0" fill="none" stroke="{INK}" stroke-width="2"/>'
            f'<path d="M{-r*1.1:.0f} {r*1.5:.0f}q{r*1.1:.0f}-{r*0.6:.0f} {r*2.2:.0f} 0l-{r*0.3:.0f} {r*1.2:.0f}h-{r*1.6:.0f}z" fill="{TONES[shirt][0]}" class="o"/></g>')
def doc(x, y, w=100, h=130, lines=4, cls=None):
    g = [f'<g transform="translate({x} {y})"><path d="M{-w/2} {-h/2}h{w}v{h}h{-w}z" class="paper"/>']
    for i in range(lines):
        g.append(f'<rect x="{-w/2+14}" y="{-h/2+22+i*(h-50)/max(lines,1):.0f}" width="{w-28-(i%3)*16}" height="8" rx="4" fill="{MUTED}"/>')
    g.append('</g>')
    return ''.join(g)

# --- 家族 -------------------------------------------------------------------
add('aunt', '家系図で親の姉妹にあたるおばの位置が示されている', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g fill="none" stroke="{BRN}" stroke-width="4">
  <path d="M300 90v30M170 120h260M170 120v40M430 120v40M300 210v40M240 250h120M240 250v30M360 250v30"/>
</g>
{head(300, 60, 24, 'gold', 'bun')}
{head(170, 190, 24, 'teal', 'short')}
{head(430, 190, 24, 'coral', 'bun')}
{head(240, 310, 20, 'green', 'cap')}
{head(360, 310, 20, 'violet', 'bob')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="10 8"><circle cx="430" cy="196" r="52"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M540 300l-70-70"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M170 260q60 40 130 40"/></g>''', ground=False)

add('cousin', 'おじおばの子どもが自分と同じ世代に並んでいる', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g fill="none" stroke="{BRN}" stroke-width="4">
  <path d="M300 90v30M150 120h300M150 120v40M450 120v40M150 210v40M450 210v40M100 250h100M400 250h100M100 250v30M200 250v30M400 250v30M500 250v30"/>
</g>
{head(300, 60, 24, 'gold', 'bun')}
{head(150, 190, 22, 'teal', 'short')}
{head(450, 190, 22, 'coral', 'bun')}
{head(100, 310, 19, 'blue', 'cap')}
{head(200, 310, 19, 'green', 'bob')}
{head(400, 310, 19, 'violet', 'short')}
{head(500, 310, 19, 'gold', 'bun')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="10 8"><ellipse cx="450" cy="316" rx="88" ry="52"/></g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="10 8"><ellipse cx="150" cy="316" rx="88" ry="52"/></g>''', ground=False)

add('babysitter', '親の留守中に子どもの世話をする人', f'''
{table(370)}
{sit(220, 370, 1.05, 1, 'coral', 'blue', 'bun', 'smile', 'lap')}
<g transform="translate(180 300)">
  <path d="M-36-20q36-22 72 0 6 36-16 44-30 8-48-4-14-16-8-40z" class="teal o"/>
  <circle cx="-4" cy="-40" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-28-50q4-24 24-22 18 2 22 22z" fill="{HAIR}"/>
  <circle cx="-12" cy="-42" r="2.4" fill="{INK}"/><circle cx="4" cy="-42" r="2.4" fill="{INK}"/>
  <path d="M-10-32q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
{chair(220, 370, 1.0, 'gold', 1)}
<g transform="translate(450 250)">
  <path d="M-60-40h120v70h-120z" fill="#3b4450" class="o"/>
  <path d="M-52-32h104v54h-104z" fill="#dceaf4"/>
  <path d="M-30 30h60v10h-60z" fill="#5a6270"/>
</g>
<g transform="translate(470 340)">
  <path d="M-40-20h80v40h-80z" class="coralp o"/>
  <circle cx="-20" r="10" class="coral o"/><circle cx="20" r="10" class="teal o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M320 180h140"/></g>
<g transform="translate(120 170)">
  <path d="M-40-28h80q10 0 10 10v30q0 10-10 10h-52l-18 14v-14q-10 0-10-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M-14 6q14-24 28 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
</g>''', ground=False)

add('baker', 'パン職人がかまどから焼き上がったパンを出す', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
{table(360)}
<g transform="translate(430 240)">
  <path d="M-120-120h240v240h-240z" fill="#a89880" class="o"/>
  <path d="M-90-90h180v150h-180z" fill="#2c2420" class="o"/>
  <path d="M-80-80h160v130h-160z" fill="#c8703a" opacity="0.5"/>
  <g class="o">
    <ellipse cx="-40" cy="20" rx="34" ry="20" fill="#c8934a"/><ellipse cx="34" cy="20" rx="34" ry="20" fill="#c8934a"/>
  </g>
</g>
{person(160, 360, 1.15, 1, 'teal', 'gold', 'reach', 'bun', 'smile')}
<g transform="translate(160 232)">
  <path d="M-30-16q0-30 30-30t30 30q10 8 0 16h-60q-10-8 0-16z" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(260 250) rotate(-16)">
  <path d="M-70-8h130v16h-130z" fill="#c9a464" class="o"/>
  <path d="M60-40h60v80H60z" fill="#d9b877" class="o"/>
  <ellipse cx="90" cy="0" rx="30" ry="20" fill="#c8934a" class="o"/>
</g>''', ground=False)

# --- 家の中 -----------------------------------------------------------------
add('backpack', '肩ひも二本で背負うリュックサック', f'''
{table(340)}
<g transform="translate(300 240)">
  <path d="M-70-60h140v130q0 16-70 16t-70-16z" class="teal o"/>
  <path d="M-70-60q0-40 70-40t70 40z" class="teald o"/>
  <path d="M-50 20h100v40h-100z" class="tealp o"/>
  <path d="M-50 20h100" fill="none" stroke="{TONES['teal'][2]}" stroke-width="3"/>
  <path d="M-34-96q-40 30-40 90t26 76M34-96q40 30 40 90t-26 76" fill="none" stroke="{TONES['teal'][2]}" stroke-width="12"/>
  <path d="M-14-70h28v22h-28z" fill="{INK}"/>
</g>''', ground=False)

add('balcony', 'マンションの外に張り出した手すりつきのバルコニー', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
<path d="M0 0h300v400H0z" fill="#e0d6c0" class="o"/>
<g fill="none" stroke="#c8b8a0" stroke-width="3">
''' + ''.join(f'<path d="M0 {40+i*70}h300"/>' for i in range(5)) + f'''
</g>
<g transform="translate(240 200)">
  <path d="M-100-120h100v90h-100z" class="bluep o"/>
  <path d="M-14-30h60v100h-60z" fill="{BRN}" class="o"/>
</g>
<g transform="translate(300 280)">
  <path d="M-60 0h230v20h-230z" fill="#c8d0d8" class="o"/>
  <path d="M-60-90h230v14h-230z" fill="#8f9aa6" class="o"/>
  <g stroke="#8f9aa6" stroke-width="7" fill="none">
''' + ''.join(f'<path d="M{-40+i*36} -76v76"/>' for i in range(7)) + f'''
  </g>
  <path d="M-60 20h230v20h-230z" fill="#b8bfc8" class="o"/>
</g>
{person(400, 280, 0.85, -1, 'coral', 'blue', 'hold', 'bob', 'smile')}
<g transform="translate(500 250)">
  <path d="M-24-16h48l-6 40q-2 8-18 8t-18-8z" fill="#c8703a" class="o"/>
  <path d="M-6-16v-24" stroke="{TONES['green'][2]}" stroke-width="6" fill="none"/>
  <path d="M-6-30q-30-16-24-34 26 4 24 34z" class="greenp o"/>
</g>''', ground=False)

add('closet', '扉を開けると服がハンガーで並んでいる押し入れ', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<path d="M0 370h600v30H0z" fill="#c9a464" class="o"/>
<g transform="translate(300 200)">
  <path d="M-180-170h360v340h-360z" fill="{BRN}" class="o"/>
  <path d="M-150-140h300v280h-300z" fill="#f0e6d0" class="o"/>
  <path d="M-150-70h300" stroke="#8f9aa6" stroke-width="8" fill="none"/>
  <g>
''' + ''.join(f'''<g transform="translate({-116+i*46} -70)">
  <path d="M0 0v-16q0-10 8-12" fill="none" stroke="#8f9aa6" stroke-width="4"/>
  <path d="M-30 0h60l10 20h-80z" fill="{TONES[["teal","coral","gold","violet","blue","green"][i%6]][1]}" class="o"/>
  <path d="M-32 20h64l-8 100h-48z" fill="{TONES[["teal","coral","gold","violet","blue","green"][i%6]][0]}" class="o"/>
</g>''' for i in range(6)) + f'''
  </g>
  <path d="M-150 90h300v50h-300z" fill="#e0d6c0" class="o"/>
</g>
<path d="M120 30h20v340h-20z" fill="{BRN}" class="o"/>''', ground=False)

add('couch', 'ひじ掛けと背もたれのある長いソファー', f'''
{table(370)}
<g transform="translate(300 300)">
  <path d="M-200-30h400v70q0 14-16 14h-368q-16 0-16-14z" class="coral o"/>
  <path d="M-200-30q0-100 30-100h340q30 0 30 100z" class="coralp o"/>
  <path d="M-200-30q40-16 70-16h260q30 0 70 16z" class="corald o"/>
  <path d="M-230-40h50v70q0 10-25 10t-25-10zM180-40h50v70q0 10-25 10t-25-10z" class="corald o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"><path d="M-66-124v96M66-124v96"/></g>
  <path d="M-160 54v20M160 54v20" stroke="{BRN}" stroke-width="12" stroke-linecap="round" fill="none"/>
</g>
<g transform="translate(180 240) rotate(-8)">
  <path d="M-36-30h72v60h-72z" class="goldp o"/>
</g>''', ground=False)

add('windowsill', '窓の下枠に鉢植えと本が置かれている', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<g transform="translate(300 180)">
  <path d="M-180-160h360v300h-360z" fill="{BRN}" class="o"/>
  <path d="M-150-130h300v240h-300z" fill="#dceaf4"/>
  <path d="M0-130v240M-150-10h300" stroke="{BRN}" stroke-width="10" fill="none"/>
  {sun(90, -80, 26)}
  {tree(-80, 90, 0.8)}
</g>
<g transform="translate(300 330)">
  <path d="M-220-20h440v30h-440z" fill="#d9b877" class="o"/>
  <path d="M-220 10h440v14h-440z" fill="#c9a464" class="o"/>
</g>
<g transform="translate(200 290)">
  <path d="M-30-20h60l-6 40q-2 10-24 10t-24-10z" fill="#c8703a" class="o"/>
  <path d="M-8-20v-30" stroke="{TONES['green'][2]}" stroke-width="6" fill="none"/>
  <path d="M-8-38q-40-20-32-44 34 6 32 44zM4-46q40-20 48 4-34 18-48-4z" class="greenp o"/>
</g>
<g transform="translate(400 296)">
  <path d="M-50-14h100v28h-100z" class="teal o"/>
  <path d="M-50-30h100v16h-100z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M500 380v-50"/></g>''', arrow=True, ground=False)

add('berry', 'つやのある小さな実がいくつも房になっている', f'''
{table(320)}
<g transform="translate(280 240)">
  <g class="coral o">
''' + ''.join(f'<circle cx="{-70+ (i%5)*36}" cy="{-30+(i//5)*40}" r="24"/>' for i in range(10)) + f'''
    <circle cx="-16" cy="50" r="22"/><circle cx="34" cy="52" r="20"/>
  </g>
  <g fill="#fffefd" opacity="0.5">
''' + ''.join(f'<ellipse cx="{-78+ (i%5)*36}" cy="{-38+(i//5)*40}" rx="8" ry="5" transform="rotate(-30 {-78+(i%5)*36} {-38+(i//5)*40})"/>' for i in range(10)) + f'''
  </g>
  <g class="greend o">
    <path d="M-40-60q-50-20-46-44 44 4 46 44zM10-64q46-24 56 0-40 22-56 0z"/>
  </g>
</g>
<g class="coral o"><circle cx="470" cy="300" r="18"/><circle cx="504" cy="310" r="15"/></g>''', ground=False)

add('blueberry', '青紫色の小さな実にへこんだ星形の跡がある', f'''
{table(320)}
<g>
''' + ''.join(f'''<g transform="translate({160+ (i%4)*84} {230+(i//4)*66})">
  <circle r="{36-(i%3)*4}" fill="#5b5b96" class="o"/>
  <circle r="{28-(i%3)*3}" fill="#6b6bad"/>
  <g fill="none" stroke="#40406e" stroke-width="3">
''' + ''.join(f'<path d="M0 0l{13*math.cos(j*1.2566):.0f} {13*math.sin(j*1.2566):.0f}"/>' for j in range(5)) + f'''
  </g>
  <circle r="6" fill="#40406e"/>
  <ellipse cx="-14" cy="-16" rx="8" ry="5" fill="#fffefd" opacity="0.45" transform="rotate(-30 -14 -16)"/>
</g>''' for i in range(7)) + f'''
</g>
<g class="greend o"><path d="M200 190q-46-20-42-44 42 4 42 44z"/></g>''', ground=False)

add('crispy', '衣がかりっと立ったフライにフォークが当たる', f'''
{table(330)}
<g transform="translate(290 260)">
  <ellipse rx="140" ry="34" fill="#fffdf6" class="o"/>
  <path d="M-140 0q0 40 140 40t140-40z" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(270 226)">
  <path d="M-90 16q-16-40 10-56 50-30 110-12 40 12 40 44 0 30-60 34-70 6-100-10z" fill="#d9a34a" class="o"/>
  <g fill="#c8853a">
''' + ''.join(f'<path d="M{-70+i*30} {-14+(i%3)*14}l12-12 10 14z"/>' for i in range(6)) + f'''
  </g>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M150 160l-24-22M420 150l26-20M470 210h30"/>
</g>
<g transform="translate(400 170) rotate(30)">
  <path d="M-8-70h16v100h-16z" fill="#c8d0d8" class="o"/>
  <path d="M-24-70q0 26 8 26M0-70v26M24-70q0 26-8 26" fill="none" stroke="#c8d0d8" stroke-width="6" stroke-linecap="round"/>
</g>''', ground=False)

add('creamy', 'なめらかで濃い白いソースがとろりと流れる', f'''
{table(330)}
<g transform="translate(300 270)">
  <ellipse rx="140" ry="34" fill="#fffdf6" class="o"/>
  <path d="M-140 0q0 40 140 40t140-40z" fill="#fffdf6" class="o"/>
  <path d="M-100-10q60-30 130-10 50 14 60 22-50 22-130 20t-60-32z" fill="#f6ecd4" class="o"/>
</g>
<g transform="translate(300 150)">
  <path d="M-46-70h92l-12 100q-2 14-34 14t-34-14z" fill="#e8f0f6" class="o"/>
  <path d="M-40-30h80l-8 60q-2 10-32 10t-32-10z" fill="#f6ecd4"/>
</g>
<path d="M300 240q-8 40 6 60" fill="none" stroke="#f6ecd4" stroke-width="20" stroke-linecap="round"/>
<path d="M300 240q-8 40 6 60" fill="none" stroke="#e8dcbc" stroke-width="2.5"/>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M470 200l24-20M480 260h30"/>
</g>''', ground=False)

# --- 動作 -------------------------------------------------------------------
add('ape', '長い腕を持つ類人猿が木の枝にぶら下がる', f'''
<path d="M0 0h600v400H0z" fill="#cfe0d4"/>
<path d="M0 90q140 40 300 20t300-30" fill="none" stroke="{BRN}" stroke-width="18" stroke-linecap="round"/>
<g class="greenp o">
  <path d="M120 100q-40-30-20-52 34 12 20 52zM440 84q40-30 62-8-30 30-62 8z"/>
</g>
<g transform="translate(300 250)">
  <path d="M-90-110q40-24 76-2" fill="none" stroke="#5b4a3c" stroke-width="22" stroke-linecap="round"/>
  <path d="M-56 90q-46-90 0-130 56-30 112 0 46 40 0 130-56 24-112 0z" fill="#5b4a3c" class="o"/>
  <path d="M-30 66q30-46 60 0 6 40-30 40t-30-40z" fill="#a89078"/>
  <circle cx="6" cy="-96" r="50" fill="#5b4a3c" class="o"/>
  <ellipse cx="6" cy="-84" rx="34" ry="30" fill="#a89078"/>
  <circle cx="-10" cy="-104" r="5" fill="{INK}"/><circle cx="22" cy="-104" r="5" fill="{INK}"/>
  <g fill="{INK}"><circle cx="-2" cy="-84" r="3"/><circle cx="14" cy="-84" r="3"/></g>
  <path d="M-8-68q14 10 28 0" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-46-100q-24 0-24 20t24 20zM58-100q24 0 24 20t-24 20z" fill="#5b4a3c" class="o"/>
  <path d="M60-70q60-20 90 30-50 40-90-8z" fill="#5b4a3c" class="o"/>
</g>''', ground=False)

add('athletic', 'たくましい体つきで軽々と走り出す', f'''
{table(370)}
<g transform="translate(300 370)">
  <path d="M-12-10l-52 34M12-10l52 32" fill="none" stroke="{TONES['blue'][2]}" stroke-width="15" stroke-linecap="round"/>
  <path d="M-40-96q40-20 80 0l-10 90h-60z" class="coral o"/>
  <path d="M-38-86l-46 20M38-86l46-30" fill="none" stroke="{SKIN}" stroke-width="15" stroke-linecap="round"/>
  <circle cy="-126" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['cap']}" transform="translate(0 -18) scale(1.08)" fill="{TONES['blue'][0]}"/>
  <circle cx="-9" cy="-122" r="2.4" fill="{INK}"/><circle cx="9" cy="-122" r="2.4" fill="{INK}"/>
  <path d="M-8-110q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2"/>
  <g fill="none" stroke="{SKINL}" stroke-width="3"><path d="M-20-70q20 10 40 0M-18-50q18 8 36 0"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M110 220h70M90 270h50M120 320h70"/>
</g>
<g class="a" marker-end="url(#ar)" stroke-width="5"><path d="M420 200h110"/></g>''', ground=False)

add('audition', '審査員の前で歌って選考を受けている', f'''
<path d="M0 0h600v400H0z" fill="#3b3550"/>
<path d="M0 320h600v80H0z" fill="#5a4a3c" class="o"/>
{person(240, 320, 1.15, 1, 'coral', 'blue', 'up', 'bun', 'smile')}
<g transform="translate(280 236) rotate(24)">
  <path d="M-8-40h16v70h-16z" fill="#5a6270" class="o"/>
  <ellipse cy="-46" rx="18" ry="24" fill="#8f9aa6" class="o"/>
</g>
<g fill="{TONES['gold'][1]}" opacity="0.25"><path d="M240 60L120 320h240z"/></g>
{sit(450, 380, 0.8, -1, 'violet', 'blue', 'bun', 'neutral', 'lap')}
{sit(540, 380, 0.8, -1, 'teal', 'blue', 'short', 'smile', 'lap')}
<g transform="translate(470 310) rotate(-8)">
  <path d="M-34-24h68v48h-68z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}"><rect x="-24" y="-12" width="44" height="7" rx="3.5"/><rect x="-24" y="2" width="32" height="7" rx="3.5"/></g>
</g>
<g fill="{INK}">
  <g transform="translate(150 140)"><ellipse rx="12" ry="9" transform="rotate(-20)"/><path d="M10-4v-40h4v40z"/></g>
  <g transform="translate(360 110)"><ellipse rx="12" ry="9" transform="rotate(-20)"/><path d="M10-4v-40h4v40z"/></g>
</g>''', ground=False)

add('autograph', '有名人が色紙に自分のサインを書く', f'''
{table(340)}
{person(160, 340, 1.05, 1, 'coral', 'blue', 'reach', 'bun', 'smile')}
<g transform="translate(340 250) rotate(-6)">
  <path d="M-100-70h200v140h-200z" class="paper"/>
  <path d="M-70 20q40-60 70-10t60-40" fill="none" stroke="{TONES['blue'][0]}" stroke-width="6" stroke-linecap="round"/>
  <path d="M-40 44q60 14 110-10" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"/>
</g>
<g transform="translate(280 230) rotate(34)">
  <path d="M0-80l12 26v70h-24V-54z" class="teal o"/>
  <path d="M-12 16h24v40l-12 20-12-20z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M120 190l-24-20M200 170l4-26"/>
</g>
{person(510, 340, 0.85, -1, 'teal', 'violet', 'reach', 'cap', 'smile')}''', ground=False)

add('bob', '水面に浮かんだ浮きが上下にひょいひょい揺れる', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v170H0z" fill="#7aa8c4"/>
<path d="M0 230q60-20 120 0t120 0 120 0 120 0 120 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
<g fill="none" stroke="#a8c8dd" stroke-width="4"><path d="M40 290h150M400 320h160"/></g>
<g transform="translate(300 210)">
  <circle r="34" class="coral o"/>
  <path d="M-34 0a34 34 0 0 0 68 0z" fill="#fffdf6" class="o"/>
  <path d="M0-34v-30" stroke="{INK}" stroke-width="5" fill="none"/>
  <path d="M0 34v40" stroke="{MUTED}" stroke-width="3" fill="none"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8">
  <ellipse cx="300" cy="230" rx="80" ry="18"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M420 250v-70"/></g>
<g class="a" marker-end="url(#ar)"><path d="M420 180v70"/></g>''', arrow=True, ground=False)

add('crumple', '紙をくしゃくしゃに丸めて捨てる', f'''
{split()}
{table(370)}
<g transform="translate(150 210)">
  <path d="M-90-120h180v240h-180z" class="paper"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-66" y="{-90+i*36}" width="{132-(i%3)*40}" height="9" rx="4.5"/>' for i in range(5)) + f'''
  </g>
</g>
<g transform="translate(450 230)">
  <path d="M-84 20q-30-50 10-80 40-30 90-16 60 16 60 60 0 46-70 52-70 6-90-16z" fill="#fffefd" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    <path d="M-60-20l40 24-20 30M20-50l-16 40 46 10M56 20l-30 20M-30-46l30 20"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 210h60"/></g>''', arrow=True, ground=False)

add('blacken', '銀の食器がくすんで黒ずんでいく', f'''
{split()}
{table(340)}
<g transform="translate(150 250)">
  <path d="M-40-70q0-30 40-30t40 30-40 46-40-46z" fill="#e0e6ea" class="o"/>
  <path d="M-10-24h20v90q0 12-10 12t-10-12z" fill="#e0e6ea" class="o"/>
</g>
<g transform="translate(450 250)">
  <path d="M-40-70q0-30 40-30t40 30-40 46-40-46z" fill="#6a6f78" class="o"/>
  <path d="M-10-24h20v90q0 12-10 12t-10-12z" fill="#6a6f78" class="o"/>
  <g fill="#3d4149"><path d="M-24-70q24-18 48 0-24 26-48 0z"/><path d="M-8 30h16v34h-16z"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M280 130q20 20 40 0"/></g>''', arrow=True, ground=False)

add('broaden', '細い道を広げて幅の広い道にする', f'''
{split()}
<path d="M0 0h600v400H0z" fill="#dfe8d8"/>
<path d="M120 400l30-260h20l30 260z" fill="#8f9aa6" class="o"/>
<g fill="none" stroke="#fffefd" stroke-width="4" stroke-dasharray="18 16"><path d="M160 380V150"/></g>
<path d="M330 400l60-260h60l90 260z" fill="#8f9aa6" class="o"/>
<g fill="none" stroke="#fffefd" stroke-width="5" stroke-dasharray="22 18"><path d="M400 380l20-230M470 380l-20-230"/></g>
<g class="a" marker-end="url(#ar)"><path d="M330 330l-40 40"/></g>
<g class="a" marker-end="url(#ar)"><path d="M510 330l40 40"/></g>
{tree(60, 380, 0.9)}
{tree(560, 200, 0.7)}''', arrow=True, ground=False)

add('cloak', '長いマントで体をすっぽり覆い隠す', f'''
{split()}
{table(380)}
{person(150, 380, 1.15, 1, 'coral', 'blue', 'stand', 'bob', 'smile')}
<g transform="translate(450 380)">
  <path d="M-40-170q40-20 80 0l50 170h-180z" class="violetd o"/>
  <path d="M-40-170q0-40 40-40t40 40q-30 30-80 0z" class="violetd o"/>
  <path d="M-34-160q34 24 68 0" fill="none" stroke="{TONES['violet'][2]}" stroke-width="3"/>
  <path d="M0-190q-30 20-30 44 30 14 60 0 0-24-30-44z" fill="{INK}" opacity="0.75"/>
  <circle cx="-14" cy="-166" r="4" fill="#fffefd"/><circle cx="14" cy="-166" r="4" fill="#fffefd"/>
  <g fill="none" stroke="{TONES['violet'][2]}" stroke-width="3"><path d="M-60-60q60 26 120 0M-76-10q76 30 152 0"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('converge', 'ばらばらの道が一点に集まってくる', f'''
<path d="M0 0h600v400H0z" fill="#eef2f6"/>
<g fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round">
  <path d="M40 60L280 190M40 340L280 210M60 200h220M300 40v130M300 360V230M540 70L320 190M540 330L320 210"/>
</g>
<circle cx="300" cy="200" r="40" class="coral o"/>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5">
  <path d="M120 110l100 56M120 300l100-56M140 200h100M300 100v60M300 300v-60M470 110l-100 56M470 300l-100-56"/>
</g>''', ground=False)

add('contradict', 'ひとりの言うことを、もうひとりが真っ向から否定する', f'''
{table(370)}
{person(150, 370, 1.05, 1, 'teal', 'blue', 'point', 'bun', 'neutral')}
{person(450, 370, 1.05, -1, 'coral', 'blue', 'point', 'short', 'sad')}
<g transform="translate(240 170)">
  <path d="M-60-40h120q12 0 12 12v40q0 12-12 12h-84l-22 16v-16q-14 0-14-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}"><rect x="-42" y="-16" width="84" height="9" rx="4.5"/><rect x="-42" y="4" width="56" height="9" rx="4.5"/></g>
</g>
<g transform="translate(400 250)">
  <path d="M60-40H-60q-12 0-12 12v40q0 12 12 12h84l22 16v-16q14 0 14-12v-40q0-12-12-12z" fill="#fffefd" class="o"/>
  <g fill="{TONES['coral'][0]}"><rect x="-42" y="-16" width="84" height="9" rx="4.5"/><rect x="-14" y="4" width="56" height="9" rx="4.5"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round">
  <path d="M290 300l50 50M340 300l-50 50"/>
</g>''', ground=False)

add('abridge', '分厚い原書を短くまとめた薄い版にする', f'''
{split()}
{table(360)}
<g transform="translate(150 250)">
  <path d="M-90-130h180v190h-180z" fill="#fffdf6" class="o"/>
  <path d="M-90-130h30v190h-30z" class="coral o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">
''' + ''.join(f'<path d="M-56 {-110+i*16}h130"/>' for i in range(12)) + f'''
  </g>
  <path d="M-96 60h192v14h-192z" fill="#d6cec0" class="o"/>
</g>
<g transform="translate(450 290)">
  <path d="M-70-50h140v70h-140z" fill="#fffdf6" class="o"/>
  <path d="M-70-50h24v70h-24z" class="coral o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">
''' + ''.join(f'<path d="M-40 {-32+i*16}h100"/>' for i in range(4)) + f'''
  </g>
  <path d="M-76 20h152v12h-152z" fill="#d6cec0" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('alleviate', '痛みのある人に薬を渡して苦しみをやわらげる', f'''
{split()}
{table(370)}
{person(150, 370, 1.05, 1, 'gold', 'blue', 'up', 'bob', 'sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M104 210l-26-20M196 200l26-20M150 160v-26"/>
</g>
<g class="coral o" opacity="0.5"><circle cx="150" cy="250" r="40"/></g>
{person(450, 370, 1.05, 1, 'gold', 'blue', 'stand', 'bob', 'smile')}
<g class="coral o" opacity="0.18"><circle cx="450" cy="250" r="22"/></g>
<g transform="translate(300 130)">
  <path d="M-34-20h68v40h-68z" fill="#fffdf6" class="o"/>
  <path d="M-34-20l10-14h68l-10 14z" fill="#f0eee6" class="o"/>
  <path d="M-6-12h12v10h10v12h-10v10h-12v-10h-10v-12h10z" class="coral"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('amplify', '小さな音がアンプを通って大きな音になる', f'''
{table(370)}
<g transform="translate(120 260)">
  <path d="M-8-40h16v70h-16z" fill="#5a6270" class="o"/>
  <ellipse cy="-46" rx="16" ry="22" fill="#8f9aa6" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M160 200q16 20 0 40M182 190q26 32 0 64"/>
</g>
<g transform="translate(300 260)">
  <path d="M-60-70h120v140h-120z" fill="#3b4450" class="o"/>
  <circle cy="-24" r="26" fill="#8f9aa6" class="o"/><circle cy="-24" r="11" fill="{INK}"/>
  <g fill="#c8d0d8" class="o"><circle cx="-30" cy="40" r="12"/><circle cx="0" cy="40" r="12"/><circle cx="30" cy="40" r="12"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M390 160q40 40 0 200M440 130q56 70 0 260M490 100q72 100 0 320"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M200 130h180"/></g>''', arrow=True, ground=False)

add('appraise', '宝石を拡大鏡でのぞいて値打ちを見きわめる', f'''
{table(340)}
<g transform="translate(250 260)">
  <path d="M-46 0l20-40h52l20 40-46 50z" class="tealp o"/>
  <path d="M-26-40l14 40h64l14-40M-46 0h92" fill="none" stroke="{TONES['teal'][2]}" stroke-width="3"/>
</g>
<g transform="translate(340 180) rotate(30)">
  <circle r="60" fill="#e8f0f6" class="o" opacity="0.8"/>
  <circle r="60" fill="none" stroke="#8f9aa6" stroke-width="10"/>
  <path d="M44 44l50 50" stroke="{INK}" stroke-width="14" stroke-linecap="round" fill="none"/>
</g>
{person(500, 340, 0.9, -1, 'violet', 'blue', 'hold', 'bun', 'neutral')}
<g transform="translate(140 250) rotate(-8)">
  <path d="M-40-30h80v60h-80z" class="paper"/>
  <g fill="{MUTED}"><rect x="-28" y="-16" width="56" height="8" rx="4"/></g>
  <rect x="-28" y="2" width="34" height="12" rx="6" class="gold"/>
</g>''', ground=False)

add('bolster', '傾いた棚を支え木で下から補強する', f'''
{table(380)}
<g transform="translate(300 250) rotate(-8)">
  <path d="M-160-30h320v40h-320z" fill="#c9a464" class="o"/>
  <g class="o">
    <rect x="-120" y="-80" width="46" height="50" class="tealp"/>
    <rect x="-60" y="-90" width="46" height="60" class="coralp"/>
    <rect x="10" y="-76" width="46" height="46" class="goldp"/>
  </g>
</g>
<g fill="#8b6437" class="o">
  <path d="M310 262h24v120h-24z"/>
  <path d="M180 276l24-6 30 116-24 6z"/>
  <path d="M440 250h24v130h-24z"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 380v-90"/></g>
<g class="a" marker-end="url(#ar)"><path d="M520 380v-110"/></g>''', arrow=True, ground=False)

add('certify', '書類に印を押して正式に証明する', f'''
{table(350)}
<g transform="translate(280 220) rotate(-4)">
  <path d="M-140-120h280v240h-280z" class="paper"/>
  <rect x="-100" y="-94" width="140" height="16" rx="8" fill="{INK}"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-100" y="{-56+i*28}" width="{200-(i%3)*40}" height="9" rx="4.5"/>' for i in range(4)) + f'''
  </g>
  <g transform="translate(70 74)">
    <circle r="42" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
    <circle r="28" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
    <path d="M-16 0l10 12 22-26" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <path d="M-100 60q40-24 66 0t54-10" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"/>
</g>
<g transform="translate(470 200) rotate(14)">
  <path d="M-26-70h52v60h-52z" fill="#8b6437" class="o"/>
  <path d="M-40-10h80v24h-80z" fill="{INK}"/>
</g>''', ground=False)

add('broker', '売り手と買い手の間に立って取引をまとめる', f'''
{table(370)}
{person(120, 370, 0.95, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{person(480, 370, 0.95, -1, 'coral', 'violet', 'give', 'bun', 'smile')}
{person(300, 370, 1.05, 1, 'gold', 'blue', 'up', 'cap', 'smile')}
<g transform="translate(200 250)">
  <path d="M-40-30h80v60h-80z" class="tealp o"/>
</g>
<g transform="translate(400 250)">
  <path d="M-46-26h92v52h-92z" class="greenp o"/>
  <circle r="15" fill="none" stroke="{TONES['green'][2]}" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 200q70-40 140 0"/></g>
<g class="a" marker-end="url(#ar)"><path d="M370 320q-70 30-140 0"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M300 250v-40"/></g>''', arrow=True, ground=False)

add('collate', 'ばらばらの資料を順番にそろえて一つにまとめる', f'''
{split()}
{table(370)}
<g>
''' + ''.join(f'<g transform="translate({100+ (i%3)*54} {200+(i//3)*70}) rotate({-24+i*11})">{doc(0, 0, 76, 96, 3)}</g>' for i in range(6)) + f'''
</g>
<g>
''' + ''.join(f'<g transform="translate({450+i*4} {260-i*10})">{doc(0, 0, 130, 170, 4)}</g>' for i in range(4)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('corroborate', '二人目の証言が一人目の話を裏づける', f'''
{table(370)}
{person(130, 370, 1.0, 1, 'teal', 'blue', 'point', 'bun', 'neutral')}
{person(300, 370, 1.0, 1, 'coral', 'blue', 'point', 'short', 'smile')}
<g transform="translate(220 170)">
  <path d="M-60-40h120q12 0 12 12v40q0 12-12 12h-84l-22 16v-16q-14 0-14-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}"><rect x="-42" y="-16" width="84" height="9" rx="4.5"/><rect x="-42" y="4" width="56" height="9" rx="4.5"/></g>
</g>
<g transform="translate(400 240)">
  <path d="M-60-40h120q12 0 12 12v40q0 12-12 12h-84l-22 16v-16q-14 0-14-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}"><rect x="-42" y="-16" width="84" height="9" rx="4.5"/><rect x="-42" y="4" width="56" height="9" rx="4.5"/></g>
</g>
{tick(510, 190, 0.9)}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="4" stroke-dasharray="8 8"><path d="M290 180h60"/></g>''', ground=False)

add('conform', 'そろった列に合わせて、はみ出た一人が同じ形になる', f'''
{split()}
{table(380)}
''' + ''.join(person(70+i*80, 380, 0.85, 1, 'blue', 'blue', 'stand', 'short', 'neutral') for i in [0, 1]) + f'''
{person(230, 380, 0.85, 1, 'coral', 'gold', 'up', 'bun', 'smile')}
''' + ''.join(person(370+i*80, 380, 0.85, 1, 'blue', 'blue', 'stand', 'short', 'neutral') for i in range(3)) + f'''
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M40 250h520"/></g>
<g class="a" marker-end="url(#ar)"><path d="M270 160h60"/></g>''', arrow=True, ground=False)

add('counterattack', '攻められた側が押し返して反撃に出る', f'''
{table(380)}
{person(140, 380, 1.05, 1, 'coral', 'blue', 'reach', 'cap', 'neutral')}
{person(460, 380, 1.05, -1, 'teal', 'blue', 'reach', 'cap', 'neutral')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M210 180h180"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['teal'][0]}" stroke-width="7"><path d="M390 280H210"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M300 60v300"/></g>''', ground=False)

add('accidental', 'わざとではなく、うっかりコップを倒してしまう', f'''
{table(340)}
<g transform="translate(360 300) rotate(-70)">
  <path d="M-36-50h72l-10 90q-2 12-26 12t-26-12z" fill="#e8f0f6" class="o"/>
</g>
<g fill="{TONES['blue'][1]}" stroke="{TONES['blue'][0]}" stroke-width="2">
  <path d="M400 300q60-20 120 10-40 20-120 6z"/>
</g>
{person(180, 340, 1.05, 1, 'teal', 'blue', 'reach', 'bob', 'surprised')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M140 190l-24-20M220 170l4-26"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 200q60 30 60 70"/></g>
{cross(500, 150, 0.7)}
<g transform="translate(500 150)">
  <circle r="52" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
</g>''', arrow=True, ground=False)

add('childish', '大人が子どものように床で足をばたつかせて怒る', f'''
{table(380)}
<g transform="translate(300 370) rotate(-90)">
  <path d="M-12-8l-30 33M12-8l32 28" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-27-78q27-14 54 0l-8 72h-38z" class="coral o"/>
  <path d="M-24-70l-32 22M24-70l34 18" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cy="-108" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="scale(1.06)" fill="{HAIR}"/>
  <path d="M-14-108q8-10 16 0M-2-108q8-10 16 0" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <path d="M-10-88q10 12 20 0z" fill="{INK}" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M180 200l-26-24M400 190l26-22M170 300l-30 20"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M420 300q30 20 40 44M460 260q34 24 44 50"/>
</g>''', ground=False)

add('century', '百年ごとに区切られた長い時間の帯', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(300 200)">
  <path d="M-260-40h520v80h-520z" fill="#e0d6c0" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="4">
''' + ''.join(f'<path d="M{-260+i*104} -40v80"/>' for i in range(6)) + f'''
  </g>
  <g class="tealp o">
''' + ''.join(f'<rect x="{-254+i*104}" y="-34" width="92" height="68"/>' for i in range(5)) + f'''
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="2">
''' + ''.join(f'<path d="M{-250+i*10} -34v10"/>' for i in range(51)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M46 300h96"/></g>
<g class="a" marker-end="url(#ar)"><path d="M142 300H46"/></g>
<g transform="translate(300 90)">
  <circle r="40" fill="#fffdf6" class="o"/>
  <path d="M0 0v-26M0 0l18 12" stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none"/>
</g>''', arrow=True, ground=False)

add('comma', '文の途中で息を入れる小さな点', f'''
{table(370)}
<g transform="translate(300 190)">
  <path d="M-240-100h480v200h-480z" class="paper"/>
  <g fill="{INK}">
    <rect x="-200" y="-56" width="130" height="14" rx="7"/>
    <rect x="-52" y="-56" width="90" height="14" rx="7"/>
    <rect x="76" y="-56" width="120" height="14" rx="7"/>
    <rect x="-200" y="4" width="100" height="14" rx="7"/>
    <rect x="-82" y="4" width="150" height="14" rx="7"/>
  </g>
  <g class="coral">
    <path d="M46-38q14 0 14 12t-14 20q4-10-2-14t2-18z" transform="scale(1.6) translate(-18 -8)"/>
  </g>
</g>
<circle cx="374" cy="152" r="46" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M480 320l-80-130"/></g>''', arrow=True, ground=False)

# --- 句動詞（前置詞の向きを矢印で） -------------------------------------------
add('branch-out', '一本の幹から新しい枝が外へ伸びていく', f'''
{table(380)}
<g transform="translate(300 380)">
  <path d="M-24 0h48v-140h-48z" fill="{BRN}" class="o"/>
  <g stroke="{BRN}" stroke-width="14" stroke-linecap="round" fill="none">
    <path d="M0-140l-80-60M0-140l80-60"/>
  </g>
  <g class="greenp o"><circle cx="-90" cy="-210" r="42"/><circle cx="90" cy="-210" r="42"/></g>
  <g stroke="{TONES['coral'][0]}" stroke-width="12" stroke-linecap="round" fill="none">
    <path d="M0-160l-150-30M0-170l150-40"/>
  </g>
  <g class="coralp o"><circle cx="-166" cy="-196" r="34"/><circle cx="166" cy="-216" r="34"/></g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M300 100h140"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M300 100H160"/></g>''', arrow=True, ground=False)

add('call-in', '手におえないので専門家を呼び入れる', f'''
{table(380)}
<g transform="translate(180 260)">
  <path d="M-90-60h180v130h-180z" fill="#8f9aa6" class="o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
    <path d="M-40-20l50 40M10-20l-50 40"/>
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"><path d="M40 20q20-20 0-40"/></g>
</g>
{person(140, 380, 0.9, 1, 'blue', 'blue', 'up', 'bun', 'sad')}
{person(470, 380, 1.0, -1, 'gold', 'blue', 'walk', 'cap', 'smile', 'walk')}
<g transform="translate(520 280) rotate(-16)">
  <path d="M-30-10h60v20h-60z" fill="{INK}"/>
  <path d="M30-16h30v32H30z" fill="#8f9aa6" class="o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke-width="6"><path d="M430 180H260"/></g>''', ground=False)

add('chip-in', 'みんなが少しずつお金を出し合って一つにする', f'''
{table(380)}
<g transform="translate(300 300)">
  <path d="M-70-40h140v70q0 14-70 14t-70-14z" class="goldp o"/>
  <path d="M-70-40q0-16 70-16t70 16z" class="gold o"/>
  <path d="M-24-56h48v-14h-48z" fill="{INK}"/>
</g>
{coin(190, 190, 22)}
{coin(300, 160, 22)}
{coin(410, 190, 22)}
<g class="a" marker-end="url(#ar)"><path d="M190 220q30 30 70 40M300 190v40M410 220q-30 30-70 40"/></g>
{head(110, 330, 20, 'coral', 'bob')}
{head(300, 380, 20, 'teal', 'short')}
{head(500, 330, 20, 'violet', 'bun')}''', arrow=True, ground=False)

add('come-by', '道を通りかかって珍しい品をふと手に入れる', f'''
<path d="M0 0h600v250H0z" fill="#dceaf4"/>
<path d="M0 250h600v150H0z" fill="#dfe8d8"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M0 340h600v20H0z" fill="#c9a464" class="o"/>
<g transform="translate(450 300)">
  <path d="M-90-40h180v40h-180z" fill="#c9a464" class="o"/>
  <path d="M-100-40h200v-16h-200z" class="coral o"/>
  <g class="o">
    <rect x="-70" y="-70" width="34" height="30" class="tealp"/>
    <rect x="-20" y="-76" width="34" height="36" class="goldp"/>
    <rect x="30" y="-68" width="34" height="28" class="violetp"/>
  </g>
</g>
{person(200, 340, 1.0, 1, 'teal', 'blue', 'reach', 'bob', 'smile', 'walk')}
<g transform="translate(280 250) rotate(-10)">
  <path d="M-26-22h52v44h-52z" class="goldp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M360 200L280 236"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M60 370h480"/></g>''', arrow=True, ground=False)

add('crop-up', '平らな地面から問題がふいに突き出してくる', f'''
<path d="M0 0h600v260H0z" fill="#dceaf4"/>
<path d="M0 260h600v140H0z" fill="#c9d8c0"/>
<path d="M0 260h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(330 260)">
  <path d="M-70 0q30-40 70-40t70 40z" fill="#a8845c" class="o"/>
  <path d="M0-30l40 70h-80z" class="coral o"/>
  <path d="M-4-14h8v30h-8z" fill="#fffefd"/>
  <circle cy="26" r="4" fill="#fffefd"/>
</g>
<g fill="#a8845c" class="o">
  <path d="M240 254l24-14 8 20z"/><path d="M420 250l26 12-22 12z"/>
</g>
{person(130, 260, 0.9, 1, 'teal', 'blue', 'up', 'bun', 'surprised')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M330 200v-70"/></g>''', ground=False)

add('work-on', '書きかけの絵に少しずつ手を入れていく', f'''
{table(380)}
<g transform="translate(340 210) rotate(-4)">
  <path d="M-140-120h280v240h-280z" fill="#fffdf6" class="o"/>
  <path d="M-100 60L-30-40l50 60 40-70 70 110z" class="greenp o"/>
  <circle cx="70" cy="-64" r="24" class="goldp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M-100-90h180M-100-50h120"/></g>
</g>
<g transform="translate(340 350)">
  <path d="M-20 30l40-160M20 30L-20-130" fill="none" stroke="{BRN}" stroke-width="12" stroke-linecap="round"/>
</g>
{person(140, 380, 1.0, 1, 'violet', 'blue', 'reach', 'bun', 'smile')}
<g transform="translate(210 250) rotate(30)">
  <path d="M0-70l10 24v70h-20V-46z" class="coral o"/>
  <path d="M-10 24h20v34l-10 20-10-20z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8" marker-end="url(#ar)"><path d="M470 120q40 40 0 80"/></g>
<g class="a" marker-end="url(#ar)"><path d="M480 110q50 50 0 100"/></g>''', arrow=True, ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
