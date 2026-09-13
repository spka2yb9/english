"""第46回: 禁止・提案・追求・回復など39語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('profile', '横顔と名前欄が並んだ、人物紹介のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-140h380v280h-380z" class="paper"/>
  <g transform="translate(-100 -10)">
    <circle r="60" class="tealp o"/>
    <path d="M-10-40q34 0 34 30 0 14-10 22l14 16q-14 12-38 12t-30-14q10-14 10-34 0-32 20-32z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  </g>
  <g fill="{INK}"><rect x="10" y="-70" width="150" height="16"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M10-20h150M10 20h150M10 60h110"/></g>
</g>
""", ground=True)

add('prohibit', '赤い禁止の輪で、してはいけないと示すイラスト。', f"""
<g transform="translate(300 200)">
  <circle r="110" fill="none" stroke="{TONES['coral'][0]}" stroke-width="22"/>
  <path d="M-78-78l156 156" fill="none" stroke="{TONES['coral'][0]}" stroke-width="22"/>
  <g opacity=".5">{flame(0,30,1.0)}</g>
</g>
{person(500,346,0.9,-1,'teal','blue','stand','short','sad')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('promote', '看板をかかげて、広く売り込むイラスト。', f"""
{person(160,346,1.1,1,'coral','blue','carry','bob','smile')}
<g transform="translate(400 220)">
  <path d="M-130-110h260v190h-260z" fill="#fffdf6" class="o"/>
  <path d="M-100-80h200v90h-200z" class="coralp o"/>
  <g fill="{INK}"><rect x="-80" y="30" width="160" height="18"/></g>
  <path d="M0 80v60" class="ink" stroke="{INK}" stroke-width="8"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M250 150q26-16 50 0M250 190h50"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('proper', 'きちんと収まった置き方と、ずれた置き方を比べたイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-90-90h180v180h-180z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"/>
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
</g>
<g transform="translate(430 240)">
  <path d="M-90-90h180v180h-180z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"/>
  <g transform="rotate(18)"><path d="M-80-60h160v160h-160z" class="coralp o"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M120 370l20 20 34-40"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M400 360l40 40M440 360l-40 40"/></g>
""", ground=True)

add('propose', '案を書いた紙を出して、こうしようと持ちかけるイラスト。', f"""
{person(150,346,1.1,1,'teal','blue','give','short','smile')}
<g transform="translate(320 230)">
  <path d="M-90-80h180v160h-180z" class="paper"/>
  <g fill="{INK}"><rect x="-60" y="-50" width="90" height="12"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-10h120M-60 20h120M-60 50h80"/></g>
</g>
{person(490,346,1.1,-1,'blue','blue','think','bob','neutral')}
<path d="M230 250h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('prosecute', '法廷で、書類を示して罪を訴えるイラスト。', f"""
<g transform="translate(300 130)">
  <path d="M-90 40h180v20h-180z" class="goldd o"/>
  <path d="M-6-60h12v100h-12z" class="ink"/>
  <path d="M-70-60h140v10h-140z" class="ink"/>
  <g class="goldp o"><path d="M-70-50l-30 40h60z"/><path d="M70-50l-30 40h60z"/></g>
</g>
{person(150,346,1.1,1,'violet','blue','point','short','neutral')}
{person(470,346,1.1,-1,'coral','gold','stand','bob','sad')}
<path d="M240 280h140" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('proud', '胸を張って、誇らしげに立つイラスト。', f"""
{person(280,346,1.5,1,'coral','blue','stand','short','smile')}
<g transform="translate(280 236)"><path d="M-16-18l6 16 18 2-13 13 3 18-14-8-14 8 3-18-13-13 18-2z" class="gold o"/></g>
<g class="golds" style="stroke-width:5"><path d="M170 180l-26-20M390 180l26-20M280 130v-26"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('prove', '手がかりを並べて、正しいと示すイラスト。', f"""
<g transform="translate(280 220)">
  <path d="M-180-130h360v260h-360z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-140-80h280M-140-30h280M-140 20h280"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round">
    <path d="M-160-86l12 12 20-24"/><path d="M-160-36l12 12 20-24"/><path d="M-160 14l12 12 20-24"/>
  </g>
</g>
<g transform="translate(500 320)"><path d="M-40-18h80v36h-80z" class="teal o"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="10" stroke-linecap="round"><path d="M470 130l22 22 38-44"/></g>
""", ground=True)

add('provoke', '棒でつついて、相手を怒らせるイラスト。', f"""
{person(150,346,1.05,1,'teal','blue','reach','short','neutral')}
<path d="M210 250h100" fill="none" stroke="{INK}" stroke-width="8"/>
{person(430,346,1.2,-1,'coral','gold','up','bob','flat')}
<g class="corals" style="stroke-width:5"><path d="M500 190q24 24 24 46M540 170q34 34 34 66"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('pub', 'カウンターでジョッキを傾ける酒場のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-240-30h480v40h-240z" class="goldd o"/>
  <path d="M-240-30h480v40h-480z" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(200 240)">
  <path d="M-40-60h70v90h-70z" fill="#f7e6bd" stroke="{INK}" stroke-width="3"/>
  <path d="M-40-60h70v-16h-70z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M30-40q30 0 30 24t-30 24" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
{person(420,290,0.95,-1,'teal','blue','stand','bob','smile')}
{person(510,290,0.95,-1,'coral','gold','stand','short','smile')}
<path d="M60 350h480" class="a"/>
""", ground=True)

add('public', 'だれでも入れる公園で、みんなが過ごすイラスト。', f"""
{sun(510,90,28)}
{tree(120,320,1.0)}
<g transform="translate(300 300)"><path d="M-70-20h140v18h-140z" class="goldd o"/><path d="M-60-2h14v30h-14zM46-2h14v30H46z" class="goldd o"/></g>
{person(220,300,0.8,1,'teal','blue','stand','short','smile')}
{person(380,300,0.8,-1,'coral','gold','stand','bob','smile')}
{person(470,330,0.85,1,'violet','blue','walk','cap','smile')}
<path d="M60 340h480" class="a"/>
""", ground=True)

add('punch', 'こぶしを突き出して打つイラスト。', f"""
{person(180,346,1.25,1,'coral','blue','point','short','flat')}
<g transform="translate(330 230)">
  <circle r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <g fill="none" stroke="{SKINL}" stroke-width="2.5"><path d="M-10-14h24M-10 0h24M-10 14h20"/></g>
</g>
<g transform="translate(430 230)">
  <path d="M0-60l16 34 36-12-18 34 30 24-38 4 8 36-34-22-30 26 2-38-38-6 26-28-22-30 38 8z" class="coralp o"/>
</g>
<path d="M250 200h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('purchase', 'お金を渡して品物を買うイラスト。', f"""
{person(140,346,1.05,1,'teal','blue','give','short','smile')}
<g transform="translate(280 250)">
  <path d="M-60-30h120v50h-120z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <circle r="16" class="goldd o"/>
</g>
<g transform="translate(430 260)">{box(0,0,120,90,26,'gold')}</g>
<path d="M200 200h40" class="a" marker-end="url(#ar)"/>
<path d="M380 320h-80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('pure', '混じり気のない澄んだ水と、濁った水を比べたイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-70-90h140l-14 180h-112z" fill="#f7fbfe" class="o"/>
  <path d="M-62-40h124l-10 130h-104z" fill="#d6effa" class="o"/>
</g>
<g transform="translate(430 240)">
  <path d="M-70-90h140l-14 180h-112z" fill="#f7fbfe" class="o"/>
  <path d="M-62-40h124l-10 130h-104z" fill="#c8bfa4" class="o"/>
  <g fill="#8b8161"><circle cx="-20" cy="20" r="9"/><circle cx="24" cy="50" r="7"/><circle cx="0" cy="70" r="8"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M120 370l20 20 34-40"/></g>
""", ground=True)

add('pursue', '目標を追いかけて、どこまでも進むイラスト。', f"""
{person(140,346,1.1,1,'teal','blue','walk','short','neutral')}
<path d="M220 250h200" fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="14 10" marker-end="url(#ar)"/>
<g transform="translate(490 230)">
  <circle r="60" fill="#fffdf6" class="o"/>
  <circle r="40" class="coralp o"/>
  <circle r="18" class="coral o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('queen', '王冠をかぶった女王のイラスト。', f"""
{person(300,346,1.5,1,'violet','violet','stand','bob','smile')}
<g transform="translate(300 172)"><path d="M-46 22l-10-58 28 24 28-40 28 40 28-24-10 58z" class="gold o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('quote', '本の一節をそのまま抜き出して示すイラスト。', f"""
<g transform="translate(170 220)">
  <path d="M-110-130h220v260h-220z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-80 {-90+i*36}h160"/>' for i in range(6))}</g>
  <path d="M-84-24h168v40h-168z" class="goldp o" opacity=".8"/>
</g>
<g transform="translate(440 220)">
  <path d="M-110-90h220v180h-220z" fill="#fffdf6" class="o"/>
  <g fill="{TONES['teal'][0]}"><path d="M-80-50q-20 20-20 40h24v24h-32v-24q0-26 28-40zM-20-50q-20 20-20 40h24v24h-32v-24q0-26 28-40z"/></g>
  <g fill="{INK}"><rect x="-80" y="10" width="160" height="12"/><rect x="-80" y="40" width="110" height="12"/></g>
</g>
<path d="M300 210h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('railway', '二本のレールがまっすぐ延びる線路のイラスト。', f"""
<g transform="translate(300 260)">
  <g fill="#b09274">{''.join(f'<rect x="{-250+i*50}" y="0" width="34" height="80" transform="skewX(-6)"/>' for i in range(11))}</g>
  <path d="M-230 100L-60-30M230 100L60-30" fill="none" stroke="#8b98a6" stroke-width="12"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('raise', '腕を伸ばして、物を高く持ち上げるイラスト。', f"""
{person(280,346,1.3,1,'teal','blue','up','short','neutral')}
<g transform="translate(280 130)"><path d="M-60-30h120v50h-120z" class="goldd o"/></g>
<path d="M400 280v-120" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('rally', '旗を立てて人が集まる集会のイラスト。', f"""
{person(150,346,1.0,1,'coral','blue','up','short','neutral')}
{person(250,346,1.0,1,'gold','blue','up','bob','neutral')}
{person(350,346,1.0,1,'teal','gold','up','cap','neutral')}
{person(450,346,1.0,1,'violet','blue','up','short','neutral')}
<g transform="translate(300 140)">
  <path d="M-4-60h8v100h-8z" class="ink"/>
  <path d="M4-56h90v50H4z" class="coralp o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('rank', '高さの順に並べて、順位を示したイラスト。', f"""
<path d="M60 340h480" class="a"/>
<g class="tealp o"><rect x="300" y="180" width="90" height="160"/><rect x="410" y="220" width="90" height="120"/></g>
<rect x="190" y="140" width="90" height="200" class="coral o"/>
<g transform="translate(235 100)"><circle r="26" class="gold o"/><path d="M-4-14h8v28h-8z" fill="#fffdf6"/></g>
""", ground=False)

add('rare', 'たくさんの同じ石の中に、一つだけ違う宝石があるイラスト。', f"""
<g class="mutedfill" fill="#c9d3dc" stroke="{INK}" stroke-width="2">
  {''.join(f'<circle cx="{110+c*70}" cy="{170+r*70}" r="26"/>' for r in range(3) for c in range(6))}
</g>
<g transform="translate(320 240)">
  <path d="M0-40l34 20v40L0 40l-34-20v-40z" class="violet o"/>
  <path d="M0-40v80" fill="none" stroke="#fffdf6" stroke-width="3"/>
</g>
<circle cx="320" cy="240" r="52" fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
""", ground=False)

add('reassure', '肩に手をそえて、大丈夫だと安心させるイラスト。', f"""
{person(230,346,1.15,1,'blue','blue','reach','short','smile')}
{person(370,346,1.15,-1,'coral','gold','stand','bob','smile')}
<path d="M300 250h20" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 180l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('rebuild', 'こわれた家を建て直すイラスト。', f"""
<g transform="translate(160 280)" opacity=".5">
  <path d="M-80 60h160v-90h-160z" fill="#d8d2c2" stroke="{INK}" stroke-width="3"/>
  <path d="M-80-30l40-50h80l-30 40" fill="none" stroke="{INK}" stroke-width="3"/>
  <g class="muted"><path d="M-40 20h40M0-10h40"/></g>
</g>
<g transform="translate(430 280)">
  <path d="M-90 60h180v-100h-180z" fill="#f4ead2" class="o"/>
  <path d="M-110-40l110-70 110 70z" class="coral o"/>
  <path d="M-30 60V10h60v50z" class="goldd o"/>
</g>
<path d="M260 220h60" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('recall', '昔の場面を思い出して、頭に呼び戻すイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','think','short','neutral')}
<g transform="translate(420 200)">
  <path d="M-120-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-156q-38-4-36-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 6) scale(0.5)">
    <path d="M-90-50h180v110h-180z" class="paper"/>
    <path d="M-60 50l50-70 34 34 30-44 30 80z" class="tealp o"/>
  </g>
</g>
<path d="M300 260q-40-40-10-70" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('recent', 'カレンダーで、いまに近い日を示したイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-130h400v260h-400z" class="paper"/>
  <path d="M-200-130h400v50h-400z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">{''.join(f'<path d="M{-200+c*100}-80v210"/>' for c in range(1,4))}{''.join(f'<path d="M-200 {-10+r*70}h400"/>' for r in range(2))}</g>
  <g opacity=".3"><circle cx="-150" cy="-45" r="24" class="muted"/><circle cx="-50" cy="-45" r="24" class="muted"/></g>
  <circle cx="150" cy="60" r="28" class="coral o"/>
</g>
<path d="M470 130v50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('reception', '入口の受付カウンターで迎えられるイラスト。', f"""
<g transform="translate(360 290)">
  <path d="M-140-40h280v80h-280z" class="goldd o"/>
  <path d="M-140-40h280v-16h-280z" class="goldp o"/>
</g>
<g transform="translate(300 220)"><circle r="16" class="gold o"/><path d="M-20 16h40v6h-40z" class="ink"/></g>
{person(430,230,0.9,-1,'blue','blue','stand','bob','smile')}
{person(150,346,1.0,1,'teal','gold','walk','short','smile')}
<path d="M210 300h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('recipe', '材料と手順が書かれた作り方の紙のイラスト。', f"""
<g transform="translate(240 220)">
  <path d="M-150-140h300v280h-300z" class="paper"/>
  <g fill="{INK}"><rect x="-110" y="-110" width="140" height="16"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-110 {-60+i*36}h220"/>' for i in range(5))}</g>
  <g class="teal o"><circle cx="-124" cy="-64" r="8"/><circle cx="-124" cy="-28" r="8"/><circle cx="-124" cy="8" r="8"/></g>
</g>
<g transform="translate(470 280)">
  <path d="M-60 20h120l-12-60h-96z" fill="#dfe6ea" class="o"/>
  <path d="M-60-40h120v-12h-120z" fill="#c9d3dc" class="o"/>
  <g class="muted"><path d="M-24-70q0-26 20-26M20-70q0-26 20-26"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('reckon', '指を折って、だいたいの数を見積もるイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','think','short','neutral')}
{hand(310,220,1)}
<g transform="translate(440 210)">
  <path d="M-90-70h180v140h-180z" class="paper"/>
  <g fill="{INK}"><rect x="-60" y="-40" width="50" height="10"/><rect x="10" y="-40" width="50" height="10"/><rect x="-60" y="0" width="120" height="6"/><rect x="-10" y="30" width="70" height="10"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('recording', '音の波を吹き込んで録音するイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-30-90h60v120h-60z" fill="#41506a"/>
  <circle cy="-90" r="34" fill="#7f8ea6" stroke="{INK}" stroke-width="3"/>
  <path d="M-40 30h80v20h-80z" class="ink"/>
</g>
<g transform="translate(410 230)">
  <path d="M-130-70h260v140h-260z" fill="#f7fbfe" class="o"/>
  <g fill="{TONES['teal'][0]}">{''.join(f'<rect x="{-110+i*22}" y="{-int(50*[0.3,0.7,1,0.5,0.9,0.4,0.8,0.6,1,0.35][i])}" width="12" height="{int(100*[0.3,0.7,1,0.5,0.9,0.4,0.8,0.6,1,0.35][i])}"/>' for i in range(10))}</g>
</g>
<g class="coral o"><circle cx="300" cy="150" r="14"/></g>
<path d="M240 230h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('recount', '出来事の場面を順に、くわしく語るイラスト。', f"""
{person(140,346,1.1,1,'teal','blue','point','short','neutral')}
<g transform="translate(390 220)">
  <g class="paper"><path d="M-160-100h100v90h-100z"/><path d="M-40-100h100v90h-100z"/><path d="M80-100h100v90H80z"/></g>
  <g class="tealp o"><circle cx="-110" cy="-56" r="20"/><rect x="-30" y="-76" width="60" height="40"/></g>
  <path d="M110-30l30-40 30 40z" class="coralp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-160 20h320M-160 50h320M-160 80h240"/></g>
</g>
<path d="M220 200h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('recruit', '募集の貼り紙を見て、新しい人が加わるイラスト。', f"""
<g transform="translate(180 210)">
  <path d="M-110-120h220v220h-220z" class="paper"/>
  <g fill="{INK}"><rect x="-80" y="-90" width="160" height="18"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-80-40h160M-80 0h160M-80 40h110"/></g>
</g>
{person(400,346,1.0,1,'teal','blue','stand','short','neutral')}
{person(490,346,1.0,1,'gold','blue','stand','bob','neutral')}
{person(320,346,1.0,1,'coral','gold','walk','cap','smile')}
<path d="M250 300h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('regain', '失ったものが、また手もとに戻るイラスト。', f"""
{person(160,346,1.1,1,'teal','blue','reach','short','smile')}
<g transform="translate(420 250)">
  <path d="M-50-50h100v100h-100z" class="gold o"/>
</g>
<g opacity=".3" transform="translate(300 180)"><path d="M-40-40h80v80h-80z" class="muted"/></g>
<path d="M370 280q-90 40-130-20" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('regard', '相手をこういう人だとみなして見るイラスト。', f"""
{person(150,346,1.05,1,'teal','blue','point','short','neutral')}
{person(430,346,1.15,-1,'coral','gold','stand','bob','smile')}
<g transform="translate(430 180)">
  <path d="M-70-40h140v56h-140z" class="paper"/>
  <path d="M-14 16l14 16 14-16z" class="paper"/>
  <g transform="translate(0 -12)"><path d="M-16-16l6 14 16 2-12 11 3 16-13-8-13 8 3-16-12-11 16-2z" class="gold o"/></g>
</g>
<path d="M230 240h100" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('regional', '地図の中の一つの地域を色分けしたイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-140v280M80-140v280M-200 0h400"/></g>
  <path d="M-60 0h140v140H-60z" class="teal o"/>
</g>
<path d="M120 130q60-60 120-30" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('regular', '同じ間隔でくり返す印のイラスト。', f"""
<path d="M60 250h480" fill="none" stroke="{MUTED}" stroke-width="4"/>
<g class="teal o">{''.join(f'<circle cx="{100+i*70}" cy="250" r="24"/>' for i in range(7))}</g>
<g class="a" marker-end="url(#ar)"><path d="M100 330h60M170 330h-60"/></g>
<g class="a" marker-end="url(#ar)"><path d="M240 330h60M310 330h-60"/></g>
""", ground=False, arrow=True)

add('reign', '玉座にすわって国をおさめるイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-90-120h180v40h-180z" class="violetp o"/>
  <path d="M-70-80h140v80h-140z" class="violet o"/>
  <path d="M-70 0h30v60h-30zM40 0h30v60H40z" class="violetd o"/>
</g>
<g transform="translate(300 200) scale(0.9)">{person(0,50,1.0,1,'gold','violet','stand','bob','neutral')}</g>
<g transform="translate(300 130)"><path d="M-40 20l-8-50 24 20 24-34 24 34 24-20-8 50z" class="gold o"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('reinforce', '弱い柱に支えを足して補強するイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-16-100h32v200h-32z" fill="#c9d3dc" class="o"/>
  <g class="corals" style="stroke-width:4"><path d="M30-40q20 20 0 40"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-16-100h32v200h-32z" fill="#c9d3dc" class="o"/>
  <path d="M-16-60l-70 160h24l62-140zM16-60l70 160h-24l-62-140z" class="teal o"/>
</g>
<path d="M260 240h60" class="a" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('reject', '差し出された紙を、受け取らずに突き返すイラスト。', f"""
{person(150,346,1.05,1,'teal','blue','give','short','neutral')}
<g transform="translate(300 230)">
  <path d="M-70-60h140v120h-140z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-46-30h92M-46 0h92"/></g>
</g>
{person(470,346,1.1,-1,'blue','blue','point','bob','flat')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"><path d="M360 180l50 50M410 180l-50 50"/></g>
<path d="M380 300h-80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
