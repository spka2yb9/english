# -*- coding: utf-8 -*-
"""第128回。de-/dis- の動詞と日常の名詞。de-/dis- は「元の状態 → 取り除いた状態」で描く。"""
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

# --- 食べ物・物 --------------------------------------------------------------
add('crunchy', 'かたい野菜スティックをぼりぼりとかむ', f'''
{table(330)}
<g transform="translate(400 270)">
  <path d="M-70-30h140v40q0 12-70 12t-70-12z" fill="#fffdf6" class="o"/>
  <g class="o">
    <path d="M-50-110h24v84h-24z" fill="#e8983a"/><path d="M-16-100h24v74h-24z" fill="#e8983a"/>
    <path d="M14-114h22v88H14z" class="green"/><path d="M42-96v70h22v-70z" class="green"/>
  </g>
</g>
<g transform="translate(180 210)">
  <circle r="90" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-78-26q6-64 78-64t78 64q-38-30-78-30t-78 30z" fill="{HAIR}"/>
  <path d="M-52 0q16-14 30 0M22 0q16-14 30 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <path d="M-26 40q26 28 52 0-26 10-52 0z" fill="{INK}" class="o"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M290 130l24-22M300 210h30M290 290l24 22"/>
</g>''', ground=False)

add('dessert', '食事のあとに出る甘いケーキ', f'''
{table(340)}
<g transform="translate(300 260)">
  <ellipse rx="120" ry="30" fill="#fffdf6" class="o"/>
  <path d="M-120 0q0 34 120 34t120-34z" fill="#fffdf6" class="o"/>
  <g transform="translate(0 -40)">
    <path d="M-64 30h128l-10-70h-108z" fill="#f6e0c0" class="o"/>
    <path d="M-74-40h148l-8-30h-132z" class="coralp o"/>
    <path d="M-74-70q0-24 74-24t74 24z" class="coral o"/>
    <circle cx="0" cy="-96" r="14" class="corald o"/>
    <path d="M-40-10h80" fill="none" stroke="#e0c8a0" stroke-width="3"/>
  </g>
</g>
<g transform="translate(460 300) rotate(20)">
  <path d="M-6-70h12v90h-12z" fill="#c8d0d8" class="o"/>
  <ellipse cy="-80" rx="18" ry="26" fill="#c8d0d8" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 120h100"/></g>
<g transform="translate(80 120)">
  <ellipse rx="46" ry="12" fill="#fffdf6" class="o"/>
  <path d="M-46 0q0 16 46 16t46-16z" fill="#fffdf6" class="o"/>
</g>''', arrow=True, ground=False)

add('earring', '耳たぶに下がった小さな飾り', f'''
{table(380)}
<g transform="translate(300 200)">
  <circle r="130" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-116-40q10-90 116-90t116 90q-30-46-116-46t-116 46z" fill="{HAIR}"/>
  <path d="M-118-40q-40 100-16 150 30 22 40-20M118-40q40 100 16 150-30 22-40-20" fill="{HAIR}"/>
  <circle cx="-52" cy="-10" r="8" fill="{INK}"/><circle cx="52" cy="-10" r="8" fill="{INK}"/>
  <path d="M-24 56q24 20 48 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <ellipse cx="-126" cy="20" rx="18" ry="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <ellipse cx="126" cy="20" rx="18" ry="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g>
  <path d="M174 236v22M426 236v22" stroke="{TONES['gold'][2]}" stroke-width="4" fill="none"/>
  <circle cx="174" cy="272" r="18" class="gold o"/>
  <circle cx="426" cy="272" r="18" class="gold o"/>
  <circle cx="174" cy="272" r="8" class="tealp o"/>
  <circle cx="426" cy="272" r="8" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M500 350l-60-64"/></g>''', arrow=True, ground=False)

add('dock', '船が埠頭に横づけして荷を降ろす', f'''
<path d="M0 0h600v210H0z" fill="#dceaf4"/>
<path d="M0 210h600v190H0z" fill="#7aa8c4"/>
<path d="M0 210h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M0 210h230v190H0z" fill="#c9a464" class="o"/>
<g fill="none" stroke="#a0764a" stroke-width="3">
''' + ''.join(f'<path d="M0 {240+i*40}h230"/>' for i in range(4)) + f'''
</g>
<g transform="translate(400 250)">
  <path d="M-160 0h320l-40 70q-6 12-120 12T-120 70z" class="blue o"/>
  <path d="M-130-70h260v70h-260z" fill="#fffdf6" class="o"/>
  <g class="bluep o">
''' + ''.join(f'<rect x="{-110+i*54}" y="-54" width="40" height="34"/>' for i in range(4)) + f'''
  </g>
  <path d="M100-130h20v60h-20z" class="coral o"/>
</g>
<g fill="{INK}">
  <path d="M228 250h40v6h-40zM228 320h40v6h-40z"/>
</g>
{box(120, 300, 90, 60, 20, 'gold')}
{box(120, 220, 80, 52, 18, 'teal')}
<g class="a" marker-end="url(#ar)"><path d="M320 160l-90 40"/></g>''', arrow=True, ground=False)

