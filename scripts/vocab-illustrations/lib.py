"""英単語の記憶イラスト(SVG)を書き出すための共通部品。

使い方: 同じディレクトリに batchNN.py を作り、`from lib import *` して emit() を呼ぶ。
  python3 scripts/vocab-illustrations/batch04.py
規約は docs/vocabulary-illustrations.md を参照。SVGは public/images/vocabulary/ に出る。
"""
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'public', 'images', 'vocabulary')
TONES = {
 'teal':('#238b83','#dff4ef','#176a66'),
 'coral':('#e86452','#fde9e3','#b74338'),
 'gold':('#d99a2b','#fff0c5','#a66b15'),
 'blue':('#4e86c6','#e1edfb','#315f98'),
 'violet':('#816eb2','#eee8fb','#5f4d91'),
 'green':('#4e986a','#e1f3e5','#34734d'),
}
INK='#2f4055'; SKIN='#f2c29d'; SKINL='#a86f55'; HAIR='#34475a'; MUTED='#80909d'
STYLE = f"""  <style>
    .a {{ fill: none; stroke: {INK}; stroke-width: 3; stroke-linecap: round; stroke-linejoin: round; }}
    .o {{ stroke: {INK}; stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; }}
    .ground {{ fill: #edf3ed; stroke: none; }}
    .paper {{ fill: #fffefd; stroke: {INK}; stroke-width: 2.5; stroke-linejoin: round; }}
    .muted {{ fill: none; stroke: {MUTED}; stroke-width: 2.5; stroke-dasharray: 7 8; stroke-linecap: round; }}
    .ink {{ fill: {INK}; stroke: none; }}
    text {{ display: none; }}
"""
for n,(s,p,d) in TONES.items():
    STYLE += f"    .{n} {{ fill: {s}; }} .{n}p {{ fill: {p}; }} .{n}d {{ fill: {d}; }} .{n}s {{ fill: none; stroke: {s}; stroke-width: 3; stroke-linecap: round; stroke-linejoin: round; }}\n"
STYLE += "  </style>\n"

ARROW = f'  <defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M1 1l8 4-8 4z" fill="{INK}"/></marker></defs>\n'

POSES = {
 'stand': 'M-22-70l-16 45M22-70l16 45',
 'carry': 'M-22-70l12 34M22-70L10-36',
 'point': 'M-22-70l-14 44M22-70l44 5',
 'walk':  'M-22-70l-28 29M22-70l31 24',
 'reach': 'M-22-70l-16 45M22-70l40-30',
 'give':  'M-22-70l-16 45M22-70l46 6',
 'up':    'M-22-70l-26-35-5-17M22-70l26-35 5-17',
 'hold':  'M-22-70l24 26M22-70L2-44',
 'think': 'M-22-70l-17 41M22-70L8-94',
}
LEGS = {
 'walk': 'M-12-8l-26 33M12-8l28 28',
 'stand':'M-12-8l-7 35M12-8l7 35',
}
HAIRS = {
 'short':'M-24-109q3-28 25-28 24 0 28 25-13-10-27-4-12-11-26 7z',
 'bob':'M-29-108q1-31 29-31t30 31v23l-11-9v-18q-20 9-40 0v20l-8 8z',
 'bun':'M-26-111q3-28 27-28 22 0 27 27-15-13-28-3-12-9-26 4z',
 'cap':'M-25-116q8-25 29-21 19 2 23 23z',
}
def person(x,y,scale=1,facing=1,shirt='teal',trousers='blue',pose='stand',hair='short',mood='smile',legs=None):
    ts,tp,td = TONES[shirt]; ls,lp,ld = TONES[trousers]
    legs = legs or ('walk' if pose=='walk' else 'stand')
    mouth = {'smile':'M-8-94q8 8 16 0','sad':'M-8-90q8-8 16 0','neutral':'M-7-92h14'}.get(mood)
    g = [f'<g transform="translate({x} {y}) scale({scale*facing} {scale})">']
    g.append(f'<path d="{LEGS[legs]}" fill="none" stroke="{ld}" stroke-width="11" stroke-linecap="round"/>')
    g.append(f'<path d="M-25-78q25-13 50 0l-8 72h-34z" fill="{ts}" class="o"/>')
    g.append(f'<path d="{POSES[pose]}" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>')
    g.append(f'<circle cx="0" cy="-108" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>')
    hc = TONES['blue'][0] if hair=='cap' else HAIR
    g.append(f'<path d="{HAIRS[hair]}" fill="{hc}" stroke="{hc}" stroke-width="2"/>')
    g.append(f'<circle cx="-8" cy="-104" r="2.2" class="ink"/><circle cx="8" cy="-104" r="2.2" class="ink"/>')
    if mood=='surprised':
        g.append(f'<circle cx="0" cy="-91" r="4" fill="none" stroke="{INK}" stroke-width="2"/>')
    else:
        g.append(f'<path d="{mouth}" fill="none" stroke="{INK}" stroke-width="2"/>')
    g.append('</g>')
    return ''.join(g)

