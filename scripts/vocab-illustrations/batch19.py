"""第19回: 生活・行動・器具など30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('visible', '霧が晴れて、遠くの山がはっきり見えているイラスト。', f"""
<path d="M60 300L240 120l140 140 90-70 130 110z" class="tealp o"/>
<g opacity=".35"><path d="M0 60h240v260H0z" fill="#ffffff"/></g>
<path d="M0 300h600v100H0z" class="ground"/>
<path d="M0 300h600" class="a"/>
{person(120,340,0.85,1,'coral','blue','point','short','smile')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><path d="M190 220h140" marker-end="url(#ar)"/></g>
""", ground=False, arrow=True)

add('vital', '心臓が動き続け、生命を支えていることを示したイラスト。', f"""
<circle cx="300" cy="200" r="150" class="coralp" opacity=".4"/>
<g transform="translate(280 190)">
  <path d="M0 70l-70-84 34-42 36 34 36-34 34 42z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][2]}" stroke-width="5" stroke-linecap="round">
  <path d="M80 320h100l20-40 30 80 26-60 20 20h180"/>
</g>
<g class="corals" opacity=".7" style="stroke-width:4"><circle cx="280" cy="190" r="110" fill="none"/></g>
""", ground=False)

add('wave', '海面に立つ波が、次々と打ち寄せてくるイラスト。', f"""
<path d="M0 220h600v180H0z" class="bluep"/>
<path d="M0 240q60-60 140 0t140 0 140 0 140 0" fill="none" stroke="{TONES['blue'][0]}" stroke-width="8"/>
<path d="M0 300q60-60 140 0t140 0 140 0 140 0" fill="none" stroke="{TONES['blue'][0]}" stroke-width="8"/>
<path d="M0 360q60-60 140 0t140 0 140 0 140 0" fill="none" stroke="{TONES['blue'][0]}" stroke-width="8"/>
<path d="M120 160q120-40 240 0" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('weapon', '戦いに使う剣と盾を並べたイラスト。', f"""
<g transform="translate(220 240) rotate(-14)">
  <path d="M-10-140h20v200h-20z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-10-140l10-30 10 30z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-40 60h80v16h-80z" class="goldd o"/>
  <path d="M-8 76h16v50H-8z" class="goldd o"/>
</g>
<g transform="translate(400 250)">
  <path d="M-70-90h140v90q0 70-70 110-70-40-70-110z" class="tealp o"/>
  <path d="M0-90v200M-70 0h140" fill="none" stroke="{TONES['teal'][0]}" stroke-width="5"/>
</g>
""", ground=True)

add('wish', '流れ星に向かって、願いをかけているイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#2b3a4a"/>
<g fill="#f7e6a8"><circle cx="120" cy="90" r="4"/><circle cx="200" cy="140" r="3"/><circle cx="520" cy="230" r="3"/></g>
<g transform="translate(430 110)">
  <path d="M0-26l10 18 20 4-16 14 4 20-18-10-18 10 4-20-16-14 20-4z" class="gold o"/>
  <path d="M-20 10L-120 90" fill="none" stroke="#f7e6a8" stroke-width="4" stroke-linecap="round"/>
</g>
<g transform="translate(220 350)">{person(0,0,1.1,1,'violet','blue','hold','bob','smile')}</g>
<g fill="none" stroke="#f2c29d" stroke-width="0"></g>
""", ground=False)

add('worry', '頭の上に心配の雲がかかり、眉を寄せている人のイラスト。', f"""
{person(220,346,1.2,1,'teal','blue','think','short','sad')}
{cloud(400,160,1.6,'violet')}
<g class="muted"><path d="M400 200v30M440 210v24M360 208v26"/></g>
<g fill="{INK}"><path d="M420 240q0-24 24-24t24 24q0 16-18 22v10h-10v-18q18-2 18-14 0-10-14-10t-14 10z"/><circle cx="444" cy="290" r="6"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('yard', '家の前の芝生の庭を、囲いとともに描いたイラスト。', f"""
<path d="M0 230h600v170H0z" fill="#e4efe2"/>
<path d="M0 230h600" class="a" opacity=".4"/>
{building(300,240,0.7,'teal')}
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="9" stroke-linecap="round">
  <path d="M60 300v70M160 300v70M260 300v70M360 300v70M460 300v70M540 300v70M40 320h520"/>
</g>
{tree(120,300,0.6)}
""", ground=False)

add('able', '重い荷物を難なく持ち上げられる人のイラスト。', f"""
<circle cx="470" cy="96" r="54" class="greenp"/>
{box(280,220,120,86,0,'gold')}
<path d="M220 270l-30 30M340 270l30 30" fill="none" stroke="{SKIN}" stroke-width="18" stroke-linecap="round"/>
{person(280,366,1.25,1,'teal','blue','up','short','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M430 300l20 20 34-40"/></g>
""", ground=True)

add('account', '銀行の口座に残高が記録されているイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-160-120h320v240h-320z" class="paper"/>
  <path d="M-160-120h320v50h-320z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-120-40h240M-120 0h240M-120 40h180"/></g>
  <g class="goldp o"><rect x="60" y="60" width="90" height="34"/></g>
</g>
<g transform="translate(300 380)"><circle r="0"/></g>
<path d="M120 380h360" class="a"/>
""", ground=True)

add('active', '動き回って、休まず活動している人のイラスト。', f"""
<circle cx="470" cy="96" r="54" class="coralp"/>
{person(180,346,1.1,1,'coral','blue','walk','short','smile')}
<g opacity=".4">{person(300,346,1.1,1,'coral','blue','up','short','smile')}</g>
{person(430,346,1.1,1,'coral','blue','walk','short','smile')}
<path d="M120 200q120-60 240 0t120-20" class="muted" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('activist', '主張を書いた板を掲げて、行動している人のイラスト。', f"""
{person(240,346,1.2,1,'coral','blue','up','bun','neutral')}
<g transform="translate(240 170)">
  <path d="M-80-50h160v80h-160z" class="paper"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M-56-24h112M-56 4h80"/></g>
  <path d="M-6 30h12v60H-6z" class="goldd o"/>
</g>
<g opacity=".7">{person(430,346,1.0,1,'violet','gold','up','short','neutral')}</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('admire', '見事な絵の前で、感心して見入っているイラスト。', f"""
<g transform="translate(420 220)">
  <path d="M-110-110h220v220h-220z" class="goldd o"/>
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <path d="M-60 60l50-90 40 50 40-60 30 100z" class="tealp o"/>
  <circle cx="40" cy="-50" r="22" class="goldp o"/>
</g>
{person(160,346,1.15,1,'coral','blue','hold','bob','smile')}
<g class="golds" style="stroke-width:4"><path d="M240 200l24-24M250 250h26"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M230 220h70" marker-end="url(#ar)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('admit', '受付で身分証を見せ、入場を認められるイラスト。', f"""
<g transform="translate(450 240)">
  <path d="M-90-120h180v240h-180z" fill="#e0d6c2" stroke="{INK}" stroke-width="3"/>
  <path d="M-40-20h80v140h-80z" class="goldd o"/>
</g>
{person(180,346,1.1,1,'teal','blue','give','short','neutral')}
<g transform="translate(280 250)">
  <path d="M-44-30h88v60h-88z" class="paper"/>
  <circle cx="-18" cy="-6" r="12" class="tealp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M4-10h30M4 4h24"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M340 180l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('adult', '子どもと大人が並び、体の大きさの違いを示したイラスト。', f"""
{person(220,346,1.35,1,'teal','blue','stand','short','smile')}
{person(400,346,0.8,1,'coral','gold','stand','bob','smile')}
<path d="M150 152h140M340 250h120" class="muted"/>
<path d="M140 152v194M470 250v96" class="muted"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('advise', '相談相手に助言を伝えているイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','point','short','neutral')}
{person(440,346,1.1,-1,'coral','gold','think','bob','neutral')}
<g transform="translate(300 190)">
  <path d="M-66-40h132q16 0 16 16v42q0 16-16 16h-90l-26 22 6-22h-22q-16 0-16-16v-42q0-16 16-16z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-40-14h80M-40 6h56"/></g>
  <circle cx="52" cy="-4" r="10" class="goldp o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('age', '若い木が年月を経て、太く大きく育つイラスト。', f"""
{tree(160,340,0.7)}
{tree(430,340,1.3)}
<path d="M250 200h100" class="a" marker-end="url(#ar)"/>
<g fill="{INK}"><circle cx="240" cy="250" r="0"/></g>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('aim', '弓を構えて、的の中心へ狙いを定めているイラスト。', f"""
<g transform="translate(450 220)">
  <circle r="90" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <circle r="64" class="coralp o"/><circle r="38" fill="#fffdf6" stroke="{INK}" stroke-width="3"/><circle r="14" class="coral o"/>
</g>
<g transform="translate(180 220)">
  <path d="M-30-90a110 110 0 0 1 0 180" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10"/>
  <path d="M-30-90L-30 90" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M-30 0h150" fill="none" stroke="{TONES['gold'][2]}" stroke-width="7"/>
  <path d="M120 0l-16-10v20z" class="ink"/>
</g>
<path d="M300 260h60" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('aircraft', '空を飛ぶ航空機を、雲とともに描いたイラスト。', f"""
{cloud(120,110,1.2)}{cloud(470,270,1.0)}
{plane(300,200,1.2,-6,'blue')}
<path d="M100 280q100-40 160-56" class="muted"/>
""", ground=False)

add('alarm', 'ベルが鳴って、警報を知らせているイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-90 20a90 100 0 0 1 180 0z" class="coral o"/>
  <path d="M-100 20h200v20h-200z" class="coralp o"/>
  <path d="M0-80v-20" class="a"/>
  <circle cy="60" r="16" class="coral o"/>
  <path d="M-60-70l-30-30M60-70l30-30" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
</g>
<g class="corals" opacity=".9" style="stroke-width:5">
  <path d="M420 200q26 26 26 46t-26 46"/><path d="M180 200q-26 26-26 46t26 46"/>
</g>
""", ground=True)

add('alive', '芽が出て葉を広げ、生きて育っている植物のイラスト。', f"""
{sun(480,90,44)}
<path d="M0 300h600v100H0z" fill="#e7d9c4"/>
<path d="M0 300h600" class="a"/>
<g transform="translate(280 300)">
  <path d="M0 0v-140" fill="none" stroke="{TONES['green'][2]}" stroke-width="9" stroke-linecap="round"/>
  <path d="M0-60c-46-10-60-38-60-38 42-10 60 38 60 38z" class="green o"/>
  <path d="M0-100c46-10 60-38 60-38-42-10-60 38-60 38z" class="green o"/>
  <path d="M0-140c-30-16-30-48-30-48 30 6 30 48 30 48z" class="green o"/>
</g>
<g class="greens" style="stroke-width:4"><path d="M180 180l-20-20M380 160l20-20"/></g>
""", ground=False)

add('alone', 'ほかに誰もいない場所に、一人だけ座っているイラスト。', f"""
<g transform="translate(300 330)">
  <path d="M-100-20h200v18h-200z" class="goldp o"/>
  <path d="M-90 0v50M90 0v50" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
</g>
<g transform="translate(290 310)">
  <path d="M-30-70q30-14 60 0l-8 68h-44z" class="teal o"/>
  <path d="M-24-8l-56 20M20-8l14 30" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-26-58l-30 34M26-58l26 26" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
  <circle cx="0" cy="-96" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-24-98q3-28 25-28 24 0 28 25-13-10-27-4-12-11-26 7z" fill="{HAIR}"/>
  <circle cx="-8" cy="-92" r="2.2" class="ink"/><circle cx="8" cy="-92" r="2.2" class="ink"/>
  <path d="M-8-80h16" class="a"/>
</g>
<g class="muted"><path d="M80 240h100M420 240h100"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('ambulance', 'サイレンを鳴らして走る救急車のイラスト。', f"""
<g transform="translate(300 270)">
  <path d="M-180 50h360v-90q0-40-40-40h-260l-60 60z" fill="#fffdf6" class="o"/>
  <path d="M-176-10h80v-46h-34z" class="bluep o"/>
  <path d="M-80-56h60v46h-60z" class="bluep o"/>
  <circle cx="-120" cy="62" r="30" class="ink"/><circle cx="110" cy="62" r="30" class="ink"/>
  <path d="M50-10h20v-40h30v-20h-30v-40H50v40H20v20h30z" class="coral o"/>
  <path d="M-40-90h80v20h-80z" class="coral o"/>
</g>
<g class="corals" opacity=".9" style="stroke-width:5"><path d="M170 130q26 20 26 40M470 130q-26 20-26 40"/></g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('analyse', 'データの山を細かく分けて、内訳を調べているイラスト。', f"""
<g transform="translate(160 250)">
  <circle r="90" class="tealp o"/>
  <path d="M0 0v-90a90 90 0 0 1 78 45z" class="coralp o"/>
  <path d="M0 0l78 45a90 90 0 0 1-78 45z" class="goldp o"/>
</g>
<g transform="translate(420 260)">
  <path d="M-110 60h220" class="a"/>
  <g class="tealp o"><rect x="-90" y="-20" width="40" height="80"/><rect x="-30" y="-60" width="40" height="120"/><rect x="30" y="0" width="40" height="60"/></g>
</g>
<path d="M270 250h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('announce', 'マイクを使って、大勢に向けて発表しているイラスト。', f"""
{person(190,346,1.2,1,'teal','blue','point','short','neutral')}
<g transform="translate(260 236)">
  <path d="M-16-14h32v28h-32z" class="ink"/>
  <path d="M16-4l60-30v56z" class="ink" opacity=".8"/>
</g>
<g class="teals" opacity=".9" style="stroke-width:5">
  <path d="M370 190q30 30 30 56t-30 56"/><path d="M420 170q38 38 38 76t-38 76"/>
</g>
<g opacity=".6">{person(510,346,0.8,-1,'coral','gold','stand','bob','smile')}</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('annoy', '近くの音がうるさくて、いらいらしている人のイラスト。', f"""
{person(200,346,1.2,1,'coral','blue','hold','short','sad')}
<circle cx="160" cy="238" r="15" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<circle cx="240" cy="238" r="15" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<g transform="translate(440 250)">
  <path d="M-60-60h120v120h-120z" class="goldp o"/>
  <circle r="26" class="gold o"/>
</g>
<g class="corals" opacity=".9" style="stroke-width:5">
  <path d="M350 210q-26 26-26 40t26 40"/><path d="M310 190q-34 34-34 60t34 60"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('apparatus', '実験用の器具が組み合わされた装置のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-200-20h400v20h-400z" fill="#dfe6ea" class="o"/>
</g>
<g transform="translate(200 220)">
  <path d="M-10-70h20v30l36 60H-46l36-60z" fill="#f4fbff" class="o"/>
  <path d="M-40 20h80l10 12H-50z" class="coralp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="6"><path d="M200 150q80-60 160 0"/></g>
<g transform="translate(380 240)">
  <path d="M-14-80h28v66a14 14 0 0 1-28 0z" fill="#f4fbff" class="o"/>
  <path d="M-14-30h28v16a14 14 0 0 1-28 0z" class="greenp o"/>
</g>
<path d="M180 280v-30M380 280v-20" fill="none" stroke="{INK}" stroke-width="8"/>
""", ground=True)

add('arms', '軍の武器がまとめて並べられているイラスト。', f"""
<g transform="translate(300 260)">
  {''.join(f'<g transform="translate({-160+i*80} 0) rotate({-8+i*8})"><path d="M-8-90h16v150h-16z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/><path d="M-8-90l8-24 8 24z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/><path d="M-28 60h56v14h-56z" class="goldd o"/></g>' for i in range(5))}
</g>
<path d="M60 350h480" class="a"/>
""", ground=True)

add('arrest', '手錠をかけられて、警官に連れられていくイラスト。', f"""
{person(240,346,1.1,1,'coral','blue','hold','short','sad')}
{person(400,346,1.1,-1,'blue','violet','point','cap','neutral')}
<g transform="translate(300 264)">
  <circle cx="-24" r="20" fill="none" stroke="{MUTED}" stroke-width="7"/>
  <circle cx="24" r="20" fill="none" stroke="{MUTED}" stroke-width="7"/>
  <path d="M-4 0h8" fill="none" stroke="{MUTED}" stroke-width="6"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('asleep', 'ベッドで目を閉じて眠っている人のイラスト。', f"""
<g transform="translate(280 300)">
  <path d="M-160-20h320v50h-320z" class="tealp o"/>
  <path d="M-170 30h340v20h-340z" class="goldd o"/>
  <ellipse cx="-100" cy="-40" rx="50" ry="26" fill="#fffdf6" class="o"/>
  <g transform="translate(-100 -60)">
    <circle r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <path d="M-26-4q3-28 25-28 24 0 28 25-13-10-27-4-12-11-26 7z" fill="{HAIR}"/>
    <path d="M-12 2h8M6 2h8" class="a"/>
  </g>
</g>
<g fill="{INK}" opacity=".7">
  <path d="M360 200q0-14 14-14t14 14q0 8-14 14h14v10h-30v-8q14-6 14-12 0-6-6-6t-6 6z"/>
  <path d="M400 160q0-12 12-12t12 12q0 8-12 12h12v8h-26v-6q12-6 12-10 0-4-6-4t-4 4z"/>
</g>
<path d="M80 370h440" class="a"/>
""", ground=True)

add('assistance', '荷物を運ぶ人を、もう一人が支えて手助けするイラスト。', f"""
<circle cx="470" cy="96" r="54" class="greenp"/>
{person(230,346,1.1,1,'coral','blue','carry','short','neutral')}
{box(300,266,110,74,0,'gold')}
{person(400,346,1.1,-1,'green','violet','give','bob','smile')}
<path d="M356 272h-40" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M130 200l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('association', '複数の点が線で結ばれ、関連づけられているイラスト。', f"""
<g class="tealp o">
  <circle cx="150" cy="160" r="34"/><circle cx="450" cy="160" r="34"/><circle cx="300" cy="300" r="34"/><circle cx="300" cy="120" r="34"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="4">
  <path d="M184 160h82M334 160h82M300 154v112M180 186l96 96M420 186l-96 96"/>
</g>
<path d="M60 360h480" class="muted"/>
""", ground=False)

add('attach', '書類にクリップを付けて、まとめて留めているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="bluep"/>
<g transform="translate(280 250)">
  <g transform="rotate(-6)"><path d="M-90-110h180v220h-180z" class="paper"/></g>
  <g transform="rotate(3) translate(0 -10)"><path d="M-90-110h180v220h-180z" class="paper"/>
    <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-60h120M-60-30h120M-60 0h90"/></g>
  </g>
  <g transform="translate(-70 -110) rotate(-10)">
    <path d="M-16-30v54a16 16 0 0 0 32 0v-44a10 10 0 0 1 20 0v50" fill="none" stroke="{MUTED}" stroke-width="6"/>
  </g>
</g>
<path d="M430 180q-40 0-70-20" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)
print(' '.join(W)); print(sheet(W))
