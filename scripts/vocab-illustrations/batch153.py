# -*- coding: utf-8 -*-
"""第153回。an-/ap-/ar-/as-/at-/au-/av- の抽象名詞と慣用表現。"""
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

def bottle(x, y, s=1, cls='green'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-30 0v-70q0-16 12-24v-24h36v24q12 8 12 24V0z" class="{cls} o"/>'
            f'<path d="M-18-118h36v14h-36z" class="{cls}d o"/></g>')

def germ(x, y, s=1, cls='violet'):
    spikes = ''.join(f'<path d="M0 -22v-12" transform="rotate({d})"/>' for d in range(0, 360, 45))
    return (f'<g transform="translate({x} {y}) scale({s})"><g class="{cls}s" stroke-width="4">{spikes}</g>'
            f'<circle r="22" class="{cls} o"/><circle cx="-7" cy="-5" r="4" fill="#fffefd"/></g>')

def magnifier(x, y, r=60, rot=24):
    return (f'<g transform="translate({x} {y}) rotate({rot})"><circle r="{r}" fill="#ffffff" opacity="0.16" stroke="{INK}" stroke-width="6"/>'
            f'<path d="M0 {r}v{r*0.7:.0f}" stroke="{INK}" stroke-width="15" stroke-linecap="round"/></g>')

def gear(x, y, r=44, cls='teal'):
    teeth = ''.join(f'<rect x="-8" y="{-r-14}" width="16" height="18" rx="3" transform="rotate({d})"/>' for d in range(0, 360, 45))
    return (f'<g transform="translate({x} {y})"><g class="{cls} o">{teeth}</g>'
            f'<circle r="{r}" class="{cls} o"/><circle r="{r*0.34:.0f}" fill="#fffdf6" class="o"/></g>')

# --- 気持ち ------------------------------------------------------------------

add('anguish', '身をかがめ、頭をかかえて深く苦しむ', f'''
<g transform="translate(300 306)">
  <path d="M-16-6l-14 30M16-6l14 30" fill="none" stroke="{BLUD}" stroke-width="14" stroke-linecap="round"/>
  <path d="M-34-90q34-16 68 0l-12 84h-44z" fill="{VIO}" class="o"/>
  <path d="M-30-84q-30 20-24 54M30-84q30 20 24 54" fill="none" stroke="{SKIN}" stroke-width="13" stroke-linecap="round"/>
  <circle cx="0" cy="-126" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="{HAIRS['short']}" transform="translate(0 -18) scale(1.24)" fill="{HAIR}"/>
  <path d="M-18-134l16 8M18-134l-16 8" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>
  <path d="M-9-106q9-10 18 0" fill="none" stroke="{INK}" stroke-width="3"/>
  {hand(-54, -128, 1)}{hand(54, -128, -1)}
</g>
<g opacity="0.7">{cloud(300, 90, 1.6, 'violet')}</g>
{drop(250, 200, 1.0)}{drop(348, 204, 1.0)}''')

add('annoyance', '耳もとを飛び回る虫が、いつまでもうるさい', f'''
{person(280, 306, 1.3, 1, 'teal', 'blue', 'reach', 'short', 'sad')}
<g transform="translate(400 150)"><ellipse rx="18" ry="11" fill="{INK}"/>
  <ellipse cx="-10" cy="-14" rx="16" ry="8" fill="#c9d4da" opacity="0.8" transform="rotate(-30 -10 -14)"/>
  <ellipse cx="6" cy="-16" rx="16" ry="8" fill="#c9d4da" opacity="0.8" transform="rotate(20 6 -16)"/></g>
<path d="M330 180q60-70 120-20t-60 90" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M170 180q16-20 0-40M180 240h-40"/></g>''')

add('apprehension', 'この先に起きることを思って、落ち着かない', f'''
{person(180, 306, 1.2, 1, 'coral', 'blue', 'hold', 'bob', 'sad')}
<circle cx="270" cy="190" r="9" fill="#fffefd" class="o"/>
<circle cx="296" cy="158" r="13" fill="#fffefd" class="o"/>
<g transform="translate(440 140)"><ellipse rx="126" ry="88" fill="#fffefd" class="o"/>
  <path d="M-90 50h180" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M-20-10h40v60h-40z" class="coral o"/>
  <path d="M0-10v-40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 7"/>
  <g class="corals" stroke-width="4">{''.join(f'<path d="M0 -60v-16" transform="rotate({d})"/>' for d in [-30, 0, 30])}</g></g>
{drop(150, 190, 0.9)}''')

