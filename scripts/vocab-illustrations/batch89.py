"""第89回: pe〜pr の名詞を中心に45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'

add('petition', '大勢の署名を集めて差し出す請願のイラスト。', f"""
<g transform="translate(320 200)">
  <path d="M-150-150h300v300h-300z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-110-110h220M-110-80h180"/></g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-linecap="round">
    {''.join(f'<path d="M-110 {-20+i*40}q20-16 40 0t40-6 40 8"/>' for i in range(4))}
  </g>
</g>
{hand(120,260,1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M500 300h60"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('phase', '月の形が移るように変わる段階のイラスト。', f"""
<circle cx="110" cy="200" r="46" class="goldp o"/>
<g transform="translate(240 200)">
  <circle r="46" class="goldp o"/>
  <path d="M0-46a46 46 0 0 0 0 92z" class="ink"/>
</g>
<g transform="translate(370 200)">
  <circle r="46" class="goldp o"/>
  <path d="M0-46a46 46 0 0 1 0 92 30 46 0 0 0 0-92z" class="ink"/>
</g>
<circle cx="500" cy="200" r="46" fill="{INK}" stroke="{INK}" stroke-width="3"/>
<g class="a" marker-end="url(#ar)"><path d="M60 320h480"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"><circle cx="370" cy="200" r="66"/></g>
""", ground=False, arrow=True)

add('phenomenon', '空に現れた不思議な光の現象のイラスト。', f"""
<path d="M0 0h600v300H0z" fill="#1f2b3d"/>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="18" opacity="0.75">
  <path d="M60 220q80-160 180-120t140-60 160 40"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="12" opacity="0.6">
  <path d="M60 260q100-150 200-110t120-60 160 50"/>
</g>
<g fill="#fffdf6">{''.join(f'<circle cx="{40+i*67}" cy="{50+(i*37)%120}" r="3"/>' for i in range(9))}</g>
<path d="M0 300h600v100H0z" class="ground"/>
{person(200,376,0.9,1,'coral','blue','up','short','surprised')}
{person(380,376,0.9,-1,'gold','violet','up','bob','surprised')}
""", ground=False)

add('philosopher', '問いを立てて考えつづける哲学者のイラスト。', f"""
{person(220,352,1.3,1,'violet','violet','think','short','neutral')}
<g transform="translate(220 260)">
  <path d="M-24 0q24 40 48 0 4 40-24 44-28-4-24-44z" fill="#d8d2c4" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g transform="translate(430 160)">
  <path d="M-110-50q-6-42 32-46 16-32 50-20 28-4 34 26 32 4 28 36-4 28-34 28h-76q-30-2-34-24z" class="bluep o"/>
  <path d="M-26-30q0-30 30-30t30 28q0 22-30 30v14" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <circle cx="4" cy="34" r="8" class="blued"/>
</g>
<g class="o" fill="#e1edfb"><circle cx="300" cy="240" r="16"/><circle cx="278" cy="272" r="10"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('philosophy', '生き方の根っこを問う哲学の書のイラスト。', f"""
<g transform="translate(250 210)">
  <path d="M-170-150h340v300h-340z" class="violet o"/>
  <path d="M-150-130h300v260h-300z" fill="#fffdf6" class="o"/>
  <path d="M-40-60q0-46 44-46t44 42q0 34-44 46v22" fill="none" stroke="{TONES['violet'][0]}" stroke-width="18" stroke-linecap="round"/>
  <circle cx="4" cy="58" r="12" class="violet"/>
</g>
<g transform="translate(500 250)">
  <path d="M-30 100v-40q-50-14-50-64 0-64 62-64 64 0 64 60 0 32-26 44v64z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M430 220h-30"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('physician', '聴診器を当てて診る医師のイラスト。', f"""
{person(220,352,1.35,1,'violet','blue','reach','bun','smile')}
<g fill="none" stroke="{INK}" stroke-width="5">
  <path d="M196 250q-16 40 14 56M244 250q16 40-14 56"/>
</g>
<circle cx="230" cy="312" r="16" fill="{MUTED}" stroke="{INK}" stroke-width="3"/>
{person(450,352,1.1,-1,'teal','gold','stand','short','neutral')}
<g transform="translate(340 180)">
  <path d="M-14-40h28v28h28v28h-28v28h-28v-28h-28v-28h28z" class="coral o"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('pill', '飲みこむ小さな錠剤のイラスト。', f"""
<g transform="translate(300 220)">
  <ellipse rx="150" ry="90" fill="#fffdf6" class="o"/>
  <path d="M-150 0h300" class="a"/>
  <path d="M-150 0a150 90 0 0 1 300 0z" class="coralp"/>
</g>
<g class="goldp o"><circle cx="140" cy="340" r="22"/><circle cx="460" cy="340" r="22"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('pipeline', '遠くまで液体を送る管のイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="46" stroke-linecap="round">
  <path d="M60 200h180q40 0 40 40v60q0 40 40 40h220"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="16" stroke-linecap="round">
  <path d="M60 200h180q40 0 40 40v60q0 40 40 40h220"/>
</g>
<g fill="{MUTED}" class="o">
  <rect x="150" y="164" width="24" height="72"/><rect x="400" y="304" width="24" height="72"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M60 120h180"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('pirate', '黒い旗をかかげた海賊船のイラスト。', f"""
<path d="M0 300h600v100H0z" class="bluep"/>
<g transform="translate(300 290)">
  <path d="M-160 10h320l-50 60h-220z" class="goldd o"/>
  <path d="M-6 10v-180h12v180z" fill="{TONES['gold'][2]}"/>
  <path d="M6-170h150l-40 40 40 40H6z" class="tealp o"/>
  <path d="M-120-170h120v56h-120z" class="ink"/>
  <g fill="#fffdf6"><circle cx="-70" cy="-150" r="13"/><path d="M-60-130h-40v8h40z"/></g>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"><path d="M60 360q40-16 80 0t80 0M380 380q40-16 80 0t80 0"/></g>
""", ground=False)

add('pit', '地面に開いた深い穴のイラスト。', f"""
<path d="M0 240h600v160H0z" fill="#e8ded2"/>
<path d="M0 240h600" class="a"/>
<g transform="translate(300 250)">
  <ellipse rx="150" ry="46" fill="#5e4a3c" class="o"/>
  <path d="M-150 0q0 120 150 120T150 0z" fill="#4a3a2f"/>
  <path d="M-150 0q0 120 150 120T150 0" fill="none" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"><path d="M520 250v90"/></g>
""", ground=False, arrow=True)

add('pitch', 'くいを打ってテントを張るイラスト。', f"""
<g transform="translate(330 320)">
  <path d="M-130 0l130-170 130 170z" class="coralp o"/>
  <path d="M-44 0l44-58 44 58z" class="corald o"/>
  <path d="M-130 0l-40 20M130 0l40 20" fill="none" stroke="{MUTED}" stroke-width="5"/>
</g>
{person(140,352,1.1,1,'teal','blue','reach','cap','neutral')}
<g transform="translate(200 300) rotate(20)">
  <path d="M-8-40h16v70h-16z" fill="{MUTED}" class="o"/>
  <path d="M-18-50h36v16h-36z" fill="{MUTED}" class="o"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('plea', 'ひざをついて必死に願うイラスト。', f"""
<g transform="translate(280 350)">
  <path d="M-60 0h100v-16h-100z" fill="{TONES['blue'][2]}" class="o"/>
  <path d="M-30-16h30v-40h-30z" fill="{TONES['blue'][2]}" class="o"/>
  <path d="M-34-56q34-16 68 0l-10 46h-48z" class="coral o"/>
  <circle cx="10" cy="-88" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-15-85q4-30 27-30 26 0 30 27-14-11-29-4-13-11-28 7z" fill="{HAIR}" stroke="{HAIR}" stroke-width="2"/>
  <g fill="{INK}"><circle cx="2" cy="-86" r="2.5"/><circle cx="20" cy="-86" r="2.5"/></g>
  <path d="M2-74q10 8 18 0" fill="none" stroke="{INK}" stroke-width="2"/>
  <path d="M30-50l40-16" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
</g>
{hand(430,280,-1)}
<g transform="translate(300 170)">
  <path d="M-70-40h140v70h-140zM-40 30l-10 26 34-26z" fill="#fffdf6" class="o"/>
  <path d="M-16-20q0-16 16-16t16 14q0 12-16 16v8" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"/>
  <circle cy="16" r="5" class="coral"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('pole', 'まっすぐ立てられた長い棒のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-16-180h32v320h-32z" fill="{TONES['gold'][2]}" class="o"/>
  <ellipse cy="-180" rx="16" ry="8" class="gold o"/>
</g>
<ellipse cx="300" cy="360" rx="70" ry="18" class="greenp o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M480 360V60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('pond', 'すいれんの浮かぶ小さな池のイラスト。', f"""
<g transform="translate(300 260)">
  <ellipse rx="240" ry="110" class="bluep o"/>
  <ellipse rx="200" ry="84" fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"/>
</g>
<g class="greenp o"><ellipse cx="190" cy="240" rx="46" ry="20"/><ellipse cx="400" cy="290" rx="40" ry="18"/></g>
<g class="coralp o"><circle cx="330" cy="220" r="20"/></g>
<g class="gold o"><ellipse cx="250" cy="300" rx="30" ry="14"/><path d="M280 300l24-14v28z"/></g>
{tree(90,240,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('popularity', '大勢に取り囲まれて人気のあるイラスト。', f"""
{person(300,346,1.25,1,'coral','blue','up','bun','smile')}
{person(140,352,0.8,1,'teal','blue','up','short','smile')}
{person(210,352,0.8,1,'gold','violet','up','bob','smile')}
{person(400,352,0.8,-1,'green','blue','up','short','smile')}
{person(470,352,0.8,-1,'violet','gold','up','bun','smile')}
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M200 150q-18-24 0-34 18-10 18 14 0-24 18-14 18 10 0 34l-18 18z"/>
  <path d="M390 150q-18-24 0-34 18-10 18 14 0-24 18-14 18 10 0 34l-18 18z"/>
</g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2">
  <path d="M300 120l12 26 28 3-20 20 5 28-25-14-25 14 5-28-20-20 28-3z"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('portion', '全体から取り分けた一人前のイラスト。', f"""
<g transform="translate(190 230)">
  <circle r="120" fill="#fffdf6" class="o"/>
  <circle r="96" class="goldp o"/>
  <path d="M0 0L0-96A96 96 0 0 1 68 68z" fill="#fffaf1" stroke="{INK}" stroke-width="2.5"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M340 230h50"/></g>
<g transform="translate(480 250)">
  <ellipse rx="80" ry="24" fill="#fffdf6" class="o"/>
  <path d="M-40-10l50-40 40 40z" class="goldp o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('portrait', '額に入った人物の肖像画のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-160-150h320v300h-320z" class="goldd o"/>
  <path d="M-134-124h268v248h-268z" fill="#fdf6e3" class="o"/>
  <circle cx="0" cy="-30" r="60" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-32-38q6-46 34-46 30 0 36 42-18-16-36-6-16-14-34 10z" fill="{HAIR}" stroke="{HAIR}" stroke-width="2"/>
  <g fill="{INK}"><circle cx="-18" cy="-30" r="4"/><circle cx="18" cy="-30" r="4"/></g>
  <path d="M-14-8q14 12 28 0" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-80 124v-40q0-50 80-50t80 50v40z" class="teal o"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('possession', '自分のものとして持っている品のイラスト。', f"""
{person(150,352,1.2,1,'teal','blue','carry','short','smile')}
{box(330,300,140,100,28,'gold')}
<g transform="translate(470 300)">
  <path d="M-40-40h80v80h-80z" class="coralp o"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="12 10"><rect x="250" y="200" width="300" height="170" rx="22"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('poverty', '財布も棚も空っぽな貧しさのイラスト。', f"""
<g transform="translate(400 240)">
  <path d="M-120-90h240v180h-240z" fill="#fffdf6" class="o"/>
  <path d="M-120-30h240M-120 30h240" class="a"/>
</g>
{person(170,352,1.15,1,'blue','blue','hold','short','sad')}
<g transform="translate(230 280)">
  <path d="M-40-24h80v48h-80z" class="goldd o"/>
  <path d="M-40-24q40-20 80 0" fill="none" stroke="{TONES['gold'][0]}" stroke-width="4"/>
</g>
{xx(400,240,1.1,MUTED)}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('practitioner', '看板を出して実際に仕事をする開業者のイラスト。', f"""
<g transform="translate(400 250)">
  <path d="M-140-140h280v290h-280z" fill="#fffdf6" class="o"/>
  <path d="M-140-140h280v40h-280z" class="teal o"/>
  <path d="M-40 60h80v90h-80z" class="teald o"/>
</g>
<path d="M170 200h150v60H170z" class="paper"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M200 230h90"/></g>
<path d="M245 200v-30" class="a"/>
{person(200,352,1.15,1,'violet','blue','stand','bun','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('precedent', '前の例にならって決めるイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-110-120h220v240h-220z" class="paper"/>
  <path d="M-80-90h160v60h-160z" class="tealp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-80 0h160M-80 30h160M-80 60h120"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 230h60"/></g>
<g transform="translate(460 230)">
  <path d="M-100-120h200v240h-200z" class="paper"/>
  <path d="M-70-90h140v60h-140z" class="tealp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-70 0h140M-70 30h140"/></g>
</g>
{ck(460,330,0.9)}
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('precision', 'ねらいの中心にぴたりと当てる正確さのイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="150" fill="#fffdf6" class="o"/>
  <circle r="112" class="coralp o"/>
  <circle r="74" fill="#fffdf6" class="o"/>
  <circle r="36" class="coral o"/>
  <circle r="10" class="ink"/>
</g>
<g transform="translate(300 210) rotate(35)">
  <path d="M6 0h180v10H6z" fill="{TONES['gold'][2]}"/>
  <path d="M170-14h40v38h-40z" class="tealp o"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('predator', '小さな獲物を追う捕食者のイラスト。', f"""
<g transform="translate(190 280)">
  <path d="M-110 60q-30-60 10-100 50-50 130-30 70 20 60 70-10 56-100 60-70 4-100 0z" fill="#6b5a4a" class="o"/>
  <path d="M100-70q40-20 60 10 20 30-10 50-20-30-50-20z" fill="#6b5a4a" class="o"/>
  <circle cx="140" cy="-30" r="5" fill="#fffdf6"/>
  <path d="M-110 60l-40 30M-40 70v30M40 70v30" fill="none" stroke="#6b5a4a" stroke-width="12" stroke-linecap="round"/>
</g>
<g transform="translate(490 330)">
  <ellipse rx="44" ry="28" fill="#b9a98f" class="o"/>
  <circle cx="36" cy="-20" r="20" fill="#b9a98f" class="o"/>
  <path d="M52-26l22 8-22 10z" class="corald o"/>
  <circle cx="42" cy="-26" r="4" class="ink"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M360 250h60"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('predecessor', '前の人から席を引き継ぐイラスト。', f"""
{person(150,352,1.15,1,'violet','violet','give','bun','smile')}
{person(460,352,1.15,-1,'teal','blue','reach','short','smile')}
<g transform="translate(300 300)">
  <path d="M-50 60v-60h100v60" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linejoin="round"/>
  <path d="M-50 0v-90" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"/>
  <path d="M-50-90h100" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 180h140"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('prediction', '先のことを言い当てる予測のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-220-140h440v280h-440z" class="paper"/>
  <path d="M-180 80l60-40 50 20 40-50" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"/>
  <path d="M-30 10q60-40 90-80t100-30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="14 12"/>
  <circle cx="-30" cy="10" r="9" class="teal"/>
  <path d="M-180-120v220h380" class="a"/>
</g>
<g transform="translate(480 130)">
  <path d="M-26-24q0-26 26-26t26 24q0 20-26 26v12" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"/>
  <circle cy="34" r="6" class="coral"/>
</g>
""", ground=False)

add('pregnancy', 'おなかに赤ちゃんを宿した妊娠のイラスト。', f"""
<g transform="translate(300 350)">
  <path d="M-12-10l-8 10M12-10l8 10" fill="none" stroke="{TONES['blue'][2]}" stroke-width="16" stroke-linecap="round"/>
  <path d="M-34-96q34-16 68 0l16 46q10 30-16 42h-68q-26-12-16-42z" class="coral o"/>
  <circle cx="0" cy="-126" r="28" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-33-129q4-32 29-32 28 0 32 29-15-12-31-5-14-12-30 8z" fill="{HAIR}" stroke="{HAIR}" stroke-width="2"/>
  <g fill="{INK}"><circle cx="-9" cy="-126" r="2.5"/><circle cx="9" cy="-126" r="2.5"/></g>
  <path d="M-8-114q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2"/>
  <path d="M-34-80q-30 10-24 46" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
  <path d="M34-80q30 10 24 46" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
</g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M300 252q-16-20 0-28 16-8 16 12 0-20 16-12 16 8 0 28l-16 16z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('prejudice', '色つきの見方で決めつける偏見のイラスト。', f"""
{face(170,210,80,'smile')}
<g transform="translate(330 210)">
  <path d="M-40-130h80v260h-80z" class="coralp o" opacity="0.8"/>
</g>
<g transform="translate(490 210)">
  <ellipse rx="60" ry="36" fill="#fffdf6" class="o"/>
  <circle r="22" class="coral o"/><circle r="9" class="ink"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M420 210h-160"/></g>
{xx(330,340,0.8)}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('premise', '上に組み立てる土台となる前提のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-200-40h400v70h-400z" class="teal o"/>
  <path d="M-120-110h240v70h-240z" class="tealp o"/>
  <path d="M-60-180h120v70H-60z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M520 280h-80"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('premium', '割増を払って手にする上等な品のイラスト。', f"""
<g transform="translate(210 280)">
  <path d="M-70-60h140v120h-140z" class="tealp o"/>
</g>
<g transform="translate(430 250)">
  <path d="M-90-80h180v160h-180z" class="teal o"/>
  <path d="M-40-130l20 34 36 6-26 24 6 36-36-18-36 18 6-36-26-24 36-6z" class="gold o" transform="translate(40 0)"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round" marker-end="url(#ar)"><path d="M540 350v-80"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('prescription', '医師が書いた薬の処方箋のイラスト。', f"""
<g transform="translate(270 210)">
  <path d="M-150-150h300v300h-300z" class="paper"/>
  <path d="M-120-120h120v40h-120z" class="coral o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-120-40h240M-120 0h240M-120 40h180"/></g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-linecap="round"><path d="M-120 100q30-20 60 0t60-6"/></g>
</g>
<g transform="translate(500 300)">
  <path d="M-50-16h50v32h-50q-16 0-16-16t16-16z" class="coral o"/>
  <path d="M0-16h34q16 0 16 16t-16 16H0z" fill="#fffdf6" class="o"/>
</g>
<g class="goldp o"><circle cx="490" cy="230" r="20"/><circle cx="540" cy="250" r="20"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('presence', '空いた席の中でその人が居合わせているイラスト。', f"""
{sit(300,340,1.25,1,'coral','blue','short','smile','down')}
<g transform="translate(300 340)">
  <path d="M-50 0v-40h100v40" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linejoin="round"/>
  <path d="M-50-40v-90" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="10" stroke-linejoin="round" stroke-linecap="round">
  <path d="M90 340v-40h80v40M90 300v-80M410 340v-40h80v40M410 300v-80"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10"><circle cx="300" cy="250" r="120"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('preservation', '手を加えずそのまま守り残す保存のイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-90 0v-90h180V0z" fill="#fffdf6" class="o"/>
  <path d="M-104-90L0-150l104 60z" class="coral o"/>
  <path d="M-24-56h48V0h-48z" class="corald o"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" opacity="0.8">
  <path d="M120 320V180q0-90 180-90t180 90v140"/>
</g>
<path d="M120 320h360" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"/>
{ck(300,140,1)}
<path d="M60 356h480" class="a"/>
""", ground=True)

add('prevalence', 'どこもかしこも同じものばかりになる普及のイラスト。', f"""
<g class="teal o">
  {''.join(f'<circle cx="{100+c*80}" cy="{150+r*80}" r="30"/>' for r in range(3) for c in range(6))}
</g>
<circle cx="340" cy="230" r="30" class="coralp o"/>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="12 10"><rect x="50" y="100" width="500" height="260" rx="26"/></g>
""", ground=False)

add('prevention', '届く前に食い止める予防のイラスト。', f"""
<g transform="translate(360 210)">
  <path d="M0-130l120 40v90q0 80-120 120-120-40-120-120v-90z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"><path d="M-50-10l34 40 66-70"/></g>
</g>
<g class="coral o"><circle cx="120" cy="150" r="20"/><circle cx="110" cy="240" r="18"/><circle cx="130" cy="320" r="16"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M150 150h50M140 240h50M155 320h40"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('prey', '追われる側の獲物のイラスト。', f"""
<g transform="translate(430 310)">
  <ellipse rx="60" ry="40" fill="#b9a98f" class="o"/>
  <circle cx="50" cy="-30" r="28" fill="#b9a98f" class="o"/>
  <path d="M72-38l28 10-28 12z" class="corald o"/>
  <circle cx="58" cy="-38" r="5" class="ink"/>
  <path d="M-40 40v34M20 42v32" fill="none" stroke="#8a7a63" stroke-width="10" stroke-linecap="round"/>
  <path d="M30-52q-6-34 16-40-4 24 4 40z" fill="#b9a98f" class="o"/>
</g>
<g fill="#4a4038">
  <path d="M60 330q-20-50 10-80 40-40 100-20 50 20 40 56-10 40-70 44-50 4-80 0z"/>
  <path d="M150 240q30-16 44 6 16 22-8 36-14-22-36-14z"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M230 250h110"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"><ellipse cx="440" cy="280" rx="130" ry="100"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('pride', '胸を張って誇りを示すイラスト。', f"""
{person(300,346,1.4,1,'coral','blue','stand','short','smile')}
<g transform="translate(300 250)">
  <circle cy="20" r="38" class="gold o"/>
  <path d="M0-6l12 24 26 4-19 18 5 26-24-14-24 14 5-26-19-18 26-4z" class="goldd"/>
  <path d="M-30-40l24 34h-24zM30-40l-24 34h24z" class="coral o"/>
</g>
<g class="golds"><path d="M170 170l-22-20M430 170l22-20M300 110v-24"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('priority', '先にやるべきものを一番上に置くイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-190-150h380v300h-380z" class="paper"/>
  <path d="M-160-120h320v70h-320z" class="coral o"/>
  <path d="M-160-30h320v46h-320z" class="tealp o"/>
  <path d="M-160 36h320v46h-320z" class="tealp o"/>
  <path d="M-160 102h320v46h-320z" class="tealp o"/>
</g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2">
  <path d="M540 130l12 26 28 3-20 20 5 28-25-14-25 14 5-28-20-20 28-3z"/>
</g>
""", ground=False)

add('privacy', 'カーテンを閉じて中を見せないイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-200-160h400v320h-400z" fill="#dfe6ea" class="o"/>
  <path d="M-160-120h320v240h-320z" fill="#fffdf6" class="o"/>
  <path d="M-160-120h170q40 120 0 240h-170z" class="bluep o"/>
  <path d="M160-120H-10q-40 120 0 240h170z" class="bluep o"/>
  <path d="M-180-130h360v18h-360z" class="ink"/>
</g>
{hand(540,240,-1)}
{xx(470,240,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('proceeding', '決まった順に進める手続きのイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-230-80h120v120h-120z" class="paper"/>
  <path d="M-60-80h120v120H-60z" class="paper"/>
  <path d="M110-80h120v120H110z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">
    <path d="M-200-40h60M-200-16h60M-30-40h60M-30-16h60M140-40h60M140-16h60"/>
  </g>
  <g fill="none" stroke="{GRN}" stroke-width="6"><path d="M-190 16l10 12 20-24M-20 16l10 12 20-24M150 16l10 12 20-24"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 220h50M350 220h50"/></g>
<g transform="translate(300 340) rotate(-20)">
  <path d="M-60-14h50v28h-50z" class="goldd o"/>
  <path d="M-10-8h100v16H-10z" class="gold o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('processing', '原料を通して仕上げる加工のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-100-110h200v220h-200z" class="bluep o"/>
  <path d="M-50-60h100v90h-100z" class="ink"/>
  <path d="M-30 50h60v40h-60z" class="blued o"/>
</g>
<g class="goldp o"><path d="M80 200l40-16 14 38-40 12z"/></g>
<g class="gold o"><rect x="470" y="196" width="60" height="60" rx="8"/></g>
<g class="a" marker-end="url(#ar)"><path d="M150 230h40M410 230h40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('programming', '画面に命令を書き並べるプログラミングのイラスト。', f"""
<g transform="translate(300 180)">
  <path d="M-220-140h440v260h-440z" class="ink"/>
  <path d="M-206-126h412v232h-412z" fill="#26303f"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="7" stroke-linecap="round">
    <path d="M-170-90h90M-140-50h130M-140-10h80M-110 30h120M-170 70h60"/>
  </g>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="7" stroke-linecap="round">
    <path d="M40-90h80M20-50h70M-40-10h60M40 30h60"/>
  </g>
</g>
<g transform="translate(300 350)">
  <path d="M-140-24h280v48h-280z" class="bluep o"/>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="2">{''.join(f'<rect x="{-124+c*35}" y="{-14+r*18}" width="28" height="14" rx="3"/>' for r in range(2) for c in range(7))}</g>
</g>
""", ground=False)

add('projection', '映写機が壁に映し出す投影のイラスト。', f"""
<g transform="translate(120 250)">
  <path d="M-60-40h120v80h-120z" class="ink"/>
  <path d="M60-24h26v48H60z" class="bluep o"/>
  <circle cx="-30" cy="-20" r="7" class="coral"/>
</g>
<path d="M206 226L420 120v260L206 274z" fill="{TONES['gold'][1]}" opacity="0.7"/>
<g transform="translate(480 250)">
  <path d="M-70-140h140v280h-140z" fill="#fffdf6" class="o"/>
  <path d="M-50-40l40-50 34 40 26-30v110h-100z" class="greenp o"/>
  <circle cx="30" cy="-70" r="18" class="goldp o"/>
</g>
<path d="M60 390h480" class="a"/>
""", ground=True)

add('promotion', '一段上の役に上がる昇進のイラスト。', f"""
<g transform="translate(300 330)">
  <path d="M-200 0h120v-50h-120z" class="tealp o"/>
  <path d="M-80-50h120v-90H-80z" class="teal o"/>
  <path d="M40-140h120v-130H40z" class="teald o"/>
</g>
{person(100,326,0.95,1,'gold','blue','stand','short','smile')}
{person(220,236,0.95,1,'gold','blue','walk','short','smile')}
{person(340,186,0.95,1,'coral','blue','up','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M120 240q100-120 200-140"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('proof', '確かだと示す証拠のイラスト。', f"""
<g transform="translate(250 210)">
  <path d="M-160-150h320v300h-320z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-120-110h240M-120-70h240M-120-30h180"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"><circle cx="60" cy="80" r="44"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4">
    <path d="M30 80q30-30 60 0M40 96q20-20 40 0M50 110q10-10 20 0"/>
  </g>
</g>
<g transform="translate(490 200)">
  <circle r="60" fill="none" stroke="{INK}" stroke-width="8"/>
  <circle r="52" fill="#fffdf6" opacity="0.4"/>
  <path d="M44 44l50 50" fill="none" stroke="{INK}" stroke-width="14" stroke-linecap="round"/>
</g>
{ck(250,340,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('propaganda', '拡声器で一方的に言い広める宣伝のイラスト。', f"""
<g transform="translate(180 200)">
  <path d="M-40-40h50v80h-50z" class="ink"/>
  <path d="M10-70l90-40v220l-90-40z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M300 160q30 40 0 80M350 130q60 70 0 140M400 100q90 100 0 200"/>
</g>
{person(500,352,0.9,-1,'teal','blue','stand','short','neutral')}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('proposal', '案をまとめて差し出す提案のイラスト。', f"""
{person(150,352,1.15,1,'teal','blue','give','short','smile')}
<g transform="translate(320 240)">
  <path d="M-90-80h180v160h-180z" class="paper"/>
  <path d="M-60-50h120v40h-120z" class="tealp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-60 10h120M-60 40h90"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M430 240h50"/></g>
{person(540,352,1.1,-1,'coral','gold','reach','bob','smile')}
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

print(len(W), ' '.join(W))
print(sheet(W))
