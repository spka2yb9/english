"""第108回: 残りの句動詞・名詞・副詞45語。"""
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
def clock(x,y,r=60,hand=-90):
    import math
    ex, ey = x+r*0.55*math.cos(math.radians(hand)), y+r*0.55*math.sin(math.radians(hand))
    return (f'<g><circle cx="{x}" cy="{y}" r="{r}" fill="#fffdf6" class="o"/>'
            f'<path d="M{x} {y}v-{r*0.6:.0f}" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M{x} {y}L{ex:.0f} {ey:.0f}" fill="none" stroke="{TONES["coral"][0]}" stroke-width="5" stroke-linecap="round"/>'
            f'<circle cx="{x}" cy="{y}" r="6" class="ink"/></g>')

add('it', 'そのものを指し示すイラスト。', f"""
<g transform="translate(400 240)">
  <path d="M-90-90h180v180h-180z" class="teal o"/>
</g>
{hand(150,240,1)}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M220 240h70"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="400" cy="240" r="120"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('indictment', '罪を問う書面を裁きの場に出すイラスト。', f"""
<g transform="translate(230 220)">
  <path d="M-140-150h280v300h-280z" class="paper"/>
  <path d="M-110-110h220v40h-220z" class="coral o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-110 {-30+i*44}h220"/>' for i in range(3))}</g>
  <circle cx="80" cy="100" r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
<g transform="translate(470 300) rotate(-24)">
  <path d="M-60-16h50v32h-50z" class="goldd o"/>
  <path d="M-10-9h110v18H-10z" class="gold o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M390 200h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('inmate', '番号をつけて収容されている人のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-180-140h360v290h-360z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="9">{''.join(f'<path d="M{-130+i*65} -140v290"/>' for i in range(5))}</g>
</g>
{person(300,340,0.9,1,'gold','gold','stand','short','neutral')}
<g transform="translate(300 268)">
  <path d="M-28-16h56v32h-56z" class="paper"/>
  <g fill="{INK}"><rect x="-14" y="-6" width="10" height="14"/><rect x="4" y="-6" width="10" height="14"/></g>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('leave', 'その場を離れて出ていくイラスト。', f"""
<g transform="translate(180 240)">
  <path d="M-130-150h260v300h-260z" fill="#dfe6ea" class="o"/>
  <path d="M-70-110h190v260H-70z" fill="#fffaf1" class="o"/>
  <circle cx="100" cy="20" r="8" class="ink"/>
</g>
{person(440,352,1.2,1,'teal','blue','walk','short','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M330 260h100"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('lost', 'こぼして無駄にしてしまったイラスト。', f"""
<g transform="translate(240 240) rotate(40)">
  <path d="M-50-60h100l-12 100h-76z" fill="#fffdf6" class="o"/>
</g>
<g class="bluep o">
  <path d="M300 300q50 40 30 70-46 12-46-30 0-24 16-40z"/>
  <ellipse cx="330" cy="378" rx="80" ry="18"/>
</g>
{xx(470,180,1.2)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('magistrate', '町の小さな法廷で裁く判事のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-170-30h340v80h-340z" class="goldd o"/>
  <path d="M-180-50h360v20h-360z" class="gold o"/>
</g>
{person(300,270,1.15,1,'violet','violet','stand','bun','neutral')}
<g transform="translate(440 180) rotate(-20)">
  <path d="M-50-14h44v28h-44z" class="goldd o"/>
  <path d="M-6-8h90v16H-6z" class="gold o"/>
</g>
<path d="M60 390h480" class="a"/>
""", ground=True)

add('on-purpose', 'わざとそうするイラスト。', f"""
{person(180,352,1.2,1,'coral','blue','reach','short','smile')}
<g transform="translate(400 330) rotate(24)">
  <path d="M-50-70h100l-12 110h-76z" fill="#fffdf6" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M260 250h80"/></g>
{ck(160,180,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('point-out', '細かい点を指さして示すイラスト。', f"""
<g transform="translate(330 230)">
  <path d="M-190-140h380v280h-380z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-150 {-100+i*48}h300"/>' for i in range(5))}</g>
  <path d="M-150-4h300" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
{hand(130,230,1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M190 230h30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('punk', '気分がさえずうつむいているイラスト。', f"""
{sit(280,352,1.3,1,'blue','blue','short','sad','down')}
{cloud(280,110,1.2,'violet')}
<g transform="translate(470 280)">
  <path d="M-80 0a80 80 0 0 1 160 0z" fill="#fffdf6" class="o"/>
  <path d="M-80 0h160" class="a"/>
  <path d="M0 0l-64-30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"/>
  <circle r="9" class="ink"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('put-off', '予定を先の日に延ばすイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-220-150h440v300h-440z" class="paper"/>
  <path d="M-220-150h440v50h-440z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M-220 {-50+i*50}h440"/>' for i in range(4))}
    {''.join(f'<path d="M{-157+c*63} -100v250"/>' for c in range(6))}
  </g>
  <g opacity="0.35"><circle cx="-94" cy="0" r="22" class="coralp o"/></g>
  <circle cx="94" cy="100" r="22" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M220 240q80 60 160 60"/></g>
""", ground=False, arrow=True)

add('rather-than', 'そちらではなくこちらを選ぶイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
</g>
{xx(170,150,0.9)}
<g transform="translate(450 250)">
  <path d="M-80-80h160v160h-160z" class="coral o"/>
</g>
{ck(450,150,1)}
{hand(300,340,1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M360 320h40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('run-out-of', '使い切って空になるイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-90-120h180v240h-180z" fill="#fffdf6" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M320 250h60"/></g>
<g transform="translate(480 250)">
  <path d="M-90-120h180v240h-180z" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(200 250)"><path d="M-90 0h180v120h-180z" class="teal o"/></g>
{xx(480,250,1.6)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('self-esteem', '鏡の中の自分を肯定するイラスト。', f"""
{person(190,352,1.25,1,'teal','blue','stand','short','smile')}
<g transform="translate(430 220)">
  <path d="M-110-150h220v300h-220z" class="goldd o"/>
  <path d="M-90-130h180v260h-180z" fill="#e9f2f7" class="o"/>
</g>
{person(440,340,1.1,-1,'teal','blue','stand','short','smile')}
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M300 150q-20-26 0-36 20-10 20 14 0-24 20-14 20 10 0 36l-20 20z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('set-up', '組み立てて新しく立ち上げるイラスト。', f"""
<g transform="translate(160 250)">
  <path d="M-60-40h50v50h-50z" class="tealp o" transform="rotate(-12)"/>
  <path d="M10-30h50v50H10z" class="tealp o" transform="rotate(14)"/>
  <path d="M-40 30h50v50h-50z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 250h60"/></g>
<g transform="translate(460 300)">
  <path d="M-90 0v-90h180V0z" fill="#fffdf6" class="o"/>
  <path d="M-104-90L0-146l104 56z" class="teal o"/>
  <path d="M-24-56h48V0h-48z" class="teald o"/>
</g>
{ck(460,140,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('show-up', '約束の場に姿を見せるイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-120-150h240v300h-240z" fill="#dfe6ea" class="o"/>
  <path d="M-60-110h180v260H-60z" fill="#fffaf1" class="o"/>
</g>
{person(400,352,1.25,1,'teal','blue','walk','short','smile')}
{ck(500,180,1)}
<g class="a" marker-end="url(#ar)"><path d="M300 260h70"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('therefore', '前の話からこう結論するイラスト。', f"""
<g transform="translate(180 200)">
  <path d="M-100-70h200v60h-200z" class="tealp o"/>
  <path d="M-100 10h200v60h-200z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="14" marker-end="url(#ar)"><path d="M310 200h50"/></g>
<g transform="translate(470 200)">
  <path d="M-80-70h160v140h-160z" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('this', 'すぐそばのこれを指すイラスト。', f"""
{person(200,352,1.25,1,'teal','blue','point','short','neutral')}
<g transform="translate(310 300)">
  <path d="M-50-50h100v100h-100z" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M268 260h-10"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="310" cy="300" r="80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('totally', '端から端まですっかり満ちているイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-230-50h460v100h-460z" class="teal o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M70 340h460M70 340v-24M530 340v-24"/></g>
{ck(300,140,1.2)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('try', 'うまくいくかやってみるイラスト。', f"""
{person(220,352,1.25,1,'teal','blue','reach','short','neutral')}
<g transform="translate(420 250)">
  <path d="M-70-70h140v140h-140z" class="tealp o"/>
  <circle r="34" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="10 8"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round"><path d="M160 190l-14-20M280 180v-22"/></g>
<g class="a" marker-end="url(#ar)"><path d="M300 250h50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('try-out', '実際に動かして試すイラスト。', f"""
<g transform="translate(390 250)">
  <path d="M-120-110h240v220h-240z" class="bluep o"/>
  <path d="M-70-70h140v100h-140z" class="ink"/>
  <circle cx="0" cy="70" r="24" class="coral o"/>
</g>
{person(150,352,1.15,1,'teal','blue','reach','short','neutral')}
{ck(500,150,0.9)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M230 280h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('turn-up', 'つまみを回して音量を上げるイラスト。', f"""
<g transform="translate(200 240)">
  <circle r="80" fill="#fffdf6" class="o"/>
  <path d="M0 0l56-56" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"/>
  <circle r="12" class="ink"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M0 -92v-14" transform="rotate({-90+i*45})"/>' for i in range(5))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M340 220q20 20 0 40M390 190q46 50 0 100M440 160q74 80 0 160"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M230 130a70 70 0 0 1 60 30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('typically', 'いちばんよくある型を示すイラスト。', f"""
<g class="teal o">{''.join(f'<circle cx="{130+i*70}" cy="240" r="30"/>' for i in range(5))}</g>
<circle cx="490" cy="240" r="30" class="coralp o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="270" cy="240" r="54"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M270 360v-60"/></g>
""", ground=False, arrow=True)

add('unless', '鍵がなければ通れないイラスト。', f"""
<g transform="translate(340 250)">
  <path d="M-20-140h40v280h-40z" class="ink"/>
  <path d="M-160-80h140v30h-140z" class="coral o"/>
</g>
<g transform="translate(180 250)" opacity="0.35">
  <circle r="26" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10"/>
  <path d="M24 0h60v12h-14v14h-12v-14h-12v14h-12v-14h-10z" fill="{TONES['gold'][2]}"/>
</g>
{xx(180,150,1)}
{xx(470,200,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('unlike', '似ても似つかないふたつのイラスト。', f"""
<g transform="translate(170 240)">
  <circle r="80" class="tealp o"/>
</g>
<g transform="translate(450 240)">
  <path d="M-80-80h160v160h-160z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9">
  <path d="M280 220h60M280 260h60M340 190l-60 100"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('upon', '倒れると同時に次が動くイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-200-80h40v160h-40z" class="tealp o" transform="rotate(-40 -180 80)"/>
  <path d="M-100-80h40v160h-40z" class="tealp o" transform="rotate(-24 -80 80)"/>
  <path d="M0-80h40v160H0z" class="tealp o" transform="rotate(-10 20 80)"/>
  <path d="M100-80h40v160h-40z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M100 140h360"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('warm-up', '運動の前に体をほぐすイラスト。', f"""
{person(220,352,1.3,1,'coral','blue','up','short','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M340 220q22 22 0 44M384 190q42 44 0 96"/>
</g>
<g transform="translate(480 320)">
  <path d="M-70-14h140v28h-140z" fill="{MUTED}"/>
  <path d="M-90-34h30v68h-30zM60-34h30v68H60z" fill="{INK}"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('well-being', '心も体も満ち足りているイラスト。', f"""
{person(300,352,1.3,1,'teal','blue','up','short','smile')}
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2.5">
  <path d="M180 180q-24-32 0-46 24-14 24 18 0-32 24-18 24 14 0 46l-24 24z"/>
</g>
<g transform="translate(450 320)">
  <path d="M0 40v-70" class="greens"/>
  <path d="M0-40q-44-6-50-44 42-6 50 44z" class="greenp o"/>
  <path d="M0-60q44-6 50-44-42-6-50 44z" class="greenp o"/>
</g>
{sun(500,110,34)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('whenever', 'いつでも構わないイラスト。', f"""
{clock(150,200,60,-60)}
{clock(300,200,60,30)}
{clock(450,200,60,140)}
{ck(150,330,0.8)}
{ck(300,330,0.8)}
{ck(450,330,0.8)}
""", ground=False)

add('whether', 'どちらであるかを問うイラスト。', f"""
<g transform="translate(170 260)">
  <path d="M-80-70h160v140h-160z" class="tealp o"/>
</g>
<g transform="translate(450 260)">
  <path d="M-80-70h160v140h-160z" class="coralp o"/>
</g>
{qmark(300,150,1.4)}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M270 220l-40 20M330 220l40 20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('whoever', 'だれであっても構わないイラスト。', f"""
{person(140,352,0.95,1,'teal','blue','stand','short','neutral')}
{person(250,352,0.95,1,'coral','gold','stand','bob','neutral')}
{person(360,352,0.95,-1,'gold','violet','stand','short','neutral')}
{person(470,352,0.95,-1,'green','blue','stand','bun','neutral')}
{ck(140,200,0.7)}
{ck(250,200,0.7)}
{ck(360,200,0.7)}
{ck(470,200,0.7)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('whom', '動きの受け手のほうを指すイラスト。', f"""
{person(160,352,1.2,1,'teal','blue','give','short','neutral')}
{person(450,352,1.2,-1,'coral','gold','reach','bob','neutral')}
<g transform="translate(300 260)"><path d="M-34-26h68v52h-68z" class="goldp o"/></g>
<g class="a" marker-end="url(#ar)"><path d="M240 180h140"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="450" cy="260" r="90"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('width', '横のさしわたしを測るイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-200-90h400v180h-400z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M300 380H110M300 380h190"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M100 350v50M500 350v50"/></g>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('wildlife', '野に生きる生き物のイラスト。', f"""
{tree(100,330,1.1)}
{tree(520,330,1)}
<g transform="translate(300 300)">
  <ellipse rx="70" ry="44" class="goldd o"/>
  <circle cx="60" cy="-36" r="30" class="goldd o"/>
  <path d="M84-44l30 10-30 14z" class="gold o"/>
  <circle cx="70" cy="-46" r="5" class="ink"/>
  <path d="M50-64l-10-34 26 18M74-66l14-32 10 30" fill="none" stroke="{TONES['gold'][2]}" stroke-width="6"/>
  <path d="M-40 44v30M20 46v28" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"><path d="M180 120q18-18 36 0M180 120q-18-18-36 0"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('willingness', '進んで手を挙げて引き受けるイラスト。', f"""
{person(250,352,1.35,1,'coral','blue','up','short','smile')}
{person(430,356,0.85,-1,'teal','blue','stand','bob','neutral')}
{person(510,356,0.85,-1,'gold','violet','stand','short','neutral')}
{ck(140,200,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('wire', '電柱をつなぐ電線のイラスト。', f"""
<g transform="translate(140 320)">
  <path d="M-10-200h20v200h-20z" fill="{TONES['gold'][2]}"/>
  <path d="M-60-180h120v14h-120z" fill="{TONES['gold'][2]}"/>
</g>
<g transform="translate(460 320)">
  <path d="M-10-200h20v200h-20z" fill="{TONES['gold'][2]}"/>
  <path d="M-60-180h120v14h-120z" fill="{TONES['gold'][2]}"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="4">
  <path d="M90 148q210 70 420 0M140 128q160 60 320 0M190 168q110 50 220 0"/>
</g>
<path d="M60 326h480" class="a"/>
""", ground=True)

add('wisdom', '長く生きて得た知恵のイラスト。', f"""
{person(200,352,1.3,1,'violet','violet','stand','bun','smile')}
<g transform="translate(430 210)">
  <path d="M0-80q52 0 52 50 0 30-22 42v20h-60v-20q-22-12-22-42 0-50 52-50z" class="gold o"/>
  <path d="M-30 32h60v18h-60z" class="goldd o"/>
  <g class="golds"><path d="M-84-30l-28-14M84-30l28-14M0-104v-26"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M280 230h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('wit', 'とっさに気の利いたことを言うイラスト。', f"""
{person(190,352,1.25,1,'teal','blue','point','short','smile')}
<g transform="translate(410 200)">
  <path d="M-110-70h220v110h-220zM-70 40l-14 30 44-30z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5"><path d="M-70-36h140M-70-8h100"/></g>
</g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2">
  <path d="M500 120l12 26 28 3-20 20 5 28-25-14-25 14 5-28-20-20 28-3z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('withdrawal', '預けたお金を引き出すイラスト。', f"""
<g transform="translate(360 240)">
  <path d="M-130-140h260v280h-260z" class="bluep o"/>
  <path d="M-90-110h180v100h-180z" class="ink"/>
  <path d="M-60 30h120v20h-120z" fill="{MUTED}" class="o"/>
</g>
<g transform="translate(300 300)">
  <path d="M-56-24h112v48h-112z" class="greenp o"/>
  <circle r="14" class="gold o"/>
</g>
{hand(150,300,1)}
<g class="a" marker-end="url(#ar)"><path d="M300 200h-90"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('within', '枠の内側におさまっているイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-150h440v300h-440z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="16 12"/>
  <path d="M-100-70h200v140h-200z" class="teal o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"><path d="M540 380L340 300"/></g>
""", ground=False, arrow=True)

add('work-out', '重りを持ち上げて体を動かすイラスト。', f"""
{person(300,352,1.3,1,'coral','blue','up','short','neutral')}
<g transform="translate(300 168)">
  <path d="M-110-16h220v32h-220z" fill="{MUTED}"/>
  <path d="M-140-40h30v80h-30zM110-40h30v80h-30z" fill="{INK}"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round"><path d="M210 240l-14-20M390 240l14-20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('workout', '運動の献立を書いた表のイラスト。', f"""
<g transform="translate(260 210)">
  <path d="M-170-150h340v300h-340z" class="paper"/>
  <path d="M-140-110h280v40h-280z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-100 {-30+i*50}h240"/>' for i in range(4))}</g>
  <g fill="none" stroke="{GRN}" stroke-width="6">{''.join(f'<path d="M-136 {-36+i*50}l10 12 20-24"/>' for i in range(4))}</g>
</g>
<g transform="translate(490 320)">
  <path d="M-50-12h100v24h-100z" fill="{MUTED}"/>
  <path d="M-70-30h24v60h-24zM46-30h24v60H46z" fill="{INK}"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('workplace', '机の並ぶ職場のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-250-160h500v320h-500z" fill="#fffdf6" class="o"/>
  <path d="M-250 130h500" class="a"/>
</g>
<g transform="translate(190 300)">
  <path d="M-90-20h180v20h-180z" class="goldd o"/>
  <path d="M-70 0v40M70 0v40" class="a"/>
  <path d="M-50-70h100v50h-100z" class="ink"/>
</g>
<g transform="translate(430 300)">
  <path d="M-90-20h180v20h-180z" class="goldd o"/>
  <path d="M-70 0v40M70 0v40" class="a"/>
  <path d="M-50-70h100v50h-100z" class="ink"/>
</g>
{person(190,290,0.75,1,'teal','blue','stand','short','neutral')}
{person(430,290,0.75,-1,'coral','gold','stand','bob','neutral')}
<path d="M50 340h500" class="a"/>
""", ground=False)

add('youngster', 'まだ年若い子のイラスト。', f"""
{person(300,354,0.85,1,'gold','coral','up','short','smile')}
<circle cx="450" cy="330" r="36" class="coralp o"/>
<g fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"><path d="M414 330h72M450 294v72"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M170 300h480"/></g>
<g opacity="0.4">{person(150,352,1.3,1,'violet','blue','stand','bun','neutral')}</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('zone', '区切られた一帯を示すイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-240-150h480v300h-480z" class="greenp o"/>
  <path d="M-120-90h240v180h-240z" class="coralp o"/>
  <path d="M-120-90h240v180h-240z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="14 12"/>
</g>
""", ground=False)

add('accidentally', 'うっかり手が当たって倒すイラスト。', f"""
{person(200,352,1.2,1,'teal','blue','reach','short','surprised')}
<g transform="translate(400 330) rotate(70)">
  <path d="M-30-60h60l-8 100h-44z" fill="#fffdf6" class="o"/>
</g>
<g class="bluep o"><ellipse cx="440" cy="378" rx="70" ry="16"/></g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2.5">
  <path d="M330 160h26l-6 70h-14zM343 252a13 13 0 1 0 0 26 13 13 0 1 0 0-26z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
