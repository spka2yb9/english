# -*- coding: utf-8 -*-
"""batch168 以降の共通部品。lib.py の上に、各回で毎回書き写していた小物をまとめた。

使い方:
    from kit import *
    add('slug', 'altの文', 'captionの文', f'''<svg本体>''')
    finish(__file__)   # SVG一覧HTML と illustrations.ts 追記用の JSON を書き出す
"""
import json, os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *  # noqa: F401,F403

GLD, GLDP, GLDD = TONES['gold']
CRL, CRLP, CRLD = TONES['coral']
GRN, GRNP, GRND = TONES['green']
BLU, BLUP, BLUD = TONES['blue']
TEA, TEAP, TEAD = TONES['teal']
VIO, VIOP, VIOD = TONES['violet']
BRN = '#8b6437'
STONE = '#c3cbd1'

W = []        # 書き出した slug
ENTRIES = []  # illustrations.ts へ入れる {slug, alt, caption}


def add(slug, alt, caption, body, key=None, **k):
    """key は illustrations.ts のキー。省略時は slug。非ASCIIの見出し語だけ分ける。"""
    W.append(emit(slug, alt, body, **k))
    ENTRIES.append({'slug': slug.replace(' ', '-'), 'key': key or slug, 'alt': alt, 'caption': caption})


def finish(path):
    """一覧HTMLと、illustrations.ts 追記用の JSON を出す。"""
    name = os.path.splitext(os.path.basename(path))[0]
    out = os.path.join('/tmp', name + '.json')
    with open(out, 'w') as f:
        json.dump(ENTRIES, f, ensure_ascii=False)
    print(sheet(W, f'/tmp/{name}.html', 5), out, len(W))


# --- 背景・下地 --------------------------------------------------------------

def table(y=300):
    return (f'<path d="M40 {y}h520v20H40z" fill="#c9a464" class="o"/>'
            f'<path d="M80 {y+20}v60M520 {y+20}v60" stroke="#a0764a" stroke-width="14" stroke-linecap="round" fill="none"/>')


def split(x=300):
    return f'<path d="M{x} 20v360" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9" fill="none"/>'


def ring(x, y, r=64, dash=False, cls='coral'):
    d = ' stroke-dasharray="11 10"' if dash else ''
    c = MUTED if dash else TONES[cls][0]
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{c}" stroke-width="4"{d}/>'


# --- 記号 --------------------------------------------------------------------

def cross(x, y, s=1):
    return (f'<g fill="none" stroke="{CRL}" stroke-width="{9*s}" stroke-linecap="round">'
            f'<path d="M{x-26*s} {y-26*s}l{52*s} {52*s}M{x+26*s} {y-26*s}l{-52*s} {52*s}"/></g>')


def tick(x, y, s=1):
    return (f'<g fill="none" stroke="{GRN}" stroke-width="{9*s}" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M{x-30*s} {y}l{22*s} {24*s} {42*s}-{52*s}"/></g>')


def ban(x, y, r=44):
    """禁止・不可を示す ⊖。"""
    return (f'<g fill="none" stroke="{CRL}" stroke-width="9" stroke-linecap="round">'
            f'<circle cx="{x}" cy="{y}" r="{r}"/><path d="M{x-r*0.62} {y}h{r*1.24}"/></g>')


def spark(x, y, s=1, cls='gold'):
    return (f'<path d="M{x} {y-16*s}l{5*s} {11*s} {11*s} {5*s}-{11*s} {5*s}-{5*s} {11*s}'
            f'-{5*s}-{11*s}-{11*s}-{5*s} {11*s}-{5*s}z" class="{cls} o"/>')


def bolt(x, y, s=1):
    return (f'<path d="M{x} {y-44*s}l-{22*s} {52*s}h{16*s}l-{10*s} {40*s} {30*s}-{56*s}h-{17*s}z" class="gold o"/>')


