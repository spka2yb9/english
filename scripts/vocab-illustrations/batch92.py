"""第92回: rh〜sl の名詞を中心に45語。"""
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

add('rhetoric', '飾り立てた言い回しで語るイラスト。', f"""
{person(150,352,1.2,1,'violet','blue','point','short','neutral')}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M230 250q40-40 80 0t80 0 80-40"/>
  <path d="M230 290q50 40 100 0t100 20"/>
</g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M330 180q-20-26 0-36 20-10 20 14 0-24 20-14 20 10 0 36l-20 20z"/>
</g>
{star(470,180,26,'gold')}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('riot', '群衆が荒れて物が倒れる暴動のイラスト。', f"""
{cloud(140,110,1.3,'blue')}
{person(200,352,1.05,1,'coral','blue','up','cap','sad')}
{person(300,352,1.05,1,'gold','violet','up','short','sad')}
{person(400,352,1.05,-1,'coral','gold','up','cap','sad')}
<g transform="translate(510 340) rotate(28)">
  <path d="M-50-20h100v40h-100z" class="teald o"/>
  <path d="M-50-20v-46h100v46z" class="teal o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M150 180l-16-22M250 170v-24M350 170v-24M450 180l16-22"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('rocket', '炎をふいて飛び立つロケットのイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-40 60V-60q0-70 40-110 40 40 40 110V60z" fill="#fffdf6" class="o"/>
  <circle cx="0" cy="-40" r="22" class="bluep o"/>
  <path d="M-40 20l-50 60h50zM40 20l50 60H40z" class="coral o"/>
  <path d="M-40 60h80v20h-80z" class="corald o"/>
</g>
{flame(300,380,0.9)}
<g fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"><path d="M470 340V120"/></g>
""", ground=False, arrow=True)

add('rod', 'まっすぐ細長い棒のイラスト。', f"""
<g transform="translate(300 220) rotate(-18)">
  <path d="M-240-12h480v24h-480z" class="goldd o"/>
  <circle cx="-240" cy="0" r="16" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M100 340h400"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M100 320v40M500 320v40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('romance', '心を寄せ合うふたりの恋物語のイラスト。', f"""
{person(210,352,1.15,1,'coral','blue','reach','bun','smile')}
{person(390,352,1.15,-1,'teal','gold','reach','short','smile')}
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2.5">
  <path d="M300 170q-34-42 0-60 34-18 34 24 0-42 34-24 34 18 0 60l-34 34z"/>
</g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M150 190q-16-20 0-28 16-8 16 12 0-20 16-12 16 8 0 28l-16 16z"/>
  <path d="M450 200q-14-18 0-25 14-7 14 11 0-18 14-11 14 7 0 25l-14 14z"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('rotation', '軸のまわりを順にめぐる回転のイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="18" stroke-linecap="round">
  <path d="M300 100a120 120 0 1 1-85 35"/>
</g>
<path d="M300 62l56 38-56 38z" fill="{TONES['teal'][2]}" stroke="{INK}" stroke-width="3"/>
<circle cx="300" cy="220" r="20" class="ink"/>
<circle cx="420" cy="220" r="24" class="coralp o"/>
<circle cx="300" cy="340" r="24" class="goldp o"/>
<circle cx="180" cy="220" r="24" class="greenp o"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('rubber', 'よく伸びて戻るゴムのイラスト。', f"""
<g fill="none" stroke="{INK}" stroke-width="16">
  <ellipse cx="300" cy="220" rx="200" ry="70"/>
</g>
{hand(110,220,1)}
{hand(490,220,-1)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M230 340h-90M370 340h90"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('rubbish', 'ごみ袋があふれたくずかごのイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-110 0h220l-20 110h-180z" class="tealp o"/>
  <path d="M-120-16h240v16h-240z" class="teal o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3"><path d="M-70 20v90M0 20v90M70 20v90"/></g>
</g>
<g class="goldd o">
  <path d="M240 250q-20-40 10-56 40-20 70 6 26 24 0 50-50 16-80 0z"/>
  <path d="M270 194l-10-20 30 10z"/>
</g>
<g class="coralp o"><path d="M400 290l40-16 12 34-40 12z"/></g>
<path d="M60 390h480" class="a"/>
""", ground=True)

add('ruling', '裁きとして下される決定のイラスト。', f"""
<g transform="translate(260 210)">
  <path d="M-140-140h280v280h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-100 {-100+i*44}h200"/>' for i in range(4))}</g>
  <g fill="none" stroke="{GRN}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"><path d="M-50 90l24 28 54-64"/></g>
</g>
<g transform="translate(470 300) rotate(-24)">
  <path d="M-60-16h50v32h-50z" class="goldd o"/>
  <path d="M-10-9h110v18H-10z" class="gold o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('rumour', '耳から耳へ伝わってふくらむうわさのイラスト。', f"""
{person(140,352,1,1,'teal','blue','point','short','neutral')}
{person(300,352,1,1,'gold','violet','point','bob','neutral')}
{person(460,352,1,1,'coral','gold','point','short','surprised')}
<g transform="translate(190 230)">
  <path d="M-40-24h80v40h-80zM-18 16l-8 20 26-20z" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(350 210)">
  <path d="M-56-34h112v56h-112zM-30 22l-10 26 32-26z" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(510 180)">
  <path d="M-70-44h140v70h-140zM-36 26l-12 30 38-30z" fill="#fffdf6" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 290h40M390 290h40"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('saint', '光の輪をいただく聖人のイラスト。', f"""
{person(300,352,1.3,1,'violet','violet','give','bun','smile')}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="9"><ellipse cx="300" cy="192" rx="56" ry="16"/></g>
<g class="golds"><path d="M180 200l-24-20M420 200l24-20M300 130v-24"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('sanction', '取引を止めて罰を課す制裁のイラスト。', f"""
<g transform="translate(160 250)">
  <path d="M-80 60q0-100 80-100t80 100z" class="tealp o"/>
  <path d="M-20-20v-70h4l50 18-50 18" class="ink"/>
</g>
<g transform="translate(470 250)">
  <path d="M-80 60q0-100 80-100t80 100z" class="coralp o"/>
  <path d="M-20-20v-70h4l50 18-50 18" class="ink"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M260 200h80"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="14" stroke-linecap="round"><path d="M270 130l60 60M330 130l-60 60"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('saving', 'こつこつ貯金箱にためる節約のイラスト。', f"""
<g transform="translate(300 270)">
  <ellipse rx="130" ry="96" class="coralp o"/>
  <circle cx="96" cy="-30" r="42" class="coralp o"/>
  <ellipse cx="130" cy="-24" rx="20" ry="14" class="coral o"/>
  <circle cx="108" cy="-44" r="5" class="ink"/>
  <path d="M-20-90h50v14h-50z" class="corald o"/>
  <path d="M-80 90v26M-20 94v22M40 94v22M96 88v28" fill="none" stroke="{TONES['coral'][2]}" stroke-width="16" stroke-linecap="round"/>
  <path d="M-110 40q-30 10-20 46" fill="none" stroke="{TONES['coral'][2]}" stroke-width="8"/>
</g>
<g class="gold o"><ellipse cx="300" cy="110" rx="30" ry="13"/></g>
<g class="a" marker-end="url(#ar)"><path d="M300 140v26"/></g>
<path d="M60 390h480" class="a"/>
""", ground=True, arrow=True)

add('scandal', '新聞に書かれて追われる醜聞のイラスト。', f"""
<g transform="translate(190 200)">
  <path d="M-140-130h280v240h-280z" class="paper"/>
  <path d="M-110-100h220v40h-220z" class="ink"/>
  <path d="M-110-40h100v70h-100z" class="corald o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M10-40h100M10-14h100M10 12h80M-110 60h220M-110 86h180"/></g>
</g>
{person(450,352,1.2,-1,'violet','blue','up','short','sad')}
<g fill="{INK}"><rect x="500" y="220" width="56" height="36" rx="6"/></g>
<g class="golds"><path d="M500 200l-16-20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('scenario', '起こりうる筋書きを並べた想定のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-230-120h140v100h-140z" class="paper"/>
  <path d="M-70-120h140v100H-70z" class="paper"/>
  <path d="M90-120h140v100H90z" class="paper"/>
  <path d="M-230 20h140v100h-140z" class="paper"/>
  <path d="M-70 20h140v100H-70z" class="paper"/>
  <path d="M90 20h140v100H90z" class="paper"/>
  <g class="tealp o"><circle cx="-160" cy="-70" r="26"/><path d="M-30-96h80v52h-80z"/><path d="M160-96l30 52h-60z"/></g>
  <g class="goldp o"><circle cx="-160" cy="70" r="26"/><path d="M-30 44h80v52h-80z"/><path d="M160 44l30 52h-60z"/></g>
</g>
""", ground=False)

add('scholar', '本に囲まれて学び深める学者のイラスト。', f"""
{sit(300,352,1.3,1,'violet','violet','bun','neutral','lap')}
{chair(310,356,1.25,'gold',1)}
<g transform="translate(370 300)"><path d="M-50-16h100v34h-100z" class="paper"/></g>
<g transform="translate(120 330)">
  <path d="M-50 30h100v-26h-100z" class="tealp o"/>
  <path d="M-40 4h80v-26h-80z" class="coralp o"/>
  <path d="M-30-22h60v-26h-60z" class="goldp o"/>
</g>
<g transform="translate(480 300)">
  <path d="M-40-20h80v40h-80z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-24-4h48M-24 8h32"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('scholarship', '学ぶ費用を助ける奨学金のイラスト。', f"""
<g transform="translate(250 200)">
  <path d="M-150-130h300v260h-300z" class="paper"/>
  <path d="M-110-100h220v40h-220z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-110-30h220M-110 0h180"/></g>
  <g class="greenp o"><path d="M-40 40h140v60h-140z"/></g>
  <circle cx="30" cy="70" r="18" class="gold o"/>
</g>
<g transform="translate(480 230)">
  <path d="M-70-10L0-40l70 30L0 20z" class="ink"/>
  <path d="M46 0v44" fill="none" stroke="{TONES['gold'][0]}" stroke-width="5"/>
  <circle cx="46" cy="48" r="9" class="gold"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('scope', 'ここからここまでという及ぶ範囲のイラスト。', f"""
<g transform="translate(300 220)">
  <g class="tealp o">{''.join(f'<circle cx="{-220+i*55}" cy="0" r="24"/>' for i in range(9))}</g>
  <g class="teal o">{''.join(f'<circle cx="{-110+i*55}" cy="0" r="24"/>' for i in range(5))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M170 300h260M170 300v-30M430 300v-30"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M300 300h-120M300 300h120"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('screening', '機械で体を調べる検診のイラスト。', f"""
<g transform="translate(360 230)">
  <path d="M-160-140h320v280h-320z" class="bluep o"/>
  <path d="M-120-100h240v200h-240z" fill="#fffdf6" class="o"/>
  <circle cx="0" cy="-40" r="34" fill="#dfe6ea" class="o"/>
  <path d="M-50 90v-50q0-50 50-50t50 50v50z" fill="#dfe6ea" class="o"/>
  <path d="M-90 0h180" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
{person(140,352,1.05,1,'teal','blue','stand','bun','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M200 250h40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('scrutiny', '細部まで念入りに調べる精査のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-160 {-100+i*30}h320"/>' for i in range(7))}</g>
</g>
<g transform="translate(360 230)">
  <circle r="90" fill="none" stroke="{INK}" stroke-width="11"/>
  <circle r="78" fill="#fffdf6" opacity="0.35"/>
  <g fill="none" stroke="{INK}" stroke-width="5">{''.join(f'<path d="M-56 {-46+i*30}h112"/>' for i in range(4))}</g>
  <path d="M64 64l60 60" fill="none" stroke="{INK}" stroke-width="17" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('seeker', '明かりをかざして探し求める人のイラスト。', f"""
{person(210,352,1.25,1,'teal','blue','reach','cap','neutral')}
<g transform="translate(300 230)">
  <path d="M-30-40h60v70h-60z" class="goldp o"/>
  <path d="M-30-40q30-24 60 0z" class="goldd o"/>
  <path d="M0-40v-24" class="a"/>
  <circle cy="-6" r="16" class="gold o"/>
</g>
<path d="M330 240l140-40v120l-140-20z" fill="{TONES['gold'][1]}" opacity="0.6"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><circle cx="470" cy="260" r="34"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('segment', 'いくつかに区切られた中のひと区画のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-240-60h96v120h-96z" class="tealp o"/>
  <path d="M-144-60h96v120h-96z" class="tealp o"/>
  <path d="M-48-60h96v120h-96z" class="coral o"/>
  <path d="M48-60h96v120H48z" class="tealp o"/>
  <path d="M144-60h96v120h-96z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><rect x="244" y="146" width="112" height="148" rx="12"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('selection', 'いくつかの中から選び取るイラスト。', f"""
<g transform="translate(230 200)">
  <circle cx="-110" cy="-60" r="40" class="tealp o"/>
  <circle cx="0" cy="-60" r="40" class="tealp o"/>
  <circle cx="110" cy="-60" r="40" class="coral o"/>
  <circle cx="-110" cy="50" r="40" class="tealp o"/>
  <circle cx="0" cy="50" r="40" class="tealp o"/>
  <circle cx="110" cy="50" r="40" class="tealp o"/>
</g>
{hand(430,140,-1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M390 150h-40"/></g>
<g transform="translate(470 320)">
  <path d="M-70-30h140l-16 70h-108z" class="goldp o"/>
  <circle cx="0" cy="-4" r="26" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('self', '鏡にうつる自分自身のイラスト。', f"""
{person(180,352,1.25,1,'teal','blue','reach','short','smile')}
<g transform="translate(430 220)">
  <path d="M-110-150h220v300h-220z" class="goldd o"/>
  <path d="M-90-130h180v260h-180z" fill="#e9f2f7" class="o"/>
</g>
{person(440,340,1.1,-1,'teal','blue','reach','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M260 230h60"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('seminar', '少人数で学び合うセミナーのイラスト。', f"""
<g transform="translate(300 130)">
  <path d="M-150-70h300v120h-300z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5"><path d="M-110-40h220M-110-10h180M-110 20h140"/></g>
</g>
{person(140,300,0.85,1,'violet','blue','point','bun','neutral')}
{sit(280,356,0.85,1,'teal','blue','short','neutral','lap')}
{sit(400,356,0.85,1,'coral','gold','bob','neutral','lap')}
{sit(520,356,0.85,-1,'green','violet','short','neutral','lap')}
<g transform="translate(400 330)">
  <path d="M-150-20h300v16h-300z" class="goldd o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sensation', '肌に伝わるびりびりした感覚のイラスト。', f"""
{hand(230,240,1)}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M330 200q18 18 0 36M364 180q34 36 0 72M398 160q50 54 0 108"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M180 160l-14-24M240 150v-26M300 160l14-24"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sensitivity', 'そっと触れただけで葉が閉じる敏感さのイラスト。', f"""
<g transform="translate(180 330)">
  <path d="M0 0v-110" class="greens"/>
  <path d="M0-70q-44-6-50-44 42-6 50 44zM0-92q44-6 50-44-42-6-50 44z" class="greenp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M330 200h50"/></g>
<g transform="translate(470 330)">
  <path d="M0 0v-110" class="greens"/>
  <path d="M0-70q-20-24-18-50 22 14 18 50zM0-92q20-24 18-50-22 14-18 50z" class="green o"/>
</g>
{hand(280,200,1)}
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('sentiment', '胸にいだく思いのイラスト。', f"""
{person(190,352,1.25,1,'teal','blue','think','short','smile')}
<g transform="translate(410 190)">
  <path d="M-120-60q-6-44 34-48 16-34 52-22 30-4 36 28 34 4 30 38-4 30-36 30h-82q-32-2-34-26z" class="bluep o"/>
</g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2.5">
  <path d="M410 200q-28-34 0-50 28-16 28 20 0-36 28-20 28 16 0 50l-28 28z"/>
</g>
<g class="o" fill="#e1edfb"><circle cx="280" cy="230" r="15"/><circle cx="258" cy="262" r="10"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('separation', 'ひとつだったものが左右に分かれるイラスト。', f"""
<g transform="translate(160 230)">
  <path d="M-90-90h180v180h-180z" class="tealp o"/>
</g>
<g transform="translate(440 230)">
  <path d="M-90-90h180v180h-180z" class="coralp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12"><path d="M300 100v260"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="6" marker-end="url(#ar)"><path d="M270 340h-60M330 340h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('sequence', '番号どおりに並ぶ順序のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-230-60h120v120h-120z" class="tealp o"/>
  <path d="M-60-60h120v120H-60z" class="tealp o"/>
  <path d="M110-60h120v120H110z" class="tealp o"/>
  <g class="teal">{''.join(f'<rect x="{-200+i*170}" y="-30" width="{14+i*14}" height="14"/>' for i in range(3))}</g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 220h50M350 220h50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('series', 'ひと続きにつながった一連のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-250-70h100v140h-100z" class="paper"/>
  <path d="M-130-70h100v140h-100z" class="paper"/>
  <path d="M-10-70h100v140H-10z" class="paper"/>
  <path d="M110-70h100v140H110z" class="paper"/>
  <g class="tealp o"><circle cx="-200" cy="-20" r="24"/><circle cx="-80" cy="-20" r="24"/><circle cx="40" cy="-20" r="24"/><circle cx="160" cy="-20" r="24"/></g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"><path d="M-150 40h20M-30 40h20M90 40h20"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('settlement', '書面に手を打って争いを収める和解のイラスト。', f"""
{person(140,352,1.15,1,'teal','blue','give','short','smile')}
{person(460,352,1.15,-1,'coral','gold','give','bob','smile')}
<g transform="translate(300 250)">
  <path d="M-70 0h60v20h-60z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M10 0h60v20H10z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-20-16h40v52h-40z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g transform="translate(300 150)">
  <path d="M-70-50h140v80h-140z" class="paper"/>
  <g fill="none" stroke="{GRN}" stroke-width="6"><path d="M-30-10l12 14 24-28"/></g>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('settler', '新しい土地に家を建てて住みつく入植者のイラスト。', f"""
<g transform="translate(430 300)">
  <path d="M-80 0v-70h160V0z" fill="#fffdf6" class="o"/>
  <path d="M-94-70L0-124l94 54z" class="coral o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="6"><path d="M-80-70h160M-40-70V0M40-70V0"/></g>
</g>
{person(180,352,1.2,1,'gold','green','carry','cap','neutral')}
<g transform="translate(250 300)">
  <path d="M-40-30h80v60h-80z" class="goldd o"/>
</g>
{tree(80,340,0.8)}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('shade', '木のかげに入って日をよけるイラスト。', f"""
{sun(500,90,44)}
{tree(300,300,1.7)}
<ellipse cx="270" cy="330" rx="170" ry="46" fill="#c7d3c7" opacity="0.8"/>
{sit(210,340,1,1,'teal','blue','bob','smile','down')}
<path d="M60 356h480" class="a"/>
""", ground=True)

add('shareholder', '会社の株を持つ株主のイラスト。', f"""
{person(170,352,1.25,1,'violet','blue','carry','bun','smile')}
<g transform="translate(270 270)">
  <path d="M-60-46h120v92h-120z" class="paper"/>
  <path d="M-40-26h80v30h-80z" class="tealp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-40 16h80M-40 30h56"/></g>
</g>
{tower(470,320,0.7,'teal',5)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M340 250h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sibling', '背の高さがちがう兄弟のイラスト。', f"""
{person(230,352,1.2,1,'teal','blue','give','short','smile')}
{person(390,354,0.85,-1,'coral','gold','give','bob','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M310 200v160"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('signal', '進めと止まれを知らせる信号のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-60-160h120v320h-120z" class="ink"/>
  <circle cx="0" cy="-100" r="36" class="coral o"/>
  <circle cx="0" cy="0" r="36" class="goldp o"/>
  <circle cx="0" cy="100" r="36" class="greenp o"/>
</g>
<path d="M294 380v20" class="a"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M400 120h60"/></g>
""", ground=False, arrow=True)

add('signature', '書類に自分の名前を書きつける署名のイラスト。', f"""
<g transform="translate(280 230)">
  <path d="M-190-140h380v280h-380z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-150-100h300M-150-70h300M-150-40h240"/></g>
  <path d="M-150 60h300" fill="none" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-linecap="round">
    <path d="M-130 40q30-30 50 10t40-20 40 20 50-30"/>
  </g>
</g>
<g transform="translate(490 300) rotate(30)">
  <path d="M-14-130h28l10 130-24 40-24-40z" class="gold o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('silk', 'なめらかに流れる絹の布のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-230-90q80-40 160 0t160 0v180q-80 40-160 0t-160 0z" class="violetp o"/>
  <g fill="none" stroke="#fffdf6" stroke-width="8" opacity="0.9">
    <path d="M-230-40q80-40 160 0t160 0M-230 20q80-40 160 0t160 0"/>
  </g>
</g>
<g class="goldp o"><ellipse cx="120" cy="360" rx="40" ry="20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sin', '白い心に落ちた黒いしみのイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M0-60q-60-70-104-18-42 50 104 156 146-106 104-156-44-52-104 18z" fill="#fffdf6" class="o"/>
  <path d="M-30-10q30-30 60-4 20 26-10 44-36 10-50-40z" fill="#3a3f4d"/>
</g>
<g fill="#3a3f4d"><circle cx="220" cy="120" r="9"/><circle cx="380" cy="140" r="7"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sketch', '線でざっと描いた下絵のイラスト。', f"""
<g transform="translate(260 210)">
  <path d="M-160-150h320v300h-320z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
    <path d="M-100 80l70-100 50 60 40-40 60 80"/>
    <path d="M-104 84l70-100M-96 76l66-96"/>
    <circle cx="60" cy="-80" r="30"/>
    <path d="M-100 100h220"/>
  </g>
</g>
<g transform="translate(500 300) rotate(26)">
  <path d="M-14-130h28l10 130-24 40-24-40z" class="gold o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('slave', '鎖につながれて働かされる人のイラスト。', f"""
{person(300,352,1.3,1,'gold','gold','carry','short','sad')}
<g fill="none" stroke="{MUTED}" stroke-width="8">
  <circle cx="360" cy="300" r="18"/><circle cx="400" cy="310" r="18"/><circle cx="440" cy="320" r="18"/>
</g>
{box(200,270,110,80,22,'gold')}
<g fill="none" stroke="{MUTED}" stroke-width="10"><path d="M458 328h60"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('slavery', '大勢が鎖につながれて働かされる制度のイラスト。', f"""
{person(150,352,1,1,'gold','gold','carry','short','sad')}
{person(280,352,1,1,'gold','gold','carry','bob','sad')}
{person(410,352,1,1,'gold','gold','carry','short','sad')}
<g fill="none" stroke="{MUTED}" stroke-width="7">
  {''.join(f'<circle cx="{200+i*40}" cy="300" r="15"/>' for i in range(6))}
</g>
{person(540,346,1.05,-1,'violet','violet','point','cap','neutral')}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('slogan', '短いことばを掲げた標語のイラスト。', f"""
<g transform="translate(340 190)">
  <path d="M-200-80h400v160h-400z" class="coral o"/>
  <g fill="#fffdf6"><rect x="-150" y="-40" width="300" height="26" rx="13"/><rect x="-110" y="6" width="220" height="26" rx="13"/></g>
  <path d="M-200-80v-24M200-80v-24" class="a"/>
</g>
<g transform="translate(140 300)">
  <path d="M-40-30h40v60h-40z" class="ink"/>
  <path d="M0-52l70-30v164L0 52z" class="teal o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('slope', 'かたむいた坂のイラスト。', f"""
<path d="M60 360L520 140v220z" class="greenp o"/>
<path d="M60 360L520 140" fill="none" stroke="{INK}" stroke-width="4"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M160 360a110 110 0 0 0 44-52"/></g>
{person(330,266,0.9,1,'teal','blue','walk','short','neutral')}
<path d="M60 380h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
