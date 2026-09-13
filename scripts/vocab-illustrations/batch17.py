"""第17回: 経路・記録・休息・航海など30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('purpose', '矢が的の中心を狙って進む、目的のはっきりした動きのイラスト。', f"""
<g transform="translate(430 220)">
  <circle r="96" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <circle r="68" class="tealp o"/><circle r="42" fill="#fffdf6" stroke="{INK}" stroke-width="3"/><circle r="16" class="teal o"/>
</g>
<path d="M90 300L390 232" fill="none" stroke="{TONES['gold'][2]}" stroke-width="8" stroke-linecap="round"/>
<path d="M390 232l-24-12 4 24z" class="ink"/>
<path d="M120 340q80-40 240-64" class="muted"/>
""", ground=True)

add('question', '大きな疑問符と、首をかしげている人のイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','think','short','neutral')}
<g transform="translate(400 210)" fill="{INK}">
  <path d="M-50-70q0-50 50-50t50 50q0 34-40 46v24h-20v-40q40-4 40-30 0-24-30-24t-30 24z"/>
  <circle cx="0" cy="60" r="13"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('race', '横に並んだ走者が、同時にゴールを目指して競うイラスト。', f"""
<path d="M0 240h600v160H0z" fill="#e2b7a2"/>
<g fill="none" stroke="#fffdf6" stroke-width="4"><path d="M0 300h600M0 360h600"/></g>
{person(180,290,1.0,1,'coral','blue','walk','short','neutral')}
{person(300,350,1.0,1,'teal','gold','walk','cap','neutral')}
<path d="M520 240V120" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
<path d="M528 126l60 20-60 20z" class="coral o"/>
<path d="M400 200h90" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('random', 'ばらばらな位置に散らばった点と、規則正しく並んだ点を比べたイラスト。', f"""
<g class="tealp o">
  {''.join(f'<rect x="{80+ (i%4)*54}" y="{170 + (i//4)*54}" width="34" height="34"/>' for i in range(12))}
</g>
<g class="coralp o">
  <circle cx="360" cy="180" r="16"/><circle cx="470" cy="230" r="16"/><circle cx="400" cy="300" r="16"/>
  <circle cx="520" cy="160" r="16"/><circle cx="340" cy="330" r="16"/><circle cx="500" cy="330" r="16"/>
</g>
<path d="M300 130v240" class="muted"/>
""", ground=False)

