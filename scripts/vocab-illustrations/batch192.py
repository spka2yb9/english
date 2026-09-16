"""第40回: plus40(a–c)の100語。"""
from kit import *


# --- この回で使う小物 ---------------------------------------------------------

def gl(y=386):
    """地面の内側に引く水平線。"""
    return f'<path d="M60 {y}h480" class="a"/>'


def halo(x, y, rx=120, ry=100):
    """「どれか1つ」を囲む点線の輪。"""
    return (f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="none" stroke="{MUTED}" '
            f'stroke-width="4" stroke-dasharray="12 11"/>')


def apple(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-46 4q-10-46 22-58 14-6 24 6 10-12 24-6 32 12 22 58-8 42-46 44-38-2-46-44z" class="{cls} o"/>'
            f'<path d="M0-58v-20" fill="none" stroke="{BRN}" stroke-width="6" stroke-linecap="round"/>'
            f'<path d="M4-76q28-20 44 2-24 14-44-2z" class="green o"/></g>')


def ball(x, y, r=32, cls='coral'):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" class="{cls} o"/>'
            f'<path d="M{x-r} {y}q{r} -{r*0.8} {2*r} 0" fill="none" stroke="{INK}" stroke-width="2.5"/>'
            f'<path d="M{x-r*0.7} {y-r*0.7}q{r*0.7} {r*0.7} 0 {r*1.4}" fill="none" stroke="{INK}" stroke-width="2.5"/>')


def leaf(x, y, rot=0, cls='gold', s=1):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
            f'<path d="M-20 0q20-16 40 0-20 16-40 0z" class="{cls} o"/>'
            f'<path d="M-20 0h40" fill="none" stroke="{INK}" stroke-width="2"/></g>')


def butterfly(x, y, s=1, cls='violet'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<ellipse cx="-26" cy="-14" rx="26" ry="18" class="{cls} o" transform="rotate(-24 -26 -14)"/>'
            f'<ellipse cx="26" cy="-14" rx="26" ry="18" class="{cls}p o" transform="rotate(24 26 -14)"/>'
            f'<ellipse cx="-20" cy="16" rx="18" ry="13" class="{cls}p o"/>'
            f'<ellipse cx="20" cy="16" rx="18" ry="13" class="{cls} o"/>'
            f'<path d="M0-30v50" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M0-30q-14-14-24-16M0-30q14-14 24-16" fill="none" stroke="{INK}" stroke-width="3"/></g>')


def bird(x, y, s=1, cls='blue', facing=1, sing=False):
    g = [f'<g transform="translate({x} {y}) scale({s*facing} {s})">',
         f'<ellipse cx="0" cy="-34" rx="44" ry="30" class="{cls} o"/>',
         f'<path d="M-40-42L-84-56l34 30z" class="{cls}p o"/>',
         f'<path d="M-2-52q12-22 32-18 18 4 18 20-22-10-50-2z" class="{cls}p o"/>',
         f'<circle cx="34" cy="-60" r="20" class="{cls} o"/>',
         f'<path d="M50-64l24 6-24 8z" class="gold o"/>',
         f'<circle cx="40" cy="-66" r="3.5" class="ink"/>',
         f'<path d="M-10-6l-4 16M12-6l4 16" fill="none" stroke="{GLDD}" stroke-width="5" stroke-linecap="round"/>',
         f'<path d="M-18 10h18M6 10h18" fill="none" stroke="{GLDD}" stroke-width="4" stroke-linecap="round"/>']
    if sing:
        g.append(f'<g fill="none" stroke="{CRL}" stroke-width="4" stroke-linecap="round">'
                 f'<path d="M66-84q16-4 22-20M78-68q18 4 30-6"/></g>')
    g.append('</g>')
    return ''.join(g)


def bike(x, y, s=1, training=False, cls='blue'):
    ts, tp, td = TONES[cls]
    g = [f'<g transform="translate({x} {y}) scale({s})">',
         f'<g fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round">',
         f'<circle cx="-78" cy="-40" r="40"/><circle cx="78" cy="-40" r="40"/>',
         f'<path d="M-78-40L-30-102M-30-102L2-40M-78-40L2-40M2-40L62-104M-30-102L62-104M62-104V-126h36"/></g>',
         f'<circle cx="-78" cy="-40" r="7" class="ink"/><circle cx="78" cy="-40" r="7" class="ink"/>',
         f'<path d="M-56-108h46v-12h-46z" fill="{ts}" class="o"/>',
         f'<circle cx="2" cy="-40" r="14" fill="{td}" class="o"/>',
         f'<path d="M2-40l18 16M2-40l-18 16" fill="none" stroke="{td}" stroke-width="7" stroke-linecap="round"/>']
    if training:
        g.append(f'<circle cx="-116" cy="-16" r="20" fill="#fffefd" class="o"/>')
    g.append('</g>')
    return ''.join(g)


def fish(x, y, s=1, cls='blue', facing=1, stripes=0):
    g = [f'<g transform="translate({x} {y}) scale({s*facing} {s})">',
         f'<path d="M-92 0q42-44 112-38 44 4 66 38-22 34-66 38-70 6-112-38z" class="{cls} o"/>',
         f'<path d="M-92 0l-50-32v64z" class="{cls}p o"/>',
         f'<path d="M6-40q14-22 32-14" fill="none" stroke="{INK}" stroke-width="3"/>',
         f'<path d="M-4 34q14 18 30 10" fill="none" stroke="{INK}" stroke-width="3"/>',
         f'<circle cx="44" cy="-12" r="7" fill="#fffefd" stroke="{INK}" stroke-width="2"/>',
         f'<circle cx="46" cy="-12" r="3" class="ink"/>']
    for i in range(stripes):
        g.append(f'<path d="M{-60+i*26}-34q10 34 0 68" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    g.append('</g>')
    return ''.join(g)


def banana(x, y, rot=0, s=1, cls='gold'):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
            f'<ellipse rx="86" ry="30" class="{cls} o"/>'
            f'<path d="M74 0q16-2 20-16" fill="none" stroke="{GLDD}" stroke-width="7" stroke-linecap="round"/>'
            f'<path d="M-40-6q14 26 62 28" fill="none" stroke="{GLDD}" stroke-width="4"/></g>')


def bubble(x, y, w=150, h=104, dots=3):
    g = [f'<g transform="translate({x} {y})">',
         f'<rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="22" fill="#fffefd" stroke="{INK}" stroke-width="3"/>',
         f'<path d="M-30 {h/2-4}L-4 {h/2-4}L-24 {h/2+26}Z" fill="#fffefd"/>',
         f'<path d="M-30 {h/2}L-24 {h/2+26}L-4 {h/2}" fill="none" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>']
    for i in range(dots):
        g.append(f'<circle cx="{-w/4 + i*w/2/max(dots-1,1):.0f}" cy="0" r="9" class="ink"/>')
    g.append('</g>')
    return ''.join(g)


def swatch(x, y, fill, w=220, h=140):
    return (f'<g transform="translate({x} {y})">'
            f'<rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="14" fill="{fill}" stroke="{INK}" stroke-width="3"/>'
            f'<path d="M{-w/2+18} {h/2-24}q42-18 82 0t82 0" fill="none" stroke="#fffefd" stroke-width="8" '
            f'stroke-linecap="round" opacity="0.5"/></g>')


def brush(x, y, rot=0, s=1):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
            f'<path d="M-9 40h18v-120h-18z" fill="{BRN}" class="o"/>'
            f'<path d="M-15-80h30v32h-30z" fill="{STONE}" class="o"/>'
            f'<path d="M-15-48h30l-7 44h-16z" fill="#3a3f45" class="o"/></g>')


def tin(x, y, fill, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-54-46h108v-12h-108z" fill="{STONE}" class="o"/>'
            f'<path d="M-48-34h96v70h-96z" fill="#fffefd" class="o"/>'
            f'<path d="M-48-34h96v26h-96z" fill="{fill}"/>'
            f'<path d="M-48-34h96v70h-96z" fill="none" class="o"/>'
            f'<path d="M0-58q16 6 14 20" fill="none" stroke="{STONE}" stroke-width="6" stroke-linecap="round"/></g>')


def cup(x, y, s=1, cls='teal'):
    ts, tp, td = TONES[cls]
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-46-56h92l-10 62a14 14 0 0 1-14 12h-44a14 14 0 0 1-14-12z" fill="{ts}" class="o"/>'
            f'<path d="M46-42q32 4 30 28-2 22-32 22" fill="none" stroke="{td}" stroke-width="8" stroke-linecap="round"/>'
            f'<path d="M-36-56h72" fill="none" stroke="{td}" stroke-width="6"/></g>')


def umbrella(x, y, s=1, cls='blue'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-100 0q0-78 100-78t100 78q-25-14-50 0-25-14-50 0-25-14-50 0-25-14-50 0z" class="{cls} o"/>'
            f'<path d="M0-78V40q0 24-24 24t-22-18" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
            f'<path d="M0-100v-18" fill="none" stroke="{INK}" stroke-width="6"/></g>')


def bottle(x, y, s=1, cls='gold'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-13-112h26v64q36 8 36 46v96a16 16 0 0 1-16 16h-66a16 16 0 0 1-16-16v-96q0-38 36-46z" class="{cls}p o"/>'
            f'<path d="M-16-126h32v16h-32z" fill="{STONE}" class="o"/>'
            f'<path d="M-40-20h80" fill="none" stroke="{INK}" stroke-width="3"/></g>')


def plate(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<ellipse rx="150" ry="34" fill="#fffefd" class="o"/>'
            f'<ellipse rx="112" ry="22" fill="none" stroke="{MUTED}" stroke-width="3"/></g>')


