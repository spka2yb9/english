"""第105回: 句動詞45語。"""
from lib import *
W=[]
def add(slug,a,b,**k): W.append(emit(slug,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'
def house(x,y,s=1,cls='teal'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-80 0v-80h160V0z" fill="#fffdf6" class="o"/>'
            f'<path d="M-94-80L0-136l94 56z" class="{cls} o"/>'
            f'<path d="M-24-50h48V0h-48z" class="{cls}d o"/></g>')
def bulb(x,y,s=1,on=True):
    c = 'gold' if on else None
    body = f'class="{c} o"' if on else f'fill="#dfe6ea" class="o"'
    rays = f'<g class="golds"><path d="M-76-34l-24-12M76-34l24-12M0-92v-24"/></g>' if on else ''
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0-70q46 0 46 44 0 26-20 38v18h-52v-18q-20-12-20-38 0-44 46-44z" {body}/>'
            f'<path d="M-26 30h52v16h-52z" fill="{TONES["gold"][2] if on else MUTED}" class="o"/>{rays}</g>')
def switch(x,y,s=1,on=True):
    knob = 24 if on else -24
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect x="-50" y="-30" width="100" height="60" rx="30" fill="{TONES["teal"][0] if on else MUTED}" class="o"/>'
            f'<circle cx="{knob}" cy="0" r="22" fill="#fffdf6" class="o"/></g>')

