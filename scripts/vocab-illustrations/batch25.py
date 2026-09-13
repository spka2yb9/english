"""第25回: 医療・道徳・服装・容器など30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('lovely', '花に囲まれた、見ていて心地よい景色のイラスト。', f"""
{sun(490,90,44)}
<path d="M0 280h600v120H0z" fill="#e4efe2"/>
<path d="M0 280h600" class="a" opacity=".4"/>
{''.join(f'<g transform="translate({100+i*90} {310 - (i%2)*20})"><path d="M0 0v-50" fill="none" stroke="{TONES["green"][2]}" stroke-width="6"/><circle cy="-56" r="14" class="{["coral","gold","violet"][i%3]} o"/><g class="{["coralp","goldp","violetp"][i%3]} o"><circle cx="-20" cy="-70" r="12"/><circle cx="20" cy="-70" r="12"/><circle cx="0" cy="-84" r="12"/></g></g>' for i in range(5))}
<g class="golds" style="stroke-width:4"><path d="M120 180l-20-20M420 160l20-20"/></g>
""", ground=False)

add('lucky', '四つ葉のクローバーを見つけて、喜んでいるイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','up','bob','smile')}
<g transform="translate(420 250)">
  <g class="green o">
    <ellipse cx="0" cy="-40" rx="30" ry="38"/><ellipse cx="40" cy="0" rx="38" ry="30"/>
    <ellipse cx="0" cy="40" rx="30" ry="38"/><ellipse cx="-40" cy="0" rx="38" ry="30"/>
  </g>
  <path d="M0 40v60" fill="none" stroke="{TONES['green'][2]}" stroke-width="7"/>
</g>
<g class="golds" style="stroke-width:4"><path d="M300 180l24-24M290 240h-26M330 300l24 24"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('mainland', '小島から離れた、大きな陸地の本土を示したイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#dbeaf8"/>
<path d="M0 400h380V140q-60 20-120 10T140 120 20 170 0 160z" fill="#e4efe2" stroke="{INK}" stroke-width="3"/>
{building(150,300,0.5,'teal')}{tree(260,300,0.5)}
<g transform="translate(500 250)">
  <ellipse rx="60" ry="34" fill="#e4efe2" stroke="{INK}" stroke-width="3"/>
  {tree(0,-6,0.35)}
</g>
<path d="M420 200h-60" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('market', '売り手が品物を並べ、買い手と取引をしているイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-190-20h380v20h-380z" class="goldp o"/>
  <g class="coral o"><circle cx="-140" cy="-40" r="20"/><circle cx="-100" cy="-40" r="20"/></g>
  <g class="greenp o"><rect x="-60" y="-58" width="40" height="38"/><rect x="-10" y="-58" width="40" height="38"/></g>
  <g class="gold o"><circle cx="70" cy="-40" r="20"/><circle cx="110" cy="-40" r="20"/></g>
  <path d="M-206-70h412l-30-40h-352z" class="teal o"/>
</g>
{person(120,346,0.9,1,'teal','blue','give','bob','smile')}
{person(480,346,0.9,-1,'coral','gold','give','short','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('means', '目的地へ着くための手段として、乗り物を選ぶイラスト。', f"""
<circle cx="520" cy="140" r="34" class="coral o"/>
<g transform="translate(160 250) scale(0.45)">
  <path d="M-150 40h300l-16-56h-50l-34-56h-120l-34 56h-62z" class="teal o"/>
  <circle cx="-84" cy="48" r="30" class="ink"/><circle cx="84" cy="48" r="30" class="ink"/>
</g>
<g transform="translate(160 340) scale(0.45)">
  <circle cx="-100" cy="0" r="56" fill="none" stroke="{INK}" stroke-width="10"/>
  <circle cx="100" cy="0" r="56" fill="none" stroke="{INK}" stroke-width="10"/>
  <path d="M-100 0l56-64h74l70 64" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10"/>
