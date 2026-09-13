"""第48回: 急ぐ・探す・驚く・似るなど39語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('round', '柱のまわりをぐるりと一周するイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-24-90h48v180h-48z" fill="#c9d3dc" class="o"/>
  <ellipse cy="110" rx="170" ry="60" fill="none" stroke="{TONES['teal'][0]}" stroke-width="8" stroke-dasharray="18 14"/>
</g>
{person(140,330,0.85,1,'coral','blue','walk','short','neutral')}
<path d="M430 380a170 60 0 0 0 60-30" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('run', '蛇口から水が流れ出るイラスト。', f"""
<g transform="translate(240 160)">
  <path d="M-100-20h100v40h-100z" fill="#c9d3dc" class="o"/>
  <path d="M0-20h40v70H0z" fill="#c9d3dc" class="o"/>
  <path d="M-40-40h30v20h-30z" class="teal o"/>
</g>
<path d="M260 220q6 80 0 120" fill="none" stroke="{TONES['blue'][0]}" stroke-width="22" stroke-linecap="round"/>
<g transform="translate(320 330)">
  <path d="M-140 40h280l-20-60h-240z" fill="#dfe6ea" class="o"/>
  <path d="M-100-20h200v10h-200z" class="bluep o"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('rush', '時計を気にして、あわてて駆け出すイラスト。', f"""
<g transform="translate(280 346) rotate(-14)">{person(0,0,1.3,1,'coral','blue','walk','short','surprised')}</g>
<g class="muted"><path d="M170 200h-90M160 250h-90M180 300h-90"/></g>
<g transform="translate(470 150)">
  <circle r="54" fill="#fffdf6" class="o"/>
  <path d="M0-34v34l26 14" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('sacrifice', '自分の持ち分を差し出して、相手のために手放すイラスト。', f"""
{person(150,346,1.1,1,'teal','blue','give','short','neutral')}
<g transform="translate(310 250)">
  <path d="M-50-40h100v80h-100z" class="gold o"/>
</g>
{person(470,346,1.1,-1,'coral','gold','reach','bob','smile')}
<path d="M240 220h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(150 240)" opacity=".35"><path d="M-40-30h80v60h-80z" class="muted"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('sailing', '帆を張ったヨットで海をすべるイラスト。', f"""
<path d="M0 300h600v100H0z" class="bluep"/>
<g transform="translate(300 270)">
  <path d="M-120 30h240l-40 40h-160z" fill="#fffdf6" class="o"/>
  <path d="M-6-160h12v190h-12z" class="ink"/>
  <path d="M6-150l90 170H6z" class="coralp o"/>
  <path d="M-6-140L-80 20h74z" fill="#fffdf6" class="o"/>
</g>
<g class="muted"><path d="M60 340q40-20 80 0M460 350q40-20 80 0"/></g>
{sun(510,80,28)}
""", ground=False)

add('salary', '封筒に入った月々の給料を受け取るイラスト。', f"""
{person(160,346,1.05,1,'blue','blue','give','bob','smile')}
<g transform="translate(320 240)">
  <path d="M-80-50h160v100h-160z" class="paper"/>
  <path d="M-80-50l80 60 80-60" fill="none" stroke="{INK}" stroke-width="3"/>
  <g class="green o"><rect x="-40" y="-30" width="80" height="34"/></g>
</g>
{person(480,346,1.05,-1,'teal','gold','reach','short','smile')}
<path d="M240 300h120" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('sale', '値札に安売りの札がついた店先のイラスト。', f"""
<g transform="translate(230 260)">
  {box(0,0,180,130,30,'teal')}
</g>
<g transform="translate(440 200) rotate(-12)">
  <path d="M-90-60h150l30 60-30 60h-150z" class="coral o"/>
  <circle cx="50" r="10" fill="#fffdf6"/>
  <g fill="#fffdf6"><rect x="-70" y="-20" width="100" height="18"/><rect x="-70" y="10" width="60" height="12"/></g>
</g>
<g class="corals" style="stroke-width:5"><path d="M170 130l-20-24M250 110v-26"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('satisfy', 'ほしかったものが手に入り、満ち足りるイラスト。', f"""
{person(200,346,1.25,1,'teal','gold','carry','bob','smile')}
<g transform="translate(200 250)">
  <path d="M-50-30h100v60h-100z" class="gold o"/>
</g>
<g transform="translate(430 210)">
  <path d="M-90 60V-60h180v120z" fill="#f7fbfe" class="o"/>
  <path d="M-90 60V0h180v60z" class="teal o"/>
  <path d="M-90 60V-60h180v120z" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M420 340l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('sauce', '料理にとろりとソースをかけるイラスト。', f"""
<g transform="translate(220 180) rotate(30)">
  <path d="M-50-70h100l-10 130h-80z" fill="#e7f6fb" stroke="{INK}" stroke-width="3"/>
  <path d="M-44-20h88l-6 80h-76z" class="coralp o"/>
  <path d="M-24-84h48v14h-48z" class="ink"/>
</g>
<path d="M300 230q10 40 6 60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="12" stroke-linecap="round"/>
<g transform="translate(340 320)">
  <ellipse rx="130" ry="34" fill="#fffdf6" class="o"/>
  <ellipse cy="-10" rx="90" ry="24" class="goldp o"/>
  <path d="M-40-24q40-16 80 0 0 20-40 20t-40-20z" class="coral o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('scare', '大きな影で相手をおどかすイラスト。', f"""
<g transform="translate(180 240)">
  <path d="M-90 100q-20-130 90-130t90 130z" fill="#41506a" opacity=".8"/>
  <g fill="#fffdf6"><circle cx="-24" cy="-40" r="10"/><circle cx="24" cy="-40" r="10"/></g>
</g>
{person(450,346,1.15,-1,'coral','gold','up','bob','surprised')}
<path d="M290 220h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('scared', '身をすくめて、おびえている人のイラスト。', f"""
{person(300,346,1.35,1,'coral','blue','up','bob','surprised')}
<g class="corals" style="stroke-width:5"><path d="M180 200q-24 16-24 44M420 200q24 16 24 44"/></g>
{drop(370,240,0.8)}{drop(240,250,0.7)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('scientific', '実験器具とデータで、科学のやり方を示したイラスト。', f"""
<g transform="translate(180 260)">
  <path d="M-16-90h32v40l50 100h-132l50-100z" fill="#e7f6fb" stroke="{INK}" stroke-width="3"/>
  <path d="M-56 20h112l24 30h-160z" class="tealp o"/>
</g>
<g transform="translate(430 220)">
  <path d="M-110-90h220v180h-220z" fill="#f7fbfe" class="o"/>
  <path d="M-80 50l50-60 40 30 50-70" fill="none" stroke="{TONES['teal'][0]}" stroke-width="5"/>
  <g fill="{INK}"><circle cx="-80" cy="50" r="6"/><circle cx="-30" cy="-10" r="6"/><circle cx="10" cy="20" r="6"/><circle cx="60" cy="-50" r="6"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('scream', '口を大きく開けて、悲鳴を上げるイラスト。', f"""
{face(240,200,90,'flat')}
<g transform="translate(240 240)"><ellipse rx="30" ry="38" fill="#8b4a3e"/></g>
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M186 150l38 18M294 150l-38 18"/></g>
<g class="corals" opacity=".9" style="stroke-width:6"><path d="M360 160q30 40 30 80t-30 80M410 130q46 56 46 110t-46 110"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('screw', 'ねじ山のあるねじと、それを回すドライバーのイラスト。', f"""
<g transform="translate(230 230)">
  <path d="M-50-100h100v30h-100z" fill="#c9d3dc" class="o"/>
  <path d="M-16-70h32v170l-16 30-16-30z" fill="#c9d3dc" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">{''.join(f'<path d="M-16 {-40+i*24}h32"/>' for i in range(6))}</g>
  <path d="M-30-90h60" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g transform="translate(430 220) rotate(20)">
  <path d="M-16-120h32v130h-32z" class="coral o"/>
  <path d="M-8 10h16v90h-16z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('search', '虫めがねで、あちこち探し回るイラスト。', f"""
{person(150,346,1.05,1,'teal','blue','reach','short','neutral')}
<g transform="translate(330 210) rotate(30)">
  <circle r="66" fill="#e7f6fb" opacity=".85" stroke="{INK}" stroke-width="8"/>
  <path d="M0 66v70" fill="none" stroke="{INK}" stroke-width="16"/>
</g>
<g class="muted"><path d="M430 150q40 30 20 70M450 260q30 30 10 60"/></g>
<g class="tealp o"><circle cx="480" cy="200" r="18"/><circle cx="520" cy="300" r="14"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('season', '四つの季節の景色を並べたイラスト。', f"""
<g transform="translate(160 150)">
  <path d="M-100-70h200v140h-200z" fill="#fdeaf0" class="o"/>
  {tree(0,50,0.6)}
</g>
<g transform="translate(430 150)">
  <path d="M-100-70h200v140h-200z" fill="#e6f7ec" class="o"/>
  {sun(0,-20,22)}
</g>
<g transform="translate(160 320)">
  <path d="M-100-70h200v140h-200z" fill="#fdf0d8" class="o"/>
  <g class="goldd o"><ellipse cx="-30" cy="10" rx="24" ry="14" transform="rotate(-20 -30 10)"/><ellipse cx="30" cy="-20" rx="24" ry="14" transform="rotate(20 30 -20)"/></g>
</g>
<g transform="translate(430 320)">
  <path d="M-100-70h200v140h-200z" fill="#eaf3fb" class="o"/>
  <g fill="#fffdf6" stroke="{MUTED}" stroke-width="2"><circle cx="-30" cy="-20" r="12"/><circle cx="20" cy="20" r="14"/><circle cx="50" cy="-30" r="10"/></g>
</g>
""", ground=False)

add('secondary', '主なものの後ろにある、二番目のものを示したイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-100-110h200v220h-200z" class="teal o"/>
  <g fill="#fffdf6"><rect x="-14" y="-40" width="28" height="80"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-70-80h140v160h-140z" class="tealp o"/>
  <g fill="{TONES['teal'][2]}"><rect x="-30" y="-30" width="20" height="60"/><rect x="10" y="-30" width="20" height="60"/></g>
</g>
<path d="M300 230h60" class="a" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('secret', '口もとに指を当てて、ないしょにするイラスト。', f"""
{face(280,200,95,'flat')}
<g transform="translate(280 250)">
  <path d="M-10 0h20v-70h-20z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5" transform="rotate(0)"/>
  <path d="M-30 0q30 20 60 0" fill="none" stroke="{SKINL}" stroke-width="2"/>
</g>
<g transform="translate(450 150)">
  <path d="M-70-50h140v80h-140z" fill="#fffdf6" class="o"/>
  <path d="M-40 30l-14 34 44-34z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{MUTED}"><circle cx="-30" cy="-10" r="8"/><circle cx="0" cy="-10" r="8"/><circle cx="30" cy="-10" r="8"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('secretary', '書類と電話で、上役の仕事を支える秘書のイラスト。', f"""
<g transform="translate(330 300)">
  <path d="M-160-30h320v30h-320z" class="goldd o"/>
  <path d="M-150 0h14v60h-14zM136 0h14v60h-14z" class="goldd o"/>
</g>
<g transform="translate(240 250)">
  <path d="M-60-30h120v40h-120z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-40-14h80M-40 0h60"/></g>
</g>
<g transform="translate(420 250)">
  <path d="M-40 10h80v-20h-80z" class="ink"/>
  <path d="M-40-10q40-40 80 0" fill="none" stroke="{INK}" stroke-width="8"/>
</g>
{person(140,330,1.0,1,'blue','blue','reach','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('seek', '灯りをかかげて、求めるものを探し求めるイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#33445c"/>
{person(180,340,1.15,1,'teal','blue','up','short','neutral')}
<g transform="translate(230 170)">
  <circle r="30" fill="#f7e6bd"/>
  <g opacity=".35" fill="#f7e6bd"><path d="M0-30L200 60 200-100z"/></g>
</g>
<g transform="translate(470 250)"><path d="M0-40l14 28 30 4-22 21 6 30-28-15-28 15 6-30-22-21 30-4z" class="gold o"/></g>
<path d="M300 250h90" fill="none" stroke="#f7e6bd" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('select', '並んだものから一つを選び取るイラスト。', f"""
<g class="tealp o"><rect x="110" y="230" width="90" height="90"/><rect x="310" y="230" width="90" height="90"/><rect x="420" y="230" width="90" height="90"/></g>
<g transform="translate(255 190)"><path d="M-45-40h90v90h-90z" class="coral o"/></g>
{hand(255,120,1)}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M480 170l18 18 30-36"/></g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('serious', 'まじめな顔で、重い話を受け止めるイラスト。', f"""
{face(230,200,95,'flat')}
<g fill="none" stroke="{INK}" stroke-width="7"><path d="M180 150l40 10M280 150l-40 10"/></g>
<g transform="translate(440 230)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-50h120M-60-20h120M-60 10h90"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M-40 50h100"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('several', 'いくつかの数だけ並んだ丸のイラスト。', f"""
<g class="teal o"><circle cx="150" cy="200" r="30"/><circle cx="240" cy="200" r="30"/><circle cx="330" cy="200" r="30"/><circle cx="420" cy="200" r="30"/></g>
<g class="muted"><path d="M480 200h60"/></g>
<g class="a" marker-end="url(#ar)"><path d="M150 290h270M420 290H150"/></g>
""", ground=False, arrow=True)

add('sharp', 'とがってよく切れる刃のイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-160-20h240l60 20-60 20h-240z" fill="#dbe3ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-160-20h-60v40h60z" class="goldd o"/>
  <path d="M40-14h100l40 14-40 14H40z" fill="#f7fbfe"/>
</g>
<g class="golds" style="stroke-width:4"><path d="M420 180l24-20M440 210h26"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('shatter', 'ガラスが粉々に砕けるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-160-130h320v260h-320z" fill="#e7f6fb" opacity=".5" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{INK}" stroke-width="3">
    <path d="M0 0L-160-130M0 0L-40-130M0 0L90-130M0 0L160-60M0 0L160 90M0 0L60 130M0 0L-90 130M0 0L-160 40"/>
  </g>
</g>
<g fill="#cfe6f2" stroke="{INK}" stroke-width="2">
  <path d="M470 120l40 20-30 30z"/><path d="M100 100l30 26-34 14z"/><path d="M520 300l34 16-30 24z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('shed', '木が葉を落とすイラスト。', f"""
{tree(220,300,1.5)}
<g class="green o" opacity=".9">
  <ellipse cx="360" cy="200" rx="20" ry="11" transform="rotate(20 360 200)"/>
  <ellipse cx="400" cy="270" rx="20" ry="11" transform="rotate(-25 400 270)"/>
  <ellipse cx="350" cy="320" rx="20" ry="11" transform="rotate(40 350 320)"/>
  <ellipse cx="430" cy="340" rx="20" ry="11" transform="rotate(-10 430 340)"/>
</g>
<path d="M370 160q40 90 20 170" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 9" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('sheet', '一枚の紙を取り出したイラスト。', f"""
<g transform="translate(330 250)" opacity=".5">
  <path d="M-130-100h260v200h-260z" class="paper"/>
</g>
<g transform="translate(280 220) rotate(-6)">
  <path d="M-130-110h260v220h-260z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-100 {-70+i*36}h200"/>' for i in range(5))}</g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 130v-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('shiny', '表面がつるつるに光っているイラスト。', f"""
<g transform="translate(300 240)">
  <circle r="110" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <path d="M-70-60q40-40 90-30-50 10-70 60z" fill="#ffffff" opacity=".9"/>
  <circle cx="50" cy="50" r="18" fill="#ffffff" opacity=".6"/>
</g>
<g class="golds" style="stroke-width:5"><path d="M160 110l-26-24M440 110l26-24M300 100V70"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('shocked', '目を見開いて、ぎょっと驚くイラスト。', f"""
{face(280,200,95,'flat')}
<g fill="#fffdf6" stroke="{INK}" stroke-width="3"><circle cx="242" cy="185" r="20"/><circle cx="318" cy="185" r="20"/></g>
<g fill="{INK}"><circle cx="242" cy="185" r="9"/><circle cx="318" cy="185" r="9"/></g>
<g transform="translate(280 250)"><ellipse rx="22" ry="26" fill="#8b4a3e"/></g>
<g class="corals" style="stroke-width:6"><path d="M400 130l30-24M420 180h34M400 230l30 24"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('shoot', '的をねらって矢を放つイラスト。', f"""
{person(150,346,1.1,1,'teal','blue','reach','short','neutral')}
<path d="M220 220h180" fill="none" stroke="{INK}" stroke-width="5"/>
<path d="M400 220l-24-12v24z" fill="{INK}"/>
<g transform="translate(470 220)">
  <circle r="70" fill="#fffdf6" class="o"/>
  <circle r="46" class="coralp o"/>
  <circle r="20" class="coral o"/>
</g>
<path d="M240 160h120" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('shoulder', '腕と首のつけ根にある肩を示したイラスト。', f"""
<g transform="translate(300 250)">
  <circle cy="-110" r="46" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-90 130q0-130 90-130t90 130z" class="teal o"/>
  <path d="M-84 20q-40 20-40 70" fill="none" stroke="{SKIN}" stroke-width="18" stroke-linecap="round"/>
  <path d="M84 20q40 20 40 70" fill="none" stroke="{SKIN}" stroke-width="18" stroke-linecap="round"/>
</g>
<circle cx="216" cy="270" r="46" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M130 270h40" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('shrug', '肩を上げて、さあねと示すイラスト。', f"""
{person(280,346,1.35,1,'teal','blue','up','short','flat')}
<g class="a" marker-end="url(#ar)"><path d="M170 210v-30M390 210v-30"/></g>
<g fill="{INK}" transform="translate(470 160)">
  <path d="M0 0q0-30 22-30t22 30q0 16-18 20v16h-10v-24q16-4 16-16t-10-12-12 16z"/>
  <rect x="12" y="48" width="12" height="12"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('sigh', '肩を落として、ふうっとため息をつくイラスト。', f"""
{person(220,346,1.3,1,'teal','blue','stand','short','sad')}
<g class="muted"><path d="M300 220q40-16 70 0t70 0"/></g>
<g class="muted" opacity=".7"><path d="M300 260q40-16 70 0t70 0"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('silent', '口を閉じて、音のない静けさを示したイラスト。', f"""
{face(280,200,95,'smile')}
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M250 250h60"/></g>
<g transform="translate(450 200)">
  <path d="M-50-50h60l50-40v180l-50-40h-60z" class="ink"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M40-40l60 60M100-40l-60 60"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('silly', 'つじつまの合わないことをして、間の抜けているイラスト。', f"""
{person(230,346,1.25,1,'gold','blue','up','short','smile')}
<g transform="translate(230 190)">
  <path d="M-40-60h80v34h-80z" class="tealp o"/>
  <path d="M-56-26h112v10h-112z" class="teal o"/>
</g>
<g transform="translate(440 220)">
  <path d="M-70-60h140v100h-140z" fill="#fffdf6" class="o"/>
  <path d="M-40 40l-14 34 44-34z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><path d="M-14-30q0-24 20-24t20 24q0 14-14 18v12h-12v-18q12-4 12-14t-8-8-8 10z"/><rect x="0" y="16" width="10" height="10"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('similar', 'よく似た形を並べて、同じようだと示すイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-80 80q0-160 80-160t80 160z" class="teal o"/>
</g>
<g transform="translate(430 230)">
  <path d="M-76 80q0-150 76-150t76 150z" class="tealp o"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M290 200q20-14 40 0M290 250q20-14 40 0"/></g>
<path d="M60 336h480" class="a"/>
""", ground=True)

add('simulate', '本物そっくりの模型で、動きをまねて試すイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-90-60h180v120h-180z" class="tealp o"/>
  <path d="M-60-20h120v60h-120z" fill="#e8f4fb" class="o"/>
  <circle cx="-50" cy="50" r="22" class="ink"/><circle cx="50" cy="50" r="22" class="ink"/>
</g>
<g transform="translate(440 230)">
  <path d="M-110-110h220v220h-220z" fill="#f7fbfe" class="o"/>
  <g opacity=".75">
    <path d="M-70-40h140v90h-140z" class="tealp o"/>
    <path d="M-46-10h92v46h-92z" fill="#e8f4fb" class="o"/>
    <circle cx="-40" cy="40" r="16" class="ink"/><circle cx="40" cy="40" r="16" class="ink"/>
  </g>
  <g class="muted"><path d="M-90 80h180"/></g>
</g>
<path d="M290 230h40" class="a" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('singing', '口を開いて歌い、音符が飛び出すイラスト。', f"""
{person(220,346,1.3,1,'coral','gold','up','bob','smile')}
<g fill="{INK}">
  <ellipse cx="380" cy="200" rx="18" ry="13" transform="rotate(-18 380 200)"/><rect x="392" y="150" width="6" height="46"/>
  <ellipse cx="460" cy="150" rx="18" ry="13" transform="rotate(-18 460 150)"/><rect x="472" y="100" width="6" height="46"/>
  <ellipse cx="450" cy="260" rx="18" ry="13" transform="rotate(-18 450 260)"/><rect x="462" y="210" width="6" height="46"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('side', '箱の一つの面だけを示したイラスト。', f"""
<g transform="translate(280 240)">
  {box(0,0,200,150,40,'teal')}
</g>
<g transform="translate(280 240)"><path d="M-100-75h200v150h-200z" class="coral o" opacity=".85"/></g>
<path d="M470 300h-60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