def candle(x, y, h=70, cls='coral'):
    return (f'<g transform="translate({x} {y})">'
            f'<path d="M-10 0h20v-{h}h-20z" class="{cls} o"/>'
            f'<path d="M0-{h}v-14" fill="none" stroke="{INK}" stroke-width="4"/>'
            f'<path d="M0-{h+14}q-16-16 0-30 16 14 0 30z" class="gold o"/></g>')


def bulb(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<circle r="40" class="goldp o"/>'
            f'<path d="M-16 36h32v12a8 8 0 0 1-8 8h-16a8 8 0 0 1-8-8z" fill="{STONE}" class="o"/>'
            f'<path d="M-14-16q14-18 28 0M-14 0q14 18 28 0" fill="none" stroke="{GLDD}" stroke-width="4"/></g>')


def flag(x, y, h=120, cls='coral'):
    return (f'<g transform="translate({x} {y})">'
            f'<path d="M0 0v-{h}" fill="none" stroke="{BRN}" stroke-width="8" stroke-linecap="round"/>'
            f'<path d="M0-{h}h74l-16 22 16 22H0z" class="{cls} o"/></g>')


def phone(x, y, s=1, rot=0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
            f'<rect x="-24" y="-44" width="48" height="88" rx="10" fill="#3a3f45" stroke="{INK}" stroke-width="3"/>'
            f'<rect x="-17" y="-35" width="34" height="62" rx="5" fill="#cfe0f2"/></g>')


def openbox(x, y, w=200, h=120, d=50, cls='gold'):
    ts, tp, td = TONES[cls]
    return (f'<g transform="translate({x} {y})">'
            f'<path d="M{-w/2-8} {-h/2-6}l{-d} {-d} 44 30 {d} {d}z" fill="{ts}" class="o"/>'
            f'<path d="M{w/2+8} {-h/2-6}l{d} {-d} -44 30 {-d} {d}z" fill="{ts}" class="o"/>'
            f'<path d="M{-w/2} {-h/2}l{d} {-d}h{w}l{-d} {d}z" fill="{td}" class="o"/>'
            f'<path d="M{-w/2} {-h/2}h{w}v{h}h{-w}z" fill="{tp}" class="o"/>'
            f'<path d="M{w/2} {-h/2}l{d} {-d}v{h}l{-d} {d}z" fill="{td}" class="o"/></g>')


# --- a ------------------------------------------------------------------------

add('a', '1匹の犬が点線の輪で囲まれているイラスト。', '「ある〜、1つの〜」。たくさんある中のどれか1つを指す冠詞。', f"""
{beast(300,330,0.95)}
{halo(300,265,200,120)}
{gl()}
""")

add('about', '二人が向かい合い、間の吹き出しの中の物について話しているイラスト。', '「〜について」。話題をぐるりと取り囲むのが原義で、話の対象を示す。', f"""
{person(150,352,1.1,1,'teal','blue','point','short','smile')}
{person(470,352,1.1,-1,'coral','blue','think','bob','smile')}
{bubble(310,170,180,110,0)}
{ball(310,170,26,'gold')}
<g class="muted"><path d="M236 228q38 24 62 34M384 228q-38 24-62 34"/></g>
{gl()}
""")

add('above', '飛行機が雲のずっと上の空を飛んでいるイラスト。', '「〜の上に(離れて)」。接している on と違い、間があいた上の位置を表す。', f"""
{plane(300,120,0.85,0,'teal')}
{cloud(140,260,1.0,'blue')}
{cloud(440,250,0.85,'blue')}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="12 11"><path d="M50 224h500"/></g>
{gl()}
""")

add('across', '人が橋を端から端へ渡りきっていくイラスト。', '「〜を横切って」。線を横に越えて、向こう側まで届く動き。', f"""
<rect x="0" y="252" width="600" height="54" class="bluep"/>
<g fill="none" stroke="{BLU}" stroke-width="3" stroke-linecap="round"><path d="M40 286q22-14 44 0t44 0"/><path d="M440 286q22-14 44 0t44 0"/></g>
<path d="M30 250h540" fill="none" stroke="{BRN}" stroke-width="16" stroke-linecap="round"/>
<path d="M120 250q60 66 180 66M480 250q-60 66-180 66" fill="none" stroke="{BRN}" stroke-width="10"/>
{person(300,250,0.95,1,'teal','blue','walk','short','smile')}
{line(170,336,430,336,cls=CRL,w=5)}
""", arrow=True)

add('adapter', '形の違うプラグとコンセントの間に、変換アダプターが入っているイラスト。', '「変換アダプター」。規格の違うものを間に立ってつなぐ道具。', f"""
<g transform="translate(90 210)">
  <rect x="-58" y="-78" width="116" height="156" rx="16" fill="#fffdf6" class="o"/>
  <circle cx="0" cy="-30" r="13" fill="none" stroke="{INK}" stroke-width="5"/>
  <circle cx="0" cy="30" r="13" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g transform="translate(250 210)">
  <rect x="-92" y="-62" width="184" height="124" rx="20" class="teal o"/>
  <path d="M-92-40h-72v20h72zM-92 20h-72v20h72z" fill="{STONE}" class="o"/>
  <circle cx="-40" cy="0" r="10" fill="{TEAP}"/>
  <circle cx="40" cy="0" r="10" fill="{TEAP}"/>
</g>
<g transform="translate(430 210)">
  <rect x="-40" y="-38" width="80" height="76" rx="12" class="goldd o"/>
  <path d="M-40-40h-36v20h36zM-40 20h-36v20h36z" fill="{STONE}" class="o"/>
  <path d="M40 0h80" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
</g>
{gl()}
""")

add('advice', '大人が指さして助言し、聞き手の頭の上に電球がともっているイラスト。', '「助言、忠告」。相手のためになる言葉をかけて、気づかせること。', f"""
{person(160,352,1.15,1,'violet','blue','point','bun','smile')}
{person(430,352,1.15,-1,'teal','blue','hold','short','smile')}
{bulb(430,140,0.9)}
<g class="muted"><path d="M240 200h128"/></g>
{gl()}
""")

add('afraid', '犬から逃げようと、両手を上げて後ずさる人のイラスト。', '「恐れて、怖がって」。こわい物から身を引く気持ち。', f"""
{beast(450,330,0.72,facing=-1)}
{person(190,352,1.15,1,'teal','blue','up','short','surprised')}
{drop(112,216,1.3,'blue')}
{drop(256,202,0.9,'blue')}
<g class="muted"><path d="M300 246q44 32 96 20"/></g>
{gl()}
""")

add('afternoon', '時計が午後3時をさし、太陽が西へ傾いてきたイラスト。', '「午後」。正午を過ぎて日が傾き、夕方へ向かう時間帯。', f"""
{clock(130,230,54,3,0)}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="12 11"><path d="M190 84q140-24 250 132"/></g>
<circle cx="300" cy="108" r="28" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9"/>
{sun(470,250,42)}
{gl()}
""")

add('again', 'かごに入らず戻ってきたボールを、もう一度投げようとしているイラスト。', '「もう一度、また」。同じことを繰り返す動きを表す。', f"""
{person(150,352,1.15,1,'teal','blue','up','short','smile')}
<g transform="translate(470 300)">
  <path d="M0 0V-160" fill="none" stroke="{STONE}" stroke-width="14" stroke-linecap="round"/>
  <rect x="-58" y="-142" width="116" height="34" fill="#fffefd" class="o"/>
  <path d="M-44-108h88" fill="none" stroke="{CRL}" stroke-width="9" stroke-linecap="round"/>
  <path d="M-44-108v20M-15-108v26M15-108v26M44-108v20" fill="none" stroke="{MUTED}" stroke-width="3"/>
</g>
{ball(470,150,22,'gold')}
<g class="muted"><path d="M436 186q-70 60-166 40"/></g>
{ball(250,232,24,'gold')}
{gl()}
""")

add('ago', '歩いてきた道をふり返り、後方に時計が置かれているイラスト。', '「〜前に」。今からさかのぼった、過去の時点を示す。', f"""
{person(430,352,1.15,1,'teal','blue','walk','short','neutral')}
{clock(160,200,56,2,30)}
{arrowline([(370,300),(240,268)], cls=MUTED, dash=True)}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="12 11"><path d="M120 340h340"/></g>
{gl()}
""")

add('air conditioner', '壁につけた室内機から、冷たい風と雪の印が出ているイラスト。', '「エアコン、空調機」。部屋の空気を冷やしたり温めたりする装置。', f"""
<g transform="translate(300 130)">
  <rect x="-170" y="-52" width="340" height="104" rx="20" fill="#fffefd" class="o"/>
  <path d="M-146 22h292" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <path d="M-146 40h292" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <circle cx="120" cy="-16" r="12" fill="none" stroke="{MUTED}" stroke-width="3"/>
</g>
<g fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round" stroke-dasharray="16 12">
  <path d="M150 200q34 46 68 0t68 0"/>
  <path d="M320 210q34 46 68 0t68 0"/>
</g>
<g transform="translate(500 268)" fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round">
  <path d="M-30 0h60M-15-26 15 26M15-26-15 26"/>
</g>
{gl()}
""")

add('aloud', '本を手に持ち、声に出して読み上げているイラスト。', '「声に出して」。心の中でなく、耳に届く声で読むこと。', f"""
{person(290,352,1.2,1,'teal','blue','hold','short','smile')}
{book(300,286,0.66,'gold')}
<g fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round">
  <path d="M330 208q22 24 0 48"/>
  <path d="M362 190q34 42 0 84"/>
  <path d="M394 172q48 60 0 120"/>
</g>
{gl()}
""")

