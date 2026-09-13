"""第33回（最終）: 選択・分類・協力・告白など44語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('cheer', '観客が声を上げて、選手を応援しているイラスト。', f"""
{person(160,346,1.05,1,'coral','blue','up','bob','smile')}
{person(280,346,1.05,1,'teal','gold','up','short','smile')}
{person(400,346,1.05,1,'violet','teal','up','cap','smile')}
<g class="golds" style="stroke-width:4"><path d="M110 200l-24-24M460 200l24-24M280 170v-24"/></g>
<path d="M500 260h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('chef', '帽子をかぶって料理をしている料理人のイラスト。', f"""
{person(230,346,1.2,1,'teal','teal','carry','short','smile')}
<g transform="translate(230 210)">
  <path d="M-36-10q-14-40 16-40 8-22 40-12 26 4 22 30 22 10 6 32z" fill="#fffdf6" class="o"/>
  <path d="M-36 0h72v14h-72z" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(400 290)">
  <path d="M-90-30h180l-14 60h-152z" fill="#dfe6ea" class="o"/>
  <path d="M-104-30h208" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
</g>
{flame(400,346,0.7)}
<path d="M80 366h440" class="a"/>
""", ground=True)

add('chip', '皿のふちが小さく欠けているイラスト。', f"""
<g transform="translate(300 250)">
  <ellipse rx="140" ry="46" fill="#fffdf6" class="o"/>
  <ellipse rx="96" ry="30" class="bluep o"/>
  <path d="M110-24l30-6-24 22z" fill="#fffaf1" stroke="{INK}" stroke-width="2.5"/>
</g>
<circle cx="410" cy="230" r="46" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M120 340h360" class="a"/>
""", ground=True)

add('choice', '三つの道のうち、一つを選んで進むイラスト。', f"""
<circle cx="110" cy="240" r="22" class="teal o"/>
<path d="M140 230q120-90 220-70t140 20" class="muted"/>
<path d="M140 240h360" fill="none" stroke="{TONES['teal'][0]}" stroke-width="12" stroke-linecap="round" marker-end="url(#ar)"/>
<path d="M140 250q120 90 220 70t140-20" class="muted"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M300 190l18 18 30-36"/></g>
""", ground=False, arrow=True)

add('chop', '包丁で野菜をたたき切って、細かくしているイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-160-20h320l-16 30h-288z" class="paper"/>
  <g class="green o"><rect x="-120" y="-50" width="34" height="30"/><rect x="-80" y="-50" width="34" height="30"/><rect x="-40" y="-50" width="34" height="30"/></g>
  <path d="M20-60h120v40H20z" class="green o"/>
</g>
<g transform="translate(180 180) rotate(-16)">
  <path d="M-10-6h140l30 26h-170z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-80-4h70v22h-70z" class="ink"/>
</g>
<path d="M240 210v50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('church', '尖塔に十字のついた教会の建物のイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-150 100V-30h300v130z" fill="#fffdf6" class="o"/>
  <path d="M-166-30L0-120l166 90z" class="teal o"/>
  <path d="M-40 100V20h80v80z" class="goldd o"/>
  <path d="M-40 20a40 40 0 0 1 80 0z" class="goldd o"/>
  <path d="M-10-160h20v50h-20zM-30-140h60v20h-60z" class="ink"/>
  <g class="bluep o"><rect x="-110" y="0" width="40" height="50"/><rect x="70" y="0" width="40" height="50"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('cigarette', '灰皿の上で煙を上げている紙巻きたばこのイラスト。', f"""
<g transform="translate(280 280)">
  <ellipse rx="110" ry="34" fill="#dfe6ea" class="o"/>
  <ellipse rx="70" ry="20" fill="#cfd8de"/>
</g>
<g transform="translate(300 250) rotate(-14)">
  <path d="M-100-12h160v24h-160z" fill="#fffdf6" stroke="{INK}" stroke-width="2.5"/>
  <path d="M60-12h40v24H60z" class="goldd o"/>
  <path d="M-100-12h14v24h-14z" class="coral"/>
