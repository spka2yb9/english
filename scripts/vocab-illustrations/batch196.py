# -*- coding: utf-8 -*-
"""第196回: plus44(m〜p)の100語。"""
from kit import *

CS = ['coral', 'gold', 'teal', 'violet', 'blue', 'green']


# --- この回で使う小物 --------------------------------------------------------

def bubble(x, y, s=1, cls='blue', f=1, style='lines'):
    """せりふ・考えの吹き出し。style='none' なら中身は空。"""
    c = TONES[cls][0]
    g = [f'<g transform="translate({x} {y}) scale({s*f} {s})">',
         f'<path d="M-56-50h112a14 14 0 0 1 14 14v50a14 14 0 0 1-14 14H-14l-30 32 6-32h-18'
         f'a14 14 0 0 1-14-14v-50a14 14 0 0 1 14-14z" class="{cls}p o"/>']
    if style == 'none':
        pass
    elif style == 'wave':
        g.append(f'<g fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round">'
                 f'<path d="M-38-18q16-16 32 0t32 0M-38 14h64"/></g>')
    else:
        g.append(''.join(f'<rect x="-38" y="{-26+i*24}" width="{76-(i%3)*18}" height="10" rx="5" fill="{c}"/>'
                         for i in range(3)))
    g.append('</g>')
    return ''.join(g)


def heart(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0C-38-26-46-52-26-62-8-70 0-56 0-44 0-56 8-70 26-62 46-52 38-26 0 0Z" '
            f'class="{cls} o"/></g>')


def star(x, y, s=1, cls='gold'):
    pts = []
    for i in range(10):
        r = (18 if i % 2 == 0 else 7.5) * s
        a = math.radians(-90 + i * 36)
        pts.append(f'{x + r*math.cos(a):.0f} {y + r*math.sin(a):.0f}')
    return f'<path d="M{"L".join(pts)}z" class="{cls} o"/>'


def moon(x, y, r=44, cls='gold'):
    return (f'<path d="M{x} {y-r}A{r} {r} 0 0 0 {x} {y+r}'
            f'A{r*1.4} {r*1.4} 0 0 1 {x} {y-r}Z" class="{cls} o"/>')


def note(x, y, s=1, cls='violet'):
    c = TONES[cls][0]
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<ellipse rx="13" ry="10" transform="rotate(-18)" class="{cls} o"/>'
            f'<path d="M10-2v-40h5v40z" class="{cls}"/>'
            f'<path d="M15-42q24 6 26 26" fill="none" stroke="{c}" stroke-width="6" stroke-linecap="round"/></g>')


def bulb(x, y, s=1, on=True):
    """(x,y)は口金の下。on=False なら消えている。"""
    glass = 'class="goldp o"' if on else f'fill="#eeeae0" stroke="{MUTED}" stroke-width="2.5"'
    rays = (f'<g fill="none" stroke="{GLD}" stroke-width="4" stroke-linecap="round">'
            f'<path d="M0-108v-16M-42-94l-12-12M42-94l12-12"/></g>') if on else ''
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<circle cy="-58" r="38" {glass}/>'
            f'<path d="M-16-22h32v14h-32z" fill="{MUTED}" class="o"/>'
            f'<path d="M-14 0h28v-14h-28z" fill="#8f9aa3" class="o"/>'
            f'{rays}</g>')


def ball(x, y, r=24, cls='coral'):
    return f'<circle cx="{x}" cy="{y}" r="{r}" class="{cls} o"/>'


def soccer(x, y, r=26):
    g = [f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fffefd" class="o"/>',
         f'<path d="M{x-r*0.34:.0f} {y-r*0.28:.0f}l{r*0.34:.0f} -{r*0.3:.0f} {r*0.34:.0f} {r*0.3:.0f}'
         f'-{r*0.14:.0f} {r*0.42:.0f}h-{r*0.4:.0f}z" class="ink"/>']
    for d in range(0, 360, 72):
        a = math.radians(d)
        g.append(f'<path d="M{x + r*0.66*math.cos(a):.0f} {y + r*0.66*math.sin(a):.0f}'
                 f'l{r*0.22*math.cos(a+1.1):.0f} {r*0.22*math.sin(a+1.1):.0f}"'
                 f' fill="none" stroke="{INK}" stroke-width="3"/>')
    return ''.join(g)


def mags(x, y, n=4):
    """積み上げた雑誌。"""
    g = []
    for i in range(n):
        c = TONES[CS[i % 6]][0]
        g.append(f'<g transform="translate({x + i*4} {y - i*14}) rotate({-4 + i*3})">'
                 f'<rect x="-58" y="-40" width="116" height="80" rx="6" class="paper"/>'
                 f'<path d="M-46-26h42" fill="none" stroke="{c}" stroke-width="9" stroke-linecap="round"/>'
                 f'<rect x="-46" y="-4" width="92" height="9" rx="4.5" fill="{MUTED}"/>'
                 f'<rect x="-46" y="14" width="64" height="9" rx="4.5" fill="{MUTED}"/></g>')
    return ''.join(g)


def car(x, y, s=1, cls='teal', f=1):
    return (f'<g transform="translate({x} {y}) scale({s*f} {s})">'
            f'<path d="M-76-14q2-28 26-32l22-28h60l26 28q26 6 24 32 0 16-18 16h-124q-18 0-16-16z" class="{cls} o"/>'
            f'<path d="M-14-44l14-22h46l18 22z" class="bluep o"/>'
            f'<circle cx="-40" cy="4" r="17" fill="#fffefd" class="o"/>'
            f'<circle cx="40" cy="4" r="17" fill="#fffefd" class="o"/></g>')


def road(y=336):
    return (f'<path d="M0 {y}h600v64H0z" fill="#d9d3c9"/>'
            f'<path d="M0 {y}h600M0 {y+64}h600" fill="none" stroke="{INK}" stroke-width="3"/>'
            f'<path d="M10 {y+32}h580" fill="none" stroke="#fffefd" stroke-width="6" stroke-dasharray="40 30"/>')


def mountain(x, y, s=1, cls='teal'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-140 0L-40-130l100 130z" class="{cls}d o"/>'
            f'<path d="M-40-130l26 34-14 6-20-16-20 14-14-8z" fill="#fffefd" class="o"/>'
            f'<path d="M10 0L96-104l86 104z" class="{cls} o"/>'
            f'<path d="M96-104l22 26-14 6-16-14-16 14-12-8z" fill="#fffefd" class="o"/></g>')


def doorframe(x, y, s=1, cls='gold'):
    """開いた戸。枠と、外へ振れた戸板。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-16-256h32v256h-32z" fill="{BRN}" class="o"/>'
            f'<path d="M-16-256h216v22h-216z" fill="{BRN}" class="o"/>'
            f'<path d="M16-234h180v234H16z" fill="#efe6d4" class="o"/>'
            f'</g>'
            f'<g transform="translate({x} {y}) scale({s}) skewY(-30)">'
            f'<path d="M16-234h150v234H16z" class="{cls}p o"/>'
            f'<circle cx="146" cy="-120" r="12" class="{cls}d o"/></g>')


def switch(x, y, s=1, on=False):
    c = 'gold' if on else 'blue'
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect x="-36" y="-56" width="72" height="112" rx="12" fill="#fffdf6" class="o"/>'
            f'<rect x="-22" y="{-34 if on else 8}" width="44" height="26" rx="9" class="{c} o"/></g>')


def calendar(x, y, s=1, cls='coral', mark=(1,)):
    c = TONES[cls][0]
    cells = ''.join(f'<rect x="{-96 + col*30}" y="{-30 + row*30}" width="22" height="20" rx="4" '
                    f'fill="{c if row in mark else MUTED}" opacity="{1 if row in mark else 0.45}"/>'
                    for row in range(4) for col in range(7))
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-108-84h216v168h-216z" class="paper"/>'
            f'<path d="M-108-84h216v40h-216z" class="{cls} o"/>'
            f'<path d="M-72-100v26M72-100v26" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>'
            f'<g>{cells}</g></g>')


def phone(x, y, s=1, cls='teal'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect x="-40" y="-76" width="80" height="152" rx="16" fill="#fffdf6" class="o"/>'
            f'<rect x="-28" y="-58" width="56" height="112" rx="6" class="{cls}p o"/></g>')


def laptop(x, y, s=1, cls='teal'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-84-96h168v96h-168z" class="{cls}d o"/>'
            f'<path d="M-70-82h140v68h-140z" fill="#eaf4ff" class="o"/>'
            f'<path d="M-104 0h208l14 22h-236z" fill="{MUTED}" class="o"/></g>')


def wifi(x, y, s=1, cls='blue'):
    c = TONES[cls][0]
    return (f'<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{c}" '
            f'stroke-width="7" stroke-linecap="round">'
            f'<path d="M-48 4a64 64 0 0 1 96 0M-24 26a32 32 0 0 1 48 0"/>'
            f'<circle cy="48" r="6" fill="{c}" stroke="none"/></g>')


def tag(x, y, s=1, rot=0, cls='gold'):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
            f'<path d="M-4-32h42l26 32-26 32h-42z" class="{cls}p o"/>'
            f'<circle cx="8" cy="0" r="7" fill="#fffefd" class="o"/></g>')


def chart(x, y, s=1):
    """地図。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-70-56h140v112h-140z" class="paper"/>'
            f'<g fill="none" stroke="{MUTED}" stroke-width="3">'
            f'<path d="M-70-56l34 28M70-56l-34 28M-70 56l34-28M70 56l-34-28"/></g>'
            f'<path d="M-26 26q14-52 52-24" fill="none" stroke="{CRL}" stroke-width="6" '
            f'stroke-dasharray="10 8" stroke-linecap="round"/>'
            f'<circle cx="6" cy="-10" r="9" class="coral o"/></g>')


def cane(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0v-120q0-28 28-28t28 28" fill="none" stroke="{BRN}" '
            f'stroke-width="10" stroke-linecap="round"/></g>')


