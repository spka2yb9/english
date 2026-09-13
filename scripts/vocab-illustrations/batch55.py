"""第55回: 境界・予算・祝賀・比較など40語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('bizarre', '魚が空を泳ぐ、ふつうでない奇妙なイラスト。', f"""
{cloud(150,110,1.0)}{cloud(430,90,0.8)}
<g transform="translate(300 230)">
  <ellipse rx="90" ry="50" class="tealp o"/>
  <path d="M-90 0l-50-40v80z" class="tealp o"/>
  <circle cx="50" cy="-12" r="7" class="ink"/>
</g>
<g fill="{INK}" transform="translate(480 260)">
  <path d="M0 0q0-32 24-32t24 32q0 18-20 22v16h-12v-26q18-4 18-18t-10-12-12 18z"/>
  <rect x="14" y="52" width="12" height="12"/>
</g>
{person(120,346,0.9,1,'coral','blue','up','short','surprised')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('bold', '高い所から思いきって飛び込む、大胆なイラスト。', f"""
<path d="M0 300h600v100H0z" class="bluep"/>
<g transform="translate(160 200)"><path d="M-80-40h100v240h-100z" fill="#c9d3dc" class="o"/></g>
<g transform="translate(300 190) rotate(30)">{person(0,0,1.0,1,'coral','blue','up','short','smile')}</g>
<path d="M370 180q60 60 80 110" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="#fffdf6" stroke-width="6"><path d="M420 310q40-24 80 0"/></g>
""", ground=False, arrow=True)

add('border', '二つの国を分ける境界線のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-140h220v280h-220z" class="tealp o"/>
  <path d="M0-140h220v280H0z" class="goldp o"/>
  <path d="M0-140v280" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-dasharray="20 14"/>
</g>
<g transform="translate(150 130)"><path d="M-4-40h8v50h-8z" class="ink"/><path d="M4-38h40v26H4z" class="teal o"/></g>
<g transform="translate(450 130)"><path d="M-4-40h8v50h-8z" class="ink"/><path d="M4-38h40v26H4z" class="gold o"/></g>
""", ground=False)

add('bound', '行き先が表示された列車のイラスト。', f"""
<g transform="translate(320 250)">
  <path d="M-180 60h360v-150h-360z" class="bluep o"/>
  <path d="M-140-60h100v60h-100zM40-60h100v60H40z" fill="#e8f4fb" stroke="{INK}" stroke-width="3"/>
  <path d="M-40-80h80v26h-80z" fill="#fffdf6" stroke="{INK}" stroke-width="2"/>
  <g fill="{INK}"><rect x="-28" y="-72" width="56" height="10"/></g>
  <circle cx="-100" cy="80" r="26" class="ink"/><circle cx="100" cy="80" r="26" class="ink"/>
</g>
<path d="M520 200h50" class="a" marker-end="url(#ar)"/>
<path d="M60 350h480" class="a"/>
""", ground=True, arrow=True)

add('brand', '同じ印がついた商品が並ぶイラスト。', f"""
<g transform="translate(300 260)">
  {box(-160,0,120,110,26,'teal')}
  {box(0,0,120,110,26,'teal')}
  {box(160,0,120,110,26,'teal')}
</g>
<g fill="#fffdf6">
  {''.join(f'<path d="M{140+i*160} 250l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z"/>' for i in range(3))}
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('breath', '口から白い息がふっと出るイラスト。', f"""
{face(220,200,85,'flat')}
<g transform="translate(220 240)"><ellipse rx="16" ry="12" fill="#8b4a3e"/></g>
<g fill="#fffdf6" stroke="{MUTED}" stroke-width="2" opacity=".9">
  <ellipse cx="330" cy="230" rx="40" ry="26"/><ellipse cx="400" cy="215" rx="30" ry="20"/><ellipse cx="455" cy="205" rx="20" ry="14"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('breathing', '胸がふくらんで、また戻る呼吸のイラスト。', f"""
<g transform="translate(220 250)">
  <circle cy="-120" r="40" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-80 130q0-130 80-130t80 130z" class="teal o"/>
</g>
<g opacity=".35" transform="translate(220 250)">
  <path d="M-100 130q0-150 100-150t100 150z" fill="none" stroke="{TONES['teal'][0]}" stroke-width="5"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M400 200h50M400 280h-50"/></g>
<g class="muted"><path d="M420 240h100"/></g>
""", ground=False, arrow=True)

add('brutal', '容赦なく打ちつける、荒々しいイラスト。', f"""
<g transform="translate(300 160) rotate(-16)">
  <path d="M-80-34h160v54h-160z" fill="#7f8ea6" stroke="{INK}" stroke-width="3"/>
  <path d="M-10 20h20v150h-20z" class="goldd o"/>
</g>
<g fill="#b6bfc9" stroke="{INK}" stroke-width="3">
  <path d="M170 340l40-60 30 40z"/><path d="M280 340l50-40 20 40z"/><path d="M380 340l40-50 40 50z"/>
</g>
<g class="corals" style="stroke-width:6"><path d="M140 250l-30 20M460 250l30 20M300 280v34"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('bubble', '水の中で丸いあわが立ちのぼるイラスト。', f"""
<path d="M0 60h600v340H0z" class="bluep"/>
<g fill="#e7f6fb" stroke="#9ec7dd" stroke-width="3" opacity=".9">
  <circle cx="200" cy="300" r="26"/><circle cx="260" cy="220" r="36"/><circle cx="180" cy="150" r="20"/>
  <circle cx="380" cy="270" r="30"/><circle cx="430" cy="180" r="22"/><circle cx="330" cy="120" r="16"/>
</g>
<g fill="#ffffff" opacity=".7"><circle cx="250" cy="208" r="9"/><circle cx="372" cy="258" r="7"/></g>
""", ground=False)

add('budget', '使えるお金の枠を項目に割りふるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g fill="{INK}"><rect x="-160" y="-110" width="120" height="16"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-160-50h320M-160 0h320M-160 50h320"/></g>
  <g class="teal o"><rect x="-160" y="-46" width="180" height="30"/><rect x="-160" y="4" width="120" height="30"/><rect x="-160" y="54" width="240" height="30"/></g>
  <g class="goldd o"><circle cx="150" cy="-100" r="26"/></g>
</g>
""", ground=True)

add('burst', '風船が勢いよくはじけるイラスト。', f"""
<g transform="translate(170 230)" opacity=".5">
  <circle r="70" class="coralp o"/>
  <path d="M0 70v60" fill="none" stroke="{MUTED}" stroke-width="3"/>
</g>
<g transform="translate(430 230)">
  <path d="M0-120l30 66 74-24-48 60 48 60-74-24-30 66-30-66-74 24 48-60-48-60 74 24z" class="coral o"/>
</g>
<g fill="{TONES['coral'][1]}"><circle cx="360" cy="120" r="10"/><circle cx="520" cy="140" r="9"/><circle cx="500" cy="330" r="8"/></g>
<path d="M280 230h50" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('calm', '波のない静かな水面のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#e4f2f8"/>
<path d="M0 240h600v160H0z" class="bluep"/>
<g fill="none" stroke="{TONES['blue'][2]}" stroke-width="3" opacity=".6"><path d="M60 300h480M60 340h480"/></g>
{sun(480,110,30)}
<g transform="translate(200 240)">
  <path d="M-70 0h140l-20 30h-100z" class="goldd o"/>
  <path d="M-6-90h12v90h-12z" class="ink"/>
</g>
<g opacity=".3" transform="translate(200 270) scale(1 -0.5)">
  <path d="M-70 0h140l-20 30h-100z" class="goldd o"/>
</g>
""", ground=False)

add('campus', '学舎と広場が並ぶ大学の構内のイラスト。', f"""
{building(180,300,1.0,'teal')}
{building(430,300,0.85,'blue')}
{tree(300,320,0.8)}
<g transform="translate(300 350)"><path d="M-240-10h480v14h-480z" fill="#e6dcc9"/></g>
{person(340,340,0.7,1,'coral','gold','walk','bob','smile')}
{person(250,340,0.7,-1,'violet','blue','walk','short','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('candidate', '名前が並び、選ばれる候補者のイラスト。', f"""
{person(160,346,1.15,1,'blue','blue','stand','short','smile')}
{person(300,346,1.15,1,'coral','gold','stand','bob','smile')}
{person(440,346,1.15,1,'teal','blue','stand','cap','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="100" y="180" width="400" height="180" rx="16"/></g>
<g transform="translate(300 120)">
  <path d="M-70-40h140v56h-140z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><rect x="-56" y="-26" width="20" height="20"/></g>
  <g fill="{MUTED}"><rect x="-26" y="-22" width="80" height="12"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('capitalist', '資本を投じて、利益を得るしくみのイラスト。', f"""
<g transform="translate(160 250)">
  <path d="M-60-40h120v70h-120z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <circle r="20" class="goldd o"/>
</g>
{building(330,300,0.8,'teal')}
<g transform="translate(490 250)">
  <path d="M-60-40h120v70h-120z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <circle cx="-24" r="20" class="goldd o"/><circle cx="24" r="20" class="goldd o"/>
</g>
<path d="M240 200h50M400 200h30" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('captain', '帽子をかぶって舵を取る長のイラスト。', f"""
{person(200,346,1.35,1,'blue','blue','reach','cap','neutral')}
<g transform="translate(200 226)"><path d="M-40-10h80v10h-80z" class="bluep o"/><g transform="translate(0 -22)"><path d="M0-14l6 12 14 2-10 10 2 14-12-8-12 8 2-14-10-10 14-2z" class="gold o"/></g></g>
<g transform="translate(430 260)">
  <circle r="76" fill="none" stroke="{INK}" stroke-width="14"/>
  <circle r="18" class="ink"/>
  <path d="M-60 0h120M0-60v120" fill="none" stroke="{INK}" stroke-width="10"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('capture', '網でとらえて、逃がさないイラスト。', f"""
<g transform="translate(360 240)">
  <path d="M-110 0a110 110 0 0 1 220 0z" fill="#e7f6fb" opacity=".7" stroke="{INK}" stroke-width="4"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">{''.join(f'<path d="M{-90+i*30}-70v70"/>' for i in range(7))}<path d="M-104-40h208M-70-66h140"/></g>
  <path d="M-110 0h220v14h-220z" class="ink"/>
  <g class="goldp o"><ellipse cy="-40" rx="34" ry="24"/></g>
</g>
<path d="M-6-80h12v90h-12z" class="ink" transform="translate(360 320)"/>
{person(150,346,1.05,1,'teal','blue','reach','short','neutral')}
<path d="M220 200h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('carefully', '手もとをよく見ながら、慎重に注ぐイラスト。', f"""
<g transform="translate(230 180) rotate(24)">
  <path d="M-50-50h100v90h-100z" fill="#e7f6fb" stroke="{INK}" stroke-width="3"/>
  <path d="M50-20q40 6 50 30" fill="none" stroke="{INK}" stroke-width="8"/>
</g>
<path d="M330 220q6 40 0 60" fill="none" stroke="{TONES['blue'][0]}" stroke-width="10" stroke-linecap="round"/>
<g transform="translate(330 320)">
  <path d="M-50-40h100l-10 80h-80z" fill="#f7fbfe" class="o"/>
  <path d="M-44 0h88l-6 40h-76z" class="bluep o"/>
</g>
<g transform="translate(480 190)">
  <ellipse rx="46" ry="30" fill="#fffdf6" class="o"/>
  <circle r="14" class="ink"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('casual', 'かたい服装と、くつろいだ普段着を比べたイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-70-80h140v90h-140z" class="bluep o"/>
  <path d="M-40 10h80v80h-80z" class="blue o"/>
  <path d="M-8-80h16v40h-16z" class="coral o"/>
</g>
<g transform="translate(430 250)">
  <path d="M-70-70h140v80h-140z" class="tealp o"/>
  <path d="M-60 10h120v80h-120z" fill="#cfd8e0" class="o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M480 130l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('category', '種類ごとに箱へ分けて入れるイラスト。', f"""
<g fill="none" stroke="{INK}" stroke-width="4"><rect x="90" y="200" width="130" height="130"/><rect x="240" y="200" width="130" height="130"/><rect x="390" y="200" width="130" height="130"/></g>
<g class="teal o"><circle cx="130" cy="240" r="20"/><circle cx="180" cy="290" r="20"/></g>
<g class="coral o"><rect x="260" y="220" width="40" height="40"/><rect x="310" y="270" width="40" height="40"/></g>
<g class="gold o"><path d="M430 260l30-40 30 40z"/><path d="M450 320l30-40 30 40z"/></g>
<path d="M60 350h480" class="a"/>
""", ground=True)

add('cause', 'こちらの出来事が、あちらの結果を引き起こすイラスト。', f"""
<g transform="translate(160 240)">{flame(160,240,1.1)}</g>
<g transform="translate(440 240)">
  <g class="muted" opacity=".9"><path d="M0-60q30-40 0-70M40-40q30-40 0-70"/></g>
  <path d="M-70 60h140v-40h-140z" fill="#b6bfc9" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M250 240h90" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('cautious', '足もとを確かめながら、用心して進むイラスト。', f"""
{person(200,320,1.15,1,'teal','blue','walk','short','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M260 340h120"/></g>
<g transform="translate(430 300)">
  <path d="M0-70l70 120h-140z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-6" y="-20" width="12" height="40"/><rect x="-6" y="30" width="12" height="12"/></g>
</g>
{drop(260,240,0.7)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('ceiling', '部屋の上をおおう天井を示したイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-140h440v280h-440z" fill="#fffdf6" class="o"/>
  <path d="M-220-140h440v50h-440z" fill="#dfe6ea" class="o"/>
  <path d="M-6-90h12v40h-12z" class="ink"/>
  <g class="goldp o"><path d="M-40-50h80l16 30h-112z"/></g>
</g>
{person(180,340,0.85,1,'teal','blue','up','short','neutral')}
<path d="M420 160v-40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('celebration', 'くす玉と拍手で祝うイラスト。', f"""
{person(180,346,1.15,1,'coral','gold','up','bob','smile')}
{person(420,346,1.15,1,'teal','blue','up','short','smile')}
<g transform="translate(300 150)">
  <path d="M-60-40h120v70h-120z" class="goldp o"/>
  <g class="corals" style="stroke-width:5"><path d="M-70 40l-30 30M70 40l30 30M0 40v40"/></g>
</g>
<g fill="{TONES['coral'][0]}"><circle cx="200" cy="200" r="8"/><circle cx="400" cy="220" r="7"/></g>
<g fill="{TONES['teal'][0]}"><circle cx="260" cy="240" r="7"/><circle cx="350" cy="180" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('cell', '顕微鏡で見た細胞のイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="140" class="tealp o"/>
  <circle r="140" fill="none" stroke="{TONES['teal'][2]}" stroke-width="5"/>
  <circle r="46" class="teal o"/>
  <circle r="18" class="teald o"/>
  <g class="teal o" opacity=".7"><ellipse cx="-80" cy="40" rx="24" ry="14" transform="rotate(-20 -80 40)"/><ellipse cx="70" cy="-60" rx="24" ry="14" transform="rotate(20 70 -60)"/></g>
</g>
""", ground=False)

add('ceremony', '壇上で式が行われる式典のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-200-40h400v40h-400z" class="coralp o"/>
  <path d="M-200 0h400v20h-400z" class="coral o"/>
</g>
<g transform="translate(300 190) scale(0.95)">{person(0,60,1.0,1,'blue','blue','give','short','neutral')}</g>
<g transform="translate(300 120)"><path d="M-60-40h120v50h-120z" class="paper"/></g>
{person(120,340,0.7,1,'teal','gold','stand','bob','smile')}
{person(480,340,0.7,-1,'violet','blue','stand','short','smile')}
<path d="M60 360h480" class="a"/>
""", ground=True)

add('certainly', 'はっきりうなずいて、たしかにと請け合うイラスト。', f"""
{person(220,346,1.25,1,'teal','blue','stand','short','smile')}
<g transform="translate(400 180)">
  <path d="M-70-50h140v70h-140z" fill="#fffdf6" class="o"/>
  <path d="M-40 20l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M-26-16l18 20 34-40"/></g>
</g>
<path d="M290 240q30 30 0 60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('challenging', '急な坂を登る、やりがいのあるイラスト。', f"""
<path d="M60 340L340 120h60v220z" class="green o"/>
<g transform="translate(250 240) rotate(-38)">{person(0,0,1.0,1,'coral','blue','walk','short','neutral')}</g>
<g transform="translate(380 90)"><path d="M-4-40h8v50h-8z" class="ink"/><path d="M4-38h50v30H4z" class="coral o"/></g>
<g class="corals" style="stroke-width:5"><path d="M180 190l-24-16M190 230h-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('champion', '一位の表彰台に立つ優勝者のイラスト。', f"""
<g transform="translate(300 330)">
  <path d="M-60-90h120v90h-120z" class="gold o"/>
  <path d="M-180-50h120v50h-120z" class="tealp o"/>
  <path d="M60-30h120v30H60z" class="coralp o"/>
</g>
<g transform="translate(300 180) scale(0.95)">{person(0,60,1.0,1,'coral','blue','up','short','smile')}</g>
<g transform="translate(300 100)"><path d="M0-30l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" class="gold o"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('channel', 'テレビのチャンネルを切り替えるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-140h360v250h-360z" fill="#dfe6ea" class="o"/>
  <path d="M-150-110h300v190h-300z" class="bluep o"/>
  <g fill="#fffdf6"><rect x="80" y="-90" width="50" height="40"/></g>
  <g fill="{INK}"><rect x="92" y="-80" width="26" height="20"/></g>
</g>
<g transform="translate(300 370)">
  <path d="M-60-14h120v28h-120z" fill="#41506a"/>
  <g fill="#f3e3ae"><circle cx="-30" r="7"/><circle cx="0" r="7"/><circle cx="30" r="7"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M420 300h50"/></g>
""", ground=True, arrow=True)

add('chapter', '本の中の一つの章を開くイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-130h400v260h-400z" class="violet o"/>
  <path d="M-180-110h360v220h-360z" fill="#fffdf6" class="o"/>
  <path d="M0-110v220" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-140" y="-80" width="80" height="16"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-140 {-40+i*30}h120"/>' for i in range(5))}{''.join(f'<path d="M20 {-80+i*30}h120"/>' for i in range(7))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('charming', '思わず引きつけられる、愛らしい笑顔のイラスト。', f"""
{face(260,200,95,'smile')}
<g fill="{TONES['coral'][1]}"><circle cx="200" cy="230" r="20"/><circle cx="320" cy="230" r="20"/></g>
<g class="golds" style="stroke-width:5"><path d="M390 140l26-20M400 190h30M390 240l26 20"/></g>
<g transform="translate(470 300)"><path d="M0 30c-30-24-42-34-42-52a22 22 0 0 1 42-12 22 22 0 0 1 42 12c0 18-12 28-42 52z" class="coral o"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('chest', '胸の位置を示したイラスト。', f"""
<g transform="translate(300 250)">
  <circle cy="-130" r="44" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-90 130q0-140 90-140t90 140z" class="teal o"/>
  <path d="M-84 30q-40 20-40 80" fill="none" stroke="{SKIN}" stroke-width="18" stroke-linecap="round"/>
  <path d="M84 30q40 20 40 80" fill="none" stroke="{SKIN}" stroke-width="18" stroke-linecap="round"/>
</g>
<circle cx="300" cy="220" r="54" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M440 220h-70" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('childhood', '小さいころの遊んだ日々を思い出すイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','think','short','smile')}
<g transform="translate(430 200)">
  <path d="M-130-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-166q-38-4-26-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(-30 0) scale(0.55)">{person(0,60,1.0,1,'coral','gold','up','bob','smile')}</g>
  <g transform="translate(60 10)"><circle r="24" class="goldp o"/><path d="M-24 0h48" fill="none" stroke="{TONES['gold'][2]}" stroke-width="3"/></g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="280" cy="300" r="12"/><circle cx="256" cy="324" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('chronic', '同じ痛みが長く続いているイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-120h440v240h-440z" fill="#f7fbfe" class="o"/>
  <path d="M-190 60h380" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M-190 0q40 30 80 0t80 0t80 0t80 0t60 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M100 380h400"/></g>
""", ground=False, arrow=True)

add('citizen', '国旗のもとに暮らす市民のイラスト。', f"""
<g transform="translate(300 150)">
  <path d="M-4-60h8v90h-8z" class="ink"/>
  <path d="M4-56h90v56H4z" class="tealp o"/>
</g>
{person(160,346,1.05,1,'coral','blue','stand','bob','smile')}
{person(300,346,1.05,1,'teal','gold','stand','short','smile')}
{person(440,346,1.05,1,'gold','blue','stand','cap','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('civic', '市役所の前に集まる市民のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-180 100h360v-140h-360z" fill="#f4ead2" class="o"/>
  <path d="M-200-40l200-90 200 90z" class="teal o"/>
  <g class="goldp o"><rect x="-140" y="0" width="50" height="100"/><rect x="-25" y="0" width="50" height="100"/><rect x="90" y="0" width="50" height="100"/></g>
</g>
{person(150,350,0.7,1,'coral','blue','stand','bob','smile')}
{person(450,350,0.7,-1,'teal','gold','stand','short','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('civil', '軍でなく、ふつうの市民の立場を示すイラスト。', f"""
{person(180,346,1.2,1,'teal','gold','stand','bob','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M110 180l20 20 34-40"/></g>
{person(430,346,1.2,1,'green','green','stand','cap','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M500 170l30 30M530 170l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('clause', '契約書の中の一つの条項を示したイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <g fill="{INK}"><rect x="-140" y="-110" width="120" height="14"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-140 {-60+i*36}h280"/>' for i in range(6))}</g>
  <path d="M-146-12h292v40h-292z" class="goldp o" opacity=".85"/>
</g>
<path d="M500 230h-40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('clearly', 'くもりが晴れて、はっきり見えるイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-90-90h180v180h-180z" fill="#dfe6ea" class="o"/>
  <g opacity=".35"><circle r="50" class="teal o"/></g>
</g>
<g transform="translate(430 230)">
  <path d="M-90-90h180v180h-180z" fill="#fffdf6" class="o"/>
  <circle r="50" class="teal o"/>
</g>
<path d="M290 230h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M480 360l20 20 34-40"/></g>
""", ground=True, arrow=True)

add('client', '相談に来た依頼人と、応じる担当者のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-120-20h240v26h-240z" class="goldd o"/>
  <path d="M-110 6h14v60h-14zM96 6h14v60H96z" class="goldd o"/>
</g>
{person(140,330,1.05,1,'coral','gold','reach','bob','smile')}
{person(460,330,1.05,-1,'blue','blue','reach','short','smile')}
<g transform="translate(300 250)"><path d="M-60-30h120v40h-120z" class="paper"/></g>
<circle cx="140" cy="300" r="80" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('coin', '手のひらの上の硬貨のイラスト。', f"""
<g transform="translate(240 200)">
  <circle r="80" class="goldd o"/>
  <circle r="62" fill="#e5b56b" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-26" y="-8" width="52" height="16"/></g>
</g>
<g transform="translate(410 240)">
  <ellipse rx="70" ry="20" class="goldd o"/>
  <ellipse cy="-14" rx="70" ry="20" class="goldd o"/>
  <ellipse cy="-28" rx="70" ry="20" class="goldd o"/>
</g>
{hand(240,320,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)
print(len(W), ' '.join(W)); print(sheet(W))