add('give-back', '借りたものを持ち主に返すイラスト。', f"""
{person(150,352,1.15,1,'teal','blue','give','short','neutral')}
{person(470,352,1.15,-1,'coral','gold','reach','bob','smile')}
<g transform="translate(310 260)"><path d="M-40-30h80v60h-80z" class="goldp o"/></g>
<g class="a" marker-end="url(#ar)"><path d="M240 180h150"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('go-back', '来た道を引き返すイラスト。', f"""
{person(360,352,1.2,-1,'teal','blue','walk','short','neutral')}
{house(150,340,0.9)}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M420 260q-60-80-180-60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('go-on', '止まらずそのまま続いていくイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M60 250h480"/></g>
<g class="teal o">{''.join(f'<rect x="{100+i*80}" y="200" width="50" height="50"/>' for i in range(5))}</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M70 320h460"/></g>
""", ground=False, arrow=True)

add('go-out', '家から外へ出かけるイラスト。', f"""
{house(160,330,0.95)}
{person(430,352,1.2,1,'teal','blue','walk','short','smile')}
<g class="a" marker-end="url(#ar)"><path d="M280 260h130"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('grow-up', '子どもが大人になるイラスト。', f"""
{person(150,354,0.6,1,'gold','coral','stand','short','smile')}
{person(300,354,0.9,1,'teal','blue','stand','short','smile')}
{person(460,352,1.25,1,'violet','blue','stand','short','smile')}
<g class="a" marker-end="url(#ar)"><path d="M80 386h440"/></g>
""", ground=True, arrow=True)

add('look-out', '危ないと気をつけるイラスト。', f"""
{person(220,352,1.25,1,'coral','blue','up','short','surprised')}
{box(300,120,120,70,20,'gold')}
<g class="a" marker-end="url(#ar)"><path d="M300 180v50"/></g>
<g transform="translate(460 200)">
  <path d="M0-70l70 120h-140z" class="gold o"/>
  <g fill="{INK}"><rect x="-9" y="-20" width="18" height="42" rx="9"/><circle cy="34" r="10"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('look-up', '辞書で意味を調べるイラスト。', f"""
<g transform="translate(280 230)">
  <path d="M-190-130h380v240h-380z" class="paper"/>
  <path d="M0-130v240" class="a"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-160 {-90+i*36}h140M20 {-90+i*36}h140"/>' for i in range(5))}</g>
</g>
<g transform="translate(400 240)">
  <circle r="76" fill="none" stroke="{INK}" stroke-width="9"/>
  <circle r="66" fill="#fffdf6" opacity="0.4"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M-40-10h80M-40 16h50"/></g>
  <path d="M54 54l56 56" fill="none" stroke="{INK}" stroke-width="14" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('put-away', '引き出しにしまい込むイラスト。', f"""
<g transform="translate(330 290)">
  <path d="M-140-100h280v200h-280z" class="goldd o"/>
  <path d="M-120-20h240v100h-240z" class="goldp o"/>
  <path d="M-30 20h60v14h-60z" class="a" fill="none"/>
</g>
{hand(120,200,1)}
<g transform="translate(230 190)"><path d="M-30-24h60v48h-60z" class="tealp o"/></g>
<g class="a" marker-end="url(#ar)"><path d="M280 220l40 50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('put-back', '取った物を元の場所に戻すイラスト。', f"""
<g transform="translate(360 230)">
  <path d="M-180-130h360v260h-360z" fill="#fffdf6" class="o"/>
  <path d="M-180-30h360M-180 60h360" class="a"/>
  <g class="tealp o"><rect x="-150" y="-110" width="50" height="80"/><rect x="-80" y="-110" width="50" height="80"/></g>
  <path d="M-10-110h50v80h-50z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"/>
</g>
{hand(130,270,1)}
<g transform="translate(230 250)"><path d="M-26-40h50v80h-50z" class="tealp o"/></g>
<g class="a" marker-end="url(#ar)"><path d="M280 180q60-60 100-20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('put-on', '上着を身につけるイラスト。', f"""
{person(180,352,1.2,1,'teal','blue','reach','short','smile')}
<g transform="translate(400 250)">
  <path d="M-90-70q90-40 180 0l-20 140h-140z" class="coral o"/>
  <path d="M-90-70l-40 60 40 30M90-70l40 60-40 30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="20" stroke-linecap="round"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('slow-down', '速度を落とすイラスト。', f"""
<g transform="translate(360 300)">
  <path d="M-120 0v-40l40-50h150l40 50V0z" class="teal o"/>
  <g fill="#fffdf6" class="o"><rect x="-70" y="-80" width="56" height="36"/><rect x="0" y="-80" width="56" height="36"/></g>
  <g fill="{INK}"><circle cx="-70" cy="6" r="24"/><circle cx="80" cy="6" r="24"/></g>
</g>
<g transform="translate(160 200)">
  <path d="M-90 0a90 90 0 0 1 180 0z" fill="#fffdf6" class="o"/>
  <path d="M-90 0h180" class="a"/>
  <path d="M0 0l-60-40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"/>
  <circle r="9" class="ink"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M240 130a80 80 0 0 0-60-30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('stay-up', '夜おそくまで起きているイラスト。', f"""
<path d="M0 0h600v400H0z" fill="#1f2b3d"/>
<g fill="#fffdf6">{''.join(f'<circle cx="{40+i*70}" cy="{40+(i*53)%100}" r="3"/>' for i in range(8))}</g>
<path d="M0 306h600v94H0z" fill="#2c3a4d"/>
{sit(220,352,1.2,1,'teal','blue','short','sad','lap')}
<g transform="translate(290 300)"><path d="M-46-16h92v34h-92z" class="paper"/></g>
<g transform="translate(470 180)">
  <circle r="60" fill="#fffdf6" class="o"/>
  <path d="M0 0v-38M0 0l-24 14" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle r="7" class="ink"/>
</g>
""", ground=False)

add('take-out', 'かばんから中身を取り出すイラスト。', f"""
<g transform="translate(200 300)">
  <path d="M-90-40h180v100h-180z" class="goldd o"/>
  <path d="M-90-40q90-50 180 0z" class="gold o"/>
</g>
{hand(400,190,-1)}
<g transform="translate(300 230)"><path d="M-30-26h60v52h-60z" class="tealp o"/></g>
<g class="a" marker-end="url(#ar)"><path d="M240 220l50-30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('throw-away', 'いらない物をごみ箱に捨てるイラスト。', f"""
{person(170,352,1.2,1,'teal','blue','reach','short','neutral')}
<g transform="translate(440 300)">
  <path d="M-80 0h160l-16 90h-128z" class="tealp o"/>
  <path d="M-90-16h180v16h-180z" class="teal o"/>
</g>
<g transform="translate(320 190)"><path d="M-24-20h48v40h-48z" class="goldd o"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M260 220q90-70 170 40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('try-on', '鏡の前で服を試着するイラスト。', f"""
{person(190,352,1.25,1,'coral','blue','stand','short','smile')}
<g transform="translate(440 220)">
  <path d="M-110-150h220v300h-220z" class="goldd o"/>
  <path d="M-90-130h180v260h-180z" fill="#e9f2f7" class="o"/>
</g>
{person(450,340,1.1,-1,'coral','blue','stand','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M270 230h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('turn-off', 'スイッチを切って明かりを消すイラスト。', f"""
{bulb(200,240,1.2,False)}
{switch(430,250,1.2,False)}
{xx(430,140,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('turn-on', 'スイッチを入れて明かりをつけるイラスト。', f"""
{bulb(200,240,1.2,True)}
{switch(430,250,1.2,True)}
{ck(430,140,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('write-down', 'ノートに書きとめるイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-170-120h340v240h-340z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-130 {-70+i*44}h260"/>' for i in range(4))}</g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-linecap="round"><path d="M-130-70q30-20 60 0t60-6"/></g>
</g>
<g transform="translate(430 190) rotate(30)">
  <path d="M-14-130h28l10 130-24 40-24-40z" class="gold o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('end-up', '曲がりくねった末に思わぬ所に着くイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="14 12" marker-end="url(#ar)">
  <path d="M110 330q80-130 170-60t90-130 100 200"/>
</g>
{person(110,352,1,1,'teal','blue','walk','short','neutral')}
<g transform="translate(480 350)">
  <path d="M-60-30h120v60h-120z" class="coralp o"/>
</g>
<g fill="{TONES['coral'][0]}"><rect x="470" y="230" width="20" height="46" rx="10"/><circle cx="480" cy="292" r="11"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('fill-in', '空欄をうめるイラスト。', f"""
<g transform="translate(280 220)">
  <path d="M-170-150h340v300h-340z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-130 {-90+i*60}h120"/>' for i in range(4))}</g>
  <g fill="#fffdf6" stroke="{TONES['coral'][0]}" stroke-width="4">{''.join(f'<rect x="20" y="{-108+i*60}" width="110" height="36"/>' for i in range(4))}</g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><path d="M36-96h80M36-36h60"/></g>
</g>
<g transform="translate(470 300) rotate(28)">
  <path d="M-14-130h28l10 130-24 40-24-40z" class="gold o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('fill-out', '用紙をすべて書き上げるイラスト。', f"""
<g transform="translate(280 220)">
  <path d="M-170-150h340v300h-340z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-130 {-90+i*60}h120"/>' for i in range(4))}</g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4">{''.join(f'<path d="M20 {-96+i*60}h110"/>' for i in range(4))}</g>
</g>
{ck(490,180,1.1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('get-along', '仲よくやっていくイラスト。', f"""
{person(220,352,1.2,1,'teal','blue','give','short','smile')}
{person(380,352,1.2,-1,'coral','gold','give','bob','smile')}
<g fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"><path d="M270 290h60"/></g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M300 170q-20-26 0-36 20-10 20 14 0-24 20-14 20 10 0 36l-20 20z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('get-away', 'その場から逃げ出すイラスト。', f"""
<g transform="translate(150 250)">
  <path d="M-90-130h180v260h-180z" fill="#dfe6ea" class="o"/>
  <path d="M-50-90h140v220H-50z" fill="#fffaf1" class="o"/>
</g>
{person(430,352,1.2,1,'coral','blue','walk','short','surprised')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M250 300h250"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('get-into', '車の中へ乗り込むイラスト。', f"""
<g transform="translate(400 320)">
  <path d="M-130 0v-40l40-50h150l40 50V0z" class="teal o"/>
  <g fill="#fffdf6" class="o"><rect x="-70" y="-80" width="56" height="36"/><rect x="0" y="-80" width="56" height="36"/></g>
  <g fill="{INK}"><circle cx="-70" cy="6" r="22"/><circle cx="70" cy="6" r="22"/></g>
</g>
{person(150,352,1.15,1,'coral','blue','walk','short','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M210 250h80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('get-through', '狭い通路を抜けきるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-240-150h180v300h-180zM60-150h180v300H60z" fill="#dfe6ea" class="o"/>
</g>
{person(300,352,1.05,1,'teal','blue','walk','short','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M180 130h240"/></g>
{ck(470,330,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('get-together', '人が寄り集まるイラスト。', f"""
{person(200,352,1,1,'teal','blue','stand','short','smile')}
{person(280,352,1,1,'coral','gold','stand','bob','smile')}
{person(360,352,1,-1,'gold','violet','stand','short','smile')}
{person(430,352,1,-1,'green','blue','stand','bun','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M100 300h60M540 300h-60"/></g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="12 10"><ellipse cx="315" cy="250" rx="180" ry="130"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('give-away', 'ただで配ってしまうイラスト。', f"""
{person(160,352,1.2,1,'teal','blue','give','short','smile')}
{person(400,356,0.85,-1,'coral','gold','reach','bob','smile')}
{person(500,356,0.85,-1,'gold','violet','reach','short','smile')}
<g transform="translate(290 250)"><path d="M-36-26h72v52h-72z" class="goldp o"/></g>
<g class="a" marker-end="url(#ar)"><path d="M240 180h120M240 220h190"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('give-in', '手を上げて折れるイラスト。', f"""
{person(200,352,1.25,1,'teal','blue','up','short','sad')}
{person(450,352,1.15,-1,'coral','gold','point','bob','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="6" marker-end="url(#ar)"><path d="M380 250h-90"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('give-off', '光やにおいを放つイラスト。', f"""
{bulb(300,250,1.4,True)}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M120 200q-26 30 0 60M470 200q26 30 0 60M300 380q-30-24-60 0M300 380q30-24 60 0"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('give-out', '大勢に配って回るイラスト。', f"""
{person(300,352,1.2,1,'violet','blue','give','bun','smile')}
{person(120,356,0.8,1,'teal','blue','reach','short','smile')}
{person(480,356,0.8,-1,'coral','gold','reach','bob','smile')}
<g class="paper"><rect x="180" y="240" width="60" height="40"/><rect x="360" y="240" width="60" height="40"/></g>
<g class="a" marker-end="url(#ar)"><path d="M260 200h-90M340 200h90"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('go-ahead', '青信号で先へ進むイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-50-140h100v280h-100z" class="ink"/>
  <circle cx="0" cy="-90" r="30" fill="#4a4a4a"/>
  <circle cx="0" cy="-10" r="30" fill="#4a4a4a"/>
  <circle cx="0" cy="70" r="30" class="green o"/>
</g>
{person(400,352,1.2,1,'teal','blue','walk','short','smile')}
<g class="a" marker-end="url(#ar)"><path d="M300 250h180"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('go-off', '目覚ましが鳴り出すイラスト。', f"""
<g transform="translate(300 250)">
  <circle r="90" fill="#fffdf6" class="o"/>
  <path d="M0 0v-56M0 0l36 22" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <circle r="9" class="ink"/>
  <path d="M-66-70l-28-28M66-70l28-28" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <path d="M-62-72q-28-38 8-58M62-72q28-38-8-58" fill="none" stroke="{INK}" stroke-width="7"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M150 200q-26 50 0 100M100 170q-50 80 0 160M450 200q26 50 0 100M500 170q50 80 0 160"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('go-over', '書いたものを見直すイラスト。', f"""
<g transform="translate(260 230)">
  <path d="M-160-140h320v280h-320z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-120 {-100+i*44}h240"/>' for i in range(5))}</g>
</g>
<g transform="translate(400 240)">
  <circle r="80" fill="none" stroke="{INK}" stroke-width="9"/>
  <circle r="70" fill="#fffdf6" opacity="0.35"/>
  <path d="M58 58l52 52" fill="none" stroke="{INK}" stroke-width="14" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M120 340h340"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('go-through', 'トンネルを通り抜けるイラスト。', f"""
<path d="M0 340V180q0-120 300-120t300 120v160z" class="greenp o"/>
<path d="M180 340V240q0-80 120-80t120 80v100z" fill="#3b3630"/>
{person(300,340,1.05,1,'teal','blue','walk','short','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M120 380h360"/></g>
""", ground=False, arrow=True)

add('hand-in', '書いたものを先生に提出するイラスト。', f"""
{person(160,352,1.2,1,'teal','blue','give','short','neutral')}
{person(470,352,1.2,-1,'violet','violet','reach','bun','smile')}
<g transform="translate(310 250)"><path d="M-44-56h88v112h-88z" class="paper"/></g>
<g class="a" marker-end="url(#ar)"><path d="M240 170h150"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('hand-out', '一人ずつに紙を配るイラスト。', f"""
{person(150,352,1.2,1,'violet','blue','give','bun','smile')}
{sit(320,356,0.8,1,'teal','blue','short','neutral','lap')}
{sit(450,356,0.8,1,'coral','gold','bob','neutral','lap')}
<g class="paper"><rect x="230" y="250" width="56" height="40"/><rect x="380" y="250" width="56" height="40"/></g>
<g class="a" marker-end="url(#ar)"><path d="M220 200h80M300 200h140"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('hang-on', 'ロープにしっかりつかまるイラスト。', f"""
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"><path d="M300 40v200"/></g>
{hand(300,230,1)}
{person(310,352,1.15,1,'teal','blue','up','short','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round"><path d="M420 200l24-24M180 200l-24-24"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('hang-out', 'いっしょにのんびり過ごすイラスト。', f"""
{sit(200,352,1.15,1,'teal','blue','short','smile','down')}
{sit(400,352,1.15,-1,'coral','gold','bob','smile','down')}
<g transform="translate(300 340)">
  <path d="M-70-20h140v20h-140z" class="goldd o"/>
  <path d="M-40-40h30v20h-30zM10-40h30v20H10z" class="tealp o"/>
</g>
{sun(510,100,38)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('hold-back', '前に出ようとするのを押しとどめるイラスト。', f"""
{person(400,352,1.2,1,'coral','blue','reach','short','neutral')}
{hand(180,250,1)}
<g fill="none" stroke="{MUTED}" stroke-width="12" stroke-linecap="round"><path d="M240 250h80"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" marker-end="url(#ar)"><path d="M470 200h70"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="7" marker-end="url(#ar)"><path d="M360 200h-70"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('hold-on', '「ちょっと待って」と手で示すイラスト。', f"""
{person(230,352,1.25,1,'teal','blue','reach','short','neutral')}
{hand(370,230,1)}
<g transform="translate(500 240)">
  <path d="M-40-70h80v140h-80z" class="ink"/>
  <path d="M-30-58h60v110h-60z" fill="{TONES['blue'][1]}"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M430 230h30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('hold-up', '下から支えて持ちこたえるイラスト。', f"""
{person(300,352,1.3,1,'teal','blue','up','short','neutral')}
{box(300,170,240,80,0,'gold')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M160 260v-50M440 260v-50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('keep-on', 'やめずに同じことを続けるイラスト。', f"""
{person(220,352,1.2,1,'teal','blue','walk','short','neutral')}
<g class="ink" opacity="0.5">{''.join(f'<ellipse cx="{80+i*45}" cy="{372+(i%2)*-16}" rx="18" ry="10" transform="rotate(-20 {80+i*45} {372+(i%2)*-16})"/>' for i in range(4))}</g>
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="16 12" marker-end="url(#ar)"><path d="M300 300h240"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('keep-up', '遅れずに横に並んで進むイラスト。', f"""
{person(230,352,1.2,1,'teal','blue','walk','short','neutral')}
{person(360,352,1.2,1,'coral','gold','walk','bob','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M440 250h100"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M295 190v190"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('knock-down', '建っていたものを打ち倒すイラスト。', f"""
<g transform="translate(180 300)">
  <path d="M-60 0v-140h120V0z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>
<g transform="translate(450 340) rotate(80)">
  <path d="M-60 0v-140h120V0z" class="tealp o"/>
</g>
<g class="goldp o"><path d="M380 360l30-10 8 22-30 8z"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('lay-off', '働き手が職を解かれるイラスト。', f"""
{tower(170,320,0.6,'teal',4)}
{person(400,352,1.2,1,'violet','blue','carry','short','sad')}
<g transform="translate(470 320)">
  <path d="M-40-30h80v60h-80z" class="goldd o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M260 250h200"/></g>
{xx(300,150,1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

print(len(W), ' '.join(W))
print(sheet(W))