</g>
<path d="M260 250q140-60 220-90" class="a" marker-end="url(#ar)"/>
<path d="M260 330q140-100 230-160" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('medical', '聴診器と薬が並んだ、医療の道具のイラスト。', f"""
<g transform="translate(220 240)">
  <circle cy="60" r="34" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M0 26q-50-30-50-80" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-50-54q-30 0-30-30M-50-54q30 0 30-30" fill="none" stroke="{INK}" stroke-width="7"/>
</g>
<g transform="translate(430 260)">
  <path d="M-50-70h100l-8 140h-84z" fill="#f4fbff" class="o"/>
  <path d="M-44-20h88l-6 90h-76z" class="coralp o"/>
  <path d="M-24-80h48v14h-48z" class="ink"/>
</g>
<g transform="translate(430 130)">
  <path d="M-12-30h24v18h18v24h-18v18h-24v-18h-18v-24h18z" class="coral o"/>
</g>
<path d="M120 360h360" class="a"/>
""", ground=True)

add('missile', '発射されて飛んでいくミサイルのイラスト。', f"""
<g transform="translate(300 200) rotate(-16)">
  <path d="M-120-24h180l60 24-60 24h-180z" fill="#8f9aa5" stroke="{INK}" stroke-width="3"/>
  <path d="M-120-24l-30-40h40l20 40zM-120 24l-30 40h40l20-40z" class="coral o"/>
  <path d="M-60-24v48" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>
<g class="corals" style="stroke-width:6"><path d="M120 250q-40 20-70 30M140 280q-40 10-70 24"/></g>
<path d="M420 130h100" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('missing', '並んだ品の中に、一つだけ欠けている場所があるイラスト。', f"""
<g class="tealp o">
  {''.join(f'<rect x="{90+i*80}" y="200" width="60" height="80"/>' for i in range(6) if i != 3)}
</g>
<rect x="330" y="200" width="60" height="80" class="muted"/>
<circle cx="360" cy="240" r="56" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="11 9"/>
<path d="M60 300h480" class="a"/>
""", ground=False)

add('monk', '簡素な衣をまとって、静かに祈っている修道士のイラスト。', f"""
<circle cx="300" cy="140" r="86" class="goldp" opacity=".55"/>
{person(300,346,1.3,1,'gold','gold','hold','short','neutral')}
<g transform="translate(300 300)">
  <path d="M-58-70q58-24 116 0l20 116h-156z" class="goldd o"/>
</g>
<g transform="translate(300 254)">
  <path d="M-26-20h52q10 0 10 20t-10 20h-52q-10 0-10-20t10-20z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('moral', '拾った物を届ける行いに、丸印がついているイラスト。', f"""
{person(180,346,1.1,1,'teal','blue','give','short','smile')}
{person(430,346,1.1,-1,'coral','gold','give','bob','smile')}
<g transform="translate(300 280)">
  <path d="M-46-28h92v56h-92z" class="goldd o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M270 170l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('morality', '天びんに正しい行いと誤った行いを載せて量るイラスト。', f"""
<path d="M300 340V140" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<path d="M250 356h100" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>
<path d="M150 150h300" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<circle cx="300" cy="150" r="13" class="teal o"/>
<path d="M150 150v30M450 150v30" class="a"/>
<path d="M96 180h108l-14 30H110z" class="goldp o"/>
<path d="M396 180h108l-14 30H410z" class="goldp o"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round"><path d="M130 170l12 12 20-24"/></g>
<g class="corals" style="stroke-width:7"><path d="M432 162l30 30M462 162l-30 30"/></g>
""", ground=True)

add('motorist', 'ハンドルを握って車を運転している人のイラスト。', f"""
<g transform="translate(320 270)">
  <path d="M-190 50h380l-20-70h-60l-40-66h-140l-40 66h-80z" class="tealp o"/>
  <path d="M-140-20h100v-52h-70zM-20-72h90l32 52H-20z" class="bluep o"/>
  <circle cx="-110" cy="58" r="34" class="ink"/><circle cx="110" cy="58" r="34" class="ink"/>
</g>
<g transform="translate(200 210)">
  <circle r="26" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-26 0h52M0 0v26" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<circle cx="200" cy="172" r="22" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<path d="M176 158q4-24 24-24 20 0 24 22-14-8-26-2-10-6-22 4z" fill="{HAIR}"/>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('murder', '事件現場に、立ち入り禁止の線が張られているイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-200-40h400v160h-400z" class="muted"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="12">
    <path d="M-210-10h420"/><path d="M-210 60h420"/>
  </g>
</g>
<g fill="#c9bda6"><ellipse cx="240" cy="330" rx="12" ry="18"/><ellipse cx="290" cy="350" rx="11" ry="17"/></g>
{person(120,346,0.9,1,'blue','violet','stand','cap','sad')}
<g class="corals" style="stroke-width:8"><path d="M440 160l40 40M480 160l-40 40"/></g>
""", ground=True)

add('navigation', '海図と方位磁石で、進む方向を決めているイラスト。', f"""
<g transform="translate(240 250)">
  <path d="M-150-110h300v220h-300z" fill="#f3e6c8" stroke="{INK}" stroke-width="3"/>
  <path d="M-150 40q80-40 150 0t150-20" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"/>
  <path d="M-100-60q60-30 120 0t130-10" fill="none" stroke="{TONES['blue'][0]}" stroke-width="3" stroke-dasharray="10 8"/>
</g>
<g transform="translate(460 240)">
  <circle r="70" fill="#fffdf6" stroke="{INK}" stroke-width="4"/>
  <path d="M0-50l14 40 40 14-40 14-14 40-14-40-40-14 40-14z" class="coral o"/>
</g>
<path d="M120 360h360" class="a"/>
""", ground=True)

add('necessary', 'これがないと動かない、欠かせない部品を示したイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-140-90h280v180h-280z" fill="#dfe6ea" class="o"/>
  <circle cx="-50" cy="-20" r="40" fill="none" stroke="{TONES['teal'][0]}" stroke-width="12"/>
  <circle cx="40" cy="20" r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-dasharray="8 8"/>
</g>
<g class="corals" style="stroke-width:7"><path d="M470 150l30 30M500 150l-30 30"/></g>
<path d="M410 270h60" class="a" marker-end="url(#ar)" transform="rotate(180 440 270)"/>
""", ground=True, arrow=True)

