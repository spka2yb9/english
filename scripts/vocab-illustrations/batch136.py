# -*- coding: utf-8 -*-
"""第136回。人柄を表す形容詞と、量・時を表す連語。"""
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
add('appetizer', '主菜の前に出る小さな一皿', f'''
{table(360)}
<g transform="translate(180 260)">
  <ellipse rx="70" ry="20" fill="#fffdf6" class="o"/>
  <path d="M-70 0q0 24 70 24t70-24z" fill="#fffdf6" class="o"/>
  <g class="o">
    <circle cx="-24" cy="-10" r="16" class="coral"/><circle cx="12" cy="-14" r="14" class="green"/><circle cx="40" cy="-6" r="12" class="gold"/>
  </g>
</g>
<g transform="translate(420 280)">
  <ellipse rx="110" ry="30" fill="#fffdf6" class="o"/>
  <path d="M-110 0q0 36 110 36t110-36z" fill="#fffdf6" class="o"/>
  <path d="M-60-16q60-34 120-4 6 26-30 30-70 6-90-26z" fill="#a8552c" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M260 160h120"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M300 200v140"/></g>''', arrow=True, ground=False)

add('aspirin', '白い小さな錠剤が二錠出ている', f'''
{table(340)}
<g transform="translate(230 250)">
  <path d="M-46-70h92v110q0 16-46 16t-46-16z" fill="#e8f0f6" class="o"/>
  <path d="M-46-70h92v-16h-92z" class="coral o"/>
  <path d="M-36-30h72v58q0 12-36 12t-36-12z" fill="#fffdf6"/>
  <path d="M-24-14h48v10h-48z" class="coralp"/>
</g>
<g class="o">
  <ellipse cx="380" cy="290" rx="34" ry="24" fill="#fffdf6"/>
  <path d="M346 290h68" stroke="{MUTED}" stroke-width="3" fill="none"/>
  <ellipse cx="450" cy="270" rx="34" ry="24" fill="#fffdf6"/>
  <path d="M416 270h68" stroke="{MUTED}" stroke-width="3" fill="none"/>
</g>
<g transform="translate(500 180)">
  <path d="M-8-24h16v16h16v16h-16v16h-16v-16h-16v-16h16z" class="coral o"/>
</g>''', ground=False)

add('atom', '中心の核のまわりを電子が回っている', f'''
<path d="M0 0h600v400H0z" fill="#eef4f8"/>
<g transform="translate(300 200)">
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4">
    <ellipse rx="170" ry="66"/>
    <ellipse rx="170" ry="66" transform="rotate(60)"/>
    <ellipse rx="170" ry="66" transform="rotate(-60)"/>
  </g>
  <g class="coral o">
    <circle cx="-40" cy="-30" r="22"/><circle cx="30" cy="-24" r="22"/><circle cx="6" cy="30" r="22"/>
  </g>
  <g class="teal o"><circle cx="-14" cy="-4" r="20"/><circle cx="24" cy="4" r="20"/></g>
  <g class="blued o">
    <circle cx="170" r="14"/><circle cx="-85" cy="-57" r="14"/><circle cx="-85" cy="57" r="14"/>
  </g>
</g>''', ground=False)

add('banknote', '数字と模様の入った紙のお札', f'''
{table(340)}
<g transform="translate(300 250) rotate(-4)">
  <path d="M-160-80h320v160h-320z" class="greenp o"/>
  <path d="M-140-60h280v120h-280z" fill="none" stroke="{TONES['green'][2]}" stroke-width="3"/>
  <circle cx="-70" r="42" fill="{TONES['green'][1]}" class="o"/>
  <circle cx="-70" cy="-12" r="16" fill="{SKIN}" stroke="{SKINL}" stroke-width="2"/>
  <path d="M-92 24q22-26 44 0z" fill="{TONES['green'][2]}"/>
  {word(60, -20, 3, 34, TONES['green'][2])}
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="3">
    <path d="M20 30q40-14 80 0t40 0"/>
  </g>
</g>''', ground=False)

add('amusement', '芸を見て思わず笑ってしまう', f'''
{table(380)}
<g transform="translate(200 210)">
  <circle r="100" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-86-30q6-70 86-70t86 70q-42-32-86-32t-86 32z" fill="{HAIR}"/>
  <path d="M-54 0q18-16 34 0M20 0q18-16 34 0" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <path d="M-32 44q32 34 64 0-32 12-64 0z" fill="{INK}" class="o"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M330 130l24-22M340 210h30M330 290l24 22"/>
</g>
{person(490, 380, 0.9, -1, 'violet', 'gold', 'up', 'cap', 'smile')}
<g fill="{TONES['gold'][0]}"><circle cx="440" cy="200" r="12"/><circle cx="530" cy="180" r="10"/><circle cx="490" cy="150" r="9"/></g>''', ground=False)

