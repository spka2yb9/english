"""第96回: 動詞・形容詞中心の45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'

add('abolish', '定めを取りやめて無くすイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-160-150h320v300h-320z" class="paper"/>
  <path d="M-120-110h240v40h-240z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-120 {-30+i*44}h240"/>' for i in range(4))}</g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="18" stroke-linecap="round"><path d="M-130-120L130 130"/></g>
</g>
{xx(490,120,1.1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('academic', '大学で学問に取り組むイラスト。', f"""
{building(400,300,0.85,'teal')}
{person(160,352,1.25,1,'violet','blue','carry','short','smile')}
<g transform="translate(160 196)">
  <path d="M-50-10L0-30l50 20L0 10z" class="ink"/>
</g>
<g transform="translate(230 320)">
  <path d="M-40 30h80v-24h-80z" class="tealp o"/>
  <path d="M-34 6h68v-24h-68z" class="coralp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('acquire', '努力して手に入れるイラスト。', f"""
{person(170,352,1.2,1,'teal','blue','reach','short','smile')}
<g transform="translate(400 230)">
  <path d="M-60-60h120v120h-120z" class="gold o"/>
  <path d="M-60-60h120v120h-120zM-60 0h120M0-60v120" class="a"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 250h80"/></g>
{ck(500,120,1)}
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('adopt', 'よいやり方を選んで取り入れるイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-56-70h112M-56-40h112M-56-10h80"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"><circle cx="30" cy="60" r="34"/><path d="M6 60h48"/></g>
</g>
<g transform="translate(420 230)">
  <path d="M-90-110h180v220h-180z" class="paper" opacity="0.5"/>
</g>
{ck(180,120,1)}
{xx(420,120,0.8,MUTED)}
<g class="a" marker-end="url(#ar)"><path d="M290 340h-80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('advance', '一歩ずつ前へ進むイラスト。', f"""
<g transform="translate(300 330)">
  <path d="M-230 0h110v-40h-110zM-120-40h110v-50h-110zM-10-90h110v-60H-10z" class="tealp o"/>
</g>
{person(130,326,0.85,1,'teal','blue','walk','short','smile')}
{person(240,286,0.85,1,'teal','blue','walk','short','smile')}
{person(350,236,0.95,1,'coral','blue','walk','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M150 220q120-100 300-130"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('advertising', '看板で商品を売り込む広告のイラスト。', f"""
<g transform="translate(300 180)">
  <path d="M-200-120h400v200h-400z" class="paper"/>
  <path d="M-160-90h150v140h-150z" class="coralp o"/>
  <circle cx="-85" cy="-20" r="46" class="coral o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="8"><path d="M20-60h140M20-20h140M20 20h100"/></g>
  <path d="M-140 80v40M140 80v40" class="a"/>
</g>
{person(180,376,0.7,1,'teal','blue','stand','short','smile')}
{person(420,376,0.7,-1,'gold','violet','stand','bob','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('ahead', '先頭に立って前を行くイラスト。', f"""
{person(430,352,1.15,1,'coral','blue','walk','short','smile')}
{person(260,354,1,1,'teal','blue','walk','bob','neutral')}
{person(140,354,1,1,'gold','violet','walk','short','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M100 150h420"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"><path d="M430 200v160"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('alcoholic', '酒の強さを示すイラスト。', f"""
<g transform="translate(210 250)">
  <path d="M-40 110V-20q0-30 20-40v-60h40v60q20 10 20 40v130z" fill="#fffdf6" class="o"/>
  <path d="M-40 110V20q40-14 80 0v90z" class="corald o"/>
  <path d="M-20-120h40v20h-40z" class="coral o"/>
</g>
<g transform="translate(400 280)">
  <path d="M-50-60h100l-30 60v40h-40v-40z" fill="#fffdf6" class="o"/>
  <path d="M-34-44h68l-20 40h-28z" class="corald o"/>
  <path d="M-40 80h80v16h-80z" class="o" fill="#fffdf6"/>
</g>
<g transform="translate(510 180)">
  <path d="M-30-60h60v130h-60z" fill="#fffdf6" class="o"/>
  <path d="M-30 10h60v60h-60z" class="coral o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-30 {50-i*30}h16"/>' for i in range(4))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('alongside', 'すぐ横に並んで付き添うイラスト。', f"""
<path d="M0 300h600v100H0z" class="bluep"/>
<path d="M0 280h600v20H0z" class="goldd o"/>
<g transform="translate(330 330)">
  <path d="M-160 0h320l-40 50h-240z" class="coral o"/>
  <path d="M-60-60h120v60h-120z" fill="#fffdf6" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><path d="M170 300h330"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M170 270v50M500 270v50"/></g>
""", ground=False)

add('arise', 'ふいに問題が持ち上がるイラスト。', f"""
{person(160,352,1.15,1,'teal','blue','walk','short','surprised')}
<g transform="translate(400 240)">
  <path d="M0-130l34 62 68-20-24 66 62 34-62 34 24 66-68-20-34 62-34-62-68 20 24-66-62-34 62-34-24-66 68 20z" class="coralp o"/>
  <g fill="{TONES['coral'][2]}"><rect x="-14" y="-60" width="28" height="76" rx="14"/><circle cy="44" r="16"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M400 380v-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('authorize', '判を押して許しを与えるイラスト。', f"""
<g transform="translate(230 180)">
  <path d="M-70-40h140v60h-140z" class="violet o"/>
  <path d="M-30-90h60v50h-60z" class="violetd o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 250v40"/></g>
<g transform="translate(400 300)">
  <path d="M-120-70h240v130h-240z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-90-40h180M-90-14h140"/></g>
  <g fill="none" stroke="{GRN}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"><path d="M20 20l20 24 46-54"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('barely', 'ぎりぎりで届くか届かないかのイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-160-140h320v280h-320z" fill="#fffdf6" class="o"/>
  <path d="M-160 110h320v30h-320z" class="teal o"/>
  <path d="M-180 100h360v10h-360z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M520 340V360"/></g>
{ck(500,200,0.8)}
<path d="M60 390h480" class="a"/>
""", ground=True, arrow=True)

add('bargain', '値引きされたお買い得品のイラスト。', f"""
<g transform="translate(260 230)">
  <path d="M-80-110h160v220h-160z" class="tealp o"/>
</g>
<g transform="translate(430 200)">
  <path d="M-70-60h90l50 50-90 90-50-50z" class="goldp o"/>
  <circle cx="-40" cy="-30" r="10" class="goldd o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"><path d="M-40 10l70 70"/></g>
</g>
{person(120,352,1.05,1,'coral','blue','up','bob','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('basis', '上に載るものを支える土台のイラスト。', f"""
<g transform="translate(300 310)">
  <path d="M-220-40h440v60h-440z" class="teal o"/>
  <path d="M-120-110h240v70h-240z" class="tealp o"/>
  <path d="M-60-170h120v60H-60z" class="tealp o"/>
</g>
<g transform="translate(470 350)">
  <circle r="40" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M30 30l30 30" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('beneath', '下側にあることを示すイラスト。', f"""
<g transform="translate(300 180)">
  <path d="M-160-60h320v60h-320z" class="teal o"/>
</g>
<g transform="translate(300 300)">
  <path d="M-90-40h180v80h-180z" class="coralp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 200v60"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><rect x="196" y="250" width="208" height="104" rx="14"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('beside', 'すぐ横に置かれていることを示すイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-180-90h160v180h-160z" class="teal o"/>
  <path d="M20-60h160v150H20z" class="coralp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M300 130h-30M300 130h30"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M280 110v40M320 110v40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('careless', 'よく見ないでこぼしてしまうイラスト。', f"""
{person(180,352,1.2,1,'teal','blue','carry','short','neutral')}
<g transform="translate(280 250) rotate(40)">
  <path d="M-34-40h68l-8 70h-52z" fill="#fffdf6" class="o"/>
  <path d="M-30-10h60l-6 40h-48z" class="bluep o"/>
</g>
<g class="bluep o"><path d="M330 300q40 40 20 70-40 10-40-30 0-24 20-40z"/></g>
<g class="bluep o"><ellipse cx="350" cy="378" rx="60" ry="16"/></g>
{xx(470,180,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('chair', '会議の議長をつとめるイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-220-30h440v20h-440z" class="goldd o"/>
</g>
{person(300,290,1.1,1,'violet','blue','point','bun','neutral')}
{sit(140,356,0.8,1,'teal','blue','short','neutral','lap')}
{sit(250,356,0.8,1,'coral','gold','bob','neutral','lap')}
{sit(360,356,0.8,-1,'gold','violet','short','neutral','lap')}
{sit(470,356,0.8,-1,'green','blue','bun','neutral','lap')}
<g transform="translate(370 290) rotate(-24)">
  <path d="M-40-12h36v24h-36z" class="goldd o"/>
  <path d="M-8-7h70v14H-8z" class="gold o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('chemistry', 'フラスコで物質を調べる化学のイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-26-90h52v40l50 90q8 16-10 16h-132q-18 0-10-16l50-90z" fill="#fffdf6" class="o"/>
  <path d="M-46 10l-16 30q-8 16 10 16h104q18 0 10-16l-16-30z" class="teal o"/>
  <circle cx="-10" cy="-16" r="7" class="tealp o"/>
</g>
<g transform="translate(430 200)">
  <circle cx="-60" cy="0" r="34" class="coralp o"/>
  <circle cx="60" cy="0" r="34" class="coralp o"/>
  <circle cx="0" cy="60" r="34" class="goldp o"/>
  <g fill="none" stroke="{INK}" stroke-width="5"><path d="M-30 10l60 40M30 10l-60 40M-26 0h52"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('colony', '本国の旗が立つ植民地の町のイラスト。', f"""
<g transform="translate(200 300)">
  <path d="M-60 0v-56h120V0z" fill="#fffdf6" class="o"/>
  <path d="M-72-56L0-96l72 40z" class="coral o"/>
</g>
<g transform="translate(330 300)">
  <path d="M-50 0v-46h100V0z" fill="#fffdf6" class="o"/>
  <path d="M-60-46L0-80l60 34z" class="coral o"/>
</g>
<g transform="translate(470 260)">
  <path d="M-6 100V-90" class="a"/>
  <path d="M-6-90h90v60H-6z" class="teal o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><path d="M100 200h440"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('comedy', '舞台の笑いに沸くイラスト。', f"""
<g transform="translate(300 160)">
  <path d="M-240-100h480v40h-480z" class="corald o"/>
  <path d="M-240-60q30 140 0 220h90q-24-110 0-220z" class="coral o"/>
  <path d="M240-60q-30 140 0 220h-90q24-110 0-220z" class="coral o"/>
</g>
<g transform="translate(300 200)">
  <circle r="60" class="goldp o"/>
  <g fill="{INK}"><path d="M-36-20q20-14 36 0-18 8-36 0zM0-20q20-14 36 0-18 8-36 0z"/></g>
  <path d="M-30 14q30 40 60 0z" fill="{INK}"/>
</g>
{person(140,376,0.7,1,'teal','blue','up','short','smile')}
{person(470,376,0.7,-1,'gold','violet','up','bob','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('commission', '委員が集まって依頼を受けるイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-230-30h460v20h-460z" class="goldd o"/>
</g>
{sit(130,356,0.8,1,'violet','violet','bun','neutral','lap')}
{sit(250,356,0.8,1,'teal','blue','short','neutral','lap')}
{sit(370,356,0.8,-1,'coral','gold','bob','neutral','lap')}
{sit(490,356,0.8,-1,'green','blue','short','neutral','lap')}
<g transform="translate(300 180)">
  <path d="M-90-70h180v140h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-56-40h112M-56-14h112M-56 12h80"/></g>
  <circle cx="46" cy="40" r="20" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('conclude', '筋道の末に結論を出すイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-230-50h110v100h-110z" class="tealp o"/>
  <path d="M-60-50h110v100H-60z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 210h40M350 210h40"/></g>
<g transform="translate(480 210)">
  <path d="M-80-70h160v140h-160z" class="teal o"/>
  <circle r="34" fill="none" stroke="#fffdf6" stroke-width="8"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('conflict', '両者がぶつかり合う対立のイラスト。', f"""
<g transform="translate(160 250)">
  <path d="M-90 60q0-110 90-110t90 110z" class="tealp o"/>
  <path d="M-20-30v-70h4l50 18-50 18" class="ink"/>
</g>
<g transform="translate(450 250)">
  <path d="M-90 60q0-110 90-110t90 110z" class="coralp o"/>
  <path d="M-20-30v-70h4l50 18-50 18" class="ink"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linejoin="round">
  <path d="M280 110l40 60-40 60 40 60"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('consolidate', '小さなものをまとめて一つに固めるイラスト。', f"""
<g transform="translate(160 250)">
  <path d="M-70-70h60v60h-60zM10-70h60v60H10zM-70 10h60v60h-60zM10 10h60v60H10z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 250h60"/></g>
<g transform="translate(460 250)">
  <path d="M-80-80h160v160h-160z" class="teal o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('construct', 'クレーンで組み上げて建てるイラスト。', f"""
<g transform="translate(400 300)">
  <path d="M-110 60v-140h220V60z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="7"><path d="M-110-80h220M-110 0h220M-40-140v200M40-140v200"/></g>
  <path d="M-110-140h220v60h-220z" class="tealp o"/>
</g>
<g transform="translate(150 240)">
  <path d="M-10-100h20v220h-20z" class="ink"/>
  <path d="M-10-100h200v16h-200z" class="ink"/>
  <path d="M160-84v60" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
{box(310,170,80,50,16,'gold')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('consume', '使って減っていく消費のイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-70-100h140v200h-140z" fill="#fffdf6" class="o"/>
  <path d="M-70-60h140v160h-140z" class="teal o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 250h60"/></g>
<g transform="translate(470 250)">
  <path d="M-70-100h140v200h-140z" fill="#fffdf6" class="o"/>
  <path d="M-70 60h140v40h-140z" class="teal o"/>
</g>
{person(300,376,0.6,1,'coral','blue','hold','short','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('contrast', '明と暗を並べて際立たせる対比のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-230-140h230v280h-230z" fill="#fdf6e3" class="o"/>
  <path d="M0-140h230v280H0z" fill="#2c3244" class="o"/>
  <circle cx="-115" cy="0" r="60" fill="#2c3244"/>
  <circle cx="115" cy="0" r="60" fill="#fdf6e3"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M270 380h-60M330 380h60"/></g>
""", ground=False, arrow=True)

add('cultural', 'その土地に伝わる衣装と楽器のイラスト。', f"""
<g transform="translate(160 250)">
  <path d="M-60 110l20-120q6-40 40-40t40 40l20 120z" class="coral o"/>
  <path d="M-30-60h60v20h-60z" class="corald o"/>
</g>
<g transform="translate(350 260)">
  <ellipse cy="60" rx="60" ry="34" class="goldd o"/>
  <path d="M-60 60v-40q0-30 60-30t60 30v40" class="gold o"/>
  <g fill="none" stroke="#fffdf6" stroke-width="4">{''.join(f'<path d="M{-40+i*26} 4v60"/>' for i in range(4))}</g>
</g>
<g transform="translate(500 230)">
  <path d="M-50-60q50-40 100 0 0 110-50 110T-50-60z" class="goldp o"/>
  <g fill="{INK}"><path d="M-26-30q20-14 34 0-16 10-34 0zM16-30q20-14 34 0-16 10-34 0z"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('data', '表に並んだ数値から図を作るイラスト。', f"""
<g transform="translate(180 210)">
  <path d="M-130-150h260v300h-260z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M-130 {-90+i*50}h260"/>' for i in range(5))}
    {''.join(f'<path d="M{-44+c*88} -150v300"/>' for c in range(2))}
  </g>
  <g fill="{INK}">{''.join(f'<rect x="{-110+c*88}" y="{-108+r*50}" width="40" height="10"/>' for r in range(5) for c in range(3))}</g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M330 210h40"/></g>
<g transform="translate(470 220)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g class="teal">{''.join(f'<rect x="{-70+i*38}" y="{60-(20+i*28)}" width="26" height="{20+i*28}"/>' for i in range(4))}</g>
  <path d="M-80 60h160" class="a"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('declare', '高くかかげて言い渡すイラスト。', f"""
{person(220,352,1.3,1,'violet','blue','up','short','neutral')}
<g transform="translate(400 170) rotate(10)">
  <path d="M-100-60q-24 0-24 24t24 24h200q24 0 24-24t-24-24z" class="goldp o"/>
  <path d="M-100-12h200v120h-200z" fill="#fdf6e3" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-70 20h140M-70 50h110M-70 80h140"/></g>
</g>
<g transform="translate(220 330)">
  <path d="M-50-30h100l14 50h-128z" class="goldd o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('define', '意味の範囲をはっきり区切るイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-160-100h120M-160 90h280M-160 120h200"/></g>
  <path d="M-160-60h250v120h-250z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5"><path d="M-130-20h190M-130 20h150"/></g>
</g>
""", ground=False)

add('deteriorate', '時がたつほど悪くなるイラスト。', f"""
<g transform="translate(150 250)">
  <circle r="60" class="coral o"/>
  <path d="M0-60q-14-24 10-34 14 20 4 34z" class="greenp o"/>
</g>
<g transform="translate(300 250)">
  <circle r="60" class="corald o"/>
  <path d="M-30-20q20 20 40 0" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(460 250)">
  <circle r="60" fill="#8a7a63" class="o"/>
  <g fill="#5e4a3c"><circle cx="-20" cy="-10" r="12"/><circle cx="20" cy="16" r="14"/><circle cx="14" cy="-24" r="9"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M60 360h480"/></g>
""", ground=False, arrow=True)

add('discussion', '意見を出し合って話し合うイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-200-30h400v20h-400z" class="goldd o"/>
</g>
{sit(170,356,0.95,1,'teal','blue','short','neutral','lap')}
{sit(300,356,0.95,1,'coral','gold','bob','neutral','lap')}
{sit(430,356,0.95,-1,'gold','violet','short','neutral','lap')}
<g transform="translate(160 180)">
  <path d="M-60-36h120v60h-120zM-30 24l-10 24 30-24z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><path d="M-34-16h68M-34 2h44"/></g>
</g>
<g transform="translate(430 160)">
  <path d="M-60-36h120v60h-120zM30 24l10 24-30-24z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4"><path d="M-34-16h68M-10 2h44"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('dispute', '内容に異議を唱えて言い争うイラスト。', f"""
{person(140,352,1.15,1,'teal','blue','point','short','neutral')}
{person(460,352,1.15,-1,'coral','gold','point','bob','neutral')}
<g transform="translate(300 230)">
  <path d="M-80-90h160v180h-160z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-50-50h100M-50-20h100M-50 10h70"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linejoin="round"><path d="M300 120l30-40-30-40"/></g>
<g class="a" marker-end="url(#ar)"><path d="M230 300h-40M370 300h40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('downwards', '下向きに落ちていくイラスト。', f"""
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="20" stroke-linecap="round" marker-end="url(#ar)"><path d="M300 80v200"/></g>
<g class="tealp o"><circle cx="160" cy="140" r="24"/><circle cx="440" cy="180" r="20"/><circle cx="200" cy="280" r="18"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M160 100v30M440 140v30M200 240v30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('elsewhere', 'ここではない別の場所にいるイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-100-100h200v200h-200z" fill="#fffdf6" class="o"/>
</g>
{xx(170,250,1.2,MUTED)}
<g transform="translate(440 250)">
  <path d="M-100-100h200v200h-200z" fill="#fffdf6" class="o"/>
</g>
{person(440,340,1,1,'teal','blue','stand','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M280 140h80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('empower', '力と権限を与えて強くするイラスト。', f"""
{person(170,352,1.1,1,'violet','violet','give','bun','smile')}
{person(450,346,1.25,-1,'teal','blue','up','short','smile')}
<g transform="translate(300 250)">
  <path d="M-40-30h80v60h-80z" class="gold o"/>
  <path d="M-10-60h20v30h-20z" class="goldd o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 170h140"/></g>
<g class="golds"><path d="M450 180v-24M370 210l-20-20M530 210l20-20"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('enable', 'スイッチを入れて通れるようにするイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-230-30h180v60h-180zM50-30h180v60H50z" fill="{MUTED}" class="o"/>
  <path d="M-50-40h100v80h-100z" class="teal o"/>
  <circle cx="20" cy="0" r="24" fill="#fffdf6" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M80 150h440"/></g>
{ck(300,360,0.9)}
""", ground=False, arrow=True)

add('entitle', '受け取る権利をしるした券のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-90h380v180h-380z" class="goldp o"/>
  <path d="M-190-90h380v180h-380zM60-90v180" class="a"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-150-40h180M-150 0h140M-150 40h180"/></g>
  <g fill="none" stroke="{GRN}" stroke-width="9"><path d="M100-10l16 18 34-40"/></g>
</g>
{hand(120,340,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('escalate', '小さな火が段を上るほど大きくなるイラスト。', f"""
<g transform="translate(300 330)">
  <path d="M-230 0h110v-40h-110zM-120-40h110v-60h-110zM-10-100h110v-80H-10z" class="tealp o"/>
</g>
{flame(170,290,0.4)}
{flame(290,250,0.7)}
{flame(410,200,1.1)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M150 220q140-120 320-140"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('evolve', '形を変えながら進化していくイラスト。', f"""
<g transform="translate(140 290)">
  <ellipse rx="40" ry="26" class="greenp o"/>
  <path d="M-40 0q-40 8-46 30 34 6 46-16z" class="greenp o"/>
</g>
<g transform="translate(310 280)">
  <ellipse rx="50" ry="32" class="green o"/>
  <circle cx="42" cy="-24" r="20" class="green o"/>
  <path d="M-30 32v26M14 34v24" fill="none" stroke="{TONES['green'][2]}" stroke-width="8" stroke-linecap="round"/>
</g>
{person(480,352,0.95,1,'teal','blue','walk','short','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M60 380h480"/></g>
""", ground=True, arrow=True)

add('farming', '畑を耕して作物を育てる農業のイラスト。', f"""
<path d="M0 280h600v120H0z" fill="#e8ded2"/>
<g fill="none" stroke="#c9b79f" stroke-width="6">{''.join(f'<path d="M0 {320+i*30}h600"/>' for i in range(3))}</g>
<g class="greens">{''.join(f'<path d="M{100+i*60} 300v-40"/>' for i in range(4))}</g>
<g class="greenp o">{''.join(f'<circle cx="{100+i*60}" cy="252" r="16"/>' for i in range(4))}</g>
<g transform="translate(440 250)">
  <path d="M-70 30h140v30h-140z" class="coral o"/>
  <path d="M-30-30h70v60h-70z" class="coral o"/>
  <g fill="{INK}"><circle cx="-40" cy="66" r="26"/><circle cx="50" cy="70" r="20"/></g>
</g>
<path d="M0 280h600" class="a"/>
""", ground=False)

add('female', '女性であることを示す記号のイラスト。', f"""
{person(180,352,1.35,1,'coral','violet','stand','bun','smile')}
<g transform="translate(430 200)">
  <circle r="80" fill="none" stroke="{TONES['coral'][0]}" stroke-width="20"/>
  <path d="M0 80v100M-50 140h100" fill="none" stroke="{TONES['coral'][0]}" stroke-width="20" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('firm', '看板を出した会社の事務所のイラスト。', f"""
{tower(300,320,0.9,'teal',5)}
<g transform="translate(300 120)">
  <path d="M-120-40h240v60h-240z" class="coral o"/>
  <g fill="#fffdf6"><rect x="-90" y="-22" width="180" height="24" rx="12"/></g>
</g>
{person(130,356,0.8,1,'violet','blue','walk','short','neutral')}
{person(480,356,0.8,-1,'gold','violet','walk','bob','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
