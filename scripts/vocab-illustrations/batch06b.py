"""第6回の描き直し分。batch06.py のあとに実行する。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

def hat(x,y,r=0,cls='coral'):
    return (f'<g transform="translate({x} {y}) rotate({r})">'
            f'<path d="M-40 0a40 30 0 0 1 80 0z" class="{cls} o"/>'
            f'<ellipse cy="2" rx="58" ry="12" class="{cls}p o"/></g>')

def fish(x,y,s=1,cls='teal',f=1):
    return (f'<g transform="translate({x} {y}) scale({s*f} {s})">'
            f'<path d="M0 0c-40-34-40-56 0-90 44 26 44 58 0 90z" class="{cls} o" transform="rotate(-90)"/>'
            f'<path d="M44 0l30-22v44z" class="{cls} o"/>'
            f'<path d="M-10-24q16 10 0 22" fill="none" stroke="{INK}" stroke-width="2.5"/>'
            f'<circle cx="-26" cy="-8" r="3.4" class="ink"/></g>')

add('blow', '強い風が吹きつけて、木の葉と帽子が飛ばされていくイラスト。', f"""
{tree(110,336,1.0)}
<g class="muted" style="stroke-dasharray:none" opacity=".9">
  <path d="M40 110q120-40 240 0t260-20" marker-end="url(#ar)"/>
  <path d="M60 176q120-40 240 0t250-20" marker-end="url(#ar)"/>
</g>
<g transform="translate(300 250) rotate(24)"><path d="M0 0c-26-20-22-50 6-50 22 0 34 16 34 32 0 16-18 30-40 18z" class="goldp o"/></g>
<g transform="translate(390 306) rotate(-30)"><path d="M0 0c-26-20-22-50 6-50 22 0 34 16 34 32 0 16-18 30-40 18z" class="gold o"/></g>
{hat(486,232,18)}
<path d="M420 250q40-16 60-14" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('fish', '川に釣り糸を垂らし、魚が針にかかっているイラスト。', f"""
<path d="M0 210h600v190H0z" class="bluep"/>
<path d="M0 210q60-14 120 0t120 0 120 0 120 0 120 0" class="a"/>
<path d="M110 50l180 130" fill="none" stroke="{TONES['gold'][2]}" stroke-width="8" stroke-linecap="round"/>
<path d="M290 180v96" fill="none" stroke="{MUTED}" stroke-width="2.5"/>
<path d="M290 276q20 12 0 24" fill="none" stroke="{INK}" stroke-width="4"/>
{fish(330,320,1.15,'teal',1)}
<g class="blues" opacity=".7"><path d="M60 270q40-12 80 0M460 350q40-12 80 0"/></g>
""", ground=False)

add('wind', '風が旗を横へなびかせ、木の枝をしならせているイラスト。', f"""
{tree(500,340,0.9)}
<path d="M140 380V70" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<path d="M148 80q60 0 92 26-40 26-40 52 0 26 40 50-64 26-92 26z" class="coral o"/>
<path d="M148 130q40 8 60 24" fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"/>
<g class="muted" opacity=".9">
  <path d="M60 246q140-40 240 0t250-20" marker-end="url(#ar)"/>
  <path d="M40 300q140-40 240 0t250-20" marker-end="url(#ar)"/>
</g>
""", ground=True, arrow=True)

