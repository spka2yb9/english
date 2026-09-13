"""第42回: 指導・維持・製造・記憶など40語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('leader', '列の先頭に立って、全体を導く人のイラスト。', f"""
{person(160,346,1.25,1,'coral','blue','walk','cap','neutral')}
{person(310,346,0.95,1,'teal','gold','walk','bob','neutral')}
{person(420,346,0.95,1,'violet','teal','walk','short','neutral')}
<circle cx="160" cy="220" r="52" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M100 260h-40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('leading', '複数の棒の中で、いちばん先頭に立つ棒のイラスト。', f"""
<path d="M60 340h480" class="a"/>
<g class="tealp o"><rect x="130" y="240" width="70" height="100"/><rect x="220" y="270" width="70" height="70"/><rect x="400" y="260" width="70" height="80"/></g>
<rect x="310" y="140" width="70" height="200" class="coral o"/>
<g class="golds" style="stroke-width:5"><path d="M345 120V90"/></g>
""", ground=False)

add('learning', '本を読みながら、知識を身につけていくイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','carry','bob','smile')}
<g transform="translate(180 268)">
  <path d="M-46-30h92v60h-92z" class="tealp o"/>
  <path d="M-30-30h12v60h-12z" class="teal o"/>
</g>
<g transform="translate(420 220)">
  <circle r="40" class="goldp o"/>
  <path d="M-16 40h32v14h-32z" class="ink"/>
  <g class="golds" style="stroke-width:4"><path d="M0-56v-16M-44-30l-14-10M44-30l14-10"/></g>