def emit(word, alt, body, bg='#fffaf1', ground=True, arrow=False):
    word = word.replace(' ', '-')  # ファイル名に空白を入れない
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="600" height="400" role="img"',
             f'     aria-label="{alt}">', STYLE.rstrip('\n')]
    if arrow: parts.append(ARROW.rstrip('\n'))
    parts.append(f'  <rect width="600" height="400" rx="20" fill="{bg}"/>')
    if ground: parts.append('  <path d="M0 306h600v94H0z" class="ground"/>')
    parts.append('  ' + body.strip())
    parts.append('</svg>')
    open(os.path.join(OUT, word + '.svg'),'w').write('\n'.join(parts)+'\n')
    return word


# --- 使い回す小物 ------------------------------------------------------------

def hand(x, y, f=1):
    """開いた手。f=-1 で左右反転。"""
    fingers = ''.join(f'<rect x="26" y="{-16+i*13}" width="34" height="11" rx="5.5" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>' for i in range(3))
    return (f'<g transform="translate({x} {y}) scale({f} 1)">'
            f'<ellipse cx="0" cy="4" rx="34" ry="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>{fingers}'
            f'<ellipse cx="8" cy="-26" rx="20" ry="11" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5" transform="rotate(-24 8 -26)"/></g>')

def sun(x, y, r=48):
    rays = ''.join(f'<path d="M{x} {y-r-14}v-16" transform="rotate({d} {x} {y})"/>' for d in range(0, 360, 45))
    return f'<circle cx="{x}" cy="{y}" r="{r}" class="goldp o"/><g class="golds">{rays}</g>'

def drop(x, y, s=1, cls='blue'):
    return f'<path d="M{x} {y}c{8*s} {8*s} {8*s} {15*s} 0 {19*s}c-{8*s}-{4*s}-{8*s}-{11*s} 0-{19*s}z" class="{cls} o"/>'

def tree(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-7 0v-46h14V0" class="goldd"/>'
            f'<circle cx="-16" cy="-58" r="22" class="greenp o"/><circle cx="14" cy="-64" r="25" class="greenp o"/>'
            f'<circle cx="0" cy="-86" r="20" class="greenp o"/></g>')

def box(x, y, w=84, h=66, d=22, cls='gold'):
    return (f'<g transform="translate({x} {y})"><path d="M{-w/2} {-h/2}h{w}v{h}h{-w}z" class="{cls} o"/>'
            f'<path d="M{-w/2} {-h/2}l{d} {-d}h{w}l{-d} {d}z" class="{cls}p o"/>'
            f'<path d="M{w/2} {-h/2}l{d} {-d}v{h}l{-d} {d}z" class="{cls}d o"/></g>')

def sheet(words, path='/tmp/vocab-sheet.html', cols=4):
    """作った絵をまとめて目視確認するための一覧HTML。"""
    base = os.path.abspath(OUT)
    cells = ''.join(f'<figure><img src="{base}/{w}.svg"><figcaption>{w}</figcaption></figure>' for w in words)
    open(path, 'w').write(
        f'<html><body style="margin:0;background:#eee;font:12px sans-serif">'
        f'<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:6px;padding:6px">{cells}</div>'
        f'<style>figure{{margin:0}}img{{width:100%;display:block;background:#fff}}'
        f'figcaption{{text-align:center;font-weight:700}}</style></body></html>')
    return path

