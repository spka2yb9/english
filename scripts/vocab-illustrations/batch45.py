"""第45回: 描く・予測・許可・提示など39語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('picture', '額に入った一枚の絵のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-170-130h340v260h-340z" class="goldd o"/>
  <path d="M-140-100h280v200h-280z" fill="#eaf5fb" class="o"/>
  <path d="M-140 60l90-100 60 60 60-80 70 120z" class="green o"/>
  {sun(0,-50,26)}
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('pilot', '操縦席で飛行機をあやつるパイロットのイラスト。', f"""
{plane(430,120,1.0,-6)}
<g transform="translate(220 250)">
  <path d="M-140-90h280v180h-280z" fill="#dfe6ea" class="o"/>
  <path d="M-110-60h180v90h-180z" fill="#cfe6f5" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="8"><path d="M60 60h60"/><circle cx="90" cy="36" r="18"/></g>
</g>
<g transform="translate(150 220) scale(0.8)">{person(0,60,1.0,1,'blue','blue','reach','cap','smile')}</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('pioneer', '誰もいない土地に、最初の一歩を踏み出すイラスト。', f"""
{person(150,340,1.15,1,'coral','blue','walk','cap','neutral')}
<g fill="{MUTED}" opacity=".7"><ellipse cx="105" cy="356" rx="16" ry="10"/><ellipse cx="70" cy="366" rx="16" ry="10"/></g>
<path d="M230 300h240" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="14 12" marker-end="url(#ar)"/>
{tree(430,330,0.9)}
{sun(500,90,28)}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('plain', '飾りのない無地の布と、模様入りの布を比べたイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-100-110h200v220h-200z" class="tealp o"/>
</g>
<g transform="translate(430 230)">
  <path d="M-100-110h200v220h-200z" fill="#fffdf6" class="o"/>
  <g class="coralp">{''.join(f'<circle cx="{-70+c*46}" cy="{-80+r*46}" r="14"/>' for r in range(4) for c in range(4))}</g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M140 366l18 18 30-36"/></g>
""", ground=True)

