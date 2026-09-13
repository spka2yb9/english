"""第31回: 評価・出席・平均・所属など30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('army', '隊列を組んだ陸軍の兵士が並んでいるイラスト。', f"""
{person(130,346,0.9,1,'green','green','stand','cap','neutral')}
{person(230,346,0.9,1,'green','green','stand','cap','neutral')}
{person(330,346,0.9,1,'green','green','stand','cap','neutral')}
{person(430,346,0.9,1,'green','green','stand','cap','neutral')}
{person(520,346,0.9,1,'green','green','stand','cap','neutral')}
<path d="M60 240h480" class="muted"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('articulate', '口の形をはっきり作って、明確に話しているイラスト。', f"""
{face(220,200,110,'grin')}
<g transform="translate(430 200)">
  <path d="M-70-50h140q16 0 16 16v68q0 16-16 16h-100l-24 20 6-20h-22q-16 0-16-16v-68q0-16 16-16z" class="paper"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5"><path d="M-46-20h92M-46 4h70"/></g>
</g>
<path d="M340 200h30" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('artificial', '本物の花と、造花を並べて比べたイラスト。', f"""
<g transform="translate(180 300)">
  <path d="M0 0v-80" fill="none" stroke="{TONES['green'][2]}" stroke-width="8" stroke-linecap="round"/>
  <path d="M0-40c-36-8-48-32-48-32 32-8 48 32 48 32z" class="green o"/>
  <circle cy="-90" r="24" class="coral o"/>
  <g class="coralp o"><circle cx="-32" cy="-110" r="17"/><circle cx="32" cy="-110" r="17"/><circle cx="0" cy="-130" r="17"/></g>
</g>
<g transform="translate(430 300)">
  <path d="M0 0v-80" fill="none" stroke="{MUTED}" stroke-width="8" stroke-linecap="round"/>
  <circle cy="-90" r="24" fill="none" stroke="{INK}" stroke-width="4"/>
  <g fill="none" stroke="{INK}" stroke-width="4"><circle cx="-32" cy="-110" r="17"/><circle cx="32" cy="-110" r="17"/><circle cx="0" cy="-130" r="17"/></g>
  <path d="M-40-60h80v10h-80z" class="muted"/>
</g>
<path d="M300 130v230" class="muted"/>
""", ground=True)

add('assault', '腕を振り上げて、相手に襲いかかろうとするイラスト。', f"""
{person(200,346,1.15,1,'coral','blue','up','cap','neutral')}
{person(430,346,1.1,-1,'teal','gold','up','bob','sad')}
<path d="M280 220h60" class="a" marker-end="url(#ar)" style="stroke-width:7"/>
<g class="corals" style="stroke-width:7"><path d="M340 160l30 30M370 160l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('assert', '手を強く前に出して、自分の考えを断言するイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','point','short','neutral')}
<g transform="translate(410 200)">
  <path d="M-80-46h160q16 0 16 16v50q0 16-16 16h-110l-26 22 6-22h-30q-16 0-16-16v-50q0-16 16-16z" class="paper"/>
  <path d="M-8-24h16v34h-16zM-8 18h16v14h-16z" class="teal o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('assess', '品物を見て、点数をつけて評価しているイラスト。', f"""
{person(160,346,1.15,1,'blue','violet','point','bun','neutral')}
<g transform="translate(400 260)">
  <path d="M-100-70h200v140h-200z" class="tealp o"/>
</g>
<g transform="translate(400 140)">
  <path d="M-50-30h100v60h-100z" class="paper"/>
  <g fill="{INK}"><rect x="-24" y="-14" width="10" height="28"/><path d="M0-14h30v10h-20v6h20v12H0z"/></g>
</g>
<path d="M250 200h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('assign', '担当の仕事を、それぞれの人に割り当てるイラスト。', f"""
{person(300,140,0.7,1,'blue','violet','give','short','neutral')}
{person(150,346,0.9,1,'teal','blue','hold','bob','neutral')}
{person(300,346,0.9,1,'coral','gold','hold','short','neutral')}
{person(450,346,0.9,1,'violet','teal','hold','cap','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M270 200q-80 30-110 60"/><path d="M300 200v60"/><path d="M330 200q80 30 110 60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('attain', '高い所の実に手が届いて、取ることができたイラスト。', f"""
{tree(400,340,1.3)}
<g transform="translate(400 200)"><circle r="20" class="coral o"/></g>
{person(230,340,1.15,1,'teal','blue','reach','short','smile')}
<circle cx="320" cy="215" r="15" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<path d="M280 270q30-40 60-56" class="a" marker-end="url(#ar)"/>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('attend', '教室の席に着いて、授業に出席しているイラスト。', f"""
<g transform="translate(430 200)">
  <path d="M-120-90h240v180h-240z" fill="#3d4c5c" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#c9d4dd" stroke-width="4"><path d="M-90-50h180M-90-10h140"/></g>
</g>
<g transform="translate(200 330)">
  <path d="M-70-20h140v18h-140z" class="goldp o"/>
  <path d="M-60 0v40M60 0v40" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10" stroke-linecap="round"/>
</g>
<g transform="translate(190 310)">
  <path d="M-28-66q28-14 56 0l-8 64h-40z" class="teal o"/>
  <path d="M-22-8l-52 18M18-8l14 28" fill="none" stroke="{TONES['blue'][2]}" stroke-width="11" stroke-linecap="round"/>
  <circle cx="0" cy="-92" r="23" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-23-94q3-26 24-26 22 0 26 24-12-10-26-4-11-10-24 6z" fill="{HAIR}"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M120 180l18 18 30-36"/></g>
<path d="M60 370h480" class="a"/>
""", ground=True)

add('attention', '一点に集まった視線が、注意の向きを示すイラスト。', f"""
<g transform="translate(430 220)">
  <circle r="46" class="coral o"/>
  <circle r="76" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
</g>
{person(140,346,1.0,1,'teal','blue','stand','short','neutral')}
{person(250,346,1.0,1,'violet','gold','stand','bob','neutral')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><path d="M190 230h150" marker-end="url(#ar)"/><path d="M300 240h50" marker-end="url(#ar)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('attractive', '目を引く華やかな品に、視線が集まるイラスト。', f"""
<g transform="translate(400 230)">
  <path d="M-80-80h160v160h-160z" class="coralp o"/>
  <circle r="46" class="coral o"/>
  <g class="golds" style="stroke-width:4"><path d="M0-100v-20M-96-96l-14-14M96-96l14-14"/></g>
</g>
{person(150,346,1.1,1,'teal','blue','point','bob','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M220 230h90" marker-end="url(#ar)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('attribute', 'ある結果を、原因の方へ線でつないで示したイラスト。', f"""
<g transform="translate(160 230)">
  <path d="M-70-60h140v120h-140z" class="tealp o"/>
</g>
<g transform="translate(430 230)">
  <path d="M-70-60h140v120h-140z" class="coralp o"/>
</g>
<path d="M350 230H240" class="a" marker-end="url(#ar)"/>
<path d="M120 350h360" class="muted"/>
""", ground=True, arrow=True)

add('author', '自分の書いた本を手にしている著者のイラスト。', f"""
{person(180,346,1.15,1,'violet','blue','carry','bun','smile')}
<g transform="translate(180 268)">
  <path d="M-50-34h100v68h-100z" class="violetp o"/>
  <path d="M-32-34h14v68h-14z" class="violet o"/>
</g>
<g transform="translate(420 250)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-60 {-70+i*30}h120"/>' for i in range(6))}</g>
</g>
<path d="M280 220h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('average', '高さの違う棒の中ほどに、平均の線を引いたイラスト。', f"""
<path d="M60 340h480" class="a"/>
<g class="tealp o">
  <rect x="100" y="200" width="60" height="140"/><rect x="190" y="270" width="60" height="70"/>
  <rect x="280" y="160" width="60" height="180"/><rect x="370" y="250" width="60" height="90"/><rect x="460" y="220" width="60" height="120"/>
</g>
<path d="M60 230h480" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="14 10"/>
""", ground=False)

add('await', '到着を待ちながら、駅で立っているイラスト。', f"""
<g transform="translate(430 250)">
  <path d="M-140-100h280v200h-280z" fill="#dfe6ea" class="o"/>
  <g class="bluep o"><rect x="-110" y="-70" width="80" height="60"/><rect x="-10" y="-70" width="80" height="60"/></g>
</g>
{person(170,346,1.15,1,'teal','blue','stand','short','neutral')}
<g transform="translate(250 180)">
  <circle r="36" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0v-20M0 0l14 8" class="a"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('background', '手前の人物の後ろに、遠くの景色が広がるイラスト。', f"""
<g opacity=".45">
  <path d="M40 250L200 100l120 120 90-70 150 100z" class="tealp o"/>
  {tree(500,300,0.6)}
</g>
<path d="M0 300h600v100H0z" class="ground"/>
<path d="M0 300h600" class="a"/>
{person(220,366,1.3,1,'coral','blue','stand','bob','smile')}
<path d="M420 200h60" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('baseball', 'バットとボールとグローブが並んだ野球の道具のイラスト。', f"""
<g transform="translate(180 250) rotate(-24)">
  <path d="M-20-16h130q20 0 20 16t-20 16H-20z" class="goldd o"/>
  <path d="M-80-12h60v24h-60z" class="goldp o"/>
</g>
<g transform="translate(340 220)">
  <circle r="30" fill="#fffdf6" class="o"/>
  <path d="M-20-18q20 18 0 36M20-18q-20 18 0 36" fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"/>
</g>
<g transform="translate(450 290)">
  <path d="M-70 40q-30-70 10-100 40-30 90-10 40 16 30 60-6 30-30 50z" class="goldp o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"><path d="M-30-40l20 70M0-56l14 84M30-60l6 80"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('basic', '土台となる基本の形だけを示したイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-120-60h240v120h-240z" class="tealp o"/>
  <path d="M-120-60h240v120h-240z" fill="none" class="a"/>
</g>
<g opacity=".3"><path d="M180 130h240v50H180z" class="muted"/></g>
<path d="M120 350h360" class="a"/>
<path d="M500 250h50" class="a" marker-end="url(#ar)" transform="rotate(180 525 250)"/>
""", ground=True, arrow=True)

add('basketball', 'ゴールのリングにボールを投げ入れる、バスケットボールのイラスト。', f"""
<g transform="translate(430 180)">
  <path d="M60-100v200" fill="none" stroke="{INK}" stroke-width="10"/>
  <path d="M-20-40h80v-60h-80z" fill="#fffdf6" class="o"/>
  <path d="M-40-40h40v10h-40z" class="coral o"/>
  <path d="M-40-30q20 40 0 50" fill="none" stroke="{MUTED}" stroke-width="3"/>
</g>
<g transform="translate(250 200)">
  <circle r="34" class="coral o"/>
  <path d="M-34 0h68M0-34v68M-24-24q48 48 0 0M24-24q-48 48 0 0" fill="none" stroke="{TONES['coral'][2]}" stroke-width="2.5"/>
</g>
<path d="M180 300q60-140 200-150" class="muted" marker-end="url(#ar)"/>
{person(140,346,0.9,1,'teal','blue','up','short','neutral')}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('bean', 'さやから取り出した豆が並んでいるイラスト。', f"""
<g transform="translate(220 240) rotate(-14)">
  <path d="M-110-24q110-40 220 0-110 40-220 0z" class="green o"/>
  <path d="M-110-24q110-40 220 0" fill="none" stroke="{TONES['green'][2]}" stroke-width="3"/>
</g>
<g class="goldd o">
  <ellipse cx="330" cy="300" rx="26" ry="20"/><ellipse cx="390" cy="310" rx="26" ry="20"/><ellipse cx="450" cy="298" rx="26" ry="20"/>
</g>
<path d="M290 270h30" class="a" marker-end="url(#ar)"/>
<path d="M120 340h380" class="a"/>
""", ground=True)

add('beef', '牛と、切り分けられた肉を並べたイラスト。', f"""
<g transform="translate(170 290)">
  <ellipse cy="-30" rx="80" ry="46" fill="#fffdf6" class="o"/>
  <path d="M-56 12v26M-18 16v22M18 16v22M54 8v30" fill="none" stroke="{MUTED}" stroke-width="12" stroke-linecap="round"/>
  <g transform="translate(84 -58)">
    <ellipse rx="28" ry="24" fill="#fffdf6" class="o"/>
    <path d="M-20-20q-14-26 6-26 16 0 16 20z" class="ink" opacity=".8"/>
    <circle cx="8" cy="-4" r="3" class="ink"/>
  </g>
  <g fill="{INK}" opacity=".5"><ellipse cx="-20" cy="-40" rx="18" ry="12"/><ellipse cx="30" cy="-20" rx="14" ry="10"/></g>
</g>
<g transform="translate(430 300)">
  <path d="M-70-40h140v80h-140z" class="coralp o"/>
  <path d="M-40-20h80v40h-40z" fill="#fff0c5" stroke="{INK}" stroke-width="2.5"/>
</g>
<path d="M300 280h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('before', 'あとの出来事の前に、先の出来事があるイラスト。', f"""
<path d="M60 230h480" class="a" marker-end="url(#ar)"/>
<g fill="{INK}"><circle cx="180" cy="230" r="11"/><circle cx="400" cy="230" r="11"/></g>
<g transform="translate(180 300)"><path d="M-40-24h80v48h-80z" class="coralp o"/></g>
<g transform="translate(400 300)"><path d="M-40-24h80v48h-80z" class="tealp o"/></g>
<path d="M380 160H200" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('beg', '両手を差し出して、強く頼んでいるイラスト。', f"""
{person(220,346,1.15,1,'coral','blue','give','short','sad')}
{person(440,346,1.1,-1,'teal','gold','stand','bob','neutral')}
<g fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"><circle cx="300" cy="252" r="15"/></g>
<g transform="translate(300 180)">
  <path d="M-50-26h100q12 0 12 12v26q0 12-12 12h-70l-18 16 4-16q-12 0-12-12v-26q0-12 12-12z" class="paper"/>
  <path d="M-6-14h12v22h-6z" class="coral"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('behave', '行儀よく座って、きちんとふるまっているイラスト。', f"""
<g transform="translate(300 330)">
  <path d="M-80-20h160v18h-160z" class="goldp o"/>
  <path d="M-70 0v46M70 0v46" fill="none" stroke="{TONES['gold'][2]}" stroke-width="11" stroke-linecap="round"/>
  <path d="M60-20v-100h18v100z" class="goldd o"/>
</g>
<g transform="translate(290 310)">
  <path d="M-28-66q28-14 56 0l-8 64h-40z" class="teal o"/>
  <path d="M-22-8l-52 18M18-8l14 28" fill="none" stroke="{TONES['blue'][2]}" stroke-width="11" stroke-linecap="round"/>
  <path d="M-24-56l18 26M24-56l-18 26" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
  <circle cx="0" cy="-92" r="23" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-23-94q3-26 24-26 22 0 26 24-12-10-26-4-11-10-24 6z" fill="{HAIR}"/>
  <path d="M-7-88q7 7 14 0" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M460 200l18 18 30-36"/></g>
<path d="M120 380h360" class="a"/>
""", ground=True)

add('behaviour', '同じ場面での、二通りのふるまいを並べたイラスト。', f"""
{person(170,346,1.1,1,'teal','blue','stand','short','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M240 200l18 18 30-36"/></g>
{person(430,346,1.1,1,'coral','gold','up','bob','sad')}
<g class="corals" style="stroke-width:7"><path d="M330 180l30 30M360 180l-30 30"/></g>
<path d="M300 130v240" class="muted"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('belong', '所有者の名札がついた品物が、その人の手元にあるイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','carry','short','smile')}
{box(180,266,110,74,0,'gold')}
<g transform="translate(330 200) rotate(-10)">
  <path d="M-44-24h88v48h-88z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-26-6h52M-26 8h34"/></g>
  <path d="M-44 0l-22-12v24z" class="paper"/>
</g>
<path d="M300 250l-30-30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('belt', '穴とバックルのついたベルトのイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-24h340v48h-340z" class="goldd o"/>
  <g fill="{INK}">{''.join(f'<circle cx="{40+i*26}" cy="0" r="5"/>' for i in range(4))}</g>
  <g transform="translate(-230 0)">
    <path d="M-40-34h80v68h-80z" fill="none" stroke="{INK}" stroke-width="8"/>
    <path d="M0-34v68" fill="none" stroke="{INK}" stroke-width="6"/>
  </g>
</g>
<path d="M120 340h360" class="a"/>
""", ground=True)

add('best', '三つの中で、いちばん高い評価を得た一つのイラスト。', f"""
<g class="tealp o"><rect x="120" y="240" width="90" height="120"/><rect x="400" y="270" width="90" height="90"/></g>
<rect x="260" y="180" width="90" height="180" class="gold o"/>
<g transform="translate(305 140)"><path d="M0-30l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" class="gold o"/></g>
<path d="M60 360h480" class="a"/>
""", ground=False)

add('bet', 'コインを台に置いて、勝ち負けに賭けているイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-180-20h360v20h-360z" class="greenp o"/>
  <g class="goldp o"><circle cx="-40" cy="-40" r="22"/><circle cx="0" cy="-46" r="22"/><circle cx="40" cy="-40" r="22"/></g>
</g>
{person(150,346,0.95,1,'teal','blue','point','short','neutral')}
{person(460,346,0.95,-1,'coral','gold','point','bob','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M230 220h40"/><path d="M370 220h-40" transform="translate(50 0)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('better', '低い評価から高い評価へ、一段上がるイラスト。', f"""
<g class="tealp o"><rect x="150" y="250" width="110" height="110"/></g>
<rect x="340" y="180" width="110" height="180" class="teal o"/>
<path d="M280 200h40" class="a" marker-end="url(#ar)"/>
<g class="golds" style="stroke-width:4"><path d="M395 150v-24"/></g>
<path d="M60 360h480" class="a"/>
""", ground=False, arrow=True)

add('bid', '札を挙げて、競売で入札しているイラスト。', f"""
{person(200,346,1.15,1,'teal','blue','up','short','neutral')}
<g transform="translate(200 180)">
  <path d="M-40-26h80v52h-80z" class="paper"/>
  <g fill="{INK}"><rect x="-14" y="-12" width="10" height="24"/><path d="M4-12h22v8h-14v4h14v12H4z"/></g>
</g>
{person(430,346,1.1,-1,'blue','violet','point','cap','neutral')}
<g transform="translate(430 220)">
  <path d="M-40-10h60v20h-60z" class="goldd o"/>
</g>
<path d="M280 230h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('birth', '生まれたばかりの赤ちゃんが、腕に抱かれているイラスト。', f"""
<circle cx="300" cy="140" r="80" class="coralp" opacity=".5"/>
{person(300,346,1.3,1,'violet','blue','carry','bob','smile')}
<g transform="translate(300 268)">
  <ellipse rx="56" ry="34" class="coralp o"/>
  <circle cx="-30" cy="-6" r="22" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-38-4h6M-22-4h6" class="a"/>
</g>
<g class="golds" style="stroke-width:4"><path d="M180 180l-24-24M420 180l24-24"/></g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('arm', '武器を持たせて、備えさせているイラスト。', f"""
{person(220,346,1.15,1,'green','green','carry','cap','neutral')}
<g transform="translate(300 250) rotate(20)">
  <path d="M-10-100h20v160h-20z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-10-100l10-24 10 24z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-30 60h60v14h-60z" class="goldd o"/>
</g>
<g transform="translate(450 290)">
  <path d="M-60-70h120v140h-120z" class="greenp o"/>
  <path d="M0-70v140M-60 0h120" fill="none" stroke="{TONES['green'][0]}" stroke-width="4"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('academy', '専門の学び舎の建物と看板のイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-190 100h380v20h-380z" class="goldd o"/>
  <g class="goldp o">{''.join(f'<rect x="{-160+i*70}" y="-30" width="40" height="130"/>' for i in range(5))}</g>
  <path d="M-200-30h400v-26h-400z" class="goldd o"/>
  <path d="M-200-56L0-140l200 84z" class="gold o"/>
</g>
<g transform="translate(300 200)">
  <path d="M-70-20h140v40h-140z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-46 0h92"/></g>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('allowance', '毎月決まった額の小遣いを受け取っているイラスト。', f"""
{person(160,346,1.1,1,'gold','violet','give','short','neutral')}
{person(440,346,1.1,-1,'coral','blue','hold','bob','smile')}
<g transform="translate(300 260)">
  <path d="M-50-30h100v60h-100z" class="greenp o"/>
  <circle r="14" class="green o"/>
</g>
<g transform="translate(300 160)">
  <path d="M-60-30h120v50h-120z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-36-10h72M-36 4h50"/></g>
</g>
<path d="M250 210h100" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(' '.join(W)); print(sheet(W))
