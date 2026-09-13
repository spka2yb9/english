"""第112回: 抽象名詞45語。"""
from lib import *
W=[]
def add(slug,a,b,**k): W.append(emit(slug,a,b,**k))
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
def gear(x,y,r=60,cls='teal',teeth=8):
    t=''.join(f'<rect x="-12" y="{-r-22}" width="24" height="26" transform="rotate({i*360//teeth})"/>' for i in range(teeth))
    return (f'<g transform="translate({x} {y})"><g class="{cls} o">{t}</g>'
            f'<circle r="{r}" class="{cls} o"/><circle r="{r*0.35:.0f}" fill="#fffdf6" stroke="{INK}" stroke-width="3"/></g>')

add('beneficiary', '基金から恵みを受け取る人のイラスト。', f"""
<g transform="translate(160 270)">
  <path d="M-90-40h180v100h-180z" class="goldd o"/>
  <path d="M-100-60h200v20h-200z" class="gold o"/>
</g>
{person(450,352,1.25,-1,'teal','blue','reach','bob','smile')}
<g transform="translate(310 250)">
  <path d="M-50-26h100v52h-100z" class="greenp o"/>
  <circle r="14" class="gold o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 170h140"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('campaign', '旗と看板をかかげて進める運動のイラスト。', f"""
{person(140,352,1.05,1,'coral','blue','up','short','neutral')}
{person(250,352,1.05,1,'gold','violet','up','bob','neutral')}
{person(360,352,1.05,1,'teal','gold','up','cap','neutral')}
<g class="paper"><rect x="96" y="150" width="90" height="60"/><rect x="316" y="150" width="90" height="60"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M141 210v40M361 210v40"/></g>
<g transform="translate(480 250)">
  <path d="M-6 100V-90" class="a"/>
  <path d="M-6-90h90v60H-6z" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('capitalism', '会社が競い合い金が回る仕組みのイラスト。', f"""
{tower(150,320,0.62,'teal',4)}
{tower(300,320,0.62,'coral',4)}
{tower(450,320,0.62,'violet',4)}
<g class="gold o"><ellipse cx="225" cy="160" rx="26" ry="11"/><ellipse cx="375" cy="160" rx="26" ry="11"/></g>
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="4" marker-end="url(#ar)"><path d="M190 200h40M340 200h40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('chairman', '席の上座で会をまとめる議長のイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-220-30h440v20h-440z" class="goldd o"/>
</g>
{person(300,300,1.15,1,'violet','blue','point','bun','neutral')}
<g transform="translate(300 250)">
  <path d="M-46-20h92v34h-92z" class="paper"/>
  <g fill="{INK}"><rect x="-28" y="-8" width="56" height="10"/></g>
</g>
{sit(150,376,0.75,1,'teal','blue','short','neutral','lap')}
{sit(450,376,0.75,-1,'coral','gold','bob','neutral','lap')}
<path d="M60 390h480" class="a"/>
""", ground=True)

add('circumstance', 'まわりの事情に取り巻かれているイラスト。', f"""
{person(300,352,1.2,1,'teal','blue','stand','short','neutral')}
{cloud(140,130,1,'blue')}
<g transform="translate(470 140)">
  <circle r="44" fill="#fffdf6" class="o"/>
  <path d="M0 0v-28M0 0l20 12" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
</g>
<g transform="translate(140 300)"><path d="M-50-30h100v60h-100z" class="tealp o"/></g>
<g transform="translate(470 300)"><path d="M-50-30h100v60h-100z" class="coralp o"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><circle cx="300" cy="240" r="220"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('citizenship', 'その国の一員だと認める資格のイラスト。', f"""
<g transform="translate(280 220)">
  <path d="M-140-150h280v300h-280z" class="teal o"/>
  <path d="M-120-130h240v260h-240z" fill="#fffdf6" class="o"/>
  <g transform="translate(-50 20)">
    <circle cx="0" cy="-30" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
    <path d="M-40 50v-14q0-26 40-26t40 26v14z" class="blue o"/>
  </g>
  <path d="M-90-100h180v50h-180z" class="coral o"/>
</g>
{ck(490,180,1.1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('collaboration', 'ふたりで力を合わせて作るイラスト。', f"""
{person(150,352,1.2,1,'teal','blue','reach','short','smile')}
{person(450,352,1.2,-1,'coral','gold','reach','bob','smile')}
<g transform="translate(300 250)">
  <path d="M-70-60h140v120h-140z" class="gold o"/>
  <path d="M-70 0h140M0-60v120" class="a"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M220 200h40M380 200h-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('commentary', 'その場を見ながら解説するイラスト。', f"""
{person(160,352,1.2,1,'violet','blue','hold','short','neutral')}
<g transform="translate(220 250)">
  <path d="M-16-30h32v56h-32z" class="ink"/>
  <circle cy="-40" r="20" fill="{MUTED}" class="o"/>
</g>
<g transform="translate(430 230)">
  <path d="M-130-110h260v220h-260z" class="ink"/>
  <path d="M-116-96h232v192h-232z" class="greenp"/>
</g>
{person(430,300,0.5,1,'coral','blue','walk','short','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('commerce', '品と金がやり取りされる商いのイラスト。', f"""
{tower(140,320,0.55,'teal',4)}
{tower(460,320,0.55,'coral',4)}
{box(300,200,110,70,20,'gold')}
<g transform="translate(300 300)">
  <path d="M-50-26h100v52h-100z" class="greenp o"/>
  <circle r="14" class="gold o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M220 150h140M380 330H220"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('commissioner', '任を受けて取りしきる長官のイラスト。', f"""
{person(240,352,1.35,1,'violet','blue','carry','cap','neutral')}
<g transform="translate(170 250)">
  <circle r="30" class="gold o"/>
  <path d="M0-16l7 14 16 2-12 12 3 16-14-8-14 8 3-16-12-12 16-2z" class="goldd"/>
</g>
<g transform="translate(410 260)">
  <path d="M-70-90h140v180h-140z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-44-50h88M-44-20h88"/></g>
  <circle cx="30" cy="50" r="24" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('compliance', '決まりどおりにきちんと従うイラスト。', f"""
<g transform="translate(200 220)">
  <path d="M-130-150h260v300h-260z" class="paper"/>
  <path d="M-100-110h200v40h-200z" class="teal o"/>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="3">{''.join(f'<rect x="-100" y="{-40+i*50}" width="28" height="28"/>' for i in range(4))}</g>
  <g fill="none" stroke="{GRN}" stroke-width="6">{''.join(f'<path d="M-94 {-28+i*50}l8 10 18-22"/>' for i in range(4))}</g>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-56 {-26+i*50}h150"/>' for i in range(4))}</g>
</g>
{person(470,352,1.15,-1,'teal','blue','stand','short','neutral')}
{ck(470,180,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('component', '機械から取り出したひとつの部品のイラスト。', f"""
<g transform="translate(180 240)">
  <path d="M-110-110h220v220h-220z" class="bluep o"/>
  <path d="M-60-60h50v50h-50zM10-60h50v50H10zM-60 10h50v50h-50z" class="tealp o"/>
  <path d="M10 10h50v50H10z" fill="#fffaf1" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M320 240h50"/></g>
<g transform="translate(460 240)"><path d="M-50-50h100v100h-100z" class="coral o"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('compound', 'ふたつの元素が結びついた化合物のイラスト。', f"""
<g transform="translate(180 240)">
  <circle r="50" class="tealp o"/>
</g>
<g fill="none" stroke="{GRN}" stroke-width="12" stroke-linecap="round"><path d="M270 240h50M295 215v50"/></g>
<g transform="translate(430 240)">
  <circle cx="-50" cy="0" r="44" class="tealp o"/>
  <circle cx="50" cy="0" r="44" class="coralp o"/>
  <path d="M-50 0h100" fill="none" stroke="{INK}" stroke-width="8"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('concept', '新しい形の下絵を描いたコンセプトのイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-150h400v300h-400z" fill="#e9f2f7" class="o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-dasharray="10 8">
    <path d="M-120-70h240v140h-240z"/>
    <circle cx="0" cy="0" r="46"/>
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 8"><path d="M-200-40h400M-200 60h400M-60-150v300M60-150v300"/></g>
</g>
""", ground=False)

add('conception', '頭の中で考えが形になるイラスト。', f"""
{person(180,352,1.2,1,'teal','blue','think','short','neutral')}
<g transform="translate(420 200)">
  <path d="M-140-100q-8-48 38-54 18-38 60-26 34-6 42 30 38 6 32 42-6 34-42 34h-96q-36-2-34-26z" class="bluep o"/>
  <path d="M0-90q42 0 42 40 0 24-18 34v16h-48v-16q-18-10-18-34 0-40 42-40z" class="gold o"/>
</g>
<g class="o" fill="#e1edfb"><circle cx="290" cy="250" r="14"/><circle cx="268" cy="276" r="9"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('consequence', 'したことの結果がついてくるイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 240h60"/></g>
<g transform="translate(460 240)">
  <path d="M0-100l90 160H-90z" class="coralp o"/>
  <g fill="{TONES['coral'][2]}"><rect x="-10" y="-40" width="20" height="50" rx="10"/><circle cy="34" r="11"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('consistency', 'どれも同じ形にそろっているイラスト。', f"""
<g class="teal o">{''.join(f'<rect x="{100+i*80}" y="200" width="60" height="100"/>' for i in range(6))}</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10"><path d="M80 200h480"/></g>
{ck(300,360,0.8)}
""", ground=False)

add('consultation', '専門家に向かい合って相談するイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-170-30h340v20h-340z" class="goldd o"/>
  <path d="M-140-10v46M140-10v46" class="a"/>
</g>
{sit(170,356,1,1,'teal','blue','short','neutral','lap')}
{sit(430,356,1,-1,'violet','violet','bun','smile','lap')}
<g transform="translate(360 290)"><path d="M-40-20h80v40h-80z" class="paper"/></g>
<g transform="translate(180 210)">
  <path d="M-50-30h100v50h-100zM-24 20l-10 24 30-24z" fill="#fffdf6" class="o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('consumer', '品を買って使う消費者のイラスト。', f"""
{person(200,352,1.25,1,'teal','blue','carry','bob','smile')}
<g transform="translate(280 310)">
  <path d="M-50-40h100v80h-100z" class="goldd o"/>
  <path d="M-50-40q50-30 100 0" fill="none" stroke="{TONES['gold'][0]}" stroke-width="5"/>
</g>
<g transform="translate(470 300)">
  <path d="M-110-30h220v20h-220z" class="teal o"/>
  <path d="M-110-30l-12-40h244l-12 40z" class="tealp o"/>
  <path d="M-100-10h200v70h-200z" class="goldd o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M380 200h-90"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('consumption', '使った量の合計を示すイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-220-90h440v180h-440z" fill="#fffdf6" class="o"/>
  <path d="M-220-90h300v180h-300z" class="teal o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M80 370h300"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M80 340v50M380 340v50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('contest', '賞をめざして競い合うイラスト。', f"""
{person(160,352,1.2,1,'teal','blue','up','short','neutral')}
{person(440,352,1.2,-1,'coral','gold','up','bob','neutral')}
<g transform="translate(300 200)">
  <path d="M-50-90h100v40q0 60-50 76-50-16-50-76z" class="gold o"/>
  <path d="M-14 30h28v34h-28z" class="goldd o"/>
  <path d="M-50 64h100v20H-50z" class="goldd o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M230 300h40M370 300h-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('context', 'まわりの文があって意味が決まるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-150h400v300h-400z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">
    <path d="M-160-110h320M-160-70h320M-160 30h320M-160 70h320M-160 110h240"/>
  </g>
  <path d="M-160-40h150v50h-150z" class="coralp o"/>
  <path d="M-160-40h150v50h-150z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
</g>
""", ground=False)

add('contractor', '契約を交わして工事を請け負う人のイラスト。', f"""
{person(180,352,1.25,1,'gold','blue','carry','cap','neutral')}
<g transform="translate(300 260)">
  <path d="M-60-70h120v140h-120z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-36-40h72M-36-14h72"/></g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><path d="M-36 30q20-16 40 0"/></g>
</g>
<g transform="translate(470 300)">
  <path d="M-80 60v-120h160V60z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="6"><path d="M-80-60h160M-80 0h160M-30-120v180M30-120v180"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('contradiction', '前と後ろで言うことが食い違うイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-90-70h180v140h-180z" class="tealp o"/>
  <g fill="none" stroke="{GRN}" stroke-width="10"><path d="M-40 0l20 24 46-54"/></g>
</g>
<g transform="translate(450 230)">
  <path d="M-90-70h180v140h-180z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10"><path d="M-40-30l80 60M40-30l-80 60"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linejoin="round"><path d="M300 150l24 40-24 40 24 40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('controversy', '意見が割れて論争になるイラスト。', f"""
{person(150,352,1.15,1,'teal','blue','point','short','neutral')}
{person(450,352,1.15,-1,'coral','gold','point','bob','neutral')}
<g transform="translate(300 140)">
  <path d="M-90-60h180v100h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-56-30h112M-56 0h80"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linejoin="round"><path d="M300 230l26 40-26 40 26 40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('copyright', '作った人の権利を守る印のイラスト。', f"""
<g transform="translate(230 230)">
  <path d="M-130-140h260v280h-260z" class="paper"/>
  <path d="M-100-110h200v110h-200z" class="tealp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-100 30h200M-100 60h160"/></g>
</g>
<g transform="translate(460 230)">
  <circle r="70" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10"/>
  <path d="M26-24a40 40 0 1 0 0 48" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('corporation', 'ロゴを掲げた大きな会社のイラスト。', f"""
{tower(300,330,1,'violet',6)}
<g transform="translate(300 110)">
  <path d="M-40-40h80v80h-80z" class="coral o"/>
  <path d="M-20 20l20-40 20 40z" fill="#fffdf6"/>
</g>
{person(140,356,0.75,1,'violet','blue','walk','short','neutral')}
{person(470,356,0.75,-1,'violet','blue','walk','bob','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('council', '地元の代表が円卓に集まる議会のイラスト。', f"""
<g transform="translate(300 290)">
  <ellipse rx="210" ry="72" class="goldd o"/>
  <ellipse cy="-14" rx="210" ry="72" class="gold o"/>
</g>
{sit(150,260,0.68,1,'teal','blue','short','neutral','lap')}
{sit(260,250,0.68,1,'coral','gold','bob','neutral','lap')}
{sit(370,250,0.68,-1,'gold','violet','short','neutral','lap')}
{sit(470,260,0.68,-1,'green','blue','bun','neutral','lap')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('councillor', '議会の席につく議員ひとりのイラスト。', f"""
{sit(300,352,1.3,1,'violet','violet','short','neutral','lap')}
{chair(310,356,1.25,'gold',1)}
<g transform="translate(240 250)">
  <circle r="26" class="gold o"/>
  <path d="M0-14l6 12 14 2-10 10 2 14-12-7-12 7 2-14-10-10 14-2z" class="goldd"/>
</g>
<g transform="translate(460 300)">
  <path d="M-70-20h140v20h-140z" class="goldd o"/>
  <path d="M-40-50h80v30h-80z" class="paper"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('credibility', '出どころが確かで信じられるイラスト。', f"""
<g transform="translate(260 220)">
  <path d="M-150-150h300v300h-300z" class="paper"/>
  <path d="M-120-110h240v40h-240z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-120 {-30+i*44}h240"/>' for i in range(3))}</g>
  <circle cx="90" cy="110" r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
{ck(490,180,1.2)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('cure', '薬で病がすっかり治るイラスト。', f"""
{person(170,352,1.2,1,'blue','blue','stand','short','sad')}
<g transform="translate(300 230)">
  <path d="M-34-26h68v52h-68z" class="coral o"/>
  <path d="M-12-40h24v14h-24z" class="corald o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 300h100"/></g>
{person(460,352,1.2,1,'coral','blue','up','short','smile')}
{ck(460,180,1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('custody', '守り手のもとで大事に預かるイラスト。', f"""
{person(240,352,1.3,1,'violet','violet','give','bun','smile')}
{person(360,354,0.7,-1,'gold','coral','stand','short','smile')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="14 12"><path d="M140 340q160-190 320 0"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('dealer', '車を扱って売る業者のイラスト。', f"""
<g transform="translate(400 300)">
  <path d="M-130 0v-40l40-50h150l40 50V0z" class="teal o"/>
  <g fill="#fffdf6" class="o"><rect x="-70" y="-80" width="56" height="36"/><rect x="0" y="-80" width="56" height="36"/></g>
  <g fill="{INK}"><circle cx="-70" cy="6" r="22"/><circle cx="70" cy="6" r="22"/></g>
</g>
{person(150,352,1.2,1,'violet','blue','give','short','smile')}
<g transform="translate(240 260)">
  <circle r="20" fill="none" stroke="{TONES['gold'][2]}" stroke-width="8"/>
  <path d="M18 0h50v10h-12v12h-10v-12h-10v12h-10v-12h-8z" fill="{TONES['gold'][2]}"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('debate', '壇に分かれて意見をたたかわせるイラスト。', f"""
{person(160,352,1.2,1,'teal','blue','point','short','neutral')}
{person(440,352,1.2,-1,'coral','gold','point','bob','neutral')}
<g transform="translate(160 330)"><path d="M-50-30h100l14 50h-128z" class="goldd o"/></g>
<g transform="translate(440 330)"><path d="M-50-30h100l14 50h-128z" class="goldd o"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12"><path d="M300 130v250"/></g>
<g class="a" marker-end="url(#ar)"><path d="M250 190h100M350 240H250"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('delegate', 'みんなに送り出されて出向く代表のイラスト。', f"""
{person(150,356,0.8,1,'teal','blue','stand','short','neutral')}
{person(220,356,0.8,1,'coral','gold','stand','bob','neutral')}
{person(290,356,0.8,-1,'gold','violet','stand','short','neutral')}
{person(470,352,1.25,1,'violet','blue','walk','bun','neutral')}
<g transform="translate(410 250)">
  <circle r="24" class="gold o"/>
  <path d="M0-12l5 10 12 2-9 9 2 12-10-6-10 6 2-12-9-9 12-2z" class="goldd"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M350 220h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('democracy', 'みんなの票で政を決める仕組みのイラスト。', f"""
{building(300,290,0.8,'teal')}
{person(120,356,0.8,1,'coral','blue','up','short','smile')}
{person(200,356,0.8,1,'gold','violet','up','bob','smile')}
{person(400,356,0.8,-1,'green','blue','up','short','smile')}
{person(480,356,0.8,-1,'violet','gold','up','bun','smile')}
<g transform="translate(300 130)">
  <path d="M-50-36h100v56h-100z" class="paper"/>
  <g fill="none" stroke="{GRN}" stroke-width="7"><path d="M-24-12l12 14 24-28"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('department', '会社の中のひとつの部署のイラスト。', f"""
{tower(300,330,1,'teal',6)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10"><rect x="230" y="180" width="140" height="60" rx="8"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M500 210h-110"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('desperate', 'あとがなく死に物狂いになるイラスト。', f"""
{person(230,352,1.3,1,'coral','blue','up','short','sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M150 180l-18-26M310 160v-28"/>
</g>
<g transform="translate(470 250)">
  <path d="M-20-160h40v320h-40z" class="ink"/>
  <path d="M-130-90h110v34h-110z" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('dimension', '縦横高さのさしわたしを測るイラスト。', f"""
{box(280,240,220,140,50,'teal')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)">
  <path d="M170 350h220M390 350H170"/>
  <path d="M120 320V180M120 180v140"/>
  <path d="M400 140l60-40M460 100l-60 40"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('disability', '車いすで動く人を示すイラスト。', f"""
<g transform="translate(300 300)">
  <circle cx="-10" cy="30" r="60" fill="none" stroke="{TONES['blue'][0]}" stroke-width="12"/>
  <circle cx="60" cy="70" r="18" fill="none" stroke="{TONES['blue'][0]}" stroke-width="10"/>
  <path d="M-10-30h60v40" fill="none" stroke="{TONES['blue'][0]}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="-16" cy="-60" r="24" fill="{TONES['blue'][0]}"/>
  <path d="M-10-30l-40 10" fill="none" stroke="{TONES['blue'][0]}" stroke-width="14" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('discourse', '書きことばと話しことばで論じるイラスト。', f"""
<g transform="translate(200 230)">
  <path d="M-130-140h260v280h-260z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-96 {-100+i*44}h190"/>' for i in range(6))}</g>
</g>
{person(470,352,1.2,-1,'teal','blue','point','short','neutral')}
<g transform="translate(430 190)">
  <path d="M-70-46h140v70h-140zM40 24l12 26-34-26z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><path d="M-40-24h80M-40 0h56"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('diversity', 'いろいろな人がともにいるイラスト。', f"""
{person(120,352,1,1,'coral','blue','stand','short','smile')}
{person(220,352,1,1,'gold','violet','stand','bun','smile')}
{person(320,352,1,-1,'teal','gold','stand','cap','smile')}
{person(420,352,1,-1,'green','blue','stand','bob','smile')}
{person(510,352,1,-1,'violet','coral','stand','short','smile')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="14 12"><rect x="70" y="200" width="490" height="170" rx="26"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('division', 'ひとつを線で分け合うイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-110h200v220h-200z" class="teal o"/>
  <path d="M20-110h200v220H20z" class="coralp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="16 12"><path d="M300 90v280"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('doctrine', '教えをまとめた書のイラスト。', f"""
<g transform="translate(280 220)">
  <path d="M-150-150h300v300h-300z" class="violet o"/>
  <path d="M-130-130h260v260h-260z" fill="#fffdf6" class="o"/>
  <path d="M-14-90h28v50h50v28h-50v50h-28v-50h-50v-28h50z" class="violetp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-90 70h180M-90 100h140"/></g>
</g>
{ck(500,180,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('documentation', 'とじられた記録の束のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-180-40h360v150h-360z" class="goldd o"/>
  <path d="M-180-40l-12-40h384l-12 40z" class="goldp o"/>
</g>
<g transform="translate(210 170) rotate(-8)">
  <path d="M-80-80h160v160h-160z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-50-40h100M-50-10h100M-50 20h70"/></g>
</g>
<g transform="translate(390 160) rotate(6)">
  <path d="M-80-80h160v160h-160z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-50-40h100M-50-10h100M-50 20h70"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