add('apathy', 'すぐ横で何が起きても、だれも反応しない', f'''
<g transform="translate(160 150)">
  <g class="corals" stroke-width="6">{''.join(f'<path d="M0 -56v-28" transform="rotate({d})"/>' for d in range(0, 360, 45))}</g>
  <path d="M0-52l16 34 36 4-27 26 7 36-32-18-32 18 7-36-27-26 36-4z" class="coral o"/></g>
{''.join(f'<g transform="translate({330+ (i%3)*95} {250+(i//3)*80})">{head(0, 0, 28, c, h)}'
         f'<path d="M-11 12h22" fill="none" stroke="{INK}" stroke-width="3"/></g>'
         for i, (c, h) in enumerate([('teal','short'),('violet','bob'),('green','short'),('gold','bun'),('blue','cap'),('coral','short')]))}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M230 200h60"/></g>''')

add('astonishment', '思いもよらないことに、目を丸くして立ちつくす', f'''
{person(300, 306, 1.3, 1, 'coral', 'blue', 'up', 'short', 'surprised')}
<g class="golds" stroke-width="7">{''.join(f'<path d="M300 120v-40" transform="rotate({d} 300 190)"/>' for d in range(0, 360, 30))}</g>
{''.join(spark(x, y, 1.1) for x, y in [(140,150),(470,140),(160,280),(470,280)])}''')

add('aversion', '受けつけないと、両手で強く押しのける', f'''
{table(320)}
<g transform="translate(450 280)"><ellipse rx="76" ry="20" fill="#fffefd" class="o"/>
  <ellipse cy="-14" rx="44" ry="22" fill="#8f9a72" class="o"/>
  {''.join(f'<path d="M{-20+i*20} -40q-12-20 0-36" fill="none" stroke="{GRN}" stroke-width="4"/>' for i in range(2))}</g>
{person(160, 306, 1.25, 1, 'teal', 'blue', 'reach', 'short', 'sad')}
{hand(280, 240, 1)}{hand(280, 300, 1)}
<path d="M330 240h50M330 300h50" fill="none" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>''', arrow=True)

add('awkwardness', '何を言えばいいか分からず、二人とも黙りこむ', f'''
{person(180, 306, 1.2, 1, 'teal', 'blue', 'hold', 'short', 'neutral')}
{person(430, 306, 1.2, -1, 'coral', 'blue', 'hold', 'bob', 'neutral')}
<g transform="translate(305 150)"><rect x="-70" y="-40" width="140" height="80" rx="18" class="paper"/>
  <path d="M-26 38l-6 26 26-26z" class="paper"/>
  {''.join(f'<circle cx="{-26+i*26}" cy="0" r="6" fill="{MUTED}"/>' for i in range(3))}</g>
{drop(232, 190, 0.9)}{drop(380, 194, 0.9)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M110 240h-30M500 240h30"/></g>''')

add('ardour', '胸に火をともしたように、熱をこめて打ちこむ', f'''
{table(340)}
{person(230, 306, 1.3, 1, 'coral', 'blue', 'carry', 'short', 'smile')}
<g transform="translate(230 210) scale(0.42)">{flame(0, 40, 1)}</g>
{doc(430, 230, 150, 190, 4)}
{''.join(spark(x, y, 0.9) for x, y in [(120,140),(360,120)])}
{drop(300, 150, 0.9)}''')

# --- ちがい・ずれ ------------------------------------------------------------

add('anomaly', '並んだ点のなかに、ひとつだけ大きく外れた点', f'''
<path d="M60 340h480M90 360V60" fill="none" stroke="{MUTED}" stroke-width="4"/>
{''.join(f'<circle cx="{130+i*60}" cy="{280-i*14}" r="11" class="tealp o"/>' for i in range(7))}
<circle cx="370" cy="110" r="14" class="coral o"/>
{ring(370, 110, 48)}
<path d="M110 296l420-100" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>''')

add('antonym', 'ちがう二つの語が、正反対のものを指す', f'''
{word(150, 110, 4, 34, TEA)}
{word(450, 110, 5, 30, VIO)}
<path d="M266 122h68" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>
<path d="M150 160v70M450 160v70" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<circle cx="150" cy="300" r="70" class="teal o"/>
<circle cx="450" cy="300" r="22" class="teal o"/>''', arrow=True)

