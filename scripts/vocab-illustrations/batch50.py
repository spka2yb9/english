"""第50回: 刺激・苦闘・要約・誘惑など40語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('stab', 'とがった刃で刺すイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-140-20h280v70h-280z" class="goldd o"/>
  <g class="corals" style="stroke-width:5"><path d="M-40-40l-24-20M40-40l24-20"/></g>
</g>
<g transform="translate(300 160)">
  <path d="M-16-120h32v120h-32z" class="ink"/>
  <path d="M-20 0h40l-20 80z" fill="#dbe3ea" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M400 130v90" class="a" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('stem', '花を支える一本の茎を示したイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-6-180h12v180h-12z" fill="{TONES['green'][2]}"/>
  <g class="green o"><ellipse cx="-40" cy="-120" rx="34" ry="16" transform="rotate(-20 -40 -120)"/><ellipse cx="40" cy="-80" rx="34" ry="16" transform="rotate(20 40 -80)"/></g>
  <g class="coral o"><circle cy="-190" r="34"/></g>
  <g class="gold o"><circle cy="-190" r="14"/></g>
</g>
<circle cx="300" cy="220" r="44" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M420 220h-60" class="a" marker-end="url(#ar)"/>
<path d="M60 306h480" class="a"/>
""", ground=True, arrow=True)