add('bite', '大きなりんごに歯を立てて、一口かじり取ったあとが残っているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="coralp"/>
<g transform="translate(290 226)">
  <path d="M0-110c86 0 126 58 126 108 0 18-6 34-16 48-26-12-44-30-44-52 0-24 22-40 46-46-14-38-56-58-112-58S-126 6-126 108C-126 250-86 216 0 216S126 250 126 108" fill="none" stroke="none"/>
  <path d="M0-110c72 0 122 54 122 108 0 12-4 24-10 36-30-8-52-28-52-52 0-26 24-44 52-48-18-32-60-54-112-54-76 0-124 52-124 116S-76 218 0 218s124-52 124-110" class="coral o"/>
  <path d="M0-110v-30" class="a"/>
  <path d="M0-134c34-16 44-38 44-38-32-8-44 38-44 38z" class="green o"/>
  <path d="M-64-30q30-20 60 0" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"/>
</g>
<path d="M470 190q-40 6-64 12" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('divide', '丸いケーキに切れ目を入れて、四つに切り分けているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="violetp"/>
<g transform="translate(290 240)">
  <g class="goldp o">
    <path d="M-10-8L-140-58a140 140 0 0 0 0 100z"/>
    <path d="M-4-16L-134-66a140 140 0 0 1 124-72z"/>
    <path d="M10-16l130-50a140 140 0 0 0-124-72z"/>
    <path d="M14-8l130-50a140 140 0 0 1 0 100z"/>
  </g>
  <g fill="{TONES['coral'][1]}" stroke="{INK}" stroke-width="2.5">
    <path d="M-10-14l-126-48a136 136 0 0 0 0 96z" opacity=".55"/>
  </g>
  <path d="M-6-12L-146-66M6-12l140-54M0-18v-124M0-6v112" fill="none" stroke="{INK}" stroke-width="3" stroke-dasharray="9 8"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M110 330q-24-22-30-46"/><path d="M470 330q24-22 30-46"/></g>
""", ground=True, arrow=True)

add('feed', '皿にえさを入れて、犬に食べさせているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="greenp"/>
<g transform="translate(410 322)">
  <ellipse rx="70" ry="21" class="bluep o"/>
  <path d="M-70 0q10 28 70 28t70-28" fill="none" class="a"/>
  <g class="goldd o"><circle cx="-26" cy="-8" r="12"/><circle cx="2" cy="-12" r="12"/><circle cx="30" cy="-6" r="12"/></g>
</g>
<g transform="translate(210 250)">
  <ellipse cx="0" cy="34" rx="80" ry="44" class="goldp o"/>
  <path d="M-56 70v22M-16 74v18M28 74v18M64 66v26" fill="none" stroke="{TONES['gold'][2]}" stroke-width="13" stroke-linecap="round"/>
  <path d="M-80 22q-44 4-46 46" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10" stroke-linecap="round"/>
  <g transform="translate(90 -6)">
    <path d="M-30-28q30-22 60 0 16 16 12 40-4 26-42 26t-42-26q-4-24 12-40z" class="goldp o"/>
    <path d="M20 36q30 6 44-8" fill="none" class="a"/>
    <path d="M-34-30q-20-34 4-36 20-2 22 22z" class="goldd o"/>
    <path d="M30-32q22-32 40-12 14 16-6 32z" class="goldd o"/>
    <circle cx="6" cy="-4" r="3.4" class="ink"/>
    <ellipse cx="42" cy="20" rx="9" ry="7" class="ink"/>
  </g>
</g>
<path d="M330 268q30 20 34 40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('fire', '私物の箱を抱えて職場の扉から出ていく人と、空になった机のイラスト。', f"""
<path d="M400 60h180v300H400z" fill="#e0d6c2" stroke="{INK}" stroke-width="3"/>
<path d="M400 60h30v300h-30z" class="goldd o"/>
<circle cx="452" cy="220" r="10" class="goldd"/>
<g transform="translate(150 250)">
  <path d="M-110-14h220v16h-220z" class="goldp o"/>
  <path d="M-96 2v84M96 2v84" fill="none" stroke="{TONES['gold'][2]}" stroke-width="11" stroke-linecap="round"/>
  <path d="M-70-14h140" class="a"/>
</g>
{person(300,360,1.0,1,'coral','blue','carry','short','sad')}
{box(300,282,110,70,0,'gold')}
<path d="M300 250v64" fill="none" stroke="{TONES['gold'][2]}" stroke-width="6"/>
<path d="M370 180h70" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('water', 'じょうろで花に水をやっているイラスト。水が細く注がれている。', f"""
<circle cx="480" cy="96" r="54" class="bluep"/>
<g transform="translate(160 210) rotate(30)">
  <path d="M-64-44h128l-12 100h-104z" class="tealp o"/>
  <path d="M-64-44h128" class="a"/>
  <path d="M64-34h56l30-22-86-8z" class="teal o"/>
  <path d="M-64-24q-44 12-32 56" fill="none" stroke="{INK}" stroke-width="9"/>
  <path d="M-30-64q34-14 68 0" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
</g>
<g stroke-linecap="round" fill="none">
  <path d="M292 196q34 44 40 96" stroke="{TONES['blue'][0]}" stroke-width="12"/>
  <path d="M300 194q34 46 40 98" stroke="#9dc6ea" stroke-width="5"/>
</g>
<g transform="translate(390 336)">
  <path d="M0 0v-90" fill="none" stroke="{TONES['green'][2]}" stroke-width="8" stroke-linecap="round"/>
  <path d="M0-40c-40-10-52-34-52-34 36-10 52 34 52 34z" class="green o"/>
  <g class="coralp o"><circle cx="-26" cy="-124" r="17"/><circle cx="26" cy="-124" r="17"/><circle cx="0" cy="-146" r="17"/><circle cx="-24" cy="-96" r="17"/><circle cx="24" cy="-96" r="17"/></g>
  <circle cx="0" cy="-120" r="15" class="gold o"/>
</g>
""", ground=True)

add('ankle', '足首の位置に印をつけた足元のイラスト。すねと足の境目にあたる。', f"""
<circle cx="450" cy="110" r="66" class="coralp"/>
<g transform="translate(270 200)">
  <path d="M-34-150q34-10 68 0l-8 150h-52z" fill="{TONES['blue'][0]}" stroke="{INK}" stroke-width="3"/>
  <path d="M-30 0h60v46h-60z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-30 46h60q54 6 76 46 6 12-10 12h-146q-16 0-16-16z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="0" cy="30" r="40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="11 9"/>
</g>
<path d="M410 240q-56 10-92 12" class="a" marker-end="url(#ar)"/>
<path d="M100 306h400" class="a"/>
""", ground=True, arrow=True)

add('applaud', '観客が手のひらを打ち合わせて拍手しているイラスト。', f"""
<circle cx="300" cy="130" r="96" class="goldp"/>
{person(160,336,1.0,1,'teal','blue','hold','short','smile')}
{person(300,336,1.05,1,'coral','gold','hold','bob','smile')}
{person(440,336,1.0,1,'violet','teal','hold','cap','smile')}
<g fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5">
  <ellipse cx="150" cy="264" rx="17" ry="24"/><ellipse cx="176" cy="264" rx="17" ry="24"/>
  <ellipse cx="288" cy="258" rx="18" ry="25"/><ellipse cx="316" cy="258" rx="18" ry="25"/>
  <ellipse cx="430" cy="264" rx="17" ry="24"/><ellipse cx="456" cy="264" rx="17" ry="24"/>
</g>
<g class="golds" opacity=".95" style="stroke-width:4">
  <path d="M128 244l-16-16M198 244l16-16M264 236l-18-18M340 236l18-18M408 244l-16-16M478 244l16-16"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('bin', 'ふたを開けたごみ箱に、丸めた紙くずを投げ入れているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="tealp"/>
<g transform="translate(300 306)">
  <path d="M-80-66h160l-16 136h-128z" class="tealp o"/>
  <path d="M-80-66h160" class="a"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3"><path d="M-56-36h112M-52 4h104M-46 44h92"/></g>
</g>
<g transform="translate(392 194) rotate(34)">
  <path d="M-90-11h180v22h-180z" class="teal o"/>
  <path d="M-8-11v-16h16v16z" class="a"/>
</g>
<g transform="translate(290 140)">
  <path d="M-26-8q-6-22 14-22 8-14 24-4 18-6 20 12 12 6 4 22-10 16-32 12-24 4-30-20z" fill="#fffdf6" stroke="{INK}" stroke-width="2.5"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2"><path d="M-12-14q10 10 22 4M-16 2q14 2 24-8"/></g>
</g>
<path d="M290 180v46" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('bind', 'ばらばらの棒を一束に集め、ひもをぐるぐる巻いて縛っているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="15" stroke-linecap="round">
  <path d="M90 120l420 40M96 190h410M104 260l400-40M120 320l380-90"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="13" stroke-linecap="round">
  <path d="M250 110q-46 66 0 132q46 66 0 132" transform="rotate(4 250 242)"/>
  <path d="M320 110q46 66 0 132q-46 66 0 132" transform="rotate(-4 320 242)"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M190 356q34-20 46-40"/><path d="M390 356q-30-20-40-40"/></g>
""", ground=True, arrow=True)
print(' '.join(W)); print(sheet(W))
