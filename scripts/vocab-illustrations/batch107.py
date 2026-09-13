"""第107回: 熟語・複合語45語。"""
from lib import *
W=[]
def add(slug,a,b,**k): W.append(emit(slug,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'
def qmark(x,y,s=1,cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-24-26q0-28 26-28t26 26q0 22-26 28v12" fill="none" stroke="{TONES[cls][0]}" stroke-width="10" stroke-linecap="round"/>'
            f'<circle cy="36" r="7" class="{cls}"/></g>')
def clock(x,y,r=60,hand=-90):
    import math
    ex, ey = x+r*0.55*math.cos(math.radians(hand)), y+r*0.55*math.sin(math.radians(hand))
    return (f'<g><circle cx="{x}" cy="{y}" r="{r}" fill="#fffdf6" class="o"/>'
            f'<path d="M{x} {y}v-{r*0.6:.0f}" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M{x} {y}L{ex:.0f} {ey:.0f}" fill="none" stroke="{TONES["coral"][0]}" stroke-width="5" stroke-linecap="round"/>'
            f'<circle cx="{x}" cy="{y}" r="6" class="ink"/></g>')

add('high-profile', '注目を一身に集めるイラスト。', f"""
<path d="M300 60l150 300H150z" fill="{TONES['gold'][1]}" opacity="0.7"/>
{person(300,346,1.3,1,'coral','blue','up','short','smile')}
<g fill="{INK}"><rect x="90" y="250" width="60" height="40" rx="8"/><rect x="450" y="250" width="60" height="40" rx="8"/></g>
<g class="golds"><path d="M120 230l-16-20M480 230l16-20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('in-fact', '見かけの裏の本当のところを示すイラスト。', f"""
<g transform="translate(320 250)">
  <path d="M-130-120h260v240h-260z" class="tealp o"/>
  <circle cx="0" cy="10" r="56" class="coral o"/>
</g>
<g transform="translate(320 130) rotate(-14)">
  <path d="M-150-40h300v60h-300z" class="bluep o"/>
</g>
{hand(530,130,-1)}
{ck(140,180,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('short-term', '短い期間だけの区切りのイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M60 250h480"/></g>
<g class="teal o"><rect x="140" y="200" width="90" height="50"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M140 320h90M140 320v-40M230 320v-40"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8">{''.join(f'<path d="M{120+i*80} 270v-40"/>' for i in range(6))}</g>
""", ground=False, arrow=True)

add('used-to', '以前はそうだったが今は違うイラスト。', f"""
<g opacity="0.4">{person(160,352,1.2,1,'teal','blue','walk','short','smile')}</g>
<g transform="translate(160 190)"><path d="M-70-40h140v70h-140z" fill="#dfe6ea" class="o"/></g>
{xx(160,120,0.8,MUTED)}
<g class="a" marker-end="url(#ar)"><path d="M280 250h60"/></g>
{person(450,352,1.2,1,'coral','blue','stand','short','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M100 386h400"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('line-up', '横一列に並んだ顔ぶれのイラスト。', f"""
{person(130,352,1,1,'teal','blue','stand','short','neutral')}
{person(240,352,1,1,'coral','gold','stand','bob','neutral')}
{person(350,352,1,1,'gold','violet','stand','short','neutral')}
{person(460,352,1,1,'green','blue','stand','bun','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><path d="M70 380h480"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('all-right', '問題なしと合図するイラスト。', f"""
{person(220,352,1.3,1,'teal','blue','up','short','smile')}
{ck(430,220,2)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('at-random', '順序なくばらばらに散らばるイラスト。', f"""
<g class="tealp o">
  <circle cx="140" cy="180" r="26"/><circle cx="330" cy="130" r="26"/><circle cx="480" cy="210" r="26"/>
  <circle cx="200" cy="300" r="26"/><circle cx="390" cy="320" r="26"/><circle cx="270" cy="220" r="26"/>
</g>
<g transform="translate(500 330)">
  <path d="M-40-40h80v80h-80z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><circle cx="-18" cy="-18" r="7"/><circle cx="18" cy="18" r="7"/><circle r="7"/></g>
</g>
""", ground=False)

add('old-fashioned', '昔ながらの古い型のイラスト。', f"""
<g transform="translate(280 270)">
  <path d="M-110 60h220v20h-220z" class="goldd o"/>
  <path d="M-90-40h180v100h-180z" class="goldd o"/>
  <circle cx="-20" cy="10" r="36" fill="#3a3630"/>
  <circle cx="-20" cy="10" r="8" class="goldp"/>
  <path d="M60 0q60-60 90-120" fill="none" stroke="{MUTED}" stroke-width="10"/>
  <path d="M120-140q40-30 60 20-50 30-60-20z" class="goldp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M520 340V180"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('on-the-whole', '全体としてみればこうだと示すイラスト。', f"""
<g class="teal o">{''.join(f'<circle cx="{130+i*70}" cy="230" r="28"/>' for i in range(5))}</g>
<circle cx="480" cy="230" r="28" class="coralp o"/>
<g fill="none" stroke="{GRN}" stroke-width="5"><path d="M100 320h410M100 320v-24M510 320v-24"/></g>
{ck(300,370,0.8)}
""", ground=False)

add('out-of-date', '期限が切れて古くなったイラスト。', f"""
<g transform="translate(280 210)">
  <path d="M-170-150h340v300h-340z" class="paper"/>
  <path d="M-170-150h340v46h-340z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M-170 {-50+i*48}h340"/>' for i in range(4))}
    {''.join(f'<path d="M{-114+c*57} -104v254"/>' for c in range(5))}
  </g>
  <circle cx="-86" cy="-16" r="22" class="coralp o"/>
</g>
{xx(460,140,1.4)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('per-cent', '全体を百としたときの割合のイラスト。', f"""
<g transform="translate(240 220)">
  <circle r="140" class="tealp o"/>
  <path d="M0 0v-140A140 140 0 0 1 121 70z" class="teal o"/>
</g>
<g transform="translate(470 220)">
  <circle cx="-40" cy="-40" r="26" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10"/>
  <circle cx="40" cy="40" r="26" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10"/>
  <path d="M-56 60L56-60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('up-to-date', '中身が最新に保たれているイラスト。', f"""
<g transform="translate(280 210)">
  <path d="M-170-150h340v300h-340z" class="paper"/>
  <path d="M-170-150h340v46h-340z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M-170 {-50+i*48}h340"/>' for i in range(4))}
    {''.join(f'<path d="M{-114+c*57} -104v254"/>' for c in range(5))}
  </g>
  <circle cx="114" cy="80" r="22" class="coral o"/>
</g>
{ck(470,150,1.2)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('according-to', '出どころの本にもとづいて話すイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-90-110h180v220h-180z" class="violet o"/>
  <path d="M-70-90h140v180h-140z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-40-50h80M-40-20h80M-40 10h60"/></g>
</g>
{person(450,352,1.2,-1,'teal','blue','point','short','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M270 220h110"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('any-more', 'もう残っていないイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-110-120h220v240h-220z" fill="#fffdf6" class="o"/>
</g>
{xx(300,250,2)}
<g opacity="0.35">{box(140,300,90,60,18,'gold')}</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M200 200h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('as-well-as', 'こちらもあちらも両方入れるイラスト。', f"""
<g transform="translate(180 240)">
  <path d="M-80-80h160v160h-160z" class="teal o"/>
</g>
<g fill="none" stroke="{GRN}" stroke-width="14" stroke-linecap="round"><path d="M280 240h50M305 215v50"/></g>
<g transform="translate(450 240)">
  <circle r="80" class="coral o"/>
</g>
{ck(180,360,0.7)}
{ck(450,360,0.7)}
""", ground=False)

add('at-last', '長い道の末にやっとたどり着くイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="16 12"><path d="M90 340q100-120 200-60t120-160"/></g>
{person(90,352,0.9,1,'teal','blue','walk','short','neutral')}
<g transform="translate(450 190)">
  <path d="M-6 170V-70" class="a"/>
  <path d="M-6-70h90l-18 26 18 26H-6z" class="coral o"/>
</g>
{ck(520,300,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('at-least', '少なくともこの線には届くイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-160-120h320v240h-320z" fill="#fffdf6" class="o"/>
  <path d="M-160 20h320v100h-320z" class="teal o"/>
  <path d="M-180 20h360v10h-360z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M520 380V280"/></g>
{ck(120,150,0.8)}
<path d="M60 390h480" class="a"/>
""", ground=True, arrow=True)

add('full-time', '一日の勤めをまるごと働くイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-230-30h460v60h-460z" fill="#fffdf6" class="o"/>
  <path d="M-230-30h460v60h-460z" class="teal o"/>
</g>
{clock(160,140,54,60)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M70 340h460M70 340v-24M530 340v-24"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('large-scale', '桁ちがいに大きな規模のイラスト。', f"""
<g transform="translate(140 320)">
  <path d="M-30 0v-40h60V0z" fill="#fffdf6" class="o"/>
  <path d="M-36-40L0-64l36 24z" class="teal o"/>
</g>
<g transform="translate(400 300)">
  <path d="M-150 20v-200h300v200z" fill="#fffdf6" class="o"/>
  <path d="M-170-180L0-280l170 100z" class="teal o"/>
  <g class="tealp o">{''.join(f'<rect x="{-120+c*70}" y="{-150+r*70}" width="50" height="46"/>' for r in range(2) for c in range(4))}</g>
</g>
<path d="M60 326h480" class="a"/>
""", ground=True)

add('long-standing', '長い年月ずっと立っているイラスト。', f"""
{tree(300,320,2.1)}
<g class="a" marker-end="url(#ar)"><path d="M80 380h440"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8">{''.join(f'<path d="M{120+i*80} 380v-24"/>' for i in range(6))}</g>
""", ground=False, arrow=True)

add('long-term', '長い期間にわたる区切りのイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M60 250h480"/></g>
<g class="teal o"><rect x="120" y="200" width="360" height="50"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M120 320h360M120 320v-40M480 320v-40"/></g>
""", ground=False, arrow=True)

add('long-time', '長いあいだ変わらず続く間柄のイラスト。', f"""
{person(200,352,1.15,1,'teal','blue','give','short','smile')}
{person(370,352,1.15,-1,'coral','gold','give','bob','smile')}
<g fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"><path d="M250 290h70"/></g>
<g class="a" marker-end="url(#ar)"><path d="M80 150h440"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8">{''.join(f'<path d="M{120+i*80} 150v24"/>' for i in range(6))}</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('non-profit', 'もうけを目当てにしない活動のイラスト。', f"""
{building(200,300,0.8,'teal')}
<g transform="translate(430 260)">
  <path d="M-60-30h120v60h-120z" class="greenp o"/>
  <circle r="16" class="gold o"/>
</g>
{xx(430,150,1.2)}
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M300 200q-22-28 0-40 22-12 22 16 0-28 22-16 22 12 0 40l-22 22z"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('part-time', '一日のうち一部だけ働くイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-230-30h460v60h-460z" fill="#fffdf6" class="o"/>
  <path d="M-230-30h180v60h-180z" class="teal o"/>
</g>
{clock(160,140,54,-30)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M70 340h180M70 340v-24M250 340v-24"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('post-war', '争いのあとに町を建て直すイラスト。', f"""
<g transform="translate(150 300)">
  <path d="M-70 0v-90h50l-10 40 20-40h10v90z" fill="#dfe6ea" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 240h60"/></g>
<g transform="translate(450 300)">
  <path d="M-90 0v-90h180V0z" fill="#fffdf6" class="o"/>
  <path d="M-104-90L0-146l104 56z" class="teal o"/>
  <path d="M-24-56h48V0h-48z" class="teald o"/>
</g>
{ck(450,150,0.9)}
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('so-called', '名ばかりで中身が伴わないイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-110-70h220v140h-220z" class="tealp o"/>
</g>
<g transform="translate(300 140)">
  <path d="M-90-40h180v60h-180z" class="gold o"/>
  <path d="M0 20v40" fill="none" stroke="{MUTED}" stroke-width="5"/>
</g>
{qmark(470,240,1.2)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('thought-provoking', '読むと考えが次々わくイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-100-120h200v240h-200z" class="violet o"/>
  <path d="M-80-100h160v200h-160z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-50-50h100M-50-20h100M-50 10h70"/></g>
</g>
<g class="o" fill="#e1edfb"><circle cx="320" cy="220" r="16"/><circle cx="360" cy="180" r="22"/></g>
<g transform="translate(450 150)">
  <path d="M-110-60q-6-40 30-44 14-30 46-20 26-4 32 24 30 4 26 34-4 26-32 26h-70q-28-2-32-20z" class="bluep o"/>
  {qmark(450,150,0.9).replace('translate(450 150)','translate(0 0)')}
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('apart-from', 'それだけを外して考えるイラスト。', f"""
<g class="teal o">{''.join(f'<circle cx="{140+i*80}" cy="240" r="30"/>' for i in range(4))}</g>
<circle cx="500" cy="240" r="30" class="coralp o"/>
<g fill="none" stroke="{GRN}" stroke-width="5"><path d="M100 330h300M100 330v-24M400 330v-24"/></g>
{xx(500,150,0.8)}
""", ground=False)

add('as-a-result', 'これが元でこうなったと示すイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 240h70"/></g>
<g transform="translate(460 240)">
  <path d="M-80-80h160v160h-160z" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('as-far-as', 'ここまでの範囲を示すイラスト。', f"""
<g class="a"><path d="M60 250h480"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="14" stroke-linecap="round"><path d="M100 250h260"/></g>
<circle cx="360" cy="250" r="22" class="coral o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M100 330h260M100 330v-40M360 330v-40"/></g>
{person(100,250,0.6,1,'teal','blue','stand','short','neutral')}
""", ground=False)

add('as-long-as', 'この条件を満たす間だけ通れるイラスト。', f"""
<g transform="translate(340 250)">
  <path d="M-20-140h40v280h-40z" class="ink"/>
  <path d="M-160-80h140v30h-140z" class="coral o"/>
</g>
<g transform="translate(180 250)">
  <circle r="26" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10"/>
  <path d="M24 0h60v12h-14v14h-12v-14h-12v14h-12v-14h-10z" fill="{TONES['gold'][2]}"/>
</g>
{ck(470,200,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('decision-making', '選んで決める意思決定のイラスト。', f"""
{person(300,352,1.2,1,'teal','blue','think','short','neutral')}
<g transform="translate(140 200)"><path d="M-70-60h140v120h-140z" class="tealp o"/></g>
<g transform="translate(470 200)"><path d="M-70-60h140v120h-140z" class="coralp o"/></g>
{ck(470,320,0.8)}
{xx(140,320,0.8,MUTED)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M240 250l-40-20M360 250l40-20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('due-to', '結果のもとをたどるイラスト。', f"""
<g transform="translate(460 240)">
  <path d="M-80-80h160v160h-160z" class="coral o"/>
</g>
<g transform="translate(150 240)">
  <path d="M-70-70h140v140h-140z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M360 240H240"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('film-maker', 'カメラを回して映画を撮る人のイラスト。', f"""
{person(180,352,1.2,1,'violet','blue','hold','cap','neutral')}
<g transform="translate(300 220)">
  <path d="M-70-40h140v80h-140z" class="ink"/>
  <path d="M70-24l50-26v100l-50-26z" class="ink"/>
  <circle cx="-30" cy="-56" r="26" fill="none" stroke="{INK}" stroke-width="8"/>
  <circle cx="24" cy="-56" r="26" fill="none" stroke="{INK}" stroke-width="8"/>
</g>
<g transform="translate(470 320)">
  <path d="M-60-30h120v60h-120z" class="ink"/>
  <path d="M-60-50h120v20h-120z" class="ink" transform="rotate(-14 -60 -40)"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('for-instance', 'たくさんの中からひとつ例に挙げるイラスト。', f"""
<g class="tealp o">
  {''.join(f'<circle cx="{130+c*70}" cy="{200+r*70}" r="26"/>' for r in range(2) for c in range(4))}
</g>
<g class="a" marker-end="url(#ar)"><path d="M420 240h50"/></g>
<circle cx="520" cy="240" r="40" class="coral o"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('in-addition-to', '元のものにもうひとつ加えるイラスト。', f"""
<g transform="translate(180 260)">
  <path d="M-90-60h180v120h-180z" class="teal o"/>
</g>
<g fill="none" stroke="{GRN}" stroke-width="14" stroke-linecap="round"><path d="M290 260h50M315 235v50"/></g>
<g transform="translate(460 260)">
  <path d="M-70-50h140v100h-140z" class="coralp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('in-advance', '当日より前に済ませておくイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M60 250h480"/></g>
<circle cx="420" cy="250" r="26" class="coral o"/>
<circle cx="180" cy="250" r="20" class="teal o"/>
<g transform="translate(180 150)">
  <path d="M-50-30h100v50h-100z" class="greenp o"/>
  <circle r="12" class="gold o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M180 190v34"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M400 330H200"/></g>
""", ground=False, arrow=True)

add('in-charge-of', 'その持ち場を任されているイラスト。', f"""
{person(180,352,1.3,1,'violet','blue','point','bun','neutral')}
<g transform="translate(120 250)">
  <circle r="26" class="gold o"/>
  <path d="M0-14l6 12 14 2-10 10 2 14-12-7-12 7 2-14-10-10 14-2z" class="goldd"/>
</g>
{person(400,356,0.85,1,'teal','blue','stand','short','neutral')}
{person(490,356,0.85,1,'coral','gold','stand','bob','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M260 250h100"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('in-common', 'ふたつが同じ部分を持つイラスト。', f"""
<g transform="translate(300 230)">
  <circle cx="-70" cy="0" r="120" class="tealp o"/>
  <circle cx="70" cy="0" r="120" class="coralp o"/>
  <path d="M0-98a120 120 0 0 0 0 196 120 120 0 0 0 0-196z" class="gold o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('in-general', 'たいていはこうだと示すイラスト。', f"""
<g class="teal o">{''.join(f'<circle cx="{140+i*70}" cy="240" r="30"/>' for i in range(5))}</g>
<circle cx="490" cy="240" r="30" class="coralp o"/>
<g fill="none" stroke="{GRN}" stroke-width="5"><path d="M100 330h320M100 330v-24M420 330v-24"/></g>
""", ground=False)

add('in-particular', 'その中の一点をとくに取り上げるイラスト。', f"""
<g class="tealp o">{''.join(f'<circle cx="{130+c*80}" cy="{200+r*80}" r="30"/>' for r in range(2) for c in range(5))}</g>
<circle cx="290" cy="280" r="30" class="coral o"/>
<g transform="translate(290 280)">
  <circle r="66" fill="none" stroke="{INK}" stroke-width="9"/>
  <path d="M48 48l50 50" fill="none" stroke="{INK}" stroke-width="13" stroke-linecap="round"/>
</g>
""", ground=False)

add('in-return', 'もらった代わりにお返しをするイラスト。', f"""
{person(150,352,1.15,1,'teal','blue','give','short','smile')}
{person(470,352,1.15,-1,'coral','gold','give','bob','smile')}
<g transform="translate(250 240)"><path d="M-34-26h68v52h-68z" class="goldp o"/></g>
<g transform="translate(380 300)">
  <path d="M-34-26h68v52h-68z" class="coralp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 180h160M390 350H230"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('in-spite-of', 'さまたげがあってもやりとげるイラスト。', f"""
{cloud(160,110,1.4,'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
  {''.join(f'<path d="M{100+i*32} {190+(i%3)*16}l-14 46"/>' for i in range(6))}
</g>
{person(330,352,1.2,1,'coral','blue','walk','short','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M410 300h120"/></g>
{ck(480,180,1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('no-longer', 'かつてはあったが今はもうないイラスト。', f"""
<g opacity="0.4">
  <g transform="translate(160 250)"><path d="M-80-80h160v160h-160z" class="teal o"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 250h60"/></g>
<g transform="translate(460 250)">
  <path d="M-80-80h160v160h-160z" fill="#fffdf6" class="o"/>
</g>
{xx(460,250,1.6)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('on-average', 'ならしてみるとこの高さになるイラスト。', f"""
<g transform="translate(300 250)">
  <g class="tealp o">
    <rect x="-220" y="-20" width="60" height="80"/><rect x="-140" y="-70" width="60" height="130"/>
    <rect x="-60" y="10" width="60" height="50"/><rect x="20" y="-50" width="60" height="110"/>
    <rect x="100" y="-30" width="60" height="90"/>
  </g>
  <path d="M-240-24h420" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="14 12"/>
  <path d="M-240 60h420" class="a"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M520 320v-90"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

print(len(W), ' '.join(W))
print(sheet(W))
