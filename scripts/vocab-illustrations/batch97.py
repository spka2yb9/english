"""第97回: 副詞・動詞中心の45語。"""
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

add('fishing', '網で魚をとる漁のイラスト。', f"""
<path d="M0 300h600v100H0z" class="bluep"/>
<g transform="translate(300 300)">
  <path d="M-150 0h300l-40 50h-220z" class="coral o"/>
  <path d="M-60-70h120v70h-120z" fill="#fffdf6" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3">
  {''.join(f'<path d="M{170+i*30} 340l14 50"/>' for i in range(8))}
  {''.join(f'<path d="M{160+i*40} {350+i*8}h280"/>' for i in range(3))}
</g>
<g class="teal o"><ellipse cx="240" cy="378" rx="24" ry="12"/><ellipse cx="330" cy="368" rx="20" ry="10"/></g>
""", ground=False)

add('formerly', '以前の看板が新しいものに変わったイラスト。', f"""
<g transform="translate(160 240)" opacity="0.45">
  <path d="M-90-70h180v140h-180z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="8"><path d="M-56-20h112M-56 20h80"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 240h60"/></g>
<g transform="translate(450 240)">
  <path d="M-90-70h180v140h-180z" class="coral o"/>
  <g fill="none" stroke="#fffdf6" stroke-width="8"><path d="M-56-20h112M-56 20h80"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M160 340v-30M450 340v-30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('forth', '戸口から外へ踏み出すイラスト。', f"""
<g transform="translate(150 230)">
  <path d="M-120-150h240v300h-240z" fill="#dfe6ea" class="o"/>
  <path d="M-60-110h180v260H-60z" fill="#fffaf1" class="o"/>
  <circle cx="90" cy="20" r="8" class="ink"/>
</g>
{person(400,352,1.2,1,'teal','blue','walk','short','smile')}
<g class="a" marker-end="url(#ar)"><path d="M300 250h120"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('freely', 'さえぎるものがなく自由に動けるイラスト。', f"""
<g transform="translate(160 250)">
  <path d="M-70 100v-130q0-60 70-60t70 60v130" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M14-30h60v130h-60z" fill="#fffaf1"/>
  <path d="M14-30v130M74-30v130" class="a"/>
</g>
<g transform="translate(430 170)">
  <ellipse rx="46" ry="30" class="gold o"/>
  <circle cx="40" cy="-20" r="20" class="gold o"/>
  <path d="M56-24l26 8-26 10z" class="coral o"/>
  <circle cx="46" cy="-26" r="4" class="ink"/>
  <path d="M-10-24q30-50 60-14-30 20-60 14z" class="goldp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9" marker-end="url(#ar)"><path d="M260 240q60-70 130-80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('fully', 'ふちまでいっぱいに満たすイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-110-130h220v260h-220z" fill="#fffdf6" class="o"/>
  <path d="M-110-120h220v250h-220z" class="teal o"/>
  <path d="M-130-124h260v10h-260z" class="coral o"/>
</g>
{ck(490,150,1.1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('gain', '努力して手にする分が増えるイラスト。', f"""
<g transform="translate(300 250)">
  <g class="teal o">{''.join(f'<rect x="{-200+i*70}" y="{60-(30+i*35)}" width="50" height="{30+i*35}"/>' for i in range(5))}</g>
  <path d="M-210 60h420" class="a"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"><path d="M500 150h60M530 120v60"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M110 260q180-100 380-120"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('govern', '定めにもとづいて国を治めるイラスト。', f"""
{building(190,290,0.8,'violet')}
<g transform="translate(430 230)">
  <path d="M-100-110h200v220h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-66 {-60+i*44}h132"/>' for i in range(4))}</g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M300 160h30"/></g>
{person(190,190,0.6,1,'violet','violet','point','short','neutral')}
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('greatly', '程度がぐんと大きくなるイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="6" marker-end="url(#ar)"><path d="M120 300h60"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="22" stroke-linecap="round" marker-end="url(#ar)"><path d="M120 180h360"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M180 340v-30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('halfway', '道のちょうど半分まで来たイラスト。', f"""
<path d="M60 330h480v40H60z" fill="#dfe6ea" class="o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M300 300v-60"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M300 200h-200M300 200h200"/></g>
{person(300,330,1.05,1,'teal','blue','walk','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M100 300v-40M500 300v-40"/></g>
""", ground=False, arrow=True)

add('highly', '目盛りが上の方まで振れるイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-150 0a150 150 0 0 1 300 0z" fill="#fffdf6" class="o"/>
  <path d="M-150 0h300" class="a"/>
  <path d="M0 0l120-70" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"/>
  <circle r="10" class="ink"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M{-130+i*65} -40v-20"/>' for i in range(5))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M500 300V190"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('illegal', '法に反して許されないイラスト。', f"""
<g transform="translate(230 220)">
  <path d="M-120-140h240v280h-240z" class="paper"/>
  <path d="M-90-110h180v40h-180z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-90 {-30+i*44}h180"/>' for i in range(4))}</g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="9">
  <circle cx="450" cy="250" r="34"/><circle cx="520" cy="270" r="34"/>
</g>
{xx(430,130,1.2)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('imply', '口にはせずほのめかすイラスト。', f"""
{person(150,352,1.2,1,'teal','blue','point','short','neutral')}
<g transform="translate(330 180)">
  <path d="M-80-50h160v80h-160zM-50 30l-12 26 34-26z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="6"><path d="M-50-20h100M-50 4h70"/></g>
</g>
<g transform="translate(480 300)">
  <path d="M-90-50q-6-32 26-36 12-26 40-16 22-4 26 20 26 4 22 28-4 22-26 22h-60q-24-2-28-18z" class="bluep o"/>
  <g fill="none" stroke="{TONES['blue'][2]}" stroke-width="5"><path d="M-56-18h100M-56 0h70"/></g>
</g>
<g class="o" fill="#e1edfb"><circle cx="400" cy="256" r="12"/><circle cx="382" cy="230" r="8"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('increasingly', 'だんだん度が増していくイラスト。', f"""
<g transform="translate(300 250)">
  <g class="coral o">{''.join(f'<rect x="{-220+i*62}" y="{60-(16+i*26)}" width="44" height="{16+i*26}"/>' for i in range(7))}</g>
  <path d="M-230 60h460" class="a"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M100 290q200-110 420-160"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('infer', '手がかりから答えを導き出すイラスト。', f"""
<g transform="translate(180 210)">
  <path d="M-120-110h240v220h-240z" class="paper"/>
  <g class="ink" opacity="0.6"><ellipse cx="-60" cy="-40" rx="22" ry="13" transform="rotate(-20 -60 -40)"/><ellipse cx="10" cy="0" rx="22" ry="13" transform="rotate(-20 10 0)"/><ellipse cx="70" cy="50" rx="22" ry="13" transform="rotate(-20 70 50)"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M320 210h60"/></g>
<g transform="translate(470 210)">
  <path d="M0-70q46 0 46 44 0 26-20 38v18h-52v-18q-20-12-20-38 0-44 46-44z" class="gold o"/>
  <path d="M-26 34h52v16h-52z" class="goldd o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('initially', 'いちばん初めの時点を示すイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M60 250h480"/></g>
<g class="ink">{''.join(f'<circle cx="{140+i*90}" cy="250" r="10"/>' for i in range(5))}</g>
<circle cx="140" cy="250" r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M140 350v-70"/></g>
""", ground=False, arrow=True)

add('instantly', '合図と同時にすぐ動くイラスト。', f"""
<g transform="translate(170 210)">
  <circle r="90" fill="#fffdf6" class="o"/>
  <path d="M-16-104h32v20h-32z" class="ink"/>
  <path d="M0 0v-64" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"/>
  <circle r="8" class="ink"/>
</g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2.5">
  <path d="M330 110l-54 110h44l-24 90 76-120h-48l26-80z"/>
</g>
{person(500,352,1.15,1,'teal','blue','walk','short','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('integrate', '別々のものをひとつにまとめ合わせるイラスト。', f"""
<g transform="translate(150 240)">
  <circle cx="-40" cy="-30" r="40" class="tealp o"/>
  <path d="M10-20h70v70H10z" class="coralp o"/>
  <path d="M-70 40l50-30 40 60z" class="goldp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 240h60"/></g>
<g transform="translate(460 240)">
  <circle r="90" class="tealp o"/>
  <circle cx="-30" cy="-20" r="30" class="teal o"/>
  <path d="M10-10h50v50H10z" class="coral o"/>
  <path d="M-50 34l36-22 28 44z" class="gold o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('intensify', 'つまみを回して強さを増すイラスト。', f"""
<g transform="translate(190 240)">
  <circle r="80" fill="#fffdf6" class="o"/>
  <path d="M0 0l56-56" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"/>
  <circle r="12" class="ink"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M0 -92v-14" transform="rotate({-90+i*45})"/>' for i in range(5))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M330 220q20 20 0 40M370 190q44 50 0 100M410 160q70 80 0 160"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M200 130a70 70 0 0 1 60 30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('justify', 'そうした理由を示して正しいと認めさせるイラスト。', f"""
{person(160,352,1.2,1,'teal','blue','point','short','neutral')}
<g transform="translate(340 220)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-56-50h112M-56-20h112M-56 10h80"/></g>
  <g fill="none" stroke="{GRN}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"><path d="M-40 50l20 24 46-54"/></g>
</g>
{person(510,352,1.05,-1,'coral','gold','stand','bob','smile')}
<g class="a" marker-end="url(#ar)"><path d="M250 300h50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('lady', '帽子をかぶった女性のイラスト。', f"""
{person(300,352,1.4,1,'violet','violet','stand','bun','smile')}
<g transform="translate(300 196)">
  <ellipse rx="70" ry="16" class="coral o"/>
  <path d="M-34-4q34-40 68 0z" class="corald o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('law', 'てんびんと法典で表す法のイラスト。', f"""
<g transform="translate(200 230)">
  <path d="M-110-140h220v280h-220z" class="violet o"/>
  <path d="M-90-120h180v240h-180z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-56 {-60+i*44}h112"/>' for i in range(4))}</g>
</g>
<g transform="translate(440 200)">
  <path d="M-8-60h16v170h-16z" class="ink"/>
  <path d="M-60 110h120v20H-60z" class="ink"/>
  <path d="M-100-56h200v12h-200z" class="ink"/>
  <path d="M-100-44v30M100-44v30" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-140-14h80q0 34-40 34t-40-34z" class="goldp o"/>
  <path d="M60-14h80q0 34-40 34t-40-34z" class="goldp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('legal', '法にかなって認められるイラスト。', f"""
<g transform="translate(260 220)">
  <path d="M-140-140h280v280h-280z" class="paper"/>
  <path d="M-110-110h220v40h-220z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-110 {-30+i*44}h220"/>' for i in range(3))}</g>
  <g fill="none" stroke="{GRN}" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"><path d="M-50 90l24 28 56-64"/></g>
</g>
<g transform="translate(490 210)">
  <path d="M-8-60h16v130h-16z" class="ink"/>
  <path d="M-50 70h100v16H-50z" class="ink"/>
  <path d="M-70-56h140v10H-70z" class="ink"/>
  <path d="M-94-14h60q0 26-30 26t-30-26z" class="goldp o"/>
  <path d="M34-14h60q0 26-30 26t-30-26z" class="goldp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('likewise', '同じようにもう一方も行うイラスト。', f"""
{person(180,352,1.2,1,'teal','blue','up','short','smile')}
{person(420,352,1.2,1,'coral','gold','up','bob','smile')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="9"><path d="M270 210h60M270 250h60"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('male', '男性であることを示す記号のイラスト。', f"""
{person(180,352,1.35,1,'blue','blue','stand','short','smile')}
<g transform="translate(410 240)">
  <circle cy="40" r="76" fill="none" stroke="{TONES['blue'][0]}" stroke-width="20"/>
  <path d="M44-16l70-70M70-90h50v50" fill="none" stroke="{TONES['blue'][0]}" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('maximize', 'いっぱいまで大きく広げるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-240-160h480v320h-480z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="14 12"/>
  <path d="M-230-150h460v300h-460z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round" marker-end="url(#ar)">
  <path d="M300 220L120 90M300 220l180-130M300 220L120 350M300 220l180 130"/>
</g>
""", ground=False, arrow=True)

add('merely', 'ただそれだけしかないイラスト。', f"""
<g transform="translate(300 230)">
  <circle r="40" class="teal o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M220 320h160M220 320v-24M380 320v-24"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><rect x="120" y="120" width="360" height="220" rx="20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('method', '手順が番号順に書かれたやり方のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-190-150h380v300h-380z" class="paper"/>
  <g class="tealp o">{''.join(f'<circle cx="-150" cy="{-90+i*60}" r="20"/>' for i in range(4))}</g>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-114 {-90+i*60}h260"/>' for i in range(4))}</g>
</g>
<g transform="translate(510 330) rotate(26)">
  <path d="M-8-40h16v80h-16z" fill="{MUTED}" class="o"/>
  <path d="M-18-52h36v20h-36z" fill="{MUTED}" class="o"/>
</g>
""", ground=False)

add('nature', '山と川と生き物のある自然のイラスト。', f"""
<path d="M0 0h600v240H0z" fill="#e6f0fb"/>
{sun(510,80,40)}
<path d="M0 240l150-140 110 110 90-80 250 110z" class="greenp o"/>
<path d="M150 100l50 46-100 0z" fill="#fffdf6" class="o"/>
<path d="M0 240h600v160H0z" class="green o"/>
<path d="M60 400q80-100 240-90t300 40" fill="{TONES['blue'][1]}" stroke="{INK}" stroke-width="3"/>
{tree(110,330,1)}
{tree(500,350,1.1)}
<g fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"><path d="M300 130q20-20 40 0M300 130q-20-20-40 0"/></g>
""", ground=False)

add('newly', 'おろしたての新しい品のイラスト。', f"""
{box(280,260,190,130,36,'teal')}
{star(470,140,34,'gold')}
<g class="golds"><path d="M150 150l-20-22M300 110V88"/></g>
<g transform="translate(430 330)">
  <path d="M-60-24h90l30 24-30 24h-90z" class="coralp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('notably', '大勢の中でひときわ目立つイラスト。', f"""
<path d="M300 60l130 300H170z" fill="{TONES['gold'][1]}" opacity="0.7"/>
{person(300,346,1.2,1,'coral','blue','up','short','smile')}
{person(120,356,0.8,1,'teal','blue','stand','short','neutral')}
{person(200,356,0.8,1,'teal','blue','stand','bob','neutral')}
{person(410,356,0.8,-1,'teal','blue','stand','short','neutral')}
{person(490,356,0.8,-1,'teal','blue','stand','bun','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('nowadays', '昔と違って今はこうだと示すイラスト。', f"""
<g transform="translate(150 240)" opacity="0.5">
  <path d="M-70-70h140v140h-140z" fill="#dfe6ea" class="o"/>
  <path d="M-40-30h80v70h-80z" fill="{MUTED}"/>
  <path d="M0-30v-30" fill="none" stroke="{MUTED}" stroke-width="5"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 240h60"/></g>
<g transform="translate(450 240)">
  <path d="M-60-100h120v200h-120z" class="ink"/>
  <path d="M-48-88h96v170h-96z" fill="{TONES['blue'][1]}"/>
  <g class="teal o"><rect x="-32" y="-70" width="30" height="30" rx="8"/><rect x="2" y="-70" width="30" height="30" rx="8"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('occasionally', 'ときどきしか起こらないイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M60 250h480"/></g>
<g class="coral">{''.join(f'<circle cx="{x}" cy="250" r="13"/>' for x in (140,300,470))}</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4">{''.join(f'<path d="M{x} 230v-50"/>' for x in (140,300,470))}</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 10"><path d="M70 320h460"/></g>
""", ground=False, arrow=True)

add('openly', '隠さずおおっぴらに見せるイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-160 100V-30q0-40 160-40t160 40v130z" class="teal o"/>
  <path d="M-160-30q0-40 160-40t160 40" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-130 100V-10h260v110z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="6"><path d="M-90 30h180M-90 60h140"/></g>
</g>
<g transform="translate(300 100)">
  <path d="M-160-30q60-40 160-40t160 40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"/>
</g>
{ck(500,140,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('organized', 'きちんと分けて片づけられたイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-90-110h180v220h-180z" fill="#fffdf6" class="o"/>
  <g class="goldp o"><path d="M-70-30l40-16 14 40-40 16zM10 20l40 16-14 36-40-16z"/></g>
  <g class="tealp o"><circle cx="30" cy="-50" r="24"/></g>
</g>
{xx(160,130,0.8,MUTED)}
<g class="a" marker-end="url(#ar)"><path d="M290 240h60"/></g>
<g transform="translate(460 240)">
  <path d="M-90-110h180v220h-180z" fill="#fffdf6" class="o"/>
  <path d="M-90-30h180M-90 40h180M0-110v220" class="a"/>
  <g class="goldp o"><rect x="-70" y="-90" width="50" height="50"/><rect x="20" y="-90" width="50" height="50"/></g>
  <g class="tealp o"><rect x="-70" y="-20" width="50" height="50"/><rect x="20" y="-20" width="50" height="50"/></g>
  <g class="coralp o"><rect x="-70" y="50" width="50" height="50"/><rect x="20" y="50" width="50" height="50"/></g>
</g>
{ck(460,130,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('otherwise', 'そうでなければ別の道になるイラスト。', f"""
<g transform="translate(180 210)">
  <path d="M-100-70h200v140h-200z" class="tealp o"/>
  <g fill="none" stroke="{GRN}" stroke-width="9"><path d="M-40 0l20 24 46-54"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)">
  <path d="M300 210h80"/>
</g>
<g transform="translate(470 210)">
  <path d="M-90-70h180v140h-180z" class="coralp o"/>
</g>
{xx(180,330,0.8)}
{ck(470,330,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('overly', '度を越して行き過ぎたイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-160 0a160 160 0 0 1 320 0z" fill="#fffdf6" class="o"/>
  <path d="M-160 0h320" class="a"/>
  <path d="M80-139A160 160 0 0 1 160 0h-80z" class="coralp"/>
  <path d="M0 0l150-50" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"/>
  <circle r="11" class="ink"/>
</g>
{xx(500,160,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('overnight', '一晩のうちに変わるイラスト。', f"""
<g transform="translate(160 200)">
  <path d="M-110-120h220v240h-220z" fill="#1f2b3d" class="o"/>
  <path d="M20-70a40 40 0 1 0 30 60 46 46 0 1 1-30-60z" class="gold o"/>
  <g fill="#fffdf6"><circle cx="-60" cy="-70" r="3"/><circle cx="-30" cy="-30" r="3"/><circle cx="-70" cy="20" r="3"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 200h60"/></g>
<g transform="translate(460 200)">
  <path d="M-110-120h220v240h-220z" fill="#e6f0fb" class="o"/>
</g>
{sun(460,180,40)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('oversee', '高い所から作業全体を見わたすイラスト。', f"""
<g transform="translate(150 200)">
  <path d="M-90 190v-40h180v40z" class="goldd o"/>
  <path d="M-90 150h180v-16h-180z" class="gold o"/>
</g>
{person(150,340,1.05,1,'violet','blue','point','bun','neutral')}
{person(400,376,0.8,1,'teal','blue','reach','cap','neutral')}
{person(510,376,0.8,1,'gold','violet','reach','short','neutral')}
{box(460,330,80,50,14,'gold')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M230 280l150 60"/></g>
<path d="M60 390h480" class="a"/>
""", ground=True)

add('partially', '一部だけ満ちているイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-220-60h440v120h-440z" fill="#fffdf6" class="o"/>
  <path d="M-220-60h180v120h-180z" class="teal o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M80 350h50M180 350h-50"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M80 330v40M180 330v40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('partly', '全体のうちの一部を示すイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="150" class="tealp o"/>
  <path d="M0 0v-150A150 150 0 0 1 130 75z" class="teal o"/>
  <g fill="none" stroke="{INK}" stroke-width="2.5"><path d="M0 0v-150M0 0l130 75"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M540 130l-70 50"/></g>
""", ground=False, arrow=True)

add('permanently', 'ボルトで固めてずっと変わらないイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-160-60h320v120h-320z" fill="#b9c2c9" class="o"/>
  <g class="goldd o"><circle cx="-120" cy="0" r="18"/><circle cx="0" cy="0" r="18"/><circle cx="120" cy="0" r="18"/></g>
  <path d="M-180 60h360v30h-360z" fill="{MUTED}" class="o"/>
</g>
<g transform="translate(300 130)">
  <path d="M0 0q-24-40-56-40T-112 0q0 40 56 40T0 0q24-40 56-40T112 0q0 40-56 40T0 0z" fill="none" stroke="{TONES['teal'][0]}" stroke-width="12" stroke-linejoin="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('political', '演壇で国の方針を論じる政治のイラスト。', f"""
{person(230,352,1.25,1,'violet','blue','point','short','neutral')}
<g transform="translate(230 330)">
  <path d="M-60-40h120l16 60h-152z" class="goldd o"/>
</g>
<g transform="translate(450 250)">
  <path d="M-6 130V-110" class="a"/>
  <path d="M-6-110h100v70H-6z" class="coral o"/>
</g>
{person(520,356,0.75,-1,'teal','gold','stand','bob','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('positive', '前向きで上を向いているイラスト。', f"""
<g transform="translate(180 210)">
  <circle r="90" class="goldp o"/>
  <g fill="{INK}"><circle cx="-32" cy="-20" r="8"/><circle cx="32" cy="-20" r="8"/></g>
  <path d="M-36 20q36 42 72 0" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{GRN}" stroke-width="16" stroke-linecap="round"><path d="M400 250h100M450 200v100"/></g>
<g fill="none" stroke="{GRN}" stroke-width="6" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M320 350q100-40 180-140"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('possess', '自分のものとして持っているイラスト。', f"""
{person(150,352,1.2,1,'teal','blue','carry','short','smile')}
<g transform="translate(230 300)">
  <path d="M-30-40h60v80h-60z" class="paper"/>
  <circle cx="0" cy="-6" r="12" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
</g>
{box(390,300,120,90,26,'gold')}
<g transform="translate(510 250)">
  <circle r="26" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10"/>
  <path d="M24 0h60v10h-14v16h-12v-16h-12v16h-12v-16h-10z" fill="{TONES['gold'][2]}"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="12 10"><rect x="290" y="200" width="280" height="170" rx="20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('powerful', '大きな力を持っていることを示すイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-70 100l-24-70q-10-30 18-38 26-8 38 18" fill="none" stroke="{SKIN}" stroke-width="30" stroke-linecap="round"/>
  <path d="M-40-20q46-56 86-6 34 40-12 66-46 22-74-60z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M46 52q38 18 50 48" fill="none" stroke="{SKIN}" stroke-width="30" stroke-linecap="round"/>
</g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2.5">
  <path d="M440 100l-56 110h46l-26 90 80-120h-50l30-80z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