</g>
<g class="muted" opacity=".9"><path d="M180 200q-16-40 6-70M220 210q-16-44 8-76"/></g>
""", ground=True)

add('circulate', '血が体をめぐるように、輪を描いて循環するイラスト。', f"""
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="14" stroke-linecap="round">
  <path d="M300 100a130 130 0 0 1 112 194" marker-end="url(#ar)"/>
  <path d="M412 294a130 130 0 0 1-224 0" marker-end="url(#ar)"/>
  <path d="M188 294a130 130 0 0 1 112-194" marker-end="url(#ar)"/>
</g>
<g transform="translate(300 200)"><path d="M0 50l-46-56 22-26 24 24 24-24 22 26z" class="coral o"/></g>
""", ground=False, arrow=True)

add('cite', '本の一節に印をつけて、引用しているイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M0 30q-70-40-150-20v-140q80-20 150 20z" class="paper"/>
  <path d="M0 30q70-40 150-20v-140q-80-20-150 20z" class="paper"/>
  <path d="M0-110v140" class="a"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-130-70h100M-130-46h90M20-70h100"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M20-46h110"/></g>
</g>
<g transform="translate(450 240)">
  <path d="M-70-50h140v100h-140z" class="paper"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M-46-20h92M-46 4h60"/></g>
  <path d="M-58-38h10v-14h-10zM-42-38h10v-14h-10z" class="coral"/>
</g>
<path d="M340 240h40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('claim', '自分のものだと主張して、手を挙げているイラスト。', f"""
{person(200,346,1.15,1,'coral','blue','up','short','neutral')}
{box(430,290,110,80,0,'gold')}
<g transform="translate(300 180)">
  <path d="M-50-30h100q12 0 12 12v30q0 12-12 12h-70l-18 16 4-16q-12 0-12-12v-30q0-12 12-12z" class="paper"/>
  <path d="M-6-14h12v22h-6z" class="coral"/>
</g>
<path d="M300 290h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('clarify', 'ぼやけた文字が、はっきり読める形になるイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <g fill="none" stroke="#cfd8de" stroke-width="8"><path d="M-60-40h120M-60 0h100M-60 40h80"/></g>
</g>
<g transform="translate(430 230)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="4"><path d="M-60-40h120M-60 0h100M-60 40h80"/></g>
</g>
<path d="M280 230h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('classify', '形の違う品を、種類ごとに三つの箱へ分けるイラスト。', f"""
<g transform="translate(300 130)">
  <path d="M-90-40h180l-16 60H-74z" class="paper"/>
  <circle cx="-50" cy="-4" r="14" class="coral o"/>
  <rect x="-16" y="-18" width="28" height="28" class="teal o"/>
  <path d="M50-20l16 28h-32z" class="gold o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 200q-60 40-80 80"/><path d="M300 200v80"/><path d="M350 200q60 40 80 80"/></g>
<g transform="translate(150 330)"><path d="M-50-20h100l-12 44H-38z" class="coralp o"/></g>
<g transform="translate(300 330)"><path d="M-50-20h100l-12 44H-38z" class="tealp o"/></g>
<g transform="translate(450 330)"><path d="M-50-20h100l-12 44H-38z" class="goldp o"/></g>
""", ground=False, arrow=True)

add('cling', '子が親の腕にしっかりしがみついているイラスト。', f"""
{person(240,346,1.25,1,'teal','blue','carry','bob','smile')}
<g transform="translate(330 280)">
  <path d="M-30-40q30-14 60 0l-8 70h-44z" class="coral o"/>
  <path d="M-30-30l-50-6M30-30l14 20" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
  <circle cx="0" cy="-66" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-24-68q3-26 24-26 22 0 26 24-12-10-26-4-11-10-24 6z" fill="{HAIR}"/>
  <path d="M-8-60h6M6-60h6" class="a"/>
