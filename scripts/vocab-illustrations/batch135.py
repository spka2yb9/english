# -*- coding: utf-8 -*-
"""第135回。画面まわりの語、un- の形容詞、量を表す連語。"""
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


# --- 画面まわり ---------------------------------------------------------------
add('upload', '手元の写真を上のサーバーへ送り上げる', f'''
{table(380)}
<g transform="translate(220 300)">
  <path d="M-100-60h200v110h-200z" fill="#3b4450" class="o"/>
  <path d="M-90-50h180v90h-180z" fill="#dceaf4"/>
  <path d="M-30 50h60v14h-60z" fill="#5a6270"/>
  <path d="M-70 30L-20-30l30 34 26-40 44 66z" class="greenp o"/>
</g>
<g transform="translate(450 120)">
  <path d="M-90-50h180v100h-180z" fill="#5a6270" class="o"/>
  <g fill="{TONES['green'][0]}"><circle cx="-60" cy="-24" r="7"/><circle cx="-60" cy="4" r="7"/><circle cx="-60" cy="30" r="7"/></g>
  <g fill="none" stroke="#8f9aa6" stroke-width="3"><path d="M-90-10h180M-90 18h180"/></g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="6"><path d="M300 260L400 170"/></g>
<g fill="{TONES['green'][0]}"><path d="M330 240l-6-30 34 8z"/></g>''', ground=False)

add('username', 'ログイン画面の名前の欄だけが囲まれている', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-190-140h380v260h-380z" fill="#3b4450" class="o"/>
  <path d="M-170-120h340v220h-340z" fill="#eef2f6"/>
  <g transform="translate(0 -70)">
    <circle r="28" fill="{TONES['teal'][1]}" class="o"/>
    <circle cy="-8" r="10" fill="{TONES['teal'][0]}"/>
    <path d="M-16 18q16-18 32 0z" fill="{TONES['teal'][0]}"/>
  </g>
  <path d="M-120-20h240v34h-240z" fill="#fffefd" class="o"/>
  {word(-40, -3, 4, 22, INK)}
  <path d="M-120 30h240v34h-240z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}"><circle cx="-100" cy="47" r="7"/><circle cx="-80" cy="47" r="7"/><circle cx="-60" cy="47" r="7"/></g>
  <path d="M-134-32h268v56h-268z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M540 340l-90-160"/></g>''', arrow=True, ground=False)

add('troll', '掲示板にわざと荒らしの書き込みをする', f'''
{table(380)}
<g transform="translate(320 190)">
  <path d="M-200-140h400v250h-400z" fill="#3b4450" class="o"/>
  <path d="M-180-120h360v210h-360z" fill="#eef2f6"/>
  <g>
''' + ''.join(f'''<g transform="translate(0 {-86+i*54})">
  <circle cx="-150" r="16" fill="{TONES[["teal","coral","gold"][i]][1]}" class="o"/>
  <rect x="-124" y="-9" width="{240-(i%3)*40}" height="18" rx="9" fill="{MUTED if i!=1 else TONES['coral'][0]}"/>
</g>''' for i in range(3)) + f'''
  </g>
  <path d="M-140-40h300v40h-300z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
</g>
{person(110, 380, 0.9, 1, 'violet', 'blue', 'reach', 'cap', 'neutral')}
<g fill="{INK}" opacity="0.2"><path d="M40 200h140v180H40z"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M200 260l-30-24"/>
</g>''', ground=False)

add('viral', '一つの投稿が短い間に爆発的に広まる', f'''
<path d="M0 0h600v400H0z" fill="#eef2f6"/>
<g transform="translate(120 200)">
  <path d="M-60-40h120v80h-120z" class="coral o"/>
  <rect x="-40" y="-10" width="80" height="20" rx="10" fill="#fffefd"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="4">
  <path d="M190 180l70-60M190 200h70M190 220l70 60"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="3">
''' + ''.join(f'<path d="M{300+ (i%3)*0} {120+ (i//3)*80}l60 {-40+ (i%3)*40}"/>' for i in range(9)) + f'''
</g>
<g>
{head(290, 120, 20, 'teal', 'short')}
{head(290, 200, 20, 'gold', 'bob')}
{head(290, 290, 20, 'violet', 'cap')}
''' + ''.join(head(420+ (i%2)*80, 70+i*44, 16, ['coral','teal','gold','violet','green','blue'][i%6], ['short','bob','bun','cap'][i%4]) for i in range(7)) + f'''
</g>''', ground=False)

add('trending', '話題の順に並んだ一覧の一位が急上昇している', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-190-150h380v300h-380z" fill="#3b4450" class="o"/>
  <path d="M-170-130h340v260h-340z" fill="#eef2f6"/>
  <g>
''' + ''.join(f'''<g transform="translate(0 {-90+i*54})">
  <circle cx="-140" r="16" fill="{TONES['teal'][1]}" class="o"/>
  <rect x="-114" y="-9" width="{200-i*30}" height="18" rx="9" fill="{INK if i==0 else MUTED}"/>
</g>''' for i in range(4)) + f'''
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linejoin="round">
    <path d="M100-104l30-24 34 20"/>
  </g>
  <path d="M164-108l6-26 22 16z" fill="{TONES['coral'][0]}"/>
</g>''', ground=False)

