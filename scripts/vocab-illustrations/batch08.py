"""第8回: 高低・生き物・道具・職業などの30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('close', '開いていた本を、手でぱたんと閉じているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="tealp"/>
<g transform="translate(280 280)">
  <path d="M0 0q-60-30-124-10v-96q64-20 124 10z" class="tealp o"/>
  <path d="M0 0q30-16 66-18l50-70q-56-4-116 32z" class="tealp o" transform="rotate(-28 0 0)"/>
  <path d="M0-96v96" class="a"/>
</g>
<path d="M330 130q40 40 20 90" class="a" marker-end="url(#ar)"/>
{hand(390,150,-1)}
""", ground=True, arrow=True)

add('cooker', '台所の調理器の上でなべを火にかけているイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-160-40h320v100h-320z" fill="#dfe6ea" class="o"/>
  <path d="M-160-40h320" class="a"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><circle cx="-90" cy="-70" r="34"/><circle cx="20" cy="-70" r="34"/></g>
  <g class="coral o"><circle cx="90" cy="20" r="16"/><circle cx="130" cy="20" r="16"/></g>
</g>
<g transform="translate(210 210)">
  <path d="M-70-30h140l-10 60h-120z" fill="#eef4f8" class="o"/>
  <path d="M-84-30h168" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <path d="M0-30v-14" class="a"/>
</g>
{flame(320,262,0.7)}
<g class="muted" opacity=".8"><path d="M190 150q-14-30 4-52M230 146q-14-34 6-56"/></g>
""", ground=True)

add('distinguish', '見た目のよく似た二つの葉の、形の違いを見分けているイラスト。', f"""
<circle cx="300" cy="180" r="150" class="greenp" opacity=".5"/>
<g transform="translate(190 200)">
  <path d="M0-90C60-70 66 30 0 90-66 30-60-70 0-90z" class="green o"/>
  <path d="M0-90V90" fill="none" stroke="#e1f3e5" stroke-width="5"/>
</g>
<g transform="translate(410 200)">
  <path d="M0-90C70-64 60 20 0 90-60 20-70-64 0-90z" class="green o"/>
  <path d="M0-90V90" fill="none" stroke="#e1f3e5" stroke-width="5"/>
  <path d="M-46-20q46-16 92 0M-40 30q40-14 80 0" fill="none" stroke="#e1f3e5" stroke-width="4"/>
</g>
<path d="M300 340V240" class="a"/>
<path d="M300 300h-70M300 300h70" class="a" marker-end="url(#ar)"/>
<circle cx="300" cy="360" r="30" fill="none" stroke="{INK}" stroke-width="5"/>
<path d="M322 382l24 20" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
""", ground=False, arrow=True)

add('dressed', '上着とくつをきちんと身につけて、身支度を終えた人のイラスト。', f"""
<circle cx="470" cy="100" r="56" class="violetp"/>
{person(300,340,1.3,1,'violet','blue','stand','short','smile')}
<g transform="translate(300 250)">
  <path d="M-42-20h84v10h-84z" class="paper"/>
  <path d="M-10-24l10 16 10-16z" class="coral o"/>
</g>
<g class="ink"><rect x="264" y="338" width="30" height="14" rx="4"/><rect x="306" y="338" width="30" height="14" rx="4"/></g>
<path d="M120 200q-30 60-10 120" class="muted"/>
<path d="M100 140h60v50h-60z" class="muted"/>
""", ground=True)

add('fail', '積み木の塔が崩れて、目標の高さに届かなかったイラスト。', f"""
<path d="M120 120h360" class="muted"/>
{box(200,300,80,60,0,'gold')}
{box(200,242,80,60,0,'gold')}
<g transform="rotate(34 340 300)">{box(340,300,80,60,0,'gold')}</g>
<g transform="rotate(-60 420 330)">{box(420,330,80,60,0,'gold')}</g>
<g class="corals" style="stroke-width:9"><path d="M270 160l50 50M320 160l-50 50"/></g>
<path d="M200 200v-60" class="muted" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('handle', 'なべの取っ手を握って、しっかり持ち上げているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="goldp"/>
<g transform="translate(320 270)">
  <path d="M-110-40h220l-16 100h-188z" fill="#dfe6ea" class="o"/>
  <path d="M-110-40h220" class="a"/>
  <path d="M-110-30q-70 0-70 24t70 24" fill="none" stroke="{INK}" stroke-width="14"/>
</g>
{hand(190,250,1)}
<path d="M190 170v40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('high', 'とても高い所にある旗と、地上からの高さを示す長い矢印のイラスト。', f"""
<path d="M420 340V70" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<path d="M428 76l90 26-90 26z" class="coral o"/>
<path d="M200 340V80" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
{person(110,340,0.8,1,'teal','blue','up','short','neutral')}
<path d="M60 340h500" class="a"/>
""", ground=True, arrow=True)

add('low', '地面のすぐ近くにある旗と、短い高さを示す矢印のイラスト。', f"""
<path d="M420 340v-70" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<path d="M428 276l70 20-70 20z" class="coral o"/>
<path d="M200 340v-64" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
{person(110,340,0.8,1,'teal','blue','point','short','neutral')}
<path d="M60 340h500" class="a"/>
""", ground=True, arrow=True)

add('insect', '六本の足と触角を持つ昆虫を、上から見たイラスト。', f"""
<circle cx="470" cy="100" r="56" class="greenp"/>
<g transform="translate(280 210)">
  <ellipse cy="60" rx="54" ry="76" class="teal o"/>
  <ellipse cy="-20" rx="40" ry="34" class="teald o"/>
  <circle cy="-70" r="30" class="teald o"/>
  <path d="M-14-92q-24-40-48-46M14-92q24-40 48-46" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <circle cx="-62" cy="-138" r="7" class="ink"/><circle cx="62" cy="-138" r="7" class="ink"/>
  <g fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round">
    <path d="M-40-20l-70-30M40-20l70-30M-50 30l-84 6M50 30l84 6M-46 90l-76 40M46 90l76 40"/>
  </g>
  <path d="M0-16v130" fill="none" stroke="{TONES['teal'][2]}" stroke-width="3"/>
</g>
""", ground=True)

add('knife', '刃と柄がはっきり分かれたナイフのイラスト。', f"""
<circle cx="120" cy="100" r="56" class="tealp"/>
<g transform="translate(300 220) rotate(-18)">
  <path d="M-190-30h230l40 30-40 30h-230z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <path d="M-190-30h230l40 30h-270z" fill="#f7fbfe"/>
  <path d="M-300-24h114v48h-114q-14 0-14-14v-20q0-14 14-14z" class="goldd o"/>
  <g fill="{INK}"><circle cx="-260" cy="0" r="5"/><circle cx="-220" cy="0" r="5"/></g>
</g>
<path d="M120 330h360" class="a"/>
""", ground=True)

add('lab', '実験台の上にフラスコと試験管が並んだ実験室のイラスト。', f"""
<g transform="translate(300 310)">
  <path d="M-220-20h440v20h-440z" fill="#dfe6ea" class="o"/>
  <path d="M-200 0v70M200 0v70" fill="none" stroke="{MUTED}" stroke-width="10"/>
</g>
<g transform="translate(180 250)">
  <path d="M-10-70h20v30l40 70h-100l40-70z" fill="#f4fbff" class="o"/>
  <path d="M-46 20h92l14 10h-120z" class="bluep o"/>
  <path d="M-34 0h68l12 20h-92z" class="bluep o"/>
</g>
<g transform="translate(320 260)">
  <path d="M-14-80h28v70a14 14 0 0 1-28 0z" fill="#f4fbff" class="o"/>
  <path d="M-14-20h28v10a14 14 0 0 1-28 0z" class="coralp o"/>
</g>
<g transform="translate(400 260)">
  <path d="M-14-80h28v70a14 14 0 0 1-28 0z" fill="#f4fbff" class="o"/>
  <path d="M-14-40h28v30a14 14 0 0 1-28 0z" class="greenp o"/>
</g>
<g class="muted" opacity=".8"><path d="M170 160q-14-30 4-52"/></g>
""", ground=True)

add('lead', '先頭に立つ人が、後ろの列を引き連れて進んでいくイラスト。', f"""
{person(180,336,1.1,1,'coral','blue','walk','cap','neutral')}
{person(320,336,0.95,1,'teal','gold','walk','bob','neutral')}
{person(430,336,0.85,1,'violet','teal','walk','short','neutral')}
<path d="M230 200h140" class="muted"/>
<path d="M120 240q-30-40-10-70" class="a" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('leap', '両足で強くけって、みぞの向こう側へ大きく跳び越えるイラスト。', f"""
<path d="M0 330h200v70H0zM400 330h200v70H400z" class="ground"/>
<path d="M0 330h200M400 330h200" class="a"/>
<path d="M200 330h200v70H200z" fill="#dfe6ea" opacity=".5"/>
{person(300,240,1.05,1,'coral','blue','up','short','neutral')}
<path d="M150 300q120-160 300-30" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('lemon', '切り口の見えるレモンと、丸ごと一個のレモンのイラスト。', f"""
<circle cx="470" cy="100" r="56" class="goldp"/>
<g transform="translate(200 240)">
  <ellipse rx="100" ry="72" class="gold o" transform="rotate(-12)"/>
  <path d="M96-24l24-12-20 26z" class="gold o"/>
  <path d="M-104 14l-24 10 22 12z" class="gold o"/>
</g>
<g transform="translate(390 270)">
  <circle r="76" fill="#fff6d6" stroke="{INK}" stroke-width="3"/>
  <circle r="64" class="goldp o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="3">
    <path d="M0 0v-64M0 0v64M0 0h-64M0 0h64M0 0l-46-46M0 0l46 46M0 0l46-46M0 0l-46 46"/>
  </g>
</g>
""", ground=True)

add('listener', 'ヘッドホンをつけて、耳を傾けて聞いている人のイラスト。', f"""
<circle cx="470" cy="100" r="56" class="tealp"/>
{person(280,346,1.3,1,'teal','blue','stand','short','smile')}
<g transform="translate(280 208)">
  <path d="M-38-14a38 38 0 0 1 76 0" fill="none" stroke="{INK}" stroke-width="9"/>
  <rect x="-52" y="-14" width="24" height="34" rx="8" class="coral o"/>
  <rect x="28" y="-14" width="24" height="34" rx="8" class="coral o"/>
</g>
<g class="teals" opacity=".9" style="stroke-width:4">
  <path d="M370 190q26 26 26 60t-26 60"/><path d="M410 170q34 34 34 80t-34 80"/>
</g>
<path d="M80 366h400" class="a"/>
""", ground=True)

add('monkey', '木の枝にぶら下がった猿のイラスト。長い尾が巻きついている。', f"""
<path d="M0 110q160-30 300-22t300 12" fill="none" stroke="{TONES['gold'][2]}" stroke-width="16" stroke-linecap="round"/>
<g transform="translate(300 210)">
  <path d="M-30-90q30-16 60 0 16 40 0 76-30 16-60 0-16-36 0-76z" class="goldd o"/>
  <circle cy="-110" r="42" class="goldd o"/>
  <circle cy="-104" r="30" class="goldp o"/>
  <circle cx="-42" cy="-118" r="14" class="goldd o"/><circle cx="42" cy="-118" r="14" class="goldd o"/>
  <circle cx="-11" cy="-112" r="3.6" class="ink"/><circle cx="11" cy="-112" r="3.6" class="ink"/>
  <path d="M-9-92q9 8 18 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-28-84l-40-40M28-84l40-40" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"/>
  <path d="M-20 0l-16 44M20 0l16 44" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"/>
  <path d="M30-30q60 10 50 70" fill="none" stroke="{TONES['gold'][2]}" stroke-width="9" stroke-linecap="round"/>
</g>
""", ground=True)

add('musician', 'ギターを抱えて演奏している人と、音符が飛び出しているイラスト。', f"""
<circle cx="470" cy="110" r="66" class="violetp"/>
{person(240,346,1.2,1,'violet','blue','carry','bun','smile')}
<g transform="translate(300 260) rotate(-16)">
  <ellipse rx="60" ry="70" class="goldp o"/>
  <circle r="22" class="goldd o"/>
  <path d="M-8-70h16v-90h-16z" class="goldd o"/>
  <path d="M-12-160h24v20h-24z" class="ink"/>
</g>
<g fill="{INK}">
  <g transform="translate(400 170)"><ellipse rx="12" ry="9" transform="rotate(-20)"/><path d="M10-4v-42h5v42z"/></g>
  <g transform="translate(460 220) scale(0.8)"><ellipse rx="12" ry="9" transform="rotate(-20)"/><path d="M10-4v-42h5v42z"/></g>
</g>
<path d="M80 366h420" class="a"/>
""", ground=True)

add('observe', '虫めがねで葉の上の虫を、じっくり観察しているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="tealp"/>
<g transform="translate(330 280)">
  <path d="M-10 30C-90 22-94-50-2-58 78-52 84 22-10 30z" class="green o"/>
  <g transform="translate(10 -14) scale(0.5)">
    <ellipse cy="40" rx="50" ry="66" class="teal o"/>
    <circle cy="-30" r="30" class="teald o"/>
    <g fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"><path d="M-40 20l-60-20M40 20l60-20M-40 70l-60 30M40 70l60 30"/></g>
  </g>
</g>
<g transform="translate(280 170)">
  <circle r="80" fill="#e8f4fb" opacity=".5" stroke="{INK}" stroke-width="6"/>
  <path d="M56 58l60 60" fill="none" stroke="{INK}" stroke-width="14" stroke-linecap="round"/>
</g>
<path d="M300 250v40" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('owner', '店の前に立ち、鍵を手にしている持ち主のイラスト。', f"""
{building(390,300,1.05,'teal')}
{person(160,340,1.15,1,'coral','blue','point','cap','smile')}
<g transform="translate(250 240) rotate(20)">
  <circle r="16" fill="none" stroke="{TONES['gold'][2]}" stroke-width="7"/>
  <path d="M16 0h50v10h-14v10h-10v-10h-26z" class="goldd o"/>
</g>
<path d="M290 200q40-20 60-10" class="muted" marker-end="url(#ar)"/>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('painter', 'カンバスに絵筆で絵を描いている画家のイラスト。', f"""
<g transform="translate(360 240)">
  <path d="M-110-120h220v220h-220z" class="paper"/>
  <path d="M-80 60l60-90 40 50 40-60 30 100z" class="tealp o"/>
  <circle cx="60" cy="-70" r="24" class="goldp o"/>
  <path d="M-110 100l-30 90M110 100l30 90M0 100v90" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10" stroke-linecap="round"/>
</g>
{person(150,346,1.1,1,'coral','violet','point','bun','smile')}
<g transform="translate(230 220) rotate(-24)">
  <path d="M0-6h70v12H0z" class="goldd o"/>
  <path d="M70-8h24v16H70z" class="coral o"/>
</g>
<path d="M80 366h460" class="a"/>
""", ground=True)

add('parking', '白線で区切られた駐車ますに、車が一台とまっているイラスト。', f"""
<path d="M0 180h600v220H0z" fill="#d8d3ca"/>
<g fill="none" stroke="#fffdf6" stroke-width="6"><path d="M60 180v220M240 180v220M420 180v220M580 180v220M60 180h520"/></g>
<g transform="translate(150 290) scale(0.8)">
  <path d="M-150 40h300l-16-56h-50l-34-56h-120l-34 56h-62z" class="coral o"/>
  <path d="M-110-16h80v-44h-58zM-10-60h74l26 44H-10z" class="bluep o"/>
  <circle cx="-84" cy="48" r="30" class="ink"/><circle cx="84" cy="48" r="30" class="ink"/>
</g>
<g transform="translate(500 250)">
  <path d="M-10 90V-60h20V90z" class="ink"/>
  <rect x="-40" y="-110" width="80" height="60" rx="8" class="bluep o"/>
  <path d="M-18-96h22a14 14 0 0 1 0 28h-22v-28zM-18-68v14" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
""", ground=False)

add('patrol', '懐中電灯を持った警備の人が、決まった道を見回っているイラスト。', f"""
{building(120,290,0.8,'blue')}
{building(480,290,0.8,'blue')}
{person(300,340,1.1,1,'blue','violet','walk','cap','neutral')}
<path d="M348 250l90-30" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
<path d="M438 220l80-40 20 60z" class="goldp" opacity=".7"/>
<path d="M140 366q80 24 160 0t160 0" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('plate', '料理をのせる平らな一枚の皿のイラスト。', f"""
<circle cx="470" cy="100" r="56" class="bluep"/>
<g transform="translate(280 250)">
  <ellipse rx="150" ry="60" fill="#fffdf6" class="o"/>
  <ellipse rx="104" ry="40" class="bluep o"/>
  <ellipse cy="10" rx="150" ry="60" fill="none" class="a" opacity=".35"/>
</g>
<path d="M120 340h340" class="a"/>
""", ground=True)

add('private', '「立入禁止」を示す柵で囲われ、他人が入れない場所のイラスト。', f"""
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="10" stroke-linecap="round">
  <path d="M60 180v160M180 180v160M300 180v160M420 180v160M540 180v160M40 220h520M40 290h520"/>
</g>
{building(300,150,0.6,'teal')}
{person(120,376,0.7,1,'coral','blue','stand','short','sad')}
<g class="corals" style="stroke-width:8"><path d="M180 340l40 40M220 340l-40 40"/></g>
""", ground=True)

add('recognize', '人ごみの中で、知っている顔を見つけて気づくイラスト。', f"""
<g opacity=".45">
  {person(120,336,0.9,1,'blue','violet','stand','short','neutral')}
  {person(220,336,0.9,1,'violet','teal','stand','bob','neutral')}
  {person(480,336,0.9,1,'blue','teal','stand','cap','neutral')}
</g>
{person(340,336,1.0,1,'coral','gold','wave' if 'wave' in POSES else 'point','bun','smile')}
<circle cx="340" cy="228" r="52" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="11 9"/>
<g class="golds" style="stroke-width:4"><path d="M400 170l26-24M300 160l-8-30"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('retreat', '前へ進むのをやめて、後ろへ下がっていく人のイラスト。', f"""
{person(360,336,1.1,-1,'coral','blue','walk','cap','sad')}
<path d="M300 220H140" class="a" marker-end="url(#ar)"/>
<path d="M420 220h120" class="muted"/>
<g class="corals" style="stroke-width:8"><path d="M470 190l40 40M510 190l-40 40"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('ride', '自転車の後ろに人を乗せて運んでいるイラスト。', f"""
<g transform="translate(300 300) scale(0.9)">
  <circle cx="-120" cy="0" r="60" fill="none" stroke="{INK}" stroke-width="9"/>
  <circle cx="120" cy="0" r="60" fill="none" stroke="{INK}" stroke-width="9"/>
  <path d="M-120 0l60-70h80l80 70M-60-70l60 70M0 0h120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linejoin="round"/>
  <path d="M-60-70v-24h34" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
</g>
{person(232,236,0.62,1,'teal','blue','stand','short','smile')}
{person(384,236,0.55,1,'violet','gold','stand','bob','smile')}
<path d="M460 200h80" class="a" marker-end="url(#ar)"/>
<path d="M60 370h480" class="a"/>
""", ground=True, arrow=True)

add('seize', '差し出された旗の柄を、手で強くつかみ取るイラスト。', f"""
<circle cx="120" cy="100" r="56" class="coralp"/>
<path d="M300 380V120" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
<path d="M308 126l90 26-90 26z" class="coral o"/>
{hand(300,250,1)}
<g class="corals" style="stroke-width:5"><path d="M370 200l30-26M386 246l34-12M348 178l6-30"/></g>
<path d="M180 300q40-30 80-40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('serve', '料理をのせた皿を、テーブルの客の前へ出しているイラスト。', f"""
<g transform="translate(360 320)">
  <path d="M-160-20h320v20h-320z" class="goldp o"/>
  <path d="M-140 0v60M140 0v60" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
</g>
<g transform="translate(380 280)">
  <ellipse rx="70" ry="26" fill="#fffdf6" class="o"/>
  <ellipse rx="44" ry="15" class="coralp o"/>
</g>
{person(140,346,1.15,1,'teal','blue','give','bob','smile')}
<circle cx="250" cy="256" r="15" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<path d="M280 210q50-14 80 24" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('breed', '親犬のそばに子犬が並び、同じ品種として育っているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="greenp"/>
<g transform="translate(220 280)">
  <ellipse cx="0" cy="20" rx="90" ry="50" class="goldp o"/>
  <path d="M-60 60v26M-20 64v22M28 64v22M64 56v30" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"/>
  <g transform="translate(100 -20)">
    <path d="M-32-30q32-24 64 0 18 18 14 42-4 28-46 28t-46-28q-4-24 14-42z" class="goldp o"/>
    <path d="M-36-32q-22-36 4-38 22-2 24 24z" class="goldd o"/>
    <path d="M32-34q24-34 42-12 16 16-6 34z" class="goldd o"/>
    <circle cx="6" cy="-4" r="3.4" class="ink"/><ellipse cx="44" cy="20" rx="9" ry="7" class="ink"/>
  </g>
</g>
<g transform="translate(430 320) scale(0.55)">
  <ellipse cx="0" cy="20" rx="90" ry="50" class="goldp o"/>
  <path d="M-60 60v26M-20 64v22M28 64v22M64 56v30" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"/>
  <g transform="translate(100 -20)">
    <path d="M-32-30q32-24 64 0 18 18 14 42-4 28-46 28t-46-28q-4-24 14-42z" class="goldp o"/>
    <path d="M-36-32q-22-36 4-38 22-2 24 24z" class="goldd o"/>
    <circle cx="6" cy="-4" r="3.4" class="ink"/><ellipse cx="44" cy="20" rx="9" ry="7" class="ink"/>
  </g>
</g>
<path d="M340 250q60 10 80 40" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('leapfrog' if False else 'cheerful', '明るい表情で軽やかに手をふっている人のイラスト。', f"""
{sun(480,100,44)}
{face(280,180,110,'grin')}
<g class="golds" style="stroke-width:5"><path d="M150 110l-24-24M410 110l24-24M140 210h-30M420 210h30"/></g>
<path d="M280 300v40" fill="none" stroke="{INK}" stroke-width="0"/>
<g transform="translate(280 330)">
  <path d="M-70-20q70-16 140 0l-10 40h-120z" class="coral o"/>
  <path d="M-70-14l-40 30M70-14l44-40" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
</g>
<path d="M60 356h440" class="a"/>
""", ground=True)
print(' '.join(W)); print(sheet(W))
