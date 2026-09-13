"""第111回: 名詞・形容詞45語。"""
from lib import *
W=[]
def add(slug,a,b,**k): W.append(emit(slug,a,b,**k))
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
def female(x,y,s=1,cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<circle cy="-40" r="60" fill="none" stroke="{TONES[cls][0]}" stroke-width="16"/>'
            f'<path d="M0 20v80M-36 66h72" fill="none" stroke="{TONES[cls][0]}" stroke-width="16" stroke-linecap="round"/></g>')
def male(x,y,s=1,cls='blue'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<circle cy="20" r="58" fill="none" stroke="{TONES[cls][0]}" stroke-width="16"/>'
            f'<path d="M34-22l56-56M50-84h44v44" fill="none" stroke="{TONES[cls][0]}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/></g>')

add('sexual', '雌雄を示す記号のイラスト。', f"""
{female(190,230,1,'coral')}
{male(420,220,1,'blue')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sex', '男女の別を示す記号のイラスト。', f"""
{female(190,230,1,'violet')}
{male(420,220,1,'teal')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12"><path d="M300 110v240"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('gay', '男性どうしが手をつなぐイラスト。', f"""
{person(230,352,1.2,1,'teal','blue','give','short','smile')}
{person(380,352,1.2,-1,'gold','violet','give','cap','smile')}
<g fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"><path d="M280 290h50"/></g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2.5">
  <path d="M305 170q-26-34 0-48 26-14 26 20 0-34 26-20 26 14 0 48l-26 26z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('lesbian', '女性どうしが手をつなぐイラスト。', f"""
{person(230,352,1.2,1,'coral','violet','give','bun','smile')}
{person(380,352,1.2,-1,'teal','gold','give','bob','smile')}
<g fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"><path d="M280 290h50"/></g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2.5">
  <path d="M305 170q-26-34 0-48 26-14 26 20 0-34 26-20 26 14 0 48l-26 26z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('profit', '売上から費用を引いて残る利益のイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-200-140h130v240h-130z" class="teal o"/>
  <path d="M-50-40h130v140H-50z" fill="#dfe6ea" class="o"/>
  <path d="M100-100h110v200H100z" class="coral o"/>
  <path d="M-210 100h430" class="a"/>
</g>
<g fill="none" stroke="{GRN}" stroke-width="12" stroke-linecap="round"><path d="M480 130h50M505 105v50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('profitable', 'もうけが出て黒字になるイラスト。', f"""
<g transform="translate(280 220)">
  <path d="M-180-130h360v260h-360z" class="paper"/>
  <path d="M-140 90l60-50 50 26 70-100" fill="none" stroke="{GRN}" stroke-width="8"/>
  <path d="M-150-110v210h300" class="a"/>
</g>
<g class="gold o"><ellipse cx="500" cy="330" rx="34" ry="14"/><ellipse cx="500" cy="308" rx="34" ry="14"/><ellipse cx="500" cy="286" rx="34" ry="14"/></g>
{ck(500,180,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('property', '自分のものである土地と家のイラスト。', f"""
<g transform="translate(280 300)">
  <path d="M-90 0v-90h180V0z" fill="#fffdf6" class="o"/>
  <path d="M-104-90L0-146l104 56z" class="teal o"/>
  <path d="M-24-56h48V0h-48z" class="teald o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="14 12"><rect x="110" y="180" width="380" height="180" rx="14"/></g>
<g transform="translate(460 250)">
  <path d="M-40-40h80v80h-80z" class="paper"/>
  <circle cx="0" cy="10" r="14" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('psychiatric', '心の病を診る医学のイラスト。', f"""
<g transform="translate(230 230)">
  <path d="M-30 140v-40q-70-16-70-90 0-90 90-90 92 0 92 86 0 44-36 62v72z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2.5">
  <path d="M230 200q-26-34 0-48 26-14 26 20 0-34 26-20 26 14 0 48l-26 26z"/>
</g>
<g transform="translate(460 240)">
  <path d="M-70-90h140v180h-140z" class="paper"/>
  <path d="M-14-70h28v20h20v28h-20v20h-28v-20h-20v-28h20z" class="coralp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-44 20h88M-44 50h60"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('quality', '品を調べて上等だと認めるイラスト。', f"""
{box(240,260,180,130,34,'teal')}
<g transform="translate(430 180)">
  <circle r="60" fill="none" stroke="{INK}" stroke-width="8"/>
  <path d="M44 44l46 46" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>
</g>
{star(160,140,26,'gold')}
{star(230,120,26,'gold')}
{star(300,140,26,'gold')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('rate', '速さや割合を目盛りで表すイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-160 0a160 160 0 0 1 320 0z" fill="#fffdf6" class="o"/>
  <path d="M-160 0h320" class="a"/>
  <path d="M0 0l90-110" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"/>
  <circle r="11" class="ink"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M0 -140v-16" transform="rotate({-90+i*30})"/>' for i in range(7))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('rational', '感情でなく筋道で考えるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-30 140v-40q-70-16-70-90 0-90 90-90 92 0 92 86 0 44-36 62v72z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <g class="teal o"><rect x="-56" y="-70" width="40" height="34"/><rect x="4" y="-70" width="40" height="34"/></g>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="4" marker-end="url(#ar)"><path d="M-14-52h14"/></g>
</g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2" opacity="0.4">
  <path d="M500 200q-22-28 0-40 22-12 22 16 0-28 22-16 22 12 0 40l-22 22z"/>
</g>
{xx(510,220,0.8,MUTED)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('relationship', 'ふたりのあいだのつながりのイラスト。', f"""
{person(200,352,1.2,1,'teal','blue','give','short','smile')}
{person(400,352,1.2,-1,'coral','gold','give','bob','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10"><path d="M262 280h76"/></g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2.5">
  <path d="M300 180q-24-32 0-44 24-12 24 18 0-30 24-18 24 12 0 44l-24 24z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('rule', '守るべき決まりを書いたルールのイラスト。', f"""
<g transform="translate(230 220)">
  <path d="M-140-150h280v300h-280z" class="paper"/>
  <path d="M-110-110h220v40h-220z" class="teal o"/>
  <g class="tealp o">{''.join(f'<circle cx="-86" cy="{-30+i*50}" r="16"/>' for i in range(3))}</g>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-56 {-30+i*50}h170"/>' for i in range(3))}</g>
</g>
<g transform="translate(470 230)">
  <circle r="70" fill="none" stroke="{TONES['coral'][0]}" stroke-width="16"/>
  <path d="M-44 0h88" fill="none" stroke="{TONES['coral'][0]}" stroke-width="16" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('service', '客をもてなして応対するイラスト。', f"""
{person(200,352,1.2,1,'violet','violet','give','bun','smile')}
<g transform="translate(300 250)">
  <ellipse rx="70" ry="20" class="goldp o"/>
  <path d="M-30-30h60l-8 30h-44z" class="coral o"/>
</g>
{sit(450,352,1.15,-1,'teal','blue','short','smile','lap')}
{chair(440,356,1.1,'gold',-1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('shift', '位置をずらして移すイラスト。', f"""
<g transform="translate(180 250)" opacity="0.4">
  <path d="M-70-70h140v140h-140z" class="teal o"/>
</g>
<g transform="translate(420 250)">
  <path d="M-70-70h140v140h-140z" class="teal o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h70"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('situation', '今どうなっているかを見わたすイラスト。', f"""
{person(300,352,1.2,1,'teal','blue','stand','short','neutral')}
{cloud(140,120,1.1,'blue')}
<g transform="translate(470 300)">
  <path d="M-70-40h140v80h-140z" class="coralp o"/>
</g>
<g transform="translate(150 300)">
  <path d="M-60-30h120v60h-120z" class="tealp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><circle cx="300" cy="240" r="220"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('socialist', 'みんなで分け合う立場のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-6 180V-90" class="a"/>
  <path d="M-6-90h120v70H-6z" class="coral o"/>
</g>
{person(140,352,0.9,1,'coral','blue','reach','short','neutral')}
{person(460,352,0.9,-1,'coral','gold','reach','bob','neutral')}
<g class="gold o"><ellipse cx="230" cy="330" rx="28" ry="12"/><ellipse cx="370" cy="330" rx="28" ry="12"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M300 330h-40M300 330h40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('solution', '問題の鍵がぴたりとはまるイラスト。', f"""
<g transform="translate(400 250)">
  <path d="M-70-40h140v100h-140z" class="gold o"/>
  <path d="M-40-40v-30q0-40 40-40t40 40v30" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14"/>
  <path d="M-14 10h28v34h-28z" class="goldd o"/>
</g>
<g transform="translate(180 260)">
  <circle r="30" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12"/>
  <path d="M26 0h80v14h-18v18h-14v-18h-16v18h-14v-18h-18z" fill="{TONES['gold'][2]}"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 180h50"/></g>
{ck(500,150,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('specialized', 'その用にだけ合う専用の道具のイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-70-70h140v140h-140z" class="tealp o"/>
  <path d="M-30-14h60v28h-60z" fill="#fffaf1" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(400 250) rotate(20)">
  <path d="M-10-70h20v110h-20z" fill="{MUTED}" class="o"/>
  <path d="M-34 40h68v24h-68z" fill="{MUTED}" class="o"/>
</g>
{ck(500,150,0.9)}
<g class="a" marker-end="url(#ar)"><path d="M330 320h-70"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('spending', '財布からお金が出ていくイラスト。', f"""
<g transform="translate(200 290)">
  <path d="M-90-40h180v100h-180z" class="goldd o"/>
  <path d="M-90-40q90-30 180 0" fill="none" stroke="{TONES['gold'][0]}" stroke-width="5"/>
</g>
<g class="gold o"><ellipse cx="330" cy="220" rx="28" ry="12"/><ellipse cx="410" cy="190" rx="28" ry="12"/><ellipse cx="490" cy="220" rx="28" ry="12"/></g>
<g class="a" marker-end="url(#ar)"><path d="M280 200h180"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('spiritual', '心の奥や祈りにかかわるイラスト。', f"""
<g transform="translate(300 330)">
  <path d="M-90 0q0-30 90-30t90 30z" class="bluep o"/>
  <path d="M-60-30q20-40 60-40t60 40z" class="violet o"/>
  <circle cy="-96" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-31-99q4-34 31-34 30 0 34 31-16-12-33-5-15-13-32 8z" fill="{HAIR}" stroke="{HAIR}" stroke-width="2"/>
  <g fill="none" stroke="{INK}" stroke-width="2.5"><path d="M-16-96q8 6 16 0M0-96q8 6 16 0"/></g>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="8"><ellipse cx="300" cy="192" rx="52" ry="14"/></g>
<g class="golds"><path d="M300 140v-24M200 180l-20-20M400 180l20-20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('statistical', '数値の散らばりを図にした統計のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-210-140h420v280h-420z" class="paper"/>
  <g class="tealp o">{''.join(f'<rect x="{-170+i*50}" y="{100-(100-abs(i-3)*28)}" width="36" height="{100-abs(i-3)*28}"/>' for i in range(7))}</g>
  <path d="M-180 100h380" class="a"/>
  <path d="M-170-20q80-90 170-90t170 90" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
""", ground=False)

add('steep', '傾きが急な坂のイラスト。', f"""
<path d="M120 360L440 90v270z" class="greenp o"/>
<path d="M120 360L440 90" fill="none" stroke="{INK}" stroke-width="5"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M180 360a80 80 0 0 0 34-58"/></g>
{person(320,232,0.9,1,'teal','blue','walk','short','sad')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('straightforward', 'ひとすじの分かりやすい道のイラスト。', f"""
<g class="ink"><circle cx="120" cy="240" r="20"/><circle cx="480" cy="240" r="20"/></g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="16" marker-end="url(#ar)"><path d="M150 240h300"/></g>
{ck(300,340,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('sum', 'いくつかの数を足した合計のイラスト。', f"""
<g transform="translate(300 230)">
  <g class="tealp o"><rect x="-220" y="-40" width="70" height="80"/><rect x="-120" y="-60" width="70" height="100"/><rect x="-20" y="-20" width="70" height="60"/></g>
  <g fill="none" stroke="{GRN}" stroke-width="10" stroke-linecap="round"><path d="M80 0h50M105-25v50"/></g>
  <path d="M160-90h120v130H160z" class="teal o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sustainable', '使っても回り続けて尽きないイラスト。', f"""
<g fill="none" stroke="{GRN}" stroke-width="18" stroke-linecap="round">
  <path d="M300 100a130 130 0 1 1-92 38"/>
</g>
<path d="M300 62l56 38-56 38z" fill="{TONES['green'][2]}" stroke="{INK}" stroke-width="3"/>
<g transform="translate(300 250)">
  <path d="M0 60V-10" class="greens"/>
  <path d="M0-10q-44-6-50-44 42-6 50 44z" class="greenp o"/>
  <path d="M0-30q44-6 50-44-42-6-50 44z" class="greenp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tax', '払う額から差し引かれる税のイラスト。', f"""
<g transform="translate(280 220)">
  <path d="M-140-150h280v300h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-100 {-100+i*44}h200"/>' for i in range(3))}</g>
  <path d="M-110 40h220v60h-220z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M-110 20h220"/></g>
</g>
{building(480,320,0.6,'violet')}
<g class="a" marker-end="url(#ar)"><path d="M430 250h40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('theory', '黒板に立てた考えの筋のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-220-140h440v280h-440z" class="ink"/>
  <path d="M-204-126h408v252h-408z" fill="#2c3a30"/>
  <g fill="none" stroke="#e8f1e8" stroke-width="6" stroke-linecap="round">
    <path d="M-160-70h80M-120-96v52M-40-70h60M60-96l40 52M100-96l-40 52"/>
    <path d="M-160 20h100M-160 60q40-40 80 0M20 20h120M20 60h90"/>
  </g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('total', '全部を合わせた総額のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-230-40h140v80h-140z" class="tealp o"/>
  <path d="M-80-40h140v80h-140z" class="tealp o"/>
  <path d="M70-40h160v80H70z" class="teal o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M70 340h460M70 340v-24M530 340v-24"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('treatment', '薬と手当てで病を治すイラスト。', f"""
<g transform="translate(230 300)">
  <path d="M-120 20h240v16h-240z" class="ink"/>
  <path d="M-120-14h240v34h-240z" fill="#fffdf6" class="o"/>
  <path d="M-120-50h46v36h-46z" class="bluep o"/>
  <ellipse cx="-90" cy="-62" rx="20" ry="16" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
{person(460,346,1.1,-1,'violet','violet','reach','bun','smile')}
<g transform="translate(390 220)">
  <path d="M-30-24h60v48h-60z" class="coral o"/>
  <path d="M-10-38h20v14h-20z" class="corald o"/>
</g>
{ck(300,150,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tropical', 'やしの木と強い日ざしの熱帯のイラスト。', f"""
{sun(480,110,50)}
<g transform="translate(200 330)">
  <path d="M-10 0q-6-100 10-150" fill="none" stroke="{TONES['gold'][2]}" stroke-width="18"/>
  <path d="M0-150q-60-20-90 20 60 14 90-20zM0-150q60-20 90 20-60 14-90-20zM0-150q-20-50-70-56 20 50 70 56zM0-150q20-50 70-56-20 50-70 56z" class="green o"/>
  <circle cx="4" cy="-140" r="12" class="goldd o"/>
</g>
<path d="M0 340h600v60H0z" fill="#f0e3c8"/>
<path d="M0 340h600" class="a"/>
""", ground=False)

add('unemployment', '働き口がなく職を探す人が並ぶイラスト。', f"""
<g transform="translate(420 220)">
  <path d="M-130-120h260v220h-260z" fill="#fffdf6" class="o"/>
</g>
{xx(420,220,1.6)}
{person(120,356,0.9,1,'teal','blue','carry','short','sad')}
{person(210,356,0.9,1,'coral','gold','carry','bob','sad')}
{person(300,356,0.9,1,'gold','violet','carry','short','sad')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('varied', '色も形もさまざまなイラスト。', f"""
<circle cx="140" cy="200" r="44" class="tealp o"/>
<path d="M240 160h90v90h-90z" class="coralp o"/>
<path d="M420 250l50-90 50 90z" class="goldp o"/>
<ellipse cx="180" cy="320" rx="60" ry="34" class="violetp o"/>
<path d="M290 290h100v60h-100z" class="greenp o"/>
<circle cx="480" cy="330" r="34" class="bluep o"/>
""", ground=False)

add('accomplishment', 'やり遂げて手にした成果のイラスト。', f"""
<g transform="translate(200 230)">
  <path d="M-110-130h220v260h-220z" class="paper"/>
  <g fill="none" stroke="{GRN}" stroke-width="8">{''.join(f'<path d="M-80 {-70+i*50}l12 14 26-30"/>' for i in range(4))}</g>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-20 {-66+i*50}h100"/>' for i in range(4))}</g>
</g>
<g transform="translate(450 260)">
  <path d="M-60-100h120v46q0 70-60 88-60-18-60-88z" class="gold o"/>
  <path d="M-60-86q-44 0-44 30t44 30M60-86q44 0 44 30t-44 30" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10"/>
  <path d="M-14 34h28v40h-28z" class="goldd o"/>
  <path d="M-60 74h120v26H-60z" class="goldd o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('activation', 'ボタンを押して働き始めるイラスト。', f"""
<g transform="translate(400 240)">
  <path d="M-130-120h260v240h-260z" class="bluep o"/>
  <path d="M-90-80h180v120h-180z" class="ink"/>
  <g fill="{TONES['green'][0]}"><circle cx="0" cy="80" r="20"/></g>
</g>
{hand(150,240,1)}
<g class="a" marker-end="url(#ar)"><path d="M220 240h50"/></g>
<g class="golds"><path d="M400 90v-24M300 120l-20-20M500 120l20-20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('administration', '判と書類で組織を動かす行政のイラスト。', f"""
{building(180,300,0.8,'violet')}
<g transform="translate(430 240)">
  <path d="M-110-120h220v240h-220z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-70 {-70+i*44}h140"/>' for i in range(4))}</g>
  <circle cx="50" cy="80" r="28" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M280 240h30"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('aftermath', '嵐が去ったあとの散らかりのイラスト。', f"""
{cloud(120,90,1.1,'blue')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M190 110h100"/></g>
<g transform="translate(400 300)">
  <path d="M-90 0v-70h50l-10 30 20-30h30V0z" fill="#dfe6ea" class="o"/>
</g>
<g class="goldp o">
  <path d="M180 340l40-16 12 34-40 12z"/><path d="M270 360l36 12-10 30-36-12z"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 8"><path d="M160 300q60-30 110-10"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('agenda', '会議で話す項目を並べた表のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-190-150h380v300h-380z" class="paper"/>
  <path d="M-150-110h300v40h-300z" class="teal o"/>
  <g class="tealp o">{''.join(f'<circle cx="-120" cy="{-30+i*50}" r="16"/>' for i in range(4))}</g>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-90 {-30+i*50}h230"/>' for i in range(4))}</g>
</g>
""", ground=False)

add('aggression', '前へ押し出す攻めの構えのイラスト。', f"""
{person(220,352,1.3,1,'coral','blue','reach','short','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="12" marker-end="url(#ar)"><path d="M310 220h120"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M150 190l-16-22M270 170v-24"/>
</g>
{person(500,352,1.05,-1,'teal','gold','stand','bob','sad')}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('agriculture', '田畑と納屋と収穫のある農業のイラスト。', f"""
<g transform="translate(470 280)">
  <path d="M-80 0v-70h160V0z" class="coral o"/>
  <path d="M-94-70L0-126l94 56z" class="corald o"/>
  <path d="M-26-40h52V0h-52z" fill="#fffdf6" class="o"/>
</g>
<path d="M0 300h600v100H0z" fill="#e8ded2"/>
<g fill="none" stroke="#c9b79f" stroke-width="6">{''.join(f'<path d="M0 {330+i*30}h600"/>' for i in range(2))}</g>
<g class="golds" stroke-width="5">{''.join(f'<path d="M{90+i*60} 300v-70"/>' for i in range(5))}</g>
<g class="gold o">{''.join(f'<ellipse cx="{90+i*60}" cy="216" rx="12" ry="26"/>' for i in range(5))}</g>
<path d="M0 300h600" class="a"/>
""", ground=False)

add('assembly', '人が集まって開かれる集まりのイラスト。', f"""
<g transform="translate(300 130)">
  <path d="M-160-60h320v100h-320z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"><path d="M-120-30h240M-120 0h180"/></g>
</g>
{sit(140,376,0.8,1,'teal','blue','short','neutral','lap')}
{sit(250,376,0.8,1,'coral','gold','bob','neutral','lap')}
{sit(360,376,0.8,1,'gold','violet','short','neutral','lap')}
{sit(470,376,0.8,1,'green','blue','bun','neutral','lap')}
<path d="M60 390h480" class="a"/>
""", ground=True)

add('assessment', '出来ばえを点数で見きわめるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-150h380v300h-380z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-150 {-100+i*44}h190"/>' for i in range(4))}</g>
  <g fill="none" stroke="{GRN}" stroke-width="8">{''.join(f'<path d="M70 {-106+i*44}l12 14 26-30"/>' for i in range(3))}</g>
  <path d="M-150 90h300v50h-300z" class="tealp o"/>
</g>
{star(520,140,28,'gold')}
""", ground=False)

add('asset', 'こちら側に積み上がる強みのイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-8-80h16v170h-16z" class="ink"/>
  <path d="M-60 90h120v20H-60z" class="ink"/>
  <path d="M-120-76h240v12h-240z" class="ink"/>
  <path d="M-120-64v50M120-64v20" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-170 6h100q0 36-50 36t-50-36z" class="goldp o"/>
  <path d="M70-24h100q0 36-50 36t-50-36z" class="tealp o"/>
</g>
<g class="gold o"><ellipse cx="180" cy="222" rx="30" ry="13"/><ellipse cx="180" cy="200" rx="30" ry="13"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('authority', 'バッジを持ち決める力があるイラスト。', f"""
{person(240,352,1.35,1,'violet','blue','point','bun','neutral')}
<g transform="translate(170 250)">
  <circle r="30" class="gold o"/>
  <path d="M0-16l7 14 16 2-12 12 3 16-14-8-14 8 3-16-12-12 16-2z" class="goldd"/>
</g>
{person(470,356,0.85,-1,'teal','blue','stand','short','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M340 250h70"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('autonomy', '自分たちのことは自分たちで決めるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-240-140q100-40 240-10t240 0v240q-140 40-240 0t-240 10z" class="greenp o"/>
  <path d="M-60-60q80-30 160 0v130q-80 30-160 0z" class="coralp o"/>
  <path d="M-60-60q80-30 160 0v130q-80 30-160 0z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10"/>
</g>
<g transform="translate(300 200)">
  <path d="M-6 60V-60" class="a"/>
  <path d="M-6-60h70v44H-6z" class="coral o"/>
</g>
""", ground=False)

print(len(W), ' '.join(W))
print(sheet(W))
