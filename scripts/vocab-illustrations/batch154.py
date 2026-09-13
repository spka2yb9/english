# -*- coding: utf-8 -*-
"""第154回。b- の名詞と慣用表現。"""
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

GLD, GLDP, GLDD = TONES['gold']
CRL, CRLP, CRLD = TONES['coral']
GRN, GRNP, GRND = TONES['green']
BLU, BLUP, BLUD = TONES['blue']
TEA, TEAP, TEAD = TONES['teal']
VIO, VIOP, VIOD = TONES['violet']

def spark(x, y, s=1, cls='gold'):
    return (f'<path d="M{x} {y-16*s}l{5*s} {11*s} {11*s} {5*s}-{11*s} {5*s}-{5*s} {11*s}'
            f'-{5*s}-{11*s}-{11*s}-{5*s} {11*s}-{5*s}z" class="{cls} o"/>')

def ring(x, y, r=64, dash=False, cls='coral'):
    d = ' stroke-dasharray="11 10"' if dash else ''
    c = MUTED if dash else TONES[cls][0]
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{c}" stroke-width="4"{d}/>'

def torso(x, y, s=1):
    """内臓を示すための、上半身の輪郭。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0-190a44 44 0 1 1 0 88 44 44 0 1 1 0-88z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>'
            f'<path d="M-90-96q90-30 180 0 20 130 0 226h-180q-20-96 0-226z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/></g>')

def bulb(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><circle r="28" class="goldp o"/>'
            f'<path d="M-11 28h22v10h-22z" class="goldd o"/>'
            f'<g class="golds"><path d="M0-42v-16"/><path d="M32-30l12-12"/><path d="M-32-30l-12-12"/></g></g>')

def clock(x, y, s=1, h=5, m=0):
    ah = math.radians(h*30 + m*0.5 - 90); am = math.radians(m*6 - 90)
    return (f'<g transform="translate({x} {y}) scale({s})"><circle r="54" fill="#fffefd" class="o"/>'
            f'<path d="M0 0l{42*math.cos(am):.0f} {42*math.sin(am):.0f}" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
            f'<path d="M0 0l{28*math.cos(ah):.0f} {28*math.sin(ah):.0f}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
            f'<circle r="4" class="ink"/></g>')

# --- からだ ------------------------------------------------------------------

add('backbone', '背中の中心を通る、節の連なった骨', f'''
{torso(300, 300, 1.0)}
<g transform="translate(300 210)">
  {''.join(f'<rect x="-22" y="{-90+i*26}" width="44" height="20" rx="6" class="teal o"/>' for i in range(8))}
  <path d="M0-96v210" fill="none" stroke="{TEAD}" stroke-width="4"/></g>
{ring(300, 205, 130)}''')

add('bladder', '下腹にある、尿をためる袋', f'''
{torso(300, 300, 1.0)}
<g transform="translate(300 270)"><path d="M0-46q56 0 56 46t-56 46-56-46 56-46z" class="gold o"/>
  <path d="M-18-46q0-40 18-56 18 16 18 56" fill="none" stroke="{GLDD}" stroke-width="6"/></g>
{ring(300, 272, 92)}''')

add('bowel', '腹のなかで折りたたまれた、長い腸', f'''
{torso(300, 300, 1.0)}
<g transform="translate(300 250)" fill="none" stroke="{CRL}" stroke-width="20" stroke-linecap="round" stroke-linejoin="round">
  <path d="M-60-40h120v34h-120v34h120v34h-120"/></g>
{ring(300, 262, 108)}''')

add('bib', '赤ちゃんの首にかける、胸あて', f'''
{table(360)}
<g transform="translate(300 300)">
  <circle cx="0" cy="-190" r="54" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-30-224q30-24 60 0" fill="none" stroke="{HAIR}" stroke-width="8" stroke-linecap="round"/>
  <circle cx="-18" cy="-192" r="5" class="ink"/><circle cx="18" cy="-192" r="5" class="ink"/>
  <path d="M-14-170q14 14 28 0" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-70-130q70-30 140 0v40h-140z" class="teal o"/>
  <path d="M-60-124q-24 100 60 116 84-16 60-116-60 26-120 0z" class="coralp o"/>
  <path d="M-46-128q46 20 92 0" fill="none" stroke="{CRL}" stroke-width="5"/>
  <circle cx="0" cy="-40" r="18" class="coral o"/></g>''')

# --- 気持ち ------------------------------------------------------------------

add('bereavement', '身近な人を亡くし、写真の前でひとり過ごす', f'''
{table(320)}
<g transform="translate(400 250) rotate(-4)"><rect x="-64" y="-80" width="128" height="160" rx="6" fill="#f3ead6" class="o"/>
  <rect x="-50" y="-66" width="100" height="106" fill="#e6e2d8" class="o"/>
  {head(400, 216, 30, 'violet', 'bun')}
  <path d="M-50 56h100" fill="none" stroke="{MUTED}" stroke-width="4"/></g>
<g transform="translate(500 288)"><path d="M0 20v-40" fill="none" stroke="{GRND}" stroke-width="5"/>
  {''.join(f'<ellipse cx="0" cy="-38" rx="8" ry="16" class="coralp o" transform="rotate({d} 0 -20)"/>' for d in range(0, 360, 72))}</g>
{sit(180, 320, 1.2, 1, 'blue', 'blue', 'short', 'sad', 'down')}
{chair(194, 320, 1.1, 'gold', -1)}
{drop(154, 210, 0.9)}''')

add('betrayal', '味方の顔をしながら、うしろで相手側に通じている', f'''
{person(150, 306, 1.15, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{person(300, 306, 1.15, -1, 'violet', 'blue', 'give', 'bun', 'smile')}
<g transform="translate(226 220)">{hand(-16, 0, 1)}{hand(16, 0, -1)}</g>
{person(510, 306, 1.1, -1, 'coral', 'blue', 'reach', 'short', 'neutral')}
<path d="M330 330q80 30 130-14" fill="none" stroke="{CRL}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"/>
<g transform="translate(370 350)"><rect x="-26" y="-16" width="52" height="32" rx="4" class="paper"/></g>''', arrow=True)

add('bewilderment', 'あちこちを指す矢印に囲まれて、頭が真っ白になる', f'''
{person(300, 320, 1.2, 1, 'teal', 'blue', 'hold', 'short', 'surprised')}
{''.join(f'<g transform="rotate({a} 300 200)"><path d="M300 90h-1" fill="none"/><path d="M300 110v-60" class="a" stroke-width="5" marker-end="url(#ar)"/></g>' for a in range(0, 360, 45))}
<g transform="translate(430 90)"><path d="M-14-30a26 26 0 1 1 22 42q-8 8-8 18" fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="46" r="6" fill="{MUTED}"/></g>''', arrow=True)

add('bitterness', '苦い一口に、思わず顔がゆがむ', f'''
{table(330)}
<g transform="translate(180 300)"><path d="M-40 0v-90h80V0z" fill="#fffefd" class="o"/>
  <path d="M-34-76h68v72h-68z" fill="#4a3a2c"/>
  <path d="M40-70q26 0 26 20t-26 20" fill="none" class="o"/></g>
<g transform="translate(420 220)"><circle r="70" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="{HAIRS['short']}" transform="translate(0 328) scale(2.9)" fill="{HAIR}"/>
  <path d="M-40-20l26 12M40-20l-26 12" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <path d="M-22 30q22-22 44 0" fill="none" stroke="{INK}" stroke-width="5"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M320 150q16-20 0-40M520 160q-16-20 0-40"/></g>''')

add('boldness', 'みんながためらう割れ目を、ひと息に跳び越える', f'''
<path d="M0 306h200v94H0zM400 306h200v94H400z" class="ground"/>
<path d="M200 306l24 94h-24zM400 306l-24 94h24z" fill="#5b6b78"/>
<g transform="translate(300 200) rotate(-14)">{person(0, 0, 1.15, 1, 'coral', 'blue', 'up', 'cap', 'smile', 'walk')}</g>
<path d="M160 220q140-120 260 30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"/>
{person(90, 306, 1.0, 1, 'teal', 'blue', 'hold', 'bob', 'sad')}
{person(520, 306, 1.0, -1, 'violet', 'blue', 'hold', 'short', 'surprised')}''')

add('brutality', '大きなこぶしが、力まかせに押しつぶす', f'''
<g transform="translate(300 130) scale(2.2 1.8) rotate(180)">{hand(0, 0, 1)}</g>
<g transform="translate(300 320)"><path d="M-90 0q-16-40 8-50 30-12 60 0t50 8q10 30-10 42z" class="tealp o"/>
  <path d="M-40-46l-16-30M20-52l14-32M60-40l30-24" fill="none" stroke="{TEA}" stroke-width="5" stroke-linecap="round"/></g>
<g fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round">
  <path d="M140 250h-50M470 250h50M170 320h-60M450 320h60"/></g>''')

# --- 経済・社会 --------------------------------------------------------------

add('backlash', '押しこんだ分だけ、より強く押し返される', f'''
<path d="M60 150h180" class="a" stroke-width="8" marker-end="url(#ar)"/>
<g transform="translate(300 200)"><rect x="-30" y="-140" width="60" height="280" rx="8" class="teald o"/></g>
<path d="M540 280h-260" class="a" stroke="{CRL}" stroke-width="18" marker-end="url(#ar)"/>
{''.join(head(400 + (i%3)*70, 90 + (i//3)*0, 26, c, h) for i, (c, h) in enumerate([('coral','short'),('violet','bob'),('gold','bun')]))}
{''.join(f'<path d="M{376+i*70} 62q16-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}''', arrow=True)

add('bailout', 'しずみかけた船に、外から救いの手が入る', f'''
<path d="M0 260h600v140H0z" fill="{BLUP}"/>
<g transform="translate(240 280) rotate(16)"><path d="M-110 0h220l-36 56h-148z" class="coral o"/>
  <path d="M0 0v-90" fill="none" stroke="{GLDD}" stroke-width="7"/>
  <path d="M0-90l50 34-50 22z" fill="#fffefd" class="o"/></g>
<g transform="translate(450 160)"><circle r="56" fill="none" stroke="{CRL}" stroke-width="22"/>
  <circle r="56" fill="none" stroke="#fffefd" stroke-width="22" stroke-dasharray="30 30"/></g>
<path d="M450 230v50" class="a" stroke-width="5" marker-end="url(#ar)"/>
{coin(520, 90, 26)}{coin(560, 140, 22)}''', arrow=True)

add('bandwidth', '細い管と太い管では、いちどに通る量がちがう', f'''
{split()}
<g transform="translate(150 200)"><rect x="-120" y="-24" width="240" height="48" rx="24" class="tealp o"/>
  {''.join(f'<circle cx="{-80+i*54}" cy="0" r="12" class="teal o"/>' for i in range(4))}</g>
{ring(150, 200, 128, True)}
<g transform="translate(450 200)"><rect x="-120" y="-70" width="240" height="140" rx="70" class="tealp o"/>
  {''.join(f'<circle cx="{-84+ (i%4)*56}" cy="{-36+(i//4)*36}" r="14" class="teal o"/>' for i in range(12))}</g>
{ring(450, 200, 138)}''')

add('bankruptcy', '金庫は空、店は閉め、支払いができなくなる', f'''
<g transform="translate(180 250)"><rect x="-100" y="-100" width="200" height="200" rx="10" fill="#9aa6ae" class="o"/>
  <path d="M-80-80h150v160h-150z" fill="#dfe6ea" class="o" transform="rotate(-16 -80 0)"/>
  <circle cx="60" cy="0" r="22" fill="none" stroke="{INK}" stroke-width="7"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8">
  <circle cx="130" cy="240" r="18"/><circle cx="170" cy="290" r="15"/></g>
<g transform="translate(450 306)"><path d="M-100 0v-130h200V0z" fill="#fffefd" class="o"/>
  <path d="M-112-130h224l-26-36h-172z" class="corald o"/>
  <path d="M-60-40h120v40h-120z" fill="#c3cbd1" class="o"/>
  {''.join(f'<path d="M-100 {-116+i*22}h200" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(5))}</g>''')

add('buyout', '大きな会社が金を出して、小さな店を丸ごと買い取る', f'''
{tower(140, 306, 0.9, 'teal', 4)}
<g transform="translate(470 306)"><path d="M-80 0v-100h160V0z" fill="#fffefd" class="o"/>
  <path d="M-92-100h184l-22-32h-140z" class="coral o"/></g>
<path d="M240 200h140" class="a" stroke-width="5" marker-end="url(#ar)"/>
{''.join(coin(270 + i*40, 260, 22) for i in range(3))}
<path d="M470 130v-40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
<g transform="translate(470 60)"><rect x="-56" y="-24" width="112" height="44" rx="8" class="teal o"/></g>''', arrow=True)

add('bribery', '机の下で、そっと金を握らせる', f'''
{table(240)}
{person(150, 380, 1.15, 1, 'coral', 'blue', 'give', 'short', 'neutral')}
{person(450, 380, 1.15, -1, 'violet', 'blue', 'give', 'bun', 'neutral')}
<g transform="translate(300 320)"><path d="M-56-24h112v48h-112z" class="goldp o"/>
  {coin(0, 0, 16)}</g>
<path d="M234 316h30M366 316h-30" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"><path d="M300 268v-30"/></g>''')

add('borough', '市を区切った、行政の一区画', f'''
<g transform="translate(300 200)"><rect x="-260" y="-160" width="520" height="320" rx="10" fill="#f2f5f6" class="o"/>
  <path d="M-100-160v320M100-160v320M-260-40h520M-260 60h520" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M-100-160h200v120h-200z" class="tealp o"/>
  {''.join(f'<g transform="translate({x} {y})"><rect x="-18" y="-16" width="36" height="32" rx="4" fill="#fffefd" class="o"/></g>'
           for x, y in [(-190,-110),(-190,10),(-190,110),(0,-110),(0,10),(0,110),(180,-110),(180,10),(180,110)])}</g>
{ring(300, 140, 120)}''')

add('bulletin', '掲示板にはり出される、短い知らせ', f'''
<g transform="translate(300 200)"><rect x="-230" y="-150" width="460" height="300" rx="10" fill="#c19a5e" class="o"/>
  <rect x="-210" y="-130" width="420" height="260" rx="6" fill="#e8dcc4"/></g>
{''.join(f'<g transform="translate({190+ (i%3)*110} {150+(i//3)*110}) rotate({-6+i*4})">'
         f'<rect x="-46" y="-56" width="92" height="112" rx="4" class="paper"/>'
         f'<rect x="-32" y="-40" width="64" height="10" rx="5" class="coral"/>'
         f'{"".join(f2 for f2 in ["<rect x=@-32@ y=@" + str(-16+j*18) + "@ width=@64@ height=@8@ rx=@4@ fill=@" + MUTED + "@/>" for j in range(3)])}'.replace('@', chr(34))
         + f'<circle cx="0" cy="-52" r="6" class="coral o"/></g>' for i in range(6))}''')

add('briefing', '動き出す前に、要点を短くまとめて伝える', f'''
<g transform="translate(410 190)"><rect x="-150" y="-110" width="300" height="220" rx="10" class="teald o"/>
  <rect x="-134" y="-94" width="268" height="188" rx="4" fill="#f4f7f8"/>
  {''.join(f'<g><circle cx="-100" cy="{-60+i*46}" r="8" class="coral o"/>'
           f'<rect x="-80" y="{-68+i*46}" width="{180-(i%2)*60}" height="14" rx="7" fill="{MUTED}"/></g>' for i in range(4))}</g>
{person(130, 306, 1.2, 1, 'violet', 'blue', 'point', 'bun', 'neutral')}
{''.join(head(210 + i*70, 380, 24, c, h) for i, (c, h) in enumerate([('teal','cap'),('coral','short'),('green','cap'),('gold','short')]))}''')

# --- 学び・ことば ------------------------------------------------------------

add('bibliography', '本の終わりにつける、参考にした本の一覧', f'''
{doc(300, 200, 340, 300, 0)}
<path d="M150 110h300" fill="none" stroke="{INK}" stroke-width="4"/>
{word(200, 90, 3, 32, INK)}
{''.join(f'<g transform="translate(170 {150+i*46})">'
         f'<rect x="0" y="-14" width="20" height="28" rx="3" class="{c} o"/>'
         f'<rect x="34" y="-8" width="{230-(i%2)*60}" height="12" rx="6" fill="{MUTED}"/></g>'
         for i, c in enumerate(['teal','coral','gold','violet']))}''')

add('bracket', 'ことばの前後をはさんで、まとめて示す印', f'''
{word(300, 200, 6, 44, INK)}
<g fill="none" stroke="{CRL}" stroke-width="10" stroke-linecap="round">
  <path d="M180 150q-24 50 0 100"/><path d="M420 150q24 50 0 100"/></g>
{ring(300, 200, 150)}''')

add('brevity', '同じことを、うんと短い長さで言い切る', f'''
<g transform="translate(300 140)"><rect x="-240" y="-24" width="480" height="48" rx="10" class="tealp o"/></g>
<path d="M60 200h480" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>
<g transform="translate(160 280)"><rect x="-100" y="-24" width="200" height="48" rx="10" class="teal o"/></g>
<path d="M60 340h200" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>
{ring(160, 280, 120)}''', arrow=True)

add('byline', '見出しの下に入る、書いた人の名前', f'''
{doc(300, 200, 360, 300, 0)}
<path d="M140 130h320" fill="none" stroke="{INK}" stroke-width="4"/>
{word(300, 100, 4, 56, INK)}
{word(230, 156, 3, 26, CRL)}
{''.join(f'<rect x="{140+ (i%2)*186}" y="{200+(i//2)*36}" width="164" height="12" rx="6" fill="{MUTED}"/>' for i in range(6))}
{ring(230, 156, 66)}''')

add('brainstorm', 'めいめいが思いつきを出し合って、板にはり出す', f'''
<g transform="translate(340 180)"><rect x="-190" y="-130" width="380" height="260" rx="10" fill="#f4f7f8" class="o"/>
  {''.join(f'<rect x="{-150+ (i%3)*106}" y="{-96+(i//3)*90}" width="86" height="70" rx="6" class="{c}p o" transform="rotate({-6+i*4} {-107+(i%3)*106} {-61+(i//3)*90})"/>'
           for i, c in enumerate(['coral','gold','teal','violet','green','blue']))}</g>
{head(80, 300, 26, 'teal', 'short')}{head(150, 350, 26, 'coral', 'bob')}
{bulb(90, 220, 0.9)}{bulb(170, 270, 0.8)}
<path d="M120 240l110-40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('brush up on', 'ほこりを払って、忘れかけた技をやり直す', f'''
{table(330)}
<g transform="translate(200 300) rotate(-8)"><path d="M-70 0v-160h140V0z" class="teal o"/>
  <path d="M-70 0v-160h20v160z" class="teald o"/>
  <path d="M-40-130h80v14h-80z" fill="#fffefd" opacity="0.8"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3">
  <path d="M120 200q40-16 76 0M124 230q30-12 56 4"/></g>
{hand(300, 180, 1)}
{person(460, 306, 1.2, -1, 'coral', 'blue', 'reach', 'bob', 'smile')}
{''.join(spark(x, y, 0.8) for x, y in [(360,120),(520,140)])}''')

# --- 慣用表現 ----------------------------------------------------------------

add('be bound to', 'レールの上なので、行き着く先は決まっている', f'''
<path d="M40 300h520M40 340h520" fill="none" stroke="{GLDD}" stroke-width="8"/>
{''.join(f'<path d="M{70+i*54} 296v48" fill="none" stroke="{GLDD}" stroke-width="6"/>' for i in range(10))}
<g transform="translate(220 280)"><path d="M-70 0v-70q0-20 20-20h100V0z" class="teal o"/>
  {''.join(f'<rect x="{-50+i*44}" y="-56" width="32" height="30" rx="4" class="tealp o"/>' for i in range(3))}
  <circle cx="-40" cy="14" r="18" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle cx="30" cy="14" r="18" fill="none" stroke="{INK}" stroke-width="7"/></g>
<g transform="translate(510 250)"><circle r="46" class="coral o"/></g>
<path d="M330 200h120" class="a" stroke-width="5" marker-end="url(#ar)"/>''', arrow=True)

add('be liable to', 'ひびが入っているので、どうしてももれやすい', f'''
{table(340)}
<g transform="translate(280 300)"><path d="M-70 0v-140h140V0z" fill="#fffefd" class="o"/>
  <path d="M-64-120h128v116h-128z" class="bluep"/>
  <path d="M-70 0v-140h140V0z" fill="none" class="o"/>
  <path d="M-70-60l30 16-24 16 24 12" fill="none" stroke="{CRL}" stroke-width="5"/></g>
{''.join(drop(200 - i*16, 270 + i*24, 1.0) for i in range(3))}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M400 240h60"/></g>
{head(510, 250, 26, 'teal', 'short')}''')

add('be subject to', '通す前に、かならず検査の門を通される', f'''
<g transform="translate(300 200)"><rect x="-40" y="-150" width="80" height="300" rx="8" class="teald o"/>
  <rect x="-40" y="-150" width="80" height="300" rx="8" fill="none" class="o"/>
  <circle cx="0" cy="0" r="26" class="goldp o"/></g>
{box(110, 220, 100, 70, 22, 'coral')}
<path d="M180 130h80M340 130h80" class="a" marker-end="url(#ar)"/>
{box(500, 220, 100, 70, 22, 'coral')}
<g transform="translate(500 130) rotate(-14)"><circle r="26" fill="none" stroke="{CRL}" stroke-width="6"/></g>''', arrow=True)

add('believe in', '見えなくても、そこにあると信じる', f'''
{person(180, 306, 1.25, 1, 'teal', 'blue', 'hold', 'bob', 'smile')}
<g transform="translate(430 200)"><circle r="80" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="13 10"/>
  <circle r="46" class="goldp o"/></g>
{''.join(spark(x, y, 0.9) for x, y in [(340,110),(520,110),(520,290)])}
<path d="M250 210h90" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('bite the bullet', '歯を食いしばって、いやなことを引き受ける', f'''
{person(200, 306, 1.3, 1, 'coral', 'blue', 'reach', 'short', 'neutral')}
<g transform="translate(200 190)"><rect x="-26" y="-8" width="52" height="16" rx="4" fill="#fffefd" class="o"/>
  {''.join(f'<path d="M{-20+i*13} -8v16" fill="none" stroke="{INK}" stroke-width="2.5"/>' for i in range(4))}</g>
<path d="M170 170l16 6M230 170l-16 6" fill="none" stroke="{INK}" stroke-width="3.5"/>
<g transform="translate(430 230) rotate(30)"><path d="M-16-70h32v110h-32z" fill="#fffefd" class="o"/>
  <path d="M-9 40h18v24h-18z" class="blue o"/><path d="M0 64v44" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-16-70h32v-18h-32z" class="blued o"/></g>
{drop(150, 180, 0.9)}''')

add('break the ice', '二人のあいだの氷が割れて、話がはずみだす', f'''
{person(130, 306, 1.15, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{person(470, 306, 1.15, -1, 'coral', 'blue', 'give', 'bob', 'smile')}
<g transform="translate(300 240)"><path d="M-70-90l-14 180h48l-10-96 30 96h56l-24-180z" fill="#d6ecf6" class="o"/>
  <path d="M-70-90l40 60-30 30 34 20M60-90l-30 50 26 30-16 24" fill="none" stroke="#8fc4dd" stroke-width="5"/></g>
{''.join(f'<path d="M{240+i*40} {120-i*10}l-16-24" fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round"/>' for i in range(3))}
<g transform="translate(180 150)"><rect x="-50" y="-30" width="100" height="60" rx="16" class="paper"/>
  {''.join(f'<circle cx="{-20+i*20}" cy="0" r="5" fill="{MUTED}"/>' for i in range(3))}</g>''')

add('bump into', '角でばったり、思いがけない人に出くわす', f'''
<g transform="translate(300 306)"><path d="M-40 0v-260h80V0z" fill="#c3cbd1" class="o"/></g>
{person(200, 306, 1.15, 1, 'teal', 'blue', 'walk', 'short', 'surprised')}
{person(400, 306, 1.15, -1, 'coral', 'blue', 'walk', 'bob', 'surprised')}
<g class="golds" stroke-width="6">{''.join(f'<path d="M300 150v-30" transform="rotate({d} 300 190)"/>' for d in [-45, 0, 45])}</g>
{''.join(f'<path d="M{120+i*0} {200+i*40}h30" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}''')

add('by contrast', '並べて見ると、まるで逆だとよく分かる', f'''
{split()}
<g transform="translate(150 200)"><rect x="-110" y="-120" width="220" height="240" rx="10" fill="#2f4055" class="o"/>
  <circle r="46" fill="#fffefd"/></g>
<g transform="translate(450 200)"><rect x="-110" y="-120" width="220" height="240" rx="10" fill="#fffefd" class="o"/>
  <circle r="46" fill="#2f4055"/></g>
<path d="M256 340h88" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>''', arrow=True)

add('by far', '二位との差が、けたちがいに大きい', f'''
<path d="M60 340h480" fill="none" stroke="{MUTED}" stroke-width="5"/>
<rect x="100" y="70" width="90" height="270" rx="6" class="coral o"/>
{''.join(f'<rect x="{240+i*90}" y="{270}" width="60" height="70" rx="5" class="tealp o"/>' for i in range(3))}
<path d="M226 70v200" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>
<path d="M100 60h90M240 260h60" fill="none" stroke="{MUTED}" stroke-width="3"/>''', arrow=True)

add('by virtue of', '持っている資格のおかげで、門が開く', f'''
<g transform="translate(150 220) rotate(-6)"><rect x="-80" y="-54" width="160" height="108" rx="8" class="paper"/>
  <circle cx="-44" cy="-14" r="18" class="tealp o"/>
  <rect x="-16" y="-22" width="80" height="12" rx="6" fill="{MUTED}"/>
  <rect x="-64" y="20" width="128" height="12" rx="6" fill="{MUTED}"/>
  <circle cx="52" cy="34" r="16" fill="none" stroke="{CRL}" stroke-width="5"/></g>
<path d="M250 200h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(460 306)"><path d="M-100 0v-16h200v16z" class="goldd o"/>
  <path d="M-80-16v-190h20v190z" class="goldd o"/>
  <path d="M-60-206h160" fill="none" stroke="{GLDD}" stroke-width="10" transform="rotate(-46 -60 -206)"/></g>''', arrow=True)

add('call it a day', '日が暮れ、道具を置いて今日は切り上げる', f'''
<path d="M0 306h600v94H0z" class="ground"/>
<g transform="translate(500 300)"><circle r="60" class="coralp o"/>
  <path d="M-80 0h160" fill="none" stroke="{GLDD}" stroke-width="0"/></g>
{person(200, 306, 1.2, 1, 'teal', 'blue', 'reach', 'cap', 'smile')}
<g transform="translate(290 296) rotate(70)"><path d="M-8 0h16v120h-16z" class="goldd o"/>
  <path d="M-26-26h52v26h-52z" class="ink"/></g>
{clock(110, 120, 0.8, 5, 0)}''')

add('cancellation', '入っていた予定が、取り消されて空になる', f'''
<g transform="translate(300 200)"><rect x="-230" y="-140" width="460" height="280" rx="10" class="paper"/>
  <rect x="-230" y="-140" width="460" height="50" rx="0" class="teal o"/>
  {''.join(f'<rect x="{-200+ (i%4)*112}" y="{-64+(i//4)*68}" width="90" height="50" rx="6" fill="#eef2f4"/>' for i in range(8))}
  <rect x="-88" y="4" width="90" height="50" rx="6" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="10 8"/>
  <path d="M-78 14l70 30M-8 14l-70 30" fill="none" stroke="{CRL}" stroke-width="6"/></g>''')

# --- もの ---------------------------------------------------------------------

add('barley', '長いひげのある穂をつける、大麦', f'''
<g transform="translate(300 340)"><path d="M0 0v-190" fill="none" stroke="{GRND}" stroke-width="7"/>
  {''.join(f'<g transform="translate(0 {-100-i*34})">'
           f'<ellipse cx="-20" cy="0" rx="11" ry="18" class="goldp o" transform="rotate(-24 -20 0)"/>'
           f'<ellipse cx="20" cy="-8" rx="11" ry="18" class="goldp o" transform="rotate(24 20 -8)"/>'
           f'<path d="M-26-14l-30-70M26-22l30-70" fill="none" stroke="{GLDD}" stroke-width="3"/></g>' for i in range(4))}
  <ellipse cy="-244" rx="11" ry="18" class="goldp o"/>
  <path d="M0-262v-70" fill="none" stroke="{GLDD}" stroke-width="3"/></g>
{''.join(f'<path d="M{160+i*60} 340v-{50+(i%3)*20}" fill="none" stroke="{GRND}" stroke-width="5"/>' for i in range(6) if i not in (2, 3))}''')

add('basil', '鉢に植えた、丸くて香りのよい葉', f'''
{table(340)}
<g transform="translate(300 306)"><path d="M-60 0l10-70h100l10 70z" class="corald o"/>
  <path d="M-64-70h128v-16h-128z" class="coral o"/>
  <path d="M0-86v-60" fill="none" stroke="{GRND}" stroke-width="6"/>
  {''.join(f'<path d="M0-{100+i*30}q-{40+i*6}-6-{46+i*6}-34 {36+i*6} 2 {46+i*6} 26zM0-{112+i*30}q{40+i*6}-8 {46+i*6}-36-{36+i*6} 4-{46+i*6} 28z" class="greenp o"/>' for i in range(3))}
  <path d="M0-206q-24-4-30-26 22 0 30 18z" class="greenp o"/></g>
<g fill="none" stroke="{GRN}" stroke-width="4" stroke-linecap="round">
  <path d="M430 190q-14-24 0-44M470 210q-14-24 0-44"/></g>''')

add('blueprint', '青い紙に引いた、建物の設計図', f'''
<g transform="translate(300 200)"><rect x="-250" y="-150" width="500" height="300" rx="8" fill="#2f5f8e" class="o"/>
  <g fill="none" stroke="#dce9f5" stroke-width="4">
    <path d="M-160 100v-140h320v140z"/><path d="M-180-40L0-150l180 110"/>
    <path d="M-40 100V20h80v80"/><path d="M-120-10h60v50h-60zM60-10h60v50h-60z"/>
    <path d="M-200 130h400M-200 122v16M200 122v16"/>
    <path d="M-230-40h-30M-230 100h-30M-246-40v140"/></g></g>''')

add('brooch', '服の胸につける、飾りの留めピン', f'''
<g transform="translate(300 210)">
  <path d="M-150 160V-40l60-56h180l60 56v200z" class="violet o"/>
  <path d="M-90-96q90 60 180 0l-56 56h-68z" fill="#fffaf1" class="o"/></g>
<g transform="translate(370 150)"><circle r="46" class="goldp o"/>
  {''.join(f'<ellipse cx="0" cy="-30" rx="12" ry="20" class="gold o" transform="rotate({d} 0 0)"/>' for d in range(0, 360, 60))}
  <circle r="16" class="coral o"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(440,90),(310,90)])}''')

add('broadsheet', '大きく広げて読む、大判の新聞', f'''
{''.join(f'<g transform="translate({300+ (0 if i==0 else 0)} 200)"></g>' for i in range(1))}
<g transform="translate(300 200)">
  <path d="M-260-150h250v300h-250z" class="paper"/>
  <path d="M260-150H10v300h250z" class="paper"/>
  <path d="M10-150v300" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M-240-120h210" fill="none" stroke="{INK}" stroke-width="4"/>
  {word(-135, -80, 4, 40, INK)}
  {''.join(f'<rect x="{-240+ (i%2)*110}" y="{-30+(i//2)*32}" width="100" height="10" rx="5" fill="{MUTED}"/>' for i in range(8))}
  {''.join(f'<rect x="{30+ (i%2)*110}" y="{-120+(i//2)*32}" width="100" height="10" rx="5" fill="{MUTED}"/>' for i in range(10))}
  <rect x="30" y="40" width="210" height="100" rx="4" class="tealp o"/></g>
{hand(60, 210, 1)}{hand(540, 210, -1)}''')

add('brotherhood', '肩を組んで並ぶ、固い仲間意識', f'''
{''.join(f'<g transform="translate({120+i*120} 306)">{person(0, 0, 1.1, 1, c, "blue", "stand", h, "smile")}</g>'
         for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('green','short'),('gold','cap')]))}
<path d="M120 200q60-40 120 0t120 0 120 0" fill="none" stroke="{SKIN}" stroke-width="13" stroke-linecap="round"/>
{''.join(spark(x, y, 0.8) for x, y in [(90,110),(500,100)])}''')

add('bystander', 'かかわらずに、横で見ているだけの人', f'''
{person(180, 306, 1.15, 1, 'coral', 'blue', 'reach', 'short', 'neutral')}
{person(300, 306, 1.15, -1, 'violet', 'blue', 'reach', 'bob', 'neutral')}
<g class="corals" stroke-width="6">{''.join(f'<path d="M240 180v-26" transform="rotate({d} 240 220)"/>' for d in [-40, 0, 40])}</g>
{person(500, 306, 1.15, -1, 'teal', 'blue', 'hold', 'short', 'neutral')}
<path d="M440 200h-60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{ring(500, 210, 118)}''')

add('brink', 'つま先が、がけのふちぎりぎりにかかる', f'''
<path d="M0 240h300v160H0z" fill="#c3cbd1" class="o"/>
<path d="M300 240v160" fill="none" stroke="{INK}" stroke-width="4"/>
<g transform="translate(230 210)">
  <path d="M-90 30q-10-30 10-34l60-8q20-2 40 10l50 28q12 8 0 14h-150q-12 0-10-10z" fill="{CRL}" class="o"/>
  <path d="M-60-8l70-6" fill="none" stroke="{CRLD}" stroke-width="4"/>
  <path d="M-90 24h160" fill="none" stroke="{CRLD}" stroke-width="4"/>
  <path d="M-70-4v-70h60v62" fill="{BLUD}" stroke="{INK}" stroke-width="2.5"/></g>
<path d="M300 200v-40M310 180h60" fill="none" stroke="{CRL}" stroke-width="4"/>
<path d="M290 160h20" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>''', arrow=True)

add('bout', 'しばらく寝こんで、そのあとは元にもどる', f'''
<path d="M60 260h480" fill="none" stroke="{MUTED}" stroke-width="5"/>
<path d="M60 260h140l40-130 60 130h240" fill="none" stroke="{CRL}" stroke-width="7"/>
<g transform="translate(240 330)"><path d="M-120 0v-30h240V0z" class="goldd o"/>
  <path d="M-100-30v-24h200v24z" class="tealp o"/></g>
{head(240, 316, 20, 'coral', 'short')}
{person(480, 320, 0.9, 1, 'teal', 'blue', 'up', 'short', 'smile')}
<path d="M180 300h120" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>''', arrow=True)

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