def flame(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0c-30-16-34-54-6-84 4 22 18 26 22 12 6-20 22-30 30-44 10 30 30 34 30 62C76-22 44 12 0 0z" class="coral o"/>'
            f'<path d="M2-8c-16-10-18-32-4-50 4 14 12 16 14 8 4-12 12-18 16-26 6 18 16 20 16 36C44-20 26-2 2-8z" class="goldp o"/></g>')

def building(x, y, s=1, cls='teal'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-70 0v-96h140V0z" fill="#fffdf6" class="o"/>'
            f'<path d="M-82-96L0-146l82 50z" class="{cls} o"/>'
            f'<rect x="-46" y="-76" width="34" height="30" class="{cls}p o"/>'
            f'<rect x="12" y="-76" width="34" height="30" class="{cls}p o"/>'
            f'<path d="M-18-40h36V0h-36z" class="{cls}d o"/></g>')

def thermometer(x, y, level=0.8, s=1):
    """level: 0(低い)〜1(高い)。"""
    h = 150 * level
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect x="-14" y="-176" width="28" height="176" rx="14" fill="#fffdf6" class="o"/>'
            f'<circle cx="0" cy="6" r="26" fill="#fffdf6" class="o"/>'
            f'<rect x="-7" y="{-4-h}" width="14" height="{h+10}" rx="7" class="coral"/>'
            f'<circle cx="0" cy="6" r="17" class="coral"/>'
            f'<g fill="none" stroke="{MUTED}" stroke-width="2">'
            + ''.join(f'<path d="M14 {-30-i*30}h10"/>' for i in range(5)) + '</g></g>')

def cloud(x, y, s=1, cls='blue'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-52 16q-5-25 19-31 8-31 39-20 17 2 22 20 28-3 30 22 1 22-24 24h-66q-17-1-20-15z" class="{cls}p o"/></g>')

def plane(x, y, s=1, r=0, cls='teal'):
    return (f'<g transform="translate({x} {y}) scale({s}) rotate({r})">'
            f'<path d="M-30-14L-96-92h30l86 78zM-30 14l-66 78h30l86-78z" class="{cls}p o"/>'
            f'<path d="M-120-2q0-18 24-20h150l44-30h22l-16 30h30q22 0 22 22t-22 22h-30l16 30h-22l-44-30H-96q-24-2-24-24z" class="{cls} o"/>'
            f'<g fill="#fffdf6" stroke="{INK}" stroke-width="2">'
            f'<circle cx="30" cy="-2" r="7"/><circle cx="56" cy="-2" r="7"/><circle cx="82" cy="-2" r="7"/></g></g>')

def face(x, y, r=90, mood='smile'):
    mouths = {
        'smile': f'M{-r*0.42} {r*0.2}q{r*0.42} {r*0.5} {r*0.84} 0',
        'sad': f'M{-r*0.42} {r*0.42}q{r*0.42} {-r*0.5} {r*0.84} 0',
        'grin': f'M{-r*0.46} {r*0.16}q{r*0.46} {r*0.56} {r*0.92} 0z',
        'flat': f'M{-r*0.38} {r*0.3}h{r*0.76}',
    }
    fill = f'fill="{INK}"' if mood == 'grin' else 'fill="none"'
    return (f'<g transform="translate({x} {y})">'
            f'<circle r="{r}" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>'
            f'<circle cx="{-r*0.34}" cy="{-r*0.18}" r="{r*0.075}" class="ink"/>'
            f'<circle cx="{r*0.34}" cy="{-r*0.18}" r="{r*0.075}" class="ink"/>'
            f'<path d="{mouths[mood]}" {fill} stroke="{INK}" stroke-width="{r*0.07}" stroke-linecap="round" stroke-linejoin="round"/></g>')

def tower(x, y, s=1, cls='teal', floors=5):
    """窓の並んだ高い建物。第83回から使用。"""
    win = ''.join(f'<rect x="{-40+c*36}" y="{-30*f-24}" width="24" height="18"/>' for f in range(floors) for c in range(3))
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-56 0v-{30*floors+20}h112V0z" fill="#fffdf6" class="o"/>'
            f'<g class="{cls}p o">{win}</g>'
            f'<path d="M-20-30h40V0h-40z" class="{cls}d o"/></g>')