# --- 物 ---------------------------------------------------------------------
add('wallet', '札とカードを入れる二つ折りの財布', f'''
{table(340)}
<g transform="translate(300 250)">
  <path d="M-120-60h240v110q0 14-120 14t-120-14z" fill="#8b6437" class="o"/>
  <path d="M-120-60q120-30 240 0" fill="none" stroke="#6b4c28" stroke-width="4"/>
  <path d="M40-20h100v50H40z" class="greenp o"/>
  <path d="M-100-40h110v30h-110z" fill="#fffdf6" class="o"/>
  <circle cx="90" cy="5" r="12" fill="none" stroke="{TONES['green'][2]}" stroke-width="3"/>
  <path d="M-60 34h140v14h-140z" fill="#6b4c28"/>
</g>''', ground=False)

add('violin', '弓で四本の弦をこすって音を出す', f'''
{table(380)}
<g transform="translate(280 250) rotate(-20)">
  <path d="M-40 40q-60 0-60-50t60-50q34 0 40 26 6 26 0 48-6 26-40 26z" fill="#c8703a" class="o"/>
  <path d="M40 40q60 0 60-56t-60-56q-38 0-44 30-6 32 0 60 6 22 44 22z" fill="#c8703a" class="o"/>
  <path d="M-20-14q-10 10 0 20M-20 6q10 10 20 0" fill="none" stroke="#8b3a1c" stroke-width="4"/>
  <path d="M100-16h80v32h-80z" fill="#5b4a3c" class="o"/>
  <path d="M180-24h40v48h-40z" fill="#c8703a" class="o"/>
  <g fill="none" stroke="#e8dcc0" stroke-width="2">
''' + ''.join(f'<path d="M-70 {-9+i*6}H200"/>' for i in range(4)) + f'''
  </g>
</g>
<g transform="translate(360 200) rotate(60)">
  <path d="M-110-5h220v10h-220z" fill="#c9a464" class="o"/>
  <path d="M-110-2h220v4h-220z" fill="#e8dcc0"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M450 150q30 40 0 80M490 120q46 70 0 140"/>
</g>''', ground=False)

add('yoghurt', 'ふたを開けたカップに白いヨーグルトが入っている', f'''
{table(330)}
<g transform="translate(280 260)">
  <path d="M-70-70h140l-16 110q-2 16-54 16t-54-16z" class="bluep o"/>
  <ellipse cy="-70" rx="70" ry="18" fill="#fffdf6" class="o"/>
  <path d="M-56-30h112l-10 66q-2 12-46 12t-46-12z" class="blue" opacity="0.35"/>
</g>
<g transform="translate(430 170) rotate(24)">
  <ellipse rx="60" ry="16" fill="#c8d0d8" class="o"/>
  <path d="M-60 0q0 10 60 10t60-10" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>
<g transform="translate(180 250) rotate(-20)">
  <path d="M-6-70h12v100h-12z" fill="#c8d0d8" class="o"/>
  <ellipse cy="-84" rx="20" ry="26" fill="#c8d0d8" class="o"/>
  <ellipse cy="-84" rx="13" ry="18" fill="#fffdf6"/>
</g>''', ground=False)

add('almond', '殻から出た細長いアーモンドの実', f'''
{table(330)}
<g transform="translate(200 250)">
  <path d="M0-70q40 30 40 70t-40 44-40-44 40-70z" fill="#c8a070" class="o"/>
  <g fill="none" stroke="#a8804c" stroke-width="3"><path d="M0-50v90"/></g>
</g>
<g transform="translate(340 270) rotate(20)">
  <path d="M0-60q34 26 34 60t-34 38-34-38 34-60z" fill="#c8a070" class="o"/>
</g>
<g transform="translate(460 250)">
  <path d="M0-80q46 34 46 80t-46 50-46-50 46-80z" fill="#8b6437" class="o"/>
  <path d="M-30-20q30-24 60 0-30 44-60 0z" fill="#e8d0b0" class="o"/>
  <g fill="none" stroke="#6b4c28" stroke-width="3"><path d="M-20-40q20 60 40 0"/></g>
</g>''', ground=False)

add('allergy', '花粉を吸ってくしゃみと発疹が出る', f'''
{table(380)}
{person(200, 380, 1.1, 1, 'coral', 'blue', 'up', 'bob', 'sad')}
<g transform="translate(200 250)">
  <path d="M-20-6q12-14 24 0M0-6q12-14 24 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round" transform="translate(-12 0)"/>
  <ellipse cy="20" rx="18" ry="14" fill="{INK}"/>
</g>
<g fill="{TONES['blue'][1]}" stroke="{TONES['blue'][0]}" stroke-width="2">
''' + ''.join(f'<circle cx="{280+i*30}" cy="{240+ (i%3)*24}" r="{9-(i%3)*2}"/>' for i in range(5)) + f'''
</g>
<g fill="{TONES['coral'][0]}">
''' + ''.join(f'<circle cx="{160+ (i%4)*24}" cy="{300+(i//4)*22}" r="6"/>' for i in range(8)) + f'''
</g>
<g transform="translate(470 250)">
  <path d="M-8 0v-70h16V0z" class="greend o"/>
  <g class="gold o">
''' + ''.join(f'<ellipse cx="{34*math.cos(j*1.2566):.0f}" cy="{-100+34*math.sin(j*1.2566):.0f}" rx="24" ry="19" transform="rotate({j*72} {34*math.cos(j*1.2566):.0f} {-100+34*math.sin(j*1.2566):.0f})"/>' for j in range(5)) + f'''
  </g>
  <circle cy="-100" r="16" class="goldd o"/>
</g>
<g fill="{TONES['gold'][0]}">
''' + ''.join(f'<circle cx="{400-i*24}" cy="{180+ (i%3)*22}" r="5"/>' for i in range(5)) + f'''
</g>''', ground=False)