</g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('clothing', 'たなに並んだ衣類のイラスト。', f"""
<path d="M40 110h520" fill="none" stroke="{MUTED}" stroke-width="4"/>
<g transform="translate(160 170)">
  <path d="M-60-50l-26 14 10 26 16-8v88h120V-18l16 8 10-26-26-14h-34q-12 10-24 0z" class="tealp o"/>
</g>
<g transform="translate(330 180)">
  <path d="M-50-40h100v30l-14 90h-72l-14-90z" class="coralp o"/>
</g>
<g transform="translate(480 170)">
  <path d="M-46-46h92v40l-16 86h-60l-16-86z" class="violetp o"/>
</g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('code', '数字の並びを入力して、暗証番号を打ち込むイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-110-130h220v260h-220z" fill="#dfe6ea" class="o"/>
  <path d="M-80-100h160v50h-160z" class="bluep o"/>
  <g class="ink">{''.join(f'<rect x="{-76 + (i%3)*52}" y="{-30 + (i//3)*52}" width="40" height="40" rx="8"/>' for i in range(9))}</g>
</g>
{hand(160,220,1)}
<path d="M230 220h30" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('coincide', '二つの線が、同じ点でぴったり重なるイラスト。', f"""
<path d="M60 120L300 240" fill="none" stroke="{TONES['teal'][0]}" stroke-width="8"/>
<path d="M540 120L300 240" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
<circle cx="300" cy="240" r="26" fill="none" stroke="{INK}" stroke-width="5"/>
<circle cx="300" cy="240" r="10" class="ink"/>
<path d="M300 340v-60" class="a" marker-end="url(#ar)" transform="rotate(180 300 310)"/>
""", ground=False, arrow=True)

add('collaborate', '二人で一つの作品を、一緒に作り上げているイラスト。', f"""
{person(160,346,1.1,1,'teal','blue','point','short','smile')}
{person(440,346,1.1,-1,'coral','gold','point','bob','smile')}
<g transform="translate(300 250)">
  <path d="M-80-70h160v140h-160z" class="paper"/>
  <path d="M-80-70h80v70h-80z" class="tealp o"/>
  <path d="M0 0h80v70H0z" class="coralp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 190h30"/><path d="M370 190h-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('coloured', '白い形と、色を塗った形を並べて比べたイラスト。', f"""
<g transform="translate(170 230)">
  <circle r="80" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(430 230)">
  <circle r="80" class="coral o"/>
</g>
<path d="M280 230h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(300 350) rotate(-20)">
  <path d="M-50-8h100v16H-50z" class="goldd o"/>
  <path d="M50-12h26v24H50z" class="coral o"/>
</g>
""", ground=True, arrow=True)

add('column', '縦に並んだ数字の列と、石の円柱を並べたイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-90-120h180v240h-180z" class="paper"/>
  <g fill="{INK}">{''.join(f'<rect x="-30" y="{-90+i*40}" width="60" height="10"/>' for i in range(5))}</g>
  <path d="M-40-120v240" fill="none" stroke="{MUTED}" stroke-width="3"/>
</g>
<g transform="translate(440 250)">
  <path d="M-40-110h80v220h-80z" class="goldp o"/>
  <path d="M-54-110h108v-20h-108zM-54 110h108v20h-108z" class="goldd o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="3"><path d="M-20-100v200M0-100v200M20-100v200"/></g>
</g>
""", ground=True)

