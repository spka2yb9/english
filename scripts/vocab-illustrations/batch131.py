# -*- coding: utf-8 -*-
"""第131回。over- の動詞と身のまわりの語。over- は「本来の線を越える」で描く。"""
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


# --- over- の動詞 --------------------------------------------------------------
add('overdo', '味つけの塩を入れすぎて料理を台無しにする', f'''
{split()}
{table(340)}
<g transform="translate(150 270)">
  <ellipse rx="80" ry="20" fill="#fffdf6" class="o"/>
  <path d="M-80 0q0 26 80 26t80-26z" fill="#fffdf6" class="o"/>
  <path d="M-40-12q40-24 80-2 4 20-24 24-46 4-56-22z" class="gold o"/>
</g>
<g fill="#fffefd" stroke="{MUTED}" stroke-width="1.5">
''' + ''.join(f'<circle cx="{130+ (i%3)*16}" cy="{180+i*14}" r="3.5"/>' for i in range(4)) + f'''
</g>
{tick(150, 120, 0.7)}
<g transform="translate(450 270)">
  <ellipse rx="80" ry="20" fill="#fffdf6" class="o"/>
  <path d="M-80 0q0 26 80 26t80-26z" fill="#fffdf6" class="o"/>
  <path d="M-40-12q40-24 80-2 4 20-24 24-46 4-56-22z" class="gold o"/>
  <g fill="#fffefd" stroke="{MUTED}" stroke-width="1.5">
''' + ''.join(f'<circle cx="{-60+ (i%8)*18}" cy="{-16+(i//8)*16}" r="4"/>' for i in range(24)) + f'''
  </g>
</g>
<g transform="translate(430 130) rotate(160)">
  <path d="M-22 0h44l-6 56q-2 10-16 10t-16-10z" fill="#fffdf6" class="o"/>
  <path d="M-22 0q0-18 22-18t22 18z" fill="#b8bfc8" class="o"/>
</g>
{cross(450, 120, 0.7)}''', ground=False)

add('overdose', '決められた量より多くの薬を飲んでしまう', f'''
{split()}
{table(340)}
<g transform="translate(150 280)">
  <ellipse rx="60" ry="16" fill="#fffdf6" class="o"/>
  <path d="M-60 0q0 22 60 22t60-22z" fill="#fffdf6" class="o"/>
  <g class="coral o"><ellipse cx="-16" cy="-6" rx="16" ry="11"/><ellipse cx="16" cy="-8" rx="16" ry="11"/></g>
</g>
{tick(150, 130, 0.7)}
<g transform="translate(450 280)">
  <ellipse rx="60" ry="16" fill="#fffdf6" class="o"/>
  <path d="M-60 0q0 22 60 22t60-22z" fill="#fffdf6" class="o"/>
  <g class="coral o">
''' + ''.join(f'<ellipse cx="{-40+ (i%5)*20}" cy="{-8-(i//5)*16}" rx="15" ry="10"/>' for i in range(14)) + f'''
  </g>
</g>
{cross(450, 130, 0.7)}
<g transform="translate(300 130)">
  <path d="M-30-20h60v40h-60z" fill="#fffdf6" class="o"/>
  <path d="M-6-12h12v10h10v12h-10v10h-12v-10h-10v-12h10z" class="coral"/>
</g>''', ground=False)

