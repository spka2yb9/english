"""第91回: re〜rh の名詞を中心に45語。"""
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

add('refugee', '荷を背負って国を離れる難民のイラスト。', f"""
<g transform="translate(110 300)">
  <path d="M-60 0v-70h40l-8 30 16-30h12v70z" fill="#dfe6ea" class="o"/>
  <path d="M-70-70l30-24 22 16" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
{person(260,356,1,1,'coral','blue','carry','bun','sad')}
{person(350,356,0.8,1,'gold','violet','walk','short','sad')}
<g transform="translate(300 300)"><path d="M-30-24h60v48h-60z" class="goldd o"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="14 12"><path d="M470 120v260"/></g>
<g class="a" marker-end="url(#ar)"><path d="M400 200h80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('refusal', '差し出されたものを断る拒否のイラスト。', f"""
{person(170,352,1.2,1,'teal','blue','reach','short','neutral')}
<g transform="translate(390 270)">
  <path d="M-60-30h120v60h-120z" class="greenp o"/>
  <circle r="16" class="gold o"/>
</g>
{hand(530,270,-1)}
{xx(300,200,1.2)}
<g class="a" marker-end="url(#ar)"><path d="M330 320h-70"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('regime', '上から下へ命令が通る政権のイラスト。', f"""
{person(300,180,1.05,1,'violet','violet','point','short','neutral')}
<g transform="translate(300 190)">
  <path d="M-60-10h120v24h-120z" class="goldd o"/>
</g>
{person(160,356,0.85,1,'blue','blue','stand','cap','neutral')}
{person(300,356,0.85,1,'blue','blue','stand','cap','neutral')}
{person(440,356,0.85,1,'blue','blue','stand','cap','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M300 220v40M300 260l-140 40M300 260l140 40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('registration', '窓口で名前を書いて登録するイラスト。', f"""
<g transform="translate(380 300)">
  <path d="M-160-30h320v20h-320z" class="goldd o"/>
  <path d="M-130-10v46M130-10v46" class="a"/>
  <path d="M-100-90h200v60h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-70-70h140M-70-50h100"/></g>
</g>
{person(150,352,1.1,1,'teal','blue','reach','short','smile')}
<g transform="translate(250 250) rotate(30)">
  <path d="M-8-50h16v80h-16z" class="gold o"/>
</g>
{ck(500,180,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('regulation', '守るべき決まりを定めた規則のイラスト。', f"""
<g transform="translate(230 210)">
  <path d="M-140-150h280v300h-280z" class="paper"/>
  <path d="M-110-120h220v40h-220z" class="coral o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-110 {-40+i*44}h220"/>' for i in range(4))}</g>
</g>
<g transform="translate(470 220)">
  <circle r="80" fill="none" stroke="{TONES['coral'][0]}" stroke-width="18"/>
  <path d="M-50 0h100" fill="none" stroke="{TONES['coral'][0]}" stroke-width="18" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('regulator', '会社を監督する規制当局のイラスト。', f"""
{building(180,280,0.85,'violet')}
{tower(420,300,0.55,'teal',4)}
{tower(540,300,0.55,'teal',4)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M270 200h90M270 240h200"/></g>
<g transform="translate(180 130)">
  <circle r="34" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M26 26l30 30" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('rehabilitation', '手すりにつかまって歩く力を取り戻すイラスト。', f"""
{person(300,352,1.2,1,'teal','blue','walk','short','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="12" stroke-linecap="round">
  <path d="M120 270h360M120 270v90M480 270v90M300 270v90"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M150 180h300"/></g>
{ck(500,200,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('rejection', '申し込みが差し戻される不採用のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-130-140h260v280h-260z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-90 {-90+i*44}h180"/>' for i in range(4))}</g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="14" stroke-linecap="round"><path d="M-60 60l120 60M60 60l-120 60"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M150 100h-70"/></g>
{hand(530,230,-1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('reliability', 'いつも同じように働く確かさのイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="120" fill="#fffdf6" class="o"/>
  <path d="M0 0v-84" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <path d="M0 0l54 32" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"/>
  <circle r="9" class="ink"/>
  <g fill="{INK}">{''.join(f'<rect x="-4" y="-110" width="8" height="18" transform="rotate({a})"/>' for a in range(0,360,30))}</g>
</g>
{ck(140,350,0.8)}
{ck(300,370,0.8)}
{ck(460,350,0.8)}
""", ground=False)

add('relief', '重荷が外れてほっとするイラスト。', f"""
{person(230,352,1.25,1,'teal','blue','up','short','smile')}
{box(460,180,140,90,26,'gold')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M300 200h80"/></g>
<g class="o" fill="#e1edfb"><circle cx="300" cy="280" r="16"/><circle cx="330" cy="300" r="11"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('reluctance', '引かれても気が進まず後ろへ引くイラスト。', f"""
{person(300,352,1.25,-1,'teal','blue','reach','short','sad')}
{hand(500,250,-1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M430 250h-80"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M240 300h-80"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M400 320h60"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('remainder', '分けたあとに残ったあまりのイラスト。', f"""
<g transform="translate(240 230)">
  <g class="teal o">{''.join(f'<rect x="{-180+c*64}" y="{-60+r*64}" width="50" height="50"/>' for r in range(2) for c in range(5))}</g>
</g>
<g class="coralp o"><rect x="440" y="230" width="50" height="50"/><rect x="500" y="230" width="50" height="50"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><rect x="426" y="216" width="138" height="78" rx="14"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M400 140v220"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('reminder', '忘れないように貼りつけた覚え書きのイラスト。', f"""
<g transform="translate(240 200)">
  <path d="M-130-130h260v220l-40 40h-220z" class="goldp o"/>
  <path d="M90 90h40l-40 40z" class="gold o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-90 {-80+i*44}h180"/>' for i in range(3))}</g>
</g>
<g transform="translate(470 250)">
  <circle r="70" fill="#fffdf6" class="o"/>
  <path d="M0 0v-46M0 0l30 18" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle r="7" class="ink"/>
  <path d="M-50-58l-24-22M50-58l24-22" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <path d="M-46-60q-24-30 6-46M46-60q24-30-6-46" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('removal', 'こびりついた汚れを取り除くイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-190-110h380v220h-380z" fill="#fffdf6" class="o"/>
  <path d="M-90-30q40-40 80 0t60 30-70 40-90-20 20-50z" class="goldd o" opacity="0.55"/>
</g>
{hand(140,170,1)}
{xx(300,220,1.4)}
<g class="a" marker-end="url(#ar)"><path d="M400 120h80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('rental', '期間を決めて貸し出す賃貸のイラスト。', f"""
{hand(130,250,1)}
<g transform="translate(300 250)">
  <circle cx="-40" cy="0" r="34" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12"/>
  <path d="M-10 0h90v14h-20v20h-14v-20h-20v20h-14v-20h-22z" fill="{TONES['gold'][2]}"/>
</g>
<g transform="translate(480 250)">
  <circle r="66" fill="#fffdf6" class="o"/>
  <path d="M0 0v-44M0 0l28 16" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle r="7" class="ink"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M200 170h180"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('replacement', '古い部品を新しいものに取りかえるイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-80-80h160v160h-160z" fill="#dfe6ea" class="o"/>
  <circle r="40" fill="none" stroke="{MUTED}" stroke-width="12"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 240h60"/></g>
<g transform="translate(440 240)">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
  <circle r="40" fill="none" stroke="{TONES['teal'][0]}" stroke-width="12"/>
</g>
{xx(160,130,0.8,MUTED)}
{ck(440,130,0.9)}
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('representation', 'みんなの代わりにひとりが立つ代表のイラスト。', f"""
{person(430,346,1.3,1,'coral','blue','point','bun','neutral')}
{person(110,356,0.7,1,'teal','blue','stand','short','neutral')}
{person(175,356,0.7,1,'teal','blue','stand','bob','neutral')}
{person(240,356,0.7,1,'teal','blue','stand','short','neutral')}
{person(305,356,0.7,1,'teal','blue','stand','bun','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M210 200h140"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('representative', 'バッジをつけて窓口に立つ担当者のイラスト。', f"""
{person(300,352,1.4,1,'violet','blue','point','short','smile')}
<g transform="translate(240 250)">
  <path d="M-34-24h68v48h-68z" class="paper"/>
  <circle cx="-14" cy="0" r="12" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M4-6h22M4 6h22"/></g>
</g>
<g transform="translate(450 330)">
  <path d="M-90-30h180v20h-180z" class="goldd o"/>
  <path d="M-70-10v46M70-10v46" class="a"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('reproduction', '同じものを何枚も写し取る複製のイラスト。', f"""
<g transform="translate(250 210)">
  <path d="M-130-120h260v200h-260z" class="bluep o"/>
  <path d="M-100-90h200v60h-200z" class="ink"/>
  <path d="M-130 30h260v20h-260z" class="blued o"/>
</g>
<g transform="translate(470 280)">
  <path d="M-80-60h160v120h-160z" class="paper" transform="rotate(-6)"/>
  <path d="M-80-60h160v120h-160z" class="paper" transform="rotate(3) translate(14 10)"/>
  <g transform="rotate(3) translate(14 10)"><path d="M-50-30h100v60h-100z" class="tealp o"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M330 260h40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('republic', '王を置かず国民が決める共和国のイラスト。', f"""
{building(300,300,1,'teal')}
<g transform="translate(300 110)">
  <path d="M-50 10l-10-50 30 20 30-40 30 40 30-20-10 50z" fill="#dfe6ea" class="o"/>
</g>
{xx(300,110,1.3)}
{person(130,356,0.8,1,'coral','blue','up','short','smile')}
{person(480,356,0.8,-1,'gold','violet','up','bob','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('reputation', '人の口から口へ伝わる評判のイラスト。', f"""
{person(300,352,1.25,1,'teal','blue','stand','short','smile')}
{star(180,180,30,'gold')}
{star(300,140,34,'gold')}
{star(420,180,30,'gold')}
<g transform="translate(120 280)">
  <path d="M-56-30h112v50h-112zM-26 20l-10 24 32-24z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{GRN}" stroke-width="5"><path d="M-24-6l10 12 20-24"/></g>
</g>
<g transform="translate(490 280)">
  <path d="M-56-30h112v50h-112zM26 20l10 24-32-24z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{GRN}" stroke-width="5"><path d="M-24-6l10 12 20-24"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('resemblance', 'よく似たふたつを並べたイラスト。', f"""
{face(170,210,86,'smile')}
{face(430,210,86,'smile')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="8">
  <path d="M272 190q28-16 56 0M272 226q28-16 56 0"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('resentment', '仕打ちを根に持って恨むイラスト。', f"""
{person(200,352,1.2,1,'blue','blue','think','short','sad')}
{cloud(180,100,1.2,'violet')}
<g transform="translate(430 200)">
  <path d="M-110-70h220v140h-220z" class="paper"/>
</g>
{person(430,250,0.55,-1,'coral','gold','reach','bob','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M300 200h-30"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round"><path d="M130 190l-16-22M250 180v-24"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('residence', '表札のついた住まいのイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-110 0v-110h220V0z" fill="#fffdf6" class="o"/>
  <path d="M-126-110L0-180l126 70z" class="teal o"/>
  <path d="M-30-70h60V0h-60z" class="teald o"/>
  <path d="M40-86h50v36H40z" class="tealp o"/>
  <path d="M-100-86h50v36h-50z" class="tealp o"/>
</g>
<g transform="translate(420 250)">
  <path d="M-40-20h80v40h-80z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-24-4h48M-24 8h32"/></g>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('resident', 'その住まいに暮らしている住民のイラスト。', f"""
{tower(420,320,0.8,'teal',5)}
{person(170,352,1.25,1,'coral','blue','stand','bun','smile')}
<g transform="translate(250 250)">
  <path d="M-36-20h72v40h-72z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-20-4h40M-20 8h28"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M300 300h50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('residue', '容器の底に残ったかすのイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-100-130h200v230q0 30-100 30t-100-30z" fill="#fffdf6" class="o"/>
  <path d="M-100 70q0 30 100 30t100-30V40q-100 30-200 0z" class="goldd o"/>
  <path d="M-104-140h208v20h-208z" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M500 300h-90"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('resignation', '辞表を出して職を辞すイラスト。', f"""
{person(160,352,1.15,1,'violet','blue','give','short','neutral')}
<g transform="translate(320 250)">
  <path d="M-70-90h140v180h-140z" class="paper"/>
  <path d="M-40-60h80v30h-80z" class="coral o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-40 0h80M-40 30h60"/></g>
</g>
{hand(500,250,-1)}
<g class="a" marker-end="url(#ar)"><path d="M250 170h160"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('resistance', '押してくる力を押し返す抵抗のイラスト。', f"""
{person(360,352,1.25,-1,'teal','blue','reach','short','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" marker-end="url(#ar)"><path d="M80 250h170"/></g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="10" marker-end="url(#ar)"><path d="M520 250H350"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round"><path d="M300 200v-24M270 210l-20-20M330 210l20-20"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('resolution', 'こうすると固く心を決めるイラスト。', f"""
{person(200,352,1.3,1,'coral','blue','up','short','neutral')}
<g transform="translate(430 240)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-56-60h112M-56-20h112M-56 20h80"/></g>
  <g fill="none" stroke="{GRN}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"><path d="M-40 66l20 24 44-52"/></g>
</g>
<g class="golds"><path d="M200 160v-26M120 190l-20-20M280 190l20-20"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('respect', '頭を下げて敬意を示すイラスト。', f"""
<g transform="translate(220 350)">
  <path d="M-14 0l-10-40M14 0l10-40" fill="none" stroke="{TONES['blue'][2]}" stroke-width="16" stroke-linecap="round"/>
  <path d="M-30-44q34-16 66 4l14 40q-40 16-80-4z" class="teal o"/>
  <circle cx="52" cy="-66" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M30-80q14-24 38-16 20 8 16 30-16-14-30-4-12-12-24-10z" fill="{HAIR}" stroke="{HAIR}" stroke-width="2"/>
  <path d="M-24-30q-20 20-6 40" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
</g>
{person(450,352,1.25,-1,'violet','violet','stand','bun','smile')}
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M330 190q-20-26 0-36 20-10 20 14 0-24 20-14 20 10 0 36l-20 20z"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('restoration', '傷んだ絵をもとの姿に直す修復のイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-110-110h220v220h-220z" class="goldd o"/>
  <path d="M-88-88h176v176h-176z" fill="#e7dfd0" class="o"/>
  <path d="M-60 60l50-70 40 40 30-30 40 60z" fill="#c9bfa9" class="o"/>
  <path d="M-20-88l16 176M50-88L36 88" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 230h50"/></g>
<g transform="translate(460 230)">
  <path d="M-110-110h220v220h-220z" class="goldd o"/>
  <path d="M-88-88h176v176h-176z" fill="#fdf6e3" class="o"/>
  <path d="M-60 60l50-70 40 40 30-30 40 60z" class="greenp o"/>
  <circle cx="40" cy="-40" r="22" class="goldp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('restraint', '飛び出しそうな自分を押しとどめる自制のイラスト。', f"""
{person(360,352,1.25,1,'coral','blue','reach','short','neutral')}
{hand(150,250,1)}
<g fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round"><path d="M210 250h80"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" marker-end="url(#ar)"><path d="M450 200h70"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="8" marker-end="url(#ar)"><path d="M330 200h-80"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('restriction', '通り道をせばめて量を抑える制限のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-240-120h180v240h-180z" class="bluep o"/>
  <path d="M-60-120h30v90h-30zM-60 30h30v90h-30z" fill="{MUTED}" class="o"/>
  <path d="M-30-120h270v60h-270zM-30 60h270v60h-270z" class="bluep o"/>
  <path d="M-30-30h270v60h-270z" class="bluep o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M100 350h400"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M240 130v50M240 310v-50"/></g>
""", ground=False, arrow=True)

add('result', '取り組みの末に出た点数のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-180-150h360v300h-360z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-140-100h160M-140-60h160M-140-20h120"/></g>
  <g fill="none" stroke="{GRN}" stroke-width="9" stroke-linecap="round"><path d="M60-100l14 16 30-36M60-60l14 16 30-36"/></g>
  <path d="M-140 40h320v100h-320z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="10"><path d="M-100 90h120M60 90h60"/></g>
</g>
""", ground=False)

add('retail', '店先で客にひとつずつ売る小売りのイラスト。', f"""
<g transform="translate(340 300)">
  <path d="M-170-30h340v20h-340z" class="teald o"/>
  <path d="M-140-10v46M140-10v46" class="a"/>
  <path d="M-170-30l-14-40h368l-14 40z" class="teal o"/>
</g>
{person(400,250,1,-1,'gold','blue','give','short','smile')}
{person(140,352,1,1,'coral','blue','carry','bob','smile')}
<g transform="translate(220 300)">
  <path d="M-34-24h68v48h-68z" class="goldp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('retirement', '勤めを終えてのんびり過ごす引退のイラスト。', f"""
{sit(230,350,1.3,1,'violet','violet','bun','smile','down')}
{chair(240,356,1.25,'gold',1)}
{sun(500,110,42)}
{tree(500,330,0.9)}
<g transform="translate(120 200)">
  <circle r="54" fill="#fffdf6" class="o"/>
  <path d="M0 0v-34M0 0l24 14" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <circle r="6" class="ink"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M180 200h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('revelation', '覆いをめくって明かされる新事実のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-140-100h280v200h-280z" class="tealp o"/>
  <circle r="56" class="coral o"/>
</g>
<g transform="translate(300 120) rotate(-18)">
  <path d="M-160-40h320v70h-320z" class="bluep o"/>
</g>
{hand(520,120,-1)}
<g transform="translate(160 140)">
  <g fill="{TONES['gold'][0]}"><rect x="-13" y="-44" width="26" height="58" rx="13"/><circle cy="32" r="13"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('revenge', 'やられたことをやり返す復讐のイラスト。', f"""
{person(150,352,1.15,1,'coral','blue','reach','short','neutral')}
{person(450,352,1.15,-1,'teal','gold','stand','bob','sad')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M380 160H220"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" marker-end="url(#ar)"><path d="M230 260h150"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('reverse', '向きをそっくり逆にするイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="10" marker-end="url(#ar)"><path d="M120 170h330"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" marker-end="url(#ar)"><path d="M480 290H150"/></g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="10 8"><path d="M300 200v60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('review', '出来たものを見直して評価するイラスト。', f"""
<g transform="translate(250 220)">
  <path d="M-140-140h280v280h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-100 {-100+i*44}h200"/>' for i in range(4))}</g>
</g>
<g transform="translate(420 180)">
  <circle r="66" fill="none" stroke="{INK}" stroke-width="9"/>
  <circle r="56" fill="#fffdf6" opacity="0.4"/>
  <path d="M48 48l50 50" fill="none" stroke="{INK}" stroke-width="14" stroke-linecap="round"/>
</g>
{star(180,350,26,'gold')}
{star(250,350,26,'gold')}
{star(320,350,26,'gold')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('revision', '赤を入れて書き直す修正のイラスト。', f"""
<g transform="translate(180 220)">
  <path d="M-120-140h240v280h-240z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-90 {-100+i*44}h180"/>' for i in range(5))}</g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5">
    <path d="M-90-56h100M-70-60q30 20 60-6M-90 34h120"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M330 220h50"/></g>
<g transform="translate(480 220)">
  <path d="M-90-140h180v280h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-60 {-100+i*44}h120"/>' for i in range(5))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('revival', '消えていた明かりがまたともる復活のイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M0-70q46 0 46 44 0 26-20 38v18h-52v-18q-20-12-20-38 0-44 46-44z" fill="#dfe6ea" class="o"/>
  <path d="M-26 30h52v16h-52z" fill="{MUTED}" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 240h60"/></g>
<g transform="translate(440 240)">
  <path d="M0-70q46 0 46 44 0 26-20 38v18h-52v-18q-20-12-20-38 0-44 46-44z" class="gold o"/>
  <path d="M-26 30h52v16h-52z" class="goldd o"/>
  <g class="golds"><path d="M-90-40l-26-14M90-40l26-14M0-100v-26"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('revolution', '古い支配をくつがえす革命のイラスト。', f"""
<g transform="translate(480 320) rotate(180)">
  <path d="M-50 10l-10-50 30 20 30-40 30 40 30-20-10 50z" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round"><path d="M450 250l60 60M510 250l-60 60"/></g>
{person(120,352,1,1,'coral','blue','up','short','neutral')}
{person(210,352,1,1,'gold','violet','up','bob','neutral')}
{person(300,352,1,1,'coral','gold','up','cap','neutral')}
<g class="coral o"><path d="M146 200h70l-14 22 14 22h-70z"/><path d="M236 200h70l-14 22 14 22h-70z"/></g>
<g class="a"><path d="M146 260v-70M236 260v-70"/></g>
<g class="a" marker-end="url(#ar)"><path d="M360 160h70"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('reward', 'よくやったしるしに渡されるほうびのイラスト。', f"""
{person(160,352,1.15,1,'teal','blue','reach','short','smile')}
{hand(520,240,-1)}
<g transform="translate(350 250)">
  <path d="M-60-40h120v80h-120z" class="coral o"/>
  <path d="M-60-40h120v18h-120zM-10-40v80" class="a"/>
  <path d="M0-40q-30-30-40-6 20 12 40 6zM0-40q30-30 40-6-20 12-40 6z" class="coralp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M460 180H300"/></g>
{ck(160,190,0.9)}
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('rhythm', '一定の間で打ちつづけるリズムのイラスト。', f"""
<g transform="translate(160 270)">
  <ellipse cy="-60" rx="80" ry="26" fill="#fdf6e3" class="o"/>
  <path d="M-80-60v60q0 26 80 26t80-26v-60" class="coralp o"/>
  <path d="M-80-40h160" fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round">
  <path d="M180 150l60 40M230 130l50 46"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="8" stroke-linecap="round">
  <path d="M300 300v-70M360 300v-40M420 300v-70M480 300v-40M540 300v-70"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 340h270"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

print(len(W), ' '.join(W))
print(sheet(W))
