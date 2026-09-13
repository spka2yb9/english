"""第88回: ob〜pe の名詞を中心に45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'
def note(x,y,s=1,cls='ink'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 30q-14 0-14-12t14-12q8 0 12 5v-45l30-9v14l-20 6v40q0 13-22 13z" '
            f'fill="{INK if cls=="ink" else TONES[cls][0]}"/></g>')

add('obstacle', '道の途中に立ちはだかる障害のイラスト。', f"""
{person(150,352,1.15,1,'teal','blue','walk','short','sad')}
<g transform="translate(360 300)">
  <path d="M-110 60q-30-90 20-130 60-46 130-10 60 30 30 100z" fill="#8b98a6" class="o"/>
  <path d="M-40-50l30 100M40-70l-20 120" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 250h30"/></g>
{xx(360,140,1)}
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('occurrence', '時の流れの上で起きた出来事のイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M60 320h480"/></g>
<g class="ink">{''.join(f'<circle cx="{120+i*90}" cy="320" r="8"/>' for i in range(5))}</g>
<g transform="translate(300 190)">
  <path d="M0-110l30 54 58-18-18 58 54 30-54 30 18 58-58-18-30 54-30-54-58 18 18-58-54-30 54-30-18-58 58 18z" class="coralp o"/>
  <g fill="{TONES['coral'][2]}"><rect x="-12" y="-56" width="24" height="70" rx="12"/><circle cy="38" r="14"/></g>
</g>
<path d="M300 286v20" class="a"/>
""", ground=False, arrow=True)

add('offence', '決まりを破ってしまう違反のイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-10-90h20v200h-20z" class="ink"/>
  <circle cy="-120" r="60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="14"/>
  <path d="M-40-120h80" fill="none" stroke="{TONES['coral'][0]}" stroke-width="14"/>
</g>
{person(420,352,1.15,1,'coral','blue','walk','short','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="14 12"><path d="M300 130v250"/></g>
<g class="a" marker-end="url(#ar)"><path d="M360 300h-90"/></g>
{xx(300,110,0.9)}
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('offender', '決まりを破った人が指し示されるイラスト。', f"""
{person(360,352,1.25,1,'coral','blue','stand','short','sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10"><rect x="290" y="200" width="150" height="180" rx="20"/></g>
{hand(130,250,1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M190 250h80"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('offering', '両手でささげ持って差し出す供え物のイラスト。', f"""
{person(300,352,1.25,1,'violet','blue','give','bun','neutral')}
<g transform="translate(410 250)">
  <ellipse rx="90" ry="26" class="goldp o"/>
  <path d="M-40-40h80l-10 40h-60z" class="gold o"/>
  <circle cx="-46" cy="-20" r="18" class="coralp o"/>
  <circle cx="46" cy="-18" r="18" class="greenp o"/>
</g>
<g class="golds"><path d="M410 150v-24M330 170l-20-20M490 170l20-20"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('offspring', '親のあとに続く子どもたちのイラスト。', f"""
{person(180,352,1.3,1,'violet','blue','give','bun','smile')}
{person(330,354,0.8,1,'teal','blue','walk','short','smile')}
{person(420,354,0.7,1,'gold','violet','walk','bob','smile')}
{person(500,354,0.6,1,'coral','green','walk','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M250 280h40"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('opening', 'テープを切って始まる開幕のイラスト。', f"""
{person(150,352,1.1,1,'violet','blue','reach','bun','smile')}
{person(450,352,1.1,-1,'teal','gold','reach','short','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10">
  <path d="M110 250h150M340 250h150"/>
</g>
<g transform="translate(300 250) rotate(-20)">
  <path d="M0-10l-50-40q-16-14 0-24 12-8 22 6zM0 10l-50 40q-16 14 0 24 12 8 22-6z" fill="#c8d2d8" class="o"/>
  <path d="M0-10q40 0 40 10t-40 10z" fill="{MUTED}" class="o"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('opera', '舞台で高らかに歌うオペラのイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-260-160h520v50h-520z" class="corald o"/>
  <path d="M-260-110q40 200 0 300h100q-30-160 0-300z" class="coral o"/>
  <path d="M260-110q-40 200 0 300H160q30-160 0-300z" class="coral o"/>
</g>
{person(300,352,1.3,1,'violet','violet','up','bun','smile')}
{note(400,180,1.2,'gold')}
{note(200,150,1.2,'gold')}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('opposition', '真正面からぶつかり合う反対のイラスト。', f"""
{person(150,352,1.15,1,'teal','blue','reach','short','neutral')}
{person(450,352,1.15,-1,'coral','gold','reach','bob','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M230 250h50M370 250h-50"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M300 210v-30M270 220l-20-20M330 220l20-20"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('orchestra', '指揮者と奏者がそろう管弦楽団のイラスト。', f"""
{person(300,220,1.05,1,'violet','violet','up','bun','neutral')}
{sit(130,360,0.8,1,'teal','blue','short','neutral','lap')}
{sit(250,360,0.8,1,'teal','blue','bob','neutral','lap')}
{sit(370,360,0.8,1,'teal','blue','short','neutral','lap')}
{sit(490,360,0.8,1,'teal','blue','bun','neutral','lap')}
<g class="gold o">
  <path d="M170 300q-16 40 10 46 26 6 26-30 0-30-20-30z"/>
  <path d="M290 300q-16 40 10 46 26 6 26-30 0-30-20-30z"/>
  <path d="M410 300q-16 40 10 46 26 6 26-30 0-30-20-30z"/>
</g>
{note(80,150,1,'coral')}
{note(520,150,1,'coral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('orientation', '地図と方位で向きを定めるイラスト。', f"""
<g transform="translate(190 220)">
  <circle r="110" fill="#fffdf6" class="o"/>
  <path d="M0-80l24 60-24 20-24-20z" class="coral o"/>
  <path d="M0 80l-24-60 24-20 24 20z" fill="#dfe6ea" class="o"/>
  <circle r="10" class="ink"/>
  <g fill="{INK}">{''.join(f'<rect x="-3" y="-104" width="6" height="14" transform="rotate({a})"/>' for a in range(0,360,45))}</g>
</g>
{person(430,352,1.2,1,'teal','blue','carry','cap','neutral')}
<g transform="translate(470 260)">
  <path d="M-50-36h100v72h-100z" class="paper"/>
  <path d="M-50 10q30-30 50 0t50-10" fill="none" stroke="{GRN}" stroke-width="4"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('origin', '川の始まりとなる源のイラスト。', f"""
<path d="M0 400V240l120-140 100 90 90-70 290 160v120z" class="greenp o"/>
<g transform="translate(140 180)">
  <circle r="30" class="blue o"/>
  <circle r="46" fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"/>
</g>
<path d="M150 200q60 80 20 130t80 70h350" fill="none" stroke="{TONES['blue'][0]}" stroke-width="18" stroke-linecap="round"/>
<g class="a" marker-end="url(#ar)"><path d="M240 130l-60 20"/></g>
""", ground=False, arrow=True)

add('outbreak', '一点から一気に広がる発生のイラスト。', f"""
<circle cx="180" cy="240" r="30" class="coral o"/>
<g class="coralp o">
  <circle cx="290" cy="180" r="20"/><circle cx="320" cy="270" r="20"/><circle cx="260" cy="320" r="18"/>
  <circle cx="410" cy="140" r="16"/><circle cx="440" cy="240" r="16"/><circle cx="400" cy="330" r="16"/>
  <circle cx="520" cy="200" r="13"/><circle cx="530" cy="300" r="13"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3" stroke-dasharray="8 8">
  <path d="M215 225q60-30 130-40M215 250q80 20 190 0M210 265q50 50 120 60"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('outcome', '流れの末に出てきた結果のイラスト。', f"""
<g transform="translate(220 230)">
  <path d="M-160-70h140v140h-140z" class="tealp o"/>
  <path d="M20-70h140v140H20z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M100 230h30M300 230h40"/></g>
<g transform="translate(460 230)">
  <path d="M-80-80h160v160h-160z" class="teal o"/>
  <g fill="none" stroke="#fffdf6" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"><path d="M-40 0l24 30 56-64"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('outdoors', '建物の外の空の下にいるイラスト。', f"""
<path d="M0 0h600v300H0z" fill="#e6f0fb"/>
{sun(500,80,42)}
{cloud(160,90,1.2,'blue')}
{tree(110,320,1.1)}
{tree(520,320,1)}
<g transform="translate(300 320)">
  <path d="M-90 0l90-120 90 120z" class="coralp o"/>
  <path d="M-30 0l30-40 30 40z" class="corald o"/>
</g>
{person(200,340,0.85,1,'teal','blue','walk','short','smile')}
<path d="M0 320h600" class="a"/>
""", ground=False)

add('outing', 'かごを持って出かける遠出のイラスト。', f"""
{tree(520,330,1.1)}
{person(200,352,1.15,1,'coral','blue','walk','bun','smile')}
{person(310,354,0.85,1,'gold','violet','walk','short','smile')}
<g transform="translate(258 300)">
  <path d="M-40 0h80l-10 50h-60z" class="goldp o"/>
  <path d="M-40 0q40-44 80 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="5"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M380 340h100"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('outlook', '高い所から先を見わたす見通しのイラスト。', f"""
<path d="M0 400V300l120-90 100 60v130z" class="greenp o"/>
{person(160,300,1.1,1,'teal','blue','hold','short','neutral')}
<g transform="translate(210 200)">
  <path d="M-30-12h90v24h-90z" fill="{MUTED}" class="o"/>
  <path d="M60-20h30v40H60z" class="ink"/>
</g>
<path d="M260 260h340" class="a"/>
{sun(500,150,38)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><path d="M290 210h230"/></g>
""", ground=False)

add('output', '機械から次々と出てくる生産物のイラスト。', f"""
<g transform="translate(200 230)">
  <path d="M-140-110h280v220h-280z" class="bluep o"/>
  <path d="M-60-60h120v80h-120z" class="ink"/>
  <path d="M140-30h60v60h-60z" class="blued o"/>
</g>
<path d="M400 260h180v30H400z" fill="#dfe6ea" class="o"/>
<g class="gold o"><rect x="410" y="200" width="50" height="56"/><rect x="480" y="200" width="50" height="56"/></g>
<g class="a" marker-end="url(#ar)"><path d="M370 160h80"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('oxygen', '息をするのに要る酸素のイラスト。', f"""
{tree(140,340,1.3)}
<g transform="translate(400 200)">
  <circle cx="-46" cy="0" r="58" class="tealp o"/>
  <circle cx="46" cy="0" r="58" class="tealp o"/>
  <path d="M-46 0h92" fill="none" stroke="{TONES['teal'][0]}" stroke-width="8"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M230 250q60-60 100-60"/></g>
<g class="tealp o"><circle cx="500" cy="320" r="18"/><circle cx="540" cy="290" r="12"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('pad', '角を守るために当てるパッドのイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-140-40h280v130h-280z" class="goldd o"/>
  <path d="M-150-70q40-30 80 0 40-30 80 0 40-30 80 0v40h-240z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"><path d="M-80-60v40M0-60v40M80-60v40"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M300 100v60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('panel', '壁に取り付けられた平たい板のイラスト。', f"""
<g transform="translate(300 210) rotate(-8)">
  <path d="M-190-120h380v240h-380z" class="bluep o"/>
  <g fill="none" stroke="{TONES['blue'][2]}" stroke-width="4">
    {''.join(f'<path d="M{-190+i*76} -120v240"/>' for i in range(1,5))}
    <path d="M-190 0h380"/>
  </g>
</g>
<g fill="{MUTED}" class="o"><rect x="230" y="330" width="30" height="60"/><rect x="340" y="330" width="30" height="60"/></g>
<path d="M60 390h480" class="a"/>
""", ground=True)

add('panic', 'あわてふためいて逃げまどうイラスト。', f"""
{person(140,352,1.1,-1,'coral','blue','up','short','surprised')}
{person(300,352,1.15,1,'gold','violet','up','bob','surprised')}
{person(470,352,1.1,1,'teal','gold','up','short','surprised')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M90 190l-16-22M220 170v-24M370 180l-14-24M530 190l16-22"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M110 130H60M490 130h50"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('paperwork', '山と積まれた事務書類のイラスト。', f"""
<g transform="translate(360 250)">
  <path d="M-130-30h260v130h-260z" class="paper"/>
  <path d="M-136-60h260v130h-260z" class="paper"/>
  <path d="M-124-90h260v130h-260z" class="paper"/>
  <path d="M-130-124h260v130h-260z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-100-96h200M-100-70h200M-100-44h160"/></g>
</g>
{person(140,352,1.1,1,'violet','blue','up','short','sad')}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('parade', '旗をかかげて列を作り歩く行進のイラスト。', f"""
{person(140,352,1.05,1,'coral','blue','walk','cap','smile')}
{person(250,352,1.05,1,'teal','blue','walk','cap','smile')}
{person(360,352,1.05,1,'gold','blue','walk','cap','smile')}
{person(470,352,1.05,1,'violet','blue','walk','cap','smile')}
<g class="coral o">
  <path d="M176 200h70l-14 22 14 22h-70z"/><path d="M286 200h70l-14 22 14 22h-70z"/>
  <path d="M396 200h70l-14 22 14 22h-70z"/><path d="M506 200h70l-14 22 14 22h-70z"/>
</g>
<g class="a"><path d="M176 260v-70M286 260v-70M396 260v-70M506 260v-70"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('parallel', 'どこまでも交わらない平行線のイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="12" stroke-linecap="round">
  <path d="M60 160h480M60 260h480"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5">
  <path d="M180 160v100M300 160v100M420 160v100"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M170 160h20M170 260h20M290 160h20M290 260h20M410 160h20M410 260h20"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('parameter', '目盛りの上で値を決める設定のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-220-60h440v20h-440z" fill="#dfe6ea" class="o"/>
  <path d="M-220-60h240v20h-240z" class="teal o"/>
  <path d="M0-88h40v76H0z" class="teald o"/>
  <path d="M-220 60h440v20h-440z" fill="#dfe6ea" class="o"/>
  <path d="M-220 60h100v20h-100z" class="coral o"/>
  <path d="M-140 32h40v76h-40z" class="corald o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M{80+i*88} 320v14"/>' for i in range(6))}</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('parish', '教会を中心とした受け持ちの区域のイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="16 12"><circle cx="300" cy="230" r="180"/></g>
<g transform="translate(300 300)">
  <path d="M-60 0v-90h120V0z" fill="#fffdf6" class="o"/>
  <path d="M-72-90L0-146l72 56z" class="teal o"/>
  <path d="M-14-56h28V0h-28z" class="teald o"/>
  <path d="M-8-190h16v50h-16zM-24-176h48v16h-48z" class="ink"/>
</g>
<g class="goldp o"><path d="M130 320h50v40h-50zM420 320h50v40h-50z"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('participant', '番号をつけて催しに加わる参加者のイラスト。', f"""
{person(300,352,1.35,1,'teal','blue','stand','short','smile')}
<g transform="translate(300 290)">
  <path d="M-46-34h92v68h-92z" class="paper"/>
  <g fill="{INK}"><rect x="-26" y="-12" width="18" height="26"/><rect x="8" y="-12" width="18" height="26"/></g>
</g>
{person(120,356,0.8,1,'gold','violet','stand','bob','smile')}
{person(490,356,0.8,-1,'coral','gold','stand','bun','smile')}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('participation', 'みんなが手を挙げて加わるイラスト。', f"""
{person(120,352,1,1,'teal','blue','up','short','smile')}
{person(240,352,1,1,'gold','violet','up','bob','smile')}
{person(360,352,1,1,'coral','blue','up','short','smile')}
{person(480,352,1,1,'green','gold','up','bun','smile')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="14 12"><circle cx="300" cy="240" r="220"/></g>
{ck(300,90,1)}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('partnership', '手を結んで組む提携のイラスト。', f"""
{person(160,352,1.15,1,'teal','blue','give','short','smile')}
{person(440,352,1.15,-1,'coral','gold','give','bob','smile')}
<g transform="translate(300 260)">
  <path d="M-70 0h60v20h-60z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M10 0h60v20H10z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-20-16h40v52h-40z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g transform="translate(160 180)"><circle r="34" class="tealp o"/></g>
<g transform="translate(440 180)"><path d="M-30-30h60v60h-60z" class="coralp o"/></g>
<g class="a"><path d="M200 180h200"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('passage', '本の中の一節に印をつけたイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-220-150h440v300h-440z" class="paper"/>
  <path d="M0-150v300" class="a"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">
    <path d="M-190-110h160M-190-80h160M-190-50h130M-190 40h160M-190 70h160M-190 100h120"/>
    <path d="M30-110h160M30-80h160M30-50h130M30-20h160M30 10h160M30 40h120M30 70h160M30 100h130"/>
  </g>
  <path d="M-200-30h180v54h-180z" class="goldp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-190-20h160M-190 10h130"/></g>
</g>
""", ground=False)

add('password', '合いことばを入れて開く鍵のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-170-140h340v280h-340z" class="ink"/>
  <path d="M-156-126h312v252h-312z" fill="#fffdf6"/>
  <path d="M-60-40h120v90h-120z" class="gold o"/>
  <path d="M-34-40v-24q0-34 34-34t34 34v24" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10"/>
  <g class="ink">{''.join(f'<circle cx="{-42+i*28}" cy="80" r="9"/>' for i in range(4))}</g>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('pastor', '教会で説教をする牧師のイラスト。', f"""
<g transform="translate(430 260)">
  <path d="M-120 60v-130h240V60z" fill="#fffdf6" class="o"/>
  <path d="M-134-70L0-146l134 76z" class="teal o"/>
  <path d="M-8-230h16v60h-16zM-26-214h52v16h-52z" class="ink"/>
  <path d="M-40-30h80v90h-80z" class="tealp o"/>
</g>
{person(180,352,1.25,1,'violet','violet','point','short','neutral')}
<g transform="translate(180 330)">
  <path d="M-46-40h92l14 60h-120z" class="goldd o"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('patch', '穴の上に当て布をつぎ当てるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-130h400v270h-400z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3">{''.join(f'<path d="M{-170+i*40} -130v270"/>' for i in range(9))}</g>
</g>
<g transform="translate(300 220) rotate(8)">
  <path d="M-80-60h160v120h-160z" class="goldp o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="3" stroke-dasharray="10 8"><path d="M-70-50h140v100h-140z"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('patent', '発明を認める特許状のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-190-150h380v300h-380z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-140 60h280M-140 96h220"/></g>
  <circle cx="120" cy="-16" r="40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
  <path d="M96-16h48M120-40v48" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
</g>
<g transform="translate(230 180)">
  <path d="M0-70q46 0 46 44 0 26-20 38v18h-52v-18q-20-12-20-38 0-44 46-44z" class="gold o"/>
  <path d="M-26 34h52v16h-52z" class="goldd o"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('pathway', '先へ続く一本の小道のイラスト。', f"""
<path d="M240 400q0-120 60-160t60-140h60q0 120-60 160t-60 140z" fill="#dfe6ea" class="o"/>
{tree(120,340,1)}
{tree(500,300,0.9)}
{person(250,370,0.85,1,'teal','blue','walk','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M290 350q40-100 90-150"/></g>
""", ground=False, arrow=True)

add('patience', '砂が落ちきるまで静かに待つ忍耐のイラスト。', f"""
<g transform="translate(420 220)">
  <path d="M-80-130h160v20h-160zM-80 130h160v20h-160z" fill="{TONES['gold'][2]}"/>
  <path d="M-70-110h140L10 0l60 110h-140L-10 0z" fill="#fffdf6" class="o"/>
  <path d="M-60-100h120L0-14z" class="goldp o"/>
  <path d="M-50 100h100L0 24z" class="gold o"/>
  <path d="M0-10v40" fill="none" stroke="{TONES['gold'][0]}" stroke-width="4"/>
</g>
{sit(160,350,1.2,1,'teal','blue','short','neutral','down')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('patron', '芸術家を金銭で支える後援者のイラスト。', f"""
{person(150,352,1.2,1,'violet','violet','give','bun','smile')}
<g transform="translate(300 250)">
  <path d="M-60-30h120v60h-120z" class="greenp o"/>
  <circle r="16" class="gold o"/>
</g>
{person(460,352,1.15,-1,'teal','gold','reach','short','smile')}
<g transform="translate(510 230)">
  <path d="M-40-50h80v100h-80z" class="paper"/>
  <path d="M-30 30l24-40 20 20 16-14v34z" class="coralp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 190h140"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('peak', '山のいちばん高い頂のイラスト。', f"""
<path d="M0 360l180-220 90 110 70-70 260 180z" class="greenp o"/>
<path d="M180 140l60 74H120z" fill="#fffdf6" class="o"/>
<g transform="translate(180 140)">
  <path d="M-4 0v-70h4l60 24-60 22" class="ink"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="180" cy="140" r="66"/></g>
<path d="M0 360h600" class="a"/>
""", ground=False)

add('peasant', '畑を耕す農民のイラスト。', f"""
<path d="M0 300h600v100H0z" fill="#e8ded2"/>
<g fill="none" stroke="#c9b79f" stroke-width="6">{''.join(f'<path d="M0 {320+i*26}h600"/>' for i in range(3))}</g>
{person(220,340,1.2,1,'gold','green','reach','cap','neutral')}
<g transform="translate(320 250) rotate(28)">
  <path d="M-8-40h16v120h-16z" fill="{TONES['gold'][2]}"/>
  <path d="M-40 80h80v20h-80z" fill="{MUTED}" class="o"/>
</g>
<g class="greens">{''.join(f'<path d="M{430+i*50} 330v-30"/>' for i in range(3))}</g>
<path d="M0 300h600" class="a"/>
""", ground=False)

add('peer', '目をこらしてじっと見つめるイラスト。', f"""
{face(220,210,90,'flat')}
<g fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round">
  <path d="M158 176q22-14 44 0M238 176q22-14 44 0"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M320 210h120"/></g>
<g transform="translate(500 210)">
  <circle r="46" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle r="20" class="coralp o"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('penalty', '違反に対して科される罰のイラスト。', f"""
{person(170,352,1.15,1,'blue','blue','stand','short','sad')}
<g transform="translate(400 210) rotate(10)">
  <path d="M-50-80h100v160h-100z" class="coral o"/>
</g>
<g transform="translate(400 340)">
  <path d="M-80-30h160v50h-160z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-56-12h112M-56 4h80"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M250 210h80"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('pension', '年をとってから定期に受け取る年金のイラスト。', f"""
{person(180,352,1.2,1,'violet','violet','reach','bun','smile')}
<g transform="translate(400 250)">
  <path d="M-70-30h140v60h-140z" class="greenp o"/>
  <circle r="16" class="gold o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M330 190h-70"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M330 320h-60M370 350h-60"/></g>
<g transform="translate(520 200)">
  <circle r="46" fill="#fffdf6" class="o"/>
  <path d="M0 0v-30M0 0l20 12" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <circle r="5" class="ink"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('perception', '目や耳から入って頭で受け取る知覚のイラスト。', f"""
<g transform="translate(400 210)">
  <path d="M-30 130v-40q-70-16-70-90 0-90 90-90 92 0 92 86 0 44-36 62v72z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="10" cy="-30" r="46" class="goldp o"/>
</g>
<g transform="translate(140 160)">
  <ellipse rx="60" ry="34" fill="#fffdf6" class="o"/>
  <circle r="20" class="blue o"/><circle r="9" class="ink"/>
</g>
<g transform="translate(140 300)">
  <path d="M-30 40v-20q-30-10-30-40 0-40 40-40t40 36q0 20-18 28-8 4-8 12v24z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)">
  <path d="M210 170h80M200 290q60-40 100-60"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('personnel', '名簿に並ぶ職員のイラスト。', f"""
<g transform="translate(190 210)">
  <path d="M-130-150h260v300h-260z" class="paper"/>
  <g>{''.join(f'<circle cx="-90" cy="{-100+i*60}" r="20" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>' for i in range(5))}</g>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-56 {-100+i*60}h150"/>' for i in range(5))}</g>
</g>
{person(400,356,0.85,1,'teal','blue','stand','short','neutral')}
{person(480,356,0.85,1,'gold','violet','stand','bob','neutral')}
{person(550,356,0.85,-1,'coral','blue','stand','bun','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
