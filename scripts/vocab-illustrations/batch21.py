"""第21回: 含む・確認・混雑・配達など30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('composer', '五線譜に音符を書き入れて、曲を作っている人のイラスト。', f"""
{person(160,346,1.15,1,'violet','blue','point','bun','neutral')}
<g transform="translate(400 230)">
  <path d="M-140-100h280v200h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-110 {-60+i*20}h220"/>' for i in range(5))}</g>
  <g fill="{INK}">
    <g transform="translate(-60 -40)"><ellipse rx="11" ry="8" transform="rotate(-20)"/><path d="M9-4v-38h4v38z"/></g>
    <g transform="translate(0 -20)"><ellipse rx="11" ry="8" transform="rotate(-20)"/><path d="M9-4v-38h4v38z"/></g>
    <g transform="translate(60 -40)"><ellipse rx="11" ry="8" transform="rotate(-20)"/><path d="M9-4v-38h4v38z"/></g>
  </g>
</g>
<path d="M240 200h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('concentrate', '周りを見ず、一点に注意を集めているイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','stand','short','neutral')}
<g transform="translate(420 220)">
  <circle r="90" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 8"/>
  <circle r="50" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
  <circle r="16" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5"><path d="M240 210h130" marker-end="url(#ar)"/></g>
<g class="muted" opacity=".6"><path d="M300 100h180M300 350h180"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('confirm', '予約の内容を照らし合わせて、間違いないと確かめるイラスト。', f"""
<g transform="translate(200 230)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-70h120M-60-40h120M-60-10h90"/></g>
</g>
<g transform="translate(410 230)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-70h120M-60-40h120M-60-10h90"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="10" stroke-linecap="round"><path d="M270 300l24 24 40-48"/></g>
<path d="M300 160h-20M320 160h20" class="a"/>
""", ground=True)

add('confuse', '道しるべが四方を指していて、どちらか分からず迷うイラスト。', f"""
{person(200,346,1.2,1,'coral','blue','think','short','sad')}
<g transform="translate(430 240)">
  <path d="M-8-120h16v240H-8z" class="goldd o"/>
  <g class="goldp o">
    <path d="M8-100h100l-20 20 20 20H8z"/>
    <path d="M-8-40h-100l20 20-20 20h100z"/>
    <path d="M8 20h100l-20 20 20 20H8z"/>
  </g>
</g>
<g fill="{INK}"><path d="M290 170q0-26 26-26t26 26q0 18-20 24v12h-12v-20q20-2 20-16 0-12-14-12t-14 12z"/><circle cx="316" cy="236" r="7"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('connected', '二つの機器がケーブルでつながっているイラスト。', f"""
<g transform="translate(150 240)">
  <path d="M-70-70h140v140h-140z" fill="#dfe6ea" class="o"/>
  <path d="M-46-46h92v70h-92z" class="bluep o"/>
</g>
<g transform="translate(450 240)">
  <path d="M-70-70h140v140h-140z" fill="#dfe6ea" class="o"/>
  <path d="M-46-46h92v70h-92z" class="bluep o"/>
</g>
<path d="M220 260q80 60 160 0" fill="none" stroke="{TONES['teal'][0]}" stroke-width="10"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M280 150l18 18 30-36"/></g>
""", ground=True)

add('consider', '二つの案を並べて、どちらがよいか考えているイラスト。', f"""
{person(300,346,1.2,1,'teal','blue','think','short','neutral')}
<g transform="translate(140 200)">
  <path d="M-70-60h140v120h-140z" class="tealp o"/>
</g>
<g transform="translate(460 200)">
  <path d="M-70-60h140v120h-140z" class="coralp o"/>
</g>
<g class="muted" marker-end="url(#ar)"><path d="M260 240q-60-20-90-20"/><path d="M340 240q60-20 90-20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('consist', '三つの部品が集まって、一つの全体をつくっているイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-110-90h220v180h-220z" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="12 8"/>
  <path d="M-90-70h80v70h-80z" class="teal o"/>
  <path d="M10-70h80v70h-80z" class="coral o"/>
  <path d="M-90 10h180v60h-180z" class="gold o"/>
</g>
<path d="M120 360h360" class="a"/>
""", ground=True)

add('contain', '箱の中に品物が入っていることを、断面で示したイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-140-90h280v180h-280z" class="goldp o"/>
  <path d="M-140-90h280v180h-280z" fill="none" class="a"/>
  <g class="tealp o"><circle cx="-70" cy="20" r="34"/><circle cx="0" cy="30" r="34"/><circle cx="70" cy="20" r="34"/></g>
  <path d="M-140-90l40-30h280l-40 30z" class="gold o"/>
</g>
<path d="M120 360h360" class="a"/>
""", ground=True)

add('content', '箱を開けて、中身をすべて取り出して見せているイラスト。', f"""
<g transform="translate(180 290)">
  <path d="M-90-60h180v120h-180z" class="goldp o"/>
  <path d="M-90-60l-30-40h180l-30 40" fill="none" class="a"/>
</g>
<g transform="translate(420 300)">
  <g class="tealp o"><rect x="-90" y="-40" width="60" height="60"/><rect x="-20" y="-30" width="50" height="50"/></g>
  <circle cx="60" cy="-10" r="30" class="coralp o"/>
</g>
<path d="M290 250h60" class="a" marker-end="url(#ar)"/>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('convince', '証拠を示して、相手を納得させているイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','point','short','neutral')}
{person(440,346,1.1,-1,'coral','gold','stand','bob','smile')}
<g transform="translate(300 240)">
  <path d="M-70-70h140v140h-140z" class="paper"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"><path d="M-40-40h80M-40-14h80"/></g>
  <path d="M-40 20l50 30 40-50" fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 180l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('counterpart', '左右に同じ役目のものが一つずつ、対になって並ぶイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
  <circle r="40" class="teal o"/>
</g>
<g transform="translate(420 230)">
  <path d="M-80-80h160v160h-160z" class="coralp o"/>
  <circle r="40" class="coral o"/>
</g>
<path d="M270 230h60" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
<path d="M120 360h360" class="a"/>
""", ground=True, arrow=True)

add('coverage', '報道の記者たちが、現場を取り囲んで伝えているイラスト。', f"""
{building(300,240,0.7,'teal')}
{person(140,346,0.95,1,'coral','blue','hold','cap','neutral')}
{person(460,346,0.95,-1,'violet','gold','hold','bob','neutral')}
<g transform="translate(190 250)"><path d="M-30-20h60v40h-60z" class="ink"/><circle r="12" fill="#dfe6ea" stroke="{INK}" stroke-width="2.5"/></g>
<g transform="translate(410 250)"><path d="M-30-20h60v40h-60z" class="ink"/><circle r="12" fill="#dfe6ea" stroke="{INK}" stroke-width="2.5"/></g>
<g class="corals" opacity=".8" style="stroke-width:4"><path d="M240 200q30-20 60-20M360 200q-30-20-60-20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('crazy', '危ない高さから飛び降りようとしている、無謀な行動のイラスト。', f"""
<path d="M60 340h200v60H60z" class="ground"/>
<path d="M60 340h200" class="a"/>
<path d="M260 130h40v210h-40z" class="goldd o"/>
{person(280,130,0.85,1,'coral','blue','up','short','surprised')}
<path d="M330 180q80 60 100 150" class="muted" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:7"><path d="M470 200l40 40M510 200l-40 40"/></g>
""", ground=False, arrow=True)

add('critic', '作品を前にして、厳しく評価を述べている人のイラスト。', f"""
<g transform="translate(420 220)">
  <path d="M-100-100h200v200h-200z" class="goldd o"/>
  <path d="M-84-84h168v168h-168z" class="paper"/>
  <path d="M-56 50l46-80 36 44 36-54 26 90z" class="tealp o"/>
</g>
{person(150,346,1.15,1,'violet','blue','point','short','sad')}
<g transform="translate(260 200)">
  <path d="M-50-30h100q12 0 12 12v30q0 12-12 12h-70l-20 16 4-16q-12 0-12-12v-30q0-12 12-12z" class="paper"/>
  <path d="M-6-16h12v26h-12zM-6 16h12v10h-12z" class="coral o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('crowded', '狭い場所に人がぎっしり集まっているイラスト。', f"""
<g class="tealp o">
  {''.join(f'<g transform="translate({70+ (i%9)*62} {200 + (i//9)*70})"><circle cy="-24" r="18"/><path d="M-22 34q0-34 22-34t22 34z"/></g>' for i in range(27))}
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M40 150h520M40 380h520"/></g>
""", ground=False)

add('crystal', '透明で角のそろった結晶のイラスト。', f"""
<circle cx="470" cy="96" r="54" class="bluep"/>
<g transform="translate(280 230)">
  <path d="M0-130l70 50v100l-70 50-70-50V-80z" fill="#e8f4fb" class="o"/>
  <path d="M0-130v230M-70-80l140 100M70-80L-70 20" fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"/>
</g>
<g class="blues" style="stroke-width:4"><path d="M160 130l-24-24M400 130l24-24M150 240h-30"/></g>
""", ground=True)

add('curly', 'くるくると巻いた髪の人と、まっすぐな髪の人を並べたイラスト。', f"""
{person(190,346,1.2,1,'teal','blue','stand','curl' if 'curl' in HAIRS else 'bob','smile')}
<g transform="translate(190 230)">
  <g fill="{HAIR}"><circle cx="-30" cy="-14" r="14"/><circle cx="-10" cy="-28" r="14"/><circle cx="12" cy="-30" r="14"/><circle cx="32" cy="-16" r="14"/></g>
</g>
{person(420,346,1.2,1,'coral','gold','stand','bob','smile')}
<path d="M300 130v220" class="muted"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('currently', '時計の針が今の時刻を指していることを示すイラスト。', f"""
<g transform="translate(300 200)">
  <circle r="120" fill="#fffdf6" stroke="{INK}" stroke-width="4"/>
  <path d="M0 0v-80M0 0l56 34" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M0 -120v-14" transform="rotate({i*30})"/>' for i in range(12))}</g>
  <circle r="10" class="coral o"/>
</g>
<path d="M300 350v-40" class="a" marker-end="url(#ar)" transform="rotate(180 300 330)"/>
""", ground=False, arrow=True)

add('cutting', '新聞から記事を切り抜いた紙片のイラスト。', f"""
<g transform="translate(220 240)">
  <path d="M-120-120h240v240h-240z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-90 {-90+i*30}h180"/>' for i in range(7))}</g>
  <path d="M-40-60h120v90h-120z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"/>
</g>
<g transform="translate(440 240) rotate(8)">
  <path d="M-60-46h120v92h-120z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-40-20h80M-40 4h60"/></g>
</g>
<path d="M340 240h30" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('daily', 'カレンダーの毎日に同じ印がついているイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <path d="M-180-140h360v50h-360z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5">
    {''.join(f'<rect x="{-160 + (i%7)*46}" y="{-70 + (i//7)*52}" width="42" height="46"/>' for i in range(21))}
  </g>
  <g fill="{TONES['coral'][0]}">
    {''.join(f'<circle cx="{-139 + (i%7)*46}" cy="{-47 + (i//7)*52}" r="10"/>' for i in range(21))}
  </g>
</g>
""", ground=True)

add('dead', '枯れて葉の落ちた木のイラスト。', f"""
<g transform="translate(280 340)">
  <path d="M-10 0v-160h20V0z" fill="#a08b62" stroke="{INK}" stroke-width="3"/>
  <path d="M0-120l-70-50M0-100l70-40M0-140l-40-60M0-150l50-50" fill="none" stroke="#a08b62" stroke-width="10" stroke-linecap="round"/>
</g>
<g fill="#c9b48c"><path d="M420 330q-20 10-20 20 20 4 20-20z"/><path d="M180 340q-20 10-20 20 20 4 20-20z"/></g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('decorate', '飾りをつけて、部屋をにぎやかに整えているイラスト。', f"""
<path d="M60 130q120 60 240 0t240 40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g>
  {''.join(f'<g transform="translate({110+i*80} {170 + (0 if i%2 else 20)})"><path d="M0-20l-16 26h32z" class="{["coral","gold","teal","violet"][i%4]} o"/></g>' for i in range(6))}
</g>
{person(200,346,1.1,1,'teal','blue','up','bob','smile')}
{tree(460,346,0.7)}
<g class="golds" style="stroke-width:4"><path d="M460 240l24-24M420 260h-24"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('deficiency', '必要な量に届かず、目盛りが不足を示しているイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-80-130h160l-10 250h-140z" fill="#f7fbfe" class="o"/>
  <path d="M-64 40h128l-6 80h-116z" class="bluep o"/>
  <path d="M-64 40h128" class="a"/>
  <path d="M-80-60h160" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"/>
</g>
<path d="M420 190v100" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:6"><path d="M460 150l30 30M490 150l-30 30"/></g>
""", ground=True, arrow=True)

add('deficit', '収入より支出が多く、差が赤くなっているイラスト。', f"""
<path d="M60 340h480" class="a"/>
<rect x="150" y="200" width="90" height="140" class="tealp o"/>
<rect x="340" y="130" width="90" height="210" class="coral o"/>
<path d="M240 165h100" class="muted"/>
<path d="M480 130v70" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
<g fill="{TONES['coral'][0]}"><rect x="490" y="240" width="40" height="8"/></g>
""", ground=False, arrow=True)

add('delay', '予定の時刻より遅れて、到着が後ろにずれるイラスト。', f"""
<path d="M60 200h480" class="a"/>
<g fill="{INK}"><circle cx="220" cy="200" r="10"/></g>
<circle cx="420" cy="200" r="10" class="coral o"/>
<path d="M230 260h180" class="a" marker-end="url(#ar)"/>
<g transform="translate(220 140)"><path d="M-30-30h60v20h-60z" class="muted"/></g>
<g transform="translate(420 140)">
  <circle r="28" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0v-18M0 0l14 8" class="a"/>
</g>
""", ground=False, arrow=True)

add('deliver', '玄関先まで荷物を届けているイラスト。', f"""
{building(450,300,0.9,'teal')}
{person(200,346,1.1,1,'coral','blue','carry','cap','smile')}
{box(200,266,100,70,0,'gold')}
<path d="M280 220h80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('demonstration', '人前で使い方を実演して見せているイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','point','bun','neutral')}
<g transform="translate(300 260)">
  <path d="M-70-40h140v100h-140z" class="tealp o"/>
  <path d="M-70-40h140" class="a"/>
  <circle cy="-70" r="16" class="coral o"/>
  <path d="M0-54v14" class="a"/>
</g>
<g opacity=".8">{person(450,346,0.85,-1,'violet','gold','stand','short','smile')}{person(530,346,0.85,-1,'coral','teal','stand','bob','smile')}</g>
<path d="M240 200h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('depend', '一本の支柱に、上の板が頼って支えられているイラスト。', f"""
<path d="M120 200h360v30H120z" class="tealp o"/>
<path d="M290 230v130h20V230z" class="goldd o"/>
<path d="M120 360h360" class="a"/>
<g class="corals" style="stroke-width:5"><path d="M300 240v100"/></g>
<path d="M520 240v100" class="a" marker-end="url(#ar)" transform="rotate(180 520 290)"/>
""", ground=True, arrow=True)

add('deposit', '銀行の窓口にお金を預けているイラスト。', f"""
<g transform="translate(420 250)">
  <path d="M-120-120h240v240h-240z" fill="#dfe6ea" class="o"/>
  <path d="M-90-90h180v70h-180z" class="bluep o"/>
  <path d="M-60 40h120v20h-120z" class="ink"/>
</g>
{person(160,346,1.1,1,'coral','blue','give','bob','neutral')}
<g transform="translate(270 260)">
  <path d="M-40-20h80v40h-80z" class="greenp o"/>
  <circle r="10" class="green o"/>
</g>
<path d="M320 210h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('descent', '斜面を下へ降りていく動きを、矢印で示したイラスト。', f"""
<path d="M60 120L540 340H60z" class="tealp o"/>
<path d="M60 120L540 340" class="a"/>
{person(180,200,0.75,1,'coral','blue','walk','short','neutral')}
<path d="M240 200L420 290" class="a" marker-end="url(#ar)"/>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('describe', '見たものの特徴を、言葉で細かく伝えているイラスト。', f"""
{person(160,346,1.15,1,'teal','blue','point','short','neutral')}
<g transform="translate(330 190)">
  <path d="M-90-50h180q16 0 16 16v56q0 16-16 16h-120l-26 22 6-22h-40q-16 0-16-16v-56q0-16 16-16z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-20h120M-60 4h90"/></g>
</g>
<g transform="translate(490 300)">
  <path d="M-60-60h120v120h-120z" class="coralp o"/>
  <circle r="26" class="coral o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('destroy', '建物が壊されて、がれきになっているイラスト。', f"""
<g transform="translate(180 300)">
  <path d="M-90 40V-60h180V40z" fill="#fffdf6" class="o"/>
  <path d="M-104-60L0-130l104 70z" class="teal o"/>
</g>
<g transform="translate(430 330)">
  <g fill="#cfc7b8" stroke="{INK}" stroke-width="2.5">
    <path d="M-70 10q-14-30 10-40 26-10 46 4 20 14 12 36z"/>
    <path d="M20 10q-10-22 8-30 18-8 32 4 12 10 6 26z"/>
    <path d="M-40 30h100v10h-100z"/>
  </g>
  <path d="M-60-30h50v-40h-50z" class="tealp o" transform="rotate(20 -35 -50)"/>
</g>
<path d="M290 240h60" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:6"><path d="M300 170l40 40M340 170l-40 40"/></g>
""", ground=True, arrow=True)
print(' '.join(W)); print(sheet(W))
