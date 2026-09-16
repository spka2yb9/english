# -*- coding: utf-8 -*-
"""第199回: plus47(t〜z)の100語。"""
from kit import *


# --- この回で使う小物 --------------------------------------------------------

def bubble(x, y, s=1, cls='blue', f=1, lines=3):
    """せりふの吹き出し。"""
    g = [f'<g transform="translate({x} {y}) scale({s*f} {s})">',
         f'<path d="M-70-56h140a16 16 0 0 1 16 16v58a16 16 0 0 1-16 16H-16l-34 34 8-34h-28'
         f'a16 16 0 0 1-16-16v-58a16 16 0 0 1 16-16z" class="{cls}p o"/>']
    for i in range(lines):
        g.append(f'<rect x="-46" y="{-30+i*24}" width="{92-(i%3)*20}" height="11" rx="5.5" '
                 f'fill="{TONES[cls][0]}"/>')
    g.append('</g>')
    return ''.join(g)


def page(x, y, s=1, cls='blue', play=False):
    """ブラウザ風の画面(ウェブサイト)。"""
    g = [f'<g transform="translate({x} {y}) scale({s})">',
         f'<rect x="-124" y="-96" width="248" height="192" rx="14" class="paper"/>',
         f'<path d="M-124-66h248" fill="none" stroke="{INK}" stroke-width="3"/>']
    for i in range(3):
        g.append(f'<circle cx="{-104+i*22}" cy="-81" r="6" fill="{MUTED}"/>')
    g.append(f'<rect x="-104" y="-50" width="118" height="74" rx="8" class="{cls}p o"/>')
    if play:
        g.append(f'<path d="M-56-32l34 19-34 19z" class="{cls}"/>')
    else:
        g.append(f'<circle cx="-45" cy="-13" r="21" class="{cls}"/>')
    for i in range(4):
        g.append(f'<rect x="30" y="{-50+i*21}" width="{68-(i%2)*22}" height="10" rx="5" '
                 f'fill="{MUTED}"/>')
    g.append(f'<rect x="-104" y="40" width="118" height="10" rx="5" fill="{MUTED}"/>')
    g.append(f'<rect x="-104" y="60" width="78" height="10" rx="5" fill="{MUTED}"/>')
    g.append('</g>')
    return ''.join(g)


def calendar(x, y, s=1, cols=7, rows=3, mark=None, cls='coral'):
    """暦。mark は色を付けるマスの番号(0始まり)。"""
    cw, ch = 30, 30
    top = -rows * ch / 2 - 30
    g = [f'<g transform="translate({x} {y}) scale({s})">',
         f'<rect x="{-cols*cw/2-10}" y="{top}" width="{cols*cw+20}" height="{rows*ch+44}" '
         f'rx="12" class="paper"/>',
         f'<path d="M{-cols*cw/2-2} {top+22}h{cols*cw-16}" fill="none" stroke="{MUTED}" '
         f'stroke-width="5"/>',
         f'<path d="M{-cols*cw/2+24} {top-14}v16M{cols*cw/2-24} {top-14}v16" fill="none" '
         f'stroke="{TONES[cls][2]}" stroke-width="7" stroke-linecap="round"/>']
    for r in range(rows):
        for c in range(cols):
            i = r * cols + c
            cx = -cols * cw / 2 + c * cw
            cy = -rows * ch / 2 + r * ch
            if i == mark:
                g.append(f'<rect x="{cx+4}" y="{cy+4}" width="{cw-8}" height="{ch-8}" rx="6" '
                         f'class="{cls} o"/>')
            else:
                g.append(f'<rect x="{cx+4}" y="{cy+4}" width="{cw-8}" height="{ch-8}" rx="6" '
                         f'fill="{MUTED}" opacity="0.3"/>')
    g.append('</g>')
    return ''.join(g)


def marks(x, y, n, cols=6, r=20, cls='coral'):
    """n個の丸を並べ、最後の1個だけ色をつけて囲む(序数)。"""
    step = r * 2 + 14
    rows = (n + cols - 1) // cols
    g = [f'<g transform="translate({x} {y})">']
    for i in range(n):
        cx = -(cols-1) * step / 2 + (i % cols) * step
        cy = -(rows-1) * step / 2 + (i // cols) * step
        if i == n - 1:
            g.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" class="{cls} o"/>')
            g.append(f'<circle cx="{cx}" cy="{cy}" r="{r+13}" fill="none" '
                     f'stroke="{TONES[cls][0]}" stroke-width="4" stroke-dasharray="10 8"/>')
        else:
            g.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" class="{cls}p o"/>')
    g.append('</g>')
    return ''.join(g)


def car(x, y, s=1, cls='coral', f=1):
    """車。(x,y)は車輪の接地位置。"""
    return (f'<g transform="translate({x} {y}) scale({s*f} {s})">'
            f'<path d="M-92-19q-16 0-16-18v-14q0-14 16-18l28-6 20-26q8-10 22-10h34q14 0 20 10'
            f'l18 26 28 6q16 4 16 18v14q0 18-16 18z" class="{cls} o"/>'
            f'<path d="M-32-75h30v24h-52zM8-75h28l16 24H8z" class="bluep o"/>'
            f'<circle cx="-52" cy="-19" r="19" fill="{INK}"/>'
            f'<circle cx="-52" cy="-19" r="8" fill="{MUTED}"/>'
            f'<circle cx="54" cy="-19" r="19" fill="{INK}"/>'
            f'<circle cx="54" cy="-19" r="8" fill="{MUTED}"/></g>')


def toaster(x, y, s=1, cls='blue', up=1):
    """トースター。(x,y)は置いた面。up は食パンの出ている高さ。"""
    ty = -76 - 16 * up
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-58 0h116v-72a12 12 0 0 0-12-12h-92a12 12 0 0 0-12 12z" class="{cls} o"/>'
            f'<path d="M-36-84h72" fill="none" stroke="{TONES[cls][2]}" stroke-width="6" '
            f'stroke-linecap="round"/>'
            f'<rect x="40" y="-62" width="13" height="36" rx="6.5" fill="{MUTED}"/>'
            f'<rect x="38" y="-80" width="17" height="12" rx="4" class="{cls}d"/>'
            f'<g transform="translate(0 {ty})">'
            f'<path d="M-32 0h64v-54a10 10 0 0 0-10-10h-44a10 10 0 0 0-10 10z" class="goldp o"/>'
            f'</g></g>')


def gift(x, y, w=124, h=100, cls='coral', ribbon='gold'):
    """リボンをかけた贈り物の箱。(x,y)は中心。"""
    return (f'<g transform="translate({x} {y})">'
            f'<rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="8" class="{cls} o"/>'
            f'<rect x="-17" y="{-h/2}" width="34" height="{h}" class="{ribbon}"/>'
            f'<rect x="{-w/2}" y="-15" width="{w}" height="30" class="{ribbon}"/>'
            f'<rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="8" fill="none" class="o"/>'
            f'<path d="M-20 {-h/2}q-34-26-52-8-12 14 14 14 24 0 38-6z'
            f'M20 {-h/2}q34-26 52-8 12 14-14 14-24 0-38-6z" class="{ribbon} o"/></g>')


def mug(x, y, s=1, cls='blue'):
    """カップ。(x,y)は底。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-34-46h68v44a22 22 0 0 1-22 22h-24a22 22 0 0 1-22-22z" fill="#fffefd"/>'
            f'<path d="M-34-46h68v12h-68z" class="{cls}"/>'
            f'<path d="M-34-46h68v44a22 22 0 0 1-22 22h-24a22 22 0 0 1-22-22z" fill="none" '
            f'class="o"/>'
            f'<path d="M34-34h16a17 17 0 0 1 0 34H34" fill="none" stroke="{INK}" '
            f'stroke-width="7"/></g>')


def dog(x, y, s=1, f=1, cls='gold'):
    """犬。f=-1 で左向き。"""
    return (f'<g transform="translate({x} {y}) scale({s*f} {s})">'
            f'<path d="M-46 0l-6 28M-24 0l-4 30M30 0l6 30M46 0l6 28" fill="none" '
            f'stroke="{TONES[cls][2]}" stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M-58-30q-4-36 40-36h38q30 0 32 28 2 26-16 30h-78q-14-2-16-22z" '
            f'class="{cls} o"/>'
            f'<path d="M48-44q24-16 36 2 6 14-12 16-16 2-24-18z" class="{cls}d o"/>'
            f'<path d="M-58-42q-26-12-32-36 22 6 34 24z" class="{cls}d o"/>'
            f'<circle cx="70" cy="-40" r="4.5" class="ink"/>'
            f'<circle cx="74" cy="-34" r="6" fill="{INK}"/></g>')


def moon(x, y, r=40, cls='gold'):
    """三日月。"""
    return (f'<path d="M{x} {y-r}A{r} {r} 0 0 0 {x} {y+r}A{r*1.45} {r*1.45} 0 0 1 {x} {y-r}Z" '
            f'class="{cls} o"/>')


def heart(x, y, s=1, cls='coral'):
    """ハート。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0C-38-26-46-52-26-62-8-70 0-56 0-44 0-56 8-70 26-62 46-52 38-26 0 0Z" '
            f'class="{cls} o"/></g>')


def leaf(x, y, s=1, cls='gold'):
    """1枚の葉。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0q46-6 48-52-46 6-48 52z" class="{cls} o"/>'
            f'<path d="M2-4q18-18 40-42" fill="none" stroke="{TONES[cls][2]}" stroke-width="3"/>'
            f'</g>')


def snow(x, y, s=1, cls='blue'):
    """雪の結晶。"""
    g = ''.join(f'<path d="M{x} {y-s*17}V{y+s*17}" transform="rotate({d} {x} {y})"/>'
                for d in (0, 60, 120))
    return (f'<g fill="none" stroke="{TONES[cls][0]}" stroke-width="{4*s}" '
            f'stroke-linecap="round">{g}</g>')


def spiral(x, y, r=110, turns=3, cls='violet', sw=12):
    """渦巻き(竜巻・台風の雲)。"""
    n = int(turns * 18)
    pts = []
    for i in range(n + 1):
        t = i / n
        a = t * turns * 2 * math.pi
        pts.append((x + r * t * math.cos(a), y + r * t * math.sin(a)))
    d = 'M' + 'L'.join(f'{px:.0f} {py:.0f}' for px, py in pts)
    return (f'<path d="{d}" fill="none" stroke="{TONES[cls][0]}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def wavy(x, y, w=540, n=4, amp=13, cls='blue', sw=5):
    """波線(水面)。"""
    seg = w / (2 * n)
    d = f'M{x} {y}'
    for i in range(2 * n):
        d += f'q{seg/2:.0f} {amp if i % 2 == 0 else -amp} {seg:.0f} 0'
    return (f'<path d="{d}" fill="none" stroke="{TONES[cls][0]}" stroke-width="{sw}" '
            f'stroke-linecap="round"/>')


def pin(x, y, s=1, cls='coral'):
    """地図のピン。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0q-28-32-28-54a28 28 0 0 1 56 0q0 22-28 54z" class="{cls} o"/>'
            f'<circle cy="-54" r="11" fill="#fffefd" class="o"/></g>')