add('combat', '盾を構えて、正面から戦っているイラスト。', f"""
{person(180,346,1.1,1,'green','green','point','cap','neutral')}
{person(440,346,1.1,-1,'coral','gold','point','cap','neutral')}
<g transform="translate(260 260)">
  <path d="M-40-50h80v60q0 40-40 60-40-20-40-60z" class="tealp o"/>
</g>
<g transform="translate(360 250) rotate(20)">
  <path d="M-8-70h16v120h-16z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-24 50h48v12h-48z" class="goldd o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('comfort', '落ち込む人の背に手を添えて、慰めているイラスト。', f"""
{person(360,346,1.15,1,'coral','blue','hold','bob','sad')}
{person(180,346,1.15,1,'teal','gold','point','short','smile')}
<path d="M250 250h60" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<g transform="translate(430 200)"><path d="M0 24l-28-34 14-16 14 14 14-14 14 16z" class="coral o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('command', '指を差して、はっきり命令を出しているイラスト。', f"""
{person(180,346,1.2,1,'blue','violet','point','cap','neutral')}
{person(440,346,1.05,-1,'green','green','stand','cap','neutral')}
<g transform="translate(310 190)">
  <path d="M-56-30h112q14 0 14 14v30q0 14-14 14h-80l-20 16 4-16q-14 0-14-14v-30q0-14 14-14z" class="paper"/>
  <path d="M-6-14h12v22h-6z" class="ink"/>
</g>
<path d="M280 250h80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('commence', '開始の合図で、線が動き出すイラスト。', f"""
<path d="M120 200v120" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>
<path d="M140 260h380" fill="none" stroke="{TONES['teal'][0]}" stroke-width="14" stroke-linecap="round" marker-end="url(#ar)"/>
<g transform="translate(120 160)"><circle r="26" class="green o"/></g>
<path d="M200 340h180" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('commit', '約束の書類に署名して、引き受けるイラスト。', f"""
{person(160,346,1.15,1,'teal','blue','point','short','neutral')}
<g transform="translate(400 250)">
  <path d="M-110-100h220v200h-220z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-80-60h160M-80-30h160M-80 0h120"/></g>
  <path d="M-80 50q40-20 70 0t70-10" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
</g>
<path d="M250 220h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('compel', '後ろから押されて、いやおうなく進まされるイラスト。', f"""
{person(330,346,1.15,1,'coral','blue','walk','short','sad')}
{person(160,346,1.15,1,'blue','violet','point','cap','neutral')}
<path d="M230 250h50" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<path d="M400 240h100" class="a" marker-end="url(#ar)" style="stroke-width:7"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('compensate', '不足した分を、別の分で埋め合わせるイラスト。', f"""
<path d="M300 340V140" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<path d="M250 356h100" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>
<path d="M150 150h300" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<circle cx="300" cy="150" r="13" class="teal o"/>
<path d="M150 150v30M450 150v30" class="a"/>
<path d="M96 180h108l-14 30H110z" class="goldp o"/>
<path d="M396 180h108l-14 30H410z" class="goldp o"/>
<g class="tealp o"><rect x="120" y="140" width="60" height="34"/></g>
<g class="coral o"><rect x="420" y="150" width="60" height="24"/></g>
<path d="M240 120h120" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('compile', 'ばらばらの紙を集めて、一冊にまとめるイラスト。', f"""
<g transform="translate(170 220)">
  <g transform="rotate(-12)"><path d="M-60-70h120v140h-120z" class="paper"/></g>
  <g transform="rotate(10) translate(20 20)"><path d="M-60-70h120v140h-120z" class="paper"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-90-110h180v220h-180z" class="tealp o"/>
  <path d="M-70-110h20v220h-20z" class="teal o"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"><path d="M-30-60h100M-30-30h80"/></g>
</g>
<path d="M280 230h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('complement', '欠けた部分に、ぴったり合う片が加わるイラスト。', f"""
<g transform="translate(240 250)">
  <path d="M-100-90h200v180h-200z" class="tealp o"/>
  <path d="M40-30h60v60H40z" fill="#fffaf1" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(450 160)">
  <path d="M-30-30h60v60h-60z" class="coral o"/>
</g>
<path d="M400 200l-80 40" class="a" marker-end="url(#ar)"/>
<path d="M120 350h360" class="a"/>
""", ground=True, arrow=True)

add('complicated', '線が入り組んで、たどるのが難しい図のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="4">
    <path d="M-170-100h120v60h-160M-100-100v120h140v-80h80"/>
    <path d="M60 20v60h-180M100-60v140h60"/>
    <path d="M-170 60h60v40h100"/>
  </g>
</g>
<g fill="{INK}"><path d="M470 130q0-26 26-26t26 26q0 18-20 24v12h-12v-20q20-2 20-16 0-12-14-12t-14 12z"/><circle cx="496" cy="196" r="7"/></g>
""", ground=True)

add('comply', '示された規則に従って、線の内側を進むイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 10"><path d="M60 180h480M60 320h480"/></g>
{person(200,300,1.0,1,'teal','blue','walk','short','neutral')}
<path d="M300 250h180" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M500 130l18 18 30-36"/></g>
""", ground=False, arrow=True)

add('comprise', '三つの部分が集まって、一つの円を構成するイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M0 0v-130a130 130 0 0 1 113 65z" class="tealp o"/>
  <path d="M0 0l113-65a130 130 0 0 1-113 195z" class="coralp o"/>
  <path d="M0 0v130a130 130 0 0 1-113-195z" class="goldp o"/>
  <circle r="130" fill="none" class="a"/>
</g>
""", ground=False)

add('compromise', '両者が少しずつ譲って、中間で折り合うイラスト。', f"""
{person(150,346,1.1,1,'teal','blue','give','short','neutral')}
{person(450,346,1.1,-1,'coral','gold','give','bob','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M220 250h50"/><path d="M380 250h-50"/></g>
<g transform="translate(300 250)">
  <path d="M-30-30h60v60h-60z" class="violet o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M280 160l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('compute', '計算機が数値を処理して、答えを出すイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-140-100h280v200h-280z" fill="#dfe6ea" class="o"/>
  <path d="M-110-70h220v60h-220z" class="bluep o"/>
  <g class="ink">{''.join(f'<rect x="{-100 + (i%5)*44}" y="{10 + (i//5)*40}" width="34" height="30" rx="6"/>' for i in range(10))}</g>
</g>
<g transform="translate(300 110)">
  <path d="M-60-24h120v48h-120z" class="paper"/>
  <g fill="{INK}"><rect x="-30" y="-6" width="24" height="8"/><rect x="6" y="-6" width="24" height="8"/></g>
</g>
<path d="M300 150v-16" class="a" marker-end="url(#ar)" transform="rotate(180 300 142)"/>
""", ground=True, arrow=True)

add('conceal', '布をかけて、中身を見えなくしているイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-110 60V-20h220v80z" class="muted"/>
  <path d="M-140 60q-20-90 40-120 50-24 100-24t100 24q60 30 40 120z" class="violetp o"/>
  <path d="M-140 60q60 20 140 20t140-20" fill="none" class="a"/>
</g>
<g class="corals" style="stroke-width:6"><path d="M470 180l30 30M500 180l-30 30"/></g>
""", ground=True)

add('concede', '主張を取り下げて、相手の言い分を認めるイラスト。', f"""
{person(200,346,1.15,1,'coral','blue','up','short','sad')}
{person(440,346,1.1,-1,'teal','gold','point','bob','neutral')}
<g transform="translate(310 180)">
  <path d="M-56-30h112q14 0 14 14v30q0 14-14 14h-80l-20 16 4-16q-14 0-14-14v-30q0-14 14-14z" class="paper"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"><path d="M-20 0l12 12 22-24"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('conceive', '頭の中に、新しい案が思い浮かぶイラスト。', f"""
{person(180,346,1.15,1,'violet','blue','think','bun','smile')}
<g transform="translate(420 190)">
  <path d="M-110-50q-14-54 44-64 18-46 88-32 40 6 52 46 66-6 70 52 4 50-58 54h-160q-40-4-36-56z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 14)">
    <circle r="30" class="goldp o"/>
    <path d="M-12 30h24v14h-24z" class="ink"/>
    <g class="golds" style="stroke-width:4"><path d="M0-44v-16M-34-24l-14-8M34-24l14-8"/></g>
  </g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="290" cy="270" r="12"/><circle cx="264" cy="296" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('condemn', '悪い行いを、はっきり非難しているイラスト。', f"""
{person(180,346,1.15,1,'blue','violet','point','short','neutral')}
{person(450,346,1.1,-1,'coral','gold','stand','bob','sad')}
<g transform="translate(310 180)">
  <path d="M-56-30h112q14 0 14 14v30q0 14-14 14h-80l-20 16 4-16q-14 0-14-14v-30q0-14 14-14z" class="paper"/>
  <path d="M-6-14h12v22h-6z" class="coral"/>
</g>
<g class="corals" style="stroke-width:7"><path d="M370 250l30 30M400 250l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('confess', 'うつむいて、自分がやったと打ち明けているイラスト。', f"""
{person(200,346,1.15,1,'coral','blue','hold','short','sad')}
{person(450,346,1.1,-1,'blue','violet','stand','cap','neutral')}
<g transform="translate(320 190)">
  <path d="M-60-30h120q14 0 14 14v30q0 14-14 14h-80l-20 16 4-16q-14 0-14-14v-30q0-14 14-14z" class="paper"/>
  <g fill="{MUTED}"><circle cx="-20" cy="0" r="4"/><circle cx="0" cy="0" r="4"/><circle cx="20" cy="0" r="4"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('confident', '胸を張って、自信をもって立っているイラスト。', f"""
{person(280,346,1.3,1,'teal','blue','stand','short','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M440 220l20 20 34-40"/></g>
<g class="golds" style="stroke-width:4"><path d="M160 200l-24-24M400 200l24-24"/></g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('confine', '囲いの中に閉じ込めて、外へ出られないイラスト。', f"""
<g fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round">
  <path d="M180 130v240M240 130v240M300 130v240M360 130v240M420 130v240M160 150h280M160 350h280"/>
</g>
{person(300,340,0.85,1,'coral','blue','stand','short','sad')}
<g class="corals" style="stroke-width:7"><path d="M490 210l30 30M520 210l-30 30"/></g>
""", ground=True)

add('confront', '正面から向き合って、立ち向かうイラスト。', f"""
{person(190,346,1.15,1,'teal','blue','point','short','neutral')}
{person(430,346,1.15,-1,'coral','gold','point','cap','neutral')}
<path d="M260 230h100" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('confused', 'いくつもの矢印が入り組んで、どれか分からないイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','think','short','sad')}
<g class="muted" marker-end="url(#ar)">
  <path d="M320 180q60 40 120 0"/><path d="M320 240q60-40 120 0"/><path d="M320 300q60 40 120 0"/>
</g>
<g fill="{INK}"><path d="M470 130q0-26 26-26t26 26q0 18-20 24v12h-12v-20q20-2 20-16 0-12-14-12t-14 12z"/><circle cx="496" cy="196" r="7"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('congratulate', '拍手と紙ふぶきで、相手を祝っているイラスト。', f"""
<g fill="none">
  {''.join(f'<rect x="{100+i*60}" y="{90 + (i%3)*36}" width="16" height="10" fill="{[TONES["coral"][0],TONES["gold"][0],TONES["teal"][0]][i%3]}" transform="rotate({i*41} {108+i*60} {95+(i%3)*36})"/>' for i in range(8))}
</g>
{person(200,346,1.1,1,'teal','blue','hold','short','smile')}
<g fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"><ellipse cx="190" cy="264" rx="16" ry="22"/><ellipse cx="214" cy="264" rx="16" ry="22"/></g>
{person(420,346,1.15,-1,'coral','gold','up','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('consent', '同意の欄に印をつけて、承諾しているイラスト。', f"""
<g transform="translate(280 240)">
  <path d="M-130-130h260v260h-260z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-100-90h200M-100-50h200M-100-10h160"/></g>
  <g fill="none" stroke="{INK}" stroke-width="3"><rect x="-100" y="40" width="40" height="40"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M-92 56l14 14 26-30"/></g>
</g>
{hand(450,180,-1)}
<path d="M400 220h-30" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('conserve', '水を止めて、資源を節約しているイラスト。', f"""
<g transform="translate(300 190)">
  <path d="M-10 0v-90h120" fill="none" stroke="#cfd8de" stroke-width="24" stroke-linecap="round"/>
  <path d="M-10 0v20" fill="none" stroke="#cfd8de" stroke-width="30"/>
  <path d="M96-90v-30" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
  <path d="M70-124h52v14H70z" class="coral o"/>
</g>
{drop(290,250,1.0)}
<g class="corals" style="stroke-width:7"><path d="M440 260l30 30M470 260l-30 30"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M140 260l18 18 30-36"/></g>
""", ground=True)

add('constitute', '三つの部品が合わさって、全体をなすイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-140-100h280v200h-280z" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="12 8"/>
  <path d="M-120-80h100v80h-100z" class="teal o"/>
  <path d="M0-80h120v80H0z" class="coral o"/>
  <path d="M-120 20h240v60h-240z" class="gold o"/>
</g>
<path d="M120 360h360" class="a"/>
""", ground=True)
print(len(W), ' '.join(W)); print(sheet(W))