# --- 人柄の形容詞 --------------------------------------------------------------
add('ambivalent', '進むか戻るか、心が二つに割れて決めかねる', f'''
{table(380)}
{person(300, 380, 1.2, 1, 'violet', 'blue', 'think', 'bun', 'neutral')}
<g transform="translate(160 150)">
  <path d="M-60-36h120q12 0 12 12v36q0 12-12 12h-80l-20 16v-16q-12 0-12-12v-36q0-12 12-12z" fill="#fffefd" class="o"/>
  {tick(0, -4, 0.42)}
</g>
<g transform="translate(450 150)">
  <path d="M60-36H-60q-12 0-12 12v36q0 12 12 12h80l20 16v-16q12 0 12-12v-36q0-12-12-12z" fill="#fffefd" class="o"/>
  {cross(0, -4, 0.42)}
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 210l-50-30"/></g>
<g class="a" marker-end="url(#ar)"><path d="M350 210l50-30"/></g>''', arrow=True, ground=False)

add('amiable', '笑顔で手を差し出して気持ちよく迎える', f'''
{table(380)}
{person(200, 380, 1.1, 1, 'teal', 'blue', 'give', 'bun', 'smile')}
{person(430, 380, 1.1, -1, 'coral', 'blue', 'give', 'short', 'smile')}
<g>
  <path d="M268 260q40-14 76 0" stroke="{SKINL}" stroke-width="26" stroke-linecap="round" fill="none"/>
  <path d="M268 260q40-14 76 0" stroke="{SKIN}" stroke-width="21" stroke-linecap="round" fill="none"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M120 210l-24-18M510 200l24-18"/>
</g>''', ground=False)

add('ample', '必要な分をはるかに超えて、たっぷりある', f'''
{split()}
{table(380)}
<g transform="translate(150 320)">
''' + ''.join(f'<circle cx="{-40+i*40}" cy="-20" r="18" class="tealp o"/>' for i in range(3)) + f'''
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 6"><path d="M-70-46h140"/></g>
</g>
<g transform="translate(450 340)">
''' + ''.join(f'<circle cx="{-100+ (i%6)*40}" cy="{-20-(i//6)*40}" r="18" class="tealp o"/>' for i in range(18)) + f'''
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 6"><path d="M-130-46h260"/></g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M560 300v-140"/></g>
{tick(150, 130, 0.5)}''', ground=False)

add('analogous', '心臓とポンプのように、働きの似た二つ', f'''
{split()}
{table(380)}
<g transform="translate(150 240)">
  <path d="M0-50q40-40 70 0 20 40-70 100-90-60-70-100 30-40 70 0z" class="coral o"/>
  <g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5">
    <path d="M-90-70q-30 30 0 60M90-70q30 30 0 60"/>
  </g>
</g>
<g transform="translate(450 250)">
  <circle r="56" fill="#8f9aa6" class="o"/>
  <circle r="24" fill="#c8d0d8" class="o"/>
  <path d="M-56 0h-50v-30h-20v60h20v-30M56 0h50v-30h20v60h-20v-30" fill="none" stroke="#8f9aa6" stroke-width="10"/>
  <g class="a" marker-end="url(#ar)" stroke="{TONES['blue'][0]}" stroke-width="5"><path d="M-96 40h190"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M270 340q30-14 60 0M270 366q30-14 60 0"/>
</g>''', ground=False)