def mirror(x, y, s=1):
    """姿見の鏡。(x,y)は鏡の中心。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<ellipse rx="96" ry="130" class="goldd o"/>'
            f'<ellipse rx="82" ry="116" fill="#e2eef7" class="o"/>'
            f'<path d="M-30 134h60v16h-60z" class="gold o"/>'
            f'<path d="M-56 150h112" fill="none" stroke="{TONES["gold"][2]}" stroke-width="12" '
            f'stroke-linecap="round"/></g>')


def bulb(x, y, s=1, cls='gold'):
    """電球(ひらめき)。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<circle r="38" class="{cls}p o"/>'
            f'<path d="M-16 30h32v12a8 8 0 0 1-8 8h-16a8 8 0 0 1-8-8z" class="{cls}d o"/>'
            f'<path d="M-14 22h28M-12 32h24" fill="none" stroke="{TONES[cls][2]}" '
            f'stroke-width="4"/>'
            f'<path d="M-20-14q10-16 22-10" fill="none" stroke="#fffdf6" stroke-width="7" '
            f'stroke-linecap="round"/>'
            f'{spark(0,-62,0.9,cls)}{spark(-48,-32,0.7,cls)}{spark(48,-32,0.7,cls)}</g>')


def rainbow(x, y, r=150, w=16):
    """虹。(x,y)は両端の地面。"""
    cols = ['coral', 'gold', 'green', 'blue', 'violet']
    g = []
    for i, c in enumerate(cols):
        rad = r - i * w
        g.append(f'<path d="M{x-rad} {y}a{rad} {rad} 0 0 1 {2*rad} 0" fill="none" '
                 f'stroke="{TONES[c][0]}" stroke-width="{w}" stroke-linecap="round"/>')
    return ''.join(g)


def boat(x, y, s=1, cls='teal'):
    """ヨット。(x,y)は船体の底。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0-152v152" fill="none" stroke="{BRN}" stroke-width="8" '
            f'stroke-linecap="round"/>'
            f'<path d="M-8-146q-62 62-68 116h76z" fill="#fffefd" class="o"/>'
            f'<path d="M8-140q58 62 62 110H8z" class="{cls}p o"/>'
            f'<path d="M-92 0h184l-30 40H-62z" class="{cls} o"/></g>')


def footprint(x, y, s=1, f=1, rot=0):
    """足あと。"""
    return (f'<g transform="translate({x} {y}) scale({s*f} {s}) rotate({rot})">'
            f'<ellipse rx="13" ry="19" fill="{MUTED}" opacity="0.55"/>'
            f'<ellipse cy="-24" rx="8" ry="7" fill="{MUTED}" opacity="0.55"/></g>')


def umbrella(x, y, s=1, cls='coral', dash=False):
    """かさ。(x,y)はかさの骨の中央下。"""
    d = ' stroke-dasharray="10 8"' if dash else ''
    c = MUTED if dash else TONES[cls][0]
    fill = 'none' if dash else TONES[cls][1]
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-84 0q6-56 84-56t84 56q-28-14-42 0-14-14-28 0-14-14-28 0-14-14-28 0'
            f'-14-14-42 0z" fill="{fill}" stroke="{c}" stroke-width="4"{d}/>'
            f'<path d="M0-56v70q0 22-24 22" fill="none" stroke="{BRN}" stroke-width="8" '
            f'stroke-linecap="round"{d}/></g>')


def snowman(x, y, s=1):
    """雪だるま。(x,y)は底。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-32-98l-48 22M32-98l48 22" fill="none" stroke="{BRN}" stroke-width="7" '
            f'stroke-linecap="round"/>'
            f'<circle cy="-58" r="48" class="paper"/>'
            f'<circle cy="-140" r="34" class="paper"/>'
            f'<path d="M-34-110q34 16 68 0" fill="none" stroke="{TONES["coral"][0]}" '
            f'stroke-width="10"/>'
            f'<path d="M18-104q12 12 4 28" fill="none" stroke="{TONES["coral"][2]}" '
            f'stroke-width="10" stroke-linecap="round"/>'
            f'<path d="M-30-172h60v12h-60z" class="coral o"/>'
            f'<path d="M-18-172h36v-30h-36z" class="coral o"/>'
            f'<circle cx="-12" cy="-146" r="4.5" class="ink"/>'
            f'<circle cx="12" cy="-146" r="4.5" class="ink"/>'
            f'<path d="M0-138l26 10-26 10z" class="gold o"/>'
            f'<circle cy="-58" r="5" class="ink"/><circle cx="0" cy="-40" r="5" class="ink"/>'
            f'</g>')


def bed(x, y, s=1, cls='blue'):
    """ベッド。(x,y)は床。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-150 0v-118h22v118z" class="goldd o"/>'
            f'<path d="M-150-44h300v20h-300z" class="gold o"/>'
            f'<path d="M-140-44v44M140-44v44" fill="none" stroke="{BRN}" stroke-width="12" '
            f'stroke-linecap="round"/>'
            f'<path d="M-142-58h284v16h-284z" fill="#fffefd" class="o"/>'
            f'<path d="M-134-58h104v-30a14 14 0 0 1 14-14h34a14 14 0 0 1 14 14v30z" '
            f'fill="#fffefd" class="o"/>'
            f'<path d="M-26-58q0-24 26-24h108q26 0 26 24z" class="{cls} o"/></g>')


def frame(x, y, s=1, cls='gold'):
    """写真立て。(x,y)は中心。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect x="-134" y="-100" width="268" height="200" rx="12" class="{cls}d o"/>'
            f'<rect x="-116" y="-82" width="232" height="164" fill="#fffdf6" class="o"/>'
            f'<path d="M-70 100h140v14h-140z" class="{cls} o"/></g>')


