# -*- coding: utf-8 -*-
"""第197回: plus45(p〜s)の100語。"""
from kit import *


# --- この回で使う小物 --------------------------------------------------------

def steam(x, y, n=1, s=1, cls='blue'):
    """湯気。立ちのぼる波線を n 本。"""
    d = ''.join(f'<path d="M{x+i*32*s} {y}q{-15*s} {-18*s} 0 {-36*s}t0 {-36*s}"/>' for i in range(n))
    return (f'<g fill="none" stroke="{TONES[cls][0]}" stroke-width="{5*s}" '
            f'stroke-linecap="round">{d}</g>')


def ball(x, y, r=28, cls='coral'):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" class="{cls} o"/>'
            f'<g fill="none" stroke="{INK}" stroke-width="3">'
            f'<ellipse cx="{x}" cy="{y}" rx="{r*0.42:.0f}" ry="{r}"/>'
            f'<path d="M{x-r} {y}h{2*r}"/></g>')


def garland(x, y, w=220, n=7, cls='coral'):
    """三角旗のガーランド。"""
    g = [f'<path d="M{x-w} {y}q{w} {w*0.22:.0f} {2*w} 0" fill="none" stroke="{MUTED}" stroke-width="3"/>']
    for i in range(n):
        t = (i + 0.5) / n
        bx, by = x - w + 2*w*t, y + 2*(1-t)*t*(w*0.22)
        g.append(f'<path d="M{bx-11:.0f} {by:.0f}h22l-11 26z" class="{cls} o"/>')
    return ''.join(g)


def balloon(x, y, s=1, cls='coral', string=True):
    """風船。string=False でひもを自分で引く。"""
    g = [f'<ellipse cx="0" cy="-32" rx="30" ry="36" class="{cls}p o"/>',
         f'<path d="M-8 4h16l-8 12z" class="{cls} o"/>']
    if string:
        g.append(f'<path d="M0 16q10 26 0 50" fill="none" stroke="{MUTED}" stroke-width="3"/>')
    return f'<g transform="translate({x} {y}) scale({s})">' + ''.join(g) + '</g>'


def tv(x, y, s=1, cls='teal'):
    """テレビ。画面に映像が映っている。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect x="-116" y="-84" width="232" height="164" rx="14" class="paper"/>'
            f'<rect x="-100" y="-68" width="200" height="132" class="{cls}p"/>'
            f'<path d="M-100 14q52-56 200-18v68h-200z" class="greenp"/>'
            f'<circle cx="50" cy="-36" r="20" class="gold"/>'
            f'<rect x="-116" y="-84" width="232" height="164" rx="14" fill="none" class="o"/>'
            f'<path d="M-40 84h80" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"/></g>')


def eye(x, y, s=1):
    """大きな目。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-100 0q100-74 200 0-100 70-200 0z" fill="#fffefd" class="o"/>'
            f'<circle cx="0" cy="-2" r="32" class="blue o"/>'
            f'<circle cx="0" cy="-2" r="13" class="ink"/></g>')


def screw(x, y, s=1, r=0, cls='blue'):
    """頭と軸、ねじ山のあるねじ。"""
    teeth = ''.join(f'<path d="M{8+i*18} -12l-10 24"/>' for i in range(4))
    return (f'<g transform="translate({x} {y}) scale({s}) rotate({r})">'
            f'<rect x="0" y="-12" width="84" height="24" rx="4" class="{cls}p o"/>'
            f'<g fill="none" stroke="{TONES[cls][0]}" stroke-width="3.5" stroke-linecap="round">{teeth}</g>'
            f'<path d="M0-24h-8a24 24 0 0 0 0 48h8z" class="{cls} o"/>'
            f'<path d="M-14-10l14 10-14 10" fill="none" stroke="{INK}" stroke-width="3"/></g>')


def pencil(x, y, r=0, s=1, cls='gold'):
    return (f'<g transform="translate({x} {y}) rotate({r}) scale({s})">'
            f'<rect x="-70" y="-15" width="140" height="30" rx="4" class="{cls} o"/>'
            f'<path d="M70-15l34 15-34 15z" fill="#e8d8b8" class="o"/>'
            f'<path d="M94-3l10 3-10 3z" class="ink"/>'
            f'<rect x="-80" y="-15" width="16" height="30" rx="6" class="coral o"/></g>')


def monitor(x, y, s=1, cls='teal'):
    """コードの行が並ぶモニター。"""
    rows = ''.join(f'<rect x="-68" y="{-44+i*20}" width="{148-(i%3)*34}" height="9" rx="4"/>' for i in range(5))
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect x="-92" y="-68" width="184" height="128" rx="10" class="paper"/>'
            f'<rect x="-80" y="-56" width="160" height="104" rx="6" class="{cls}p"/>'
            f'<g fill="{TONES[cls][0]}">{rows}</g>'
            f'<rect x="-92" y="-68" width="184" height="128" rx="10" fill="none" class="o"/>'
            f'<rect x="-20" y="60" width="40" height="14" class="goldd o"/>'
            f'<rect x="-54" y="74" width="108" height="12" rx="6" class="gold o"/></g>')


def gear(x, y, r=50, cls='gold', teeth=9):
    g = [f'<g transform="translate({x} {y})">']
    for i in range(teeth):
        g.append(f'<rect x="{-r*0.16:.0f}" y="{-r-8:.0f}" width="{r*0.32:.0f}" height="18" rx="5" '
                 f'class="{cls} o" transform="rotate({i*360.0/teeth:.1f})"/>')
    g.append(f'<circle r="{r}" class="{cls}p o"/><circle r="{r*0.4:.0f}" fill="#fffefd" class="o"/></g>')
    return ''.join(g)


def needle(x, y, r=0, s=1):
    """糸を通す穴のあいた針。"""
    return (f'<g transform="translate({x} {y}) rotate({r}) scale({s})">'
            f'<path d="M-90 0h146" fill="none" stroke="{STONE}" stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M56-6l38 6-38 6z" fill="{STONE}" class="o"/>'
            f'<circle cx="-90" cy="0" r="7" fill="none" stroke="{STONE}" stroke-width="5"/></g>')


def scissors(x, y, r=0, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) rotate({r}) scale({s})">'
            f'<g fill="none" stroke="{STONE}" stroke-width="9" stroke-linecap="round">'
            f'<path d="M-78-26L56 12M-78 26L56-12"/></g>'
            f'<g fill="none" stroke="{TONES[cls][0]}" stroke-width="10" stroke-linecap="round">'
            f'<circle cx="-100" cy="-42" r="22"/><circle cx="-100" cy="42" r="22"/></g>'
            f'<circle cx="0" cy="0" r="8" class="gold o"/></g>')


def car(x, y, s=1, cls='blue', facing=1):
    return (f'<g transform="translate({x} {y}) scale({s*facing} {s})">'
            f'<path d="M-96 0v-32q0-12 12-12h22l20-32h76l18 32h36q12 0 12 12v32z" class="{cls} o"/>'
            f'<path d="M-40-44l14-24h46l14 24z" class="{cls}p o"/>'
            f'<circle cx="-52" cy="0" r="24" fill="#fffdf6" class="o"/>'
            f'<circle cx="58" cy="0" r="24" fill="#fffdf6" class="o"/></g>')


