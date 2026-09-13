"""第95回: tr〜wi の名詞を中心に45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'
def star(x,y,r=30,cls='gold'):
    import math
    pts=[]
    for i in range(10):
        rr = r if i%2==0 else r*0.45
        a = math.radians(-90+i*36)
        pts.append(f'{x+rr*math.cos(a):.0f} {y+rr*math.sin(a):.0f}')
    return f'<path d="M{"L".join(pts)}z" class="{cls} o"/>'
def note(x,y,s=1,cls='ink'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 30q-14 0-14-12t14-12q8 0 12 5v-45l30-9v14l-20 6v40q0 13-22 13z" '
            f'fill="{INK if cls=="ink" else TONES[cls][0]}"/></g>')

add('trio', '三人ひと組で演じるイラスト。', f"""
{person(160,352,1.1,1,'teal','blue','up','short','smile')}
{person(300,352,1.1,1,'coral','gold','up','bob','smile')}
{person(440,352,1.1,1,'gold','violet','up','bun','smile')}
{note(120,160,1,'teal')}
{note(290,140,1,'coral')}
{note(460,160,1,'gold')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="12 10"><rect x="100" y="200" width="410" height="170" rx="22"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('triumph', '大きな勝利にわき立つイラスト。', f"""
{person(300,282,1.3,1,'coral','blue','up','short','smile')}
<g transform="translate(300 350)">
  <path d="M-70-70h140v70h-140z" class="gold o"/>
  <path d="M-190-30h120v30h-120zM70-14h120v14H70z" class="goldp o"/>
</g>
{star(180,150,26,'gold')}
{star(420,150,26,'gold')}
<g class="golds"><path d="M300 120v-26M220 190l-20-20M380 190l20-20"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('trustee', '人から預かって管理する受託者のイラスト。', f"""
{person(150,352,1.15,1,'teal','blue','give','short','neutral')}
{person(450,352,1.15,-1,'violet','violet','reach','bun','neutral')}
{box(300,250,120,90,24,'gold')}
<g class="a" marker-end="url(#ar)"><path d="M230 160h140"/></g>
<g transform="translate(300 370)">
  <path d="M-40-16h80v32h-80z" class="paper"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('tsunami', '岸に迫る巨大な波のイラスト。', f"""
<path d="M0 400V200q140-120 260-20 40 34 20 80t-90 40q-40-4-40-40t40-40q30 0 40 26" fill="{TONES['blue'][1]}" stroke="{INK}" stroke-width="4"/>
<path d="M0 320h600v80H0z" class="bluep"/>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"><path d="M320 360q40-16 80 0t80 0"/></g>
<g transform="translate(500 300)">
  <path d="M-50 0v-60h100V0z" fill="#fffdf6" class="o"/>
  <path d="M-62-60L0-104l62 44z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M330 140h100"/></g>
""", ground=False, arrow=True)

add('tune', '短い曲を奏でるイラスト。', f"""
<g transform="translate(220 280)">
  <path d="M-110-40h220v100h-220z" class="goldd o"/>
  <path d="M-110-40h220v-30h-220z" class="gold o"/>
  <g fill="none" stroke="#fffdf6" stroke-width="4">{''.join(f'<path d="M{-90+i*30} -30v90"/>' for i in range(7))}</g>
</g>
{note(380,190,1.3,'coral')}
{note(470,150,1.3,'coral')}
{note(530,200,1.3,'coral')}
<g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M340 240h240M340 270h240"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('uncertainty', 'どちらになるか分からない不確かさのイラスト。', f"""
{person(300,352,1.2,1,'teal','blue','think','short','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)">
  <path d="M240 290L120 210M360 290l120-80"/>
</g>
<g opacity="0.4"><circle cx="110" cy="170" r="40" class="tealp o"/></g>
<g opacity="0.4"><path d="M450 130h80v80h-80z" class="coralp o"/></g>
<g transform="translate(300 130)">
  <path d="M-24-30q0-28 26-28t26 26q0 20-26 28v12" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"/>
  <circle cy="36" r="7" class="coral"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('undergraduate', 'まだ卒業していない学部生のイラスト。', f"""
{building(430,310,0.8,'teal')}
{person(180,352,1.25,1,'teal','blue','carry','short','smile')}
<g transform="translate(250 300)">
  <path d="M-40 30h80v-24h-80z" class="tealp o"/>
  <path d="M-34 6h68v-24h-68z" class="coralp o"/>
</g>
<g transform="translate(180 200)">
  <path d="M-50-10L0-30l50 20L0 10z" class="ink"/>
</g>
{xx(250,180,0.7,MUTED)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('unity', 'ばらばらの片が集まってひとつになる団結のイラスト。', f"""
<g transform="translate(150 230)">
  <path d="M-60-60h50v50h-50z" class="tealp o" transform="rotate(-12)"/>
  <path d="M10-50h50v50H10z" class="tealp o" transform="rotate(14)"/>
  <path d="M-50 20h50v50h-50z" class="tealp o" transform="rotate(8)"/>
  <path d="M20 20h50v50H20z" class="tealp o" transform="rotate(-10)"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 230h60"/></g>
<g transform="translate(450 230)">
  <path d="M-70-70h140v140h-140z" class="teal o"/>
  <path d="M-70 0h140M0-70v140" class="a"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('universe', '星と銀河の広がる宇宙のイラスト。', f"""
<path d="M0 0h600v400H0z" fill="#161f33"/>
<g fill="#fffdf6">{''.join(f'<circle cx="{30+i*43}" cy="{40+(i*67)%320}" r="{2+(i%3)}"/>' for i in range(14))}</g>
<g transform="translate(200 220)">
  <ellipse rx="140" ry="50" fill="none" stroke="#8b98a6" stroke-width="4" transform="rotate(-20)"/>
  <ellipse rx="90" ry="32" fill="#4e86c6" opacity="0.7" transform="rotate(-20)"/>
  <circle r="26" fill="#fffdf6"/>
</g>
<circle cx="470" cy="130" r="40" fill="{TONES['coral'][0]}"/>
<ellipse cx="470" cy="130" rx="70" ry="16" fill="none" stroke="{TONES['gold'][0]}" stroke-width="6" transform="rotate(-18 470 130)"/>
<circle cx="440" cy="320" r="22" fill="{TONES['green'][0]}"/>
""", ground=False)

add('utility', '水道と電気をまかなう公共の設備のイラスト。', f"""
<g transform="translate(180 240)">
  <path d="M-30-90h60v60h-60z" fill="{MUTED}" class="o"/>
  <path d="M-10-30h20v100h-20z" fill="{MUTED}" class="o"/>
  <path d="M-60-110h120v20h-120z" fill="{MUTED}" class="o"/>
</g>
{drop(180,330,1.6,'blue')}
<g transform="translate(430 240)">
  <path d="M-50-60h100v90h-100z" class="goldp o"/>
  <path d="M-24 30h16v50h-16zM8 30h16v50H8z" fill="{TONES['gold'][2]}"/>
  <g fill="{INK}"><circle cx="-20" cy="-20" r="9"/><circle cx="20" cy="-20" r="9"/></g>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round"><path d="M430 340l-20-30h30l-16-24"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('variable', 'つまみの位置で値が変わるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-220-20h440v40h-440z" fill="#dfe6ea" class="o"/>
  <path d="M-220-20h130v40h-130z" class="teal o"/>
  <path d="M-110-50h40v100h-40z" class="teald o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M{-200+i*55} 40v16"/>' for i in range(9))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M200 320h-80M400 320h80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('vein', '腕にすじが浮かぶ静脈のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-60q140-40 260 0 90 30 140 90H-200z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="8" stroke-linecap="round">
    <path d="M-160-20q80-20 150 10t120 60"/>
    <path d="M-60 10q40 20 60 60M60 20q20 30 20 60"/>
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M470 130l-60 60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('venue', '催しが開かれる会場のイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-220 70v-140h440v140z" fill="#fffdf6" class="o"/>
  <path d="M-240-70h480l-40-40h-400z" class="teal o"/>
  <path d="M-40 70v-70h80v70z" class="teald o"/>
  <path d="M-170-40h90v50h-90zM80-40h90v50H80z" class="tealp o"/>
</g>
<g transform="translate(300 120)">
  <path d="M-150-40h300v60h-300z" class="coral o"/>
  <g fill="#fffdf6"><rect x="-110" y="-22" width="220" height="24" rx="12"/></g>
</g>
{person(120,376,0.7,1,'gold','blue','walk','short','smile')}
{person(490,376,0.7,-1,'violet','gold','walk','bob','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('verdict', '封を開けて読み上げる評決のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-140-100h280v200h-280z" fill="#fffdf6" class="o"/>
  <path d="M-140-100L0 20l140-120" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-90-60h180v120h-180z" class="paper"/>
  <g fill="none" stroke="{GRN}" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"><path d="M-44 0l24 28 56-64"/></g>
</g>
{person(140,356,0.85,1,'violet','violet','point','bun','neutral')}
{person(470,356,0.85,-1,'teal','blue','stand','short','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('verse', '行を区切って書かれた詩の一節のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-190-150h380v300h-380z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">
    <path d="M-140-100h200M-140-70h240M-140-40h180"/>
  </g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5">
    <path d="M-140 20h220M-140 50h180M-140 80h240M-140 110h160"/>
  </g>
  <path d="M-160-10h320" fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="8 8"/>
</g>
""", ground=False)

add('veteran', '長く勤めを果たした退役軍人のイラスト。', f"""
{person(300,352,1.3,1,'green','green','stand','short','neutral')}
<g transform="translate(260 250)">
  <path d="M-24-20h20v40h-20zM6-20h20v40H6z" class="coral o"/>
  <circle cx="-14" cy="34" r="14" class="gold o"/>
  <circle cx="16" cy="34" r="14" class="goldd o"/>
</g>
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="8" stroke-linecap="round"><path d="M400 250v130"/></g>
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="8" stroke-linecap="round"><path d="M400 250q-24 0-24 16"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('vice', '断ち切れない悪い癖のイラスト。', f"""
{person(200,352,1.2,1,'blue','blue','reach','short','sad')}
<g transform="translate(400 270)">
  <path d="M-60-40h120v80h-120z" class="corald o"/>
  <path d="M-30-70h60v30h-60z" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="8"><circle cx="300" cy="300" r="18"/><circle cx="336" cy="308" r="18"/></g>
{xx(400,150,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('victory', '頂に旗を立てた勝利のイラスト。', f"""
<path d="M0 380l200-230 100 120 80-80 220 190z" class="greenp o"/>
<g transform="translate(200 150)">
  <path d="M-6 0v-100" class="a"/>
  <path d="M-6-100h90l-18 26 18 26H-6z" class="coral o"/>
</g>
{person(280,300,0.9,1,'gold','blue','up','short','smile')}
<g class="golds"><path d="M200 20v-14M120 60l-16-16M280 60l16-16"/></g>
<path d="M0 380h600" class="a"/>
""", ground=False)

add('viewpoint', '同じものを違う側から見るイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-60-60h120v120h-120z" class="tealp o"/>
  <path d="M60-60l50-30v120l-50 30z" class="teal o"/>
  <path d="M-60-60l50-30h120l-50 30z" class="tealp o"/>
</g>
{person(110,352,1,1,'coral','blue','point','short','neutral')}
{person(500,352,1,-1,'violet','gold','point','bob','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M170 250h60M440 250h-60"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('villager', '小さな村に住む村人のイラスト。', f"""
<g transform="translate(420 300)">
  <path d="M-60 0v-56h120V0z" fill="#fffdf6" class="o"/>
  <path d="M-72-56L0-96l72 40z" class="coral o"/>
</g>
<g transform="translate(530 300)">
  <path d="M-46 0v-46h92V0z" fill="#fffdf6" class="o"/>
  <path d="M-56-46L0-80l56 34z" class="teal o"/>
</g>
{tree(320,320,0.7)}
{person(160,352,1.25,1,'gold','green','stand','bun','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('violation', '決まりを踏み越える違反のイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-56 {-60+i*44}h112"/>' for i in range(4))}</g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="16 12"><path d="M360 100v280"/></g>
{person(450,352,1.15,-1,'coral','blue','walk','short','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M420 290h-90"/></g>
{xx(360,140,1)}
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('violence', '力にまかせて傷つける暴力のイラスト。', f"""
<g transform="translate(230 240)">
  <rect x="-80" y="-40" width="160" height="110" rx="32" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <g fill="none" stroke="{SKINL}" stroke-width="2.5"><path d="M-30-40v110M20-40v110"/></g>
  <path d="M-80 10q-36-10-36-40 0-26 30-26" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M340 200l40-30M350 250h50M340 300l40 30"/>
</g>
{xx(470,240,1.3)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('virtue', '人のためになる行いのよさのイラスト。', f"""
{person(200,352,1.2,1,'teal','blue','give','short','smile')}
<g transform="translate(340 270)">
  <path d="M-50-30h100v60h-100z" class="coralp o"/>
  <path d="M0-30q-30-30-40-6 20 12 40 6zM0-30q30-30 40-6-20 12-40 6z" class="coral o"/>
</g>
{person(470,352,1.1,-1,'gold','violet','reach','bob','smile')}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="8"><ellipse cx="200" cy="196" rx="50" ry="14"/></g>
{ck(340,150,1)}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('visa', '入国の許しが押されたビザのイラスト。', f"""
<g transform="translate(280 220)">
  <path d="M-150-150h300v300h-300z" class="teal o"/>
  <path d="M-130-130h260v260h-260z" fill="#fffdf6" class="o"/>
  <circle cx="-40" cy="-50" r="40" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M-80-50h80M-40-90v80" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-100 20h200M-100 50h160"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" transform="rotate(-16 60 80)">
    <rect x="20" y="50" width="110" height="60" rx="8"/>
    <path d="M40 80h70"/>
  </g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('vision', 'これから目指す将来像を思い描くイラスト。', f"""
{person(150,352,1.2,1,'teal','blue','point','short','smile')}
<g transform="translate(410 210)">
  <path d="M-160-120h320v240h-320z" fill="#fffdf6" class="o"/>
  <path d="M-160 120v-70l90-70 70 60 60-50 100 60v70z" class="greenp o"/>
  <circle cx="70" cy="-60" r="30" class="goldp o"/>
</g>
{tower(390,320,0.5,'teal',4)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M230 240h30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('vitamin', '野菜や果物に含まれるビタミンのイラスト。', f"""
<g transform="translate(180 260)">
  <circle r="70" class="gold o"/>
  <path d="M0-70q-14-24 10-34 14 20 4 34z" class="greenp o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="3"><circle r="46"/></g>
</g>
<g transform="translate(340 300)">
  <path d="M0 30V-40" class="greens"/>
  <path d="M0-20q-40-6-46-40 38-6 46 40z" class="greenp o"/>
  <path d="M0-40q40-6 46-40-38-6-46 40z" class="greenp o"/>
</g>
<g transform="translate(470 260) rotate(-20)">
  <path d="M-70-26h70v52h-70q-26 0-26-26t26-26z" class="coral o"/>
  <path d="M0-26h44q26 0 26 26t-26 26H0z" fill="#fffdf6" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M400 200h40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('volume', 'つまみで音の大きさを変えるイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-50-40h50v80h-50z" class="ink"/>
  <path d="M0-70l70-40v220L0 40z" class="teal o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M300 200q26 30 0 60M340 170q56 60 0 120M380 140q86 90 0 180"/>
</g>
<g transform="translate(500 300)">
  <path d="M-70-16h140v32h-140z" fill="#dfe6ea" class="o"/>
  <path d="M-70-16h90v32h-90z" class="coral o"/>
  <path d="M0-40h40v80H0z" class="corald o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('voting', '票を箱に入れる投票のイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-120-40h240v130h-240z" class="tealp o"/>
  <path d="M-70-50h140v14h-140z" class="ink"/>
</g>
<g transform="translate(300 150)">
  <path d="M-60-46h120v70h-120z" class="paper"/>
  <g fill="none" stroke="{GRN}" stroke-width="8"><path d="M-30-16l14 16 28-32"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 200v40"/></g>
{person(130,356,0.9,1,'coral','blue','give','short','smile')}
{person(480,356,0.9,-1,'gold','violet','give','bob','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('wage', '働いた時間に応じて払われる賃金のイラスト。', f"""
<g transform="translate(180 220)">
  <circle r="80" fill="#fffdf6" class="o"/>
  <path d="M0 0v-56M0 0l32 20" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <circle r="8" class="ink"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 220h50"/></g>
<g transform="translate(450 240)">
  <path d="M-90-60h180v120h-180z" class="goldp o"/>
  <path d="M-90-60L0 10l90-70" fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"/>
  <g class="greenp o"><rect x="-50" y="-30" width="100" height="40"/></g>
  <circle r="12" class="gold o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('ward', 'ベッドが並ぶ病棟のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-250-160h500v320h-500z" fill="#fffdf6" class="o"/>
  <path d="M-250 60h500" class="a"/>
</g>
<g transform="translate(180 300)">
  <path d="M-90 20h180v14h-180z" class="ink"/>
  <path d="M-90-10h180v30h-180z" fill="#fffdf6" class="o"/>
  <path d="M-90-40h40v30h-40z" class="bluep o"/>
  <path d="M-50-10h130v-16q0-10-12-10H-38q-12 0-12 10z" class="tealp o"/>
</g>
<g transform="translate(430 300)">
  <path d="M-90 20h180v14h-180z" class="ink"/>
  <path d="M-90-10h180v30h-180z" fill="#fffdf6" class="o"/>
  <path d="M-90-40h40v30h-40z" class="bluep o"/>
  <path d="M-50-10h130v-16q0-10-12-10H-38q-12 0-12 10z" class="tealp o"/>
</g>
<g transform="translate(300 130)">
  <path d="M-14-30h28v22h22v28h-22v22h-28v-22h-22v-28h22z" class="coral o"/>
</g>
<path d="M50 340h500" class="a"/>
""", ground=False)

add('warehouse', 'トラックが着けつける倉庫のイラスト。', f"""
<g transform="translate(360 260)">
  <path d="M-180 100v-160h360v160z" fill="#fffdf6" class="o"/>
  <path d="M-200-60L0-150l200 90z" class="teal o"/>
  <path d="M-80 100v-110h160v110z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4">{''.join(f'<path d="M-80 {-80+i*34}h160"/>' for i in range(4))}</g>
</g>
<g transform="translate(120 320)">
  <path d="M-60-70h120v70h-120z" class="coral o"/>
  <g fill="{INK}"><circle cx="-30" cy="6" r="20"/><circle cx="30" cy="6" r="20"/></g>
  <g fill="#fffdf6" class="o"><rect x="20" y="-60" width="36" height="26"/></g>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('warfare', '国と国がぶつかり合う戦いのイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-260-140h230v280h-230z" class="tealp o"/>
  <path d="M-10-140h270v280h-270z" class="coralp o"/>
  <path d="M-20-140v280" fill="none" stroke="{INK}" stroke-width="6" stroke-dasharray="16 12"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="8" marker-end="url(#ar)"><path d="M120 150h150M120 270h150"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" marker-end="url(#ar)"><path d="M480 210H330"/></g>
{xx(300,340,1)}
""", ground=False, arrow=True)

add('warmth', '火のそばであたたかく過ごすイラスト。', f"""
{flame(180,320,1.2)}
{sit(400,350,1.3,-1,'coral','gold','bun','smile','down')}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M250 240q24-24 0-48M290 210q40-40 0-80"/>
</g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M470 190q-20-26 0-36 20-10 20 14 0-24 20-14 20 10 0 36l-20 20z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('warrior', '盾とかぶとで身を固めた戦士のイラスト。', f"""
{person(280,352,1.3,1,'gold','gold','carry','cap','neutral')}
<g transform="translate(400 260)">
  <path d="M-60-70h120v70q0 70-60 100-60-30-60-100z" class="tealp o"/>
  <path d="M-30-40h60v60h-60z" class="teal o"/>
</g>
<g transform="translate(160 230) rotate(-20)">
  <path d="M-8-120h16l6 150h-28z" fill="#c3cad0" class="o"/>
  <path d="M-30 30h60v16h-60z" class="goldd o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('weakness', '鎖の一か所だけが弱くて切れるイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="14">
  <circle cx="130" cy="210" r="34"/><circle cx="196" cy="210" r="34"/>
  <circle cx="404" cy="210" r="34"/><circle cx="470" cy="210" r="34"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="12">
  <path d="M240 190a34 34 0 0 0 0 40M360 190a34 34 0 0 1 0 40"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M290 170v-28M310 170v-28M300 260v28"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('wealth', '家も金も持ち合わせた富のイラスト。', f"""
<g transform="translate(180 290)">
  <path d="M-90 0v-90h180V0z" fill="#fffdf6" class="o"/>
  <path d="M-106-90L0-150l106 60z" class="teal o"/>
  <path d="M-24-56h48V0h-48z" class="teald o"/>
</g>
<g class="gold o">
  <ellipse cx="420" cy="350" rx="66" ry="22"/><ellipse cx="420" cy="320" rx="66" ry="22"/>
  <ellipse cx="420" cy="292" rx="54" ry="19"/><ellipse cx="420" cy="266" rx="42" ry="16"/>
</g>
<g transform="translate(520 200)">
  <path d="M-30-10h60l-30 40z" class="tealp o"/>
  <path d="M-30-10l14-20h32l14 20z" class="teal o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('weed', '畑にはびこる雑草を抜くイラスト。', f"""
<path d="M0 300h600v100H0z" fill="#e8ded2"/>
<g class="greens">{''.join(f'<path d="M{120+i*70} 330v-40"/>' for i in range(3))}</g>
<g class="greenp o">{''.join(f'<circle cx="{120+i*70}" cy="284" r="14"/>' for i in range(3))}</g>
<g fill="none" stroke="{TONES['green'][2]}" stroke-width="5" stroke-linecap="round">
  <path d="M380 300q-14-40 10-70M400 300q10-40 40-56M420 300q26-30 60-30"/>
</g>
{hand(470,180,-1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"><path d="M440 230v-40"/></g>
<path d="M0 300h600" class="a"/>
""", ground=False)

add('welfare', '暮らしを下から支える福祉のイラスト。', f"""
{person(230,300,0.95,1,'teal','blue','stand','bun','smile')}
{person(320,300,0.75,1,'coral','gold','stand','short','smile')}
{hand(300,380,1)}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="8">
  <path d="M120 330q180 60 360 0"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4">
  <path d="M120 330v-40M480 330v-40M240 352v-40M360 352v-40"/>
</g>
<path d="M60 390h480" class="a"/>
""", ground=True)

add('well', 'つるべで水をくむ井戸のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-100 80v-90h200v90z" fill="#b9c2c9" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">{''.join(f'<path d="M{-100+i*50} -10v90"/>' for i in range(5))}<path d="M-100 30h200"/></g>
  <path d="M-90-10l-10-100M90-10l10-100" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10"/>
  <path d="M-110-110h220v16h-220z" class="goldd o"/>
  <path d="M0-94v40" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M-24-54h48l-8 40h-32z" class="goldd o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('wheat', '穂を垂らす小麦のイラスト。', f"""
<g class="golds" stroke-width="6">{''.join(f'<path d="M{180+i*80} 356v-150"/>' for i in range(4))}</g>
<g class="gold o">{''.join(f'<ellipse cx="{180+i*80}" cy="{186}" rx="16" ry="40"/>' for i in range(4))}</g>
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="3">
  {''.join(f'<path d="M{180+i*80} 156v60M{180+i*80} 176l-14 10M{180+i*80} 176l14 10M{180+i*80} 200l-14 10M{180+i*80} 200l14 10"/>' for i in range(4))}
</g>
<g class="greens">{''.join(f'<path d="M{180+i*80} 300l{-30 if i%2 else 30} -20"/>' for i in range(4))}</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('widow', '夫を亡くしてひとり墓に立つ未亡人のイラスト。', f"""
<g transform="translate(400 260)">
  <path d="M-70 60v-100q0-40 70-40t70 40v100z" fill="#dfe6ea" class="o"/>
  <g fill="{MUTED}"><rect x="-30" y="-40" width="60" height="12"/><rect x="-6" y="-64" width="12" height="60"/></g>
</g>
{person(190,352,1.25,1,'violet','violet','stand','bun','sad')}
<g class="coral o"><circle cx="330" cy="340" r="14"/></g>
<g class="greens"><path d="M330 354v22"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tonne', '一トンのおもりを積み上げたイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-170 0h340v20h-340z" class="goldd o"/>
  <path d="M-120-70h240v70h-240z" class="ink"/>
  <path d="M-80-140h160v70h-160z" class="ink"/>
  <path d="M-40-200h80v60h-80z" class="ink"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M520 320V100"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M490 320h60M490 100h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('trillion', '桁がとんでもなく大きい数のイラスト。', f"""
<g transform="translate(300 250)">
  <g class="teal o">{''.join(f'<rect x="{-240+i*56}" y="{60-(8+i*i*3)}" width="40" height="{8+i*i*3}"/>' for i in range(8))}</g>
  <path d="M-250 60h500" class="a"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M120 300q200-30 340-260"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('robbery', '覆面で金品を奪い取る強盗のイラスト。', f"""
{person(220,352,1.25,1,'blue','blue','carry','cap','neutral')}
<g transform="translate(220 224)">
  <path d="M-28-6h56v20h-56z" class="ink"/>
</g>
<g transform="translate(330 300)">
  <path d="M-50-30h100v80h-100z" class="goldd o"/>
  <path d="M-50-30q50-30 100 0z" class="gold o"/>
</g>
{person(480,352,1.1,-1,'coral','gold','up','bob','sad')}
{xx(330,160,1.1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('spite', 'わざと嫌がることをする悪意のイラスト。', f"""
{person(180,352,1.2,1,'blue','blue','reach','short','neutral')}
{person(470,352,1.15,-1,'coral','gold','up','bob','sad')}
<g transform="translate(330 290)">
  <path d="M-50-30h100v60h-100z" class="tealp o"/>
  <path d="M-50-30l100 60M50-30l-100 60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
{cloud(200,110,1.2,'violet')}
{xx(330,170,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