add('at odds with', 'かみ合うはずの歯車が、たがいに食い違う', f'''
{gear(200, 200, 70, 'teal')}
{gear(420, 220, 56, 'coral')}
<g fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round">
  <path d="M300 130l-20-24M320 300l-16 26M330 200h-24"/></g>
<path d="M200 40a70 70 0 0 1 40 20" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/>
<path d="M420 350a56 56 0 0 0 40-20" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/>''', arrow=True)

add('as opposed to', 'こちらではなく、そちらのほうを取る', f'''
{split()}
{box(150, 210, 150, 110, 32, 'gold')}
{ring(150, 200, 130, True)}
{box(450, 210, 150, 110, 32, 'coral')}
{ring(450, 200, 130)}
<path d="M300 350h-1" fill="none"/>
<path d="M240 340h120" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('at first glance', 'ちらっと見ると別のものに見えるが、よく見るとちがう', f'''
{split()}
<g transform="translate(150 200)"><path d="M-70 60l70-120 70 120z" class="teal o"/></g>
{''.join(f'<path d="M{40+i*20} {110+i*20}l30 20" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}
{ring(150, 200, 130, True)}
<g transform="translate(450 200)"><path d="M-70 60l70-120 70 120z" class="teal o"/>
  <path d="M-70 60h140" fill="none" stroke="{CRL}" stroke-width="6"/>
  <circle cx="0" cy="20" r="14" class="coral o"/></g>
{magnifier(470, 226, 70, 24)}''')

add('as a rule', 'たいていはそうなるが、まれに外れもある', f'''
{''.join(f'<g transform="translate({100+ (i%5)*100} {160+(i//5)*120})"><circle r="40" class="tealp o"/>'
         f'<path d="M-16 0l12 14 22-26" fill="none" stroke="{GRN}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>' for i in range(9))}
<g transform="translate(500 280)"><circle r="40" class="coralp o"/>
  <path d="M-14-14l28 28M14-14l-28 28" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/></g>''')

add('aside from', 'ひとまとまりの外に、これだけを別に置く', f'''
<circle cx="230" cy="210" r="150" fill="none" stroke="{TEA}" stroke-width="6" stroke-dasharray="0"/>
{''.join(f'<circle cx="{230+90*math.cos(math.radians(a)):.0f}" cy="{210+90*math.sin(math.radians(a)):.0f}" r="34" class="teal o"/>' for a in range(0, 360, 60))}
<g transform="translate(510 210)"><circle r="40" class="coral o"/></g>
{ring(510, 210, 62)}
<path d="M400 210h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('at any rate', '言い合いはひとまず置いて、とにかく次へ進む', f'''
<g opacity="0.45">
  <g transform="translate(150 130)"><rect x="-90" y="-46" width="180" height="92" rx="20" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9"/></g>
  <g transform="translate(400 120)"><rect x="-90" y="-46" width="180" height="92" rx="20" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9"/></g>
</g>
{person(150, 340, 1.15, 1, 'teal', 'blue', 'point', 'short', 'neutral')}
<path d="M230 280h180" class="a" stroke-width="6" marker-end="url(#ar)"/>
{box(500, 300, 90, 64, 20, 'coral')}''', arrow=True)

add('approximation', 'ぴったりではないが、ほぼ重なる線を引く', f'''
<path d="M60 340h480M90 360V70" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M90 300q80-140 160-100t160-90" fill="none" stroke="{TEA}" stroke-width="8"/>
<path d="M90 296L410 116" fill="none" stroke="{CRL}" stroke-width="6" stroke-dasharray="14 10"/>
<g transform="translate(490 130)" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round">
  <path d="M-40-14q20-20 40 0t40 0"/><path d="M-40 24q20-20 40 0t40 0"/></g>''')

# --- しくみ・仕事 ------------------------------------------------------------

add('an array of', 'ちがう品が、ずらりと見わたすかぎり並ぶ', f'''
{''.join(f'<path d="M40 {126+i*80}h520v10H40z" class="goldd o"/>' for i in range(3))}
{''.join(f'<g transform="translate({80+ (i%6)*88} {110+(i//6)*80})">'
         + (f'<circle r="26" class="{c} o"/>' if i % 3 == 0 else
            f'<rect x="-24" y="-24" width="48" height="48" rx="6" class="{c} o"/>' if i % 3 == 1 else
            f'<path d="M-26 22l26-46 26 46z" class="{c} o"/>')
         + '</g>' for i, c in enumerate(['teal','coral','gold','green','violet','blue',
                                          'coral','gold','teal','blue','green','violet',
                                          'gold','violet','coral','teal','blue','green']))}''')

add('analytics', 'たまった数字を、図に直して読み解く', f'''
<g transform="translate(300 180)"><rect x="-250" y="-140" width="500" height="280" rx="12" class="paper"/>
  {''.join(f'<rect x="{-220+i*44}" y="{80-h}" width="30" height="{h}" rx="4" class="teal o"/>' for i, h in enumerate([70, 120, 90, 150, 110]))}
  <path d="M20 60l50-70 50 40 60-90" fill="none" stroke="{CRL}" stroke-width="6"/>
  {''.join(f'<circle cx="{20+i*53}" cy="{60-i*33}" r="8" class="coral o"/>' for i in range(4))}
  <circle cx="150" cy="-60" r="0" fill="none"/></g>
{magnifier(430, 300, 66, 24)}
{head(120, 330, 26, 'violet', 'bun')}''')

add('appraisal', '働きぶりを段階で評価して、書きこむ', f'''
{table(330)}
{doc(230, 190, 220, 250, 0)}
{''.join(f'<g><rect x="140" y="{100+i*52}" width="110" height="12" rx="6" fill="{MUTED}"/>'
         f'{"".join(f2 for f2 in [f"<circle cx=@{278+j*30}@ cy=@{106+i*52}@ r=@10@ class=@{chr(39) if False else (chr(103)+chr(111)+chr(108)+chr(100)) if j <= i else chr(103)+chr(111)+chr(108)+chr(100)+chr(112)} o@/>".replace("@", chr(34)) for j in range(3)])}</g>' for i in range(4))}
{person(470, 306, 1.2, -1, 'teal', 'blue', 'point', 'bun', 'neutral')}
{head(90, 300, 26, 'coral', 'short')}''')

add('apprentice', '親方のそばで、同じ手わざを見て覚える', f'''
{table(330)}
<g transform="translate(300 296)"><path d="M-70 0v-40h140V0z" fill="#8d949a" class="o"/></g>
{person(190, 306, 1.25, 1, 'coral', 'blue', 'hold', 'cap', 'neutral')}
<g transform="translate(240 200) rotate(24)"><path d="M-8 0h16v70h-16z" class="goldd o"/>
  <path d="M-30-30h60v26h-60z" class="ink"/></g>
{person(430, 306, 0.95, -1, 'teal', 'blue', 'hold', 'short', 'smile')}
<g transform="translate(390 220) rotate(-24)"><path d="M-6 0h12v52h-6z" class="goldd o"/>
  <path d="M-22-22h44v20h-44z" class="ink"/></g>
<path d="M360 160h-60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('arbitration', 'あいだに立つ第三者が、話を聞いて裁定する', f'''
{table(280)}
{person(110, 306, 1.05, 1, 'coral', 'blue', 'point', 'short', 'neutral')}
{person(490, 306, 1.05, -1, 'teal', 'blue', 'point', 'bob', 'neutral')}
<g transform="translate(300 220)"><path d="M-80-70h160v140h-160z" class="paper"/>
  {''.join(f'<rect x="-58" y="{-46+i*36}" width="{116-(i%2)*40}" height="12" rx="6" fill="{MUTED}"/>' for i in range(3))}
  <circle cx="40" cy="46" r="20" fill="none" stroke="{CRL}" stroke-width="5"/></g>
{person(300, 400, 1.0, 1, 'violet', 'green', 'stand', 'bun', 'neutral')}
<path d="M190 180h50M410 180h-50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('archaeology', '層になった土を掘り、埋もれた器を掘り出す', f'''
<path d="M0 200h600v200H0z" fill="#d9c9a4"/>
<path d="M0 250h600M0 300h600M0 350h600" fill="none" stroke="#c0ab7f" stroke-width="4"/>
<g transform="translate(400 320)"><path d="M-50 0q-16-60 0-76h100q16 16 0 76z" class="corald o"/>
  <path d="M-56-76h112v-14h-112z" class="coral o"/>
  <path d="M-20-60l14 60M20-64l-8 64" fill="none" stroke="{CRLD}" stroke-width="3"/></g>
{person(170, 260, 1.05, 1, 'teal', 'blue', 'reach', 'cap', 'neutral')}
<g transform="translate(240 180) rotate(40)"><path d="M-7 0h14v70h-14z" class="goldd o"/>
  <path d="M-24-24h48v24h-48z" class="ink"/></g>
{magnifier(120, 130, 46, 20)}''')

add('auditor', '帳簿の数字を、外から一つずつ点検する', f'''
{table(330)}
{doc(230, 200, 210, 250, 0)}
{''.join(f'<g><rect x="140" y="{110+i*50}" width="100" height="12" rx="6" fill="{MUTED}"/>'
         f'<rect x="256" y="{110+i*50}" width="54" height="12" rx="6" class="teal"/></g>' for i in range(4))}
{magnifier(300, 240, 76, 20)}
<g transform="translate(470 200)"><path d="M-30 40h60v20h-60z" class="corald o"/>
  <path d="M-16-40h32v80h-32z" class="coral o"/><path d="M-30-56h60v18h-60z" class="corald o"/></g>
{head(520, 320, 26, 'violet', 'bun')}''')

add('authorisation', '判を押した許可証が出て、はじめて通れる', f'''
{table(280)}
<g transform="translate(200 200) rotate(-6)"><rect x="-90" y="-60" width="180" height="120" rx="8" class="paper"/>
  {''.join(f'<rect x="-70" y="{-40+i*30}" width="{130-(i%2)*40}" height="12" rx="6" fill="{MUTED}"/>' for i in range(3))}
  <circle cx="52" cy="34" r="26" fill="none" stroke="{CRL}" stroke-width="6"/></g>
<path d="M310 200h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(470 306)"><path d="M-90 0v-16h180v16z" class="goldd o"/>
  <path d="M-70-16v-180h20v180z" class="goldd o"/>
  <path d="M-50-180h150" fill="none" stroke="{GLDD}" stroke-width="10" transform="rotate(-44 -50 -180)"/></g>''', arrow=True)

add('austerity', 'ベルトをきつく締め、支出をぐっと切りつめる', f'''
<g transform="translate(300 190)"><path d="M-200-40h400v80h-400z" class="goldd o"/>
  <path d="M-60-56h120v112h-120z" fill="#8c6b42" class="o"/>
  <path d="M-30-56v112" fill="none" stroke="{INK}" stroke-width="4"/>
  {''.join(f'<circle cx="{60+i*40}" cy="0" r="8" fill="#6f5230"/>' for i in range(3))}</g>
<g fill="none" class="a" stroke-width="6">
  <path d="M120 300h100" marker-end="url(#ar)"/><path d="M480 300h-100" marker-end="url(#ar)"/></g>
{''.join(f'<rect x="{90+i*90}" y="{356-h}" width="46" height="{h}" rx="4" class="tealp o"/>' for i, h in enumerate([30, 24, 20, 16, 12]))}''', arrow=True)

add('attainment', '目ざした高さに、ついに手がとどく', f'''
<path d="M60 340h480" fill="none" stroke="{MUTED}" stroke-width="0"/>
{''.join(f'<path d="M120 {330-i*54}h360" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9"/>' for i in range(5))}
<path d="M120 114h360" fill="none" stroke="{CRL}" stroke-width="6"/>
{''.join(f'<rect x="{160+i*80}" y="{330-h}" width="50" height="{h}" rx="5" class="tealp o"/>' for i, h in enumerate([70, 120, 170, 216]))}
<rect x="400" y="114" width="50" height="216" rx="5" class="teal o"/>
{''.join(spark(x, y, 0.9) for x, y in [(360,80),(490,86)])}''')

# --- 医療・自然 --------------------------------------------------------------

add('antibiotic', '薬をのむと、体の中の菌が減っていく', f'''
{split()}
<g transform="translate(150 200)"><circle r="120" fill="{TONES['blue'][1]}" class="o"/>
  {''.join(germ(70*math.cos(math.radians(a)), 70*math.sin(math.radians(a)), 1.0) for a in range(0, 360, 60))}</g>
<g transform="translate(300 340)"><rect x="-44" y="-22" width="88" height="44" rx="22" fill="#fffefd" class="o"/>
  <path d="M-44 0a44 22 0 0 1 44-22v44a44 22 0 0 1-44-22z" class="coral o"/></g>
<g transform="translate(450 200)"><circle r="120" fill="{TONES['blue'][1]}" class="o"/>
  {germ(-30, 20, 0.7)}
  {''.join(f'<circle cx="{70*math.cos(math.radians(a)):.0f}" cy="{70*math.sin(math.radians(a)):.0f}" r="22" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"/>' for a in [0, 60, 180, 240, 300])}</g>
<path d="M240 130h120" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('antidote', '毒を打ち消す薬を飲んで、体がもとにもどる', f'''
{bottle(140, 300, 1.0, 'violet')}
<g transform="translate(140 230)"><circle r="26" fill="#fffefd" class="o"/>
  <path d="M-12-6h24M-6-14v22" fill="none" stroke="{VIOD}" stroke-width="4" transform="rotate(45)"/></g>
<path d="M220 200h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{bottle(330, 300, 1.0, 'green')}
<path d="M410 200h50" class="a" marker-end="url(#ar)"/>
{person(520, 306, 1.05, 1, 'teal', 'blue', 'up', 'short', 'smile')}''', arrow=True)

add('asthma', '息が細くなり、吸入器で楽にする', f'''
{person(220, 306, 1.25, 1, 'coral', 'blue', 'hold', 'short', 'sad')}
<g transform="translate(220 210)"><ellipse rx="46" ry="34" fill="none" stroke="{CRL}" stroke-width="5"/>
  <path d="M-30 0h60M-24 14h48M-24-14h48" fill="none" stroke="{CRL}" stroke-width="4"/></g>
<g transform="translate(400 250)"><path d="M-26 60v-70h52v70z" class="blue o"/>
  <path d="M-18-10v-40h36v40z" class="blued o"/>
  <path d="M-14-50h28v-16h-28z" class="teal o"/></g>
{''.join(f'<path d="M{440+i*24} {170-i*22}q16 16 0 32" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}''')

add('antler', '枝分かれした、シカの角', f'''
<g transform="translate(300 320)">
  <ellipse cx="0" cy="-30" rx="66" ry="80" fill="#b58a58" class="o"/>
  <ellipse cx="0" cy="20" rx="38" ry="30" fill="#c9a06c" class="o"/>
  <circle cx="-14" cy="16" r="5" class="ink"/><circle cx="14" cy="16" r="5" class="ink"/>
  <circle cx="-20" cy="-50" r="7" class="ink"/><circle cx="20" cy="-50" r="7" class="ink"/>
  <path d="M-52-90q-40-14-50-50M-40-120q-34-20-38-56M-34-150q-24-26-16-56M-30-160q30-26 50-14" fill="none" stroke="#8c6b42" stroke-width="9" stroke-linecap="round"/>
  <path d="M52-90q40-14 50-50M40-120q34-20 38-56M34-150q24-26 16-56M30-160q-30-26-50-14" fill="none" stroke="#8c6b42" stroke-width="9" stroke-linecap="round"/>
</g>''')

add('asteroid', '宇宙に浮かぶ、ごつごつした小さな岩', f'''
<rect width="600" height="400" fill="#2a3340"/>
{''.join(f'<circle cx="{(i*97)%580+10}" cy="{(i*61)%380+10}" r="{2+(i%3)}" fill="#fffefd" opacity="{0.5+(i%3)*0.2:.1f}"/>' for i in range(40))}
<g transform="translate(300 200) rotate(-14)">
  <path d="M-110-20q-14-60 40-80 70-26 130 16 46 32 20 82-32 60-110 50-66-8-80-68z" fill="#9aa3a8" stroke="#fffefd" stroke-width="2.5"/>
  {''.join(f'<ellipse cx="{-70+i*44}" cy="{-20+(i%3)*30}" rx="{14-(i%3)*3}" ry="{10-(i%3)*2}" fill="#7d868c"/>' for i in range(5))}</g>''')

# --- 記号・もの --------------------------------------------------------------

add('apostrophe', '語の上につく、小さなかぎ形の印', f'''
{''.join(word(x, 220, n, 34, INK) for x, n in [(180, 3), (420, 4)])}
<g transform="translate(300 190)"><path d="M-8-40q24 6 20 34-2 16-16 18 10-16 4-26-14-4-8-26z" class="coral o"/></g>
{ring(300, 180, 62)}''')

add('asterisk', '文の横につけて、注を示す星印', f'''
{doc(230, 210, 240, 280, 0)}
{''.join(f'<rect x="130" y="{120+i*46}" width="{190-(i%2)*60}" height="12" rx="6" fill="{MUTED}"/>' for i in range(4))}
<g transform="translate(340 126)" stroke="{CRL}" stroke-width="7" stroke-linecap="round" fill="none">
  {''.join(f'<path d="M0 -18v36" transform="rotate({d})"/>' for d in [0, 60, 120])}</g>
<path d="M130 300h190" fill="none" stroke="{INK}" stroke-width="3"/>
<g transform="translate(150 326)" stroke="{CRL}" stroke-width="5" stroke-linecap="round" fill="none">
  {''.join(f'<path d="M0 -12v24" transform="rotate({d})"/>' for d in [0, 60, 120])}</g>
<rect x="176" y="320" width="120" height="10" rx="5" fill="{MUTED}"/>
{ring(340, 126, 54)}''')

add('appliance', 'コンセントにつないで使う、家の中の機械', f'''
{table(340)}
<g transform="translate(140 300)"><rect x="-60" y="-110" width="120" height="110" rx="10" class="teal o"/>
  <circle cy="-56" r="36" fill="#dfe6ea" class="o"/><circle cy="-56" r="24" fill="#bcd6e6"/>
  <rect x="-46" y="-100" width="30" height="16" rx="4" class="teald o"/></g>
<g transform="translate(300 300)"><path d="M-40 0v-70h80V0z" class="coral o"/>
  <path d="M40-56q26 0 26 18t-26 18" fill="none" class="o"/>
  <path d="M-20-70v-14h40v14z" class="corald o"/></g>
<g transform="translate(450 300)"><rect x="-56" y="-70" width="112" height="70" rx="8" class="gold o"/>
  <rect x="-30" y="-84" width="16" height="20" rx="4" class="goldd o"/>
  <rect x="14" y="-84" width="16" height="20" rx="4" class="goldd o"/></g>
<path d="M508 300q40 20 40 60" fill="none" stroke="{INK}" stroke-width="5"/>
<g transform="translate(552 366)"><rect x="-16" y="-14" width="32" height="28" rx="5" class="ink"/></g>''')

add('autobiography', '自分のことを、自分で書いた本', f'''
{table(340)}
{person(160, 306, 1.2, 1, 'teal', 'blue', 'reach', 'bun', 'smile')}
<g transform="translate(240 200) rotate(30)"><path d="M-7-80h14v110l-7 18-7-18z" class="coral o"/></g>
<g transform="translate(430 250)"><path d="M-90-120h180v240h-180z" class="violet o"/>
  <path d="M-90-120h20v240h-20z" class="violetd o"/>
  <circle cx="20" cy="-40" r="42" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="{HAIRS['bun']}" transform="translate(20 148) scale(1.7)" fill="{HAIR}"/>
  <circle cx="6" cy="-44" r="4" class="ink"/><circle cx="34" cy="-44" r="4" class="ink"/>
  <path d="M8-28q12 10 24 0" fill="none" stroke="{INK}" stroke-width="3"/>
  <rect x="-40" y="40" width="120" height="14" rx="7" fill="#fffefd" opacity="0.85"/></g>
<path d="M310 200h40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('autopilot', '手を離しても、機械が自分で操縦する', f'''
<g transform="translate(300 220)"><rect x="-250" y="-140" width="500" height="180" rx="14" class="teald o"/>
  <path d="M-230-120h460v100h-460z" fill="#bcd6e6" class="o"/>
  {cloud(-120, -60, 0.7, 'blue')}{cloud(120, -70, 0.8, 'blue')}
  <rect x="-250" y="40" width="500" height="80" rx="8" fill="#dfe6ea" class="o"/>
  {''.join(f'<circle cx="{-190+i*70}" cy="80" r="14" class="{c} o"/>' for i, c in enumerate(['coral','gold','green','teal','violet','blue']))}
  <g transform="translate(200 80)"><rect x="-40" y="-18" width="80" height="36" rx="18" class="green o"/>
    <circle cx="20" cy="0" r="14" fill="#fffefd" class="o"/></g></g>
<g transform="translate(300 330)"><circle r="56" fill="none" stroke="{INK}" stroke-width="14"/>
  <path d="M-56 0h112M0 0v56" fill="none" stroke="{INK}" stroke-width="12"/></g>
{hand(150, 340, 1)}{hand(450, 340, -1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"><path d="M196 340h44M404 340h-44"/></g>''')

# --- 動き・状況 --------------------------------------------------------------

add('ascent', '気球がゆっくりと空へのぼっていく', f'''
{cloud(120, 120, 1.2, 'blue')}{cloud(470, 90, 1.4, 'blue')}
<g transform="translate(300 210)"><path d="M0-110q76 0 76 76 0 44-76 90-76-46-76-90 0-76 76-76z" class="coral o"/>
  <path d="M-26 46q26 20 52 0l-8 30h-36z" class="goldd o"/>
  <path d="M0-110v146M-42-96q0 80 42 132M42-96q0 80-42 132" fill="none" stroke="{CRLD}" stroke-width="3"/></g>
<path d="M300 390v-60" class="a" stroke-width="6" marker-end="url(#ar)"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M180 380h240"/></g>''', arrow=True)

add('avoidance', '正面から行かず、まわり道でよける', f'''
<g transform="translate(300 210)"><circle r="70" fill="#b9c1c6" class="o"/></g>
<path d="M60 210h140" fill="none" stroke="{TEA}" stroke-width="8"/>
<path d="M200 210q100-160 200 0" fill="none" stroke="{TEA}" stroke-width="8" stroke-dasharray="0"/>
<path d="M400 210h140" fill="none" stroke="{TEA}" stroke-width="8" marker-end="url(#ar)"/>
<path d="M200 210h200" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{person(90, 320, 0.9, 1, 'coral', 'blue', 'walk', 'short', 'neutral')}''', arrow=True)

add('at all costs', 'いくつ手放しても、必ずそこへたどりつく', f'''
<path d="M40 340q140-20 280-10t240 6" fill="none" stroke="{GLDD}" stroke-width="8" stroke-dasharray="18 14"/>
{''.join(f'<g transform="translate({120+i*90} 300) rotate({-20+i*18})">{box(0, 0, 56, 40, 12, "gold")}</g>' for i in range(3))}
{person(420, 340, 1.2, 1, 'coral', 'blue', 'walk', 'cap', 'neutral', 'walk')}
<g transform="translate(540 340)"><path d="M0 0v-140" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M0-140h-90l22 30-22 30h90z" class="coral o"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M320 200h-40M300 250h-50"/></g>''')

add('at stake', 'ここで負けたら失うものが、まん中に積んである', f'''
{table(320)}
{''.join(coin(300 + (i%3-1)*44, 280 - (i//3)*22, 24) for i in range(6))}
{ring(300, 258, 96)}
{person(100, 306, 1.0, 1, 'teal', 'blue', 'reach', 'short', 'neutral')}
{person(500, 306, 1.0, -1, 'coral', 'blue', 'reach', 'bob', 'neutral')}
{drop(150, 190, 0.9)}{drop(456, 194, 0.9)}''')

add('at the expense of', '片方をふやすと、もう片方がへる', f'''
<g transform="translate(300 240)"><path d="M-30 60L0 0l30 60z" class="teald o"/>
  <path d="M-220-14h440v26h-440z" class="teal o" transform="rotate(-14)"/></g>
{''.join(f'<rect x="{80+ (i%2)*40}" y="{130-(i//2)*36}" width="70" height="30" rx="5" class="gold o"/>' for i in range(4))}
<rect x="440" y="290" width="70" height="30" rx="5" class="goldp o"/>
<path d="M120 60v-40" class="a" stroke-width="5" marker-end="url(#ar)"/>
<path d="M480 350v30" class="a" stroke-width="5" marker-end="url(#ar)"/>''', arrow=True)

add('at the mercy of', '大きな手のなかで、なすすべもない', f'''
<g transform="translate(300 260) scale(2.6 2.0)">{hand(0, 0, 1)}</g>
{person(310, 236, 0.62, 1, 'coral', 'blue', 'up', 'short', 'sad')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M240 110q16-20 0-40M380 110q-16-20 0-40"/></g>''')

add('armistice', '双方が武器を下ろし、白い旗を立てる', f'''
{person(120, 306, 1.15, 1, 'teal', 'blue', 'stand', 'cap', 'neutral')}
{person(480, 306, 1.15, -1, 'coral', 'blue', 'stand', 'cap', 'neutral')}
<g transform="translate(190 320) rotate(76)"><path d="M-8 0h16v130h-16z" class="goldd o"/></g>
<g transform="translate(410 320) rotate(-76)"><path d="M-8 0h16v130h-16z" class="goldd o"/></g>
<g transform="translate(300 306)"><path d="M0 0v-200" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M0-200h110l-26 34 26 34H0z" fill="#fffefd" class="o"/></g>
{''.join(f'<path d="M{200+i*100} 120q26-16 0-32" fill="none" stroke="{MUTED}" stroke-width="0"/>' for i in range(0))}''')

add('anticipation', '包みを前に、開ける前からわくわくして待つ', f'''
{table(320)}
<g transform="translate(390 260)">{box(0, 0, 130, 96, 28, 'coral')}
  <path d="M-65-48h130M0-96v144" fill="none" stroke="{GLD}" stroke-width="10"/>
  <path d="M0-100q-30-30-2-40 16-6 12 22 12-26 26-16 20 14-14 34z" class="gold o"/></g>
{person(150, 306, 1.2, 1, 'teal', 'blue', 'reach', 'bob', 'smile')}
{''.join(spark(x, y, 0.9) for x, y in [(230,120),(300,90),(500,110)])}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"><path d="M226 200h60"/></g>''')

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
