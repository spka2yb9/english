"""第14回: 体験・感情・道具・空間など30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('arrange', 'ばらばらの本を、たなにきちんと並べ直しているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="tealp"/>
<g transform="translate(300 300)">
  <path d="M-180-20h360v20h-360z" class="goldp o"/>
  <g class="tealp o">
    <rect x="-160" y="-90" width="26" height="70"/><rect x="-128" y="-90" width="26" height="70"/>
    <rect x="-96" y="-90" width="26" height="70"/><rect x="-64" y="-90" width="26" height="70"/>
  </g>
  <g class="coralp o">
    <rect x="60" y="-84" width="26" height="64" transform="rotate(14 73 -52)"/>
    <rect x="110" y="-80" width="26" height="60" transform="rotate(-18 123 -50)"/>
  </g>
</g>
<path d="M110 180h380" class="muted"/>
{hand(230,180,1)}
<path d="M290 190h-30" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('conduct', '指揮棒を振って、楽団の演奏をまとめているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="violetp"/>
{person(200,346,1.2,1,'violet','blue','up','bun','neutral')}
<path d="M254 190l60-40" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
<g opacity=".85">
  {person(400,346,0.85,-1,'teal','gold','stand','short','neutral')}
  {person(490,346,0.85,-1,'coral','violet','stand','bob','neutral')}
</g>
<g fill="{INK}">
  <g transform="translate(340 210) scale(0.8)"><ellipse rx="12" ry="9" transform="rotate(-20)"/><path d="M10-4v-42h5v42z"/></g>
  <g transform="translate(400 170) scale(0.7)"><ellipse rx="12" ry="9" transform="rotate(-20)"/><path d="M10-4v-42h5v42z"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('entry', '受付を通って会場の中へ入り、名簿に記入するイラスト。', f"""
<g transform="translate(430 240)">
  <path d="M-90-120h180v240h-180z" fill="#e0d6c2" stroke="{INK}" stroke-width="3"/>
  <path d="M-40-30h80v150h-80z" class="goldd o"/>
</g>
{person(200,346,1.05,1,'teal','blue','walk','short','smile')}
<g transform="translate(300 250)">
  <path d="M-50-40h100v80h-100z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-30-16h60M-30 4h60"/></g>
</g>
<path d="M270 180h80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('ethical', '拾った財布を持ち主へ返して、正しい行いをするイラスト。', f"""
<circle cx="300" cy="120" r="66" class="greenp"/>
<g transform="translate(300 176)"><path d="M-30 20l30-40 30 40z" class="green o"/><path d="M-30 20h60" class="a"/></g>
{person(160,346,1.05,1,'teal','blue','give','short','smile')}
{person(440,346,1.05,-1,'coral','gold','give','bob','smile')}
<g transform="translate(300 280)">
  <path d="M-50-30h100v60h-100z" class="goldd o"/>
  <path d="M-50-6h100" fill="none" stroke="{TONES['gold'][1]}" stroke-width="5"/>
</g>
<path d="M234 280h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('exotic', '見慣れない形の果物と花が、南国の風景に並んでいるイラスト。', f"""
{sun(480,90,44)}
<g transform="translate(140 300)">
  <path d="M0 40V-60" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="12" stroke-linecap="round">
    <path d="M0-60q-60-20-80 10M0-60q60-20 80 10M0-60q-30-50-70-50M0-60q30-50 70-50"/>
  </g>
</g>
<g transform="translate(330 300)">
  <ellipse rx="46" ry="60" class="goldp o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="3"><path d="M-24-40q24 80 48 0M0-60v120"/></g>
  <path d="M0-60l-16-24 32 6z" class="green o"/>
</g>
<g transform="translate(470 300)">
  <circle r="26" class="violet o"/>
  <g class="coral o"><circle cx="-34" cy="-18" r="18"/><circle cx="34" cy="-18" r="18"/><circle cx="0" cy="-40" r="18"/><circle cx="-24" cy="20" r="18"/><circle cx="24" cy="20" r="18"/></g>
  <circle r="14" class="gold o"/>
