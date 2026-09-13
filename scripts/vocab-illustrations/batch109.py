"""第109回: 副詞・句動詞45語。"""
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
def gauge(x,y,r=110,ang=-40,cls='coral'):
    import math
    ex, ey = x+r*0.8*math.cos(math.radians(ang)), y+r*0.8*math.sin(math.radians(ang))
    return (f'<path d="M{x-r} {y}a{r} {r} 0 0 1 {2*r} 0" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>'
            f'<path d="M{x-r} {y}h{2*r}" class="a"/>'
            f'<path d="M{x} {y}L{ex:.0f} {ey:.0f}" fill="none" stroke="{TONES[cls][0]}" stroke-width="8" stroke-linecap="round"/>'
            f'<circle cx="{x}" cy="{y}" r="10" class="ink"/>')

add('accordingly', '相手の動きに合わせて調子を変えるイラスト。', f"""
<g transform="translate(170 230)">
  <g class="teal o">{''.join(f'<rect x="{-80+i*54}" y="{60-(30+i*30)}" width="40" height="{30+i*30}"/>' for i in range(3))}</g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 240h60"/></g>
<g transform="translate(460 230)">
  <g class="coralp o">{''.join(f'<rect x="{-80+i*54}" y="{60-(30+i*30)}" width="40" height="{30+i*30}"/>' for i in range(3))}</g>
</g>
{ck(300,340,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('accurately', '測った値が本当の値とぴたり合うイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-220-60h440v60h-440z" class="goldp o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">{''.join(f'<path d="M{-200+i*40} -60v{26 if i%2==0 else 16}"/>' for i in range(11))}</g>
  <path d="M-40-90h80v30h-80z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="8 8"><path d="M300 150v-60"/></g>
{ck(470,150,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('additionally', 'さらにもうひとつ加えるイラスト。', f"""
<g transform="translate(200 280)">
  <path d="M-110-40h220v90h-220z" class="teal o"/>
</g>
<g transform="translate(420 200)">
  <path d="M-70-40h140v80h-140z" class="coralp o"/>
</g>
<g fill="none" stroke="{GRN}" stroke-width="14" stroke-linecap="round"><path d="M300 150h50M325 125v50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('adequately', '荷を支えるのに足りる強さのイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-200-20h400v40h-400z" fill="#b9c2c9" class="o"/>
  <path d="M-200 20v70M200 20v70" fill="none" stroke="{MUTED}" stroke-width="16"/>
</g>
{box(300,230,180,90,0,'gold')}
{ck(500,180,1)}
<path d="M60 390h480" class="a"/>
""", ground=True)

add('afterwards', 'そのあとに次が来るイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M60 250h480"/></g>
<circle cx="180" cy="250" r="30" class="teal o"/>
<circle cx="400" cy="250" r="30" class="coral o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M220 330h140"/></g>
""", ground=False, arrow=True)

