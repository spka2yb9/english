# -*- coding: utf-8 -*-
"""第152回。v-/w- の語と、a- で始まる抽象名詞。"""
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

def bin_(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-50 0l8-110h84l8 110z" fill="#c3cbd1" class="o"/>'
            f'<path d="M-58-110h116v-16h-116z" fill="#9aa6ae" class="o"/>'
            f'{"".join(f2 for f2 in [f"<path d=@M{-24+i*24} -100v84@ fill=@none@ stroke=@{INK}@ stroke-width=@3@/>".replace("@", chr(34)) for i in range(3)])}</g>')

def flagpole(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0v-200" fill="none" stroke="{INK}" stroke-width="7"/>'
            f'<path d="M0-200h120l-28 40 28 40H0z" class="{cls} o"/></g>')

# --- 残りの un-/w- 形容詞 ------------------------------------------------------

add('unresolved', 'もつれたままで、まだほどけていない', f'''
{table(340)}
<g transform="translate(280 210)" fill="none" stroke="{CRLD}" stroke-width="14" stroke-linecap="round">
  <path d="M-110 60q60-120 130-40t-90 40 100-90 40 70-140-30"/></g>
{head(500, 260, 28, 'teal', 'short')}
<g transform="translate(500 150)"><path d="M-14-30a26 26 0 1 1 22 42q-8 8-8 18" fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="46" r="6" fill="{MUTED}"/></g>''')

add('unsettling', 'すこし開いた扉の奥が暗く、思わずあとずさる', f'''
<g transform="translate(430 306)"><path d="M-100 0v-220h200V0z" fill="#fffefd" class="o"/>
  <path d="M-80 0v-200h60V0z" fill="#2a3340"/>
  <path d="M-20 0v-200h100V0z" class="goldp o"/><circle cx="-4" cy="-100" r="8" class="ink"/></g>
{person(180, 306, 1.2, -1, 'teal', 'blue', 'reach', 'short', 'surprised')}
<g fill="none" stroke="{VIO}" stroke-width="4" stroke-dasharray="9 8">
  <path d="M280 140q20 30 0 60M310 130q24 36 0 72"/></g>
{drop(150, 180, 1.0)}''')

add('untenable', '足もとが欠けていき、その場に立っていられない', f'''
<path d="M0 300h600v100H0z" fill="{BLUP}"/>
<path d="M180 300q-30 60 40 76t150-20 30-56z" fill="#eaf4fb" class="o"/>
<g opacity="0.35"><path d="M120 300q-40 70 20 96" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9"/></g>
{person(280, 300, 1.15, 1, 'coral', 'blue', 'up', 'short', 'surprised')}
<path d="M400 320q30 20 60 6M120 330q26 18 54 4" fill="none" stroke="{BLU}" stroke-width="5"/>
{''.join(f'<path d="M{430+i*40} {290-i*10}l-30 20" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}''')