add('reach', '伸ばした手が、棚の上の品にちょうど届くイラスト。', f"""
<g transform="translate(400 200)">
  <path d="M-100-20h200v20h-200z" class="goldp o"/>
  <path d="M-30-80h60v60h-60z" class="coralp o"/>
</g>
{person(200,346,1.2,1,'teal','blue','reach','short','neutral')}
<circle cx="300" cy="204" r="15" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<path d="M240 260q40-40 60-52" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('realistic', '写実的に描いた絵と、単純な線の絵を並べて比べたイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <path d="M-70 60l50-90 40 50 40-60 30 100z" class="tealp o"/>
  <circle cx="40" cy="-50" r="22" class="goldp o"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="2"><path d="M-70 30q40-20 70 0t70-14"/></g>
</g>
<g transform="translate(430 230)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <path d="M-60 60L0-20l60 80z" fill="none" stroke="{INK}" stroke-width="4"/>
  <circle cx="40" cy="-50" r="20" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
<path d="M300 350h-60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('reality', '想像の中の場面と、目の前の現実を並べたイラスト。', f"""
<g transform="translate(170 210)">
  <path d="M-120 40q-14-60 44-72 18-48 84-34 40 6 52 46 64-6 70 52 4 52-56 56h-156q-40-4-38-48z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 10)">{building(0,20,0.45,'violet')}</g>
</g>
{building(430,300,0.9,'teal')}
{person(300,346,0.9,1,'coral','blue','stand','short','neutral')}
<path d="M300 160h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('record', '声を録音して、波形として残しているイラスト。', f"""
<g transform="translate(200 230)">
  <path d="M-30-70h60v100a30 30 0 0 1-60 0z" fill="#dfe6ea" class="o"/>
  <path d="M0 30v40M-30 70h60" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-16-50h32M-16-30h32M-16-10h32"/></g>
</g>
<g transform="translate(420 230)">
  <path d="M-110 0h220" class="a"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
    <path d="M-90 0v-30M-70 0v50M-50 0v-60M-30 0v34M-10 0v-46M10 0v56M30 0v-26M50 0v40M70 0v-50M90 0v20"/>
  </g>
</g>
<path d="M270 230h50" class="a" marker-end="url(#ar)"/>
<g class="coral o"><circle cx="200" cy="130" r="12"/></g>
""", ground=True, arrow=True)

add('recycle', '使い終わった容器が、ぐるりと回って新しい品に戻るイラスト。', f"""
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="14" stroke-linecap="round">
  <path d="M300 100a140 140 0 0 1 120 210" marker-end="url(#ar)"/>
  <path d="M420 310a140 140 0 0 1-240 0" marker-end="url(#ar)"/>
  <path d="M180 310a140 140 0 0 1 120-210" marker-end="url(#ar)"/>
</g>
<g transform="translate(300 210)">
  <path d="M-40-40h80l-8 80h-64z" fill="#f4fbff" class="o"/>
  <path d="M-40-40h80" class="a"/>
</g>
""", ground=False, arrow=True)

add('refer', '辞書のページを指して、そこを参照しているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="bluep"/>
<g transform="translate(330 260)">
  <path d="M0 30q-70-40-150-20v-120q80-20 150 20z" class="bluep o"/>
  <path d="M0 30q70-40 150-20v-120q-80-20-150 20z" class="bluep o"/>
  <path d="M0-90v120" class="a"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-130-60h100M-130-36h90M20-60h100M20-36h90"/></g>
</g>
{hand(250,180,1)}
<path d="M290 210l-20 20" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('remarkable', 'ふつうの結果の中に、飛び抜けて高い一本の棒があるイラスト。', f"""
<path d="M60 340h480" class="a"/>
<g class="tealp o">
  <rect x="90" y="270" width="50" height="70"/><rect x="160" y="250" width="50" height="90"/>
  <rect x="230" y="280" width="50" height="60"/><rect x="400" y="260" width="50" height="80"/><rect x="470" y="276" width="50" height="64"/>
</g>
<rect x="310" y="110" width="60" height="230" class="coral o"/>
<g class="golds" style="stroke-width:4"><path d="M340 80V56M290 100l-20-20M390 100l20-20"/></g>
""", ground=False)

add('reply', '届いた手紙に、返事を書いて送り返しているイラスト。', f"""
<g transform="translate(180 210) rotate(-8)">
  <path d="M-70-46h140v92h-140z" class="paper"/>
  <path d="M-70-46L0 6l70-52" fill="none" class="a"/>
</g>
<g transform="translate(420 280) rotate(6)">
  <path d="M-70-46h140v92h-140z" class="paper"/>
  <path d="M-70-46L0 6l70-52" fill="none" class="a"/>
  <circle cx="50" cy="30" r="12" class="coral o"/>
</g>
<path d="M270 180q60-30 110 40" class="a" marker-end="url(#ar)"/>
<path d="M330 320q-60 30-110-40" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('report', '調べた内容を書類にまとめて、相手に提出するイラスト。', f"""
{person(160,346,1.1,1,'teal','blue','give','short','neutral')}
{person(450,346,1.1,-1,'coral','gold','give','bob','neutral')}
<g transform="translate(300 240) rotate(-4)">
  <path d="M-70-90h140v180h-140z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-46-56h92M-46-30h92M-46-4h70"/></g>
  <g class="tealp o"><rect x="-46" y="20" width="40" height="40"/></g>
</g>
<path d="M250 170h100" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('rest', '作業を止めていすに座り、ひと休みしているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="tealp"/>
<g transform="translate(300 300)">
  <path d="M-70-20h140v18h-140z" class="goldp o"/>
  <path d="M-60 0v56M60 0v56" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M60-20v-90h16v90z" class="goldd o"/>
</g>
<g transform="translate(292 250) scale(0.9)">{person(0,0,1.0,1,'teal','blue','hold','short','smile')}</g>
<g class="muted"><path d="M400 200q-14-30 4-52M436 196q-14-34 6-56"/></g>
<path d="M120 350h360" class="a"/>
""", ground=True)

add('ring', '指にはめた輪の指輪と、輪の形を示したイラスト。', f"""
<circle cx="120" cy="100" r="56" class="goldp"/>
<g transform="translate(240 240)">
  <circle r="70" fill="none" stroke="{TONES['gold'][0]}" stroke-width="18"/>
  <path d="M0-70l-14-26h28z" class="goldp o"/>
</g>
<g transform="translate(430 260)">
  <path d="M-20-90h40v130h-40z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="0" cy="-30" r="26" fill="none" stroke="{TONES['gold'][0]}" stroke-width="10"/>
</g>
""", ground=True)

add('route', '出発点から目的地までの、決まった道筋を線で示したイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-240-140h480v280h-480z" class="paper"/>
  <path d="M-200 100q60-90 140-60t120-90 140 20" fill="none" stroke="{TONES['blue'][0]}" stroke-width="10" stroke-dasharray="18 12"/>
  <circle cx="-200" cy="100" r="14" class="teal o"/>
  <circle cx="200" cy="-30" r="14" class="coral o"/>
</g>
<path d="M120 340h360" class="a"/>
""", ground=True)

add('routine', '毎日同じ順番でこなす手順が、輪になって繰り返されるイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="10">
  <circle cx="300" cy="210" r="130" stroke-dasharray="22 16"/>
</g>
<g transform="translate(300 80)">{sun(0,0,26)}</g>
<g transform="translate(430 210)">
  <path d="M-26-26h52v52h-52z" class="goldp o"/>
</g>
<g transform="translate(300 340)">
  <path d="M-30-16h60v32h-60z" class="tealp o"/>
</g>
<g transform="translate(170 210)">
  <circle r="26" class="violetp o"/>
</g>
<path d="M380 120a140 140 0 0 1 40 60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('ruin', '崩れて柱だけが残った建物の廃墟のイラスト。', f"""
<g fill="none" stroke="{INK}" stroke-width="3">
  <path d="M100 340V180h40v160z" fill="#cfc7b8"/>
  <path d="M200 340V210h40v130z" fill="#cfc7b8"/>
  <path d="M360 340V160h40v180z" fill="#cfc7b8"/>
  <path d="M460 340V240h40v100z" fill="#cfc7b8"/>
</g>
<path d="M80 340h440" class="a"/>
<g fill="#cfc7b8" stroke="{INK}" stroke-width="2.5"><path d="M280 340q10-30 40-20t20 20z"/></g>
<g class="muted"><path d="M140 160v-30M380 140v-30"/></g>
""", ground=True)

add('sail', '帆に風を受けて、ヨットが水面を進むイラスト。', f"""
<path d="M0 280h600v120H0z" class="bluep"/>
<path d="M0 280q60-14 120 0t120 0 120 0 120 0 120 0" class="a"/>
<g transform="translate(300 250)">
  <path d="M-110 0h220l-30 34h-160z" class="teal o"/>
  <path d="M0 0v-160" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <path d="M8-152q70 60 60 140H8z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M-8-140q-50 60-44 128h44z" fill="#f4fbff" stroke="{INK}" stroke-width="3"/>
</g>
<g class="muted"><path d="M60 130q100-30 180 0" marker-end="url(#ar)"/></g>
""", ground=False, arrow=True)

add('sailor', '船の上で働く船員のイラスト。帽子とロープを持っている。', f"""
<path d="M0 300h600v100H0z" class="bluep"/>
<path d="M0 300q60-14 120 0t120 0 120 0 120 0 120 0" class="a"/>
<g transform="translate(300 300)">
  <path d="M-200 0h400l-30 40h-340z" class="teal o"/>
  <path d="M-200 0h400" class="a"/>
</g>
{person(280,300,1.1,1,'blue','blue','hold','cap','smile')}
<g transform="translate(360 250)">
  <path d="M0 0q40 30 0 60" fill="none" stroke="{TONES['gold'][0]}" stroke-width="9"/>
</g>
""", ground=False)

add('save', '使わずに残したお金を、貯金箱に入れて取っておくイラスト。', f"""
<circle cx="470" cy="96" r="54" class="greenp"/>
<g transform="translate(290 290)">
  <ellipse cy="0" rx="110" ry="76" class="coralp o"/>
  <circle cx="86" cy="-30" r="34" class="coralp o"/>
  <path d="M104-44l24-10-12 26z" class="coral o"/>
  <path d="M-70 66v24M-20 72v20M30 72v20M70 62v28" fill="none" stroke="{TONES['coral'][2]}" stroke-width="14" stroke-linecap="round"/>
  <path d="M-30-70h60v10h-60z" class="ink"/>
  <circle cx="80" cy="-38" r="4" class="ink"/>
</g>
<g transform="translate(290 150)">
  <circle r="24" class="goldp o"/>
  <path d="M-7-10h14v20h-14z" class="goldd"/>
</g>
<path d="M290 190v20" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('scan', 'ページ全体を上から下へ、視線でざっと走らせているイラスト。', f"""
<g transform="translate(280 230)">
  <path d="M-140-140h280v280h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M-110 {-100+i*32}h220"/>' for i in range(7))}
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)">
  <path d="M150 120h270"/><path d="M420 170H150"/><path d="M150 220h270"/><path d="M420 270H150"/>
</g>
""", ground=True, arrow=True)

add('scenery', '山と湖が広がる、遠くまで見える風景のイラスト。', f"""
{sun(500,80,44)}
<path d="M40 250L200 90l120 120 90-70 150 110z" class="tealp o"/>
<path d="M0 250h600v150H0z" class="bluep"/>
<path d="M0 250h600" class="a"/>
{tree(90,330,0.7)}{tree(520,340,0.6)}
<g class="blues" opacity=".7"><path d="M100 300q50-14 100 0t100 0M340 350q50-14 100 0t100 0"/></g>
""", ground=False)

add('script', 'せりふが並んだ台本を開いて読んでいるイラスト。', f"""
<circle cx="120" cy="100" r="56" class="violetp"/>
<g transform="translate(320 250)">
  <path d="M0 30q-70-40-150-20v-130q80-20 150 20z" class="paper"/>
  <path d="M0 30q70-40 150-20v-130q-80-20-150 20z" class="paper"/>
  <path d="M0-100v130" class="a"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    <path d="M-130-70h40M-80-70h50M-130-46h100M-130-22h80"/>
    <path d="M30-70h40M80-70h50M30-46h100M30-22h80"/>
  </g>
</g>
<path d="M120 340h380" class="a"/>
""", ground=True)

add('seat', '背もたれのあるいすの座面を示したイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g transform="translate(280 260)">
  <path d="M-90-16h180v22h-180z" class="gold o"/>
  <path d="M-80 6v90M80 6v90" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"/>
  <path d="M70-16v-110h20v110z" class="goldd o"/>
  <path d="M-70-40h140v24h-140z" class="goldp o" opacity=".8"/>
</g>
<path d="M180 210h60" class="a" marker-end="url(#ar)" transform="rotate(180 210 210)"/>
<path d="M120 360h360" class="a"/>
""", ground=True, arrow=True)

add('seem', '布をかぶった形が、見た目では何かに見えているイラスト。', f"""
<g transform="translate(280 280)">
  <path d="M-120 60V-30h240V60z" class="muted"/>
  <path d="M-150 60q-20-100 40-130 50-24 110-24t110 24q60 30 40 130z" class="violetp o"/>
  <path d="M-150 60q60 20 150 20t150-20" fill="none" class="a"/>
</g>
<g transform="translate(470 160)" fill="{INK}">
  <path d="M-26-36q0-26 26-26t26 26q0 18-20 24v12h-12v-20q20-2 20-16 0-12-14-12t-14 12z"/>
  <circle cy="30" r="7"/>
</g>
""", ground=True)

add('shake', 'びんを上下に振って、中身をかき混ぜているイラスト。', f"""
{hand(300,140,1)}
<g transform="translate(300 260)">
  <path d="M-50-70h100l-8 140h-84z" fill="#f4fbff" class="o"/>
  <path d="M-50-70h100" class="a"/>
  <path d="M-42-20h84l-6 90h-72z" class="coralp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M420 200v-40"/><path d="M420 260v40"/></g>
<g class="muted"><path d="M200 210q-14 20-14 40M400 210q14 20 14 40"/></g>
""", ground=True, arrow=True)

add('sincere', '胸に手を当てて、心からの気持ちを伝えているイラスト。', f"""
<circle cx="300" cy="130" r="70" class="coralp"/>
<g transform="translate(300 176)"><path d="M0 30l-34-42 16-20 18 18 18-18 16 20z" class="coral o"/></g>
{person(300,346,1.3,1,'teal','blue','hold','short','smile')}
<circle cx="300" cy="266" r="16" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('racial', '肌の色が違う人たちが、同じ輪の中に並んでいるイラスト。', f"""
<circle cx="300" cy="220" r="160" class="tealp" opacity=".4"/>
{person(170,346,1.0,1,'teal','blue','stand','short','smile')}
{person(300,346,1.0,1,'coral','gold','stand','bob','smile')}
{person(430,346,1.0,1,'violet','teal','stand','cap','smile')}
<g fill="#8a5a3c" stroke="#5f3d28" stroke-width="2.5"><circle cx="300" cy="238" r="24"/></g>
<path d="M276 226q4-26 26-26 22 0 26 24-14-8-28-2-10-6-24 4z" fill="{HAIR}"/>
<g fill="{INK}"><circle cx="292" cy="238" r="2.2"/><circle cx="308" cy="238" r="2.2"/></g>
<path d="M292 250q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('renowned', '受賞のメダルとともに、名の知られた人が紹介されるイラスト。', f"""
<circle cx="300" cy="140" r="80" class="goldp"/>
{person(300,346,1.25,1,'violet','blue','stand','bun','smile')}
<g transform="translate(300 270)">
  <circle r="30" class="gold o"/>
  <path d="M-18-30l-16-40h32l10 30zM18-30l16-40h-32l-10 30z" class="coral o"/>
  <circle r="14" class="goldp o"/>
</g>
<g class="golds" style="stroke-width:4"><path d="M180 180l-26-26M420 180l26-26M170 260h-30M430 260h30"/></g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('number', '数字の並びと、対応する個数の点を示したイラスト。', f"""
<g class="tealp o">
  <circle cx="140" cy="200" r="22"/>
  <circle cx="280" cy="180" r="22"/><circle cx="320" cy="220" r="22"/>
  <circle cx="440" cy="160" r="22"/><circle cx="480" cy="200" r="22"/><circle cx="440" cy="240" r="22"/>
</g>
<g fill="{INK}">
  <rect x="130" y="300" width="10" height="40"/>
  <path d="M264 300h44v10l-34 30h34v10h-48v-12l34-28h-30z"/>
  <path d="M424 300h44v10l-16 14 16 14v12h-44v-10h30l-14-14 14-12h-30z"/>
</g>
<path d="M60 270h480" class="muted"/>
""", ground=False)

add('need', '砂漠で水を求めて、水筒を差し出されるイラスト。', f"""
<path d="M0 280q120-40 240-10t360-20v150H0z" fill="#efdcb8" stroke="{INK}" stroke-width="3"/>
{sun(500,80,42)}
{person(220,340,1.1,1,'coral','blue','reach','cap','sad')}
<g transform="translate(360 270)">
  <path d="M-34-50h68l-8 100h-52z" class="tealp o"/>
  <path d="M-14-60h28v10h-28z" class="ink"/>
  {drop(0,-84,1.1)}
</g>
<path d="M290 250h40" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)
print(' '.join(W)); print(sheet(W))