</g>
""", ground=True)

add('expect', 'カレンダーの日付を見て、届く荷物を心待ちにしているイラスト。', f"""
{person(170,346,1.1,1,'teal','blue','think','short','smile')}
<g transform="translate(400 250)">
  <path d="M-110-100h220v200h-220z" class="paper"/>
  <path d="M-110-100h220v40h-220z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5">
    {''.join(f'<rect x="{-90 + i%5*38}" y="{-46 + i//5*40}" width="34" height="34"/>' for i in range(10))}
  </g>
  <circle cx="20" cy="26" r="20" class="coral o"/>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="250" cy="220" r="28"/></g>
{box(250,220,34,24,0,'gold')}
<path d="M290 220h40" class="muted" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('experience', '同じ作業を何度も繰り返して、手つきが慣れていくイラスト。', f"""
<g opacity=".4">{person(140,346,0.9,1,'coral','blue','point','short','neutral')}</g>
<g opacity=".7">{person(280,346,1.0,1,'coral','blue','point','short','neutral')}</g>
{person(440,346,1.1,1,'coral','blue','point','short','smile')}
<path d="M100 200h400" class="a" marker-end="url(#ar)"/>
{box(200,300,50,36,0,'gold')}
{box(350,300,50,36,0,'gold')}
{box(520,300,50,36,0,'gold')}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('experiment', '試験管の液体を混ぜて、結果を観察している実験のイラスト。', f"""
<g transform="translate(300 310)">
  <path d="M-220-20h440v20h-440z" fill="#dfe6ea" class="o"/>
</g>
<g transform="translate(200 250)">
  <path d="M-10-80h20v30l36 64H-46l36-64z" fill="#f4fbff" class="o"/>
  <path d="M-36 20h72l12 14H-48z" class="coralp o"/>
</g>
<g transform="translate(330 260)">
  <path d="M-14-90h28v76a14 14 0 0 1-28 0z" fill="#f4fbff" class="o"/>
  <path d="M-14-30h28v16a14 14 0 0 1-28 0z" class="greenp o"/>
</g>
<g transform="translate(420 210) rotate(140)">
  <path d="M-14-70h28v56a14 14 0 0 1-28 0z" fill="#f4fbff" class="o"/>
  <path d="M-14-30h28v16a14 14 0 0 1-28 0z" class="bluep o"/>
</g>
<path d="M370 200q30 20 40 40" class="blues" marker-end="url(#ar)"/>
<g class="muted" opacity=".8"><path d="M196 140q-14-30 4-52"/></g>
""", ground=True, arrow=True)

add('experimental', '試作段階の装置に、まだ調整中の札がついているイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-120-90h240v180h-240z" fill="#dfe6ea" class="o"/>
  <circle cx="-50" cy="-30" r="30" class="tealp o"/>
  <path d="M-50-30l18-20" class="a"/>
  <path d="M20-60h70v60H20z" class="coralp o"/>
  <path d="M-90 50h180" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="10 8"/>
</g>
<g transform="translate(440 170) rotate(14)">
  <path d="M-50-26h100v52h-100z" class="goldp o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"><path d="M-30-6h60M-30 10h40"/></g>
  <path d="M-50 0l-24-14v28z" class="goldp o"/>
</g>
""", ground=True)

