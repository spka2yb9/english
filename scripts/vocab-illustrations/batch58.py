"""第58回（2,000語到達）: 多様・疑い・努力・選挙など28語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('diverse', '形も色もさまざまな仲間が集まるイラスト。', f"""
{person(120,346,1.0,1,'coral','gold','stand','bob','smile')}
{person(230,346,1.15,1,'teal','blue','stand','short','smile')}
{person(340,346,0.9,1,'gold','violet','stand','cap','smile')}
{person(450,346,1.1,1,'violet','teal','stand','bob','smile')}
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="70" y="170" width="450" height="190" rx="20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('divine', '天から光が差す、神聖なイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#f6f0dc"/>
<g fill="#f3e3ae" opacity=".75"><path d="M300 40L120 400h360z"/></g>
<g transform="translate(300 110)">
  <circle r="54" fill="#f7e6bd" stroke="#d9c286" stroke-width="3"/>
  <g fill="none" stroke="#d9c286" stroke-width="5"><circle r="80"/></g>
</g>
<g transform="translate(300 340) scale(0.9)">{person(0,0,1.0,1,'violet','blue','up','short','neutral')}</g>
""", ground=False)

add('dizzy', '足もとがふらついて、めまいがするイラスト。', f"""
{face(280,210,90,'flat')}
<g fill="none" stroke="{INK}" stroke-width="4">
  <path d="M232 190a14 14 0 1 0 28 0a14 14 0 1 0-28 0"/>
  <path d="M300 190a14 14 0 1 0 28 0a14 14 0 1 0-28 0"/>
