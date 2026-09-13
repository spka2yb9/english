"""第79回: 地区・寄付・強調・平等など47語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('district', '町の中の一区画を示したイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-200-40h400M-200 50h400M-70-140v280M70-140v280"/></g>
  <path d="M-70-40h140v90h-140z" class="tealp o"/>
</g>
{building(160,330,0.4,'teal')}
<path d="M480 120l-100 60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('domain', '自分の受け持つ領域を囲って示すイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="14 10"><rect x="120" y="150" width="360" height="200" rx="18"/></g>
<g class="tealp o"><circle cx="220" cy="230" r="34"/><rect x="290" y="200" width="60" height="60"/><path d="M420 260l30-50 30 50z"/></g>
{person(120,346,0.7,1,'blue','blue','point','short','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('dominance', '一つが場を占めて優位に立つイラスト。', f"""
<path d="M60 346h480" class="a"/>
<g class="tealp o"><rect x="110" y="290" width="60" height="56"/><rect x="440" y="300" width="60" height="46"/></g>
<rect x="220" y="120" width="180" height="226" class="coral o"/>
<path d="M310 80v30" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('donation', '募金箱にお金を入れて寄付するイラスト。', f"""
{person(170,346,1.1,1,'teal','blue','give','short','smile')}
<g transform="translate(400 280)">
  <path d="M-90-60h180v120h-180z" fill="#dfe6ea" class="o"/>
  <path d="M-40-70h80v14h-80z" class="ink"/>
  <g transform="translate(0 10)"><path d="M0 30c-30-24-42-34-42-52a22 22 0 0 1 42-12 22 22 0 0 1 42 12c0 18-12 28-42 52z" class="coralp o"/></g>
</g>
<g transform="translate(300 180)"><circle r="18" class="goldd o"/></g>
<path d="M260 200q60-30 100 20" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('donor', 'ものを提供してくれる寄贈者のイラスト。', f"""
{person(180,346,1.2,1,'teal','blue','give','bob','smile')}
{box(330,260,100,80,0,'gold')}
{person(490,346,1.1,-1,'coral','gold','reach','short','smile')}
<path d="M250 300h50" class="a" marker-end="url(#ar)"/>
<circle cx="180" cy="240" r="90" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('dot', '小さな点をひとつ打つイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-130h360v260h-360z" class="paper"/>
  <circle r="16" class="ink"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="300" cy="220" r="60"/></g>
<path d="M500 130l-140 60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('downside', '良い面の裏にある欠点を示したイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-160-120h320v240h-320z" fill="#fffdf6" class="o"/>
  <path d="M-160-120h320v120h-320z" class="tealp o"/>
  <path d="M-160 0h320v120h-320z" class="coralp o"/>
  <path d="M-160 0h320" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M480 130l18 18 30-36"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M480 280l28 28M508 280l-28 28"/></g>
""", ground=True)

add('downtown', '店とビルが集まる町の中心街のイラスト。', f"""
<g transform="translate(300 260)">
  <g fill="#dfe6ea" stroke="{INK}" stroke-width="3">
    <rect x="-220" y="-100" width="90" height="180"/><rect x="-120" y="-140" width="100" height="220"/><rect x="-10" y="-110" width="90" height="190"/><rect x="90" y="-160" width="100" height="240"/>
  </g>
  <g fill="#cfe6f5">{''.join(f'<rect x="{-205+c*30}" y="{-80+r*40}" width="20" height="24"/>' for r in range(3) for c in range(2))}{''.join(f'<rect x="{105+c*30}" y="{-140+r*40}" width="20" height="24"/>' for r in range(4) for c in range(2))}</g>
</g>
{person(160,346,0.7,1,'coral','gold','walk','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('dozen', '十二個ひとまとめのイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-100h400v200h-400z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="goldp o">{''.join(f'<ellipse cx="{-160+c*64}" cy="{-50+r*100}" rx="26" ry="34"/>' for r in range(2) for c in range(6))}</g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M100 380h400"/></g>
""", ground=False, arrow=True)

add('drawback', '良い品にひとつだけ難点があるイラスト。', f"""
<g transform="translate(280 240)">
  <path d="M-110-90h220v180h-220z" class="tealp o"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M-70-30l18 18 30-36"/></g>
</g>
<g transform="translate(460 300)">
  <path d="M-50-40h100v80h-100z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M-24-16l48 48M24-16l-48 48"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('drought', '水が枯れて土が割れる干ばつのイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#f6e4c2"/>
{sun(480,90,44)}
<g fill="#c8a978"><path d="M0 280h600v120H0z"/></g>
<g fill="none" stroke="#8b6f4e" stroke-width="4"><path d="M80 320l40 40M200 300l30 50M340 310l20 50M460 300l40 40"/></g>
<g fill="#a8a37f"><path d="M120 280q10-40 30-40t20 40z"/></g>
""", ground=False)

add('dull', '色がくすんで、退屈な感じのイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-80-80h160v160h-160z" fill="#b9b6a8" class="o"/>
</g>
<g transform="translate(430 240)">
  <path d="M-80-80h160v160h-160z" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M280 240h50"/></g>
<g fill="{MUTED}"><rect x="150" y="350" width="40" height="6"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('duo', '二人組のイラスト。', f"""
{person(240,346,1.25,1,'teal','blue','stand','short','smile')}
{person(360,346,1.25,1,'coral','gold','stand','bob','smile')}
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="180" y="180" width="240" height="180" rx="16"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('duration', '始まりから終わりまで続く長さのイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-200-30h400v60h-400z" fill="#dfe6ea" class="o"/>
  <path d="M-200-30h300v60h-300z" class="teal o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M-200-70v140M100-70v140"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M100 350h300M400 350H100"/></g>
""", ground=False, arrow=True)

add('edition', '同じ本の版が刷り直されるイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-80-90h160v180h-160z" class="tealp o"/>
  <g fill="{TONES['teal'][2]}"><rect x="-50" y="-50" width="100" height="16"/><rect x="-30" y="50" width="20" height="10"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-80-90h160v180h-160z" class="teal o"/>
  <g fill="#fffdf6"><rect x="-50" y="-50" width="100" height="16"/><rect x="-34" y="50" width="40" height="10"/></g>
</g>
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('educator', '黒板の前で教える教育者のイラスト。', f"""
<g transform="translate(400 210)">
  <path d="M-150-110h300v190h-300z" fill="#31473d" class="o"/>
  <g fill="none" stroke="#e9f3ec" stroke-width="4"><path d="M-110-60h180M-110-20h220M-110 20h150"/></g>
</g>
{person(140,346,1.15,1,'violet','blue','point','short','smile')}
<path d="M220 210h30" class="a" marker-end="url(#ar)"/>
{person(280,366,0.55,1,'teal','gold','stand','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('effectively', '少ない手数で大きな成果が出るイラスト。', f"""
<g transform="translate(170 260)">
  <g class="tealp o"><rect x="-40" y="-30" width="80" height="60"/></g>
</g>
<g transform="translate(430 240)">
  <path d="M-90-80h180v160h-180z" class="teal o"/>
</g>
<path d="M250 250h100" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 350l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('ego', '鏡に映る自分に見入るイラスト。', f"""
{person(180,346,1.2,1,'violet','blue','point','short','smile')}
<g transform="translate(430 220)">
  <path d="M-90-130h180v260h-180z" fill="#e6f2f7" stroke="{INK}" stroke-width="4"/>
  <g transform="translate(0 126) scale(0.85)">{person(0,0,1.2,-1,'violet','blue','point','short','smile')}</g>
</g>
<path d="M270 220h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('elbow', '腕の関節のひじを示したイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-140 60h80v-50h-80z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-60 60L40 60" fill="none" stroke="{SKIN}" stroke-width="52" stroke-linecap="round"/>
  <path d="M40 60L10-70" fill="none" stroke="{SKIN}" stroke-width="46" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="342" cy="310" r="44"/></g>
<path d="M470 250l-90 40" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('electrical', 'コードと電気の記号のイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-60-60h120v120h-120z" fill="#41506a"/>
  <g fill="#c9d3dc"><rect x="60" y="-40" width="80" height="16"/><rect x="60" y="24" width="80" height="16"/></g>
  <path d="M-60-20q-90 0-90 60" fill="none" stroke="{INK}" stroke-width="10"/>
</g>
<g transform="translate(450 240)">
  <path d="M0-90l-40 100h40l-30 90 80-120h-46l30-70z" fill="#f3c94f" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('elite', '選ばれた少数の精鋭のイラスト。', f"""
<g class="tealp o">{''.join(f'<circle cx="{110+i*46}" cy="300" r="18"/>' for i in range(9))}</g>
{person(300,220,1.0,1,'blue','blue','stand','short','neutral')}
<g transform="translate(300 130)"><path d="M0-24l8 16 18 2-13 13 3 18-16-9-16 9 3-18-13-13 18-2z" class="gold o"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"><circle cx="300" cy="200" r="90"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('embarrassment', '顔を赤くして恥ずかしがるイラスト。', f"""
{face(280,200,95,'flat')}
<g class="coralp"><circle cx="196" cy="230" r="26"/><circle cx="364" cy="230" r="26"/></g>
{drop(370,180,0.7)}
<g class="corals" style="stroke-width:5"><path d="M420 150q26 20 26 44"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('embassy', '国旗を掲げた大使館のイラスト。', f"""
<g transform="translate(320 260)">
  <path d="M-160 80h320v-150h-320z" fill="#f4ead2" class="o"/>
  <path d="M-180-70l180-90 180 90z" class="teal o"/>
  <g class="goldp o"><rect x="-120" y="-30" width="60" height="110"/><rect x="-30" y="-30" width="60" height="110"/><rect x="60" y="-30" width="60" height="110"/></g>
</g>
<g transform="translate(140 200)"><path d="M-4-70h8v100h-8z" class="ink"/><path d="M4-66h60v40H4z" class="coral o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('emission', '煙突から排出される煙のイラスト。', f"""
<g transform="translate(250 280)">
  <path d="M-100 60h200v-120h-200z" fill="#8b8161" stroke="{INK}" stroke-width="3"/>
  <path d="M-60-120h40v60h-40zM20-120h40v60H20z" fill="#6f6a4a"/>
</g>
<g fill="#9b9683" opacity=".9"><ellipse cx="200" cy="120" rx="40" ry="26"/><ellipse cx="270" cy="90" rx="48" ry="30"/><ellipse cx="350" cy="70" rx="40" ry="26"/></g>
<g class="a" marker-end="url(#ar)"><path d="M420 90h60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('emphasis', '大事な語を太くして強調するイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-130h380v260h-380z" class="paper"/>
  <g fill="{MUTED}"><rect x="-150" y="-70" width="90" height="16"/><rect x="30" y="-70" width="120" height="16"/><rect x="-150" y="30" width="140" height="16"/></g>
  <g fill="{INK}"><rect x="-50" y="-76" width="70" height="28"/></g>
  <g class="corals" style="stroke-width:5"><path d="M-30-100q26-20 50 0"/></g>
</g>
""", ground=True)

add('empire', '広い版図を治める帝国のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-140h440v280h-440z" class="paper"/>
  <path d="M-190-100q160-40 240 20t120 160h-360z" class="violetp o"/>
  <path d="M-190-100q160-40 240 20t120 160h-360z" fill="none" stroke="{TONES['violet'][0]}" stroke-width="4"/>
</g>
<g transform="translate(300 120)"><path d="M-40 20l-8-48 24 20 24-32 24 32 24-20-8 48z" class="gold o"/></g>
""", ground=True)

add('encouragement', '声をかけて後押しするイラスト。', f"""
{person(230,346,1.2,1,'blue','blue','reach','short','smile')}
{person(390,346,1.2,1,'coral','gold','walk','bob','smile')}
<path d="M300 250h40" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<g transform="translate(300 150)">
  <path d="M-70-40h140v60h-140z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><rect x="-50" y="-20" width="100" height="14"/></g>
</g>
<path d="M460 250h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('endeavour', '汗をかいて力を尽くすイラスト。', f"""
<g transform="translate(300 300) rotate(-20)">{person(0,0,1.2,1,'coral','blue','reach','short','flat')}</g>
<g transform="translate(430 240)"><circle r="56" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/></g>
{drop(240,220,0.8)}{drop(270,180,0.7)}
<path d="M170 340l180-110" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('endorsement', '推薦の印をつけて後押しするイラスト。', f"""
{person(160,346,1.15,1,'blue','blue','give','short','smile')}
<g transform="translate(340 230)">
  <path d="M-90-80h180v160h-180z" class="paper"/>
  <g fill="{INK}"><rect x="-60" y="-50" width="90" height="14"/></g>
  <g transform="translate(40 40)"><path d="M0-24l8 16 18 2-13 13 3 18-16-9-16 9 3-18-13-13 18-2z" class="gold o"/></g>
</g>
{person(490,346,1.1,-1,'coral','gold','stand','bob','smile')}
<path d="M430 260h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('endurance', '長い道を最後まで走り続ける持久力のイラスト。', f"""
<path d="M80 340q120-60 200 0t220-40" fill="none" stroke="#e6dcc9" stroke-width="14"/>
<g opacity=".35">{person(140,320,0.9,1,'coral','blue','walk','short','neutral')}</g>
<g opacity=".6">{person(300,300,0.9,1,'coral','blue','walk','short','neutral')}</g>
{person(460,290,0.95,1,'coral','blue','walk','short','flat')}
<path d="M140 200h340" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('enforcement', '決まりを守らせて取り締まるイラスト。', f"""
{person(180,346,1.25,1,'blue','blue','point','cap','flat')}
<g transform="translate(420 230)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-50h140M-70-10h140"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M-70 40h140"/></g>
</g>
<path d="M270 220h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('engagement', '指輪を贈って婚約するイラスト。', f"""
{person(230,346,1.2,1,'blue','blue','reach','short','smile')}
{person(380,346,1.2,-1,'coral','gold','reach','bob','smile')}
<g transform="translate(305 240)">
  <circle r="24" fill="none" stroke="{TONES['gold'][0]}" stroke-width="8"/>
  <path d="M0-38l10 16h-20z" class="gold o"/>
</g>
<g transform="translate(305 150)">
  <path d="M0 30c-30-24-42-34-42-52a22 22 0 0 1 42-12 22 22 0 0 1 42 12c0 18-12 28-42 52z" class="coralp o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('enquiry', '窓口で問い合わせるイラスト。', f"""
<g transform="translate(360 290)">
  <path d="M-140-30h280v40h-280z" class="goldd o"/>
  <path d="M-140-30h280v-16h-280z" class="goldp o"/>
</g>
{person(400,240,0.95,-1,'blue','blue','stand','bob','smile')}
{person(150,346,1.05,1,'coral','gold','point','short','neutral')}
<g fill="{INK}" transform="translate(240 180)">
  <path d="M0 0q0-24 18-24t18 24q0 12-12 16v10h-10v-18q12-4 12-12t-7-8-7 12z"/><rect x="11" y="38" width="10" height="10"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('entity', 'ひとつのまとまった実体を示したイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-110-110h220v220h-220z" class="teal o"/>
  <g fill="none" stroke="#fffdf6" stroke-width="4"><path d="M0-110v220M-110 0h220"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><rect x="150" y="70" width="300" height="300" rx="18"/></g>
""", ground=False)

add('entrepreneur', '自分で事業を立ち上げる企業家のイラスト。', f"""
{person(180,346,1.25,1,'blue','blue','carry','short','smile')}
<g transform="translate(180 250)"><path d="M-40-28h80v40h-80z" class="ink"/><path d="M-14-36h28v8h-28z" class="ink"/></g>
{building(430,300,0.8,'teal')}
<g class="golds" style="stroke-width:5"><path d="M300 190l24-18M310 230h28"/></g>
<path d="M270 300h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('envelope', '便りを入れる封筒のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-180-120h360v240h-360z" class="paper"/>
  <path d="M-180-120l180 140 180-140" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-180 120l140-110M180 120L40 10" fill="none" stroke="{MUTED}" stroke-width="3"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('environment', '木と水と空気に囲まれた自然環境のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#eaf5fb"/>
{sun(500,90,30)}
<g class="green o" opacity=".9"><path d="M0 300q150-50 300-20t300-20v140H0z"/></g>
{tree(150,300,1.1)}{tree(430,310,0.9)}
<path d="M240 340q60-20 120 0t120 0" fill="none" stroke="{TONES['blue'][0]}" stroke-width="8"/>
""", ground=False)

add('epidemic', '病が人から人へ広がるイラスト。', f"""
{person(120,346,0.85,1,'coral','gold','stand','short','sad')}
{person(230,346,0.85,1,'coral','gold','stand','bob','sad')}
{person(340,346,0.85,1,'coral','gold','stand','cap','sad')}
{person(450,346,0.85,1,'coral','gold','stand','short','sad')}
<g class="a" marker-end="url(#ar)"><path d="M150 200h50M260 200h50M370 200h50"/></g>
<g transform="translate(120 170)"><circle r="14" class="coral o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('equality', '両方に同じ量が行きわたるイラスト。', f"""
<g transform="translate(300 170)">
  <path d="M-6-40h12v60h-12z" class="ink"/>
  <path d="M-170 20h340" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-170 20v50M170 20v50" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(130 260)"><g class="teal o"><circle r="26"/><circle cx="40" cy="10" r="26"/></g></g>
<g transform="translate(470 260)"><g class="teal o"><circle r="26"/><circle cx="-40" cy="10" r="26"/></g></g>
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M280 340h40M280 370h40"/></g>
""", ground=False)

add('equally', '同じ大きさに等分するイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="130" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="4"><path d="M0 0v-130M0 0l113 65M0 0l-113 65"/></g>
  <path d="M0-130A130 130 0 0 1 113 65z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 370h360"/></g>
""", ground=False, arrow=True)

add('equation', '左右が等しい式のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-90h400v180h-400z" class="paper"/>
  <g fill="{INK}"><rect x="-160" y="-14" width="60" height="16"/><rect x="-84" y="-20" width="14" height="28"/><rect x="-91" y="-14" width="28" height="16"/><rect x="-46" y="-14" width="60" height="16"/></g>
  <g fill="{INK}"><rect x="40" y="-26" width="40" height="10"/><rect x="40" y="0" width="40" height="10"/></g>
  <g fill="{INK}"><rect x="110" y="-14" width="60" height="16"/></g>
</g>
""", ground=True)

add('era', '時代の区切りを示したイラスト。', f"""
<path d="M60 250h480" fill="none" stroke="{MUTED}" stroke-width="5"/>
<g class="tealp o"><rect x="90" y="210" width="140" height="80"/></g>
<g class="coralp o"><rect x="250" y="210" width="140" height="80"/></g>
<g class="goldp o"><rect x="410" y="210" width="130" height="80"/></g>
<g fill="none" stroke="{INK}" stroke-width="4"><path d="M240 190v120M400 190v120"/></g>
<g class="a" marker-end="url(#ar)"><path d="M100 350h400"/></g>
""", ground=False, arrow=True)

add('essence', '余分を落として核だけを残すイラスト。', f"""
<g transform="translate(170 240)">
  <circle r="90" class="tealp o"/>
  <circle r="30" class="teal o"/>
</g>
<g transform="translate(430 240)">
  <circle r="30" class="teal o"/>
</g>
<path d="M290 240h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('ethic', 'してよい事といけない事の線を引くイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-190-130h380v260h-380z" class="paper"/>
  <path d="M0-130v260" fill="none" stroke="{INK}" stroke-width="5"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M-130-40l20 20 34-40"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M70-50l40 40M110-50l-40 40"/></g>
  <g fill="{MUTED}"><rect x="-150" y="40" width="120" height="14"/><rect x="40" y="40" width="120" height="14"/></g>
</g>
""", ground=True)

add('evaluation', '出来ばえに点をつけて評価するイラスト。', f"""
<g transform="translate(280 230)">
  <path d="M-150-130h300v260h-300z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-110-70h220M-110-30h220M-110 10h180"/></g>
  <g class="golds" style="stroke-width:0"></g>
  <g class="gold o"><path d="M-90 80l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z"/><path d="M-20 80l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z"/><path d="M50 80l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z"/></g>
</g>
<g transform="translate(500 320) rotate(24)"><path d="M-10-80h20v110h-20z" class="coral o"/><path d="M-10 30h20l-10 24z" class="ink"/></g>
""", ground=True)

add('eventually', '長くかかって最後に届くイラスト。', f"""
<path d="M80 340q120-70 200 10t220-70" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12"/>
<g opacity=".35">{person(130,340,0.85,1,'teal','blue','walk','short','neutral')}</g>
{person(430,280,1.0,1,'teal','blue','up','short','smile')}
<g transform="translate(520 250)"><path d="M-4-60h8v70h-8z" class="ink"/><path d="M4-56h50v34H4z" class="coral o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('evolution', '形が代を追って変わっていくイラスト。', f"""
<g class="tealp o"><ellipse cx="130" cy="290" rx="34" ry="20"/></g>
<g class="teal o"><ellipse cx="280" cy="280" rx="40" ry="24"/><path d="M240 296h80v20h-80z" opacity=".0"/></g>
<g transform="translate(450 300) scale(0.9)">{person(0,0,1.0,1,'teal','blue','stand','short','neutral')}</g>
<path d="M110 190h360" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
