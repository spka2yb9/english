"""第41回: 注入・設置・調査・王など40語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('initiate', '合図のボタンを押して、工程を開始するイラスト。', f"""
{hand(160,240,1)}
<g transform="translate(300 250)">
  <path d="M-60-50h120v100h-120z" fill="#dfe6ea" class="o"/>
  <circle r="30" class="green o"/>
</g>
<g class="tealp o">{''.join(f'<circle cx="{410+i*60}" cy="250" r="24"/>' for i in range(3))}</g>
<g class="a" marker-end="url(#ar)"><path d="M230 240h30"/><path d="M370 250h10"/></g>
""", ground=True, arrow=True)

add('inject', '注射器で、中身を体へ注入するイラスト。', f"""
<g transform="translate(280 240) rotate(20)">
  <path d="M-140-20h180v40h-180z" fill="#f4fbff" class="o"/>
  <path d="M-160-14h20v28h-20z" class="ink"/>
  <path d="M-100-20h60v40h-60z" class="bluep o"/>
  <path d="M40-6h110v12H40z" fill="#dfe6ea" stroke="{INK}" stroke-width="2.5"/>
</g>
<g transform="translate(460 300)">
  <path d="M-60-40h120v80h-120z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<path d="M380 280h40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('injured', '腕に包帯を巻いた、けがをした人のイラスト。', f"""
{person(280,346,1.25,1,'teal','blue','stand','short','sad')}
<g transform="translate(230 250) rotate(-24)">
  <path d="M-26-14h52v28h-52z" fill="#fffdf6" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-26-4h52M-26 6h52" fill="none" stroke="{MUTED}" stroke-width="2.5"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M180 200l-20-20"/></g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('insert', 'すきまにカードを差し込むイラスト。', f"""
<g transform="translate(320 280)">
  <path d="M-140-70h280v140h-280z" fill="#dfe6ea" class="o"/>
  <path d="M-70-50h140v14h-140z" class="ink"/>
</g>
<g transform="translate(320 150)">
  <path d="M-70-24h140v48h-140z" class="tealp o"/>
  <path d="M-50-10h60v8h-60z" fill="none" stroke="{TONES['teal'][0]}" stroke-width="3"/>
</g>
<path d="M320 190v40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('inside', '箱の内側に品物が入っていることを示したイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-150-90h300v180h-300z" class="goldp o"/>
  <path d="M-150-90h300v180h-300z" fill="none" class="a"/>
  <circle r="46" class="coral o"/>
  <path d="M-150-90l40-30h300l-40 30z" class="gold o"/>
</g>
<path d="M470 130q-40 40-60 60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('inspect', '虫めがねで、部品を一つずつ点検するイラスト。', f"""
<g transform="translate(330 300)">
  <path d="M-180-20h360v20h-360z" class="goldp o"/>
  <g class="tealp o">{''.join(f'<rect x="{-160+i*70}" y="-60" width="50" height="40"/>' for i in range(5))}</g>
</g>
<g transform="translate(300 200)">
  <circle r="70" fill="#e8f4fb" opacity=".4" stroke="{INK}" stroke-width="6"/>
  <path d="M50 50l50 50" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>
</g>
{person(120,346,0.85,1,'blue','violet','point','cap','neutral')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('inspire', '見た手本に触れて、やる気が湧くイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','up','bob','smile')}
<g transform="translate(430 240)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <path d="M-56 46l46-80 34 44 34-56 26 92z" class="tealp o"/>
</g>
<g transform="translate(280 150)">
  <circle r="30" class="goldp o"/>
  <path d="M-12 30h24v12h-24z" class="ink"/>
  <g class="golds" style="stroke-width:4"><path d="M0-42v-14M-32-22l-12-8M32-22l12-8"/></g>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4"><path d="M340 220h-30" marker-end="url(#ar)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('install', '機器を壁に取り付けて、設置するイラスト。', f"""
<g transform="translate(380 240)">
  <path d="M-100-80h200v160h-200z" fill="#dfe6ea" class="o"/>
  <path d="M-70-50h140v100h-140z" class="bluep o"/>
  <g fill="none" stroke="{INK}" stroke-width="4"><circle cx="-80" cy="-60" r="10"/><circle cx="80" cy="60" r="10"/></g>
</g>
{hand(180,220,1)}
<path d="M250 230h30" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M170 330l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('instruct', '手順を示して、やり方を指示するイラスト。', f"""
{person(160,346,1.15,1,'blue','violet','point','short','neutral')}
<g transform="translate(400 240)">
  <path d="M-100-90h200v180h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-50 {-60+i*40}h120"/>' for i in range(4))}</g>
  <g fill="{INK}">{''.join(f'<rect x="-76" y="{-66+i*40}" width="{6+i*2}" height="14"/>' for i in range(4))}</g>
</g>
<path d="M250 220h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('instructor', '受講者に、動作を教えている指導者のイラスト。', f"""
{person(180,346,1.2,1,'teal','teal','point','cap','neutral')}
<g opacity=".85">{person(400,346,0.95,-1,'coral','gold','up','bob','neutral')}{person(490,346,0.95,-1,'violet','teal','up','short','neutral')}</g>
<path d="M260 230h80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('insult', '侮辱する言葉を投げつけて、相手を傷つけるイラスト。', f"""
{person(180,346,1.15,1,'coral','blue','point','cap','neutral')}
{person(450,346,1.1,-1,'teal','gold','hold','bob','sad')}
<g transform="translate(310 190)">
  <path d="M-60-30h120q14 0 14 14v30q0 14-14 14h-80l-20 16 4-16q-14 0-14-14v-30q0-14 14-14z" class="paper"/>
  <g class="corals" style="stroke-width:5"><path d="M-20-8l40 22M20-8l-40 22"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('interact', '二人が言葉と身ぶりでやりとりするイラスト。', f"""
{person(170,346,1.1,1,'teal','blue','give','short','smile')}
{person(430,346,1.1,-1,'coral','gold','give','bob','smile')}
<g fill="none" stroke="{INK}" stroke-width="4">
  <path d="M240 200h120" marker-end="url(#ar)"/><path d="M360 250H240" marker-end="url(#ar)"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('interfere', '他人の作業に横から手を出して、妨げるイラスト。', f"""
{person(200,346,1.15,1,'teal','blue','point','short','sad')}
<g transform="translate(320 280)">
  <path d="M-90-40h180v80h-180z" class="tealp o"/>
</g>
{hand(430,200,-1)}
<path d="M390 240l-30 20" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:7"><path d="M300 180l30 30M330 180l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('interpret', '同じ図を見て、意味を読み取っているイラスト。', f"""
<g transform="translate(200 230)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="4"><path d="M-60 40l50-70 40 40 40-50"/></g>
</g>
{person(430,346,1.1,-1,'teal','blue','think','short','neutral')}
<g transform="translate(430 180)">
  <path d="M-70-40h140q16 0 16 16v40q0 16-16 16h-90l-24 20 6-20h-32q-16 0-16-16v-40q0-16 16-16z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-44-12h88M-44 10h60"/></g>
</g>
<path d="M320 240h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('intervene', '争う二人の間に、第三者が入って止めるイラスト。', f"""
{person(150,346,1.05,1,'coral','blue','point','short','neutral')}
{person(450,346,1.05,-1,'gold','violet','point','bob','neutral')}
{person(300,346,1.15,1,'blue','violet','up','cap','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M300 160v50"/></g>
<g class="corals" style="stroke-width:6"><path d="M230 260h-30M370 260h30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('introduction', '本の最初に置かれた、入門の章を示したイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-160-140h320v280h-320z" class="paper"/>
  <path d="M-160-140h320v60h-320z" class="tealp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-120 {-40+i*30}h240"/>' for i in range(6))}</g>
</g>
<path d="M470 130q-40 20-60 30" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('invade', '国境を越えて、軍が侵入してくるイラスト。', f"""
<path d="M300 100v260" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="16 12"/>
{person(160,346,1.0,1,'green','green','walk','cap','neutral')}
{person(250,346,1.0,1,'green','green','walk','cap','neutral')}
<path d="M340 240h140" class="a" marker-end="url(#ar)" style="stroke-width:7"/>
{building(500,346,0.5,'teal')}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('invention', '新しく作り出された装置と、発明の閃きのイラスト。', f"""
<g transform="translate(380 250)">
  <path d="M-110-80h220v160h-220z" fill="#dfe6ea" class="o"/>
  <circle cx="-40" cy="-20" r="34" fill="none" stroke="{INK}" stroke-width="6"/>
  <circle cx="40" cy="20" r="24" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M-40-20l80 40" class="a"/>
</g>
<g transform="translate(180 200)">
  <circle r="36" class="goldp o"/>
  <path d="M-14 36h28v14h-28z" class="ink"/>
  <g class="golds" style="stroke-width:4"><path d="M0-50v-18M-38-28l-14-10M38-28l14-10"/></g>
</g>
<path d="M240 230h30" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('invest', '手持ちのお金を事業に入れて、育てるイラスト。', f"""
<g transform="translate(170 260)">
  <circle r="30" class="goldp o"/>
  <path d="M-9-12h18v24h-18z" class="goldd"/>
</g>
<g transform="translate(430 250)">
  <path d="M-90 60h180M-90 60V-60" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-80 40l60-40 60 20 60-50" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" marker-end="url(#ar)"/>
</g>
<path d="M240 260h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('investigate', '現場を虫めがねで調べて、手がかりを探すイラスト。', f"""
<g fill="#c9bda6"><ellipse cx="200" cy="330" rx="12" ry="18"/><ellipse cx="250" cy="310" rx="11" ry="17"/></g>
<g transform="translate(320 230)">
  <circle r="80" fill="#e8f4fb" opacity=".4" stroke="{INK}" stroke-width="7"/>
  <path d="M56 56l56 56" fill="none" stroke="{INK}" stroke-width="13" stroke-linecap="round"/>
</g>
{person(130,346,0.9,1,'blue','violet','point','cap','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M470 300h50" marker-start="url(#ar)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('invoke', '規則の条文を引き合いに出して、示すイラスト。', f"""
{person(170,346,1.15,1,'blue','violet','point','short','neutral')}
<g transform="translate(410 240)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-60h140M-70-30h140M-70 30h120"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M-70 0h140"/></g>
</g>
<path d="M260 220h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('isolate', '一つだけを囲いの外へ出して、切り離すイラスト。', f"""
<circle cx="230" cy="230" r="120" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" stroke-dasharray="16 12"/>
<g class="tealp o"><circle cx="190" cy="200" r="32"/><circle cx="270" cy="210" r="32"/><circle cx="225" cy="285" r="32"/></g>
<circle cx="480" cy="290" r="32" class="coral o"/>
<circle cx="480" cy="290" r="60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"/>
<path d="M370 260h50" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('itself', 'それ自体が単独で示されているイラスト。', f"""
{box(300,250,160,120,0,'gold')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="200" y="170" width="200" height="160"/></g>
<g opacity=".3">{box(120,300,80,60,0,'teal')}{box(500,300,80,60,0,'teal')}</g>
<path d="M300 380v-30" class="a" marker-end="url(#ar)" transform="rotate(180 300 365)"/>
""", ground=True, arrow=True)

add('jail', '鉄格子の中に入れられている、刑務所のイラスト。', f"""
<g fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round">
  <path d="M160 130v240M230 130v240M300 130v240M370 130v240M440 130v240M140 150h320M140 350h320"/>
</g>
{person(300,340,0.85,1,'coral','blue','stand','short','sad')}
<path d="M520 240h-40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('jam', '車がびっしり詰まって、渋滞しているイラスト。', f"""
<path d="M0 180h600v220H0z" fill="#d8d3ca"/>
<path d="M0 180h600" class="a"/>
{''.join(f'<g transform="translate({100+ (i%3)*160} {230 + (i//3)*80}) scale(0.35)"><path d="M-150 40h300l-16-56h-50l-34-56h-120l-34 56h-62z" class="{["coral","teal","gold"][i%3]} o"/><circle cx="-84" cy="48" r="30" class="ink"/><circle cx="84" cy="48" r="30" class="ink"/></g>' for i in range(6))}
<g class="corals" style="stroke-width:6"><path d="M520 260h-40M520 300h-40"/></g>
""", ground=False)

add('jazz', 'サキソフォンを吹いて、ジャズを演奏しているイラスト。', f"""
{person(240,346,1.2,1,'violet','blue','carry','bun','smile')}
<g transform="translate(320 250)">
  <path d="M-10-90h20v60q0 60 40 70t40-30" fill="none" stroke="{TONES['gold'][0]}" stroke-width="16" stroke-linecap="round"/>
  <path d="M80-20q40 0 40 30t-40 30" fill="none" stroke="{TONES['gold'][0]}" stroke-width="16"/>
  <path d="M-16-96h32v12h-32z" class="ink"/>
</g>
<g fill="{INK}"><g transform="translate(470 190) scale(0.8)"><ellipse rx="12" ry="9" transform="rotate(-20)"/><path d="M10-4v-42h5v42z"/></g></g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('jewellery', '指輪と首飾りが並んだ装身具のイラスト。', f"""
<g transform="translate(200 250)">
  <circle r="50" fill="none" stroke="{TONES['gold'][0]}" stroke-width="12"/>
  <path d="M0-50l-14-20h28z" class="goldp o"/>
</g>
<g transform="translate(420 240)">
  <path d="M-80-40a80 80 0 0 0 160 0" fill="none" stroke="{TONES['gold'][0]}" stroke-width="8"/>
  <circle cy="44" r="18" class="bluep o"/>
</g>
<g class="golds" style="stroke-width:4"><path d="M150 150l-20-20M470 150l20-20"/></g>
<path d="M120 340h360" class="a"/>
""", ground=True)

add('journalist', '手帳とマイクを持って、取材する記者のイラスト。', f"""
{person(200,346,1.15,1,'blue','violet','hold','bob','neutral')}
<g transform="translate(260 250)">
  <path d="M-16-14h32v28h-32z" class="ink"/>
  <path d="M16-4l50-24v48z" class="ink" opacity=".8"/>
</g>
<g transform="translate(450 280)">
  <path d="M-50-60h100v120h-100z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-30-30h60M-30-6h60M-30 18h40"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('kid', '小さな子どもが立っているイラスト。', f"""
{person(300,346,0.8,1,'coral','gold','stand','short','smile')}
<g opacity=".4">{person(160,346,1.3,1,'teal','blue','stand','bob','smile')}</g>
<path d="M240 260h120" class="muted"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('kidnap', '人が連れ去られて、車に乗せられるイラスト。', f"""
<g transform="translate(420 290) scale(0.55)">
  <path d="M-200 40h430v-100q0-34-34-34h-396z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <circle cx="-120" cy="52" r="26" class="ink"/><circle cx="120" cy="52" r="26" class="ink"/>
</g>
{person(200,346,1.05,1,'coral','blue','up','short','sad')}
{person(300,346,1.05,-1,'violet','violet','point','cap','neutral')}
<path d="M250 230h100" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:7"><path d="M150 200l30 30M180 200l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('kind', '困っている人に手を差し出す、親切なイラスト。', f"""
<circle cx="300" cy="140" r="76" class="coralp"/>
<g transform="translate(300 176)"><path d="M0 24l-28-34 14-16 14 14 14-14 14 16z" class="coral o"/></g>
{person(180,346,1.15,1,'teal','blue','give','short','smile')}
{person(430,346,1.1,-1,'gold','violet','give','bob','sad')}
<g fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"><circle cx="300" cy="256" r="15"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('king', '王冠をかぶって玉座に座る、王のイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-90-20h180v40h-180z" class="goldd o"/>
  <path d="M80-20v-140h20v140z" class="goldd o"/>
  <path d="M-100-20v-100h20v100z" class="goldd o"/>
</g>
<g transform="translate(300 290)">
  <path d="M-34-70q34-16 68 0l-10 70h-48z" class="violet o"/>
  <circle cx="0" cy="-100" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-34-124l-6-32 18 14 12-22 12 22 18-14-6 32z" class="gold o"/>
</g>
<path d="M120 380h360" class="a"/>
""", ground=True)

add('knee', '脚の関節にあるひざの位置を示したイラスト。', f"""
<g transform="translate(280 220)">
  <path d="M-30-140h60v120h-60z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-30-20h60v40h-60z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-30 20h60v130h-60z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="0" cy="0" r="38" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="11 9"/>
</g>
<path d="M440 220h-90" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('lake', '山にかこまれた湖のイラスト。', f"""
<path d="M40 220L200 90l120 110 90-70 150 90z" class="tealp o"/>
<path d="M0 220h600v180H0z" class="bluep"/>
<path d="M0 220h600" class="a"/>
{tree(80,300,0.6)}
<g class="blues" opacity=".7"><path d="M100 280q50-14 100 0t100 0M340 330q50-14 100 0t100 0"/></g>
""", ground=False)

add('lamp', 'かさのついた明かりが、机を照らすイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-70-60h140l-30-60h-80z" class="goldp o"/>
  <path d="M0-60v100" fill="none" stroke="{INK}" stroke-width="8"/>
  <ellipse cy="46" rx="60" ry="16" class="goldd o"/>
</g>
<path d="M180 380h240l-60-80h-120z" class="goldp" opacity=".45"/>
<g class="golds" style="stroke-width:4"><path d="M180 200l-24-16M420 200l24-16"/></g>
<path d="M120 380h360" class="a"/>
""", ground=True)

add('laptop', '開いた画面とキーボードのノートパソコンのイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-150-120h300v170h-300z" fill="#dfe6ea" class="o"/>
  <path d="M-126-96h252v122h-252z" class="bluep o"/>
  <path d="M-180 50h360l20 30h-400z" fill="#cfd8de" stroke="{INK}" stroke-width="3"/>
  <g class="ink">{''.join(f'<rect x="{-140 + (i%8)*36}" y="58" width="26" height="12" rx="3"/>' for i in range(8))}</g>
</g>
<path d="M120 380h360" class="a"/>
""", ground=True)

add('last', '電池の残量が最後まで持ちこたえるイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-140-70h280v140h-280z" fill="#dfe6ea" class="o"/>
  <path d="M140-30h24v60h-24z" class="ink"/>
  <g class="green o"><rect x="-120" y="-50" width="70" height="100"/><rect x="-40" y="-50" width="70" height="100"/><rect x="40" y="-50" width="70" height="100"/></g>
</g>
<path d="M120 350h360" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('latest', '並んだ版のうち、いちばん新しいものを示すイラスト。', f"""
<g class="tealp o">{''.join(f'<rect x="{110+i*90}" y="220" width="70" height="90"/>' for i in range(4))}</g>
<rect x="470" y="200" width="70" height="110" class="coral o"/>
<g class="golds" style="stroke-width:4"><path d="M505 180v-24"/></g>
<path d="M110 350h430" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('laughter', '声を上げて、みんなで笑っているイラスト。', f"""
{face(180,210,90,'grin')}
{face(360,210,90,'grin')}
<g class="golds" style="stroke-width:5">
  <path d="M180 100V70M100 150l-26-16M260 150l26-16M360 100V70M280 150l-26-16M440 150l26-16"/>
</g>
<g transform="translate(490 300)">
  <path d="M-40-24h80q10 0 10 10v22q0 10-10 10h-52l-14 12 4-12q-10 0-10-10v-22q0-10 10-10z" class="paper"/>
  <path d="M-24 0q24 24 48 0" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
""", ground=False)

add('lawyer', '法律書を手にして、弁護をする人のイラスト。', f"""
{person(200,346,1.2,1,'blue','blue','point','short','neutral')}
<g transform="translate(200 262)">
  <path d="M-40-24h80v6h-80z" class="paper"/>
  <path d="M-12-20l12 18 12-18z" class="ink"/>
</g>
<g transform="translate(420 270)">
  <path d="M-70-90h140v180h-140z" class="violetp o"/>
  <path d="M-50-90h16v180h-16z" class="violet o"/>
  <g fill="none" stroke="{TONES['violet'][2]}" stroke-width="4"><path d="M-16-50h70M-16-20h60"/></g>
</g>
<path d="M280 220h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