def baby(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<ellipse rx="56" ry="32" class="bluep o"/>'
            f'<circle cx="-46" cy="-26" r="28" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>'
            f'<path d="M-64-44q18-16 36 0" fill="none" stroke="{HAIR}" stroke-width="6" stroke-linecap="round"/>'
            f'<circle cx="-53" cy="-28" r="3" class="ink"/><circle cx="-39" cy="-28" r="3" class="ink"/>'
            f'<path d="M-58-12q10 9 20 0" fill="none" stroke="{INK}" stroke-width="2.5"/>'
            f'<path d="M-16 8h60l12 24H-26z" fill="#fffefd" class="o"/></g>')


def swirl(x, y, s=1, cls='green'):
    c = TONES[cls][0]
    g = ''.join(f'<path d="M{-8-i*16} {-8-i*16}a{10+i*16} {10+i*16} 0 0 1 {16+i*32} 0"/>'
                for i in range(3))
    return (f'<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{c}" '
            f'stroke-width="5" stroke-linecap="round">{g}</g>')


def plate(x, y, s=1, cls='blue'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<ellipse rx="98" ry="30" fill="#fffefd" class="o"/>'
            f'<ellipse rx="74" ry="19" fill="none" stroke="{TONES[cls][0]}" stroke-width="3"/></g>')


def mug(x, y, s=1, cls='gold', steam=False):
    st = ''.join(f'<path d="M{-14+i*14} -64q-12-18 0-32t0-30" fill="none" stroke="{MUTED}" '
                 f'stroke-width="4" stroke-linecap="round"/>' for i in range(2)) if steam else ''
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-34-56h68v48a14 14 0 0 1-14 14h-40a14 14 0 0 1-14-14z" class="{cls}p o"/>'
            f'<path d="M34-38h18a18 18 0 0 1 0 36H34" fill="none" stroke="{TONES[cls][2]}" stroke-width="8"/>'
            f'<path d="M-34-56h68" fill="none" stroke="{INK}" stroke-width="4"/>{st}</g>')


def moneybag(x, y, s=1, cls='gold'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-14-96h28l-8 14q40 22 34 72-6 44-40 44t-40-44q-6-50 34-72z" class="{cls} o"/>'
            f'<path d="M-20-110h40v16h-40z" class="{cls}d o"/></g>')


def mitten(x, y, s=1, rot=0, cls='coral'):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
            f'<path d="M-28-68q-38 0-38 40 0 28 24 34l-4 38q-2 14 12 14h44q14 0 12-14l-4-38'
            f'q24-6 24-34 0-40-38-40z" class="{cls} o"/>'
            f'<path d="M-62-44q-26-6-30-28 18-12 32-4z" class="{cls} o"/>'
            f'<path d="M-24 42q26 14 54 0" fill="none" stroke="{TONES[cls][2]}" stroke-width="7"/></g>')


def carton(x, y, s=1, cls='blue'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-56-150h112v150h-112z" fill="#fffdf6" class="o"/>'
            f'<path d="M-56-150h112l-24-32h-64z" class="{cls}p o"/>'
            f'<rect x="-38" y="-108" width="76" height="54" rx="8" class="{cls}p o"/>'
            f'<path d="M-38-80h76" fill="none" stroke="{TONES[cls][0]}" stroke-width="9"/></g>')


def glassmilk(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-34-100h68l-10 92a12 12 0 0 1-12 8h-24a12 12 0 0 1-12-8z" fill="#fffefd" class="o"/>'
            f'<path d="M-30-56h60l-7 48a12 12 0 0 1-12 8h-22a12 12 0 0 1-12-8z" fill="#eef4fb" class="o"/></g>')


def card(x, y, s=1, cls='blue'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-64-40h128v80h-128z" class="paper"/>'
            f'<rect x="-48" y="-24" width="96" height="16" rx="8" fill="{TONES[cls][0]}"/>'
            f'<rect x="-48" y="4" width="60" height="11" rx="5.5" fill="{MUTED}"/></g>')


def signpost(x, y, s=1, cls='gold', f=1):
    return (f'<g transform="translate({x} {y}) scale({s*f} {s})">'
            f'<path d="M0-170v170" fill="none" stroke="{BRN}" stroke-width="12" stroke-linecap="round"/>'
            f'<path d="M0-158h100l24 24-24 24H0z" class="{cls} o"/></g>')


def speaker(x, y, s=1, cls='violet'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect x="-72" y="-116" width="144" height="232" rx="14" class="paper"/>'
            f'<circle cy="-52" r="42" class="{cls}p o"/><circle cy="-52" r="15" class="{cls} o"/>'
            f'<circle cy="52" r="28" class="{cls}p o"/><circle cy="52" r="10" class="{cls} o"/></g>')


def piece(x, y, s=1, cls='gold', rot=0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
            f'<path d="M-40-40h30a14 14 0 1 1 20 0h30v30a14 14 0 1 1 0 20v30H30'
            f'a14 14 0 1 0-20 0h-30v-30a14 14 0 1 0 0-20z" class="{cls} o"/></g>')


def bench(x, y, s=1, cls='gold'):
    ts, tp, td = TONES[cls]
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-56-30v30M56-30v30" fill="none" stroke="{td}" stroke-width="10" stroke-linecap="round"/>'
            f'<path d="M-70-30h140v16h-140z" fill="{ts}" class="o"/>'
            f'<path d="M-70-84h140v14h-140z" fill="{ts}" class="o"/>'
            f'<path d="M-56-84v54M56-84v54" fill="none" stroke="{td}" stroke-width="8"/></g>')


def fence(x, y, s=1):
    posts = ''.join(f'<path d="M{-96+i*48}-56l12-16 12 16v56h-24z" fill="#fffdf6" class="o"/>'
                    for i in range(5))
    return (f'<g transform="translate({x} {y}) scale({s})">{posts}'
            f'<path d="M-120-34h240M-120-12h240" fill="none" stroke="{BRN}" stroke-width="8"/></g>')


def thumbup(x, y, s=1, f=1):
    return (f'<g transform="translate({x} {y}) scale({s*f} {s})">'
            f'<ellipse rx="44" ry="38" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>'
            f'<path d="M-14-30q-10-48 18-54 24-4 24 26 0 12-8 24z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>'
            f'<g fill="none" stroke="{SKINL}" stroke-width="3"><path d="M-26-6h42M-26 14h36"/></g></g>')


def shoe(x, y, s=1, cls='coral', f=1):
    return (f'<g transform="translate({x} {y}) scale({s*f} {s})">'
            f'<path d="M-70 0q0-24 20-30l26-42h34l40 48q26 6 26 24z" class="{cls} o"/>'
            f'<path d="M-72 0h146v14h-146z" fill="#fffefd" class="o"/></g>')


# --- m ----------------------------------------------------------------------

