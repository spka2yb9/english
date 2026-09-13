"""第27回: 修理・交換・共有・解決など30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('remains', '崩れた柱だけが残る、古い遺跡のイラスト。', f"""
<g fill="#cfc7b8" stroke="{INK}" stroke-width="3">
  <path d="M110 340V190h40v150z"/><path d="M210 340V230h40v110z"/><path d="M350 340V170h40v170z"/><path d="M450 340V250h40v90z"/>
</g>
<path d="M80 340h440" class="a"/>
<g fill="#cfc7b8" stroke="{INK}" stroke-width="2.5"><path d="M280 340q12-30 42-20t18 20z"/></g>
""", ground=True)

add('remind', 'ひもを指に結んで、用事を思い出させるイラスト。', f"""
{person(190,346,1.15,1,'teal','blue','point','short','neutral')}
<g transform="translate(300 232)">
  <circle r="15" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-16 0q16 12 32 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
<g transform="translate(430 190)">
  <path d="M-70-46q-12-48 40-56 16-38 72-26 32 6 40 34 54-6 58 44 2 40-46 44h-134q-32-4-30-40z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-30-30h70M-30-8h50"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('repair', '壊れたいすを工具で直しているイラスト。', f"""
<g transform="translate(320 290)">
  <path d="M-90-20h180v18h-180z" class="goldp o"/>
  <path d="M-80 0v50M80 0v50" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M70-20v-100h18v100z" class="goldd o"/>
</g>
{hand(180,220,1)}
<g transform="translate(250 240) rotate(-20)">
  <path d="M-44-20h88v26h-88z" class="goldd o"/>
  <path d="M0 6v40" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 180l18 18 30-36"/></g>
""", ground=True)

