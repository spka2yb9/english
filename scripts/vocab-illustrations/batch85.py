"""第85回: j〜l の名詞を中心に45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'

add('journalism', '取材して世に伝える報道のイラスト。', f"""
{person(160,352,1.15,1,'violet','blue','give','cap','neutral')}
<g transform="translate(250 250)">
  <path d="M-16-30h32v50h-32z" class="ink"/>
  <circle cy="-34" r="20" fill="{MUTED}" class="o"/>
</g>
<g transform="translate(430 220)">
  <path d="M-130-110h260v220h-260z" class="paper"/>
  <path d="M-100-84h200v34h-200z" class="ink"/>
  <path d="M-100-34h90v70h-90z" class="tealp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">
    <path d="M10-30h90M10-6h90M10 18h70M-100 56h200M-100 80h200"/>
  </g>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('joy', '思わず飛び上がるほどの喜びのイラスト。', f"""
{person(300,340,1.4,1,'coral','blue','up','short','smile')}
<g class="golds" stroke-width="5">
  <path d="M150 150l-24-22M450 150l24-22M300 90v-26M110 250H84M490 250h26"/>
</g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2">
  <path d="M180 250l10 22 24 3-17 17 4 24-21-12-21 12 4-24-17-17 24-3z"/>
  <path d="M420 250l10 22 24 3-17 17 4 24-21-12-21 12 4-24-17-17 24-3z"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('judgement', '二つを見比べてどちらかを選び取る判断のイラスト。', f"""
{person(300,352,1.2,1,'teal','blue','think','short','neutral')}
<g transform="translate(140 190)">
  <path d="M-70-60h140v120h-140z" class="tealp o"/>
</g>
<g transform="translate(470 190)">
  <path d="M-70-60h140v120h-140z" class="coralp o"/>
</g>
{ck(470,300,1)}
{xx(140,300,0.9,MUTED)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M250 240l-40-20M350 240l40-20"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('judgment', '法廷で下される判決のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-120-20h240v30h-240z" class="goldd o"/>
  <path d="M-90 10h180v40h-180z" class="gold o"/>
</g>
<g transform="translate(300 170) rotate(-24)">
  <path d="M-90-18h60v36h-60z" class="goldd o"/>
  <path d="M-30-8h130v16H-30z" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M170 120l-14-24M230 100v-26"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('junction', '道が交わり分かれる分岐点のイラスト。', f"""
<path d="M240 400V180h120v220z" fill="#dfe6ea" class="o"/>
<path d="M0 130h600v100H0z" fill="#dfe6ea" class="o"/>
<g fill="none" stroke="#fffdf6" stroke-width="5" stroke-dasharray="24 20"><path d="M0 180h600M300 400V180"/></g>
<g transform="translate(470 260)">
  <path d="M-6 90V-30" class="a"/>
  <path d="M-6-30h80l20 20-20 20H-6z" class="gold o"/>
  <path d="M-6 10h-80l-20 20 20 20h80z" class="goldp o"/>
</g>
""", ground=False)

add('jury', '席に並んで判断する陪審員団のイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-260-40h520v70h-520z" class="goldd o"/>
  <path d="M-260-40h520v14h-520z" class="gold o"/>
</g>
{sit(140,300,0.8,1,'teal','blue','short','neutral')}
{sit(230,300,0.8,1,'coral','blue','bob','neutral')}
{sit(320,300,0.8,1,'gold','violet','short','neutral')}
{sit(410,300,0.8,1,'green','blue','bun','neutral')}
{sit(500,300,0.8,1,'violet','gold','cap','neutral')}
<g transform="translate(300 120)">
  <path d="M-70-60h140v90h-140z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-40-34h80M-40-10h80M-40 14h50"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('kidney', '背中側にある二つの腎臓のイラスト。', f"""
<g transform="translate(300 210)">
  <circle cx="0" cy="-140" r="40" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-120 150v-110q0-90 120-90t120 90v110z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-60-30q-40 0-40 46t40 56q30 0 30-30t-14-36 14-16-30-20z" class="coral o"/>
  <path d="M60-30q40 0 40 46t-40 56q-30 0-30-30t14-36-14-16 30-20z" class="coral o"/>
  <path d="M-30 40q30 20 60 0" fill="none" stroke="{TONES['coral'][2]}" stroke-width="5"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('kingdom', '王の治める国の城のイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-160 0v-140h320V0z" fill="#fffdf6" class="o"/>
  <path d="M-160-140h40v-30h30v30h30v-30h30v30h140v-30h30v30h30v-30h30v30h-40" class="teal o"/>
  <path d="M-40-70h80v70h-80z" class="teald o"/>
  <path d="M-100-110h40v40h-40zM60-110h40v40H60z" class="tealp o"/>
</g>
<path d="M300 180v-60" class="a"/>
<g transform="translate(300 110)">
  <path d="M-50 10l-10-50 30 20 30-40 30 40 30-20-10 50z" class="gold o"/>
  <circle cx="0" cy="-42" r="8" class="coral o"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('kit', '道具ひとそろいの入った箱のイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-180 0h360v90h-360z" class="goldd o"/>
  <path d="M-180 0l-30-90h420l-30 90z" class="goldp o"/>
  <path d="M-150-70h300" class="a"/>
</g>
<g transform="translate(210 230)">
  <path d="M-10-40h20v70h-20z" class="ink"/>
  <path d="M-24-56h48v20h-48z" class="ink"/>
</g>
<g transform="translate(300 230)">
  <path d="M-8-40h16v70h-16z" class="ink"/>
  <path d="M-8-40l-14-16h44l-14 16z" class="ink"/>
</g>
<g transform="translate(390 230)">
  <circle cy="-30" r="20" fill="none" stroke="{INK}" stroke-width="8"/>
  <path d="M-6-10h12v40h-12z" class="ink"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('labour', '汗を流して働く労働のイラスト。', f"""
{person(180,352,1.2,1,'coral','blue','reach','cap','neutral')}
<g transform="translate(280 250)">
  <path d="M-10-70h20v130h-20z" fill="{TONES['gold'][2]}"/>
  <path d="M-50-90h100v30h-100z" fill="{MUTED}" class="o"/>
</g>
{box(450,300,150,90,26,'gold')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M120 200l-14-20M250 190v-22"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('lad', '元気な男の子のイラスト。', f"""
{person(300,352,0.9,1,'gold','blue','up','cap','smile')}
<circle cx="440" cy="330" r="38" class="coralp o"/>
<g fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"><path d="M402 330h76M440 292v76"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M360 250q40-30 70-10"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('landing', '滑走路に降り立つ着陸のイラスト。', f"""
{plane(360,180,0.85,12,'teal')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="14 12"><path d="M80 90q180 100 300 130"/></g>
<path d="M40 320h520v50H40z" fill="#dfe6ea" class="o"/>
<g fill="none" stroke="#fffdf6" stroke-width="5" stroke-dasharray="26 22"><path d="M40 345h520"/></g>
<g class="a" marker-end="url(#ar)"><path d="M470 230v70"/></g>
""", ground=False, arrow=True)

add('landscape', '見晴らしのよい景色のイラスト。', f"""
<path d="M0 0h600v230H0z" fill="#e6f0fb"/>
{sun(490,90,40)}
<path d="M0 230l150-140 110 110 90-80 250 110z" class="greenp o"/>
<path d="M150 90l50 46-100 0z" fill="#fffdf6" class="o"/>
<path d="M0 230h600v170H0z" class="green o"/>
<path d="M120 400q60-120 200-120t280 60" fill="{TONES['blue'][1]}" stroke="{INK}" stroke-width="3"/>
{tree(90,330,0.9)}
{tree(500,350,1)}
""", ground=False)

add('lap', 'いすに座ったひざの上のイラスト。', f"""
<g transform="translate(300 340)">
  <path d="M-90-20h180v20h-180z" class="goldd o"/>
  <path d="M-80 0v40M80 0v40" class="a"/>
  <path d="M60-150h30v130h-30z" class="gold o"/>
</g>
{sit(280,340,1.4,1,'teal','blue','short','smile','lap')}
<g transform="translate(336 292)">
  <path d="M-46-16h92v32h-92z" class="paper"/>
  <path d="M0-16v32" class="a"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><ellipse cx="336" cy="294" rx="70" ry="34"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('laser', 'まっすぐ細く伸びるレーザー光のイラスト。', f"""
<g transform="translate(130 220)">
  <path d="M-60-40h120v80h-120z" class="ink"/>
  <path d="M60-20h30v40H60z" class="bluep o"/>
  <circle cx="-30" cy="-20" r="7" class="coral"/>
</g>
<path d="M220 220h270" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"/>
<path d="M220 220h270" fill="none" stroke="#ffd9d1" stroke-width="3"/>
<g transform="translate(520 220)">
  <path d="M-30-90h60v180h-60z" fill="#dfe6ea" class="o"/>
  <circle r="16" class="coral o"/>
  <g class="corals" fill="none"><circle r="30"/><circle r="46"/></g>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('lately', 'ここ最近の日付だけに印がついたイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-220-150h440v300h-440z" class="paper"/>
  <path d="M-220-150h440v50h-440z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M-220 {-50+r*50}h440"/>' for r in range(4))}
    {''.join(f'<path d="M{-157+c*63} -100v250"/>' for c in range(6))}
  </g>
  <g class="coralp o">{''.join(f'<circle cx="{31+c*63}" cy="100" r="20"/>' for c in range(3))}</g>
  <g class="coralp o">{''.join(f'<circle cx="{-94+c*63}" cy="50" r="20"/>' for c in range(4))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M530 300v-60"/></g>
""", ground=False, arrow=True)

add('lawn', '刈りそろえられた芝生のイラスト。', f"""
<path d="M0 200h600v200H0z" class="green o"/>
<g fill="none" stroke="{TONES['green'][2]}" stroke-width="6" stroke-dasharray="30 24">
  {''.join(f'<path d="M0 {230+i*34}h600"/>' for i in range(5))}
</g>
<g transform="translate(430 250)">
  <path d="M-70 40h140v30h-140z" class="coral o"/>
  <path d="M60 40l50-80" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <circle cx="-50" cy="76" r="18" class="ink"/><circle cx="50" cy="76" r="18" class="ink"/>
</g>
{tree(90,200,0.9)}
""", ground=False)

add('lawsuit', '書類を持って法廷で争う訴訟のイラスト。', f"""
<g transform="translate(300 190)">
  <path d="M-130 60h260v40h-260z" class="teald o"/>
  <path d="M-100-60h200v120h-200z" fill="#fffdf6" class="o"/>
  <path d="M-114-60L0-120l114 60z" class="teal o"/>
  <g class="tealp o"><rect x="-70" y="-30" width="30" height="90"/><rect x="-15" y="-30" width="30" height="90"/><rect x="40" y="-30" width="30" height="90"/></g>
</g>
{person(130,356,1,1,'coral','blue','carry','short','neutral')}
{person(470,356,1,-1,'violet','gold','carry','bob','neutral')}
<g transform="translate(178 320)"><path d="M-24-30h48v56h-48z" class="paper"/></g>
<g transform="translate(422 320)"><path d="M-24-30h48v56h-48z" class="paper"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('layer', '幾重にも重なった層のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-190 60h380v40h-380z" class="goldd o"/>
  <path d="M-190 20h380v40h-380z" class="coralp o"/>
  <path d="M-190-20h380v40h-380z" class="gold o"/>
  <path d="M-190-60h380v40h-380z" class="tealp o"/>
  <path d="M-190-100h380v40h-380z" class="teal o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M520 340v-200"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('layout', '要素の置き場所を決めた配置のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-200-150h400v300h-400z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="6 8">
    {''.join(f'<path d="M{-160+c*80} -150v300"/>' for c in range(5))}
    {''.join(f'<path d="M-200 {-110+r*60}h400"/>' for r in range(5))}
  </g>
  <path d="M-170-120h340v70h-340z" class="teal o"/>
  <path d="M-170-30h150v110h-150z" class="tealp o"/>
  <path d="M0-30h170v50H0z" class="gold o"/>
  <path d="M0 40h170v40H0z" class="goldp o"/>
  <path d="M-170 100h340v30h-340z" class="bluep o"/>
</g>
""", ground=False)

add('leadership', '先頭に立って皆を引っぱる指導力のイラスト。', f"""
{person(180,350,1.25,1,'coral','blue','carry','short','smile')}
<g transform="translate(212 220)">
  <path d="M0 130V-60" class="a"/>
  <path d="M0-60h90l-16 24 16 24H0z" class="coral o"/>
</g>
{person(340,352,1,1,'teal','blue','walk','bob','smile')}
{person(430,352,1,1,'gold','violet','walk','short','smile')}
{person(520,352,1,1,'green','blue','walk','bun','smile')}
<path d="M60 376h480" class="a"/>
""", ground=True)

add('leaflet', '手渡しで配るちらしのイラスト。', f"""
{hand(140,220,1)}
<g transform="translate(340 220)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <path d="M-60-80h120v60h-120z" class="coralp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-60 0h120M-60 24h120M-60 48h90"/></g>
</g>
<g transform="translate(500 320)">
  <path d="M-60-40h120v50h-120z" class="paper"/>
  <path d="M-64-28h120v50h-120z" class="paper"/>
  <path d="M-68-16h120v50h-120z" class="paper"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('league', '複数のチームが競い合うリーグのイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-230-130h140v90h-140z" class="tealp o"/>
  <path d="M-70-130h140v90H-70z" class="coralp o"/>
  <path d="M90-130h140v90H90z" class="goldp o"/>
  <g class="o" fill="none">
    <path d="M-160-40v40h80v40M0-40v80M160-40v40H80"/>
  </g>
  <path d="M-40 80h80v60h-80z" class="teal o"/>
  <path d="M-40 80l40-40 40 40z" class="gold o"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('legacy', '前の世代から受け継がれるもののイラスト。', f"""
{person(150,352,1.1,1,'violet','violet','give','bun','smile')}
{person(460,352,1.1,-1,'teal','blue','reach','short','smile')}
<g transform="translate(300 250)">
  <path d="M-70-40h140v80h-140z" class="goldd o"/>
  <path d="M-70-40q0-40 70-40t70 40z" class="gold o"/>
  <path d="M-14 0h28v30h-28z" class="goldp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 180h120"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('legend', '語り継がれる古い伝説のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-200-120q-30 0-30 30t30 30h360q30 0 30-30t-30-30z" class="goldp o"/>
  <path d="M-200 60q-30 0-30 30t30 30h360q30 0 30-30t-30-30z" class="goldp o"/>
  <path d="M-200-60h400v120h-400z" fill="#fdf6e3" class="o"/>
  <path d="M-150-20q40-40 80 0t80 0 80 0" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M-90 30q60-40 120 0" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M120-10q30-30 50 0-20 30-50 0z" class="coral o"/>
</g>
{flame(300,360,0.7)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('leisure', 'いすに深く座ってくつろぐ余暇のイラスト。', f"""
{sun(510,90,42)}
{sit(250,340,1.4,1,'coral','gold','bob','smile','down')}
<g transform="translate(250 340)">
  <path d="M-60 0v-40h130v40" fill="none" stroke="{TONES['blue'][2]}" stroke-width="14" stroke-linejoin="round"/>
  <path d="M-60-40v-120" fill="none" stroke="{TONES['blue'][2]}" stroke-width="14" stroke-linecap="round"/>
</g>
<g transform="translate(440 300)">
  <path d="M-30-40h60l-8 46h-44z" class="tealp o"/>
  <path d="M-30-40h60v10h-60z" class="teal o"/>
  <path d="M20-56v20" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('lens', '光を一点に集めるレンズのイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M0-130q60 60 0 260-60-130 0-260z" class="bluep o"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4">
  <path d="M60 130h230M60 175h230M60 220h230M60 265h230M60 310h230"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4">
  <path d="M312 140l150 78M312 180l150 38M312 220h150M312 260l150-42M312 300l150-82"/>
</g>
<circle cx="470" cy="218" r="14" class="gold o"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('liberation', '鎖が断ち切られて解き放たれるイラスト。', f"""
{person(300,352,1.3,1,'teal','blue','up','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="9">
  <circle cx="130" cy="200" r="20"/><circle cx="170" cy="215" r="20"/>
  <circle cx="470" cy="200" r="20"/><circle cx="430" cy="215" r="20"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M200 180l40 30M240 180l-40 30M360 180l40 30M400 180l-40 30"/>
</g>
<g class="golds"><path d="M300 90v-24M180 120l-20-20M420 120l20-20"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('liberty', '高くかかげられた自由のたいまつのイラスト。', f"""
{person(300,352,1.35,1,'teal','violet','up','bun','smile')}
<g transform="translate(258 120)">
  <path d="M-16 60h32l-8-70h-16z" class="goldd o"/>
  <path d="M-24-10h48v14h-48z" class="gold o"/>
  <path d="M0-90q30 30 22 60-10 22-22 22t-22-22c-8-30 22-60 22-60z" class="coral o"/>
  <path d="M0-56q14 18 8 34-4 12-8 12t-8-12c-4-16 8-34 8-34z" class="goldp o"/>
</g>
<g class="golds"><path d="M180 90l-24-16M340 76l20-20"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('licence', '資格を認める免許証のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-200-120h400v240h-400z" class="paper"/>
  <path d="M-200-120h400v44h-400z" class="teal o"/>
  <g transform="translate(-110 30)">
    <circle cx="0" cy="-34" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
    <path d="M-46 56v-14q0-30 46-30t46 30v14z" class="blue o"/>
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-10-30h170M-10 10h170M-10 50h130"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"><circle cx="130" cy="76" r="34"/><path d="M108 76h44"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('lifetime', '生まれてから年を重ねるまでの一生のイラスト。', f"""
{person(120,340,0.6,1,'gold','gold','stand','short','smile')}
{person(280,344,0.9,1,'teal','blue','stand','short','smile')}
{person(460,346,1.05,1,'violet','violet','stand','bun','smile')}
<g class="a" marker-end="url(#ar)"><path d="M70 376h480"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M120 300v-60M280 250v-60M460 220v-60"/></g>
""", ground=True, arrow=True)

add('limitation', 'ここから先へは進めない制約のイラスト。', f"""
{person(180,352,1.15,1,'teal','blue','walk','short','sad')}
<g transform="translate(380 250)">
  <path d="M-10-100h20v230h-20z" class="ink"/>
  <path d="M-140-100h280v30h-280z" class="coral o"/>
  <g fill="none" stroke="#fffdf6" stroke-width="6">{''.join(f'<path d="M{-120+i*40} -100l-20 30"/>' for i in range(7))}</g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M260 280h80"/></g>
{xx(380 ,150,0.9)}
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('link', '輪と輪がつながる結びつきのイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="22" stroke-linecap="round">
  <ellipse cx="220" cy="210" rx="90" ry="56"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="22" stroke-linecap="round">
  <ellipse cx="380" cy="210" rx="90" ry="56"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="22" stroke-linecap="round">
  <path d="M290 154a90 56 0 0 0-20 56 90 56 0 0 0 20 56"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('listing', '項目を並べて載せた一覧のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-200-150h400v300h-400z" class="paper"/>
  <path d="M-200-150h400v46h-400z" class="teal o"/>
  <g class="tealp o">{''.join(f'<rect x="-170" y="{-80+i*46}" width="26" height="26"/>' for i in range(5))}</g>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-120 {-68+i*46}h300"/>' for i in range(5))}</g>
  <g fill="none" stroke="{MUTED}" stroke-width="2">{''.join(f'<path d="M-200 {-42+i*46}h400"/>' for i in range(4))}</g>
</g>
""", ground=False)

add('literacy', '文字を読み書きできる力のイラスト。', f"""
<g transform="translate(200 210)">
  <path d="M-130-100h260v200h-260z" class="paper"/>
  <path d="M0-100v200" class="a"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">
    <path d="M-100-60h80M-100-30h80M-100 0h60M20-60h80M20-30h80M20 0h60"/>
  </g>
</g>
<g transform="translate(440 230)">
  <path d="M-14-130h28l10 130-24 40-24-40z" class="gold o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" stroke-linecap="round"><path d="M-70 90q40-40 80 0t80-10"/></g>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('litre', '一リットルの目盛りまで入った容器のイラスト。', f"""
<g transform="translate(280 240)">
  <path d="M-90 130v-200q0-30 30-34v-30h120v30q30 4 30 34v200z" fill="#fffdf6" class="o"/>
  <path d="M-90 130V20q80-16 180 0v110z" class="bluep o"/>
  <path d="M-90 20q80-16 180 0" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-90 {100-i*40}h34"/>' for i in range(5))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M470 380V260"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M430 260h80M430 380h80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('litter', '散らかったごみのイラスト。', f"""
<g transform="translate(470 290)">
  <path d="M-70 0h140l-16 90h-108z" class="tealp o"/>
  <path d="M-80-14h160v14h-160z" class="teal o"/>
</g>
<g class="goldp o">
  <path d="M120 330l40-16 12 36-40 10z"/>
  <ellipse cx="230" cy="356" rx="34" ry="14"/>
  <path d="M300 320l30 20-24 26-20-26z"/>
</g>
<g class="coralp o"><path d="M180 380l40-10 6 24-40 8z"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 8"><path d="M160 300q40-40 90-30M280 290q60-30 100-10"/></g>
<path d="M60 396h480" class="a"/>
""", ground=True)

add('liver', 'おなかの右上にある肝臓のイラスト。', f"""
<g transform="translate(300 210)">
  <circle cx="0" cy="-140" r="40" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-120 150v-110q0-90 120-90t120 90v110z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-100-40q60-30 140-20 60 8 60 40 0 46-70 50-70 4-100-20-30-24-30-50z" class="corald o"/>
  <path d="M20-56q10 60-10 84" fill="none" stroke="{TONES['coral'][1]}" stroke-width="5"/>
  <path d="M60 0q20 0 24 20" fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('loan', '借りたお金を後で返すイラスト。', f"""
{person(140,352,1.1,1,'violet','blue','give','bun','neutral')}
{person(470,352,1.1,-1,'teal','gold','give','short','neutral')}
<g transform="translate(300 200)">
  <path d="M-70-30h140v60h-140z" class="greenp o"/>
  <circle r="16" class="gold o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M220 160h160"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M390 290H220"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('logic', '筋道立てて順に結論へ進む論理のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-230-50h100v100h-100z" class="tealp o"/>
  <path d="M-60-50h100v100H-60z" class="tealp o"/>
  <path d="M110-50h120v100H110z" class="teal o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 220h50M350 220h50"/></g>
{ck(470,120,1)}
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('logo', '看板に掲げられた店のマークのイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-190-120h380v240h-380z" fill="#fffdf6" class="o"/>
  <g transform="translate(-90 0)">
    <circle r="70" class="teal o"/>
    <path d="M-30 20l30-56 30 56z" fill="#fffdf6"/>
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round"><path d="M20-30h150M20 20h110"/></g>
</g>
<path d="M300 330v40" class="a"/>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('loneliness', 'だれもいない中でひとりきりの寂しさのイラスト。', f"""
{sit(300,330,1.3,1,'blue','blue','short','sad','down')}
<g transform="translate(300 330)">
  <path d="M-120-14h240v14h-240z" class="goldd o"/>
  <path d="M-100 0v40M100 0v40" class="a"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 12"><circle cx="300" cy="230" r="200"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('loop', 'ぐるりと回ってもとに戻る輪のイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="20" stroke-linecap="round" marker-end="url(#ar)">
  <path d="M420 130a130 130 0 1 0 30 110"/>
</g>
<g fill="none" stroke="{TONES['teal'][1]}" stroke-width="6">
  <path d="M420 130a130 130 0 1 0 30 110"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('lord', '土地を治める領主のイラスト。', f"""
{person(190,352,1.3,1,'violet','violet','stand','short','neutral')}
<g transform="translate(190 200)">
  <path d="M-40 8l-8-42 24 16 24-32 24 32 24-16-8 42z" class="gold o"/>
</g>
<g transform="translate(450 310)">
  <path d="M-90 0v-90h180V0z" fill="#fffdf6" class="o"/>
  <path d="M-104-90L0-150l104 60z" class="teal o"/>
  <path d="M-24-56h48V0h-48z" class="teald o"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('lottery', '当たりを引き当てる宝くじのイラスト。', f"""
<g transform="translate(230 240)">
  <path d="M-130-70h260v140h-260z" class="goldp o"/>
  <path d="M-130-70h260v140h-260zM-60-70v140M60-70v140" class="a"/>
  <circle cx="-90" cy="0" r="20" class="coral o"/>
  <circle cx="0" cy="0" r="20" class="coral o"/>
  <circle cx="90" cy="0" r="20" class="coral o"/>
</g>
<g class="golds"><path d="M80 120l-20-24M380 120l20-24M230 100v-24"/></g>
<g transform="translate(480 260)">
  <circle r="70" fill="#fffdf6" class="o"/>
  <circle cx="-20" cy="-14" r="18" class="tealp o"/>
  <circle cx="24" cy="10" r="18" class="coralp o"/>
  <circle cx="-6" cy="34" r="18" class="goldp o"/>
  <path d="M-70 60h140v30h-140z" class="ink"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