</g>
<path d="M256 260q24 16 48 0" fill="none" stroke="{INK}" stroke-width="5"/>
<g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M400 120q60 30 20 70t40 60" marker-end="url(#ar)"/></g>
<g class="muted"><path d="M120 140q-30 30 0 60t-30 60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('document', '署名欄のある正式な書類のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <g fill="{INK}"><rect x="-130" y="-110" width="150" height="18"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-130 {-60+i*36}h260"/>' for i in range(4))}</g>
  <path d="M-130 90q40-24 80 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><path d="M-130 110h140"/></g>
</g>
""", ground=True)

add('documentary', '現場をそのまま撮った記録番組のイラスト。', f"""
<g transform="translate(330 230)">
  <path d="M-160-120h320v220h-320z" fill="#41506a"/>
  <path d="M-136-96h272v172h-272z" class="bluep"/>
  <g transform="translate(-40 40) scale(0.5)">{person(0,20,1.0,1,'teal','gold','walk','short','neutral')}</g>
  <g class="coral o"><circle cx="-110" cy="-70" r="14"/></g>
</g>
<g transform="translate(140 300)">
  <path d="M-60-40h120v70h-120z" fill="#2f4055"/>
  <path d="M60-20l50-30v70l-50-30z" fill="#2f4055"/>
  <path d="M-30 30h60v40h-60z" fill="#41506a"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('dominant', '一つだけ大きく場を占めているイラスト。', f"""
<path d="M60 340h480" class="a"/>
<g class="tealp o"><rect x="110" y="280" width="70" height="60"/><rect x="440" y="290" width="70" height="50"/></g>
<rect x="220" y="120" width="180" height="220" class="coral o"/>
<path d="M310 80v30" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('doubt', '本当だろうかと、うたぐって首をかしげるイラスト。', f"""
{person(180,346,1.2,1,'teal','blue','think','short','flat')}
<g transform="translate(430 210)">
  <path d="M-120-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-156q-38-4-36-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><path d="M-20-30q0-34 26-34t26 34q0 18-18 24v16h-14v-26q16-6 16-18t-10-12-12 16z"/><rect x="-6" y="28" width="14" height="14"/></g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="290" cy="300" r="12"/><circle cx="266" cy="324" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('drag', '重い箱を床の上で引きずるイラスト。', f"""
{person(400,346,1.15,1,'teal','blue','walk','short','flat')}
<g transform="translate(230 300)">
  <path d="M-70-50h140v90h-140z" class="goldd o"/>
  <path d="M70-20q60 0 90-20" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g class="muted"><path d="M120 350h80M140 370h100"/></g>
<path d="M300 200h100" class="a" marker-end="url(#ar)" transform="rotate(180 350 200)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('drum', 'ばちで打ち鳴らす太鼓のイラスト。', f"""
<g transform="translate(300 270)">
  <ellipse cy="-60" rx="120" ry="40" fill="#f7e6bd" stroke="{INK}" stroke-width="3"/>
  <path d="M-120-60v70a120 40 0 0 0 240 0v-70z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"><path d="M-80-30l40 60M0-20v70M80-30l-40 60"/></g>
</g>
<g transform="translate(200 130) rotate(30)"><path d="M-8-60h16v110h-16z" class="goldd o"/><circle cy="-70" r="16" class="goldd o"/></g>
<g transform="translate(400 130) rotate(-30)"><path d="M-8-60h16v110h-16z" class="goldd o"/><circle cy="-70" r="16" class="goldd o"/></g>
<g class="corals" style="stroke-width:5"><path d="M470 220q26 20 26 44M120 220q-26 20-26 44"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('dual', '二つの口がそろって並ぶ、二重のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-120h380v240h-380z" fill="#dfe6ea" class="o"/>
  <g class="teal o"><rect x="-150" y="-80" width="130" height="160"/><rect x="20" y="-80" width="130" height="160"/></g>
  <g fill="#fffdf6"><rect x="-120" y="-20" width="70" height="20"/><rect x="50" y="-20" width="70" height="20"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 380v-30M420 380v-30"/></g>
""", ground=False, arrow=True)

add('due', 'カレンダーの締め切り日が来たイラスト。', f"""
<g transform="translate(260 220)">
  <path d="M-180-130h360v260h-360z" class="paper"/>
  <path d="M-180-130h360v50h-360z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">{''.join(f'<path d="M{-180+c*90}-80v210"/>' for c in range(1,4))}{''.join(f'<path d="M-180 {-10+r*70}h360"/>' for r in range(2))}</g>
  <circle cx="90" cy="25" r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M64 55l52-60"/></g>
</g>
<g transform="translate(500 130)">
  <circle r="50" fill="#fffdf6" class="o"/>
  <path d="M0-32v32l24 12" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
""", ground=True)

add('dust', '棚にたまったほこりを払うイラスト。', f"""
<g transform="translate(280 290)">
  <path d="M-180-20h360v26h-360z" class="goldd o"/>
  <g fill="#c8c2b0" opacity=".8"><ellipse cx="60" cy="-30" rx="40" ry="14"/><ellipse cx="130" cy="-26" rx="26" ry="10"/></g>
</g>
<g transform="translate(180 220) rotate(20)">
  <path d="M-10-40h20v70h-20z" class="goldd o"/>
  <path d="M-40 30h80l16 60h-112z" fill="#d9b476" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="#c8c2b0" opacity=".9"><circle cx="330" cy="200" r="7"/><circle cx="370" cy="170" r="5"/><circle cx="300" cy="160" r="6"/></g>
<g class="a" marker-end="url(#ar)"><path d="M250 180h80"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('dynamic', '勢いよく動きまわる、活力のあるイラスト。', f"""
<g opacity=".3">{person(170,346,1.2,1,'coral','blue','walk','short','neutral')}</g>
<g opacity=".6">{person(290,346,1.2,1,'coral','blue','up','short','neutral')}</g>
{person(420,346,1.2,1,'coral','blue','walk','short','smile')}
<g class="corals" style="stroke-width:5"><path d="M120 180q-24 16-24 44M500 180q24 16 24 44"/></g>
<path d="M140 150h340" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('eager', '身を乗り出して、しきりにやりたがるイラスト。', f"""
<g transform="translate(220 346) rotate(14)">{person(0,0,1.3,1,'coral','gold','up','bob','smile')}</g>
<g transform="translate(450 230)">
  <path d="M-70-70h140v140h-140z" class="teal o"/>
</g>
<path d="M320 240h50" class="a" marker-end="url(#ar)"/>
<g class="golds" style="stroke-width:5"><path d="M140 170l-26-20M150 210h-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('earthquake', '地面が揺れて建物がきしむ地震のイラスト。', f"""
<g transform="translate(300 250)" >
  <path d="M-120 60h240v-160h-240z" fill="#f4ead2" stroke="{INK}" stroke-width="3" transform="rotate(-5)"/>
</g>
<path d="M60 330q60 20 120 0t120 0t120 0t120 0" fill="none" stroke="{INK}" stroke-width="6"/>
<g fill="none" stroke="{INK}" stroke-width="4"><path d="M200 340l-20 50M300 340l10 50M400 340l-14 50"/></g>
<g class="corals" style="stroke-width:6"><path d="M120 200l-30-24M480 200l30-24M300 120v-30"/></g>
""", ground=False)

add('easily', '軽い荷を片手でひょいと持ち上げるイラスト。', f"""
{person(260,346,1.3,1,'teal','blue','up','short','smile')}
<g transform="translate(260 130)"><path d="M-40-24h80v40h-80z" class="goldp o"/></g>
<g class="golds" style="stroke-width:5"><path d="M370 170l26-20M380 210h30"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M120 200l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('edge', '板のいちばん端を示したイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-200-60h400v120h-400z" class="goldd o"/>
  <path d="M190-60h10v120h-10z" class="coral o"/>
</g>
<circle cx="475" cy="250" r="40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M475 150v50" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('editor', '原稿に手を入れて整える編集者のイラスト。', f"""
{person(150,346,1.1,1,'blue','blue','reach','bob','neutral')}
<g transform="translate(360 230)">
  <path d="M-140-130h280v260h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-100 {-90+i*40}h200"/>' for i in range(5))}</g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M-110-96h80M-40-56h120M-110 24h60"/></g>
</g>
<g transform="translate(240 300) rotate(28)"><path d="M-10-70h20v90h-20z" class="coral o"/><path d="M-10 20h20l-10 22z" class="ink"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('effort', '汗をかきながら、力をふりしぼるイラスト。', f"""
<g transform="translate(300 300) rotate(-16)">{person(0,0,1.25,1,'coral','blue','reach','short','flat')}</g>
<g transform="translate(430 240)"><circle r="60" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/></g>
{drop(250,220,0.8)}{drop(280,180,0.7)}
<g class="corals" style="stroke-width:5"><path d="M180 210l-24-16M190 250h-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('election', '投票箱に票を入れて代表を選ぶイラスト。', f"""
<g transform="translate(360 280)">
  <path d="M-100-60h200v120h-200z" fill="#dfe6ea" class="o"/>
  <path d="M-40-70h80v14h-80z" class="ink"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><rect x="-70" y="-20" width="140" height="60"/></g>
</g>
<g transform="translate(350 170) rotate(-10)">
  <path d="M-50-34h100v56h-100z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><rect x="-38" y="-20" width="18" height="18"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"><path d="M-34-12l10 10 18-22"/></g>
</g>
{person(150,346,1.05,1,'teal','blue','give','bob','smile')}
<path d="M230 220h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('elegant', 'すらりと整った、上品な花びんのイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-50 110q-30-90 10-130t-6-90h92q-46 50-6 90t10 130z" fill="#e7f6fb" stroke="{INK}" stroke-width="3"/>
  <path d="M-20-110h40v-30h-40z" class="tealp o"/>
</g>
<g class="golds" style="stroke-width:5"><path d="M170 150l-26-20M430 150l26-20"/></g>
<path d="M120 366h360" class="a"/>
""", ground=True)

add('elementary', 'いちばん初歩の、易しい段のイラスト。', f"""
<g class="goldd o">{''.join(f'<rect x="{110+i*90}" y="{320-i*50}" width="90" height="{50+i*50}"/>' for i in range(4))}</g>
<g transform="translate(155 290)"><circle r="26" class="coral o"/><path d="M-4-14h8v28h-8z" fill="#fffdf6"/></g>
<path d="M155 200v40" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('emerge', '水の中から姿を現すイラスト。', f"""
<path d="M0 260h600v140H0z" class="bluep"/>
<g fill="none" stroke="#fffdf6" stroke-width="5" opacity=".8"><path d="M20 270q40-20 80 0t80 0t80 0t80 0t80 0t80 0"/></g>
<g transform="translate(300 300)">
  <circle cy="-120" r="40" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-70 60q0-120 70-120t70 120z" class="teal o"/>
</g>
<path d="M430 340v-140" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('emergency', '赤い非常灯がまわる緊急事態のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-70 60h140v-40h-140z" fill="#c9d3dc" class="o"/>
  <path d="M-50 20q0-70 50-70t50 70z" class="coral o"/>
  <g class="corals" opacity=".9" style="stroke-width:6"><path d="M-90-30q-30 20-30 50M90-30q30 20 30 50M0-100v-34"/></g>
</g>
<g transform="translate(300 340)"><path d="M-10-20h20v14h14v20h-14v14h-20v-14h-14v-20h14z" class="coral o"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('emotion', '喜び・怒り・悲しみが胸に湧くイラスト。', f"""
{face(140,200,66,'smile')}
{face(300,200,66,'flat')}
{face(460,200,66,'sad')}
<g transform="translate(300 320)">
  <path d="M0 40c-40-30-56-44-56-66a30 30 0 0 1 56-16 30 30 0 0 1 56 16c0 22-16 36-56 66z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 280l90 20M420 280l-90 20"/></g>
""", ground=False, arrow=True)

add('employer', '人を雇って給料を払う側のイラスト。', f"""
{person(160,346,1.25,1,'blue','blue','give','short','smile')}
<g transform="translate(300 250)">
  <path d="M-60-30h120v50h-120z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <circle r="16" class="goldd o"/>
</g>
{person(470,346,1.05,-1,'teal','gold','reach','bob','smile')}
<path d="M240 300h120" class="a" marker-end="url(#ar)"/>
<circle cx="160" cy="240" r="90" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('encounter', '曲がり角で、ばったり出会うイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-40-140h80v280h-80z" fill="#c9d3dc" class="o"/>
</g>
{person(200,346,1.15,1,'teal','blue','walk','short','surprised')}
{person(400,346,1.15,-1,'coral','gold','walk','bob','surprised')}
<g class="golds" style="stroke-width:5"><path d="M300 130v-26M250 150l-20-20M350 150l20-20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('endless', '道がどこまでも果てなく続くイラスト。', f"""
<path d="M60 380h480" class="a"/>
<path d="M120 380L290 120h20L480 380z" fill="#e6dcc9" stroke="{INK}" stroke-width="2"/>
<g fill="#fffdf6">{''.join(f'<rect x="{296-i*2}" y="{340-i*36}" width="{10-i}" height="{18-i*2}"/>' for i in range(6))}</g>
<g fill="{MUTED}"><circle cx="300" cy="110" r="6" opacity=".8"/></g>
<g class="muted"><path d="M300 100V70"/></g>
<path d="M470 200h50" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