add('also', '同じりんごが二つ並び、両方に印がついているイラスト。', '「〜もまた」。前のものに同じものが加わることを示す。', f"""
{apple(170,240,1.0)}
{apple(430,240,1.0)}
<g fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"><path d="M272 226h56M300 198v56"/></g>
{tick(170,342,0.75)}
{tick(430,342,0.75)}
{gl()}
""")

add('always', '時計の周りを矢印が何度も回り続けているイラスト。', '「いつも、常に」。いつ何度見ても変わらない様子。', f"""
{clock(300,200,64,10,10)}
<g fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round" marker-end="url(#ar)">
  <path d="M300 96a104 104 0 1 1-22 206"/>
</g>
{gl()}
""", arrow=True)

add('am', '自分自身の胸を指さしているイラスト。', '「〜である、〜にいる」。主語が I のときにつかう be動詞。', f"""
{person(300,352,1.25,1,'teal','blue','hold','short','smile')}
{arc(150,150,272,250,60,CRL)}
{tick(300,104,0.85)}
{gl()}
""", arrow=True)

add('an', '手のひらにのせたりんごが点線で囲まれているイラスト。', '「ある〜、1つの〜」。母音で始まる語の前では an をつかう。', f"""
{apple(370,240,1.3)}
{hand(206,256,1)}
{halo(370,240,116,100)}
{gl()}
""")

add('and', 'りんごとバナナがひもで結ばれて一つになっているイラスト。', '「〜と、そして」。二つのものを並べて結びつけることば。', f"""
{apple(150,250,1.0)}
{banana(450,250,-10,1.0)}
<path d="M228 254q72-34 144-6" fill="none" stroke="{BRN}" stroke-width="6" stroke-linecap="round"/>
<circle cx="300" cy="250" r="18" fill="none" stroke="{BRN}" stroke-width="8"/>
{gl()}
""")

add('angry', '顔をしかめて両腕を上げ、頭の横に怒りの印が出ているイラスト。', '「怒った、腹を立てた」。かっとなって感情が高ぶった様子。', f"""
{person(300,352,1.3,1,'coral','blue','up','short','sad')}
{spark(190,164,1.5,'coral')}
{spark(410,158,1.3,'coral')}
<g fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round">
  <path d="M232 212q-16-14-14-34M368 210q16-14 14-34"/>
</g>
{gl()}
""")

add('animal', '草地に四つ足のけものと小鳥がいるイラスト。', '「動物」。人以外の生きものをまとめて指すことば。', f"""
{beast(250,330,0.85)}
{bird(500,296,0.62,'blue')}
{tree(80,340,0.9)}
{sun(520,110,34)}
{gl()}
""")

add('another', '手に取ったりんごとは別のもう1つが、点線で囲まれているイラスト。', '「もう1つの、別の」。同じ種類で、別の1つを指す。', f"""
{apple(160,250,1.05)}
{apple(420,250,1.15)}
{halo(420,250,108,96)}
{hand(474,148,-1)}
{line(252,222,342,232,cls=CRL,w=5)}
{gl()}
""", arrow=True)

# --- answer – apartment -------------------------------------------------------

add('answer', '手を挙げて答えようとする人と、正解を示す丸い印のイラスト。', '「答え、返事」。問いに対して、正しい内容を返すこと。', f"""
{person(180,352,1.2,1,'teal','blue','up','bob','smile')}
<circle cx="440" cy="176" r="80" fill="#fffefd" class="o"/>
{tick(440,176,1.4)}
<g class="muted"><path d="M276 200q64-24 100-34"/></g>
{gl()}
""")

add('antique', 'ひびの入った古い意が台の上に置かれ、隅にほこりがたまっているイラスト。', '「骨董の、骨董品」。作られてから、長い年月がたった古い品。', f"""
{table(300)}
<g transform="translate(300 300)">
  <path d="M-34-96h68l-6 24q44 14 44 52v6a20 20 0 0 1-20 20h-100a20 20 0 0 1-20-20v-6q0-38 44-52z" class="violet o"/>
  <g fill="none" stroke="{VIOD}" stroke-width="4"><path d="M-34-70h64M-40-42h80M-30-14h60"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-8-92l12 26 12-22"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="2.5">
  <path d="M30 56q40 4 74 26M30 56q-6 40 12 76M30 56q42 34 36 84"/>
  <path d="M96 104q-14-26-52-40M44 144q26-30-14-88"/>
</g>
{gl()}
""")

add('anyone', '三人のうち、だれか一人が点線で囲まれているイラスト。', '「だれか、だれでも」。人を特定せずに指すことば。', f"""
{person(120,352,0.95,1,'teal','blue','stand','short','smile')}
{person(300,352,0.95,1,'violet','blue','stand','bob','smile')}
{person(480,352,0.95,1,'gold','blue','stand','cap','smile')}
{halo(300,232,110,124)}
{gl()}
""")

add('anything', '箱からいろいろな物が出てきて、1つが点線で囲まれているイラスト。', '「何か、何でも」。物を特定せずに指すことば。', f"""
{ball(214,222,32,'blue')}
{apple(388,216,0.9)}
{book(300,150,0.5,'teal')}
{openbox(300,290,190,120,48,'gold')}
{halo(388,216,86,78)}
{gl()}
""")

add('apartment', '窓の並んだ集合住宅の、1室が点線で囲まれているイラスト。', '「アパート、マンションの1室」。人が暮らす、住まいの1区画。', f"""
{person(120,352,1.0,1,'coral','blue','walk','short','smile')}
{tower(360,306,1.2,'teal',4)}
{halo(360,164,88,54)}
{gl()}
""")

# --- apple – automotive -------------------------------------------------------

add('apple', '葉のついた赤いりんごが一つ置かれているイラスト。', '「りんご」。丸い実と、へたにつく葉が目印の果物。', f"""
{apple(300,300,1.5)}
{gl()}
""")

add('herring', '細長い銀色のニシンが群れになって泳いでいるイラスト。', '「ニシン」。冷たい海でよくとれる、細長い青い魚。', f"""
<rect x="0" y="60" width="600" height="246" class="bluep"/>
{fish(250,190,0.9,'blue',1)}
{fish(380,280,0.75,'blue',1)}
{fish(180,290,0.8,'blue',1)}
{fish(470,150,0.7,'blue',-1)}
<g fill="#fffefd" opacity="0.9"><circle cx="330" cy="230" r="6"/><circle cx="360" cy="212" r="4"/><circle cx="300" cy="240" r="3"/></g>
{gl()}
""")

add('archery', '弓から放たれた矢が、的の真ん中に突きささっているイラスト。', '「アーチェリー、弓術」。弓で矢を射て、的にあてる競技。', f"""
<g transform="translate(150 250)">
  <path d="M0-100q54 100 0 200" fill="none" stroke="{BRN}" stroke-width="11" stroke-linecap="round"/>
  <path d="M0-100L0 100" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M0-22q22 22 0 44" fill="none" stroke="{BRN}" stroke-width="8"/>
</g>
<g class="muted"><path d="M170 240h180"/></g>
<g transform="translate(470 240)">
  <circle r="78" class="paper"/>
  <circle r="54" fill="none" stroke="{BLU}" stroke-width="12"/>
  <circle r="30" fill="none" stroke="{CRL}" stroke-width="12"/>
  <circle r="8" class="ink"/>
  <path d="M-6 0l-70-18" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <path d="M-76-20l-18-6 8 16z" class="coral o"/>
</g>
{gl()}
""")

add('are', '二人が並んで点線で囲まれ、上に印がついているイラスト。', '「〜である、〜にいる」。you や複数の主語につく be動詞。', f"""
{person(200,352,1.05,1,'teal','blue','stand','short','smile')}
{person(400,352,1.05,1,'coral','blue','stand','bob','smile')}
{halo(300,235,172,132)}
{tick(300,92,0.85)}
{gl()}
""")

add('area', '地図の一部が境界で区切られ、内側の広さが示されているイラスト。', '「地域、区域」と「面積」。区切られた場所と、その広さ。', f"""
<path d="M60 290q-10-90 70-124 96-40 220-14 116 24 130 108z" class="greenp o"/>
<rect x="190" y="190" width="180" height="86" class="bluep o"/>
<g fill="none" stroke="{BLU}" stroke-width="3">
  <path d="M200 268l40-70M246 276l40-70M292 276l40-70M338 274l22-38"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="4"><path d="M182 190h16M182 190v16M378 190h-16M378 190v16M182 276h16M182 276v-16M378 276h-16M378 276v-16"/></g>
{gl()}
""")

add('around', '家の周りを、人がぐるりと回って歩いているイラスト。', '「〜の周りに」。あるものの周囲を囲むように動くこと。', f"""
{house(300,300,0.82,'coral')}
{person(120,290,0.85,1,'teal','blue','walk','short','smile')}
<ellipse cx="300" cy="230" rx="215" ry="118" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="14 12"/>
<g fill="none" stroke="{MUTED}" stroke-width="5" marker-end="url(#ar)"><path d="M150 332q40-28 70-38"/></g>
{gl()}
""", arrow=True)