add('analytic', '一つの塊を要素に分けて調べる', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-80-70h160v140h-160z" class="tealp o"/>
</g>
<g transform="translate(450 250)">
  <g class="o">
    <rect x="-80" y="-70" width="70" height="60" class="coralp"/>
    <rect x="10" y="-70" width="70" height="60" class="goldp"/>
    <rect x="-80" y="10" width="70" height="60" class="violetp"/>
    <rect x="10" y="10" width="70" height="60" class="greenp"/>
  </g>
</g>
<g transform="translate(520 140)">
  <circle r="40" fill="none" stroke="#8f9aa6" stroke-width="9"/>
  <path d="M28 28l30 30" stroke="{INK}" stroke-width="11" stroke-linecap="round" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('antisocial', '集まりの誘いを断って一人で背を向ける', f'''
{table(380)}
{head(120, 260, 22, 'teal', 'short')}
{head(190, 300, 22, 'coral', 'bun')}
{head(120, 340, 22, 'gold', 'cap')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="12 10"><ellipse cx="155" cy="300" rx="110" ry="80"/></g>
{person(470, 380, 1.1, 1, 'blue', 'blue', 'stand', 'short', 'neutral')}
<g class="a" marker-end="url(#ar)" stroke="{MUTED}" stroke-width="5"><path d="M290 250h100"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M340 220l40 40M380 220l-40 40"/>
</g>''', ground=False)

add('apathetic', '何が起きても関心を示さず無反応でいる', f'''
{table(380)}
{sit(300, 380, 1.2, 1, 'blue', 'blue', 'short', 'neutral', 'down')}
{chair(300, 380, 1.1, 'gold', 1)}
<g transform="translate(300 250)">
  <path d="M-26-6h18M8-6h18" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <path d="M-12 18h24" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
</g>
<g transform="translate(480 160)">
  <path d="M-60-40h120q12 0 12 12v40q0 12-12 12h-84l-20 16v-16q-12 0-12-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <path d="M-30-16l60 40M30-16l-60 40" stroke="{TONES['coral'][0]}" stroke-width="6" fill="none"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M390 200h-50"/></g>
<g transform="translate(120 200)">
  <path d="M-40-30h80q10 0 10 10v30q0 10-10 10h-52l-18 14v-14q-10 0-10-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M0-16l7 14 15 2-11 12 3 16-14-8-14 8 3-16-11-12 15-2z" class="gold"/>
</g>''', ground=False)

add('apologetic', '頭を下げて申し訳なさそうにあやまる', f'''
{table(380)}
{person(430, 380, 1.05, -1, 'coral', 'blue', 'stand', 'bun', 'neutral')}
<g transform="translate(200 380)">
  <path d="M-14-8l-10 8M14-8l10 8" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-28-76q28-16 56 0l-8 68h-40z" class="teal o"/>
  <g transform="translate(28 -80) rotate(42)">
    <circle cy="-30" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <path d="{HAIRS['short']}" transform="translate(0 78) scale(1.06)" fill="{HAIR}"/>
    <path d="M-14-30q8-8 16 0M-2-30q8-8 16 0" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
    <path d="M-8-14q8-8 16 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
  </g>
  <path d="M-24-70l-12 46M24-72l16 44" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
</g>
<g transform="translate(300 160)">
  <path d="M-56-36h112q12 0 12 12v36q0 12-12 12h-72l-22 16v-16q-18 0-18-12v-36q0-12 12-12z" fill="#fffefd" class="o"/>
  {word(0, -4, 3, 26, MUTED)}
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M120 250q-14 10-14 26"/>
</g>''', ground=False)

add('appreciative', 'もらった贈り物のよさが分かって喜ぶ', f'''
<path d="M0 0h600v400H0z" fill="#fff6e0"/>
{table(380)}
{person(300, 380, 1.15, 1, 'coral', 'blue', 'hold', 'bun', 'smile')}
<g transform="translate(300 260)">
  <path d="M-56-40h112v70h-112z" class="teal o"/>
  <path d="M-56-40h112v-16h-112z" class="teald o"/>
  <path d="M-8-56h16v70h-16z" class="coral"/>
  <path d="M-56-24h112" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{300+150*math.cos(3.5+i*0.45):.0f} {200+150*math.sin(3.5+i*0.45):.0f}l{20*math.cos(3.5+i*0.45):.0f} {20*math.sin(3.5+i*0.45):.0f}"/>' for i in range(8)) + f'''
</g>
<g fill="{TONES['coral'][0]}">
  <path d="M300 120q-14-20 0-28 14-6 18 10 4-16 18-10 14 8 0 28l-18 20z"/>
</g>''', ground=False)

add('apprehensive', 'これから始まる試験を前に不安そうに待つ', f'''
{table(380)}
{sit(220, 380, 1.1, 1, 'teal', 'blue', 'bob', 'sad', 'lap')}
{chair(220, 380, 1.05, 'gold', 1)}
<g transform="translate(250 290)">{doc(0, 0, 110, 40, 1)}</g>
<g transform="translate(430 160)">
  <circle r="56" fill="#fffdf6" class="o"/>
  <path d="M0 0v-38M0 0l26 16" stroke="{INK}" stroke-width="6" stroke-linecap="round" fill="none"/>
  <circle r="8" fill="{INK}"/>
</g>
<g fill="{TONES['blue'][0]}"><path d="M166 246q9 10 9 17t-9 8-9-8 9-17z"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M180 210q-14 10-14 26M270 206q14 10 14 26"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M320 200h50"/></g>''', ground=False)

add('approximate', 'ぴったりの数ではなく、およその数で示す', f'''
{split()}
{table(380)}
<g transform="translate(150 240)">
  <path d="M-90-50h180v100h-180z" class="paper"/>
  {word(0, 0, 4, 34, INK)}
</g>
{tick(150, 130, 0.5)}
<g transform="translate(450 240)">
  <path d="M-90-50h180v100h-180z" class="paper"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
    <path d="M-64-24q16-16 32 0t32 0"/>
  </g>
  {word(6, 16, 3, 30, MUTED)}
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M300 340h240"/></g>''', ground=False)

add('apt', '選んだ道具がその場にぴたりと合っている', f'''
{split()}
{table(380)}
<g transform="translate(150 260)">
  <path d="M-70-40h140v80h-140z" fill="#c8d0d8" class="o"/>
  <path d="M-30-40v-50h60v50z" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="8 6"/>
  <path d="M-30-90h60v-40h-60z" class="coralp o" transform="rotate(24 0 -110)"/>
</g>
{cross(150, 130, 0.6)}
<g transform="translate(450 260)">
  <path d="M-70-40h140v80h-140z" fill="#c8d0d8" class="o"/>
  <path d="M-30-40v-50h60v50z" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="8 6"/>
  <path d="M-30-90h60v-50h-60z" class="tealp o"/>
  <path d="M-30-40h60v-50h-60z" class="tealp o"/>
</g>
{tick(450, 130, 0.6)}''', ground=False)

add('archaic', 'いまは使われない古い書き方の巻物', f'''
{split()}
{table(380)}
<g transform="translate(150 240)">
  <path d="M-100-90h200v180h-200z" fill="#e8dcc0" class="o"/>
  <path d="M-100-90q-26 0-26 18t26 18M100-90q26 0 26 18t-26 18" fill="#e0d4b0" class="o"/>
  <g fill="none" stroke="#a89878" stroke-width="4" stroke-linecap="round">
''' + ''.join(f'<path d="M-70 {-44+i*30}q20-14 40 0t40 0 40 0"/>' for i in range(4)) + f'''
  </g>
</g>
{cross(150, 120, 0.6)}
<g transform="translate(450 240)">
  <path d="M-100-90h200v180h-200z" class="paper"/>
  <g fill="{INK}">
''' + ''.join(f'<rect x="-72" y="{-52+i*30}" width="{144-(i%3)*36}" height="12" rx="6"/>' for i in range(4)) + f'''
  </g>
</g>
{tick(450, 120, 0.6)}''', ground=False)

add('arduous', '急な坂道を汗をかきながら登り続ける', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
<path d="M0 400L440 60h160v340z" fill="#9aa5b0" class="o"/>
{person(280, 300, 1.05, 1, 'gold', 'blue', 'walk', 'cap', 'sad', 'walk')}
<g transform="translate(250 210)">
  <path d="M-34-46h68v78q0 14-34 14t-34-14z" class="teal o"/>
</g>
<g fill="{TONES['blue'][0]}">
  <path d="M210 200q9 10 9 17t-9 8-9-8 9-17z"/><path d="M196 240q8 9 8 15t-8 7-8-7 8-15z"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M340 260L500 140"/></g>
{sun(80, 70, 30)}''', ground=False)

add('arrogant', 'あごを上げ、腕を組んで人を見下す', f'''
{table(380)}
{person(300, 380, 1.3, 1, 'violet', 'blue', 'hold', 'short', 'neutral')}
<g transform="translate(300 254)">
  <path d="M-62 0q62-26 124 0" stroke="{SKIN}" stroke-width="20" stroke-linecap="round" fill="none"/>
  <path d="M-52 20q56-22 108 0" stroke="{SKIN}" stroke-width="18" stroke-linecap="round" fill="none"/>
  <path d="M-62 0q62-26 124 0M-52 20q56-22 108 0" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g transform="translate(300 226)">
  <path d="M-26-16q14-8 26 0M2-16q14-8 26 0" fill="none" stroke="{HAIR}" stroke-width="5" stroke-linecap="round" transform="translate(-2 0)"/>
  <path d="M-14 12h28" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
</g>
{head(110, 340, 22, 'coral', 'bob')}
<g class="a" marker-end="url(#ar)" stroke="{MUTED}"><path d="M240 260l-90 50"/></g>''', ground=False)

add('assertive', '会議ではっきり自分の意見を主張する', f'''
{table(380)}
{sit(160, 380, 0.95, 1, 'blue', 'blue', 'short', 'neutral', 'lap')}
{sit(440, 380, 0.95, -1, 'gold', 'blue', 'bun', 'neutral', 'lap')}
{person(300, 380, 1.1, 1, 'coral', 'blue', 'up', 'bob', 'neutral')}
<g transform="translate(300 150)">
  <path d="M-90-40h180q12 0 12 12v40q0 12-12 12h-120l-24 16v-16q-12 0-12-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  {word(0, -4, 5, 28, INK)}
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M220 220l-24-18M380 216l24-18"/>
</g>''', ground=False)

add('atrocious', '見るにたえないほどひどい仕上がり', f'''
{split()}
{table(380)}
<g transform="translate(150 240)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <path d="M-60 60L-10-30l40 44 40-66 40 112z" class="greenp o"/>
</g>
{tick(150, 120, 0.6)}
<g transform="translate(450 240)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="8" stroke-linecap="round">
    <path d="M-60-40q40 60 20-10t60 90M-40 50q60-40 100 20"/>
  </g>
  <g fill="{TONES['coral'][0]}"><circle cx="30" cy="-50" r="16"/></g>
</g>
{cross(450, 120, 0.7)}''', ground=False)

add('attentive', '客の様子をよく見て先に気づいて動く', f'''
{table(380)}
{sit(180, 380, 0.95, 1, 'coral', 'blue', 'bun', 'smile', 'lap')}
{chair(180, 380, 0.9, 'gold', 1)}
<g transform="translate(220 300)">
  <path d="M-50-16h100v20h-100z" fill="#c9a464" class="o"/>
  <path d="M-30-40h60v24h-60z" fill="#e8f0f6" class="o"/>
</g>
{person(430, 380, 1.05, -1, 'teal', 'teal', 'reach', 'short', 'smile')}
<g transform="translate(430 260)">
  <ellipse cx="-14" rx="13" ry="11" fill="#fffefd" class="o"/><circle cx="-18" r="6" fill="{INK}"/>
  <ellipse cx="14" rx="13" ry="11" fill="#fffefd" class="o"/><circle cx="10" r="6" fill="{INK}"/>
</g>
<g transform="translate(500 200)">
  <path d="M-30-40h60v70q0 12-30 12t-30-12z" fill="#e8f0f6" class="o"/>
  <path d="M-24-16h48v46q0 10-24 10t-24-10z" fill="{TONES['blue'][1]}"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M380 260l-90 20"/></g>''', ground=False)

add('audacious', '高い崖から思い切って飛び込む', f'''
<path d="M0 0h600v250H0z" fill="#dceaf4"/>
<path d="M0 250h600v150H0z" fill="#7aa8c4"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M0 0h150v250H0z" fill="#a8845c" class="o"/>
<g transform="translate(230 180) rotate(30)">
  <path d="M-12-8l-30 30M12-8l32 26" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-27-78q27-14 54 0l-8 72h-38z" class="coral o"/>
  <path d="M-22-70l-34-24M22-70l34-24" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cy="-108" r="25" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['cap']}" transform="scale(1.04)" fill="{TONES['blue'][0]}"/>
  <circle cx="-8" cy="-104" r="2.4" fill="{INK}"/><circle cx="8" cy="-104" r="2.4" fill="{INK}"/>
  <path d="M-8-92q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M180 130q120 40 200 140"/></g>
<g fill="none" stroke="#a8c8dd" stroke-width="4"><path d="M380 300h150M420 350h140"/></g>''', ground=False)

add('audible', 'ごく小さな音でもはっきり聞き取れる', f'''
{table(380)}
<g transform="translate(180 260)">
  <path d="M-40-40h80v70q0 12-40 12t-40-12z" fill="#c8d0d8" class="o"/>
  <circle cy="-10" r="16" fill="#8f9aa6" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M250 220q20 26 0 52M280 200q34 46 0 92"/>
</g>
{person(450, 380, 1.05, -1, 'teal', 'blue', 'up', 'bob', 'smile')}
<g transform="translate(410 250)">
  <ellipse rx="16" ry="22" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-6 6q10-14 0-22" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
</g>
{tick(520, 160, 0.6)}''', ground=False)

add('autonomous', '人が乗らなくても自分で判断して走る車', f'''
<path d="M0 250h600v150H0z" fill="#6f7b88"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="#fffefd" stroke-width="5" stroke-dasharray="30 26"><path d="M0 330h600"/></g>
<g transform="translate(320 320)">
  <path d="M-130 30h260v-46q0-16-16-16h-70l-40-38H-90l-24 38h-16q-16 0-16 16z" class="teal o"/>
  <path d="M-84-32h100l30 38H-108z" fill="#dceaf4" class="o"/>
  <circle cx="-70" cy="30" r="24" fill="{INK}"/><circle cx="70" cy="30" r="24" fill="{INK}"/>
  <circle cx="0" cy="-40" r="14" fill="#5a6270" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8">
  <path d="M320 250q-60-60-150-50M320 250q60-60 150-50"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M236 296h50v40h-50z"/></g>
{cross(261, 316, 0.5)}''', ground=False)

add('avoidable', '事前に取り除けばよかった、避けられた事故', f'''
{split()}
{table(380)}
<g transform="translate(150 340)">
  <path d="M-40-16h80v16h-80z" fill="#c9a464" class="o"/>
</g>
{person(150, 340, 0.85, 1, 'coral', 'blue', 'up', 'bob', 'sad')}
{cross(150, 130, 0.6)}
<g transform="translate(450 300)">
  <path d="M-40-16h80v16h-80z" fill="#c9a464" class="o" transform="rotate(20)"/>
</g>
{person(500, 380, 0.85, 1, 'coral', 'blue', 'walk', 'bob', 'smile', 'walk')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M380 240q60-60 130 0"/></g>
{tick(450, 130, 0.6)}''', ground=False)

add('baggy', 'サイズの大きい服が体からだぶついている', f'''
{table(380)}
<g transform="translate(300 380)">
  <path d="M-16-10l-9 10M16-10l9 10" fill="none" stroke="{TONES['blue'][2]}" stroke-width="13" stroke-linecap="round"/>
  <path d="M-80-90q80-34 160 0l-20 90H-60z" class="tealp o"/>
  <path d="M-80-90l-54 56 26 22 36-38M80-90l54 56-26 22-36-38" class="tealp o"/>
  <path d="M-60-40q60 20 120 0M-70-10q70 24 140 0" fill="none" stroke="{TONES['teal'][0]}" stroke-width="3"/>
  <circle cy="-124" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 -14) scale(1.08)" fill="{HAIR}"/>
  <circle cx="-9" cy="-120" r="2.4" fill="{INK}"/><circle cx="9" cy="-120" r="2.4" fill="{INK}"/>
  <path d="M-9-108q9 8 18 0" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 250l-100-20"/></g>
<g class="a" marker-end="url(#ar)"><path d="M130 250l100-20"/></g>''', arrow=True, ground=False)

add('bankrupt', '店が閉まり、金庫が空になって破産する', f'''
{table(380)}
<g transform="translate(200 380)">
  <path d="M-90 0v-140h180V0z" fill="#c8d0d8" class="o"/>
  <path d="M-104-140h208v-24h-208z" fill="#8f9aa6" class="o"/>
  <path d="M-60-110h120v70h-120z" fill="#6f7b88" class="o"/>
  <g fill="none" stroke="#5a6270" stroke-width="4">
''' + ''.join(f'<path d="M-60 {-100+i*16}h120"/>' for i in range(5)) + f'''
  </g>
  <path d="M-60-30h120v20h-120z" class="coral o" transform="rotate(-8 0 -20)"/>
</g>
<g transform="translate(450 300)">
  <path d="M-70-70h140v140h-140z" fill="#8f9aa6" class="o"/>
  <path d="M-56-56h112v112h-112z" fill="#c8d0d8" class="o"/>
  <circle cx="0" cy="0" r="20" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M-56-56h112v112h-112z" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"><path d="M400 220h100"/></g>
{cross(450, 160, 0.7)}''', ground=False)

add('bashful', '顔を赤らめてもじもじと下を向く', f'''
{table(380)}
{person(300, 380, 1.2, 1, 'coral', 'blue', 'hold', 'bob', 'smile')}
<g transform="translate(300 240)">
  <g class="coralp"><circle cx="-30" cy="10" r="14"/><circle cx="30" cy="10" r="14"/></g>
  <path d="M-22-6q10-8 18 0M4-6q10-8 18 0" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>
  <path d="M-8 22q8 6 16 0" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(300 290)">
  <path d="M-40 0q40-24 80 0" stroke="{SKIN}" stroke-width="18" stroke-linecap="round" fill="none"/>
  <path d="M-40 0q40-24 80 0" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
</g>
{person(470, 380, 0.95, -1, 'teal', 'blue', 'stand', 'short', 'smile')}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M400 250h-60"/></g>''', ground=False)

add('bang', 'ドアを勢いよく閉めてバンと大きな音を出す', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<g transform="translate(380 200)">
  <path d="M-120-180h240v360h-240z" fill="{BRN}" class="o"/>
  <path d="M-96-156h192v312h-192z" fill="#a0764a" class="o"/>
  <circle cx="-70" cy="10" r="12" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round">
  <path d="M240 100l-50-40M230 200h-60M240 300l-50 40"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M300 60l-20-40M460 60l20-40M300 340l-20 40M460 340l20 40"/>
</g>
<g class="a" marker-end="url(#ar)" stroke-width="6"><path d="M120 200h100"/></g>
{person(60, 380, 0.8, 1, 'coral', 'blue', 'reach', 'short', 'neutral')}''', ground=False)

# --- 副詞 -------------------------------------------------------------------
add('collectively', 'ばらばらの一本ずつでは折れるが、束にすると折れない', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-70-6h60v12h-60zM10-6h60v12H10z" fill="#c9a464" class="o"/>
  <path d="M-10-6l20 12" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
</g>
{cross(150, 130, 0.6)}
<g transform="translate(450 250)">
  <g fill="#c9a464" class="o">
''' + ''.join(f'<path d="M-110 {-30+i*14}h220v12h-220z"/>' for i in range(5)) + f'''
  </g>
  <path d="M-30-40h60v70h-60z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
{tick(450, 130, 0.6)}''', ground=False)

add('harshly', '厳しい口調で強くとがめる', f'''
{table(380)}
{person(180, 380, 1.15, 1, 'violet', 'blue', 'point', 'short', 'sad')}
{person(450, 380, 1.0, -1, 'coral', 'blue', 'stand', 'bob', 'sad')}
<g transform="translate(310 170)">
  <path d="M-80-46l16 16-16 16 16 16-16 16h160l-16-16 16-16-16-16 16-16z" fill="#fffefd" class="o"/>
  <g fill="{TONES['coral'][0]}"><rect x="-40" y="-9" width="80" height="18" rx="9"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M120 210l-30-26M240 180l8-30"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M410 250q-14 10-14 26"/>
</g>''', ground=False)

add('markedly', '前の年より目に見えて大きく増えている', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(300 250)">
  <path d="M-250 100h500v6h-500z" fill="{INK}"/>
  <path d="M-250-200v300h6v-300z" fill="{INK}"/>
  <g class="teal o">
    <rect x="-200" y="40" width="70" height="60"/>
    <rect x="-100" y="20" width="70" height="80"/>
    <rect x="0" y="10" width="70" height="90"/>
    <rect x="100" y="-160" width="70" height="260"/>
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M-244 10h420"/></g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M500 260V100"/></g>''', ground=False)

add('noticeably', '同じ形の中で一つだけ色が違い、すぐ目につく', f'''
{table(380)}
<g class="o">
''' + ''.join(f'<circle cx="{90+ (i%6)*80}" cy="{220+(i//6)*90}" r="34" class="tealp"/>' for i in range(11)) + f'''
  <circle cx="330" cy="310" r="34" class="coral"/>
</g>
{person(540, 380, 0.8, -1, 'blue', 'blue', 'point', 'bun', 'smile')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M470 340l-100-20"/></g>''', ground=False)

# --- 連語・慣用表現 -----------------------------------------------------------
add('a-great-deal-of', '数えられない水がたっぷりある', f'''
{table(380)}
<g transform="translate(300 260)">
  <path d="M-160-100h320v170q0 24-160 24t-160-24z" fill="#e8f0f6" class="o"/>
  <path d="M-152-40h304v106q0 20-152 20t-152-20z" fill="{TONES['blue'][0]}"/>
  <path d="M-152-40h304" stroke="{TONES['blue'][2]}" stroke-width="4" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['blue'][0]}" stroke-width="5"><path d="M520 340v-120"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M100 220h60"/></g>''', ground=False)

add('a-number-of', '数えられる品がいくつも並んでいる', f'''
{table(380)}
<g class="o">
''' + ''.join(f'<rect x="{70+ (i%7)*70}" y="{220+(i//7)*80}" width="50" height="60" class="goldp"/>' for i in range(13)) + f'''
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3">
''' + ''.join(f'<path d="M{95+ (i%7)*70} {210+(i//7)*80}v-14"/>' for i in range(13)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M70 160h420"/></g>''', arrow=True, ground=False)

add('a-range-of', '小さいものから大きいものまで幅がある', f'''
{table(380)}
<g class="o">
''' + ''.join(f'<circle cx="{80+i*80}" cy="300" r="{12+i*10}" class="tealp"/>' for i in range(6)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M80 180h480"/></g>
<g class="a" marker-end="url(#ar)"><path d="M560 180H80"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M80 130v90M560 130v90"/></g>''', arrow=True, ground=False)

add('a-series-of', '同じ形の出来事が順につながって続く', f'''
{table(380)}
<g>
''' + ''.join(f'<g transform="translate({90+i*100} 250)"><path d="M-36-36h72v72h-72z" class="violetp o"/><circle r="12" class="violet"/></g>' for i in range(5)) + f'''
</g>
<g class="a" marker-end="url(#ar)">
''' + ''.join(f'<path d="M{132+i*100} 250h30"/>' for i in range(4)) + f'''
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M54 330h480"/></g>''', arrow=True, ground=False)

add('after-all', 'あれこれあった末に、結局もとの案に落ち着く', f'''
{table(380)}
<g transform="translate(150 250)">
  <path d="M-70-50h140v100h-140z" class="tealp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10">
  <path d="M230 250q40-140 150-100t60 130"/>
</g>
<g transform="translate(460 250)">
  <path d="M-70-50h140v100h-140z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M440 340H160"/></g>
{tick(300 , 130, 0.6)}''', ground=False)

add('along-with', '本体の品に付属の品も一緒についてくる', f'''
{table(380)}
<g transform="translate(220 260)">
  <path d="M-90-70h180v140h-180z" class="teal o"/>
  <path d="M-90-70l20-24h180l-20 24z" fill="{TONES['teal'][1]}" class="o"/>
  <path d="M90-70l20-24v140l-20 24z" fill="{TONES['teal'][2]}" class="o"/>
</g>
<g transform="translate(430 300)">
  <path d="M-50-40h100v80h-100z" class="goldp o"/>
  <path d="M-50-40l12-16h100l-12 16z" fill="{TONES['gold'][1]}" class="o"/>
</g>
<g transform="translate(510 250)">
  <path d="M-30-24h60v48h-60z" class="coralp o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M330 200h50M355 175v50"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M360 340h190v-140"/></g>''', ground=False)

add('as-a-result-of', '雨が降った、その結果として道が濡れた', f'''
{table(380)}
{cloud(150, 110, 1.2, 'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{100+i*34} {170+(i%3)*30}l-12 34"/>' for i in range(5)) + f'''
</g>
<g class="a" marker-end="url(#ar)" stroke-width="6"><path d="M290 220h80"/></g>
<g transform="translate(470 300)">
  <path d="M-110 40h220v20h-220z" fill="#6f7b88" class="o"/>
  <g fill="{TONES['blue'][1]}" class="o">
    <ellipse cx="-50" cy="34" rx="40" ry="12"/><ellipse cx="40" cy="40" rx="50" ry="14"/>
  </g>
</g>
<g fill="{TONES['blue'][0]}"><path d="M430 260q9 10 9 17t-9 8-9-8 9-17z"/></g>''', ground=False)

add('at-most', '上限の線までで、それ以上は行かない', f'''
{table(380)}
<g transform="translate(300 260)">
  <path d="M-200-30h400v60h-400z" fill="#e0d6c0" class="o"/>
  <path d="M-200-30h300v60h-300z" class="teal o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">
''' + ''.join(f'<path d="M{-200+i*40} -30v{16 if i%2 else 30}"/>' for i in range(11)) + f'''
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M400 160v160"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M470 200h-60"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M410 340h130"/></g>''', ground=False)

add('at-once', 'ベルが鳴った瞬間に飛び出す', f'''
{table(380)}
<g transform="translate(140 180)">
  <circle r="56" fill="#fffdf6" class="o"/>
  <path d="M-40-40l-22-22M40-40l22-22" stroke="{INK}" stroke-width="9" stroke-linecap="round" fill="none"/>
  <circle cx="-40" cy="-48" r="15" class="coral o"/><circle cx="40" cy="-48" r="15" class="coral o"/>
  <path d="M0 0v-34M0 0l24 16" stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M210 150q26 30 0 60M240 130q40 46 0 100"/>
</g>
{person(420, 380, 1.15, 1, 'coral', 'blue', 'walk', 'cap', 'surprised', 'walk')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M310 240h50M300 290h40"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M490 250h70"/></g>''', ground=False)

add('at-present', '過去と未来の間の、いまこの時点', f'''
{table(380)}
<g transform="translate(300 240)">
  <path d="M-250-10h500v20h-500z" fill="#e0d6c0" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">
''' + ''.join(f'<path d="M{-250+i*50} -10v20"/>' for i in range(11)) + f'''
  </g>
  <circle cx="0" r="26" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}" stroke-width="4"><path d="M270 160H80"/></g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}" stroke-width="4"><path d="M330 160h190"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M300 340v-60"/></g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
