# -*- coding: utf-8 -*-
"""第144回。dis-/re- の動詞と、判断・態度をあらわす形容詞。"""
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

def spark(x, y, s=1, cls='gold'):
    return (f'<path d="M{x} {y-16*s}l{5*s} {11*s} {11*s} {5*s}-{11*s} {5*s}-{5*s} {11*s}'
            f'-{5*s}-{11*s}-{11*s}-{5*s} {11*s}-{5*s}z" class="{cls} o"/>')

def ring(x, y, r=64, dash=False, cls='coral'):
    d = ' stroke-dasharray="11 10"' if dash else ''
    c = MUTED if dash else TONES[cls][0]
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{c}" stroke-width="4"{d}/>'

def bubble(x, y, w=150, h=92, f=1, inner=''):
    return (f'<g transform="translate({x} {y})"><path d="M{-w/2} {-h/2}h{w}v{h}h{-w/2*f-30*f if False else 0}z" fill="none"/>'
            f'<rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="18" class="paper"/>'
            f'<path d="M{-18*f} {h/2}l{-6*f} 26 {34*f}-26z" class="paper"/>{inner}</g>')

def eye(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-34 0q34-26 68 0-34 26-68 0z" fill="#fffefd" class="o"/>'
            f'<circle r="11" class="ink"/></g>')

def gear(x, y, r=44, cls='teal'):
    teeth = ''.join(f'<rect x="-8" y="{-r-14}" width="16" height="18" rx="3" transform="rotate({d})"/>' for d in range(0, 360, 45))
    return (f'<g transform="translate({x} {y})"><g class="{cls} o">{teeth}</g>'
            f'<circle r="{r}" class="{cls} o"/><circle r="{r*0.34:.0f}" fill="#fffdf6" class="o"/></g>')

def jug(x, y, level, mark=0.72):
    """目盛り線 mark に対して level まで入った容器。suffice / deficient で使う。"""
    h, w = 150, 108
    fh = h * level
    return (f'<g transform="translate({x} {y})">'
            f'<path d="M{-w/2} {-h}h{w}v{h}h{-w}z" fill="#fffefd" class="o"/>'
            f'<path d="M{-w/2+5} {-fh}h{w-10}v{fh-5}h{-w+10}z" class="bluep"/>'
            f'<path d="M{-w/2} {-h}h{w}v{h}h{-w}z" fill="none" class="o"/>'
            f'<path d="M{-w/2-22} {-h*mark}h{w+44}" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="10 8"/></g>')

# --- 気持ち・評価 -----------------------------------------------------------

add('fantastic', 'きらめきに囲まれて両手を上げて喜ぶ人', f'''
{sun(500, 80, 42)}
{''.join(spark(x, y, s) for x, y, s in [(150,90,1.5),(230,50,1),(370,70,1.2),(120,180,1),(430,150,1.3)])}
{person(280, 306, 1.25, 1, 'coral', 'blue', 'up', 'short', 'smile')}''')

add('hardworking', '汗をかきながら荷物を運び、積み上がった箱', f'''
{person(200, 306, 1.2, 1, 'teal', 'blue', 'carry', 'cap', 'neutral')}
<g transform="translate(214 210)"><path d="M-44-30h88v58h-88z" class="gold o"/><path d="M-44-30h88v14h-88z" class="goldd o"/></g>
{drop(150, 200, 1.1)}{drop(132, 224, 0.9)}
{box(430, 280, 76, 44, 16, 'gold')}{box(430, 232, 76, 44, 16, 'gold')}{box(430, 184, 76, 44, 16, 'gold')}
{sun(90, 74, 34)}
<path d="M520 74a30 30 0 1 1-24-30 24 24 0 0 0 24 30z" class="goldp o"/>''')