def flag(x, y, s=1, cls='blue'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0v-170" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M0-170h96l-20 28 20 28H0z" class="{cls} o"/></g>')


def coinrow(x, y, n=7, gap=54, r=22):
    return ''.join(coin(x + i*gap, y, r) for i in range(n))


def dotcol(x, y, n=10, gap=17, r=7, cls='teal'):
    """縦一列の点(10のまとまり)。"""
    return (f'<g class="{cls}">'
            + ''.join(f'<circle cx="{x}" cy="{y+i*gap}" r="{r}"/>' for i in range(n)) + '</g>')


# --- p ----------------------------------------------------------------------

add('party', '飾り旗を張った部屋で、グラスを手に三人が集まっているイラスト。', '人が集まって楽しむ会、パーティー。', f"""
{garland(300, 54, 250, 9, 'coral')}
{garland(300, 54, 130, 5, 'gold')}
{person(150, 352, 1.05, 1, 'teal', 'blue', 'hold', 'bob')}
{person(300, 344, 0.9, 1, 'violet', 'blue', 'up', 'short')}
{person(450, 352, 1.05, -1, 'green', 'gold', 'hold', 'bun')}
<g transform="translate(300 330)">
  <rect x="-72" y="8" width="144" height="16" rx="6" class="gold o"/>
  <path d="M-54 24v30M54 24v30" fill="none" stroke="{GLDD}" stroke-width="10" stroke-linecap="round"/>
  <path d="M-40 8q40-46 80 0z" class="corald o"/>
  <path d="M0-4v-24" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <path d="M0-30c-10-8-6-18 4-14 4-10 16-4 12 6z" class="gold o"/>
</g>
""")

add('peeler', '皮むき器を当てたジャガイモから、長い皮の帯がカールして落ちるイラスト。', '野菜の皮をむく道具、皮むき器。', f"""
<g transform="translate(240 176)">
  <ellipse rx="66" ry="52" fill="#e8d8b8" class="o"/>
  <ellipse cx="-22" cy="-14" rx="9" ry="7" fill="{GLDD}"/>
  <ellipse cx="24" cy="12" rx="8" ry="6" fill="{GLDD}"/>
</g>
<path d="M292 196q44 22 16 56t-40 62" fill="none" stroke="{GLD}" stroke-width="13" stroke-linecap="round"/>
<g transform="translate(324 150) rotate(-16)">
  <rect x="0" y="-24" width="130" height="48" rx="14" class="teal o"/>
  <rect x="-52" y="-26" width="54" height="52" rx="10" class="gold o"/>
  <path d="M-40-8h30M-40 8h30" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
</g>
{hand(468, 132, 1)}
""")

add('pen', 'ペンの先から紙に線が引かれていくイラスト。', 'インクで書く筆記用具、ペン。', f"""
{doc(300, 250, 272, 168, 4, '#c9d3dc')}
<path d="M196 218q40-26 84 0t84 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
<g transform="translate(250 218) rotate(-24)">
  <rect x="0" y="-16" width="150" height="32" rx="8" class="violet o"/>
  <path d="M0-16l-52 16 52 16z" class="gold o"/>
  <path d="M-52 0h-12" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
</g>
{hand(430, 150, 1)}
""")

add('people', '広い場所にたくさんの人が集まり、それぞれ別の方を向いて立っているイラスト。', 'たくさんの人々。person の複数として使う。', f"""
{person(246, 296, 0.62, 1, 'gold', 'blue', 'stand', 'short')}
{person(350, 296, 0.62, -1, 'teal', 'blue', 'stand', 'bun')}
{person(90, 352, 0.85, 1, 'teal', 'blue', 'stand', 'bob')}
{person(196, 352, 0.95, 1, 'violet', 'blue', 'walk', 'short')}
{person(300, 340, 0.8, 1, 'coral', 'gold', 'hold', 'short')}
{person(396, 352, 0.95, -1, 'green', 'blue', 'walk', 'bun')}
{person(506, 352, 0.85, -1, 'blue', 'violet', 'stand', 'cap')}
""")

add('perfect', '的の真ん中に矢が突き刺さり、そばに印がつくイラスト。', '欠点がなく申し分ない、完璧な。', f"""
<g transform="translate(230 196)">
  <circle r="108" class="corald o"/>
  <circle r="82" fill="#fffdf6" class="o"/>
  <circle r="56" class="corald o"/>
  <circle r="30" fill="#fffdf6" class="o"/>
  <circle r="11" class="gold o"/>
</g>
<path d="M230 196L110 76" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<path d="M110 76l-38-14 22-22z" class="blue o"/>
<path d="M110 76l14-38 24 20z" class="blue o"/>
{tick(478, 130, 1.5)}
""")

add('person', '点線の輪で囲まれた一人の人物のイラスト。', '一人の人間、個人。people の単数。', f"""
{ring(300, 210, 152, True)}
{person(300, 352, 1.5, 1, 'teal', 'blue', 'stand', 'short')}
""")

add('phone', 'スマートフォンを耳に当てて話す人のイラスト。', '電話。動詞では電話をかける。', f"""
{person(300, 352, 1.3, 1, 'blue', 'blue', 'think', 'short', 'smile')}
<g transform="translate(348 198) rotate(-14)">
  <rect x="-32" y="-58" width="64" height="112" rx="12" class="violet o"/>
  <rect x="-24" y="-46" width="48" height="82" rx="6" class="violetp"/>
  <circle cx="0" cy="48" r="5" class="ink"/>
</g>
""")

add('photo', 'カメラのレンズの横に、写した写真が出ているイラスト。', 'カメラで写した写真。', f"""
{spark(104, 150, 1.1)}
<g transform="translate(230 200)">
  <rect x="-116" y="-72" width="232" height="144" rx="16" class="violet o"/>
  <circle cx="6" cy="0" r="52" fill="#fffdf6" class="o"/>
  <circle cx="6" cy="0" r="30" class="blue o"/>
  <circle cx="6" cy="0" r="13" class="bluep o"/>
  <rect x="-100" y="-62" width="34" height="16" rx="6" class="gold o"/>
  <rect x="44" y="-82" width="46" height="20" rx="6" class="gold o"/>
</g>
<g transform="translate(462 250) rotate(-8)">
  <rect x="-96" y="-72" width="192" height="160" rx="6" class="paper"/>
  <rect x="-80" y="-56" width="160" height="104" class="bluep"/>
  <path d="M-80 34q46-58 100-32 28 14 60 4v26h-160z" class="greenp"/>
  <circle cx="34" cy="-28" r="18" class="gold"/>
</g>
""")

add('picnic', 'シートの上にバスケットと果物を広げ、女の子が座っているイラスト。', '戸外で食事を楽しむこと、ピクニック。', f"""
<g transform="translate(310 352)">
  <path d="M-160 0h320l-26-56h-268z" class="green o"/>
  <path d="M-134-56h268v12h-268z" class="greenp o"/>
</g>
<g transform="translate(430 300)">
  <path d="M-70-50h140v46H-20l-18 26h-72z" class="gold o"/>
  <path d="M-40-50q40-42 80 0" fill="none" stroke="{GLDD}" stroke-width="8"/>
</g>
<circle cx="360" cy="284" r="20" class="coral o"/>
<circle cx="404" cy="292" r="16" class="corald o"/>
{sit(210, 352, 1.05, 1, 'coral', 'blue', 'bob', 'smile', 'down')}
{hand(300, 250, 1)}
""")

add('piece', '丸いケーキに切り込みが入り、切り分けた一切れが皿に置かれているイラスト。', '全体から切り分けた 1 片、部分。', f"""
<g transform="translate(190 230)">
  <circle r="110" class="goldp o"/>
  <circle r="92" fill="#f7e3c4"/>
  <path d="M0 0v-110M0 0l78-78" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <g class="corald o"><circle cx="-46" cy="-30" r="15"/><circle cx="30" cy="-56" r="13"/><circle cx="-14" cy="34" r="14"/></g>
</g>
<g transform="translate(470 300)">
  <ellipse rx="98" ry="24" class="paper"/>
  <g transform="translate(0 -4) rotate(-16)">
    <path d="M0 0L-104-40A110 110 0 0 0 -104 40Z" class="goldp o"/>
    <circle cx="-56" cy="-24" r="13" class="corald o"/>
    <circle cx="-64" cy="14" r="11" class="corald o"/>
  </g>
</g>
""")

add('pig', '丸い体の豚が鼻先を下に向けて立っているイラスト。', '家畜として飼われる動物、豚。', f"""
<g transform="translate(310 296)">
  <path d="M-112-44l-14 74M-40-8l-8 70M62-8l8 70M120-44l14 74" fill="none"
        stroke="{CRLD}" stroke-width="18" stroke-linecap="round"/>
  <ellipse cx="0" cy="-62" rx="132" ry="84" class="coral o"/>
  <path d="M138-72c32-16 36 24 6 22" fill="none" stroke="{CRLD}" stroke-width="9" stroke-linecap="round"/>
  <circle cx="-116" cy="-80" r="52" class="coral o"/>
  <path d="M-148-120l-16-40 42 26z" class="coral o"/>
  <circle cx="-106" cy="-98" r="6" class="ink"/>
  <ellipse cx="-150" cy="-68" rx="24" ry="18" class="corald o"/>
  <circle cx="-156" cy="-72" r="5" fill="{SKINL}"/><circle cx="-156" cy="-58" r="5" fill="{SKINL}"/>
</g>
""")

add('pink', 'うすい桃色の風船を三つ持って立つ人のイラスト。', 'ピンク色。うすい赤むらさきの色。', f"""
{balloon(200, 136, 1, 'coral', False)}
{balloon(300, 106, 1.15, 'coral', False)}
{balloon(400, 136, 1, 'coral', False)}
<g fill="none" stroke="{MUTED}" stroke-width="3">
  <path d="M200 158v40l96 34M300 144v88M400 158v40l-96 34"/>
</g>
{person(300, 352, 1.1, 1, 'coral', 'blue', 'up', 'bob')}
""")

add('pizza', '丸いピザに切り込みが入り、一切れが皿にのっているイラスト。', '薄い生地に具をのせて焼いた料理、ピザ。', f"""
<g transform="translate(190 240)">
  <circle r="112" class="goldp o"/>
  <circle r="92" fill="#f6dfae"/>
  <g class="coral o"><circle cx="-48" cy="-28" r="16"/><circle cx="36" cy="-52" r="14"/>
    <circle cx="-16" cy="32" r="15"/><circle cx="58" cy="20" r="13"/><circle cx="4" cy="-6" r="14"/></g>
  <path d="M0 0v-112M0 0l98-52" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
</g>
<g transform="translate(452 292) rotate(18)">
  <path d="M0 0L0-112A112 112 0 0 1 105-38Z" class="goldp o"/>
  <path d="M0-112A112 112 0 0 1 105-38" fill="none" stroke="{GLD}" stroke-width="16"/>
  <circle cx="44" cy="-62" r="14" class="coral o"/>
</g>
<g transform="translate(452 320)"><ellipse rx="96" ry="22" class="paper"/></g>
""")

add('plan', '紙の上に三つの囲みが矢印でつながり、それぞれに印がつくイラスト。', '前もって決めておく段取り、計画。', f"""
<rect x="118" y="128" width="364" height="150" rx="10" class="paper"/>
<g class="bluep o">
  <rect x="146" y="166" width="76" height="52" rx="8"/>
  <rect x="262" y="166" width="76" height="52" rx="8"/>
  <rect x="378" y="166" width="76" height="52" rx="8"/>
</g>
{tick(184, 192, 0.5)}{tick(300, 192, 0.5)}{tick(416, 192, 0.5)}
{line(228, 192, 256, 192, INK, False, 4)}
{line(344, 192, 372, 192, INK, False, 4)}
{table(280)}
""", arrow=True)

add('plane', '雲の間を飛んでいく飛行機と、点線の航跡のイラスト。', '空を飛ぶ乗り物、飛行機。', f"""
{cloud(120, 96, 1.1)}
{cloud(508, 148, 0.85)}
{arrowline([(50, 316),(180, 296),(280, 276)], MUTED, 5, True)}
{plane(360, 210, 0.8, -12)}
""", arrow=True)

add('play', '芝生の上で子どもがボールを蹴って遊ぶイラスト。', '楽しんで体を動かす、遊ぶ。', f"""
{tree(78, 306, 0.9)}
{person(210, 352, 1.1, 1, 'gold', 'blue', 'walk', 'short')}
{arc(262, 322, 372, 250, 46, MUTED, True)}
{ball(404, 236, 28, 'coral')}
""", arrow=True)

add('player', 'ユニフォームを着た選手がボールを両手で持っているイラスト。', '競技をする人、選手。', f"""
{person(300, 352, 1.35, 1, 'coral', 'blue', 'hold', 'short')}
<circle cx="316" cy="292" r="40" class="gold o"/>
<g fill="none" stroke="{INK}" stroke-width="3">
  <ellipse cx="316" cy="292" rx="17" ry="40"/><path d="M276 292h80"/>
</g>
""")

add('police', '制帽と制服姿の警察官が立っているイラスト。', '社会の安全を守る警察官、警察。', f"""
{person(300, 352, 1.35, 1, 'blue', 'blue', 'stand', 'cap', 'neutral')}
<path d="M-12-12l4 8 9 1-6 6 2 9-9-5-9 5 2-9-6-6 9-1z" class="gold o" transform="translate(272 292) scale(1.5)"/>
""")

add('police station', '警察官が前に立つ警察署の建物のイラスト。', '警察官が勤める建物、警察署。', f"""
{building(380, 352, 1.3, 'blue')}
<circle cx="418" cy="228" r="22" class="goldp o"/>
{person(150, 352, 1.15, 1, 'blue', 'blue', 'stand', 'cap', 'neutral')}
{flag(96, 306, 0.9, 'blue')}
""")

add('pool', '仕切りのロープが張られたプールの水面のイラスト。', '泳ぐために水を張った施設、プール。', f"""
<g transform="translate(300 340)">
  <rect x="-260" y="-120" width="520" height="180" rx="12" class="bluep o"/>
  <g fill="none" stroke="#fffdf6" stroke-width="5" stroke-dasharray="18 12">
    <path d="M-260-88h520M-260-40h520"/>
  </g>
  <g fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round">
    <path d="M-220-104q26-14 52 0t52 0t52 0"/>
    <path d="M-160-56q26-14 52 0t52 0t52 0"/>
  </g>
</g>
<path d="M60 306v-40M540 306v-40" fill="none" stroke="{TEA}" stroke-width="10" stroke-linecap="round"/>
""")

add('poor', '逆さにした財布から小銭が一枚だけ落ちるイラスト。', 'お金が足りない、貧しい。', f"""
{hand(180, 180, 1)}
<g transform="translate(250 190) rotate(148)">
  <rect x="-62" y="-46" width="124" height="92" rx="18" class="corald o"/>
  <path d="M-62-46h124l-14-24h-96z" class="coral o"/>
  <circle cx="0" cy="4" r="10" class="goldp o"/>
</g>
<path d="M300 268v46" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9" stroke-linecap="round"/>
{coin(300, 338, 26)}
""")

add('popular', '大勢の人から手を差し出されて囲まれた人のイラスト。', '多くの人に好かれている、人気がある。', f"""
{spark(300, 128, 1.2)}
{hand(112, 214, 1)}{hand(188, 158, 1)}{hand(430, 168, -1)}{hand(508, 224, -1)}
{person(300, 352, 1.3, 1, 'coral', 'blue', 'up', 'bob')}
""")

add('possible', '塀の切れ目に開いた門を人が通り抜けていくイラスト。', 'できる、ありうる、可能な。', f"""
<g fill="none" stroke="{BRN}" stroke-width="10" stroke-linecap="round">
  <path d="M70 306V166h176M354 166h176v140"/>
  <path d="M96 208h132M372 208h132"/>
</g>
<path d="M248 306L228 172" fill="none" stroke="{BRN}" stroke-width="12" stroke-linecap="round"/>
<path d="M352 306l20-134" fill="none" stroke="{BRN}" stroke-width="12" stroke-linecap="round"/>
{person(300, 352, 1.2, 1, 'teal', 'blue', 'walk', 'short')}
{tick(492, 120, 1.2)}
""")

add('post', '赤いポストの差し入れ口に封筒を入れようとする手のイラスト。', '郵便、郵便物。動詞では投函する。', f"""
<g transform="translate(340 300)">
  <rect x="-84" y="-190" width="168" height="190" rx="26" class="corald o"/>
  <rect x="-84" y="-190" width="168" height="46" rx="22" class="coral o"/>
  <rect x="-58" y="-118" width="116" height="20" rx="6" class="ink"/>
  <rect x="-58" y="-68" width="116" height="14" rx="6" fill="{MUTED}"/>
</g>
<g transform="translate(170 196) rotate(14)">
  <rect x="-76" y="-48" width="152" height="96" rx="4" class="paper"/>
  <path d="M-76-48l76 56 76-56" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
{hand(126, 200, 1)}
{arrowline([(216, 214),(262, 196)], MUTED, 5, True)}
""", arrow=True)

add('potato', '土の中にジャガイモがいくつも育ち、掘り出された芋がそばにあるイラスト。', '土の中で育ついも、ジャガイモ。', f"""
<rect x="60" y="216" width="480" height="90" fill="#e2d3b4" stroke="{INK}" stroke-width="2.5"/>
<g fill="#d9b877" class="o">
  <ellipse cx="150" cy="258" rx="40" ry="28" transform="rotate(-12 150 258)"/>
  <ellipse cx="240" cy="240" rx="30" ry="24"/>
  <ellipse cx="300" cy="278" rx="34" ry="24" transform="rotate(14 300 278)"/>
  <ellipse cx="378" cy="248" rx="38" ry="26"/>
  <ellipse cx="452" cy="272" rx="30" ry="22"/>
</g>
<g fill="none" stroke="{GRND}" stroke-width="5" stroke-linecap="round">
  <path d="M120 306v-24q0-10-12-14M480 306v-22q0-10 12-14"/>
</g>
<g transform="translate(500 170) rotate(-18)">
  <ellipse rx="52" ry="40" fill="#d9b877" class="o"/>
  <path d="M-20-24l12 30M16-28l-4 32M-4 8l18-22" fill="none" stroke="{GLDD}" stroke-width="4"/>
</g>
{arrowline([(410, 208),(468, 202)], MUTED, 5, True)}
""", arrow=True)

add('power strip', '電源タップに三つのプラグが差され、コードが伸びているイラスト。', 'コンセントを増やす延長用の電源タップ。', f"""
<g transform="translate(300 300) rotate(-4)">
  <rect x="-196" y="-58" width="392" height="116" rx="18" class="green o"/>
  <g class="greenp o">{''.join(f'<rect x="{-158+c*80}" y="-32" width="56" height="64" rx="12"/>' for c in range(5))}</g>
  <g fill="{INK}">{''.join(f'<circle cx="{-130+c*80}" cy="-14" r="6"/><circle cx="{-130+c*80}" cy="14" r="6"/>' for c in range(5))}</g>
</g>
<g class="gold o"><rect x="130" y="186" width="52" height="56" rx="8"/>
  <rect x="290" y="186" width="52" height="56" rx="8"/><rect x="450" y="186" width="52" height="56" rx="8"/></g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="3">
  <circle cx="146" cy="242" r="6"/><circle cx="166" cy="242" r="6"/>
  <circle cx="306" cy="242" r="6"/><circle cx="326" cy="242" r="6"/>
  <circle cx="466" cy="242" r="6"/><circle cx="486" cy="242" r="6"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round">
  <path d="M156 186q-24-52 12-84M316 186q-4-56 34-86M476 186q22-50 46-72"/>
</g>
""")

add('practice', '同じ形を書き写した行が三つ並び、周りを循環矢印が回るイラスト。', '上達のために同じことを繰り返すこと、練習。', f"""
<rect x="128" y="112" width="264" height="250" rx="10" class="paper"/>
{word(260, 170, 4, 42, 'teal')}
{word(260, 235, 4, 42, 'teal')}
{word(260, 300, 4, 42, 'teal')}
<path d="M424 126a112 112 0 1 1 0 220" fill="none" stroke="{GLD}" stroke-width="7"
      stroke-linecap="round" marker-end="url(#ar)"/>
""", arrow=True)

add('practise', 'いすに座ってギターを繰り返し弾く練習をするイラスト。', '実際に体を動かして練習する(英つづり)。', f"""
{chair(250, 352, 1.1, 'gold', 1)}
{sit(250, 352, 1.1, 1, 'teal', 'blue', 'short', 'smile', 'lap')}
<g transform="translate(348 300) rotate(-20)">
  <ellipse rx="54" ry="42" class="coral o"/>
  <circle cx="0" cy="0" r="15" fill="#fffdf6" class="o"/>
  <path d="M0-40L-96-124" fill="none" stroke="{BRN}" stroke-width="16" stroke-linecap="round"/>
  <path d="M-90-130l-22-22 22-8z" class="gold o"/>
</g>
""")

add('prepare', 'スーツケースに服を詰め、そばの手がもう一枚を入れようとしているイラスト。', '前もって用意すること、準備する。', f"""
<g transform="translate(280 350)">
  <path d="M-150-124h300v124h-300z" class="violet o"/>
  <path d="M-150-124l-26-44h352l-26 44z" class="violetd o"/>
  <path d="M-96-124h64v34h-64z" class="coral o"/>
  <path d="M-14-124h58v38h-58z" class="teal o"/>
  <path d="M-64-8v8M64-8v8" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>
</g>
<g transform="translate(410 170) rotate(-14)"><path d="M-46-30h92v60h-92z" class="coral o"/></g>
{hand(462, 172, -1)}
{arrowline([(410, 220),(352, 258)], MUTED, 5, True)}
""", arrow=True)

add('pressure cooker', 'ふたを留めた圧力鍋から蒸気が勢いよく立ちのぼるイラスト。', '圧力をかけて短時間で調理する鍋。', f"""
<g transform="translate(300 300)">
  <path d="M-142 0h284l-12-104h-260z" class="blue o"/>
  <rect x="-156" y="-146" width="312" height="42" rx="16" class="bluep o"/>
  <path d="M-186-124h30M156-124h30" fill="none" stroke="{INK}" stroke-width="16" stroke-linecap="round"/>
  <path d="M0-146v-30" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>
  <circle cx="0" cy="-190" r="18" class="gold o"/>
</g>
{steam(258, 74, 2, 1, 'blue')}
{steam(314, 66, 2, 1, 'blue')}
""")

add('pretty', '花を髪に飾って微笑む女の子のイラスト。', '見た目がかわいい、きれいな。', f"""
{spark(432, 190, 1.1)}{spark(172, 176, 1.1)}
{person(300, 352, 1.35, 1, 'violet', 'blue', 'hold', 'bob')}
{flower(254, 212, 0.62, 'coral')}
{flower(384, 300, 0.5, 'gold')}
""")

add('probably', '曇り空の下、かさを持って出かける人のイラスト。', 'たぶん、おそらく(起こりそう)。', f"""
{cloud(140, 96, 1.15, 'blue')}
{cloud(340, 74, 0.85, 'blue')}
{person(250, 352, 1.25, 1, 'gold', 'blue', 'carry', 'short', 'neutral')}
<g transform="translate(420 220)">
  <path d="M-116 0q116-124 232 0z" class="coral o"/>
  <path d="M0-108v96q0 24-24 24" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
</g>
{arrowline([(470, 300),(534, 300)], MUTED, 5, True)}
""", arrow=True)

add('problem', 'かみ合わない歯車を、困った顔で二人が見ているイラスト。', '困った事柄、解決すべき問題。', f"""
<g transform="translate(210 200)">{gear(0, 0, 76, 'blue', 10)}</g>
<g transform="translate(392 232)">{gear(0, 0, 56, 'gold', 8)}</g>
{cross(304, 216, 0.7)}
{person(200, 352, 1.2, 1, 'teal', 'blue', 'think', 'short', 'sad')}
{person(430, 352, 1.2, -1, 'violet', 'blue', 'think', 'short', 'neutral')}
""")

add('programme', 'テレビ画面に映像が映り、番組が流れているイラスト。', 'テレビやラジオの番組。', f"""
{tv(300, 210, 1.05)}
<g transform="translate(120 120)">{spark(0, 0, 1.1)}{spark(60, -30, 0.8)}</g>
""")

add('programmer', '机の上の二台のモニターに向かってコードを書く人のイラスト。', 'プログラムを書く人、プログラマー。', f"""
<g transform="translate(150 300)"><rect x="-130" y="0" width="430" height="16" rx="6" class="goldd o"/>
  <path d="M-104 16v34M196 16v34" fill="none" stroke="{GLDD}" stroke-width="12" stroke-linecap="round"/></g>
{monitor(300, 216, 0.72, 'teal')}
{monitor(470, 232, 0.62, 'violet')}
{sit(120, 356, 1.05, 1, 'teal', 'blue', 'short', 'neutral', 'lap')}
<path d="M186 268h60" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
""")

add('purple', '紫色のぶどうの房と葉のイラスト。', '赤と青の中間の色、紫。', f"""
<g transform="translate(300 210)">
  <path d="M0-146q56-30 96-6" fill="none" stroke="{GRND}" stroke-width="9" stroke-linecap="round"/>
  <path d="M62-138q44-12 46-48 28 26 8 58-24 36-58 12z" class="green o"/>
  <g class="violet o">
    <circle cx="-40" cy="-64" r="27"/><circle cx="0" cy="-72" r="27"/><circle cx="40" cy="-62" r="27"/>
    <circle cx="-60" cy="-20" r="27"/><circle cx="-20" cy="-24" r="27"/><circle cx="20" cy="-22" r="27"/><circle cx="60" cy="-18" r="27"/>
    <circle cx="-42" cy="22" r="27"/><circle cx="-2" cy="20" r="27"/><circle cx="38" cy="24" r="27"/>
    <circle cx="-22" cy="68" r="27"/><circle cx="18" cy="70" r="27"/>
    <circle cx="-2" cy="114" r="25"/>
  </g>
</g>
""")

add('pushchair', '赤ちゃんを乗せたベビーカーを親が押して歩くイラスト。', '赤ちゃんを乗せて押す車、ベビーカー(英)。', f"""
<g transform="translate(250 306)">
  <path d="M-104-96h96q62 0 88 62l16 34h-200z" class="teal o"/>
  <path d="M-116-108q76-42 140 8" fill="none" stroke="{TEAD}" stroke-width="12" stroke-linecap="round"/>
  <circle cx="-4" cy="-44" r="28" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <circle cx="-14" cy="-50" r="3" class="ink"/><circle cx="8" cy="-50" r="3" class="ink"/>
  <path d="M-74-84l-8-24M52-84l8-24" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle cx="-72" cy="-4" r="26" fill="#fffdf6" class="o"/>
  <circle cx="66" cy="-4" r="26" fill="#fffdf6" class="o"/>
  <path d="M90-70l64-10" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>
</g>
{person(500, 352, 1.15, -1, 'violet', 'blue', 'reach', 'bob')}
""")

add('put', '手に持ったりんごを箱の中へ入れるイラスト。', '手で持って中に入れる、置く。', f"""
{box(320, 350, 240, 92, 30, 'gold')}
<g transform="translate(240 172)">
  <circle r="46" class="coral o"/>
  <path d="M0-46v-14" fill="none" stroke="{BRN}" stroke-width="6" stroke-linecap="round"/>
  <path d="M2-58q22-16 30 4-20 10-30-4z" class="green o"/>
</g>
{hand(120, 150, 1)}
{arrowline([(250, 232),(300, 268),(292, 300)], MUTED, 5, True)}
""", arrow=True)

add('pyjamas', 'ベッドの上に上下そろえたパジャマが置かれているイラスト。', '寝るときに着る服、パジャマ(英)。', f"""
<g transform="translate(300 344)">
  <rect x="-260" y="-96" width="520" height="96" rx="12" class="bluep o"/>
  <rect x="-258" y="-150" width="36" height="150" class="blue o"/>
  <rect x="-200" y="-136" width="118" height="42" rx="12" class="paper"/>
</g>
<g transform="translate(300 236)">
  <path d="M-96-58l-72 40 24 46 48-24v96h192v-72l-48 24-48-70z" class="paper"/>
  <path d="M-44-58l44 42 44-42-26-14h-36z" class="violetp o"/>

  <g fill="{VIOP}">{''.join(f'<rect x="{-62+c*44}" y="{-14+r*26}" width="30" height="14" rx="7"/>' for r in range(3) for c in range(3))}</g>
</g>
""")

add('quick', '速度の線を引いて速く走る人のイラスト。', '動きが速い、素早い。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round">
  <path d="M70 226h116M46 272h96M84 318h86"/>
</g>
{person(330, 352, 1.3, 1, 'gold', 'blue', 'walk', 'short')}
{spark(470, 160, 1.1)}
""")

add('quickly', '時計を確かめながら急いで走る人のイラスト。', '素早く、すぐに(副詞)。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round">
  <path d="M60 246h100M74 292h88"/>
</g>
{person(250, 352, 1.2, 1, 'coral', 'blue', 'walk', 'bob', 'surprised')}
{clock(470, 140, 56, 10, 2)}
""")

add('quite', '思ったより大きな箱を両手で持ち上げる人のイラスト。', 'かなり、思った以上に(程度を示す)。', f"""
{person(300, 352, 1.25, 1, 'violet', 'blue', 'up', 'short', 'surprised')}
<g transform="translate(300 126)">
  <rect x="-112" y="-62" width="224" height="124" rx="6" class="gold o"/>
  <path d="M-112-62h224l-30-32h-164z" class="goldp o"/>
  <path d="M0-62v124" fill="none" stroke="{GLDD}" stroke-width="5"/>
</g>
{spark(120, 150, 1.1)}{spark(480, 158, 1.1)}
""")

add('quiz', '四つの選択肢が並ぶ解答用紙に印をつけるイラスト。', '知識を問う小テスト、クイズ。', f"""
<rect x="150" y="112" width="300" height="240" rx="8" class="paper"/>
<g fill="{MUTED}"><rect x="180" y="150" width="130" height="12" rx="6"/><rect x="180" y="182" width="90" height="12" rx="6"/></g>
<g class="bluep o">{''.join(f'<rect x="{178+i*52}" y="222" width="36" height="36" rx="8"/>' for i in range(4))}</g>
{tick(248, 240, 0.5)}
<g fill="{MUTED}"><rect x="180" y="300" width="180" height="12" rx="6"/><rect x="180" y="326" width="120" height="12" rx="6"/></g>
{pencil(452, 176, -28, 1, 'gold')}
{hand(520, 140, -1)}
""")

add('radio', 'アンテナを伸ばしたラジオから音の波が広がるイラスト。', '音声を電波で受信する機器、ラジオ。', f"""
<g transform="translate(260 300)">
  <rect x="-146" y="-140" width="292" height="140" rx="16" class="coral o"/>
  <circle cx="-92" cy="-70" r="36" class="coralp o"/>
  <path d="M-92-96v52" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <g class="coralp o">{''.join(f'<rect x="{-36+c*32}" y="{-110+r*42}" width="24" height="34" rx="7"/>' for r in range(3) for c in range(3))}</g>
  <path d="M104-140l58-96" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{GLD}" stroke-width="6" stroke-linecap="round">
  <path d="M362 62a58 58 0 0 1 0 70"/>
  <path d="M384 42a88 88 0 0 1 0 110"/>
  <path d="M406 22a118 118 0 0 1 0 150"/>
</g>
""")

add('rain', '雲から雨粒が降り、足もとに水たまりができているイラスト。', '空から降ってくる水、雨。', f"""
{cloud(170, 96, 1.2, 'blue')}
{cloud(430, 128, 1.0, 'blue')}
<g class="blue">{drop(150, 200, 1.2)}{drop(230, 172, 1.1)}{drop(320, 196, 1.2)}{drop(410, 168, 1.1)}{drop(490, 202, 1.2)}</g>
<g class="blue">{drop(190, 262, 1.0)}{drop(280, 250, 0.9)}{drop(370, 268, 1.0)}{drop(452, 246, 0.9)}</g>
<ellipse cx="300" cy="360" rx="200" ry="26" class="bluep o"/>
<g fill="none" stroke="{BLU}" stroke-width="4" stroke-linecap="round">
  <path d="M140 348q26-14 52 0M400 350q26-14 52 0"/>
</g>
""")

add('rainbow', '空にかかる六色の虹と、足もとの雲のイラスト。', '雨上がりに見える七色の弧、虹。', f"""
<g fill="none" stroke-width="20" stroke-linecap="butt">
  <path d="M54 306a246 246 0 0 1 492 0" stroke="{CRLD}"/>
  <path d="M76 306a224 224 0 0 1 448 0" stroke="{GLD}"/>
  <path d="M98 306a202 202 0 0 1 404 0" stroke="{GRN}"/>
  <path d="M120 306a180 180 0 0 1 360 0" stroke="{TEA}"/>
  <path d="M142 306a158 158 0 0 1 316 0" stroke="{BLU}"/>
  <path d="M164 306a136 136 0 0 1 272 0" stroke="{VIO}"/>
</g>
{cloud(84, 302, 0.8)}
{cloud(516, 302, 0.8)}
""")

add('raincoat', '黄色いレインコートを着て雨の中を歩くイラスト。', '雨を防ぐために着る上着、レインコート。', f"""
{cloud(120, 84, 1.05, 'blue')}
<g class="blue">{drop(190, 160, 1.1)}{drop(410, 150, 1.0)}{drop(486, 200, 1.1)}{drop(120, 216, 1.0)}</g>
{person(300, 352, 1.3, 1, 'gold', 'gold', 'walk', 'short')}
<g transform="translate(300 352) scale(1.3)">
  <path d="M-50-104q50-26 100 0l8 130h-116z" class="gold o"/>
  <path d="M0-104v130" fill="none" stroke="{GLDD}" stroke-width="4"/>
  <path d="M-42-140q42-34 84 0-18-12-42-12t-42 12z" class="goldd o"/>
</g>
""")

add('read', 'いすに座って開いた本を読む人のイラスト。', '文字を目で追って内容を理解する、読む。', f"""
{chair(300, 352, 1.15, 'gold', 1)}
{sit(300, 352, 1.15, 1, 'teal', 'blue', 'short', 'smile', 'lap')}
{book(300, 296, 0.55, 'coral')}
""")

add('ready', '荷物を背負って出発線に立ち、印がつくイラスト。', '支度がすんでいつでも始められる、用意ができた。', f"""
<g transform="translate(300 366)"><path d="M-240 0h480" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="14 12"/></g>
<g transform="translate(222 262) rotate(-6)">
  <rect x="-56" y="-62" width="112" height="124" rx="20" class="violet o"/>
  <path d="M-30-62q30-24 60 0" fill="none" stroke="{VIOD}" stroke-width="9"/>
</g>
{person(310, 352, 1.25, 1, 'green', 'blue', 'carry', 'short')}
{tick(470, 160, 1.5)}
""")

add('real', '木になっている本物の実に手を伸ばして確かめるイラスト。', 'にせものではない、本当の・実際の。', f"""
{tree(170, 306, 1.4)}
<g class="coral o"><circle cx="138" cy="198" r="24"/><circle cx="206" cy="176" r="22"/><circle cx="170" cy="240" r="20"/><circle cx="226" cy="220" r="20"/></g>
{person(310, 352, 1.3, -1, 'teal', 'blue', 'reach', 'short')}
{spark(330, 200, 1.1)}
""")

add('really', '驚いて両手を上げ、目を丸くした人のイラスト。', '本当に、実に(気持ちを強める)。', f"""
{spark(110, 132, 1.4)}{spark(488, 122, 1.4)}{spark(158, 250, 1.1)}{spark(440, 244, 1.1)}
{person(300, 352, 1.45, 1, 'coral', 'blue', 'up', 'bob', 'surprised')}
""")

add('reason', '赤信号の前で車が止まり、信号から車へ矢印が伸びるイラスト。', '物事がそうなるわけ、理由・原因。', f"""
<g transform="translate(130 200)">
  <path d="M0 140V0" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>
  <rect x="-40" y="-128" width="80" height="146" rx="18" class="paper"/>
  <circle cx="0" cy="-102" r="22" class="coral o"/>
  <circle cx="0" cy="-56" r="22" class="goldp o"/>
  <circle cx="0" cy="-10" r="22" class="greenp o"/>
</g>
{arrowline([(210, 150),(360, 250)], MUTED, 5, True)}
<g transform="translate(452 312)">{car(0, 0, 1.0, 'blue', -1)}</g>
""", arrow=True)

add('rechargeable', '電池にプラグをつないで充電するイラスト。', '充電して何度も使える、充電できる。', f"""
<g transform="translate(196 220)">
  <rect x="-48" y="-104" width="96" height="196" rx="14" class="green o"/>
  <rect x="-30" y="-88" width="60" height="42" rx="6" class="greenp"/>
  <path d="M0-104v-20" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>
</g>
{bolt(196, 240, 1.4)}
<g transform="translate(430 190) rotate(-28)">
  <rect x="-42" y="-36" width="84" height="72" rx="12" class="gold o"/>
  <path d="M-42-14h-32M-42 14h-32" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>
</g>
<path d="M420 216q-80-46-170-16" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
""")

add('red', '赤いりんごが三つ、かごに入っているイラスト。', 'りんごや血のような色、赤。', f"""
<g transform="translate(240 200)">
  <circle r="58" class="coral o"/>
  <path d="M0-58v-16" fill="none" stroke="{BRN}" stroke-width="7" stroke-linecap="round"/>
  <path d="M4-72q24-16 32 4-22 10-32-4z" class="green o"/>
</g>
<g transform="translate(346 232)"><circle r="52" class="coral o"/>
  <path d="M0-52v-14" fill="none" stroke="{BRN}" stroke-width="7" stroke-linecap="round"/>
  <path d="M4-64q22-14 30 4-20 10-30-4z" class="green o"/></g>
<g transform="translate(292 286)"><circle r="50" class="coral o"/></g>
<g transform="translate(300 340)">
  <path d="M-170 0h340l-32 66h-276z" class="gold o"/>
  <path d="M-170 0h340v-14h-340z" class="goldp o"/>
</g>
""")

add('remember', '古い写真を見て、頭の上に思い出の輪が浮かぶイラスト。', '心に浮かべる、思い出す。', f"""
<g transform="translate(280 180)">
  <circle r="46" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 10"/>
</g>
<g transform="translate(360 108)">
  <circle r="28" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 10"/>
</g>
{spark(300, 130, 1.1)}
{chair(230, 352, 1.1, 'gold', 1)}
{sit(230, 352, 1.1, 1, 'violet', 'blue', 'bob', 'smile', 'lap')}
<g transform="translate(330 268) rotate(-8)">
  <rect x="-54" y="-42" width="108" height="84" rx="4" class="paper"/>
  <rect x="-44" y="-32" width="88" height="52" class="bluep"/>
  <circle cx="4" cy="-8" r="14" class="gold"/>
</g>
""")

add('remote control', 'リモコンをテレビに向けてボタンを押すイラスト。', 'テレビなどを遠くから操作する道具、リモコン。', f"""
{tv(380, 206, 0.9)}
<g transform="translate(150 210) rotate(12)">
  <rect x="-42" y="-100" width="84" height="200" rx="18" class="violet o"/>
  <circle cx="0" cy="-64" r="15" class="corald o"/>
  <g class="violetp o">{''.join(f'<rect x="{-28+c*30}" y="{-26+r*36}" width="22" height="26" rx="6"/>' for r in range(4) for c in range(2))}</g>
</g>
{hand(96, 320, 1)}
<g fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round">
  <path d="M232 142q34-8 46-40M250 108q40-10 54-48"/>
</g>
""")

add('restaurant', '給仕が皿を運び、客がテーブルに着いているイラスト。', '食事を出す店、レストラン。', f"""
{table(330)}
<g transform="translate(300 316)">
  <ellipse rx="126" ry="26" class="paper"/>
  <ellipse rx="72" ry="14" class="goldp"/>
  <path d="M-96-14q26-16 44 0" fill="none" stroke="{MUTED}" stroke-width="5"/>
</g>
{person(510, 352, 1.1, -1, 'teal', 'blue', 'carry', 'short')}
<g transform="translate(454 296)">
  <ellipse rx="58" ry="16" class="paper"/>
  <path d="M-32-14q32-28 64 0z" class="goldp o"/>
</g>
{chair(130, 352, 1.0, 'coral', 1)}
{sit(130, 352, 1.0, 1, 'violet', 'blue', 'bob', 'smile', 'lap')}
""")

add('return', '棚に本を差し戻す手と、逆向きの矢印のイラスト。', '元の場所へ戻す、返す。', f"""
<g transform="translate(300 200)">
  <rect x="-230" y="-70" width="460" height="18" class="goldd o"/>
  <rect x="-230" y="90" width="460" height="18" class="goldd o"/>
  <g class="teal o"><rect x="-200" y="-116" width="30" height="46"/><rect x="-160" y="-126" width="26" height="56"/>
    <rect x="-124" y="-110" width="28" height="40"/><rect x="-86" y="-124" width="26" height="54"/></g>
  <g class="blue o"><rect x="-200" y="42" width="26" height="48"/><rect x="-164" y="34" width="30" height="56"/>
    <rect x="-124" y="48" width="26" height="42"/></g>
</g>
<g transform="translate(408 74) rotate(-12)"><rect x="-30" y="-22" width="60" height="44" rx="4" class="coral o"/></g>
{hand(470, 74, -1)}
{arrowline([(430, 320),(300, 348),(196, 300),(210, 240)], MUTED, 5, True)}
""", arrow=True)

add('rice', '茶碗に盛った白いご飯と、そばに稲の穂があるイラスト。', '炊いたご飯、米。', f"""
<g transform="translate(230 306)">
  <path d="M-116-64h232q-16 74-116 74T-116-64z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M-88-66q88-72 176 0-88-26-176 0z" fill="#fffefd" stroke="{INK}" stroke-width="3"/>
  <path d="M-116-64h232" fill="none" stroke="{INK}" stroke-width="4"/>
  <g fill="none" stroke="{GLDD}" stroke-width="3">
    <path d="M-58-60q10-24 26-30M0-62q0-28 12-34M58-58q-8-24-22-30"/>
  </g>
</g>
<g transform="translate(470 300)">
  <path d="M0 0q-24-84 4-160" fill="none" stroke="{GRND}" stroke-width="7" stroke-linecap="round"/>
  <g class="gold o">{''.join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="15" transform="rotate({r} {x} {y})"/>'
                             for x, y, r in [(-14,-40,30),(-24,-76,26),(-30,-112,22),(-14,-14,34),(2,-58,-20),(6,-96,-24)])}</g>
</g>
""")

add('rice cooker', 'ふたを開けた炊飯器から湯気が立ちのぼるイラスト。', 'ご飯を炊く電気器具、炊飯器。', f"""
<g transform="translate(300 300)">
  <path d="M-142 0h284V-96a26 26 0 0 0-26-26h-232a26 26 0 0 0-26 26z" class="blue o"/>
  <rect x="-166" y="-146" width="200" height="30" rx="14" class="bluep o"/>
  <path d="M-166-120h200" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-186-126h30M166-126h30" fill="none" stroke="{INK}" stroke-width="16" stroke-linecap="round"/>
  <rect x="52" y="-186" width="96" height="44" rx="12" class="bluep o"/>
  <circle cx="100" cy="-164" r="14" class="gold o"/>
</g>
{steam(196, 132, 3, 1, 'blue')}
""")

add('rich', '金貨の山の前に立って満足げな人のイラスト。', 'お金や物をたくさん持っている、豊かな。', f"""
<g transform="translate(230 352)">
  <g class="gold o">{''.join(f'<ellipse cx="{x}" cy="{y}" rx="46" ry="19"/>'
                             for y, xs in [(0, [-108, -8, 92]), (-38, [-58, 42]), (-76, [-8])] for x in xs)}</g>
  <g fill="none" stroke="{GLDD}" stroke-width="3">
    <ellipse cx="-108" cy="0" rx="28" ry="11"/><ellipse cx="-8" cy="0" rx="28" ry="11"/><ellipse cx="92" cy="0" rx="28" ry="11"/>
  </g>
</g>
{person(480, 352, 1.2, -1, 'violet', 'gold', 'hold', 'short')}
{spark(120, 176, 1.2)}{spark(500, 130, 1.1)}
""")

add('right', '右を指さし、右向きの矢印が伸びるイラスト。', '右の、右へ(方向)。', f"""
{person(200, 352, 1.3, 1, 'teal', 'blue', 'point', 'short')}
{arrowline([(320, 214),(548, 214)], MUTED, 7, True)}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" stroke-dasharray="12 10">
  <path d="M320 268h216"/>
</g>
""", arrow=True)

add('river', '岸に木が並ぶ川が、ゆるやかに蛇行して流れるイラスト。', '陸の水が流れる筋、川。', f"""
<path d="M140 400C120 320 260 300 250 210 240 130 340 120 330 30"
      fill="none" stroke="{BLUD}" stroke-width="98" stroke-linecap="round"/>
<path d="M140 400C120 320 260 300 250 210 240 130 340 120 330 30"
      fill="none" stroke="{BLUP}" stroke-width="78" stroke-linecap="round"/>
<path d="M140 400C120 320 260 300 250 210 240 130 340 120 330 30"
      fill="none" stroke="{BLU}" stroke-width="4" stroke-dasharray="24 20" stroke-linecap="round"/>
{tree(56, 306, 0.9)}
{tree(534, 286, 0.85)}
{tree(398, 96, 0.6)}
""")

add('road', '中央線のある道路が遠くへ伸び、車が走っているイラスト。', '人や車が通る道、道路。', f"""
<path d="M96 306L266 92h68l170 214z" fill="#cfd6db"/>
<path d="M300 306V92" fill="none" stroke="#fffdf6" stroke-width="10" stroke-dasharray="22 18"/>
<path d="M136 306L272 92M464 306L328 92" fill="none" stroke="#fffdf6" stroke-width="5"/>
{tree(48, 306, 0.8)}
{tree(556, 306, 0.8)}
{car(300, 306, 0.3, 'gold', 1)}
{car(228, 268, 0.72, 'blue', -1)}
""")

add('room', '窓とドアのある部屋に、ベッドと家具が置かれているイラスト。', '建物の中の仕切られた空間、部屋。', f"""
<rect x="70" y="60" width="460" height="246" fill="#fffdf6" class="o"/>
<rect x="306" y="92" width="176" height="120" rx="6" class="bluep o"/>
<path d="M394 92v120M306 152h176" fill="none" stroke="{INK}" stroke-width="3"/>
<rect x="96" y="176" width="104" height="130" class="goldd o"/>
<circle cx="182" cy="244" r="8" class="gold"/>
<g transform="translate(330 300)">
  <path d="M-150-58h300v58h-300z" class="bluep o"/>
  <path d="M-152-58h300v-14h-300z" class="blue o"/>
  <rect x="-140" y="-100" width="34" height="100" class="blue o"/>
  <rect x="-96" y="-92" width="106" height="36" rx="12" class="paper"/>
  <path d="M18-58h132v-30q0-16-16-16H36q-18 0-18 16z" class="tealp o"/>
</g>
<ellipse cx="180" cy="368" rx="150" ry="26" class="violetp o"/>
""")

add('rubber band', '輪ゴムで束ねた鉛筆と、伸び縮みを示す両向きの矢印のイラスト。', '輪の形をしたゴム、輪ゴム。', f"""
<g transform="translate(300 200)">
  <g class="gold o">{''.join(f'<rect x="-16" y="-96" width="32" height="192" rx="6" transform="rotate({d} 0 0)"/>'
                             for d in (-24, -12, 0, 12, 24))}</g>
  <g fill="#e8d8b8" class="o">{''.join(f'<path d="M0-96l-8-22h16z" transform="rotate({d} 0 0)"/>' for d in (-24, -12, 0, 12, 24))}</g>
  <ellipse cx="0" cy="6" rx="34" ry="52" fill="none" stroke="{CRL}" stroke-width="16"/>
</g>
{arrowline([(220, 200),(120, 200)], MUTED, 6, True)}
{arrowline([(380, 200),(480, 200)], MUTED, 6, True)}
""", arrow=True)

add('rust', '鉄の板の一部に赤茶色のさびが広がっていくイラスト。', '鉄が酸化して赤茶色になること、さび。', f"""
<rect x="140" y="118" width="320" height="180" rx="10" fill="#cfd6db" stroke="{INK}" stroke-width="3"/>
<g fill="{BRN}">
  <ellipse cx="250" cy="210" rx="52" ry="40" transform="rotate(-12 250 210)"/>
  <ellipse cx="316" cy="250" rx="34" ry="26"/>
  <ellipse cx="212" cy="264" rx="26" ry="20"/>
  <ellipse cx="296" cy="176" rx="22" ry="16"/>
</g>
<g fill="none" stroke="{BRN}" stroke-width="5" stroke-dasharray="12 10" stroke-linecap="round">
  <path d="M300 210a86 86 0 0 1 0 96"/>
  <path d="M300 210a126 126 0 0 1 0 150"/>
</g>
{clock(520, 96, 40, 10, 2)}
""")

add('rusty', '古びて板の全体がさび色になった鉄のイラスト。', 'さびがついた、さびている。', f"""
<rect x="140" y="118" width="320" height="180" rx="10" fill="{BRN}" stroke="{INK}" stroke-width="3"/>
<g fill="{GLDD}">
  <ellipse cx="230" cy="196" rx="46" ry="34" transform="rotate(-10 230 196)"/>
  <ellipse cx="352" cy="240" rx="52" ry="40"/>
  <ellipse cx="264" cy="268" rx="30" ry="22"/>
  <circle cx="392" cy="164" r="20"/>
</g>
<g fill="none" stroke="{GLDD}" stroke-width="4" stroke-linecap="round">
  <path d="M180 150l40 26M300 128l-8 30M420 220l-24 26"/>
</g>
""")

add('sad', '涙をこぼして悲しそうな顔のイラスト。', '心が痛んで泣きたい気持ち、悲しい。', f"""
{face(300, 190, 112, 'sad')}
<g fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round">
  <path d="M214 146l44-25M386 146l-44-25"/>
</g>
<g class="blue">{drop(254, 268, 1.3)}{drop(346, 268, 1.3)}</g>
""")

add('sadness', 'うつむいて座り、涙をこぼしている人のイラスト。', '悲しいという気持ち、悲しみ。', f"""
{chair(300, 352, 1.15, 'blue', 1)}
{sit(300, 352, 1.15, 1, 'blue', 'blue', 'bob', 'sad', 'lap')}
<g class="blue">{drop(232, 250, 1.2)}{drop(368, 250, 1.2)}</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" stroke-dasharray="11 10">
  <path d="M150 130q40 30 0 62M450 130q-40 30 0 62"/>
</g>
""")

add('salad', 'ボウルに葉野菜とトマトを入れたサラダのイラスト。', '野菜を生で混ぜて食べる料理、サラダ。', f"""
<g transform="translate(300 250)">
  <g class="green o">
    <ellipse cx="-84" cy="-44" rx="52" ry="30" transform="rotate(-26 -84 -44)"/>
    <ellipse cx="80" cy="-44" rx="52" ry="30" transform="rotate(26 80 -44)"/>
    <ellipse cx="-8" cy="-66" rx="56" ry="32"/>
  </g>
  <circle cx="-38" cy="-22" r="28" class="coral o"/>
  <circle cx="42" cy="-14" r="24" class="coral o"/>
  <path d="M-134-40h268q-18 96-134 96t-134-96z" class="teal o"/>
  <path d="M-134-40h268" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
<g transform="translate(496 250) rotate(14)">
  <path d="M-12 0h24v96h-24z" class="paper"/>
  <path d="M-12-30h24v30h-24z" class="paper"/>
  <path d="M-24-56l14 26M24-56l-14 26M-8-58v6M8-58v6" fill="none" stroke="{STONE}" stroke-width="5" stroke-linecap="round"/>
</g>
""")

add('same', '同じ形と色の箱が二つ並び、間に等号が置かれているイラスト。', '違いがない、同様の。', f"""
{box(140, 300, 148, 116, 36, 'blue')}
{box(460, 300, 148, 116, 36, 'blue')}
<g fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round">
  <path d="M262 282h76M262 320h76"/>
</g>
""")

add('underestimate', '小さな袋から、思ったより大きな荷物が出てくるイラスト。', '実際より小さいと見積もる、軽く見る。', f"""
<g transform="translate(160 262)">
  <path d="M-74-62h148l-12 124h-124z" class="violet o"/>
  <path d="M-44-62q44-32 88 0" fill="none" stroke="{VIOD}" stroke-width="9"/>
</g>
<g transform="translate(430 240) rotate(-8)">
  <rect x="-100" y="-76" width="200" height="152" rx="8" class="gold o"/>
  <path d="M-100-76h200l-28-32h-144z" class="goldp o"/>
  <path d="M0-76v152" fill="none" stroke="{GLDD}" stroke-width="5"/>
</g>
{arrowline([(238, 190),(310, 148),(348, 158)], MUTED, 5, True)}
{spark(516, 128, 1.3)}
""", arrow=True)

add('scales', '体重計の上に立って目盛りを見る人のイラスト。', '体重を量るはかり、体重計。', f"""
{person(300, 322, 1.25, 1, 'teal', 'blue', 'stand', 'short', 'neutral')}
<g transform="translate(300 358)">
  <rect x="-176" y="-42" width="352" height="42" rx="14" class="blue o"/>
  <rect x="-136" y="-36" width="272" height="26" rx="10" class="bluep o"/>
  <path d="M-60-36v26M-20-36v26M20-36v26M60-36v26" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
""")

add('school', '校舎の前に子どもたちが集まり、旗が立っているイラスト。', '勉強や学びのための場所、学校。', f"""
{building(400, 340, 1.35, 'coral')}
{flag(120, 306, 1.0, 'blue')}
{person(190, 352, 1.05, 1, 'teal', 'blue', 'walk', 'short')}
{person(268, 352, 0.95, 1, 'gold', 'blue', 'walk', 'bob')}
{person(340, 352, 0.95, 1, 'violet', 'blue', 'stand', 'bun')}
""")

add('science', 'フラスコから泡が立ちのぼり、試験管が並ぶ実験のイラスト。', '自然のしくみを調べる学問、科学・理科。', f"""
<g transform="translate(230 306)">
  <path d="M-34-176h68v70l66 100h-200z" fill="#fffefd" stroke="{INK}" stroke-width="3"/>
  <path d="M-58-60h116l36 54h-188z" class="greenp"/>
  <path d="M-34-176h68v70l66 100h-200z" fill="none" stroke="{INK}" stroke-width="3"/>
  <g class="greenp o"><circle cx="-22" cy="-84" r="12"/><circle cx="16" cy="-104" r="9"/><circle cx="-4" cy="-130" r="7"/></g>
</g>
<g transform="translate(430 306)">
  <path d="M-26-146v112a26 26 0 0 0 52 0v-112z" fill="#fffefd" stroke="{INK}" stroke-width="3"/>
  <path d="M-26-46v12a26 26 0 0 0 52 0v-12z" class="violetp"/>
  <path d="M-26-146h52" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
</g>
<g transform="translate(300 306)">
  <rect x="80" y="-20" width="160" height="16" rx="8" class="goldd o"/>
  <path d="M96-4v4M224-4v4" fill="none" stroke="{GLDD}" stroke-width="10" stroke-linecap="round"/>
</g>
{spark(300, 96, 1.1)}
""")

add('screws', 'ドライバーでねじを板に締めつけているイラスト。', '回して締める金具、ねじ(複数形)。', f"""
<rect x="120" y="206" width="360" height="118" rx="8" class="goldp o"/>
{screw(200, 300)}
{screw(392, 262)}
<g transform="translate(371 256) rotate(200)">
  <path d="M0 0h120" fill="none" stroke="{STONE}" stroke-width="14" stroke-linecap="round"/>
  <rect x="120" y="-30" width="118" height="60" rx="16" class="coral o"/>
  <path d="M0-11l-18 5 18 6z" fill="{STONE}" class="o"/>
</g>
""")

add('sea', '波のうねる海にヨットが浮かび、太陽が光るイラスト。', '広く水をたたえた広がり、海。', f"""
{sun(500, 84, 44)}
<rect x="0" y="236" width="600" height="164" class="bluep"/>
<path d="M0 236h600" fill="none" stroke="{BLU}" stroke-width="4"/>
<g fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round">
  <path d="M40 270q24-14 48 0t48 0"/>
  <path d="M330 268q24-14 48 0t48 0"/>
  <path d="M120 304q24-14 48 0t48 0"/>
  <path d="M420 306q24-14 48 0t48 0"/>
</g>
<g transform="translate(230 236)">
  <path d="M-72 0h144l-28 34h-88z" class="coral o"/>
  <path d="M-4-6v-104" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <path d="M4-14l56 26H4z" class="teal o"/>
  <path d="M-10-4l-40 20h40z" class="tealp o"/>
</g>
""")

add('seaside', '砂浜にパラソルとビーチボールがあり、波が寄せているイラスト。', '海のすぐそば、海辺。', f"""
<rect x="0" y="236" width="600" height="70" class="bluep"/>
<g fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round">
  <path d="M40 250q24-14 48 0t48 0M360 254q24-14 48 0t48 0"/>
</g>
<g fill="none" stroke="#fffdf6" stroke-width="6" stroke-linecap="round">
  <path d="M0 300q60-26 120 0t120 0 120 0 120 0 120 0"/>
</g>
<rect x="0" y="306" width="600" height="94" fill="#f4e3c0"/>
<g transform="translate(180 306)">
  <path d="M0 0v-160" fill="none" stroke="{BRN}" stroke-width="10" stroke-linecap="round"/>
  <path d="M-116-160h232l-46-64h-140z" class="coral o"/>
  <path d="M-70-224l46 64M0-224l46 64M70-224l46 64" fill="none" stroke="{GLD}" stroke-width="10"/>
</g>
<g transform="translate(420 356)">
  <circle r="40" class="paper"/>
  <path d="M0-40A40 40 0 0 1 34 20L0 0z" class="coral o"/>
  <path d="M0-40A40 40 0 0 0 -34 20L0 0z" class="blue o"/>
  <circle r="7" class="gold"/>
</g>
<path d="M300 388h190" fill="none" stroke="{TEA}" stroke-width="12" stroke-linecap="round"/>
""")

add('see', '大きな目の前から、見ている先の木へ点線が伸びるイラスト。', '目でとらえる、見る。', f"""
{eye(200, 190, 1)}
{tree(480, 306, 1.15)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 10" stroke-linecap="round">
  <path d="M320 168q66-24 108-10M320 210q66 22 108 12"/>
</g>
""")

add('seedling', '土の上に双葉の芽が出たばかりのイラスト。', '芽を出したばかりの若い植物、苗。', f"""
<path d="M160 360q140-70 280 0z" fill="{BRN}"/>
<path d="M160 360q140-70 280 0" fill="none" stroke="{INK}" stroke-width="3"/>
<g transform="translate(300 340)">
  <path d="M0 20V-76" fill="none" stroke="{GRND}" stroke-width="10" stroke-linecap="round"/>
  <path d="M0-50q-74-14-88-66 62-6 88 66z" class="green o"/>
  <path d="M0-50q74-14 88-66-62-6-88 66z" class="green o"/>
</g>
{drop(390, 130, 1.3)}
{arc(400, 176, 344, 214, 30, MUTED, True)}
""", arrow=True)

add('sell', '店員が商品を手渡し、客が代金を払うイラスト。', '品物をお金と引きかえる、売る。', f"""
{table(318)}
<g transform="translate(300 246)">
  <path d="M-56-38h112v76h-112z" class="gold o"/>
  <path d="M-32-38q32-30 64 0" fill="none" stroke="{GLDD}" stroke-width="7"/>
</g>
{person(120, 352, 1.15, 1, 'teal', 'blue', 'give', 'short')}
{person(480, 352, 1.15, -1, 'violet', 'blue', 'reach', 'bob')}
{coin(230, 300, 24)}
{coin(266, 314, 20)}
""")

add('send', '封筒が矢印の向きに飛んでいくイラスト。', '相手に向けて届ける、送る。', f"""
{hand(120, 300, 1)}
<g transform="translate(248 214) rotate(-14)">
  <rect x="-78" y="-52" width="156" height="104" rx="4" class="paper"/>
  <path d="M-78-52l78 60 78-60" fill="none" stroke="{MUTED}" stroke-width="5"/>
</g>
{arrowline([(350, 190),(556, 180)], MUTED, 6, True)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" stroke-linecap="round">
  <path d="M360 274q80-6 140-10"/>
</g>
""", arrow=True)

add('unwilling', '引っ張られても体を引いて動こうとしない人のイラスト。', '気が進まない、いやいやの。', f"""
{person(380, 352, 1.3, 1, 'coral', 'blue', 'reach', 'short', 'sad')}
<path d="M286 258L120 268" fill="none" stroke="{BRN}" stroke-width="6" stroke-linecap="round"/>
{arrowline([(120, 268),(44, 272)], MUTED, 6, True)}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" stroke-dasharray="12 10">
  <path d="M440 340q40 12 84 0"/>
</g>
""", arrow=True)

add('seven', '金貨が七枚、横一列に並んでいるイラスト。', '数7、七つ。', f"""
{coinrow(78, 240, 7, 74, 32)}
""")

add('seventeen', '金貨が十枚と七枚、二段に並んでいるイラスト。', '数17、十七。', f"""
{coinrow(90, 150, 10, 46, 19)}
{coinrow(150, 286, 7, 50, 19)}
""")

add('seventh', '七つの箱が階段状に並び、七番目の箱だけが金色のイラスト。', '7番目の、7分の1。', f"""
{''.join(f'<rect x="{60+i*76}" y="{306-(44+i*18)}" width="60" height="{44+i*18}" rx="8" class="bluep o"/>' for i in range(6))}
<rect x="516" y="158" width="60" height="148" rx="8" class="gold o"/>
<g transform="translate(546 132)">{spark(0, 0, 1.2)}</g>
{ring(546, 232, 62, True)}
""")

add('seventy', '十のまとまりが七つ、縦に並んでいるイラスト。', '数70、七十。', f"""
{''.join(dotcol(64 + c*80, 108, 10, 17, 8, 'teal') for c in range(7))}
""")

add('sewing', '針と糸で二枚の布を縫い合わせるイラスト。', '布を縫って衣服を作ること、裁縫。', f"""
<g transform="translate(300 300)">
  <rect x="-170" y="-64" width="196" height="128" rx="10" class="tealp o"/>
  <rect x="-12" y="-64" width="182" height="128" rx="10" class="bluep o"/>
  <path d="M-12-64v128" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="14 11"/>
</g>
<g transform="translate(178 190) rotate(34)">{needle(0, 0)}</g>
<path d="M120 148q-44-32-70 8t-40 96" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round"/>
""")

add('sharpener', '鉛筆削りに鉛筆を差し込み、削りかすが落ちているイラスト。', '鉛筆の芯をとがらせる道具、鉛筆削り。', f"""
<g transform="translate(320 250)">
  <rect x="-76" y="-66" width="152" height="132" rx="20" class="teal o"/>
  <circle cx="0" cy="-8" r="28" class="teal o"/>
  <circle cx="0" cy="-8" r="13" class="ink"/>
</g>
<g transform="translate(399 192) rotate(148)">{pencil(0, 0, 0, 0.9, 'gold')}</g>
<path d="M330 330q-34 22-70 8" fill="none" stroke="{GLD}" stroke-width="8" stroke-linecap="round"/>
<path d="M280 348q-30 20-62 10" fill="none" stroke="{GLD}" stroke-width="8" stroke-linecap="round"/>
""")

add('shaver', '電気シェーバーを頬に当ててひげをそるイラスト。', 'ひげをそる道具、かみそり・シェーバー。', f"""
{face(240, 190, 100, 'flat')}
<g fill="{HAIR}">{''.join(f'<circle cx="{x}" cy="{y}" r="4"/>'
                           for x, y in [(206, 262), (232, 268), (258, 268), (284, 262), (220, 280), (248, 282), (272, 276)])}</g>
<g transform="translate(392 320) rotate(-22)">
  <rect x="-36" y="-88" width="72" height="124" rx="18" class="blue o"/>
  <rect x="-36" y="-148" width="72" height="62" rx="10" class="bluep o"/>
  <g fill="none" stroke="{BLU}" stroke-width="4">
    <path d="M-26-148v62M-8-148v62M10-148v62M28-148v62"/>
  </g>
</g>
{hand(384, 348, 1)}
""")

add('she', '二人のうち右の女性が点線の輪で囲まれ、矢印で指されているイラスト。', '彼女は、彼女が(女性を指す語)。', f"""
{person(160, 352, 1.2, 1, 'blue', 'blue', 'stand', 'short', 'neutral')}
{ring(430, 220, 128, True)}
{person(430, 352, 1.25, 1, 'coral', 'blue', 'up', 'bob')}
{arrowline([(46, 132),(300, 186)], MUTED, 6, True)}
{spark(500, 120, 1.1)}
""", arrow=True)

add('sheep', 'もこもこの毛をした羊が草を食べているイラスト。', '毛や肉をとるために飼われる動物、羊。', f"""
<g transform="translate(310 296)">
  <path d="M-92-46l-14 66M-30-16l-8 62M52-16l8 62M112-46l14 66" fill="none"
        stroke="{INK}" stroke-width="16" stroke-linecap="round"/>
  <g class="paper o">{''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>'
                              for x, y, r in [(0,-72,52),(62,-58,42),(-62,-58,42),(22,-104,38),(-24,-100,36)])}</g>
  <circle cx="-128" cy="-72" r="44" class="paper o"/>
  <path d="M-160-100l-16-34 40 22z" class="paper o"/>
  <circle cx="-140" cy="-86" r="6" class="ink"/>
  <ellipse cx="-166" cy="-62" rx="14" ry="11" class="ink"/>
</g>
<g fill="none" stroke="{GRND}" stroke-width="5" stroke-linecap="round">
  <path d="M120 306v-22q0-10-12-14M520 306v-20q0-10 12-14"/>
</g>
""")

add('shepherd', '杖を持った羊飼いが、羊を二匹連れて歩くイラスト。', '羊を飼って世話をする人、羊飼い。', f"""
{person(470, 352, 1.25, -1, 'green', 'blue', 'hold', 'cap')}
<path d="M486 340L470 162" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>
<path d="M470 162q-40-24-60 6" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>
<g transform="translate(180 316) scale(0.62)">
  <path d="M-92-46l-14 46M-30-16l-8 42M52-16l8 42M112-46l14 46" fill="none" stroke="{INK}" stroke-width="16" stroke-linecap="round"/>
  <g class="paper o">{''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(0,-72,52),(62,-58,42),(-62,-58,42),(20,-104,38)])}</g>
  <circle cx="-128" cy="-72" r="44" class="paper o"/>
  <circle cx="-140" cy="-86" r="8" class="ink"/>
</g>
<g transform="translate(300 320) scale(0.5)">
  <path d="M-92-46l-14 46M-30-16l-8 42M52-16l8 42M112-46l14 46" fill="none" stroke="{INK}" stroke-width="16" stroke-linecap="round"/>
  <g class="paper o">{''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(0,-72,52),(62,-58,42),(-62,-58,42),(20,-104,38)])}</g>
  <circle cx="-128" cy="-72" r="44" class="paper o"/>
  <circle cx="-140" cy="-86" r="8" class="ink"/>
</g>
""")

add('shirt', 'ハンガーにかけたワイシャツとネクタイのイラスト。', '上半身に着る衣服、シャツ。', f"""
<g transform="translate(300 220)">
  <path d="M-100-96l-86 46 26 52 60-30z" class="paper"/>
  <path d="M100-96l86 46-26 52-60-30z" class="paper"/>
  <rect x="-100" y="-96" width="200" height="212" rx="12" class="paper"/>
  <path d="M-46-96l46 46 46-46-26-14h-40z" class="bluep o"/>
  <path d="M0-30l-24 20 24 100 24-100z" class="coral o"/>
  <path d="M44 4h46v42h-46z" class="paper"/>
  <path d="M-74-96l74-42 74 42" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>
  <path d="M0-138v-26q0-16 14-16" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>
</g>
""")

add('shoe', '一足の靴が並べて置かれているイラスト。', '足を保護するはきもの、靴。', f"""
<g transform="translate(210 320)">
  <path d="M-124 0h248q0-34-44-46l-96-20q-44-10-74-50l-34 24z" class="coral o"/>
  <path d="M-124 0h248v16h-248z" class="ink"/>
  <path d="M-64-92q34-18 68 0M-74-78q40-22 82 0" fill="none" stroke="#fffdf6" stroke-width="6"/>
</g>
<g transform="translate(430 336) rotate(-6)">
  <path d="M-124 0h248q0-34-44-46l-96-20q-44-10-74-50l-34 24z" class="teal o"/>
  <path d="M-124 0h248v16h-248z" class="ink"/>
  <path d="M-64-92q34-18 68 0M-74-78q40-22 82 0" fill="none" stroke="#fffdf6" stroke-width="6"/>
</g>
""")

add('shop', 'ひさしとショーウィンドウのある店先のイラスト。', '品物を売る場所、店。', f"""
<g transform="translate(300 306)">
  <rect x="-236" y="-186" width="472" height="186" class="paper"/>
  <rect x="-260" y="-186" width="520" height="34" class="coral o"/>
  <g fill="none" stroke="{CRLD}" stroke-width="5">
    <path d="M-186-186v34M-112-186v34M-38-186v34M36-186v34M110-186v34M184-186v34"/>
  </g>
  <rect x="-208" y="-152" width="184" height="112" class="bluep o"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><path d="M-208-96h184M-116-152v112"/></g>
  <g class="gold o"><rect x="-190" y="-86" width="42" height="34" rx="6"/><rect x="-130" y="-78" width="34" height="26" rx="6"/></g>
  <rect x="16" y="-152" width="116" height="152" class="teald o"/>
  <circle cx="118" cy="-72" r="9" class="gold"/>
  <g class="greenp o"><rect x="156" y="-136" width="80" height="40" rx="6"/><rect x="156" y="-84" width="80" height="40" rx="6"/></g>
</g>
{person(546, 352, 0.95, -1, 'violet', 'blue', 'walk', 'bob')}
""")

add('shopping list', '買い物かごの横で、メモの項目に印をつけていくイラスト。', '買う物を書き出したメモ、買い物リスト。', f"""
<rect x="130" y="104" width="240" height="256" rx="8" class="paper"/>
<g class="bluep o">{''.join(f'<rect x="152" y="{126+i*56}" width="30" height="30" rx="6"/>' for i in range(4))}</g>
{tick(167, 141, 0.4)}{tick(167, 197, 0.4)}
<g fill="{MUTED}">{''.join(f'<rect x="196" y="{134+i*56}" width="{146-(i%3)*40}" height="13" rx="6"/>' for i in range(4))}</g>
{pencil(430, 250, 146, 0.85, 'gold')}
{hand(504, 208, -1)}
<g transform="translate(500 200)">
  <path d="M-46-56h92l-14 76h-64z" class="teal o"/>
  <path d="M-30-56q30-30 60 0" fill="none" stroke="{TEAD}" stroke-width="7"/>
</g>
""")

add('short', '長いひもをはさみで切り、短くなった端を手に持つイラスト。', '長さや丈が短い。', f"""
<path d="M40 208q130-46 250-6" fill="none" stroke="{GLD}" stroke-width="13" stroke-linecap="round"/>
{scissors(300, 200, -14, 1)}
<path d="M334 206q80 18 168 6" fill="none" stroke="{GLD}" stroke-width="13" stroke-linecap="round"/>
{hand(534, 214, -1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" stroke-linecap="round">
  <path d="M40 268q120 22 214-16"/>
</g>
""")

add('should', '作業の前にヘルメットをかぶり、そばに印がつくイラスト。', '〜すべきだ(助言や義務)。', f"""
{person(290, 352, 1.3, 1, 'gold', 'blue', 'hold', 'short')}
<g transform="translate(290 352) scale(1.3)">
  <path d="M-40-134a40 40 0 0 1 80 0v12h-80z" class="goldd o"/>
  <path d="M-50-124h100" fill="none" stroke="{GLDD}" stroke-width="12" stroke-linecap="round"/>
</g>
{tick(480, 156, 1.5)}
""")

finish(__file__)
