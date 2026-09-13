"""第12回: 現れる・祝う・広い・道具など30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('washing', 'たらいで衣類を洗い、洗濯物を干しているイラスト。', f"""
<path d="M40 90h520" fill="none" stroke="{MUTED}" stroke-width="4"/>
<g transform="translate(180 150)">
  <path d="M-60-40l-26 14 10 24 14-8v70h124V-10l14 8 10-24-26-14h-34q-14 12-28 0z" class="tealp o"/>
</g>
<g transform="translate(420 150)">
  <path d="M-40-40h80v100h-80z" class="coralp o"/>
  <path d="M-40-40h80" class="a"/>
</g>
<g transform="translate(300 300)">
  <path d="M-140-40h280l-24 100h-232z" fill="#eef4f8" class="o"/>
  <path d="M-140-40h280" class="a"/>
  <path d="M-120 0h240l-16 60h-208z" class="bluep o"/>
</g>
<g fill="#ffffff" class="o"><circle cx="220" cy="240" r="18"/><circle cx="262" cy="216" r="12"/><circle cx="360" cy="228" r="15"/></g>
""", ground=True)

add('actual', '見取り図の予想と、実際にできあがった形を並べて比べたイラスト。', f"""
<g transform="translate(160 220)">
  <path d="M-110-110h220v220h-220z" class="paper"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3" stroke-dasharray="8 7"><path d="M-70-60h140v120h-140z"/><path d="M-70 0h140M0-60v120"/></g>