add('albeit', 'よい結果だが小さな難もあるイラスト。', f"""
<g transform="translate(280 240)">
  <path d="M-140-120h280v240h-280z" class="teal o"/>
</g>
{ck(280,240,1.6)}
<g transform="translate(480 330)">
  <path d="M-50-30h100v60h-100z" class="coralp o"/>
</g>
{xx(480,330,0.7)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('allegedly', '確かではないが噂ではそうらしいイラスト。', f"""
{person(160,352,1.2,1,'teal','blue','point','short','neutral')}
<g transform="translate(400 200)">
  <path d="M-120-80h240v130h-240zM-80 50l-14 34 44-34z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="12 10"><path d="M-80-40h160M-80-6h120"/></g>
</g>
{qmark(490,320,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('altogether', '全部合わせた数のイラスト。', f"""
<g transform="translate(300 230)">
  <g class="tealp o">{''.join(f'<circle cx="{-200+i*60}" cy="-60" r="24"/>' for i in range(3))}</g>
  <g class="coralp o">{''.join(f'<circle cx="{-200+i*60}" cy="20" r="24"/>' for i in range(4))}</g>
  <g class="goldp o">{''.join(f'<circle cx="{-200+i*60}" cy="100" r="24"/>' for i in range(2))}</g>
</g>
<g fill="none" stroke="{GRN}" stroke-width="6"><path d="M50 150h20M50 150v170M50 320h20M50 235h-20"/></g>
<g transform="translate(480 230)">
  <path d="M-60-60h120v120h-120z" class="teal o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('amid', '波のただ中に浮かぶ舟のイラスト。', f"""
<path d="M0 200h600v200H0z" class="bluep"/>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="6">
  <path d="M0 240q50-30 100 0t100 0 100 0 100 0 100 0 100 0"/>
  <path d="M0 320q50-30 100 0t100 0 100 0 100 0 100 0 100 0"/>
</g>
<g transform="translate(300 250)">
  <path d="M-90 0h180l-24 40h-132z" class="coral o"/>
  <path d="M-6-70h12v70H-6z" fill="{TONES['gold'][2]}"/>
  <path d="M6-70h70l-20 30 20 30H6z" class="tealp o"/>
</g>
""", ground=False)

add('annually', '一年に一度めぐってくるイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="18" stroke-linecap="round">
  <path d="M300 100a130 130 0 1 1-92 38"/>
</g>
<path d="M300 62l56 38-56 38z" fill="{TONES['teal'][2]}" stroke="{INK}" stroke-width="3"/>
<g transform="translate(300 230)">
  <path d="M-70-60h140v120h-140z" class="paper"/>
  <path d="M-70-60h140v30h-140z" class="coral o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70 0h140M-24-30v90M24-30v90"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('apparently', '見たところそうらしいイラスト。', f"""
{person(160,352,1.2,1,'teal','blue','think','short','neutral')}
<g transform="translate(420 230)" opacity="0.5">
  <path d="M-110-110h220v220h-220z" class="tealp o"/>
  <circle r="60" class="teal o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M250 250h50"/></g>
{qmark(320,130,1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('appeal', '心を引きつける魅力のイラスト。', f"""
<g transform="translate(380 230)">
  <path d="M-130-130h260v260h-260z" class="paper"/>
  <circle cx="0" cy="-40" r="60" class="coralp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="6"><path d="M-90 60h180M-90 90h130"/></g>
</g>
{person(140,352,1.15,1,'teal','blue','reach','short','smile')}
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M230 160q-18-24 0-34 18-10 18 14 0-24 18-14 18 10 0 34l-18 18z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('appropriately', '場に合ったものを選ぶイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-70-70h140v140h-140z" class="tealp o"/>
  <circle r="40" fill="#fffaf1" stroke="{INK}" stroke-width="3"/>
</g>
<circle cx="330" cy="250" r="40" class="teal o"/>
{ck(330,140,0.9)}
<g transform="translate(480 250)"><path d="M-40-40h80v80h-80z" class="coralp o"/></g>
{xx(480,140,0.8)}
<g class="a" marker-end="url(#ar)"><path d="M290 320h-60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('aside', 'わきへよけて道をあけるイラスト。', f"""
{person(180,352,1.2,-1,'teal','blue','stand','short','neutral')}
{person(420,352,1.2,1,'coral','gold','walk','bob','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M300 300h180"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M240 200h-60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('basically', '土台の部分がもとになっているイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-220-40h440v60h-440z" class="teal o"/>
  <path d="M-140-110h280v70h-280z" class="tealp o"/>
  <path d="M-70-170h140v60H-70z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><rect x="70" y="270" width="460" height="70" rx="14"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('break-into', '窓から押し入るイラスト。', f"""
<g transform="translate(340 240)">
  <path d="M-160-150h320v300h-320z" fill="#dfe6ea" class="o"/>
  <path d="M-90-100h180v140h-180z" class="bluep o"/>
  <g fill="none" stroke="{INK}" stroke-width="4"><path d="M-90-100l180 140M90-100L-90 40"/></g>
</g>
{person(140,352,1.15,1,'blue','blue','walk','cap','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M200 250h60"/></g>
{xx(490,140,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('bring-about', 'ハンドルを回して変化を起こすイラスト。', f"""
{hand(150,220,1)}
<g transform="translate(250 250)">
  <circle r="46" fill="none" stroke="{MUTED}" stroke-width="12"/>
  <path d="M0 0l40-24" fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M330 250h60"/></g>
<g transform="translate(470 250)">
  <circle r="70" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('broadly', '広い幅にわたって行きわたるイラスト。', f"""
<g class="tealp o">
  {''.join(f'<circle cx="{90+c*72}" cy="{180+r*80}" r="26"/>' for r in range(3) for c in range(7))}
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M300 380H60M300 380h240"/></g>
""", ground=False, arrow=True)

add('but', '一方こちらは違うと折り返すイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-90-90h180v180h-180z" class="tealp o"/>
</g>
{ck(170,350,0.8)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linejoin="round" marker-end="url(#ar)">
  <path d="M290 180h60l-30 60h60"/>
</g>
<g transform="translate(470 230)">
  <path d="M-90-90h180v180h-180z" class="coralp o"/>
</g>
{xx(470,350,0.8)}
""", ground=False, arrow=True)

add('by-no-means', 'まったくそうではないと打ち消すイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-130h380v260h-380z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-150 {-80+i*50}h300"/>' for i in range(4))}</g>
</g>
{xx(300,220,3)}
""", ground=False)

add('call-for', 'その場が道具を必要とするイラスト。', f"""
<g transform="translate(200 230)">
  <path d="M0-120l110 190h-220z" class="coralp o"/>
  <g fill="{TONES['coral'][2]}"><rect x="-11" y="-50" width="22" height="58" rx="11"/><circle cy="34" r="12"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M330 250h60"/></g>
<g transform="translate(470 250) rotate(20)">
  <path d="M-8-60h16v110h-16z" fill="{MUTED}" class="o"/>
  <path d="M-20-76h40v24h-40z" fill="{MUTED}" class="o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('characterize', '特徴を書き出して言い表すイラスト。', f"""
<g transform="translate(180 250)">
  <circle r="80" class="teal o"/>
  <path d="M-30-30h60v60h-60z" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M280 250h50"/></g>
<g transform="translate(460 240)">
  <path d="M-100-110h200v220h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-40 {-60+i*44}h100"/>' for i in range(4))}</g>
  <g fill="none" stroke="{GRN}" stroke-width="6">{''.join(f'<path d="M-70 {-66+i*44}l8 10 18-22"/>' for i in range(4))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('closely', 'すきまなくぴったり寄っているイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-180-90h170v180h-170z" class="teal o"/>
  <path d="M10-90h170v180H10z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M240 370h50M360 370h-50"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M290 340v50M310 340v50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('commonly', 'よく見かけるふつうの型のイラスト。', f"""
<g class="teal o">{''.join(f'<circle cx="{110+c*80}" cy="{200+r*80}" r="30"/>' for r in range(2) for c in range(6) if not (r==1 and c>3))}</g>
<circle cx="430" cy="280" r="30" class="coralp o"/>
<circle cx="510" cy="280" r="30" class="goldp o"/>
<g fill="none" stroke="{GRN}" stroke-width="5"><path d="M70 360h300M70 360v-24M370 360v-24"/></g>
""", ground=False)

add('confer', '向かい合って相談するイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-160-30h320v20h-320z" class="goldd o"/>
  <path d="M-130-10v46M130-10v46" class="a"/>
</g>
{sit(180,356,1,1,'violet','violet','short','neutral','lap')}
{sit(420,356,1,-1,'teal','blue','bun','neutral','lap')}
<g transform="translate(180 200)">
  <path d="M-56-34h112v56h-112zM-30 22l-10 24 30-24z" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(420 200)">
  <path d="M-56-34h112v56h-112zM30 22l10 24-30-24z" fill="#fffdf6" class="o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('consequently', 'それが元でこうなったと続けるイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 240h50"/></g>
<g transform="translate(400 240)">
  <path d="M-60-60h120v120h-120z" class="coralp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M480 240h30"/></g>
<g transform="translate(550 240)">
  <path d="M-40-40h80v80h-80z" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('considerably', '差がはっきり分かるほど大きいイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-220 0h110v60h-110z" class="tealp o"/>
  <path d="M100-190h110v250H100z" class="coral o"/>
  <path d="M-230 60h450" class="a"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M60 300V120"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M40 300h50M40 120h50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('consistently', 'いつも同じ結果になるイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M60 320h480"/></g>
<g class="teal o">{''.join(f'<rect x="{100+i*80}" y="180" width="50" height="120"/>' for i in range(6))}</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10"><path d="M70 180h480"/></g>
""", ground=False, arrow=True)

add('continually', '切れ目なく何度もくり返すイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M60 250h480"/></g>
<g class="coral">{''.join(f'<circle cx="{100+i*45}" cy="250" r="12"/>' for i in range(10))}</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)">{''.join(f'<path d="M{108+i*45} 320h30"/>' for i in range(9))}</g>
""", ground=False, arrow=True)

add('critically', '目盛りが赤の域まで振れて深刻なイラスト。', f"""
{gauge(300,300,160,-20,'coral')}
<g fill="{TONES['coral'][0]}" opacity="0.35"><path d="M300 300A160 160 0 0 0 460 300z" transform="rotate(-60 300 300)"/></g>
<g fill="{TONES['coral'][0]}"><rect x="480" y="130" width="24" height="70" rx="12"/><circle cx="492" cy="228" r="14"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('deeply', '深いところまで沈んでいるイラスト。', f"""
<path d="M0 140h600v260H0z" class="bluep"/>
<path d="M0 140h600" class="a"/>
<circle cx="300" cy="340" r="34" class="teal o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M480 150v160"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M450 145h60M450 340h60"/></g>
""", ground=False, arrow=True)

add('deliberately', '手元を見ながらゆっくり慎重に置くイラスト。', f"""
{hand(200,180,1)}
<g transform="translate(310 320)">
  <path d="M-140-20h280v20h-280z" class="goldd o"/>
  <path d="M-40-70h80v50h-80z" class="tealp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="6 10" marker-end="url(#ar)"><path d="M270 210l40 50"/></g>
{ck(490,180,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('desperately', '最後の望みに必死で手を伸ばすイラスト。', f"""
{person(230,352,1.3,1,'coral','blue','reach','short','sad')}
<g transform="translate(470 180)">
  <path d="M-40-40h80v80h-80z" class="goldp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M170 190l-16-24M290 170v-26"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M330 220h90"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('do-without', 'それがなくても済ませるイラスト。', f"""
{person(180,352,1.2,1,'teal','blue','stand','short','smile')}
<g transform="translate(430 250)" opacity="0.35">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
</g>
{xx(430,250,1.6)}
{ck(180,200,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('dramatically', '一気に大きく変わるイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-220 0h110v60h-110z" class="tealp o"/>
  <path d="M100-220h110v280H100z" class="coral o"/>
  <path d="M-230 60h450" class="a"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M120 290q80-40 250-200"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('drop-out', '途中でやめて列から抜けるイラスト。', f"""
{person(140,352,1,1,'teal','blue','walk','short','neutral')}
{person(250,352,1,1,'teal','blue','walk','bob','neutral')}
{person(360,352,1,1,'teal','blue','walk','short','neutral')}
{person(510,352,1,-1,'coral','gold','walk','bun','sad')}
<g class="a" marker-end="url(#ar)"><path d="M100 150h330"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M420 250q60 40 100 40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('emotionally', '気持ちが大きく動くイラスト。', f"""
{person(220,352,1.3,1,'coral','blue','up','short','sad')}
{drop(190,240,1.2,'blue')}
{drop(252,246,1.2,'blue')}
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2.5">
  <path d="M440 200q-30-38 0-54 30-16 30 22 0-38 30-22 30 16 0 54l-30 30z"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round"><path d="M360 260q20-20 0-40M330 290q40-40 0-80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('entirely', '欠けなく丸ごと全部のイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="150" class="teal o"/>
</g>
{ck(300,380,1)}
""", ground=False)

add('essentially', 'いちばん大事な芯を取り出すイラスト。', f"""
<g transform="translate(180 240)">
  <circle r="110" class="tealp o"/>
  <circle r="40" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M320 240h60"/></g>
<circle cx="460" cy="240" r="60" class="coral o"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('exclusively', 'ひとりだけが入れるイラスト。', f"""
<g transform="translate(360 260)">
  <path d="M-140 0h280v60h-280z" class="coral o"/>
  <path d="M-120-20h50v20h-50zM90-20h50v20H90z" fill="{TONES['gold'][2]}"/>
</g>
{person(300,260,1.1,1,'violet','violet','walk','bun','smile')}
{ck(300,140,0.8)}
{person(520,352,0.9,-1,'teal','blue','stand','short','sad')}
{xx(520,220,0.8)}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="12 10"><path d="M470 160v220"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('explicitly', 'あいまいでなくはっきり書いてあるイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-100-110h200v220h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="10 10"><path d="M-66-50h132M-66-10h100M-66 30h132"/></g>
</g>
{xx(170,350,0.8,MUTED)}
<g transform="translate(450 230)">
  <path d="M-100-110h200v220h-200z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="7"><path d="M-66-50h132M-66-10h100M-66 30h132"/></g>
</g>
{ck(450,350,0.9)}
""", ground=False)

add('extensively', '広い面をくまなく覆うイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-240-150h480v300h-480z" fill="#fffdf6" class="o"/>
  <g class="tealp o">{''.join(f'<rect x="{-230+c*70}" y="{-140+r*70}" width="60" height="60"/>' for r in range(4) for c in range(7))}</g>
</g>
{ck(300,380,0.8)}
""", ground=False)

add('fall-apart', 'ばらばらに崩れてしまうイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-70-70h140v140h-140z" class="tealp o"/>
  <path d="M-70 0h140M0-70v140" class="a"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 240h60"/></g>
<g class="tealp o">
  <path d="M400 170h60v60h-60z" transform="rotate(-18 430 200)"/>
  <path d="M480 200h60v60h-60z" transform="rotate(14 510 230)"/>
  <path d="M400 280h60v60h-60z" transform="rotate(24 430 310)"/>
  <path d="M490 300h60v60h-60z" transform="rotate(-10 520 330)"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('fall-behind', '後ろに引き離されるイラスト。', f"""
{person(430,352,1.15,1,'teal','blue','walk','short','neutral')}
{person(180,352,1.15,1,'coral','gold','walk','bob','sad')}
<g class="a" marker-end="url(#ar)"><path d="M120 150h400"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M260 250h-80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('firmly', 'びくともしないほど固く据えるイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-20-160h40v220h-40z" fill="{TONES['gold'][2]}"/>
  <path d="M-110 60h220v40h-220z" fill="#b9c2c9" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M120 200h100M480 200H380"/></g>
{xx(300,140,0.8,MUTED)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

print(len(W), ' '.join(W))
print(sheet(W))