</g>
<path d="M280 220h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('least', '並んだ量のうち、いちばん少ないものを示したイラスト。', f"""
<path d="M60 340h480" class="a"/>
<g class="tealp o"><rect x="120" y="180" width="70" height="160"/><rect x="220" y="220" width="70" height="120"/><rect x="420" y="200" width="70" height="140"/></g>
<rect x="320" y="300" width="70" height="40" class="coral o"/>
<path d="M355 380v-30" class="a" marker-end="url(#ar)" transform="rotate(180 355 365)"/>
""", ground=False, arrow=True)

add('less', '二つの量を比べて、少ない方を示したイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-70-100h140l-12 200h-116z" fill="#f7fbfe" class="o"/>
  <path d="M-64-60h128l-8 160h-112z" class="bluep o"/>
</g>
<g transform="translate(430 250)">
  <path d="M-70-100h140l-12 200h-116z" fill="#f7fbfe" class="o"/>
  <path d="M-50 40h100l-4 60h-92z" class="bluep o"/>
</g>
<path d="M300 130v220" class="muted"/>
<g fill="{INK}"><path d="M470 130l-40 20 40 20v-40z" opacity=".0"/></g>
<path d="M340 350h120" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('lifestyle', '一日の過ごし方を、輪にして示したイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="10"><circle cx="300" cy="220" r="130" stroke-dasharray="20 14"/></g>
{sun(300,90,26)}
<g transform="translate(430 220)"><path d="M-36-36h72v72h-72z" class="goldp o"/></g>
<g transform="translate(300 350)"><path d="M-40-18h80v36h-80z" class="tealp o"/></g>
<g transform="translate(170 220)"><circle r="28" class="violetp o"/></g>
<path d="M380 120a140 140 0 0 1 40 60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('likely', '二つの道のうち、太い線の方が起こりやすいイラスト。', f"""
<circle cx="90" cy="230" r="22" class="teal o"/>
<path d="M120 210q120-80 220-60t140 20" fill="none" stroke="{TONES['teal'][0]}" stroke-width="14" stroke-linecap="round" marker-end="url(#ar)"/>
<path d="M120 250q120 80 220 60t140-20" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('line', '人が一列に並んだ、まっすぐな列のイラスト。', f"""
{person(130,346,0.9,1,'teal','blue','stand','short','neutral')}
{person(230,346,0.9,1,'coral','gold','stand','bob','neutral')}
{person(330,346,0.9,1,'violet','teal','stand','cap','neutral')}
{person(430,346,0.9,1,'gold','blue','stand','short','neutral')}
<path d="M100 250h380" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('linger', '人が去ったあとも、一人だけ残っているイラスト。', f"""
<g opacity=".25">{person(150,346,1.0,1,'teal','blue','walk','short','neutral')}{person(240,346,1.0,1,'coral','gold','walk','bob','neutral')}</g>
{person(430,346,1.1,1,'violet','blue','stand','short','neutral')}
<g class="muted" marker-end="url(#ar)"><path d="M200 240h-120"/></g>
<circle cx="430" cy="230" r="56" fill="none" stroke={'"'+TONES['violet'][0]+'"'} stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('literally', '書かれた語の通りに、そのままの絵で示したイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-90-60h180v120h-180z" class="paper"/>
  <g fill="{INK}"><rect x="-60" y="-14" width="120" height="12"/></g>
</g>
<g transform="translate(430 230)">
  <circle r="70" class="tealp o"/>
  <path d="M-40 0h80" fill="none" stroke="{TONES['teal'][0]}" stroke-width="10"/>
</g>
<path d="M290 230h60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 130l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('live', '生放送の印がついた画面のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-180-130h360v260h-360z" fill="#dfe6ea" class="o"/>
  <path d="M-150-100h300v200h-300z" class="bluep o"/>
  <g transform="translate(0 20) scale(0.55)">{person(0,60,1.0,1,'coral','gold','up','bob','smile')}</g>
  <g class="coral o"><circle cx="-110" cy="-70" r="16"/></g>
</g>
<g class="corals" opacity=".9" style="stroke-width:4"><path d="M480 180q26 26 26 50t-26 50"/></g>
""", ground=True)

add('lobby', '建物の入口にある、広い待合の空間のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-220-140h440v280h-440z" fill="#fffdf6" class="o"/>
  <path d="M-220-140h440v40h-440z" class="teal o"/>
  <g class="goldp o"><rect x="-180" y="40" width="120" height="20"/><rect x="60" y="40" width="120" height="20"/></g>
  <path d="M-40 140V60h80v80z" class="goldd o"/>
</g>
{person(180,340,0.8,1,'coral','blue','stand','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('located', '地図上のある地点に、位置が示されているイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <path d="M-200 40q100-40 200 0t200-20" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"/>
  <g class="greenp o"><rect x="-160" y="-100" width="120" height="70"/></g>
</g>
<g transform="translate(340 200)">
  <path d="M0 40c-30-40-40-56-40-72a40 40 0 0 1 80 0c0 16-10 32-40 72z" class="coral o"/>
  <circle cy="-34" r="13" fill="#fffdf6"/>
</g>
""", ground=True)

add('log', '出来事を日付ごとに書き留めた記録のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-160-140h320v280h-320z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-120 {-90+i*40}h240"/>' for i in range(5))}</g>
  <g fill="{INK}">{''.join(f'<rect x="-110" y="{-104+i*40}" width="50" height="8"/>' for i in range(5))}</g>