add('arrive', '荷物を持った人が、目印の旗のところへたどり着いたイラスト。', '「到着する、着く」。目指していた場所にたどりつくこと。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="14 12"><path d="M600 302q-160-38-316 26"/></g>
{flag(170,306,132,'coral')}
{person(300,352,1.1,1,'teal','blue','walk','short','smile')}
<g transform="translate(420 320)">
  <rect x="-34" y="-26" width="68" height="52" rx="10" class="goldd o"/>
  <path d="M-14-26v-14a14 14 0 0 1 28 0v14" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
{tick(300,110,0.9)}
{gl()}
""")

add('art', 'イーゼルに立てたカンバスに絵を描き、そばにパレットが置かれているイラスト。', '「芸術、美術」。絵や彫刻など、形や色で表す表現。', f"""
<g transform="translate(340 300)">
  <path d="M-96 0L-16-72M96 0L16-72" fill="none" stroke="{BRN}" stroke-width="11" stroke-linecap="round"/>
  <path d="M-96-46h192" fill="none" stroke="{BRN}" stroke-width="12" stroke-linecap="round"/>
  <rect x="-96" y="-196" width="192" height="146" class="paper"/>
  <path d="M-70-76q42-74 84 0z" class="bluep o"/>
  <circle cx="42" cy="-158" r="22" class="gold o"/>
  <path d="M-96-150h192" fill="none" stroke="{BRN}" stroke-width="12" stroke-linecap="round"/>
</g>
<g transform="translate(110 300)">
  <ellipse rx="72" ry="52" class="goldp o"/>
  <circle cx="-30" cy="-12" r="13" class="coral"/><circle cx="2" cy="-28" r="13" class="blue"/>
  <circle cx="28" cy="-6" r="13" class="green"/><circle cx="-4" cy="10" r="13" class="violet"/>
  <ellipse cx="10" cy="28" rx="18" ry="10" fill="#fffefd" class="o"/>
  <path d="M44-40l50-50" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>
</g>
{gl()}
""")

add('ask', '一方が手を上げてたずね、相手がそれに応じているイラスト。', '「たずねる、頼む」。知りたいことや、してほしいことを相手に言う。', f"""
{person(150,352,1.15,1,'teal','blue','point','short','smile')}
{person(460,352,1.15,-1,'violet','blue','stand','bob','smile')}
{bubble(305,170,160,104,3)}
{gl()}
""")

add('at', '家の戸口の一点が、点線の輪と矢印で示されているイラスト。', '「〜に」。場所や時刻の一点を、ぴたりと指す前置詞。', f"""
{house(370,306,1.05,'coral')}
{person(140,352,1.0,1,'teal','blue','point','short','smile')}
{halo(370,282,56,38)}
{line(226,258,300,272,cls=CRL,w=5)}
{gl()}
""", arrow=True)

add('aubergine', 'つやのある紫のナスと、その切り口のイラスト。', '「ナス」。むらさき色の皮と、へたが特徴の野菜(英)。', f"""
<g transform="translate(230 250) rotate(-14)">
  <ellipse cx="0" cy="20" rx="54" ry="78" class="violet o"/>
  <path d="M-30-46h60l-10-30h-40z" class="green o"/>
  <path d="M0-76v-18" fill="none" stroke="{GRND}" stroke-width="8" stroke-linecap="round"/>
  <path d="M-38 6q-8-32 10-50" fill="none" stroke="{VIOD}" stroke-width="4"/>
</g>
<g transform="translate(460 280)">
  <circle r="62" class="violet o"/>
  <circle r="48" class="violetp"/>
  <circle r="30" fill="none" stroke="{VIOD}" stroke-width="3"/>
  <g fill="{GLDP}"><ellipse cx="-10" cy="-12" rx="5" ry="8"/><ellipse cx="12" cy="-6" rx="5" ry="8"/><ellipse cx="-2" cy="12" rx="5" ry="8"/><ellipse cx="-16" cy="6" rx="5" ry="8"/></g>
</g>
{gl()}
""")

add('mackerel', '皿の上に、背中にしま模様のあるサバがのっているイラスト。', '「サバ」。背中のしま模様が目印の、青い海の魚。', f"""
{plate(300,306,0.95)}
{fish(290,258,0.9,'blue',1,4)}
<g transform="translate(470 282)">
  <circle r="30" class="goldp o"/>
  <path d="M-30 0h60M0-30v60M-21-21 21 21M21-21-21 21" fill="none" stroke="{GLDD}" stroke-width="3"/>
</g>
{gl()}
""")

add('autumn', '木の葉が赤や黄色に色づいて、散りはじめているイラスト。', '「秋」。葉が色づき、実りの季節になる頃(英)。', f"""
{tree(250,306,1.15)}
<g class="gold o"><circle cx="212" cy="238" r="26"/><circle cx="286" cy="228" r="24"/></g>
<g class="coral o"><circle cx="232" cy="206" r="24"/></g>
{leaf(120,170,-20,'gold',1.1)}
{leaf(420,140,18,'coral',1.2)}
{leaf(470,250,30,'gold',0.9)}
{leaf(180,330,10,'coral',1.0)}
{leaf(440,346,-14,'gold',0.8)}
{leaf(320,362,22,'coral',0.9)}
{gl()}
""")

add('avalanche', '山の斜面の雪が、大きなかたまりになって落ちてくるイラスト。', '「雪崩」。山の斜面の雪が、急に崩れて落ちること。', f"""
<path d="M60 306L300 56l240 250z" fill="#e9eef2" class="o"/>
<path d="M300 56l96 100-44 6-32-32-38 26z" fill="#fffefd" class="o"/>
<g transform="translate(300 210)">
  <path d="M-74-34q62-42 124 10 42 36-10 64-62 32-114-10-32-32 0-64z" fill="#fffefd" class="o"/>
</g>
<g fill="none" stroke="{BLU}" stroke-width="4" stroke-linecap="round" stroke-dasharray="12 10">
  <path d="M168 156q62 42 34 114M414 148q-62 42-40 110"/>
</g>
{tree(130,344,0.8)}
{tree(486,344,0.72)}
{gl(356)}
""")

add('avocado', 'アボカドが一つまるごとと、種の見える半割りで並んでいるイラスト。', '「アボカド」。緑色の皮と、大きな種をもつ果実。', f"""
<g transform="translate(160 280) rotate(-12)">
  <ellipse cx="0" cy="0" rx="56" ry="78" class="green o"/>
  <ellipse cx="0" cy="-12" rx="34" ry="48" fill="#4f8a4a"/>
  <path d="M0-78v-22" fill="none" stroke="{GRND}" stroke-width="8" stroke-linecap="round"/>
</g>
<g transform="translate(430 280)">
  <ellipse rx="68" ry="86" fill="#3f6b46" class="o"/>
  <ellipse rx="56" ry="74" fill="#bfe08a"/>
  <ellipse cx="0" cy="8" rx="30" ry="34" fill="{BRN}" class="o"/>
  <ellipse cx="-11" cy="-6" rx="7" ry="11" fill="#fffefd" opacity="0.5"/>
</g>
{gl()}
""")

add('away', '家から離れて、遠くへ歩き去っていく人のイラスト。', '「離れて、向こうへ」。手もとや元いた場所から遠ざかること。', f"""
{house(110,300,0.95,'coral')}
{person(470,352,1.1,1,'teal','blue','walk','short','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="14 12"><path d="M190 342h230"/></g>
{gl()}
""")

add('axe', '丸太に斧の刃を打ちこみ、木くずが飛んでいるイラスト。', '「おの、斧」。木を割るための、重い刃のついた道具。', f"""
<g transform="translate(200 330)">
  <rect x="-126" y="-40" width="252" height="80" rx="34" class="gold o"/>
  <ellipse cx="120" cy="0" rx="18" ry="40" class="goldp o"/>
</g>
<g transform="translate(200 292) rotate(-45)">
  <path d="M0-26q-58-8-64 26 26 34 64 22z" fill="{STONE}" class="o"/>
  <path d="M-6-10h146v20h-146z" fill="{BRN}" class="o"/>
</g>
<g class="gold o"><path d="M120 220l8-22 16 12z"/><path d="M92 250l-22-4 10-18z"/><path d="M300 210l20-10 2 20z"/></g>
{gl()}
""")

# --- baby – bus ---------------------------------------------------------------

add('baby', 'ガラガラを持った赤ちゃんが、おむつをして座っているイラスト。', '「赤ちゃん、乳児」。生まれてまもない、小さな子。', f"""
<g transform="translate(280 344)">
  <path d="M-86 0q-16-66 42-78h86q58 12 42 78z" class="goldp o"/>
  <circle cx="40" cy="-106" r="52" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M14-156q10-22 34-16" fill="none" stroke="{HAIR}" stroke-width="8" stroke-linecap="round"/>
  <circle cx="24" cy="-114" r="5" class="ink"/><circle cx="58" cy="-114" r="5" class="ink"/>
  <path d="M28-86q14 12 26-2" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <path d="M-70-52l-32 12M74-52l30 24" fill="none" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
</g>
<g transform="translate(400 310)">
  <path d="M0 0l40-46" fill="none" stroke="{BRN}" stroke-width="8" stroke-linecap="round"/>
  <circle cx="48" cy="-56" r="16" class="coral o"/>
</g>
{gl()}
""")

add('babysit', '大人が小さな子と手をつなぎ、そばで見守っているイラスト。', '「(留守中の)子どもの世話をする」。親の代わりに子を見守ること。', f"""
{person(240,352,1.25,1,'teal','blue','hold','bob','smile')}
{person(400,352,0.68,1,'gold','violet','stand','short','smile')}
<path d="M252 300q56 34 114 32" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
{ball(486,336,26,'coral')}
{gl()}
""")

add('bad', '虫に食われて傷んだりんごと、その横にばつの印があるイラスト。', '「悪い、ひどい」。状態や質が、よくないこと。', f"""
{apple(240,250,1.3,'gold')}
<circle cx="212" cy="236" r="15" fill="{INK}"/>
<path d="M206 250q-16 32 6 46t30-2" fill="none" stroke="{GRN}" stroke-width="13" stroke-linecap="round"/>
<circle cx="288" cy="272" r="11" fill="{INK}"/>
{cross(460,240,1.3)}
{gl()}
""")

add('bag', '取っ手のついたかばんに、パンとりんごが入っているイラスト。', '「かばん、袋」。物を入れて持ち運ぶ、入れもの。', f"""
{apple(262,232,0.62)}
<path d="M300 150q40-22 78 4-20 34-78 26z" class="gold o"/>
<g transform="translate(300 300)">
  <path d="M-92-60h184v112a16 16 0 0 1-16 16h-152a16 16 0 0 1-16-16z" class="teal o"/>
  <path d="M-50-60q0-54 50-54t50 54" fill="none" stroke="{TEAD}" stroke-width="11" stroke-linecap="round"/>
  <path d="M-92-6h184" fill="none" stroke="{TEAD}" stroke-width="5"/>
</g>
{gl()}
""")

add('ball', 'ボールが床ではずみながら、弾んでいくイラスト。', '「ボール、球」。投げたり蹴ったりして遊ぶ、丸いもの。', f"""
{ball(140,300,40,'coral')}
<g class="muted"><path d="M190 262q50-96 130-44t140-24"/></g>
{ball(258,152,24,'coral')}
{ball(392,124,17,'coral')}
{ball(516,180,22,'coral')}
{gl()}
""")

add('banana', '房になったバナナと、皮をむいた1本が並んでいるイラスト。', '「バナナ」。細長く曲がった、黄色い果物。', f"""
{banana(170,206,-26,0.78)}
{banana(170,258,-14,0.84)}
{banana(170,312,-4,0.9)}
<g transform="translate(430 270)">
  <ellipse rx="62" ry="26" class="goldp o"/>
  <path d="M-58 6q-26 34 6 56 42 22 64-12-34-12-46-44z" class="gold o"/>
  <path d="M58-4q30 26 2 56-24 24-56 6 30-18 40-54z" class="gold o"/>
</g>
{gl()}
""")

add('banjo', '丸い胴と長い棹をもつバンジョーを、手で弾いているイラスト。', '「バンジョー」。丸い胴に弦を張った、弦楽器。', f"""
<g transform="translate(300 270) rotate(-16)">
  <rect x="88" y="-18" width="232" height="36" rx="12" class="goldd o"/>
  <circle cx="0" cy="0" r="94" class="goldp o"/>
  <circle cx="0" cy="0" r="34" fill="#fffefd" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="2"><path d="M-80-20h330M-80 0h330M-80 20h330"/></g>
  <path d="M300-22v44" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
{hand(232,178,-1)}
<g fill="none" stroke="{CRL}" stroke-width="4" stroke-linecap="round"><path d="M168 324q-24-18-20-44M136 344q-34-24-26-58"/></g>
{gl()}
""")

add('bank', '柱の並んだ銀行の建物と、その前に置かれた硬貨のイラスト。', '「銀行」。お金を預けたり借りたりする、金融の機関。', f"""
<g transform="translate(340 306)">
  <path d="M-190-84L0-172l190 88z" class="goldd o"/>
  <path d="M-158-84h316v18h-316z" class="goldp o"/>
  <rect x="-134" y="-66" width="268" height="66" fill="#fffdf6" class="o"/>
  <g class="goldp o"><rect x="-110" y="-60" width="24" height="60"/><rect x="-58" y="-60" width="24" height="60"/><rect x="34" y="-60" width="24" height="60"/><rect x="86" y="-60" width="24" height="60"/></g>
  <path d="M-26 0v-40h52v40z" class="gold o"/>
  <path d="M-158 0h316" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
</g>
{coin(160,290,26)}
{coin(112,300,20)}
{gl()}
""")

add('barber', 'いすに座った客の髪を、理髪師がはさみで切っているイラスト。', '「理髪師、床屋」。髪を切ったり、整えたりする人。', f"""
<g transform="translate(110 250)">
  <rect x="-24" y="-72" width="48" height="144" rx="24" fill="#fffefd" class="o"/>
  <g fill="none" stroke="{CRL}" stroke-width="9" stroke-linecap="round"><path d="M-18-60l20 20M-18-40l20 20M-18-20l20 20M-18 0l20 20M-18 20l20 20M-18 40l20 20"/></g>
</g>
{chair(300,352,1.0,'gold')}
{sit(300,352,1.0,1,'teal','blue','short','smile')}
{person(470,352,1.0,-1,'violet','blue','reach','bun','smile')}
<g transform="translate(388 244) rotate(-20)">
  <path d="M-30 0l62-28M-30 0l62 28" fill="none" stroke="{STONE}" stroke-width="7" stroke-linecap="round"/>
  <circle cx="-34" cy="-8" r="10" fill="none" stroke="{STONE}" stroke-width="6"/>
  <circle cx="-34" cy="8" r="10" fill="none" stroke="{STONE}" stroke-width="6"/>
</g>
{gl()}
""")

add('bath', '湯を張った浴槽に人がつかり、泡が浮いているイラスト。', '「入浴、浴槽」。湯につかって体を洗うこと、その容器。', f"""
<g transform="translate(300 322)">
  <path d="M-172-72h344v34a74 74 0 0 1-74 74h-196a74 74 0 0 1-74-74z" fill="#fffefd" class="o"/>
  <path d="M-160-58h320v22a60 60 0 0 1-60 60h-200a60 60 0 0 1-60-60z" class="bluep"/>
  <path d="M-172-72h344" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
</g>
<g transform="translate(300 268)">
  <circle r="46" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-42-14q0-44 42-44t42 42q-16-18-42-18t-42 20z" fill="{HAIR}"/>
  <circle cx="-14" cy="6" r="4" class="ink"/><circle cx="14" cy="6" r="4" class="ink"/>
  <path d="M-12 22q12 12 24 0" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g class="bluep o"><circle cx="196" cy="222" r="24"/><circle cx="156" cy="266" r="16"/><circle cx="436" cy="216" r="20"/><circle cx="472" cy="262" r="14"/></g>
{gl()}
""")

add('batter', 'ボウルに入った衣と、そばの泡立て器と具のイラスト。', '「(料理の)衣、生地」。粉と水分を混ぜた、揚げ物につけるとろみ。', f"""
<g transform="translate(230 300)">
  <path d="M-124-52h248l-32 98a22 22 0 0 1-22 16h-140a22 22 0 0 1-22-16z" fill="#fffefd" class="o"/>
  <path d="M-114-40h228l-24 74a12 12 0 0 1-12 10h-156a12 12 0 0 1-12-10z" class="goldp"/>
  <ellipse cx="0" cy="-52" rx="124" ry="18" fill="none" class="o"/>
</g>
<g transform="translate(430 230) rotate(18)">
  <path d="M-9-160h18v96h-18z" fill="{STONE}" class="o"/>
  <g fill="none" stroke="{STONE}" stroke-width="7"><path d="M0-64q-48 32 0 66 48-34 0-66zM0-64q-26 46 0 78 26-32 0-78z"/></g>
</g>
<g transform="translate(430 340)">
  <ellipse rx="86" ry="22" class="paper"/>
  <path d="M-46-6q22-26 66-16 30 8 28 26-34 10-94-6z" class="gold o"/>
</g>
{gl()}
""")

add('be', '木とベンチのある場所に人が立ち、足もとが点線で囲まれているイラスト。', '「〜である、〜にいる」。主語の状態や居場所を表す be動詞の原形。', f"""
{person(290,352,1.15,1,'teal','blue','stand','short','smile')}
{tree(110,340,0.85)}
<g transform="translate(480 300)">
  <path d="M-66-34h132v14h-132z" class="goldd o"/>
  <path d="M-56 0h112v12h-112z" class="gold o"/>
  <path d="M-48 12v34M48 12v34" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>
  <path d="M-56-64h112v12h-112z" class="goldd o"/>
  <path d="M-48-52v18M48-52v18" fill="none" stroke="{BRN}" stroke-width="8" stroke-linecap="round"/>
</g>
{halo(290,352,92,26)}
{gl()}
""")

add('beach', '砂浜にパラソルとビーチボールがあり、海が広がっているイラスト。', '「浜辺、ビーチ」。海や湖に面した、砂の平地。', f"""
<rect x="0" y="196" width="600" height="82" class="bluep"/>
<g fill="none" stroke="{BLU}" stroke-width="4" stroke-linecap="round"><path d="M40 240q26-16 52 0t52 0M380 264q26-16 52 0t52 0"/></g>
{sun(510,104,40)}
<g transform="translate(210 300)">
  <path d="M0 0V-140" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>
  <path d="M-84-128q84-78 168 0z" class="coral o"/>
  <path d="M-28-140q28-46 56-40-8 24-16 40z" fill="#fffefd"/>
</g>
{ball(400,332,30,'coral')}
{gl()}
""")

add('beautiful', '大きな花が咲き、光のきらめきとちょうちょが集まっているイラスト。', '「美しい、きれいな」。見て心が引かれるほど、すばらしい様子。', f"""
{flower(300,250,2.0,'coral')}
{spark(170,190,1.4)}
{spark(430,160,1.1)}
{spark(300,96,0.9)}
{butterfly(480,262,0.85,'violet')}
{person(110,352,0.95,1,'teal','blue','point','bob','smile')}
{gl()}
""")

add('because', '雨雲から雨が降り、その下で人が傘をさしているイラスト。', '「〜だから、〜なので」。理由と結果をつなぐことば。', f"""
{cloud(220,130,1.2,'blue')}
<g fill="none" stroke="{BLU}" stroke-width="4" stroke-linecap="round"><path d="M156 188l-10 28M206 198l-10 28M256 188l-10 28M300 198l-10 28"/></g>
{person(410,352,1.15,1,'teal','blue','hold','short','smile')}
{umbrella(424,214,0.8,'blue')}
<g class="muted"><path d="M330 176q40 30 62 52"/></g>
{gl()}
""")

add('become', '青虫が、矢印の先でちょうちょに変わっているイラスト。', '「〜になる」。ある状態から、別の状態へ変わること。', f"""
<g transform="translate(150 320)">
  <g class="green o"><circle cx="-92" cy="-20" r="24"/><circle cx="-50" cy="-22" r="26"/><circle cx="-4" cy="-20" r="25"/><circle cx="40" cy="-16" r="22"/></g>
  <path d="M-104-40l-12-20M-86-44l-4-22" fill="none" stroke="{GRND}" stroke-width="4" stroke-linecap="round"/>
  <circle cx="-100" cy="-26" r="3" class="ink"/><circle cx="-88" cy="-28" r="3" class="ink"/>
</g>
{arc(140,240,368,196,72,CRL)}
{butterfly(478,180,1.0,'violet')}
{gl()}
""", arrow=True)

add('bed', 'ベッドに横になって、気持ちよさそうに眠っているイラスト。', '「ベッド、寝床」。横になって眠るための家具。', f"""
<g transform="translate(300 330)">
  <path d="M-196 0h392v16h-392z" fill="{BRN}"/>
  <path d="M-190 16v34M182 16v34" fill="none" stroke="{BRN}" stroke-width="14" stroke-linecap="round"/>
  <path d="M-196-108h24v108h-24z" fill="{BRN}"/>
  <rect x="-170" y="-44" width="352" height="46" rx="12" fill="#fffefd" class="o"/>
  <rect x="-150" y="-32" width="300" height="44" rx="16" class="teal o"/>
  <rect x="-164" y="-66" width="80" height="32" rx="15" fill="#fffefd" class="o"/>
  <circle cx="-118" cy="-76" r="28" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-136-86q18-20 36-2" fill="none" stroke="{HAIR}" stroke-width="8"/>
  <path d="M-128-72q10-8 20 0" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"><path d="M180 186q22-22 0-44M212 166q18-18 0-36"/></g>
{gl()}
""")

add('beer', '泡のあふれたビールのジョッキが、机の上に置かれているイラスト。', '「ビール」。麦から作られる、泡の出る苦い酒。', f"""
{table(300)}
<g transform="translate(280 300)">
  <path d="M-80-158h160v142a16 16 0 0 1-16 16h-128a16 16 0 0 1-16-16z" fill="#fffefd" class="o"/>
  <path d="M-74-116h148v100a10 10 0 0 1-10 10h-128a10 10 0 0 1-10-10z" class="gold"/>
  <path d="M80-116q42 6 40 44t-42 44" fill="none" stroke="{STONE}" stroke-width="16" stroke-linecap="round"/>
  <g class="bluep o"><circle cx="-40" cy="-78" r="7"/><circle cx="10" cy="-56" r="5"/><circle cx="44" cy="-84" r="6"/><circle cx="-10" cy="-34" r="4"/></g>
  <g fill="#fffefd" class="o"><circle cx="-62" cy="-142" r="20"/><circle cx="-22" cy="-152" r="24"/><circle cx="24" cy="-146" r="22"/><circle cx="58" cy="-136" r="16"/></g>
</g>
{gl()}
""")

add('beetroot', '丸くふくらんだ赤紫の根と、青々とした葉のイラスト。', '「ビート、テンサイの根」。濃い赤紫色をした、根の野菜(英)。', f"""
<g transform="translate(300 300)">
  <path d="M0 48q-74-26-68-98 6-48 68-48t68 48q6 72-68 98z" class="violet o"/>
  <path d="M0 48v36" fill="none" stroke="{VIOD}" stroke-width="9" stroke-linecap="round"/>
  <path d="M-34 4q-16-42 4-66" fill="none" stroke="{VIOD}" stroke-width="4"/>
  <g class="green o"><ellipse cx="-42" cy="-152" rx="20" ry="46" transform="rotate(-28 -42 -152)"/><ellipse cx="42" cy="-152" rx="20" ry="46" transform="rotate(28 42 -152)"/><ellipse cx="0" cy="-168" rx="18" ry="48"/></g>
</g>
{gl()}
""")

add('begin', 'スタートラインに立ち、前方へ走り出そうとしているイラスト。', '「始める、始まる」。物事の、最初の一歩を踏み出すこと。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12"><path d="M150 176v146"/></g>
{flag(150,176,62,'coral')}
{person(200,352,1.15,1,'teal','blue','walk','short','smile')}
{line(300,186,470,186,cls=CRL,w=5)}
{gl()}
""", arrow=True)

add('beginner', '補助輪のついた自転車にまたがり、おそるおそる進むイラスト。', '「初心者」。習い始めて、まだ間もない人。', f"""
{bike(300,344,1.0,training=True)}
{person(452,352,1.0,-1,'teal','blue','hold','cap','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" stroke-dasharray="10 9"><path d="M140 316h50M124 344h44"/></g>
{gl()}
""")

add('behind', '大きな箱の後ろに隠れて、頭と手だけのぞかせているイラスト。', '「〜の後ろに」。ある物を隔てて、見えない側にあること。', f"""
{person(300,352,1.6,1,'teal','blue','up','short','smile')}
{box(300,300,190,130,44,'gold')}
{gl()}
""")

add('believe', '書類を見て、頭の上に正しいという印が浮かんでいるイラスト。', '「信じる、〜だと思う」。本当だとして、受け入れること。', f"""
{doc(180,240,150,180,4)}
{person(440,352,1.2,-1,'teal','blue','think','bob','smile')}
{tick(440,132,1.1)}
<g class="muted"><path d="M300 244q64 0 100 30"/></g>
{gl()}
""")

add('below', '水面の下を魚が泳ぎ、水面には小舟が浮かんでいるイラスト。', '「〜より下に、以下の」。基準より低い位置を表す。', f"""
<rect x="0" y="200" width="600" height="106" class="bluep"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="14 12"><path d="M30 200h540"/></g>
<g transform="translate(170 200)">
  <path d="M-84 0h168l-24 30h-120z" class="coral o"/>
  <path d="M-30-10l-46 34M30-10l46 34" fill="none" stroke="{BRN}" stroke-width="8" stroke-linecap="round"/>
</g>
{fish(320,270,0.9,'blue',1)}
<g fill="#fffefd" opacity="0.9"><circle cx="360" cy="228" r="6"/><circle cx="386" cy="212" r="4"/></g>
{gl()}
""")

add('big', '大きな箱と、その脇に小さな箱が並んでいるイラスト。', '「大きい」と「重要な」。かさや程度が、はなはだしいこと。', f"""
{box(220,300,240,170,56,'blue')}
{box(496,324,70,46,18,'blue')}
{spark(150,150,1.4)}
{gl()}
""")

add('bike', 'かごのついた自転車が、走っているイラスト。', '「自転車」。ペダルをこいで進む、二輪の乗り物(口語)。', f"""
{bike(300,344,1.15)}
<g transform="translate(398 214)"><path d="M-26 16h52l-10 34h-32z" class="goldd o"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"><path d="M126 300h-52M112 332h-44"/></g>
{gl()}
""")

add('bikini', 'ハンガーにかけた上下2枚の水着と、そばのビーチボールのイラスト。', '「ビキニ(水着)」。上下2枚に分かれた、女性用の水着。', f"""
<g transform="translate(300 240)">
  <path d="M-70-150v-52l70 38 70-38v52" fill="none" stroke="{STONE}" stroke-width="8" stroke-linecap="round"/>
  <path d="M-84-100q84-44 168 0l-26 34q-58-34-116 0z" class="coral o"/>
  <path d="M-84-100h-26M84-100h26" fill="none" stroke="{CRLD}" stroke-width="8" stroke-linecap="round"/>
  <path d="M-62 6q62-36 124 0l-18 36q-44-26-88 0z" class="coral o"/>
  <path d="M-62 6l-30-14M62 6l30-14" fill="none" stroke="{CRLD}" stroke-width="8" stroke-linecap="round"/>
</g>
{ball(490,320,30,'gold')}
{sun(120,120,34)}
{gl()}
""")

add('bird', '枝にとまった小鳥が、さえずっているイラスト。', '「鳥」。羽とくちばしをもち、空を飛ぶ生きもの。', f"""
<path d="M50 216h500" fill="none" stroke="{BRN}" stroke-width="16" stroke-linecap="round"/>
<g class="green o"><ellipse cx="110" cy="196" rx="26" ry="12" transform="rotate(-24 110 196)"/><ellipse cx="500" cy="200" rx="24" ry="11" transform="rotate(20 500 200)"/></g>
{bird(300,200,1.25,'blue',1,sing=True)}
{gl()}
""")

add('birthday', 'ろうそくの火のついたケーキと、浮かんだ風船のイラスト。', '「誕生日」。生まれた日を祝う、毎年めぐってくる日。', f"""
{table(300)}
<g transform="translate(300 300)">
  <path d="M-110 0v-72h220v72z" class="coral o"/>
  <path d="M-110-72q110-26 220 0" fill="#fffefd" class="o"/>
  <path d="M-110-42h220" fill="none" stroke="{CRLP}" stroke-width="12"/>
</g>
{candle(250,228,54,'gold')}
{candle(300,228,66,'teal')}
{candle(350,228,48,'violet')}
<g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M110 100q22 60 44 130M490 100q-22 60-44 130"/></g>
<ellipse cx="110" cy="58" rx="34" ry="42" class="coral o"/>
<ellipse cx="490" cy="58" rx="34" ry="42" class="blue o"/>
{gl()}
""")

add('black', '絵の具の缶と筆で、黒い色面が塗られているイラスト。', '「黒い、黒」。光をほとんど反射しない、いちばん暗い色。', f"""
{tin(130,296,'#22262c')}
{swatch(370,250,'#22262c')}
{brush(440,214,20)}
{gl()}
""")

add('blackboard', '黒板にチョークの線が書かれ、チョークと黒板消しが置かれているイラスト。', '「黒板」。教室でチョークをつかって書く、黒い板。', f"""
<g transform="translate(300 232)">
  <rect x="-222" y="-130" width="444" height="260" rx="10" fill="#33403f" stroke="{BRN}" stroke-width="14"/>
  <g fill="none" stroke="#fffefd" stroke-width="6" stroke-linecap="round">
    <path d="M-170-72q40-30 80 0t80 0"/>
    <path d="M-170-22h180"/>
    <path d="M-170 28q60 26 130-6"/>
  </g>
  <path d="M-180 132h360" fill="none" stroke="{BRN}" stroke-width="16" stroke-linecap="round"/>
  <path d="M-150 148h72" fill="none" stroke="#fffefd" stroke-width="16" stroke-linecap="round"/>
  <rect x="92" y="126" width="82" height="32" rx="8" class="violet o"/>
</g>
{gl()}
""")

add('blazer', 'ハンガーにかかった上着が、えりとポケットを見せているイラスト。', '「ブレザー、上着」。えりのある、かっちりした上着。', f"""
<g transform="translate(300 210)">
  <path d="M0-152v-40" fill="none" stroke="{STONE}" stroke-width="8"/>
  <path d="M-72-152h144l-16 26h-112z" fill="{STONE}" class="o"/>
  <path d="M-88-118q22-34 88-34t88 34v206a14 14 0 0 1-14 14h-148a14 14 0 0 1-14-14z" class="blue o"/>
  <path d="M-30-146L-58-32l32 4z" class="blued o"/>
  <path d="M30-146L58-32l-32 4z" class="blued o"/>
  <path d="M-22-146L0-26l22-120z" fill="#fffefd" class="o"/>
  <g class="goldp o"><circle cx="0" cy="4" r="7"/><circle cx="0" cy="42" r="7"/></g>
  <path d="M-72 56h46v26h-46z" class="blued o"/>
</g>
{gl()}
""")

add('blue', '絵の具の缶と筆で、青い色面が塗られているイラスト。', '「青い、青」。晴れた空や、海の色。', f"""
{tin(130,296,BLU)}
{swatch(370,250,BLU)}
{brush(440,214,20)}
{gl()}
""")

add('boat', '小舟が水面に浮かび、オールが添えられているイラスト。', '「ボート、小舟」。こいで進む、小さな舟。', f"""
<rect x="0" y="238" width="600" height="68" class="bluep"/>
<g fill="none" stroke="{BLU}" stroke-width="4" stroke-linecap="round"><path d="M40 272q22-14 44 0t44 0M440 268q22-14 44 0t44 0"/></g>
<g transform="translate(300 238)">
  <path d="M-152 0h304l-58 58h-188z" class="coral o"/>
  <path d="M-142-14h284" fill="none" stroke="{CRLD}" stroke-width="10" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{BRN}" stroke-width="8" stroke-linecap="round">
  <path d="M232 196l56 76M368 196l-56 76"/>
</g>
<g class="goldd o"><ellipse cx="300" cy="286" rx="26" ry="12"/><ellipse cx="300" cy="286" rx="26" ry="12"/></g>
{gl()}
""")

add('body', '体全体が点線で囲まれ、関節の位置に印がついているイラスト。', '「体、身体」。人や動物の、頭から足までの全体。', f"""
{person(300,352,1.25,1,'teal','blue','stand','short','smile')}
<ellipse cx="300" cy="240" rx="90" ry="152" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 11"/>
<g class="coral o"><circle cx="272" cy="264" r="8"/><circle cx="328" cy="264" r="8"/><circle cx="262" cy="296" r="7"/><circle cx="338" cy="296" r="7"/><circle cx="283" cy="364" r="7"/><circle cx="317" cy="364" r="7"/></g>
{gl()}
""")

add('bored', 'いすにだらりと座り、時計を見てあきているイラスト。', '「退屈した、飽きた」。することがなくて、いやになってくる様子。', f"""
{chair(230,352,1.0,'gold')}
{sit(230,352,1.05,1,'teal','blue','short','neutral',arm='up')}
{clock(480,214,56,4,0)}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9"><path d="M300 200h104"/></g>
{gl()}
""")

add('boring', '同じ形の棒が並ぶ話を聞きながら、居眠りしている人のイラスト。', '「退屈な、つまらない」。関心がわかず、長く感じられる様子。', f"""
{bar(120,250,[30,30,30,30,30,30],36,10,1.5,'blue')}
{sit(470,352,1.0,-1,'teal','blue','short','neutral',arm='down')}
<g class="muted"><circle cx="516" cy="212" r="9"/></g>
<g class="muted"><circle cx="540" cy="180" r="12"/></g>
{gl()}
""")

add('born', '卵の殻が割れて、中からひなが生まれ出ているイラスト。', '「生まれた」。この世に出てきたことを表す。', f"""
<g transform="translate(290 306)">
  <path d="M-64-3q64-14 64 60 0 66-64 66t-64-66q0-74 64-60z" fill="#fffefd" class="o"/>
  <path d="M-64-2l20 12 18-14 18 14 10-10" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-24 24l14-12M6 28l16-14" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(290 280)">
  <circle r="42" class="gold o"/>
  <circle cx="-14" cy="-8" r="5" class="ink"/><circle cx="14" cy="-8" r="5" class="ink"/>
  <path d="M-8 12l16 0-8 10z" class="coral o"/>
  <path d="M30 6q22 4 20 22-20 10-34-6z" class="goldp o"/>
</g>
<g transform="translate(452 320) rotate(26)">
  <path d="M-62 0q0-62 62-62t62 62z" fill="#fffefd" class="o"/>
  <path d="M-62 0l22-14 20 12 18-14 14 12" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
{spark(180,150,1.3)}{spark(430,148,1.0)}
{gl()}
""")

add('both', '同じ茶わんが二つ並び、両方に印がついているイラスト。', '「両方の、どちらも」。二つのうちの一方だけでなく、どちらも指す。', f"""
{cup(200,300,1.15,'teal')}
{cup(400,300,1.15,'coral')}
{tick(200,148,1.0)}
{tick(400,148,1.0)}
{halo(300,232,214,146)}
{gl()}
""")

add('bottle opener', '栓抜きでびんのふたを外し、ふたが浮き上がっているイラスト。', '「栓抜き」。びんのふたを、てこの力で外す道具。', f"""
{bottle(250,290,0.78)}
<g transform="translate(258 202) rotate(30)">
  <path d="M-8-14h150v22h-150z" fill="{STONE}" class="o"/>
  <path d="M-8-14q-30 14-26 44 30 6 50-14z" fill="{STONE}" class="o"/>
  <circle cx="16" cy="24" r="9" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g transform="translate(400 176) rotate(-26)">
  <rect x="-36" y="-13" width="72" height="26" rx="7" class="coral o"/>
</g>
{line(400,158,486,116,cls=CRL,w=5)}
{gl()}
""", arrow=True)

add('box', 'ふたの開いた段ボール箱が、床に置かれているイラスト。', '「箱」。物を入れて、運ぶための四角い入れもの。', f"""
{openbox(300,300,190,126,48,'gold')}
{gl()}
""")

add('boxer', 'グローブをつけた人が、ぶら下がったサンドバッグを打っているイラスト。', '「ボクサー」。ボクシングをする人、その選手。', f"""
{person(170,352,1.2,1,'coral','blue','point','short','smile')}
<g class="coral o"><circle cx="264" cy="272" r="25"/><circle cx="132" cy="318" r="25"/></g>
<g transform="translate(470 300)">
  <path d="M0 0v-56" fill="none" stroke="{MUTED}" stroke-width="5"/>
  <rect x="-54" y="-156" width="108" height="100" rx="28" class="goldd o"/>
  <g fill="none" stroke="{GLD}" stroke-width="4"><path d="M-54-126h108M-54-96h108"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"><path d="M406 186q24-18 6-42M372 202q24-18 6-42"/></g>
{gl()}
""")

add('boy', '帽子をかぶった男の子が、ボールで遊んでいるイラスト。', '「男の子、少年」。年がいかない、男の子。', f"""
{person(270,352,0.94,1,'blue','gold','walk','cap','smile')}
{ball(470,320,32,'coral')}
{line(356,292,418,306,cls=CRL,w=5)}
{gl()}
""", arrow=True)

add('bread', '焼きたてのパンの山と、切り分けた一切れのイラスト。', '「パン」。粉をこねて焼いた、主食になる食べ物。', f"""
{table(300)}
<g transform="translate(210 300)">
  <path d="M-142 0q-12-86 46-98 100-24 214 0 58 12 46 98z" class="gold o"/>
  <path d="M-104-88q62-16 136-8" fill="none" stroke="{GLDP}" stroke-width="10" stroke-linecap="round"/>
  <path d="M-60-96q10 40 0 90" fill="none" stroke="{GLDD}" stroke-width="4"/>
</g>
<g transform="translate(468 300)">
  <path d="M-50 0q-8-88 50-88t50 88z" fill="#fffefd" class="o"/>
  <path d="M-50 0q-8-88 50-88t50 88z" fill="none" stroke="{GLDD}" stroke-width="5"/>
  <path d="M-28-40q-6-30 28-30" fill="none" stroke="{GLDP}" stroke-width="6"/>
</g>
{gl()}
""")

add('break', '両手で持った棒が、真ん中から折れているイラスト。', '「壊す、割る」。力を加えて、ものを二つに分けること。', f"""
<g transform="translate(300 250)">
  <path d="M-220 0L-18-8" fill="none" stroke="{BRN}" stroke-width="26" stroke-linecap="round"/>
  <path d="M22 8L220 14" fill="none" stroke="{BRN}" stroke-width="26" stroke-linecap="round"/>
  <path d="M-18-8l12-16M22 8l-12 14" fill="none" stroke="{GLDD}" stroke-width="4"/>
  <g fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round"><path d="M-34-26l-16-16M0-38v-22M34-22l16-16"/></g>
</g>
{hand(96,262,1)}
{hand(506,266,-1)}
{gl()}
""")

add('bring', '箱を抱えた人が、待っている相手の方へ歩いていくイラスト。', '「持ってくる、連れてくる」。話し手の方へ、物や人を運んでくる。', f"""
{person(150,352,1.15,1,'teal','blue','carry','short','smile')}
{box(152,296,92,70,26,'gold')}
{person(490,352,1.1,-1,'coral','blue','up','bob','smile')}
{line(268,240,392,240,cls=CRL,w=5)}
{gl()}
""", arrow=True)

add('brother', '背の違う二人の男の子が、並んでボールで遊んでいるイラスト。', '「兄、弟」。同じ親から生まれた、男きょうだい。', f"""
{person(200,352,1.25,1,'blue','blue','stand','short','smile')}
{person(420,352,0.92,1,'green','gold','stand','cap','smile')}
<path d="M262 244q38-28 76 0" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>
{ball(312,346,24,'coral')}
{gl()}
""")

add('brown', '絵の具の缶と筆で、茶色の色面が塗られているイラスト。', '「茶色の、茶色」。土や木の皮のような、暗い橙の色。', f"""
{tin(130,296,BRN)}
{swatch(370,250,BRN)}
{brush(440,214,20)}
{gl()}
""")

add('build', 'れんがを積み上げて、壁を造っているイラスト。', '「建てる、組み立てる」。材料を組み合わせて、形あるものにする。', f"""
<g transform="translate(400 300)">
  <g class="coral o">
    <rect x="-120" y="-184" width="120" height="42"/><rect x="0" y="-184" width="120" height="42"/>
    <rect x="-120" y="-138" width="120" height="42"/><rect x="0" y="-138" width="120" height="42"/>
    <rect x="-120" y="-92" width="120" height="42"/><rect x="0" y="-92" width="120" height="42"/>
    <rect x="-120" y="-46" width="120" height="42"/><rect x="0" y="-46" width="120" height="42"/>
  </g>
</g>
{person(160,352,1.15,1,'teal','blue','carry','short','smile')}
<rect x="112" y="272" width="92" height="40" class="coral o"/>
<g transform="translate(280 250) rotate(24)">
  <path d="M-8 0h16v-56h-16z" fill="{BRN}" class="o"/>
  <path d="M-30 0h60l-10 22h-40z" fill="{STONE}" class="o"/>
</g>
{gl()}
""")

add('building', '窓の並んだ高い建物と、その前の木のイラスト。', '「建物、ビル」。人が住んだり働いたりするために、建てたもの。', f"""
{tower(390,306,1.3,'teal',4)}
{tree(96,344,1.0)}
{person(210,352,1.0,1,'coral','blue','walk','short','smile')}
{gl()}
""")

add('bus', 'バスが停留所にとまり、人が乗りこもうとしているイラスト。', '「バス」。多くの人が乗って、決まった道を走る車。', f"""
<g transform="translate(370 300)">
  <rect x="-200" y="-142" width="380" height="142" rx="24" class="blue o"/>
  <g class="bluep o">
    <rect x="-180" y="-126" width="72" height="54" rx="8"/><rect x="-94" y="-126" width="72" height="54" rx="8"/>
    <rect x="-8" y="-126" width="72" height="54" rx="8"/><rect x="78" y="-126" width="70" height="54" rx="8"/>
  </g>
  <path d="M180-142h28a22 22 0 0 1 22 22v98a22 22 0 0 1-22 22h-28z" class="blue o"/>
  <rect x="188" y="-126" width="42" height="54" rx="8" class="bluep o"/>
  <circle cx="-120" cy="-4" r="34" fill="#3a3f45" class="o"/>
  <circle cx="120" cy="-4" r="34" fill="#3a3f45" class="o"/>
  <path d="M-200 0h380" fill="none" stroke="{BLUD}" stroke-width="10"/>
</g>
<g transform="translate(96 300)">
  <path d="M0 0v-104" fill="none" stroke="{STONE}" stroke-width="9" stroke-linecap="round"/>
  <circle r="26" class="gold o"/>
</g>
{person(200,352,1.0,1,'teal','blue','walk','short','smile')}
{line(230,236,300,254,cls=CRL,w=5)}
{gl()}
""", arrow=True)

add('business', '書類と硬貨をやり取りしている二人と、そばの鞄のイラスト。', '「仕事、商売」。お金や品をやり取りして、成り立つ活動。', f"""
{person(190,352,1.15,1,'blue','blue','give','short','smile')}
{person(440,352,1.15,-1,'violet','blue','hold','bun','smile')}
{doc(316,250,104,140,4)}
{coin(316,340,22)}
<g transform="translate(90 344)">
  <rect x="-58" y="-38" width="116" height="76" rx="12" class="goldd o"/>
  <path d="M-24-38v-14h48v14" fill="none" stroke="{BRN}" stroke-width="8"/>
</g>
{gl()}
""")

add('busy', '書類と電話を同時に扱い、頭の上に時計が浮かんでいるイラスト。', '「忙しい」。やることが多くて、余裕がない様子。', f"""
{person(280,352,1.25,1,'coral','blue','up','short','neutral')}
{doc(140,232,104,140,4)}
{phone(392,220,1.1,-16)}
{clock(300,112,44,3,0)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"><path d="M206 200q-24-16-14-38M424 190q26-14 16-38"/></g>
{gl()}
""")

add('buy', '店の人に硬貨を渡して、品物を受け取っているイラスト。', '「買う」。代金を払って、品物を手に入れること。', f"""
{table(300)}
{person(470,300,1.0,-1,'violet','blue','hold','bun','smile')}
{apple(392,282,0.62)}
{apple(448,282,0.62)}
{person(170,352,1.15,1,'teal','blue','give','short','smile')}
{coin(300,300,26)}
{line(252,286,300,296,cls=CRL,w=5)}
{gl()}
""", arrow=True)

add('cake', '皿にのった層になったケーキと、上のさくらんぼのイラスト。', '「ケーキ、菓子」。粉と卵を焼いて、甘く仕上げた食べ物。', f"""
{plate(300,336,0.92)}
<g transform="translate(300 326)">
  <path d="M-96 0v-46h192v46z" class="gold o"/>
  <path d="M-96-46h192v-30h-192z" fill="#fffefd" class="o"/>
  <path d="M-96-76h192v-28h-192z" class="goldd o"/>
  <circle cx="0" cy="-120" r="18" class="coral o"/>
  <path d="M0-138q8-14 20-16" fill="none" stroke="{GRND}" stroke-width="5" stroke-linecap="round"/>
</g>
{gl()}
""")

add('call', '電話を耳にあてて、話しているイラスト。', '「電話する、呼ぶ」。声を届けて、相手と話すこと。', f"""
{person(250,352,1.25,1,'teal','blue','hold','short','smile')}
{phone(302,224,0.8,-12)}
<g fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round">
  <path d="M344 190q26 22 4 52"/><path d="M376 172q42 40 6 92"/>
</g>
{gl()}
""")

add('came', '遠くから歩いてきた人が、友だちの家の前に着いて手を振っているイラスト。', '「来た」。話し手のいる方へ、移動してきたことを表す過去形。', f"""
{house(460,306,1.0,'coral')}
{person(170,352,1.1,1,'teal','blue','walk','short','smile')}
{person(330,352,1.0,-1,'violet','blue','up','bob','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="14 12"><path d="M30 348q60-14 116 4"/></g>
{gl()}
""")

add('camera', 'カメラを構えた人が、手を振る相手を写そうとしているイラスト。', '「カメラ」。光を記録して、写真をとる道具。', f"""
{person(190,352,1.15,1,'teal','blue','hold','short','smile')}
<g transform="translate(298 232)">
  <rect x="-72" y="-46" width="144" height="92" rx="16" class="violet o"/>
  <circle cx="6" cy="0" r="32" fill="#fffefd" class="o"/>
  <circle cx="6" cy="0" r="19" class="blued o"/>
  <rect x="-42" y="-64" width="48" height="20" rx="6" class="violetd o"/>
  <path d="M72-26h28v20H72z" class="violetd o"/>
</g>
{person(492,352,1.05,-1,'coral','blue','up','bob','smile')}
{spark(384,146,0.9)}
{gl()}
""")

finish(__file__)