add('avert', 'まぶしい閃光から顔と体をそむける人', f'''
<g transform="translate(490 170)">
  <g class="golds">{''.join(f'<path d="M0 -60v-34" transform="rotate({d})"/>' for d in range(0, 360, 30))}</g>
  <circle r="52" class="goldp o"/>
</g>
{person(210, 306, 1.25, -1, 'coral', 'blue', 'reach', 'short', 'sad')}
<path d="M300 120q-46-30-96-18" fill="none" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('deafen', '大音量に耳をふさぐ人。耳の先の音は届かない', f'''
<g transform="translate(120 200)"><path d="M-34-46h34l52-42v176l-52-42h-34z" class="teal o"/></g>
<g class="corals">{''.join(f'<path d="M170 200a{r} {r} 0 0 1 0 0" />' for r in [1])}</g>
{''.join(f'<path d="M180 {200-38-i*22}q{34+i*18} {38+i*22} 0 {(38+i*22)*2}" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>' for i in range(3))}
{person(430, 306, 1.25, -1, 'blue', 'teal', 'hold', 'short', 'sad')}
<path d="M392 190q-22-8-22-26M468 190q22-8 22-26" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('debit', '口座の残高から自動で引き落とされて店に払われる', f'''
<g transform="translate(150 170)"><path d="M-84-56h168v112h-168z" fill="#fffefd" class="o"/>
  <path d="M-84-56h168v28h-168z" class="teal o"/>
  <rect x="-64" y="-14" width="128" height="16" rx="8" fill="{MUTED}"/>
  <rect x="-64" y="16" width="86" height="16" rx="8" fill="{MUTED}"/></g>
<path d="M254 170h96" class="a" marker-end="url(#ar)"/>
{coin(300, 118, 22)}
<g transform="translate(460 180)"><path d="M-70 60v-96h140v96z" fill="#fffefd" class="o"/>
  <path d="M-82-36h164l-22-38h-120z" class="coral o"/>
  <path d="M-24 60v-56h48v56z" class="corald o"/></g>
<path d="M150 240v54" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('discern', 'よく似た二つの形の違いを虫めがねで見分ける', f'''
<g transform="translate(180 170)"><path d="M-52 46l52-92 52 92z" class="teal o"/></g>
<g transform="translate(360 170)"><path d="M-52 46l52-92 52 92z" class="teal o"/>
  <path d="M-52 46h104" fill="none" stroke="{CRL}" stroke-width="6"/>
  <circle cx="0" cy="10" r="9" class="coral o"/></g>
<g transform="translate(392 196) rotate(24)"><circle r="62" fill="#ffffff" opacity="0.45" stroke="{INK}" stroke-width="6"/>
  <path d="M0 62v46" stroke="{INK}" stroke-width="16" stroke-linecap="round"/></g>
{head(120, 300, 22, 'coral', 'bob')}''')

add('discontinue', 'つくり続けていた品を、途中でやめて出荷を止める', f'''
{split()}
<g transform="translate(150 200)">
  <path d="M-96 60h192v14h-192z" class="teald o"/>
  <path d="M-96-56h74v116h-74z" class="teal o"/>
  {box(24, 40, 56, 34, 12, 'gold')}{box(88, 40, 56, 34, 12, 'gold')}
  <path d="M-8 0h60" fill="none" stroke="{INK}" stroke-width="4" marker-end="url(#ar)"/>
</g>
<g transform="translate(450 200)">
  <path d="M-96 60h192v14h-192z" class="teald o"/>
  <path d="M-96-56h74v116h-74z" class="teal o"/>
  <path d="M-16-56h112v90h-112z" fill="#e6e9ea" class="o"/>
  {''.join(f'<path d="M-16 {-46+i*18}h112" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(5))}
</g>''', arrow=True)

add('disembark', '船から桟橋へタラップを降りる人たち', f'''
<path d="M0 306h600v94H0z" fill="{BLUP}"/>
<g transform="translate(160 250)">
  <path d="M-130 56q10 40 60 40h150q46 0 58-40z" class="coral o"/>
  <path d="M-110-10h230v66h-230z" fill="#fffefd" class="o"/>
  {''.join(f'<circle cx="{-80+i*46}" cy="22" r="13" class="bluep o"/>' for i in range(5))}
</g>
<path d="M270 300l120 -10v18l-120 10z" class="gold o"/>
<path d="M400 288h180v20H400z" class="goldd o"/>
{head(310, 268, 18, 'teal', 'short')}
{head(376, 258, 18, 'violet', 'bob')}
{person(500, 306, 1.05, -1, 'green', 'blue', 'walk', 'short', 'smile')}''')

add('disengage', 'かみ合っていた歯車の片方が離れていく', f'''
{gear(210, 190, 66, 'teal')}
{gear(400, 190, 50, 'coral')}
<path d="M340 190h-40" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>
<path d="M470 190h90" class="a" marker-end="url(#ar)"/>
<path d="M300 300q80-24 160 0" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>''', arrow=True)

add('disgrace', '冠が落ち、うつむく人を周りが指さす', f'''
{person(300, 306, 1.3, 1, 'violet', 'blue', 'stand', 'short', 'sad')}
<g transform="translate(374 150) rotate(28)"><path d="M-38 18l-8-46 22 16 14-28 14 28 22-16-8 46z" class="gold o"/></g>
{head(110, 290, 24, 'coral', 'bob')}
{head(500, 290, 24, 'teal', 'short')}
<path d="M148 268l70 -14M462 268l-70 -14" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('dwell', '同じつまずきを頭の中でぐるぐる思い返す', f'''
{sit(200, 306, 1.15, 1, 'teal', 'blue', 'short', 'sad', 'lap')}
{chair(214, 306, 1.05, 'gold', -1)}
<circle cx="300" cy="240" r="9" fill="#fffefd" class="o"/>
<circle cx="322" cy="212" r="13" fill="#fffefd" class="o"/>
<g transform="translate(430 140)">
  <ellipse rx="128" ry="86" fill="#fffefd" class="o"/>
  <path d="M-70 26q22-56 62-8" fill="none" stroke="{MUTED}" stroke-width="5"/>
  <path d="M-8 18l30 20" fill="none" stroke="{CRL}" stroke-width="5"/>
  {head(2, 4, 18, 'coral', 'short')}
  <path d="M-84-38a92 62 0 1 1 6 66" fill="none" class="a" marker-end="url(#ar)"/>
</g>''', arrow=True)

add('falter', 'まっすぐだった足あとが乱れ、歩みがよろめく', f'''
{''.join(f'<ellipse cx="{70+i*54}" cy="{330 if i%2 else 350}" rx="17" ry="9" class="ink"/>' for i in range(4))}
{''.join(f'<ellipse cx="{298+i*54}" cy="{318+(i%2)*44}" rx="17" ry="9" class="ink" transform="rotate({-24+i*22} {298+i*54} {318+(i%2)*44})"/>' for i in range(3))}
{person(430, 306, 1.25, 1, 'coral', 'blue', 'reach', 'short', 'sad', 'walk')}
<path d="M330 150q16-18 0-36M540 150q-16-18 0-36" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"/>''')

add('forestall', '倒れる前につっかい棒をあてて食い止める', f'''
<g transform="translate(200 306) rotate(-12)">{tower(0, 0, 0.9, 'teal', 4)}</g>
<g opacity="0.4"><g transform="translate(200 306) rotate(-58)">{tower(0, 0, 0.9, 'teal', 4)}</g></g>
<path d="M262 300l58-96" fill="none" stroke="{GLDD}" stroke-width="16" stroke-linecap="round"/>
{person(430, 306, 1.1, -1, 'coral', 'blue', 'reach', 'short', 'neutral')}''')

add('gratify', '望んでいたものを手渡され、満足のめもりが満ちる', f'''
{person(150, 306, 1.15, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{box(280, 250, 66, 52, 16, 'coral')}
<path d="M330 250h56" class="a" marker-end="url(#ar)"/>
{person(470, 306, 1.15, -1, 'violet', 'green', 'reach', 'bob', 'smile')}
<g transform="translate(470 120)"><rect x="-76" y="-18" width="152" height="36" rx="18" fill="#fffefd" class="o"/>
  <rect x="-72" y="-14" width="144" height="28" rx="14" class="green"/></g>''', arrow=True)

add('noticeable', '同じ形が並ぶ中で一つだけ目立って浮き上がる', f'''
{''.join(f'<rect x="{68+i*88}" y="200" width="60" height="86" rx="10" fill="#d8dfe2" class="o"/>' for i in range(6) if i != 3)}
<g transform="translate(362 220)"><rect x="-34" y="-34" width="68" height="100" rx="12" class="coral o"/></g>
<g class="corals">{''.join(f'<path d="M362 140v-26" transform="rotate({d} 362 186)"/>' for d in [-40, -20, 0, 20, 40])}</g>
{head(120, 128, 24, 'teal', 'short')}
<path d="M160 126l150 40" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('procure', '遠い道のりをたどって、ようやく品を手に入れて戻る', f'''
<path d="M40 330q90-120 190-90t130-110" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="14 12"/>
<g transform="translate(430 130)"><path d="M-70 74l70-118 70 118z" fill="#c3cbd1" class="o"/></g>
{person(150, 320, 1.2, -1, 'coral', 'blue', 'carry', 'cap', 'smile', 'walk')}
<g transform="translate(164 236)"><path d="M-40-26h80v52h-80z" class="gold o"/><path d="M-40-26h80v12h-80z" class="goldd o"/></g>''')

add('reclaim', 'あずけていた自分のかばんを受け取って取り戻す', f'''
{table(240)}
<g transform="translate(190 210)"><path d="M-44 30v-52h88v52z" class="violet o"/><path d="M-18-22v-16h36v16" fill="none" class="a"/></g>
<g transform="translate(300 214)"><path d="M-34 26v-44h68v44z" class="teal o"/></g>
<path d="M250 150q90-56 176 0" fill="none" class="a" marker-end="url(#ar)"/>
{person(470, 306, 1.2, -1, 'coral', 'blue', 'reach', 'bob', 'smile')}''', arrow=True)

add('redeem', '引換券を渡して品物と交換してもらう', f'''
{table(250)}
{person(130, 306, 1.15, 1, 'teal', 'blue', 'give', 'short', 'smile')}
<g transform="translate(240 196) rotate(-8)"><path d="M-46-26h92v52h-92z" class="gold o"/>
  <path d="M-24-26v52M2-26v52" fill="none" stroke="{GLDD}" stroke-width="3" stroke-dasharray="6 6"/></g>
<path d="M280 150h84" class="a" marker-end="url(#ar)"/>
<path d="M364 240h-84" class="a" marker-end="url(#ar)"/>
{box(410, 210, 70, 54, 16, 'coral')}
{head(510, 240, 24, 'violet', 'bun')}''', arrow=True)

add('reignite', '消えたろうそくにもう一度火をつける', f'''
{split()}
{table(300)}
<g transform="translate(160 300)"><path d="M-22-100h44v100h-44z" fill="#fffefd" class="o"/>
  <path d="M0-100v-16" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-4-124q-14-16 4-28" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M6-138q16-14 2-30" fill="none" stroke="{MUTED}" stroke-width="4"/></g>
<path d="M232 190h124" class="a" marker-end="url(#ar)"/>
<g transform="translate(440 300)"><path d="M-22-100h44v100h-44z" fill="#fffefd" class="o"/>
  <path d="M0-100v-10" fill="none" stroke="{INK}" stroke-width="4"/></g>
<g transform="translate(422 130) scale(0.5)">{flame(0, 0, 1)}</g>''', arrow=True)

add('relive', '写真を見て、そのときの場面をもう一度たどる', f'''
{sit(160, 306, 1.1, 1, 'teal', 'blue', 'bob', 'smile', 'lap')}
{chair(174, 306, 1.0, 'gold', -1)}
<g transform="translate(228 224) rotate(-10)"><path d="M-36-46h72v92h-72z" fill="#fffefd" class="o"/>
  <path d="M-30-40h60v58h-60z" class="bluep o"/><circle cx="8" cy="-16" r="10" class="gold o"/></g>
<circle cx="300" cy="180" r="9" fill="#fffefd" class="o"/>
<circle cx="322" cy="152" r="13" fill="#fffefd" class="o"/>
<g transform="translate(450 150)"><ellipse rx="122" ry="88" fill="#fffefd" class="o"/>
  {sun(-56, -34, 26)}{tree(56, 44, 0.7)}
  {person(-24, 46, 0.42, 1, 'coral', 'blue', 'up', 'bob', 'smile')}</g>''')

add('slander', 'その場にいない人について、口で悪いうわさを流す', f'''
{person(140, 306, 1.15, 1, 'coral', 'blue', 'point', 'short', 'neutral')}
<g transform="translate(320 150)"><rect x="-96" y="-56" width="192" height="112" rx="22" class="paper"/>
  <path d="M-84 46l-30 34 22-34z" class="paper"/>
  <ellipse cx="-24" cy="-8" rx="34" ry="24" fill="{INK}" opacity="0.75"/>
  <ellipse cx="34" cy="14" rx="20" ry="14" fill="{INK}" opacity="0.55"/></g>
<g transform="translate(500 250)"><rect x="-52" y="-64" width="104" height="128" rx="8" fill="#fffefd" class="o"/>
  {head(0, -8, 24, 'teal', 'bob')}
  <path d="M-40 56h80" fill="none" stroke="{MUTED}" stroke-width="4"/></g>
<path d="M418 140q46-14 62 34" fill="none" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('suffice', '必要な線にちょうど届くだけ入っている', f'''
{jug(300, 320, 0.72)}
<path d="M96 212h74" class="a" marker-end="url(#ar)"/>
{head(500, 250, 26, 'green', 'short')}''', arrow=True)

add('deficient', '必要な線にとどかず足りていない', f'''
{jug(300, 320, 0.36)}
<path d="M300 232v-56" fill="none" stroke="{CRL}" stroke-width="4" marker-end="url(#ar)"/>
<path d="M96 212h74" class="a" marker-end="url(#ar)"/>
{head(500, 250, 26, 'coral', 'short')}''', arrow=True)

add('unavailable', '棚のその品だけが切れていて手に入らない', f'''
{table(300)}
{''.join(box(100 + i*118, 268, 76, 58, 18, 'gold') for i in range(2))}
<g transform="translate(342 262)"><path d="M-42-34h84v68h-84z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9"/></g>
{box(482, 268, 76, 58, 18, 'gold')}
{hand(342, 150, 1)}
<path d="M342 190v34" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('astute', 'うまい話の裏に隠れた仕掛けを見抜く', f'''
{box(200, 200, 120, 88, 26, 'gold')}
{''.join(spark(x, y, 0.8) for x, y in [(130,110),(272,104)])}
<path d="M200 246q-2 44 40 44 30 0 30-26" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/>
<g transform="translate(400 250) rotate(-20)"><circle r="56" fill="#ffffff" opacity="0.45" stroke="{INK}" stroke-width="6"/>
  <path d="M0 56v42" stroke="{INK}" stroke-width="15" stroke-linecap="round"/></g>
{head(500, 130, 26, 'teal', 'short')}''')

add('believable', '大げさな話と、ありそうな話の対比', f'''
{split()}
{head(74, 300, 22, 'coral', 'short')}
<g transform="translate(190 170)"><rect x="-96" y="-70" width="192" height="140" rx="20" class="paper"/>
  <path d="M-90 50q60-52 122-8 26 20-10 34-70 8-112-26z" class="bluep o"/>
  <circle cx="-52" cy="52" r="5" class="ink"/></g>
{ring(190, 170, 106, True)}
{head(374, 300, 22, 'teal', 'bob')}
<g transform="translate(452 170)"><rect x="-96" y="-70" width="192" height="140" rx="20" class="paper"/>
  <path d="M-30 22q34-30 70-6 14 12-6 20-40 6-64-14z" class="bluep o"/>
  <circle cx="-12" cy="24" r="4" class="ink"/></g>
{ring(452, 170, 106)}''')

add('course', '前菜・主菜・デザートと順に出てくる一皿ずつ', f'''
{table(300)}
{''.join(f'<g transform="translate({120+i*180} 268)"><ellipse rx="66" ry="20" fill="#fffefd" class="o"/>'
         f'<ellipse rx="46" ry="12" fill="none" stroke="{MUTED}" stroke-width="2.5"/></g>' for i in range(3))}
<ellipse cx="120" cy="258" rx="30" ry="14" class="greenp o"/>
<path d="M272 250q28-24 56 0-6 20-28 20t-28-20z" class="coral o"/>
<path d="M460 236q30 0 30 22h-60q0-22 30-22z" class="goldp o"/>
<circle cx="460" cy="230" r="8" class="coral o"/>
<path d="M186 180h48M366 180h48" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('discontented', '出されたものに納得できず腕を組んでふくれる', f'''
{table(290)}
<g transform="translate(420 258)"><ellipse rx="62" ry="19" fill="#fffefd" class="o"/>
  <circle cx="0" cy="-6" r="10" class="greenp o"/></g>
{sit(230, 306, 1.2, 1, 'coral', 'blue', 'short', 'sad', 'lap')}
{chair(244, 306, 1.05, 'gold', -1)}
<path d="M196 216h68" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
<path d="M196 232h68" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
<path d="M180 130q14-16 0-32M280 130q-14-16 0-32" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"/>''')

add('discreet', '言いふらす人と、口をつぐんで守る人の対比', f'''
{split()}
{person(150, 320, 1.05, 1, 'coral', 'blue', 'up', 'short', 'neutral')}
{''.join(f'<path d="M196 {182-i*20}q{22+i*14} {22+i*16} 0 {(22+i*16)*2}" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round"/>' for i in range(3))}
{head(258, 300, 18, 'teal', 'bob')}
{ring(150, 200, 108, True)}
{person(450, 320, 1.05, 1, 'teal', 'blue', 'hold', 'bob', 'neutral')}
<path d="M440 208h26" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
<g transform="translate(516 216)"><rect x="-20" y="-14" width="40" height="34" rx="6" class="gold o"/>
  <path d="M-11-14v-12a11 11 0 0 1 22 0v12" fill="none" class="a"/></g>
{ring(450, 200, 108)}''')

add('disparate', 'そろった仲間と、まるで種類の違う寄せ集めの対比', f'''
{split()}
{''.join(f'<circle cx="{110+ (i%2)*80}" cy="{150+(i//2)*90}" r="34" class="teal o"/>' for i in range(4))}
{ring(150, 195, 112, True)}
<circle cx="380" cy="140" r="32" class="coral o"/>
<path d="M448 106h68v68h-68z" class="gold o"/>
<path d="M382 292l-38-64h76z" class="green o"/>
<path d="M446 232h74v58h-74z" class="violetp o" transform="rotate(-14 483 261)"/>
{ring(452, 198, 112)}''')

add('elusive', 'つかもうとした魚が手からするりと逃げる', f'''
<path d="M0 306h600v94H0z" fill="{BLUP}"/>
{hand(180, 220, 1)}
{hand(320, 234, -1)}
<g transform="translate(430 180) rotate(-14)">
  <path d="M-70 0q40-46 100-14 22 12 0 26-60 32-100-12z" class="teal o"/>
  <path d="M30 12l44-26v52z" class="teal o"/>
  <circle cx="-40" cy="-6" r="5" class="ink"/></g>
{''.join(f'<path d="M{250+i*22} {206+i*10}q10-14 20 0" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}''')

add('fictional', '本の中から現れる、実在しない生きもの', f'''
{table(320)}
<g transform="translate(280 300)"><path d="M-110 0l6-70h104v70z" fill="#fffefd" class="o"/>
  <path d="M110 0l-6-70H0v70z" fill="#fffefd" class="o"/>
  <path d="M-104-70h208" fill="none" stroke="{MUTED}" stroke-width="3"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9">
  <path d="M250 226q-30-56 20-88 52-32 96 12 30 30-4 62"/>
  <path d="M366 212q40-24 62 8-34 22-58 6"/>
  <path d="M282 150l-18-34 42 14M330 138l12-38 24 32"/>
</g>
<circle cx="322" cy="176" r="5" class="ink"/>''')

add('glaring', '誰の目にもすぐ分かるほど大きな誤り', f'''
{doc(250, 180, 200, 250, 5)}
<g transform="translate(300 200)">{cross(0, 0, 2.2)}</g>
<g class="corals">{''.join(f'<path d="M300 68v-26" transform="rotate({d} 300 200)"/>' for d in range(0, 360, 45))}</g>
{head(500, 240, 26, 'teal', 'short')}
{head(506, 320, 22, 'violet', 'bob')}
<path d="M462 236l-88-20" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('hysterical', '感情が抑えられず、涙を飛ばして取り乱す', f'''
{person(300, 306, 1.35, 1, 'coral', 'blue', 'up', 'short', 'sad')}
{''.join(drop(x, y, 1.1) for x, y in [(240,140),(360,146),(226,186),(376,190)])}
<g fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round">
  <path d="M150 130q16-20 0-40M450 130q-16-20 0-40"/>
  <path d="M186 90q18-14 6-38M414 90q-18-14-6-38"/>
</g>''')

add('incidental', '主なものにくっついてくる、ついでの小さなもの', f'''
{box(220, 220, 160, 130, 34, 'teal')}
{box(430, 268, 66, 52, 16, 'gold')}
<path d="M310 268h56" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{ring(430, 252, 78)}''')

add('keep-an-eye-on', 'なべから目を離さずに見張る', f'''
{table(300)}
<g transform="translate(430 268)"><path d="M-56 0v-48h112V0z" class="teal o"/>
  <path d="M-64-48h128" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <path d="M56-36h28" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <path d="M-20-60q-12-18 4-32M20-60q-12-18 4-32" fill="none" stroke="{MUTED}" stroke-width="4"/></g>
{head(140, 250, 30, 'coral', 'bob')}
{eye(140, 140, 1.1)}
<path d="M186 160l190 62" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>''')

add('loyal-to', 'みんなが去ってもそばを離れない犬', f'''
{person(400, 306, 1.25, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
<g transform="translate(300 300) scale(0.42)">{beast(0, 0, 1, '#8a6a48', -1)}</g>
<path d="M266 262q-24-22-10-46" fill="none" stroke="#8a6a48" stroke-width="9" stroke-linecap="round"/>
<g opacity="0.35">{head(110, 250, 22, 'violet', 'bob')}{head(60, 290, 20, 'coral', 'short')}</g>
<path d="M150 200l-70-30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('methodical', '手当たり次第と、手順どおりに並べるやり方の対比', f'''
{split()}
{''.join(f'<rect x="{-30}" y="{-22}" width="60" height="44" rx="8" class="gold o" transform="translate({100+(i%3)*66} {150+(i//3)*80}) rotate({-40+i*23})"/>' for i in range(6))}
{ring(160, 200, 118, True)}
{''.join(f'<rect x="{354+(i%3)*70}" y="{130+(i//3)*76}" width="60" height="44" rx="8" class="gold o"/>' for i in range(6))}
{''.join(f'<circle cx="{384+(i%3)*70}" cy="{152+(i//3)*76}" r="12" class="goldp o"/>' for i in range(6))}
{ring(454, 190, 122)}''')

add('no-wonder', '水やりを忘れた空のじょうろを見て、しおれた理由に気づく', f'''
{table(310)}
<g transform="translate(160 276)"><path d="M-30 0v-40h60v40z" class="goldd o"/>
  <path d="M-8-40q-30-6-34-46 26 6 34 30 8-30 34-38-2 46-34 54z" class="greenp o"/></g>
<g transform="translate(400 262) rotate(-118)"><path d="M-40 22v-52h74v52z" class="teal o"/>
  <path d="M34-22l44-20v46z" class="teal o"/>
  <path d="M-40 0q-26 0-26-22" fill="none" stroke="{TEAD}" stroke-width="9"/></g>
<path d="M330 200q-70-40-140-10" fill="none" class="a" marker-end="url(#ar)"/>
<g transform="translate(510 120)"><circle r="30" class="goldp o"/>
  <path d="M-12 30h24" fill="none" class="a"/>
  <g class="golds"><path d="M0-46v-18"/><path d="M34-34l14-14"/><path d="M-34-34l-14-14"/></g></g>''', arrow=True)

add('rhetorical', 'そのままの言い方と、飾り立てた言い回しの対比', f'''
{split()}
<g transform="translate(160 180)"><rect x="-104" y="-64" width="208" height="128" rx="20" class="paper"/>
  <path d="M-70 56l-14 30 40-30z" class="paper"/>
  {word(0, -18, 5, 30)}{word(-16, 24, 4, 30)}</g>
{ring(160, 190, 122, True)}
<g transform="translate(452 180)"><path d="M-104-64h208v128h-208z" fill="none"/>
  <rect x="-104" y="-64" width="208" height="128" rx="20" class="paper"/>
  <path d="M-70 56l-14 30 40-30z" class="paper"/>
  <path d="M-80-22q30-34 60 0t60 0" fill="none" stroke="{TEA}" stroke-width="6" stroke-linecap="round"/>
  <path d="M-80 24q30-34 60 0t60 0" fill="none" stroke="{TEA}" stroke-width="6" stroke-linecap="round"/>
  {spark(-60, 2, 0.7)}{spark(66, 40, 0.7)}</g>
{ring(452, 190, 122)}''')

add('stylistic', '同じ中身を、書きぶりだけ変えて並べる', f'''
{doc(150, 190, 190, 240, 0)}
{''.join(word(150, 130 + i*46, 5, 28) for i in range(4))}
{doc(450, 190, 190, 240, 0)}
{''.join(f'<g transform="rotate(-8 450 {130+i*46})">{word(450, 130 + i*46, 5, 28, TEA)}</g>' for i in range(4))}
<path d="M262 336h76M414 336h-76" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('conducive', '日ざしと水がそろうと、よく育つ', f'''
{sun(120, 90, 44)}
<g transform="translate(300 130) rotate(-124)"><path d="M-34 18v-44h64v44z" class="blue o"/>
  <path d="M30-18l40-18v42z" class="blue o"/></g>
{''.join(drop(300 + i*20, 176 + i*14, 0.9) for i in range(3))}
<path d="M232 240q58-32 118 0" fill="none" class="a" marker-end="url(#ar)"/>
<g transform="translate(460 306)"><path d="M-6 0v-130" fill="none" stroke="{GRND}" stroke-width="9"/>
  <path d="M-6-70q-52-8-58-58 46 2 58 44zM-6-104q40-14 44-58-40 6-48 44z" class="greenp o"/></g>''', arrow=True)

add('content-with', 'ささやかな一皿で十分だと、満ち足りている', f'''
{table(290)}
<g transform="translate(200 258)"><ellipse rx="60" ry="18" fill="#fffefd" class="o"/>
  <circle cx="-10" cy="-6" r="11" class="greenp o"/><circle cx="16" cy="-4" r="9" class="coral o"/></g>
{sit(330, 306, 1.2, -1, 'green', 'blue', 'short', 'smile', 'lap')}
{chair(316, 306, 1.05, 'gold', 1)}
<g opacity="0.35">{box(500, 264, 84, 56, 18, 'gold')}{box(500, 208, 84, 56, 18, 'gold')}</g>
<path d="M420 200h44" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('cremation', '火葬場の煙突と、骨つぼに花を供える', f'''
<g transform="translate(180 306)"><path d="M-90 0v-108h180V0z" fill="#fffefd" class="o"/>
  <path d="M-98-108h196l-24-34h-148z" class="teald o"/>
  <path d="M46-142h30v-58h-30z" class="teal o"/>
  <path d="M-24 0v-64h48V0z" class="teal o"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M61 200q-20-26 0-50 20-24 0-48"/><path d="M92 192q-18-24 0-46"/></g>
{table(300)}
<g transform="translate(430 270)"><path d="M-34 0q-16-40 0-58 12-14 34-14t34 14q16 18 0 58z" fill="#e8e4dc" class="o"/>
  <path d="M-40-72h80v14h-80z" fill="#e8e4dc" class="o"/></g>
<g transform="translate(526 262)"><path d="M0 40v-30" fill="none" stroke="{GRND}" stroke-width="5"/>
  <circle cy="-4" r="8" class="goldp o"/>
  {''.join(f'<ellipse cx="0" cy="-20" rx="7" ry="14" class="coral o" transform="rotate({d} 0 -4)"/>' for d in range(0, 360, 72))}</g>''')

add('dissatisfaction', '不満の声と苦情の紙が次々に集まる', f'''
{head(120, 250, 26, 'coral', 'short')}
{head(230, 230, 26, 'teal', 'bob')}
{head(340, 250, 26, 'violet', 'short')}
{''.join(f'<path d="M{88+i*110} 176q14-16 0-34" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}
<g transform="translate(480 250)">
  {''.join(f'<g transform="translate(0 {-i*30}) rotate({-10+i*7})"><rect x="-58" y="-22" width="116" height="44" rx="6" class="paper"/>'
           f'<rect x="-44" y="-8" width="70" height="8" rx="4" fill="{MUTED}"/></g>' for i in range(4))}
</g>
<path d="M390 200l50-16" class="a" marker-end="url(#ar)"/>''', arrow=True)

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
