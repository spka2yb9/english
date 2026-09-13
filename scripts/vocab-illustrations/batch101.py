"""第101回: 残りの名詞45語。"""
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

add('publishing', '刷った本を世に出す出版業のイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-100-100h200v160h-200z" class="bluep o"/>
  <path d="M-60-70h120v90h-120z" class="ink"/>
  <path d="M100-20h34v40h-34z" class="blued o"/>
</g>
<g transform="translate(420 280)">
  <path d="M-100 60h200v-26h-200z" class="tealp o"/>
  <path d="M-90 34h180v-26h-180z" class="coralp o"/>
  <path d="M-80 8h160v-26h-160z" class="goldp o"/>
  <path d="M-70-18h140v-26h-140z" class="violetp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 240h40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('qualification', '条件を満たしたしるしの資格のイラスト。', f"""
<g transform="translate(280 210)">
  <path d="M-170-150h340v300h-340z" class="paper"/>
  <path d="M-140-110h280v40h-280z" class="teal o"/>
  <g fill="none" stroke="{GRN}" stroke-width="7"><path d="M-130-30l10 12 20-24M-130 10l10 12 20-24M-130 50l10 12 20-24"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-80-28h200M-80 12h200M-80 52h160"/></g>
  <circle cx="110" cy="110" r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
{ck(500,180,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('ratio', 'ふたつの量の割り合いを示すイラスト。', f"""
<g transform="translate(300 250)">
  <g class="teal o">{''.join(f'<rect x="{-220+i*66}" y="-50" width="52" height="100"/>' for i in range(3))}</g>
  <g class="coralp o"><rect x="60" y="-50" width="52" height="100"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M60 340h270M60 340v-24M330 340v-24M390 340h120M390 340v-24M510 340v-24"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('reasoning', '前提から順に考えを運ぶ論法のイラスト。', f"""
{person(140,352,1.15,1,'teal','blue','think','short','neutral')}
<g transform="translate(400 190)">
  <path d="M-170-110q-8-54 42-60 20-42 64-28 36-6 44 34 42 6 36 46-6 38-44 38h-106q-40-2-36-30z" class="bluep o"/>
  <g class="teal o"><rect x="-120" y="-70" width="46" height="38"/><rect x="-40" y="-70" width="46" height="38"/></g>
  <g class="coral o"><rect x="46" y="-70" width="46" height="38"/></g>
  <g fill="none" stroke="{TONES['blue'][2]}" stroke-width="4" marker-end="url(#ar)"><path d="M-66-50h18M14-50h24"/></g>
</g>
<g class="o" fill="#e1edfb"><circle cx="240" cy="270" r="14"/><circle cx="218" cy="296" r="9"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('recovery', '落ちこんだあと元に戻る回復のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-210-140h420v280h-420z" class="paper"/>
  <path d="M-170 100v-220h340" class="a"/>
  <path d="M-160-40l60 80 50 20" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
  <path d="M-50 60q60 10 100-50t100-60" fill="none" stroke="{TONES['teal'][0]}" stroke-width="8"/>
</g>
{ck(500,120,0.9)}
""", ground=False)

add('relevance', '話の輪の中にあって関わりがあるイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="14 12"><circle cx="300" cy="220" r="160"/></g>
<g class="tealp o"><circle cx="230" cy="170" r="34"/><circle cx="350" cy="240" r="34"/></g>
<g class="coral o"><circle cx="250" cy="290" r="34"/></g>
{ck(470,340,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('remedy', '手当てをして不具合を直す治療法のイラスト。', f"""
<g transform="translate(180 240)">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
  <g fill="none" stroke="{INK}" stroke-width="6"><path d="M-80-20l50 20-30 40 50 40"/></g>
</g>
<g transform="translate(300 160)">
  <path d="M-40-30h80v60h-80z" class="coral o"/>
  <path d="M-14-46h28v16h-28z" class="corald o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 240h60"/></g>
<g transform="translate(460 240)">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
</g>
{ck(460,150,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('requirement', '入る前に満たすべき条件のイラスト。', f"""
<g transform="translate(200 220)">
  <path d="M-130-150h260v300h-260z" class="paper"/>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="3">{''.join(f'<rect x="-100" y="{-110+i*60}" width="30" height="30"/>' for i in range(4))}</g>
  <g fill="none" stroke="{GRN}" stroke-width="6">{''.join(f'<path d="M-94 {-98+i*60}l8 10 18-22"/>' for i in range(4))}</g>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-50 {-96+i*60}h150"/>' for i in range(4))}</g>
</g>
<g transform="translate(470 250)">
  <path d="M-20-160h40v300h-40z" class="ink"/>
  <path d="M-140-80h120v30h-120z" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('resource', '使うもとになる資源のイラスト。', f"""
<g transform="translate(180 290)">
  <path d="M-110 60q0-70 50-100 60-36 120-6 60 30 40 106z" fill="#8b98a6" class="o"/>
  <path d="M-40-10h60l-20 60h-30z" class="tealp o"/>
</g>
<g transform="translate(440 280)">
  <path d="M-90 70h180v-30h-180z" class="tealp o"/>
  <path d="M-80 40h160v-30h-160z" class="coralp o"/>
  <path d="M-70 10h140v-30h-140z" class="goldp o"/>
</g>
{drop(300,180,1.6,'blue')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('revenue', '会社に入ってくる収益のイラスト。', f"""
{tower(190,320,0.7,'teal',5)}
<g class="gold o"><ellipse cx="400" cy="180" rx="30" ry="13"/><ellipse cx="440" cy="230" rx="30" ry="13"/><ellipse cx="410" cy="280" rx="30" ry="13"/></g>
<g class="a" marker-end="url(#ar)"><path d="M480 150L290 170M500 230H290M480 320L300 290"/></g>
<g transform="translate(520 100)">
  <path d="M-40 40l30-30 20 16 30-40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('say', '手を挙げて発言の場をもらうイラスト。', f"""
{person(240,352,1.3,1,'teal','blue','up','short','neutral')}
<g transform="translate(430 250)">
  <path d="M-16-30h32v60h-32z" class="ink"/>
  <circle cy="-40" r="24" fill="{MUTED}" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M380 230h-60"/></g>
{ck(140,200,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('scheme', '段取りを描いた計画図のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-200-150h400v300h-400z" fill="#e9f2f7" class="o"/>
  <g class="tealp o"><rect x="-160" y="-110" width="100" height="60"/><rect x="-20" y="-110" width="100" height="60"/><rect x="-160" y="10" width="100" height="60"/><rect x="-20" y="10" width="100" height="60"/></g>
  <g fill="none" stroke="{INK}" stroke-width="3" marker-end="url(#ar)"><path d="M-56-80h30M-16-46v50M-56 40h30"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 8"><path d="M100-110v180M-200 90h400"/></g>
</g>
""", ground=False, arrow=True)

add('sector', '全体をいくつかに割ったうちの一部門のイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="150" class="tealp o"/>
  <path d="M0 0v-150A150 150 0 0 1 130 75z" class="coral o"/>
  <g fill="none" stroke="{INK}" stroke-width="2.5"><path d="M0 0v-150M0 0l130 75M0 0l-130 75"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M540 120l-70 40"/></g>
""", ground=False, arrow=True)

add('senator', '議席につく上院議員のイラスト。', f"""
{sit(300,352,1.3,1,'violet','violet','short','neutral','lap')}
{chair(310,356,1.25,'gold',1)}
<g transform="translate(240 250)">
  <circle r="26" class="gold o"/>
  <path d="M0-14l6 12 14 2-10 10 2 14-12-7-12 7 2-14-10-10 14-2z" class="goldd"/>
</g>
<g transform="translate(470 200)">
  <path d="M-6 140V-90" class="a"/>
  <path d="M-6-90h96v60H-6z" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sense', '目・耳・鼻・手で受け取る感覚のイラスト。', f"""
<g transform="translate(150 180)">
  <ellipse rx="60" ry="34" fill="#fffdf6" class="o"/>
  <circle r="22" class="blue o"/><circle r="9" class="ink"/>
</g>
<g transform="translate(320 180)">
  <path d="M-24 46v-20q-30-12-30-44 0-44 44-44t44 40q0 22-20 30-10 4-10 14v24z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g transform="translate(450 180)">
  <path d="M-20 40q-26-20-26-50 0-40 26-50 10 20 10 44 0 30-10 56z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
{hand(300,320,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('session', '予定表の中のひとこまの時間のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-210-150h420v300h-420z" class="paper"/>
  <path d="M-210-150h420v50h-420z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M-210 {-60+i*50}h420"/>' for i in range(4))}
    {''.join(f'<path d="M{-140+c*70} -100v250"/>' for c in range(5))}
  </g>
  <path d="M-70-60h70v100h-70z" class="coralp o"/>
</g>
""", ground=False)

add('significance', '重みのある大切さを測るイラスト。', f"""
<g transform="translate(240 240)">
  <path d="M-8-60h16v170h-16z" class="ink"/>
  <path d="M-60 110h120v20H-60z" class="ink"/>
  <path d="M-120-56h240v12h-240z" class="ink"/>
  <path d="M-120-44v50M120-44v20" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-170 6h100q0 36-50 36t-50-36z" class="coralp o"/>
  <path d="M70-24h100q0 36-50 36t-50-36z" class="tealp o"/>
  <path d="M-140-40h60v40h-60z" class="coral o"/>
</g>
<g fill="{TONES['coral'][0]}"><rect x="490" y="150" width="24" height="80" rx="12"/><circle cx="502" cy="258" r="14"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sovereignty', '自らの旗のもとで国を治める主権のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-240-120q100-40 240-10t240 0v230q-140 40-240 0t-240 10z" class="greenp o"/>
</g>
<g transform="translate(300 130)">
  <path d="M-50 10l-10-50 30 20 30-40 30 40 30-20-10 50z" class="gold o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="16 12"><path d="M60 250q120-30 240 0t240-16"/></g>
{xx(520,90,0.7,MUTED)}
""", ground=False)

add('spirit', '胸に燃える気力のイラスト。', f"""
{person(300,352,1.35,1,'coral','blue','up','short','neutral')}
{flame(300,280,0.6)}
<g class="golds"><path d="M300 130v-24M200 170l-20-20M400 170l20-20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sponsorship', '資金を出して催しを支える後援のイラスト。', f"""
{tower(150,320,0.6,'teal',4)}
<g transform="translate(300 250)">
  <path d="M-60-30h120v60h-120z" class="greenp o"/>
  <circle r="16" class="gold o"/>
</g>
{person(470,352,1.2,-1,'coral','blue','up','short','smile')}
<g class="a" marker-end="url(#ar)"><path d="M230 170h150"/></g>
<g transform="translate(470 200)">
  <path d="M-40-20h80v40h-80z" class="tealp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('stability', '底が広くてぐらつかない安定のイラスト。', f"""
<g transform="translate(170 300)">
  <path d="M-110 60L-40-140h80l70 200z" class="teal o"/>
</g>
{ck(170,140,0.9)}
<g transform="translate(450 300) rotate(14)">
  <path d="M-30 60L-16-140h32l30 200z" class="coralp o"/>
</g>
{xx(450,130,0.9)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('stake', '地面に打ちこむ杭のイラスト。', f"""
<g transform="translate(280 260)">
  <path d="M-24-140h48v170l-24 40-24-40z" class="goldd o"/>
  <path d="M-24-140h48v20h-48z" class="gold o"/>
</g>
<g transform="translate(400 140) rotate(30)">
  <path d="M-10 0h20v120h-20z" fill="{TONES['gold'][2]}"/>
  <path d="M-36-30h72v34h-72z" fill="{MUTED}" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M180 180v60"/></g>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('statistic', '図から取り出したひとつの数値のイラスト。', f"""
<g transform="translate(240 220)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <g class="tealp o">{''.join(f'<rect x="{-140+i*56}" y="{80-(30+i*24)}" width="40" height="{30+i*24}"/>' for i in range(5))}</g>
  <path d="M-150 80h300" class="a"/>
  <rect x="-28" y="2" width="40" height="78" class="coral o"/>
</g>
<g transform="translate(470 230)">
  <circle r="60" fill="none" stroke="{INK}" stroke-width="8"/>
  <circle r="50" fill="#fffdf6" opacity="0.4"/>
  <rect x="-14" y="-30" width="28" height="60" class="coral o"/>
  <path d="M44 44l50 50" fill="none" stroke="{INK}" stroke-width="13" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('status', '段階で表される地位のイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-230 0h120v-40h-120zM-110-40h120v-80h-120zM10-120h120v-120H10z" class="tealp o"/>
  <path d="M10-240h120v-60H10z" class="coral o"/>
</g>
{star(70,150,26,'gold')}
{person(70,352,0.8,1,'teal','blue','stand','short','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M540 340V80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('stimulus', 'つつかれて跳ね返る刺激のイラスト。', f"""
{hand(140,240,1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M210 240h60"/></g>
<g transform="translate(360 250)">
  <path d="M-50 90V60q0-20 100-20V10q0-20-100-20v-30" fill="none" stroke="{TONES['teal'][0]}" stroke-width="12" stroke-linejoin="round"/>
  <circle cx="-50" cy="-50" r="26" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M470 160l24-20M490 210h30M470 260l24 20"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('strategy', '盤の上で打つ手を組み立てる戦略のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" fill="#fffdf6" class="o"/>
  <g fill="{MUTED}" opacity="0.25">{''.join(f'<rect x="{-200+c*100}" y="{-140+r*93}" width="100" height="93"/>' for r in range(3) for c in range(4) if (r+c)%2==0)}</g>
  <circle cx="-150" cy="-94" r="30" class="teal o"/>
  <circle cx="-50" cy="0" r="30" class="teal o"/>
  <path d="M120 62h60v40h-60z" class="coral o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M-120-70l50 50M-20 20l120 50"/></g>
</g>
""", ground=False, arrow=True)

add('summit', '旗を立てて頂で会談するイラスト。', f"""
<path d="M0 380l200-240 110 130 80-90 210 200z" class="greenp o"/>
{person(160,150,0.6,1,'teal','blue','stand','short','neutral')}
{person(240,150,0.6,-1,'coral','gold','stand','bob','neutral')}
<g transform="translate(200 130)">
  <path d="M-40-6h80v12h-80z" class="goldd o"/>
</g>
<g transform="translate(120 80)"><path d="M-4 60V0h60l-12 18 12 18H-4z" class="coral o"/></g>
<g transform="translate(280 80)"><path d="M4 60V0h-60l12 18-12 18h60z" class="teal o"/></g>
<path d="M0 380h600" class="a"/>
""", ground=False)

add('surrounding', 'まわりをぐるりと取り囲むイラスト。', f"""
<g transform="translate(300 230)">
  <circle r="56" class="coral o"/>
  <g class="tealp o">{''.join(f'<circle cx="{int(150*__import__("math").cos(__import__("math").radians(a)))}" cy="{int(150*__import__("math").sin(__import__("math").radians(a)))}" r="34"/>' for a in range(0,360,45))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('synthesis', '二つを混ぜ合わせて新しいものを作る合成のイラスト。', f"""
<g transform="translate(150 180)">
  <path d="M-40-70h80l-10 100h-60z" fill="#fffdf6" class="o"/>
  <path d="M-34-20h68l-6 50h-56z" class="tealp o"/>
</g>
<g transform="translate(300 180)">
  <path d="M-40-70h80l-10 100h-60z" fill="#fffdf6" class="o"/>
  <path d="M-34-20h68l-6 50h-56z" class="coralp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"><path d="M160 230l60 60M310 230l60 60"/></g>
<g transform="translate(430 320)">
  <path d="M-30-100h60v40l50 90q8 16-10 16h-130q-18 0-10-16l50-90z" fill="#fffdf6" class="o"/>
  <path d="M-50 10l-16 30q-8 16 10 16h104q18 0 10-16l-16-30z" class="violet o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('taxpayer', '税を納める人のイラスト。', f"""
{person(160,352,1.2,1,'teal','blue','give','short','neutral')}
<g transform="translate(300 250)">
  <path d="M-60-30h120v60h-120z" class="greenp o"/>
  <circle r="16" class="gold o"/>
</g>
{building(470,320,0.75,'violet')}
<g class="a" marker-end="url(#ar)"><path d="M240 170h140"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('tendency', '点の散らばりが一方へかたよる傾向のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g class="teal">{''.join(f'<circle cx="{-170+i*38}" cy="{90-i*17+((i*29)%40)-20}" r="9"/>' for i in range(10))}</g>
  <path d="M-180 90q160-40 350-140" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-dasharray="14 12"/>
  <path d="M-180-120v220h360" class="a"/>
</g>
""", ground=False)

add('tenure', '長く同じ職にとどまる在職期間のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-220-30h440v60h-440z" class="teal o"/>
  <g fill="none" stroke="#fffdf6" stroke-width="4">{''.join(f'<path d="M{-160+i*80} -30v60"/>' for i in range(5))}</g>
</g>
{chair(150,190,0.6,'gold',1)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M80 340h440"/></g>
<circle cx="500" cy="200" r="34" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('terms', '契約に並べられた条件のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-190-150h380v300h-380z" class="paper"/>
  <path d="M-150-110h180v24h-180z" class="ink"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-110 {-50+i*44}h260"/>' for i in range(5))}</g>
  <g class="tealp o">{''.join(f'<rect x="-150" y="{-62+i*44}" width="24" height="24"/>' for i in range(5))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M520 170v140M520 170h-20M520 310h-20"/></g>
""", ground=False)

add('thesis', '研究をまとめた分厚い論文のイラスト。', f"""
<g transform="translate(250 220)">
  <path d="M-140-150h280v300h-280z" class="violet o"/>
  <path d="M-120-130h240v260h-240z" fill="#fffdf6" class="o"/>
  <path d="M-80-100h160v40h-160z" class="violetp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-80-20h160M-80 14h160M-80 48h120"/></g>
  <path d="M140-150h20v300h-20z" class="violetd o"/>
</g>
{person(470,352,1.1,-1,'violet','violet','point','bun','neutral')}
<g transform="translate(470 330)"><path d="M-40-30h80l14 50h-108z" class="goldd o"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tissue', '箱から出すティッシュと細かい組織のイラスト。', f"""
<g transform="translate(180 290)">
  <path d="M-90-40h180v100h-180z" class="bluep o"/>
  <path d="M-40-40h80v-60q-40 30-80 0z" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(430 230)">
  <circle r="100" fill="none" stroke="{INK}" stroke-width="8"/>
  <circle r="90" fill="#fffdf6"/>
  <g class="coralp o">{''.join(f'<circle cx="{-50+(i%3)*50}" cy="{-50+(i//3)*50}" r="24"/>' for i in range(9))}</g>
  <circle r="90" fill="none" stroke="{INK}" stroke-width="8"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tolerance', '形が違っても受け入れる寛容さのイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="14 12"><rect x="70" y="120" width="460" height="220" rx="30"/></g>
<circle cx="160" cy="230" r="40" class="tealp o"/>
<path d="M240 190h80v80h-80z" class="coralp o"/>
<path d="M400 270l40-80 40 80z" class="goldp o"/>
<circle cx="520" cy="230" r="34" class="violetp o"/>
{ck(300,370,0.9)}
""", ground=False)

add('tragedy', '悲しみの面が掛かる舞台のイラスト。', f"""
<g transform="translate(300 170)">
  <path d="M-250-110h500v40h-500z" class="violetd o"/>
  <path d="M-250-70q30 150 0 260h90q-24-120 0-260z" class="violet o"/>
  <path d="M250-70q-30 150 0 260h-90q24-120 0-260z" class="violet o"/>
</g>
<g transform="translate(300 220)">
  <path d="M-70-60q70-40 140 0 0 120-70 120T-70-60z" class="goldp o"/>
  <g fill="{INK}"><path d="M-40-30q20-16 36 0-18 10-36 0zM14-30q20-16 36 0-18 10-36 0z"/></g>
  <path d="M-20 46q20-20 40 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="5"/>
</g>
{drop(250,190,1,'blue')}
{drop(350,190,1,'blue')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('trait', 'その人に備わった目立つ特性のイラスト。', f"""
{person(250,352,1.35,1,'teal','blue','stand','short','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="250" cy="210" r="60"/></g>
<g transform="translate(460 210)">
  <path d="M-50-50h100v100h-100z" class="coralp o"/>
  <circle r="26" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M320 210h80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('transformation', 'まるごと別の姿に変わる変容のイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 240h60"/></g>
<g transform="translate(460 240)">
  <circle r="90" class="coral o"/>
</g>
<g class="golds"><path d="M290 150l-20-20M370 150l20-20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('transparency', '中身がすっかり見える透明さのイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-100-100h200v200h-200z" fill="#e9f2f7" class="o" opacity="0.8"/>
  <circle cx="-20" cy="20" r="40" class="coralp o"/>
  <path d="M20-40h60v60H20z" class="tealp o"/>
</g>
{ck(200,120,0.9)}
<g transform="translate(450 250)">
  <path d="M-100-100h200v200h-200z" fill="{MUTED}" class="o"/>
</g>
{xx(450,120,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tribunal', '数人がそろって裁く審判所のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-230-40h460v90h-460z" class="goldd o"/>
  <path d="M-240-60h480v20h-480z" class="gold o"/>
</g>
{sit(180,270,0.8,1,'violet','violet','short','neutral','lap')}
{sit(300,270,0.85,1,'violet','violet','bun','neutral','lap')}
{sit(420,270,0.8,1,'violet','violet','cap','neutral','lap')}
<g transform="translate(300 120)">
  <path d="M-8-40h16v70h-16z" class="ink"/>
  <path d="M-60-40h120v10H-60z" class="ink"/>
  <path d="M-84-14h56q0 24-28 24t-28-24z" class="goldp o"/>
  <path d="M28-14h56q0 24-28 24t-28-24z" class="goldp o"/>
</g>
<path d="M60 390h480" class="a"/>
""", ground=True)

add('tuition', '授業のために払う月謝のイラスト。', f"""
{person(150,352,1.15,1,'teal','blue','give','short','neutral')}
<g transform="translate(280 250)">
  <path d="M-60-30h120v60h-120z" class="greenp o"/>
  <circle r="16" class="gold o"/>
</g>
{building(470,320,0.75,'teal')}
<g class="a" marker-end="url(#ar)"><path d="M230 170h140"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('turnout', '会場に集まった人数を数えるイラスト。', f"""
{person(110,356,0.75,1,'teal','blue','stand','short','smile')}
{person(180,356,0.75,1,'coral','gold','stand','bob','smile')}
{person(250,356,0.75,1,'gold','violet','stand','short','smile')}
{person(320,356,0.75,-1,'green','blue','stand','bun','smile')}
{person(390,356,0.75,-1,'violet','gold','stand','short','smile')}
{person(460,356,0.75,-1,'blue','teal','stand','bob','smile')}
<g transform="translate(300 140)">
  <path d="M-110-60h220v100h-220z" class="ink"/>
  <g fill="{TONES['green'][0]}">{''.join(f'<rect x="{-80+i*50}" y="-40" width="34" height="60"/>' for i in range(3))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('turnover', '品が入れ替わりながら回っていくイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="18" stroke-linecap="round">
  <path d="M300 100a130 130 0 1 1-92 38"/>
</g>
<path d="M300 62l56 38-56 38z" fill="{TONES['teal'][2]}" stroke="{INK}" stroke-width="3"/>
{box(300,230,110,70,20,'gold')}
<g class="gold o"><ellipse cx="460" cy="330" rx="26" ry="11"/><ellipse cx="140" cy="330" rx="26" ry="11"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('usage', '正しい使い方と誤った使い方を並べたイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-56-30h112M-56 10h80"/></g>
</g>
{ck(180,340,0.9)}
<g transform="translate(440 230)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-56-30h112M-56 10h80"/></g>
</g>
{xx(440,340,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