add('valueless', '宝石に見えたが、ただのガラスで値がつかない', f'''
{table(340)}
<g transform="translate(240 250)"><path d="M-56-30h112l-56 84z" fill="#eef4f6" class="o"/>
  <path d="M-56-30l26-28h60l26 28z" fill="#f8fbfc" class="o"/></g>
<g transform="translate(450 220) rotate(-10)"><path d="M-62-34h96l28 34-28 34h-96z" class="paper"/>
  <circle cx="34" cy="0" r="7" class="ink"/>
  <path d="M-42 0h44" fill="none" stroke="{MUTED}" stroke-width="7"/></g>
{head(140, 200, 26, 'coral', 'short')}
<path d="M172 190q16-16 0-34" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

add('worthless', 'こわれて役に立たず、捨てるほかない', f'''
{table(340)}
<g transform="translate(200 260) rotate(-14)"><path d="M-8 0h16v70h-16z" class="goldd o"/>
  <path d="M-40-40h80v34h-80z" fill="#8d949a" class="o"/>
  <path d="M0-40l-30-30M0-40l26-34" fill="none" stroke="{CRL}" stroke-width="5"/>
  <path d="M-40-6l-26 16M40-6l26 16" fill="none" stroke="{CRL}" stroke-width="5"/></g>
<path d="M300 220h70" class="a" marker-end="url(#ar)"/>
{bin_(470, 330, 1.0)}''', arrow=True)

add('wary', 'うますぎる話には、距離を取って近づかない', f'''
{person(150, 306, 1.2, -1, 'teal', 'blue', 'reach', 'short', 'neutral')}
<g transform="translate(430 220)">{box(0, 0, 130, 96, 28, 'gold')}
  {spark(-80, -60, 0.9)}{spark(78, -66, 0.9)}</g>
<path d="M430 300v40q0 26 26 26t26-20" fill="none" stroke="{CRL}" stroke-width="8" stroke-linecap="round"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M226 220h100"/></g>
<path d="M120 190l16 6M184 190l-16 6" fill="none" stroke="{INK}" stroke-width="3"/>''')

add('watchful', '広く目を配り、少しの動きも見のがさない', f'''
{person(160, 306, 1.25, 1, 'blue', 'blue', 'stand', 'cap', 'neutral')}
<g transform="translate(300 130)"><path d="M-40 0q40-30 80 0-40 30-80 0z" fill="#fffefd" class="o"/><circle r="13" class="ink"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9">
  <path d="M228 190L520 110M228 210L540 230M232 240L500 340"/></g>
{box(520, 300, 70, 48, 14, 'gold')}
{head(520, 130, 22, 'coral', 'bob')}''')

add('weary', '長い道のりを終えて、疲れきってうなだれる', f'''
<path d="M40 340q140-24 280-8t240 12" fill="none" stroke="{GLDD}" stroke-width="8" stroke-dasharray="20 14"/>
{''.join(f'<ellipse cx="{60+i*54}" cy="{350+(i%2)*14}" rx="14" ry="7" class="ink" opacity="0.35"/>' for i in range(6))}
<g transform="translate(430 340)">
  <path d="M-14-8l-10 32M14-8l10 32" fill="none" stroke="{BLUD}" stroke-width="13" stroke-linecap="round"/>
  <path d="M-28-80q28-14 56 0l-9 72h-38z" fill="{TEA}" class="o"/>
  <path d="M-24-72l-8 56M24-72l8 56" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
  <circle cx="0" cy="-108" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 -2) scale(1.05)" fill="{HAIR}"/>
  <path d="M-16-112l14 6M16-112l-14 6" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-8-92q8-8 16 0" fill="none" stroke="{INK}" stroke-width="2.5"/></g>
{''.join(f'<path d="M{490+i*24} {230-i*22}q16 16 0 32" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}''')

add('weightless', '重さがなくなり、人も物も浮かんでいる', f'''
<g transform="translate(300 200)"><rect x="-270" y="-170" width="540" height="340" rx="16" fill="#e9eef2" class="o"/>
  <circle cx="-190" cy="-110" r="46" class="bluep o"/><circle cx="-190" cy="-110" r="36" fill="#dbe6ee"/></g>
<g transform="translate(300 210) rotate(-18)">{person(0, 60, 1.0, 1, 'coral', 'blue', 'up', 'cap', 'smile')}</g>
{''.join(f'<g transform="translate({x} {y}) rotate({r})">{box(0, 0, 54, 40, 12, "gold")}</g>' for x, y, r in [(120,290,20),(480,150,-24),(500,300,12)])}
{''.join(f'<circle cx="{x}" cy="{y}" r="9" class="tealp o"/>' for x, y in [(180,140),(240,320),(420,90),(390,330)])}''')

add('wholesome', '野菜たっぷりの食事で、体の調子がよい', f'''
{table(320)}
<g transform="translate(210 280)"><ellipse rx="100" ry="26" fill="#fffefd" class="o"/>
  <circle cx="-46" cy="-16" r="24" class="greenp o"/><circle cx="-4" cy="-22" r="20" class="coral o"/>
  <path d="M28-18q34-16 50 8-32 16-50-8z" class="green o"/>
  <circle cx="60" cy="-32" r="14" class="goldp o"/></g>
{person(460, 306, 1.2, 1, 'green', 'blue', 'up', 'short', 'smile')}
{''.join(spark(x, y, 0.9) for x, y in [(380,120),(540,130)])}''')

add('wilful', '禁止の札を見ながら、わざと線をまたぐ', f'''
<path d="M300 90v250" fill="none" stroke="{CRL}" stroke-width="6" stroke-dasharray="14 12"/>
<g transform="translate(300 120)"><rect x="-70" y="-46" width="140" height="80" rx="8" class="paper"/>
  <path d="M-46 0h92" fill="none" stroke="{CRL}" stroke-width="10"/></g>
{person(320, 340, 1.2, 1, 'coral', 'blue', 'walk', 'short', 'neutral', 'walk')}
<path d="M356 232l90-20" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
<path d="M300 232h56" fill="none" stroke="{MUTED}" stroke-width="0"/>
<path d="M370 216l-14 4 4-14" fill="none" stroke="{MUTED}" stroke-width="0"/>
<path d="M356 226q-40-40-6-84" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('wind up', '会が終わり、コードを巻き取って片づける', f'''
{''.join(f'<g transform="translate({120+i*100} 340)">{chair(0, 0, 0.7, "violet", 1)}</g>' for i in range(3))}
{person(450, 340, 1.2, -1, 'teal', 'blue', 'hold', 'bun', 'smile')}
<g transform="translate(400 230)"><circle r="46" fill="none" stroke="{INK}" stroke-width="10"/>
  <circle r="26" fill="none" stroke="{INK}" stroke-width="10"/>
  <path d="M-46 0q-70 20-110-10" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/></g>
<path d="M400 150a56 56 0 0 1 40 30" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/>''', arrow=True)

add('wink', '片目だけをつぶって合図する', f'''
<g transform="translate(300 200)"><circle r="140" fill="{SKIN}" stroke="{SKINL}" stroke-width="4"/>
  <path d="{HAIRS['short']}" transform="translate(0 620) scale(5.6)" fill="{HAIR}"/>
  <circle cx="-52" cy="-20" r="14" class="ink"/>
  <path d="M28-20q24-22 48 0" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
  <path d="M-40 50q40 40 80 0" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/></g>
{''.join(spark(x, y, 1) for x, y in [(470,120),(510,190)])}''')

add('witty', 'すかさず返したひとことで、みんなが笑う', f'''
{person(150, 306, 1.15, 1, 'teal', 'blue', 'point', 'short', 'smile')}
<g transform="translate(320 160)"><rect x="-90" y="-52" width="180" height="104" rx="24" class="paper"/>
  <path d="M-70 46l-24 30 4-30z" class="paper"/>
  {word(0, 0, 3, 32, TEA)}{spark(66, -40, 0.8)}</g>
{head(480, 250, 30, 'coral', 'bob')}{head(540, 320, 26, 'violet', 'short')}
<path d="M456 216q16-16 0-30M520 290q16-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M460 262q22 16 44 0" fill="none" stroke="{INK}" stroke-width="3"/>''')

add('worry about', 'まだ起きていないことを、あれこれ心配する', f'''
{sit(200, 330, 1.25, 1, 'teal', 'blue', 'short', 'sad', 'lap')}
{chair(214, 330, 1.15, 'gold', -1)}
<circle cx="300" cy="200" r="9" fill="#fffefd" class="o"/>
<circle cx="326" cy="170" r="13" fill="#fffefd" class="o"/>
<g transform="translate(450 130)"><ellipse rx="126" ry="86" fill="#fffefd" class="o"/>
  {cloud(-30, -20, 1.1, 'violet')}
  <path d="M10 10l-22 42h28l-22 44 60-66h-28l20-28z" class="gold o"/></g>
{drop(150, 200, 1.0)}''')

add('wasteful', '使ってもいない水を、出しっぱなしにする', f'''
<g transform="translate(220 150)"><path d="M-90-40h40v50h-40z" class="teald o"/>
  <path d="M-50-30h100v22h-30v40h-24v-40h-46z" class="teal o"/></g>
<path d="M244 172v130" fill="none" stroke="{BLU}" stroke-width="16" stroke-linecap="round"/>
<g transform="translate(244 320)"><ellipse rx="80" ry="20" fill="{BLUP}" class="o"/></g>
{''.join(drop(300 + i*22, 250 + i*18, 1.0) for i in range(3))}
{bin_(470, 320, 0.85)}
{''.join(f'<circle cx="{440+i*28}" cy="{200-i*14}" r="14" class="greenp o"/>' for i in range(3))}
<path d="M470 190v20" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="7 6"/>''')

add('vigorous', '力いっぱい、勢いよく体を動かす', f'''
{person(300, 306, 1.35, 1, 'coral', 'blue', 'up', 'cap', 'smile')}
<g fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round">
  <path d="M150 130q26-26 0-52M110 190h-40M160 250h-46M450 130q-26-26 0-52M490 190h40M440 250h46"/></g>
{''.join(drop(x, y, 1.0) for x, y in [(230,120),(376,116)])}''')

add('vivid', 'くすんだ色と、目のさめるような鮮やかな色の対比', f'''
{split()}
<g transform="translate(150 200)"><path d="M-96-96h192v192h-192z" fill="#d8d4cb" class="o"/>
  <path d="M-96 60l60-70 44 44 40-56 52 82v40h-196z" fill="#b9bdae"/>
  <circle cx="46" cy="-50" r="24" fill="#cfc6ab"/></g>
{ring(150, 200, 132, True)}
<g transform="translate(450 200)"><path d="M-96-96h192v192h-192z" fill="#bfe9f7" class="o"/>
  <path d="M-96 60l60-70 44 44 40-56 52 82v40h-196z" class="green o"/>
  <circle cx="46" cy="-50" r="24" class="gold o"/></g>
{ring(450, 200, 132)}''')

# --- 名詞・慣用 --------------------------------------------------------------

add('vest', 'そでのない、上半身に着るもの', f'''
{table(340)}
<g transform="translate(300 200)">
  <path d="M-110 120V-40l46-46h128l46 46v160z" class="violet o"/>
  <path d="M-64-86q64 46 128 0l-40 46h-48z" fill="#fffaf1" class="o"/>
  <path d="M-16-40L-16 120M16-40L16 120" fill="none" stroke="{VIOD}" stroke-width="3"/>
  {''.join(f'<circle cx="0" cy="{-4+i*40}" r="8" class="goldp o"/>' for i in range(3))}</g>''')

add('vinegar', 'つんとすっぱい、酢のびん', f'''
{table(340)}
<g transform="translate(220 306)"><path d="M-40 0v-100q0-22 16-32v-30h48v30q16 10 16 32V0z" fill="#f3e2b6" class="o"/>
  <path d="M-24-162h48v-18h-48z" class="goldd o"/>
  <path d="M-32-90h64v78h-64z" fill="#e0c580"/></g>
{head(430, 250, 40, 'green', 'bob')}
<path d="M410 268q20-12 40 0" fill="none" stroke="{INK}" stroke-width="4"/>
<path d="M404 236l16 8M456 236l-16 8" fill="none" stroke="{INK}" stroke-width="3.5"/>
<g fill="none" stroke="{GRN}" stroke-width="5" stroke-linecap="round">
  <path d="M300 170q-16-26 0-50M340 150q-16-26 0-50"/></g>''')

add('vowel', '口をあけて、さえぎらずに出す音', f'''
<g transform="translate(200 200)"><ellipse rx="130" ry="96" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <ellipse cy="10" rx="56" ry="66" fill="#7a2f28" class="o"/>
  <ellipse cy="34" rx="34" ry="24" fill="#c05a52"/></g>
{''.join(f'<path d="M340 {200-14-i*24}q{14+i*24} {14+i*24} 0 {(14+i*24)*2}" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/>' for i in range(3))}
<path d="M330 200h150" fill="none" stroke="{CRL}" stroke-width="5" stroke-dasharray="0" marker-end="url(#ar)"/>''', arrow=True)

add('walnut', 'かたい殻を割ると、しわの多い実が出てくる', f'''
{table(340)}
<g transform="translate(180 270)"><ellipse rx="70" ry="76" fill="#b98d55" class="o"/>
  <path d="M0-76v152" fill="none" stroke="#8c6a3c" stroke-width="4"/>
  {''.join(f'<path d="M{-46+i*26} -60q10 60 0 120" fill="none" stroke="#8c6a3c" stroke-width="3"/>' for i in range(4))}</g>
<path d="M280 250h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(440 270)"><ellipse rx="76" ry="80" fill="#b98d55" class="o"/>
  <ellipse rx="60" ry="66" fill="#e6cfa4" class="o"/>
  <path d="M0-64v128" fill="none" stroke="#c9ab74" stroke-width="4"/>
  {''.join(f'<path d="M{-38+i*22} {-44+ (i%2)*16}q22 22 0 44q-22 22 0 44" fill="none" stroke="#c9ab74" stroke-width="4"/>' for i in range(4))}</g>''', arrow=True)

add('a far cry from', 'ねらいと結果が、あまりにかけ離れている', f'''
<path d="M60 300h480" fill="none" stroke="{MUTED}" stroke-width="5"/>
<circle cx="110" cy="300" r="18" class="coral o"/>
<circle cx="500" cy="300" r="18" class="teal o"/>
<path d="M140 220h330" class="a" stroke-width="5" marker-end="url(#ar)" marker-start="url(#ar)"/>
<g transform="translate(110 160)"><path d="M-40 40l40-70 40 70z" class="coralp o"/></g>
<g transform="translate(500 160)"><circle r="40" class="tealp o"/></g>''', arrow=True)

add('a handful of', '袋いっぱいではなく、手にひと握りだけ', f'''
{split()}
<g transform="translate(150 290)"><path d="M-70 0q-16-110 16-140h108q32 30 16 140z" fill="#d9c9a4" class="o"/>
  {''.join(f'<circle cx="{-40+ (i%4)*28}" cy="{-100+(i//4)*30}" r="12" class="goldp o"/>' for i in range(8))}</g>
{ring(150, 220, 128, True)}
{hand(450, 250, 1)}
{''.join(f'<circle cx="{424+ (i%3)*24}" cy="{206+(i//3)*20}" r="11" class="goldp o"/>' for i in range(5))}
{ring(450, 230, 118)}''')

add('all the same', 'さまたげがあっても、行きつく先は変わらない', f'''
<path d="M60 200h150" fill="none" stroke="{TEA}" stroke-width="8"/>
<g transform="translate(250 200)"><path d="M-30-70h60v140h-60z" fill="#c3cbd1" class="o"/></g>
<path d="M290 200h180" fill="none" stroke="{TEA}" stroke-width="8" marker-end="url(#ar)"/>
<path d="M210 200q40-90 80 0" fill="none" stroke="{TEA}" stroke-width="8"/>
<g transform="translate(520 200)"><circle r="46" class="coral o"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M250 300v40"/></g>''', arrow=True)

add('abolition', '掲げてあった決まりを、外して取りやめる', f'''
<g transform="translate(180 306)"><path d="M-8 0v-230h16V0z" class="goldd o"/>
  <path d="M-90-230h180v-16h-180z" class="goldd o"/>
  <rect x="-90" y="-230" width="180" height="0" fill="none"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10">
  <rect x="90" y="120" width="180" height="120" rx="8"/></g>
<path d="M300 190h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(470 210) rotate(20)">{doc(0, 0, 170, 200, 4)}</g>
{hand(470, 90, 1)}''', arrow=True)

add('absurdity', '野原のまん中に、どこにも通じない扉が立っている', f'''
<path d="M0 280q140-30 300-26t300 26v120H0z" class="greenp o"/>
<g transform="translate(300 306)"><path d="M-70 0v-200h140V0z" fill="#fffefd" class="o"/>
  <path d="M-56 0v-186h112V0z" class="goldp o"/><circle cx="34" cy="-96" r="8" class="ink"/></g>
{person(150, 320, 1.05, 1, 'teal', 'blue', 'reach', 'short', 'surprised')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M380 210h120"/></g>
<g transform="translate(520 130)"><path d="M-14-30a26 26 0 1 1 22 42q-8 8-8 18" fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="46" r="6" fill="{MUTED}"/></g>''')

add('acceleration', '進むほど、間かくが広がって速くなる', f'''
<path d="M40 330h520v10H40z" class="goldd o"/>
{''.join(f'<circle cx="{x}" cy="300" r="10" class="tealp o"/>' for x in [70, 100, 140, 200, 280, 390])}
<g transform="translate(470 290)">
  <path d="M-110 20v-30l30-40h150l30 40v30z" class="coral o"/>
  <path d="M-60-50l16-24h88l18 24z" class="bluep o"/>
  <circle cx="-60" cy="26" r="22" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle cx="70" cy="26" r="22" fill="none" stroke="{INK}" stroke-width="7"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round">
  <path d="M300 200h-60M270 240h-90"/></g>
<path d="M120 150h360" class="a" stroke-width="5" marker-end="url(#ar)"/>''', arrow=True)

add('accountancy', '帳簿の数を合わせて、収支をまとめる仕事', f'''
{table(320)}
{doc(200, 200, 200, 240, 0)}
{''.join(f'<g><rect x="120" y="{110+i*44}" width="90" height="12" rx="6" fill="{MUTED}"/>'
         f'<rect x="230" y="{110+i*44}" width="50" height="12" rx="6" class="teal"/></g>' for i in range(4))}
<path d="M110 296h180" fill="none" stroke="{INK}" stroke-width="4"/>
<g transform="translate(430 250)"><rect x="-70" y="-100" width="140" height="200" rx="10" class="teald o"/>
  <rect x="-54" y="-84" width="108" height="44" rx="4" fill="#dfe6ea"/>
  {''.join(f'<circle cx="{-34+ (i%3)*34}" cy="{-14+(i//3)*34}" r="12" class="tealp o"/>' for i in range(9))}</g>
{head(540, 130, 26, 'violet', 'bun')}''')

add('acorn', 'ぼうしをかぶった、かしの木の実', f'''
{table(340)}
<g transform="translate(260 260)"><path d="M-46 0q0 70 46 70t46-70z" fill="#c9944a" class="o"/>
  <ellipse cy="-6" rx="52" ry="34" fill="#8a6236" class="o"/>
  {''.join(f'<path d="M{-44+i*18} -30v46" fill="none" stroke="#6f4d28" stroke-width="3"/>' for i in range(5))}
  <path d="M0-40v-22" fill="none" stroke="#6f4d28" stroke-width="6" stroke-linecap="round"/></g>
<g transform="translate(450 250)"><path d="M0 60q-70-10-70-60 0-40 34-56 6-30 36-30t36 30q34 16 34 56 0 50-70 60z" class="greenp o"/>
  <path d="M0 60V-100" fill="none" stroke="{GRND}" stroke-width="4"/></g>''')

add('acquaintance', '親友ほどではない、顔を知っている程度の間がら', f'''
{split()}
{person(90, 306, 1.0, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(210, 306, 1.0, -1, 'coral', 'blue', 'stand', 'bob', 'smile')}
<path d="M126 200h48" fill="none" stroke="{GRN}" stroke-width="14" stroke-linecap="round"/>
{ring(150, 210, 122, True)}
{person(370, 306, 1.0, 1, 'violet', 'blue', 'stand', 'short', 'neutral')}
{person(530, 306, 1.0, -1, 'gold', 'blue', 'stand', 'bun', 'neutral')}
<path d="M406 200h88" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>
{ring(450, 210, 130)}''')

add('acquittal', '罪ではないと決まり、囲いの外へ出される', f'''
<g transform="translate(180 210)"><path d="M-96-96h192v192h-192z" fill="none" stroke="{INK}" stroke-width="6"/>
  {''.join(f'<path d="M{-66+i*34} -96v192" fill="none" stroke="{INK}" stroke-width="6"/>' for i in range(5))}
  <path d="M30-96v192" fill="none" stroke="{GLDD}" stroke-width="8" transform="rotate(28 30 0)"/></g>
{person(430, 306, 1.2, 1, 'teal', 'blue', 'up', 'short', 'smile')}
<path d="M300 210h70" class="a" marker-end="url(#ar)"/>
<g transform="translate(520 120) rotate(24)"><path d="M-10 0h20v70h-20z" class="goldd o"/>
  <path d="M-34-40h68v40h-68z" class="goldd o"/></g>''', arrow=True)

add('addict', 'やめられず、空の容器が積み上がる', f'''
{table(330)}
{person(180, 306, 1.2, 1, 'coral', 'blue', 'hold', 'short', 'neutral')}
<g transform="translate(214 218)"><path d="M-22 0v-52h44V0z" class="teal o"/></g>
{''.join(f'<g transform="translate({350+ (i%3)*70} {300-(i//3)*56})"><path d="M-20 0v-46h40V0z" class="tealp o"/></g>' for i in range(6))}
<g transform="translate(180 120)"><path d="M-46 0a46 46 0 1 1 16 34" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/></g>''', arrow=True)

add('adherence', '引かれた線から、はみ出さずにたどる', f'''
<path d="M60 240q80-100 180-60t130 100 140-60" fill="none" stroke="{CRL}" stroke-width="8" stroke-dasharray="16 12"/>
{''.join(f'<ellipse cx="{x}" cy="{y}" rx="15" ry="8" class="ink" transform="rotate({r} {x} {y})"/>' for x, y, r in
  [(90,224,-40),(150,190,-30),(210,178,-6),(270,196,20),(330,236,34),(390,266,20),(450,262,-14),(510,232,-30)])}
{person(560, 210, 0.9, 1, 'teal', 'blue', 'walk', 'short', 'neutral', 'walk')}''')

add('admiration', 'すぐれた人を見上げて、拍手を送る', f'''
{person(300, 250, 1.15, 1, 'violet', 'blue', 'up', 'bun', 'smile')}
<g transform="translate(300 306)"><path d="M-90 0v-46h180V0z" class="goldd o"/></g>
{''.join(spark(x, y, 1) for x, y in [(200,90),(400,80),(150,170),(460,160)])}
{''.join(f'<g transform="translate({x} 386)">{head(0, 0, 26, c, h)}</g>' for x, (c, h) in
  zip([80, 170, 430, 520], [('teal','short'),('coral','bob'),('green','short'),('gold','cap')]))}
{''.join(f'<g transform="translate({x} 320)">{hand(-14, 0, 1)}{hand(14, 0, -1)}</g>' for x in [125, 475])}''')

add('adolescence', '子どもから大人へ変わっていく、その途中の時期', f'''
{table(400)}
{person(120, 330, 0.72, 1, 'coral', 'blue', 'stand', 'bob', 'smile')}
{person(300, 330, 1.0, 1, 'teal', 'blue', 'stand', 'short', 'neutral')}
{person(490, 330, 1.25, 1, 'violet', 'blue', 'stand', 'short', 'smile')}
<path d="M190 200h50M370 200h50" class="a" marker-end="url(#ar)"/>
{ring(300, 220, 122)}''', arrow=True)

add('adulthood', '育ちきって、大人としての時期に入る', f'''
{table(400)}
{person(120, 330, 0.72, 1, 'coral', 'blue', 'stand', 'bob', 'smile')}
{person(300, 330, 1.0, 1, 'teal', 'blue', 'stand', 'short', 'neutral')}
{person(490, 330, 1.25, 1, 'violet', 'blue', 'stand', 'short', 'smile')}
<path d="M190 200h50M370 200h50" class="a" marker-end="url(#ar)"/>
{ring(490, 200, 140)}''', arrow=True)

add('advancement', '段を一つずつ上がって、高いところへ進む', f'''
{''.join(f'<rect x="{60+i*100}" y="{330-i*60}" width="100" height="{60+i*60}" rx="4" class="tealp o"/>' for i in range(5))}
{person(500, 90, 0.9, 1, 'coral', 'blue', 'up', 'short', 'smile')}
<path d="M120 250q160-140 340-160" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/>''', arrow=True)

add('adversity', '向かい風と雨のなかを、坂を上っていく', f'''
<path d="M0 400q160-160 600-220v220z" class="greenp o"/>
{cloud(180, 90, 1.5, 'violet')}{cloud(420, 70, 1.6, 'violet')}
{''.join(f'<path d="M{60+i*46} {150+(i%3)*20}l-20 40" fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round"/>' for i in range(10))}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M520 200h-100M540 250h-120"/></g>
<g transform="translate(300 306) rotate(-14)">{person(0, 0, 1.15, 1, 'coral', 'blue', 'reach', 'cap', 'neutral', 'walk')}</g>''')

add('affiliation', '団体の輪に加わり、しるしを身につける', f'''
<circle cx="240" cy="200" r="140" fill="none" stroke="{TEA}" stroke-width="7"/>
{''.join(f'<g transform="translate({240+96*math.cos(math.radians(a)):.0f} {200+96*math.sin(math.radians(a)):.0f})">{head(0, 0, 26, c, h)}</g>'
         for a, (c, h) in zip([250, 320, 30, 100, 170], [('teal','short'),('coral','bob'),('green','short'),('gold','bun'),('blue','cap')]))}
{person(500, 306, 1.15, -1, 'violet', 'blue', 'walk', 'short', 'smile')}
<path d="M448 210h-60" class="a" marker-end="url(#ar)"/>
<g transform="translate(500 208)"><circle r="17" class="coral o"/></g>''', arrow=True)

add('affirmation', 'はっきりうなずいて、そうだと認める', f'''
{person(200, 306, 1.3, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
<g fill="none" class="a" stroke-width="5">
  <path d="M270 150a56 56 0 0 1 0 60" marker-end="url(#ar)"/></g>
<g transform="translate(430 170)"><rect x="-110" y="-64" width="220" height="128" rx="24" class="paper"/>
  <path d="M-90 52l-32 40 6-40z" class="paper"/>
  <circle r="42" fill="none" stroke="{GRN}" stroke-width="12"/></g>''', arrow=True)

add('allegiance', '旗じるしに、しっかり結ばれて離れない', f'''
{flagpole(430, 306, 1.0, 'coral')}
{person(160, 306, 1.2, 1, 'teal', 'blue', 'stand', 'short', 'neutral')}
<path d="M200 220q120-40 226-6" fill="none" stroke="{GLDD}" stroke-width="9"/>
<path d="M196 216q-16 10 0 20" fill="none" stroke="{GLDD}" stroke-width="9"/>
<path d="M160 216h36" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>''')

add('allure', '明るい店先に、人が引き寄せられていく', f'''
<g transform="translate(430 306)"><path d="M-120 0v-160h240V0z" fill="#fff6d8" class="o"/>
  <path d="M-134-160h268l-30-40h-208z" class="coral o"/>
  {''.join(f'<circle cx="{-70+i*70}" cy="-90" r="26" class="goldp o"/>' for i in range(3))}</g>
{''.join(spark(x, y, 1) for x, y in [(320,120),(540,110)])}
{person(120, 306, 1.05, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
{person(220, 306, 1.0, 1, 'violet', 'blue', 'walk', 'bob', 'smile')}
<path d="M120 180h160" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('altar', 'ろうそくを置いた、儀式のための台', f'''
<g transform="translate(300 306)"><path d="M-160 0v-140q0-120 160-120t160 120V0z" fill="#f0ece2" class="o"/>
  <path d="M-110 0v-120q0-90 110-90t110 90V0z" fill="#fdfbf6" class="o"/></g>
<g transform="translate(300 300)"><path d="M-120 0v-40h240V0z" class="violetd o"/>
  <path d="M-100-40v-50h200v50z" fill="#fffefd" class="o"/>
  <path d="M-100-40h200" fill="none" stroke="{VIO}" stroke-width="5"/></g>
{''.join(f'<g transform="translate({x} 260)"><path d="M-10-40h20v40h-20z" fill="#fffefd" class="o"/>'
         f'<path d="M0-40v-10" fill="none" stroke="{INK}" stroke-width="3"/>'
         f'<path d="M0-52q-14-16 0-30 14 14 0 30z" class="coral o"/></g>' for x in [200, 400])}''')

add('amphibian', '水にも陸にもすむ生きもの', f'''
<path d="M300 306h300v94H300z" fill="{BLUP}"/>
<path d="M300 306v94" fill="none" stroke="{BLU}" stroke-width="4"/>
<g transform="translate(250 280)"><ellipse rx="76" ry="52" class="green o"/>
  <circle cx="-34" cy="-46" r="24" class="green o"/><circle cx="30" cy="-48" r="24" class="green o"/>
  <circle cx="-34" cy="-50" r="10" fill="#fffefd" class="o"/><circle cx="30" cy="-52" r="10" fill="#fffefd" class="o"/>
  <circle cx="-34" cy="-50" r="5" class="ink"/><circle cx="30" cy="-52" r="5" class="ink"/>
  <path d="M-30 8q30 20 60 0" fill="none" stroke="{GRND}" stroke-width="4"/>
  <path d="M-70 40l-40 26 40 6M64 44l44 22-40 10" fill="none" stroke="{GRN}" stroke-width="10" stroke-linecap="round"/></g>
<g transform="translate(470 350)"><ellipse rx="34" ry="24" class="green o"/>
  <path d="M32-4l40-24v50z" class="greenp o"/>
  <circle cx="-14" cy="-6" r="5" class="ink"/></g>''')

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