add('planet', '輪をもつ惑星が宇宙に浮かぶイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#2b3a52"/>
<g fill="#fdf6e0"><circle cx="90" cy="80" r="4"/><circle cx="150" cy="300" r="4"/><circle cx="520" cy="120" r="5"/><circle cx="480" cy="330" r="4"/><circle cx="60" cy="200" r="3"/></g>
<circle cx="300" cy="200" r="100" fill="#d78d6b" stroke="#a86f55" stroke-width="3"/>
<path d="M300 160q60 14 120 4" fill="none" stroke="#a86f55" stroke-width="10" opacity=".6"/>
<path d="M240 240q70 16 130-6" fill="none" stroke="#a86f55" stroke-width="12" opacity=".6"/>
<g fill="none" stroke="#f3e3ae" stroke-width="12"><ellipse cx="300" cy="210" rx="180" ry="40" transform="rotate(-14 300 210)"/></g>
<circle cx="300" cy="200" r="100" fill="#d78d6b" opacity=".0"/>
""", ground=False)

add('plastic', '軽くて透ける、プラスチックの容器のイラスト。', f"""
<g transform="translate(220 250)">
  <path d="M-80-90h160l-16 180h-128z" fill="#e7f6fb" stroke="{INK}" stroke-width="3"/>
  <path d="M-40-90h20l-6 180h-20z" fill="#ffffff" opacity=".8"/>
</g>
<g transform="translate(430 260)">
  <path d="M-60-60h120v140h-120z" fill="#e7f6fb" stroke="{INK}" stroke-width="3"/>
  <path d="M-60-60h120v-16h-120z" class="tealp o"/>
  <path d="M-30-60h16v140h-16z" fill="#ffffff" opacity=".8"/>
</g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('platform', '電車を待つ駅のホームのイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-260 40h260v-60h-260z" fill="#dfe6ea" class="o"/>
  <path d="M-260-20h260v-10h-260z" class="coralp o"/>
  <path d="M20 40h240v-140H20z" class="bluep o"/>
  <g fill="#e8f4fb" stroke="{INK}" stroke-width="3"><rect x="50" y="-80" width="70" height="60"/><rect x="150" y="-80" width="70" height="60"/></g>
</g>
{person(120,240,0.85,1,'teal','blue','stand','short','neutral')}
{person(220,240,0.85,1,'coral','gold','stand','bob','neutral')}
<path d="M60 306h480" class="a"/>
""", ground=True)

add('plead', 'ひざまずいて、両手を合わせて願うイラスト。', f"""
<g transform="translate(220 330)">
  <path d="M-40-70q40-16 80 0l-10 70h-60z" class="coral o"/>
  <path d="M-30-40q40-30 70 0" fill="none" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
  <circle cy="-98" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-40 0h80v20h-80z" class="blue o"/>
  <path d="M-40 20h110v16h-110z" class="blue o"/>
</g>
<g transform="translate(230 214)"><path d="M-14 26q0-30 14-40 14 10 14 40z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/></g>
{person(460,346,1.05,-1,'blue','blue','stand','bob','neutral')}
<path d="M300 220h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('pleasant', '心地よい風の中で、気持ちよく過ごすイラスト。', f"""
{sun(490,90,30)}
{person(250,340,1.2,1,'teal','gold','stand','bob','smile')}
<g class="muted" opacity=".9"><path d="M60 180q60-26 120 0t120 0"/><path d="M60 240q60-26 120 0t120 0"/></g>
{tree(440,330,0.9)}
<g class="green o" opacity=".7"><path d="M420 200q20-14 34 4-18 16-34-4z"/></g>
<path d="M60 350h480" class="a"/>
""", ground=True)

add('pledge', '手を挙げて、書面の誓いを立てるイラスト。', f"""
{person(190,346,1.25,1,'blue','blue','up','short','neutral')}
<g transform="translate(430 230)">
  <path d="M-110-110h220v220h-220z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-80-60h160M-80-20h160M-80 20h160"/></g>
  <path d="M-80 70q40-24 80 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
<path d="M300 200h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('plug', 'コンセントにプラグを差し込むイラスト。', f"""
<g transform="translate(420 220)">
  <path d="M-70-90h140v180h-140z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><rect x="-26" y="-40" width="14" height="46"/><rect x="12" y="-40" width="14" height="46"/></g>
</g>
<g transform="translate(220 220)">
  <path d="M-60-60h120v120h-120z" fill="#41506a"/>
  <g fill="#c9d3dc"><rect x="60" y="-40" width="90" height="16"/><rect x="60" y="24" width="90" height="16"/></g>
  <path d="M-60-20q-90 0-90 60" fill="none" stroke="{INK}" stroke-width="10"/>
</g>
<path d="M300 130h60" class="a" marker-end="url(#ar)"/>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('plunge', '高い所から水にまっすぐ飛び込むイラスト。', f"""
<path d="M0 280h600v120H0z" class="bluep"/>
<g transform="translate(180 160)"><path d="M-70-40h60v260h-60z" fill="#c9d3dc" class="o"/></g>
<g transform="translate(320 190) rotate(150)">{person(0,0,0.95,1,'coral','blue','up','short','neutral')}</g>
<path d="M360 150v120" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="#fffdf6" stroke-width="6"><path d="M330 290q30-24 60 0M300 310q60-30 120 0"/></g>
""", ground=False, arrow=True)

add('pocket', '上着についた小さなポケットのイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-150-130h300v260h-300z" class="teal o"/>
  <path d="M-150-130l60 40-30 220h-30z" fill="{TONES['teal'][2]}" opacity=".4"/>
  <path d="M40 10h100v90H40z" fill="{TONES['teal'][2]}" stroke="{INK}" stroke-width="3"/>
  <path d="M40 10h100v-16H40z" class="tealp o"/>
</g>
<circle cx="390" cy="230" r="66" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('poisonous', 'どくろの印がついた瓶で、有毒を示したイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-90-80h180l-16 180h-148z" fill="#e2eee2" stroke="{INK}" stroke-width="3"/>
  <path d="M-40-110h80v30h-80z" class="ink"/>
  <g transform="translate(0 30)">
    <circle r="42" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
    <g fill="{INK}"><circle cx="-14" cy="-8" r="8"/><circle cx="14" cy="-8" r="8"/><rect x="-4" y="6" width="8" height="12"/></g>
    <path d="M-20 24h40" fill="none" stroke="{INK}" stroke-width="4"/>
  </g>
</g>
<g class="corals" style="stroke-width:5"><path d="M440 150q26 20 26 50M480 130q40 30 40 70"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('polite', '帽子をとって、丁寧に頭を下げるイラスト。', f"""
<g transform="translate(220 346) rotate(18)">{person(0,0,1.2,1,'blue','blue','give','short','smile')}</g>
{hand(300,190,1)}
{person(460,346,1.05,-1,'coral','gold','stand','bob','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M110 200l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('portray', '人物を絵に描き表すイラスト。', f"""
<g transform="translate(390 230)">
  <path d="M-110-120h220v240h-220z" fill="#fffdf6" class="o"/>
  <circle cy="-30" r="42" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-60 110q0-90 60-90t60 90z" class="tealp o"/>
</g>
{person(150,346,1.05,1,'coral','blue','reach','bob','smile')}
<path d="M230 230h40" class="a" marker-end="url(#ar)"/>
<g transform="translate(510 330) rotate(28)"><path d="M-10-70h20v90h-20z" class="coral o"/><path d="M-10 20h20l-10 22z" class="ink"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('pose', 'カメラの前で、姿勢を決めて構えるイラスト。', f"""
{person(200,346,1.3,1,'coral','gold','up','bob','smile')}
<g transform="translate(450 240)">
  <path d="M-80-50h160v110h-160z" fill="#41506a"/>
  <circle r="34" fill="#7f8ea6" stroke="{INK}" stroke-width="3"/>
  <circle r="16" fill="#e8f4fb"/>
  <path d="M-40-50h50v-20h-50z" fill="#41506a"/>
</g>
<g class="golds" style="stroke-width:5"><path d="M340 160l-30-20M350 200h-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('poster', '壁に貼られた大きなポスターのイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-160-150h320v300h-320z" fill="#fffdf6" class="o"/>
  <path d="M-130-120h260v120h-260z" class="coralp o"/>
  <circle cy="-60" r="40" class="coral o"/>
  <g fill="{INK}"><rect x="-110" y="20" width="220" height="20"/><rect x="-70" y="60" width="140" height="14"/></g>
  <g class="gold o"><circle cx="-140" cy="-136" r="10"/><circle cx="140" cy="-136" r="10"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('postpone', '予定の日を、あとの日にずらすイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-130h400v260h-400z" class="paper"/>
  <path d="M-200-130h400v50h-400z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">{''.join(f'<path d="M{-200+c*100}-80v210"/>' for c in range(1,4))}{''.join(f'<path d="M-200 {-10+r*70}h400"/>' for r in range(2))}</g>
  <g opacity=".35"><circle cx="-150" cy="-45" r="26" class="coral o"/></g>
  <circle cx="150" cy="25" r="26" class="coral o"/>
</g>
<path d="M170 175q120-60 260 60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('praise', '拍手を受けて、よくやったとほめられるイラスト。', f"""
{person(200,346,1.25,1,'coral','blue','stand','bob','smile')}
<g transform="translate(200 150)"><path d="M0-34l12 24 26 4-19 18 5 26-24-13-24 13 5-26-19-18 26-4z" class="gold o"/></g>
{person(450,346,1.05,-1,'teal','gold','give','short','smile')}
{hand(380,250,-1)}
<g class="golds" style="stroke-width:4"><path d="M350 200l-20-16M356 236h-26"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('preach', '壇の上から、聴衆に説き聞かせるイラスト。', f"""
<g transform="translate(180 300)">
  <path d="M-80-40h160v100h-160z" class="goldd o"/>
  <path d="M-60-56h120v16h-120z" class="goldp o"/>
</g>
<g transform="translate(180 190)">{person(0,60,1.05,1,'violet','blue','up','short','neutral')}</g>
<g opacity=".85">{person(400,346,0.85,-1,'teal','blue','stand','bob','neutral')}{person(490,346,0.85,-1,'coral','gold','stand','short','neutral')}</g>
<path d="M270 200h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('precede', '二つのうち、先に来るほうを示したイラスト。', f"""
<g transform="translate(160 230)">
  <circle r="60" class="coral o"/>
  <path d="M-14-24h28v48h-28z" fill="#fffdf6"/>
</g>
<g transform="translate(400 230)">
  <circle r="60" class="tealp o"/>
  <g fill="{TONES['teal'][2]}"><rect x="-24" y="-24" width="14" height="48"/><rect x="10" y="-24" width="14" height="48"/></g>
</g>
<path d="M170 340h280" class="a" marker-end="url(#ar)"/>
<path d="M100 130v40" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('predict', '先のことを言い当てて、予測を示すイラスト。', f"""
{person(150,346,1.05,1,'violet','blue','point','short','neutral')}
<g transform="translate(400 220)">
  <path d="M-130-110h260v220h-260z" fill="#f7fbfe" class="o"/>
  <path d="M-100 60l50-40 40 20 50-70" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"/>
  <path d="M40-30q50-40 90-60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="12 9" marker-end="url(#ar)"/>
</g>
<path d="M230 220h30" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('pregnant', 'おなかが大きくなった人のイラスト。', f"""
<g transform="translate(300 330)">
  <path d="M-40-100q46-20 84 0 20 40 6 100h-90z" class="coral o"/>
  <ellipse cx="34" cy="-30" rx="46" ry="42" class="coral o"/>
  <path d="M40-30q30 20 20 60" fill="none" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
  <path d="M-40-70q-30 20-20 60" fill="none" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
  <circle cy="-134" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-30-150q30-30 60 0z" fill="{HAIR}"/>
  <path d="M-18 0l-8 66M18 4l10 62" fill="none" stroke="{TONES['blue'][0]}" stroke-width="13" stroke-linecap="round"/>
</g>
<circle cx="334" cy="300" r="56" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 400h480" class="a"/>
""", ground=True)

add('prepared', '道具をきちんとそろえて、支度が整ったイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-230-20h460v20h-460z" class="goldd o"/>
</g>
<g transform="translate(140 250)"><path d="M-50-40h100v60h-100z" class="tealp o"/></g>
<g transform="translate(290 250)"><path d="M-10-70h20v90h-20z" class="coral o"/><path d="M-10 20h20l-10 20z" class="ink"/></g>
<g transform="translate(430 250)">{box(0,0,90,60,0,'gold')}</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M480 140l20 20 34-40"/></g>
<path d="M60 350h480" class="a"/>
""", ground=True)

add('prescribe', '医師が薬の指示書を書いて渡すイラスト。', f"""
{person(140,346,1.05,1,'blue','blue','give','bob','smile')}
<g transform="translate(320 220)">
  <path d="M-80-100h160v200h-160z" class="paper"/>
  <g fill="{INK}"><rect x="-50" y="-70" width="60" height="12"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-50-30h100M-50 0h100M-50 30h70"/></g>
</g>
<g transform="translate(470 260)">
  <path d="M-40-50h80l-8 110h-64z" fill="#f4fbff" class="o"/>
  <path d="M-34-10h68l-6 70h-56z" class="coralp o"/>
  <path d="M-20-60h40v12h-40z" class="ink"/>
</g>
<path d="M220 190h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('present', '資料を前に示して、みんなに発表するイラスト。', f"""
<g transform="translate(400 220)">
  <path d="M-150-130h300v230h-300z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"><path d="M-110 60l60-70 50 40 60-80"/></g>
  <g fill="{INK}"><rect x="-110" y="-110" width="140" height="14"/></g>
  <path d="M0 100v40" class="ink" stroke="{INK}" stroke-width="6"/>
</g>
{person(140,346,1.1,1,'blue','blue','point','short','smile')}
<path d="M220 210h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('preserve', '瓶に密封して、そのまま保っておくイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-100-90h200v50h-200z" class="goldd o"/>
  <path d="M-90-40h180v160h-180z" fill="#e7f6fb" stroke="{INK}" stroke-width="3"/>
  <g class="green o"><circle cx="-40" cy="30" r="26"/><circle cx="20" cy="60" r="26"/><circle cx="50" cy="10" r="26"/><circle cx="-20" cy="90" r="26"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 170l18 18 30-36"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('presume', '確かめないまま、そうだろうと思い込むイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','think','short','neutral')}
<g transform="translate(430 190)">
  <path d="M-120-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-156q-38-4-36-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 -6)" opacity=".55"><path d="M-50-40h100v90h-100z" class="tealp o"/></g>
  <g fill="{INK}"><path d="M104 10q0-26 20-26t20 26q0 14-16 18v14h-10v-20q14-4 14-14t-8-10-10 12z"/><rect x="112" y="54" width="10" height="10"/></g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="290" cy="290" r="12"/><circle cx="266" cy="314" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('prevail', '一方が広く行きわたって、全体をおおうイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-230-120h460v240h-460z" fill="#fffdf6" class="o"/>
  <g class="tealp">{''.join(f'<circle cx="{-190+c*56}" cy="{-80+r*56}" r="20"/>' for r in range(4) for c in range(8))}</g>
  <g class="coral o"><circle cx="-190" cy="-80" r="20"/><circle cx="-134" cy="-80" r="20"/></g>
</g>
<path d="M120 360h360" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('previous', '並んだ日付のうち、ひとつ前を示したイラスト。', f"""
<g class="tealp o"><rect x="120" y="200" width="100" height="110"/><rect x="360" y="200" width="100" height="110"/><rect x="480" y="200" width="100" height="110"/></g>
<rect x="240" y="200" width="100" height="110" class="coral o"/>
<circle cx="410" cy="255" r="52" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M370 150h-60" class="a" marker-end="url(#ar)"/>
<path d="M60 330h480" class="a"/>
""", ground=True, arrow=True)

add('price', '商品につけられた値札のイラスト。', f"""
<g transform="translate(230 250)">
  {box(0,0,180,140,30,'teal')}
</g>
<g transform="translate(430 200) rotate(-10)">
  <path d="M-90-50h160l30 50-30 50h-160z" fill="#fffdf6" class="o"/>
  <circle cx="60" r="10" class="ink"/>
  <g fill="{INK}"><rect x="-60" y="-14" width="90" height="14"/><rect x="-60" y="10" width="60" height="10"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('printer', '紙を出力しているプリンターのイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-150-60h300v120h-300z" fill="#dfe6ea" class="o"/>
  <path d="M-100-60h200v-50h-200z" fill="#c9d3dc" class="o"/>
  <path d="M-90 0h180v14h-180z" class="ink"/>
  <g class="green o"><circle cx="110" cy="-30" r="10"/></g>
</g>
<g transform="translate(300 130)">
  <path d="M-90-70h180v80h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-40h120M-60-14h120"/></g>
</g>
<path d="M60 326h480" class="a"/>
""", ground=True)

add('prize', 'リボンのついた優勝カップのイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-80-90h160l-16 90a64 64 0 0 1-128 0z" class="gold o"/>
  <path d="M-80-70q-50 0-50 40t50 40M80-70q50 0 50 40t-50 40" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10"/>
  <path d="M-20 60h40v40h-40z" class="goldd o"/>
  <path d="M-70 100h140v22h-140z" class="goldd o"/>
</g>
<g transform="translate(300 150)"><path d="M0-24l8 16 18 2-13 13 3 18-16-9-16 9 3-18-13-13 18-2z" fill="#fffdf6"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('probe', '虫めがねで中を細かく調べるイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-160-90h320v180h-320z" fill="#fffdf6" class="o"/>
  <g class="tealp o"><circle cx="-90" cy="-20" r="26"/><circle cx="0" cy="30" r="26"/><circle cx="80" cy="-30" r="26"/></g>
</g>
<g transform="translate(370 190) rotate(30)">
  <circle r="70" fill="#e7f6fb" opacity=".85" stroke="{INK}" stroke-width="8"/>
  <path d="M0 70v70" fill="none" stroke="{INK}" stroke-width="16"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('proclaim', '広場で大声に知らせを告げるイラスト。', f"""
{person(180,346,1.2,1,'violet','blue','up','short','neutral')}
<g transform="translate(300 190) rotate(-10)">
  <path d="M0-40l120-50v180L0 40z" class="coral o"/>
  <path d="M0-40h-50v80H0z" class="coralp o"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M450 170q26 30 26 60M490 140q40 44 40 90"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('produce', '材料から次々に製品を作り出すイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-120-100h240v200h-240z" fill="#dfe6ea" class="o"/>
  <path d="M-80-140h40v40h-40zM0-140h40v40H0z" fill="#c9d3dc" class="o"/>
  <g class="muted"><path d="M-60-160q0-30 20-30M20-160q0-30 20-30"/></g>
  <g fill="none" stroke="{INK}" stroke-width="10"><circle cx="-30" cy="0" r="34"/><circle cx="50" cy="40" r="26"/></g>
</g>
<g transform="translate(430 300)">{box(0,0,90,60,0,'gold')}{box(0,-70,90,60,0,'gold')}</g>
<path d="M330 220h50" class="a" marker-end="url(#ar)"/>
<path d="M60 350h480" class="a"/>
""", ground=True, arrow=True)

add('professional', '専門の道具を手に、仕事として腕をふるうイラスト。', f"""
{person(200,346,1.3,1,'blue','blue','carry','short','neutral')}
<g transform="translate(200 240)"><path d="M-50-30h100v60h-100z" class="ink"/><path d="M-16-40h32v10h-32z" class="ink"/></g>
<g transform="translate(430 240)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <path d="M-50-40h100v20h-100z" class="teal"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-50 10h100M-50 40h70"/></g>
  <g transform="translate(60 -70)"><path d="M0-24l8 16 18 2-13 13 3 18-16-9-16 9 3-18-13-13 18-2z" class="gold o"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('professor', '大学の教壇で、黒板を使って講義する教授のイラスト。', f"""
<g transform="translate(380 210)">
  <path d="M-160-120h320v210h-320z" fill="#31473d" class="o"/>
  <g fill="none" stroke="#e9f3ec" stroke-width="4"><path d="M-120-70h200M-120-30h240M-120 10h160"/><circle cx="80" cy="40" r="26"/></g>
</g>
{person(140,346,1.15,1,'violet','blue','point','short','neutral')}
<g transform="translate(140 252)"><path d="M-40-30h80v10h-80z" class="paper"/></g>
<path d="M220 220h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
