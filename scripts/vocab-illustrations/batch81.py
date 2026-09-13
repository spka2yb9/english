"""第81回: 保険・気づき・宝石・沿岸・枠組など45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'
def house(x,y,s=1,cls='gold'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-60 0v-70h120V0z" fill="#fffdf6" class="o"/>'
            f'<path d="M-74-70L0-126l74 56z" class="{cls} o"/>'
            f'<rect x="-18" y="-46" width="36" height="46" class="{cls}d o"/>'
            f'<rect x="-48" y="-56" width="24" height="22" class="{cls}p o"/>'
            f'<rect x="24" y="-56" width="24" height="22" class="{cls}p o"/></g>')

add('cover', '家と車をまとめて覆う保険のイラスト。', f"""
<path d="M110 210q190-130 380 0z" class="bluep o"/>
<path d="M110 210h380" class="a"/>
{house(230,300,0.9)}
<g transform="translate(420 286)">
  <path d="M-64 0v-30l18-26h80l20 26V0z" class="teal o"/>
  <g fill="#fffdf6" class="o"><rect x="-40" y="-50" width="36" height="22"/><rect x="6" y="-50" width="36" height="22"/></g>
  <g fill="{INK}"><circle cx="-36" cy="4" r="13"/><circle cx="38" cy="4" r="13"/></g>
</g>
{ck(300,150,1.1)}
<path d="M60 340h480" class="a"/>
""", ground=True)

add('realize', 'はっと気づいて頭にひらめきがともるイラスト。', f"""
{person(200,350,1.2,1,'teal','blue','think','short','surprised')}
<g transform="translate(400 170)">
  <path d="M0-70q46 0 46 44 0 26-20 38v18h-52v-18q-20-12-20-38 0-44 46-44z" class="gold o"/>
  <path d="M-26 34h52v16h-52z" class="goldd o"/>
  <g class="golds"><path d="M-78-40l-26-12M78-40l26-12M0-100v-26"/></g>