add('expert', '長年の経験で、複雑な作業を難なくこなしている人のイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
{person(190,346,1.15,1,'teal','blue','point','cap','smile')}
<g transform="translate(380 250)">
  <path d="M-90-70h180v140h-180z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"><path d="M-60-40h120M-60-10h120M-60 20h90"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M290 160l18 18 30-36"/></g>
<g transform="translate(190 210)"><path d="M0-30l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" class="gold o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('faithful', '主人のそばを離れずに、ずっと付き添っている犬のイラスト。', f"""
{person(220,346,1.15,1,'teal','blue','stand','short','smile')}
<g transform="translate(400 300)">
  <ellipse cx="0" cy="20" rx="76" ry="42" class="goldp o"/>
  <path d="M-52 56v26M-16 60v22M28 60v22M60 52v30" fill="none" stroke="{TONES['gold'][2]}" stroke-width="13" stroke-linecap="round"/>
  <path d="M-76 8q-40 4-42 44" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10" stroke-linecap="round"/>
  <g transform="translate(84 -14)">
    <path d="M-30-28q30-22 60 0 16 16 12 40-4 26-42 26t-42-26q-4-24 12-40z" class="goldp o"/>
    <path d="M-34-30q-20-34 4-36 20-2 22 22z" class="goldd o"/>
    <path d="M30-32q22-32 40-12 14 16-6 32z" class="goldd o"/>
    <circle cx="6" cy="-4" r="3.4" class="ink"/><ellipse cx="42" cy="20" rx="9" ry="7" class="ink"/>
  </g>
</g>
<g transform="translate(310 200)"><path d="M0 20l-24-30 12-14 12 12 12-12 12 14z" class="coral o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('fear', '暗がりの中で身をすくめ、恐れている人のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#3a4a5c"/>
<g transform="translate(240 350)">{person(0,0,1.15,1,'coral','blue','up','short','sad')}</g>
<g fill="#22303e" stroke="#556777" stroke-width="3"><path d="M430 350q-30-80 30-120 50-34 90 10 40 44-10 110z"/></g>
<g fill="#f7e6a8"><circle cx="470" cy="250" r="8"/><circle cx="520" cy="250" r="8"/></g>
<g fill="none" stroke="#e8b4a8" stroke-width="4"><path d="M300 210q20-24 16-44M180 210q-20-24-16-44"/></g>
""", ground=False)

add('fight', '二人が向かい合って組み合い、争っているイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-140 0l60-30-20-50 60 26 20-56 24 54 56-24-18 52 60 10-52 30 40 44-60-8-8 56-40-46-46 38 8-56z" class="coralp o"/>
</g>
{person(190,346,1.1,1,'coral','blue','point','cap','sad')}
{person(410,346,1.1,-1,'blue','violet','point','short','sad')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('figure', '表の中に並んだ数字と、その大きさを示す棒グラフのイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-110-120h220v240h-220z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5"><path d="M-110-60h220M-110 0h220M-110 60h220M0-120v240"/></g>
  <g fill="{INK}">
    <rect x="-80" y="-96" width="40" height="8"/><rect x="30" y="-96" width="50" height="8"/>
    <rect x="-80" y="-36" width="40" height="8"/><rect x="30" y="-36" width="30" height="8"/>
  </g>
</g>
<g transform="translate(430 300)">
  <path d="M-90 0h180" class="a"/>
  <g class="tealp o"><rect x="-70" y="-60" width="34" height="60"/><rect x="-20" y="-110" width="34" height="110"/><rect x="30" y="-80" width="34" height="80"/></g>
</g>
""", ground=True)

