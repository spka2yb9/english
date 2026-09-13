"""第44回: 取り付け・機会・痛み・許可など40語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('mount', '壁に金具でパネルを取り付けるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-220-140h60v280h-60z" fill="#e4e9ee" class="o"/>
  <path d="M-160-70h40v140h-40z" fill="#c9d3dc" class="o"/>
  <path d="M-120-100h240v190h-240z" class="bluep o"/>
  <g fill="{INK}"><circle cx="-140" cy="-40" r="7"/><circle cx="-140" cy="40" r="7"/></g>
</g>
<g transform="translate(470 330) rotate(20)">
  <path d="M-10-70h20v90h-20z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <path d="M-20-90h40v22h-40z" class="coral o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('offend', 'とげのある言葉を投げて、相手を怒らせるイラスト。', f"""
{person(140,346,1.05,1,'teal','blue','point','short','neutral')}
<g transform="translate(300 190)">
  <path d="M-70-50l24 14-6-30 30 18 10-32 22 26 20-22 6 32 30-8-14 28 26 12-30 20h-118z" class="coralp o"/>
</g>
{person(480,346,1.1,-1,'coral','gold','stand','bob','sad')}
<g class="corals" style="stroke-width:5"><path d="M540 220q20 20 20 40"/></g>
<path d="M220 150h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('officer', '帽子と記章をつけた警官のイラスト。', f"""
{person(300,346,1.5,1,'blue','blue','stand','cap','neutral')}
<g transform="translate(300 232)">
  <path d="M-14-16l6 14 16 2-12 11 3 16-13-8-13 8 3-16-12-11 16-2z" class="gold o"/>
</g>
<g transform="translate(300 148)"><path d="M-40-8h80v10h-80z" class="bluep o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('oil', '缶からとろりと油をそそぐイラスト。', f"""
<g transform="translate(230 200) rotate(20)">
  <path d="M-70-50h120v100h-120z" fill="#c9d3dc" class="o"/>
  <path d="M50-30q70 6 96 40" fill="none" stroke="{INK}" stroke-width="10"/>
  <path d="M-40-70h60v20h-60z" fill="#dbe3ea" class="o"/>
