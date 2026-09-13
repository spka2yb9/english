"""第37回: 耐える・超える・評価・展示など42語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('ending', '物語の最後のページに、終わりの印があるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-140-140h280v280h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-100 {-100+i*30}h200"/>' for i in range(6))}</g>
  <path d="M-40 100h80v10h-80z" class="ink"/>
</g>
<path d="M470 300q-40-20-60-30" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('endorse', '書類に署名して、正式に支持を示すイラスト。', f"""
{person(160,346,1.15,1,'blue','violet','point','short','smile')}
<g transform="translate(400 250)">
  <path d="M-110-100h220v200h-220z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-80-60h160M-80-30h160"/></g>
  <path d="M-80 40q40-20 70 0t70-10" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round"><path d="M40 70l14 14 26-30"/></g>
</g>
<path d="M250 220h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('endure', '重い荷を背負っても、耐えて立ち続けるイラスト。', f"""
{box(300,180,160,90,0,'gold')}
<path d="M240 240l-30 30M360 240l30 30" fill="none" stroke="{SKIN}" stroke-width="18" stroke-linecap="round"/>
{person(300,366,1.25,1,'teal','blue','up','short','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M180 160v70"/><path d="M420 160v70"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M480 300l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('energy', '電池から力が送り出されて、装置が動くイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-60-70h120v140h-120z" class="tealp o"/>
  <path d="M-20-84h40v14h-40z" class="ink"/>
  <path d="M-14-30l-16 46h20l-10 34 30-50h-20l16-30z" class="gold o"/>
</g>
<g transform="translate(430 250)">
  <circle r="60" fill="none" stroke="{INK}" stroke-width="6"/>
  <g class="tealp o"><path d="M0 0q50-30 60 16-36 24-60-16z"/><path d="M0 0q-30 50-66 14 24-36 66-14z"/><path d="M0 0q-18-56 36-56 8 42-36 56z"/></g>
</g>
<path d="M260 250h100" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('enforce', '規則の札を示して、従わせているイラスト。', f"""
{person(430,346,1.15,-1,'blue','violet','point','cap','neutral')}
{person(180,346,1.1,1,'coral','blue','stand','short','neutral')}
<g transform="translate(320 200)">
  <path d="M-60-40h120v80h-120z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-36-16h72M-36 6h50"/></g>
</g>
<path d="M280 260h-40" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M110 200l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('engaged', '指輪をつけた手を見せて、婚約を示すイラスト。', f"""
<circle cx="300" cy="150" r="76" class="coralp"/>
<g transform="translate(300 200)">
  <path d="M-26-70h52v130h-52z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cy="-10" r="30" fill="none" stroke="{TONES['gold'][0]}" stroke-width="10"/>
  <path d="M0-40l-12-16h24z" class="gold o"/>
</g>
<path d="M120 360h360" class="a"/>
""", ground=True)

add('engineer', '設計図と工具を持って、機械を扱う技師のイラスト。', f"""
{person(170,346,1.15,1,'gold','blue','point','cap','neutral')}
<g transform="translate(410 250)">
  <path d="M-110-90h220v180h-220z" fill="#dfe6ea" class="o"/>
  <circle cx="-40" cy="-20" r="40" fill="none" stroke="{INK}" stroke-width="12"/>
  <circle cx="40" cy="30" r="26" fill="none" stroke="{INK}" stroke-width="9"/>
</g>
<g transform="translate(270 260) rotate(-20)">
  <path d="M-40-16h80v32h-80z" class="goldd o"/>
  <path d="M40-22h26v44H40z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('enhance', 'ぼやけた絵が、鮮やかで見やすくなるイラスト。', f"""
<g transform="translate(170 230)" opacity=".45">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <path d="M-60 50l50-80 40 46 40-56 26 90z" class="tealp o"/>
</g>
<g transform="translate(430 230)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <path d="M-60 50l50-80 40 46 40-56 26 90z" class="teal o"/>
  <circle cx="40" cy="-50" r="22" class="gold o"/>
</g>
<path d="M280 230h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('enormous', '人と比べて、はるかに大きな箱のイラスト。', f"""
{box(370,240,300,220,0,'gold')}
{person(120,346,0.9,1,'teal','blue','up','short','surprised')}
<path d="M180 340h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('enquire', '窓口で尋ねて、問い合わせているイラスト。', f"""
<g transform="translate(430 250)">
  <path d="M-110-120h220v240h-220z" fill="#dfe6ea" class="o"/>
  <path d="M-80-90h160v70h-160z" class="bluep o"/>
  <path d="M-60 20h120v20h-120z" class="ink"/>
</g>
{person(160,346,1.1,1,'teal','blue','point','bob','neutral')}
<g transform="translate(290 190)" fill="{INK}">
  <path d="M-16-30q0-20 16-20t16 20q0 14-12 18v10h-10v-16q12-2 12-12 0-8-8-8t-8 8z"/>
  <circle cy="18" r="6"/>
</g>
<path d="M240 240h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('enrich', '土に肥料を足して、作物が豊かに育つイラスト。', f"""
<path d="M0 260h600v140H0z" fill="#e7d9c4"/>
<path d="M0 260h600" class="a"/>
<g transform="translate(180 260)">
  <path d="M0 0v-50" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
  <path d="M0-30c-26-6-34-22-34-22 24-6 34 22 34 22z" class="green o"/>
</g>
<g transform="translate(430 260)">
  <path d="M0 0v-110" fill="none" stroke="{TONES['green'][2]}" stroke-width="9"/>
  <path d="M0-50c-46-10-60-38-60-38 42-10 60 38 60 38z" class="green o"/>
  <path d="M0-86c46-10 60-38 60-38-42-10-60 38-60 38z" class="green o"/>
</g>
<g fill="{TONES['gold'][2]}"><circle cx="300" cy="210" r="8"/><circle cx="330" cy="230" r="7"/><circle cx="280" cy="240" r="6"/></g>
<path d="M260 300h100" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('enrol', '名簿に名前を書いて、登録するイラスト。', f"""
<g transform="translate(320 250)">
  <path d="M-140-110h280v220h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-100 {-70+i*40}h200"/>' for i in range(4))}</g>
  <g fill="{INK}"><rect x="-90" y="-86" width="70" height="8"/><rect x="-90" y="-46" width="90" height="8"/></g>
</g>
{hand(150,190,1)}
<path d="M220 210h30" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('ensue', 'ある出来事のあとに、続けて次が起こるイラスト。', f"""
<path d="M60 230h480" class="a" marker-end="url(#ar)"/>
<g transform="translate(180 230)"><circle r="34" class="tealp o"/></g>
<g transform="translate(340 230)"><circle r="34" class="coralp o"/></g>
<g transform="translate(470 230)"><circle r="34" class="goldp o"/></g>
<path d="M220 320h220" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('enthusiastic', '身を乗り出して、熱心に取り組んでいるイラスト。', f"""
{person(220,346,1.2,1,'coral','blue','up','bun','smile')}
<g class="golds" style="stroke-width:5"><path d="M300 180l24-24M310 240h30M300 300l24 24"/></g>
<g transform="translate(450 250)">
  <path d="M-70-70h140v140h-140z" class="goldp o"/>
  <path d="M-40-40h80v80h-80z" class="gold o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('environmental', '木と水と空を守る、環境の輪を示したイラスト。', f"""
<circle cx="300" cy="220" r="150" fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-dasharray="18 12"/>
{tree(230,300,0.8)}
<g class="bluep o"><path d="M330 300q60-20 110 0v40q-60 20-110 0z"/></g>
{cloud(360,150,1.1)}
{sun(200,140,30)}
""", ground=False)

add('equal', '天びんが左右まったく同じ高さで釣り合うイラスト。', f"""
<path d="M300 340V140" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<path d="M250 356h100" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>
<path d="M150 150h300" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<circle cx="300" cy="150" r="13" class="teal o"/>
<path d="M150 150v34M450 150v34" class="a"/>
{box(150,220,80,60,0,'gold')}
{box(450,220,80,60,0,'gold')}
<g fill="{INK}"><rect x="270" y="240" width="60" height="10"/><rect x="270" y="266" width="60" height="10"/></g>
""", ground=True)

add('equip', '必要な装備をひとそろい身につけさせるイラスト。', f"""
{person(300,346,1.25,1,'gold','blue','stand','cap','neutral')}
<g transform="translate(300 216)">
  <path d="M-34 0a34 30 0 0 1 68 0z" class="gold o"/>
  <path d="M-38 0h76v10h-76z" class="goldd o"/>
</g>
<g transform="translate(420 300)">
  <path d="M-40-30h80v60h-80z" class="tealp o"/>
  <path d="M-20-30q0-20 20-20t20 20" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M140 200l18 18 30-36"/></g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('erect', '倒れていた柱を、まっすぐ立てるイラスト。', f"""
<g transform="translate(160 330) rotate(-70)"><path d="M-16-140h32v140h-32z" class="goldd o"/></g>
<g transform="translate(430 330)"><path d="M-16-190h32v190h-32z" class="goldd o"/></g>
<path d="M250 250a120 120 0 0 1 110-60" class="a" marker-end="url(#ar)"/>
<path d="M60 330h480" class="a"/>
""", ground=True, arrow=True)

add('essential', 'これを抜くと全体が成り立たない、中心の部品のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-160-100h320v200h-320z" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="12 8"/>
  <g class="tealp o"><rect x="-140" y="-80" width="80" height="80"/><rect x="60" y="-80" width="80" height="80"/><rect x="-140" y="20" width="80" height="60"/><rect x="60" y="20" width="80" height="60"/></g>
  <circle r="46" class="coral o"/>
</g>
<path d="M300 400v-40" class="a" marker-end="url(#ar)" transform="rotate(180 300 380)"/>
""", ground=False, arrow=True)

add('evacuate', '建物から人が外へ避難していくイラスト。', f"""
{building(160,300,0.95,'teal')}
<path d="M142 300v-46h36v46z" fill="#3d4c5c"/>
{person(340,346,0.95,1,'coral','blue','walk','short','surprised')}
{person(460,346,0.95,1,'teal','gold','walk','bob','surprised')}
<path d="M250 240h180" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:5"><path d="M160 180q-14-30 4-52"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('evaluate', '成果に点数をつけて、価値を測るイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-90-90h180v180h-180z" class="tealp o"/>
</g>
<g transform="translate(440 250)">
  <path d="M-70-50h140v100h-140z" class="paper"/>
  <g fill="{INK}"><rect x="-40" y="-20" width="12" height="40"/><path d="M-8-20h40v14h-26v6h26v20H-8z"/></g>
</g>
<path d="M310 250h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('evoke', '香りが、昔の場面を呼び起こすイラスト。', f"""
<g transform="translate(180 300)">
  <path d="M-50-40h100l-10 80h-80z" fill="#fffdf6" class="o"/>
  <g class="muted"><path d="M-20-50q-14-30 4-52M20-56q-14-34 6-56"/></g>
</g>
<g transform="translate(420 190)">
  <path d="M-120-60q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-156q-38-4-36-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 10) scale(0.6)">{tree(-40,40,0.8)}{sun(60,-20,24)}</g>
</g>
<path d="M260 200h40" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('exact', '目盛りにぴったり一致した値を示したイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-30h440v60h-440z" class="goldp o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">{''.join(f'<path d="M{-200+i*40} -30v{20 if i%2 else 30}"/>' for i in range(11))}</g>
</g>
<path d="M300 300V160" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M420 330l18 18 30-36"/></g>
""", ground=False)

add('exaggerate', '小さな事実が、話すうちに大きくなるイラスト。', f"""
<g transform="translate(150 300)"><circle r="26" class="tealp o"/></g>
<g transform="translate(300 280)"><circle r="52" class="tealp o"/></g>
<g transform="translate(460 250)"><circle r="86" class="tealp o"/></g>
<path d="M110 130h420" class="a" marker-end="url(#ar)"/>
<g transform="translate(150 180)">
  <path d="M-40-24h80q10 0 10 10v22q0 10-10 10h-52l-14 12 4-12q-10 0-10-10v-22q0-10 10-10z" class="paper"/>
</g>
""", ground=True, arrow=True)

add('exceed', '線で示した上限を、棒が超えているイラスト。', f"""
<path d="M60 340h480" class="a"/>
<path d="M60 180h480" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="14 10"/>
<g class="tealp o"><rect x="120" y="240" width="70" height="100"/><rect x="220" y="210" width="70" height="130"/><rect x="420" y="230" width="70" height="110"/></g>
<rect x="320" y="120" width="70" height="220" class="coral o"/>
<path d="M355 100V70" class="a" marker-end="url(#ar)" transform="rotate(180 355 85)"/>
""", ground=False, arrow=True)

add('excellent', '最高評価の星が三つ並んだイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-160-70h320v140h-320z" class="paper"/>
  {''.join(f'<g transform="translate({-100+i*100} 0)"><path d="M0-40l14 28 30 4-22 22 6 30-28-16-28 16 6-30-22-22 30-4z" class="gold o"/></g>' for i in range(3))}
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 340l18 18 30-36"/></g>
""", ground=True)

add('except', '並んだ丸の中で、一つだけ外されているイラスト。', f"""
<g class="tealp o">
  {''.join(f'<circle cx="{110+i*80}" cy="230" r="30"/>' for i in range(6) if i != 3)}
</g>
<g class="muted"><circle cx="350" cy="230" r="30"/></g>
<g class="corals" style="stroke-width:7"><path d="M330 210l40 40M370 210l-40 40"/></g>
<path d="M60 320h480" class="muted"/>
""", ground=False)

add('exclude', '囲いの外へ一つを出して、仲間から外すイラスト。', f"""
<circle cx="250" cy="230" r="130" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" stroke-dasharray="16 12"/>
<g class="tealp o"><circle cx="200" cy="200" r="34"/><circle cx="290" cy="210" r="34"/><circle cx="240" cy="290" r="34"/></g>
<circle cx="490" cy="290" r="34" class="coral o"/>
<path d="M390 260h60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('excuse', '遅れた理由を述べて、言い訳しているイラスト。', f"""
{person(180,346,1.15,1,'coral','blue','point','short','sad')}
{person(460,346,1.1,-1,'blue','violet','stand','cap','neutral')}
<g transform="translate(320 190)">
  <path d="M-70-40h140q16 0 16 16v40q0 16-16 16h-90l-24 20 6-20h-32q-16 0-16-16v-40q0-16 16-16z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-44-14h88M-44 8h60"/></g>
</g>
<g transform="translate(190 200)">
  <circle r="24" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0v-14M0 0l10 6" class="a"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('exert', '力を込めて、重い物を押し動かしているイラスト。', f"""
{person(200,346,1.15,1,'coral','blue','point','short','neutral')}
{box(400,290,130,100,0,'gold')}
<path d="M280 250h60" class="a" marker-end="url(#ar)" style="stroke-width:8"/>
<g class="corals" style="stroke-width:5"><path d="M170 200l-20-20M240 190l-6-26"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('exhibit', '展示台に品を並べて、見せているイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-190-20h380v20h-380z" class="goldp o"/>
  <g class="tealp o"><rect x="-160" y="-90" width="80" height="70"/></g>
  <g class="coralp o"><circle cx="0" cy="-56" r="36"/></g>
  <g class="violetp o"><path d="M110-90h80v70h-80z"/></g>
</g>
{person(120,346,0.85,1,'teal','blue','point','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('expected', '予想の点線どおりに、結果の線が進むイラスト。', f"""
<path d="M60 340h480M100 340V100" fill="none" stroke="{INK}" stroke-width="4"/>
<path d="M110 300l100-50 100-60 110-40" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
<path d="M110 300l100-50 100-60 110-40" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" opacity=".85"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 140l18 18 30-36"/></g>
""", ground=False)

add('experienced', '同じ作業を何度も重ねて、手慣れているイラスト。', f"""
<g opacity=".35">{person(140,346,0.95,1,'coral','blue','point','short','neutral')}</g>
<g opacity=".65">{person(280,346,1.05,1,'coral','blue','point','short','neutral')}</g>
{person(430,346,1.15,1,'coral','blue','point','short','smile')}
<path d="M100 180h420" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M500 260l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('expire', '期限の日付を過ぎて、券が使えなくなるイラスト。', f"""
<g transform="translate(280 240)">
  <path d="M-130-80h260v160h-260z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-100-40h200M-100-10h160"/></g>
  <g fill="{INK}"><rect x="-100" y="30" width="90" height="10"/></g>
  <g class="corals" style="stroke-width:6"><path d="M-140-90l280 180"/></g>
</g>
<g transform="translate(470 160)">
  <circle r="40" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0v-24M0 0l18 10" class="a"/>
</g>
""", ground=True)

add('exploit', '働かせた人から、利益だけを取り上げるイラスト。', f"""
{person(200,346,1.1,1,'gold','blue','carry','cap','sad')}
{box(200,266,90,64,0,'gold')}
{person(450,346,1.15,-1,'blue','violet','give','short','neutral')}
<g transform="translate(350 250)">
  <circle r="22" class="goldp o"/>
  <path d="M-7-10h14v20h-14z" class="goldd"/>
</g>
<path d="M300 210h60" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:6"><path d="M160 200l30 30M190 200l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('expose', '覆いを外して、中身を光の下にさらすイラスト。', f"""
{sun(480,100,44)}
<g transform="translate(280 290)">
  <path d="M-100 60V-30h200V60z" class="tealp o"/>
  <path d="M-100 60h200" class="a"/>
</g>
<g transform="translate(150 160) rotate(-24)">
  <path d="M-110-26q110-36 220 0-110 36-220 0z" class="violetp o"/>
</g>
<g class="golds" style="stroke-width:4"><path d="M380 180l-40 40M420 220l-50 30"/></g>
<path d="M280 220v-40" class="a" marker-end="url(#ar)" transform="rotate(180 280 200)"/>
""", ground=True, arrow=True)

add('extend', '短かった棒を引き伸ばして、長くするイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-100-20h200v40h-200z" class="tealp o"/>
</g>
<g transform="translate(300 300)">
  <path d="M-200-20h400v40h-400z" class="teal o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 250h-80"/><path d="M420 250h80"/></g>
""", ground=False, arrow=True)

add('extreme', '目盛りの端まで振り切れている、極端な状態のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-200-30h400v60h-400z" class="goldp o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">{''.join(f'<path d="M{-180+i*40} -30v20"/>' for i in range(10))}</g>
  <path d="M180 40V-50" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
</g>
<path d="M150 150h300" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('facilitate', '橋をかけて、渡るのを容易にするイラスト。', f"""
<path d="M0 260h600v140H0z" class="bluep"/>
<path d="M0 260h180v140H0zM420 260h180v140H420z" class="ground"/>
<path d="M0 260h180M420 260h180" class="a"/>
<path d="M150 220h300" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"/>
{person(300,214,0.6,1,'teal','blue','walk','short','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M480 150l18 18 30-36"/></g>
""", ground=False)

add('factory', '煙突のある工場で、製品が作られているイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-200 80V-40h400V80z" fill="#dfe6ea" class="o"/>
  <path d="M-200-40l60-50 60 50zM-80-40l60-50 60 50zM40-40l60-50 60 50z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M120-90h40v-60h-40z" class="ink"/>
  <g class="bluep o"><rect x="-160" y="0" width="60" height="50"/><rect x="-60" y="0" width="60" height="50"/><rect x="40" y="0" width="60" height="50"/></g>
</g>
<g fill="#c9ccd1" stroke="{MUTED}" stroke-width="2.5"><circle cx="450" cy="140" r="20"/><circle cx="482" cy="104" r="15"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)
print(len(W), ' '.join(W)); print(sheet(W))