add('veil', '顔の前に薄い布をかけて隠す', f'''
{table(380)}
{person(300, 380, 1.2, 1, 'violet', 'blue', 'stand', 'bun', 'smile')}
<g transform="translate(300 240)">
  <path d="M-50-60q50-30 100 0 16 90-10 116-40 14-80 0-26-26-10-116z" fill="#fffefd" class="o" opacity="0.62"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2" opacity="0.7">
''' + ''.join(f'<path d="M{-40+i*20} -70v130"/>' for i in range(5)) + f'''
''' + ''.join(f'<path d="M-52 {-40+i*30}h104"/>' for i in range(4)) + f'''
  </g>
  <path d="M-50-60q50-30 100 0" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 200l-110 30"/></g>''', arrow=True, ground=False)

add('vacation', '休みの日に海辺でくつろぐ', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v70H0z" fill="#7aa8c4"/>
<path d="M0 300h600v100H0z" fill="#f0dfb8"/>
<path d="M0 230h600M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
{sun(500, 80, 38)}
<g transform="translate(220 300)">
  <path d="M-6 0v-90h12V0z" fill="{BRN}"/>
  <path d="M-100-90h200q-34-50-100-50t-100 50z" class="coralp o"/>
  <path d="M-100-90h200" fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"/>
</g>
<g transform="translate(250 350) rotate(-8)">
  <path d="M-80-16h160v32h-160z" class="tealp o"/>
  <path d="M-80-16h160" fill="none" stroke="{TONES['teal'][0]}" stroke-width="3"/>
  <path d="M50-40h30v24h-30z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2"/>
</g>
<g transform="translate(470 330)">
  <path d="M-6 0v-70h12V0z" fill="{BRN}"/>
  <path d="M-40-70q-30-20-40-44 40 4 50 40zM6-74q30-24 60-6-30 30-60 6zM0-74q-14-40 4-52 20 14 6 52z" class="greenp o"/>
</g>''', ground=False)

add('weekday', 'カレンダーで月から金までの五日が色分けされている', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-200-150h400v300h-400z" class="paper"/>
  <path d="M-200-150h400v56h-400z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5">
''' + ''.join(f'<path d="M{-200+i*57} -94v244"/>' for i in range(8)) + ''.join(f'<path d="M-200 {-40+i*50}h400"/>' for i in range(4)) + f'''
  </g>
  <path d="M-200-94h285v244h-285z" class="tealp" opacity="0.55"/>
  <g fill="{INK}">
''' + ''.join(f'<rect x="{-186+i*57}" y="-130" width="30" height="14" rx="7"/>' for i in range(5)) + f'''
  </g>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="{100+i*57}" y="-130" width="30" height="14" rx="7"/>' for i in range(2)) + f'''
  </g>
</g>''', ground=False)

add('weekend', 'カレンダーの土日の二日だけが色づいている', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-200-150h400v300h-400z" class="paper"/>
  <path d="M-200-150h400v56h-400z" class="coral o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5">
''' + ''.join(f'<path d="M{-200+i*57} -94v244"/>' for i in range(8)) + ''.join(f'<path d="M-200 {-40+i*50}h400"/>' for i in range(4)) + f'''
  </g>
  <path d="M85-94h115v244H85z" class="coralp" opacity="0.65"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="{-186+i*57}" y="-130" width="30" height="14" rx="7"/>' for i in range(5)) + f'''
  </g>
  <g fill="{INK}">
''' + ''.join(f'<rect x="{100+i*57}" y="-130" width="30" height="14" rx="7"/>' for i in range(2)) + f'''
  </g>
</g>''', ground=False)

add('subpoena', '出廷を命じる召喚状が手渡される', f'''
{table(380)}
<g transform="translate(300 200) rotate(-4)">
  <path d="M-150-140h300v260h-300z" class="paper"/>
  <rect x="-110" y="-112" width="180" height="18" rx="9" fill="{INK}"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-110" y="{-64+i*32}" width="{220-(i%3)*50}" height="10" rx="5"/>' for i in range(4)) + f'''
  </g>
  <circle cx="90" cy="76" r="26" class="coral o"/>
  <g transform="translate(-90 76)">
    <path d="M-40-10h80v6h-80z" fill="#c9a464"/>
    <path d="M-6-4h12v14h-12z" fill="#c9a464"/>
    <path d="M-24-24h48v14h-48z" fill="#c9a464" class="o"/>
  </g>
</g>
{person(90, 380, 0.8, 1, 'violet', 'blue', 'give', 'cap', 'neutral')}
{person(530, 380, 0.8, -1, 'coral', 'blue', 'give', 'short', 'sad')}''', ground=False)

# --- 動詞 -------------------------------------------------------------------
add('understate', '大きな成果を、ごく小さなことのように言う', f'''
{table(380)}
<g transform="translate(400 260)">
  <path d="M-110-100h220v200h-220z" class="tealp o"/>
  <path d="M-110-100l20-24h220l-20 24z" fill="{TONES['teal'][1]}" class="o"/>
</g>
{person(120, 380, 1.05, 1, 'coral', 'blue', 'point', 'bun', 'smile')}
<g transform="translate(220 150)">
  <path d="M-60-40h120q12 0 12 12v40q0 12-12 12h-84l-18 16v-16q-12 0-12-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <path d="M-14-10h28v26h-28z" class="tealp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M290 180q40 20 60 40"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M300 350l-90-140"/></g>''', ground=False)

add('utilise', '余っていた木箱をいすとして役立てる', f'''
{split()}
{table(380)}
<g transform="translate(150 320)">
  <path d="M-70-60h140v60h-140z" fill="#c9a464" class="o"/>
  <path d="M-70-60l16-20h140l-16 20z" fill="#d9b877" class="o"/>
  <path d="M70-60l16-20v60l-16 20z" fill="#a0764a" class="o"/>
</g>
<g fill="{MUTED}" opacity="0.4"><path d="M60 240h180v40H60z"/></g>
<g transform="translate(450 320)">
  <path d="M-70-60h140v60h-140z" fill="#c9a464" class="o"/>
  <path d="M-70-60l16-20h140l-16 20z" fill="#d9b877" class="o"/>
</g>
{sit(450, 320, 0.95, 1, 'coral', 'blue', 'bun', 'smile', 'lap')}
{tick(450, 130, 0.6)}
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', ground=False)

add('vindicate', '疑われていた人の正しさが証拠で証明される', f'''
{split()}
{table(380)}
{person(150, 380, 1.05, 1, 'blue', 'blue', 'stand', 'short', 'sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M90 230l-26-20M210 226l26-20"/>
</g>
<g transform="translate(150 150)">
  <path d="M-40-30h80q10 0 10 10v30q0 10-10 10h-52l-18 14v-14q-10 0-10-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M-16-16q0-16 16-16t16 16-16 14v8" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>
  <circle cy="18" r="4" fill="{MUTED}"/>
</g>
{person(450, 380, 1.05, 1, 'coral', 'blue', 'up', 'short', 'smile')}
<g transform="translate(450 160)">
  {doc(0, 0, 110, 120, 3)}
  {tick(0, 34, 0.4)}
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}"><path d="M270 300h60"/></g>''', ground=False)

add('whiten', 'くすんだシャツを洗って白くする', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-60-70q60-30 120 0l-10 130h-100z" fill="#d8d0c0" class="o"/>
  <path d="M-60-70l-40 40 20 20 26-24M60-70l40 40-20 20-26-24" fill="#d8d0c0" class="o"/>
</g>
<g transform="translate(450 250)">
  <path d="M-60-70q60-30 120 0l-10 130h-100z" fill="#fffefd" class="o"/>
  <path d="M-60-70l-40 40 20 20 26-24M60-70l40 40-20 20-26-24" fill="#fffefd" class="o"/>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
    <path d="M84-70l24-20M100-20h26"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('withhold', '渡すはずの書類を手元にとどめて渡さない', f'''
{table(380)}
{person(180, 380, 1.05, 1, 'violet', 'blue', 'hold', 'bun', 'neutral')}
{person(450, 380, 1.05, -1, 'coral', 'blue', 'reach', 'short', 'sad')}
<g transform="translate(210 260)">{doc(0, 0, 100, 120, 3)}</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M380 250h-70"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M300 180l40 40M340 180l-40 40"/>
</g>''', ground=False)

add('withstand', '強風の中でも折れずに立ち続ける木', f'''
<path d="M0 0h600v400H0z" fill="#c8d2da"/>
{table(370)}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M20 110q80-24 150 0t150-10M20 190q80-24 150 0t150-10M20 270q70-22 130 0"/>
</g>
<g transform="translate(400 370)">
  <path d="M-24 0h48v-160h-48z" fill="{BRN}" class="o"/>
  <g class="greenp o" transform="rotate(-8 0 -160)">
    <circle cx="-56" cy="-200" r="52"/><circle cx="20" cy="-232" r="60"/><circle cx="80" cy="-196" r="48"/>
  </g>
  <g stroke="{BRN}" stroke-width="10" stroke-linecap="round" fill="none">
    <path d="M0 0l-50 20M0 0l50 20"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M540 300v-70"/></g>''', ground=False)

add('verge', '崖のふちすれすれのところに立つ', f'''
<path d="M0 0h600v260H0z" fill="#dceaf4"/>
<path d="M0 260h300v140H0z" fill="#c9d8c0" class="o"/>
<path d="M300 260q0 60-24 140h-30q40-80 30-140z" fill="#a8845c"/>
<path d="M0 380h600v20H0z" fill="#8f9aa6" opacity="0.4"/>
{person(230, 260, 1.0, 1, 'coral', 'blue', 'up', 'cap', 'surprised')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="16 12"><path d="M300 240v-90"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M420 200l-100 50"/></g>
{sun(510, 70, 30)}''', ground=False)

# --- un- の形容詞 --------------------------------------------------------------
add('unfamiliar', '見慣れた道具の横に、見たことのない道具がある', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-10-70h20v90h-20z" fill="#8f9aa6" class="o"/>
  <path d="M-30 20h40v40q0 10-20 10t-20-10z" fill="{INK}"/>
  <path d="M-10-70l-16-18h52l-16 18z" fill="#b8bfc8" class="o"/>
</g>
{tick(150, 120, 0.6)}
<g transform="translate(450 250)">
  <path d="M-50-50q50-30 100 0-10 60-40 70-40 4-50-24-16-24-10-46z" fill="#9aa5b0" class="o"/>
  <path d="M-10 20h20v70h-20z" fill="#8f9aa6" class="o"/>
  <circle cx="20" cy="-20" r="14" fill="#c8d0d8" class="o"/>
</g>
<g transform="translate(540 140)">
  <path d="M-18-30q0-24 18-24t18 24-18 20v12" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="26" r="5.5" fill="{INK}"/>
</g>''', ground=False)

add('unhelpful', '尋ねても肩をすくめるだけで助けにならない', f'''
{table(380)}
{person(180, 380, 1.05, 1, 'coral', 'blue', 'up', 'bob', 'sad')}
{person(450, 380, 1.05, -1, 'blue', 'blue', 'up', 'short', 'neutral')}
<g transform="translate(300 160)">
  <path d="M-50-40h100q12 0 12 12v40q0 12-12 12h-66l-20 16v-16q-14 0-14-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <path d="M-16-24q0-18 16-18t16 18-16 14v10" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle cy="18" r="4.5" fill="{INK}"/>
</g>
<g transform="translate(450 250)">
  <path d="M-60-10q60-24 120 0" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
  <path d="M-60-10q60-24 120 0" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
</g>
{cross(300, 300, 0.7)}''', ground=False)

add('unlimited', '回数の上限がなく、いくらでも使える', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-90-70h180v140h-180z" class="paper"/>
  <g fill="{TONES['teal'][0]}">
''' + ''.join(f'<circle cx="{-56+ (i%3)*56}" cy="{-30+(i//3)*56}" r="18"/>' for i in range(6)) + f'''
  </g>
  <g fill="{MUTED}"><circle cx="0" cy="26" r="18"/><circle cx="56" cy="26" r="18"/></g>
</g>
<g transform="translate(450 250)">
  <path d="M-90-70h180v140h-180z" class="paper"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="14" stroke-linecap="round">
    <path d="M-40 0q0-34 20-34t20 34 20 34 20-34-20-34-20 34-20 34-20-34z"/>
  </g>
</g>
{tick(450, 130, 0.6)}''', ground=False)

add('unsafe', '手すりのない足場と、手すりのある足場', f'''
{split()}
{table(380)}
<g transform="translate(150 300)">
  <path d="M-100-14h200v28h-200z" fill="#c9a464" class="o"/>
  <path d="M-80 14v70M80 14v70" stroke="#8f9aa6" stroke-width="10" fill="none"/>
</g>
{person(150, 300, 0.8, 1, 'coral', 'blue', 'up', 'cap', 'sad')}
{cross(150, 130, 0.6)}
<g transform="translate(450 300)">
  <path d="M-100-14h200v28h-200z" fill="#c9a464" class="o"/>
  <path d="M-80 14v70M80 14v70" stroke="#8f9aa6" stroke-width="10" fill="none"/>
  <g fill="none" stroke="#8f9aa6" stroke-width="8">
    <path d="M-100-80h200M-100-14v-70M100-14v-70M-100-48h200"/>
  </g>
</g>
{person(450, 300, 0.8, 1, 'coral', 'blue', 'stand', 'cap', 'smile')}
{tick(450, 130, 0.6)}''', ground=False)

add('unsuccessful', '的を外れた矢と、的に当たった矢', f'''
{split()}
{table(380)}
<g transform="translate(150 240)">
  <circle r="80" fill="#fffdf6" class="o"/>
  <circle r="56" class="coralp o"/><circle r="32" fill="#fffdf6" class="o"/><circle r="12" class="coral o"/>
  <path d="M-160 90L-30 40" stroke="{BRN}" stroke-width="6" fill="none"/>
  <path d="M-30 40l-26 8 8-18z" fill="{INK}"/>
</g>
{cross(150, 120, 0.6)}
<g transform="translate(450 240)">
  <circle r="80" fill="#fffdf6" class="o"/>
  <circle r="56" class="coralp o"/><circle r="32" fill="#fffdf6" class="o"/><circle r="12" class="coral o"/>
  <path d="M-160-60L-10-4" stroke="{BRN}" stroke-width="6" fill="none"/>
  <path d="M-10-4l-28-4 10-16z" fill="{INK}"/>
</g>
{tick(450, 120, 0.6)}''', ground=False)

add('ambiguous', '上から見ると丸、横から見ると四角に見える形', f'''
{table(380)}
<g transform="translate(300 230)">
  <path d="M-70-90h140v180h-140z" class="tealp o"/>
  <ellipse cy="-90" rx="70" ry="26" class="teal o"/>
  <ellipse cy="90" rx="70" ry="26" fill="{TONES['teal'][2]}" class="o"/>
</g>
<g transform="translate(110 140)">
  <circle r="46" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 8"/>
  <circle r="26" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<g transform="translate(500 300)">
  <path d="M-40-40h80v80h-80z" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 8"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}"><path d="M180 170l60 30M450 290l-90-30"/></g>
<g transform="translate(300 60)">
  <path d="M-16-26q0-22 16-22t16 22-16 18v10" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle cy="22" r="5" fill="{INK}"/>
</g>''', ground=False)

add('abrupt', 'なめらかだった道が突然途切れて段になる', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v170H0z" fill="#c9d8c0"/>
<path d="M0 230h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M0 400V300h300V150h300v250z" fill="#a8845c" class="o"/>
<g fill="none" stroke="#8f6f4a" stroke-width="4"><path d="M0 340h280M340 220h260"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="14 10"><path d="M300 300V150"/></g>
{person(180, 300, 0.9, 1, 'teal', 'blue', 'walk', 'cap', 'surprised', 'walk')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M420 100l-100 90"/></g>''', ground=False)

add('acidic', 'レモンをなめて口をすぼめる', f'''
{table(340)}
<g transform="translate(430 270)">
  <path d="M-70 0q0-46 70-46t70 46-70 46-70-46z" class="gold o"/>
  <path d="M-70 0q0-46 70-46" fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"/>
  <path d="M-84 0h-16M84 0h16" stroke="{TONES['gold'][2]}" stroke-width="6" stroke-linecap="round" fill="none"/>
</g>
<g transform="translate(200 210)">
  <circle r="100" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-70-24q26-22 46 0M24-24q26-22 46 0" fill="none" stroke="{HAIR}" stroke-width="7" stroke-linecap="round"/>
  <path d="M-42 6q14-14 26 0M16 6q14-14 26 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <ellipse cy="50" rx="18" ry="14" fill="{INK}"/>
  <g fill="none" stroke="{SKINL}" stroke-width="3"><path d="M-30 40q30-14 60 0"/></g>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M320 140l-24-22M330 210h-26M320 280l-24 22"/>
</g>''', ground=False)

add('adept', '同じ道具を、片方だけが手早く上手に使う', f'''
{split()}
{table(380)}
{person(150, 380, 1.05, 1, 'blue', 'blue', 'reach', 'short', 'sad')}
<g transform="translate(150 280)">
  <path d="M-50-30h100v50h-100z" class="tealp o"/>
  <path d="M-30-10l60 30M30-10l-60 30" stroke="{TONES['coral'][0]}" stroke-width="4" fill="none"/>
</g>
{person(450, 380, 1.05, 1, 'coral', 'blue', 'reach', 'bun', 'smile')}
<g transform="translate(450 280)">
  <path d="M-50-30h100v50h-100z" class="tealp o"/>
  {tick(20, 0, 0.35)}
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M540 220l-24-18M550 280h-26"/>
</g>''', ground=False)

add('admirable', '困っている人を助ける姿に周りが感心する', f'''
{table(380)}
{person(200, 380, 1.05, 1, 'coral', 'blue', 'reach', 'bun', 'smile')}
{sit(330, 380, 0.9, -1, 'blue', 'blue', 'short', 'sad', 'down')}
<g>
  <path d="M256 260q50-14 90 6" stroke="{SKINL}" stroke-width="22" stroke-linecap="round" fill="none"/>
  <path d="M256 260q50-14 90 6" stroke="{SKIN}" stroke-width="18" stroke-linecap="round" fill="none"/>
</g>
{head(480, 300, 22, 'teal', 'short')}
{head(540, 330, 22, 'violet', 'bun')}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M120 220l-26-22M180 170l4-26"/>
</g>
<g transform="translate(500 190)">
  <path d="M-30-24h60q10 0 10 10v24q0 10-10 10h-40l-14 12v-12q-16 0-16-10v-24q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M0-14l7 14 15 2-11 10 3 16-14-8-14 8 3-16-11-10 15-2z" class="gold"/>
</g>''', ground=False)

add('advisable', '専門家が「そうしたほうがよい」と勧める', f'''
{table(380)}
{person(160, 380, 1.05, 1, 'teal', 'teal', 'point', 'bun', 'smile')}
{person(450, 380, 1.05, -1, 'coral', 'blue', 'stand', 'short', 'neutral')}
<g transform="translate(300 170)">
  <path d="M-70-40h140q12 0 12 12v40q0 12-12 12h-96l-22 16v-16q-12 0-12-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <path d="M0-20q18 0 18 16t-10 16v6h-16v-6q-10 0-10-16t18-16z" class="gold"/>
</g>
{tick(520, 200, 0.6)}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M380 220h60"/></g>''', ground=False)

add('aerobic', '息を切らさない速さで長く走り続ける', f'''
{table(380)}
{person(300, 380, 1.15, 1, 'coral', 'blue', 'walk', 'cap', 'smile', 'walk')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M120 230h60M100 280h44M130 330h56"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M420 220q16-20 0-36M450 230q22-26 0-52"/>
</g>
<g transform="translate(500 130)">
  <circle r="46" fill="#fffdf6" class="o"/>
  <path d="M-30 0h12l8-18 10 34 10-24 8 8h12" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linejoin="round"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 130h300"/></g>''', arrow=True, ground=False)

add('affirmative', 'はいという答えに丸がついている', f'''
{table(380)}
<g transform="translate(300 210)">
  <path d="M-170-130h340v260h-340z" class="paper"/>
  <g fill="{MUTED}"><rect x="-130" y="-104" width="200" height="14" rx="7"/></g>
  <g transform="translate(-70 -20)">
    <circle r="24" fill="none" stroke="{TONES['green'][0]}" stroke-width="6"/>
    <rect x="40" y="-9" width="90" height="18" rx="9" fill="{INK}"/>
  </g>
  <g transform="translate(-70 60)">
    <circle r="24" fill="none" stroke="{MUTED}" stroke-width="4"/>
    <rect x="40" y="-9" width="70" height="18" rx="9" fill="{MUTED}"/>
  </g>
</g>
{tick(480, 120, 0.7)}''', ground=False)

add('agreeable', '感じよくほほえんで受け入れる', f'''
{table(380)}
{person(200, 380, 1.1, 1, 'teal', 'blue', 'up', 'bob', 'smile')}
{person(450, 380, 1.05, -1, 'coral', 'blue', 'give', 'short', 'smile')}
<g transform="translate(320 170)">
  <path d="M-60-36h120q12 0 12 12v36q0 12-12 12h-80l-20 16v-16q-12 0-12-12v-36q0-12 12-12z" fill="#fffefd" class="o"/>
  {tick(0, -4, 0.42)}
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M120 220l-24-18M280 200l6-26"/>
</g>''', ground=False)

add('akin', '犬とオオカミのように、種類の近い二つ', f'''
{split()}
{table(380)}
<g transform="translate(150 300)">
  <ellipse rx="70" ry="44" fill="#c8a070" class="o"/>
  <circle cx="60" cy="-34" r="30" fill="#c8a070" class="o"/>
  <path d="M40-56q-10-40 6-40 14 6 10 40zM76-56q10-38 26-30 6 12-10 32z" fill="#a8804c" class="o"/>
  <path d="M86-26l24 8-24 10z" fill="#a8804c" class="o"/>
  <circle cx="70" cy="-38" r="4" fill="{INK}"/>
  <path d="M-70-4q-40-30-54 0 34 26 54 6z" fill="#c8a070" class="o"/>
  <g stroke="#a8804c" stroke-width="10" stroke-linecap="round" fill="none"><path d="M-30 42v20M20 42v20"/></g>
</g>
<g transform="translate(450 300)">
  <ellipse rx="74" ry="46" fill="#8f9aa6" class="o"/>
  <circle cx="64" cy="-36" r="32" fill="#8f9aa6" class="o"/>
  <path d="M44-60q-10-42 6-42 14 6 10 42zM82-60q10-40 26-32 6 12-10 34z" fill="#7d8894" class="o"/>
  <path d="M92-28l26 8-26 10z" fill="#7d8894" class="o"/>
  <circle cx="74" cy="-40" r="4" fill="{INK}"/>
  <path d="M-74-6q-44-24-56 8 38 22 56 2z" fill="#8f9aa6" class="o"/>
  <g stroke="#7d8894" stroke-width="10" stroke-linecap="round" fill="none"><path d="M-30 44v20M20 44v20"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M270 160q30-14 60 0M270 186q30-14 60 0"/>
</g>''', ground=False)

add('aloof', '輪に加わらず、離れたところで一人でいる', f'''
{table(380)}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="12 10"><ellipse cx="220" cy="290" rx="150" ry="90"/></g>
{head(150, 250, 22, 'teal', 'short')}
{head(290, 245, 22, 'coral', 'bun')}
{head(160, 330, 22, 'gold', 'cap')}
{head(280, 330, 22, 'green', 'bob')}
{head(220, 288, 22, 'violet', 'short')}
{person(520, 380, 1.0, -1, 'blue', 'blue', 'stand', 'short', 'neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M410 120v260"/></g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}"><path d="M470 200l-60 20"/></g>''', ground=False)

# --- 副詞・連語 ---------------------------------------------------------------
add('visibly', 'だれの目にもはっきり分かるほど震えている', f'''
{table(380)}
{person(300, 380, 1.2, 1, 'blue', 'blue', 'stand', 'short', 'sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M200 240q-16 12-16 26M400 236q16 12 16 26M190 300q-20 10-24 24M410 296q20 10 24 24"/>
</g>
{head(90, 320, 22, 'teal', 'short')}
{head(520, 320, 22, 'coral', 'bun')}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M130 290h90M470 290h-90"/></g>
<g transform="translate(300 110)">
  <ellipse rx="46" ry="30" fill="#fffefd" class="o"/>
  <circle r="16" fill="{INK}"/>
</g>''', ground=False)

add('instead-of', 'コーヒーの代わりにお茶を選ぶ', f'''
{table(340)}
<g transform="translate(180 270)">
  <path d="M-44-50h88l-10 70q-2 12-34 12t-34-12z" fill="#e8f0f6" class="o"/>
  <path d="M-38-20h76l-6 40q-2 10-32 10t-32-10z" fill="#6b4c28"/>
  <path d="M44-40q34 0 34 22t-34 22" fill="none" stroke="{INK}" stroke-width="7"/>
</g>
{cross(180, 270, 1.3)}
<g transform="translate(420 270)">
  <path d="M-44-50h88l-10 70q-2 12-34 12t-34-12z" fill="#e8f0f6" class="o"/>
  <path d="M-38-20h76l-6 40q-2 10-32 10t-32-10z" class="green"/>
  <path d="M44-40q34 0 34 22t-34 22" fill="none" stroke="{INK}" stroke-width="7"/>
</g>
{tick(420, 130, 0.6)}
<g class="a" marker-end="url(#ar)"><path d="M270 150h60"/></g>''', ground=False)

add('pay-attention-to', '黒板の一点をじっと見つめて注意を向ける', f'''
{table(380)}
<g transform="translate(400 200)">
  <path d="M-160-120h320v220h-320z" fill="#2f4a3a" class="o"/>
  <g fill="#e8f0e4">
''' + ''.join(f'<rect x="-130" y="{-90+i*44}" width="{240-(i%3)*60}" height="12" rx="6"/>' for i in range(4)) + f'''
  </g>
  <circle cx="60" cy="20" r="40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
{sit(140, 380, 1.0, 1, 'teal', 'blue', 'bun', 'neutral', 'lap')}
{chair(140, 380, 0.95, 'gold', 1)}
<g transform="translate(158 262)">
  <ellipse cx="-4" rx="13" ry="11" fill="#fffefd" class="o"/><circle cx="0" r="6" fill="{INK}"/>
  <ellipse cx="24" rx="13" ry="11" fill="#fffefd" class="o"/><circle cx="28" r="6" fill="{INK}"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M200 260l240-40"/></g>''', ground=False)

add('proud-of', '子どもの賞状を見せて誇らしく思う', f'''
{table(380)}
{person(200, 380, 1.15, 1, 'coral', 'blue', 'up', 'bun', 'smile')}
{person(400, 380, 0.85, 1, 'teal', 'blue', 'stand', 'cap', 'smile')}
<g transform="translate(310 220) rotate(-6)">
  <path d="M-80-56h160v112h-160z" class="paper"/>
  <rect x="-56" y="-36" width="112" height="14" rx="7" fill="{INK}"/>
  <g fill="{MUTED}"><rect x="-56" y="-10" width="80" height="10" rx="5"/></g>
  <circle cx="46" cy="26" r="20" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M120 210l-26-22M290 150l6-26"/>
</g>
<g fill="{TONES['coral'][0]}">
  <path d="M480 190q-14-20 0-28 14-6 18 10 4-16 18-10 14 8 0 28l-18 20z"/>
</g>''', ground=False)

add('responsible-for', '名札のついた区画をひとりで受け持つ', f'''
{table(380)}
<g transform="translate(300 240)">
  <path d="M-240-100h480v200h-480z" fill="#e8f0e4" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="4"><path d="M-80-100v200M80-100v200"/></g>
  <path d="M-80-100h160v200h-160z" class="tealp o"/>
</g>
{person(300, 340, 0.9, 1, 'teal', 'blue', 'up', 'bun', 'neutral')}
<g transform="translate(300 120)">
  <path d="M-70-26h140v52h-140z" fill="#fffefd" class="o"/>
  {word(0, 0, 4, 26, TONES['teal'][2])}
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['teal'][0]}"><path d="M300 156v40"/></g>''', arrow=True, ground=False)

add('a-variety-of', '形も色もさまざまな品が並んでいる', f'''
{table(340)}
<g class="o">
  <circle cx="110" cy="250" r="34" class="coralp"/>
  <rect x="180" y="216" width="66" height="66" class="tealp"/>
  <path d="M300 216l40 66h-80z" class="goldp"/>
  <ellipse cx="410" cy="250" rx="40" ry="28" class="violetp"/>
  <path d="M500 216l24 22 24-22 0 66h-48z" class="greenp"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><path d="M60 160h480"/></g>
<g class="a" marker-end="url(#ar)"><path d="M60 130h480"/></g>''', arrow=True, ground=False)

add('above-all', 'いくつもの理由の中で、いちばん上の一つが大事', f'''
{table(380)}
<g>
''' + ''.join(f'''<g transform="translate(300 {260+i*50})">
  <path d="M-160-20h320v40h-320z" fill="#e8e2d6" class="o"/>
  <rect x="-130" y="-8" width="{200-i*30}" height="16" rx="8" fill="{MUTED}"/>
</g>''' for i in range(3)) + f'''
</g>
<g transform="translate(300 170)">
  <path d="M-180-30h360v60h-360z" class="goldp o"/>
  <rect x="-150" y="-9" width="240" height="18" rx="9" fill="{INK}"/>
  <path d="M110-14l7 14 15 2-11 12 3 16-14-8-14 8 3-16-11-12 15-2z" class="gold"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['gold'][0]}" stroke-width="5"><path d="M520 300v-110"/></g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
