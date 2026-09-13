"""第102回: 残りの名詞45語。"""
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

add('institute', '研究を行う建物のイラスト。', f"""
{building(230,300,0.95,'violet')}
<g transform="translate(450 280)">
  <path d="M-26-80h52v36l44 80q8 14-8 14h-116q-16 0-8-14l44-80z" fill="#fffdf6" class="o"/>
  <path d="M-46 10l-14 26q-8 14 8 14h96q16 0 8-14l-14-26z" class="teal o"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('integration', '別々だったものが混ざり合って一体になるイラスト。', f"""
<g transform="translate(160 240)">
  <g class="tealp o"><circle cx="-40" cy="-30" r="24"/><circle cx="0" cy="20" r="24"/><circle cx="-50" cy="40" r="24"/></g>
  <g class="coralp o"><circle cx="50" cy="-40" r="24"/><circle cx="60" cy="30" r="24"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 240h60"/></g>
<g transform="translate(460 240)">
  <circle r="100" fill="none" stroke="{TONES['teal'][0]}" stroke-width="5"/>
  <g class="tealp o"><circle cx="-40" cy="-30" r="24"/><circle cx="20" cy="30" r="24"/></g>
  <g class="coralp o"><circle cx="30" cy="-40" r="24"/><circle cx="-40" cy="36" r="24"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('intelligence', '頭がよく働いて答えを出すイラスト。', f"""
<g transform="translate(250 230)">
  <path d="M-30 140v-40q-70-16-70-90 0-90 90-90 92 0 92 86 0 44-36 62v72z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="10" cy="-30" r="46" class="goldp o"/>
  <g class="golds"><path d="M10-96v-20M70-66l18-12M-50-66l-18-12"/></g>
</g>
<g transform="translate(470 250)">
  <path d="M-70-70h140v140h-140z" class="tealp o"/>
  <path d="M-70 0h140M0-70v140" class="a"/>
  <path d="M-70-70h70v70h-70z" class="teal o"/>
</g>
{ck(470,140,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('investment', 'お金を入れて育てる投資のイラスト。', f"""
<g transform="translate(180 300)">
  <path d="M-70-30h140l-16 90h-108z" class="goldp o"/>
  <path d="M0-30v-40" class="greens"/>
  <path d="M0-50q-40-6-46-40 38-6 46 40z" class="greenp o"/>
</g>
<g class="gold o"><ellipse cx="180" cy="150" rx="30" ry="13"/></g>
<g class="a" marker-end="url(#ar)"><path d="M180 180v50"/></g>
<g transform="translate(440 300)">
  <path d="M-70-30h140l-16 90h-108z" class="goldp o"/>
  <path d="M0-30v-120" class="greens"/>
  <path d="M0-80q-56-8-64-56 54-8 64 56zM0-110q56-8 64-56-54-8-64 56z" class="greenp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 320h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('investor', '資金を出して見返りを待つ投資者のイラスト。', f"""
{person(160,352,1.2,1,'violet','blue','give','bun','neutral')}
<g transform="translate(300 250)">
  <path d="M-60-30h120v60h-120z" class="greenp o"/>
  <circle r="16" class="gold o"/>
</g>
<g transform="translate(470 230)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <path d="M-60 70l40-50 30 24 50-80" fill="none" stroke="{TONES['teal'][0]}" stroke-width="7"/>
  <path d="M-70-90v180h150" class="a"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 170h130"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('issue', '話の中で問題になっている点のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-160 {-100+i*50}h320"/>' for i in range(5))}</g>
</g>
<g transform="translate(360 250)">
  <circle r="56" class="coralp o"/>
  <g fill="{TONES['coral'][2]}"><rect x="-10" y="-30" width="20" height="38" rx="10"/><circle cy="24" r="11"/></g>
</g>
""", ground=False)

add('jurisdiction', '裁きの力が及ぶ区域のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-240-110q100-40 240-10t240 0v170q-140 40-240 0t-240 10z" class="greenp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="16 12"><path d="M60 260q120-30 240 0t240-16"/></g>
<g transform="translate(300 130) rotate(-20)">
  <path d="M-60-16h50v32h-50z" class="goldd o"/>
  <path d="M-10-9h110v18H-10z" class="gold o"/>
</g>
""", ground=False)

add('justice', 'かたよりなく釣り合ったてんびんのイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-8-80h16v190h-16z" class="ink"/>
  <path d="M-70 110h140v20H-70z" class="ink"/>
  <path d="M-140-76h280v12h-280z" class="ink"/>
  <path d="M-140-64v40M140-64v40" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-190-24h100q0 40-50 40t-50-40z" class="goldp o"/>
  <path d="M90-24h100q0 40-50 40t-50-40z" class="goldp o"/>
</g>
{ck(490,150,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('justification', 'そうする理由を添えて通すイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-100-110h200v220h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-66 {-60+i*44}h132"/>' for i in range(4))}</g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 230h50"/></g>
<g transform="translate(460 230)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{GRN}" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"><path d="M-44 0l24 28 56-64"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('legislation', '法案が判を受けて法になるイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-56 {-60+i*44}h112"/>' for i in range(4))}</g>
</g>
<g transform="translate(300 150)">
  <path d="M-50-30h100v50h-100z" class="violet o"/>
  <path d="M-20-56h40v26h-40z" class="violetd o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 250h50"/></g>
<g transform="translate(460 240)">
  <path d="M-90-110h180v220h-180z" class="violet o"/>
  <path d="M-70-90h140v180h-140z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-46 {-50+i*44}h92"/>' for i in range(3))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('legislature', '法をつくる議会の建物のイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-230 0h460v20h-460z" class="teald o"/>
  <path d="M-180-140h360v140h-360z" fill="#fffdf6" class="o"/>
  <g class="tealp o">{''.join(f'<rect x="{-160+i*64}" y="-130" width="44" height="130"/>' for i in range(5))}</g>
  <path d="M-210-140h420l-90-70h-240z" class="teal o"/>
  <path d="M-6-250h12v40h-12z" class="gold o"/>
  <circle cx="0" cy="-256" r="12" class="gold o"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('liberal', '門を広く開けて誰でも通すイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-140h40v280h-40zM180-140h40v280h-40z" class="tealp o"/>
  <path d="M-220-160h440v26h-440z" class="teal o"/>
</g>
{person(200,356,0.8,1,'coral','blue','walk','short','smile')}
{person(300,356,0.8,1,'gold','violet','walk','bob','smile')}
{person(400,356,0.8,1,'green','blue','walk','bun','smile')}
{ck(300,150,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('lighting', '何本もの明かりで室内を照らすイラスト。', f"""
<g transform="translate(300 120)">
  <path d="M-160-20h40v20h-40zM-20-20h40v20h-40zM120-20h40v20h-40z" class="ink"/>
  <path d="M-170 0h60l-10 30h-40zM-30 0h60l-10 30h-40zM110 0h60l-10 30h-40z" class="gold o"/>
</g>
<g fill="{TONES['gold'][1]}" opacity="0.7">
  <path d="M130 150l60 200H70zM270 150l60 200H210zM410 150l60 200H350z"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('likelihood', 'たぶん起こると目盛りが示すイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-160 0a160 160 0 0 1 320 0z" fill="#fffdf6" class="o"/>
  <path d="M-160 0h320" class="a"/>
  <path d="M0 0l130-70" fill="none" stroke="{TONES['teal'][0]}" stroke-width="10" stroke-linecap="round"/>
  <circle r="11" class="ink"/>
  <path d="M-160 0A160 160 0 0 1-60-148L0 0z" class="coralp" opacity="0.5"/>
  <path d="M160 0A160 160 0 0 0 60-148L0 0z" class="greenp" opacity="0.6"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('mandate', '票に裏づけられた権限のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-150-140h300v250h-300z" class="paper"/>
  <path d="M-120-110h240v40h-240z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-120-30h240M-120 10h180"/></g>
  <circle cx="90" cy="70" r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
{person(130,376,0.6,1,'coral','blue','up','short','smile')}
{person(210,376,0.6,1,'gold','violet','up','bob','smile')}
{person(390,376,0.6,-1,'green','blue','up','short','smile')}
{person(470,376,0.6,-1,'violet','gold','up','bun','smile')}
""", ground=False)

add('manufacturing', '流れ作業で製品を作る製造のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-240 60h480v30h-480z" fill="#b9c2c9" class="o"/>
  <g fill="{INK}">{''.join(f'<circle cx="{-210+i*70}" cy="105" r="14"/>' for i in range(7))}</g>
</g>
<g class="goldp o"><rect x="110" y="270" width="50" height="40"/></g>
<g class="gold o"><rect x="250" y="262" width="56" height="48" rx="6"/></g>
<g class="gold o"><rect x="400" y="258" width="60" height="52" rx="8"/></g>
<g transform="translate(300 150)">
  <path d="M-120-60h240v80h-240z" class="bluep o"/>
  <g fill="{MUTED}" class="o">{''.join(f'<rect x="{-90+i*70}" y="20" width="30" height="40"/>' for i in range(3))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('measurement', '巻き尺で測って値を記すイラスト。', f"""
<g transform="translate(260 280)">
  <path d="M-160-60h320v60h-320z" class="goldp o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">
    {''.join(f'<path d="M{-140+i*40} -60v{26 if i%2==0 else 16}"/>' for i in range(8))}
  </g>
  <path d="M-160 0h320v40h-320z" class="tealp o"/>
</g>
<g transform="translate(490 200)">
  <path d="M-60-70h120v140h-120z" class="paper"/>
  <g fill="{INK}"><rect x="-34" y="-30" width="68" height="14"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-34 10h68M-34 34h48"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('mining', '坑道から鉱石を運び出す採掘のイラスト。', f"""
<path d="M0 140h600v260H0z" fill="#5e4a3c"/>
<path d="M60 200q120-70 240-40t240 40v160H60z" fill="#7a6252"/>
{person(180,320,1.1,1,'gold','blue','reach','cap','neutral')}
<g transform="translate(250 240) rotate(28)">
  <path d="M-8-10h16v110h-16z" fill="{TONES['gold'][2]}"/>
  <path d="M-60-16q60-24 120 0-60 16-120 0z" fill="#b9c2c9" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(440 330)">
  <path d="M-60-40h120v40h-120z" class="goldd o"/>
  <g fill="{INK}"><circle cx="-34" cy="8" r="16"/><circle cx="34" cy="8" r="16"/></g>
  <g class="tealp o"><circle cx="-20" cy="-50" r="14"/><circle cx="16" cy="-54" r="14"/></g>
</g>
""", ground=False)

add('mobility', '身軽にあちこち移り動けるイラスト。', f"""
{person(300,340,1.15,1,'teal','blue','walk','short','smile')}
<g class="ink"><circle cx="110" cy="330" r="16"/><circle cx="500" cy="330" r="16"/><circle cx="300" cy="150" r="16"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)">
  <path d="M250 300h-110M350 300h110M300 230v-60"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('nonsense', '筋の通らないばかげた話のイラスト。', f"""
<g transform="translate(280 190)">
  <path d="M-160-110h320v200h-320zM-110 90l-16 40 54-40z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round">
    <path d="M-110-60q40 40 70-20t80 30"/>
    <path d="M-110 10q50-30 80 20t70-30"/>
  </g>
</g>
{xx(300,320,1.1)}
{person(510,352,1,-1,'teal','blue','think','short','sad')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('notion', '頭にふと浮かぶ考えのイラスト。', f"""
{person(180,352,1.2,1,'teal','blue','think','short','neutral')}
<g transform="translate(420 190)">
  <path d="M-140-90q-8-46 36-52 18-36 56-24 32-6 38 28 36 6 30 40-6 32-38 32h-90q-34-2-32-24z" class="bluep o"/>
  <circle cx="0" cy="-44" r="34" class="teal o"/>
</g>
<g class="o" fill="#e1edfb"><circle cx="290" cy="250" r="14"/><circle cx="268" cy="276" r="9"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('objection', '手を挙げて異議をとなえるイラスト。', f"""
{person(200,352,1.3,1,'coral','blue','up','short','neutral')}
<g transform="translate(430 200)">
  <path d="M-110-80h220v150h-220z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-76-40h152M-76-10h110M-76 20h152"/></g>
</g>
{xx(430,200,1.6)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('occupation', 'それぞれの仕事の道具を並べたイラスト。', f"""
<g transform="translate(140 230)">
  <path d="M-40-40h80v80h-80z" class="tealp o"/>
  <path d="M-24-16h48v32h-48z" class="ink"/>
</g>
<g transform="translate(300 230)">
  <path d="M-10-50h20v100h-20z" fill="{MUTED}" class="o"/>
  <path d="M-34-62h68v26h-68z" fill="{MUTED}" class="o"/>
</g>
<g transform="translate(450 230)">
  <path d="M-14-30h28v28h28v28h-28v28h-28v-28h-28v-28h28z" class="coral o"/>
</g>
{person(540,352,0.9,-1,'violet','blue','stand','bun','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('odds', 'さいころの出る見込みを表すイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-70-70h140v140h-140z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><circle cx="-34" cy="-34" r="11"/><circle cx="34" cy="34" r="11"/><circle r="11"/><circle cx="34" cy="-34" r="11"/><circle cx="-34" cy="34" r="11"/></g>
</g>
<g transform="translate(440 240)">
  <circle r="110" class="tealp o"/>
  <path d="M0 0v-110A110 110 0 0 1 55-95z" class="coral o"/>
  <g fill="none" stroke="{INK}" stroke-width="2.5">{''.join(f'<path d="M0 0l{int(110*__import__("math").cos(__import__("math").radians(-90+a)))} {int(110*__import__("math").sin(__import__("math").radians(-90+a)))}"/>' for a in range(0,360,60))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('optimism', '雨の窓の向こうに晴れを見る楽観のイラスト。', f"""
<g transform="translate(400 210)">
  <path d="M-140-130h280v260h-280z" class="bluep o"/>
  <path d="M0-130v260M-140 0h280" class="a"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
    {''.join(f'<path d="M{-110+i*36} {-100+(i%3)*26}l-14 40"/>' for i in range(6))}
  </g>
</g>
{sun(520,110,34)}
{person(160,352,1.2,1,'coral','blue','stand','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M230 230h30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('ownership', '鍵と証書で持ち主だと示す所有権のイラスト。', f"""
<g transform="translate(400 300)">
  <path d="M-90 0v-90h180V0z" fill="#fffdf6" class="o"/>
  <path d="M-104-90L0-146l104 56z" class="teal o"/>
  <path d="M-24-56h48V0h-48z" class="teald o"/>
</g>
{person(150,352,1.2,1,'violet','blue','carry','bun','smile')}
<g transform="translate(230 260)">
  <circle r="22" fill="none" stroke="{TONES['gold'][2]}" stroke-width="9"/>
  <path d="M20 0h56v10h-14v14h-12v-14h-12v14h-12v-14h-6z" fill="{TONES['gold'][2]}"/>
</g>
<g transform="translate(230 340)"><path d="M-34-24h68v48h-68z" class="paper"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('parliament', '段になった議席が並ぶ議会のイラスト。', f"""
<g transform="translate(300 340)">
  <path d="M-250 0h500v20h-500z" class="goldd o"/>
  <path d="M-210-40h420v40h-420z" class="goldd o"/>
  <path d="M-160-80h320v40h-320z" class="goldd o"/>
  <path d="M-110-120h220v40h-220z" class="goldd o"/>
</g>
{sit(180,300,0.6,1,'teal','blue','short','neutral','lap')}
{sit(300,260,0.6,1,'coral','gold','bob','neutral','lap')}
{sit(420,220,0.6,-1,'violet','violet','short','neutral','lap')}
<g transform="translate(300 140)">
  <path d="M-70-20h140v16h-140z" class="gold o"/>
  <circle cx="-80" cy="-12" r="12" class="goldd o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('perspective', '奥へすぼまる線で見え方を表す視点のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-240-140h480v280h-480z" fill="#fffdf6" class="o"/>
  <circle cx="0" cy="0" r="10" class="coral"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    <path d="M0 0L-240-140M0 0L240-140M0 0L-240 140M0 0L240 140M0 0h-240M0 0h240M0 0v-140M0 0v140"/>
  </g>
  <path d="M-140-70h90v60h-90z" class="tealp o"/>
  <path d="M60 30h120v80H60z" class="tealp o"/>
</g>
""", ground=False)

add('poll', '意見をたずねて結果を集めるイラスト。', f"""
{person(140,352,1,1,'teal','blue','stand','short','neutral')}
<g transform="translate(210 240)">
  <path d="M-50-34h100v56h-100zM-24 22l-10 24 30-24z" fill="#fffdf6" class="o"/>
  <path d="M-14-16q0-14 14-14t14 12q0 10-14 14v6" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round"/>
</g>
<g transform="translate(440 250)">
  <path d="M-110-110h220v220h-220z" class="paper"/>
  <g class="teal o">{''.join(f'<rect x="{-80+i*50}" y="{70-(30+i*24)}" width="34" height="{30+i*24}"/>' for i in range(3))}</g>
  <path d="M-90 70h180" class="a"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('portfolio', '作品をまとめたファイルのイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-180-40h360v150h-360z" class="goldd o"/>
  <path d="M-180-40l-10-40h380l-10 40z" class="goldp o"/>
</g>
<g transform="translate(200 170) rotate(-10)">
  <path d="M-70-70h140v140h-140z" class="paper"/>
  <path d="M-50 40l40-50 30 30 26-26v46z" class="greenp o"/>
</g>
<g transform="translate(370 160) rotate(8)">
  <path d="M-70-70h140v140h-140z" class="paper"/>
  <g class="teal">{''.join(f'<rect x="{-40+i*30}" y="{40-(20+i*20)}" width="20" height="{20+i*20}"/>' for i in range(3))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('preference', '好きなほうを選び取るイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-80-80h160v160h-160z" class="teal o"/>
</g>
<g transform="translate(450 250)">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
</g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2.5">
  <path d="M180 130q-26-34 0-48 26-14 26 18 0-32 26-18 26 14 0 48l-26 26z"/>
</g>
{hand(300,340,1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M260 320h-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('presidency', '在任のあいだ席につく大統領職のイラスト。', f"""
{chair(300,330,1.4,'gold',1)}
<g transform="translate(300 170)">
  <circle r="46" class="gold o"/>
  <path d="M0-26l12 24 26 4-19 18 5 26-24-14-24 14 5-26-19-18 26-4z" class="goldp"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M100 370h400"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M100 350v40M500 350v40"/></g>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('principle', '石板に刻まれた変わらぬ原則のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-140-150q140-60 280 0v290h-280z" fill="#dfe6ea" class="o"/>
  <g fill="{MUTED}"><rect x="-90" y="-80" width="180" height="18"/><rect x="-90" y="-30" width="180" height="18"/><rect x="-90" y="20" width="140" height="18"/></g>
</g>
{ck(500,180,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('privatization', '公のものが会社の手に移る民営化のイラスト。', f"""
{building(160,300,0.75,'violet')}
<g class="a" marker-end="url(#ar)"><path d="M290 220h60"/></g>
{tower(470,320,0.7,'teal',5)}
<g transform="translate(370 320)">
  <circle r="22" fill="none" stroke="{TONES['gold'][2]}" stroke-width="8"/>
  <path d="M20 0h50v10h-12v12h-10v-12h-10v12h-10v-12h-8z" fill="{TONES['gold'][2]}"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('privilege', '一部の人だけが通れる特権のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-200 0h400v60h-400z" class="coral o"/>
  <path d="M-160-20h60v20h-60zM140-20h60v20h-60z" fill="{TONES['gold'][2]}"/>
</g>
{person(230,300,1.1,1,'violet','violet','walk','bun','smile')}
{ck(230,170,0.8)}
{person(510,352,1,-1,'teal','blue','stand','short','sad')}
{xx(510,220,0.8)}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="12 10"><path d="M420 180v200"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('probability', '当たる見込みを割合で表すイラスト。', f"""
<g transform="translate(200 240)">
  <circle r="110" class="tealp o"/>
  <path d="M0 0v-110A110 110 0 0 1 95 55z" class="coral o"/>
  <g fill="none" stroke="{INK}" stroke-width="2.5"><path d="M0 0v-110M0 0l95 55M0 0L-95 55"/></g>
</g>
<g transform="translate(460 260)">
  <path d="M-60-60h120v120h-120z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><circle cx="-28" cy="-28" r="10"/><circle cx="28" cy="28" r="10"/><circle r="10"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('proceeds', '売って得たお金が入るイラスト。', f"""
<g transform="translate(180 300)">
  <path d="M-90-30h180v20h-180z" class="teald o"/>
  <path d="M-100-50h200v20h-200z" class="teal o"/>
  <g class="goldp o"><rect x="-70" y="-80" width="46" height="30"/><rect x="-10" y="-80" width="46" height="30"/></g>
</g>
<g transform="translate(450 290)">
  <path d="M-90-40h180v100h-180z" class="goldd o"/>
  <path d="M-100-60h200v20h-200z" class="gold o"/>
  <path d="M-30-80h60v20h-60z" class="a" fill="none"/>
</g>
<g class="gold o"><ellipse cx="320" cy="200" rx="26" ry="11"/></g>
<g class="a" marker-end="url(#ar)"><path d="M260 180h140"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('processor', '情報を処理する半導体のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-110-110h220v220h-220z" class="ink"/>
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
  <g fill="{INK}">{''.join(f'<rect x="{-96+i*46}" y="-140" width="16" height="30"/><rect x="{-96+i*46}" y="110" width="16" height="30"/>' for i in range(5))}</g>
  <g fill="{INK}">{''.join(f'<rect x="-140" y="{-96+i*46}" width="30" height="16"/><rect x="110" y="{-96+i*46}" width="30" height="16"/>' for i in range(5))}</g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M80 230h60M460 230h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('productivity', '同じ時間でより多く作れる生産性のイラスト。', f"""
<g transform="translate(180 210)">
  <circle r="60" fill="#fffdf6" class="o"/>
  <path d="M0 0v-38M0 0l20 12" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <circle r="6" class="ink"/>
</g>
<g transform="translate(180 330)">
  <g class="gold o"><rect x="-40" y="-30" width="34" height="34"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 260h60"/></g>
<g transform="translate(460 210)">
  <circle r="60" fill="#fffdf6" class="o"/>
  <path d="M0 0v-38M0 0l20 12" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <circle r="6" class="ink"/>
</g>
<g class="gold o">{''.join(f'<rect x="{380+ (i%3)*48}" y="{290+(i//3)*40}" width="34" height="34"/>' for i in range(6))}</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('proportion', '全体に対する釣り合った割合のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-240-60h130v120h-130z" class="teal o"/>
  <path d="M-110-60h80v120h-80z" class="coral o"/>
  <path d="M-30-60h60v120h-60z" class="gold o"/>
  <path d="M30-60h210v120H30z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M60 340h480M60 340v-24M540 340v-24"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('prospect', '望遠鏡で先の見込みを眺めるイラスト。', f"""
<path d="M0 400V320l120-70 100 50v100z" class="greenp o"/>
{person(140,320,1.05,1,'teal','blue','hold','short','neutral')}
<g transform="translate(190 220)">
  <path d="M-30-12h90v24h-90z" fill="{MUTED}" class="o"/>
  <path d="M60-20h30v40H60z" class="ink"/>
</g>
{sun(480,140,40)}
<g transform="translate(470 290)">
  <path d="M-60 40v-60h30v60zM-14 40v-100h30v100zM32 40v-46h30v46z" class="tealp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><path d="M270 220h140"/></g>
<path d="M240 330h360" class="a"/>
""", ground=False)

add('protest', '看板をかかげて抗議する人々のイラスト。', f"""
{person(140,352,1.05,1,'coral','blue','up','short','neutral')}
{person(250,352,1.05,1,'gold','violet','up','bob','neutral')}
{person(360,352,1.05,1,'teal','gold','up','cap','neutral')}
{person(470,352,1.05,1,'violet','blue','up','short','neutral')}
<g class="paper">
  <rect x="96" y="150" width="90" height="60"/><rect x="206" y="130" width="90" height="60"/>
  <rect x="316" y="150" width="90" height="60"/><rect x="426" y="130" width="90" height="60"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M141 210v40M251 190v60M361 210v40M471 190v60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('protester', 'ひとりで看板を持って訴える人のイラスト。', f"""
{person(300,352,1.35,1,'coral','blue','up','short','neutral')}
<g transform="translate(300 160)">
  <path d="M-90-60h180v100h-180z" class="paper"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M-56-30h112M-56 0h80"/></g>
  <path d="M0 40v60" fill="none" stroke="{MUTED}" stroke-width="6"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('validity', '期限内で有効だと判が示すイラスト。', f"""
<g transform="translate(280 210)">
  <path d="M-170-150h340v300h-340z" class="paper"/>
  <path d="M-140-110h280v40h-280z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-140-30h280M-140 10h200"/></g>
  <g fill="none" stroke="{GRN}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"><path d="M-100 90l24 28 56-64"/></g>
</g>
<g transform="translate(480 320)">
  <circle r="50" fill="#fffdf6" class="o"/>
  <path d="M0 0v-32M0 0l22 14" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <circle r="6" class="ink"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('variation', '同じものの少しちがう型が並ぶイラスト。', f"""
<g transform="translate(300 240)">
  <circle cx="-200" cy="0" r="50" class="tealp o"/>
  <circle cx="-70" cy="0" r="50" class="teal o"/>
  <circle cx="60" cy="0" r="50" class="coralp o"/>
  <circle cx="190" cy="0" r="50" class="goldp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M120 350q40-20 80 0t80 0 80 0 80 0"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