def ladder(x, y, h=210, w=54, cls='gold'):
    """はしご。(x,y)は脚もと。"""
    n = int((h - 40) // 30) + 1
    rungs = ''.join(f'<path d="M{-w/2} {-24-i*30}h{w}"/>' for i in range(n))
    return (f'<g transform="translate({x} {y})">'
            f'<path d="M{-w/2} 0v-{h}M{w/2} 0v-{h}" fill="none" stroke="{TONES[cls][2]}" '
            f'stroke-width="10" stroke-linecap="round"/>'
            f'<g fill="none" stroke="{TONES[cls][0]}" stroke-width="7" '
            f'stroke-linecap="round">{rungs}</g></g>')


def desk(x, y, w=340):
    """机。(x,y)は天板の上面。"""
    return (f'<g transform="translate({x} {y})">'
            f'<path d="M{-w/2} 0h{w}v20h-{w}z" class="gold o"/>'
            f'<path d="M{-w/2+22} 20v70M{w/2-22} 20v70" fill="none" stroke="{GLDD}" '
            f'stroke-width="16" stroke-linecap="round"/></g>')


def wall(x, y, w=520, h=300):
    """れんがの壁。(x,y)は左上。"""
    bw, bh = 118, 56
    g = [f'<g transform="translate({x} {y})">',
         f'<rect width="{w}" height="{h}" fill="#dcc8a4" class="o"/>',
         '<g fill="none" stroke="#b49571" stroke-width="5">']
    for r in range(int(h // bh)):
        g.append(f'<path d="M0 {r*bh}h{w}"/>')
        x0 = 0 if r % 2 == 0 else bw // 2
        while x0 < w:
            if 0 < x0 < w:
                g.append(f'<path d="M{x0} {r*bh}v{bh}"/>')
            x0 += bw
    g.append('</g></g>')
    return ''.join(g)


def lotus(x, y, s=1, cls='violet'):
    """あぐらをかいて座った人(ヨガ)。(x,y)は座面。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-100 0q34-42 100-42t100 42q-44 26-100 26T-100 0z" class="{cls}d o"/>'
            f'<path d="M-46-18q46-16 92 0l-10-94h-72z" class="{cls} o"/>'
            f'<path d="M-40-104l-42 76M40-104l42 76" fill="none" stroke="{SKIN}" '
            f'stroke-width="13" stroke-linecap="round"/>'
            f'<circle cy="-140" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>'
            f'<path d="M-32-148q10-9 20 0M12-148q10-9 20 0" fill="none" stroke="{INK}" '
            f'stroke-width="3" stroke-linecap="round"/>'
            f'<path d="M-10-122q10 7 20 0" fill="none" stroke="{INK}" stroke-width="3"/>'
            f'<path d="M-34-162q34-26 68 0" fill="{HAIR}"/></g>')


# --- t ----------------------------------------------------------------------

add('tired', 'いすにぐったり腰かけて肩を落とし、頭の上に疲れの波線が漂うイラスト。',
    '疲れて力が入らず、ぐったりしているようす。', f"""
{chair(240,352,1.15,'gold')}
{sit(240,352,1.15,1,'blue','blue','short','sad','down')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M372 150q-16-18 0-36t0-34M428 176q-16-18 0-36t0-34M310 126q-14-16 0-32t0-30"/>
</g>
{drop(196,190,0.9,'blue')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('to', '点線の道にそって、駅のような建物へ歩いていくイラスト。',
    '行き先や到達点を表す前置詞「〜へ、〜に」。', f"""
{person(170,352,1.2,1,'teal','blue','walk','short','smile')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3" stroke-dasharray="12 10">
  <path d="M242 366q110-14 176-14"/>
</g>
{arrowline([(240,362),(300,354),(360,346)], TONES['blue'][0], 5)}
{building(470,336,0.95,'coral')}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('toasters', 'カウンターに2台のトースターが並び、どちらからも食パンが飛び出しているイラスト。',
    'パンを焼く道具トースターの複数形。', f"""
{table(300)}
{toaster(180,300,1.0,'blue',1)}
{toaster(420,300,1.0,'coral',1)}
{spark(180,112,0.9)}{spark(420,118,0.8)}{spark(300,96,0.7)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('today', '暦のまん中のマスが色づき、その上に太陽がかがやいているイラスト。',
    '今この日を指す「今日」。', f"""
{calendar(300,196,1.05,7,3,10)}
{sun(150,124,40)}
{person(504,352,1.0,-1,'teal','blue','point','short','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('together', '二人が左右から同じ大きな箱をかかえて持ち上げているイラスト。',
    '同じ場所でいっしょに、まとまって。', f"""
{person(205,352,1.15,1,'teal','blue','carry','short','smile')}
{person(395,352,1.15,-1,'coral','blue','carry','bob','smile')}
{box(300,262,180,96,30,'gold')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M60 330h50M490 330h50"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('toilet', '便器とタンク、壁のトイレットペーパーが並んでいるイラスト。',
    '用を足す場所、便所。', f"""
<g transform="translate(300 348)">
  <path d="M-62-200h124a10 10 0 0 1 10 10v70h-144v-70a10 10 0 0 1 10-10z" class="paper"/>
  <path d="M-74-120h148v18h-148z" class="paper"/>
  <path d="M-46-84h92l-16 84h-60z" class="paper"/>
  <ellipse cy="-92" rx="62" ry="22" class="bluep o"/>
  <ellipse cy="-92" rx="36" ry="12" fill="#fffefd" class="o"/>
  <rect x="-16" y="-216" width="32" height="16" rx="7" class="blue"/>
  <path d="M-62-200h124a10 10 0 0 1 10 10v70h-144v-70a10 10 0 0 1 10-10z" fill="none" class="o"/>
  <path d="M-74-120h148" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<g transform="translate(500 210)">
  <circle r="32" class="paper"/>
  <circle r="13" fill="#fffefd" class="o"/>
  <circle r="32" fill="none" class="o"/>
  <path d="M-32 0h-46" fill="none" stroke="{MUTED}" stroke-width="8" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tomato', 'へたのついた丸いトマトと、切って種が見えるトマトのイラスト。',
    '赤くて丸い野菜、トマト。', f"""
<g transform="translate(200 250)">
  <circle r="82" class="coral o"/>
  <path d="M0-80q-40-6-56-40 44-8 60 30zM0-80q40-6 56-40-44-8-60 30z" class="greenp o"/>
  <path d="M0-84v-30" fill="none" stroke="{GRND}" stroke-width="9" stroke-linecap="round"/>
  <path d="M2-112q-10-18 4-30 12-12 28-12-6 22-32 42z" class="green o"/>
</g>
<g transform="translate(424 258)">
  <circle r="74" class="coral o"/>
  <circle r="58" class="coralp o"/>
  <g fill="{TONES['gold'][0]}">{''.join(f'<ellipse cx="{x}" cy="{y}" rx="7" ry="11"/>'
      for x, y in [(-28,2),(-8,10),(14,4),(30,12),(2,-6),(-18,-10)])}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tomorrow', '暦の次のマスへ矢印がのび、そばで朝日がのぼっているイラスト。',
    'これから来る次の日、明日。', f"""
{calendar(300,196,1.05,7,3,11)}
<g transform="translate(300 196) scale(1.05)">
  {arrowline([(-6,-15),(10,-15)], TONES['coral'][0], 4)}
</g>
{sun(122,206,34)}
{person(504,352,1.0,-1,'teal','blue','point','short','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('tongs', 'トングでフライパンのソーセージをはさみ、裏返そうとしているイラスト。',
    '2本の腕で物をつかむ台所の道具、トング。', f"""
<g transform="translate(300 356)">
  <ellipse rx="132" ry="30" fill="#5b6572" class="o"/>
  <ellipse cy="-4" rx="114" ry="22" fill="#7d8794"/>
  <path d="M132-4h74" fill="none" stroke="{BRN}" stroke-width="14" stroke-linecap="round"/>
  <ellipse cx="-16" cy="-16" rx="60" ry="20" class="coral o"/>
  <path d="M-44-26q28-8 58 0" fill="none" stroke="{CRLD}" stroke-width="5"/>
</g>
<g transform="translate(300 74) rotate(-10)">
  <path d="M-9 14q-34 110-64 244M9 14q34 110 64 244" fill="none" stroke="{MUTED}"
    stroke-width="14" stroke-linecap="round"/>
  <path d="M-9 14q-34 110-64 244M9 14q34 110 64 244" fill="none" stroke="{INK}"
    stroke-width="2.5"/>
  <circle r="15" class="goldd o"/>
</g>
""", ground=True)

add('tonight', '夜の空に月と星が光り、家の窓だけがあたたかく灯っているイラスト。',
    '今日の夜、今夜。', f"""
{house(300,344,1.3,'coral')}
<rect x="219" y="234" width="46" height="40" rx="4" class="goldp o"/>
{moon(470,110,44,'gold')}
{spark(120,90,0.9)}{spark(200,166,0.7)}{spark(76,220,0.6)}{spark(524,226,0.8)}
{spark(560,86,0.6)}
<path d="M60 386h480" class="a"/>
""", ground=True, bg='#e6ecf6')

add('too', '荷物をつめすぎてスーツケースから服があふれ、ふたが閉まらないイラスト。',
    '「〜すぎる」「〜もまた」を表す副詞。', f"""
<g transform="translate(300 336)">
  <path d="M-36-118v-22a36 36 0 0 1 72 0v22" fill="none" stroke="{VIOD}" stroke-width="12"
    stroke-linecap="round"/>
  <path d="M-152-118h304v102a16 16 0 0 1-16 16h-272a16 16 0 0 1-16-16z" class="violet o"/>
  <path d="M-152-118h304" fill="none" stroke="{VIOD}" stroke-width="9"/>
  <path d="M-108-118h30v118h-30zM78-118h30v118h-30z" class="violetd o"/>
  <path d="M-70-118q-30-44 4-60t48 26z" class="coral o"/>
  <path d="M18-120q-4-46 32-50t42 34z" class="bluep o"/>
  <path d="M96-122q22-30 54-20" fill="none" stroke="{TONES['gold'][0]}" stroke-width="9"
    stroke-linecap="round"/>
</g>
{drop(196,150,0.8,'blue')}
{drop(414,158,0.7,'blue')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tooth', '白く光る歯と、そばに立てかけた歯ブラシのイラスト。',
    '口の中にあって物をかむ、歯。', f"""
<g transform="translate(240 244)">
  <path d="M0-86c46 0 78 30 78 68 0 22-9 30-13 52-5 24-9 38-22 38-16 0-16-27-25-45-5-9-7-13-18-13
    s-13 4-18 13c-9 18-9 45-25 45-13 0-17-14-22-38-4-22-13-30-13-52 0-38 32-68 78-68z"
    class="paper"/>
  <path d="M-44-44q28-18 64-12" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
{spark(196,118,1.0)}{spark(330,132,0.8)}{spark(160,300,0.7)}
<g transform="translate(474 240) rotate(14)">
  <path d="M-14-104h28v116a14 14 0 0 1-28 0z" class="blue o"/>
  <rect x="-16" y="-136" width="32" height="34" rx="9" class="bluep o"/>
  <g fill="#fffefd">{''.join(f'<rect x="-11" y="{-128+i*11}" width="22" height="5" rx="2.5"/>'
      for i in range(3))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('toothpick', 'つまようじに刺したチーズとオリーブを皿にのせ、予備の1本も置いてあるイラスト。',
    '食べ物に刺して使う小さな木のつまようじ。', f"""
<g transform="translate(300 352)">
  <ellipse rx="158" ry="32" class="paper"/>
  <ellipse rx="138" ry="24" fill="none" class="o"/>
  <g transform="translate(-18 -30)">
    <rect x="-36" y="-36" width="72" height="72" rx="8" class="goldp o"/>
    <circle cy="-66" r="25" class="green o"/>
    <circle cy="-104" r="19" class="coral o"/>
    <path d="M-56-166L10-44" fill="none" stroke="{BRN}" stroke-width="10" stroke-linecap="round"/>
  </g>
  <path d="M92-6l60-20" fill="none" stroke="{BRN}" stroke-width="10" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('topic', '向かい合った二人の間の吹き出しに、話題を表す語のブロックが並んでいるイラスト。',
    '話の中心になる題材、話題。', f"""
{person(150,352,1.15,1,'teal','blue','point','short','smile')}
{person(450,352,1.15,-1,'violet','blue','point','bob','smile')}
{bubble(300,206,1.2,'blue',1,3)}
{word(300,202,5,26)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tornado', '太い雲から細い漏斗がのびて地上に達し、木や瓦が巻き上げられているイラスト。',
    '激しい風が渦を巻いて地上を襲う竜巻。', f"""
{cloud(300,76,1.7,'violet')}
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="14" stroke-linecap="round">
  <path d="M176 148q124 26 248 0"/>
  <path d="M204 196q96 24 192 0"/>
  <path d="M232 244q68 20 136 0"/>
  <path d="M256 288q44 16 88 0"/>
</g>
<g transform="translate(112 350) rotate(-24)">
  <path d="M-8 0h16v-80h-16z" class="goldd"/>
  <circle cy="-96" r="36" class="greenp o"/>
</g>
<g fill="{MUTED}">
  <rect x="432" y="152" width="24" height="15" rx="3" transform="rotate(22 444 159)"/>
  <rect x="474" y="238" width="19" height="13" rx="3" transform="rotate(-32 483 244)"/>
  <rect x="398" y="300" width="21" height="14" rx="3" transform="rotate(42 408 307)"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('town', '背の高い建物と家が道に沿って並び、街灯が立っているイラスト。',
    '家や店が集まってできた町。', f"""
{tower(110,336,0.72,'blue',4)}
{building(272,336,0.82,'teal')}
{house(418,336,0.8,'coral')}
{house(520,336,0.6,'violet')}
<path d="M40 344h520" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="16 12">
  <path d="M60 374h480"/>
</g>
<path d="M186 348v-126" fill="none" stroke="{BRN}" stroke-width="8" stroke-linecap="round"/>
<circle cx="186" cy="216" r="15" class="goldp o"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('town hall', '柱と時計、屋上の旗がついた石造りの市役所のイラスト。',
    '町の行政の中心になる建物、市役所。', f"""
<g transform="translate(300 344)">
  <path d="M-236 0h472v-124h-472z" fill="#fffdf6" class="o"/>
  <path d="M-258-124L0-198l258 74z" class="teal o"/>
  <circle cy="-156" r="27" class="paper"/>
  <path d="M0-176v16M0-176l14 8" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  {''.join(f'<rect x="{x}" y="-108" width="32" height="108" rx="4" class="teal o"/>'
           for x in (-186, -116, 84, 154))}
  <path d="M-36 0v-76h72V0z" class="teald o"/>
  <circle cx="12" cy="-38" r="5" class="gold"/>
  <path d="M-258 0h516v-16h-516z" fill="#ded3c2" class="o"/>
  <path d="M-282 0h564v14h-564z" fill="#e8ddcb" class="o"/>
  <path d="M0-198v-58" fill="none" stroke="{BRN}" stroke-width="7" stroke-linecap="round"/>
  <path d="M3-254l56 14-56 18z" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tracksuit', '白いラインの入った上下そろいの服を着て走っているイラスト。',
    '運動着の上下そろい、ジャージ。', f"""
{person(300,352,1.3,1,'blue','blue','walk','short','smile')}
<g transform="translate(300 352) scale(1.3)">
  <path d="M-12-8l-26 33M12-8l28 28M-22-70l-28 29M22-70l31 24" fill="none"
    stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round"/>
  <path d="M-18-74v64" fill="none" stroke="{TONES['blue'][2]}" stroke-width="5"
    stroke-linecap="round"/>
  <path d="M-10-80q10 12 20 0" fill="none" stroke="{TONES['blue'][2]}" stroke-width="6"
    stroke-linecap="round"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round">
  <path d="M62 240h54M46 292h46"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('trade-off', '天秤の片方に金貨、もう片方に時計がのり、つり合わずに傾いているイラスト。',
    '一方を取れば他方をあきらめる、二者択一の妥協。', f"""
{scales(300, 290, -8)}
<g transform="translate(300 290) rotate(-8)">
  <g transform="translate(-110 -128)">{coin(0,0,24)}</g>
  <g transform="translate(110 -128)">{clock(0,0,26,3,9)}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('traffic', '道路に車が数珠つなぎに並び、信号が赤くともっているイラスト。',
    '道を行き交う車や人の流れ、交通。', f"""
<path d="M0 352h600v54H0z" fill="#6d7783"/>
<g fill="none" stroke="#fffefd" stroke-width="5" stroke-dasharray="28 22">
  <path d="M0 380h600"/>
</g>
{car(170,352,0.78,'coral',1)}
{car(340,352,0.78,'blue',1)}
{car(500,352,0.78,'teal',1)}
<g transform="translate(52 194)">
  <rect x="-26" y="-90" width="52" height="150" rx="16" fill="#3d4855" class="o"/>
  <circle cy="-58" r="15" class="coral"/>
  <circle cy="-14" r="15" fill="#5d6874"/>
  <circle cy="30" r="15" fill="#5d6874"/>
  <path d="M0 60v104" fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round"/>
</g>
""", ground=True)

add('travel', 'スーツケースを引いて歩く人と、空を飛ぶ飛行機のイラスト。',
    '遠くへ出かけること、旅行。', f"""
{person(240,352,1.2,1,'teal','blue','walk','short','smile')}
<g transform="translate(348 344) rotate(-6)">
  <path d="M-16-68v-14a16 16 0 0 1 32 0v14" fill="none" stroke="{VIOD}" stroke-width="9"
    stroke-linecap="round"/>
  <rect x="-52" y="-68" width="104" height="68" rx="10" class="violet o"/>
  <path d="M-52-42h104" fill="none" stroke="{VIOD}" stroke-width="6"/>
  <circle cx="-30" cy="8" r="9" fill="{INK}"/><circle cx="30" cy="8" r="9" fill="{INK}"/>
</g>
<path d="M320 330q-34-8-60-10" fill="none" stroke="{MUTED}" stroke-width="5"
  stroke-linecap="round"/>
{plane(462, 146, 0.72, 0, 'blue')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tree', '幹の太い大きな木が枝を広げ、実がいくつかなっているイラスト。',
    '幹と枝のある大きな植物、木。', f"""
{tree(300,352,2.1)}
<g class="gold">{''.join(f'<circle cx="{x}" cy="{y}" r="13"/>'
    for x, y in [(232,208),(362,190),(300,152),(258,272),(376,262)])}</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('true', '書類の上に大きな緑のチェックが描かれているイラスト。',
    '事実に合っていて正しい、本当の。', f"""
{doc(300,220,168,214,5)}
{tick(300,214,1.5)}
{spark(140,120,1.0)}{spark(470,130,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('grower', 'じょうろで畑の野菜の苗に水をやっている人のイラスト。',
    '作物を育てて出荷する人、栽培者。', f"""
{person(150,352,1.2,1,'teal','blue','reach','short','smile')}
<g transform="translate(272 232) rotate(18)">
  <rect x="-52" y="-40" width="104" height="78" rx="10" class="blue o"/>
  <path d="M-52-40h104" fill="none" stroke="{BLUD}" stroke-width="7"/>
  <path d="M52-22l50-32" fill="none" stroke="{BLUD}" stroke-width="18" stroke-linecap="round"/>
  <path d="M52-22l50-32" fill="none" stroke="{BLU}" stroke-width="7"/>
  <path d="M-26-40q-6-46 26-46" fill="none" stroke="{BLUD}" stroke-width="9"
    stroke-linecap="round"/>
</g>
<g class="blue">{''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>'
    for x, y, r in [(384,232,7),(400,278,6),(420,318,6),(360,300,6),(410,240,5)])}</g>
<g transform="translate(478 350)">
  <path d="M-124 0h248v-14a10 10 0 0 0-10-10h-228a10 10 0 0 0-10 10z" fill="#c9a464" class="o"/>
  {''.join(f'<path d="M{-104+i*52} -14q0-30-12-46" fill="none" stroke="{GRND}" '
           f'stroke-width="8" stroke-linecap="round"/>' for i in range(5))}
  {''.join(f'<path d="M{-104+i*52} -54q-20-4-26-22 20-4 28 14z" class="greenp o"/>'
           for i in range(5))}
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('turn', '道が右手へ曲がっていて、車がそのカーブにそって進んでいくイラスト。',
    '進む向きを変える、曲がる。', f"""
<g fill="none" stroke="#6d7783" stroke-width="56" stroke-linecap="round">
  <path d="M30 366h250q120 0 134-108"/>
</g>
<g fill="none" stroke="#fffefd" stroke-width="4" stroke-dasharray="22 20">
  <path d="M30 366h250q120 0 134-108"/>
</g>
{car(196,352,0.72,'coral',1)}
{arrowline([(364,300),(396,232)], TONES['coral'][0], 6, True)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('twelfth', '12個の丸が並び、最後の12番目だけが色づいて点線で囲まれているイラスト。',
    '12番目であることを表す数詞。', f"""
{marks(300,214,12,6,20)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('twelve', '12個の卵がきっちり収まった卵パックのイラスト。',
    '12、十二という数。', f"""
<g transform="translate(300 230)">
  <rect x="-186" y="-104" width="372" height="208" rx="24" class="gold o"/>
  <g>{''.join(f'<ellipse cx="{-150+c*60}" cy="{-52+r*104}" rx="27" ry="33" class="goldd"/>'
              for r in range(2) for c in range(6))}</g>
  <g>{''.join(f'<ellipse cx="{-150+c*60}" cy="{-56+r*104}" rx="27" ry="33" class="paper"/>'
              for r in range(2) for c in range(6))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('twentieth', '20個の丸が並び、最後の20番目だけが色づいて点線で囲まれているイラスト。',
    '20番目であることを表す数詞。', f"""
{marks(300,200,20,5,18)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('twenty', '金貨が10枚ずつ2列、全部で20枚ならべられているイラスト。',
    '20、二十という数。', f"""
<g class="gold">{''.join(f'<circle cx="{102+i*44}" cy="238" r="19"/>'
                        for i in range(10))}</g>
<g class="gold">{''.join(f'<circle cx="{102+i*44}" cy="302" r="19"/>'
                        for i in range(10))}</g>
<g fill="none" stroke="{GLDD}" stroke-width="2.5">
  {''.join(f'<circle cx="{102+i*44}" cy="{y}" r="12"/>' for y in (238, 302) for i in range(10))}
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('twice', '鐘のまわりを二まわりする矢印が、2回鳴らすことを示しているイラスト。',
    '同じことを2回する、2度。', f"""
<g transform="translate(300 190)">
  <path d="M-64 16q0-96 64-96t64 96q0 16 26 24H-90q26-8 26-24z" class="gold o"/>
  <circle cy="54" r="16" class="goldd o"/>
  <path d="M0-84v-30" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>
  <circle cy="-126" r="14" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M118 154a124 124 0 0 1 182-8" marker-end="url(#ar)"/>
  <path d="M482 228a124 124 0 0 1-182 8" marker-end="url(#ar)"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M406 158l38-24M414 212l42 6"/>
</g>
""", ground=True, arrow=True)

add('two', 'よく似たカップが2つ、湯気を立てて並んでいるイラスト。',
    '2、二つという数。', f"""
{table(300)}
{mug(206,300,1.25,'blue')}
{mug(392,300,1.25,'coral')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M182 226q-16-18 0-36t0-34M230 226q-16-18 0-36t0-34M368 226q-16-18 0-36t0-34M416 226q-16-18 0-36t0-34"/>
</g>
""", ground=True)

add('typhoon', '海の上で渦を巻く雲から激しい雨が降り、木が風にしなっているイラスト。',
    '夏から秋に日本へ来る強い熱帯低気圧、台風。', f"""
<g transform="translate(300 40)">{spiral(0,0,150,2.4,'violet',13)}</g>
<g stroke="{TONES['blue'][0]}" stroke-width="6" stroke-linecap="round">
  {''.join(f'<path d="M{x} {y}l-20 44"/>'
           for x, y in [(96,180),(160,236),(232,150),(376,170),(440,226),(508,166),(300,120),
                        (120,300),(420,318)])}
</g>
<g transform="translate(120 352) rotate(-26)">
  <path d="M-8 0h16v-86h-16z" class="goldd"/>
  <path d="M-4-70q-54-14-66-56 58 6 70 46z" class="greenp o"/>
  <path d="M4-70q54-14 66-56-58 6-70 46z" class="greenp o"/>
  <circle cy="-98" r="34" class="greenp o"/>
</g>
<path d="M30 392q60-26 120 0t120 0 120 0 120 0" fill="none" stroke="{TONES['blue'][0]}"
  stroke-width="6" stroke-linecap="round"/>
""", ground=True, bg='#eef3fa')


# --- u ----------------------------------------------------------------------

add('uncertain', '二つに分かれた点線の道の手前で、腕を広げて迷っているイラスト。',
    'どちらが正しいか、どうなるか確信が持てない。', f"""
{person(170,352,1.2,1,'violet','blue','reach','short','neutral')}
<g transform="translate(170 352) scale(1.2)">
  <path d="M-22-70l-46 24" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round" stroke-dasharray="16 14">
  <path d="M296 372q86-20 96-152"/>
  <path d="M296 372q106 34 150-34"/>
</g>
{spark(352,196,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('under', 'テーブルの下にボールが転がりこみ、下向きの矢印がその位置を示しているイラスト。',
    'あるものより低い位置を表す「〜の下に」。', f"""
<g transform="translate(300 200)">
  <path d="M-190 0h380v22h-380z" class="gold o"/>
  <path d="M-160 22v130M160 22v130" fill="none" stroke="{BRN}" stroke-width="16" stroke-linecap="round"/>
</g>
<circle cx="300" cy="322" r="30" class="coral o"/>
<path d="M256 298q32-26 70-8" fill="none" stroke="{CRLD}" stroke-width="5"/>
{arrowline([(300,56),(300,148)], TONES['blue'][0], 6, True)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('understand', '頭の上に電球が光り、ひらめいたようすのイラスト。',
    '内容がわかる、理解する。', f"""
{person(300,352,1.25,1,'teal','blue','think','short','smile')}
{bulb(300,116,1.05)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('university', '時計台の屋根に角帽がのった、柱の多い大きな校舎のイラスト。',
    '高等教育を受ける学校、大学。', f"""
<g transform="translate(300 336)">
  <path d="M-240 0h480v-96h-480z" fill="#fffdf6" class="o"/>
  <path d="M-84 0h168v-206h-168z" fill="#fffdf6" class="o"/>
  <path d="M-104-206L0-272l104 66z" class="violet o"/>
  <g class="violet">
    {''.join(f'<rect x="{x}" y="-78" width="34" height="32" rx="4"/>' for x in (-216, -156, 122, 182))}
    {''.join(f'<rect x="{x}" y="{y}" width="42" height="30" rx="4"/>'
             for y in (-186, -142, -98) for x in (-56, 14))}
  </g>
  <path d="M-34 0v-64h68V0z" class="violetd o"/>
  <path d="M-264 0h528v-16h-528z" fill="#ded3c2" class="o"/>
  <path d="M-288 0h576v14h-576z" fill="#e8ddcb" class="o"/>
  <g transform="translate(0 -280)">
    <path d="M-64 0l64-30 64 30-64 30z" class="ink"/>
    <path d="M42 6v30" fill="none" stroke="{INK}" stroke-width="7"/>
    <circle cx="42" cy="40" r="9" class="gold"/>
  </g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('untie', 'かた結びになったロープの両端を、外側へ引いてほどこうとしているイラスト。',
    '結んだものをほどく、結びを解く。', f"""
<g fill="none" stroke="{BRN}" stroke-width="16" stroke-linecap="round">
  <path d="M40 226q120-46 200-16"/>
  <path d="M362 210q92-30 198 6"/>
</g>
<g transform="translate(300 206)">
  <path d="M-58-30q6-46 58-40t54 44q-2 36-42 30-34-6-32-32 2-24 28-22" fill="none"
    stroke="{BRN}" stroke-width="16" stroke-linecap="round"/>
  <path d="M-16-78q10-16 26-12" fill="none" stroke="{BRN}" stroke-width="12"
    stroke-linecap="round"/>
</g>
{arrowline([(116,246),(46,250)], TONES['coral'][0], 6, True)}
{arrowline([(486,234),(554,240)], TONES['coral'][0], 6, True)}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M236 132l-18-28M368 126l18-28"/>
</g>
""", ground=True, arrow=True)

add('until', 'いすに座って待ちつづける人と、そこまでの時間を矢印で示す時計のイラスト。',
    'ある時点まで続くことを表す「〜まで」。', f"""
{chair(180,352,1.1,'gold')}
{sit(180,352,1.1,1,'teal','blue','short','neutral','lap')}
{clock(470,190,66,2,10)}
{arrowline([(292,306),(392,250)], TONES['blue'][0], 6, True)}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M260 250q20-12 40-4M272 214q18-10 36-2"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('unwrap', '贈り物の箱のふたを持ち上げ、リボンをほどいて中をたしかめているイラスト。',
    '包みや包装を解いて開ける。', f"""
{gift(268,272,150,120,'coral','gold')}
<g transform="translate(268 138) rotate(-16)">
  <rect x="-84" y="-18" width="168" height="36" rx="6" class="coral o"/>
  <path d="M0-18q-30-30-46-12-8 12 14 12 20 0 32-8zM0-18q30-30 46-12 8 12-14 12-20 0-32-8z"
    class="gold o"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="9" stroke-linecap="round">
  <path d="M414 300q30-10 44 22t-8 40"/>
</g>
{spark(268,88,1.1)}{spark(150,168,0.9)}{spark(430,140,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('up', '気球が空へのぼっていくようすを、上向きの矢印が示しているイラスト。',
    '上の方へ、上へ。', f"""
<g transform="translate(300 118)">
  <path d="M0 96C-56 56-88 16-88-30A88 88 0 0 1 88-30C88 16 56 56 0 96Z" class="coral o"/>
  <path d="M-88-30h176" fill="none" stroke="{CRLD}" stroke-width="5"/>
  <path d="M-46-88q46 34 92 0" fill="none" stroke="{CRLD}" stroke-width="5"/>
  <path d="M-34 60l-10 46M34 60l10 46" fill="none" stroke="{BRN}" stroke-width="6"/>
  <rect x="-34" y="104" width="68" height="44" rx="8" class="gold o"/>
</g>
{arrowline([(178,246),(178,124)], TONES['blue'][0], 7, True)}
{person(500,352,1.1,-1,'teal','blue','point','short','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('uphill', '急な坂道で、荷物をうしろから押し上げているイラスト。',
    '上り坂の、上り坂で。', f"""
<path d="M40 360L560 200v64L40 404z" fill="#ded3c2" class="o"/>
<path d="M40 360L560 200" fill="none" stroke="{MUTED}" stroke-width="4"
  stroke-dasharray="20 16"/>
<g transform="translate(320 240) rotate(-17)">
  {box(0,0,104,76,22,'gold')}
</g>
<g transform="translate(232 296) rotate(-17)">
  {person(0,0,1.1,1,'teal','blue','reach','short','smile')}
</g>
{drop(190,196,0.8,'blue')}
{arrowline([(96,344),(180,318)], TONES['coral'][0], 6, True)}
""", ground=True, arrow=True)

add('us', '外から箱を手渡された三人のグループに、点線の輪がかけられているイラスト。',
    '話し手を含む複数が受け取る側になる「私たちを・私たちに」。', f"""
{person(116,352,1.15,1,'coral','blue','give','short','smile')}
{box(206,262,74,56,18,'gold')}
{person(372,352,1.05,1,'teal','blue','hold','short','smile')}
{person(452,352,1.0,1,'violet','blue','stand','bob','smile')}
{person(528,352,1.0,1,'green','blue','stand','short','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10">
  <ellipse cx="450" cy="250" rx="140" ry="126"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('useful', 'はしごにのぼり、棚の上のびんを取ろうとしているイラスト。',
    '使うと役に立つ、便利な。', f"""
<g transform="translate(150 348)">
  <path d="M-142 0h284v-22h-284z" class="goldd o"/>
  <path d="M-124-22h248v-158h-248z" fill="#f6e3c4" class="o"/>
  <path d="M-124-88h248" fill="none" stroke="{GLDD}" stroke-width="12"/>
  <path d="M-124-164h248" fill="none" stroke="{GLDD}" stroke-width="14"/>
  <g class="teal">{''.join(f'<rect x="{-100+i*60}" y="-152" width="40" height="62" rx="6"/>'
      for i in range(4))}</g>
  <g class="violet">{''.join(f'<rect x="{-100+i*60}" y="-76" width="40" height="52" rx="6"/>'
      for i in range(4))}</g>
</g>
{ladder(330,352,226,54,'gold')}
{person(330,242,1.0,-1,'coral','blue','reach','short','smile')}
{spark(272,150,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('usually', 'いつもの習慣のように、カップを持つ人と、繰り返しを表す輪の矢印がついた時計のイラスト。',
    'たいてい、ふつうは。', f"""
{mug(288,296,1.1,'coral')}
{person(280,352,1.2,1,'teal','blue','hold','short','smile')}
<g transform="translate(466 190)">
  {clock(0,0,62,3,10)}
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="6" stroke-linecap="round">
    <path d="M-94 0a94 94 0 0 1 94-94" marker-end="url(#ar)"/>
    <path d="M94 0a94 94 0 0 1-94 94" marker-end="url(#ar)"/>
  </g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('vacuum cleaner', 'そうじ機のノズルを床に当て、ほこりを吸い取っているイラスト。',
    '床やじゅうたんのごみを吸い取る電気掃除機。', f"""
{person(480,352,1.2,-1,'teal','blue','hold','short','smile')}
<g transform="translate(322 352)">
  <path d="M-72 0h144v-24a12 12 0 0 0-12-12h-120a12 12 0 0 0-12 12z" class="blue o"/>
  <path d="M-72 0h144" fill="none" stroke="{BLUD}" stroke-width="6"/>
</g>
<path d="M330 318q56-44 138-26" fill="none" stroke="{MUTED}" stroke-width="13"
  stroke-linecap="round"/>
<g fill="{MUTED}">
  {''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>'
           for x, y, r in [(232,342,8),(206,354,6),(252,326,6),(188,336,5)])}
</g>
{arrowline([(196,346),(272,350)], TONES['blue'][0], 5, True)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('vegetable', 'かごにトマト、にんじん、ブロッコリーなどが山もりになっているイラスト。',
    '畑でとれる、食べられる植物、野菜。', f"""
<g transform="translate(300 300)">
  <path d="M-156-18h312l-28 84h-256z" class="gold o"/>
  <path d="M-156-18h312" fill="none" stroke="{GLDD}" stroke-width="12"/>
  <g fill="none" stroke="{GLDD}" stroke-width="4">
    <path d="M-130 6h260M-116 38h232M-96-18l14 84M0-18v84M96-18l-14 84"/>
  </g>
</g>
<g transform="translate(206 254)"><circle r="42" class="coral o"/>
  <path d="M0-40q-26-4-34-22 26-6 38 16zM0-40q26-4 34-22-26-6-38 16z" class="greenp o"/></g>
<g transform="translate(300 240) rotate(6)">
  <path d="M-26 46L0-46l26 92z" fill="#e08a2e" class="o"/>
  <path d="M-6-46q-26-24-18-48 26 10 28 42zM6-46q26-24 18-48-26 10-28 42z" class="greenp o"/>
</g>
<g transform="translate(394 250)">
  <circle cx="-22" cy="-8" r="26" class="greenp o"/><circle cx="20" cy="-12" r="28" class="greenp o"/>
  <circle cy="16" r="24" class="greenp o"/>
  <path d="M0 34v26" fill="none" stroke="{GRND}" stroke-width="10"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('video', 'ノートパソコンの画面いっぱいに再生の三角形が映っているイラスト。',
    '録画された映像、動画。', f"""
{page(300,206,1.05,'blue',True)}
<g transform="translate(300 318)">
  <path d="M-158 0h316l22-30h-360z" class="blue o"/>
</g>
{spark(140,110,0.9)}{spark(466,116,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('violet', '紫色のすみれの花が三つ、葉の間から咲いているイラスト。',
    'すみれ、およびそのすみれ色。', f"""
{flower(208,304,1.5,'violet')}
{flower(392,304,1.5,'violet')}
{flower(300,292,1.3,'violet')}
<g class="greenp o">
  <path d="M208 346q-72-6-98-48 68-10 102 36z"/>
  <path d="M392 346q72-6 98-48-68-10-102 36z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('visit', '玄関のドアの前に、贈り物を持って立っている人のイラスト。',
    '人の家や施設をたずねる、訪問する。', f"""
{house(462,348,1.3,'coral')}
{person(232,352,1.2,1,'violet','blue','give','short','smile')}
{gift(322,318,78,62,'gold','coral')}
{spark(400,180,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('wagon', '荷物を高く積んだ四輪の荷車を、人が引っぱって歩いているイラスト。',
    '荷物を運ぶための、車輪のついた荷車。', f"""
{person(170,352,1.15,1,'teal','blue','carry','short','smile')}
<path d="M256 344l92-14" fill="none" stroke="{BRN}" stroke-width="11" stroke-linecap="round"/>
<g transform="translate(444 300)">
  <path d="M-150-70h300v62a10 10 0 0 1-10 10h-280a10 10 0 0 1-10-10z" fill="#c9a464" class="o"/>
  <g fill="none" stroke="#a0764a" stroke-width="5">
    <path d="M-150-46h300M-150-24h300M-100-70v72M0-70v72M100-70v72"/>
  </g>
  <circle cx="-104" cy="44" r="40" fill="#a0764a" class="o"/>
  <g fill="none" stroke="#7a5731" stroke-width="7">
    <path d="M-104 4v80M-144 44h80M-132 12l56 64M-76 12l-56 64"/>
  </g>
  <circle cx="104" cy="44" r="40" fill="#a0764a" class="o"/>
  <g fill="none" stroke="#7a5731" stroke-width="7">
    <path d="M104 4v80M64 44h80M76 12l56 64M132 12l-56 64"/>
  </g>
</g>
{box(404,190,108,80,22,'gold')}
{box(514,204,80,58,18,'teal')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('wake', 'ベッドのそばで両腕を上げてのびをし、目覚まし時計が鳴っているイラスト。',
    '眠りから目を覚ます、起こす。', f"""
{bed(400,352,1.0,'blue')}
{person(168,352,1.2,1,'coral','blue','up','bob','smile')}
<g transform="translate(298 300)">{clock(0,0,46,7,0)}</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M350 264l34-22M354 300h40M350 336l34 22"/>
</g>
{spark(160,142,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('walk', '足あとを残しながら、腕をふって歩いていくイラスト。',
    '足で進む、散歩する。', f"""
{person(330,352,1.25,1,'teal','blue','walk','short','smile')}
{footprint(214,366,1.0,1,-12)}{footprint(156,370,1.0,1,10)}{footprint(96,366,1.0,1,-10)}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round">
  <path d="M62 258h52M46 300h46"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('wall', 'れんがの壁にボールが当たり、はね返っていくイラスト。',
    '部屋や外を仕切る、れんがや板の壁。', f"""
{wall(300,60,300,326)}
<circle cx="186" cy="240" r="38" class="coral o"/>
<path d="M160 216q-24-16-28-42" fill="none" stroke="{CRLD}" stroke-width="5"/>
<path d="M314 208L268 232" fill="none" stroke="{MUTED}" stroke-width="5"/>
<path d="M310 268L266 284" fill="none" stroke="{MUTED}" stroke-width="5"/>
{arrowline([(300,246),(226,246)], TONES['blue'][0], 5, True)}
<path d="M60 386h62" class="a"/>
""", ground=True, arrow=True)

add('want', 'ケーキに手をのばし、頭の上にハートが浮かんでいるイラスト。',
    'ほしいと思う、〜したいと思う。', f"""
{person(158,352,1.2,1,'teal','blue','reach','short','smile')}
{heart(186,166,0.95,'coral')}
<g transform="translate(430 300)">
  <ellipse cy="8" rx="112" ry="24" class="paper"/>
  <path d="M-76 0h152v-56a10 10 0 0 0-10-10h-132a10 10 0 0 0-10 10z" class="goldp o"/>
  <rect x="-80" y="-80" width="160" height="26" rx="13" class="coral o"/>
  <g class="coral">{''.join(f'<circle cx="{x}" cy="-62" r="9"/>' for x in (-52, -18, 16, 50))}</g>
  <rect x="-6" y="-116" width="12" height="36" rx="5" class="blue o"/>
  <path d="M0-124q11-13 0-26-11 13 0 26z" class="gold o"/>
</g>
{arrowline([(210,236),(314,262)], TONES['coral'][0], 5, True)}
""", ground=True, arrow=True)

add('was', '写真立ての中に昔の家のようすがおさまり、時計からの矢印が過去を示しているイラスト。',
    'be動詞の過去形で「〜だった」「〜にいた」。', f"""
{clock(120,190,52,3,9)}
{frame(380,200,1.0,'gold')}
{house(380,268,0.55,'coral')}
{person(300,268,0.3,1,'teal','blue','stand','short','smile')}
<path d="M126 246q12 62 84 76" fill="none" stroke="{TONES['blue'][0]}" stroke-width="5"
  stroke-dasharray="12 10" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('wash up', '流しに皿を重ね、泡立てながら洗っているイラスト。',
    '食器を洗う(英)、手を洗う(米)。', f"""
{person(140,352,1.2,1,'teal','blue','reach','short','smile')}
<g transform="translate(408 344)">
  <path d="M-190-64h380v20h-380z" class="paper"/>
  <path d="M-150-44h300v52a20 20 0 0 1-20 20h-260a20 20 0 0 1-20-20z" fill="#fffdf6" class="o"/>
  <path d="M-150-44h300" fill="none" stroke="{MUTED}" stroke-width="5"/>
  <path d="M-56-64v-46q0-16 16-16h18" fill="none" stroke="{MUTED}" stroke-width="11"
    stroke-linecap="round"/>
  <g class="goldp">
    <ellipse cx="-64" cy="-28" rx="54" ry="14"/>
    <ellipse cx="12" cy="-38" rx="50" ry="13"/>
  </g>
  <g class="teal">
    <path d="M-104-40q-6-32 6-52 14-22 36-20-6 32-26 42-10 6-16 30z"/>
    <path d="M64-38q-8-34 6-52 16-20 38-18-8 32-28 42-10 6-16 28z"/>
  </g>
  <g fill="#fffefd" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>'
             for x, y, r in [(-124,-22,15),(-70,-58,19),(30,-58,17),(112,-24,14),(62,-14,12),(-16,-16,11)])}
  </g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('watch', '手首に巻いた小さな時計を、じっと見ているイラスト。',
    '身につける小型の時計、腕時計。', f"""
{person(280,352,1.25,1,'teal','blue','think','short','neutral')}
<g transform="translate(292 226) rotate(20)">
  <path d="M-9-104h18v64h-18zM-9 40h18v64h-18z" class="blue o"/>
  <circle r="42" class="goldd o"/>
  <circle r="33" fill="#fffefd" class="o"/>
  <path d="M0 0v-20M0 0l16 12" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <circle r="4" class="ink"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('we', '三人がそろって手を上げ、いっしょに行動しているイラスト。',
    '話し手を含む複数が主語になる「私たちは・私たちが」。', f"""
{person(180,352,1.15,1,'teal','blue','up','short','smile')}
{person(300,352,1.25,1,'coral','blue','up','bob','smile')}
{person(420,352,1.15,1,'violet','blue','up','short','smile')}
{spark(240,112,0.9)}{spark(360,98,1.0)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('wear', 'コートを羽織り、マフラーを身につけているイラスト。',
    '衣服などを身につけている、着ている。', f"""
{person(300,352,1.3,1,'teal','blue','stand','short','smile')}
<g transform="translate(300 352) scale(1.3)">
  <path d="M-28-78q28-14 56 0l9 76h-18l-7-62h-24l-7 62h-18z" class="violet o"/>
  <path d="M-18-76q18 10 36 0" fill="none" stroke="{VIOD}" stroke-width="8" stroke-linecap="round"/>
  <path d="M-22-88q22 16 44 0l4 16q-26 14-52 0z" class="coral o"/>
  <path d="M18-72q12 12 4 30" fill="none" stroke="{TONES['coral'][2]}" stroke-width="11"
    stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('weather', '窓のガラスの向こうに太陽と雲が見え、人が外の空模様を見ているイラスト。',
    'その日の空模様、天気。', f"""
<g transform="translate(258 200)">
  <rect x="-152" y="-132" width="304" height="264" rx="12" fill="#e2eefb" class="o"/>
  <rect x="-152" y="-132" width="304" height="178" fill="#cfe3f5"/>
  {sun(-64,-72,40)}
  {cloud(66,-52,0.66,'blue')}
  <rect x="-152" y="-132" width="304" height="264" rx="12" fill="none" stroke="{INK}"
    stroke-width="9"/>
  <path d="M0-132V132M-152 46h304" fill="none" stroke="{INK}" stroke-width="9"/>
  <path d="M-182 132h364v22h-364z" class="goldp o"/>
</g>
{person(520,352,1.15,-1,'teal','blue','stand','short','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('website', 'ノートパソコンの画面に、写真と文章が並んだページが映っているイラスト。',
    'インターネット上で公開されているページ、ウェブサイト。', f"""
{page(300,196,1.05,'blue',False)}
<g transform="translate(300 318)">
  <path d="M-158 0h316l22-30h-360z" class="blue o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('websites', '三つのブラウザ画面が並んで開いているイラスト。',
    'ウェブサイトの複数形で、いくつものページ。', f"""
{page(148,212,0.6,'blue')}
{page(300,166,0.6,'violet')}
{page(452,212,0.6,'teal')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('trader', '屋台の品物と硬貨を、商人と客が交換しているイラスト。',
    '品物を売り買いする人、商人。', f"""
<g transform="translate(320 300)">
  <path d="M-140 0h280v20h-280z" class="gold o"/>
  <path d="M-120 20v62M120 20v62" fill="none" stroke="{GLDD}" stroke-width="14"
    stroke-linecap="round"/>
</g>
<g transform="translate(254 262)">
  <path d="M-26 38h52v-30a8 8 0 0 0-8-8h-36a8 8 0 0 0-8 8z" class="goldp o"/>
</g>
<g transform="translate(382 278)"><circle r="22" class="coral o"/></g>
{person(140,352,1.15,1,'teal','blue','give','short','smile')}
{person(492,352,1.15,-1,'violet','blue','reach','bob','smile')}
{coin(320,200,26)}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-dasharray="10 8">
  <path d="M288 200h-42M352 200h42"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('week', '7つのマスが横に並び、全体が囲まれて1週間を表しているイラスト。',
    '7日間をひとまとまりにした期間、週。', f"""
<g transform="translate(300 216)">
  {''.join(f'<rect x="{-212+i*62}" y="-46" width="52" height="92" rx="10" class="bluep o"/>'
           for i in range(7))}
  <path d="M-232 76h464" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <path d="M-232 76v16M232 76v16" fill="none" stroke="{INK}" stroke-width="6"
    stroke-linecap="round"/>
  <ellipse cy="0" rx="250" ry="100" fill="none" stroke="{TONES['coral'][0]}"
    stroke-width="4" stroke-dasharray="12 10"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('went', '家から建物へ点線の道と足あとがのび、その先に立っているイラスト。',
    'go の過去形で「行った」。', f"""
{house(110,352,0.85,'coral')}
{building(500,340,0.8,'teal')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round"
   stroke-dasharray="16 12"><path d="M200 372q140-26 240-40"/></g>
{footprint(240,370,1.0,1,-8)}{footprint(310,362,1.0,1,-8)}{footprint(376,354,1.0,1,-8)}
{person(410,352,1.1,1,'violet','blue','walk','short','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('were', '写真立ての中に複数の家がおさまり、時計からの矢印が過去を示しているイラスト。',
    'be動詞の過去形で、複数の主語に使う「〜だった」。', f"""
{clock(120,190,50,3,9)}
{frame(380,200,1.0,'gold')}
{house(330,268,0.5,'coral')}
{house(432,268,0.5,'blue')}
<path d="M126 244q14 58 82 74" fill="none" stroke="{TONES['blue'][0]}" stroke-width="5"
  stroke-dasharray="12 10" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('west', '海に沈む太陽と、左を指す矢印、方位の星のマークのイラスト。',
    '方角の西、西側。', f"""
<g transform="translate(150 296)">{sun(0,0,62)}</g>
<rect y="296" width="600" height="104" fill="#cfe3f5" class="o"/>
<g fill="none" stroke="{TONES['blue'][2]}" stroke-width="5" stroke-linecap="round">
  <path d="M40 326h130M70 356h96M410 330h150M440 362h110"/>
</g>
{arrowline([(330,120),(160,120)], TONES['coral'][0], 7, True)}
<g transform="translate(486 190)">
  <circle r="72" class="paper"/>
  <path d="M0-56L15 0 0 56-15 0zM-56 0L0-15 56 0 0 15z" class="coral o"/>
</g>
""", ground=True, arrow=True)

add('what', 'ふたの開いた箱の中身が点線でぼかされ、そばの人が首をかしげているイラスト。',
    'ものや内容をたずねる「何」。', f"""
{box(346,296,176,124,34,'gold')}
<g transform="translate(346 236) rotate(-8)">
  <path d="M-96-40h192v14a8 8 0 0 1-8 8h-176a8 8 0 0 1-8-8z" class="goldd o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10">
  <path d="M288 200q22-32 48-8t46-12q16-14 34 8"/>
</g>
{spark(300,152,0.9)}{spark(404,158,0.8)}
{person(116,352,1.15,1,'violet','blue','reach','short','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('when', '時計と暦の間を点線の矢印が行き来し、時をたずねていることを示すイラスト。',
    '時をたずねる「いつ」。', f"""
{clock(170,190,66,3,9)}
{calendar(430,190,0.9,7,3,3)}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M250 132q86-38 96 0" marker-end="url(#ar)"/>
  <path d="M350 252q-86 38-96 0" marker-end="url(#ar)"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('where', '地図に場所のピンが立ち、人が地図を広げて行き先を探しているイラスト。',
    '場所をたずねる「どこで・どこへ」。', f"""
<g transform="translate(316 286) rotate(-8)">
  <path d="M-164-84h328v168h-328z" class="paper"/>
  <path d="M-164-84h328v168h-328z" fill="none" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10">
    <path d="M-56-84V84M62-84V84"/>
  </g>
  <path d="M-112 44q84-24 62-64t88-42" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"
    stroke-dasharray="12 10"/>
</g>
{pin(280,158,0.95,'coral')}
{pin(416,196,0.8,'violet')}
{person(126,352,1.15,1,'teal','blue','hold','short','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('which', '同じに見える二つの扉の前で、どちらにしようかと迷っているイラスト。',
    '二つ以上のうちどれかをたずねる「どちら・どれ」。', f"""
<g transform="translate(150 344)">
  <path d="M-72 0h144v-198h-144z" class="gold o"/>
  <circle cx="44" cy="-100" r="9" class="ink"/>
  <path d="M-72 0h144v-198h-144z" fill="none" class="o"/>
</g>
<g transform="translate(450 344)">
  <path d="M-72 0h144v-198h-144z" class="gold o"/>
  <circle cx="44" cy="-100" r="9" class="ink"/>
  <path d="M-72 0h144v-198h-144z" fill="none" class="o"/>
</g>
<g transform="translate(300 344)"><path d="M-200 0h400v-14h-400z" fill="#ded3c2" class="o"/></g>
{person(300,352,1.15,1,'violet','blue','point','short','neutral')}
<g transform="translate(300 352) scale(1.15)">
  <path d="M-22-70l-44 22" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
</g>
{arrowline([(226,244),(170,244)], TONES['blue'][0], 5, True)}
{arrowline([(374,244),(430,244)], TONES['blue'][0], 5, True)}
""", ground=True, arrow=True)

add('white', 'ローラーで壁を白く塗り分けているイラスト。',
    '白、白色。', f"""
<rect x="40" y="60" width="520" height="300" fill="#dde3e8" class="o"/>
<rect x="40" y="60" width="300" height="300" fill="#fffefd"/>
<rect x="40" y="60" width="520" height="300" fill="none" class="o"/>
<g transform="translate(352 200) rotate(-26)">
  <rect x="-58" y="-36" width="116" height="72" rx="12" class="blue o"/>
  <path d="M58 0h62" fill="none" stroke="{MUTED}" stroke-width="13" stroke-linecap="round"/>
  <path d="M120 0v56" fill="none" stroke="{MUTED}" stroke-width="13" stroke-linecap="round"/>
  <path d="M120 56h52" fill="none" stroke="{MUTED}" stroke-width="13" stroke-linecap="round"/>
</g>
<g fill="#fffefd">
  {''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>'
           for x, y, r in [(312,300,10),(278,332,8),(342,320,7),(296,208,6)])}
</g>
""", ground=True)

add('who', 'カーテンのかげに人の形の点線が見え、そばの人が指さしているイラスト。',
    '人をたずねる「だれ」。', f"""
<g transform="translate(400 344)">
  <path d="M-136 0h272v-276h-272z" fill="#eee8fb" class="o"/>
  <path d="M-96-276v276M-32-276v276M32-276v276M96-276v276" fill="none"
    stroke="{TONES['violet'][0]}" stroke-width="4"/>
  <path d="M-136 0h272v-276h-272z" fill="none" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10">
  <circle cx="400" cy="176" r="30"/>
  <path d="M362 330q0-78 38-96 38 18 38 96"/>
</g>
{person(160,352,1.2,1,'teal','blue','point','short','neutral')}
{arrowline([(230,244),(322,244)], TONES['blue'][0], 5, True)}
""", ground=True, arrow=True)

add('why', '石につまずいた人が石をふり返り、理由をたずねるように見つめているイラスト。',
    '理由をたずねる「なぜ」。', f"""
<g transform="translate(150 342)">
  <ellipse rx="58" ry="30" fill="#b9c2c9" class="o"/>
  <path d="M-32-14q32-14 64 2" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
{spark(196,298,0.9,'gold')}
{person(430,352,1.15,-1,'coral','blue','stand','short','sad')}
{arrowline([(224,300),(368,242)], TONES['coral'][0], 5, True)}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M408 180q-16-18 0-34t0-32"/>
</g>
""", ground=True, arrow=True)

add('wife', '向かい合った夫婦が手をつなぎ、間に指輪とハートが浮かんでいるイラスト。',
    '結婚している相手の女性、妻。', f"""
{person(230,352,1.15,1,'teal','blue','reach','short','smile')}
{person(370,352,1.15,-1,'blue','blue','reach','bob','smile')}
<circle cx="300" cy="317" r="24" fill="none" stroke="{TONES['gold'][0]}" stroke-width="8"/>
{heart(300,196,0.95,'coral')}
{spark(196,240,0.7)}{spark(404,240,0.7)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('window', 'カーテンのついた四角い窓から、外の太陽と木が見えているイラスト。',
    '光や風を入れるために壁に開けた開口部、窓。', f"""
<g transform="translate(300 196)">
  <rect x="-160" y="-130" width="320" height="260" rx="8" fill="#e2eefb" class="o"/>
  <rect x="-160" y="-130" width="320" height="176" fill="#cfe3f5"/>
  {sun(-72,-66,40)}
  {cloud(64,-46,0.6,'blue')}
  {tree(104,126,0.78)}
  <g fill="none" stroke="{INK}" stroke-width="9">
    <rect x="-160" y="-130" width="320" height="260" rx="8"/>
    <path d="M0-130V130M-160 46h320"/>
  </g>
  <path d="M-186 130h372v22h-372z" class="goldp o"/>
</g>
<g class="coral">
  <path d="M118 66q52 82 8 264h46q-26-150 10-264z"/>
  <path d="M482 66q-52 82-8 264h-46q26-150-10-264z"/>
</g>
""", ground=True)

add('wine', 'ぶどう酒のびんと、赤い液体の入ったグラスがテーブルに並んでいるイラスト。',
    'ぶどうから作る酒、ワイン。', f"""
{table(300)}
<g transform="translate(190 300)">
  <path d="M-14-192h28v34a30 30 0 0 1 14 26v122a10 10 0 0 1-10 10h-36a10 10 0 0 1-10-10v-122
    a30 30 0 0 1 14-26z" class="violet o"/>
  <rect x="-17" y="-208" width="34" height="20" rx="7" class="violetd o"/>
  <rect x="-34" y="-96" width="68" height="54" rx="6" fill="#fffdf6" class="o"/>
  <path d="M-16-70h32M-16-56h22" fill="none" stroke="{MUTED}" stroke-width="5"/>
</g>
<g transform="translate(404 300)">
  <path d="M-44-98h88l-8 56a36 36 0 0 1-72 0z" fill="#fffdf6" class="o"/>
  <path d="M-40-90h80l-7 48a33 33 0 0 1-66 0z" class="coral"/>
  <path d="M-48-42h96" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M0-42v56" fill="none" stroke="{MUTED}" stroke-width="8"/>
  <path d="M-32 14h64" fill="none" stroke="{MUTED}" stroke-width="9" stroke-linecap="round"/>
</g>
""", ground=True)

add('winter', '葉を落とした裸の木と雪だるま、舞う雪で冬の景色を表したイラスト。',
    '一年で最も寒い季節、冬。', f"""
<path d="M0 306h600v94H0z" fill="#eef4f9"/>
{snowman(420,352,1.15)}
<g transform="translate(140 352)">
  <path d="M-9 0h18v-112h-18z" class="goldd"/>
  <path d="M0-98L-58-152M0-82L56-138M-2-118L-30-168M4-114L38-166" fill="none" stroke="{BRN}"
    stroke-width="9" stroke-linecap="round"/>
</g>
{snow(200,140,1.0)}{snow(318,96,0.8)}{snow(508,168,0.9)}{snow(76,236,0.7)}{snow(566,262,0.8)}
{snow(400,60,0.7)}
<path d="M60 386h480" class="a"/>
""", ground=True, bg='#eef5fb')

add('with', '犬を連れて、いっしょに散歩しているイラスト。',
    '「〜と一緒に」を表す前置詞。', f"""
{person(230,352,1.2,1,'teal','blue','point','short','smile')}
{dog(420,352,1.05,-1,'gold')}
<path d="M288 356q40 12 64-18" fill="none" stroke="{CRLD}" stroke-width="5"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('without', '雨の中でかさを持たずにぬれている人と、打ち消されたかさの点線のイラスト。',
    '「〜なしで、〜がなければ」を表す前置詞。', f"""
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
  {''.join(f'<path d="M{x} {y}l-16 42"/>'
           for x, y in [(80,60),(160,40),(240,70),(320,40),(400,60),(480,40),(566,70),
                        (120,180),(360,170),(520,180),(200,296),(444,300),(560,320)])}
</g>
{person(300,352,1.25,1,'teal','blue','stand','short','sad')}
{umbrella(300,196,1.0,'coral',True)}
{cross(300,150,1.1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('woman', 'スカートを着て、かばんを持って立っている女性のイラスト。',
    'おとなの女の人、女性。', f"""
{person(300,352,1.25,1,'violet','blue','stand','bob','smile')}
<g transform="translate(300 352) scale(1.25)">
  <path d="M-36-8h72l12 44h-96z" class="violet o"/>
  <path d="M-36-8h72" fill="none" stroke="{VIOD}" stroke-width="6"/>
</g>
<g transform="translate(348 320)">
  <path d="M-26-24h52v44a10 10 0 0 1-10 10h-32a10 10 0 0 1-10-10z" class="gold o"/>
  <path d="M-16-24q0-22 16-22t16 22" fill="none" stroke="{BRN}" stroke-width="7"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('wonderful', '大きな虹の下で人が両手を上げ、きらきらが光っているイラスト。',
    'とてもすばらしい、素敵な。', f"""
{rainbow(300,320,150,16)}
{person(300,352,1.2,1,'coral','blue','up','bob','smile')}
{spark(140,140,1.0)}{spark(462,130,0.9)}{spark(300,74,1.1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('word', '吹き出しの中に、語のかたまりを表す四角が並んでいるイラスト。',
    '意味をもつ言葉の単位、単語。', f"""
{person(190,352,1.2,1,'teal','blue','point','short','smile')}
{bubble(400,190,1.35,'blue',1,3)}
{word(400,186,5,26)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('work', '机に向かってノートパソコンで仕事をしているイラスト。',
    '仕事、働くこと、機械が動くこと。', f"""
{chair(300,352,1.1,'gold')}
{sit(300,352,1.1,1,'teal','blue','short','smile','down')}
{desk(440,300,280)}
{page(470,240,0.5,'blue')}
{doc(360,266,160,64,4)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('world', '台にのった地球儀と、そのまわりに立つ人びとのイラスト。',
    '地球全体、世の中。', f"""
<g transform="translate(280 210)">
  <circle r="96" class="bluep o"/>
  <g class="greenp o">
    <path d="M-64-40q30-24 54-4 8 26-12 38-26 16-40-4-8-18-2-30z"/>
    <path d="M24-56q34-14 50 10 6 26-20 30-22 4-30-18-4-12 0-22z"/>
    <path d="M-34 16q34-12 54 12 10 28-22 38-32 10-40-20-4-20 8-30z"/>
  </g>
  <circle r="96" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M0-96v192M-96 0h192" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M0 96v24" fill="none" stroke="{BRN}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-58 140h116" fill="none" stroke="{BRN}" stroke-width="14" stroke-linecap="round"/>
  <path d="M-58 140v14M58 140v14" fill="none" stroke="{BRN}" stroke-width="10"
    stroke-linecap="round"/>
</g>
{person(504,352,1.1,-1,'teal','blue','point','short','smile')}
{person(104,352,1.0,1,'violet','blue','stand','bob','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('would', 'いすに座った人の頭の上に、家の夢を思いうかべる点線の吹き出しがあるイラスト。',
    '仮定や過去の習慣を表す助動詞「〜だろう」。', f"""
{chair(180,352,1.15,'gold')}
{sit(180,352,1.15,1,'violet','blue','short','neutral','lap')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10">
  <ellipse cx="380" cy="150" rx="112" ry="70"/>
  <circle cx="272" cy="238" r="14"/>
  <circle cx="248" cy="268" r="8"/>
</g>
<g transform="translate(380 196)">{house(0,0,0.46,'coral')}</g>
{spark(318,118,0.8)}{spark(444,140,0.7)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('wrapping paper', '柄の入った包装紙のロールと、リボンで包まれた箱のイラスト。',
    '贈り物を包むための、模様のついた紙。', f"""
<g transform="translate(160 246)">
  <rect x="-58" y="-104" width="116" height="208" rx="10" class="coral o"/>
  <g fill="none" stroke="{CRLD}" stroke-width="4">
    <path d="M-58-70h116M-58-24h116M-58 22h116M-58 68h116M-20-104v208M20-104v208"/>
  </g>
  <ellipse cx="58" cy="0" rx="20" ry="104" class="coral o"/>
  <ellipse cx="58" cy="0" rx="10" ry="60" fill="#fffefd" class="o"/>
</g>
{gift(400,274,150,124,'blue','gold')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('wring', 'ぬれた布を両手でひねって、水をしぼり出しているイラスト。',
    '布などをねじって水や液を出す、絞る。', f"""
<g transform="translate(300 176)">
  <path d="M-136 6q44-30 84-6 26 16 52 16t52-16q40-24 84 6" fill="none"
    stroke="{TONES['blue'][0]}" stroke-width="30" stroke-linecap="round"/>
  <path d="M-30 12q30 22 60 0" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12"
    stroke-linecap="round"/>
</g>
{hand(146,182,1)}
{hand(454,182,-1)}
<g class="blue">
  {''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>'
           for x, y, r in [(300,232,7),(286,264,6),(316,270,6),(300,302,5),(288,334,4)])}
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('write', '机に向かってペンで紙に文字を書き込んでいるイラスト。',
    '文字や文章を書く。', f"""
{chair(300,352,1.1,'gold')}
{sit(300,352,1.1,1,'teal','blue','short','smile','down')}
{desk(440,300,280)}
{doc(360,266,160,64,4)}
<path d="M300 290l50-44 14 12-50 44z" class="blue o"/>
<path d="M300 290l-16 12 9-19z" class="blued o"/>
<g transform="translate(300 352) scale(1.1)">
  <path d="M-14-76l60-20" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cx="46" cy="-96" r="12" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
""", ground=True)


# --- y / z ------------------------------------------------------------------

add('yacht', '二枚の帆を上げたヨットが、波の上を走っているイラスト。',
    '帆やエンジンで走る小型の船、ヨット。', f"""
{boat(300,320,1.15,'teal')}
{wavy(30,352,540,4,13,'blue')}
{wavy(60,384,470,3,10,'blue')}
{sun(500,96,40)}
""", ground=True)

add('yam', '土のついた長い山いもと、切って白い中身が見える輪切りのイラスト。',
    'ねばりのある長い根菜、ヤム・山いも。', f"""
<g transform="translate(196 246) rotate(-10)">
  <ellipse rx="46" ry="152" fill="#cdae7f" class="o"/>
  <g fill="none" stroke="#a0764a" stroke-width="5">
    <path d="M-30-100q18 10 16 30M-32-40q20 12 18 32M-36 30q18 10 16 30M-30 90q14 8 12 24"/>
  </g>
  <g fill="none" stroke="{BRN}" stroke-width="6" stroke-linecap="round">
    <path d="M-24-146q-18-16-34-14M22-148q10-20 26-24M-40 140q-16 12-30 8"/>
  </g>
</g>
<g transform="translate(420 244)">
  <circle r="68" fill="#e8dfc9" class="o"/>
  <circle r="54" fill="#fffdf6" class="o"/>
  <g fill="{MUTED}" opacity="0.55">
    {''.join(f'<circle cx="{x}" cy="{y}" r="5"/>'
             for x, y in [(-26,-18),(-4,-30),(24,-14),(32,14),(10,26),(-18,18),(-2,-4),(16,0)])}
  </g>
</g>
<g transform="translate(470 336)">
  <circle r="44" fill="#e8dfc9" class="o"/>
  <circle r="33" fill="#fffdf6" class="o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('year', '花・太陽・葉・雪が円く並び、回る矢印が一年の巡りを表しているイラスト。',
    '1月から12月までの12か月、1年。', f"""
<circle cx="300" cy="200" r="112" fill="none" stroke="{MUTED}" stroke-width="4"
  stroke-dasharray="14 12"/>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M300 88a112 112 0 1 1-72 28" marker-end="url(#ar)"/>
</g>
{flower(300,70,0.85,'coral')}
{sun(414,200,34)}
{leaf(300,320,1.05,'gold')}
{snow(186,200,1.5,'blue')}
""", ground=True, arrow=True)

add('yellow', '黄色い花びらを広げた大きなひまわりが咲いているイラスト。',
    '黄色、黄色い色。', f"""
<g transform="translate(300 148)">
  {''.join(f'<ellipse cx="0" cy="-84" rx="17" ry="42" class="gold o" transform="rotate({d})"/>'
           for d in range(0, 360, 30))}
  <circle r="48" fill="#8b6437" class="o"/>
  <g fill="{TONES['gold'][2]}">
    {''.join(f'<circle cx="{x}" cy="{y}" r="4"/>'
             for x, y in [(-20,-20),(0,-26),(20,-18),(26,2),(14,20),(-8,24),(-24,6),(4,-2)])}
  </g>
</g>
<path d="M300 196v152" fill="none" stroke="{GRND}" stroke-width="15" stroke-linecap="round"/>
<g class="greenp o">
  <path d="M300 258q-78-12-106-62 74-10 110 48z"/>
  <path d="M300 314q78-12 106-62-74-10-110 48z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('yes', 'うなずいて手を上げる人のそばに、大きな緑のチェックが描かれているイラスト。',
    '肯定の返事「はい、そうだ」。', f"""
{person(200,352,1.25,1,'teal','blue','up','short','smile')}
{tick(420,244,1.6)}
{spark(382,124,1.0)}{spark(474,330,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('yesterday', '暦の前のマスへ後ろ向きの矢印がのび、そばに低い太陽がしずんでいるイラスト。',
    '今日より前の1日、昨日。', f"""
{calendar(300,196,1.05,7,3,9)}
<g transform="translate(300 196) scale(1.05)">
  {arrowline([(-6,-15),(-42,-15)], TONES['coral'][0], 4)}
</g>
{sun(96,270,30)}
{person(504,352,1.0,-1,'violet','blue','point','short','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('yoga', 'マットの上であぐらをかき、背すじをのばして座っているイラスト。',
    '心と体をととのえる、インド生まれの体操、ヨガ。', f"""
<g transform="translate(300 354)">
  <rect x="-176" y="-14" width="352" height="28" rx="14" class="violet o"/>
</g>
{lotus(300,344,1.15)}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M164 208a82 82 0 0 1 40-58M436 208a82 82 0 0 0-40-58"/>
</g>
""", ground=True)

add('you', '話し手が手をさしのべ、目の前にいる相手の点線の姿を指しているイラスト。',
    '目の前にいる相手を指す「あなたは・あなたを」。', f"""
{person(160,352,1.25,1,'teal','blue','point','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10">
  <circle cx="430" cy="212" r="46"/>
  <path d="M364 350v-26q0-54 66-54t66 54v26"/>
</g>
{arrowline([(244,238),(374,214)], TONES['coral'][0], 5, True)}
{spark(502,138,0.8)}
""", ground=True, arrow=True)

add('your', '相手の点線の姿がかばんを持ち、そのかばんが囲まれて示されているイラスト。',
    '相手の持ち物を指す「あなたの」。', f"""
{person(160,352,1.2,1,'teal','blue','point','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10">
  <circle cx="440" cy="196" r="46"/>
  <path d="M374 348v-26q0-54 66-54t66 54v26"/>
</g>
<g transform="translate(440 344)">
  <path d="M-44-62h88v56a10 10 0 0 1-10 10h-68a10 10 0 0 1-10-10z" class="gold o"/>
  <path d="M-26-62q0-32 26-32t26 32" fill="none" stroke="{BRN}" stroke-width="8"/>
</g>
<ellipse cx="440" cy="310" rx="86" ry="70" fill="none" stroke="{TONES['coral'][0]}"
  stroke-width="4" stroke-dasharray="10 8"/>
{arrowline([(240,268),(346,292)], TONES['coral'][0], 5, True)}
""", ground=True, arrow=True)

add('yourself', '姿見の前に立つ人が、鏡の中の自分を見ているイラスト。',
    '自分自身、自分で。', f"""
{person(200,352,1.2,1,'teal','blue','stand','short','smile')}
{mirror(430,214,1.0)}
<g transform="translate(430 214)">
  <g transform="scale(0.9)">{person(-4,76,0.78,-1,'teal','blue','stand','short','smile')}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('zoo', '柵で囲われた場所で動物がくつろぎ、外から人が見ているイラスト。',
    '動物を飼って見せる施設、動物園。', f"""
{tree(516,346,0.72)}
{beast(388,346,0.6,'#6b5a4a',-1)}
<g transform="translate(350 348)">
  <path d="M-220-64h440v14h-440z" class="gold o"/>
  <path d="M-220-20h440v14h-440z" class="gold o"/>
  <path d="M-200 0v-72M-120 0v-72M-40 0v-72M40 0v-72M120 0v-72M200 0v-72" fill="none"
    stroke="{GLDD}" stroke-width="14" stroke-linecap="round"/>
</g>
{person(74,352,1.1,1,'teal','blue','point','short','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

finish(__file__)