add('overestimate', '実際よりずっと大きく見積もる', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-90-130h180v260h-180z" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 10"/>
  <g transform="translate(0 60)">
    <path d="M-40-40h80v80h-80z" class="tealp o"/>
  </g>
</g>
<g transform="translate(450 250)">
  <path d="M-40 90h80v40h-80z" fill="none"/>
  <path d="M-44 90h88V10h-88z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M150 100v-60"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M40 300h520"/></g>
{cross(150, 60, 0.6)}
{tick(450, 60, 0.6)}''', arrow=True, ground=False)

add('overhaul', '機械をいったん全部ばらして総点検する', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-80-70h160v140h-160z" fill="#8f9aa6" class="o"/>
  <circle r="42" fill="#c8d0d8" class="o"/>
  <g fill="{INK}">
''' + ''.join(f'<rect x="-6" y="-52" width="12" height="20" rx="6" transform="rotate({i*45})"/>' for i in range(8)) + f'''
  </g>
</g>
<g>
''' + ''.join(f'''<g transform="translate({370+ (i%3)*70} {180+(i//3)*90}) rotate({-20+i*14})">
  <circle r="24" fill="#c8d0d8" class="o"/>
  <g fill="{INK}">''' + ''.join(f'<rect x="-4" y="-30" width="8" height="12" rx="4" transform="rotate({j*60})"/>' for j in range(6)) + '''</g>
</g>''' for i in range(6)) + f'''
</g>
<g transform="translate(540 340) rotate(30)">
  <path d="M-40-8h80v16h-80z" fill="{INK}"/>
  <path d="M40-14h30v28H40z" fill="#8f9aa6" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('overpower', '大きな相手が力でねじ伏せる', f'''
{table(380)}
<g transform="translate(400 380)">
  <path d="M-110 0v-180q0-66 110-66t110 66V0z" class="teald o" transform="scale(0.8 1)"/>
  <circle cy="-272" r="54" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-52-286q6-52 52-52 46 0 52 52-26-22-52-12-24-18-52 12z" fill="{HAIR}"/>
  <circle cx="-20" cy="-278" r="5" fill="{INK}"/><circle cx="20" cy="-278" r="5" fill="{INK}"/>
  <path d="M-18-250h36" stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none"/>
  <path d="M-90-180l-90 30" stroke="{SKIN}" stroke-width="28" stroke-linecap="round" fill="none"/>
</g>
{person(150, 380, 0.85, 1, 'coral', 'blue', 'up', 'bob', 'sad')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M280 200H160"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M96 220l-26-18M204 210l24-18"/>
</g>''', ground=False)

add('overreact', '小さな失敗に大げさに騒ぎ立てる', f'''
{split()}
{table(380)}
<g transform="translate(150 300)">
  <path d="M-40-20h80v40h-80z" fill="#fffdf6" class="o"/>
  <circle cx="14" cy="4" r="5" class="coral"/>
</g>
{person(150, 380, 0.9, 1, 'teal', 'blue', 'stand', 'short', 'neutral')}
{person(450, 380, 1.15, 1, 'coral', 'blue', 'up', 'bun', 'sad')}
<g transform="translate(450 300)">
  <path d="M-40-20h80v40h-80z" fill="#fffdf6" class="o"/>
  <circle cx="14" cy="4" r="5" class="coral"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M340 190l-30-26M560 180l30-24M360 260l-40-6M540 250l40-6"/>
</g>
<g transform="translate(450 130)">
  <path d="M-30-28h60q10 0 10 10v28q0 10-10 10h-40l-16 14v-14q-14 0-14-10v-28q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M-4-16h8v22h-8z" fill="{TONES['coral'][0]}"/>
  <circle cy="14" r="4.5" fill="{TONES['coral'][0]}"/>
</g>''', ground=False)

add('overrule', '上位の判断が下の決定を覆す', f'''
{table(380)}
<g transform="translate(300 300)">
  {doc(0, 0, 170, 200, 4)}
  {tick(0, 60, 0.55)}
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round">
  <path d="M230 240l140 130M370 240L230 370"/>
</g>
<g transform="translate(300 120)">
  <path d="M-90-40h180v20h-180z" fill="#c9a464" class="o"/>
  <path d="M-8-20h16v40h-16z" fill="#c9a464" class="o"/>
  <path d="M-70 20h140v14h-140z" fill="#8b6437" class="o"/>
  <path d="M-70-40h-40q0 30 40 30zM70-40h40q0 30-40 30z" fill="#c8d0d8" class="o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M300 170v50"/></g>''', ground=False)

add('overrun', '決めた時間を大きく超えて会議が続く', f'''
{table(380)}
<g transform="translate(300 210)">
  <circle r="130" fill="#fffdf6" class="o"/>
  <g fill="{INK}">
''' + ''.join(f'<rect x="-5" y="-108" width="10" height="22" rx="5" transform="rotate({i*30})"/>' for i in range(12)) + f'''
  </g>
  <path d="M0-112A112 112 0 0 1 79 79L0 0z" fill="{TONES['green'][1]}" opacity="0.5"/>
  <path d="M79 79A112 112 0 0 1-79 79L0 0z" fill="{TONES['coral'][1]}" opacity="0.7"/>
  <path d="M0 0v-90" stroke="{INK}" stroke-width="8" stroke-linecap="round" fill="none"/>
  <path d="M0 0l-64 64" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round" fill="none"/>
  <circle r="10" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M420 330q-60 40-160 20"/></g>
{head(120, 350, 20, 'teal', 'short')}
{head(500, 350, 20, 'coral', 'bun')}''', ground=False)

add('overshadow', '大きな建物の影が小さな家を覆ってしまう', f'''
<path d="M0 0h600v300H0z" fill="#dceaf4"/>
<path d="M0 300h600v100H0z" fill="#dfe8d8"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
{sun(70, 70, 34)}
<g transform="translate(430 300)">
  <path d="M-110 0v-270h220V0z" fill="#8f9aa6" class="o"/>
  <g class="bluep o">
''' + ''.join(f'<rect x="{-88+ (i%3)*66}" y="{-246+(i//3)*54}" width="44" height="36"/>' for i in range(12)) + f'''
  </g>
</g>
<g fill="{INK}" opacity="0.28"><path d="M320 300L80 380V240z"/></g>
<g transform="translate(190 300)">
  <path d="M-60 0v-70h120V0z" fill="#fffdf6" class="o"/>
  <path d="M-72-70L0-120l72 50z" class="coral o"/>
  <path d="M-16-40h32V0h-32z" class="corald o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M330 160l-90 90"/></g>''', ground=False)

add('overstate', '小さな成果を実物よりずっと大きく語る', f'''
{table(380)}
{person(140, 380, 1.05, 1, 'coral', 'blue', 'up', 'bun', 'smile')}
<g transform="translate(140 300)">
  <path d="M-20-16h40v32h-40z" class="tealp o"/>
</g>
<g transform="translate(400 200)">
  <path d="M-130-90h260q16 0 16 16v100q0 16-16 16h-180l-30 24v-24q-16 0-16-16v-100q0-16 16-16z" fill="#fffefd" class="o"/>
  <path d="M-70-40h140v100h-140z" class="tealp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M180 290q40-60 90-70"/></g>
<g class="a" marker-end="url(#ar)"><path d="M320 350l-140-40"/></g>''', arrow=True, ground=False)

add('overtake', '後ろの車が前の車を追い越す', f'''
<path d="M0 250h600v150H0z" fill="#6f7b88"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="#fffefd" stroke-width="5" stroke-dasharray="30 26"><path d="M0 320h600"/></g>
<g transform="translate(200 360) scale(0.6)">
  <path d="M-130 30h260v-46q0-16-16-16h-70l-40-38H-90l-24 38h-16q-16 0-16 16z" class="teal o"/>
  <circle cx="-70" cy="30" r="24" fill="{INK}"/><circle cx="70" cy="30" r="24" fill="{INK}"/>
</g>
<g transform="translate(400 280) scale(0.6)">
  <path d="M-130 30h260v-46q0-16-16-16h-70l-40-38H-90l-24 38h-16q-16 0-16 16z" class="coral o"/>
  <circle cx="-70" cy="30" r="24" fill="{INK}"/><circle cx="70" cy="30" r="24" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M180 200q120-80 300 40"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M280 270h50M260 300h40"/>
</g>''', ground=False)

add('overweight', '体重計の針が標準より上を指している', f'''
{table(380)}
{person(240, 340, 1.05, 1, 'coral', 'blue', 'stand', 'short', 'sad')}
<g transform="translate(240 240)">
  <ellipse rx="66" ry="52" class="coral o"/>
</g>
<g transform="translate(240 358)">
  <path d="M-90-24h180v24q0 12-16 12h-148q-16 0-16-12z" fill="#c8d0d8" class="o"/>
  <path d="M-90-24q0-16 90-16t90 16z" fill="#e0e6ea" class="o"/>
</g>
<g transform="translate(450 210)">
  <circle r="88" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
''' + ''.join(f'<path d="M{70*math.cos(math.pi*(0.75+i*0.083)):.0f} {70*math.sin(math.pi*(0.75+i*0.083)):.0f}L{84*math.cos(math.pi*(0.75+i*0.083)):.0f} {84*math.sin(math.pi*(0.75+i*0.083)):.0f}"/>' for i in range(19)) + f'''
  </g>
  <path d="M-62-62A88 88 0 0 1 62-62" fill="none" stroke="{TONES['green'][0]}" stroke-width="8"/>
  <path d="M0 0l58-40" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round" fill="none"/>
  <circle r="9" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M450 320v-40"/></g>''', ground=False)

# --- 身のまわりの語 -----------------------------------------------------------
add('paragraph', '一字下げで始まるひとまとまりの文の固まり', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-190-150h380v300h-380z" class="paper"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="{-150+ (24 if i==0 else 0)}" y="{-110+i*24}" width="{300-(24 if i==0 else 0)-(0 if i<3 else 120)}" height="11" rx="5.5"/>' for i in range(4)) + f'''
  </g>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="{-150+ (24 if i==0 else 0)}" y="{10+i*24}" width="{300-(24 if i==0 else 0)-(0 if i<2 else 170)}" height="11" rx="5.5"/>' for i in range(3)) + f'''
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="8 6">
    <path d="M-160-120h320v104h-320z"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M520 330l-90-190"/></g>''', arrow=True, ground=False)

add('passport', '顔写真とスタンプの並んだ旅券', f'''
{table(360)}
<g transform="translate(280 230) rotate(-6)">
  <path d="M-110-140h220v280h-220z" class="blued o"/>
  <path d="M-90-120h180v240h-180z" fill="#fffdf6" class="o"/>
  <g transform="translate(-40 -50)">
    <path d="M-40-50h80v100h-80z" class="bluep o"/>
    <circle cy="-14" r="20" fill="{SKIN}" stroke="{SKINL}" stroke-width="2"/>
    <path d="M-26 40q26-32 52 0z" fill="{TONES['teal'][0]}"/>
  </g>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="10" y="{-84+i*26}" width="{68-(i%3)*18}" height="9" rx="4.5"/>' for i in range(4)) + f'''
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" opacity="0.8">
    <circle cx="-40" cy="60" r="30"/><circle cx="40" cy="86" r="26"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M480 130l-110 60"/></g>''', arrow=True, ground=False)

add('peel', 'りんごの皮をナイフでらせん状にむく', f'''
{table(340)}
<g transform="translate(280 240)">
  <circle r="90" class="coral o"/>
  <path d="M0-90q-16-30 8-38 20 8 8 38z" class="greend o"/>
  <path d="M-90 0a90 90 0 0 1 60-84" fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"/>
  <path d="M40-70q40 40 30 90" fill="none" stroke="#f6e0c8" stroke-width="26"/>
</g>
<path d="M370 200q50 40 30 90t-70 60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="16" stroke-linecap="round"/>
<path d="M370 200q50 40 30 90t-70 60" fill="none" stroke="{TONES['coral'][2]}" stroke-width="2.5"/>
<g transform="translate(400 150) rotate(120)">
  <path d="M-70-14h100l30 14-30 14h-100z" fill="#dde3e8" class="o"/>
  <path d="M-110-10h44v20h-44q-8 0-8-10t8-10z" fill="{INK}"/>
</g>''', ground=False)

add('podcast', 'マイクの前で話した音声が耳に届く', f'''
{table(380)}
<g transform="translate(180 250)">
  <path d="M-24-70h48v90q0 14-24 14t-24-14z" fill="#5a6270" class="o"/>
  <g fill="#8f9aa6">
''' + ''.join(f'<rect x="-18" y="{-60+i*16}" width="36" height="8" rx="4"/>' for i in range(5)) + f'''
  </g>
  <path d="M-40 20q0 40 40 40t40-40" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M0 60v30M-30 90h60" stroke="{INK}" stroke-width="6" stroke-linecap="round" fill="none"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M260 200q30 40 0 80M300 176q46 64 0 128M340 152q62 88 0 176"/>
</g>
<g transform="translate(470 220)">
  <path d="M-40-50q0-40 40-40t40 40v40q0 14-14 14h-14v-40h14v-14q0-26-26-26t-26 26v14h14v40h-14q-14 0-14-14z" fill="#3b4450" class="o"/>
</g>
{head(470, 320, 24, 'teal', 'bob')}''', ground=False)

add('portable', '折りたためて持ち運べる小さな机', f'''
{split()}
{table(380)}
<g transform="translate(150 300)">
  <path d="M-110-20h220v20h-220z" fill="#c9a464" class="o"/>
  <path d="M-90 0v80M90 0v80" stroke="#a0764a" stroke-width="14" stroke-linecap="round" fill="none"/>
</g>
<g transform="translate(450 300)">
  <path d="M-30-100h60v170q0 14-30 14t-30-14z" fill="#c9a464" class="o"/>
  <path d="M-30-100h60v-14h-60z" fill="#a0764a"/>
  <path d="M-30-40h60" fill="none" stroke="#a0764a" stroke-width="3"/>
</g>
{person(520, 380, 0.8, -1, 'teal', 'blue', 'carry', 'bun', 'smile')}
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('optional', '必ず選ぶ品と、選んでも選ばなくてもよい品', f'''
{split()}
{table(380)}
<g transform="translate(150 240)">
  <path d="M-90-100h180v200h-180z" class="paper"/>
  <g>
''' + ''.join(f'''<g transform="translate(0 {-64+i*44})">
  <rect x="-64" y="-14" width="28" height="28" rx="5" fill="none" stroke="{INK}" stroke-width="3"/>
  <rect x="-24" y="-7" width="{86-(i%2)*24}" height="14" rx="7" fill="{MUTED}"/>
</g>''' for i in range(4)) + f'''
  </g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
''' + ''.join(f'<path d="M-58 {-64+i*44}l8 10 18-22"/>' for i in range(4)) + f'''
  </g>
</g>
<g transform="translate(450 240)">
  <path d="M-90-100h180v200h-180z" class="paper"/>
  <g>
''' + ''.join(f'''<g transform="translate(0 {-64+i*44})">
  <rect x="-64" y="-14" width="28" height="28" rx="5" fill="none" stroke="{TONES['coral'][0]}" stroke-width="3" stroke-dasharray="6 4"/>
  <rect x="-24" y="-7" width="{86-(i%2)*24}" height="14" rx="7" fill="{MUTED}"/>
</g>''' for i in range(4)) + f'''
  </g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M-58-64l8 10 18-22"/><path d="M-58 24l8 10 18-22"/>
  </g>
</g>''', ground=False)

add('messy', '机の上に物が散らかって足の踏み場もない', f'''
{split()}
{table(380)}
<g transform="translate(150 300)">
  <path d="M-110-20h220v20h-220z" fill="#c9a464" class="o"/>
  {doc(-50, -70, 70, 90, 3)}
  <g class="o"><rect x="10" y="-60" width="50" height="40" class="tealp"/></g>
  <path d="M70-24h20v4H70z" fill="{INK}"/>
</g>
<g transform="translate(450 300)">
  <path d="M-110-20h220v20h-220z" fill="#c9a464" class="o"/>
''' + ''.join(f'<g transform="translate({-70+ (i%4)*44} {-56-(i//4)*36}) rotate({-30+i*17})">{doc(0, 0, 56, 70, 2)}</g>' for i in range(8)) + f'''
  <g class="o"><rect x="-20" y="-30" width="46" height="30" class="tealp" transform="rotate(24 0 -14)"/></g>
  <path d="M60-30l30 10-10 14z" fill="{INK}"/>
</g>
{tick(150, 130, 0.7)}
{cross(450, 130, 0.7)}''', ground=False)

add('gradual', '一段ずつ少しずつ上がっていく坂', f'''
{split()}
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
<path d="M0 380h600v20H0z" fill="#dfe8d8"/>
<path d="M120 380L120 120h60v260z" fill="#8f9aa6" class="o"/>
<path d="M330 380l180-200h30v200z" fill="#8f9aa6" class="o"/>
{person(90, 380, 0.7, 1, 'coral', 'blue', 'up', 'cap', 'sad')}
{person(400, 300, 0.7, 1, 'teal', 'blue', 'walk', 'cap', 'smile', 'walk')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M100 300v-140"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}"><path d="M340 350l160-160"/></g>''', ground=False)

# --- 動作と抽象 --------------------------------------------------------------
add('narrate', '絵に合わせて声で物語を進める', f'''
{table(380)}
<g transform="translate(400 210)">
  <path d="M-150-120h300v240h-300z" fill="#dceaf4" class="o"/>
  {tree(-90, 90, 0.8)}
  <path d="M40 90V20h80v70z" fill="#fffdf6" class="o"/>
  <path d="M28 20L80-22l52 42z" class="coral o"/>
  {sun(100, -70, 24)}
</g>
{person(120, 380, 1.05, 1, 'violet', 'blue', 'hold', 'bun', 'smile')}
<g transform="translate(160 250) rotate(20)">
  <path d="M-8-40h16v70h-16z" fill="#5a6270" class="o"/>
  <ellipse cy="-48" rx="16" ry="22" fill="#8f9aa6" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M220 190q30 34 0 68M256 166q46 60 0 120"/>
</g>''', ground=False)

add('negate', '積み上げた成果を一撃で無効にする', f'''
{table(380)}
<g transform="translate(300 300)">
  <g class="teal o">
''' + ''.join(f'<rect x="{-90+ (i%3)*62}" y="{-40-(i//3)*46}" width="52" height="40"/>' for i in range(9)) + f'''
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="14" stroke-linecap="round">
  <path d="M160 120l280 220M440 120L160 340"/>
</g>
<g transform="translate(500 120)">
  <circle r="34" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
  <path d="M-22 22L22-22" stroke="{TONES['coral'][0]}" stroke-width="8" fill="none"/>
</g>''', ground=False)

add('orchestrate', '多くの人の動きをひとりが周到にまとめ上げる', f'''
{table(380)}
{person(300, 300, 1.0, 1, 'violet', 'blue', 'up', 'bun', 'neutral')}
<g transform="translate(300 340)">
  <path d="M-70-30h140v40h-140z" fill="#8b6437" class="o"/>
</g>
<g>
''' + ''.join(head(70+i*100, 370, 20, ['teal','coral','gold','green','blue','violet'][i%6], ['short','bob','bun','cap'][i%4]) for i in [0,1,3,4]) + f'''
</g>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="3" stroke-dasharray="8 7">
  <path d="M280 210q-90 40-200 130M320 210q90 40 200 130M290 210q-60 60-120 140M310 210q60 60 120 140"/>
</g>
<g fill="{INK}">
  <g transform="translate(120 140)"><ellipse rx="12" ry="9" transform="rotate(-20)"/><path d="M10-4v-40h4v40z"/></g>
  <g transform="translate(470 150)"><ellipse rx="12" ry="9" transform="rotate(-20)"/><path d="M10-4v-40h4v40z"/></g>
</g>''', ground=False)

add('pacify', '泣いている子をなだめて落ち着かせる', f'''
{split()}
{table(380)}
<g transform="translate(150 380)">
  <path d="M-12-8l-24 8M12-8l24 8" fill="none" stroke="{TONES['blue'][2]}" stroke-width="11" stroke-linecap="round"/>
  <path d="M-25-70q25-14 50 0l-8 64h-34z" class="coral o"/>
  <path d="M-22-64l-30-24M22-64l30-24" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
  <circle cy="-100" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 8)" fill="{HAIR}"/>
  <path d="M-14-102q8-8 16 0M-2-102q8-8 16 0" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <path d="M-10-84q10 12 20 0z" fill="{INK}" class="o"/>
</g>
<g fill="{TONES['blue'][0]}"><path d="M120 296q9 10 9 17t-9 8-9-8 9-17z"/><path d="M180 296q9 10 9 17t-9 8-9-8 9-17z"/></g>
<g transform="translate(450 380)">
  <path d="M-12-8l-8 8M12-8l8 8" fill="none" stroke="{TONES['blue'][2]}" stroke-width="11" stroke-linecap="round"/>
  <path d="M-25-70q25-14 50 0l-8 64h-34z" class="coral o"/>
  <circle cy="-100" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 8)" fill="{HAIR}"/>
  <circle cx="-8" cy="-96" r="2.2" fill="{INK}"/><circle cx="8" cy="-96" r="2.2" fill="{INK}"/>
  <path d="M-8-84q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
{hand(390, 300, 1)}
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('penetrate', '矢が板を貫いて反対側に出る', f'''
{table(380)}
<g transform="translate(340 220)">
  <path d="M-30-140h60v280h-60z" fill="#c9a464" class="o"/>
  <g fill="none" stroke="#a0764a" stroke-width="3"><path d="M0-140v280"/></g>
  <circle r="16" fill="#8b6437"/>
</g>
<g transform="translate(300 220)">
  <path d="M-240-6h180v12h-240z" fill="none"/>
  <path d="M-240-5h190v10h-190z" fill="#c9a464" class="o"/>
  <path d="M-240-5l-30-8 6 13-6 13z" fill="#8f9aa6" class="o"/>
  <path d="M110-5h70v10h-70z" fill="#c9a464" class="o"/>
  <path d="M180 0l30-14v28z" fill="#8f9aa6" class="o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M120 140h320"/></g>''', ground=False)

add('permeate', '水がしみ渡って布全体を濡らす', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" fill="#e8f0f6" class="o"/>
  <g fill="{TONES['blue'][1]}">
    <circle cx="-160" cy="-100" r="70"/><circle cx="-60" cy="-60" r="90"/><circle cx="60" cy="-20" r="100"/>
    <circle cx="150" cy="40" r="90"/><circle cx="-120" cy="60" r="80"/><circle cx="20" cy="100" r="86"/>
  </g>
  <path d="M-200-140h400v280h-400z" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <g fill="{TONES['blue'][0]}" opacity="0.5">
''' + ''.join(f'<circle cx="{-170+ (i%7)*58}" cy="{-100+(i//7)*70}" r="14"/>' for i in range(21)) + f'''
  </g>
</g>
<g fill="{TONES['blue'][0]}">
  <path d="M120 70q10 12 10 20t-10 8-10-8 10-20z"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 100q40 40 40 90"/></g>''', arrow=True, ground=False)

add('personify', '正義という考えを人の姿で表す', f'''
{split()}
{table(380)}
<g transform="translate(150 220)">
  <path d="M-10 0h20v130h-20z" fill="#8f9aa6" class="o"/>
  <path d="M-70 130h140v20h-140z" fill="#8f9aa6" class="o"/>
  <path d="M-120-8h240v16h-240z" fill="#b8bfc8" class="o"/>
  <circle r="16" fill="#8f9aa6" class="o"/>
  <path d="M-110 8v30M110 8v30" stroke="{INK}" stroke-width="3" fill="none"/>
  <path d="M-160 38h100q0 26-50 26t-50-26z" class="goldp o"/>
  <path d="M60 38h100q0 26-50 26t-50-26z" class="goldp o"/>
</g>
<g transform="translate(450 380)">
  <path d="M-40-180q40-20 80 0l50 180h-180z" class="violetd o"/>
  <circle cy="-212" r="28" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-28-224q6-30 28-30 20 0 26 30z" fill="{HAIR}"/>
  <path d="M-34-216h68v10h-68z" fill="#fffdf6" class="o"/>
  <path d="M-40-180l-56 30" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-120-160h60v12h-60z" fill="#b8bfc8" class="o"/>
  <circle cx="-90" cy="-154" r="10" fill="#8f9aa6"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('pick-on', 'ひとりだけを選んで繰り返しからかう', f'''
{table(380)}
''' + ''.join(person(90+i*90, 380, 0.85, 1, 'blue', 'blue', 'stand', 'short', 'neutral') for i in [0, 1, 4, 5]) + f'''
{person(320, 380, 0.85, 1, 'coral', 'blue', 'stand', 'bob', 'sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="10 8">
  <path d="M130 250q80-40 170-20M220 240q40-20 90-10M410 240q-40-20-90-10M500 250q-80-40-170-20"/>
</g>
<circle cx="320" cy="280" r="80" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10"/>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M470 100l-120 90"/></g>''', ground=False)

add('pin-down', '地図の一点にピンを刺して場所を特定する', f'''
{table(380)}
<g transform="translate(300 210) rotate(-3)">
  <path d="M-200-150h400v300h-400z" fill="#f0e6d0" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    <path d="M-200-60h400M-200 40h400M-70-150v300M70-150v300"/>
  </g>
  <g class="greenp o"><circle cx="-120" cy="-90" r="30"/><circle cx="120" cy="70" r="26"/></g>
  <path d="M-160 100q80-90 180-30t150-100" fill="none" stroke="{TONES['blue'][0]}" stroke-width="6"/>
</g>
<g transform="translate(340 200)">
  <path d="M0 40q-30-40-30-64 0-30 30-30t30 30q0 24-30 64z" class="coral o"/>
  <circle cy="-26" r="12" fill="#fffdf6"/>
</g>
<circle cx="340" cy="240" r="46" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"/>''', ground=False)

add('pinpoint', 'ぼんやりした範囲から一点を正確に突き止める', f'''
{split()}
{table(380)}
<g transform="translate(150 230)">
  <circle r="110" fill="{TONES['coral'][1]}" opacity="0.7"/>
  <circle r="110" fill="none" stroke="{TONES['coral'][0]}" stroke-width="3" stroke-dasharray="10 8"/>
</g>
<g transform="translate(450 230)">
  <circle r="110" fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="8 8"/>
  <circle r="70" fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="8 8"/>
  <circle r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
  <circle r="10" class="coral"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
    <path d="M0-124v24M0 124v-24M-124 0h24M124 0h-24"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 230h60"/></g>''', arrow=True, ground=False)

add('populate', 'からっぽの町に人が入って住み始める', f'''
{split()}
{table(380)}
<g transform="translate(150 300)">
  <path d="M-50 0v-70h100V0z" fill="#c8d0d8" class="o"/>
  <path d="M-58-70L0-110l58 40z" fill="#8f9aa6" class="o"/>
  <path d="M-110 0v-50h80V0z" fill="#c8d0d8" class="o"/>
</g>
<g transform="translate(450 300)">
  <path d="M-50 0v-70h100V0z" fill="#fffdf6" class="o"/>
  <path d="M-58-70L0-110l58 40z" class="coral o"/>
  <path d="M-110 0v-50h80V0z" fill="#fffdf6" class="o"/>
  <path d="M-30-56h30v24h-30z" class="bluep o"/>
  <path d="M-96-38h30v24h-30z" class="bluep o"/>
</g>
{head(400, 350, 18, 'teal', 'short')}
{head(460, 356, 18, 'coral', 'bob')}
{head(520, 350, 18, 'gold', 'bun')}
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('prioritise', '仕事に番号をつけて大事な順に並べ替える', f'''
{split()}
{table(380)}
<g>
''' + ''.join(f'<g transform="translate({150} {180+i*54})"><path d="M-90-22h180v44h-180z" fill="{TONES[["tealp","coralp","goldp","violetp"][i]][0] if False else "#fff"}" class="paper"/><rect x="-70" y="-7" width="{120-(i%3)*30}" height="14" rx="7" fill="{MUTED}"/></g>' for i in range(4)) + f'''
</g>
<g>
''' + ''.join(f'''<g transform="translate(450 {180+i*54})">
  <path d="M-90-22h180v44h-180z" class="paper"/>
  <circle cx="-70" r="14" fill="{TONES[["coral","gold","teal","violet"][i]][0]}"/>
  <rect x="-48" y="-7" width="{120-(i%3)*30}" height="14" rx="7" fill="{MUTED}"/>
</g>''' for i in range(4)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 280h60"/></g>''', arrow=True, ground=False)

add('proliferate', '一つだった点が短い間に急に増える', f'''
{split()}
{table(380)}
<g class="coral o"><circle cx="150" cy="240" r="20"/></g>
<g class="coral o">
''' + ''.join(f'<circle cx="{350+ (i%7)*36}" cy="{140+(i//7)*46}" r="17"/>' for i in range(28)) + f'''
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M240 240h60"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M270 100v220"/></g>''', ground=False)

add('prolong', '短い予定を引き延ばして長くする', f'''
{split()}
{table(380)}
<g transform="translate(150 230)">
  <path d="M-90-20h180v40h-180z" class="tealp o"/>
  <path d="M-90-40v80M90-40v80" stroke="{INK}" stroke-width="4" fill="none"/>
</g>
<g transform="translate(430 230)">
  <path d="M-130-20h260v40h-260z" class="tealp o"/>
  <path d="M-130-40v80M130-40v80" stroke="{INK}" stroke-width="4" fill="none"/>
  <path d="M40-20h90v40H40z" fill="{TONES['coral'][1]}"/>
  <path d="M40-40v80" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="8 6" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M470 320h90"/></g>
<g class="a" marker-end="url(#ar)"><path d="M270 230h60"/></g>''', arrow=True, ground=False)

add('proofread', '刷る前の原稿の誤りを赤で直す', f'''
{table(380)}
<g transform="translate(290 200) rotate(-3)">
  <path d="M-170-150h340v300h-340z" class="paper"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-130" y="{-110+i*40}" width="{260-(i%3)*60}" height="11" rx="5.5"/>' for i in range(6)) + f'''
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4">
    <path d="M-100-104h60M-40-70l16-16M60-30h50"/>
    <path d="M-90 6q10-8 20 0t20 0"/>
    <circle cx="90" cy="-70" r="16"/>
  </g>
</g>
<g transform="translate(450 300) rotate(30)">
  <path d="M0-80l12 26v70h-24V-54z" class="coral o"/>
  <path d="M-12 16h24v36l-12 22-12-22z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>''', ground=False)

add('propel', 'プロペラが水を押して船を前へ進ませる', f'''
<path d="M0 0h600v170H0z" fill="#dceaf4"/>
<path d="M0 170h600v230H0z" fill="#5b8caa"/>
<path d="M0 170h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(340 200)">
  <path d="M-160 0h320l-40 60q-6 12-120 12T-120 60z" class="coral o"/>
  <path d="M-120-60h240v60h-240z" fill="#fffdf6" class="o"/>
  <g class="coralp o">
''' + ''.join(f'<rect x="{-100+i*54}" y="-44" width="38" height="30"/>' for i in range(4)) + f'''
  </g>
</g>
<g transform="translate(170 260)">
  <path d="M-8-40h16v80h-16z" fill="#8f9aa6" class="o"/>
  <g fill="#b8bfc8" class="o">
''' + ''.join(f'<ellipse cx="0" cy="{-30+i*30}" rx="30" ry="10" transform="rotate({-24+i*24} 0 {-30+i*30})"/>' for i in range(3)) + f'''
  </g>
</g>
<g fill="none" stroke="#a8c8dd" stroke-width="5" stroke-linecap="round">
  <path d="M120 220q-40 20-70 0M110 270q-40 20-70 0M130 320q-40 20-70 0"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M420 120h130"/></g>''', ground=False)

add('puncture', '釘を踏んでタイヤに穴があき空気が抜ける', f'''
{table(380)}
<g transform="translate(280 240)">
  <circle r="130" fill="{INK}"/>
  <circle r="98" fill="#4a5560"/>
  <circle r="56" fill="#c8d0d8" class="o"/>
  <circle r="18" fill="#8f9aa6" class="o"/>
  <g fill="#2c333d">
''' + ''.join(f'<rect x="-9" y="-128" width="18" height="26" rx="4" transform="rotate({i*30})"/>' for i in range(12)) + f'''
  </g>
</g>
<g transform="translate(280 240) rotate(140)">
  <path d="M-5-140h10v40h-10z" fill="#b8bfc8" class="o"/>
  <path d="M-14-150h28v12h-28z" fill="#8f9aa6" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M400 130q30-20 50 0M430 90q30-20 50 0"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M180 110l-26-24M110 180l-30-6"/>
</g>''', ground=False)

add('marginalise', '意見のある人を輪の外へ押しやる', f'''
{split()}
{table(380)}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="12 10"><circle cx="150" cy="270" r="110"/></g>
{head(100, 230, 22, 'teal', 'short')}
{head(200, 230, 22, 'coral', 'bun')}
{head(150, 320, 22, 'gold', 'cap')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="12 10"><circle cx="430" cy="270" r="110"/></g>
{head(390, 230, 22, 'teal', 'short')}
{head(480, 240, 22, 'gold', 'cap')}
{head(420, 320, 22, 'green', 'short')}
<g opacity="0.55">{head(570, 150, 20, 'coral', 'bun')}</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M480 200l70-30"/></g>''', ground=False)

add('measure-up', '決められた高さの線に届くかどうかを確かめる', f'''
{split()}
{table(380)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="14 10"><path d="M40 200h520"/></g>
{person(150, 380, 0.85, 1, 'blue', 'blue', 'stand', 'short', 'sad')}
{person(450, 380, 1.1, 1, 'coral', 'blue', 'up', 'cap', 'smile')}
<g transform="translate(60 290)">
  <path d="M-14-140h28v280h-28z" class="goldp o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">
''' + ''.join(f'<path d="M-14 {-124+i*30}h{20 if i%2 else 28}"/>' for i in range(10)) + f'''
  </g>
</g>
{cross(150, 130, 0.6)}
{tick(450, 130, 0.6)}''', ground=False)

add('incite', '群衆をあおって行動に走らせる', f'''
{table(380)}
{person(140, 380, 1.1, 1, 'violet', 'gold', 'up', 'cap', 'neutral')}
<g transform="translate(200 250) rotate(-30)">
  <path d="M-40-24h34v48h-34z" fill="{INK}"/>
  <path d="M-6-40l60-30v140l-60-30z" fill="#8f9aa6" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M290 170q40 50 0 100M330 140q60 80 0 160"/>
</g>
<g>
''' + ''.join(person(390+ (i%3)*80, 380- (i//3)*0, 0.8, 1, ['coral','gold','teal'][i%3], 'blue', 'up', ['short','bob','cap'][i%3], 'sad') for i in range(3)) + f'''
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M400 200l-20-24M550 200l20-24"/>
</g>''', ground=False)

add('horrify', '目にした光景にぞっとして立ちすくむ', f'''
{table(380)}
<g transform="translate(220 210)">
  <circle r="110" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-96-34q6-76 96-76t96 76q-44-36-96-36t-96 36z" fill="{HAIR}"/>
  <circle cx="-40" cy="-6" r="20" fill="#fffefd" class="o"/><circle cx="-40" cy="-6" r="9" fill="{INK}"/>
  <circle cx="40" cy="-6" r="20" fill="#fffefd" class="o"/><circle cx="40" cy="-6" r="9" fill="{INK}"/>
  <ellipse cy="56" rx="26" ry="30" fill="{INK}"/>
  <path d="M-70-44q22-20 44-8M26-52q22-12 44 8" fill="none" stroke="{HAIR}" stroke-width="6" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M370 100l30-26M400 200h34M370 300l30 26"/>
</g>
<g transform="translate(500 210)">
  <path d="M-50-90l100 180h-100z" fill="#4a5560" class="o"/>
  <path d="M-4-40h8v50h-8z" fill="#fffefd"/>
</g>''', ground=False)

add('galvanise', '一声で止まっていた人たちが一斉に動き出す', f'''
{split()}
{table(380)}
{sit(150, 380, 0.9, 1, 'blue', 'blue', 'short', 'sad', 'down')}
{chair(150, 380, 0.85, 'gold', 1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M110 240q-14 10-14 26M190 236q14 10 14 26"/>
</g>
<g>
''' + ''.join(person(360+i*80, 380, 0.85, 1, ['coral','gold','teal'][i%3], 'blue', 'up', ['cap','bob','short'][i%3], 'smile') for i in range(3)) + f'''
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{440+140*math.cos(3.5+i*0.44):.0f} {230+140*math.sin(3.5+i*0.44):.0f}l{20*math.cos(3.5+i*0.44):.0f} {20*math.sin(3.5+i*0.44):.0f}"/>' for i in range(8)) + f'''
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['gold'][0]}" stroke-width="5"><path d="M270 200h60"/></g>''', ground=False)

add('exonerate', '調べの結果、容疑が晴れて手錠が外れる', f'''
{split()}
{table(380)}
{person(150, 380, 1.1, 1, 'blue', 'blue', 'hold', 'short', 'sad')}
<g transform="translate(150 260)">
  <circle cx="-22" r="18" fill="none" stroke="#8f9aa6" stroke-width="7"/>
  <circle cx="22" r="18" fill="none" stroke="#8f9aa6" stroke-width="7"/>
  <path d="M-6 0h12" stroke="#8f9aa6" stroke-width="7" fill="none"/>
</g>
{person(450, 380, 1.1, 1, 'coral', 'blue', 'up', 'short', 'smile')}
<g transform="translate(510 190)">
  <circle cx="-14" r="16" fill="none" stroke="#8f9aa6" stroke-width="6" transform="rotate(30 -14 0)"/>
  <circle cx="22" r="16" fill="none" stroke="#8f9aa6" stroke-width="6" transform="rotate(-20 22 0)"/>
</g>
<g transform="translate(300 130)">
  {doc(0, 0, 100, 120, 3)}
  {tick(0, 34, 0.4)}
</g>
{cross(150, 130, 0.6)}''', ground=False)

add('fabricate', 'ありもしない話をでっち上げて書き上げる', f'''
{table(380)}
{person(140, 380, 1.05, 1, 'violet', 'blue', 'reach', 'bun', 'neutral')}
<g transform="translate(340 220) rotate(-4)">
  {doc(0, 0, 200, 240, 5)}
  <path d="M-70 90q40-24 70 0" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"/>
</g>
<g transform="translate(220 280) rotate(30)">
  <path d="M0-80l12 26v70h-24V-54z" class="violet o"/>
  <path d="M-12 16h24v36l-12 22-12-22z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g transform="translate(500 130)">
  <path d="M-40-30h80q10 0 10 10v30q0 10-10 10h-52l-18 14v-14q-10 0-10-10v-30q0-10 10-10z" fill="#fffefd" class="o" opacity="0.85"/>
  <g fill="{MUTED}" opacity="0.6"><rect x="-26" y="-12" width="52" height="9" rx="4.5"/><rect x="-26" y="4" width="36" height="9" rx="4.5"/></g>
</g>
{cross(500, 240, 0.6)}''', ground=False)

add('falsify', '記録の数字を書き換えて改ざんする', f'''
{table(380)}
<g transform="translate(300 200) rotate(-3)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <g>
''' + ''.join(f'''<g transform="translate(0 {-96+i*46})">
  <rect x="-130" y="-7" width="{120-(i%3)*24}" height="14" rx="7" fill="{MUTED}"/>
  <rect x="{56+(i%2)*14}" y="-7" width="{60-(i%2)*14}" height="14" rx="7" fill="{MUTED}"/>
</g>''' for i in range(5)) + f'''
  </g>
  <path d="M46 32h100" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round" fill="none"/>
  <rect x="60" y="46" width="80" height="18" rx="9" class="coral"/>
</g>
<g transform="translate(470 300) rotate(30)">
  <path d="M0-80l12 26v70h-24V-54z" class="coral o"/>
  <path d="M-12 16h24v36l-12 22-12-22z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
{cross(120, 120, 0.7)}''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
