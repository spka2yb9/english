"""第84回: in〜j の名詞を中心に45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'
def gauge(x,y,r=110,ang=-40,cls='coral'):
    import math
    ex, ey = x+r*0.8*math.cos(math.radians(ang)), y+r*0.8*math.sin(math.radians(ang))
    return (f'<path d="M{x-r} {y}a{r} {r} 0 0 1 {2*r} 0" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>'
            f'<path d="M{x-r} {y}h{2*r}" class="a"/>'
            f'<path d="M{x} {y}L{ex:.0f} {ey:.0f}" fill="none" stroke="{TONES[cls][0]}" stroke-width="7" stroke-linecap="round"/>'
            f'<circle cx="{x}" cy="{y}" r="9" class="ink"/>')

add('indication', '先に起こることを知らせる兆しのイラスト。', f"""
{cloud(180,140,1.5,'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round"><path d="M140 220l-10 30M190 226l-10 30M240 220l-10 30"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M290 210h90"/></g>
<g transform="translate(460 240)">
  <path d="M-110 20q30-110 110-110t110 110z" class="coralp o"/>
  <path d="M-110 20h220v20h-220z" class="coral o"/>
  <path d="M0 40v90" class="a"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('indicator', '状態を目盛りで示す指標のイラスト。', f"""
{gauge(230,270,130,-35,'coral')}
<g fill="none" stroke="{MUTED}" stroke-width="4">
  <path d="M120 250l-16-16M230 150v-22M340 250l16-16"/>
</g>
<g transform="translate(470 240)">
  <path d="M-70-90h140v180h-140z" class="paper"/>
  <path d="M-50 50l30-40 26 20 44-70" fill="none" stroke="{TONES['teal'][0]}" stroke-width="5"/>
  <circle cx="50" cy="-40" r="9" class="coral"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('indoors', '雨の外を窓ごしに見る室内のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-260-150h520v300h-260z" fill="#fffaf1"/>
  <path d="M-260-150h520v300h-520z" fill="none" class="o"/>
</g>
<g transform="translate(410 190)">
  <path d="M-90-90h180v180h-180z" class="bluep o"/>
  <path d="M0-90v180M-90 0h180" class="a"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
    {''.join(f'<path d="M{-70+i*26} {-70+(i%3)*20}l-12 40"/>' for i in range(6))}
  </g>
</g>
{person(180,340,1.05,1,'teal','blue','stand','short','smile')}
<path d="M110 350h420" class="a"/>
""", ground=False)

add('inequality', '一方に大きくかたよった不平等のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-16 100l16-90 16 90z" class="ink"/>
  <path d="M-200-40L200 40" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>
</g>
{box(140,180,110,60,0,'teal')}
{box(460,270,180,90,0,'coral')}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('infant', '腕に抱かれた赤ちゃんのイラスト。', f"""
{person(220,352,1.3,1,'teal','blue','carry','bun','smile')}
<g transform="translate(330 250)">
  <path d="M-70 30q-16-50 20-70 40-22 90 4 30 20 14 66z" class="goldp o"/>
  <circle cx="20" cy="-20" r="42" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-16-40q20-24 44-14" fill="none" stroke="{HAIR}" stroke-width="6" stroke-linecap="round"/>
  <circle cx="8" cy="-22" r="4" class="ink"/><circle cx="34" cy="-22" r="4" class="ink"/>
  <path d="M12-6q10 8 20 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('infection', '病原体がうつり広がる感染のイラスト。', f"""
{person(150,352,1.1,1,'coral','blue','stand','short','sad')}
{person(450,352,1.1,-1,'teal','gold','stand','bob','sad')}
<g class="coral o">
  <circle cx="250" cy="200" r="18"/><circle cx="310" cy="170" r="14"/><circle cx="360" cy="205" r="16"/>
</g>
<g fill="none" stroke="{TONES['coral'][2]}" stroke-width="3">
  <path d="M232 200h-14M268 200h14M250 182v-14M250 218v14"/>
  <path d="M296 170h-12M324 170h12M310 156v-12M310 184v12"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9" marker-end="url(#ar)"><path d="M210 250q90-90 180-40"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('inflation', '物の値段がふくらんで上がるイラスト。', f"""
<g transform="translate(180 250)">
  <ellipse rx="60" ry="70" class="coralp o"/>
  <path d="M0 70l-14 20h28z" class="coral o"/>
</g>
<g transform="translate(430 210)">
  <ellipse rx="110" ry="126" class="coral o"/>
  <path d="M0 126l-20 30h40z" class="corald o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M260 220h70"/></g>
<g transform="translate(430 210)">
  <path d="M-40-40h80v80h-80z" fill="none" stroke="#fffdf6" stroke-width="6"/>
  <path d="M-40 0h80M0-40v80" fill="none" stroke="#fffdf6" stroke-width="6"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('info', '知らせを掲げた案内板のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-170-130h340v230h-340z" class="paper"/>
  <circle cx="-90" cy="-40" r="46" class="teal o"/>
  <g fill="#fffdf6"><circle cx="-90" cy="-62" r="8"/><rect x="-98" y="-46" width="16" height="46" rx="8"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-10-70h140M-10-30h140M-10 10h110M-130 50h260"/></g>
  <path d="M0 100v70" class="a"/>
</g>
<path d="M60 372h480" class="a"/>
""", ground=True)

add('infrastructure', '暮らしを支える道路と送電と水道のイラスト。', f"""
{tower(140,250,0.5,'teal',4)}
{tower(300,250,0.55,'teal',4)}
{tower(460,250,0.5,'teal',4)}
<path d="M40 250h520v40H40z" fill="#dfe6ea" class="o"/>
<g fill="none" stroke="#fffdf6" stroke-width="4" stroke-dasharray="24 20"><path d="M40 270h520"/></g>
<path d="M40 300h520v90H40z" fill="#e8ded2"/>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="14" stroke-linecap="round"><path d="M60 350h480"/></g>
<g fill="none" stroke="{INK}" stroke-width="4"><path d="M120 250v-60M480 250v-60M120 200h40M440 200h40"/></g>
<path d="M120 210q180 40 360 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"/>
""", ground=False)

add('inhabitant', 'その土地に住んでいる人のイラスト。', f"""
<g transform="translate(390 300)">
  <path d="M-90 0v-90h180V0z" fill="#fffdf6" class="o"/>
  <path d="M-104-90L0-150l104 60z" class="teal o"/>
  <path d="M-24-56h48V0h-48z" class="teald o"/>
  <path d="M30-70h44v30H30z" class="tealp o"/>
</g>
{person(180,352,1.2,1,'coral','blue','stand','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M240 260h50"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('injection', '注射器で薬を注ぎ入れるイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-170-40h230v80h-230z" fill="#fffdf6" class="o"/>
  <path d="M-170-30h150v60h-150z" class="bluep o"/>
  <path d="M-200-26h30v52h-30z" class="ink"/>
  <path d="M60-24h30v48H60z" class="ink"/>
  <path d="M90-6h130v12H90z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g fill="none" stroke="{INK}" stroke-width="3">{''.join(f'<path d="M{-140+i*36} -40v18"/>' for i in range(5))}</g>
</g>
{drop(520,230,1.6,'blue')}
<path d="M60 356h480" class="a"/>
""", ground=True)

add('injustice', 'かたよった裁きで不当に扱われるイラスト。', f"""
<g transform="translate(300 170)">
  <path d="M-8-60h16v190h-16z" class="ink"/>
  <path d="M-140-56h280v12h-280z" class="ink"/>
  <path d="M-140-44v40M140-44v70" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-186 0h92l-46 40z" class="tealp o"/>
  <path d="M94 30h92l-46 40z" class="coralp o"/>
</g>
{person(180,352,0.95,1,'teal','blue','stand','short','sad')}
{person(440,352,0.95,-1,'coral','gold','stand','bob','smile')}
{xx(300,330,0.9)}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('ink', 'インクびんとペン先のイラスト。', f"""
<g transform="translate(230 290)">
  <path d="M-80 60v-90q0-30 80-30t80 30v90z" fill="#fffdf6" class="o"/>
  <path d="M-80 60v-70q80-20 160 0v70z" class="violet o"/>
  <path d="M-30-70h60v20h-60z" class="violetd o"/>
</g>
<g transform="translate(420 200)">
  <path d="M-14-130h28l10 130-24 40-24-40z" class="gold o"/>
  <path d="M0-20v40M-20 0h40" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g class="violet o"><ellipse cx="470" cy="330" rx="46" ry="18"/><circle cx="520" cy="316" r="9"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('innovation', '今までのものを新しい仕組みに変える革新のイラスト。', f"""
<g transform="translate(160 250)">
  <circle r="70" fill="none" stroke="{MUTED}" stroke-width="16"/>
  <g fill="{MUTED}">{''.join(f'<rect x="-10" y="-92" width="20" height="24" transform="rotate({a})"/>' for a in range(0,360,45))}</g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>
<g transform="translate(440 240)">
  <path d="M0-90q56 0 56 54 0 32-24 46v22h-64v-22q-24-14-24-46 0-54 56-54z" class="gold o"/>
  <path d="M-32 40h64v20h-64z" class="goldd o"/>
  <g class="golds"><path d="M-90-40l-30-14M90-40l30-14M0-116v-30"/></g>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('input', '中へ打ち込んで入れるイラスト。', f"""
<g transform="translate(400 200)">
  <path d="M-140-110h280v220h-280z" class="ink"/>
  <path d="M-126-96h252v192h-252z" fill="#fffdf6"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"><path d="M-90-50h180M-90-10h180M-90 30h120"/></g>
</g>
<g transform="translate(150 300)">
  <path d="M-90-30h180v60h-180z" class="bluep o"/>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="2">{''.join(f'<rect x="{-76+c*26}" y="{-20+r*22}" width="20" height="16" rx="3"/>' for r in range(2) for c in range(6))}</g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 250l80-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('inquiry', 'たずねて調べる問い合わせのイラスト。', f"""
{person(160,352,1.1,1,'teal','blue','point','short','neutral')}
<g transform="translate(300 170)">
  <path d="M-66-46h132v70h-132zM-36 24l-12 26 34-26z" fill="#fffdf6" class="o"/>
  <path d="M-16-24q0-14 16-14t16 14q0 12-16 16v8" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"/>
  <circle cx="0" cy="14" r="5" class="coral"/>
</g>
<g transform="translate(450 290)">
  <path d="M-110 20h220v70h-220z" class="goldd o"/>
  <path d="M-110 0h220v20h-220z" class="gold o"/>
</g>
{person(450,270,1,-1,'coral','violet','stand','bun','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('insertion', 'すきまへ差し込むイラスト。', f"""
<g transform="translate(320 260)">
  <path d="M-160-40h320v150h-320z" class="tealp o"/>
  <path d="M-70-40h140v20h-140z" class="ink"/>
</g>
<g transform="translate(320 150)">
  <path d="M-66-60h132v90h-132z" class="gold o"/>
  <circle cx="-30" cy="-20" r="14" class="goldd o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"><path d="M0 0h50M0 14h50"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M320 190v34"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('insider', '内側にいて事情を知っている人のイラスト。', f"""
<g transform="translate(230 220)">
  <path d="M-160-140h320v290h-320z" fill="#fffdf6" class="o"/>
  <path d="M-160-140h320v34h-320z" class="teal o"/>
</g>
{person(230,340,1,1,'teal','blue','carry','short','smile')}
<g transform="translate(300 300)">
  <path d="M-30-36h60v56h-60z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-18-20h36M-18-6h36M-18 8h24"/></g>
</g>
{person(500,352,1,-1,'coral','gold','stand','bob','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M450 250h-60"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('insight', '奥にある本質まで見通す洞察のイラスト。', f"""
<g transform="translate(330 210)">
  <circle r="120" class="tealp o"/>
  <circle r="46" class="coral o"/>
  <path d="M-120 0h74M46 0h74" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>
</g>
<g transform="translate(150 200)">
  <ellipse rx="80" ry="46" fill="#fffdf6" class="o"/>
  <circle r="28" class="blue o"/><circle r="12" class="ink"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-dasharray="12 9" marker-end="url(#ar)"><path d="M236 200h60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('inspection', '機械を細かく調べる点検のイラスト。', f"""
<g transform="translate(400 260)">
  <path d="M-110-90h220v180h-220z" fill="#dfe6ea" class="o"/>
  <circle cx="-40" cy="-20" r="34" fill="none" stroke="{MUTED}" stroke-width="8"/>
  <circle cx="40" cy="30" r="24" fill="none" stroke="{MUTED}" stroke-width="8"/>
  <path d="M-90 60h60v20h-60z" class="teal o"/>
</g>
<g transform="translate(300 170)">
  <circle r="52" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle r="44" fill="#fffdf6" opacity="0.5"/>
  <path d="M38 38l50 50" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>
</g>
{person(140,352,1,1,'violet','blue','carry','bun','neutral')}
<g transform="translate(196 300)">
  <path d="M-26-34h52v56h-52z" class="paper"/>
  <g fill="none" stroke="{GRN}" stroke-width="4"><path d="M-14-16l6 8 14-16M-14 4l6 8 14-16"/></g>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('inspector', 'バッジと手帳を持って調べる調査官のイラスト。', f"""
{person(300,352,1.4,1,'violet','blue','carry','cap','neutral')}
<g transform="translate(240 250)">
  <circle r="30" class="gold o"/>
  <path d="M0-18l7 14 16 2-12 12 3 16-14-8-14 8 3-16-12-12 16-2z" class="goldd"/>
</g>
<g transform="translate(410 280)">
  <path d="M-40-50h80v100h-80z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-24-24h48M-24 0h48M-24 24h32"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('inspiration', 'ふと降りてきた着想にひらめくイラスト。', f"""
{person(220,352,1.2,1,'teal','blue','up','short','smile')}
<g transform="translate(220 160)">
  <path d="M0-60q40 0 40 38 0 22-18 32v16h-44v-16q-18-10-18-32 0-38 40-38z" class="gold o"/>
  <path d="M-22 26h44v14h-44z" class="goldd o"/>
  <g class="golds"><path d="M-70-20l-26-12M70-20l26-12M0-86v-24"/></g>
</g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2">
  <path d="M470 130l14 30 32 4-24 24 6 32-28-16-28 16 6-32-24-24 32-4z"/>
  <path d="M400 250l9 18 20 3-15 14 4 20-18-10-18 10 4-20-15-14 20-3z"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('installation', '機器を壁に取り付けるイラスト。', f"""
<g transform="translate(390 200)">
  <path d="M-110-80h220v160h-220z" class="bluep o"/>
  <path d="M-90-60h180v120h-180z" class="ink"/>
  <g class="gold o"><circle cx="-110" cy="-80" r="10"/><circle cx="110" cy="-80" r="10"/><circle cx="-110" cy="80" r="10"/><circle cx="110" cy="80" r="10"/></g>
</g>
{person(150,352,1.1,1,'teal','blue','reach','short','neutral')}
<g transform="translate(240 230)">
  <path d="M-10-40h20v70h-20z" class="coral o"/>
  <path d="M-6 30h12v50h-12z" fill="{MUTED}" class="o"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('instance', 'たくさんの中から取り出したひとつの例のイラスト。', f"""
<g transform="translate(240 230)">
  <g class="tealp o">{''.join(f'<circle cx="{-140+c*70}" cy="{-70+r*70}" r="28"/>' for r in range(3) for c in range(5))}</g>
  <circle cx="-70" cy="0" r="28" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="170" cy="230" r="46"/></g>
<g class="a" marker-end="url(#ar)"><path d="M420 230h70"/></g>
<circle cx="540" cy="230" r="34" class="coral o"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('instinct', '考えるより先に体が反応する本能のイラスト。', f"""
{flame(430,300,1.3)}
{hand(210,240,1)}
<g class="a" marker-end="url(#ar)"><path d="M300 200h-90"/></g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2">
  <path d="M320 120l-40 80h34l-16 62 56-88h-36l20-54z"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('institution', '柱の並ぶ大きな公の建物のイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-200 0h400v20h-400z" class="teald o"/>
  <path d="M-170-140h340v140h-340z" fill="#fffdf6" class="o"/>
  <g class="tealp o">{''.join(f'<rect x="{-150+i*60}" y="-130" width="40" height="130"/>' for i in range(5))}</g>
  <path d="M-200-140L0-230l200 90z" class="teal o"/>
  <path d="M-200-140h400v20h-400z" class="teald o"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('intake', '取り入れる量を量るイラスト。', f"""
<g transform="translate(300 170)">
  <path d="M-120-70h240l-90 110v70h-60v-70z" class="bluep o"/>
  <path d="M-120-70h240v20h-240z" class="blue o"/>
</g>
{drop(292,270,1.6,'blue')}
<g transform="translate(300 340)">
  <path d="M-70-40h140v56q0 20-70 20t-70-20z" fill="#fffdf6" class="o"/>
  <path d="M-66-10h132v26q0 16-66 16t-66-16z" class="bluep o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-24h30M-70-4h30"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('integrity', '差し出された金を断る誠実さのイラスト。', f"""
{person(180,352,1.2,1,'teal','blue','reach','short','neutral')}
<g transform="translate(360 250)">
  <path d="M-56-30h112v60h-112z" class="greenp o"/>
  <circle r="16" class="gold o"/>
</g>
{hand(500,250,-1)}
{xx(360,150,1)}
{ck(180,180,1)}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('intensity', 'だんだん強さを増していく激しさのイラスト。', f"""
<g transform="translate(140 250)">
  <circle r="34" class="goldp o"/>
</g>
<g transform="translate(300 240)">
  <circle r="56" class="gold o"/>
  <g class="golds"><path d="M0-80v-20M0 80v20M-80 0h-20M80 0h20"/></g>
</g>
<g transform="translate(470 230)">
  <circle r="80" class="coral o"/>
  <circle r="46" class="goldp o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
    <path d="M0-110v-24M0 110v24M-110 0h-24M110 0h24M-80-80l-18-18M80 80l18 18M80-80l18-18M-80 80l-18 18"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M100 350h420"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('interaction', 'たがいにやり取りし合う交流のイラスト。', f"""
{person(160,352,1.15,1,'teal','blue','point','short','smile')}
{person(450,352,1.15,-1,'coral','gold','point','bob','smile')}
<g class="a" marker-end="url(#ar)"><path d="M250 200h110M360 260H250"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('interface', '人と機械が触れ合う接点のイラスト。', f"""
<g transform="translate(420 210)">
  <path d="M-140-120h280v240h-280z" class="ink"/>
  <path d="M-126-106h252v212h-252z" fill="#fffdf6"/>
  <g class="teal o"><rect x="-90" y="-70" width="70" height="46" rx="10"/><rect x="10" y="-70" width="70" height="46" rx="10"/></g>
  <g class="coral o"><rect x="-90" y="10" width="170" height="46" rx="10"/></g>
</g>
{hand(160,230,1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M240 230h50"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('interference', '別の波が割り込んで乱れる干渉のイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6">
  <path d="M40 160q40-50 80 0t80 0"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" stroke-dasharray="6 10">
  <path d="M360 160q40-50 80 0t80 0"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6">
  <path d="M300 60l-40 60 50 30-40 60"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M300 240v90"/></g>
{xx(300,300,0.9)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('interior', '家具の置かれた部屋の内側のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-250-160h500v300h-500z" fill="#fffdf6" class="o"/>
  <path d="M-250 60h500" class="a"/>
  <path d="M-190-100h150v100h-150z" class="bluep o"/>
  <path d="M-115-100v100M-190-50h150" class="a"/>
</g>
<g transform="translate(380 290)">
  <path d="M-130-40h260v50h-260z" class="coral o"/>
  <path d="M-130-40v-40h50v40M130-40v-40h-50v40" class="corald o"/>
  <path d="M-110 10v30M110 10v30" class="a"/>
</g>
<g transform="translate(130 300)">
  <path d="M-40 40v-70h80v70z" class="goldd o"/>
  <ellipse cy="-70" rx="46" ry="26" class="gold o"/>
</g>
<path d="M50 340h500" class="a"/>
""", ground=False)

add('interpretation', '同じものが人によって違う意味に読まれるイラスト。', f"""
<g transform="translate(300 150)">
  <path d="M-70-60h140v120h-140z" class="tealp o"/>
  <path d="M-40-30h80v60h-80z" class="teal o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)">
  <path d="M250 230L150 290M350 230l100 60"/>
</g>
{person(120,352,0.95,1,'coral','blue','stand','short','smile')}
{person(480,352,0.95,-1,'violet','gold','stand','bob','neutral')}
<g transform="translate(120 250)"><circle r="26" class="coralp o"/></g>
<g transform="translate(480 250)"><path d="M-26-26h52v52h-52z" class="violetp o"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('interval', 'ふたつの間にあいた間隔のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-240-70h120v140h-120z" class="teal o"/>
  <path d="M120-70h120v140H120z" class="teal o"/>
  <path d="M-240 100h480" class="a"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)">
  <path d="M300 230h-90M300 230h90"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3" stroke-dasharray="8 8"><path d="M180 140v180M420 140v180"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('intervention', '争いの間に割って入って止めるイラスト。', f"""
{person(130,352,1.05,1,'blue','blue','point','short','sad')}
{person(470,352,1.05,-1,'coral','gold','point','bob','sad')}
{person(300,346,1.25,1,'green','violet','up','bun','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M300 110v40"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('invasion', '国境を越えて攻め込む侵攻のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-260-150h230v300h-230z" class="tealp o"/>
  <path d="M-10-150h270v300h-270z" class="coralp o"/>
  <path d="M-20-150v300" fill="none" stroke="{INK}" stroke-width="6" stroke-dasharray="16 12"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" marker-end="url(#ar)">
  <path d="M420 130H190M440 220H190M420 310H190"/>
</g>
""", ground=False, arrow=True)

add('investigation', '手がかりを拾って調べる捜査のイラスト。', f"""
<g transform="translate(220 300)">
  <g class="ink" opacity="0.6">{''.join(f'<ellipse cx="{-160+i*70}" cy="{(i%2)*26}" rx="20" ry="12" transform="rotate(-20 {-160+i*70} {(i%2)*26})"/>' for i in range(5))}</g>
</g>
<g transform="translate(400 190)">
  <circle r="76" fill="none" stroke="{INK}" stroke-width="9"/>
  <circle r="66" fill="#fffdf6" opacity="0.45"/>
  <path d="M54 54l60 60" fill="none" stroke="{INK}" stroke-width="16" stroke-linecap="round"/>
  <g class="ink" opacity="0.6"><ellipse cx="-10" cy="10" rx="26" ry="16" transform="rotate(-20 -10 10)"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M120 200h150"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('investigator', '手帳を手に事件を追う捜査員のイラスト。', f"""
{person(230,352,1.35,1,'blue','blue','carry','cap','neutral')}
<g transform="translate(340 270)">
  <path d="M-40-56h80v112h-80z" class="paper"/>
  <path d="M-40-56h80v20h-80z" class="ink"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-24-16h48M-24 6h48M-24 28h30"/></g>
</g>
<g transform="translate(470 190)">
  <circle r="50" fill="none" stroke="{INK}" stroke-width="8"/>
  <circle r="42" fill="#fffdf6" opacity="0.4"/>
  <path d="M36 36l40 40" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('involvement', 'みんなの仕事に自分も加わって関わるイラスト。', f"""
<g transform="translate(300 250)">
  <circle r="70" class="tealp o"/>
  <circle r="30" class="teal o"/>
</g>
{hand(120,180,1)}
{hand(480,180,-1)}
{hand(300,380,1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)">
  <path d="M190 210l40 20M410 210l-40 20M300 348v-30"/>
</g>
""", ground=False, arrow=True)

add('irony', '晴れの予報なのに雨に降られる皮肉なイラスト。', f"""
<g transform="translate(180 150)">
  <path d="M-90-70h180v140h-180z" class="paper"/>
  <circle r="34" class="goldp o"/>
  <g class="golds"><path d="M0-50v-14M0 50v14M-50 0h-14M50 0h14"/></g>
</g>
{cloud(430,120,1.4,'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
  {''.join(f'<path d="M{360+i*30} {190+(i%2)*14}l-10 40"/>' for i in range(6))}
</g>
{person(430,352,1.05,1,'coral','blue','stand','short','neutral')}
{xx(300,240,0.8)}
<path d="M60 376h480" class="a"/>
""", ground=True)

add('isolation', '仲間から離れてひとりだけになるイラスト。', f"""
{person(180,340,0.8,1,'teal','blue','stand','short','smile')}
{person(250,340,0.8,1,'gold','blue','stand','bob','smile')}
{person(320,340,0.8,-1,'green','violet','stand','short','smile')}
{person(510,346,1,-1,'coral','gold','stand','bun','sad')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><circle cx="250" cy="250" r="130"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><circle cx="510" cy="250" r="70"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('jealousy', '人が得たものをうらやんでねたむイラスト。', f"""
{person(450,352,1.15,-1,'gold','blue','up','bob','smile')}
<g transform="translate(450 180)">
  <path d="M0-40l16 34 38 4-28 26 8 38-34-20-34 20 8-38-28-26 38-4z" class="gold o"/>
</g>
{person(170,352,1.15,1,'green','blue','stand','short','sad')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M110 190l-16-22M230 186v-24"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M240 250h130"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('joint', '二つの部材をつなぎ合わせた継ぎ目のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-230-40h240v80h-240z" class="teal o"/>
  <path d="M-10-40h240v80H-10z" class="coral o"/>
  <path d="M-40-60h80v120h-80z" class="goldp o"/>
  <circle cx="0" cy="-24" r="12" class="goldd o"/>
  <circle cx="0" cy="24" r="12" class="goldd o"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('journal', '研究をまとめた専門誌のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-160-140h320v280h-320z" class="paper"/>
  <path d="M-160-140h320v50h-320z" class="teal o"/>
  <path d="M-160-90h34v230h-34z" class="teald o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">
    {''.join(f'<path d="M-96 {-50+i*34}h230"/>' for i in range(6))}
  </g>
  <path d="M-96 116h150" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<g class="teal o"><rect x="470" y="130" width="30" height="40" rx="4"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