</g>
{building(430,300,1.05,'teal')}
<path d="M290 200h80" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M480 130l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('addition', '三つ積んだ箱の上に、もう一つ足しているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="greenp"/>
{box(260,330,110,60,0,'gold')}
{box(260,272,110,60,0,'gold')}
{box(260,214,110,60,0,'gold')}
<g transform="translate(260 110)">{box(0,0,110,60,0,'green')}</g>
<path d="M260 156v26" class="a" marker-end="url(#ar)"/>
<g class="greens" style="stroke-width:8"><path d="M440 240h60M470 210v60"/></g>
""", ground=True, arrow=True)

add('affordable', '値札の数字が小さく、財布のお金で無理なく買えるイラスト。', f"""
<g transform="translate(200 230)">
  <path d="M-90-70h180v140h-180z" class="tealp o"/>
  <g transform="translate(60 60)">
    <path d="M-40-24h80v48h-80z" class="paper"/>
    <circle r="12" class="goldp o"/>
  </g>
</g>
<g transform="translate(430 280)">
  <path d="M-80-50h160v100h-160z" class="goldd o"/>
  <path d="M-80-20h160" fill="none" stroke="{TONES['gold'][1]}" stroke-width="5"/>
  <g class="goldp o"><circle cx="-30" cy="10" r="18"/><circle cx="10" cy="14" r="18"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M290 150l18 18 30-36"/></g>
<path d="M340 280h-40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('allow', '開いたゲートを通してよいと示され、人が通り抜けるイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-140-100h30v200h-30zM110-100h30v200h-30z" class="goldd o"/>
  <g transform="rotate(-70 -110 -80)"><path d="M-110-90h110v20h-110z" class="goldp o"/></g>
  <g transform="rotate(70 110 -80)"><path d="M0-90h110v20H0z" class="goldp o"/></g>
</g>
{person(300,336,0.9,1,'teal','blue','walk','short','smile')}
<path d="M300 160V90" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M460 150l20 20 34-40"/></g>
""", ground=True, arrow=True)

add('alternative', '通れない道の代わりに、別の道を選んで進むイラスト。', f"""
<circle cx="80" cy="200" r="24" class="teal o"/>
<path d="M110 180q120-70 220-70t180 40" class="muted"/>
<g class="corals" style="stroke-width:8"><path d="M300 80l40 40M340 80l-40 40"/></g>
<path d="M110 220q120 90 220 90t180-60" fill="none" stroke="{TONES['green'][0]}" stroke-width="12" stroke-linecap="round" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('amount', '同じ容器に入った液体の量の違いを、目盛りで比べたイラスト。', f"""
<g transform="translate(160 250)">
  <path d="M-70-110h140l-10 220h-120z" fill="#f4fbff" class="o"/>
  <path d="M-64-60h128l-8 170h-112z" class="bluep o"/>
  <path d="M-64-60h128" class="a"/>
</g>
<g transform="translate(420 250)">
  <path d="M-70-110h140l-10 220h-120z" fill="#f4fbff" class="o"/>
  <path d="M-56 40h112l-4 70h-104z" class="bluep o"/>
  <path d="M-56 40h112" class="a"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="2.5"><path d="M76 180h24M76 120h24M76 60h24M336 180h24M336 120h24M336 60h24"/></g>
""", ground=True)

add('appear', '幕の後ろから、人が前に出て姿を見せるイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-260-160h180v320h-180zM80-160h180v320H80z" class="coralp o"/>
  <path d="M-80-160v320M80-160v320" class="a"/>
</g>
{person(300,336,1.05,1,'teal','blue','walk','short','smile')}
<path d="M300 130V80" class="a" marker-end="url(#ar)"/>
<g class="golds" style="stroke-width:4"><path d="M370 160l26-26M230 160l-26-26"/></g>
""", ground=True, arrow=True)

add('appearance', '同じ人の服装と髪型を変えて、見た目の違いを並べたイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','stand','short','smile')}
{person(420,346,1.15,1,'coral','violet','stand','bun','smile')}
<path d="M300 130v200" class="muted"/>
<g fill="none" stroke="{INK}" stroke-width="4"><circle cx="180" cy="140" r="26"/><circle cx="420" cy="140" r="26"/></g>
<path d="M180 174v20M420 174v20" class="a"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('apply', '応募書類に記入して、受付の箱へ差し出しているイラスト。', f"""
{person(150,346,1.1,1,'coral','blue','give','bob','neutral')}
<g transform="translate(290 250) rotate(-6)">
  <path d="M-70-90h140v180h-140z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-46-56h92M-46-30h92M-46-4h70"/></g>
  <g fill="none" stroke="{INK}" stroke-width="2.5"><rect x="-46" y="30" width="30" height="30"/></g>
</g>
<g transform="translate(460 300)">
  <path d="M-80-50h160v100h-160z" class="tealp o"/>
  <path d="M-40-50h80v-10h-80z" class="ink"/>
</g>
<path d="M370 200h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('arrangement', 'ばらばらの花を、花びんの中にきれいに配置しているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="violetp"/>
<g transform="translate(320 300)">
  <path d="M-50-60h100l-14 120h-72z" class="tealp o"/>
  <path d="M-50-60h100" class="a"/>
  <g>
    <path d="M-20-60v-70M0-60v-90M22-60v-76" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
    <circle cx="-20" cy="-136" r="20" class="coral o"/>
    <circle cx="0" cy="-156" r="20" class="violet o"/>
    <circle cx="22" cy="-142" r="20" class="gold o"/>
  </g>
</g>
<g transform="translate(140 300) rotate(-24)">
  <path d="M0 0v-60" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
  <circle cy="-66" r="18" class="coral o"/>
</g>
<path d="M200 250q40-30 74-18" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('artistic', '絵筆と絵の具で、独創的な模様を描いているイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-140-120h280v240h-280z" class="paper"/>
  <path d="M-110 60q40-140 110-40t100-60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="12" stroke-linecap="round"/>
  <circle cx="-50" cy="-60" r="26" class="violetp o"/>
  <path d="M40-90l40 60h-80z" class="goldp o"/>
</g>
<g transform="translate(440 130) rotate(40)">
  <path d="M-60-8h100v16H-60z" class="goldd o"/>
  <path d="M40-12h26v24H40z" class="teal o"/>
</g>
<path d="M120 360h360" class="a"/>
""", ground=True)

add('attack', '前へ突き進んで、相手の陣地へ攻めかかるイラスト。', f"""
{person(180,346,1.15,1,'coral','blue','point','cap','neutral')}
<g transform="translate(460 260)">
  <path d="M-70-60h140v120h-140z" class="tealp o"/>
  <path d="M-70-60h140" class="a"/>
</g>
<g class="corals" marker-end="url(#ar)" style="stroke-width:7">
  <path d="M270 200h100"/><path d="M270 260h100"/><path d="M270 320h100"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('awkward', '差し出された手に応じられず、気まずく立っている二人のイラスト。', f"""
{person(190,346,1.1,1,'coral','blue','give','short','neutral')}
{person(420,346,1.1,-1,'violet','gold','stand','bob','sad')}
<circle cx="270" cy="256" r="14" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M320 220h40M320 240h30"/></g>
<g class="muted"><path d="M340 160v30M370 150v30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('beat', '太鼓を手で打って、音を出しているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="coralp"/>
<g transform="translate(320 280)">
  <ellipse cy="-60" rx="110" ry="34" fill="#fffdf6" class="o"/>
  <path d="M-110-60v60q0 34 110 34t110-34v-60" class="coral o"/>
  <ellipse cy="-60" rx="110" ry="34" fill="#fffdf6" class="o"/>
  <ellipse cy="-60" rx="80" ry="22" class="coralp o"/>
</g>
{hand(300,140,1)}
<path d="M300 180v40" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:4"><path d="M460 200q26 26 26 40M480 180q34 34 34 56"/></g>
""", ground=True, arrow=True)

add('bilingual', '一人の人の頭から、二つの言語の吹き出しが出ているイラスト。', f"""
{person(300,346,1.2,1,'teal','blue','stand','short','smile')}
<g transform="translate(140 190)">
  <path d="M-70-40h140q14 0 14 14v40q0 14-14 14h-84l-26 22 6-22h-36q-14 0-14-14v-40q0-14 14-14z" class="paper"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M-40-14h80M-40 6h50"/></g>
</g>
<g transform="translate(460 190)">
  <path d="M70-40H-70q-14 0-14 14v40q0 14 14 14h84l26 22-6-22h36q14 0 14-14v-40q0-14-14-14z" class="paper"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"><path d="M-40-14h80M-10 6h50"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('blind', '目を布で覆われ、手さぐりで進んでいる人のイラスト。', f"""
{person(260,346,1.2,1,'violet','blue','point','short','neutral')}
<g transform="translate(260 232)">
  <path d="M-30-8h60v18h-60z" class="ink"/>
</g>
<path d="M340 250l70 6" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<g transform="translate(470 300)">{box(0,0,80,60,0,'gold')}</g>
<g class="muted"><path d="M370 200q30-20 60-14"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('board', '長机を囲んで会議をしている数人のイラスト。', f"""
<g transform="translate(300 300)">
  <ellipse rx="180" ry="60" class="goldp o"/>
  <ellipse rx="180" ry="60" fill="none" class="a"/>
</g>
{person(140,280,0.62,1,'teal','blue','stand','short','neutral')}
{person(300,250,0.62,1,'coral','gold','stand','bob','neutral')}
{person(460,280,0.62,-1,'violet','teal','stand','cap','neutral')}
<g transform="translate(300 296)">
  <path d="M-40-14h80v20h-80z" class="paper"/>
</g>
""", ground=True)

add('book', 'カレンダーの日付に印をつけて、席を予約しているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="tealp"/>
<g transform="translate(320 230)">
  <path d="M-130-120h260v240h-260z" class="paper"/>
  <path d="M-130-120h260v50h-260z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5">
    {''.join(f'<rect x="{-110 + i%5*44}" y="{-56 + i//5*46}" width="40" height="40"/>' for i in range(15))}
  </g>
  <circle cx="24" cy="12" r="24" class="coral o"/>
</g>
{hand(150,240,1)}
<path d="M210 240h20" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('brief', '長い文章を短くまとめて、要点だけにしたイラスト。', f"""
<g transform="translate(160 220)">
  <path d="M-100-140h200v280h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M-70 {-100+i*24}h140"/>' for i in range(9))}
  </g>
</g>
<g transform="translate(430 220)">
  <path d="M-90-70h180v140h-180z" class="paper"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M-60-30h120M-60 0h100M-60 30h70"/></g>
</g>
<path d="M280 220h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('broad', '端から端までが広い階段状の道を、幅を示す矢印とともに描いたイラスト。', f"""
<path d="M60 200h480v120H60z" class="tealp o"/>
<path d="M60 200h480" class="a"/>
<path d="M70 360h460" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
{person(300,200,0.55,1,'coral','blue','walk','short','smile')}
<path d="M120 260h360" class="muted"/>
""", ground=False, arrow=True)

add('brush', '毛の束が付いたブラシで、表面をこすっているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g transform="translate(280 200) rotate(12)">
  <path d="M-90-30h180v34h-180z" class="goldd o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">
    {''.join(f'<path d="M{-80+i*16} 4v40"/>' for i in range(11))}
  </g>
</g>
<path d="M120 300h360" fill="none" stroke="#e6dcc9" stroke-width="26" stroke-linecap="round"/>
<path d="M200 340h180" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('camp', '野外にテントを張り、たき火を囲んでいるイラスト。', f"""
{tree(90,330,0.8)}{tree(520,330,0.7)}
<g transform="translate(220 330)">
  <path d="M-90 0L0-130 90 0z" class="tealp o"/>
  <path d="M0-130L-30 0h60z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
</g>
{flame(400,326,1.1)}
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="10" stroke-linecap="round"><path d="M360 340l80-20M440 340l-80-20"/></g>
""", ground=True)

add('cap', 'つばのある帽子を横から見たイラスト。', f"""
<circle cx="470" cy="100" r="56" class="bluep"/>
<g transform="translate(270 250)">
  <path d="M-80 0a80 60 0 0 1 160 0z" class="blue o"/>
  <path d="M80 0h80q0 20-20 20H80z" class="blued o"/>
  <circle cy="-58" r="8" class="bluep o"/>
  <path d="M-80 0h160v14h-160z" class="blued o"/>
</g>
<path d="M120 320h340" class="a"/>
""", ground=True)

add('care', '弱った苗にそっと水をやり、気をつけて世話をしているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="greenp"/>
{hand(180,180,1)}
<g transform="translate(300 200) rotate(28)">
  <path d="M-40-30h80l-8 60h-64z" class="tealp o"/>
  <path d="M40-24h40l20-14-60-6z" class="teal o"/>
</g>
<g stroke-linecap="round" fill="none"><path d="M356 224q20 30 22 60" stroke="{TONES['blue'][0]}" stroke-width="8"/></g>
<g transform="translate(390 330)">
  <path d="M0 0v-60" fill="none" stroke="{TONES['green'][2]}" stroke-width="7" stroke-linecap="round"/>
  <path d="M0-34c-34-8-44-30-44-30 30-8 44 30 44 30z" class="green o"/>
  <path d="M0-50c34-8 44-30 44-30-30-8-44 30-44 30z" class="green o"/>
</g>
<g transform="translate(468 250)"><path d="M0 20l-24-30 12-14 12 12 12-12 12 14z" class="coral o"/></g>
""", ground=True)

add('celebrate', '紙ふぶきの中で、両手を上げて祝っている人たちのイラスト。', f"""
<g fill="none">
  {''.join(f'<rect x="{60+i*46}" y="{80 + (i%4)*40}" width="16" height="10" fill="{[TONES["coral"][0],TONES["gold"][0],TONES["teal"][0],TONES["violet"][0]][i%4]}" transform="rotate({i*37} {68+i*46} {85+(i%4)*40})"/>' for i in range(11))}
</g>
{person(180,346,1.1,1,'coral','blue','up','bob','smile')}
{person(300,346,1.15,1,'teal','gold','up','short','smile')}
{person(420,346,1.1,1,'violet','teal','up','cap','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('chain', '輪がつながって一本の鎖になっているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="tealp"/>
<g fill="none" stroke="{MUTED}" stroke-width="12">
  {''.join(f'<ellipse cx="{110+i*62}" cy="{230 + (0 if i%2 else 0)}" rx="38" ry="24" transform="rotate({0 if i%2 else 90} {110+i*62} 230)"/>' for i in range(7))}
</g>
<path d="M120 330h360" class="muted"/>
""", ground=True)

add('chat', '二人が向かい合って、気軽に言葉をやりとりしているイラスト。', f"""
{person(170,346,1.1,1,'teal','blue','stand','short','smile')}
{person(430,346,1.1,-1,'coral','gold','stand','bob','smile')}
<g transform="translate(240 180)">
  <path d="M-60-36h120q14 0 14 14v36q0 14-14 14h-90l-22 20 6-20h-14q-14 0-14-14v-36q0-14 14-14z" class="paper"/>
  <g fill="{MUTED}"><circle cx="-24" cy="0" r="4"/><circle cx="0" cy="0" r="4"/><circle cx="24" cy="0" r="4"/></g>
</g>
<g transform="translate(390 250)">
  <path d="M60-30H-60q-14 0-14 14v30q0 14 14 14h90l22 18-6-18h14q14 0 14-14v-30q0-14-14-14z" class="paper"/>
  <g fill="{MUTED}"><circle cx="-20" cy="0" r="4"/><circle cx="4" cy="0" r="4"/><circle cx="28" cy="0" r="4"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('circle', 'コンパスで描いた一つの円のイラスト。', f"""
<circle cx="300" cy="220" r="130" fill="none" stroke="{TONES['teal'][0]}" stroke-width="12"/>
<circle cx="300" cy="220" r="7" class="ink"/>
<path d="M300 220l92-92" class="muted" marker-end="url(#ar)"/>
<path d="M300 220h130" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('clue', '虫めがねで、地面に残った手がかりの足跡を調べているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="violetp"/>
<g fill="#c9bda6">
  <ellipse cx="200" cy="330" rx="12" ry="18"/><ellipse cx="240" cy="300" rx="11" ry="17"/><ellipse cx="278" cy="272" rx="10" ry="15"/>
</g>
<g transform="translate(330 250)">
  <circle r="80" fill="#e8f4fb" opacity=".35"/>
  <ellipse cx="10" cy="10" rx="14" ry="22" fill="#c9bda6"/>
  <circle r="80" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M58 58l60 60" fill="none" stroke="{INK}" stroke-width="14" stroke-linecap="round"/>
</g>
""", ground=True)
print(' '.join(W)); print(sheet(W))
