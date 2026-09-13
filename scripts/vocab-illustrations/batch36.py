"""第36回: 配る・そらす・効果・選挙など42語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('distract', '作業中の人の注意が、横からの音でそれるイラスト。', f"""
{person(200,346,1.15,1,'teal','blue','stand','short','sad')}
<g transform="translate(160 250)">
  <path d="M-60-40h120v80h-120z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-36-16h72M-36 6h50"/></g>
</g>
<g transform="translate(450 240)">
  <path d="M-50-50h100v100h-100z" class="goldp o"/>
  <circle r="26" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M250 220h130" marker-end="url(#ar)"/></g>
<g class="muted"><path d="M180 300h-60" marker-end="url(#ar)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('distress', '頭を抱えて、深く苦しんでいる人のイラスト。', f"""
{person(300,346,1.3,1,'violet','blue','hold','short','sad')}
<g fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"><circle cx="256" cy="240" r="16"/><circle cx="344" cy="240" r="16"/></g>
{cloud(430,140,1.4,'violet')}
<g class="muted"><path d="M430 180v26M462 188v22"/></g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('distribute', '一つの山から、複数の人へ配って回るイラスト。', f"""
{box(300,140,120,70,0,'gold')}
<g class="a" marker-end="url(#ar)"><path d="M250 200q-70 50-90 90"/><path d="M300 200v90"/><path d="M350 200q70 50 90 90"/></g>
{person(150,346,0.85,1,'teal','blue','hold','short','smile')}
{person(300,346,0.85,1,'coral','gold','hold','bob','smile')}
{person(450,346,0.85,1,'violet','teal','hold','cap','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('disturb', '眠っている人のそばで、音を立てて起こしてしまうイラスト。', f"""
<g transform="translate(240 300)">
  <path d="M-150-20h300v50h-300z" class="tealp o"/>
  <path d="M-160 30h320v20h-320z" class="goldd o"/>
  <ellipse cx="-90" cy="-40" rx="48" ry="24" fill="#fffdf6" class="o"/>
  <g transform="translate(-90 -58)">
    <circle r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <path d="M-24-4q3-26 24-26 22 0 26 24-12-10-26-4-11-10-24 6z" fill="{HAIR}"/>
    <circle cx="-8" cy="2" r="2.4" class="ink"/><circle cx="8" cy="2" r="2.4" class="ink"/>
  </g>
</g>
<g class="corals" opacity=".9" style="stroke-width:5"><path d="M470 200q-26 26-26 40t26 40"/><path d="M520 180q-34 34-34 60t34 60"/></g>
<path d="M60 370h480" class="a"/>
""", ground=True)

add('divert', 'まっすぐ進む流れを、横へそらすイラスト。', f"""
<path d="M60 200h180" fill="none" stroke="{TONES['blue'][0]}" stroke-width="14" stroke-linecap="round"/>
<path d="M240 200q60 0 60 60t80 60h140" fill="none" stroke="{TONES['blue'][0]}" stroke-width="14" stroke-linecap="round" marker-end="url(#ar)"/>
<path d="M260 200h260" class="muted"/>
<g class="corals" style="stroke-width:8"><path d="M400 170l40 40M440 170l-40 40"/></g>
""", ground=False, arrow=True)

add('divorce', '一つだった輪が二つに分かれて、離れるイラスト。', f"""
<g transform="translate(190 220)"><circle r="60" fill="none" stroke="{TONES['gold'][0]}" stroke-width="14"/></g>
<g transform="translate(410 220)"><circle r="60" fill="none" stroke="{TONES['gold'][0]}" stroke-width="14"/></g>
<g class="a" marker-end="url(#ar)"><path d="M260 330h-60"/><path d="M340 330h60"/></g>
<g class="corals" style="stroke-width:7"><path d="M280 200l40 40M320 200l-40 40"/></g>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('double', '一つだったものが、二つ分の量になるイラスト。', f"""
{box(160,280,110,80,0,'gold')}
<g transform="translate(430 0)">{box(0,280,110,80,0,'gold')}{box(0,196,110,80,0,'gold')}</g>
<path d="M280 240h60" class="a" marker-end="url(#ar)"/>
<g fill="{INK}"><rect x="300" y="140" width="10" height="30"/><rect x="320" y="140" width="10" height="30"/></g>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('draft', '手書きの下書きから、清書へ進むイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-70q40-14 60 0t60-8M-60-30q40-14 60 0t60-8M-60 10h100"/></g>
  <g class="corals" style="stroke-width:4"><path d="M-60 50h120"/></g>
</g>
<g transform="translate(430 230)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><path d="M-60-70h120M-60-30h120M-60 10h100M-60 50h110"/></g>
</g>
<path d="M280 230h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('drain', '栓を抜いて、水が排水口から出ていくイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-140-60h280l-24 130h-232z" fill="#eef4f8" class="o"/>
  <path d="M-120 0h240l-14 70h-212z" class="bluep o"/>
  <path d="M-140-60h280" class="a"/>
  <ellipse cy="70" rx="26" ry="8" class="ink"/>
</g>
<path d="M280 330v50" class="blues" marker-end="url(#ar)" style="stroke-width:8"/>
<g class="blues"><path d="M230 300q40 20 100 0" style="stroke-width:4"/></g>
""", ground=True, arrow=True)

add('drama', '舞台の幕が開いて、劇が演じられるイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-280-140h100v320h-100zM180-140h100v320h-100z" class="coralp o"/>
  <path d="M-180-140v320M180-140v320" class="a"/>
  <path d="M-280-140h560v40h-560z" class="coral o"/>
</g>
{person(240,340,1.0,1,'violet','blue','up','bob','smile')}
{person(360,340,1.0,-1,'teal','gold','up','short','sad')}
<path d="M120 380h360" class="a"/>
""", ground=False)

add('drawing', '線で描かれた図面のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-160-140h320v280h-320z" class="paper"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4">
    <path d="M-100 80h200M-80 80V-20h160v100"/><path d="M-100-20L0-90l100 70"/>
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5" stroke-dasharray="8 7"><path d="M-120 20h240M0-90v170"/></g>
</g>
<g transform="translate(440 340) rotate(-18)"><path d="M-40-8h80v16h-80z" class="goldd o"/></g>
""", ground=True)

add('driving', 'ハンドルを握って、車を走らせているイラスト。', f"""
<g transform="translate(320 270)">
  <path d="M-190 50h380l-20-70h-60l-40-66h-140l-40 66h-80z" class="coral o"/>
  <path d="M-140-20h100v-52h-70zM-20-72h90l32 52H-20z" class="bluep o"/>
  <circle cx="-110" cy="58" r="34" class="ink"/><circle cx="110" cy="58" r="34" class="ink"/>
</g>
<g transform="translate(200 210)">
  <circle r="26" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-26 0h52M0 0v26" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<circle cx="200" cy="172" r="20" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<path d="M480 190h60" class="a" marker-end="url(#ar)"/>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('drown', '水面の下に沈んで、助けを求めるイラスト。', f"""
<path d="M0 200h600v200H0z" class="bluep"/>
<path d="M0 200q60-16 120 0t120 0 120 0 120 0 120 0" class="a"/>
<g transform="translate(300 260)">
  <path d="M-40-30q40-16 80 0l-10 70h-60z" class="coral o"/>
  <path d="M-30-24l-40-60M30-24l40-60" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
  <circle cx="0" cy="-58" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-24-60q3-26 24-26 22 0 26 24-12-10-26-4-11-10-24 6z" fill="{HAIR}"/>
  <circle cx="0" cy="-44" r="5" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>
<g fill="#ffffff" opacity=".7"><circle cx="360" cy="170" r="10"/><circle cx="384" cy="140" r="7"/></g>
""", ground=False)

add('drug', 'びんに入った錠剤の薬のイラスト。', f"""
<g transform="translate(260 260)">
  <path d="M-60-90h120l-10 160h-100z" fill="#f4fbff" class="o"/>
  <path d="M-30-110h60v20h-60z" class="ink"/>
  <path d="M-50-30h100v40h-100z" class="paper"/>
</g>
<g class="coralp o"><ellipse cx="420" cy="300" rx="26" ry="18"/><ellipse cx="470" cy="310" rx="26" ry="18"/></g>
<g fill="none" stroke="{TONES['coral'][2]}" stroke-width="2.5"><path d="M420 300h0M394 300h52M444 310h52"/></g>
<path d="M340 290h40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('drunk', '足元がふらついて、酔っている人のイラスト。', f"""
<g transform="translate(280 346) rotate(-12)">{person(0,0,1.2,1,'coral','blue','up','short','sad')}</g>
<g transform="translate(430 300) rotate(20)">
  <path d="M-30-50h60l-6 70h-48z" fill="#f4fbff" class="o"/>
  <path d="M-26-20h52l-4 40h-44z" class="goldp o"/>
</g>
<g class="muted"><path d="M180 200q20-24 16-44M380 190q-16-24-12-44"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('dub', '映像の口の動きに、別の音声を重ねるイラスト。', f"""
<g transform="translate(240 220)">
  <path d="M-160-110h320v220h-320z" fill="#2b3a4a" stroke="{INK}" stroke-width="3"/>
  {face(0,0,70,'grin')}
</g>
<g transform="translate(470 220)">
  <path d="M-70-40h140q16 0 16 16v40q0 16-16 16h-90l-26 22 6-22h-30q-16 0-16-16v-40q0-16 16-16z" class="paper"/>
  <g fill="{MUTED}"><circle cx="-24" cy="-2" r="5"/><circle cx="0" cy="-2" r="5"/><circle cx="24" cy="-2" r="5"/></g>
</g>
<path d="M410 220h-40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('dump', '荷台の中身を、まとめてどさっと落とすイラスト。', f"""
<g transform="translate(240 250) rotate(-24)">
  <path d="M-110-50h220v100h-220z" class="coral o"/>
  <path d="M-110-50h220" class="a"/>
</g>
<g fill="#b9b1a3" stroke="{INK}" stroke-width="2.5">
  <path d="M380 330q-20-40 20-50 40-10 56 14 16 22-6 36z"/>
  <circle cx="360" cy="290" r="14"/><circle cx="470" cy="300" r="12"/>
</g>
<path d="M340 220q40 40 50 80" class="a" marker-end="url(#ar)"/>
<path d="M60 350h480" class="a"/>
""", ground=True, arrow=True)

add('earth', '大陸と海が見える地球のイラスト。', f"""
<circle cx="300" cy="210" r="150" class="bluep o"/>
<path d="M200 110q80-20 130 20t20 90-90 60-100-40 10-110z" fill="#e4efe2" stroke="{INK}" stroke-width="3"/>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"><path d="M150 210h300M300 60v300"/></g>
""", ground=False)

add('ease', '重い荷物を台車に載せて、楽に運べるイラスト。', f"""
<g transform="translate(360 300)">
  <path d="M-110-20h220v20h-220z" class="goldp o"/>
  <circle cx="-80" cy="20" r="20" class="ink"/><circle cx="80" cy="20" r="20" class="ink"/>
</g>
{box(360,240,140,90,0,'gold')}
{person(170,346,1.1,1,'teal','blue','point','short','smile')}
<path d="M250 250h40" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M480 160l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('eastern', '地図の東側の地域に印をつけたイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <path d="M0-140v280" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M10-130h180v260H10z" class="coralp o"/>
</g>
<g transform="translate(300 210)">
  <path d="M100 0h60" class="a" marker-end="url(#ar)"/>
</g>
""", ground=True, arrow=True)

add('echo', '声が壁に当たって、返って聞こえるイラスト。', f"""
<path d="M480 100h60v240h-60z" class="goldp o"/>
{person(180,346,1.1,1,'teal','blue','up','short','neutral')}
<g class="teals" marker-end="url(#ar)" style="stroke-width:5"><path d="M250 200h180"/></g>
<g class="corals" marker-end="url(#ar)" style="stroke-width:5" opacity=".8"><path d="M430 270H250"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('educated', '本を読み終えて、学びを身につけた人のイラスト。', f"""
{person(200,346,1.15,1,'teal','blue','carry','short','smile')}
<g transform="translate(200 268)">
  <path d="M-46-30h92v60h-92z" class="tealp o"/>
  <path d="M-30-30h12v60h-12z" class="teal o"/>
</g>
<g transform="translate(430 240)">
  <path d="M-90-70h180v140h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-56-40h112M-56-10h112M-56 20h80"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"><path d="M20 40l14 14 26-30"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('education', '黒板の前で学びが行われている、教育の場のイラスト。', f"""
<g transform="translate(400 200)">
  <path d="M-130-90h260v180h-260z" fill="#3d4c5c" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#c9d4dd" stroke-width="4"><path d="M-100-50h200M-100-10h160M-100 30h180"/></g>
</g>
{person(140,346,1.1,1,'teal','blue','point','bun','neutral')}
<g opacity=".8">{person(300,366,0.7,-1,'coral','gold','stand','short','smile')}{person(380,366,0.7,-1,'violet','teal','stand','bob','smile')}</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('educational', '遊びながら学べる、教育向けの玩具のイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-160-40h320v20h-320z" class="goldp o"/>
  <g class="tealp o"><rect x="-140" y="-100" width="60" height="60"/></g>
  <g class="coralp o"><rect x="-60" y="-100" width="60" height="60"/></g>
  <g class="goldp o"><rect x="20" y="-100" width="60" height="60"/></g>
  <g fill="{INK}"><rect x="-124" y="-80" width="10" height="24"/><path d="M-46-80h26v10h-16v4h16v10h-26z"/><path d="M36-80h26v10l-14 8 14 8v6H36v-10h14l-14-8z"/></g>
</g>
{person(140,346,0.85,1,'coral','blue','point','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('effect', '原因のボタンを押すと、結果の明かりがつくイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-70-60h140v120h-140z" fill="#dfe6ea" class="o"/>
  <circle r="34" class="coral o"/>
</g>
<g transform="translate(450 240)">
  <circle r="46" class="goldp o"/>
  <path d="M-18 46h36v16h-36z" class="ink"/>
  <g class="golds" style="stroke-width:4"><path d="M0-62v-16M-48-32l-16-10M48-32l16-10"/></g>
</g>
<path d="M270 250h100" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('effective', '少ない力で、大きな成果が出ているイラスト。', f"""
<g transform="translate(160 280)">
  <path d="M-40-40h80v80h-80z" class="tealp o"/>
</g>
<g transform="translate(430 250)">
  <path d="M-100-90h200v180h-200z" class="teal o"/>
</g>
<path d="M230 270h80" class="a" marker-end="url(#ar)" style="stroke-width:7"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M480 130l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('either', '二つの道のどちらでもよいことを示したイラスト。', f"""
<circle cx="100" cy="230" r="24" class="teal o"/>
<path d="M130 210q120-80 220-60t140 20" fill="none" stroke="{TONES['teal'][0]}" stroke-width="10" stroke-linecap="round" marker-end="url(#ar)"/>
<path d="M130 250q120 80 220 60t140-20" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round"><path d="M520 120l16 16 26-32M520 340l16 16 26-32"/></g>
""", ground=False, arrow=True)

add('elderly', 'つえをついて歩く、年配の人のイラスト。', f"""
{person(260,346,1.15,1,'violet','gold','point','short','smile')}
<path d="M340 250v110" fill="none" stroke="{TONES['gold'][2]}" stroke-width="11" stroke-linecap="round"/>
<path d="M340 250q20-18 38-8" fill="none" stroke="{TONES['gold'][2]}" stroke-width="11" stroke-linecap="round"/>
<g fill="#e7eef4"><path d="M236 228q4-26 26-26 22 0 26 24-14-8-28-2-10-6-24 4z"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('elect', '投票の結果、一人が選ばれるイラスト。', f"""
{person(150,346,0.9,1,'teal','blue','stand','short','neutral')}
{person(300,346,1.1,1,'coral','gold','up','bob','smile')}
{person(450,346,0.9,1,'violet','teal','stand','cap','neutral')}
<g transform="translate(300 150)">
  <path d="M-46-26h92v52h-92z" class="paper"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round"><path d="M-18 0l14 14 24-28"/></g>
</g>
<circle cx="300" cy="240" r="56" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('electricity', '発電所から電線を通って、電気が届くイラスト。', f"""
<g transform="translate(140 260)">
  <path d="M-70-60h140v120h-140z" fill="#dfe6ea" class="o"/>
  <path d="M-40-100h30v40h-30zM10-100h30v40H10z" class="ink"/>
</g>
<path d="M210 220h160" fill="none" stroke="{INK}" stroke-width="6"/>
<g transform="translate(300 190)"><path d="M-14-30l-16 46h20l-10 34 30-50h-20l16-30z" class="gold o"/></g>
<g transform="translate(460 250)">
  <circle r="40" class="goldp o"/>
  <path d="M-16 40h32v14h-32z" class="ink"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('electronic', '基板の上に電子部品が並んだイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-170-110h340v220h-340z" class="greenp o"/>
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="3">
    <path d="M-130-60h110v60h-150M20-60h110v120"/><path d="M-130 40h90M30 20h100"/>
  </g>
  <g class="ink"><rect x="-90" y="-30" width="60" height="36"/><rect x="30" y="30" width="70" height="36"/></g>
  <g class="coral o"><circle cx="-130" cy="-80" r="9"/><circle cx="130" cy="80" r="9"/></g>
</g>
""", ground=True)

add('elevate', '台の上へ持ち上げて、高さを上げるイラスト。', f"""
{box(180,300,90,60,0,'gold')}
<g transform="translate(430 0)">
  <path d="M-70 320h140v40h-140z" class="goldd o"/>
  {box(0,270,90,60,0,'gold')}
</g>
<path d="M280 260h60" class="a" marker-end="url(#ar)"/>
<path d="M430 190v40" class="a" marker-end="url(#ar)" transform="rotate(180 430 210)"/>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('eliminate', '並んだ候補から、一つを取り除いて消すイラスト。', f"""
<g class="tealp o">
  {''.join(f'<rect x="{100+i*90}" y="220" width="70" height="90"/>' for i in range(5) if i != 2)}
</g>
<g class="muted"><rect x="280" y="220" width="70" height="90"/></g>
<g class="corals" style="stroke-width:8"><path d="M290 240l50 50M340 240l-50 50"/></g>
<path d="M60 330h480" class="a"/>
""", ground=False)

add('embarrassed', '顔を赤くして、きまり悪そうにしている人のイラスト。', f"""
{face(280,200,120,'flat')}
<circle cx="200" cy="230" r="26" class="coralp"/><circle cx="360" cy="230" r="26" class="coralp"/>
{drop(400,180,0.9)}
<g class="muted"><path d="M440 260v24M470 250v22"/></g>
""", ground=False)

add('embarrassing', '人前で転んで、きまりの悪い場面になるイラスト。', f"""
<g transform="translate(220 340) rotate(24)">{person(0,0,1.1,1,'coral','blue','up','short','sad')}</g>
<g opacity=".75">{person(430,346,0.9,-1,'teal','gold','stand','bob','smile')}{person(510,346,0.9,-1,'violet','teal','stand','short','smile')}</g>
<g class="golds" style="stroke-width:4"><path d="M370 230l24-24M390 270h26"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('embed', '土台の中に部品を埋め込むイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-160-60h320v120h-320z" class="goldp o"/>
  <path d="M-40-40h80v70h-80z" class="teal o"/>
  <path d="M-40-40h80" class="a"/>
</g>
<path d="M300 160v50" class="a" marker-end="url(#ar)"/>
<g transform="translate(300 130)"><path d="M-40-24h80v40h-80z" class="teal o" opacity=".55"/></g>
""", ground=True, arrow=True)

add('embody', '理念を、実物の形として示しているイラスト。', f"""
<g transform="translate(160 230)">
  <path d="M-90-60q-14-40 34-48 14-34 66-24 30 6 38 34 50-6 52 40 2 36-42 38h-118q-28-4-30-40z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 -8)"><path d="M0 20l-24-30 12-14 12 12 12-12 12 14z" class="coral o"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-80-70h160v140h-160z" class="tealp o"/>
  <path d="M0-40l-24 30 12 14 12-12 12 12 12-14z" class="coral o" transform="rotate(180 0 0)"/>
</g>
<path d="M280 240h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('embrace', '両腕を広げて、相手を抱き寄せるイラスト。', f"""
<circle cx="300" cy="150" r="80" class="coralp"/>
{person(250,346,1.2,1,'violet','blue','give','bob','smile')}
{person(350,346,1.2,-1,'teal','gold','give','short','smile')}
<path d="M300 240q-40-20-60 10M300 240q40-20 60 10" fill="none" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('emotional', '涙を流して、感情があふれている顔のイラスト。', f"""
{face(280,200,120,'sad')}
{drop(230,250,1.2)}{drop(330,256,1.2)}
<g transform="translate(460 160)"><path d="M0 30l-30-36 14-16 16 14 16-14 14 16z" class="coral o"/></g>
""", ground=False)

add('emphasize', '一つの語だけを、太く大きく目立たせるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-180-120h360v240h-360z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-140-80h280M-140 30h280M-140 70h220"/></g>
  <g fill="{TONES['coral'][0]}"><rect x="-140" y="-30" width="200" height="16"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M-140 0h200"/></g>
</g>
""", ground=True)

add('enact', '法案が承認されて、規則として定まるイラスト。', f"""
<g transform="translate(280 240)">
  <path d="M-120-120h240v240h-240z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-90-80h180M-90-40h180M-90 0h140"/></g>
  <circle cx="60" cy="60" r="26" class="coral o"/>
</g>
{hand(470,180,-1)}
<path d="M420 220l-30 20" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('encompass', '大きな囲みが、複数のものをすべて含むイラスト。', f"""
<circle cx="300" cy="220" r="160" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" stroke-dasharray="16 12"/>
<g class="tealp o">
  <circle cx="220" cy="170" r="40"/><circle cx="360" cy="180" r="40"/><circle cx="290" cy="300" r="40"/>
</g>
<path d="M300 400v-20" class="a"/>
""", ground=False)
print(len(W), ' '.join(W)); print(sheet(W))