def arc(x1, y1, x2, y2, lift=60, cls=None, dash=False, w=5):
    """2点を結ぶ弧。marker-end で矢印にするので emit(arrow=True) と併用する。"""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - lift
    d = ' stroke-dasharray="10 9"' if dash else ''
    return (f'<path d="M{x1} {y1}Q{mx} {my} {x2} {y2}" fill="none" stroke="{cls or INK}" '
            f'stroke-width="{w}" stroke-linecap="round"{d} marker-end="url(#ar)"/>')


def line(x1, y1, x2, y2, cls=None, dash=False, w=5, head=True):
    d = ' stroke-dasharray="10 9"' if dash else ''
    m = ' marker-end="url(#ar)"' if head else ''
    return (f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{cls or INK}" '
            f'stroke-width="{w}" stroke-linecap="round"{d}{m}/>')


# --- もの --------------------------------------------------------------------

def coin(x, y, r=20):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" class="gold o"/>'
            f'<circle cx="{x}" cy="{y}" r="{r*0.62}" fill="none" stroke="{GLDD}" stroke-width="2.5"/>')


def doc(x, y, w=100, h=130, lines=4, cls=None):
    g = [f'<g transform="translate({x} {y})"><path d="M{-w/2} {-h/2}h{w}v{h}h{-w}z" class="paper"/>']
    for i in range(lines):
        g.append(f'<rect x="{-w/2+14}" y="{-h/2+22+i*(h-50)/max(lines,1):.0f}" '
                 f'width="{w-28-(i%3)*16}" height="8" rx="4" fill="{cls or MUTED}"/>')
    g.append('</g>')
    return ''.join(g)


def book(x, y, s=1, cls='teal'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-92-64h84v128h-84zM8-64h84v128H8z" class="paper"/>'
            f'<path d="M-8-70h16v140h-16z" class="{cls}d o"/>'
            f'<g fill="{MUTED}">' + ''.join(f'<rect x="{-78 + 100*c}" y="{-44+i*24}" width="60" height="7" rx="3.5"/>'
                                            for c in range(2) for i in range(4)) + '</g></g>')


def word(x, y, n=5, w=26, cls=None, bad=-1):
    """文字は描けないので、語を四角の並びで表す。bad の位置だけ形を崩す。"""
    g = [f'<g transform="translate({x} {y})">']
    for i in range(n):
        cx = -(n - 1) * w / 2 + i * w
        if i == bad:
            g.append(f'<rect x="{cx-9}" y="-11" width="18" height="22" rx="4" fill="{CRL}" transform="rotate(18 {cx} 0)"/>')
        else:
            g.append(f'<rect x="{cx-9}" y="-11" width="18" height="22" rx="4" fill="{cls or INK}"/>')
    g.append('</g>')
    return ''.join(g)


def head(x, y, r=22, shirt='teal', hair='short', mood='smile'):
    mouth = {'smile': f'M{-r*0.3:.0f} {r*0.35:.0f}q{r*0.3:.0f} {r*0.3:.0f} {r*0.6:.0f} 0',
             'sad': f'M{-r*0.3:.0f} {r*0.55:.0f}q{r*0.3:.0f}-{r*0.3:.0f} {r*0.6:.0f} 0',
             'flat': f'M{-r*0.3:.0f} {r*0.45:.0f}h{r*0.6:.0f}'}[mood]
    return (f'<g transform="translate({x} {y})">'
            f'<circle r="{r}" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>'
            f'<path d="{HAIRS[hair]}" transform="translate(0 108) scale({r/24:.2f})" fill="{HAIR}"/>'
            f'<circle cx="{-r*0.33:.0f}" cy="{-r*0.17:.0f}" r="2.4" fill="{INK}"/>'
            f'<circle cx="{r*0.33:.0f}" cy="{-r*0.17:.0f}" r="2.4" fill="{INK}"/>'
            f'<path d="{mouth}" fill="none" stroke="{INK}" stroke-width="2"/>'
            f'<path d="M{-r*1.1:.0f} {r*1.5:.0f}q{r*1.1:.0f}-{r*0.6:.0f} {r*2.2:.0f} 0l-{r*0.3:.0f} {r*1.2:.0f}h-{r*1.6:.0f}z" '
            f'fill="{TONES[shirt][0]}" class="o"/></g>')