</g>
<g fill="{INK}"><circle cx="278" cy="216" r="7"/><circle cx="300" cy="192" r="10"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('brilliant', 'きらめくようにカットされた宝石のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-110-50h220l-110 140z" class="tealp o"/>
  <path d="M-110-50l38-46h144l38 46z" class="teal o"/>
  <g fill="none" stroke="{INK}" stroke-width="2.5">
    <path d="M-72-96l-10 46M72-96l10 46M0-96v46M-110-50L0 90 110-50M-40-50L0 90 40-50"/>
  </g>
</g>
<g class="golds"><path d="M130 120l-22-26M470 120l22-26M300 98v-34M120 240h-34M514 240h34"/></g>
""", ground=False)

add('raid', '大勢が一気に押し入る襲撃のイラスト。', f"""
<g transform="translate(470 250)">
  <path d="M-70-110h140v110h-140z" fill="#fffdf6" class="o"/>
  <path d="M-40-84h80v84h-80z" class="bluep o"/>
  <circle cx="26" cy="-44" r="6" class="ink"/>
</g>
{person(120,350,1.05,1,'coral','blue','walk','cap','neutral')}
{person(220,350,1.05,1,'coral','blue','walk','cap','neutral')}
{person(310,350,1.05,1,'coral','blue','walk','cap','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M350 210h50"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('actually', '思っていたことと実際のことを比べるイラスト。', f"""
<g transform="translate(170 180)">
  <path d="M-96-16q-6-40 30-44 14-30 46-18 26-4 32 24 30 4 26 34-4 26-32 26h-70q-28-2-32-22z" class="bluep o"/>
  <circle cx="-10" cy="8" r="28" class="coral o"/>
</g>
{xx(170,290,0.9)}
<g transform="translate(430 180)">
  <path d="M-100-70h200v150h-200z" class="paper"/>
  <path d="M-40-10h80v70h-80z" class="teal o"/>
  <circle cx="0" cy="-36" r="24" class="tealp o"/>
</g>
{ck(430,300,1.1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M300 80v240"/></g>
""", ground=False)

add('appealing', '思わず心を引かれる魅力的なもののイラスト。', f"""
<g transform="translate(390 250)">
  <path d="M-80 40h160v22h-160z" class="goldd o"/>
  <path d="M-80-20h160v60h-160z" class="gold o"/>
  <path d="M-80-20q40-40 80-14 40-26 80 14z" class="coralp o"/>
  <circle cx="0" cy="-44" r="14" class="coral o"/>
</g>
{person(140,350,1.15,1,'teal','blue','reach','bob','smile')}
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M230 170q-14-18 0-26 14-8 14 10 0-18 14-10 14 8 0 26l-14 14z"/>
  <path d="M282 130q-10-13 0-19 10-6 10 7 0-13 10-7 10 6 0 19l-10 10z"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('empirical', '実際に試して確かめる実証のイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-30-90h60v40l40 90q6 14-10 14h-120q-16 0-10-14l40-90z" fill="#fffdf6" class="o"/>
  <path d="M-52 10l-14 30q-6 14 10 14h112q16 0 10-14l-14-30z" class="teal o"/>
  <circle cx="-14" cy="-20" r="7" class="tealp o"/><circle cx="16" cy="-46" r="6" class="tealp o"/>
</g>
<g transform="translate(440 240)">
  <path d="M-90-80h180v160h-180z" class="paper"/>
  <g class="teal"><rect x="-60" y="0" width="26" height="50"/><rect x="-20" y="-30" width="26" height="80"/><rect x="20" y="-56" width="26" height="106"/></g>
  <path d="M-66-56h60" class="a"/>
</g>
<path d="M270 240h60" class="a" marker-end="url(#ar)"/>
{ck(440,190,0.9)}
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('light', '暗がりに光を投げかけるランプのイラスト。', f"""
<path d="M300 70v26" class="a"/>
<g transform="translate(300 160)">
  <path d="M-56-64h112l26 64h-164z" class="gold o"/>
  <circle cx="0" cy="24" r="26" class="goldp o"/>
</g>
<path d="M216 190L120 330h360L384 190z" fill="{TONES['gold'][1]}" opacity="0.7"/>
{person(300,346,1,1,'teal','blue','stand','short','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('home', '帰る場所としての家のイラスト。', f"""
{house(280,320,1.5)}
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2.5">
  <path d="M460 150q-22-28 0-40 22-12 22 16 0-28 22-16 22 12 0 40l-22 22z"/>
</g>
<path d="M60 344h480" class="a"/>
""", ground=True)

add('pay', 'お金を払って受け取るイラスト。', f"""
{person(140,350,1.1,1,'teal','blue','give','short','smile')}
<g transform="translate(300 220)">
  <path d="M-56-30h112v60h-112z" class="greenp o"/>
  <circle r="16" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="3"><circle cx="300" cy="220" r="9"/></g>
{person(470,350,1.1,-1,'coral','gold','give','bob','smile')}
<path d="M240 300h120" class="a" marker-end="url(#ar)"/>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('pop', '大勢に受ける流行歌のイラスト。', f"""
<g transform="translate(290 200)">
  <path d="M-90 60q-26 0-26-20t26-20q14 0 20 8V-70l80-22v34l-56 16v90q0 22-26 22z" class="coral o"/>
</g>
<g class="golds"><path d="M120 120l-24-22M460 120l24-22M290 66v-28M110 250H80M470 250h30"/></g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2">
  <path d="M470 190l12 26 28 4-20 20 5 28-25-14-25 14 5-28-20-20 28-4z"/>
</g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('shy', '数がひとつ足りず欠けているイラスト。', f"""
<g transform="translate(300 230)">
  <g class="teal o">{''.join(f'<rect x="{-200+i*80}" y="-36" width="64" height="72"/>' for i in range(4))}</g>
  <path d="M120-36h64v72h-64z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"/>
</g>
{xx(452,150,0.8)}
<path d="M60 340h480" class="a"/>
""", ground=True)

add('attraction', '人を引きつける観光名所のイラスト。', f"""
<g transform="translate(300 190)">
  <path d="M-50 110L-14-70h28l36 180z" class="teal o"/>
  <path d="M-14-70l14-50 14 50z" class="tealp o"/>
  <path d="M-34 30h68" class="a"/>
</g>
{person(120,368,0.85,1,'coral','gold','stand','bob','smile')}
{person(480,368,0.85,-1,'violet','blue','stand','short','smile')}
<g class="a" marker-end="url(#ar)"><path d="M172 340h36M428 340h-36"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('biological', '顕微鏡でのぞいた生き物の細胞のイラスト。', f"""
<g transform="translate(430 240)">
  <circle r="106" fill="#fffdf6" class="o"/>
  <circle r="88" class="greenp"/>
  <circle cx="-24" cy="-14" r="30" class="green o"/>
  <circle cx="36" cy="30" r="22" class="green o"/>
  <circle cx="30" cy="-42" r="14" class="teal o"/>
</g>
<g transform="translate(150 260)">
  <path d="M-60 80h120v20h-120z" class="ink"/>
  <path d="M-30 80v-40h20v40z" class="o" fill="{MUTED}"/>
  <path d="M-16-90h44v50h-44z" class="teal o"/>
  <path d="M-6-110h24v20h-24z" class="teald o"/>
  <path d="M-16-40h44l-10 40h-24z" class="tealp o"/>
</g>
<path d="M250 200h60" class="a" marker-end="url(#ar)"/>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('biology', '植物と生き物を調べる生物学のイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-90-80h180v160h-180z" class="paper"/>
  <path d="M0 50v-70" class="greens"/>
  <path d="M0-20q-46-4-50-44 44-4 50 44z" class="greenp o"/>
  <path d="M0-34q46-4 50-44-44-4-50 44z" class="green o"/>
</g>
<g transform="translate(430 250)">
  <path d="M-90-80h180v160h-180z" class="paper"/>
  <ellipse cx="-14" cy="10" rx="56" ry="34" class="bluep o"/>
  <path d="M42 10l40-26v52z" class="blue o"/>
  <circle cx="-46" cy="2" r="5" class="ink"/>
  <g fill="none" stroke="{TONES['blue'][2]}" stroke-width="2.5"><path d="M-30-24v-16M0-20v-14"/></g>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('bitter', '苦い味に顔をしかめるイラスト。', f"""
{face(180,200,88,'sad')}
<g fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"><path d="M136 140l30 10M224 140l-30 10"/></g>
<g transform="translate(430 220)">
  <path d="M-56-60h112l-14 100q-2 20-42 20t-42-20z" fill="#fffdf6" class="o"/>
  <path d="M-50-20h100l-8 60q-2 20-42 20t-42-20z" class="greend o"/>
</g>
<g class="golds"><path d="M300 150l-30 16M300 200l-30 0"/></g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('clinical', 'ベッドの患者を診る臨床のイラスト。', f"""
<g transform="translate(230 290)">
  <path d="M-130 20h260v16h-260z" class="ink"/>
  <path d="M-130-20h260v40h-260z" fill="#fffdf6" class="o"/>
  <path d="M-130-56h50v36h-50z" class="bluep o"/>
  <ellipse cx="-96" cy="-66" rx="20" ry="16" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-76-20h190v-22q0-14-16-14H-60q-16 0-16 14z" class="teal o"/>
  <path d="M-130 36v30M118 36v30" class="a"/>
</g>
{person(470,346,1.1,-1,'violet','blue','reach','bun','neutral')}
<g transform="translate(500 180)">
  <path d="M-44-50h88v100h-88z" class="paper"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3"><path d="M-26-24h52M-26 0h52M-26 24h30"/></g>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('cloth', 'たたんだ布地のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-150-70h300v110q-40 26-76 0-38 26-76 0-38 26-72 0z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3">
    {''.join(f'<path d="M{-130+i*40} -70v100"/>' for i in range(7))}
    <path d="M-150-40h300M-150-10h300"/>
  </g>
  <path d="M-150-70h300v34h-300z" class="teal o"/>
</g>
<path d="M60 330h480" class="a"/>
""", ground=True)

add('coastal', '海に沿った沿岸の町のイラスト。', f"""
<path d="M0 240h600v160H0z" class="bluep"/>
<path d="M0 240q120-36 230 10 120 50 370 10v-90H0z" fill="#fffaf1"/>
<path d="M0 240q120-36 230 10 120 50 370 10" class="a"/>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3">
  <path d="M60 320q30-16 60 0t60 0M300 350q30-16 60 0t60 0M420 300q30-16 60 0t60 0"/>
</g>
{house(90,196,0.6)}
{house(200,214,0.6)}
<circle cx="470" cy="120" r="40" class="goldp o"/>
""", ground=False)

add('cognitive', '頭の中で考えが働く認知のイラスト。', f"""
<g transform="translate(290 230)">
  <path d="M-30 120v-40q-70-16-70-90 0-90 90-90 92 0 92 86 0 44-36 62v72z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g transform="translate(300 180)">
  <circle r="52" class="goldp o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="4">
    <circle r="20"/><path d="M0-52v-14M0 52v14M-52 0h-14M52 0h14M-38-38l-10-10M38 38l10 10M38-38l10-10M-38 38l-10 10"/>
  </g>
</g>
<g class="golds"><path d="M400 120l26-16M420 180h28"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('colleague', '同じ職場で机を並べる同僚のイラスト。', f"""
{person(180,300,1,1,'teal','blue','stand','short','smile')}
{person(400,300,1,-1,'coral','gold','stand','bob','smile')}
<g transform="translate(300 330)">
  <path d="M-200-24h400v20h-400z" class="goldd o"/>
  <path d="M-170-4v52M170-4v52" class="a"/>
</g>
<g transform="translate(180 246)"><path d="M-36-24h72v48h-72z" class="paper"/></g>
<g transform="translate(400 246)"><path d="M-36-24h72v48h-72z" class="paper"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('collection', '棚に集めてしならべた収蔵品のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-110h400v230h-400z" fill="#fffdf6" class="o"/>
  <path d="M-200-30h400M-200 40h400" class="a"/>
  <circle cx="-130" cy="-64" r="34" class="teal o"/>
  <path d="M-40-98h70v68h-70z" class="coral o"/>
  <path d="M80-98l40 68H40z" class="gold o"/>
  <circle cx="-120" cy="8" r="30" class="violetp o"/>
  <path d="M-30-24h80v56h-80z" class="greenp o"/>
  <circle cx="110" cy="4" r="34" class="goldp o"/>
  <path d="M-160 62h60v52h-60zM-60 62h60v52h-60zM40 62h60v52H40z" class="bluep o"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('collective', '大勢が輪になってひとつになる集団のイラスト。', f"""
{person(130,330,0.8,1,'teal','blue','up','short','smile')}
{person(250,330,0.8,1,'coral','gold','up','bob','smile')}
{person(370,330,0.8,1,'violet','blue','up','short','smile')}
{person(490,330,0.8,1,'green','gold','up','bun','smile')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="10 8"><ellipse cx="310" cy="250" rx="250" ry="130"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('colonial', '大きな国が遠くの土地を支配する植民地のイラスト。', f"""
<g transform="translate(140 250)">
  <path d="M-90 60q0-90 90-90t90 90z" class="teal o"/>
  <path d="M-20-30v-80h4l60 22-60 22" class="ink"/>
</g>
<g transform="translate(470 280)">
  <ellipse rx="90" ry="30" class="greenp o"/>
  <path d="M-10 0v-70h4l50 18-50 18" class="ink"/>
</g>
<path d="M250 210h130" class="a" marker-end="url(#ar)"/>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('colourful', '色とりどりで華やかなもののイラスト。', f"""
<g transform="translate(300 210)">
  <circle cx="-170" cy="-20" r="48" class="coral o"/>
  <circle cx="-58" cy="-56" r="48" class="gold o"/>
  <circle cx="58" cy="-30" r="48" class="teal o"/>
  <circle cx="170" cy="-64" r="48" class="violet o"/>
  <circle cx="-110" cy="60" r="42" class="green o"/>
  <circle cx="10" cy="76" r="42" class="blue o"/>
  <circle cx="130" cy="52" r="42" class="coralp o"/>
</g>
<g class="golds"><path d="M300 60v-26M110 104l-20-20M500 90l22-20"/></g>
""", ground=False)

add('combination', 'ふたつを合わせてひとつにする組み合わせのイラスト。', f"""
<g transform="translate(140 240)">
  <path d="M-56-56h112v112h-112z" class="teal o"/>
</g>
<g transform="translate(320 240)">
  <circle r="56" class="coral o"/>
</g>
<path d="M212 240h38M392 240h30" class="a" marker-end="url(#ar)"/>
<g transform="translate(500 240)">
  <path d="M-56-56h112v112h-112z" class="tealp o"/>
  <circle r="40" class="coral o"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('feel', '手で触れて感じ取るイラスト。', f"""
{hand(200,220,1)}
<g transform="translate(430 230)">
  <path d="M-70-70h140v140h-140z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="4">{''.join(f'<path d="M-70 {-46+i*30}q34-20 68 0t70 0"/>' for i in range(5))}</g>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M296 180q16 16 0 32M322 166q30 30 0 60M348 152q44 44 0 88"/>
</g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('force', '力いっぱい押して動かすイラスト。', f"""
{person(160,350,1.15,1,'coral','blue','reach','short','neutral')}
{box(390,290,150,110,30,'gold')}
<g class="a" marker-end="url(#ar)"><path d="M300 230h60"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round"><path d="M480 250l26-16M486 300h30M480 350l26 16"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('forever', '終わりなく続く永遠のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M0 0q-40-70-96-70T-192 0q0 70 96 70T0 0q40-70 96-70T192 0q0 70-96 70T0 0z" class="teals" fill="none"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round" marker-end="url(#ar)">
  <path d="M260 330q40 26 80 0"/>
</g>
<path d="M60 370h480" class="a"/>
""", ground=True, arrow=True)

add('format', '決まった体裁で整えられた書式のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-130-150h260v300h-260z" class="paper"/>
  <path d="M-90-116h180v30h-180z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-90 {-56+i*28}h180"/>' for i in range(5))}</g>
  <path d="M-90 96h80v40h-80z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3" stroke-dasharray="8 7">
  <path d="M148 60h40M148 296h40M148 60v236"/>
</g>
""", ground=False)

add('formation', 'ばらばらな部品が組み上がって形になるイラスト。', f"""
<g transform="translate(120 250)">
  <path d="M-40-40h40v40h-40z" class="tealp o"/>
  <path d="M14 10h40v40h-40z" class="tealp o" transform="rotate(20 34 30)"/>
  <path d="M-46 22h40v40h-40z" class="tealp o" transform="rotate(-14 -26 42)"/>
</g>
<g transform="translate(310 250)">
  <path d="M-40-40h40v40h-40z" class="teal o"/>
  <path d="M0-40h40v40H0z" class="teal o"/>
  <path d="M-24 12h40v40h-40z" class="tealp o" transform="rotate(12 -4 32)"/>
</g>
<g transform="translate(490 250)">
  <path d="M-40-40h80v80h-80z" class="teal o"/>
  <path d="M-40 0h80M0-40v80" class="a"/>
</g>
<path d="M200 250h34M382 250h34" class="a" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('fortune', '金貨があふれる宝箱のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-130 10h260v90h-260z" class="goldd o"/>
  <path d="M-130 10q0-70 130-70t130 70z" class="gold o"/>
  <path d="M-130 10h260" class="a"/>
  <path d="M-20 30h40v40h-40z" class="goldp o"/>
</g>
<g class="gold o">
  <ellipse cx="200" cy="316" rx="26" ry="12"/><ellipse cx="250" cy="330" rx="26" ry="12"/>
  <ellipse cx="400" cy="316" rx="26" ry="12"/><ellipse cx="350" cy="332" rx="26" ry="12"/>
</g>
<g class="golds"><path d="M140 130l-20-20M470 130l22-20M300 116v-26"/></g>
<path d="M60 360h480" class="a"/>
""", ground=True)

add('forum', '意見を出し合う話し合いの場のイラスト。', f"""
{person(130,330,0.85,1,'teal','blue','stand','short','smile')}
{person(300,340,0.85,1,'coral','gold','stand','bob','smile')}
{person(470,330,0.85,-1,'violet','blue','stand','bun','smile')}
<g transform="translate(130 160)"><path d="M-56-34h112v56h-112zM-30 22l-10 22 30-22z" fill="#fffdf6" class="o"/><g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3"><path d="M-32-14h64M-32 4h40"/></g></g>
<g transform="translate(310 130)"><path d="M-56-34h112v56h-112zM-30 22l-10 22 30-22z" fill="#fffdf6" class="o"/><g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M-32-14h64M-32 4h40"/></g></g>
<g transform="translate(470 160)"><path d="M-56-34h112v56h-112zM30 22l10 22-30-22z" fill="#fffdf6" class="o"/><g fill="none" stroke="{TONES['violet'][0]}" stroke-width="3"><path d="M-32-14h64M-8 4h40"/></g></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('fossil', '岩に残った生き物の跡の化石のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-170-100h340v210h-340z" fill="{MUTED}" class="o"/>
  <path d="M-170-100h340v210h-340z" fill="#cdd6dd"/>
  <g fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round">
    <path d="M-90 0q0-80 80-80t80 80q0 60-60 60-46 0-46-40 0-30 30-30"/>
    <path d="M-90 0q-30 6-46 30M70 60l40 30M96-60l40-26"/>
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-170-40h60M110-70h60M-170 60h40M130 30h40"/></g>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('founder', '建物の最初の石を置く創設者のイラスト。', f"""
{person(160,330,1.15,1,'teal','blue','reach','short','smile')}
<g transform="translate(400 300)">
  <path d="M-90-10h180v50h-180z" class="gold o"/>
  <path d="M-60-10v50M0-10v50M60-10v50" class="a"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M-90-10v-120h180v120"/></g>
</g>
<path d="M270 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('fraction', '全体の中のわずかな一部のイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="130" class="tealp o"/>
  <path d="M0 0v-130A130 130 0 0 1 65-113z" class="coral o"/>
  <g fill="none" stroke="{INK}" stroke-width="2.5">{''.join(f'<path d="M0 0l{130*__import__("math").cos(__import__("math").radians(a))*1:.0f} {130*__import__("math").sin(__import__("math").radians(a)):.0f}"/>' for a in range(-90,270,30))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M470 110l-60 26"/></g>
""", ground=False, arrow=True)

add('fragment', '割れて飛び散った破片のイラスト。', f"""
<g transform="translate(250 250)">
  <path d="M-80 60q-16-70 10-110l50 20 20-30 40 40 40-20q16 50 4 100z" class="goldp o"/>
  <path d="M-30-30l20 90M40-10l-10 70" class="a"/>
</g>
<g class="goldp o">
  <path d="M420 190l40-16 10 40-36 10z"/>
  <path d="M480 260l36 6-8 36-34-14z"/>
  <path d="M400 300l30 20-24 26-20-26z"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M350 200l60-20M360 250l60 10M350 300l40 10"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('framework', '建物の骨組みだけの枠組みのイラスト。', f"""
<g transform="translate(300 230)">
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="10" stroke-linejoin="round">
    <path d="M-150 130v-200h300v200"/>
    <path d="M-150-70L0-150l150 80"/>
    <path d="M-150 0h300M-150 66h300M-50-70v200M50-70v200"/>
  </g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('fraud', '仮面をかぶってお金をだまし取る詐欺のイラスト。', f"""
{person(170,350,1.15,1,'violet','blue','give','short','neutral')}
<g transform="translate(170 230)">
  <path d="M-44-16q44-24 88 0-4 40-44 40T-44-16z" class="goldp o"/>
  <g fill="{INK}"><circle cx="-20" cy="-4" r="5"/><circle cx="20" cy="-4" r="5"/></g>
</g>
<g transform="translate(330 250)">
  <path d="M-50-26h100v52h-100z" class="greenp o"/>
  <circle r="14" class="gold o"/>
</g>
{person(470,350,1.1,-1,'coral','gold','give','bob','sad')}
<path d="M400 300h-110" class="a" marker-end="url(#ar)"/>
{xx(330,150,0.9)}
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('freedom', 'かごから飛び立つ鳥の自由のイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-70 90v-120q0-50 70-50t70 50v120z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g fill="none" stroke="{INK}" stroke-width="3">{''.join(f'<path d="M{-46+i*30} 90V-24"/>' for i in range(4))}</g>
  <path d="M0-90v-20" class="a"/>
  <path d="M14-30h60v120h-60z" fill="#fffaf1"/>
  <path d="M14-30v120M74-30v120" class="a"/>
</g>
<g transform="translate(440 160)">
  <ellipse rx="46" ry="30" class="gold o"/>
  <circle cx="40" cy="-20" r="20" class="gold o"/>
  <path d="M56-24l26 8-26 10z" class="coral o"/>
  <circle cx="46" cy="-26" r="4" class="ink"/>
  <path d="M-10-24q30-50 60-14-30 20-60 14z" class="goldp o"/>
  <path d="M-46 6l-40 20 34 6z" class="goldd o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9"><path d="M270 220q60-70 130-80"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('frequency', '同じことが何度も起こる回数のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-220 60h440" class="a" marker-end="url(#ar)"/>
  <g class="coral">{''.join(f'<circle cx="{-200+i*38}" cy="60" r="11"/>' for i in range(11))}</g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3">{''.join(f'<path d="M{-200+i*38} 44V{6-((i%3)*14)}"/>' for i in range(11))}</g>
  <path d="M-220-60h130v30h-130z" class="tealp o"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('frequently', '短い間隔で何度もくり返し起こるイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-230 40h460" class="a" marker-end="url(#ar)"/>
  <g class="teal">{''.join(f'<rect x="{-216+i*30}" y="-40" width="14" height="70" rx="7"/>' for i in range(15))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M300 140h40M300 140h-40"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('frustration', '思うように進まずいら立つイラスト。', f"""
{person(220,350,1.2,1,'coral','blue','up','short','sad')}
<g transform="translate(450 260)">
  <path d="M-80-70h160v110h-160z" fill="#fffdf6" class="o"/>
  <path d="M-30 40h60v20h-60zM-70 60h140v14h-140z" class="ink"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M-30-44l60 60M30-44l-60 60"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round"><path d="M150 170l-14-26M220 150v-28M290 170l14-26"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('funeral', '花を供えて故人を送る葬式のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-70 60v-100q0-40 70-40t70 40v100z" fill="#dfe6ea" class="o"/>
  <path d="M-30-20h60v10h-60zM-6-46v60h12v-60z" fill="{MUTED}"/>
</g>
<g class="coral o"><circle cx="220" cy="320" r="16"/><circle cx="380" cy="320" r="16"/></g>
<g class="greens"><path d="M220 336v30M380 336v30"/></g>
{person(110,350,0.9,1,'violet','violet','stand','short','sad')}
{person(500,350,0.9,-1,'violet','violet','stand','bob','sad')}
<path d="M60 376h480" class="a"/>
""", ground=True)

add('future', 'これから先へ向かう将来のイラスト。', f"""
{person(150,350,1.1,1,'teal','blue','walk','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><path d="M230 330h230"/></g>
<path d="M360 330h120" class="a" marker-end="url(#ar)"/>
{sun(480,170,48)}
<g transform="translate(470 268)">
  <path d="M-60 40v-60h30v60zM-14 40v-90h30v90zM30 40v-46h30v46z" class="tealp o"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

print(len(W), ' '.join(W))
print(sheet(W))
