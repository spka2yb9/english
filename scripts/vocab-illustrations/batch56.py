"""第56回: 比較・一貫・建設・犯罪など42語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('communication', '言葉が行き交って、意思が通じ合うイラスト。', f"""
{person(150,346,1.15,1,'teal','blue','stand','short','smile')}
{person(450,346,1.15,-1,'coral','gold','stand','bob','smile')}
<g fill="#fffdf6" stroke="{INK}" stroke-width="3">
  <path d="M210 120h130v60H210z"/><path d="M255 180l-14 26 34-26z"/>
  <path d="M260 220h130v60H260z"/><path d="M330 280l14 26-34-26z"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M350 150h40M250 250h-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('comparable', 'ほぼ同じ高さで、肩を並べる二つの棒のイラスト。', f"""
<path d="M60 340h480" class="a"/>
<rect x="150" y="140" width="110" height="200" class="teal o"/>
<rect x="340" y="150" width="110" height="190" class="coral o"/>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M120 140h360"/></g>
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M285 220q20-14 40 0M285 260q20-14 40 0"/></g>
""", ground=False)

add('comparison', '二つを並べて、どこが違うか見比べるイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-90-90h180v180h-180z" class="tealp o"/>
  <circle r="40" class="teal o"/>
</g>
<g transform="translate(430 230)">
  <path d="M-90-90h180v180h-180z" class="coralp o"/>
  <path d="M-40-40h80v80h-80z" class="coral o"/>
</g>
<path d="M300 130v200" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"/>
<g class="a" marker-end="url(#ar)"><path d="M270 360h-60M330 360h60"/></g>
""", ground=True, arrow=True)

add('compelling', '説得力のある話に、思わず引き込まれるイラスト。', f"""
{person(160,346,1.15,1,'blue','blue','point','short','neutral')}
<g transform="translate(320 180)">
  <path d="M-80-50h160v80h-160z" fill="#fffdf6" class="o"/>
  <path d="M-50 30l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-56" y="-26" width="112" height="14"/></g>
</g>
<g transform="translate(470 346) rotate(-10)">{person(0,0,1.15,-1,'coral','gold','reach','bob','smile')}</g>
<path d="M420 260h-60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('competent', '道具を確かに使いこなす、有能なイラスト。', f"""
{person(200,346,1.25,1,'blue','blue','reach','short','smile')}
<g transform="translate(400 250)">
  <path d="M-100-80h200v160h-200z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="10"><circle cx="-40" cy="-20" r="34"/><circle cx="40" cy="30" r="26"/></g>
  <g class="green o"><circle cx="70" cy="-50" r="12"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M120 180l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('competition', '同じ線をめざして競い合うイラスト。', f"""
{person(160,346,1.1,1,'coral','blue','walk','short','neutral')}
{person(280,346,1.1,1,'teal','gold','walk','cap','neutral')}
{person(400,346,1.1,1,'gold','blue','walk','bob','neutral')}
<g transform="translate(520 250)"><path d="M-6-100h12v200h-12z" class="ink"/><path d="M-70-100h64v50h-64z" fill="#fffdf6" stroke="{INK}" stroke-width="2"/>
<g fill="{INK}"><rect x="-70" y="-100" width="16" height="16"/><rect x="-38" y="-100" width="16" height="16"/><rect x="-54" y="-84" width="16" height="16"/><rect x="-22" y="-84" width="16" height="16"/></g></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('competitive', '値札を下げて他に負けじと張り合うイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-80-60h160v140h-160z" class="tealp o"/>
  <g transform="translate(0 -100) rotate(-10)"><path d="M-60-30h100l20 30-20 30h-100z" class="coral o"/><g fill="#fffdf6"><rect x="-40" y="-8" width="60" height="14"/></g></g>
</g>
<g transform="translate(430 240)">
  <path d="M-80-60h160v140h-160z" class="goldp o"/>
  <g transform="translate(0 -100) rotate(10)"><path d="M-60-30h100l20 30-20 30h-100z" class="coral o"/><g fill="#fffdf6"><rect x="-40" y="-8" width="44" height="14"/></g></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 240h50M330 280h-50"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('completely', 'すきまなく全部塗り終えたイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-90-90h180v180h-180z" fill="#fffdf6" class="o"/>
  <path d="M-90-90h180v110h-180z" class="teal o"/>
</g>
<g transform="translate(430 240)">
  <path d="M-90-90h180v180h-180z" class="teal o"/>
</g>
<path d="M290 240h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 370l20 20 34-40"/></g>
""", ground=True, arrow=True)

add('complex', '線が幾重にも入り組んだ、複雑なイラスト。', f"""
<g transform="translate(300 210)">
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5">
    <path d="M-200 0q60-120 120 0t120 0t120 0"/>
    <path d="M-200 60q60 120 120 0t120 0t120 0"/>
    <path d="M-160-120q80 60 40 140t60 120"/>
    <path d="M40-120q-80 60-40 140t-60 120"/>
    <path d="M160-120q60 80 0 160t40 120"/>
  </g>
  <g class="coral o"><circle cx="-80" cy="0" r="14"/><circle cx="40" cy="60" r="14"/><circle cx="160" cy="0" r="14"/></g>
</g>
""", ground=False)

add('compose', '部品を組み合わせて、ひとつを作り上げるイラスト。', f"""
<g transform="translate(160 250)">
  <g class="tealp o"><rect x="-60" y="-60" width="50" height="50"/><rect x="10" y="-60" width="50" height="50"/><rect x="-60" y="10" width="50" height="50"/><rect x="10" y="10" width="50" height="50"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-70-70h140v140h-140z" class="teal o"/>
  <g fill="none" stroke="#fffdf6" stroke-width="3"><path d="M0-70v140M-70 0h140"/></g>
</g>
<path d="M270 240h60" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('comprehensive', '必要な項目を全部そろえて網羅するイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-140h380v280h-380z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-100 {-100+i*40}h260"/>' for i in range(6))}</g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round">{''.join(f'<path d="M-150 {-106+i*40}l14 14 24-30"/>' for i in range(6))}</g>
</g>
""", ground=True)

add('compulsory', '全員がやらねばならない、義務の印がついたイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-130-110h260v220h-260z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-90-50h180M-90-10h180M-90 30h140"/></g>
  <g fill="{TONES['coral'][0]}"><path d="M-108-98h24v60h-24zM-108-26h24v24h-24z"/></g>
</g>
{person(150,346,0.9,1,'teal','blue','stand','short','neutral')}
{person(450,346,0.9,1,'coral','gold','stand','bob','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M200 320h60M400 320h-60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('concerned', '相手のことを気づかって、心配そうに見るイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','think','short','sad')}
{person(430,346,1.1,-1,'coral','gold','stand','bob','sad')}
<path d="M280 250h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9" marker-end="url(#ar)"/>
{drop(250,220,0.7)}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('confidence', '胸を張って、自信をもって立つイラスト。', f"""
{person(280,346,1.45,1,'blue','blue','stand','short','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="10" stroke-linecap="round"><path d="M420 170l22 22 38-44"/></g>
<g class="golds" style="stroke-width:5"><path d="M170 180l-26-20M180 220h-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('confusing', '案内板の矢印がばらばらで、分かりにくいイラスト。', f"""
<g transform="translate(320 210)">
  <path d="M-140-110h280v190h-280z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="6" marker-end="url(#ar)">
    <path d="M-100-70h80"/><path d="M100-30h-80"/><path d="M-40 10l60 50"/><path d="M60-70L-20-20"/>
  </g>
  <path d="M-14 80h28v90h-28z" class="ink"/>
</g>
{person(120,346,0.95,1,'teal','blue','think','short','flat')}
<g fill="{INK}" transform="translate(120 180)">
  <path d="M0 0q0-26 20-26t20 26q0 14-14 18v12h-10v-20q14-4 14-14t-8-8-8 12z"/><rect x="12" y="42" width="10" height="10"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('conscious', '自分の動きに気づいて、意識しているイラスト。', f"""
{person(200,346,1.25,1,'teal','blue','think','short','neutral')}
<g transform="translate(430 200)">
  <path d="M-120-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-156q-38-4-36-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 0) scale(0.5)">{person(0,60,1.0,1,'teal','blue','stand','short','neutral')}</g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="300" cy="290" r="12"/><circle cx="276" cy="314" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('consecutive', '同じ印が途切れず続いて並ぶイラスト。', f"""
<g class="teal o">{''.join(f'<rect x="{100+i*66}" y="200" width="52" height="120"/>' for i in range(7))}</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round">{''.join(f'<path d="M{112+i*66} 160l12 12 20-24"/>' for i in range(7))}</g>
<path d="M100 360h420" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('conservative', '新しい形をとらず、昔ながらの形を守るイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-80-70h160v140h-160z" fill="#f4ead2" stroke="{INK}" stroke-width="3"/>
  <path d="M-100-70l100-70 100 70z" class="coral o"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M60-150l20 20 34-40"/></g>
</g>
<g transform="translate(440 250)">
  <path d="M-70-90h140v160h-140z" class="tealp o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M50-140l30 30M80-140l-30 30"/></g>
</g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('considerable', 'ひと山とは言えないほど、かなりの量があるイラスト。', f"""
<g transform="translate(160 300)">
  <g class="tealp o"><circle r="24"/><circle cx="40" cy="10" r="20"/></g>
</g>
<g transform="translate(420 260)">
  <path d="M-140 80q20-160 140-160t140 160z" class="teal o"/>
</g>
<path d="M250 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('considerate', '相手に傘を差しかけて、思いやるイラスト。', f"""
<g class="muted" opacity=".9"><path d="M120 90v40M200 70v40M380 80v40M470 90v40"/></g>
{person(230,346,1.15,1,'teal','blue','up','short','smile')}
{person(360,346,1.15,-1,'coral','gold','stand','bob','smile')}
<g transform="translate(340 180)">
  <path d="M-110 0q0-70 110-70t110 70z" class="violetp o"/>
  <path d="M-4 0h8v90h-8z" class="ink"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M500 300l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('consistent', '同じ高さがそろって続いているイラスト。', f"""
<path d="M60 340h480" class="a"/>
<g class="teal o">{''.join(f'<rect x="{100+i*70}" y="180" width="56" height="160"/>' for i in range(6))}</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M80 180h460"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M120 120l20 20 34-40"/></g>
""", ground=False)

add('constant', '止まることなく水が落ち続けるイラスト。', f"""
<g transform="translate(260 130)">
  <path d="M-100-20h100v40h-100z" fill="#c9d3dc" class="o"/>
  <path d="M0-20h40v60H0z" fill="#c9d3dc" class="o"/>
</g>
{drop(280,220,1.0)}{drop(280,280,1.0)}{drop(280,330,1.0)}
<g class="a" marker-end="url(#ar)"><path d="M380 180v160"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('construction', '足場を組んで建物を建てているイラスト。', f"""
<g transform="translate(320 250)">
  <path d="M-140 90h280v-180h-280z" fill="#f4ead2" class="o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="6"><path d="M-160-100h320M-160-40h320M-160 20h320M-160 80h320M-160-100v180M-40-100v180M80-100v180M160-100v180"/></g>
</g>
<g transform="translate(140 250)">
  <path d="M-6-140h12v240h-12z" class="ink"/>
  <path d="M-6-140h120v10h-120z" class="ink"/>
  <path d="M100-130v40" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M80-90h40v30H80z" class="goldd o"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('contact', '電話で相手に連絡をとるイラスト。', f"""
{person(150,346,1.05,1,'teal','blue','reach','short','smile')}
<g transform="translate(210 240)">
  <path d="M-24-40h48v80h-48z" fill="#41506a"/>
</g>
{person(470,346,1.05,-1,'coral','gold','reach','bob','smile')}
<g transform="translate(410 240)"><path d="M-24-40h48v80h-48z" fill="#41506a"/></g>
<g class="corals" style="stroke-width:5"><path d="M250 200q26-20 50 0M350 200q-26-20-50 0"/></g>
<path d="M260 160q40-40 80 0" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('contemporary', '昔の建物と、いまの建物を並べたイラスト。', f"""
<g transform="translate(160 280)">
  <path d="M-90 60h180v-100h-180z" fill="#f4ead2" class="o"/>
  <path d="M-110-40l110-70 110 70z" class="coral o"/>
</g>
<g transform="translate(430 260)">
  <path d="M-90 80h180v-200h-180z" fill="#dfe6ea" class="o"/>
  <g fill="#cfe6f5" stroke="{INK}" stroke-width="2">{''.join(f'<rect x="{-70+c*50}" y="{-100+r*50}" width="40" height="36"/>' for r in range(3) for c in range(3))}</g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M480 130l20 20 34-40"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('contribute', '自分の分を出して、全体に加えるイラスト。', f"""
{person(140,346,1.05,1,'teal','blue','give','short','smile')}
<g transform="translate(400 270)">
  <path d="M-110-60h220v120h-220z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="tealp o"><rect x="-90" y="-10" width="60" height="60"/><rect x="-20" y="-10" width="60" height="60"/></g>
</g>
<g transform="translate(280 200)"><path d="M-30-30h60v60h-60z" class="teal o"/></g>
<path d="M320 190q60-30 90 20" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('conventional', 'みんなと同じ、型どおりのやり方を示すイラスト。', f"""
<g class="tealp o">{''.join(f'<rect x="{90+i*90}" y="200" width="70" height="120"/>' for i in range(4))}</g>
<g transform="translate(500 260)"><path d="M-35-60h70v120h-70z" class="tealp o"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M120 150l20 20 34-40"/></g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('convinced', '証拠を見て、そうだと確信するイラスト。', f"""
{person(180,346,1.2,1,'teal','blue','stand','short','smile')}
<g transform="translate(420 230)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-50h140M-70-10h140M-70 30h100"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="10" stroke-linecap="round"><path d="M-40 60l24 24 46-56"/></g>
</g>
<path d="M270 250h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M120 180l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('cooperative', '二人で息を合わせて荷を運ぶイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','carry','short','smile')}
{person(420,346,1.15,-1,'coral','gold','carry','bob','smile')}
<g transform="translate(300 240)"><path d="M-110-30h220v60h-220z" class="goldd o"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M290 140l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('correctly', '答えが正しく書けているイラスト。', f"""
<g transform="translate(290 220)">
  <path d="M-160-140h320v280h-320z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-120-80h240M-120-20h240M-120 40h240"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round">
    <path d="M-140-86l14 14 24-30"/><path d="M-140-26l14 14 24-30"/><path d="M-140 34l14 14 24-30"/>
  </g>
</g>
<g transform="translate(500 320) rotate(24)"><path d="M-10-80h20v110h-20z" class="teal o"/><path d="M-10 30h20l-10 24z" class="ink"/></g>
""", ground=True)

add('corresponding', '左の印と右の印が一つずつ対応するイラスト。', f"""
<g class="teal o"><circle cx="150" cy="150" r="26"/><rect x="124" y="204" width="52" height="52"/><path d="M150 290l30 50h-60z"/></g>
<g class="tealp o"><circle cx="450" cy="150" r="26"/><rect x="424" y="204" width="52" height="52"/><path d="M450 290l30 50h-60z"/></g>
<g class="a" marker-end="url(#ar)"><path d="M200 150h200M200 230h200M200 320h200"/></g>
""", ground=False, arrow=True)

add('corridor', '両側に扉が並ぶ細長い廊下のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-260-140h520v280h-520z" fill="#fffdf6" class="o"/>
  <path d="M-260-140L-80-40v180L-260 140z" fill="#e4e9ee" class="o"/>
  <path d="M260-140L80-40v180l180 40z" fill="#e4e9ee" class="o"/>
  <path d="M-80-40h160v180h-160z" fill="#eef3f7" class="o"/>
  <g class="goldd o"><path d="M-210-40h50v120h-50z"/><path d="M160-40h50v120h-50z"/></g>
</g>
<path d="M300 380v-40" class="a" marker-end="url(#ar)" transform="rotate(180 300 360)"/>
""", ground=False, arrow=True)

add('corrupt', '裏で金を渡して、決まりをゆがめるイラスト。', f"""
{person(160,346,1.1,1,'violet','blue','give','cap','flat')}
{person(440,346,1.1,-1,'blue','blue','reach','short','flat')}
<g transform="translate(300 280)">
  <path d="M-60-30h120v50h-120z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <circle r="16" class="goldd o"/>
</g>
<g transform="translate(300 160)">
  <path d="M-70-40h140v70h-140z" class="paper"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M-40-20l80 40M40-20l-80 40"/></g>
</g>
<path d="M240 300h120" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('costly', '小さな品に、高い値札がついているイラスト。', f"""
<g transform="translate(200 280)"><path d="M-40-40h80v80h-80z" class="tealp o"/></g>
<g transform="translate(420 200) rotate(-10)">
  <path d="M-110-70h180l30 70-30 70h-180z" class="coral o"/>
  <circle cx="60" r="10" fill="#fffdf6"/>
  <g fill="#fffdf6"><rect x="-90" y="-26" width="130" height="20"/><rect x="-90" y="6" width="100" height="16"/></g>
</g>
{drop(230,180,0.7)}
<path d="M60 346h480" class="a"/>
""", ground=True)

add('costume', '劇のための衣装のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-120-100h240v70h-240z" class="violetp o"/>
  <path d="M-100-30h200l-20 190h-160z" class="violet o"/>
  <path d="M-120-100l-40 60 40 30M120-100l40 60-40 30" fill="none" stroke="{TONES['violet'][2]}" stroke-width="10"/>
  <g class="gold o"><circle cy="-60" r="14"/></g>
</g>
<g transform="translate(300 90)"><path d="M-50 20l-8-50 24 20 34-40 34 40 24-20-8 50z" class="gold o"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('cotton', 'ふわふわした綿花のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M0 120V20" fill="none" stroke="{TONES['green'][2]}" stroke-width="7"/>
  <g fill="#fffdf6" stroke="{MUTED}" stroke-width="2">
    <circle cx="-50" cy="-20" r="40"/><circle cx="50" cy="-20" r="40"/><circle cy="-60" r="44"/><circle cy="10" r="38"/>
  </g>
  <g class="green o"><ellipse cx="-60" cy="60" rx="34" ry="16" transform="rotate(-20 -60 60)"/><ellipse cx="60" cy="70" rx="34" ry="16" transform="rotate(20 60 70)"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('countless', '数えきれないほどの点が散らばるイラスト。', f"""
<g class="teal o">
  {''.join(f'<circle cx="{80+((i*67)%460)}" cy="{100+((i*113)%240)}" r="9"/>' for i in range(90))}
</g>
<g fill="{INK}" transform="translate(500 350)">
  <path d="M0 0q0-26 20-26t20 26q0 14-14 18v12h-10v-20q14-4 14-14t-8-8-8 12z"/><rect x="12" y="42" width="10" height="10"/>
</g>
""", ground=False)

add('countryside', '畑と農家が広がる田園のイラスト。', f"""
{sun(500,90,30)}
<g class="green o" opacity=".85"><path d="M0 320q150-60 300-30t300-20v130H0z"/></g>
<g transform="translate(180 280)">
  <path d="M-70 50h140V-10h-140z" fill="#f4ead2" class="o"/>
  <path d="M-90-10l90-60 90 60z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['green'][2]}" stroke-width="4" opacity=".8"><path d="M300 350q60-20 120 0M320 380q60-20 120 0"/></g>
{tree(470,330,0.8)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('courageous', '恐ろしいものの前に、勇気を出して立つイラスト。', f"""
<g transform="translate(450 250)">
  <path d="M-90 110q-20-170 90-170t90 170z" fill="#41506a"/>
  <g fill="{TONES['coral'][0]}"><path d="M-40-40l30 20-30 20zM40-40l-30 20 30 20z"/></g>
</g>
{person(180,346,1.25,1,'coral','blue','stand','short','neutral')}
<g transform="translate(240 250)">
  <path d="M0-50q34 14 34 44 0 36-34 50-34-14-34-50 0-30 34-44z" fill="#8b98a6" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M290 200h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('credible', '裏づけの印がそろって、信頼できるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-140-130h280v260h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-100-70h200M-100-20h200M-100 30h160"/></g>
  <g transform="translate(60 80)">
    <circle r="46" fill="none" stroke="{TONES['green'][0]}" stroke-width="7"/>
    <path d="M-22 0l16 18 30-36" fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"/>
  </g>
  <g transform="translate(-100 -110)"><path d="M0-20l8 16 18 2-13 13 3 18-16-9-16 9 3-18-13-13 18-2z" class="gold o"/></g>
</g>
""", ground=True)

add('crime', '禁じられたことをして、法を破るイラスト。', f"""
{person(180,346,1.15,1,'violet','violet','carry','cap','flat')}
<g transform="translate(240 250)"><path d="M-40-30h80v60h-80z" class="goldd o"/></g>
<g transform="translate(430 220)">
  <path d="M-100-90h200v180h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-50h140M-70-10h140"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M-40 30l70 40M30 30l-70 40"/></g>
</g>
<path d="M320 250h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('criminal', '罪を犯して捕らえられた人のイラスト。', f"""
<g transform="translate(320 230)">
  <path d="M-150-140h300v280h-300z" fill="#e4e9ee" class="o"/>
  <g fill="{INK}">{''.join(f'<rect x="{-130+i*44}" y="-120" width="14" height="240"/>' for i in range(7))}</g>
</g>
<g transform="translate(320 250) scale(0.85)">{person(0,60,1.0,1,'violet','violet','stand','cap','sad')}</g>
<path d="M60 386h480" class="a"/>
""", ground=True)
print(len(W), ' '.join(W)); print(sheet(W))