add('repeat', '同じ動きが、輪になって何度もくり返されるイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="14" stroke-linecap="round">
  <path d="M300 110a130 130 0 0 1 112 194" marker-end="url(#ar)"/>
  <path d="M412 304a130 130 0 0 1-224 0" marker-end="url(#ar)"/>
  <path d="M188 304a130 130 0 0 1 112-194" marker-end="url(#ar)"/>
</g>
<g transform="translate(300 210)"><path d="M-40-24h80v48h-80z" class="tealp o"/></g>
""", ground=False, arrow=True)

add('replace', '古い電球を外して、新しい電球に取り替えるイラスト。', f"""
<g transform="translate(170 250)" opacity=".5">
  <circle r="50" class="muted"/>
  <path d="M-20 50h40v20h-40z" class="ink"/>
</g>
<g transform="translate(430 250)">
  <circle r="50" class="goldp o"/>
  <path d="M-20 50h40v20h-40z" class="ink"/>
  <g class="golds" style="stroke-width:4"><path d="M0-66v-16M-44-40l-14-10M44-40l14-10"/></g>
</g>
<path d="M250 250h100" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:7"><path d="M150 350l40 40M190 350l-40 40"/></g>
""", ground=True, arrow=True)

add('reporting', '現場から出来事を伝えている報道のイラスト。', f"""
{building(430,300,0.7,'teal')}
{person(180,346,1.15,1,'coral','blue','hold','bob','neutral')}
<g transform="translate(230 250)"><path d="M-16-14h32v28h-32z" class="ink"/><path d="M16-4l50-24v48z" class="ink" opacity=".8"/></g>
<g class="corals" opacity=".85" style="stroke-width:4"><path d="M310 210q26 26 26 40M330 190q34 34 34 56"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('represent', '一人が集団を代表して、前に立っているイラスト。', f"""
{person(180,346,1.2,1,'coral','blue','point','cap','neutral')}
<g opacity=".55">
  {person(370,346,0.85,1,'teal','gold','stand','short','neutral')}
  {person(450,346,0.85,1,'violet','teal','stand','bob','neutral')}
  {person(530,346,0.85,1,'gold','blue','stand','cap','neutral')}
</g>
<path d="M320 220h-60" class="a" marker-end="url(#ar)"/>
<circle cx="180" cy="230" r="56" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('require', 'これがないと通れない、必要な札を示したイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-140-100h30v200h-30zM110-100h30v200h-30z" class="goldd o"/>
  <path d="M-110-20h220v40h-220z" class="coral o"/>
</g>
{person(120,346,0.95,1,'teal','blue','stand','short','neutral')}
<g transform="translate(430 190)">
  <path d="M-50-30h100v60h-100z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-30-8h60M-30 8h40"/></g>
</g>
<path d="M380 250h-60" class="a" marker-end="url(#ar)" transform="rotate(180 350 250)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('resort', '海辺の行楽地で、パラソルの下でくつろぐイラスト。', f"""
<path d="M0 250h600v150H0z" class="bluep"/>
<path d="M0 250h340v150H0z" fill="#efdcb8" stroke="{INK}" stroke-width="3"/>
<g transform="translate(180 250)">
  <path d="M-90 0a90 60 0 0 1 180 0z" class="coral o"/>
  <path d="M0 0v90" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
{person(180,340,0.7,1,'teal','gold','hold','bob','smile')}
{sun(500,100,44)}
""", ground=False)

add('respond', '呼びかけに対して、返事の吹き出しが返るイラスト。', f"""
{person(160,346,1.1,1,'teal','blue','stand','short','neutral')}
{person(450,346,1.1,-1,'coral','gold','stand','bob','smile')}
<g transform="translate(250 190)">
  <path d="M-50-30h100q12 0 12 12v28q0 12-12 12h-70l-18 16 4-16q-12 0-12-12v-28q0-12 12-12z" class="paper"/>
</g>
<g transform="translate(370 250)">
  <path d="M50-30H-50q-12 0-12 12v28q0 12 12 12h70l18 16-4-16q12 0 12-12v-28q0-12-12-12z" class="tealp o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('retire', '長年の仕事を終えて、職場を離れるイラスト。', f"""
{building(150,300,0.8,'teal')}
{person(380,346,1.15,1,'gold','blue','walk','short','smile')}
<path d="M260 240h80" class="a" marker-end="url(#ar)"/>
<g transform="translate(480 210)">
  <circle r="34" class="goldp o"/>
  <path d="M0 0v-20M0 0l16 10" class="a"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('reunion', '久しぶりに会った人たちが、集まって喜ぶイラスト。', f"""
<circle cx="300" cy="150" r="90" class="goldp" opacity=".5"/>
{person(180,346,1.1,1,'teal','blue','up','short','smile')}
{person(300,346,1.1,1,'coral','gold','up','bob','smile')}
{person(420,346,1.1,-1,'violet','teal','up','cap','smile')}
<g class="golds" style="stroke-width:4"><path d="M120 200l-24-24M480 200l24-24"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('ritual', '決まった順序でろうそくを灯す、儀式のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-180-20h360v20h-360z" class="goldp o"/>
  {''.join(f'<g transform="translate({-120+i*60} -30)"><path d="M-10-40h20v40h-20z" fill="#fffdf6" stroke="{INK}" stroke-width="2.5"/><path d="M0-40q10-16 0-26-10 10 0 26z" class="gold o"/></g>' for i in range(5))}
</g>
{person(300,240,0.7,1,'violet','violet','hold','short','neutral')}
<path d="M60 360h480" class="a"/>
""", ground=True)

add('rival', '同じ目標を狙って、張り合う二人のイラスト。', f"""
<g transform="translate(300 130)">
  <circle r="50" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <circle r="32" class="goldp o"/><circle r="12" class="gold o"/>
</g>
{person(170,346,1.15,1,'teal','blue','reach','short','neutral')}
{person(430,346,1.15,-1,'coral','gold','reach','cap','neutral')}
<g class="corals" style="stroke-width:5"><path d="M240 250l40-60M360 250l-40-60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('roll', 'ボールが坂を転がって下りていくイラスト。', f"""
<path d="M60 140L540 330H60z" class="tealp o"/>
<path d="M60 140L540 330" class="a"/>
<g opacity=".4"><circle cx="180" cy="200" r="34" class="coral o"/></g>
<g opacity=".7"><circle cx="300" cy="250" r="34" class="coral o"/></g>
<circle cx="430" cy="300" r="34" class="coral o"/>
<path d="M180 130a80 80 0 0 1 60 30" class="muted" marker-end="url(#ar)"/>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('rose', 'とげのある茎に、赤い花をつけたバラのイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M0 60V-60" fill="none" stroke="{TONES['green'][2]}" stroke-width="9" stroke-linecap="round"/>
  <path d="M0-10c-40-10-52-34-52-34 36-10 52 34 52 34z" class="green o"/>
  <path d="M0 20c40-10 52-34 52-34-36-10-52 34-52 34z" class="green o"/>
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="4"><path d="M0 10l-14-8M0 40l14-8"/></g>
  <g transform="translate(0 -90)">
    <circle r="46" class="coral o"/>
    <path d="M0-30a30 30 0 1 1 0 60 22 22 0 1 0 0-44 14 14 0 1 1 0 28" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"/>
  </g>
</g>
""", ground=True)

add('safe', 'ヘルメットをかぶって、危険から守られているイラスト。', f"""
{person(280,346,1.25,1,'teal','blue','stand','short','smile')}
<g transform="translate(280 216)">
  <path d="M-34 0a34 30 0 0 1 68 0z" class="gold o"/>
  <path d="M-38 0h76v10h-76z" class="goldd o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M440 220l20 20 34-40"/></g>
<g class="muted"><path d="M120 160v40M160 140v40"/></g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('sake', 'ある目的のために、行動を選んでいるイラスト。', f"""
{person(160,346,1.1,1,'teal','blue','point','short','neutral')}
<g transform="translate(440 220)">
  <circle r="70" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 30l-30-36 14-16 16 14 16-14 14 16z" class="coral o"/>
</g>
<path d="M240 240h120" class="a" marker-end="url(#ar)" style="stroke-width:6"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('satisfaction', '望んだ結果が得られて、満ち足りているイラスト。', f"""
{face(240,200,110,'smile')}
<g transform="translate(450 230)">
  <path d="M-70-60h140v120h-140z" class="paper"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M-30 0l20 20 36-44"/></g>
</g>
<g class="golds" style="stroke-width:4"><path d="M150 110l-24-24M330 110l24-24"/></g>
""", ground=False)

add('scale', '目盛りのついた定規と、規模を示す大小の丸のイラスト。', f"""
<g transform="translate(300 170)">
  <path d="M-220-24h440v48h-440z" class="goldp o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">{''.join(f'<path d="M{-200+i*40} -24v{20 if i%2 else 30}"/>' for i in range(11))}</g>
</g>
<circle cx="160" cy="300" r="26" class="tealp o"/>
<circle cx="300" cy="300" r="42" class="teal o"/>
<circle cx="460" cy="300" r="58" class="teald o"/>
""", ground=False)

add('scary', '暗がりから伸びる大きな影に、おびえているイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#3a4a5c"/>
{person(200,350,1.15,1,'coral','blue','up','short','sad')}
<g fill="#22303e" stroke="#556777" stroke-width="3"><path d="M400 350q-30-100 40-140 60-34 100 20 40 54-20 120z"/></g>
<g fill="#f7e6a8"><circle cx="450" cy="230" r="9"/><circle cx="500" cy="230" r="9"/></g>
""", ground=False)

add('set', 'ばらばらの部品を組み立てて、一つの形にするイラスト。', f"""
<g transform="translate(140 230)">
  <path d="M-50-40h50v50h-50z" class="teal o"/><path d="M10 10h50v50H10z" class="gold o"/>
</g>
<g transform="translate(420 240)">
  <path d="M-70-70h140v140h-140z" fill="#fffdf6" class="o"/>
  <path d="M-70-70h70v70h-70z" class="teal o"/>
  <path d="M0 0h70v70H0z" class="gold o"/>
</g>
<path d="M250 230h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('share', '一つのケーキを切り分けて、二人で分け合うイラスト。', f"""
<g transform="translate(300 250)">
  <g class="goldp o">
    <path d="M-10-8L-140-58a140 140 0 0 0 0 100z"/>
    <path d="M-4-16L-134-66a140 140 0 0 1 124-72z"/>
    <path d="M10-16l130-50a140 140 0 0 0-124-72z"/>
    <path d="M14-8l130-50a140 140 0 0 1 0 100z"/>
  </g>
  <path d="M-6-12L-146-66M6-12l140-54M0-18v-124M0-6v112" fill="none" stroke="{INK}" stroke-width="3" stroke-dasharray="9 8"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M130 340h-60"/><path d="M470 340h60"/></g>
""", ground=True, arrow=True)

add('shelter', '雨風をしのげる屋根の下に、身を寄せているイラスト。', f"""
<g class="blues" opacity=".9"><path d="M80 40l-10 30M180 60l-10 30M420 40l-10 30M520 60l-10 30"/></g>
<g transform="translate(300 250)">
  <path d="M-160-40h320v20h-320z" class="teal o"/>
  <path d="M-176-40L0-120l176 80z" class="teald o"/>
  <path d="M-150-20v130M150-20v130" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"/>
</g>
{person(300,346,0.95,1,'coral','blue','stand','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('shipping', '荷物を積んだ船が、港から出て行くイラスト。', f"""
<path d="M0 250h600v150H0z" class="bluep"/>
<path d="M0 250h160v150H0z" class="ground"/>
<path d="M0 250h160" class="a"/>
{box(80,230,70,50,0,'gold')}
<g transform="translate(380 250)">
  <path d="M-130 0h260l-28 40h-204z" class="teal o"/>
  <path d="M-130 0h260" class="a"/>
  <g class="goldp o"><rect x="-90" y="-44" width="54" height="44"/><rect x="-26" y="-44" width="54" height="44"/><rect x="-90" y="-92" width="54" height="44"/></g>
  <path d="M50 0v-50h70v50z" class="paper"/>
</g>
<path d="M200 180h280" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('shore', '波が打ち寄せる岸のふちを示したイラスト。', f"""
<path d="M0 200h600v200H0z" class="bluep"/>
<path d="M0 260q120 20 240-10t360 10v140H0z" fill="#efdcb8" stroke="{INK}" stroke-width="3"/>
<g class="blues" opacity=".8"><path d="M40 200q50-14 100 0t100 0M340 220q50-14 100 0t100 0"/></g>
<path d="M300 350v-60" class="a" marker-end="url(#ar)" transform="rotate(180 300 320)"/>
""", ground=False, arrow=True)

add('shortage', '必要な数に足りず、棚に空きが残るイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-200-20h400v20h-400z" class="goldp o"/>
  <g class="tealp o">{''.join(f'<rect x="{-180+i*70}" y="-80" width="54" height="60"/>' for i in range(3))}</g>
  <g class="muted">{''.join(f'<rect x="{40+i*70}" y="-80" width="54" height="60"/>' for i in range(3))}</g>
</g>
<g class="corals" style="stroke-width:7"><path d="M470 130l30 30M500 130l-30 30"/></g>
""", ground=True)

add('simple', '飾りのない単純な形と、複雑な形を比べたイラスト。', f"""
<g transform="translate(170 230)">
  <circle r="80" class="tealp o"/>
</g>
<g transform="translate(430 230)">
  <circle r="80" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3">
    <circle r="58"/><circle r="36"/><circle r="16"/>
    <path d="M-80 0h160M0-80v160M-56-56l112 112M56-56L-56 56"/>
  </g>
</g>
<path d="M300 130v200" class="muted"/>
""", ground=True)

add('simulation', '実物の代わりに、画面の中で試している模擬実験のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-170-120h340v240h-340z" fill="#dfe6ea" class="o"/>
  <path d="M-140-90h280v180h-280z" class="bluep o"/>
  <g transform="translate(0 10) scale(0.5)">
    <path d="M-150 40h300l-16-56h-50l-34-56h-120l-34 56h-62z" class="coral o"/>
    <circle cx="-84" cy="48" r="30" class="ink"/><circle cx="84" cy="48" r="30" class="ink"/>
  </g>
  <g fill="none" stroke="#ffffff" stroke-width="3" stroke-dasharray="10 8"><path d="M-140 60h280"/></g>
</g>
""", ground=True)

add('sincerity', '胸に手を当てて、真心を示しているイラスト。', f"""
<circle cx="300" cy="140" r="76" class="coralp"/>
<g transform="translate(300 176)"><path d="M0 30l-34-42 16-20 18 18 18-18 16 20z" class="coral o"/></g>
{person(300,346,1.3,1,'teal','blue','hold','bob','smile')}
<circle cx="300" cy="266" r="16" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('skull', '頭の骨の形を示したイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M0-110q90 0 90 90 0 40-24 60v40q0 20-26 20h-80q-26 0-26-20v-40q-24-20-24-60 0-90 90-90z" fill="#f7f2ea" stroke="{INK}" stroke-width="3"/>
  <ellipse cx="-32" cy="-14" rx="20" ry="24" fill="{INK}"/>
  <ellipse cx="32" cy="-14" rx="20" ry="24" fill="{INK}"/>
  <path d="M0 10l-12 26h24z" fill="{INK}"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><path d="M-30 60h60M-14 60v30M14 60v30"/></g>
</g>
""", ground=True)

add('slow', '速い動きが、だんだん遅くなっていくイラスト。', f"""
<g transform="translate(160 250)">
  <circle r="76" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0l52-42" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round"/>
</g>
<g transform="translate(430 250)">
  <circle r="76" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0l-48-46" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round"/>
</g>
<path d="M270 250h50" class="a" marker-end="url(#ar)"/>
<g class="muted"><path d="M120 360h100M400 360h40"/></g>
""", ground=False, arrow=True)

add('solve', '入り組んだ迷路の出口を見つけて、線を通すイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-160-120h320v240h-320z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="6">
    <path d="M-120-80h100v60h-160M-40-80v120h120v-80h60"/>
    <path d="M60 40v40h-140"/>
  </g>
  <path d="M-160-60h40q40 0 40 40t40 40h60q40 0 40-40t40-40h60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="12 8"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M500 330l18 18 30-36"/></g>
""", ground=True)
print(' '.join(W)); print(sheet(W))