# --- de- / dis- の動詞 --------------------------------------------------------
add('darken', '明るい空が日が沈んで暗くなる', f'''
{split()}
<path d="M0 0h300v400H0z" fill="#dceaf4"/>
<path d="M300 0h300v400H300z" fill="#3b4450"/>
<path d="M0 300h300v100H0z" fill="#dfe8d8"/>
<path d="M300 300h300v100H300z" fill="#2c333d"/>
{sun(150, 100, 40)}
<circle cx="450" cy="100" r="30" fill="#f0e6c0" class="o"/>
<g fill="#dcd0a8"><circle cx="440" cy="90" r="7"/><circle cx="460" cy="110" r="5"/></g>
{tree(80, 300, 0.9)}
<g opacity="0.5">{tree(380, 300, 0.9)}</g>
<g fill="#fffefd"><circle cx="520" cy="60" r="4"/><circle cx="560" cy="130" r="3"/><circle cx="350" cy="60" r="3"/></g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('dampen', '乾いた布を湿らせてしっとりさせる', f'''
{split()}
{table(340)}
<g transform="translate(150 250)">
  <path d="M-80-70h160v140h-160z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-80-20h160M-80 30h160"/></g>
</g>
<g transform="translate(450 250)">
  <path d="M-80-70h160v140h-160z" fill="#c8d4dc" class="o"/>
  <g fill="none" stroke="#a8b8c4" stroke-width="3"><path d="M-80-20h160M-80 30h160"/></g>
  <g fill="{TONES['blue'][0]}" opacity="0.5"><circle cx="-40" cy="-30" r="14"/><circle cx="20" cy="10" r="18"/><circle cx="50" cy="-40" r="12"/></g>
</g>
<g transform="translate(430 120) rotate(30)">
  <path d="M-24 0h48l-6 50q-2 10-18 10t-18-10z" fill="#e8f0f6" class="o"/>
  <path d="M-24 0q0-16 24-16t24 16z" fill="#b8bfc8" class="o"/>
  <g fill="{INK}"><circle cx="-8" cy="-8" r="2.5"/><circle cx="8" cy="-8" r="2.5"/></g>
</g>
<g fill="{TONES['blue'][0]}">
''' + ''.join(f'<path d="M{436+i*14} {180+ (i%2)*16}q7 8 7 14t-7 6-7-6 7-14z"/>' for i in range(4)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('deepen', '浅い穴をさらに掘り下げて深くする', f'''
{split()}
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v170H0z" fill="#a8845c"/>
<path d="M0 218h600v14H0z" fill="#dfe8d8"/>
<path d="M0 218h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M80 232q0 40 70 40t70-40z" fill="#6b4c28" class="o"/>
<path d="M380 232q0 130 70 130t70-130z" fill="#6b4c28" class="o"/>
<g class="a" marker-end="url(#ar)"><path d="M450 300v70"/></g>
<g transform="translate(300 150) rotate(20)">
  <path d="M-8-70h16v90h-16z" fill="#c9a464" class="o"/>
  <path d="M-30 20h60l-10 46h-40z" fill="#8f9aa6" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M40 272h520"/></g>''', arrow=True, ground=False)

add('dent', '車のドアがぶつかってへこんでいる', f'''
{table(370)}
<g transform="translate(320 300)">
  <path d="M-180 30h360v-56q0-20-20-20h-90l-44-44H-104l-30 44h-26q-20 0-20 20z" class="teal o"/>
  <path d="M-100-46h130l34 44H-130z" fill="#dceaf4" class="o"/>
  <circle cx="-110" cy="30" r="26" fill="{INK}"/><circle cx="110" cy="30" r="26" fill="{INK}"/>
  <path d="M-20 6q-40-4-46 20t46 22 50-22-50-20z" fill="{TONES['teal'][2]}"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="3">
    <path d="M-56 20q56-12 106 8M-50 36q52-8 96 8"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M300 170v70"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M240 190l-26-20M370 180l26-18"/>
</g>''', arrow=True, ground=False)

add('deserted', 'にぎわっていた広場から人がいなくなり、がらんとする', f'''
{split()}
{table(380)}
''' + ''.join(person(60+i*40, 380, 0.5, 1 if i%2 else -1, ['coral','teal','gold','violet','blue'][i%5], 'blue', 'stand', ['short','bob','bun','cap'][i%4], 'smile') for i in range(6)) + f'''
''' + ''.join(person(70+i*46, 320, 0.42, -1 if i%2 else 1, ['teal','gold','violet','coral'][i%4], 'blue', 'stand', ['bob','short','cap','bun'][i%4], 'smile') for i in range(5)) + f'''
<g transform="translate(450 340)">
  <path d="M-80-14h160v14h-160z" fill="#c9a464" class="o"/>
  <path d="M-60 0v20M60 0v20" stroke="#8b6437" stroke-width="9" stroke-linecap="round" fill="none"/>
</g>
<g fill="{MUTED}" opacity="0.4">
  <path d="M340 370q40-20 60 0-30 16-60 0z"/><path d="M520 350q30-14 44 0-22 12-44 0z"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M380 200q60-20 110 0"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 150h60"/></g>''', arrow=True, ground=False)

add('deter', '高いさくと警告板が人を近づけさせない', f'''
{table(380)}
<g transform="translate(360 380)">
  <path d="M-160-14h320v14h-320z" fill="#8f9aa6" class="o"/>
  <g stroke="#8f9aa6" stroke-width="12" stroke-linecap="round" fill="none">
''' + ''.join(f'<path d="M{-140+i*40} 0v-190"/>' for i in range(8)) + f'''
    <path d="M-160-160h320M-160-100h320"/>
  </g>
</g>
<g transform="translate(300 190)">
  <path d="M0-56l64 106H-64z" class="gold o"/>
  <path d="M-5-14h10v34h-10z" fill="{INK}"/>
  <circle cy="34" r="5" fill="{INK}"/>
</g>
{person(120, 380, 1.0, 1, 'coral', 'blue', 'up', 'bob', 'sad')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M230 250h-70"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M180 250h60"/></g>''', ground=False)

add('devalue', '同じ札束で買えるものが減っていく', f'''
{split()}
{table(340)}
<g transform="translate(150 190)">
  <path d="M-70-34h140v68h-140z" class="greenp o"/>
  <circle r="20" fill="none" stroke="{TONES['green'][2]}" stroke-width="3"/>
</g>
<g>
''' + ''.join(f'<g transform="translate({80+ (i%3)*70} {300+(i//3)*0})">{box(0, 0, 56, 40, 14, "gold")}</g>' for i in range(3)) + f'''
</g>
<g transform="translate(450 190)">
  <path d="M-70-34h140v68h-140z" class="greenp o"/>
  <circle r="20" fill="none" stroke="{TONES['green'][2]}" stroke-width="3"/>
</g>
{box(450, 300, 56, 40, 14, 'gold')}
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M520 260v60"/></g>''', arrow=True, ground=False)

add('deviate', '決められた線から外れて別の方向へそれる', f'''
{table(380)}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="20 16"><path d="M40 240h520"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['teal'][0]}" stroke-width="6"><path d="M60 240h230"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M290 240q90 0 200-100"/></g>
<circle cx="290" cy="240" r="14" fill="{INK}"/>
{person(200, 300, 0.62, 1, 'teal', 'blue', 'walk', 'cap', 'neutral', 'walk')}
{person(420, 220, 0.62, 1, 'coral', 'blue', 'walk', 'bob', 'neutral', 'walk')}''', ground=False)

add('disband', '組んでいたチームが解散してばらばらになる', f'''
{split()}
{table(380)}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="12 10"><ellipse cx="150" cy="290" rx="120" ry="90"/></g>
{head(90, 250, 22, 'coral', 'short')}
{head(150, 232, 22, 'teal', 'bun')}
{head(210, 250, 22, 'gold', 'cap')}
{head(120, 320, 22, 'violet', 'bob')}
{head(190, 320, 22, 'green', 'short')}
{head(370, 130, 20, 'coral', 'short')}
{head(560, 180, 20, 'teal', 'bun')}
{head(340, 340, 20, 'gold', 'cap')}
{head(470, 300, 20, 'violet', 'bob')}
{head(540, 360, 20, 'green', 'short')}
<g class="a" marker-end="url(#ar)" stroke="{MUTED}">
  <path d="M420 220l-50-60M440 230l100-30M410 250l-40 70M450 250l30 30"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('disguise', 'かつらと眼鏡とひげで別人に見せかける', f'''
{split()}
{table(380)}
{person(150, 380, 1.15, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(450, 380, 1.15, 1, 'coral', 'blue', 'stand', 'short', 'smile')}
<g transform="translate(450 254)">
  <path d="M-32-32q6-32 32-32t32 32q-24-6-32 6-16-14-32-6z" fill="#c8703a"/>
  <path d="M-34-30q-16 30-6 60 14 6 18-16M34-30q16 30 6 60-14 6-18-16" fill="#c8703a"/>
  <circle cx="-11" r="12" fill="none" stroke="{INK}" stroke-width="4"/>
  <circle cx="11" r="12" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-1 0h2M-23-2l-12-6M23-2l12-6" stroke="{INK}" stroke-width="4" fill="none"/>
  <path d="M-16 24q16 10 32 0 6 14-16 16t-16-16z" fill="{HAIR}"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('disinfect', '傷口を消毒液でふいて菌を取り除く', f'''
{table(360)}
<g transform="translate(280 250)">
  <path d="M-160 20q80-30 300 0" stroke="{SKIN}" stroke-width="70" stroke-linecap="round" fill="none"/>
  <path d="M-160 20q80-30 300 0" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-10-6q30-14 50 6-24 24-50-6z" class="coral o"/>
</g>
<g transform="translate(320 180) rotate(20)">
  <ellipse rx="34" ry="26" fill="#fffefd" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5"><path d="M-20-10h40M-20 10h40"/></g>
</g>
<g transform="translate(480 260)">
  <path d="M-30-60h60v90q0 14-30 14t-30-14z" fill="#e8f0f6" class="o"/>
  <path d="M-14-60v-16h28v16z" class="green o"/>
  <path d="M-24-24h48v46q0 10-24 10t-24-10z" fill="{TONES['green'][1]}"/>
  <path d="M-8 0h16" stroke="{TONES['green'][0]}" stroke-width="4" fill="none"/>
</g>
<g fill="{INK}" opacity="0.5">
''' + ''.join(f'<circle cx="{160+i*26}" cy="{130+(i%3)*20}" r="6"/>' for i in range(5)) + f'''
</g>
{cross(200, 150, 0.6)}''', ground=False)

add('dislodge', '歯にはさまった物を取り除く', f'''
{table(380)}
<g transform="translate(300 220)">
  <path d="M-200 60q0-90 200-90t200 90z" fill="#c4604a" class="o"/>
  <g fill="#fffdf6" class="o">
''' + ''.join(f'<path d="M{-170+i*50} 30q0-40 40-40t40 40q0 24-40 24t-40-24z" transform="translate(0 -20)"/>' for i in range(7)) + f'''
  </g>
  <path d="M-24-24h18v34h-18z" class="green o"/>
</g>
<g transform="translate(310 130) rotate(10)">
  <path d="M-4-90h8v70h-8z" fill="#c8d0d8" class="o"/>
  <path d="M-4-20l-4 30 8 0 4-30z" fill="#c8d0d8" class="o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M420 250l-100-40"/></g>
<g class="green o"><path d="M470 300h20v30h-20z" transform="rotate(30 480 315)"/></g>''', ground=False)

add('disperse', '集まっていた人の群れが四方へ散っていく', f'''
{split()}
{table(380)}
<g>
''' + ''.join(head(110+ (i%4)*30, 260+(i//4)*40, 18, ['coral','teal','gold','violet'][i%4], ['short','bob','bun','cap'][i%4]) for i in range(12)) + f'''
</g>
<g>
{head(350, 110, 18, 'coral', 'short')}
{head(560, 160, 18, 'teal', 'bob')}
{head(340, 340, 18, 'gold', 'bun')}
{head(500, 320, 18, 'violet', 'cap')}
{head(430, 210, 18, 'green', 'short')}
{head(570, 380, 18, 'blue', 'bob')}
</g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}">
  <path d="M430 250l-70-100M450 240l100-60M420 270l-60 50M460 260l30 40"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('disqualify', '規則違反で選手が失格になり試合から外される', f'''
{table(380)}
<path d="M0 340h600v40H0z" fill="#c8703a" class="o"/>
<g fill="none" stroke="#fffefd" stroke-width="4"><path d="M0 360h600"/></g>
{person(200, 340, 1.0, 1, 'coral', 'blue', 'stand', 'cap', 'sad')}
<g transform="translate(200 250)">
  <path d="M-30-40h60v60h-60z" fill="#fffdf6" class="o"/>
  <rect x="-16" y="-20" width="32" height="18" rx="4" fill="{INK}"/>
</g>
{cross(200, 250, 1.2)}
{person(420, 340, 1.0, -1, 'gold', 'blue', 'up', 'short', 'neutral')}
<g transform="translate(456 236) rotate(-20)">
  <path d="M-24-34h48v68h-48z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M140 180h-90"/></g>''', ground=False)

add('distrust', '相手の差し出す手を疑って受け取らない', f'''
{table(380)}
{person(160, 380, 1.05, 1, 'gold', 'blue', 'give', 'short', 'smile')}
{person(450, 380, 1.05, -1, 'teal', 'blue', 'hold', 'bun', 'sad')}
<g transform="translate(300 250)">
  <path d="M-46-26h92v52h-92z" class="greenp o"/>
  <circle r="15" fill="none" stroke="{TONES['green'][2]}" stroke-width="3"/>
</g>
<g transform="translate(450 240)">
  <path d="M-24-8q14-16 28 0M-4-8q14-16 28 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round" transform="translate(-10 0)"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M356 220l40 40M396 220l-40 40"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M420 190q-40-40-90-20"/></g>''', ground=False)

add('diverge', '一本だった道が二手に分かれていく', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v170H0z" fill="#dfe8d8"/>
<path d="M0 230h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M240 400h120L300 250z" fill="#8f9aa6" class="o"/>
<path d="M300 250L120 250l-40-30 220 30z" fill="none"/>
<path d="M300 250L60 244l-6 30 246-6z" fill="#8f9aa6" class="o"/>
<path d="M300 250l246-6-6 30L300 268z" fill="#8f9aa6" class="o"/>
<g fill="none" stroke="#fffefd" stroke-width="4" stroke-dasharray="20 18">
  <path d="M300 380v-120M290 258H70M310 258h220"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M270 220L110 200"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M330 220l160-20"/></g>
{tree(70, 350, 0.9)}
{tree(540, 350, 0.9)}''', ground=False)

add('divulge', '守っていた秘密をこっそり他人に明かす', f'''
{table(380)}
{person(170, 380, 1.05, 1, 'violet', 'blue', 'hold', 'bun', 'neutral')}
{person(430, 380, 1.05, -1, 'coral', 'blue', 'stand', 'short', 'surprised')}
<g transform="translate(300 200)">
  <path d="M-60-40h120v80h-120z" class="paper"/>
  <g fill="{MUTED}"><rect x="-42" y="-20" width="84" height="9" rx="4.5"/><rect x="-42" y="0" width="56" height="9" rx="4.5"/></g>
  <path d="M-70-56h30v20h-30z" fill="{TONES['gold'][0]}" class="o"/>
</g>
<g transform="translate(180 250)">
  <path d="M-40-30h80v60h-80z" fill="#c9a464" class="o"/>
  <circle r="10" fill="{INK}"/>
  <path d="M-16-30v-16q0-18 16-18t16 18v16" fill="none" stroke="#8f9aa6" stroke-width="7"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 160q60-40 120 0"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 6"><path d="M400 250q-20-20 0-40"/></g>''', arrow=True, ground=False)

add('disprove', '示された説が実験で誤りだと示される', f'''
{split()}
{table(380)}
<g transform="translate(150 200)">
  {doc(0, 0, 180, 220, 5)}
  <path d="M-70-70h140" stroke="{INK}" stroke-width="10" fill="none"/>
</g>
<g transform="translate(450 200)">
  {doc(0, 0, 180, 220, 5)}
</g>
{cross(450, 200, 1.6)}
<g transform="translate(450 340)">
  <path d="M-24-50h48l30 50q6 10-6 10h-96q-12 0-6-10z" fill="#e8f0f6" class="o"/>
  <path d="M-34 0h68l6 10q6 10-6 10h-68q-12 0-6-10z" class="corald"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('decode', '意味のわからない記号の列が読める文に変わる', f'''
{split()}
{table(380)}
<g transform="translate(150 200)">
  <path d="M-110-130h220v260h-220z" class="paper"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="{-88+ (i%4)*46}" y="{-104+(i//4)*44}" width="34" height="24" rx="4"/>' for i in range(16)) + f'''
  </g>
</g>
<g transform="translate(450 200)">
  <path d="M-110-130h220v260h-220z" class="paper"/>
  <g fill="{INK}">
''' + ''.join(f'<rect x="-88" y="{-104+i*44}" width="{176-(i%3)*40}" height="14" rx="7"/>' for i in range(6)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>
<g transform="translate(300 320)">
  <circle r="26" class="gold o"/>
  <path d="M20 20l24 24" stroke="{INK}" stroke-width="8" stroke-linecap="round" fill="none"/>
</g>''', arrow=True, ground=False)

add('debug', 'プログラムの中の不具合を見つけて取り除く', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-210-140h420v250h-420z" fill="#3b4450" class="o"/>
  <path d="M-190-120h380v210h-380z" fill="#2c333d"/>
  <g fill="{TONES['green'][0]}">
''' + ''.join(f'<rect x="{-170+ (i%3)*20}" y="{-100+i*24}" width="{200-(i%4)*40}" height="10" rx="5"/>' for i in range(8)) + f'''
  </g>
  <path d="M-40-16h240v34h-240z" fill="{TONES['coral'][0]}" opacity="0.3"/>
  <path d="M-40 90h120v18h-120z" fill="#5a6270"/>
</g>
<g transform="translate(330 200) scale(1.1)">
  <ellipse rx="26" ry="18" fill="{INK}"/>
  <circle cx="26" r="12" fill="{INK}"/>
  <g stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round">
    <path d="M-10-18l-8-16M6-18l6-16M-14 18l-12 16M4 18l8 16M-26 0h-20M22 0h20"/>
  </g>
  <g fill="{TONES['coral'][0]}"><circle cx="-8" cy="-4" r="4"/><circle cx="8" cy="4" r="4"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M420 130l60-50"/>
</g>
{cross(500, 70, 0.7)}''', ground=False)

add('decompose', '落ち葉が土にかえって分解されていく', f'''
{split()}
<path d="M0 0h600v250H0z" fill="#dceaf4"/>
<path d="M0 250h600v150H0z" fill="#8b6437"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g class="greenp o">
''' + ''.join(f'<ellipse cx="{70+ (i%4)*44}" cy="{200+(i//4)*40}" rx="30" ry="20" transform="rotate({-30+i*20} {70+(i%4)*44} {200+(i//4)*40})"/>' for i in range(8)) + f'''
</g>
<g fill="#6b4c28" class="o">
''' + ''.join(f'<ellipse cx="{370+ (i%4)*44}" cy="{240+(i//4)*36}" rx="22" ry="12" transform="rotate({-20+i*24} {370+(i%4)*44} {240+(i//4)*36})" opacity="{0.9-(i%4)*0.18:.2f}"/>' for i in range(8)) + f'''
</g>
<g fill="#4e3a22">
''' + ''.join(f'<circle cx="{350+i*30}" cy="{320+(i%3)*24}" r="7"/>' for i in range(7)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M280 120q20 20 40 0"/></g>''', arrow=True, ground=False)

add('dwindle', 'たっぷりあった水が日ごとに減っていく', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g>
''' + ''.join(f'''<g transform="translate({90+i*105} 280)">
  <path d="M-44-120h88v120q0 16-44 16t-44-16z" fill="#e8f0f6" class="o"/>
  <path d="M-40 {-104+i*28}h80v{104-i*28}q0 12-40 12t-40-12z" fill="{TONES['blue'][1]}"/>
  <path d="M-40 {-104+i*28}h80" stroke="{TONES['blue'][0]}" stroke-width="3" fill="none"/>
</g>''' for i in range(5)) + f'''
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M80 100h440"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M40 360h520"/></g>''', ground=False)

add('die-down', '大きかった炎がだんだん小さくなって消えかける', f'''
<path d="M0 0h600v400H0z" fill="#2b2429"/>
<path d="M0 340h600v60H0z" fill="#1c181c" class="o"/>
<g>
{flame(110, 320, 1.6)}
{flame(250, 330, 1.1)}
{flame(380, 336, 0.7)}
{flame(490, 340, 0.36)}
</g>
<g fill="#5a4a3c" class="o">
''' + ''.join(f'<path d="M{70+i*130} 344h84v14h-84z"/>' for i in range(4)) + f'''
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M100 120h400"/></g>
<g fill="{MUTED}" opacity="0.6"><circle cx="500" cy="290" r="14"/><circle cx="520" cy="264" r="10"/></g>''', ground=False)

add('ease-off', '強かった雨がしだいに弱まる', f'''
<path d="M0 0h600v400H0z" fill="#c8d2da"/>
{table(370)}
{cloud(140, 90, 1.3, 'blue')}
{cloud(430, 100, 1.0, 'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="6" stroke-linecap="round">
''' + ''.join(f'<path d="M{40+i*30} {170+(i%3)*40}l-16 60"/>' for i in range(6)) + f'''
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
''' + ''.join(f'<path d="M{250+i*34} {190+(i%3)*36}l-12 40"/>' for i in range(5)) + f'''
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="2.5" stroke-linecap="round">
''' + ''.join(f'<path d="M{460+i*36} {210+(i%2)*30}l-8 22"/>' for i in range(3)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M60 340h480"/></g>''', ground=False)

add('drum-up', '呼び込みをして客をかき集める', f'''
{table(380)}
<g transform="translate(150 300)">
  <path d="M-80-30h160v50q0 14-80 14t-80-14z" class="coral o"/>
  <path d="M-80-30q0-16 80-16t80 16z" class="coralp o"/>
  <g class="o"><rect x="-50" y="-70" width="34" height="40" class="tealp"/><rect x="-6" y="-76" width="34" height="46" class="goldp"/></g>
</g>
{person(280, 380, 1.05, 1, 'gold', 'blue', 'up', 'cap', 'smile')}
<g transform="translate(330 250) rotate(-30)">
  <path d="M-40-24h34v48h-34z" fill="{INK}"/>
  <path d="M-6-40l60-30v140l-60-30z" fill="#8f9aa6" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M420 170q40 50 0 100M460 140q60 80 0 160"/>
</g>
{head(520, 300, 20, 'teal', 'bob')}
{head(560, 350, 20, 'violet', 'short')}
<g class="a" marker-end="url(#ar)"><path d="M540 240q-60-40-160-20"/></g>''', arrow=True, ground=False)

add('draw-up', '契約書を一から作成して仕上げる', f'''
{table(380)}
<g transform="translate(320 210) rotate(-4)">
  <path d="M-150-140h300v280h-300z" class="paper"/>
  <rect x="-110" y="-112" width="150" height="16" rx="8" fill="{INK}"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-110" y="{-70+i*32}" width="{220-(i%3)*50}" height="10" rx="5"/>' for i in range(5)) + f'''
  </g>
  <path d="M-110 100h130" stroke="{MUTED}" stroke-width="3" fill="none"/>
  <path d="M-104 94q40-24 66 0" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"/>
</g>
{person(120, 380, 1.0, 1, 'teal', 'blue', 'reach', 'bun', 'neutral')}
<g transform="translate(200 280) rotate(30)">
  <path d="M0-80l12 26v70h-24V-54z" class="blue o"/>
  <path d="M-12 16h24v36l-12 22-12-22z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M500 340v-90"/></g>''', arrow=True, ground=False)

add('dreadful', '見るのもいやなほどひどい有り様', f'''
<path d="M0 0h600v400H0z" fill="#5c5560"/>
<path d="M0 340h600v60H0z" fill="#413b45" class="o"/>
<g fill="#7a6f70" class="o">
  <path d="M100 340V180h140v160z"/>
  <path d="M130 200l40 40-40 30zM180 250l40 40-40 20z"/>
</g>
<g fill="none" stroke="#5c5560" stroke-width="6">
  <path d="M110 240h120M110 290h120"/>
</g>
<g fill="#6b5f60" class="o">
''' + ''.join(f'<path d="M{270+i*40} {320+(i%3)*14}l30 12-14 22-30-14z"/>' for i in range(5)) + f'''
</g>
{person(480, 340, 1.05, -1, 'blue', 'blue', 'up', 'bob', 'sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M420 190l-26-24M520 180l26-22"/>
</g>
<g fill="{MUTED}" opacity="0.4"><circle cx="200" cy="120" r="46"/><circle cx="280" cy="90" r="54"/><circle cx="360" cy="120" r="44"/></g>''', ground=False)

add('doubtful', 'そうかなという顔で首をかしげて疑う', f'''
{table(380)}
{person(300, 380, 1.2, 1, 'teal', 'blue', 'think', 'bob', 'neutral')}
<g transform="translate(300 250) rotate(-10)">
  <path d="M-22-8q12-14 24 0M2-8q12-14 24 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round" transform="translate(-14 0)"/>
</g>
<g transform="translate(450 160)">
  <path d="M-40-40h80q12 0 12 12v40q0 12-12 12h-52l-20 16v-16q-20 0-20-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <path d="M-18-24q0-20 18-20t18 20-18 16v10" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle cy="18" r="4.5" fill="{INK}"/>
</g>
<g transform="translate(140 200)">
  {doc(0, 0, 130, 160, 4)}
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M220 220h60"/></g>''', ground=False)

add('eclipse', '月が太陽の前を横切って光をさえぎる', f'''
<path d="M0 0h600v400H0z" fill="#1e2338"/>
<g fill="#fffefd"><circle cx="80" cy="70" r="4"/><circle cx="520" cy="60" r="3"/><circle cx="120" cy="330" r="3"/><circle cx="530" cy="340" r="4"/></g>
<g transform="translate(300 200)">
  <circle r="120" class="gold o"/>
  <g class="golds" stroke-width="6">
''' + ''.join(f'<path d="M{140*math.cos(i*0.524):.0f} {140*math.sin(i*0.524):.0f}L{170*math.cos(i*0.524):.0f} {170*math.sin(i*0.524):.0f}"/>' for i in range(12)) + f'''
  </g>
  <circle cx="-40" r="110" fill="#1e2338" stroke="{INK}" stroke-width="2.5"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="#fffefd"><path d="M120 330h140"/></g>''', ground=False)

add('emit', '煙突から煙とガスが出ていく', f'''
<path d="M0 0h600v300H0z" fill="#c8d2da"/>
<path d="M0 300h600v100H0z" fill="#a8b0a8" class="o"/>
<g transform="translate(300 300)">
  <path d="M-160 0v-120h320V0z" fill="#8f9aa6" class="o"/>
  <path d="M-100-120h50v-180h-50zM40-120h50v-140H40z" fill="#6f7b88" class="o"/>
  <g class="bluep o">
''' + ''.join(f'<rect x="{-140+i*40}" y="-90" width="26" height="34"/>' for i in range(8)) + f'''
  </g>
</g>
<g fill="{MUTED}" opacity="0.8">
  <circle cx="180" cy="-10" r="0"/>
  <circle cx="190" cy="140" r="34"/><circle cx="230" cy="100" r="42"/><circle cx="290" cy="70" r="34"/><circle cx="350" cy="46" r="28"/>
  <circle cx="380" cy="150" r="26"/><circle cx="420" cy="118" r="32"/><circle cx="470" cy="90" r="24"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 190q-40-60 20-120"/></g>''', arrow=True, ground=False)

add('energetic', '疲れた人の横で、元気よく跳びはねている', f'''
{split()}
{table(380)}
{sit(150, 380, 1.05, 1, 'blue', 'blue', 'bob', 'sad', 'down')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M100 230q-16 12-16 30M200 226q16 12 16 30"/>
</g>
<g transform="translate(450 320)">
  <path d="M-12-8l-32 30M12-8l34 26" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-27-78q27-14 54 0l-8 72h-38z" class="coral o"/>
  <path d="M-22-70l-30-34M22-70l30-34" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cy="-108" r="25" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['cap']}" transform="scale(1.04)" fill="{TONES['blue'][0]}"/>
  <circle cx="-8" cy="-104" r="2.2" fill="{INK}"/><circle cx="8" cy="-104" r="2.2" fill="{INK}"/>
  <path d="M-8-92q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{450+110*math.cos(3.4+i*0.42):.0f} {240+110*math.sin(3.4+i*0.42):.0f}l{20*math.cos(3.4+i*0.42):.0f} {20*math.sin(3.4+i*0.42):.0f}"/>' for i in range(8)) + f'''
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3"><ellipse cx="450" cy="384" rx="46" ry="8"/></g>''', ground=False)

add('enlarge', '小さな写真を大きく引き伸ばす', f'''
{split()}
{table(380)}
<g transform="translate(150 240)">
  <path d="M-50-40h100v80h-100z" class="paper"/>
  <path d="M-40 26L-6-16l20 22 20-30 26 50z" class="greenp o"/>
  <circle cx="24" cy="-18" r="9" class="goldp o"/>
</g>
<g transform="translate(450 220)">
  <path d="M-110-90h220v180h-220z" class="paper"/>
  <path d="M-90 60L-14-34l44 48 44-66 58 112z" class="greenp o"/>
  <circle cx="52" cy="-40" r="20" class="goldp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 240h60"/></g>
<g class="a" marker-end="url(#ar)"><path d="M300 100l40-40M300 340l40 40"/></g>''', arrow=True, ground=False)

add('exhale', '大きく息を吐き出して白い息が見える', f'''
<path d="M0 0h600v400H0z" fill="#dfe8ee"/>
{table(380)}
<g transform="translate(220 200)">
  <circle r="106" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-92-32q6-74 92-74t92 74q-44-34-92-34t-92 34z" fill="{HAIR}"/>
  <path d="M-56 0q18-14 34 0M22 0q18-14 34 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <ellipse cy="52" rx="24" ry="18" fill="{INK}"/>
</g>
<g fill="#fffefd" opacity="0.9">
  <ellipse cx="330" cy="256" rx="46" ry="26"/><ellipse cx="400" cy="242" rx="56" ry="32"/><ellipse cx="480" cy="230" rx="50" ry="28"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 300q90 20 190-30"/></g>''', arrow=True, ground=False)

add('exhausted', '走り終えて力尽き、地面にへたり込む', f'''
{table(380)}
<g transform="translate(300 380)">
  <path d="M-70-10h140v10h-140z" fill="none"/>
  <path d="M-20-6l-60 4M20-6l60 4" fill="none" stroke="{TONES['blue'][2]}" stroke-width="14" stroke-linecap="round"/>
  <path d="M-34-70q34-16 68 0l-8 64h-52z" class="coral o"/>
  <path d="M-30-64l-50 40M30-64l50 40" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
  <circle cy="-100" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 8) scale(1.06)" fill="{HAIR}"/>
  <path d="M-16-102q10-8 18 0M-2-102q10-8 18 0" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <ellipse cy="-82" rx="14" ry="9" fill="{INK}"/>
</g>
<g fill="{TONES['blue'][0]}">
  <path d="M240 260q10 12 10 20t-10 8-10-8 10-20z"/><path d="M370 250q9 11 9 18t-9 7-9-7 9-18z"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M170 220q-16 12-16 30M430 216q16 12 16 30"/>
</g>
<g fill="{MUTED}" opacity="0.8">
''' + ''.join(f'<path d="M{460+i*36} {160-i*30}q16 0 16 12t-16 12h18" fill="none" stroke="{MUTED}" stroke-width="{4+i}"/>' for i in range(3)) + f'''
</g>''', ground=False)

add('entrust', '鍵を渡して留守中の家を人に任せる', f'''
{table(380)}
{person(160, 380, 1.05, 1, 'teal', 'blue', 'give', 'bun', 'smile')}
{person(440, 380, 1.05, -1, 'coral', 'blue', 'give', 'short', 'smile')}
<g transform="translate(300 240) rotate(-14)">
  <circle cx="-30" r="20" fill="none" stroke="{TONES['gold'][2]}" stroke-width="8"/>
  <path d="M-12-6h60v12h-60z" fill="{TONES['gold'][0]}" class="o"/>
  <path d="M32 6h10v14H32zM48 6h10v10H48z" fill="{TONES['gold'][0]}" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 180q70-40 140 0"/></g>
{building(300, 140, 0.5, 'coral')}''', arrow=True, ground=False)

add('quirk', 'いつも決まって靴をそろえてから座る、その人だけの癖', f'''
{table(380)}
{sit(370, 380, 1.1, 1, 'violet', 'blue', 'bun', 'smile', 'lap')}
{chair(370, 380, 1.0, 'gold', 1)}
<g transform="translate(180 350)">
  <path d="M-56-16h50v26h-50zM10-16h50v26H10z" fill="#4a5560" class="o"/>
  <path d="M-56 10h50v6h-50zM10 10h50v6H10z" fill="{INK}"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M180 300v-40h90"/></g>
<g transform="translate(180 220)">
  <path d="M-46-34h92q12 0 12 12v36q0 12-12 12h-62l-20 16v-16q-22 0-22-12v-36q0-12 12-12z" fill="#fffefd" class="o"/>
  <g fill="{TONES['violet'][0]}"><circle cx="-16" r="6"/><circle cx="2" r="6"/><circle cx="20" r="6"/></g>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M470 200l24-20M490 260h26"/>
</g>''', ground=False)

add('oversight', '確認表の一行だけ見落としてチェックが抜けている', f'''
{table(380)}
<g transform="translate(300 200) rotate(-3)">
  <path d="M-170-150h340v300h-340z" class="paper"/>
  <g>
''' + ''.join(f'''<g transform="translate(0 {-110+i*50})">
  <rect x="-140" y="-14" width="30" height="28" rx="5" fill="none" stroke="{INK}" stroke-width="3"/>
  <rect x="-92" y="-8" width="{200-(i%3)*40}" height="12" rx="6" fill="{MUTED}"/>
</g>''' for i in range(5)) + f'''
  </g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
''' + ''.join(f'<path d="M-134 {-110+i*50}l8 10 18-22"/>' for i in [0, 1, 3, 4]) + f'''
  </g>
  <circle cx="-125" cy="-10" r="34" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M80 340l90-140"/></g>''', arrow=True, ground=False)

add('litigation', '法廷で両者が弁護士を立てて争う', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
{table(380)}
<g transform="translate(300 160)">
  <path d="M-80-60h160v20h-160z" fill="#c9a464" class="o"/>
  <path d="M-8-40h16v70h-16z" fill="#c9a464" class="o"/>
  <path d="M-70 30h140v14h-140z" fill="#8b6437" class="o"/>
  <path d="M-70-60h-40q0 40 40 40zM70-60h40q0 40-40 40z" fill="#c8d0d8" class="o"/>
  <path d="M-140-20h60v10h-60zM80-20h60v10H80z" fill="#8f9aa6"/>
</g>
{sit(150, 380, 0.9, 1, 'blue', 'blue', 'short', 'neutral', 'lap')}
{sit(450, 380, 0.9, -1, 'coral', 'blue', 'bun', 'neutral', 'lap')}
<g transform="translate(150 300)">{doc(0, 0, 80, 100, 3)}</g>
<g transform="translate(450 300)">{doc(0, 0, 80, 100, 3)}</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M250 300h100"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 250h120"/></g>
<g class="a" marker-end="url(#ar)"><path d="M360 340H240"/></g>''', arrow=True, ground=False)

add('emphasise', '大事な一行だけ色を塗って強調する', f'''
{table(380)}
<g transform="translate(300 200) rotate(-3)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-140" y="{-104+i*44}" width="{280-(i%3)*60}" height="12" rx="6"/>' for i in range(6)) + f'''
  </g>
  <path d="M-146-24h280v34h-280z" fill="{TONES['gold'][1]}"/>
  <rect x="-140" y="-16" width="220" height="12" rx="6" fill="{INK}"/>
</g>
<g transform="translate(470 300) rotate(30)">
  <path d="M-20-80h40v90h-40z" class="gold o"/>
  <path d="M-20 10h40l-8 30h-24z" class="goldd o"/>
  <path d="M-10 40h20l-10 20z" fill="{TONES['gold'][1]}"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['gold'][0]}"><path d="M470 130l-140 40"/></g>''', arrow=True, ground=False)

add('curb', '暴れ出した馬を手綱で引いて抑える', f'''
<path d="M0 0h600v260H0z" fill="#dceaf4"/>
<path d="M0 260h600v140H0z" fill="#dfe8d8"/>
<path d="M0 260h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(330 300)">
  <path d="M-120 0q-10-52 40-62h100q46 6 56 48-40 24-104 24-76 0-92-10z" fill="#a0764a" class="o"/>
  <path d="M92-52q40-38 58-66 22 16 8 58l-24 42z" fill="#a0764a" class="o"/>
  <path d="M146-116q-8-32 6-34 12 8 6 34zM168-122q10-28 20-22 4 10-8 28z" fill="#a0764a" class="o"/>
  <path d="M152-82l28 8-28 10z" fill="#8b6437" class="o"/>
  <circle cx="140" cy="-98" r="4" fill="{INK}"/>
  <path d="M-120 0q-44-16-54-56 44 6 62 42z" fill="#6b4c28" class="o"/>
  <g stroke="#8b6437" stroke-width="13" stroke-linecap="round" fill="none">
    <path d="M-70 14l-40 40M-26 18l-6 52M40 16l40 40M76 12l6 54"/>
  </g>
  <path d="M150-96q-90 30-160-6" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
</g>
{person(120, 400, 1.05, 1, 'teal', 'blue', 'reach', 'cap', 'neutral')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M300 160H180"/></g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
