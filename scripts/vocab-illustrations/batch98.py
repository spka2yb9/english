"""第98回: 副詞中心の45語。"""
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

add('incredibly', '信じられないほどの値におどろくイラスト。', f"""
<g transform="translate(330 250)">
  <g class="coral o">{''.join(f'<rect x="{-200+i*60}" y="{60-(14+i*i*4)}" width="44" height="{14+i*i*4}"/>' for i in range(7))}</g>
  <path d="M-210 60h430" class="a"/>
</g>
{person(120,376,0.7,1,'teal','blue','up','short','surprised')}
<g fill="{TONES['coral'][0]}"><rect x="510" y="80" width="22" height="60" rx="11"/><circle cx="521" cy="160" r="12"/>
<rect x="550" y="80" width="22" height="60" rx="11"/><circle cx="561" cy="160" r="12"/></g>
""", ground=False)

add('inevitably', 'ほかに道がなくそうなるほかないイラスト。', f"""
<path d="M60 150L440 330H60z" class="greenp o"/>
<circle cx="140" cy="180" r="26" class="teal o"/>
<g transform="translate(470 330)">
  <ellipse rx="70" ry="24" fill="#5e4a3c" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M180 200q160 60 260 110"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="8"><path d="M300 120v80M420 90v110"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('ironically', '日照りの日に大きな傘をさす皮肉なイラスト。', f"""
{sun(480,100,46)}
{person(230,352,1.15,1,'coral','blue','hold','short','neutral')}
<g transform="translate(230 200)">
  <path d="M-90 0q0-90 90-90t90 90z" class="bluep o"/>
  <path d="M0 0v100q0 24 24 24" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
{cloud(120,120,1,'blue')}
{xx(120,120,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('largely', '大部分がひとつで占められているイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-240-70h380v140h-380z" class="teal o"/>
  <path d="M140-70h100v140H140z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M60 340h380M60 340v-24M440 340v-24"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('moreover', 'その上にもうひとつ加わるイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-140-40h280v40h-280z" class="teal o"/>
  <path d="M-140-90h280v50h-280z" class="teal o"/>
</g>
<g transform="translate(300 150)">
  <path d="M-140-30h280v60h-280z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 60v50"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"><path d="M500 150h50M525 125v50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('namely', 'ひとまとまりの中身を名指しで挙げるイラスト。', f"""
<g transform="translate(160 230)">
  <path d="M-90-90h180v180h-180z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 230h60"/></g>
<g transform="translate(460 230)">
  <circle cx="-60" cy="-50" r="34" class="teal o"/>
  <path d="M20-84h68v68H20z" class="coral o"/>
  <path d="M-60 20l40 60h-80z" class="gold o"/>
  <circle cx="54" cy="50" r="30" class="violet o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('nevertheless', 'さえぎりがあってもそれでも進むイラスト。', f"""
{person(150,352,1.15,1,'teal','blue','walk','short','neutral')}
<g transform="translate(320 260)">
  <path d="M-14-100h28v200h-28z" class="ink"/>
  <path d="M-130-100h260v40h-260z" class="coral o"/>
  <g fill="none" stroke="#fffdf6" stroke-width="6">{''.join(f'<path d="M{-110+i*40} -100l-24 40"/>' for i in range(7))}</g>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="8" stroke-dasharray="16 12" marker-end="url(#ar)"><path d="M230 320h250"/></g>
{ck(500,190,1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('precisely', '寸分たがわずぴたりと合わせるイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="130" fill="#fffdf6" class="o"/>
  <circle r="90" class="coralp o"/>
  <circle r="50" fill="#fffdf6" class="o"/>
  <circle r="14" class="coral o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-130 0h260M0-130v260"/></g>
</g>
<g transform="translate(300 220) rotate(42)">
  <path d="M4 0h160v8H4z" fill="{TONES['gold'][2]}"/>
  <path d="M150-12h34v32h-34z" class="tealp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('presently', '今この時を指すイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M60 250h480"/></g>
<g class="ink">{''.join(f'<circle cx="{130+i*90}" cy="250" r="9"/>' for i in range(5))}</g>
<circle cx="310" cy="250" r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
<g transform="translate(310 120)">
  <circle r="50" fill="#fffdf6" class="o"/>
  <path d="M0 0v-32M0 0l22 14" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <circle r="6" class="ink"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M310 180v40"/></g>
""", ground=False, arrow=True)

add('preside', '壇上から会をとりしきるイラスト。', f"""
{person(300,250,1.2,1,'violet','blue','point','bun','neutral')}
<g transform="translate(300 260)">
  <path d="M-90-20h180v30h-180z" class="goldd o"/>
  <path d="M-70 10h140v40h-140z" class="gold o"/>
</g>
{sit(140,376,0.8,1,'teal','blue','short','neutral','lap')}
{sit(260,376,0.8,1,'coral','gold','bob','neutral','lap')}
{sit(380,376,0.8,-1,'gold','violet','short','neutral','lap')}
{sit(500,376,0.8,-1,'green','blue','bun','neutral','lap')}
<path d="M60 390h480" class="a"/>
""", ground=True)

add('president', '国旗を背に執務する大統領のイラスト。', f"""
<g transform="translate(470 240)">
  <path d="M-6 140V-120" class="a"/>
  <path d="M-6-120h110v76H-6z" class="coral o"/>
</g>
{person(230,300,1.2,1,'violet','blue','point','short','neutral')}
<g transform="translate(230 330)">
  <path d="M-130-30h260v20h-260z" class="goldd o"/>
  <path d="M-100-10v46M100-10v46" class="a"/>
</g>
<g transform="translate(230 240)">
  <circle r="26" class="gold o"/>
  <path d="M0-14l6 12 14 2-10 10 2 14-12-7-12 7 2-14-10-10 14-2z" class="goldd"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('primarily', 'いちばん主となるものを示すイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-230-120h180v240h-180z" class="teal o"/>
  <path d="M-30-60h100v180h-100z" class="tealp o"/>
  <path d="M90-20h100v140H90z" class="tealp o"/>
</g>
{star(160,140,30,'gold')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('purely', '混じり気のない澄んだ水のイラスト。', f"""
<g transform="translate(220 250)">
  <path d="M-70-100h140l-16 200h-108z" fill="#fffdf6" class="o"/>
  <path d="M-62-40h124l-12 140h-100z" class="bluep o"/>
</g>
{ck(220,140,1)}
<g transform="translate(450 250)">
  <path d="M-70-100h140l-16 200h-108z" fill="#fffdf6" class="o"/>
  <path d="M-62-40h124l-12 140h-100z" class="goldd o" opacity="0.7"/>
  <g fill="{INK}" opacity="0.6"><circle cx="-20" cy="20" r="7"/><circle cx="20" cy="60" r="6"/><circle cx="6" cy="-10" r="5"/></g>
</g>
{xx(450,140,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('qualified', '資格を持っていることを示すイラスト。', f"""
{person(170,352,1.25,1,'violet','blue','carry','bun','smile')}
<g transform="translate(400 230)">
  <path d="M-140-120h280v240h-280z" class="paper"/>
  <path d="M-110-90h220v40h-220z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-110-20h220M-110 14h180"/></g>
  <circle cx="80" cy="70" r="32" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
{ck(270,150,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('qualify', '試験を通って先へ進む資格を得るイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-20-140h40v280h-40z" class="ink"/>
  <path d="M-160-140h140v40h-140zM20-140h140v40H20z" class="teal o"/>
</g>
{person(150,352,1,-1,'coral','blue','walk','short','neutral')}
{person(460,352,1.1,1,'teal','gold','up','bob','smile')}
<g class="a" marker-end="url(#ar)"><path d="M210 320h150"/></g>
{ck(460,180,1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('rapidly', 'ものすごい速さで進むイラスト。', f"""
<g transform="translate(360 250)">
  <path d="M-120 0v-40l40-50h150l50 50V0z" class="coral o"/>
  <g fill="#fffdf6" class="o"><rect x="-70" y="-80" width="60" height="36"/><rect x="0" y="-80" width="60" height="36"/></g>
  <g fill="{INK}"><circle cx="-70" cy="6" r="24"/><circle cx="80" cy="6" r="24"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="8" stroke-linecap="round">
  <path d="M60 190h130M40 240h140M60 290h120"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 120h340"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('readily', '求められてすぐ快く差し出すイラスト。', f"""
{person(160,352,1.2,1,'teal','blue','give','short','smile')}
<g transform="translate(330 250)">
  <path d="M-50-40h100v80h-100z" class="gold o"/>
</g>
{hand(500,250,-1)}
<g class="a" marker-end="url(#ar)"><path d="M250 180h150"/></g>
{ck(330,140,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('reasonably', '無理のない釣り合った程度のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-8-60h16v170h-16z" class="ink"/>
  <path d="M-70 110h140v20H-70z" class="ink"/>
  <path d="M-140-56h280v12h-280z" class="ink"/>
  <path d="M-140-44v34M140-44v34" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-190-10h100q0 40-50 40t-50-40z" class="tealp o"/>
  <path d="M90-10h100q0 40-50 40t-50-40z" class="tealp o"/>
</g>
{ck(500,150,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('regardless', '雨でも構わず進むイラスト。', f"""
{cloud(180,100,1.4,'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
  {''.join(f'<path d="M{110+i*32} {180+(i%3)*16}l-14 46"/>' for i in range(7))}
</g>
{person(330,352,1.2,1,'coral','blue','walk','short','smile')}
<g class="a" marker-end="url(#ar)"><path d="M410 300h110"/></g>
{xx(180,300,0.8,MUTED)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('regulate', '弁で流れを決められた量に抑えるイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="44" stroke-linecap="round"><path d="M60 250h480"/></g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="16" stroke-linecap="round"><path d="M60 250h480"/></g>
<g transform="translate(300 250)">
  <path d="M-40-40h80v80h-80z" fill="{MUTED}" class="o"/>
  <path d="M-6-100h12v60h-12z" fill="{MUTED}"/>
  <path d="M-40-110h80v16h-80z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M340 130a60 60 0 0 1 50 30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('relate', 'ふたつを線でつないで結びつけるイラスト。', f"""
<circle cx="180" cy="220" r="70" class="tealp o"/>
<circle cx="420" cy="220" r="70" class="coralp o"/>
<g fill="none" stroke="{INK}" stroke-width="10"><path d="M250 220h100"/></g>
<circle cx="180" cy="220" r="18" class="teal o"/>
<circle cx="420" cy="220" r="18" class="coral o"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('related', 'つながりのある間柄を示すイラスト。', f"""
<g transform="translate(300 160)">
  <circle r="40" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M0 40v50M-140 90h280M-140 90v40M140 90v40M0 90v40" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
<g>
  <circle cx="160" cy="330" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="300" cy="330" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="440" cy="330" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('relatively', '基準と比べてどれくらいかを示すイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-200 20h100v40h-100z" class="tealp o"/>
  <path d="M-60-60h100v120H-60z" class="teal o"/>
  <path d="M80-20h100v80H80z" class="tealp o"/>
  <path d="M-230-60h460" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M540 310V190"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('remarkably', '目をみはるほど際立った結果のイラスト。', f"""
<g transform="translate(300 250)">
  <g class="tealp o">{''.join(f'<rect x="{-220+i*70}" y="10" width="50" height="50"/>' for i in range(4))}</g>
  <path d="M100-160h60v220h-60z" class="coral o"/>
  <path d="M-230 60h420" class="a"/>
</g>
{star(500,120,32,'gold')}
{person(120,376,0.65,1,'teal','blue','up','short','surprised')}
""", ground=False)

add('respectively', 'それぞれ順に対応づけるイラスト。', f"""
<g transform="translate(200 220)">
  <circle cx="0" cy="-90" r="34" class="teal o"/>
  <path d="M-34-34h68v68h-68z" class="coral o"/>
  <path d="M0 60l40 68h-80z" class="gold o"/>
</g>
<g transform="translate(420 220)">
  <circle cx="0" cy="-90" r="34" class="tealp o"/>
  <path d="M-34-34h68v68h-68z" class="coralp o"/>
  <path d="M0 60l40 68h-80z" class="goldp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 130h110M250 220h110M250 320h110"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('roughly', 'きっちりでなくおおよそで測るイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-160-100h320v200h-320z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="14 12"><path d="M120 130h360v200H120z"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round">
  <path d="M240 370q26-16 52 0t52 0"/>
  <path d="M240 390q26-16 52 0t52 0"/>
</g>
""", ground=False)

add('seemingly', '見かけと中身が違うことを示すイラスト。', f"""
{face(200,220,88,'smile')}
<g transform="translate(430 220)">
  <path d="M-90-70q90-46 180 0 0 130-90 130T-90-70z" class="goldp o"/>
  <g fill="{INK}"><path d="M-50-34q24-16 46 0-22 12-46 0zM20-34q24-16 46 0-22 12-46 0z"/></g>
  <path d="M-30 40q30-20 60 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="5"/>
</g>
<g transform="translate(310 130)">
  <path d="M-24-26q0-26 24-26t24 24q0 20-24 26v12" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"/>
  <circle cy="34" r="7" class="coral"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('seldom', 'ひと月に一度あるかどうかのイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-220-150h440v300h-440z" class="paper"/>
  <path d="M-220-150h440v50h-440z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M-220 {-50+i*50}h440"/>' for i in range(4))}
    {''.join(f'<path d="M{-157+c*63} -100v250"/>' for c in range(6))}
  </g>
  <circle cx="31" cy="0" r="22" class="coralp o"/>
</g>
{xx(520,120,0.8)}
""", ground=False)

add('severely', 'ひどく傷んでいることを示すイラスト。', f"""
<g transform="translate(230 250)">
  <path d="M-110-110h220v220h-220z" class="tealp o"/>
  <g fill="none" stroke="{INK}" stroke-width="6">
    <path d="M-110-40l70 30-40 50 60 70M40-110l-20 70 60 20-30 60 60 70"/>
  </g>
</g>
<g transform="translate(460 260)">
  <path d="M-90 0a90 90 0 0 1 180 0z" fill="#fffdf6" class="o"/>
  <path d="M-90 0h180" class="a"/>
  <path d="M0 0l84-30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"/>
  <circle r="9" class="ink"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('shame', '恥ずかしくて顔を覆うイラスト。', f"""
{person(300,352,1.35,1,'coral','blue','think','short','sad')}
{hand(250,240,1)}
<g fill="{TONES['coral'][0]}" opacity="0.55"><circle cx="336" cy="240" r="16"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M420 210l20-24M450 260h28"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('shortly', 'もうすぐその時が来るイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="130" fill="#fffdf6" class="o"/>
  <path d="M0 0v-90" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <path d="M0 0l40 24" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"/>
  <circle r="10" class="ink"/>
  <path d="M0-130A130 130 0 0 1 44-122L14-8z" class="coralp"/>
  <g fill="{INK}">{''.join(f'<rect x="-4" y="-120" width="8" height="18" transform="rotate({a})"/>' for a in range(0,360,30))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M470 130l-60 40"/></g>
""", ground=False, arrow=True)

add('significantly', '目に見えて大きく変わるイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-200 0h110v60h-110z" class="tealp o"/>
  <path d="M90-160h110v220H90z" class="coral o"/>
  <path d="M-210 60h420" class="a"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M520 310V100"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M480 310h80M480 100h80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('similarly', 'よく似たものを同じように扱うイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
  <circle r="46" class="teal o"/>
</g>
<g transform="translate(430 230)">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
  <circle r="46" class="teal o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"><path d="M272 210q28-16 56 0M272 250q28-16 56 0"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('simultaneously', '同じ時刻にふたつのことが起きるイラスト。', f"""
<g transform="translate(160 230)">
  <path d="M-100-110h200v220h-200z" fill="#fffdf6" class="o"/>
</g>
{person(160,300,0.8,1,'teal','blue','walk','short','smile')}
<g transform="translate(440 230)">
  <path d="M-100-110h200v220h-200z" fill="#fffdf6" class="o"/>
</g>
{person(440,300,0.8,-1,'coral','gold','up','bob','smile')}
<g transform="translate(300 100)">
  <circle r="56" fill="#fffdf6" class="o"/>
  <path d="M0 0v-36M0 0l24 14" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <circle r="6" class="ink"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"><path d="M244 100H180M356 100h64"/></g>
""", ground=False)

add('solely', 'たったひとりだけで受け持つイラスト。', f"""
{person(300,352,1.3,1,'teal','blue','carry','short','neutral')}
{box(300,240,140,90,26,'gold')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><circle cx="300" cy="250" r="180"/></g>
<g opacity="0.25">{person(110,356,0.7,1,'teal','blue','stand','short','neutral')}</g>
<g opacity="0.25">{person(510,356,0.7,-1,'teal','blue','stand','bob','neutral')}</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('somehow', '曲がりくねってもどうにか着くイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="14 12" marker-end="url(#ar)">
  <path d="M110 320q60-120 150-60t60-140 130 60-40 160"/>
</g>
{person(110,352,1,1,'teal','blue','walk','short','neutral')}
<g transform="translate(500 280)">
  <path d="M-6 100V-30" class="a"/>
  <path d="M-6-30h80l-16 24 16 24H-6z" class="coral o"/>
</g>
<g transform="translate(300 120)">
  <path d="M-22-24q0-24 22-24t22 22q0 18-22 24v10" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"/>
  <circle cy="30" r="6" class="coral"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('sometime', 'いつかは分からないが先の日を指すイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-220-150h440v300h-440z" class="paper"/>
  <path d="M-220-150h440v50h-440z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M-220 {-50+i*50}h440"/>' for i in range(4))}
    {''.join(f'<path d="M{-157+c*63} -100v250"/>' for c in range(6))}
  </g>
  <g transform="translate(100 50)">
    <path d="M-18-20q0-20 18-20t18 16q0 14-18 20v8" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"/>
    <circle cy="26" r="6" class="coral"/>
  </g>
</g>
""", ground=False)

add('somewhat', '半ばくらいまでの程度を示すイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-220-50h440v100h-440z" fill="#fffdf6" class="o"/>
  <path d="M-220-50h200v100h-200z" class="teal o"/>
  <path d="M-20-70v140" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="10 8"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M{80+i*110} 320v16"/>' for i in range(5))}</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('specialize', 'ひとつの分野だけを深く究めるイラスト。', f"""
<g transform="translate(300 230)">
  <g class="tealp o">{''.join(f'<circle cx="{-200+c*80}" cy="{-70+r*70}" r="26"/>' for r in range(3) for c in range(6))}</g>
  <circle cx="-40" cy="0" r="26" class="coral o"/>
</g>
<g transform="translate(260 230)">
  <circle r="70" fill="none" stroke="{INK}" stroke-width="9"/>
  <circle r="60" fill="#fffdf6" opacity="0.35"/>
  <circle r="26" class="coral o"/>
  <path d="M50 50l50 50" fill="none" stroke="{INK}" stroke-width="14" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('strengthen', '補強を当てて強くするイラスト。', f"""
<g transform="translate(180 240)">
  <path d="M-90-14h180v28h-180z" fill="#b9c2c9" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 240h50"/></g>
<g transform="translate(460 240)">
  <path d="M-90-14h180v28h-180z" fill="#b9c2c9" class="o"/>
  <path d="M-90-46h180v26h-180zM-90 20h180v26h-180z" fill="#b9c2c9" class="o"/>
  <g class="goldd o"><circle cx="-60" cy="0" r="12"/><circle cx="0" cy="0" r="12"/><circle cx="60" cy="0" r="12"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="6"><path d="M180 300v40M460 300v40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('strictly', '寸分の狂いも許さず厳しく当てるイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-160-60h320v60h-320z" class="tealp o"/>
  <path d="M-200-100h400v40h-400z" class="goldp o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">{''.join(f'<path d="M{-180+i*40} -100v{24 if i%2==0 else 14}"/>' for i in range(10))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M140 190v-40M460 190v-40"/></g>
{ck(300,350,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('subsequently', 'そのあとに続いて起こるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-230-80h160v160h-160z" class="teal o"/>
  <path d="M70-80h160v160H70z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M220 220h80"/></g>
<g transform="translate(260 340)">
  <circle r="30" fill="#fffdf6" class="o"/>
  <path d="M0 0v-20M0 0l14 8" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('sufficiently', '必要な線まで足りているイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-110-130h220v260h-220z" fill="#fffdf6" class="o"/>
  <path d="M-110-40h220v170h-220z" class="teal o"/>
  <path d="M-130-40h260v10h-260z" class="coral o"/>
</g>
{ck(490,180,1.1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('temporarily', '一時のあいだだけ置かれるイラスト。', f"""
<g transform="translate(280 300)">
  <path d="M-130 0l130-160 130 160z" class="coralp o"/>
  <path d="M-44 0l44-56 44 56z" class="corald o"/>
</g>
<g transform="translate(490 200)">
  <circle r="56" fill="#fffdf6" class="o"/>
  <path d="M0 0v-36M0 0l24 14" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <circle r="6" class="ink"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M420 300h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('thoroughly', '隅から隅まで徹底して仕上げるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" fill="#fffdf6" class="o"/>
  <path d="M-200 0h400M0-140v280" class="a"/>
</g>
{ck(190,150,0.85)}
{ck(410,150,0.85)}
{ck(190,290,0.85)}
{ck(410,290,0.85)}
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