</g>
<path d="M360 230q10 60 6 90" fill="none" stroke="{TONES['gold'][0]}" stroke-width="12" stroke-linecap="round"/>
<g class="gold o"><ellipse cx="366" cy="336" rx="80" ry="18"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('operate', 'レバーを入れて機械が動き出すイラスト。', f"""
<g transform="translate(340 230)">
  <path d="M-150-120h300v240h-300z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="12"><circle cx="-40" cy="-30" r="46"/><circle cx="60" cy="40" r="36"/></g>
  <g class="green o"><circle cx="100" cy="-80" r="14"/></g>
  <g transform="translate(-130 90)"><path d="M-8-70h16v70h-16z" class="coral o"/><circle cy="-76" r="14" class="coral o"/></g>
</g>
<g class="corals" style="stroke-width:4"><path d="M270 120q26-14 50 4M400 190q20 20 12 44"/></g>
{person(120,346,0.9,1,'teal','blue','reach','short','neutral')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('opportunity', '開いた戸の向こうに道があり、そこへ進むイラスト。', f"""
<g transform="translate(370 220)">
  <path d="M-90-150h180v300h-180z" fill="#e4e9ee" class="o"/>
  <path d="M-60-120h120v240h-120z" class="goldp o"/>
  <path d="M-60-120l-60-30v300l60-20z" fill="#f7e6bd" class="o"/>
</g>
{person(150,346,1.05,1,'teal','blue','walk','short','smile')}
<path d="M220 240h60" class="a" marker-end="url(#ar)"/>
{sun(500,110,26)}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('oppose', '出された案に手を上げて反対するイラスト。', f"""
{person(140,346,1.05,1,'blue','blue','give','short','neutral')}
<g transform="translate(300 210)">
  <path d="M-70-60h140v120h-140z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-46-30h92M-46 0h92M-46 30h60"/></g>
</g>
{person(470,346,1.1,-1,'coral','gold','up','bob','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M370 150l50 50M420 150l-50 50"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('opt', '二つの道のうち、一方を選んで進むイラスト。', f"""
{person(120,300,1.0,1,'teal','blue','walk','short','smile')}
<path d="M180 270q90 0 130-90h130" fill="none" stroke="{TONES['teal'][0]}" stroke-width="14" marker-end="url(#ar)"/>
<path d="M180 290q90 0 130 90h130" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 130l18 18 30-36"/></g>
<path d="M60 320h480" class="a"/>
""", ground=True, arrow=True)

add('option', '三つの選択肢が並び、一つに印がつくイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-130h360v260h-360z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><rect x="-140" y="-100" width="40" height="40"/><rect x="-140" y="-20" width="40" height="40"/><rect x="-140" y="60" width="40" height="40"/></g>
  <g fill="{MUTED}"><rect x="-80" y="-88" width="180" height="14"/><rect x="-80" y="-8" width="180" height="14"/><rect x="-80" y="72" width="180" height="14"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M-134-14l14 14 24-30"/></g>
</g>
""", ground=True)

add('original', '並んだもののうち、いちばん最初のものを示したイラスト。', f"""
<g class="tealp o"><rect x="250" y="200" width="90" height="110"/><rect x="360" y="200" width="90" height="110"/><rect x="470" y="200" width="90" height="110"/></g>
<rect x="110" y="180" width="100" height="130" class="coral o"/>
<g transform="translate(160 130)"><circle r="26" class="gold o"/><path d="M-4-14h8v28h-8z" fill="#fffdf6"/></g>
<path d="M230 260h30" class="a" marker-end="url(#ar)"/>
<path d="M60 330h480" class="a"/>
""", ground=True, arrow=True)

add('originate', '泉から水が湧き出し、川となって流れ出すイラスト。', f"""
<g transform="translate(140 230)">
  <path d="M-70 60q0-80 70-80t70 80z" fill="#cfe4d5" class="o"/>
  <circle cy="20" r="34" class="bluep o"/>
  {drop(0,-40,0.9)}
</g>
<path d="M180 280q120 40 180-10t200 20" fill="none" stroke="{TONES['blue'][0]}" stroke-width="20" stroke-linecap="round" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('ourselves', '自分たち全員が、自分たちを指さしているイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','point','short','smile')}
{person(300,346,1.15,1,'coral','gold','point','bob','smile')}
{person(430,346,1.15,1,'gold','blue','point','cap','smile')}
<path d="M170 170q130-40 260 0" fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M300 150v40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('outdoor', '木とテントのある野外のイラスト。', f"""
{sun(500,90,32)}
{tree(130,320,1.2)}
<g transform="translate(340 320)">
  <path d="M0-120l110 120h-220z" class="tealp o"/>
  <path d="M0-120l40 120h-80z" fill="#fffdf6" class="o"/>
</g>
{person(470,330,0.85,-1,'coral','blue','walk','bob','smile')}
<path d="M60 340h480" class="a"/>
""", ground=True)

add('outline', '中身を省いて、輪郭と見出しだけ示したイラスト。', f"""
<g transform="translate(170 220)">
  <path d="M-100-130h200v260h-200z" class="paper"/>
  <g fill="{MUTED}">{''.join(f'<rect x="-70" y="{-100+i*30}" width="140" height="12"/>' for i in range(7))}</g>
</g>
<g transform="translate(430 220)">
  <path d="M-100-130h200v260h-200z" class="paper"/>
  <g fill="{INK}"><rect x="-70" y="-100" width="100" height="14"/><rect x="-70" y="-30" width="100" height="14"/><rect x="-70" y="40" width="100" height="14"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-70h140M-70 0h140M-70 70h140"/></g>
</g>
<path d="M290 220h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('outrage', 'こぶしを上げて、みんなが激しく怒っているイラスト。', f"""
{person(160,346,1.15,1,'coral','blue','up','short','neutral')}
{person(300,346,1.2,1,'gold','blue','up','bob','neutral')}
{person(440,346,1.15,1,'coral','gold','up','cap','neutral')}
<g class="corals" style="stroke-width:5"><path d="M110 170q-20 20-20 44M490 170q20 20 20 44M300 130v-30"/></g>
<g transform="translate(300 110)"><path d="M-40 20q10-40 40-40t40 40z" class="coralp o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('outside', '建物の外に立っている人のイラスト。', f"""
<g transform="translate(220 250)">
  <path d="M-140-90h280v180h-280z" fill="#e4e9ee" class="o"/>
  <path d="M-140-90l0-30h280v30z" class="teal o"/>
  <path d="M-40 90V10h80v80z" class="goldd o"/>
</g>
{person(470,346,1.1,-1,'coral','blue','stand','short','neutral')}
<circle cx="470" cy="250" r="70" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('oven', '扉の中で熱を出しているオーブンのイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-150-130h300v260h-300z" fill="#dfe6ea" class="o"/>
  <path d="M-120-60h240v160h-240z" fill="#41506a" class="o"/>
  <path d="M-100-40h200v120h-200z" class="goldp o"/>
  <g fill="{INK}"><rect x="-120" y="-96" width="240" height="14"/><circle cx="90" cy="-104" r="12"/></g>
  <g class="corals" style="stroke-width:5"><path d="M-40 60q20-20 0-40M20 60q20-20 0-40"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('overcome', '高い壁をよじ登って乗りこえるイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-30-140h60v200h-60z" fill="#c9d3dc" class="o"/>
</g>
<g transform="translate(300 110) rotate(20)">{person(0,0,0.95,1,'teal','blue','up','short','smile')}</g>
<path d="M150 300q40-160 150-190t180 60" class="a" marker-end="url(#ar)"/>
<path d="M60 326h480" class="a"/>
""", ground=True, arrow=True)

add('overturn', 'コップをひっくり返して逆さにするイラスト。', f"""
<g transform="translate(170 260)">
  <path d="M-50-70h100l-10 130h-80z" fill="#f7fbfe" class="o"/>
  <path d="M-44-30h88l-8 90h-72z" class="bluep o"/>
</g>
<g transform="translate(440 260) rotate(180)">
  <path d="M-50-70h100l-10 130h-80z" fill="#f7fbfe" class="o"/>
</g>
<g class="bluep o"><ellipse cx="440" cy="322" rx="70" ry="14"/></g>
<path d="M250 150q90-40 150 10" class="a" marker-end="url(#ar)"/>
<path d="M60 330h480" class="a"/>
""", ground=True, arrow=True)

add('overwhelm', '大波にのみこまれそうな小さな人のイラスト。', f"""
<path d="M120 340q40-260 260-240 160 12 160 240z" class="blue o"/>
<path d="M180 340q30-190 200-176" fill="none" stroke="#fffdf6" stroke-width="10" opacity=".7"/>
{person(120,340,0.8,-1,'coral','gold','up','short','surprised')}
<path d="M300 90q-60 60-100 120" class="a" marker-end="url(#ar)"/>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('owe', '借りた分を返す義務があることを示したイラスト。', f"""
{person(140,346,1.05,1,'teal','blue','stand','short','sad')}
{person(470,346,1.05,-1,'blue','blue','reach','bob','neutral')}
<g transform="translate(300 200)">
  <path d="M-80-50h160v100h-160z" class="paper"/>
  <g fill="{INK}"><rect x="-50" y="-20" width="100" height="12"/><rect x="-50" y="10" width="60" height="12"/></g>
</g>
<path d="M220 280h160" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('pace', '同じ間隔の足あとと速度計で、進む速さを示したイラスト。', f"""
<g fill="{MUTED}" opacity=".8">
  <ellipse cx="90" cy="330" rx="18" ry="11"/><ellipse cx="170" cy="310" rx="18" ry="11"/><ellipse cx="250" cy="330" rx="18" ry="11"/><ellipse cx="330" cy="310" rx="18" ry="11"/><ellipse cx="410" cy="330" rx="18" ry="11"/>
</g>
<g transform="translate(300 180)">
  <path d="M-110 40a110 110 0 0 1 220 0z" fill="#f7fbfe" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-92 26l-18-6M0-70v-20M92 26l18-6"/></g>
  <path d="M0 36L60-20" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"/>
  <circle cy="36" r="10" class="ink"/>
</g>
<path d="M450 320h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('pain', 'ひざを痛めて、そこがずきずきするイラスト。', f"""
{person(230,346,1.4,1,'teal','blue','stand','short','sad')}
<g transform="translate(258 292)">
  <g class="coral o"><path d="M0-34l10 18 20-8-8 20 18 10-18 10 8 20-20-8-10 18-10-18-20 8 8-20-18-10 18-10-8-20 20 8z"/></g>
</g>
<g class="corals" style="stroke-width:5"><path d="M330 280q22 6 30 26M330 250q34 0 50 20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('painful', '指を打って、顔をしかめるほど痛いイラスト。', f"""
{face(190,190,80,'flat')}
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M150 160l34 12M230 160l-34 12"/></g>
<path d="M170 226q20 16 40 0" fill="none" stroke="{INK}" stroke-width="6"/>
<g transform="translate(400 250)">
  {hand(0,60,1)}
  <g transform="translate(0 -40) rotate(-20)"><path d="M-10-60h20v70h-20z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/><path d="M-40-80h80v26h-80z" class="ink"/></g>
  <g class="coral o"><path d="M60 30l8 16 18-8-8 18 16 10-16 8 8 18-18-8-8 16-8-16-18 8 8-18-16-8 16-10-8-18 18 8z"/></g>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('palace', '王冠をいただく、豪華な宮殿のイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-220-90h440v160h-440z" fill="#f4ead2" class="o"/>
  <path d="M-220-90h440v-24h-440z" class="goldd o"/>
  <g class="goldp o"><rect x="-190" y="-60" width="60" height="130"/><rect x="-30" y="-60" width="60" height="130"/><rect x="130" y="-60" width="60" height="130"/></g>
  <path d="M-70-90l70-90 70 90z" class="teal o"/>
</g>
<g transform="translate(300 150)"><path d="M-40 20l-8-50 24 20 24-34 24 34 24-20-8 50z" class="gold o"/></g>
<path d="M60 350h480" class="a"/>
""", ground=True)

add('pale', '濃い色が、だんだん薄くなっていくイラスト。', f"""
<rect x="90" y="180" width="105" height="140" fill="{TONES['teal'][2]}" class="o"/>
<rect x="195" y="180" width="105" height="140" fill="{TONES['teal'][0]}" class="o"/>
<rect x="300" y="180" width="105" height="140" fill="#9ed6ce" class="o"/>
<rect x="405" y="180" width="105" height="140" fill="{TONES['teal'][1]}" class="o"/>
<path d="M120 360h360" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('pants', '一枚のズボンのイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-110-140h220v60h-220z" class="bluep o"/>
  <path d="M-110-80h100l16 220h-90zM10-80h100l-26 220h-90z" class="blue o"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><path d="M-110-110h220"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('passenger', 'バスの座席にすわって運ばれる人たちのイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-230-110h460v190h-460z" class="goldp o"/>
  <g fill="#e8f4fb" stroke="{INK}" stroke-width="3"><rect x="-200" y="-80" width="110" height="80"/><rect x="-60" y="-80" width="110" height="80"/><rect x="80" y="-80" width="110" height="80"/></g>
  <circle cx="-140" cy="100" r="32" class="ink"/><circle cx="140" cy="100" r="32" class="ink"/>
</g>
<g transform="translate(0 0) scale(0.42)">
  {person(340,390,1.0,1,'teal','blue','stand','short','smile')}
  {person(670,390,1.0,1,'coral','gold','stand','bob','smile')}
  {person(1000,390,1.0,1,'violet','blue','stand','cap','smile')}
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('patient', 'ベッドで医師の診察を受けている患者のイラスト。', f"""
<g transform="translate(260 300)">
  <path d="M-160-30h320v40h-320z" fill="#fffdf6" class="o"/>
  <path d="M-160 10h20v50h-20zM140 10h20v50h-20z" fill="#c9d3dc" class="o"/>
  <path d="M-160-30h100v-50h-100z" fill="#e8f4fb" class="o"/>
  <path d="M-40-30h180v-24h-180z" class="tealp o"/>
  <circle cx="-108" cy="-64" r="22" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
{person(470,330,1.0,-1,'blue','blue','reach','bob','smile')}
<g transform="translate(470 250)"><path d="M-10-16h20v12h12v20h-12v12h-20v-12h-12v-20h12z" class="coral o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('pattern', '同じ形がくり返し並ぶ模様のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-210-140h420v280h-420z" fill="#fffdf6" class="o"/>
  <g class="tealp">{''.join(f'<circle cx="{-160+c*80}" cy="{-100+r*70}" r="24"/>' for r in range(4) for c in range(5))}</g>
  <g class="coralp">{''.join(f'<rect x="{-136+c*80}" y="{-76+r*70}" width="32" height="32"/>' for r in range(3) for c in range(4))}</g>
</g>
""", ground=True)

add('pause', '再生を一時とめた、ポーズ印のイラスト。', f"""
<g transform="translate(300 190)">
  <circle r="90" class="tealp o"/>
  <g class="teal"><rect x="-34" y="-44" width="24" height="88"/><rect x="10" y="-44" width="24" height="88"/></g>
</g>
<g transform="translate(300 330)">
  <path d="M-200-10h400v20h-400z" fill="#dfe6ea" class="o"/>
  <path d="M-200-10h180v20h-180z" class="teal"/>
  <circle cx="-20" r="18" class="coral o"/>
</g>
""", ground=True)

add('peace', 'オリーブの枝をくわえたハトのイラスト。', f"""
<g transform="translate(280 210)">
  <path d="M-90 20q-20-70 50-80 60-8 90 30l40-10-30 40q10 60-60 66-70 6-90-46z" fill="#fffdf6" class="o"/>
  <path d="M-20-20q40-30 80 10-40 30-80-10z" fill="#eef4f8" class="o"/>
  <circle cx="70" cy="-40" r="5" class="ink"/>
  <path d="M110-40l30-8-30 20z" class="gold o"/>
</g>
<g transform="translate(430 200)">
  <path d="M0 0q50 10 90 40" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
  <g class="green o"><ellipse cx="40" cy="14" rx="20" ry="11" transform="rotate(20 40 14)"/><ellipse cx="80" cy="34" rx="20" ry="11" transform="rotate(20 80 34)"/></g>
</g>
<path d="M120 340h360" class="a"/>
""", ground=True)

add('peaceful', '静かな野原で、のんびり過ごしているイラスト。', f"""
{sun(490,90,30)}
<g class="green o" opacity=".8"><path d="M0 330q120-60 300-40t300-20v90H0z"/></g>
{tree(120,320,1.0)}
{person(330,330,1.0,1,'teal','gold','stand','bob','smile')}
{cloud(230,110,1.0)}
<path d="M60 340h480" class="a"/>
""", ground=True)

add('penny', '手のひらにのる小さな硬貨のイラスト。', f"""
<g transform="translate(300 200)">
  <circle r="80" class="goldd o"/>
  <circle r="62" fill="#e5b56b" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-24" y="-8" width="48" height="16"/></g>
</g>
{hand(300,320,1)}
<path d="M120 380h360" class="a"/>
""", ground=True)

add('permission', '申請書に許可の印が押されるイラスト。', f"""
<g transform="translate(280 240)">
  <path d="M-160-140h320v280h-320z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-120-90h240M-120-40h240M-120 10h160"/></g>
  <g transform="translate(70 70) rotate(-12)">
    <circle r="54" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
    <path d="M-26 0l18 20 34-40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"/>
  </g>
</g>
<g transform="translate(490 150)"><path d="M-40-40h80v40h-80z" class="ink"/><path d="M-16-90h32v50h-32z" class="ink"/></g>
""", ground=True)

add('permit', '門が開いて、通ってよいと通されるイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-10-140h20v200h-20z" fill="#c9d3dc" class="o"/>
  <g transform="rotate(-70 0 -120)"><path d="M0-130h200v20H0z" class="coral o"/></g>
</g>
{person(180,346,1.0,1,'teal','blue','walk','short','smile')}
<path d="M250 300h180" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 160l18 18 30-36"/></g>
<path d="M60 326h480" class="a"/>
""", ground=True, arrow=True)

add('persist', '倒れても何度も立ち上がって、やり続けるイラスト。', f"""
<g opacity=".35" transform="rotate(-70 160 340)">{person(160,340,0.95,1,'teal','blue','stand','short','neutral')}</g>
<g opacity=".6" transform="rotate(-35 320 340)">{person(320,340,0.95,1,'teal','blue','stand','short','neutral')}</g>
{person(480,340,1.0,1,'teal','blue','stand','short','smile')}
<path d="M180 200q140-80 280-30" class="a" marker-end="url(#ar)"/>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('pet', '犬をなでてかわいがるイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','reach','bob','smile')}
<g transform="translate(400 300)">
  <ellipse rx="90" ry="52" class="goldd o"/>
  <circle cx="86" cy="-40" r="40" class="goldd o"/>
  <path d="M66-70q-16-30 6-34 16-2 18 24z" class="goldd o"/>
  <circle cx="100" cy="-46" r="5" class="ink"/>
  <path d="M-86-20q-30-30-10-40 16-8 22 26z" class="goldd o"/>
  <g class="goldd o"><rect x="-60" y="40" width="20" height="40"/><rect x="40" y="40" width="20" height="40"/></g>
</g>
<path d="M260 250q40-20 60 0" class="a" marker-end="url(#ar)"/>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('petrol', '給油ノズルから車に燃料を入れるイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-70-120h140v240h-140z" fill="#dfe6ea" class="o"/>
  <path d="M-46-96h92v70h-92z" class="tealp o"/>
  <path d="M70-40q60 0 60 60" fill="none" stroke="{INK}" stroke-width="8"/>
</g>
<g transform="translate(390 300)">
  <path d="M-130 20h260v-50l-60-40h-140l-60 40z" class="coralp o"/>
  <circle cx="-70" cy="26" r="26" class="ink"/><circle cx="70" cy="26" r="26" class="ink"/>
  <path d="M-120-30h60v-20h-60z" fill="#e8f4fb"/>
</g>
{drop(300,240,0.9,'gold')}
<path d="M60 340h480" class="a"/>
""", ground=True)

add('physics', 'ふりことりんごの落下で、物のはたらきを調べるイラスト。', f"""
<g transform="translate(200 130)">
  <path d="M-120 0h240" class="ink" stroke="{INK}" stroke-width="6"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><path d="M-60 0l-40 150M60 0l40 150"/></g>
  <circle cx="-100" cy="160" r="22" class="teal o"/>
  <circle cx="100" cy="160" r="22" class="teal o"/>
  <g class="muted"><path d="M-70 200q80 40 160 0"/></g>
</g>
<g transform="translate(470 180)">
  <circle r="30" class="coral o"/>
  <path d="M0-30v-16" fill="none" stroke="{TONES['green'][2]}" stroke-width="5"/>
</g>
<path d="M470 230v90" class="a" marker-end="url(#ar)"/>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
