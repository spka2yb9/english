"""第99回: 残りの動詞・形容詞・名詞45語。"""
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

add('tighten', 'ボルトをしっかり締めるイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-160-40h320v80h-320z" fill="#b9c2c9" class="o"/>
  <path d="M-46-46l46-26 46 26v52l-46 26-46-26z" class="goldd o"/>
  <circle r="22" class="gold o"/>
</g>
<g transform="translate(300 250) rotate(30)">
  <path d="M-10 40h20v130h-20z" fill="{MUTED}" class="o"/>
  <path d="M-40 20h80v30h-80z" fill="{MUTED}" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M420 120a90 90 0 0 1 40 60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('tourism', 'カメラを手に名所をめぐる観光のイラスト。', f"""
<g transform="translate(430 240)">
  <path d="M-70 110L-14-70h28l56 180z" class="teal o"/>
  <path d="M-14-70l14-50 14 50z" class="tealp o"/>
</g>
{person(180,352,1.2,1,'coral','blue','hold','bob','smile')}
<g transform="translate(180 240)">
  <path d="M-50-24h100v48h-100z" class="ink"/>
  <circle cx="10" cy="0" r="16" class="bluep o"/>
  <path d="M-40-36h30v12h-30z" class="ink"/>
</g>
<g transform="translate(280 330)">
  <path d="M-34-26h68v52h-68z" class="goldd o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tradition', '古くから受け継がれてきた作法のイラスト。', f"""
<g transform="translate(430 300)">
  <path d="M-90 0v-56h180V0z" fill="#fffdf6" class="o"/>
  <path d="M-110-56h220l-30-30h-160z" class="corald o"/>
  <path d="M-80-86h160l-26-30h-108z" class="coral o"/>
</g>
{person(160,352,1.15,1,'violet','violet','give','bun','smile')}
{person(300,354,0.95,-1,'teal','blue','reach','short','smile')}
<g transform="translate(230 280)">
  <path d="M-34-16h68v32h-68z" class="goldp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M190 210h80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('ultimately', '長い道の末についにたどり着くイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="16 12"><path d="M100 340q80-120 180-60t100-140"/></g>
{person(100,352,0.9,1,'teal','blue','walk','short','neutral')}
<g transform="translate(470 250)">
  <path d="M-6 106V-70" class="a"/>
  <path d="M-6-70h90l-18 26 18 26H-6z" class="coral o"/>
</g>
{ck(470,300,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('unemployed', '働き口がなく職を探しているイラスト。', f"""
{person(180,352,1.25,1,'teal','blue','carry','short','sad')}
<g transform="translate(270 290)">
  <path d="M-40-50h80v100h-80z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-24-24h48M-24 0h48M-24 24h32"/></g>
</g>
<g transform="translate(450 250)">
  <path d="M-110-80h220v160h-220z" fill="#fffdf6" class="o"/>
</g>
{xx(450,250,1.4)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('unify', 'ばらばらの旗をひとつにまとめるイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-70-60h60v40h-60zM10-60h60v40H10zM-70 10h60v40h-60zM10 10h60v40H10z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 240h60"/></g>
<g transform="translate(460 250)">
  <path d="M-6 100V-100" class="a"/>
  <path d="M-6-100h110v70H-6z" class="teal o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('upwards', '上向きに上がっていくイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="20" stroke-linecap="round" marker-end="url(#ar)"><path d="M300 340V120"/></g>
<g class="tealp o"><circle cx="160" cy="250" r="24"/><circle cx="440" cy="220" r="20"/><circle cx="180" cy="150" r="18"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M160 290v30M440 260v30M180 190v30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('utterly', 'ひとつも残らずまったくの状態のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-140-130h280v260h-280z" fill="#fffdf6" class="o"/>
</g>
{xx(300,240,2.4,MUTED)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M120 350h360M120 350v-24M480 350v-24"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('vary', '大きさも色もそれぞれ違うイラスト。', f"""
<circle cx="130" cy="250" r="26" class="tealp o"/>
<circle cx="240" cy="230" r="46" class="coralp o"/>
<circle cx="360" cy="250" r="34" class="goldp o"/>
<circle cx="480" cy="220" r="56" class="violetp o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M120 350q40-24 80 0t80 0 80 0 80 0"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('venture', '思い切って新しい事業に踏み出すイラスト。', f"""
<path d="M60 350h180v40H60zM380 350h160v40H380z" fill="#dfe6ea" class="o"/>
{person(200,350,1.15,1,'teal','blue','walk','short','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="16 12" marker-end="url(#ar)"><path d="M250 300h180"/></g>
<g transform="translate(470 260)">
  <path d="M-6 90V-70" class="a"/>
  <path d="M-6-70h80l-16 24 16 24H-6z" class="coral o"/>
</g>
<path d="M60 390h480" class="a"/>
""", ground=True, arrow=True)

add('versus', '両者を向かい合わせて対にするイラスト。', f"""
<g transform="translate(150 240)">
  <path d="M-80-80h160v70q0 80-80 110-80-30-80-110z" class="tealp o"/>
</g>
<g transform="translate(450 240)">
  <path d="M-80-80h160v70q0 80-80 110-80-30-80-110z" class="coralp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="12" stroke-linejoin="round">
  <path d="M270 180l30 60 30-60"/>
  <path d="M270 300h60"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('via', '途中の地点を通って行くイラスト。', f"""
<g class="ink"><circle cx="110" cy="330" r="18"/><circle cx="300" cy="180" r="18"/><circle cx="500" cy="330" r="18"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M130 320l150-120M320 200l160 116"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><circle cx="300" cy="180" r="46"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('warrant', '判の押された令状のイラスト。', f"""
<g transform="translate(280 220)">
  <path d="M-160-150h320v300h-320z" class="paper"/>
  <path d="M-130-120h260v40h-260z" class="ink"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-130 {-40+i*44}h260"/>' for i in range(3))}</g>
  <circle cx="90" cy="100" r="40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
  <path d="M64 100h52M90 74v52" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
</g>
{hand(520,300,-1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('way', '差がとてつもなく大きいイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-230 0h100v60h-100z" class="tealp o"/>
  <path d="M120-250h110v310H120z" class="coral o"/>
  <path d="M-240 60h480" class="a"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M60 300V70"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('weave', '縦糸と横糸を組んで織るイラスト。', f"""
<g transform="translate(300 220)">
  <g stroke="{TONES['teal'][0]}" stroke-width="16" fill="none">{''.join(f'<path d="M{-180+i*45} -140v280"/>' for i in range(9))}</g>
  <g stroke="{TONES['coral'][0]}" stroke-width="16" fill="none">{''.join(f'<path d="M-190 {-100+i*50}h380"/>' for i in range(5))}</g>
  <g stroke="{TONES['teal'][0]}" stroke-width="16" fill="none">{''.join(f'<path d="M{-180+i*90} -140v280"/>' for i in range(5))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('whereas', '一方はこう、他方はこうと並べるイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-100-110h200v220h-200z" class="tealp o"/>
  <circle r="50" class="teal o"/>
</g>
<g transform="translate(430 230)">
  <path d="M-100-110h200v220h-200z" class="coralp o"/>
  <path d="M-50-50h100v100h-100z" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="14 12"><path d="M300 100v260"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('wherever', 'どこへ行こうともついていくイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-240-140q90-40 180-10t180 0v240q-100 40-190 0t-170 10z" class="greenp o"/>
</g>
<g class="coral o"><circle cx="150" cy="150" r="16"/><circle cx="300" cy="250" r="16"/><circle cx="450" cy="140" r="16"/></g>
{ck(150,200,0.7)}
{ck(300,300,0.7)}
{ck(450,190,0.7)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M150 150q80 120 150 100t150-110"/></g>
""", ground=False)

add('widely', '広い範囲にわたって行きわたるイラスト。', f"""
<g class="tealp o">
  {''.join(f'<circle cx="{80+c*72}" cy="{140+r*70}" r="24"/>' for r in range(4) for c in range(7))}
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M300 380H60M300 380h240"/></g>
""", ground=False, arrow=True)

add('achievement', 'やり遂げて頂に立つ達成のイラスト。', f"""
<path d="M0 380l190-230 110 130 80-90 220 190z" class="greenp o"/>
{person(190,150,0.75,1,'coral','blue','up','short','smile')}
<g transform="translate(250 110)">
  <path d="M-6 40V-60" class="a"/>
  <path d="M-6-60h70l-14 20 14 20H-6z" class="coral o"/>
</g>
{star(430,120,30,'gold')}
<path d="M0 380h600" class="a"/>
""", ground=False)

add('agricultural', '納屋と麦畑のある農業のイラスト。', f"""
<g transform="translate(450 290)">
  <path d="M-90 0v-80h180V0z" class="coral o"/>
  <path d="M-104-80L0-140l104 60z" class="corald o"/>
  <path d="M-30-46h60V0h-60z" fill="#fffdf6" class="o"/>
</g>
<g class="golds" stroke-width="5">{''.join(f'<path d="M{100+i*60} 340v-90"/>' for i in range(5))}</g>
<g class="gold o">{''.join(f'<ellipse cx="{100+i*60}" cy="232" rx="13" ry="30"/>' for i in range(5))}</g>
<path d="M0 340h600" class="a"/>
""", ground=True)

add('bear', '重い荷を肩に担いで負うイラスト。', f"""
{person(300,352,1.3,1,'teal','blue','up','short','neutral')}
{box(300,180,200,90,30,'gold')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M480 200v70M120 200v70"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('beneficial', '水をやると育ちがよくなる有益さのイラスト。', f"""
<g transform="translate(170 330)">
  <path d="M0 0v-50" class="greens"/>
  <path d="M0-30q-30-4-34-30 28-4 34 30z" class="greenp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 240h60"/></g>
<g transform="translate(440 330)">
  <path d="M0 0v-140" class="greens"/>
  <path d="M0-80q-50-8-58-50 48-8 58 50zM0-104q50-8 58-50-48-8-58 50z" class="greenp o"/>
</g>
{drop(230,180,1.5,'blue')}
{ck(440,140,1)}
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('bill', '払う額の書かれた請求書のイラスト。', f"""
<g transform="translate(280 210)">
  <path d="M-130-150h260v290l-26-20-26 20-26-20-26 20-26-20-26 20-26-20-26 20z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-96-110h190M-96-70h190M-96-30h150"/></g>
  <path d="M-96 20h190" fill="none" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="10" y="40" width="84" height="16"/></g>
</g>
{hand(500,300,-1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('career', '年を重ねて職の階段を上るイラスト。', f"""
<g transform="translate(300 330)">
  <path d="M-230 0h110v-40h-110zM-120-40h110v-70h-110zM-10-110h110v-100H-10z" class="tealp o"/>
</g>
{person(130,326,0.8,1,'teal','blue','walk','short','smile')}
{person(240,286,0.85,1,'teal','blue','walk','short','smile')}
{person(350,216,0.95,1,'violet','blue','up','short','smile')}
<g class="a" marker-end="url(#ar)"><path d="M100 380h420"/></g>
""", ground=False, arrow=True)

add('challenge', '目の前の高い壁に立ち向かうイラスト。', f"""
<g transform="translate(430 250)">
  <path d="M-100-160h200v300h-200z" fill="#b9c2c9" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">{''.join(f'<path d="M-100 {-120+i*50}h200"/>' for i in range(5))}</g>
</g>
{person(190,352,1.25,1,'coral','blue','reach','short','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M250 240q40-140 170-160"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('characteristic', 'そのものだけが持つ目印のイラスト。', f"""
<g transform="translate(300 230)">
  <g class="tealp o">{''.join(f'<circle cx="{-200+i*100}" cy="0" r="46"/>' for i in range(5))}</g>
  <circle cx="0" cy="0" r="46" class="teal o"/>
  <path d="M-20-20h40v40h-40z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="300" cy="230" r="70"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('chemical', 'びんに入った化学物質のイラスト。', f"""
<g transform="translate(200 260)">
  <path d="M-60-120h120v40h-120z" class="goldd o"/>
  <path d="M-70-80h140v180h-140z" fill="#fffdf6" class="o"/>
  <path d="M-70 0h140v100h-140z" class="green o"/>
  <path d="M-40-50h80v40h-80z" class="paper"/>
  <path d="M0-46l16 28h-32z" fill="{TONES['coral'][0]}"/>
</g>
<g transform="translate(440 220)">
  <circle cx="-50" cy="0" r="30" class="tealp o"/>
  <circle cx="50" cy="0" r="30" class="tealp o"/>
  <circle cx="0" cy="60" r="30" class="coralp o"/>
  <g fill="none" stroke="{INK}" stroke-width="5"><path d="M-24 10l50 34M24 10l-50 34M-20 0h40"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('comment', '文書に意見を書き添えるイラスト。', f"""
<g transform="translate(230 220)">
  <path d="M-140-150h280v300h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-100 {-110+i*44}h200"/>' for i in range(6))}</g>
</g>
<g transform="translate(460 180)">
  <path d="M-110-70h220v110h-220zM-70 40l-14 34 44-34z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="5"><path d="M-76-36h152M-76-6h110"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M370 250h-60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('commercial', 'テレビで流れる広告のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-200-140h400v260h-400z" class="ink"/>
  <path d="M-184-126h368v232h-368z" fill="#fffdf6"/>
  <path d="M-140-90h150v130h-150z" class="coralp o"/>
  <circle cx="-65" cy="-25" r="46" class="coral o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="9"><path d="M40-60h120M40-20h120M40 20h90"/></g>
  <path d="M-60 120v30M60 120v30" class="a"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('committee', '名札を置いた円卓の委員会のイラスト。', f"""
<g transform="translate(300 280)">
  <ellipse rx="220" ry="80" class="goldd o"/>
  <ellipse cy="-14" rx="220" ry="80" class="gold o"/>
</g>
{sit(140,250,0.7,1,'teal','blue','short','neutral','lap')}
{sit(260,240,0.7,1,'coral','gold','bob','neutral','lap')}
{sit(380,240,0.7,-1,'gold','violet','short','neutral','lap')}
{sit(490,250,0.7,-1,'green','blue','bun','neutral','lap')}
<g class="paper">{''.join(f'<rect x="{170+i*90}" y="272" width="60" height="24"/>' for i in range(4))}</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('communist', '赤い旗のもとに集まる共産主義のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-6 130V-120" class="a"/>
  <path d="M-6-120h150v90H-6z" class="coral o"/>
  <path d="M60-90l8 18 20 2-14 14 4 20-18-10-18 10 4-20-14-14 20-2z" fill="#fffdf6"/>
</g>
{person(150,352,0.85,1,'coral','blue','stand','cap','neutral')}
{person(440,352,0.85,-1,'coral','blue','stand','short','neutral')}
{person(510,352,0.85,-1,'coral','blue','stand','bob','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('conclusion', '話のいちばん最後にたどりつく結びのイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-200-150h400v300h-400z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">
    {''.join(f'<path d="M-160 {-110+i*40}h320"/>' for i in range(5))}
  </g>
  <path d="M-160 100h200v40h-200z" class="teal o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M-170 80h340"/></g>
</g>
""", ground=False)

add('condition', '調子のよしあしを見るイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-150 0a150 150 0 0 1 300 0z" fill="#fffdf6" class="o"/>
  <path d="M-150 0h300" class="a"/>
  <path d="M-150 0A150 150 0 0 1-50-141l50 141z" class="coralp"/>
  <path d="M150 0A150 150 0 0 0 50-141L0 0z" class="greenp"/>
  <path d="M0 0l60-120" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <circle r="11" class="ink"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('conference', '大勢が集まって話を聞く会議のイラスト。', f"""
<g transform="translate(300 130)">
  <path d="M-170-70h340v130h-340z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"><path d="M-130-40h260M-130-6h210M-130 28h160"/></g>
</g>
{person(120,300,0.85,1,'violet','blue','point','bun','neutral')}
{sit(240,376,0.75,1,'teal','blue','short','neutral','lap')}
{sit(340,376,0.75,1,'coral','gold','bob','neutral','lap')}
{sit(440,376,0.75,1,'gold','violet','short','neutral','lap')}
{sit(540,376,0.75,1,'green','blue','bun','neutral','lap')}
<path d="M60 390h480" class="a"/>
""", ground=True)

add('connection', 'プラグを差してつなぐイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-120-60h140v120h-140z" class="bluep o"/>
  <path d="M20-30h50v20H20zM20 10h50v20H20z" fill="{MUTED}" class="o"/>
</g>
<g transform="translate(420 230)">
  <path d="M-20-60h140v120H-20z" class="tealp o"/>
  <path d="M-70-34h50v20h-50zM-70 14h50v20h-50z" fill="{MUTED}" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="8"><path d="M250 210h100M250 250h100"/></g>
{ck(300,340,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('controversial', '賛成と反対に真っ二つに割れる話題のイラスト。', f"""
<g transform="translate(300 130)">
  <path d="M-90-60h180v100h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-56-30h112M-56 0h80"/></g>
</g>
{person(150,352,1.1,1,'teal','blue','up','short','neutral')}
{person(450,352,1.1,-1,'coral','gold','up','bob','neutral')}
{ck(150,240,0.9)}
{xx(450,240,0.9)}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="14 12"><path d="M300 220v160"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('corporate', 'ロゴを掲げた企業の本社のイラスト。', f"""
{tower(300,320,0.95,'teal',5)}
<g transform="translate(300 120)">
  <circle r="38" class="coral o"/>
  <path d="M-18 14l18-32 18 32z" fill="#fffdf6"/>
</g>
{person(140,356,0.8,1,'violet','blue','walk','short','neutral')}
{person(470,356,0.8,-1,'violet','blue','walk','bob','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('court', '裁判官の壇のある法廷のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-230-160h460v320h-460z" fill="#fffdf6" class="o"/>
  <path d="M-160 40h320v100h-320z" class="goldd o"/>
  <path d="M-170 20h340v20h-340z" class="gold o"/>
</g>
{person(300,270,1,1,'violet','violet','stand','bun','neutral')}
<g transform="translate(300 120)">
  <path d="M-8-40h16v70h-16z" class="ink"/>
  <path d="M-60-40h120v10H-60z" class="ink"/>
  <path d="M-84-14h56q0 24-28 24t-28-24z" class="goldp o"/>
  <path d="M28-14h56q0 24-28 24t-28-24z" class="goldp o"/>
</g>
<path d="M60 390h480" class="a"/>
""", ground=True)

add('crew', 'そろいの制服で働く乗組員のイラスト。', f"""
<path d="M0 320h600v80H0z" class="bluep"/>
<g transform="translate(300 320)">
  <path d="M-200 0h400l-40 50h-320z" class="coral o"/>
  <path d="M-90-70h180v70h-180z" fill="#fffdf6" class="o"/>
</g>
{person(160,320,0.8,1,'blue','blue','stand','cap','smile')}
{person(300,250,0.8,1,'blue','blue','stand','cap','smile')}
{person(440,320,0.8,-1,'blue','blue','stand','cap','smile')}
""", ground=False)

add('customs', '荷物を検査する税関のイラスト。', f"""
<g transform="translate(380 300)">
  <path d="M-160-30h320v20h-320z" class="goldd o"/>
  <path d="M-130-10v46M130-10v46" class="a"/>
  <path d="M-160-70h140v40h-140z" class="paper"/>
</g>
{person(140,352,1.05,1,'teal','blue','carry','short','neutral')}
<g transform="translate(230 320)">
  <path d="M-40-30h80v60h-80z" class="goldd o"/>
</g>
{person(470,250,1,-1,'violet','blue','reach','cap','neutral')}
<g transform="translate(330 240)">
  <circle r="40" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M30 30l30 30" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('democratic', 'みんなの票で決める民主的なイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-120-40h240v130h-240z" class="tealp o"/>
  <path d="M-70-50h140v14h-140z" class="ink"/>
</g>
{person(120,356,0.8,1,'coral','blue','up','short','smile')}
{person(200,356,0.8,1,'gold','violet','up','bob','smile')}
{person(420,356,0.8,-1,'green','blue','up','short','smile')}
{person(500,356,0.8,-1,'violet','gold','up','bun','smile')}
<g transform="translate(300 150)">
  <path d="M-50-40h100v60h-100z" class="paper"/>
  <g fill="none" stroke="{GRN}" stroke-width="7"><path d="M-24-14l12 14 24-28"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 190v50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('dramatic', '一気に大きく動く劇的な変化のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-230 60h460" class="a"/>
  <path d="M-200 40l60-10 50 6" fill="none" stroke="{TONES['teal'][0]}" stroke-width="7"/>
  <path d="M-90 36q60 6 110-140t170-40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9"/>
</g>
{star(500,110,30,'gold')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('duty', '持ち場でつとめを果たすイラスト。', f"""
{person(230,352,1.3,1,'violet','blue','stand','cap','neutral')}
<g transform="translate(170 250)">
  <circle r="26" class="gold o"/>
  <path d="M0-14l6 12 14 2-10 10 2 14-12-7-12 7 2-14-10-10 14-2z" class="goldd"/>
</g>
<g transform="translate(430 250)">
  <path d="M-70-90h140v180h-140z" class="paper"/>
  <g fill="none" stroke="{GRN}" stroke-width="6"><path d="M-44-50l10 12 22-26M-44-10l10 12 22-26M-44 30l10 12 22-26"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M0-50h44M0-10h44M0 30h34"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('economic', 'お金が家と会社をめぐる経済のイラスト。', f"""
<g transform="translate(150 290)">
  <path d="M-70 0v-70h140V0z" fill="#fffdf6" class="o"/>
  <path d="M-84-70L0-124l84 54z" class="coral o"/>
</g>
{tower(450,320,0.6,'teal',4)}
<g class="a" marker-end="url(#ar)"><path d="M240 170h140"/></g>
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="5" marker-end="url(#ar)"><path d="M380 250H240"/></g>
<g class="gold o"><ellipse cx="300" cy="130" rx="26" ry="11"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('economy', '国全体のお金の動きを表すイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-220-150h440v300h-440z" class="paper"/>
  <path d="M-180 100l60-40 50 20 60-70 50 30 70-90" fill="none" stroke="{TONES['teal'][0]}" stroke-width="8"/>
  <path d="M-180-120v220h360" class="a"/>
</g>
<g class="gold o"><ellipse cx="140" cy="360" rx="30" ry="12"/><ellipse cx="300" cy="366" rx="30" ry="12"/><ellipse cx="460" cy="360" rx="30" ry="12"/></g>
""", ground=False)

print(len(W), ' '.join(W))
print(sheet(W))