def house(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-80 0v-100h160V0z" fill="#fffefd" class="o"/>'
            f'<path d="M-94-100L0-166l94 66z" class="{cls}d o"/>'
            f'<path d="M-24 0v-56h48V0z" class="{cls} o"/>'
            f'<rect x="-62" y="-82" width="34" height="30" class="{cls}p o"/></g>')


def flower(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 40V0" fill="none" stroke="{GRND}" stroke-width="5"/>'
            + ''.join(f'<ellipse cx="0" cy="-22" rx="11" ry="22" class="{cls} o" transform="rotate({d} 0 0)"/>' for d in range(0, 360, 72))
            + f'<circle r="11" class="ink"/></g>')


def bar(x, y, vals, w=44, gap=18, unit=2.2, cls='teal'):
    """棒グラフ。vals は高さの相対値。"""
    g = []
    for i, v in enumerate(vals):
        h = v * unit
        c = cls if not isinstance(cls, (list, tuple)) else cls[i]
        g.append(f'<rect x="{x + i*(w+gap)}" y="{y-h}" width="{w}" height="{h}" rx="4" class="{c} o"/>')
    g.append(f'<path d="M{x-20} {y}h{len(vals)*(w+gap)+20}" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    return ''.join(g)


def jar(x, y, s=1, level=0.6, cls='teal'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-46-110h92v14h-92z" class="{cls}d o"/>'
            f'<path d="M-52-96h104v96a12 12 0 0 1-12 12h-80a12 12 0 0 1-12-12z" fill="#fffefd" class="o"/>'
            f'<path d="M-52 {12-108*level:.0f}h104v{108*level-12:.0f}a12 12 0 0 1-12 12h-80a12 12 0 0 1-12-12z" class="{cls}p"/>'
            f'<path d="M-52-96h104v96a12 12 0 0 1-12 12h-80a12 12 0 0 1-12-12z" fill="none" class="o"/></g>')


def scales(x, y, tilt=0, s=1):
    """天秤。tilt は左が下がる角度。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0v-150" fill="none" stroke="{BRN}" stroke-width="10" stroke-linecap="round"/>'
            f'<path d="M-40 10h80" fill="none" stroke="{BRN}" stroke-width="12" stroke-linecap="round"/>'
            f'<g transform="rotate({tilt})">'
            f'<path d="M-110-150h220" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M-110-150v40M110-150v40" fill="none" stroke="{MUTED}" stroke-width="3"/>'
            f'<path d="M-152-110h84l-16 34h-52z" class="goldp o"/>'
            f'<path d="M68-110h84l-16 34H84z" class="goldp o"/></g></g>')


def clock(x, y, r=56, h=10, m=10):
    ah, am = math.radians(h * 30 - 90), math.radians(m * 6 - 90)
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fffefd" class="o"/>'
            f'<circle cx="{x}" cy="{y}" r="{r*0.86}" fill="none" stroke="{MUTED}" stroke-width="2"/>'
            f'<path d="M{x} {y}l{r*0.46*math.cos(ah):.0f} {r*0.46*math.sin(ah):.0f}" stroke="{INK}" stroke-width="6" stroke-linecap="round" fill="none"/>'
            f'<path d="M{x} {y}l{r*0.72*math.cos(am):.0f} {r*0.72*math.sin(am):.0f}" stroke="{INK}" stroke-width="4" stroke-linecap="round" fill="none"/>'
            f'<circle cx="{x}" cy="{y}" r="4" class="ink"/>')


def arrowline(pts, cls=None, w=6, dash=False):
    d = ' stroke-dasharray="10 9"' if dash else ''
    p = 'M' + 'L'.join(f'{a} {b}' for a, b in pts)
    return (f'<path d="{p}" fill="none" stroke="{cls or INK}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round"{d} marker-end="url(#ar)"/>')
