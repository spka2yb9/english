"""第113回（最終）: 残りの44語。"""
from lib import *
W=[]
def add(slug,a,b,**k): W.append(emit(slug,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'
def qmark(x,y,s=1,cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-24-26q0-28 26-28t26 26q0 22-26 28v12" fill="none" stroke="{TONES[cls][0]}" stroke-width="10" stroke-linecap="round"/>'
            f'<circle cy="36" r="7" class="{cls}"/></g>')
def star(x,y,r=30,cls='gold'):
    import math
    pts=[]
    for i in range(10):
        rr = r if i%2==0 else r*0.45
        a = math.radians(-90+i*36)
        pts.append(f'{x+rr*math.cos(a):.0f} {y+rr*math.sin(a):.0f}')
    return f'<path d="M{"L".join(pts)}z" class="{cls} o"/>'
def gear(x,y,r=60,cls='teal',teeth=8):
    t=''.join(f'<rect x="-12" y="{-r-22}" width="24" height="26" transform="rotate({i*360//teeth})"/>' for i in range(teeth))
    return (f'<g transform="translate({x} {y})"><g class="{cls} o">{t}</g>'
            f'<circle r="{r}" class="{cls} o"/><circle r="{r*0.35:.0f}" fill="#fffdf6" stroke="{INK}" stroke-width="3"/></g>')
def female(x,y,s=1,cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<circle cy="-40" r="56" fill="none" stroke="{TONES[cls][0]}" stroke-width="16"/>'
            f'<path d="M0 16v76M-34 60h68" fill="none" stroke="{TONES[cls][0]}" stroke-width="16" stroke-linecap="round"/></g>')
def male(x,y,s=1,cls='blue'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<circle cy="20" r="54" fill="none" stroke="{TONES[cls][0]}" stroke-width="16"/>'
            f'<path d="M32-20l52-52M46-78h40v40" fill="none" stroke="{TONES[cls][0]}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/></g>')

add('affair', '取り組むべき用件が並ぶイラスト。', f"""
<g transform="translate(220 220)">
  <path d="M-150-150h300v300h-300z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-110 {-100+i*50}h220"/>' for i in range(5))}</g>
</g>
<g transform="translate(470 230)">
  <circle r="90" class="bluep o"/>
  <path d="M-40-60q40 14 20 40t14 46 40 12" class="greenp o"/>
  <g fill="none" stroke="{INK}" stroke-width="2.5"><ellipse rx="40" ry="90"/><path d="M-90 0h180"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('arguably', '議論の余地はあるがおそらくそうだイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-8-70h16v160h-16z" class="ink"/>
  <path d="M-60 90h120v20H-60z" class="ink"/>
  <path d="M-130-66h260v12h-260z" class="ink"/>
  <path d="M-130-54v40M130-54v20" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-180-14h100q0 36-50 36t-50-36z" class="tealp o"/>
  <path d="M80-34h100q0 36-50 36t-50-36z" class="coralp o"/>
</g>
{qmark(480,140,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('concern', '気にかかって心配するイラスト。', f"""
{person(200,352,1.25,1,'teal','blue','think','short','sad')}
{cloud(430,180,1.4,'violet')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round">
  <path d="M430 160v40"/><circle cx="430" cy="228" r="8" fill="{TONES['coral'][0]}" stroke="none"/>
</g>
<g class="o" fill="#e1edfb"><circle cx="300" cy="250" r="14"/><circle cx="278" cy="276" r="9"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('earnings', '働いて手にする収入のイラスト。', f"""
{person(160,352,1.2,1,'teal','blue','reach','short','smile')}
<g class="gold o"><ellipse cx="330" cy="220" rx="30" ry="13"/><ellipse cx="330" cy="198" rx="30" ry="13"/><ellipse cx="330" cy="176" rx="30" ry="13"/></g>
<g transform="translate(470 290)">
  <path d="M-80-40h160v100h-160z" class="goldd o"/>
  <path d="M-80-40q80-30 160 0" fill="none" stroke="{TONES['gold'][0]}" stroke-width="5"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 260h150"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('economics', 'お金の動きを学ぶ経済学のイラスト。', f"""
<g transform="translate(200 230)">
  <path d="M-110-130h220v260h-220z" class="violet o"/>
  <path d="M-90-110h180v220h-180z" fill="#fffdf6" class="o"/>
  <path d="M-60 60l40-50 30 26 50-70" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"/>
  <path d="M-64-80v150h140" class="a"/>
</g>
<g class="gold o"><ellipse cx="440" cy="320" rx="34" ry="14"/><ellipse cx="440" cy="296" rx="34" ry="14"/><ellipse cx="440" cy="272" rx="34" ry="14"/></g>
{gear(470,150,40,'teal',8)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('economist', '経済の図を示して説く学者のイラスト。', f"""
{person(160,352,1.25,1,'violet','blue','point','short','neutral')}
<g transform="translate(410 220)">
  <path d="M-140-120h280v240h-280z" class="paper"/>
  <path d="M-100 70l50-50 40 26 60-90" fill="none" stroke="{TONES['teal'][0]}" stroke-width="7"/>
  <path d="M-110-90v170h220" class="a"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M240 250h30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('effectiveness', 'ねらいどおりの効き目が出るイラスト。', f"""
<g transform="translate(160 250)">
  <path d="M-60-40h120v80h-120z" class="coral o"/>
  <path d="M-30-56h60v16h-60z" class="corald o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>
<g transform="translate(450 250)">
  <circle r="100" fill="#fffdf6" class="o"/>
  <circle r="66" class="coralp o"/>
  <circle r="30" class="coral o"/>
  <circle r="8" class="ink"/>
</g>
{ck(450,120,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('efficiency', '少ない元手でよく回る効率のイラスト。', f"""
<g transform="translate(150 250)">
  <path d="M-40-40h80v80h-80z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M220 250h40"/></g>
{gear(330,250,60,'teal',9)}
<g class="a" marker-end="url(#ar)"><path d="M410 250h40"/></g>
<g transform="translate(510 250)">
  <path d="M-60-60h120v120h-120z" class="teal o"/>
</g>
{ck(330,130,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('efficiently', '短い時間でうまく仕上げるイラスト。', f"""
<g transform="translate(160 210)">
  <circle r="70" fill="#fffdf6" class="o"/>
  <path d="M0 0v-44" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <path d="M0 0l26 16" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round"/>
  <path d="M0-70A70 70 0 0 1 44-54L0 0z" class="greenp"/>
  <circle r="7" class="ink"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M260 210h50"/></g>
<g class="teal o">{''.join(f'<rect x="{360+ (i%3)*66}" y="{190+(i//3)*70}" width="50" height="50"/>' for i in range(6))}</g>
{ck(300,350,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('enterprise', '旗をかかげて興した事業のイラスト。', f"""
{tower(300,330,0.95,'teal',5)}
<g transform="translate(300 120)">
  <path d="M-6 0v-70" class="a"/>
  <path d="M-6-70h90l-18 24 18 24H-6z" class="coral o"/>
</g>
{person(140,356,0.8,1,'violet','blue','up','short','smile')}
{person(470,356,0.8,-1,'gold','violet','up','bob','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('expenditure', '出ていくお金が積み上がるイラスト。', f"""
<g transform="translate(300 250)">
  <g class="coralp o">{''.join(f'<rect x="{-220+i*70}" y="{60-(30+i*26)}" width="50" height="{30+i*26}"/>' for i in range(6))}</g>
  <path d="M-230 60h460" class="a"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M540 320V140"/></g>
<g class="gold o"><ellipse cx="110" cy="150" rx="26" ry="11"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('expense', 'かかった費用を記した伝票のイラスト。', f"""
<g transform="translate(280 210)">
  <path d="M-130-150h260v290l-26-20-26 20-26-20-26 20-26-20-26 20-26-20-26 20z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-96-110h190M-96-70h190M-96-30h150"/></g>
  <path d="M-96 20h190" fill="none" stroke="{INK}" stroke-width="3"/>
  <g fill="{TONES['coral'][0]}"><rect x="10" y="40" width="84" height="16"/></g>
</g>
<g class="gold o"><ellipse cx="490" cy="320" rx="30" ry="13"/><ellipse cx="490" cy="298" rx="30" ry="13"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('extremist', '考えが端まで振り切れた立場のイラスト。', f"""
<g class="a"><path d="M60 300h480"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M{100+i*68} 300v16"/>' for i in range(7))}</g>
{person(300,300,0.8,1,'teal','blue','stand','short','neutral')}
{person(510,300,0.9,1,'coral','gold','up','cap','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="510" cy="220" r="80"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M400 340h140"/></g>
""", ground=False, arrow=True)

add('fabric', '織り上がった布地のイラスト。', f"""
<g transform="translate(300 220)">
  <g stroke="{TONES['teal'][0]}" stroke-width="18" fill="none">{''.join(f'<path d="M{-200+i*50} -130v260"/>' for i in range(9))}</g>
  <g stroke="{TONES['teal'][1]}" stroke-width="18" fill="none">{''.join(f'<path d="M-210 {-100+i*56}h420"/>' for i in range(5))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('feat', '並はずれた偉業をなしとげるイラスト。', f"""
<path d="M0 380l200-250 110 140 80-100 210 210z" class="greenp o"/>
{person(200,140,0.7,1,'coral','blue','up','short','smile')}
{star(330,120,30,'gold')}
{star(110,150,22,'gold')}
<path d="M0 380h600" class="a"/>
""", ground=False)

add('feminist', '女性の権利を訴える立場のイラスト。', f"""
{person(200,352,1.25,1,'coral','violet','up','bun','neutral')}
<g transform="translate(430 220)">
  <path d="M-110-120h220v240h-220z" class="paper"/>
  <g transform="translate(0 -10) scale(0.75)"><circle cy="-40" r="56" fill="none" stroke="{TONES['coral'][0]}" stroke-width="16"/><path d="M0 16v76M-34 60h68" fill="none" stroke="{TONES['coral'][0]}" stroke-width="16" stroke-linecap="round"/></g>
  <path d="M0 120v50" fill="none" stroke="{MUTED}" stroke-width="6"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('figure-out', '解けなかったことが分かるイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-90-90h180v180h-180z" class="tealp o"/>
  <path d="M-90 0h180M0-90v90" fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"/>
  <path d="M0 0h90v90H0z" fill="#fffaf1" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 250h50"/></g>
<g transform="translate(460 240)">
  <path d="M0-80q50 0 50 48 0 28-22 40v20h-56v-20q-22-12-22-40 0-48 50-48z" class="gold o"/>
  <path d="M-28 28h56v18h-56z" class="goldd o"/>
  <g class="golds"><path d="M-96-36l-28-14M96-36l28-14M0-106v-28"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('finance', 'お金の流れをやりくりする財務のイラスト。', f"""
{building(160,300,0.75,'violet')}
<g transform="translate(420 220)">
  <path d="M-130-110h260v220h-260z" class="paper"/>
  <path d="M-90 60l50-46 40 24 60-80" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"/>
  <path d="M-100-80v150h200" class="a"/>
</g>
<g class="gold o"><ellipse cx="290" cy="330" rx="30" ry="13"/><ellipse cx="290" cy="308" rx="30" ry="13"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('flexibility', 'よく曲がってしなやかなイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="18" stroke-linecap="round"><path d="M120 200h100"/></g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="18" stroke-linecap="round">
  <path d="M220 200q90-90 160 0t100 60"/>
</g>
{hand(120,290,1)}
{ck(300,340,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('formula', '黒板に書かれた公式のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-220-140h440v280h-440z" class="ink"/>
  <path d="M-204-126h408v252h-408z" fill="#2c3a30"/>
  <g fill="none" stroke="#e8f1e8" stroke-width="7" stroke-linecap="round">
    <path d="M-150-40h50M-125-65v50M-70-40h60M40-70h60M40-40h60M40-10h40M150-70l50 60M200-70l-50 60"/>
    <path d="M-150 50h300"/>
  </g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('frame', '絵をふちどる額縁のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-150h360v300h-360z" class="goldd o"/>
  <path d="M-140-110h280v220h-280z" fill="#fdf6e3" class="o"/>
  <path d="M-110 80l70-90 60 60 40-40 60 70z" class="greenp o"/>
  <circle cx="60" cy="-50" r="26" class="goldp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M540 370L440 330"/></g>
""", ground=False, arrow=True)

add('franchise', '同じ看板の店があちこちに並ぶイラスト。', f"""
<g transform="translate(150 300)">
  <path d="M-70 0v-70h140V0z" fill="#fffdf6" class="o"/>
  <path d="M-80-70h160v-26h-160z" class="coral o"/>
  <circle cx="0" cy="-40" r="18" class="coralp o"/>
</g>
<g transform="translate(320 300)">
  <path d="M-70 0v-70h140V0z" fill="#fffdf6" class="o"/>
  <path d="M-80-70h160v-26h-160z" class="coral o"/>
  <circle cx="0" cy="-40" r="18" class="coralp o"/>
</g>
<g transform="translate(490 300)">
  <path d="M-70 0v-70h140V0z" fill="#fffdf6" class="o"/>
  <path d="M-80-70h160v-26h-160z" class="coral o"/>
  <circle cx="0" cy="-40" r="18" class="coralp o"/>
</g>
<path d="M60 326h480" class="a"/>
""", ground=True)

add('frankly', '包み隠さず率直に言うイラスト。', f"""
{person(170,352,1.25,1,'teal','blue','give','short','neutral')}
<g transform="translate(400 200)">
  <path d="M-120-80h240v130h-240zM-80 50l-14 34 44-34z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="8"><path d="M-80-40h160M-80 0h120"/></g>
</g>
{ck(500,320,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('fund', 'ある目的のためにためたお金のイラスト。', f"""
<g transform="translate(300 270)">
  <path d="M-130-60h260v130h-260z" class="goldd o"/>
  <path d="M-140-80h280v20h-280z" class="gold o"/>
  <path d="M-40-100h80v20h-80z" class="a" fill="none"/>
</g>
<g class="gold o">
  <ellipse cx="230" cy="180" rx="30" ry="13"/><ellipse cx="300" cy="160" rx="30" ry="13"/><ellipse cx="370" cy="180" rx="30" ry="13"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 200v20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('funding', '事業にお金が出されるイラスト。', f"""
<g transform="translate(150 290)">
  <path d="M-80-40h160v100h-160z" class="goldd o"/>
  <path d="M-90-60h180v20h-180z" class="gold o"/>
</g>
<g transform="translate(300 240)">
  <path d="M-50-26h100v52h-100z" class="greenp o"/>
  <circle r="14" class="gold o"/>
</g>
{tower(470,320,0.6,'teal',4)}
<g class="a" marker-end="url(#ar)"><path d="M240 170h180"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('fundraising', '寄付を集めて資金を作るイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-100-40h200v110h-200z" class="tealp o"/>
  <path d="M-50-50h100v14h-100z" class="ink"/>
</g>
{person(130,356,0.85,1,'coral','blue','give','short','smile')}
{person(480,356,0.85,-1,'gold','violet','give','bob','smile')}
<g class="gold o"><ellipse cx="220" cy="190" rx="26" ry="11"/><ellipse cx="380" cy="190" rx="26" ry="11"/></g>
<g class="a" marker-end="url(#ar)"><path d="M240 220l40 30M380 220l-40 30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('gender', '男女という区分を示すイラスト。', f"""
{female(180,230,0.95,'violet')}
{male(430,220,0.95,'teal')}
<g fill="none" stroke="{MUTED}" stroke-width="6"><path d="M290 240h30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('governance', '舵を取って組織を運ぶイラスト。', f"""
<g transform="translate(230 250)">
  <circle r="90" fill="none" stroke="{TONES['gold'][2]}" stroke-width="18"/>
  <circle r="26" class="goldd o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="14">
    <path d="M0-90v-26M0 90v26M-90 0h-26M90 0h26"/>
  </g>
</g>
<g transform="translate(460 230)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-56 {-60+i*44}h112"/>' for i in range(4))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('heritage', '昔から受け継がれてきた建物のイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-190 0h380v20h-380z" class="goldd o"/>
  <g class="goldp o">{''.join(f'<rect x="{-160+i*70}" y="-140" width="46" height="140"/>' for i in range(5))}</g>
  <path d="M-190-140h380v26h-380z" class="gold o"/>
  <path d="M-210-166L0-230l210 64z" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"><path d="M110 320V210q0-90 190-90t190 90v110"/></g>
{ck(300,110,0.9)}
<path d="M60 356h480" class="a"/>
""", ground=True)

add('humanity', '人という種のみんなを表すイラスト。', f"""
{person(110,352,0.9,1,'coral','blue','stand','short','smile')}
{person(200,352,0.9,1,'gold','violet','stand','bun','smile')}
{person(290,352,0.9,-1,'teal','gold','stand','cap','smile')}
{person(380,352,0.9,-1,'green','blue','stand','bob','smile')}
{person(470,352,0.9,-1,'violet','coral','stand','short','smile')}
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2.5">
  <path d="M300 150q-30-38 0-54 30-16 30 22 0-38 30-22 30 16 0 54l-30 30z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('impact', 'ぶつかって強い衝撃が伝わるイラスト。', f"""
<circle cx="180" cy="230" r="46" class="teal o"/>
<g transform="translate(390 230)">
  <path d="M0-120l32 60 66-20-22 62 62 30-62 30 22 62-66-20-32 60-32-60-66 20 22-62-62-30 62-30-22-62 66 20z" class="coralp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 230h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('implication', '口にしない先の意味がにじむイラスト。', f"""
<g transform="translate(180 200)">
  <path d="M-110-70h220v120h-220zM-70 50l-14 30 44-30z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="6"><path d="M-70-30h140M-70 4h100"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M310 250h60"/></g>
<g transform="translate(470 260)" opacity="0.5">
  <path d="M-80-70h160v140h-160z" class="coralp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('incidence', 'ある広さの中で起きる回数のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-140h440v280h-440z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">
    {''.join(f'<path d="M{-220+i*55} -140v280"/>' for i in range(9))}
    {''.join(f'<path d="M-220 {-140+i*56}h440"/>' for i in range(6))}
  </g>
  <g class="coral">{''.join(f'<circle cx="{-190+(i*97)%400}" cy="{-110+(i*67)%250}" r="12"/>' for i in range(9))}</g>
</g>
""", ground=False)

add('initiative', '自分から先に動き出すイラスト。', f"""
{person(200,352,1.25,1,'coral','blue','walk','short','neutral')}
{person(430,356,0.9,1,'teal','blue','stand','short','neutral')}
{person(510,356,0.9,1,'gold','violet','stand','bob','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M120 200h180"/></g>
{ck(300,140,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('make', '材料から品を作り出すイラスト。', f"""
{hand(140,240,1)}
<g transform="translate(280 250)">
  <path d="M-60-40h50v50h-50zM10-40h50v50H10zM-30 20h50v50h-50z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M370 250h50"/></g>
<g transform="translate(490 250)">
  <path d="M-60-60h120v120h-120z" class="teal o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('makeup', '口紅とおしろいの化粧道具のイラスト。', f"""
<g transform="translate(200 270)">
  <path d="M-30 60h60v-70h-60z" class="goldd o"/>
  <path d="M-22-10h44v-40h-44z" class="corald o"/>
  <path d="M-16-50h32v-40q-16-14-32 0z" class="coral o"/>
</g>
<g transform="translate(400 290)">
  <ellipse rx="80" ry="26" class="goldp o"/>
  <ellipse cy="-20" rx="80" ry="26" fill="#fffdf6" class="o"/>
  <ellipse cy="-20" rx="54" ry="16" class="coralp o"/>
</g>
<g transform="translate(500 200) rotate(24)">
  <path d="M-8-70h16v90h-16z" fill="{TONES['gold'][2]}"/>
  <path d="M-18 20h36l-8 40h-20z" fill="{MUTED}" class="o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('militia', '住民が自ら組む隊のイラスト。', f"""
{person(150,352,1,1,'gold','green','stand','cap','neutral')}
{person(250,352,1,1,'coral','green','stand','short','neutral')}
{person(350,352,1,1,'teal','green','stand','cap','neutral')}
<g transform="translate(470 250)">
  <path d="M-6 110V-90" class="a"/>
  <path d="M-6-90h90v60H-6z" class="green o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><rect x="90" y="200" width="330" height="170" rx="20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('potentially', 'まだ表に出ていない見込みのイラスト。', f"""
<g opacity="0.35">{tree(300,340,1.9)}</g>
<g transform="translate(300 330)">
  <ellipse rx="24" ry="18" class="goldd o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M300 300V150"/></g>
{qmark(480,180,1)}
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('sexuality', 'だれに心を寄せるかのあり方のイラスト。', f"""
{female(180,230,0.8,'violet')}
{male(420,220,0.8,'teal')}
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2.5">
  <path d="M300 200q-28-36 0-52 28-16 28 22 0-38 28-22 28 16 0 52l-28 28z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('spokeswoman', '団体を代表して話す女性のイラスト。', f"""
{person(240,352,1.3,1,'violet','violet','point','bun','neutral')}
<g transform="translate(240 330)">
  <path d="M-56-40h112l16 60h-144z" class="goldd o"/>
</g>
<g transform="translate(330 250)">
  <path d="M-14-26h28v50h-28z" class="ink"/>
  <circle cy="-38" r="18" fill="{MUTED}" class="o"/>
</g>
{person(470,356,0.75,-1,'teal','blue','stand','short','neutral')}
{person(540,356,0.75,-1,'coral','gold','stand','bob','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('vulnerability', '守りに割れ目があってもろいイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M0-140l130 44v96q0 86-130 130-130-44-130-130v-96z" class="tealp o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linejoin="round">
    <path d="M-10-100l30 60-40 30 30 80"/>
  </g>
</g>
{xx(500,150,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('warming', '地球の気温が上がる温暖化のイラスト。', f"""
<g transform="translate(230 240)">
  <circle r="110" class="bluep o"/>
  <path d="M-60-80q50 18 24 52t18 58 50 16" class="greenp o"/>
  <g fill="none" stroke="{INK}" stroke-width="2.5"><ellipse rx="50" ry="110"/><path d="M-110 0h220"/></g>
</g>
{thermometer(450,330,0.9,0.9)}
{sun(510,90,38)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M380 300V180"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('workload', '机に積み上がった仕事の量のイラスト。', f"""
<g transform="translate(330 330)">
  <path d="M-170-20h340v20h-340z" class="goldd o"/>
  <path d="M-140 0v46M140 0v46" class="a"/>
</g>
<g transform="translate(330 250)">
  <path d="M-120-40h240v40h-240z" class="paper"/>
  <path d="M-110-80h240v40h-240z" class="paper"/>
  <path d="M-124-120h240v40h-240z" class="paper"/>
  <path d="M-112-160h240v40h-240z" class="paper"/>
</g>
{person(120,352,1.05,1,'teal','blue','up','short','sad')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('workshop', '手を動かして学ぶ作業の講座のイラスト。', f"""
<g transform="translate(320 320)">
  <path d="M-200-30h400v20h-400z" class="goldd o"/>
  <path d="M-170-10v46M170-10v46" class="a"/>
</g>
{person(160,290,1,1,'violet','blue','point','bun','smile')}
{person(330,300,0.9,1,'teal','blue','reach','short','smile')}
{person(460,300,0.9,-1,'coral','gold','reach','bob','smile')}
<g transform="translate(390 265) rotate(20)">
  <path d="M-8-30h16v50h-16z" fill="{MUTED}" class="o"/>
  <path d="M-18-40h36v16h-36z" fill="{MUTED}" class="o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