</g>
""", ground=True)

add('lonely', '広い場所に、たった一人でいるイラスト。', f"""
{person(300,346,1.15,1,'violet','blue','stand','short','sad')}
<g class="muted"><path d="M80 240h140M380 240h140"/></g>
{drop(340,240,0.8)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('look', '目を向けて、対象を見ているイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','stand','short','neutral')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><path d="M230 220h180" marker-end="url(#ar)"/></g>
<g transform="translate(460 220)">
  <ellipse rx="46" ry="30" fill="#fffdf6" class="o"/>
  <circle r="14" class="ink"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('loom', '霧の向こうに、大きな影がぼんやり現れるイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#e7eef4"/>
<g fill="#b9c4cf" opacity=".85"><path d="M300 340q-40-160 60-190 70-22 110 30 46 56-24 160z"/></g>
<g opacity=".55"><path d="M0 120h600v200H0z" fill="#ffffff"/></g>
{person(150,350,1.0,1,'coral','blue','stand','short','surprised')}
<path d="M230 250h60" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('loose', 'ゆるんで、すきまのできたねじのイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-140-40h280v80h-280z" class="goldp o"/>
  <g fill="none" stroke="{INK}" stroke-width="4"><circle cx="-90" r="16"/></g>
  <g transform="translate(90 -20) rotate(20)">
    <circle r="16" fill="none" stroke="{INK}" stroke-width="4"/>
    <path d="M-8-8l16 16M-8 8l16-16" fill="none" stroke="{INK}" stroke-width="3"/>
  </g>
</g>
<g class="corals" style="stroke-width:5"><path d="M420 180l24-24"/></g>
<path d="M120 350h360" class="a"/>
""", ground=True)

add('lorry', '荷台に荷を積んだ大型トラックのイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-200 40h130v-120h-130z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <path d="M-70 40h270v-90H-70z" class="tealp o"/>
  <path d="M-190-60h100v40h-100z" class="bluep o"/>
  <circle cx="-150" cy="52" r="30" class="ink"/><circle cx="70" cy="52" r="30" class="ink"/><circle cx="150" cy="52" r="30" class="ink"/>
</g>
<path d="M60 330h480" class="a"/>
""", ground=True)

add('lower', '高かった位置を、下へ下げるイラスト。', f"""
<g transform="translate(200 180)"><path d="M-70-30h140v60h-140z" class="tealp o"/></g>
<g transform="translate(430 300)"><path d="M-70-30h140v60h-140z" class="teal o"/></g>
<path d="M300 200L400 280" class="a" marker-end="url(#ar)"/>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('luck', '四つ葉のクローバーとサイコロで、運を示したイラスト。', f"""
<g transform="translate(200 240)">
  <g class="green o">
    <ellipse cy="-36" rx="28" ry="34"/><ellipse cx="36" rx="34" ry="28"/><ellipse cy="36" rx="28" ry="34"/><ellipse cx="-36" rx="34" ry="28"/>
  </g>
  <path d="M0 36v54" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
</g>
<g transform="translate(430 270)">
  <path d="M-50-50h100v100h-100z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><circle cx="-24" cy="-24" r="7"/><circle cx="24" cy="-24" r="7"/><circle cx="0" cy="0" r="7"/><circle cx="-24" cy="24" r="7"/><circle cx="24" cy="24" r="7"/></g>
</g>
<path d="M120 350h360" class="a"/>
""", ground=True)

add('mad', '顔を赤くして、激しく怒っている人のイラスト。', f"""
{face(280,200,120,'flat')}
<g fill="none" stroke="{INK}" stroke-width="7"><path d="M226 150l42 16M334 150l-42 16"/></g>
<circle cx="196" cy="230" r="24" class="coralp"/><circle cx="364" cy="230" r="24" class="coralp"/>
<g class="corals" opacity=".9" style="stroke-width:5"><path d="M420 150q26 26 26 40t-26 40M460 130q34 34 34 60t-34 60"/></g>
""", ground=False)

add('maintain', '設備に手入れをして、状態を保つイラスト。', f"""
<g transform="translate(380 250)">
  <path d="M-110-90h220v180h-220z" fill="#dfe6ea" class="o"/>
  <circle cx="-40" cy="-20" r="40" fill="none" stroke="{INK}" stroke-width="12"/>
  <g class="green o"><circle cx="70" cy="50" r="12"/></g>
</g>
<g transform="translate(200 240) rotate(-20)">
  <path d="M-26-70q-16-26 4-38 20-12 40 0 20 12 6 38l-12 12h-26z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-11-58h22v130h-22z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M480 140l18 18 30-36"/></g>
""", ground=True)

add('manage', '複数の作業を見て、全体を管理しているイラスト。', f"""
{person(160,346,1.2,1,'blue','violet','point','short','neutral')}
<g transform="translate(410 250)">
  <path d="M-120-90h240v180h-240z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-90-50h180M-90-10h180M-90 30h140"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"><path d="M-110-56l12 12 20-24M-110-16l12 12 20-24"/></g>
</g>
<path d="M250 220h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('manager', '現場を見回って、指示を出す責任者のイラスト。', f"""
{person(170,346,1.25,1,'blue','blue','point','short','neutral')}
<g transform="translate(170 258)">
  <path d="M-40-24h80v6h-80z" class="paper"/>
  <path d="M-12-20l12 18 12-18z" class="ink"/>
</g>
<g opacity=".8">{person(400,346,0.95,-1,'gold','blue','point','cap','neutral')}{person(500,346,0.95,-1,'teal','gold','point','bob','neutral')}</g>
<path d="M250 220h80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('manifest', '隠れていた印が、はっきり表に現れるイラスト。', f"""
<g transform="translate(170 230)" opacity=".3">
  <path d="M-80-70h160v140h-160z" class="paper"/>
  <circle r="34" class="muted"/>
</g>
<g transform="translate(430 230)">
  <path d="M-80-70h160v140h-160z" class="paper"/>
  <circle r="40" class="coral o"/>
</g>
<path d="M280 230h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('manipulate', '糸で人形を操って、動かしているイラスト。', f"""
{hand(300,120,1)}
<g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M270 160v70M330 160v70M300 160v50"/></g>
<g transform="translate(300 300)">
  <path d="M-30-70q30-14 60 0l-8 68h-44z" class="violet o"/>
  <path d="M-26-60l-40 20M26-60l40 20" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
  <path d="M-14-2l-16 44M14-2l16 44" fill="none" stroke="{TONES['violet'][2]}" stroke-width="11" stroke-linecap="round"/>
  <circle cx="0" cy="-96" r="22" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('manner', '姿勢を正して、丁寧な態度を示すイラスト。', f"""
{person(200,346,1.2,1,'blue','blue','stand','short','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M290 200l18 18 30-36"/></g>
<g transform="translate(450 346) rotate(18)">{person(0,0,1.1,1,'coral','gold','up','bob','neutral')}</g>
<g class="corals" style="stroke-width:7"><path d="M400 180l30 30M430 180l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('manufacture', '工場の流れ作業で、製品が作られるイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-240-20h480v40h-480z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-160-20v40M-80-20v40M0-20v40M80-20v40M160-20v40"/></g>
</g>
<g transform="translate(180 250)"><path d="M-30-30h60v60h-60z" class="tealp o"/></g>
<g transform="translate(320 250)"><path d="M-30-30h60v60h-60z" class="teal o"/></g>
<g transform="translate(460 250)">{box(0,0,70,60,0,'gold')}</g>
<path d="M120 160h360" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('map', '地形と道が描かれた地図のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-140h440v280h-440z" class="paper"/>
  <path d="M-220 40q110-40 220 0t220-20" fill="none" stroke="{TONES['blue'][0]}" stroke-width="5"/>
  <path d="M-180-40q120-60 220 0t180-20" fill="none" stroke="#e6dcc9" stroke-width="12"/>
  <g class="greenp o"><rect x="-190" y="-120" width="120" height="60"/></g>
  <g class="goldp o"><rect x="60" y="60" width="140" height="60"/></g>
</g>
""", ground=True)

add('march', 'そろった足取りで、隊列が行進するイラスト。', f"""
{person(140,346,1.0,1,'green','green','walk','cap','neutral')}
{person(250,346,1.0,1,'green','green','walk','cap','neutral')}
{person(360,346,1.0,1,'green','green','walk','cap','neutral')}
{person(470,346,1.0,1,'green','green','walk','cap','neutral')}
<path d="M520 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('master', '難しい技を完全に身につけた人のイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','point','short','smile')}
<g transform="translate(200 150)"><path d="M0-30l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" class="gold o"/></g>
<g transform="translate(420 250)">
  <path d="M-90-70h180v140h-180z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"><path d="M-60-40h120M-60-10h120M-60 20h90"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M290 170l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('mate', '肩を並べた仲間二人のイラスト。', f"""
{person(240,346,1.15,1,'teal','blue','give','short','smile')}
{person(360,346,1.15,-1,'coral','gold','give','bob','smile')}
<path d="M290 250h20" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('material', '布や木など、作るための材料が並んだイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-220-20h440v20h-440z" class="goldp o"/>
</g>
<g transform="translate(150 250)">
  <path d="M-70-40h140v60h-140z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3"><path d="M-70-20h140M-70 0h140"/></g>
</g>
<g transform="translate(310 250)"><path d="M-60-40h120v60h-120z" class="goldd o"/></g>
<g transform="translate(460 250)"><path d="M-50-40h100v60h-100z" fill="#dfe6ea" class="o"/></g>
""", ground=True)

add('mathematics', '数式と図形が並んだ、数学のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <g fill="{INK}"><rect x="-140" y="-100" width="60" height="10"/><rect x="-60" y="-104" width="10" height="18"/><rect x="-65" y="-100" width="20" height="10"/><rect x="-20" y="-100" width="60" height="10"/></g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><circle cx="-90" cy="20" r="50"/><path d="M20-30h120v120H20z"/></g>
  <path d="M60 60l40-70 40 70z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
</g>
""", ground=True)

add('maths', '筆算を解いている、算数のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-160-140h320v280h-320z" class="paper"/>
  <g fill="{INK}">
    <rect x="-40" y="-100" width="90" height="10"/>
    <rect x="-70" y="-56" width="10" height="24"/><rect x="-75" y="-49" width="20" height="10"/>
    <rect x="-40" y="-50" width="90" height="10"/>
    <rect x="-110" y="-10" width="180" height="6"/>
    <rect x="-40" y="20" width="90" height="10"/>
  </g>
</g>
<g transform="translate(470 300) rotate(30)"><path d="M-10-70h20v100h-20z" class="coral o"/><path d="M-10 30h20l-10 24z" class="ink"/></g>
""", ground=True)

add('media', 'テレビ・新聞・電話の画面が並んだメディアのイラスト。', f"""
<g transform="translate(140 250)">
  <path d="M-90-70h180v130h-180z" fill="#dfe6ea" class="o"/>
  <path d="M-70-50h140v90h-140z" class="bluep o"/>
</g>
<g transform="translate(320 250)">
  <path d="M-80-80h160v160h-160z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-56-50h112M-56-20h112M-56 10h80"/></g>
</g>
<g transform="translate(470 250)">
  <path d="M-50-90h100v180h-100z" fill="#dfe6ea" class="o"/>
  <path d="M-36-70h72v130h-72z" class="tealp o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('medicine', '聴診器と薬で、医学を示したイラスト。', f"""
<g transform="translate(200 250)">
  <circle cy="60" r="30" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M0 30q-46-28-46-76" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-46-50q-28 0-28-28M-46-50q28 0 28-28" fill="none" stroke="{INK}" stroke-width="7"/>
</g>
<g transform="translate(430 260)">
  <path d="M-50-70h100l-8 140h-84z" fill="#f4fbff" class="o"/>
  <path d="M-44-20h88l-6 90h-76z" class="coralp o"/>
  <path d="M-24-80h48v14h-48z" class="ink"/>
</g>
<g transform="translate(430 140)"><path d="M-10-26h20v16h16v20h-16v16h-20v-16h-16v-20h16z" class="coral o"/></g>
<path d="M120 360h360" class="a"/>
""", ground=True)

add('memory', '頭の中に、過去の場面が保たれているイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','think','short','smile')}
<g transform="translate(420 200)">
  <path d="M-120-60q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-156q-38-4-36-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 10) scale(0.55)">
    <path d="M-80-40h160v100h-160z" class="paper"/>
    <path d="M-56 40l40-60 30 30 30-40 22 70z" class="tealp o"/>
  </g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="290" cy="280" r="12"/><circle cx="264" cy="306" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('mental', '頭の中で考えが働いていることを示したイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','think','short','neutral')}
<g transform="translate(420 200)">
  <path d="M0-100q90 0 90 80 0 70-90 70t-90-70q0-80 90-80z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"><path d="M0-96v126M-46-80q30 26 0 52t20 52M46-80q-30 26 0 52t-20 52"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)
print(len(W), ' '.join(W)); print(sheet(W))
