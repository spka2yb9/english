"""第103回: 機能語・副詞を図式で45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'
def qmark(x,y,s=1,cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-24-26q0-28 26-28t26 26q0 22-26 28v12" fill="none" stroke="{TONES[cls][0]}" stroke-width="10" stroke-linecap="round"/>'
            f'<circle cy="36" r="7" class="{cls}"/></g>')
def clock(x,y,r=60):
    return (f'<g transform="translate({x} {y})"><circle r="{r}" fill="#fffdf6" class="o"/>'
            f'<path d="M0 0v-{r*0.6:.0f}" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M0 0l{r*0.45:.0f} {r*0.28:.0f}" fill="none" stroke="{TONES["coral"][0]}" stroke-width="5" stroke-linecap="round"/>'
            f'<circle r="6" class="ink"/></g>')

add('have', '自分のものとして持っているイラスト。', f"""
{person(200,352,1.25,1,'teal','blue','carry','short','smile')}
{box(400,300,140,100,28,'gold')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="12 10"><rect x="110" y="190" width="420" height="180" rx="24"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('might', 'そうなるかもしれないと示すイラスト。', f"""
{person(160,352,1.2,1,'teal','blue','think','short','neutral')}
<g opacity="0.45">
  <circle cx="440" cy="220" r="70" class="tealp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M240 260h120"/></g>
{qmark(330,150,1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('please', '手を合わせてていねいに頼むイラスト。', f"""
{person(220,352,1.3,1,'teal','blue','hold','short','smile')}
{hand(430,250,-1)}
<g transform="translate(340 300)">
  <path d="M-40-26h80v52h-80z" class="goldp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M300 200h60"/></g>
{ck(180,200,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('shall', '「やりましょうか」と申し出るイラスト。', f"""
{person(180,352,1.25,1,'teal','blue','up','short','smile')}
<g transform="translate(400 290)">
  <path d="M-80-30h160v80h-160z" class="goldd o"/>
  <path d="M-80-30q80-40 160 0z" class="gold o"/>
</g>
{qmark(300,170,1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M250 280h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('ah', '「ああ」と思い当たるイラスト。', f"""
{person(250,352,1.35,1,'coral','blue','point','short','surprised')}
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2.5">
  <path d="M420 130h32l-8 110h-16zM436 272a16 16 0 1 0 0 32 16 16 0 1 0 0-32z"/>
</g>
<g class="golds"><path d="M340 160l-20-20M500 160l20-20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('as', '箱をいすの代わりに使うイラスト。', f"""
{sit(300,352,1.3,1,'teal','blue','short','smile','down')}
{box(320,356,160,80,0,'gold')}
<g opacity="0.4">{chair(320,356,1.2,'gold',1)}</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M480 250h50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('can', '重い物を持ち上げられるイラスト。', f"""
{person(260,352,1.3,1,'teal','blue','up','short','smile')}
{box(260,180,190,90,30,'gold')}
{ck(470,200,1.2)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('mine', '自分のものだと指し示すイラスト。', f"""
{person(200,352,1.25,1,'teal','blue','point','short','smile')}
{box(400,300,130,90,26,'coral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10"><rect x="110" y="190" width="420" height="180" rx="24"/></g>
<g class="a" marker-end="url(#ar)"><path d="M280 250h50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('none', 'ひとつも残っていないイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-140-120h280v240h-280z" fill="#fffdf6" class="o"/>
</g>
{xx(300,250,2.2,MUTED)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M140 380h320M140 380v-24M460 380v-24"/></g>
""", ground=False)

add('neither', 'どちらでもないことを示すイラスト。', f"""
<g transform="translate(180 240)">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
</g>
<g transform="translate(450 240)">
  <path d="M-80-80h160v160h-160z" class="coralp o"/>
</g>
{xx(180,240,1.6)}
{xx(450,240,1.6)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('since', 'その時からずっと続いているイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M120 250h420"/></g>
<circle cx="140" cy="250" r="24" class="coral o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="12" stroke-linecap="round"><path d="M140 250h340"/></g>
{clock(480,140,54)}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M140 290v40M480 200v30"/></g>
""", ground=False, arrow=True)

add('while', '同じ時間に重なって続くイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-220-60h300v50h-300z" class="teal o"/>
  <path d="M-80 20h300v50h-300z" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M220 120v220M380 120v220"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" marker-end="url(#ar)"><path d="M300 360h-80M300 360h80"/></g>
""", ground=False, arrow=True)

add('whose', 'これはだれのものかをたずねるイラスト。', f"""
{box(300,250,140,100,28,'gold')}
{person(120,352,0.95,1,'teal','blue','stand','short','neutral')}
{person(480,352,0.95,-1,'coral','gold','stand','bob','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)">
  <path d="M240 300h-70M360 300h70"/>
</g>
{qmark(300,120,1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('yet', 'まだ終わっていないことを示すイラスト。', f"""
<g transform="translate(240 220)">
  <path d="M-130-140h260v280h-260z" class="paper"/>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="3">{''.join(f'<rect x="-100" y="{-100+i*56}" width="30" height="30"/>' for i in range(4))}</g>
  <g fill="none" stroke="{GRN}" stroke-width="6"><path d="M-94-88l8 10 18-22M-94-32l8 10 18-22"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-50 {-86+i*56}h150"/>' for i in range(4))}</g>
</g>
{clock(470,300,60)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('yours', 'それは相手のものだと示すイラスト。', f"""
{person(150,352,1.2,1,'teal','blue','point','short','smile')}
{box(330,300,130,90,26,'coral')}
{person(500,352,1.2,-1,'coral','gold','reach','bob','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10"><rect x="260" y="200" width="300" height="170" rx="24"/></g>
<g class="a" marker-end="url(#ar)"><path d="M230 240h70"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('all', 'ひとつ残らず全部を示すイラスト。', f"""
<g class="teal o">
  {''.join(f'<circle cx="{140+c*80}" cy="{170+r*70}" r="28"/>' for r in range(3) for c in range(5))}
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="14 12"><rect x="80" y="120" width="440" height="220" rx="30"/></g>
{ck(300,376,0.9)}
""", ground=False)

add('although', '一方はこうだが結びはこうと示すイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-100-100h200v200h-200z" class="tealp o"/>
</g>
{xx(170,230,1.2,MUTED)}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M290 300q60 60 140 0"/></g>
<g transform="translate(460 230)">
  <path d="M-90-100h180v200h-180z" class="coralp o"/>
</g>
{ck(460,230,1.2)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('any', 'どれでもよいので一つ取るイラスト。', f"""
<g class="tealp o">
  {''.join(f'<circle cx="{140+c*80}" cy="{200+r*80}" r="30"/>' for r in range(2) for c in range(5))}
</g>
{hand(300,120,1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M300 170v20"/></g>
{ck(300,370,0.8)}
""", ground=False, arrow=True)

add('anyway', '事情があってもとにかく進むイラスト。', f"""
{person(160,352,1.2,1,'teal','blue','walk','short','neutral')}
<g transform="translate(330 300)">
  <path d="M-90 60q-20-70 10-100 50-40 110-10 50 24 30 110z" fill="#8b98a6" class="o"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="7" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M230 200q100-70 250 40"/></g>
{xx(330,150,0.8,MUTED)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('onto', '上の面へ移し乗せるイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-180-30h360v30h-360z" fill="#b9c2c9" class="o"/>
  <path d="M-140 0v60M140 0v60" class="a"/>
</g>
{box(300,240,120,80,24,'gold')}
<g class="a" marker-end="url(#ar)"><path d="M140 160q60 60 140 60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('though', 'そうではあるがと言い添えるイラスト。', f"""
<g transform="translate(230 220)">
  <path d="M-150-110h300v220h-300z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="6"><path d="M-100-50h200M-100 0h150"/></g>
</g>
<g transform="translate(470 300)">
  <path d="M-80-50h160v100h-160z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="5"><path d="M-50-16h100M-50 12h70"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M390 240q30 40 0 50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('now', 'ちょうど今この時を指すイラスト。', f"""
{clock(300,210,140)}
<g class="a" marker-end="url(#ar)"><path d="M300 390v-30"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"><circle cx="300" cy="210" r="170"/></g>
""", ground=False, arrow=True)

add('obviously', '見ればすぐ分かるほど明らかなイラスト。', f"""
<g transform="translate(330 230)">
  <path d="M-130-130h260v260h-260z" class="coral o"/>
</g>
<g transform="translate(130 220)">
  <ellipse rx="60" ry="36" fill="#fffdf6" class="o"/>
  <circle r="24" class="blue o"/><circle r="10" class="ink"/>
</g>
{ck(480,120,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('once', 'たった一度だけ起きたことを示すイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M60 250h480"/></g>
<circle cx="300" cy="250" r="20" class="coral o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M300 220v-60"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 10"><path d="M70 310h460"/></g>
<g fill="{TONES['coral'][0]}"><rect x="290" y="120" width="20" height="40" rx="10"/></g>
""", ground=False, arrow=True)

add('originally', 'もとは違う形だったと示すイラスト。', f"""
<g transform="translate(160 230)">
  <path d="M-100-100h200v200h-200z" fill="#e9f2f7" class="o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-dasharray="8 8"><rect x="-60" y="-60" width="120" height="120"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 230h60"/></g>
<g transform="translate(460 230)">
  <circle r="90" class="teal o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M160 370v-30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('particularly', '細かいところを取り上げて示すイラスト。', f"""
<g transform="translate(240 220)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-130 {-100+i*44}h260"/>' for i in range(5))}</g>
</g>
<g transform="translate(370 250)">
  <circle r="90" fill="none" stroke="{INK}" stroke-width="10"/>
  <circle r="78" fill="#fffdf6" opacity="0.4"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M-50-10h100M-50 20h70"/></g>
  <path d="M64 64l54 54" fill="none" stroke="{INK}" stroke-width="15" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('passing', '目の前を通りすぎていくイラスト。', f"""
{person(340,352,1.2,1,'teal','blue','walk','short','neutral')}
<g transform="translate(150 300)">
  <path d="M-10-90h20v150h-20z" class="ink"/>
  <circle cy="-100" r="16" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M200 260h330"/></g>
<g opacity="0.35">{person(230,352,1.2,1,'teal','blue','walk','short','neutral')}</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('perfectly', '型にぴたりとはまって申し分ないイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-140-120h280v240h-280z" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
  <path d="M-134-114h268v228h-268z" class="teal o"/>
</g>
{ck(300,370,1)}
{ck(500,140,0.8)}
""", ground=False)

add('personally', '自分としてはこう思うと示すイラスト。', f"""
{person(190,352,1.25,1,'teal','blue','point','short','neutral')}
<g transform="translate(420 200)">
  <path d="M-120-80h240v130h-240zM-80 50l-14 34 44-34z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"><path d="M-80-40h160M-80-10h120"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M240 280q-30 40-60 20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('possibly', 'ひょっとしたらそうかもしれないイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M120 300h140"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M280 290q80-70 180-100"/></g>
<g opacity="0.4"><circle cx="490" cy="170" r="56" class="tealp o"/></g>
{qmark(340,120,1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('previously', 'これより前の時点を指すイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M60 250h480"/></g>
<g class="ink">{''.join(f'<circle cx="{140+i*90}" cy="250" r="9"/>' for i in range(5))}</g>
<circle cx="230" cy="250" r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
<circle cx="410" cy="250" r="14" class="teal o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M390 330H250"/></g>
""", ground=False, arrow=True)

add('properly', '正しい向きにきちんと付けるイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-80-70h160v140h-160z" class="tealp o"/>
  <path d="M-40-30h80v60h-80z" class="teal o"/>
</g>
{ck(170,360,0.9)}
<g transform="translate(450 240)">
  <path d="M-80-70h160v140h-160z" class="tealp o"/>
  <path d="M-40-30h80v60h-80z" class="teal o" transform="rotate(24 0 0) translate(30 20)"/>
</g>
{xx(450,360,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('recently', 'ここ数日のうちの出来事を指すイラスト。', f"""
<g transform="translate(280 200)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <path d="M-200-140h400v46h-400z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M-200 {-50+i*48}h400"/>' for i in range(4))}
    {''.join(f'<path d="M{-143+c*57} -94v234"/>' for c in range(6))}
  </g>
  <circle cx="143" cy="110" r="22" class="coral o"/>
  <g class="coralp o"><circle cx="86" cy="110" r="18"/><circle cx="29" cy="110" r="18"/></g>
</g>
{clock(520,320,54)}
""", ground=False)

add('regularly', '等しい間で決まって起きるイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M60 250h480"/></g>
<g class="coral">{''.join(f'<circle cx="{120+i*80}" cy="250" r="13"/>' for i in range(6))}</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4">{''.join(f'<path d="M{120+i*80} 228v-40"/>' for i in range(6))}</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)">{''.join(f'<path d="M{128+i*80} 320h64"/>' for i in range(5))}</g>
""", ground=False, arrow=True)

add('seriously', '重く受け止めてまじめに向き合うイラスト。', f"""
{face(200,220,90,'flat')}
<g fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"><path d="M150 176q24-14 46 0M214 176q24-14 46 0"/></g>
{box(450,240,150,80,0,'gold')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M450 300v50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('simply', '込み入ったものを単純にするイラスト。', f"""
<g transform="translate(160 240)">
  <g class="tealp o">{''.join(f'<rect x="{-70+(i%3)*50}" y="{-70+(i//3)*50}" width="40" height="40"/>' for i in range(9))}</g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 240h60"/></g>
<g transform="translate(460 240)">
  <path d="M-60-60h120v120h-120z" class="teal o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('skip', '途中のひとつを飛ばして進むイラスト。', f"""
<g transform="translate(300 280)">
  <g class="tealp o">{''.join(f'<circle cx="{-200+i*80}" cy="0" r="30"/>' for i in range(6))}</g>
  <circle cx="-40" cy="0" r="30" fill="#fffaf1" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M190 250q70-90 150 0"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('slightly', 'ほんの少しだけずれているイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-200-20h400v6h-400z" fill="{MUTED}"/>
  <path d="M-200 10h400v6h-400z" class="teal"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M480 190v34M480 300v-34"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M440 220h80M440 256h80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('stand', 'いすから立ち上がるイラスト。', f"""
{chair(170,356,1.1,'gold',1)}
<g opacity="0.4">{sit(160,352,1.1,1,'teal','blue','short','neutral','down')}</g>
{person(420,352,1.3,1,'teal','blue','stand','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M270 260q60-60 110-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('strongly', '太い矢印で強く押し出すイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="5" marker-end="url(#ar)"><path d="M120 320h100"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="34" stroke-linecap="round" marker-end="url(#ar)"><path d="M120 180h320"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('successfully', 'ねらいどおりやり遂げたイラスト。', f"""
{person(180,352,1.2,1,'coral','blue','up','short','smile')}
<g transform="translate(460 250)">
  <path d="M-6 106V-70" class="a"/>
  <path d="M-6-70h90l-18 26 18 26H-6z" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M250 300h150"/></g>
{ck(320,160,1.1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('suddenly', '前ぶれなくふいに起きるイラスト。', f"""
{person(160,352,1.15,1,'teal','blue','walk','short','surprised')}
<g transform="translate(400 230)">
  <path d="M0-140l36 66 72-22-26 70 66 36-66 36 26 70-72-22-36 66-36-66-72 22 26-70-66-36 66-36-26-70 72 22z" class="coralp o"/>
</g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2.5">
  <path d="M400 150l-40 80h34l-20 66 60-92h-40l26-54z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('surely', '目盛りが振り切れるほど確かなイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-160 0a160 160 0 0 1 320 0z" fill="#fffdf6" class="o"/>
  <path d="M-160 0h320" class="a"/>
  <path d="M60-148A160 160 0 0 1 160 0h-100z" class="greenp"/>
  <path d="M0 0l150-40" fill="none" stroke="{GRN}" stroke-width="10" stroke-linecap="round"/>
  <circle r="11" class="ink"/>
</g>
{ck(500,140,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tend', '毎回同じ方へかたむくイラスト。', f"""
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" marker-end="url(#ar)">
  <path d="M120 140h160M120 210h190M120 280h150M120 350h180"/>
</g>
<g transform="translate(450 240)">
  <path d="M-40-100h80v200h-80z" class="tealp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('that', '離れたあれを指すイラスト。', f"""
{person(150,352,1.25,1,'teal','blue','point','short','neutral')}
<g transform="translate(480 250)">
  <path d="M-50-50h100v100h-100z" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M230 250h180"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

print(len(W), ' '.join(W))
print(sheet(W))