add('stimulate', '刺激を受けて、動きが活発になるイラスト。', f"""
<g transform="translate(180 240)">
  <circle r="70" class="tealp o"/>
  <g class="muted"><path d="M-30 0h60"/></g>
</g>
<g transform="translate(430 240)">
  <circle r="70" class="coral o"/>
  <g class="corals" style="stroke-width:6"><path d="M-90-60l-30-24M0-96v-30M90-60l30-24M-90 60l-30 24M90 60l30 24"/></g>
</g>
<path d="M280 240h50" class="a" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('stomach', 'おなかの位置を示したイラスト。', f"""
<g transform="translate(300 240)">
  <circle cy="-120" r="44" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-90 140q0-140 90-140t90 140z" class="teal o"/>
  <path d="M-84 30q-40 20-40 80" fill="none" stroke="{SKIN}" stroke-width="18" stroke-linecap="round"/>
  <path d="M84 30q40 20 40 80" fill="none" stroke="{SKIN}" stroke-width="18" stroke-linecap="round"/>
</g>
<circle cx="300" cy="310" r="52" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M440 310h-70" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('storm', '雷と横なぐりの雨があばれる嵐のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#5b6b80"/>
<g fill="#41506a"><path d="M60 130q-10-50 50-56 20-40 80-24 40-40 100 0 60-20 80 30 60 0 60 50z"/></g>
<g fill="#f3e3ae"><path d="M240 180l-40 90h44l-30 90 90-120h-46l30-60z"/></g>
<g fill="none" stroke="#cfe0ef" stroke-width="5" stroke-linecap="round">
  <path d="M80 200l-30 70M140 230l-30 70M400 200l-30 70M460 230l-30 70M520 190l-30 70"/>
</g>
{tree(120,380,0.9)}
""", ground=False)

add('strict', '決まりを厳しく守らせるイラスト。', f"""
{person(150,346,1.2,1,'blue','blue','point','short','flat')}
<g transform="translate(400 220)">
  <path d="M-110-110h220v220h-220z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-80-60h160M-80-20h160M-80 20h160"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M-80 60h160"/></g>
</g>
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M120 200l40 12M190 200l-40 12"/></g>
<path d="M240 220h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('strive', '重い荷を押し上げようと力を尽くすイラスト。', f"""
<g transform="translate(340 250)">
  <path d="M-200 90L100-60" fill="none" stroke="{MUTED}" stroke-width="6"/>
  <circle cx="60" cy="-70" r="54" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(280 300) rotate(-24)">{person(0,0,1.05,1,'coral','blue','reach','short','flat')}</g>
<g class="corals" style="stroke-width:5"><path d="M210 200l-24-16M220 240h-30"/></g>
<path d="M170 340l180-110" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('struggle', '流れに逆らって、必死にもがくイラスト。', f"""
<path d="M0 250h600v150H0z" class="bluep"/>
<g fill="none" stroke="#fffdf6" stroke-width="6" opacity=".8">
  <path d="M40 300h140M240 300h140M60 350h160M300 350h180"/>
</g>
{person(280,290,1.2,1,'coral','blue','up','short','flat')}
<g class="a" marker-end="url(#ar)"><path d="M470 200h-100"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M180 200h80"/></g>
<g fill="none" stroke="#fffdf6" stroke-width="5"><path d="M200 270q40-24 70 0M330 280q40-24 70 0"/></g>
""", ground=False, arrow=True)

add('stun', '思いもよらぬことに、あっけにとられるイラスト。', f"""
{face(280,200,95,'flat')}
<g fill="#fffdf6" stroke="{INK}" stroke-width="3"><circle cx="242" cy="182" r="22"/><circle cx="318" cy="182" r="22"/></g>
<g fill="{INK}"><circle cx="242" cy="182" r="7"/><circle cx="318" cy="182" r="7"/></g>
<g transform="translate(280 252)"><ellipse rx="26" ry="30" fill="#8b4a3e"/></g>
<g class="golds" style="stroke-width:6"><path d="M400 120l34-26M424 170h34M400 220l34 26M160 120l-34-26M136 170h-34"/></g>
<g fill="{MUTED}" opacity=".8"><circle cx="470" cy="300" r="10"/><circle cx="500" cy="270" r="7"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('substantially', '棒が大きくのびて、量がぐっと増えるイラスト。', f"""
<path d="M60 340h480" class="a"/>
<g class="tealp o"><rect x="130" y="270" width="110" height="70"/></g>
<rect x="330" y="100" width="110" height="240" class="coral o"/>
<path d="M280 300v-180" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M130 270h330M330 100h180"/></g>
""", ground=False, arrow=True)

add('successful', '旗の立つ頂上に立って、やり終えたイラスト。', f"""
<path d="M0 400l220-260 110 130 90-90 180 220z" class="green o"/>
<g transform="translate(220 140)">
  <path d="M-4-70h8v70h-8z" class="ink"/>
  <path d="M4-66h70v40H4z" class="coralp o"/>
</g>
<g transform="translate(280 160) scale(0.7)">{person(0,60,1.0,1,'teal','blue','up','short','smile')}</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 130l20 20 34-40"/></g>
""", ground=False)

add('such', '同じ種類のものを、こういう類として示すイラスト。', f"""
<g transform="translate(170 230)">
  <circle r="80" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><rect x="300" y="130" width="230" height="200" rx="14"/></g>
<g class="coralp o"><circle cx="360" cy="190" r="34"/><circle cx="470" cy="190" r="34"/><circle cx="360" cy="280" r="34"/><circle cx="470" cy="280" r="34"/></g>
<path d="M260 230h30" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('suck', 'ストローで飲み物を吸い上げるイラスト。', f"""
<g transform="translate(330 280)">
  <path d="M-70-90h140l-14 170h-112z" fill="#f7fbfe" class="o"/>
  <path d="M-62-40h124l-10 120h-104z" class="bluep o"/>
  <path d="M20-150l30 10-50 220h-14z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
</g>
{face(160,180,70,'flat')}
<g transform="translate(160 220)"><ellipse rx="16" ry="12" fill="#8b4a3e"/></g>
<path d="M340 140q-80-20-140 30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('sudden', '何の前ぶれもなく、いきなり現れるイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12"><path d="M60 250h180"/></g>
<g transform="translate(370 230)">
  <path d="M0-140l34 80 84-20-56 68 56 68-84-20-34 80-34-80-84 20 56-68-56-68 84 20z" class="coral o"/>
  <path d="M-14-40h28v56h-28zM-14 30h28v24h-28z" fill="#fffdf6"/>
</g>
<path d="M250 250h40" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('sue', '訴状を法廷に持ち出して訴えるイラスト。', f"""
<g transform="translate(430 150)">
  <path d="M-90 40h180v20h-180z" class="goldd o"/>
  <path d="M-6-60h12v100h-12z" class="ink"/>
  <path d="M-70-60h140v10h-140z" class="ink"/>
  <g class="goldp o"><path d="M-70-50l-30 40h60z"/><path d="M70-50l-30 40h60z"/></g>
</g>
{person(160,346,1.15,1,'teal','blue','give','short','flat')}
<g transform="translate(290 260)">
  <path d="M-60-50h120v100h-120z" class="paper"/>
  <g fill="{INK}"><rect x="-36" y="-26" width="72" height="12"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-36 4h72M-36 26h50"/></g>
</g>
<path d="M240 200h100" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('suitable', '穴の形にぴたりと合う積み木のイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-220-30h440v70h-440z" fill="#dfe6ea" class="o"/>
  <path d="M-140-30h100v70h-100z" fill="#fffaf1"/>
  <path d="M60-30h100v70H60z" fill="#fffaf1"/>
  <path d="M60-30h100v70H60z" class="teal o"/>
</g>
<g transform="translate(-90+300 150)"><path d="M-50-35h100v70h-100z" class="teal o"/></g>
<path d="M210 200v40" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M420 150l20 20 34-40"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('summarize', '長い文書を短くまとめるイラスト。', f"""
<g transform="translate(160 220)">
  <path d="M-100-130h200v260h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-70 {-100+i*26}h140"/>' for i in range(9))}</g>
</g>
<g transform="translate(430 220)">
  <path d="M-100-90h200v180h-200z" class="paper"/>
  <g fill="{INK}"><rect x="-70" y="-50" width="140" height="12"/><rect x="-70" y="-10" width="120" height="12"/><rect x="-70" y="30" width="90" height="12"/></g>
</g>
<path d="M290 220h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('supervise', '作業を横から見て、監督するイラスト。', f"""
{person(150,346,1.2,1,'blue','blue','point','short','neutral')}
<g transform="translate(150 250)"><path d="M-40-30h80v10h-80z" class="paper"/></g>
{person(380,346,0.95,1,'teal','gold','reach','cap','neutral')}
{person(490,346,0.95,1,'coral','blue','carry','bob','neutral')}
<path d="M230 220h100" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round"><path d="M320 300l16 16 26-32"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('suppose', 'そうなるだろうと頭の中で仮に置くイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','think','short','neutral')}
<g transform="translate(420 190)">
  <path d="M-130-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-166q-38-4-26-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(-20 0)" opacity=".7">
    <path d="M-60-40h120v70h-120z" class="tealp o"/>
    <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="4" stroke-dasharray="8 6"><path d="M-60-40h120v70h-120z"/></g>
  </g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="280" cy="290" r="12"/><circle cx="256" cy="314" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('suppress', 'ふき出そうとする力をふたで押さえこむイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-100-40h200v100h-200z" fill="#dfe6ea" class="o"/>
  <g opacity=".7">{flame(0,-20,0.8)}</g>
  <path d="M-130-50h260v24h-260z" fill="#7f8ea6" stroke="{INK}" stroke-width="3"/>
</g>
{hand(300,150,1)}
<path d="M300 190v40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('surge', '波がどっと押し寄せて、量が跳ね上がるイラスト。', f"""
<path d="M60 340h480" class="a"/>
<g class="bluep o"><rect x="110" y="290" width="70" height="50"/><rect x="190" y="270" width="70" height="70"/><rect x="270" y="250" width="70" height="90"/></g>
<rect x="350" y="90" width="70" height="250" class="blue o"/>
<rect x="430" y="70" width="70" height="270" class="blue o"/>
<path d="M120 250q120-40 200-60t180-90" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('surround', '真ん中の一つを、ぐるりと取り囲むイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="40" class="coral o"/>
  <g class="teal o">{''.join(f'<circle cx="{int(130*__import__("math").cos(i*3.14159/4))}" cy="{int(130*__import__("math").sin(i*3.14159/4))}" r="26"/>' for i in range(8))}</g>
</g>
<circle cx="300" cy="220" r="170" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"/>
""", ground=False)

add('suspect', '相手をあやしいと思って目を向けるイラスト。', f"""
{person(160,346,1.15,1,'blue','blue','think','short','flat')}
{person(450,346,1.15,-1,'coral','gold','stand','cap','neutral')}
<g fill="{INK}" transform="translate(280 170)">
  <path d="M0 0q0-32 24-32t24 32q0 18-20 22v16h-12v-26q18-4 18-18t-10-12-12 18z"/>
  <rect x="14" y="52" width="12" height="12"/>
</g>
<path d="M230 250h140" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('suspend', '資格の札を外して、しばらく止めるイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-60h120M-60-20h120M-60 20h90"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M-60 90l60-60M0 90l-60-60"/></g>
</g>
<g transform="translate(430 210)">
  <circle r="80" class="mutedfill" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <g fill="{MUTED}"><rect x="-30" y="-40" width="22" height="80"/><rect x="8" y="-40" width="22" height="80"/></g>
</g>
<path d="M300 220h40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('sustain', '下から支え続けて、落とさないイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-110-60h220v90h-220z" class="gold o"/>
</g>
{hand(200,290,1)}{hand(400,290,-1)}
<g class="a" marker-end="url(#ar)"><path d="M200 360v-40M400 360v-40"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M500 160l20 20 34-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('swallow', '飲み込んだものが、のどを通って下りるイラスト。', f"""
{face(240,160,80,'flat')}
<g transform="translate(240 200)"><ellipse rx="20" ry="14" fill="#8b4a3e"/></g>
<g transform="translate(240 300)">
  <path d="M-30-80h60v160h-60z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3" opacity=".8"/>
  <circle cy="-30" r="18" class="coral o"/>
</g>
<path d="M340 220v90" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('swear', '片手を挙げて、うそはないと誓うイラスト。', f"""
{person(230,346,1.35,1,'blue','blue','up','short','neutral')}
<g transform="translate(430 220)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-60h120M-60-20h120"/></g>
  <path d="M-60 60q40-24 80 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M120 180l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('sweep', 'ほうきでごみを掃き寄せるイラスト。', f"""
{person(180,346,1.1,1,'teal','blue','reach','bob','neutral')}
<g transform="translate(300 300) rotate(26)">
  <path d="M-8-140h16v140h-16z" class="goldd o"/>
  <path d="M-40 0h80l16 60h-112z" fill="#d9b476" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="#c8c2b0" stroke="{INK}" stroke-width="2"><circle cx="430" cy="340" r="12"/><circle cx="470" cy="350" r="9"/><circle cx="500" cy="336" r="11"/></g>
<g class="a" marker-end="url(#ar)"><path d="M380 250h100"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('sweet', '砂糖菓子の甘さを、うれしそうに味わうイラスト。', f"""
{face(200,200,85,'smile')}
<g transform="translate(430 240)">
  <path d="M-60-60h120v120h-120z" class="coralp o"/>
  <path d="M-60-60h120v20h-120z" class="coral o"/>
  <g class="gold o"><circle cx="0" cy="-10" r="16"/></g>
</g>
<g class="golds" style="stroke-width:5"><path d="M300 160l26-20M310 200h30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('swing', 'ぶらんこが前後に揺れるイラスト。', f"""
<g transform="translate(300 150)">
  <path d="M-160 0h320" fill="none" stroke="{INK}" stroke-width="8"/>
  <g fill="none" stroke="{INK}" stroke-width="4"><path d="M-60 0v130M60 0v130"/></g>
  <path d="M-70 130h140v16h-140z" class="goldd o"/>
</g>
<g opacity=".3" transform="translate(300 150) rotate(-24)">
  <g fill="none" stroke="{INK}" stroke-width="4"><path d="M-60 0v130M60 0v130"/></g>
  <path d="M-70 130h140v16h-140z" class="goldd o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 340a200 200 0 0 1 40-60M420 340a200 200 0 0 0-40-60"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('tablet', '手のひらの錠剤と、板状の端末を並べたイラスト。', f"""
<g transform="translate(180 240)">
  <ellipse rx="70" ry="44" fill="#fffdf6" class="o"/>
  <path d="M0-44v88" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<g transform="translate(430 240)">
  <path d="M-100-130h200v260h-200z" fill="#2f4055"/>
  <path d="M-86-112h172v224h-172z" fill="#e8f4fb"/>
  <g class="teal o"><rect x="-60" y="-90" width="44" height="44"/><rect x="0" y="-90" width="44" height="44"/><rect x="-60" y="-34" width="44" height="44"/><rect x="0" y="-34" width="44" height="44"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tackle', '難しい問題に正面から取り組むイラスト。', f"""
{person(150,346,1.15,1,'coral','blue','point','short','flat')}
<g transform="translate(420 230)">
  <path d="M-110-110h220v220h-220z" fill="#dfe6ea" class="o"/>
  <g fill="{INK}"><path d="M-30-40q0-46 34-46t34 46q0 26-26 32v24h-18v-38q22-6 22-24t-14-18-16 24z"/><rect x="-4" y="46" width="18" height="18"/></g>
</g>
<path d="M240 220h60" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:5"><path d="M110 190l-24-18M116 240h-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('tag', '追いかけて相手にタッチする鬼ごっこのイラスト。', f"""
{person(180,346,1.15,1,'coral','blue','reach','short','smile')}
{person(400,346,1.15,1,'teal','gold','walk','bob','smile')}
{hand(300,250,1)}
<path d="M240 200h120" class="a" marker-end="url(#ar)"/>
<g class="muted"><path d="M480 250h60M470 300h60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('talented', '人並みはずれた腕前を見せるイラスト。', f"""
{person(200,346,1.3,1,'violet','blue','up','bob','smile')}
<g transform="translate(200 140)"><path d="M0-40l14 28 30 4-22 21 6 30-28-15-28 15 6-30-22-21 30-4z" class="gold o"/></g>
<g transform="translate(430 250)">
  <path d="M-90-60h180v140h-180z" class="paper"/>
  <path d="M-60 60l50-70 34 40 40-60 26 90z" class="tealp o"/>
</g>
<g class="golds" style="stroke-width:5"><path d="M300 190l-26-16M306 230h-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('talk', '向かい合って言葉をやりとりするイラスト。', f"""
{person(150,346,1.15,1,'teal','blue','stand','short','smile')}
{person(450,346,1.15,-1,'coral','gold','stand','bob','smile')}
<g fill="#fffdf6" stroke="{INK}" stroke-width="3">
  <path d="M210 130h130v60H210z"/><path d="M260 190l-14 26 34-26z"/>
  <path d="M370 200h130v60H370z"/><path d="M440 260l14 26-34-26z"/>
</g>
<g fill="{INK}"><rect x="230" y="152" width="90" height="14"/><rect x="390" y="222" width="90" height="14"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('teaching', '黒板の前で、教え伝えるイラスト。', f"""
<g transform="translate(390 200)">
  <path d="M-150-110h300v200h-300z" fill="#31473d" class="o"/>
  <g fill="none" stroke="#e9f3ec" stroke-width="4"><path d="M-110-60h180M-110-20h220M-110 20h150"/></g>
</g>
{person(140,346,1.1,1,'violet','blue','point','short','smile')}
<path d="M220 200h40" class="a" marker-end="url(#ar)"/>
<g opacity=".6">{person(300,366,0.6,1,'teal','gold','stand','bob','smile')}</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('temperature', '温度計の目盛りで暖かさを示したイラスト。', f"""
{thermometer(220,240,0.75,1.3)}
{sun(450,140,34)}
<g class="a" marker-end="url(#ar)"><path d="M330 300v-140"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('temporary', '仮に立てた小屋と、しっかりした建物を比べたイラスト。', f"""
<g transform="translate(170 280)">
  <path d="M0-110l110 110h-220z" class="goldp o"/>
  <g class="muted"><path d="M-60 20h120"/></g>
</g>
{building(430,300,1.0,'teal')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><rect x="60" y="140" width="230" height="200" rx="12"/></g>
<path d="M60 350h480" class="a"/>
""", ground=True)

add('tempt', 'おいしそうな菓子で、思わず手を伸ばさせるイラスト。', f"""
{person(160,346,1.15,1,'teal','blue','reach','short','smile')}
<g transform="translate(400 260)">
  <path d="M-90 60h180l-16-100h-148z" class="coralp o"/>
  <path d="M-60-40h120v-24h-120z" class="coral o"/>
  <g class="gold o"><circle cx="0" cy="-80" r="18"/></g>
</g>
<g class="golds" style="stroke-width:5"><path d="M300 180l-24-16M310 220h-30"/></g>
<path d="M240 280h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('terrify', '恐ろしいものを前に、こわくてすくむイラスト。', f"""
<g transform="translate(160 250)">
  <path d="M-90 110q-20-160 90-160t90 160z" fill="#41506a"/>
  <g fill="{TONES['coral'][0]}"><path d="M-40-50l30 20-30 20zM40-50l-30 20 30 20z"/></g>
  <path d="M-40 50q40 30 80 0" fill="none" stroke="#fffdf6" stroke-width="6"/>
</g>
{person(450,346,1.2,-1,'coral','gold','up','bob','surprised')}
{drop(500,240,0.8)}
<path d="M280 230h80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('testify', '証人台で、見たことを述べるイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-90-40h180v40h-180z" class="goldd o"/>
  <path d="M-70 0h140v60h-140z" class="goldp o"/>
</g>
<g transform="translate(300 190)">{person(0,60,1.05,1,'teal','blue','up','short','neutral')}</g>
<g transform="translate(300 130)">
  <path d="M-70-50h140v60h-140z" fill="#fffdf6" class="o"/>
  <path d="M-40 10l-14 28 40-28z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-46" y="-30" width="92" height="12"/></g>
</g>
{person(470,346,1.0,-1,'blue','blue','stand','bob','neutral')}
<path d="M60 366h480" class="a"/>
""", ground=True)
print(len(W), ' '.join(W)); print(sheet(W))
