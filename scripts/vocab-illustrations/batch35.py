"""第35回: 削除・出発・検出・失望など44語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('defy', '止める指示に逆らって、逆の方向へ進むイラスト。', f"""
{person(430,346,1.15,-1,'blue','violet','point','cap','neutral')}
{person(190,346,1.15,1,'coral','blue','walk','short','neutral')}
<path d="M340 230H270" class="a" marker-end="url(#ar)"/>
<path d="M120 300h-60" class="a" marker-end="url(#ar)" style="stroke-width:7"/>
<g class="corals" style="stroke-width:7"><path d="M280 160l30 30M310 160l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('delete', '一覧から一行を選んで、消し去るイラスト。', f"""
<g transform="translate(280 240)">
  <path d="M-140-140h280v280h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-100-90h200M-100 10h200M-100 60h160"/></g>
  <g class="muted"><path d="M-100-40h200"/></g>
  <g class="corals" style="stroke-width:6"><path d="M-110-60l220 40M-110-20l220-40"/></g>
</g>
<path d="M470 200q-40 10-60 20" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('denounce', '大勢の前で、悪い行いを公然と非難するイラスト。', f"""
{person(180,346,1.2,1,'blue','violet','point','short','neutral')}
<g transform="translate(250 220)">
  <path d="M-16-14h32v28h-32z" class="ink"/>
  <path d="M16-4l50-24v48z" class="ink" opacity=".8"/>
</g>
{person(450,346,1.05,-1,'coral','gold','stand','bob','sad')}
<g class="corals" style="stroke-width:6"><path d="M370 200l30 30M400 200l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('dentist', '歯を診てもらっている、歯科医のイラスト。', f"""
<g transform="translate(340 300)">
  <path d="M-160-20h320v30h-320z" class="tealp o"/>
  <path d="M-140 10v50M140 10v50" fill="none" stroke="{MUTED}" stroke-width="10"/>
  <ellipse cx="20" cy="-46" rx="110" ry="26" class="coral o"/>
  <circle cx="-110" cy="-56" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <circle cx="-110" cy="-46" r="8" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
{person(150,346,1.05,1,'teal','teal','point','cap','neutral')}
<g transform="translate(200 250)">
  <path d="M-6-40h12v50h-12z" class="ink"/>
  <circle cy="14" r="8" fill="#dfe6ea" stroke="{INK}" stroke-width="2.5"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('depart', '列車が駅を離れて、出発していくイラスト。', f"""
<path d="M0 320h600v50H0z" fill="#d8d3ca"/>
<g fill="none" stroke="{INK}" stroke-width="4"><path d="M0 330h600M0 352h600"/></g>
<g transform="translate(360 260)">
  <path d="M-200-60h370q30 0 30 30v70h-400z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <g class="bluep o"><rect x="-170" y="-40" width="60" height="46"/><rect x="-90" y="-40" width="60" height="46"/><rect x="-10" y="-40" width="60" height="46"/></g>
  <circle cx="-130" cy="46" r="18" class="ink"/><circle cx="110" cy="46" r="18" class="ink"/>
</g>
<g transform="translate(120 260)"><path d="M-60-70h120v140h-120z" class="goldp o"/></g>
<path d="M480 190h60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('depict', '見た景色を、絵にして描き表しているイラスト。', f"""
{tree(520,330,0.7)}
{person(180,346,1.1,1,'violet','blue','point','bun','neutral')}
<g transform="translate(330 240)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <path d="M-60 50L-10-20l40 40 40-50 30 80z" class="tealp o"/>
  {tree(50,20,0.28)}
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M440 250h50" marker-start="url(#ar)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('deploy', '待機していた隊を、各地へ配置するイラスト。', f"""
{person(300,140,0.7,1,'blue','violet','point','cap','neutral')}
{person(140,346,0.9,1,'green','green','stand','cap','neutral')}
{person(300,346,0.9,1,'green','green','stand','cap','neutral')}
{person(460,346,0.9,1,'green','green','stand','cap','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M260 200q-70 40-90 70"/><path d="M300 200v70"/><path d="M340 200q70 40 90 70"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('deprive', '持っていた物を取り上げられて、手元がなくなるイラスト。', f"""
{person(200,346,1.15,1,'coral','blue','give','short','sad')}
{person(450,346,1.1,-1,'blue','violet','give','cap','neutral')}
<g transform="translate(360 250)">{box(0,0,70,50,0,'gold')}</g>
<g transform="translate(250 250)"><path d="M-36-26h72v52h-72z" class="muted"/></g>
<path d="M300 200h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('derive', '元の語から、新しい語が枝分かれして生まれるイラスト。', f"""
<g transform="translate(160 230)">
  <path d="M-80-40h160v80h-160z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 210q60-40 110-50"/><path d="M250 250q60 40 110 50"/></g>
<g transform="translate(440 160)"><path d="M-70-34h140v68h-140z" class="coralp o"/></g>
<g transform="translate(440 300)"><path d="M-70-34h140v68h-140z" class="goldp o"/></g>
""", ground=False, arrow=True)

add('descend', '階段を一段ずつ、下へ降りていくイラスト。', f"""
<g class="goldp o">
  <rect x="80" y="130" width="90" height="230"/><rect x="170" y="190" width="90" height="170"/>
  <rect x="260" y="250" width="90" height="110"/><rect x="350" y="310" width="90" height="50"/>
</g>
{person(130,130,0.7,1,'teal','blue','walk','short','neutral')}
<path d="M220 180L420 300" class="a" marker-end="url(#ar)"/>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('deserve', '努力に見合った賞が、手わたされるイラスト。', f"""
{person(200,346,1.15,1,'teal','blue','hold','short','smile')}
<g transform="translate(200 250)">
  <circle r="30" class="gold o"/>
  <path d="M-18-30l-16-40h32l10 30zM18-30l16-40h-32l-10 30z" class="coral o"/>
</g>
<g transform="translate(430 250)">
  <path d="M-80-70h160v140h-160z" class="paper"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round">
    <path d="M-56-40l12 12 20-24M-56 0l12 12 20-24M-56 40l12 12 20-24"/>
  </g>
</g>
<path d="M340 220h-60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('designate', '地図の一区画を選び、指定の印をつけるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M{-140+i*70} -140v280"/>' for i in range(5))}<path d="M-200 0h400"/></g>
  <rect x="-70" y="-140" width="70" height="140" class="coralp o"/>
</g>
<g transform="translate(265 130)"><path d="M0 30l-24-30 12-14 12 12 12-12 12 14z" class="coral o"/></g>
{hand(120,320,1)}
""", ground=True)

add('designer', '図面を引いて、形を考えているデザイナーのイラスト。', f"""
{person(160,346,1.15,1,'violet','blue','point','bun','neutral')}
<g transform="translate(410 250)">
  <path d="M-120-110h240v220h-240z" class="paper"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"><circle r="60"/><path d="M-90 0h180M0-90v180"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5" stroke-dasharray="8 7"><rect x="-90" y="-90" width="180" height="180"/></g>
</g>
<path d="M250 220h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('detain', '通り道でとめられて、その場に引き止められるイラスト。', f"""
{person(220,346,1.15,1,'coral','blue','stand','short','sad')}
{person(400,346,1.1,-1,'blue','violet','point','cap','neutral')}
<path d="M300 250h-30" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<g class="corals" style="stroke-width:8"><path d="M300 170l40 40M340 170l-40 40"/></g>
<path d="M180 300h-60" class="muted" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('detect', '機器の針が反応して、隠れたものを見つけるイラスト。', f"""
<g transform="translate(200 240)">
  <circle r="90" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0l60-40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-64-64l-12-12M64-64l12-12M0-90v-14"/></g>
</g>
<g transform="translate(440 280)">
  <path d="M-80-60h160v120h-160z" class="goldp o"/>
  <circle cy="0" r="26" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"><path d="M300 250h60" marker-end="url(#ar)"/></g>
""", ground=True, arrow=True)

add('detective', '虫めがねと手帳で、事件を調べる刑事のイラスト。', f"""
{person(200,346,1.15,1,'blue','violet','point','cap','neutral')}
<g transform="translate(330 230)">
  <circle r="70" fill="#e8f4fb" opacity=".4" stroke="{INK}" stroke-width="6"/>
  <path d="M50 50l50 50" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>
</g>
<g fill="#c9bda6"><ellipse cx="320" cy="240" rx="12" ry="18"/></g>
<g transform="translate(480 300)">
  <path d="M-50-60h100v120h-100z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-30-30h60M-30-6h60M-30 18h40"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('determine', '調べた結果から、答えを一つに絞り込むイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-100-110h200v220h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-70h140M-70-30h140M-70 10h110"/></g>
</g>
<g transform="translate(440 230)">
  <circle r="70" fill="none" stroke="{INK}" stroke-width="4"/>
  <circle r="22" class="coral o"/>
</g>
<path d="M300 230h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('determined', 'こぶしを固めて、固い決意を示しているイラスト。', f"""
{person(280,346,1.3,1,'coral','blue','point','short','neutral')}
<g fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"><circle cx="380" cy="250" r="20"/></g>
<g transform="translate(470 200)">
  <circle r="46" fill="none" stroke="{INK}" stroke-width="4"/>
  <circle r="14" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M410 240h30" marker-end="url(#ar)"/></g>
<path d="M80 366h440" class="a"/>
""", ground=True, arrow=True)

add('devastate', '嵐が去ったあと、一帯が荒れ果てているイラスト。', f"""
<path d="M0 300h600v100H0z" fill="#d8c9ab"/>
<path d="M0 300h600" class="a"/>
<g transform="translate(160 300) rotate(-64)"><path d="M-10 0v-120h20V0z" fill="#a08b62" stroke="{INK}" stroke-width="3"/></g>
<g transform="translate(430 300) rotate(52)"><path d="M-10 0v-100h20V0z" fill="#a08b62" stroke="{INK}" stroke-width="3"/></g>
<g fill="#cfc7b8" stroke="{INK}" stroke-width="2.5"><path d="M250 300q14-34 46-22t16 22z"/></g>
<g class="muted"><path d="M40 120q140-40 240 0t280-20"/></g>
""", ground=False)

add('develop', '小さな芽が段を追って、大きな木に育つイラスト。', f"""
<g transform="translate(130 340)">
  <path d="M0 0v-40" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
  <path d="M0-26c-22-6-30-20-30-20 20-6 30 20 30 20z" class="green o"/>
</g>
{tree(300,340,0.7)}
{tree(470,340,1.3)}
<path d="M100 160h420" class="a" marker-end="url(#ar)"/>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('devise', '手元の部品から、新しい仕掛けを考え出すイラスト。', f"""
{person(160,346,1.15,1,'teal','blue','think','short','smile')}
<g transform="translate(420 250)">
  <path d="M-100-70h200v140h-200z" fill="#dfe6ea" class="o"/>
  <circle cx="-40" cy="-20" r="34" fill="none" stroke="{INK}" stroke-width="5"/>
  <circle cx="34" cy="14" r="24" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M-40-20l74 34" class="a"/>
</g>
<g transform="translate(270 150)">
  <circle r="28" class="goldp o"/>
  <path d="M-12 28h24v12h-24z" class="ink"/>
  <g class="golds" style="stroke-width:4"><path d="M0-40v-14M-30-22l-12-8M30-22l12-8"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('devote', '時間のすべてを、一つの作業に充てているイラスト。', f"""
<g transform="translate(180 230)">
  <circle r="90" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0v-90a90 90 0 1 1-1 0z" class="tealp o"/>
  <circle r="10" class="ink"/>
</g>
<path d="M300 230h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(440 240)">
  <path d="M-90-70h180v140h-180z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"><path d="M-60-40h120M-60-10h120M-60 20h90"/></g>
</g>
""", ground=True, arrow=True)

add('diagnose', '症状を調べて、病名を突き止めているイラスト。', f"""
{person(160,346,1.1,1,'teal','teal','point','cap','neutral')}
<g transform="translate(230 250)">
  <circle cy="30" r="26" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M0 4q-40-24-40-64" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<g transform="translate(430 250)">
  <path d="M-90-80h180v160h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-50h120M-60-20h120"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M-60 20h100"/></g>
</g>
<path d="M320 250h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('diary', '日付ごとに書き込まれた日記帳のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-140-140h280v280h-280z" class="violetp o"/>
  <path d="M-110-110h220v250h-220z" class="paper"/>
  <g fill="{INK}">{''.join(f'<rect x="-90" y="{-84+i*54}" width="40" height="8"/>' for i in range(4))}</g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-40 {-80+i*54}h130"/>' for i in range(4))}</g>
</g>
""", ground=True)

add('dictate', '読み上げた言葉を、相手が書き取っているイラスト。', f"""
{person(160,346,1.15,1,'blue','violet','point','short','neutral')}
{person(450,346,1.1,-1,'teal','gold','point','bob','neutral')}
<g transform="translate(300 190)">
  <path d="M-60-30h120q14 0 14 14v30q0 14-14 14h-80l-20 16 4-16q-14 0-14-14v-30q0-14 14-14z" class="paper"/>
  <g fill="{MUTED}"><circle cx="-20" cy="0" r="4"/><circle cx="0" cy="0" r="4"/><circle cx="20" cy="0" r="4"/></g>
</g>
<g transform="translate(400 290)">
  <path d="M-50-40h100v80h-100z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-30-16h60M-30 6h40"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('differ', '形の違う二つを並べて、違いを示したイラスト。', f"""
<g transform="translate(170 230)"><circle r="70" class="teal o"/></g>
<g transform="translate(430 230)"><path d="M-70-70h140v140h-140z" class="coral o"/></g>
<path d="M300 130v200" class="muted"/>
<g class="corals" style="stroke-width:7"><path d="M280 350l40-40M320 350l-40-40"/></g>
""", ground=False)

add('differentiate', 'よく似た二つの間に、境目の線を引いて区別するイラスト。', f"""
<g transform="translate(180 230)"><circle r="70" class="tealp o"/><circle r="40" class="teal o"/></g>
<g transform="translate(420 230)"><circle r="70" class="tealp o"/><circle r="40" class="teal o"/><path d="M-40 0h80" fill="none" stroke="#fffdf6" stroke-width="6"/></g>
<path d="M300 120v220" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="14 10"/>
<circle cx="300" cy="360" r="30" fill="none" stroke="{INK}" stroke-width="5"/>
<path d="M322 382l24 20" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
""", ground=False)

add('digital', '数字の並びで表された、デジタル表示のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-180-100h360v200h-360z" fill="#2b3a4a" stroke="{INK}" stroke-width="3"/>
  <g fill="#7ef0d0">
    {''.join(f'<g transform="translate({-120+i*80} 0)"><rect x="-24" y="-56" width="48" height="10"/><rect x="-30" y="-50" width="10" height="46"/><rect x="20" y="-50" width="10" height="46"/><rect x="-24" y="-10" width="48" height="10"/><rect x="-30" y="4" width="10" height="46"/><rect x="20" y="4" width="10" height="46"/><rect x="-24" y="44" width="48" height="10"/></g>' for i in range(4))}
  </g>
</g>
""", ground=True)

add('diminish', '大きかった円が、だんだん小さくなるイラスト。', f"""
<circle cx="140" cy="240" r="80" class="tealp o"/>
<circle cx="310" cy="250" r="54" class="tealp o"/>
<circle cx="450" cy="270" r="30" class="tealp o"/>
<path d="M100 120h420" class="a" marker-end="url(#ar)"/>
<path d="M60 330h480" class="a"/>
""", ground=True, arrow=True)

add('direction', '四方を指す矢印で、進む向きを示したイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="30" class="tealp o"/>
  <g class="a" marker-end="url(#ar)"><path d="M0-40v-90"/><path d="M0 40v90"/><path d="M-40 0h-110"/><path d="M40 0h110"/></g>
</g>
<path d="M60 370h480" class="muted"/>
""", ground=False, arrow=True)

add('director', '現場を指示してまとめている、取締役のイラスト。', f"""
{person(180,346,1.25,1,'blue','blue','point','short','neutral')}
<g transform="translate(180 258)">
  <path d="M-40-24h80v6h-80z" class="paper"/>
  <path d="M-12-20l12 18 12-18z" class="ink"/>
</g>
<g opacity=".7">{person(400,346,0.9,-1,'teal','gold','stand','bob','neutral')}{person(490,346,0.9,-1,'violet','teal','stand','cap','neutral')}</g>
<path d="M260 220h80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('disappoint', '期待した結果が出ず、相手を落胆させるイラスト。', f"""
{person(200,346,1.15,1,'coral','blue','hold','short','sad')}
<g transform="translate(420 240)">
  <path d="M-90-80h180v160h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-40h120M-60-10h120"/></g>
  <g class="corals" style="stroke-width:7"><path d="M-30 20l60 40M30 20l-60 40"/></g>
</g>
<path d="M300 250h40" class="a" marker-end="url(#ar)" transform="rotate(180 320 250)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('disappointed', '肩を落として、がっかりしている人のイラスト。', f"""
{person(300,346,1.3,1,'violet','blue','stand','short','sad')}
<g class="muted"><path d="M200 250v20M400 250v20"/></g>
{drop(240,230,0.9)}
<g class="corals" style="stroke-width:5"><path d="M420 200l24-24"/></g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('disappointing', '中身が思ったより少なく、期待外れなイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-120-100h240v200h-240z" class="goldp o"/>
  <path d="M-120-100l-30-30h300l-30 30" fill="none" class="a"/>
  <path d="M-60 40h60v60h-60z" class="tealp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M-100-60h200" transform="translate(300 260)"/></g>
<g class="corals" style="stroke-width:7"><path d="M470 160l30 30M500 160l-30 30"/></g>
""", ground=True)

add('discard', '不要になった紙を、ごみ箱へ捨てるイラスト。', f"""
{hand(200,180,1)}
<g transform="translate(220 130)">
  <path d="M-34-8l-6-20 22-8 10-14 20 12 22-4 2 20 14 14-16 14 2 20-24-4-16 12-14-16-20-2z" fill="#fffdf6" stroke="{INK}" stroke-width="2.5"/>
</g>
<g transform="translate(400 300)">
  <path d="M-80-66h160l-16 136h-128z" class="tealp o"/>
  <path d="M-80-66h160" class="a"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3"><path d="M-56-36h112M-52 4h104"/></g>
</g>
<path d="M280 170q60 20 90 60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('discharge', '管から中身が外へ放出されるイラスト。', f"""
<g transform="translate(200 240)">
  <path d="M-120-50h240v100h-240z" fill="#dfe6ea" class="o"/>
  <path d="M120-24h60v48h-60z" fill="#cfd8de" stroke="{INK}" stroke-width="3"/>
</g>
<g class="blues" marker-end="url(#ar)" style="stroke-width:8">
  <path d="M400 240h120"/><path d="M400 200q80-20 120 0"/><path d="M400 280q80 20 120 0"/>
</g>
<path d="M60 350h480" class="a"/>
""", ground=True, arrow=True)

add('disclose', '覆いを外して、隠していた中身を明らかにするイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-110 60V-30h220V60z" class="tealp o"/>
  <path d="M-110 60h220" class="a"/>
</g>
<g transform="translate(300 150) rotate(-16)">
  <path d="M-130-30q130-40 260 0-130 40-260 0z" class="violetp o"/>
</g>
{hand(140,140,1)}
<path d="M300 200v40" class="a" marker-end="url(#ar)" transform="rotate(180 300 220)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 300l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('discourage', '進もうとする人を止めて、思いとどまらせるイラスト。', f"""
{person(200,346,1.15,1,'coral','blue','walk','short','sad')}
{person(430,346,1.1,-1,'blue','violet','point','cap','neutral')}
<path d="M350 250h-40" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<path d="M280 300h50" class="muted" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:8"><path d="M320 170l40 40M360 170l-40 40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('displace', '元の場所から押し出されて、別の物が入るイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-140-80h280v160h-280z" class="muted"/>
  <path d="M-120-60h120v120h-120z" class="teal o"/>
</g>
<g transform="translate(470 250)"><path d="M-50-60h100v120h-100z" class="coral o" opacity=".8"/></g>
<g class="a" marker-end="url(#ar)"><path d="M400 250h-60"/><path d="M180 320h-100"/></g>
""", ground=True, arrow=True)

add('dispose', '不要な物をまとめて、処分するイラスト。', f"""
{box(160,300,80,60,0,'gold')}
{box(250,300,80,60,0,'gold')}
<g transform="translate(440 290)">
  <path d="M-90-70h180l-18 140h-144z" class="tealp o"/>
  <path d="M-90-70h180" class="a"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M220 240q80-60 150-40"/><path d="M300 250q60-40 110-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('disrupt', '整った流れに割り込んで、混乱させるイラスト。', f"""
<g class="tealp o">{''.join(f'<rect x="{80+i*70}" y="200" width="50" height="70"/>' for i in range(3))}</g>
<g transform="rotate(28 340 250)"><rect x="310" y="200" width="50" height="70" class="coral o"/></g>
<g class="tealp o" transform="rotate(-18 460 250)">{''.join(f'<rect x="{420+i*70}" y="200" width="50" height="70"/>' for i in range(2))}</g>
<path d="M340 140v40" class="a" marker-end="url(#ar)"/>
<path d="M60 300h480" class="a"/>
""", ground=True, arrow=True)

add('distort', 'まっすぐな形が、ねじれてゆがむイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-70-70h140v140h-140z" fill="none" stroke="{INK}" stroke-width="5"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70 0h140M0-70v140"/></g>
</g>
<g transform="translate(430 230)">
  <path d="M-80-60q80-30 160 20-40 90-160 40 20-40 0-60z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-10q80 20 150-10M-10-58q20 70 0 110"/></g>
</g>
<path d="M280 230h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