add('nervous', '本番前で、汗をかいて落ち着かない人のイラスト。', f"""
{person(280,346,1.25,1,'teal','blue','hold','short','sad')}
{drop(240,220,1.0)}{drop(330,214,1.0)}
<g class="muted"><path d="M200 260v-30M370 250v-30"/></g>
<g transform="translate(430 200)">
  <path d="M-70-40h140v80h-140z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-44-14h88M-44 8h60"/></g>
</g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('noisy', '大きな音が四方に響いて、うるさいイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-60-60h120v120h-120z" class="goldp o"/>
  <circle r="34" class="gold o"/>
</g>
<g class="corals" opacity=".95" style="stroke-width:6">
  <path d="M400 150q34 34 34 60t-34 60"/><path d="M200 150q-34 34-34 60t34 60"/>
  <path d="M460 120q46 46 46 90t-46 90"/><path d="M140 120q-46 46-46 90t46 90"/>
</g>
""", ground=False)

add('note', '気づいた点を、余白に書き留めているイラスト。', f"""
<g transform="translate(260 240)">
  <path d="M-140-140h280v280h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-110-90h180M-110-50h180M-110-10h150"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M-100 40h140M-100 70h100"/></g>
</g>
<g transform="translate(420 180) rotate(36)">
  <path d="M-10-90h20v130h-20z" class="coral o"/>
  <path d="M-10 40h20l-10 28z" class="ink"/>
</g>
""", ground=True)