add('magazines', 'テーブルに積まれた雑誌と、1冊を開いて読む人のイラスト。', '複数冊まとめて置いてある雑誌。magazine の複数形。', f"""
{table(300)}
{mags(170, 252, 4)}
{person(430, 352, 1.15, -1, 'teal', 'blue', 'hold', 'short', 'smile')}
<g transform="translate(402 292) rotate(-10)">
  <path d="M-66-44h68l56 44-56 44h-68z" class="paper"/>
  <path d="M2-44l56 44-56 44" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <rect x="-54" y="-26" width="44" height="8" rx="4" fill="{MUTED}"/>
  <rect x="-54" y="-6" width="38" height="8" rx="4" fill="{MUTED}"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('main', '幅の広い通りが画面を横切り、脇道が細く分かれているイラスト。', '中心になる一番大きな通り。main road / main street。', f"""
<path d="M110 336h150v-96H110z" fill="#d9d3c9"/>
<path d="M330 336h100v-76H330z" fill="#d9d3c9"/>
{building(46, 306, 0.62, 'blue')}
{tower(196, 306, 0.5, 'teal', 3)}
{building(382, 300, 0.55, 'violet')}
{building(500, 306, 0.72, 'coral')}
{road(336)}
{car(300, 372, 0.85, 'gold', 1)}
""")

add('man', 'ネクタイを締めた大人の男性が立っているイラスト。', '成人した男性。複数形は men と不規則に変わる。', f"""
{person(300, 352, 1.4, 1, 'blue', 'blue', 'stand', 'short', 'smile')}
<path d="M286 260h28l-5 16 13 58-22 14-22-14 13-58z" class="coral o"/>
<path d="M60 386h480" class="a"/>
""")

add('many', '箱からたくさんのボールがあふれ出ているイラスト。', '数えられるものが「たくさん」。many + 複数形で使う。', f"""
<g transform="translate(170 262) rotate(-30)">
  <path d="M-62-58h124v116h-124z" class="blue o"/>
  <path d="M-62-58h124l-26-30h-72z" class="bluep o"/>
</g>
<g>{''.join(f'<circle cx="{x}" cy="{y}" r="{r}" class="{c} o"/>' for x, y, r, c in [
    (250, 330, 20, 'coral'), (292, 346, 18, 'gold'), (332, 330, 19, 'teal'),
    (370, 348, 17, 'violet'), (406, 332, 20, 'blue'), (444, 346, 18, 'green'),
    (480, 332, 19, 'coral'), (300, 294, 16, 'gold'), (352, 286, 15, 'teal'),
    (412, 290, 16, 'violet'), (268, 242, 13, 'blue'), (470, 288, 15, 'green')])}</g>
<path d="M60 386h480" class="a"/>
""")

add('married', '指輪をはめた2人が並び、間にハートが浮かぶイラスト。', '結婚している状態。be married to 人 の形で使う。', f"""
{person(230, 352, 1.25, 1, 'violet', 'blue', 'give', 'bob', 'smile')}
{person(370, 352, 1.25, -1, 'blue', 'blue', 'give', 'short', 'smile')}
<circle cx="313" cy="278" r="14" fill="none" stroke="{GLD}" stroke-width="8"/>
<circle cx="287" cy="278" r="14" fill="none" stroke="{GLDD}" stroke-width="8"/>
{heart(300, 206, 0.9, 'coral')}
{spark(196, 178, 0.8)}{spark(408, 178, 0.8)}
<path d="M60 386h480" class="a"/>
""")

add('match', 'ゴールの前で2人の選手がボールを挟んで向き合うイラスト。', 'スポーツの試合。ほかに「色が合う」「マッチ棒」の意味もある。', f"""
<g transform="translate(50 306)">
  <path d="M0 0v-150h180v150" fill="none" stroke="{INK}" stroke-width="8"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5" stroke-dasharray="14 12">
    <path d="M36 0v-150M72 0v-150M108 0v-150M144 0v-150M0-75h180"/>
  </g>
</g>
{soccer(444, 352, 30)}
{person(316, 352, 1.15, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
{person(544, 352, 1.15, -1, 'coral', 'blue', 'walk', 'bob', 'smile')}
<path d="M60 386h480" class="a"/>
""")

add('math', '黒板に三角形・円・四角と計算の記号が描かれているイラスト。', '数学。学校の科目としての math。', f"""
<g transform="translate(300 194)">
  <path d="M-232-118h464v236h-464z" fill="#3c5a52" class="o"/>
  <g fill="none" stroke="#fffefd" stroke-width="5" stroke-linecap="round">
    <path d="M-186-58l-62 96h124z"/>
    <circle cx="-52" cy="-10" r="50"/>
    <path d="M40-58h108v96H40z"/>
    <path d="M-24 96h48M0 72v48"/>
    <path d="M92 74l56 52M148 74l-56 52"/>
  </g>
  <path d="M-246 130h492v16h-492z" fill="{BRN}"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('maybe', '考えている人の上に、晴れと雨の吹き出しが2つ浮かぶイラスト。', 'たぶん、もしかすると。どちらか分からない見込みを表す。', f"""
{person(300, 352, 1.25, 1, 'teal', 'blue', 'think', 'bob', 'neutral')}
{bubble(160, 140, 0.9, 'gold', -1, 'none')}
{sun(160, 132, 26)}
{bubble(448, 140, 0.9, 'blue', 1, 'none')}
{cloud(448, 128, 0.62, 'blue')}
<path d="M60 386h480" class="a"/>
""")

add('me', '品物を差し出され、自分に輪がかかっているイラスト。', '「私を・私に」。I の目的格で、give me のように使う。', f"""
{person(170, 352, 1.2, 1, 'gold', 'blue', 'give', 'short', 'smile')}
{box(252, 268, 86, 68, 24, 'teal')}
{person(440, 352, 1.2, -1, 'teal', 'blue', 'hold', 'bob', 'smile')}
{ring(440, 296, 86, dash=True)}
{arc(312, 240, 396, 262, -44)}
<path d="M60 386h480" class="a"/>
""", arrow=True)

add('measuring cup', '目盛りのついた計量カップに水が入っているイラスト。', '料理で分量を量るための計量カップ。', f"""
<g transform="translate(290 296)">
  <path d="M-86-70h172l-18 132a14 14 0 0 1-14 12h-108a14 14 0 0 1-14-12z" fill="#fffdf6" class="o"/>
  <path d="M-78-34h156l-14 94a14 14 0 0 1-14 12h-100a14 14 0 0 1-14-12z" class="bluep"/>
  <path d="M-98-78h196v20h-196z" class="bluep o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">
    <path d="M86-46H62M86-18H52M86 10H62M86 38H52"/>
  </g>
</g>
<path d="M60 386h480" class="a"/>
""")

add('meat', 'まな板の上に載った厚い肉と包丁のイラスト。', '食用の肉。ステーキやハムなど。', f"""
<g transform="translate(290 322)">
  <path d="M-176-14h352v40h-352z" class="goldp o"/>
  <path d="M-196-14h392v-14h-392z" class="gold o"/>
</g>
<g transform="translate(270 254)">
  <path d="M-100-34q74-42 176-16 42 12 36 46-6 36-58 42-126 12-160-22-26-28 6-50z" class="coral o"/>
  <path d="M-48-14q64-14 134 4" fill="none" stroke="{CRLD}" stroke-width="6"/>
  <path d="M-22 14q60-10 116 6" fill="none" stroke="{CRLD}" stroke-width="6"/>
  <path d="M84-48l56-16 10 24-56 24z" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(510 250) rotate(16)">
  <path d="M-8-72h16v122h-16z" fill="{MUTED}" class="o"/>
  <path d="M-8-98h16v26h-16z" fill="#8f9aa3" class="o"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('meet', '2人が向かい合って握手しているイラスト。', '会う、待ち合わせて会う。人と会って話すこと。', f"""
{person(216, 352, 1.3, 1, 'violet', 'blue', 'give', 'bob', 'smile')}
{person(384, 352, 1.3, -1, 'blue', 'blue', 'give', 'short', 'smile')}
<circle cx="300" cy="269" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<path d="M280 262q20-14 40 0" fill="none" stroke="{SKINL}" stroke-width="3"/>
{spark(300, 190, 1.0)}
<path d="M60 386h480" class="a"/>
""")

add('member', '並んだ4人のうち1人だけが輪で囲まれているイラスト。', '会員、メンバー。集まりの一員であること。', f"""
{person(140, 352, 1.1, 1, 'gold', 'blue', 'stand', 'short', 'smile')}
{person(276, 352, 1.1, 1, 'blue', 'blue', 'stand', 'bob', 'smile')}
{ring(412, 300, 80, dash=True)}
{person(412, 352, 1.1, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(544, 352, 1.1, 1, 'violet', 'blue', 'stand', 'bob', 'smile')}
{tick(412, 190, 0.85)}
<path d="M60 386h480" class="a"/>
""")

add('message', '携帯電話を持った人の上に吹き出しが出ているイラスト。', '伝言、メッセージ。人に伝える短いことば。', f"""
{person(230, 352, 1.2, 1, 'teal', 'blue', 'hold', 'short', 'smile')}
{phone(248, 298, 0.42, 'teal')}
{bubble(436, 168, 1.0, 'blue', 1)}
<path d="M352 226l54 40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>
<path d="M60 386h480" class="a"/>
""")

add('migraine', '頭を押さえてうつむく人の頭のまわりに、稲妻のような痛みが走るイラスト。', 'ズキズキと痛む片頭痛。', f"""
{sit(300, 352, 1.3, 1, 'violet', 'blue', 'short', 'sad', 'up')}
<g class="coral">
  <path d="M214 214l-18 30 20 10-20 30 40-34-18-10 18-32z"/>
  <path d="M386 206l20 28-20 12 20 30-40-32 18-10-18-32z"/>
  <path d="M300 156l-14 24 16 8-16 26 32-28-14-8 14-26z"/>
</g>
<g transform="translate(300 240)" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round">
  <path d="M-40 10q30-34 60-6"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('mile', '道ばたの距離標識から、遠くの家までの道のりが点線で示されたイラスト。', 'マイル。1マイルは約1.6kmの長さの単位。', f"""
<g transform="translate(140 336)">
  <path d="M-38-92q0-30 38-30t38 30v92h-76z" fill="#e6e1d6" class="o"/>
  <rect x="-24" y="-72" width="48" height="16" rx="6" fill="{MUTED}"/>
  <rect x="-24" y="-46" width="32" height="12" rx="6" fill="{MUTED}"/>
</g>
{road(336)}
{house(500, 336, 0.62, 'coral')}
<path d="M186 286q140-86 268-8" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>
{car(320, 372, 0.7, 'teal', 1)}
""")

add('milk', '牛乳パックからコップへ牛乳が注がれているイラスト。', '牛乳、ミルク。白い飲み物。', f"""
<g transform="translate(200 340)">
  {carton(0, 0, 1.0, 'blue')}
</g>
<g transform="translate(268 186) rotate(30)">
  <path d="M0 0h40v20H0z" fill="#fffdf6" class="o"/>
</g>
<path d="M292 208q26 20 42 40" fill="none" stroke="{BLU}" stroke-width="10" stroke-linecap="round"/>
{drop(322, 264, 1.1, 'blue')}
{drop(340, 300, 0.9, 'blue')}
{glassmilk(400, 340, 1.3)}
<path d="M60 386h480" class="a"/>
""")

add('million', '金貨の山と金袋が積み上がり、きらめいているイラスト。', '100万。millions of で「何百万もの」となる。', f"""
<path d="M60 372q20-150 240-150t240 150z" class="goldp o"/>
<g>{''.join(f'<circle cx="{x}" cy="{y}" r="{r}" class="gold o"/>' for x, y, r in [
    (150, 250, 26), (216, 216, 26), (300, 200, 26), (384, 218, 26), (452, 252, 26),
    (258, 254, 24), (348, 256, 24), (300, 268, 24)])}</g>
{moneybag(140, 196, 0.8)}
{moneybag(470, 200, 0.7)}
{spark(300, 122, 1.3)}{spark(170, 118, 0.9)}{spark(438, 126, 0.9)}
<path d="M60 386h480" class="a"/>
""")

add('miss', '発車していく電車に向かって、ホームから手を伸ばす人のイラスト。', '乗り遅れる。また、人に会えず寂しく思う気持ちも表す。', f"""
<g transform="translate(410 336)">
  <path d="M-142-118h284v118h-284z" fill="#eaf4ff" class="o"/>
  <path d="M-142-44h284" fill="none" stroke="{INK}" stroke-width="6"/>
  {''.join(f'<rect x="{-128+i*48}" y="-102" width="36" height="42" rx="4" class="bluep o"/>' for i in range(6))}
  <path d="M-142-18h284v18h-284z" fill="{MUTED}"/>
  <circle cx="-84" cy="14" r="16" fill="#fffefd" class="o"/>
  <circle cx="84" cy="14" r="16" fill="#fffefd" class="o"/>
</g>
{person(180, 352, 1.2, 1, 'coral', 'blue', 'reach', 'short', 'sad')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M212 240h58M212 262h44M212 284h52"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('mittens', 'ひもでつながれた2つのミトンと、雪の結晶のイラスト。', '親指だけ分かれた手袋。ふつう複数形で使う。', f"""
{mitten(200, 250, 1.15, -12, 'coral')}
{mitten(400, 268, 1.15, 10, 'blue')}
<path d="M246 292q54 46 110 8" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 9"/>
{star(300, 120, 1.1, 'blue')}{star(446, 148, 0.8, 'blue')}{star(150, 140, 0.8, 'blue')}
<path d="M60 386h480" class="a"/>
""")

add('modern', 'ガラスの窓が並ぶ、新しくて高いビルのイラスト。', '現代の、近代的な、最新の。今の時代の様子を表す。', f"""
<g transform="translate(320 356)">
  <path d="M-150 0v-256h300V0z" fill="#eaf4ff" class="o"/>
  <g class="bluep o">{''.join(f'<rect x="{-130+c*70}" y="{-232+r*56}" width="54" height="40"/>'
                              for r in range(4) for c in range(4))}</g>
  <path d="M-170-256h340v20h-340z" fill="{MUTED}" class="o"/>
  <path d="M-40 0v-74h80V0z" class="bluep o"/>
</g>
{person(110, 352, 1.15, 1, 'teal', 'blue', 'point', 'short', 'smile')}
<path d="M60 386h480" class="a"/>
""")

add('moment', 'カメラのフラッシュが光り、跳んでいる人を写しているイラスト。', '瞬間。ほんの一瞬のできごと。', f"""
{person(320, 292, 1.1, 1, 'coral', 'blue', 'up', 'short', 'smile')}
<path d="M262 300q58-42 116 0" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>
<g transform="translate(150 244) rotate(-6)">
  <path d="M-72-42h144v84h-144z" class="gold o"/>
  <path d="M-34-58h68v16h-68z" class="goldd o"/>
  <circle r="26" fill="#fffdf6" class="o"/><circle r="13" class="blue"/>
  <path d="M-58-42h22v-12h-22z" fill="{MUTED}"/>
</g>
<g fill="none" stroke="{GLD}" stroke-width="5" stroke-linecap="round">
  <path d="M234 200l30-24M228 168h36M244 138l22 16"/>
</g>
{spark(330, 170, 1.1)}
<path d="M60 386h480" class="a"/>
""")

add('second-hand', '青空市の台の上に中古の品々と値札が並んでいるイラスト。', '中古の、使い古しの。second-hand shop で中古品店。', f"""
<g transform="translate(300 110)">
  <path d="M-236 0h472l-32 66h-408z" class="coralp o"/>
  <path d="M-236 0v-16h472V0z" class="coral o"/>
  {''.join(f'<path d="M{-206+i*82} 0v66" fill="none" stroke="{CRLP}" stroke-width="10"/>' for i in range(6))}
</g>
{table(300)}
<g transform="translate(170 244)">
  <circle r="30" class="goldp o"/>
  <path d="M0 30v14" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-26 44h52" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
</g>
{clock(300, 244, 32, 3, 12)}
<g transform="translate(400 244)">
  <path d="M-40-48h80v96h-80z" class="teal o"/>
  <path d="M-40-48h80v14h-80z" class="teald o"/>
</g>
{tag(500, 202, 0.95, 14, 'gold')}
<path d="M60 386h480" class="a"/>
""")

add('money', '財布から紙幣と硬貨があふれ出ているイラスト。', 'お金、金銭。現金全般を指す語。', f"""
<g transform="translate(170 300) rotate(-12)">
  <path d="M-98-62h196v124h-196z" class="goldd o"/>
  <path d="M-98-62h196v22h-196z" class="gold o"/>
  <path d="M-98 40h196v22h-196z" class="gold o"/>
  <circle cx="0" cy="0" r="16" fill="none" stroke="{GLD}" stroke-width="7"/>
</g>
<g transform="translate(340 250) rotate(-8)">
  <rect x="-70" y="-46" width="140" height="92" rx="8" class="tealp o"/>
  <rect x="-56" y="-32" width="112" height="64" rx="6" fill="none" stroke="{TEAD}" stroke-width="4"/>
  <circle r="20" fill="none" stroke="{TEA}" stroke-width="7"/>
</g>
<g>{''.join(coin(x, y, r) for x, y, r in [
    (250, 336, 22), (292, 352, 20), (334, 340, 21), (376, 354, 19), (418, 342, 22), (200, 352, 19)])}</g>
{spark(140, 190, 0.9)}
<path d="M60 386h480" class="a"/>
""")

add('month', '1か月分のマス目が並ぶカレンダーのイラスト。', '暦の1か月。a month で「1か月」。', f"""
{calendar(300, 186, 1.25, 'coral', (1, 2))}
<path d="M240 340v34" fill="none" stroke="{BRN}" stroke-width="10" stroke-linecap="round"/>
<path d="M300 340v34" fill="none" stroke="{BRN}" stroke-width="10" stroke-linecap="round"/>
<path d="M60 386h480" class="a"/>
""")

add('moonlight', '夜空に浮かぶ月と、水面に揺れる月明かりのイラスト。', '月光、月明かり。moon + light で「月の光」。', f"""
{''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fffefd"/>' for x, y, r in [
    (90, 70, 4), (162, 118, 3), (280, 56, 3), (500, 104, 4), (546, 168, 3), (62, 186, 3)])}
{moon(300, 128, 60, 'gold')}
<g fill="none" stroke="{GLD}" stroke-width="5" stroke-linecap="round" opacity="0.55">
  <path d="M244 188l-30 92M300 194v92M356 188l30 92"/>
</g>
<path d="M0 300h600v100H0z" fill="#cfe0ee"/>
<g fill="none" stroke="#fffefd" stroke-width="6" stroke-linecap="round" opacity="0.9">
  <path d="M244 322h40M300 332h56M374 348h44M252 364h60M342 380h50"/>
</g>
""", bg='#e8eef7', ground=False)

add('more', '積み上がったコインの山に、もう1枚コインが加わるイラスト。', 'もっと多くの、さらに。more + 名詞で「もっと多くの〜」。', f"""
<g transform="translate(300 386)">
  {''.join(f'<path d="M-86 {-34-i*22}q86-26 172 0v16q-86 26-172 0z" class="gold o"/>' for i in range(6))}
</g>
{coin(300, 128, 28)}
{arrowline([(300, 176), (300, 216)], None, 7)}
{spark(180, 150, 1.0)}
{spark(420, 150, 1.0)}
""", arrow=True)

add('morning', '山の向こうから朝日が昇り、人が背伸びをしているイラスト。', '朝、午前。1日の始まりの時間。', f"""
{sun(430, 300, 62)}
<path d="M0 306h600v94H0z" class="ground"/>
<path d="M0 306q110-72 220 0z" class="greend"/>
<path d="M420 306q96-64 180-4v4z" class="greend"/>
{person(180, 352, 1.2, 1, 'coral', 'blue', 'up', 'bob', 'smile')}
<g fill="none" stroke="{GLD}" stroke-width="5" stroke-linecap="round">
  <path d="M292 196q40-22 82-8"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('most', '棒グラフの1本だけが他よりずば抜けて高いイラスト。', '最も、一番。many / much の最上級。', f"""
{bar(120, 360, [2, 3, 1, 12, 2], 58, 22, 22, ['blue', 'blue', 'blue', 'gold', 'blue'])}
{spark(396, 82, 1.3)}
<path d="M60 386h480" class="a"/>
""")

add('mother', '女性が小さな子どもの手を引いて立っているイラスト。', '母、お母さん。自分にとっての母親。', f"""
{person(250, 352, 1.3, 1, 'coral', 'blue', 'give', 'bob', 'smile')}
{person(404, 352, 0.86, -1, 'teal', 'blue', 'up', 'short', 'smile')}
<circle cx="345" cy="256" r="15" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
{heart(300, 190, 0.6, 'coral')}
<path d="M60 386h480" class="a"/>
""")

add('mountain', '雪をかぶった峰が連なるイラスト。', '山、山岳。高くそびえる山の峰。', f"""
{mountain(280, 316, 1.25, 'teal')}
<g transform="translate(230 150)">
  <path d="M0-70v70" fill="none" stroke="{BRN}" stroke-width="7"/>
  <path d="M0-70h54l-14 18 14 18H0z" class="coral o"/>
</g>
{tree(70, 330, 0.8)}
{tree(540, 326, 0.72)}
<path d="M60 386h480" class="a"/>
""")

add('mouth', '人の顔の口の部分が輪で囲まれているイラスト。', '口。食べたり話したりする器官。', f"""
{face(300, 180, 118, 'smile')}
<ellipse cx="300" cy="206" rx="54" ry="30" class="coral o"/>
<path d="M246 206q54 30 108 0" fill="none" stroke="{CRLD}" stroke-width="4"/>
{ring(300, 212, 82)}
<path d="M60 386h480" class="a"/>
""")

add('mouthful', 'スプーン1杯の食べ物を口に運んでいるイラスト。', 'ひと口、ひと口分。a mouthful of 〜 の形で使う。', f"""
{person(230, 352, 1.25, 1, 'gold', 'blue', 'hold', 'short', 'smile')}
<g transform="translate(296 234) rotate(-32)">
  <path d="M-10-24h20v44h-20z" fill="{MUTED}" class="o"/>
  <ellipse cy="-36" rx="26" ry="18" class="goldp o"/>
  <circle cy="-42" r="12" class="coral o"/>
</g>
{plate(470, 348, 0.72)}
<g transform="translate(470 340)">
  <ellipse rx="36" ry="14" class="goldp o"/>
  <ellipse cx="-8" cy="-8" rx="18" ry="10" class="goldp o"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('movie', '映写機の光がスクリーンに当たり、映像が映っているイラスト。', '映画。a movie で1本の映画。', f"""
<g transform="translate(386 168)">
  <path d="M-144-118h288v220h-288z" fill="#fffefd" class="o"/>
  <path d="M-118-84l74 104h-74z" class="tealp o"/>
  <circle cx="56" cy="-14" r="46" class="goldp o"/>
  <path d="M-110 116h220" fill="none" stroke="{MUTED}" stroke-width="6"/>
</g>
<g transform="translate(96 250)">
  <path d="M-58-58h116v116h-116z" class="violet o"/>
  <circle cx="-26" cy="-26" r="21" fill="#fffdf6" class="o"/>
  <circle cx="26" cy="-26" r="21" fill="#fffdf6" class="o"/>
  <path d="M-30 34h60v14h-60z" fill="{VIOD}"/>
  <path d="M40 16h26v24H40z" fill="{VIOD}" class="o"/>
</g>
<g fill="none" stroke="{GLD}" stroke-width="6" stroke-linecap="round" opacity="0.7" stroke-dasharray="18 14">
  <path d="M158 208l74-30M158 250h74M158 292l74 30"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('mr', 'ネクタイ姿の男性が、白い名札のそばに立っているイラスト。', '男性の姓に付ける敬称「〜さん、〜氏」。', f"""
{person(270, 352, 1.3, 1, 'blue', 'blue', 'stand', 'short', 'smile')}
<path d="M256 262h28l-5 16 13 60-22 14-22-14 13-60z" class="coral o"/>
{card(470, 250, 0.95, 'blue')}
<path d="M470 292v60" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>
<path d="M60 386h480" class="a"/>
""")

add('mrs', '手を上げて指輪を見せている女性と、ハートのイラスト。', '既婚の女性に付ける敬称「〜夫人、〜さん」。', f"""
{person(280, 352, 1.3, 1, 'violet', 'blue', 'reach', 'bob', 'smile')}
<circle cx="361" cy="222" r="16" fill="none" stroke="{GLD}" stroke-width="8"/>
<circle cx="361" cy="222" r="16" fill="none" stroke="{GLDD}" stroke-width="3"/>
{heart(452, 236, 0.8, 'coral')}
{spark(520, 180, 0.8)}
<path d="M60 386h480" class="a"/>
""")

add('ms', '書類を抱えた女性が、白い名札のそばに立っているイラスト。', '既婚・未婚を問わない女性の敬称「〜さん」。', f"""
{person(270, 352, 1.3, 1, 'teal', 'blue', 'hold', 'bob', 'smile')}
{card(466, 250, 0.95, 'teal')}
<path d="M466 292v60" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>
<path d="M60 386h480" class="a"/>
""")

add('much', 'どんぶりにごはんが山のように盛られてこぼれそうなイラスト。', '数えられないものの「多くの」。much water / much money。', f"""
<g transform="translate(300 348)">
  <path d="M-144-52h288q-12 94-144 94T-144-52z" class="teal o"/>
  <path d="M-144-52h288" fill="none" stroke="{TEAD}" stroke-width="10"/>
  <path d="M-112-52q26-92 112-92t112 92z" class="goldp o"/>
  <g class="gold">{''.join(f'<circle cx="{x}" cy="{y}" r="7"/>' for x, y in [
      (-60, -78), (-20, -96), (26, -88), (70, -70), (0, -120), (52, -116), (-44, -110)])}</g>
</g>
<path d="M60 386h480" class="a"/>
""")

add('mum', '子どもを抱きしめているお母さんのイラスト。', 'お母さん。家の中で呼びかけるときの言い方。', f"""
{person(300, 352, 1.35, 1, 'coral', 'blue', 'hold', 'bob', 'smile')}
{person(300, 368, 0.72, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
<path d="M244 276q56 34 112 0" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
{heart(300, 176, 0.85, 'coral')}
<path d="M60 386h480" class="a"/>
""")

add('music', 'スピーカーから音符が飛び出しているイラスト。', '音楽。音を使って表す芸術。', f"""
{speaker(210, 246, 1.0, 'violet')}
{note(392, 168, 1.3, 'violet')}
{note(462, 240, 1.05, 'teal')}
{note(376, 296, 1.15, 'gold')}
<g fill="none" stroke="{VIO}" stroke-width="5" stroke-linecap="round">
  <path d="M300 178q44-24 74 0M300 232q54-26 88 0"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('must', 'チェック欄の並ぶ用紙と時計を前に、人が指をさしているイラスト。', '〜しなければならない（義務）。must は強い義務を表す。', f"""
<g transform="translate(180 190)">
  <path d="M-84-104h168v208h-168z" class="paper"/>
  <path d="M-32-120h64v18h-64z" class="goldd o"/>
  {''.join(f'<rect x="-60" y="{-74+i*42}" width="86" height="10" rx="5" fill="{MUTED}"/>'
           f'<path d="M20 {-66+i*42}l11 13 22-28" fill="none" stroke="{GRN}" stroke-width="6"'
           f' stroke-linecap="round" stroke-linejoin="round"/>' for i in range(4))}
</g>
{person(420, 352, 1.25, -1, 'gold', 'blue', 'point', 'short', 'neutral')}
{clock(496, 168, 46, 8, 40)}
<path d="M60 386h480" class="a"/>
""")

add('my', '自分のバッグを抱え、持ち主を示す弧が描かれたイラスト。', '私の。話し手が自分のものだと示す語。', f"""
{person(300, 352, 1.3, 1, 'violet', 'blue', 'hold', 'bob', 'smile')}
<g transform="translate(340 296)">
  <path d="M-56-44h112v88h-112z" class="coral o"/>
  <path d="M-32-44q0-42 32-42t32 42" fill="none" stroke="{CRLD}" stroke-width="9"/>
</g>
{arc(298, 236, 336, 258, 44)}
{heart(444, 216, 0.6, 'coral')}
<path d="M60 386h480" class="a"/>
""", arrow=True)

add('name', '白い名札を指さしている人のイラスト。', '名前。人や物を呼ぶときの語。', f"""
{person(210, 352, 1.25, 1, 'teal', 'blue', 'point', 'short', 'smile')}
<g transform="translate(390 250) rotate(-4)">
  <path d="M-100-62h200v124h-200z" class="paper"/>
  <rect x="-74" y="-32" width="148" height="20" rx="10" fill="{TONES['blue'][0]}"/>
  <rect x="-74" y="4" width="94" height="13" rx="6.5" fill="{MUTED}"/>
</g>
<path d="M300 272h28" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
<path d="M60 386h480" class="a"/>
""")

add('nappy', '寝ている赤ちゃんのおむつを替えているイラスト。', 'おむつ。赤ちゃんが使う紙や布の下着。', f"""
{baby(300, 300, 1.25)}
{hand(452, 250, -1)}
{hand(150, 258, 1)}
<path d="M60 386h480" class="a"/>
""")

add('nausea', '口を手で押さえて気持ち悪そうにしているイラスト。', '吐き気、むかつき。乗り物酔いなどで感じる。', f"""
{person(290, 352, 1.25, 1, 'green', 'blue', 'hold', 'short', 'sad')}
{hand(326, 226, -1)}
{swirl(470, 200, 1.1, 'green')}
{swirl(140, 226, 0.85, 'green')}
<g transform="translate(486 342)">
  <path d="M-52 0q6-32 52-32t52 32z" class="paper"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('near', 'すぐ隣り合って建つ家と店の間に、短い両向きの矢印があるイラスト。', '〜の近くに、近い。距離が短いことを表す。', f"""
{house(170, 306, 0.95, 'coral')}
{building(430, 306, 0.9, 'teal')}
{line(300, 196, 300, 148, None, head=True)}
{line(300, 196, 300, 244, None, head=True)}
<g fill="none" stroke="{MUTED}" stroke-width="4">
  <path d="M182 330h236" stroke-dasharray="12 10"/>
</g>
<path d="M60 386h480" class="a"/>
""", arrow=True)

add('neighbor', '隣り合う2軒の家の間に塀があり、2人が塀ごしに手を振っているイラスト。', '隣人、近所の人。', f"""
{house(140, 306, 0.92, 'coral')}
{house(460, 306, 0.92, 'teal')}
{fence(300, 386, 0.8)}
{person(206, 352, 1.05, 1, 'blue', 'blue', 'up', 'bob', 'smile')}
{person(394, 352, 1.05, -1, 'violet', 'blue', 'up', 'short', 'smile')}
<path d="M60 386h480" class="a"/>
""")

add('neighborhood', '家や木が集まった住宅街のイラスト。', '近所、地域。自分が住むまわりの一帯。', f"""
{house(110, 306, 0.7, 'coral')}
{house(300, 306, 0.76, 'gold')}
{house(490, 306, 0.7, 'teal')}
{tree(200, 306, 0.82)}
{tree(400, 306, 0.75)}
<path d="M40 330h520" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="18 14"/>
{person(300, 352, 1.0, 1, 'blue', 'blue', 'walk', 'short', 'smile')}
<path d="M60 386h480" class="a"/>
""")

add('neighborhoods', '2つのまとまりに分かれて住宅街が広がっているイラスト。', '近所・地域の複数形。2つ以上の地域を指す。', f"""
{split(300)}
{house(70, 306, 0.56, 'coral')}
{house(180, 306, 0.6, 'gold')}
{house(400, 306, 0.56, 'teal')}
{house(510, 306, 0.6, 'blue')}
{tree(130, 306, 0.62)}
{tree(460, 306, 0.62)}
{person(230, 352, 0.9, 1, 'violet', 'blue', 'walk', 'short', 'smile')}
<path d="M60 386h480" class="a"/>
""")

add('never', 'クッキーのびんに手を伸ばしかけて、禁止の印が付いているイラスト。', '決して〜ない、一度も〜ない。場面としては「決して手を出さない」。', f"""
{table(300)}
{jar(430, 300, 0.95, 0.7, 'gold')}
{ban(430, 214, 54)}
{person(150, 352, 1.15, 1, 'blue', 'blue', 'reach', 'short', 'sad')}
<path d="M60 386h480" class="a"/>
""")

add('new', '箱から新品のくつが出されて、きらめいているイラスト。', '新しい、新品の。買ったばかりの状態。', f"""
{box(250, 300, 170, 116, 36, 'blue')}
<g transform="translate(320 246)">
  {shoe(0, 0, 1.05, 'coral', 1)}
</g>
{spark(452, 186, 1.2)}{spark(140, 200, 1.0)}{spark(300, 132, 1.1)}
<path d="M60 386h480" class="a"/>
""")

add('news', 'テレビ画面にニュースを読む人が映り、電波が広がっているイラスト。', 'ニュース、知らせ。テレビやラジオの報道。', f"""
<g transform="translate(240 200)">
  <path d="M-152-118h304v236h-304z" class="teald o"/>
  <path d="M-134-100h268v200h-268z" fill="#eaf4ff" class="o"/>
  <circle cx="-10" cy="-40" r="44" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-48-76q38-22 76 0" fill="{HAIR}"/>
  <circle cx="-26" cy="-44" r="4" class="ink"/><circle cx="6" cy="-44" r="4" class="ink"/>
  <path d="M-24-22q14 12 28 0" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-118 74h236v30h-236z" class="teal o"/>
  <path d="M40 44l50-30" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/>
  <circle cx="98" cy="6" r="16" fill="{MUTED}" class="o"/>
</g>
<g fill="none" stroke="{BLU}" stroke-width="6" stroke-linecap="round">
  <path d="M418 112a96 96 0 0 1 0 108M452 84a140 140 0 0 1 0 164"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('newspaper', '広げた新聞を読んでいる人のイラスト。', '新聞。news（知らせ）+ paper（紙）の語。', f"""
{sit(300, 352, 1.25, 1, 'blue', 'blue', 'short', 'neutral', 'lap')}
{chair(300, 352, 1.1, 'gold', 1)}
<g transform="translate(300 244)">
  <path d="M-116-74h232v148h-232z" class="paper"/>
  <path d="M-116-74h232v20h-232z" fill="{MUTED}"/>
  <g fill="{MUTED}">
    <rect x="-100" y="-38" width="84" height="10" rx="5"/><rect x="-100" y="-14" width="72" height="10" rx="5"/>
    <rect x="-100" y="10" width="84" height="10" rx="5"/><rect x="-100" y="34" width="62" height="10" rx="5"/>
    <rect x="8" y="-38" width="92" height="72" rx="4"/>
  </g>
  <path d="M0-74v148" fill="none" stroke="{INK}" stroke-width="2.5" stroke-dasharray="8 8"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('nice', '花を差し出して、笑顔で応えてもらっているイラスト。', 'よい、感じのよい、親切な。', f"""
{person(170, 352, 1.2, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{flower(276, 262, 0.95, 'coral')}
{person(440, 352, 1.2, -1, 'coral', 'blue', 'hold', 'bob', 'smile')}
{heart(356, 206, 0.6, 'coral')}
<path d="M60 386h480" class="a"/>
""")

add('night', '月と星が輝く夜空の下、窓明かりのついた家のイラスト。', '夜、夜間。日が沈んで暗くなった時間。', f"""
{''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fffefd"/>' for x, y, r in [
    (80, 66, 4), (170, 110, 3), (330, 58, 3), (470, 96, 4), (550, 60, 3)])}
{moon(456, 122, 52, 'gold')}
<path d="M0 306h600v94H0z" fill="#dfe6ee"/>
{house(220, 306, 1.0, 'violet')}
<rect x="196" y="252" width="34" height="30" rx="4" class="gold"/>
<rect x="256" y="252" width="34" height="30" rx="4" class="goldp"/>
{tree(70, 306, 0.8)}
""", bg='#e8eef7', ground=False)

add('nine', 'お盆の上に9つのボールが並んでいるイラスト。', '9、九。nine の数。', f"""
<g transform="translate(300 258)">
  <rect x="-192" y="-112" width="384" height="230" rx="20" class="goldp o"/>
  <rect x="-172" y="-92" width="344" height="190" rx="12" fill="#fffdf6" class="o"/>
  {''.join(f'<circle cx="{-110 + c*110}" cy="{-44 + r*92}" r="32" class="{CS[(r*3+c) % 6]} o"/>'
           for r in range(3) for c in range(3))}
</g>
""")

add('nineteen', '10のまとまりと9つのボールが並んでいるイラスト。', '19、十九。10と9に分けて数える数。', f"""
<g transform="translate(180 220)">
  <rect x="-172" y="-72" width="344" height="154" rx="14" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M{-138 + c*69} -72v154"/>' for c in range(1, 5))}
    <path d="M-172 5h344"/>
  </g>
  {''.join(f'<circle cx="{-138 + c*69}" cy="{-36 + r*78}" r="24" class="{CS[(r*5+c) % 6]} o"/>'
           for r in range(2) for c in range(5))}
</g>
{''.join(f'<circle cx="{432 + c*62}" cy="{160 + r*62}" r="25" class="{CS[(r*3+c) % 6]} o"/>'
         for r in range(3) for c in range(3))}
""")

add('ninety', '90この点が9列10行に並んでいるイラスト。', '90、九十。9が10集まった数。', f"""
<g>{''.join(f'<circle cx="{104 + c*43}" cy="{62 + r*36}" r="12" class="{CS[(r+c) % 6]}"/>'
            for r in range(9) for c in range(10))}</g>
""")

add('ninth', '9段の階段の一番上が輪で示され、旗が立っているイラスト。', '9番目の。順番が9番目であること。', f"""
<g>{''.join(f'<path d="M{60 + i*54} {386 - (i+1)*34}h54v{(i+1)*34}h-54z" class="goldp o"/>' for i in range(9))}</g>
{ring(513, 150, 66, dash=True)}
<g transform="translate(513 80)">
  <path d="M0 0v72" fill="none" stroke="{BRN}" stroke-width="8"/>
  <path d="M0 0h56l-14 18 14 18H0z" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('no', '手のひらを前に出して断り、そばに禁止の印があるイラスト。', 'いいえ、1つも〜ない。no は否定の返事。', f"""
{person(220, 352, 1.3, 1, 'blue', 'blue', 'give', 'short', 'neutral')}
{hand(330, 268, 1)}
{ban(452, 250, 62)}
<path d="M60 386h480" class="a"/>
""")

add('nobody', 'ベンチのそばに人の形の点線だけがあり、禁止の印が重なっているイラスト。', 'だれも〜ない。人が1人もいないこと。', f"""
{bench(170, 386, 1.1, 'gold')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="11 10">
  <circle cx="410" cy="196" r="36"/>
  <path d="M410 232v92M410 262l-46 28M410 262l46 28M410 324l-32 56M410 324l32 56"/>
</g>
{ban(410, 196, 64)}
<path d="M60 386h480" class="a"/>
""")

add('north', '方位磁針の針が上を指し、後ろに山がそびえるイラスト。', '北。方角としての北、北の方角。', f"""
{mountain(440, 306, 0.85, 'teal')}
<g transform="translate(180 246)">
  <circle r="102" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-102 0h204M0-102v204"/></g>
  <path d="M0-74l24 74-24-20-24 20z" class="coral o"/>
  <path d="M0 74l-24-74 24 20 24-20z" class="paper"/>
  <circle r="9" class="ink"/>
</g>
{arrowline([(180, 122), (180, 84)], None, 8)}
<path d="M60 386h480" class="a"/>
""", arrow=True)

add('nose', '人の顔の鼻の部分が輪で囲まれているイラスト。', '鼻。においを感じ、息をする器官。', f"""
{face(300, 178, 118, 'smile')}
<path d="M300 158q-18 38 0 50 16 10 30-4" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
{ring(300, 194, 84)}
<path d="M60 386h480" class="a"/>
""")

add('not', '切り替えの下がったスイッチと消えた電球に、打ち消しの印が付いているイラスト。', '〜でない、〜しない。動詞や文を打ち消す語。', f"""
{bulb(280, 300, 1.4, False)}
{cross(420, 224, 1.3)}
{switch(150, 300, 1.2, False)}
<path d="M212 246q40-26 62 0" fill="none" stroke="{MUTED}" stroke-width="5"/>
<path d="M60 386h480" class="a"/>
""")

add('nothing', 'ふたの開いた空の箱の中が、点線だけで示されているイラスト。', '何も〜ない。中身が全くないこと。', f"""
<g transform="translate(300 300)">
  <path d="M-124-52h248v112h-248z" class="gold o"/>
  <path d="M-124-52l42-42h248l-42 42z" class="goldp o"/>
  <path d="M124-52l42-42v112l-42 42z" class="goldd o"/>
  <path d="M-150-84l96-30" fill="none" stroke="{GLDD}" stroke-width="13" stroke-linecap="round"/>
  <rect x="-86" y="-24" width="172" height="72" rx="10" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 10"/>
</g>
{hand(470, 150, -1)}
<path d="M60 386h480" class="a"/>
""")

add('directions', '地図を持つ人に、もう1人が道を指して教えているイラスト。', '道順、行き方。また、指示や使い方。', f"""
{person(150, 352, 1.15, 1, 'gold', 'blue', 'hold', 'short', 'smile')}
{chart(166, 248, 0.9)}
{person(360, 352, 1.15, 1, 'teal', 'blue', 'point', 'bob', 'smile')}
{line(430, 268, 470, 250)}
{house(520, 306, 0.55, 'coral')}
<path d="M60 386h480" class="a"/>
""", arrow=True)

add('nun', '頭にベールをかぶり、胸の十字架に手を合わせているイラスト。', '修道女、尼僧。信仰のために暮らす女性。', f"""
<g transform="translate(300 196)">
  <path d="M-72 12q-8-86 72-86t72 86q0 38-26 48h-92q-26-10-26-48z" fill="#3f4f63" class="o"/>
</g>
{person(300, 352, 1.3, 1, 'blue', 'blue', 'carry', 'bob', 'smile')}
<path d="M284 284h32M300 266v46" fill="none" stroke="{GLD}" stroke-width="10" stroke-linecap="round"/>
<path d="M60 386h480" class="a"/>
""")

add('moisture', '冷えたグラスの表面に水滴がつき、湯気が立っているイラスト。', '湿気、水分。空気や物の表面にある水。', f"""
{glassmilk(300, 300, 1.5)}
<g class="blue">{''.join(f'<ellipse cx="{x}" cy="{y}" rx="6" ry="8"/>' for x, y in [
    (256, 240), (346, 226), (268, 280), (334, 292), (250, 318), (352, 322)])}</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M252 152q-16-20 0-38t0-34M300 140q-16-20 0-38t0-34M348 152q-16-20 0-38t0-34"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('of', 'オレンジから1房が取り出され、矢印で示されているイラスト。', '〜の、〜のうちの。全体から一部を取り出す関係。', f"""
<circle cx="230" cy="240" r="96" class="goldp o"/>
<g fill="none" stroke="{GLDD}" stroke-width="4">
  <path d="M230 144v192M134 240h192M162 172l136 136M298 172L162 308"/>
</g>
<circle cx="230" cy="240" r="96" fill="none" class="o"/>
<g transform="translate(452 216) rotate(16)">
  <path d="M0-58l50 32-18 58h-64l-18-58z" class="goldp o"/>
  <path d="M0-58v84M-28-26h56" fill="none" stroke="{GLDD}" stroke-width="4"/>
</g>
{arc(336, 220, 382, 208, -30)}
<path d="M60 386h480" class="a"/>
""", arrow=True)

add('off', 'スイッチが下に切り替わり、電球が消えているイラスト。', '（電源が）切れて。off は「離れて・切れて」が核。', f"""
{switch(170, 300, 1.4, False)}
<path d="M240 260q56-46 118-14" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="12 10"/>
{bulb(400, 300, 1.4, False)}
<path d="M60 386h480" class="a"/>
""")

add('office', '机の上のパソコンに向かって座って働く人のイラスト。', '事務所、会社。仕事をする部屋や組織。', f"""
<path d="M40 56h520v168H40z" fill="#f1ece0"/>
<rect x="72" y="84" width="140" height="106" rx="6" fill="#eaf4ff" class="o"/>
<path d="M142 84v106M72 138h140" fill="none" stroke="{INK}" stroke-width="4"/>
{chair(300, 352, 1.1, 'gold', 1)}
{sit(300, 352, 1.2, 1, 'blue', 'blue', 'short', 'smile', 'lap')}
<g transform="translate(300 272)">
  <path d="M-126 0h252v18h-252z" class="goldd o"/>
  <path d="M-100 18h16v58h-16zM84 18h16v58h-16z" fill="#a0764a"/>
</g>
{laptop(250, 258, 0.55, 'teal')}
{doc(392, 250, 62, 78, 3)}
{mug(470, 258, 0.55, 'coral')}
<path d="M60 386h480" class="a"/>
""")

add('often', '同じ動作を繰り返す矢印が、人をぐるりと囲んでいるイラスト。', 'しばしば、よく。頻度が高いことを表す副詞。', f"""
{person(300, 352, 1.2, 1, 'coral', 'blue', 'hold', 'bob', 'smile')}
{mug(322, 282, 0.85, 'gold', True)}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round" marker-end="url(#ar)">
  <path d="M170 302a132 132 0 1 1 30 76"/>
</g>
{clock(486, 152, 40, 3, 0)}
<path d="M60 386h480" class="a"/>
""", arrow=True)

add('oh', '驚いて口を開け、両手を上げているイラスト。', 'ああ、おや、あっ。驚きや気づきの声。', f"""
{person(300, 352, 1.35, 1, 'violet', 'blue', 'up', 'bob', 'surprised')}
{spark(196, 176, 1.2)}{spark(404, 176, 1.2)}{spark(300, 108, 1.4)}
<path d="M60 386h480" class="a"/>
""")

add('ok', '親指を立てた手と、緑のチェック印のイラスト。', '大丈夫な、問題ない。同意や承諾を表す。', f"""
{thumbup(240, 250, 1.7, 1)}
{tick(440, 240, 2.2)}
<path d="M60 386h480" class="a"/>
""")

add('old', '杖をついた年配の人が立っているイラスト。', '年老いた。また、古い、昔の。', f"""
{person(290, 352, 1.3, 1, 'blue', 'blue', 'stand', 'bun', 'smile')}
<path d="{HAIRS['bun']}" transform="translate(290 352) scale(1.3)" fill="#9aa6b1" stroke="#9aa6b1" stroke-width="2"/>
<path d="M266 246q24 20 48 0" fill="none" stroke="#cfd6dc" stroke-width="9" stroke-linecap="round"/>
{cane(380, 386, 1.0)}
<path d="M60 386h480" class="a"/>
""")

add('on', 'スイッチが上に入り、電球が明るくついているイラスト。', '（電源が）入って。on は「接触して・作動して」が核。', f"""
{switch(170, 300, 1.4, True)}
<path d="M240 268q56-46 118-16" fill="none" stroke="{MUTED}" stroke-width="6"/>
{bulb(400, 300, 1.4, True)}
<path d="M60 386h480" class="a"/>
""")

add('one', '台の上に1つだけボールが載り、輪で囲まれているイラスト。', '1、1つ。数が1であること。', f"""
<g transform="translate(300 380)">
  <path d="M-84 0h168v16h-168z" class="goldd o"/>
  <path d="M-60 16h18v22h-18zM42 16h18v22h-18z" fill="#a0764a"/>
</g>
{ball(300, 296, 42, 'coral')}
{ring(300, 300, 76)}
{spark(300, 174, 1.3)}
<path d="M60 386h480" class="a"/>
""")

add('online', 'ノートパソコンの上に電波の印が広がっているイラスト。', 'オンラインの、ネット上で。回線につながっている状態。', f"""
{laptop(300, 348, 1.25, 'teal')}
{wifi(300, 190, 1.3, 'blue')}
{cloud(300, 92, 0.8, 'blue')}
<path d="M60 386h480" class="a"/>
""")

add('only', '同じ形が並ぶ中で1つだけ色がつき、輪で示されているイラスト。', 'ただ〜だけ、唯一の。それ以外に無いことを表す。', f"""
{''.join(f'<circle cx="{106 + i*92}" cy="230" r="34" fill="none" stroke="{MUTED}" '
         f'stroke-width="4" stroke-dasharray="10 9"/>' for i in range(6) if i != 3)}
{ball(382, 230, 38, 'coral')}
{ring(382, 230, 66, dash=True)}
<path d="M60 386h480" class="a"/>
""")

add('open', '戸が外へ大きく開き、開く動きが弧の矢印で示されているイラスト。', '開ける、開く、開いている。', f"""
{doorframe(240, 356, 1.0, 'gold')}
{arc(320, 130, 448, 188, 54, dash=True)}
{person(470, 386, 1.05, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
<path d="M60 386h480" class="a"/>
""", arrow=True)

add('opinion', '手を上げて発言し、頭の上の吹き出しに電球が浮かぶイラスト。', '意見、考え。自分がどう思うかを述べたもの。', f"""
{person(270, 352, 1.25, 1, 'blue', 'blue', 'up', 'bob', 'smile')}
{bubble(436, 148, 1.05, 'gold', 1, 'none')}
{bulb(436, 206, 0.82, True)}
<path d="M338 208l52 34" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 9"/>
<path d="M60 386h480" class="a"/>
""")

add('opposite', '2人が背中合わせに立ち、左右反対向きの矢印が出ているイラスト。', '反対の、正反対の。向きや性質が逆であること。', f"""
{person(220, 352, 1.25, -1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(380, 352, 1.25, 1, 'coral', 'blue', 'stand', 'bob', 'smile')}
{line(300, 190, 196, 190, None, head=True)}
{line(300, 190, 404, 190, None, head=True)}
{split(300)}
<path d="M60 386h480" class="a"/>
""", arrow=True)

add('or', '道が二手に分かれ、それぞれ別の建物へ向かう矢印が描かれたイラスト。', 'または、それとも。2つのうちどちらか一方。', f"""
<g fill="none" stroke="#ded8cc" stroke-width="44" stroke-linecap="round">
  <path d="M330 400q-10-124-136-158"/>
  <path d="M330 400q10-124 130-160"/>
</g>
{house(180, 220, 0.6, 'coral')}
{building(486, 210, 0.6, 'teal')}
{line(246, 268, 152, 246, None, head=True)}
{line(420, 262, 494, 240, None, head=True)}
{person(330, 372, 0.85, 1, 'violet', 'blue', 'walk', 'short', 'smile')}
""", ground=True, arrow=True)

add('orange', 'オレンジの実と、切り分けた房と葉が描かれたイラスト。', 'オレンジ。色の名前にもなる果物。', f"""
<g transform="translate(220 244)">
  <circle r="88" class="gold o"/>
  <g fill="none" stroke="{GLDD}" stroke-width="3">
    <path d="M0-88v176M-88 0h176M-62-62l124 124M62-62L-62 62"/>
  </g>
  <circle r="88" fill="none" class="o"/>
  <path d="M4-86q56-36 92-4-38 32-92 4z" class="greenp o"/>
  <path d="M6-86q-10-40 8-62" fill="none" stroke="{GRND}" stroke-width="7" stroke-linecap="round"/>
</g>
<g transform="translate(452 300)">
  <path d="M0-58l48 32-18 58h-60l-18-58z" class="goldp o"/>
  <path d="M0-58v84M-30-26h60" fill="none" stroke="{GLDD}" stroke-width="4"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('order', '店員がお客の注文を書き取り、お客が指で示しているイラスト。', '注文する、注文。レストランで料理を頼む場面。順序の意味もある。', f"""
{table(300)}
{sit(150, 352, 1.15, 1, 'gold', 'blue', 'bob', 'smile', 'lap')}
{person(420, 352, 1.25, -1, 'teal', 'blue', 'hold', 'short', 'smile')}
<g transform="translate(386 248) rotate(-10)">
  <path d="M-52-66h104v132h-104z" class="paper"/>
  <path d="M-52-66h104v18h-104z" fill="{MUTED}"/>
  <g fill="{MUTED}">
    <rect x="-38" y="-32" width="76" height="8" rx="4"/>
    <rect x="-38" y="-10" width="58" height="8" rx="4"/>
    <rect x="-38" y="12" width="68" height="8" rx="4"/>
  </g>
  <path d="M52-44l32-26" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('other', '2つの箱のうち、もう一方へ矢印が向かっているイラスト。', 'ほかの、別の。今示したものではないほう。', f"""
{box(150, 300, 150, 112, 32, 'blue')}
{box(430, 300, 150, 112, 32, 'gold')}
{line(250, 214, 360, 214, INK, head=False)}
{arc(250, 218, 366, 218, 74)}
{ring(430, 300, 104, dash=True)}
<path d="M60 386h480" class="a"/>
""", arrow=True)

add('our', '3人が並んで立ち、全員が輪で囲まれているイラスト。', '私たちの。話し手を含む複数の所有を表す。', f"""
{house(300, 300, 0.95, 'gold')}
{person(140, 352, 1.05, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(300, 352, 1.05, 1, 'coral', 'blue', 'stand', 'bob', 'smile')}
{person(460, 352, 1.05, 1, 'blue', 'blue', 'stand', 'short', 'smile')}
<ellipse cx="300" cy="322" rx="248" ry="88" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 11"/>
<path d="M60 386h480" class="a"/>
""")

add('out', '開いた戸から外へ歩き出し、外向きの矢印が描かれたイラスト。', '外へ、外に。中から外へ出る動き。', f"""
{doorframe(120, 356, 1.0, 'gold')}
{person(420, 386, 1.2, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
{line(240, 240, 340, 240, None, dash=True, head=True)}
<path d="M60 386h480" class="a"/>
""", arrow=True)

add('oven glove', '鍋つかみをはめた手が、天板から熱い鉄板を引き出しているイラスト。', '鍋つかみ、オーブンミトン。熱いものを握る厚手の手袋。', f"""
<g transform="translate(470 300)">
  <path d="M-150-160h300v160h-300z" fill="#9aa4ad" class="o"/>
  <path d="M-130-142h260v142h-260z" fill="#3f4f63" class="o"/>
  <path d="M-96-56h192v56h-192z" class="bluep o"/>
</g>
{mitten(180, 268, 1.5, -22, 'coral')}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round">
  <path d="M300 150q-16-24 0-44t0-40M364 158q-16-24 0-44t0-40"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('over', '人が柵を跳び越えているイラスト。', '〜の上を越えて。越えていく動きを表す。', f"""
{fence(300, 386, 1.0)}
{person(300, 244, 1.1, 1, 'coral', 'blue', 'up', 'short', 'smile')}
{arc(180, 330, 430, 330, 128, dash=True)}
<path d="M60 386h480" class="a"/>
""", arrow=True)

add('page', '開いた本の1ページがめくられ、動きが矢印で示されているイラスト。', 'ページ。本や紙の1枚、1面。', f"""
<g transform="translate(300 220)">
  <path d="M-104-72h96v144h-96z" class="paper"/>
  <path d="M-104-72h96v144h-96z" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-4-80h10v160h-10z" class="teald o"/>
  <g transform="rotate(-22 0 -72)">
    <path d="M6-72h98v144H6z" class="paper"/>
    <path d="M6-72h98v144H6z" fill="none" stroke="{INK}" stroke-width="2.5"/>
  </g>
  <g fill="{MUTED}">
    <rect x="-88" y="-48" width="64" height="8" rx="4"/><rect x="-88" y="-26" width="52" height="8" rx="4"/>
    <rect x="-88" y="-4" width="64" height="8" rx="4"/><rect x="-88" y="18" width="44" height="8" rx="4"/>
  </g>
</g>
{arc(432, 128, 372, 104, 44)}
<path d="M60 386h480" class="a"/>
""", arrow=True)

add('paint', 'ローラーで壁にペンキを塗っているイラスト。', '塗る、描く。ペンキや絵の具で色をつける。', f"""
<g transform="translate(230 386)">
  <path d="M-190-260h380v260h-380z" fill="#fffdf6" class="o"/>
  <path d="M-190-260h190v260h-190z" class="coralp"/>
  <path d="M-190-260h190v260h-190z" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>
{person(470, 352, 1.2, -1, 'blue', 'blue', 'reach', 'short', 'smile')}
<g transform="translate(392 246) rotate(-34)">
  <rect x="-32" y="-58" width="64" height="36" rx="10" class="coral o"/>
  <path d="M0 26v44" fill="none" stroke="{MUTED}" stroke-width="10"/>
  <path d="M0 70v16" fill="none" stroke="{BRN}" stroke-width="13" stroke-linecap="round"/>
</g>
<g transform="translate(180 340)">
  <path d="M-44-56h88v56h-88z" class="coral o"/>
  <path d="M-50-56h100v-14h-100z" class="corald o"/>
  <path d="M-46-84q46-16 92 0" fill="none" stroke="{MUTED}" stroke-width="7"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('paintbrush', '絵筆の先から色のついた線が引かれているイラスト。', '絵筆、はけ。絵の具をつけて描く道具。', f"""
<g transform="translate(370 150) rotate(-16)">
  <path d="M-16-130h32v146h-32z" class="gold o"/>
  <path d="M-20-152h40v24h-40z" fill="{MUTED}" class="o"/>
  <path d="M-18 16h36q-4 50-18 50t-18-50z" class="blue o"/>
</g>
<path d="M366 216q-92 22-124 96t-96 58" fill="none" stroke="{BLU}" stroke-width="30"
      stroke-linecap="round" opacity="0.8"/>
<path d="M300 118q-64 20-88 62" fill="none" stroke="{BLU}" stroke-width="12"
      stroke-linecap="round" opacity="0.5"/>
<path d="M60 386h480" class="a"/>
""")

add('pair', '左右そろった1足のくつが並んでいるイラスト。', '1組、1対。2つで1組になるもの。', f"""
{shoe(230, 330, 1.1, 'coral', 1)}
{shoe(380, 330, 1.1, 'coral', -1)}
<path d="M250 288q56-40 108-6" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 9"/>
<path d="M60 386h480" class="a"/>
""")

add('panda', '竹を持って座っているパンダのイラスト。', 'パンダ。白黒の体をもつクマの仲間。', f"""
<g transform="translate(300 250)">
  <ellipse cy="66" rx="88" ry="78" fill="#fffefd" class="o"/>
  <ellipse cx="-72" cy="118" rx="36" ry="26" class="ink"/>
  <ellipse cx="72" cy="118" rx="36" ry="26" class="ink"/>
  <ellipse cx="-80" cy="40" rx="32" ry="46" transform="rotate(-18 -80 40)" class="ink"/>
  <ellipse cx="80" cy="40" rx="32" ry="46" transform="rotate(18 80 40)" class="ink"/>
  <circle cy="-42" r="72" fill="#fffefd" class="o"/>
  <circle cx="-58" cy="-92" r="27" class="ink"/>
  <circle cx="58" cy="-92" r="27" class="ink"/>
  <ellipse cx="-28" cy="-46" rx="21" ry="27" transform="rotate(-16 -28 -46)" class="ink"/>
  <ellipse cx="28" cy="-46" rx="21" ry="27" transform="rotate(16 28 -46)" class="ink"/>
  <circle cx="-28" cy="-46" r="7" fill="#fffefd"/><circle cx="28" cy="-46" r="7" fill="#fffefd"/>
  <ellipse cy="-14" rx="15" ry="11" fill="#fffefd" class="o"/>
  <path d="M0-4q-14 16-4 24" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(150 210) rotate(12)">
  <path d="M0-150v300" fill="none" stroke="{GRN}" stroke-width="17" stroke-linecap="round"/>
  <path d="M-9-80h18M-9-16h18M-9 48h18M-9 112h18" fill="none" stroke="{GRND}" stroke-width="5"/>
  <path d="M0-124q-52-16-66-58 46-6 66 58z" class="greenp o"/>
  <path d="M0-92q52-16 66-58-46-6-66 58z" class="greenp o"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('paper', '机の上に重ねた白い紙と鉛筆のイラスト。', '紙。書いたり包んだりする材料。', f"""
{table(300)}
{''.join(f'<g transform="translate(200 {266 - i*11}) rotate({-5 + i*3})">'
         f'<path d="M-92-72h184v144h-184z" class="paper"/></g>' for i in range(4))}
<g transform="translate(430 250) rotate(38)">
  <path d="M-12-96h24v150h-24z" class="gold o"/>
  <path d="M-12 54h24l-12 34z" fill="{SKIN}" class="o"/>
  <path d="M-12-96h24v-20h-24z" fill="{CRL}" class="o"/>
</g>
<path d="M60 386h480" class="a"/>
""")

add('parent', '親が子どもの手を引いて立っているイラスト。', '親。母親・父親のどちらも指す語。', f"""
{person(260, 352, 1.3, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{person(412, 352, 0.86, -1, 'gold', 'blue', 'up', 'short', 'smile')}
<circle cx="352" cy="256" r="15" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
{heart(336, 186, 0.55, 'coral')}
<path d="M60 386h480" class="a"/>
""")

add('park', '木とベンチのある公園で、人がボールを蹴っているイラスト。', '公園。木や芝生があって憩える場所。', f"""
{tree(110, 336, 1.0)}
{tree(500, 330, 0.9)}
{bench(300, 386, 0.95, 'gold')}
<path d="M60 386q120-40 200-6" fill="none" stroke="{MUTED}" stroke-width="14" stroke-linecap="round" opacity="0.55"/>
{soccer(430, 336, 28)}
{person(210, 352, 1.05, 1, 'coral', 'blue', 'walk', 'short', 'smile')}
<path d="M60 386h480" class="a"/>
""")

add('part', 'パズルの1ピースが抜き出され、矢印で示されているイラスト。', '部分、パーツ。全体を構成する1つ。', f"""
{''.join(piece(160 + c*74, 168 + r*74, 0.62, CS[(r*3+c) % 6])
        for r in range(2) for c in range(3) if not (r == 1 and c == 1))}
<path d="M210 200h96v96h-96z" fill="#fffaf1" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 10"/>
{piece(470, 300, 1.25, 'gold', 12)}
{arc(316, 202, 396, 268, 46)}
""", arrow=True)

add('partner', '2人が向かい合って長い箱を一緒に運んでいるイラスト。', '相棒、パートナー。一緒に何かをする相手。', f"""
{person(160, 352, 1.2, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{person(440, 352, 1.2, -1, 'coral', 'blue', 'give', 'bob', 'smile')}
<g transform="translate(300 264)">
  <path d="M-104-38h208v76h-208z" class="gold o"/>
  <path d="M-104-38h208l-24-24h-160z" class="goldp o"/>
</g>
<path d="M60 386h480" class="a"/>
""")

finish(__file__)