def sit(x, y, scale=1, facing=1, shirt='teal', trousers='blue', hair='short', mood='smile', arm='lap'):
    """いすに腰かけた人。(x,y)は足もと。第85回から使用。"""
    ts, tp, td = TONES[shirt]; ls, lp, ld = TONES[trousers]
    mouth = {'smile': 'M-8-94q8 8 16 0', 'sad': 'M-8-90q8-8 16 0', 'neutral': 'M-7-92h14'}.get(mood)
    arms = {'lap': 'M-14-76l-4 34 40 6', 'down': 'M-14-76l-6 44', 'up': 'M-14-76l-18-40'}
    g = [f'<g transform="translate({x} {y}) scale({scale*facing} {scale})">']
    g.append(f'<path d="M-6-34h40v34" fill="none" stroke="{ld}" stroke-width="17" stroke-linecap="round" stroke-linejoin="round"/>')
    g.append(f'<path d="M-26-34q26-12 52 0l-8-50h-36z" fill="{ts}" class="o"/>')
    g.append(f'<path d="{arms[arm]}" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>')
    g.append(f'<circle cx="0" cy="-108" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>')
    hc = TONES['blue'][0] if hair == 'cap' else HAIR
    g.append(f'<path d="{HAIRS[hair]}" fill="{hc}" stroke="{hc}" stroke-width="2"/>')
    g.append(f'<circle cx="-8" cy="-104" r="2.2" class="ink"/><circle cx="8" cy="-104" r="2.2" class="ink"/>')
    g.append(f'<path d="{mouth}" fill="none" stroke="{INK}" stroke-width="2"/>')
    g.append('</g>')
    return ''.join(g)

def chair(x, y, s=1, cls='gold', facing=1):
    """背もたれつきのいす。(x,y)は脚もと。第89回から使用。"""
    ts, tp, td = TONES[cls]
    return (f'<g transform="translate({x} {y}) scale({s*facing} {s})">'
            f'<path d="M-46-24v24M46-24v24" fill="none" stroke="{td}" stroke-width="11" stroke-linecap="round"/>'
            f'<path d="M-54-42h108v20h-108z" fill="{ts}" class="o"/>'
            f'<path d="M-54-42v-92h20v92z" fill="{ts}" class="o"/>'
            f'<path d="M-58-134h28v16h-28z" fill="{td}" class="o"/></g>')

def beast(x, y, s=1, fill='#6b5a4a', facing=1):
    """四つ足のけもののシルエット。第89回から使用。"""
    return (f'<g transform="translate({x} {y}) scale({s*facing} {s})">'
            f'<path d="M-96 0l-16 48M-40 0l-12 46M40 0l12 46M92 0l18 46" fill="none" stroke="{fill}" stroke-width="15" stroke-linecap="round"/>'
            f'<path d="M-110-20q-20-56 30-76 60-24 130-6 60 16 62 56 2 40-60 46-110 10-162-20z" fill="{fill}" stroke="{INK}" stroke-width="2.5"/>'
            f'<path d="M96-56q24-30 56-14 30 16 14 46-14 26-46 22z" fill="{fill}" stroke="{INK}" stroke-width="2.5"/>'
            f'<path d="M150-46l40 4-38 18z" fill="{fill}" stroke="{INK}" stroke-width="2.5"/>'
            f'<path d="M108-70l-6-34 30 22zM140-74l14-32 12 30z" fill="{fill}" stroke="{INK}" stroke-width="2.5"/>'
            f'<circle cx="140" cy="-44" r="5" fill="#fffdf6"/>'
            f'<path d="M-110-30q-46-6-56-46 40 0 58 30z" fill="{fill}" stroke="{INK}" stroke-width="2.5"/></g>')