add('novelist', '原稿を書き進めている小説家のイラスト。', f"""
{person(160,346,1.15,1,'violet','blue','point','bun','neutral')}
<g transform="translate(400 250)">
  <path d="M-130-110h260v220h-260z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-100 {-80+i*30}h200"/>' for i in range(6))}</g>
</g>
<g transform="translate(280 190) rotate(30)">
  <path d="M-9-70h18v100h-18z" class="violet o"/>
  <path d="M-9 30h18l-9 24z" class="ink"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('obesity', '体重計の目盛りが大きく振れて、体重過多を示すイラスト。', f"""
<g transform="translate(300 330)">
  <path d="M-120-30h240v40h-240z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <path d="M-120 10h240v20h-240z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(300 296)">
  <ellipse cx="0" cy="-50" rx="80" ry="60" class="teal o"/>
  <path d="M-30 8v-8M30 8v-8" fill="none" stroke="{TONES['blue'][2]}" stroke-width="14"/>
  <circle cy="-140" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-30-142q4-30 30-30 26 0 30 28-16-10-30-4-12-8-30 6z" fill="{HAIR}"/>
</g>
<g transform="translate(470 220)">
  <circle r="46" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0l30 26" class="a"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('objective', '達成すべき目標の旗を、はっきり示したイラスト。', f"""
<path d="M420 340V110" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
<path d="M428 116l90 26-90 26z" class="coral o"/>
<circle cx="420" cy="340" r="20" class="goldp o"/>
{person(140,340,1.0,1,'teal','blue','point','short','neutral')}
<path d="M220 240h150" class="a" marker-end="url(#ar)" style="stroke-width:6"/>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('occur', '静かな水面に、突然波紋が起こるイラスト。', f"""
<path d="M0 200h600v200H0z" class="bluep"/>
<path d="M0 200h600" class="a"/>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4">
  <ellipse cx="300" cy="290" rx="40" ry="16"/><ellipse cx="300" cy="290" rx="80" ry="30"/>
  <ellipse cx="300" cy="290" rx="130" ry="46"/><ellipse cx="300" cy="290" rx="190" ry="64"/>
</g>
{drop(300,150,1.6)}
<path d="M300 190v20" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('operator', '交換機の前で、通話をつないでいる人のイラスト。', f"""
<g transform="translate(410 250)">
  <path d="M-120-100h240v200h-240z" fill="#dfe6ea" class="o"/>
  <g class="ink">{''.join(f'<circle cx="{-80 + (i%4)*50}" cy="{-60 + (i//4)*50}" r="14"/>' for i in range(8))}</g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M-80-60q60 40 130 0"/></g>
</g>
{person(160,346,1.15,1,'teal','blue','hold','bob','neutral')}
<g transform="translate(160 230)">
  <path d="M-40-14a40 34 0 0 1 80 0" fill="none" stroke="{INK}" stroke-width="8"/>
  <rect x="-52" y="-14" width="22" height="30" rx="7" class="coral o"/>
  <rect x="30" y="-14" width="22" height="30" rx="7" class="coral o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('opponent', '盤をはさんで向かい合う、対戦相手のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-110-20h220v20h-220z" class="goldp o"/>
  <g>{''.join(f'<rect x="{-96 + (i%6)*32}" y="{-50 + (i//6)*15}" width="32" height="15" fill="{"#fffdf6" if (i+i//6)%2 else "#5d6b78"}"/>' for i in range(12))}</g>
</g>
{person(150,346,1.05,1,'teal','blue','stand','short','neutral')}
{person(450,346,1.05,-1,'coral','gold','stand','bob','neutral')}
<path d="M230 220h140" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('ordinary', 'まったく同じ形の品が並び、変わったところがないイラスト。', f"""
<g class="tealp o">
  {''.join(f'<rect x="{80+i*82}" y="200" width="62" height="90"/>' for i in range(6))}
</g>
<path d="M60 300h480" class="a"/>
<path d="M60 170h480" class="muted"/>
""", ground=False)

add('organ', '体の中の臓器の位置を示したイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-110-130q110-40 220 0v220q-110 40-220 0z" fill="#f7f2ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-30-60l-50-56 26-30 24 24 24-24 26 30z" class="coral o"/>
  <g class="violetp o"><path d="M-90 0q-20 60 20 90 20-40 0-90z"/><path d="M90 0q20 60-20 90-20-40 0-90z"/></g>
  <ellipse cx="10" cy="80" rx="46" ry="30" class="goldp o"/>
</g>
""", ground=True)

add('outfit', '上下そろいの服装を、ひとそろい並べたイラスト。', f"""
<g transform="translate(280 200)">
  <path d="M-70-50l-30 16 12 28 16-8v76h124V-14l16 8 12-28-30-16h-38q-14 12-28 0z" class="violetp o"/>
</g>
<g transform="translate(280 330)">
  <path d="M-60-40h120v30l-16 60h-30l-8-40-8 40h-30l-16-60z" class="bluep o"/>
</g>
<g class="ink"><rect x="400" y="330" width="40" height="18" rx="5"/><rect x="450" y="330" width="40" height="18" rx="5"/></g>
<path d="M120 380h360" class="a"/>
""", ground=True)

add('outlet', '壁のコンセントにプラグを差し込んでいるイラスト。', f"""
<g transform="translate(360 240)">
  <path d="M-70-90h140v180h-140z" fill="#fffdf6" class="o"/>
  <g class="ink"><rect x="-30" y="-40" width="16" height="40" rx="4"/><rect x="14" y="-40" width="16" height="40" rx="4"/></g>
</g>
<g transform="translate(220 240)">
  <path d="M-40-40h60v80h-60z" class="ink"/>
  <path d="M20-24h30v10H20zM20 14h30v10H20z" class="ink"/>
  <path d="M-40 0h-140" fill="none" stroke="{INK}" stroke-width="8"/>
</g>
<path d="M270 300h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('outsider', '輪の外にひとりだけ立っている人のイラスト。', f"""
<circle cx="260" cy="230" r="150" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" stroke-dasharray="16 12"/>
{person(190,320,0.85,1,'teal','blue','stand','short','smile')}
{person(300,330,0.85,1,'gold','violet','stand','bob','smile')}
{person(520,346,1.0,-1,'coral','gold','stand','cap','sad')}
<path d="M440 240h-30" class="muted"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('package', 'ひもをかけて包んだ小包のイラスト。', f"""
{box(300,250,220,150,0,'gold')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10">
  <path d="M300 175v150M190 250h220"/>
</g>
<g transform="translate(300 175)">
  <path d="M0 0q-30-30-10-40 16-8 10 40M0 0q30-30 10-40 16 8-10 40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
</g>
<path d="M120 340h360" class="a"/>
""", ground=True)

add('packet', '小さな粉の袋を、切って開けているイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-70-100h140v200h-140z" class="tealp o"/>
  <path d="M-70-100h140" class="a"/>
  <path d="M-70-100l20-20h100l20 20z" class="teal o"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"><path d="M-40-40h80M-40 0h60"/></g>
</g>
<g fill="#fffdf6" stroke="{MUTED}" stroke-width="2"><circle cx="380" cy="180" r="6"/><circle cx="400" cy="210" r="5"/><circle cx="366" cy="215" r="4"/></g>
<path d="M340 140l60-20" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('ideology', '同じ旗のもとに、考えを共有する人が並ぶイラスト。', f"""
<path d="M300 340V110" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
<path d="M308 116l90 26-90 26z" class="violet o"/>
{person(190,346,1.0,1,'violet','blue','stand','short','neutral')}
{person(410,346,1.0,-1,'violet','blue','stand','bob','neutral')}
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="150" cy="230" r="20"/><circle cx="450" cy="230" r="20"/></g>
<g class="violet"><circle cx="150" cy="230" r="8"/><circle cx="450" cy="230" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)
print(' '.join(W)); print(sheet(W))
