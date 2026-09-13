"""第30回: 達成・蓄積・広告・接近など30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('accomplish', '一覧のすべての項目に印がついて、やり切ったイラスト。', f"""
<g transform="translate(280 230)">
  <path d="M-130-130h260v260h-260z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-50 {-90+i*45}h150"/>' for i in range(5))}</g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round">
    {''.join(f'<path d="M-100 {-94+i*45}l12 12 20-24"/>' for i in range(5))}
  </g>
</g>
{person(480,346,0.9,-1,'teal','blue','up','short','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('accumulate', '同じ物が少しずつたまって、山になっていくイラスト。', f"""
{box(140,330,70,50,0,'gold')}
<g transform="translate(300 0)">{box(0,330,70,50,0,'gold')}{box(0,278,70,50,0,'gold')}</g>
<g transform="translate(460 0)">{box(0,330,70,50,0,'gold')}{box(0,278,70,50,0,'gold')}{box(0,226,70,50,0,'gold')}{box(0,174,70,50,0,'gold')}</g>
<path d="M100 130h420" class="a" marker-end="url(#ar)"/>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('accurate', '矢が的の中心にぴったり当たっているイラスト。', f"""
<g transform="translate(320 220)">
  <circle r="120" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <circle r="88" class="tealp o"/><circle r="56" fill="#fffdf6" stroke="{INK}" stroke-width="3"/><circle r="22" class="coral o"/>
  <path d="M0 0l-160 40" fill="none" stroke="{TONES['gold'][2]}" stroke-width="8" stroke-linecap="round"/>
  <path d="M-160 40l-26-6 14 22z" class="goldp o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M480 130l18 18 30-36"/></g>
""", ground=True)

add('activate', 'スイッチを入れて、装置が動き出すイラスト。', f"""
<g transform="translate(360 250)">
  <path d="M-120-90h240v180h-240z" fill="#dfe6ea" class="o"/>
  <circle cx="0" cy="-20" r="46" fill="none" stroke="{INK}" stroke-width="6"/>
  <g class="tealp o"><path d="M0-20q42-26 52 14-30 22-52-14z"/><path d="M0-20q-26 42-58 12 20-30 58-12z"/><path d="M0-20q-14-46 30-46 6 34-30 46z"/></g>
  <g class="green o"><circle cx="-88" cy="50" r="14"/></g>
</g>
{hand(170,250,1)}
<path d="M240 250h30" class="a" marker-end="url(#ar)"/>
<path d="M360 130a120 120 0 0 1 90 40" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('additional', '基本の三つに、追加の一つが加わるイラスト。', f"""
<g class="tealp o">
  <rect x="110" y="230" width="70" height="90"/><rect x="200" y="230" width="70" height="90"/><rect x="290" y="230" width="70" height="90"/>
</g>
<rect x="420" y="230" width="70" height="90" class="green o"/>
<g class="greens" style="stroke-width:8"><path d="M380 180h60M410 150v60"/></g>
<path d="M60 320h480" class="a"/>
""", ground=False)

add('address', '演壇に立って、大勢に向けて演説しているイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-80-40h160v100h-160z" class="goldp o"/>
  <path d="M-92-40h184" class="a"/>
  <path d="M0-40v-30" class="a"/>
  <circle cy="-84" r="14" class="ink"/>
</g>
{person(300,264,0.95,1,'blue','violet','point','short','neutral')}
<g class="teals" opacity=".85" style="stroke-width:4"><path d="M400 200q30 30 30 56M440 180q38 38 38 76"/></g>
<g opacity=".55">{person(120,366,0.7,1,'coral','gold','stand','bob','smile')}{person(500,366,0.7,-1,'teal','blue','stand','short','smile')}</g>
""", ground=True)

add('adhere', 'シールが面にぴったり張りついているイラスト。', f"""
<g transform="translate(320 250)">
  <path d="M-140-100h280v200h-280z" class="goldp o"/>
  <circle cx="20" cy="0" r="60" class="coralp o"/>
  <circle cx="20" cy="0" r="60" fill="none" class="a"/>
</g>
{hand(150,180,1)}
<g class="a" marker-end="url(#ar)"><path d="M210 200l40 20"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 130l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('administer', '書類と印をそろえて、全体を管理しているイラスト。', f"""
{person(160,346,1.15,1,'blue','violet','point','bun','neutral')}
<g transform="translate(400 280)">
  <path d="M-140-20h280v20h-280z" class="goldp o"/>
  <g class="tealp o"><rect x="-120" y="-80" width="70" height="60"/><rect x="-40" y="-80" width="70" height="60"/><rect x="40" y="-80" width="70" height="60"/></g>
</g>
<g transform="translate(300 170)">
  <path d="M-40-24h80v48h-80z" class="paper"/>
  <circle r="14" class="coral o"/>
</g>
<path d="M240 200h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('adventure', '地図を手に、未知の道へ踏み出していくイラスト。', f"""
{tree(80,330,0.7)}
<path d="M120 340q120-60 240-40t180-60" fill="none" stroke="#e6dcc9" stroke-width="26" stroke-linecap="round"/>
{person(200,330,1.05,1,'coral','blue','walk','cap','smile')}
<g transform="translate(300 230) rotate(-8)">
  <path d="M-50-34h100v68h-100z" class="paper"/>
  <path d="M-50 10q30-14 50 0t50-8" fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"/>
</g>
<path d="M60 300L180 180L300 250L420 130L540 200" fill="none" stroke="{TONES['teal'][1]}" stroke-width="0"/>
<path d="M380 260q100-60 160-70" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('advertise', '大きな看板で、商品を宣伝しているイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-180-120h360v200h-360z" class="paper"/>
  <path d="M-140-80h140v120h-140z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M20-60h140M20-20h120M20 20h100"/></g>
  <path d="M-60 80v60M60 80v60" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"/>
</g>
{person(120,346,0.8,1,'teal','blue','point','short','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('advertisement', '新聞の中に、商品の広告欄があるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-150 {-110+i*28}h140"/>' for i in range(9))}</g>
  <path d="M10-110h150v130H10z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M30-70h110M30-40h90"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M10 {40+i*28}h150"/>' for i in range(4))}</g>
</g>
""", ground=True)

add('advocate', '主張を書いた板を掲げて、支持を訴える人のイラスト。', f"""
{person(250,346,1.2,1,'green','blue','up','bun','neutral')}
<g transform="translate(250 170)">
  <path d="M-80-50h160v80h-160z" class="paper"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M-56-24h112M-56 4h80"/></g>
  <path d="M-6 30h12v60H-6z" class="goldd o"/>
</g>
<g opacity=".7">{person(450,346,1.0,1,'teal','gold','up','short','neutral')}</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('afford', '財布の中身で、値札の金額を払えるイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-80-50h160v100h-160z" class="goldd o"/>
  <path d="M-80-20h160" fill="none" stroke="{TONES['gold'][1]}" stroke-width="5"/>
  <g class="goldp o"><circle cx="-30" cy="12" r="18"/><circle cx="10" cy="16" r="18"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-60-36h120v72h-120z" class="paper"/>
  <circle r="16" class="goldp o"/>
</g>
<path d="M290 250h60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M430 340l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('after', '先に起きたことのあとに、次のことが続くイラスト。', f"""
<path d="M60 230h480" class="a" marker-end="url(#ar)"/>
<g fill="{INK}"><circle cx="180" cy="230" r="11"/><circle cx="400" cy="230" r="11"/></g>
<g transform="translate(180 300)"><path d="M-40-24h80v48h-80z" class="tealp o"/></g>
<g transform="translate(400 300)"><path d="M-40-24h80v48h-80z" class="coralp o"/></g>
<path d="M200 160h180" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('aged', '年輪の多い古い木と、若い木を並べたイラスト。', f"""
{tree(160,340,0.6)}
<g transform="translate(420 340)">
  <path d="M-14 0v-110h28V0z" fill="#a08b62" stroke="{INK}" stroke-width="3"/>
  <circle cx="-30" cy="-140" r="46" class="greenp o"/><circle cx="34" cy="-150" r="52" class="greenp o"/><circle cx="0" cy="-186" r="42" class="greenp o"/>
</g>
<path d="M240 200h100" class="a" marker-end="url(#ar)"/>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('allege', '証拠のないまま、相手を指して主張しているイラスト。', f"""
{person(180,346,1.15,1,'coral','blue','point','short','neutral')}
{person(450,346,1.1,-1,'teal','gold','stand','bob','sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><path d="M250 230h100" marker-end="url(#ar)"/></g>
<g transform="translate(300 150)">
  <path d="M-50-30h100v60h-100z" class="muted"/>
  <g class="corals" style="stroke-width:6"><path d="M-20-14l40 30M20-14l-40 30"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('allocate', '一つの山を、三つの箱へ割り当てて分けるイラスト。', f"""
<g transform="translate(300 130)">
  <path d="M-80-40h160l-16 60H-64z" class="paper"/>
  <g class="goldp o"><circle cx="-40" cy="0" r="14"/><circle cx="0" cy="6" r="14"/><circle cx="40" cy="0" r="14"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 200q-60 40-80 80"/><path d="M300 200v80"/><path d="M350 200q60 40 80 80"/></g>
<g transform="translate(150 330)"><path d="M-50-20h100l-12 44H-38z" class="tealp o"/></g>
<g transform="translate(300 330)"><path d="M-50-20h100l-12 44H-38z" class="tealp o"/></g>
<g transform="translate(450 330)"><path d="M-50-20h100l-12 44H-38z" class="tealp o"/></g>
""", ground=False, arrow=True)

add('along', '川に沿って、道が続いていくイラスト。', f"""
<path d="M0 300q120-60 300-20t300-40v160H0z" class="bluep o"/>
<path d="M0 300q120-60 300-20t300-40" class="a"/>
<path d="M0 250q120-60 300-20t300-40" fill="none" stroke="#e6dcc9" stroke-width="24" stroke-linecap="round"/>
{person(200,240,0.75,1,'coral','blue','walk','short','smile')}
<path d="M300 160q120-40 220-60" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('alter', '服の丈を詰めて、形を変えているイラスト。', f"""
<g transform="translate(180 240)">
  <path d="M-60-60h120v30l-16 120h-88l-16-120z" class="tealp o"/>
  <path d="M-60 60h120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"/>
</g>
<g transform="translate(430 240)">
  <path d="M-60-60h120v30l-16 80h-88l-16-80z" class="tealp o"/>
</g>
<path d="M290 240h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(300 340) rotate(20)">
  <path d="M-30 0l60-22M-30 0l60 22" fill="none" stroke="#dfe6ea" stroke-width="8"/>
  <circle cx="-40" cy="-12" r="12" fill="none" stroke="{INK}" stroke-width="4"/>
  <circle cx="-40" cy="12" r="12" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
""", ground=True, arrow=True)

add('amazed', '思いがけない光景に、目を見開いて驚くイラスト。', f"""
<g transform="translate(240 200)">
  <circle r="120" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="-44" cy="-22" r="24" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <circle cx="44" cy="-22" r="24" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <circle cx="-44" cy="-22" r="10" class="ink"/><circle cx="44" cy="-22" r="10" class="ink"/>
  <circle cy="50" r="22" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<g transform="translate(460 200)">
  <path d="M0-70l18 40 44 6-32 30 8 44-38-22-38 22 8-44-32-30 44-6z" class="gold o"/>
</g>
<g class="golds" style="stroke-width:4"><path d="M380 120l24-24M390 290l24 24"/></g>
""", ground=False)

add('amend', '文書の一部を書き直して、修正しているイラスト。', f"""
<g transform="translate(280 240)">
  <path d="M-140-140h280v280h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-100-90h200M-100-50h200M-100 30h200M-100 70h160"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M-110-10h220"/><path d="M-40-26q40-16 80 0"/></g>
</g>
<g transform="translate(430 170) rotate(34)">
  <path d="M-10-90h20v130h-20z" class="coral o"/>
  <path d="M-10 40h20l-10 28z" class="ink"/>
</g>
""", ground=True)

add('analyze', 'データを細かく分けて、内訳を調べているイラスト。', f"""
<g transform="translate(160 240)">
  <circle r="86" class="tealp o"/>
  <path d="M0 0v-86a86 86 0 0 1 74 44z" class="coralp o"/>
  <path d="M0 0l74 44a86 86 0 0 1-74 42z" class="goldp o"/>
</g>
<g transform="translate(430 260)">
  <path d="M-110 60h220" class="a"/>
  <g class="tealp o"><rect x="-90" y="-10" width="40" height="70"/><rect x="-30" y="-60" width="40" height="120"/><rect x="30" y="10" width="40" height="50"/></g>
</g>
<path d="M270 240h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('ancient', '砂に埋もれた古代の石像のイラスト。', f"""
{sun(500,90,42)}
<path d="M0 290q120-40 300-10t300-20v140H0z" fill="#efdcb8" stroke="{INK}" stroke-width="3"/>
<g transform="translate(240 290)">
  <path d="M-60 0v-90h120V0z" fill="#cfc7b8" stroke="{INK}" stroke-width="3"/>
  <path d="M-40-90q40-40 80 0z" fill="#cfc7b8" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><circle cx="-20" cy="-60" r="6"/><circle cx="20" cy="-60" r="6"/></g>
  <path d="M-16-34h32" class="a"/>
</g>
<g fill="#cfc7b8" stroke="{INK}" stroke-width="2.5"><path d="M420 300h60v-40h-60z"/></g>
""", ground=False)

add('annoyed', 'いらだって、眉を寄せている顔のイラスト。', f"""
{face(280,200,120,'flat')}
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M228 154l40 14M332 154l-40 14"/></g>
<g class="corals" opacity=".9" style="stroke-width:5"><path d="M430 170q24 24 24 40t-24 40M470 150q32 32 32 60t-32 60"/></g>
""", ground=False)

add('annoying', '耳ざわりな音が、くり返し鳴り続けているイラスト。', f"""
<g transform="translate(220 220)">
  <path d="M-60-60h120v120h-120z" class="goldp o"/>
  <circle r="32" class="gold o"/>
</g>
<g class="corals" opacity=".95" style="stroke-width:6">
  <path d="M320 160q34 34 34 60t-34 60"/><path d="M370 130q46 46 46 90t-46 90"/><path d="M420 100q58 58 58 120t-58 120"/>
</g>
""", ground=False)

add('annual', 'カレンダーの同じ月に、一年ごとの印がつくイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-120h400v240h-400z" class="paper"/>
  <path d="M-200-120h400v50h-400z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5">
    {''.join(f'<rect x="{-180 + (i%6)*62}" y="{-52 + (i//6)*56}" width="56" height="50"/>' for i in range(12))}
  </g>
  <circle cx="-152" cy="-28" r="16" class="coral o"/>
</g>
<path d="M300 380v-20" class="a"/>
""", ground=True)

add('anticipate', '来るできごとを見越して、先に準備しているイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','think','short','neutral')}
<g class="blues" opacity=".9"><path d="M420 60l-10 30M470 80l-10 30M520 60l-10 30"/></g>
<g transform="translate(400 250)">
  <path d="M-70-40h140v90h-140z" class="coralp o"/>
  <path d="M-70-40q0-40 70-40t70 40z" class="coral o"/>
</g>
<path d="M280 240h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('anybody', '複数の人のうち、どの一人でもよいことを示したイラスト。', f"""
{person(150,346,0.95,1,'teal','blue','stand','short','smile')}
{person(300,346,0.95,1,'coral','gold','stand','bob','smile')}
{person(450,346,0.95,1,'violet','teal','stand','cap','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9">
  <circle cx="150" cy="240" r="52"/><circle cx="300" cy="240" r="52"/><circle cx="450" cy="240" r="52"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('anywhere', '地図上のどの地点でもよいことを、複数の印で示したイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-140h440v280h-440z" class="paper"/>
  <path d="M-220 40q100-40 220 0t220-20" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"/>
  <g>
    {''.join(f'<g transform="translate({-150+i*100} {-60 + (i%2)*90})"><path d="M0 26c-20-26-26-36-26-46a26 26 0 0 1 52 0c0 10-6 20-26 46z" class="coral o"/><circle cy="-22" r="8" fill="#fffdf6"/></g>' for i in range(4))}
  </g>
</g>
""", ground=True)

add('apologize', '頭を下げて、相手にあやまっているイラスト。', f"""
{person(430,346,1.15,-1,'coral','gold','stand','bob','neutral')}
<g transform="translate(200 346)">
  <path d="M-12-8l-7 35M12-8l7 35" fill="none" stroke="{TONES['blue'][2]}" stroke-width="13" stroke-linecap="round"/>
  <path d="M-30-90q30-16 60 0l-10 82h-40z" class="teal o"/>
  <path d="M-26-80l-14 50M26-80l14 50" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <g transform="translate(30 -96) rotate(50)">
    <circle r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <path d="M-26-4q3-28 25-28 24 0 28 25-13-10-27-4-12-11-26 7z" fill="{HAIR}"/>
    <path d="M-10 6h6M8 6h6" class="a"/>
  </g>
</g>
<g transform="translate(300 180)">
  <path d="M-50-30h100q12 0 12 12v30q0 12-12 12h-70l-18 16 4-16q-12 0-12-12v-30q0-12 12-12z" class="paper"/>
  <g fill="{MUTED}"><circle cx="-20" cy="-2" r="4"/><circle cx="0" cy="-2" r="4"/><circle cx="20" cy="-2" r="4"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('app', '画面に並んだアプリの絵記号のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-110-150h220q16 0 16 16v268q0 16-16 16h-220q-16 0-16-16v-268q0-16 16-16z" fill="#dfe6ea" class="o"/>
  <g>
    {''.join(f'<rect x="{-88 + (i%3)*62}" y="{-110 + (i//3)*62}" width="50" height="50" rx="12" fill="{[TONES["coral"][1],TONES["teal"][1],TONES["gold"][1],TONES["violet"][1],TONES["blue"][1],TONES["green"][1]][i%6]}" stroke="{INK}" stroke-width="2.5"/>' for i in range(9))}
  </g>
</g>
""", ground=True)

add('appoint', '役職の札を渡して、任命しているイラスト。', f"""
{person(160,346,1.15,1,'blue','violet','give','short','neutral')}
{person(440,346,1.1,-1,'coral','gold','hold','bob','smile')}
<g transform="translate(300 240)">
  <path d="M-60-40h120v80h-120z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-36-14h72M-36 8h50"/></g>
  <circle cx="34" cy="24" r="10" class="coral o"/>
</g>
<path d="M250 180h100" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('approach', '目標に向かって、少しずつ近づいていくイラスト。', f"""
<g transform="translate(470 230)">
  <circle r="70" fill="none" stroke="{INK}" stroke-width="4"/>
  <circle r="20" class="coral o"/>
</g>
<g opacity=".35">{person(120,346,0.9,1,'teal','blue','walk','short','neutral')}</g>
<g opacity=".65">{person(230,346,0.95,1,'teal','blue','walk','short','neutral')}</g>
{person(340,346,1.0,1,'teal','blue','walk','short','neutral')}
<path d="M120 260h260" class="muted" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('architecture', '柱と屋根の組み方を示した、建築の図のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-190-140h380v280h-380z" class="paper"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4">
    <path d="M-140 100h280"/><path d="M-120 100V-20h240v120"/>
    <path d="M-150-20L0-110l150 90"/>
    <path d="M-60 100V20h120v80"/>
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5" stroke-dasharray="8 7"><path d="M-160 20h320M0-110v210"/></g>
</g>
""", ground=True)
print(' '.join(W)); print(sheet(W))