add('fitness', '運動して体を鍛え、体力がついていくイラスト。', f"""
{person(220,346,1.25,1,'coral','blue','up','short','neutral')}
<g transform="translate(220 240)">
  <path d="M-110-14h220v20h-220z" class="ink"/>
  <circle cx="-130" cy="-4" r="26" class="ink"/><circle cx="130" cy="-4" r="26" class="ink"/>
</g>
<g transform="translate(450 250)">
  <path d="M-60 60h120" class="a"/>
  <g class="greenp o"><rect x="-46" y="10" width="26" height="50"/><rect x="-10" y="-30" width="26" height="90"/><rect x="26" y="-70" width="26" height="130"/></g>
</g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('flavor', '料理から立ちのぼる香りを、鼻で感じているイラスト。', f"""
<g transform="translate(240 300)">
  <ellipse rx="90" ry="30" fill="#fffdf6" class="o"/>
  <path d="M-70-10q70 26 140 0" fill="none" class="a"/>
  <g class="coralp o"><circle cx="-30" cy="-14" r="20"/><circle cx="10" cy="-8" r="20"/></g>
</g>
<g class="muted" opacity=".9"><path d="M210 240q-16-40 6-70M250 232q-16-44 8-76M290 244q-16-40 6-70"/></g>
<g transform="translate(430 230)">
  <circle r="52" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-10 10q10 12 20 0" fill="none" stroke="{INK}" stroke-width="3"/>
  <circle cx="-16" cy="-14" r="3.4" class="ink"/><circle cx="16" cy="-14" r="3.4" class="ink"/>
  <path d="M-4-4q-8 10 4 12" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<path d="M340 220q30-6 44 0" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('formal', 'きちんとした正装と、くだけた普段着を並べて比べたイラスト。', f"""
{person(170,346,1.15,1,'blue','blue','stand','short','neutral')}
<g transform="translate(170 268)">
  <path d="M-40-24h80v6h-80z" class="paper"/>
  <path d="M-12-20l12 18 12-18z" class="ink"/>
  <path d="M-44-20l14 90h-30zM44-20l-14 90h30z" class="blued o"/>
</g>
{person(430,346,1.15,1,'coral','gold','stand','bun','smile')}
<path d="M300 130v210" class="muted"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('functional', 'スイッチを入れると実際に動き出す機械のイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-120-90h240v180h-240z" fill="#dfe6ea" class="o"/>
  <circle cx="0" cy="-20" r="46" fill="none" stroke="{INK}" stroke-width="6"/>
  <g class="tealp o"><path d="M0-20q40-26 50 14-30 20-50-14z"/><path d="M0-20q-26 40-56 12 20-30 56-12z"/><path d="M0-20q-14-46 30-46 6 34-30 46z"/></g>
  <circle cx="0" cy="-20" r="10" class="teald o"/>
  <g class="green o"><circle cx="-80" cy="50" r="14"/></g>
  <path d="M40 40h60v24H40z" class="coral o"/>
</g>
<path d="M280 130a120 120 0 0 1 90 40" class="muted" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 300l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('fur', '柔らかい毛におおわれた動物の毛並みのイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g transform="translate(270 250)">
  <path d="M-130 60q-30-90 30-120 40-20 100-20t100 20q60 30 30 120z" class="goldp o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="3">
    {''.join(f'<path d="M{-110+i*24} 50q6-40 14-70"/>' for i in range(10))}
  </g>
  <g fill="{INK}"><circle cx="-30" cy="-40" r="4"/><circle cx="30" cy="-40" r="4"/></g>
  <path d="M-10-18q10 10 20 0" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
""", ground=True)

add('gap', '二つの板のあいだに空いた隙間を、矢印で示したイラスト。', f"""
<g class="tealp o"><path d="M40 130h200v140H40z"/><path d="M360 130h200v140H360z"/></g>
<path d="M250 200h100" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
<path d="M240 130v140M360 130v140" class="muted"/>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('garage', 'シャッターの開いた車庫に、車を入れているイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-180 120V-40h360v160z" fill="#fffdf6" class="o"/>
  <path d="M-196-40L0-130l196 90z" class="coral o"/>
  <path d="M-120 120V20h240v100z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-120 44h240M-120 68h240M-120 92h240"/></g>
</g>
<g transform="translate(300 330) scale(0.45)">
  <path d="M-150 40h300l-16-56h-50l-34-56h-120l-34 56h-62z" class="teal o"/>
  <circle cx="-84" cy="48" r="30" class="ink"/><circle cx="84" cy="48" r="30" class="ink"/>
</g>
<path d="M480 300h-80" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('glove', '指の形に分かれた手袋を、手にはめているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="violetp"/>
<g transform="translate(250 240)">
  <path d="M-46 60q-20-60 0-90 8-40 22-40t14 34v20q4-30 18-30t14 34v10q6-24 18-22t10 26q6-16 16-12t6 24q0 40-26 46z" class="violetp o"/>
  <path d="M-46 60h100v24h-100z" class="violetd o"/>
</g>
<g transform="translate(430 250) scale(-1 1)">
  <path d="M-46 60q-20-60 0-90 8-40 22-40t14 34v20q4-30 18-30t14 34v10q6-24 18-22t10 26q6-16 16-12t6 24q0 40-26 46z" class="violetp o"/>
  <path d="M-46 60h100v24h-100z" class="violetd o"/>
</g>
<path d="M120 340h360" class="a"/>
""", ground=True)

add('greet', '出会って手を上げ、あいさつを交わしている二人のイラスト。', f"""
<circle cx="300" cy="140" r="76" class="goldp"/>
{person(180,346,1.15,1,'teal','blue','up','short','smile')}
{person(420,346,1.15,-1,'coral','gold','up','bob','smile')}
<g transform="translate(300 180)">
  <path d="M-56-30h112q14 0 14 14v28q0 14-14 14h-70l-22 18 6-18h-26q-14 0-14-14v-28q0-14 14-14z" class="paper"/>
  <g fill="{MUTED}"><circle cx="-20" cy="-2" r="4"/><circle cx="0" cy="-2" r="4"/><circle cx="20" cy="-2" r="4"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('guide', '地図を示しながら、旅行者を目的地へ案内している人のイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','point','cap','smile')}
{person(430,346,0.95,-1,'coral','gold','walk','bob','smile')}
<g transform="translate(300 230)">
  <path d="M-70-50h140v100h-140z" class="paper"/>
  <path d="M-70 10q40-20 70 0t70-10" fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"/>
  <circle cx="40" cy="-20" r="10" class="coral o"/>
</g>
<path d="M240 170q60-30 110-10" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('handy', '小さくて持ち運びやすい道具が、すぐ手に取れるイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
{hand(200,240,1)}
<g transform="translate(330 240) rotate(-10)">
  <path d="M-60-20h100v40h-100z" class="goldd o"/>
  <path d="M40-26h34v52H40z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M440 210l18 18 30-36"/></g>
<path d="M120 340h360" class="a"/>
""", ground=True)

add('harsh', '強い風と砂が吹きつける、厳しい環境のイラスト。', f"""
<path d="M0 300q120-40 240-10t360-20v130H0z" fill="#d8c9ab" stroke="{INK}" stroke-width="3"/>
<g class="muted" opacity=".95">
  <path d="M40 90q140-40 240 0t280-20" marker-end="url(#ar)"/>
  <path d="M20 150q140-40 240 0t290-20" marker-end="url(#ar)"/>
  <path d="M40 210q140-40 240 0t280-20" marker-end="url(#ar)"/>
</g>
{person(300,320,1.0,1,'coral','blue','walk','cap','sad')}
<g fill="#c9b48c"><circle cx="160" cy="250" r="5"/><circle cx="420" cy="230" r="4"/><circle cx="500" cy="270" r="5"/></g>
""", ground=False, arrow=True)

add('heat', '火にかけたなべの温度が上がり、湯気が立つイラスト。', f"""
{thermometer(470,300,0.85,1.0)}
<g transform="translate(240 250)">
  <path d="M-100-40h200l-14 100h-172z" fill="#dfe6ea" class="o"/>
  <path d="M-114-40h228" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <path d="M-86-12h172l-10 72h-152z" class="bluep o"/>
</g>
{flame(240,346,0.9)}
<g class="muted" opacity=".85"><path d="M210 160q-16-40 6-70M270 156q-16-44 8-76"/></g>
<path d="M380 200v-50" class="corals" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('hit', 'バットがボールに当たって、勢いよく飛んでいくイラスト。', f"""
<g transform="translate(200 250) rotate(-30)">
  <path d="M-20-16h140q20 0 20 16t-20 16H-20z" class="goldd o"/>
  <path d="M-80-12h60v24h-60z" class="goldp o"/>
</g>
<g transform="translate(330 200)">
  <circle r="24" fill="#fffdf6" class="o"/>
  <path d="M-16-14q16 14 0 28M16-14q-16 14 0 28" fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M300 160l-20-24M366 166l24-24M300 240l-20 24"/></g>
<path d="M370 190q80-30 170 20" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('hold', '両手で箱をかかえて、落とさないように保っているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="tealp"/>
{person(280,346,1.25,1,'teal','blue','carry','short','neutral')}
{box(280,266,140,90,0,'gold')}
<path d="M210 266h140" fill="none" stroke="{TONES['gold'][2]}" stroke-width="6"/>
<g fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"><circle cx="200" cy="290" r="15"/><circle cx="360" cy="290" r="15"/></g>
<path d="M80 366h420" class="a"/>
""", ground=True)

add('hollow', '外から見ると詰まっているが、断面は中が空洞の丸太のイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-90-60h140v120h-140z" class="goldp o"/>
  <ellipse cx="-90" cy="0" rx="22" ry="60" class="gold o"/>
  <path d="M50-60h20v120H50z" class="goldd o"/>
</g>
<g transform="translate(420 250)">
  <ellipse rx="70" ry="80" class="goldp o"/>
  <ellipse rx="38" ry="46" fill="#3d4550" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M290 250h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('homeless', '家がなく、路上で荷物とともに過ごしている人のイラスト。', f"""
{building(120,300,0.7,'teal')}
<g class="muted"><path d="M240 300h300v40H240z"/></g>
{person(400,340,1.05,1,'gold','violet','sit' if 'sit' in POSES else 'stand','short','sad')}
{box(480,320,70,50,0,'gold')}
<g class="corals" style="stroke-width:7"><path d="M180 200l40 40M220 200l-40 40"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)
print(' '.join(W)); print(sheet(W))
