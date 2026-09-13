"""第82回: g〜h の名詞を中心に45語。"""
import math
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'

add('gallon', '大きな容器いっぱいの液体を量るイラスト。', f"""
<g transform="translate(230 230)">
  <path d="M-90 110v-140q0-30 30-34v-26h56v26q34 4 34 34v140z" fill="#fffdf6" class="o"/>
  <path d="M-90 110v-96q60-16 120 0v96z" class="bluep o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-90 {60-i*34}h34"/>' for i in range(5))}</g>
  <path d="M-34-90h56v20h-56z" class="blue o"/>
</g>
<g transform="translate(450 300)">
  <path d="M-30-40h60l-8 60h-44z" fill="#fffdf6" class="o"/>
  <path d="M-26-16h52l-6 36h-40z" class="bluep o"/>
</g>
<path d="M330 260h-40M370 260h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('gambling', 'さいころとカードに金を賭ける賭博のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-230 60h460v20h-460z" class="greend o"/>
  <path d="M-230-20h460v80h-460z" class="green o"/>
</g>
<g transform="translate(170 200)">
  <path d="M-40-40h80v80h-80z" fill="#fffdf6" class="o" transform="rotate(-12)"/>
  <g fill="{INK}" transform="rotate(-12)"><circle cx="-18" cy="-18" r="7"/><circle cx="18" cy="18" r="7"/><circle r="7"/></g>
</g>
<g transform="translate(300 210)">
  <path d="M-46-56h92v112h-92z" fill="#fffdf6" class="o" transform="rotate(10)"/>
  <path d="M0-20q-30-30-30 0 0 20 30 34 30-14 30-34 0-30-30 0z" class="coral" transform="rotate(10)"/>
</g>
<g class="coral o"><ellipse cx="440" cy="240" rx="34" ry="14"/><ellipse cx="440" cy="222" rx="34" ry="14"/></g>
<g class="gold o"><ellipse cx="500" cy="248" rx="30" ry="13"/><ellipse cx="500" cy="232" rx="30" ry="13"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('gaming', 'コントローラーで遊ぶゲームのイラスト。', f"""
<g transform="translate(340 170)">
  <path d="M-140-90h280v170h-280z" class="ink"/>
  <path d="M-124-76h248v142h-248z" class="bluep"/>
  <g class="coral o"><path d="M-70 20h40v30h-40z"/><path d="M-30-10h40v60h-40z"/><path d="M10 10h40v40h-40z"/></g>
  <circle cx="70" cy="-30" r="18" class="gold o"/>
</g>
<g transform="translate(300 320)">
  <path d="M-110-30q-24 0-24 30t28 30q20 0 30-18h72q10 18 30 18t28-30-24-30q-40-8-70-8t-70 8z" class="violet o"/>
  <g fill="#fffdf6"><rect x="-84" y="4" width="34" height="10" rx="5"/><rect x="-72" y="-8" width="10" height="34" rx="5"/></g>
  <circle cx="56" cy="0" r="9" fill="#fffdf6"/><circle cx="80" cy="14" r="9" fill="#fffdf6"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('gang', 'そろいの格好でつるむ一団のイラスト。', f"""
{person(160,352,1,1,'violet','blue','stand','cap','neutral')}
{person(260,352,1,1,'violet','blue','stand','cap','neutral')}
{person(360,352,1,1,'violet','blue','stand','cap','neutral')}
{person(460,352,1,1,'violet','blue','stand','cap','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><rect x="90" y="180" width="440" height="180" rx="24"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('gathering', '人が集まって開かれる集会のイラスト。', f"""
<g transform="translate(300 120)">
  <path d="M-190-30h380v56h-380z" class="teal o"/>
  <path d="M-190-30v-20M190-30v-20" class="a"/>
  <g fill="#fffdf6"><rect x="-120" y="-8" width="240" height="12" rx="6"/></g>
</g>
{person(120,360,0.85,1,'coral','blue','stand','short','smile')}
{person(230,360,0.85,1,'gold','blue','stand','bob','smile')}
{person(340,360,0.85,-1,'green','gold','stand','short','smile')}
{person(450,360,0.85,-1,'blue','violet','stand','bun','smile')}
<path d="M60 382h480" class="a"/>
""", ground=True)

add('gene', '生き物の設計図である遺伝子のらせんのイラスト。', f"""
<g transform="translate(300 200)">
  <path d="{'M'+' L'.join(f'{40*math.sin(math.radians(i*18)):.0f} {-150+i*15:.0f}' for i in range(21))}" fill="none" stroke="{TONES['teal'][0]}" stroke-width="9" stroke-linecap="round"/>
  <path d="{'M'+' L'.join(f'{-40*math.sin(math.radians(i*18)):.0f} {-150+i*15:.0f}' for i in range(21))}" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"/>
  <g stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
    {''.join(f'<path d="M{40*math.sin(math.radians(i*18)):.0f} {-150+i*15:.0f}H{-40*math.sin(math.radians(i*18)):.0f}"/>' for i in range(1,20))}
  </g>
</g>
<path d="M60 372h480" class="a"/>
""", ground=True)

add('generally', '例外はあるが全体としてはそうだと示すイラスト。', f"""
<g transform="translate(300 220)">
  <g class="teal o">{''.join(f'<circle cx="{-190+i*66}" cy="0" r="30"/>' for i in range(5))}</g>
  <circle cx="140" cy="0" r="30" class="coralp o"/>
  <path d="M-224 56h330" fill="none" stroke="{GRN}" stroke-width="5"/>
  <path d="M-224 56v14M106 56v14M-60 56v22" fill="none" stroke="{GRN}" stroke-width="5"/>
</g>
{ck(240,320,0.9)}
<path d="M60 372h480" class="a"/>
""", ground=True)

add('generosity', '自分の分を惜しみなく分け与える気前よさのイラスト。', f"""
{person(150,350,1.15,1,'teal','blue','give','short','smile')}
<g transform="translate(320 250)">
  <path d="M-60-20h120v40h-120z" class="goldp o"/>
  <path d="M-60-20h120v40h-120zM0-20v40" class="a"/>
  <path d="M-60-40h120v20h-120z" class="gold o"/>
</g>
{person(470,350,1.1,-1,'coral','gold','reach','bob','smile')}
<path d="M250 300h130" class="a" marker-end="url(#ar)"/>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M320 140q-18-24 0-34 18-10 18 14 0-24 18-14 18 10 0 34l-18 18z"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('genius', '難しい問題をすらすら解く才能のイラスト。', f"""
<g transform="translate(400 200)">
  <path d="M-150-120h300v220h-300z" class="ink"/>
  <path d="M-136-106h272v192h-272z" fill="#2c3a30"/>
  <g fill="none" stroke="#e8f1e8" stroke-width="5" stroke-linecap="round">
    <path d="M-100-60h50M-90-84v48M-30-60h40M30-84l40 48M70-84l-40 48"/>
    <path d="M-100 10h60M-100 40q30-30 60 0M10 10h80M10 40h60"/>
  </g>
</g>
{person(140,350,1.15,1,'teal','blue','point','short','smile')}
<g transform="translate(140 190)">
  <path d="M0-40q30 0 30 28 0 16-14 24v12h-32v-12q-14-8-14-24 0-28 30-28z" class="gold o"/>
  <g class="golds"><path d="M-52-20l-18-8M52-20l18-8M0-56v-16"/></g>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('genre', '種類ごとに分けられた棚のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-230-110h460v230h-460z" fill="#fffdf6" class="o"/>
  <path d="M-76-110v230M76-110v230" class="a"/>
</g>
<g transform="translate(146 240)">
  <path d="M-40 40q-16 0-16-14t16-14q8 0 12 6V-40l40-12v20l-28 8v50q0 14-24 14z" class="coral o"/>
</g>
<g transform="translate(300 240)">
  <path d="M-44-46h88v92h-88z" class="teal o"/>
  <path d="M-44-46h88v92h-88zM-30-46v92" class="a"/>
</g>
<g transform="translate(456 240)">
  <path d="M-52-40h104v80h-104z" class="ink"/>
  <g fill="#fffdf6"><rect x="-40" y="-28" width="80" height="56"/></g>
  <g class="ink">{''.join(f'<rect x="-52" y="{-38+i*20}" width="12" height="12"/><rect x="40" y="{-38+i*20}" width="12" height="12"/>' for i in range(4))}</g>
</g>
<path d="M60 372h480" class="a"/>
""", ground=True)

add('gesture', '手ぶりで気持ちを伝えるイラスト。', f"""
{person(230,352,1.2,1,'teal','blue','point','short','smile')}
{hand(430,190,1)}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M492 140q22 22 0 44M520 118q40 40 0 88"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('glimpse', 'すき間からちらっと見えるイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-260-150h240v300h-240zM20-150h240v300H20z" class="bluep o"/>
  <path d="M-20-150v300M20-150v300" class="a"/>
</g>
<path d="M280 90h40v70h-40z" class="gold"/>
<circle cx="300" cy="200" r="18" class="coral o"/>
<path d="M280 240h40v100h-40z" class="teal"/>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M300 60v-30M240 60l-30-26M360 60l30-26"/></g>
""", ground=False)

add('globalization', '地球じゅうが線でつながるグローバル化のイラスト。', f"""
<g transform="translate(300 200)">
  <circle r="130" class="bluep o"/>
  <path d="M-70-100q60 20 30 60t20 70 60 20" class="greenp o"/>
  <path d="M40-110q50 10 60 50t-40 40" class="greenp o"/>
  <g fill="none" stroke="{INK}" stroke-width="2.5"><ellipse rx="60" ry="130"/><path d="M-130 0h260M-118-56h236M-118 56h236"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)">
  <path d="M120 90q60-70 170-70M480 300q-60 70-170 70M480 110q40 90-40 150"/>
</g>
<g class="coral">{''.join(f'<circle cx="{x}" cy="{y}" r="10"/>' for x,y in [(120,90),(480,300),(480,110),(300,20),(300,370),(120,300)])}</g>
""", ground=False, arrow=True)

add('globe', '台に載った地球儀のイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="110" class="bluep o"/>
  <path d="M-60-80q50 18 24 52t18 58 50 16" class="green o"/>
  <path d="M40-90q40 8 50 42t-34 34" class="green o"/>
  <g fill="none" stroke="{INK}" stroke-width="2.5"><ellipse rx="50" ry="110"/><path d="M-110 0h220"/></g>
</g>
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="9" stroke-linecap="round">
  <path d="M300 96a114 114 0 1 0 0 228"/>
</g>
<g transform="translate(300 350)">
  <path d="M-16-26h32v26h-32z" class="goldd o"/>
  <ellipse rx="70" ry="18" class="gold o"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('glory', '表彰台の頂点で光を浴びる栄光のイラスト。', f"""
{sun(300,110,44)}
{person(300,262,1,1,'coral','blue','up','short','smile')}
<g transform="translate(300 330)">
  <path d="M-56-70h112v70h-112z" class="gold o"/>
  <path d="M-166-30h110v30h-110z" class="goldp o"/>
  <path d="M56-14h110v14H56z" class="goldp o"/>
</g>
<g fill="{TONES['green'][0]}" stroke="{TONES['green'][2]}" stroke-width="2">
  <path d="M244 168q-22 30 0 52 8-30 0-52zM356 168q22 30 0 52-8-30 0-52z"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('goodness', '困っている人にそっと手を貸す優しさのイラスト。', f"""
{person(180,350,1.1,1,'teal','blue','give','short','smile')}
<g transform="translate(400 330)">
  <path d="M-40 30l-30-26M40 30l30-26" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10" stroke-linecap="round"/>
  <path d="M-30-4q30-16 60 0l-8 44h-44z" class="gold o"/>
  <circle cx="0" cy="-30" r="22" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-46-40l40 14" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
</g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M300 150q-22-28 0-40 22-12 22 16 0-28 22-16 22 12 0 40l-22 22z"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('governor', '州の旗の前で語る知事のイラスト。', f"""
{person(310,348,1.25,1,'violet','blue','point','short','neutral')}
<g transform="translate(310 330)">
  <path d="M-70-40h140l16 70h-172z" class="gold o"/>
  <path d="M-70-40h140v14h-140z" class="goldd o"/>
</g>
<g transform="translate(480 220)">
  <path d="M-6 140V-110" class="a"/>
  <path d="M-6-110h96v70h-96z" class="teal o"/>
  <circle cx="42" cy="-76" r="18" class="goldp o"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('grace', '水面をなめらかに進む白鳥の優雅さのイラスト。', f"""
<path d="M0 290h600v110H0z" class="bluep"/>
<g transform="translate(300 250)">
  <path d="M-110 40q-20-50 30-64 60-16 130-4-40 24-90 28 40 22 0 40z" fill="#fffdf6" class="o"/>
  <path d="M50-28q-14-70 26-84 44-16 54 22 8 28-24 34-24 4-20 28z" fill="#fffdf6" class="o"/>
  <path d="M126-92l26 10-26 12z" class="gold o"/>
  <circle cx="112" cy="-94" r="4" class="ink"/>
  <path d="M-60-8q40-26 90-6" fill="none" stroke="{MUTED}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3">
  <path d="M80 330q40-16 80 0t80 0M340 350q40-16 80 0t80 0"/>
</g>
""", ground=False)

add('gradually', '少しずつ段を上げてだんだん増えるイラスト。', f"""
<g transform="translate(300 250)">
  <g class="teal o">{''.join(f'<rect x="{-220+i*62}" y="{-16-i*24}" width="48" height="{40+i*24}"/>' for i in range(7))}</g>
  <path d="M-230 30h470" class="a"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)">
  <path d="M80 250q210-100 440-160"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('graduate', '角帽をかぶって卒業証書を受け取るイラスト。', f"""
{person(280,350,1.25,1,'violet','violet','give','short','smile')}
<g transform="translate(280 200)">
  <path d="M-56-6L0-32l56 26L0 20z" class="ink"/>
  <path d="M36 2v34" fill="none" stroke="{TONES['gold'][0]}" stroke-width="4"/>
  <circle cx="36" cy="40" r="7" class="gold"/>
</g>
<g transform="translate(450 250)">
  <path d="M-24-70h48v140h-48z" fill="#fffdf6" class="o" transform="rotate(24 0 0)"/>
  <path d="M-30 0h60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" transform="rotate(24 0 0)"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('graphics', '画面に描かれた図や絵のイラスト。', f"""
<g transform="translate(300 190)">
  <path d="M-190-120h380v240h-380z" class="ink"/>
  <path d="M-174-106h348v212h-348z" fill="#fffdf6"/>
  <circle cx="-90" cy="-40" r="46" class="coralp o"/>
  <path d="M10-90h110v100H10z" class="tealp o"/>
  <path d="M-140 90l70-90 60 90z" class="gold o"/>
  <g class="violet">{''.join(f'<rect x="{40+i*30}" y="{60-i*30}" width="20" height="{30+i*30}"/>' for i in range(3))}</g>
</g>
<g transform="translate(400 340)">
  <path d="M-110-14h150v28h-150z" class="bluep o"/>
  <path d="M40-14l70-20v68l-70-20z" class="blue o"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('gratitude', '贈り物を受けて心から感謝するイラスト。', f"""
{person(170,350,1.1,1,'teal','blue','give','short','smile')}
<g transform="translate(300 260)">
  <path d="M-56-40h112v70h-112z" class="coral o"/>
  <path d="M-56-40h112v18h-112zM-8-40v70" class="a"/>
  <path d="M0-40q-30-30-40-6 20 12 40 6zM0-40q30-30 40-6-20 12-40 6z" class="coralp o"/>
</g>
{person(460,350,1.1,-1,'gold','violet','give','bob','smile')}
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M470 160q-20-26 0-36 20-10 20 14 0-24 20-14 20 10 0 36l-20 20z"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('grave', '土を盛って石を立てた墓のイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-90-110h180v130h-180z" fill="#dfe6ea" class="o"/>
  <path d="M-90-110q90-40 180 0z" fill="#dfe6ea" class="o"/>
  <g fill="{MUTED}"><rect x="-40" y="-70" width="80" height="12"/><rect x="-8" y="-90" width="16" height="70"/></g>
  <path d="M-160 20q160-50 320 0z" class="greenp o"/>
</g>
<g class="greens"><path d="M170 300q30-30 60 0M380 300q30-30 60 0"/></g>
<path d="M60 320h480" class="a"/>
""", ground=True)

add('gravity', 'りんごが地面へ引かれて落ちる重力のイラスト。', f"""
{tree(150,330,1.3)}
<circle cx="380" cy="120" r="26" class="coral o"/>
<path d="M380 96v-14" class="greens"/>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9"><path d="M380 150v130"/></g>
<circle cx="380" cy="300" r="26" class="coral o"/>
<path d="M380 170v90" class="a" marker-end="url(#ar)"/>
<path d="M60 336h480" class="a"/>
""", ground=True, arrow=True)

add('greenhouse', 'ガラス張りの中で植物を育てる温室のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-180 80v-90q0-70 180-70t180 70v90z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3">
    <path d="M-90-72v152M0-80v160M90-72v152M-180-10h360M-180 36h360"/>
  </g>
  <path d="M-40 80V20h80v60z" class="teal o"/>
</g>
<g class="greens"><path d="M180 300v-30M420 300v-30"/></g>
<g class="greenp o"><circle cx="180" cy="262" r="22"/><circle cx="420" cy="262" r="22"/></g>
{sun(510,90,34)}
<path d="M60 322h480" class="a"/>
""", ground=True)

add('grid', '縦横に組まれた格子と送電網のイラスト。', f"""
<g transform="translate(300 210)">
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4">
    {''.join(f'<path d="M{-200+i*80} -110v220"/>' for i in range(6))}
    {''.join(f'<path d="M-200 {-110+i*55}h400"/>' for i in range(5))}
  </g>
</g>
<g transform="translate(140 330)">
  <path d="M-30 0l14-90h32L30 0M-24-40h48M-16-90h32" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g transform="translate(460 330)">
  <path d="M-30 0l14-90h32L30 0M-24-40h48M-16-90h32" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<path d="M124 246q160 40 312 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('grief', '深い悲しみに沈んで泣くイラスト。', f"""
{person(300,352,1.35,1,'blue','blue','think','bob','sad')}
{drop(268,240,1.2,'blue')}
{drop(336,246,1.2,'blue')}
{cloud(300,90,1.1,'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3" stroke-linecap="round">
  <path d="M250 130v26M290 138v26M330 130v26M370 140v22"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('growth', '芽が伸びて大きく育つ成長のイラスト。', f"""
<g transform="translate(130 330)">
  <path d="M0 0v-30" class="greens"/>
  <path d="M0-30q-24-4-26-24 22-2 26 24z" class="greenp o"/>
</g>
<g transform="translate(300 330)">
  <path d="M0 0v-90" class="greens"/>
  <path d="M0-50q-34-6-38-34 32-4 38 34zM0-70q34-6 38-34-32-4-38 34z" class="greenp o"/>
</g>
{tree(470,330,1.4)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)">
  <path d="M130 250q140-110 340-140"/>
</g>
<path d="M60 336h480" class="a"/>
""", ground=True, arrow=True)

add('guidance', '道しるべを示して導くイラスト。', f"""
{person(160,350,1.15,1,'teal','blue','point','short','smile')}
{person(300,356,0.95,1,'coral','gold','walk','bob','smile')}
<g transform="translate(470 300)">
  <path d="M-6 60V-90" class="a"/>
  <path d="M-6-90h90l24 24-24 24H-6z" class="gold o"/>
  <path d="M-6-30h70l20 20-20 20H-6z" class="goldp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M230 300h180"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('guideline', '守るべき筋道を示した指針のイラスト。', f"""
<g transform="translate(230 200)">
  <path d="M-130-140h260v290h-260z" class="paper"/>
  <path d="M-90-110h180v24h-180z" class="teal o"/>
  <g fill="none" stroke="{GRN}" stroke-width="6" stroke-linecap="round">
    <path d="M-90-50l14 14 24-30M-90 10l14 14 24-30M-90 70l14 14 24-30"/>
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-30-46h120M-30 14h120M-30 74h100"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)">
  <path d="M400 340q60-120 60-240"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('guilt', '悪いことをしてしまい心が重くなるイラスト。', f"""
{person(220,352,1.2,1,'blue','blue','think','short','sad')}
{cloud(200,100,1.1,'violet')}
<g transform="translate(450 300)">
  <path d="M-56 40q-16-60 6-90l36 16 14-24 30 30 30-14q14 40 4 82z" class="goldp o"/>
  <path d="M-16-34l14 74M28-18l-8 58" class="a"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M330 300l50-20M340 340l40 0"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('gut', 'おなかの中の腸を示したイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-110 130v-90q0-110 110-110T110 40v90z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-70-40q0-40 70-40t70 40v30q0 30-40 30t-40 30 40 30 40 30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M-70-40q0-40 70-40t70 40v30q0 30-40 30t-40 30 40 30 40 30" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4" stroke-dasharray="4 14"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('habitat', '生き物が暮らす場所のイラスト。', f"""
{tree(110,320,1.1)}
{tree(500,320,1.2)}
<path d="M180 330q120-40 240 0z" class="bluep o"/>
<g transform="translate(300 300)">
  <ellipse rx="46" ry="30" class="goldp o"/>
  <circle cx="40" cy="-24" r="22" class="goldp o"/>
  <path d="M58-28l24 8-24 10z" class="gold o"/>
  <circle cx="46" cy="-30" r="4" class="ink"/>
  <path d="M-30 26v20M10 28v18" fill="none" stroke="{TONES['gold'][2]}" stroke-width="8" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><rect x="70" y="140" width="470" height="210" rx="30"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('handful', '手のひらにひと握りだけあるイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-120 20q-16-50 20-70 40-22 100-22t100 22q36 20 20 70z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-120 20q0 40 120 40T120 20z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <g class="teal o"><circle cx="-40" cy="-42" r="16"/><circle cx="0" cy="-54" r="16"/><circle cx="40" cy="-44" r="16"/><circle cx="-16" cy="-24" r="16"/><circle cx="24" cy="-22" r="16"/></g>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('handling', '壊れ物をていねいに扱うイラスト。', f"""
{box(300,220,170,120,32,'gold')}
{hand(120,270,1)}
{hand(480,270,-1)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5">
  <path d="M292 178l14 30h-20l14 30" stroke-linecap="round"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('harassment', 'しつこく言い寄られて嫌がっているイラスト。', f"""
{person(160,352,1.15,1,'violet','blue','point','short','neutral')}
<g transform="translate(310 180)">
  <path d="M-70-40h140v60h-140zM-40 20l-10 26 34-26z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M-44-18h88M-44 2h60"/></g>
</g>
{person(470,352,1.15,-1,'coral','gold','stand','bob','sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round"><path d="M420 200l-16-22M470 186v-26"/></g>
{xx(310,300,0.8)}
<path d="M60 376h480" class="a"/>
""", ground=True)

add('harbour', '船がつながれた港のイラスト。', f"""
<path d="M0 250h600v150H0z" class="bluep"/>
<g transform="translate(300 240)">
  <path d="M-140 10h280l-40 60h-200z" class="coral o"/>
  <path d="M-70 10v-70h30v70zM-30-60l90 30-90 30z" class="gold o"/>
  <g fill="#fffdf6" class="o"><rect x="60" y="-30" width="60" height="40"/></g>
</g>
<g transform="translate(80 240)">
  <path d="M-30 0v-90h100" fill="none" stroke="{INK}" stroke-width="8"/>
  <path d="M70-90v40" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M-60 0h60v20h-60z" class="ink"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"><path d="M60 330q40-16 80 0t80 0M380 350q40-16 80 0t80 0"/></g>
""", ground=False)

add('hardly', 'ほとんど残っていないことを示すイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-100-130h200v260h-200z" fill="#fffdf6" class="o"/>
  <path d="M-100 106h200v24h-200z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-100 {80-i*44}h40"/>' for i in range(5))}</g>
</g>
{xx(470,180,1)}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('hardship', '重荷を背負って坂を登る苦難のイラスト。', f"""
<path d="M60 356L520 150v206z" class="greenp o"/>
{person(230,300,1.1,1,'coral','blue','walk','short','sad')}
{box(212,196,110,80,24,'gold')}
{cloud(160,90,1,'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3" stroke-linecap="round">
  <path d="M120 130v24M160 138v24M200 130v24"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M330 250l100-46"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('hardware', '機械を組み立てる部品のイラスト。', f"""
<g transform="translate(230 230)">
  <path d="M-130-100h260v200h-260z" class="greenp o"/>
  <path d="M-50-40h100v90h-100z" class="ink"/>
  <g class="ink">{''.join(f'<rect x="{-64}" y="{-30+i*20}" width="14" height="8"/><rect x="50" y="{-30+i*20}" width="14" height="8"/>' for i in range(4))}</g>
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="3"><path d="M-110-70h50v40M110 60H60v-40M-110 60h40v-30"/></g>
  <circle cx="-90" cy="-20" r="12" class="gold o"/>
  <circle cx="90" cy="-70" r="12" class="gold o"/>
</g>
<g transform="translate(470 260)">
  <path d="M-70-50h140v100h-140z" fill="#dfe6ea" class="o"/>
  <circle r="26" fill="none" stroke="{MUTED}" stroke-width="8"/>
  <circle r="6" class="ink"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('harm', '傷つけて害を与えることを示すイラスト。', f"""
<g transform="translate(330 280)">
  <path d="M0 40V-20" class="greens"/>
  <path d="M0-20q-40-6-44-40 38-4 44 40z" class="greenp o"/>
  <path d="M0-40q40-6 44-40-38-4-44 40z" class="greenp o" transform="rotate(30 0 -40)"/>
  <path d="M-40 40h80" class="a"/>
</g>
{hand(140,200,1)}
<g class="a" marker-end="url(#ar)"><path d="M230 240l60 30"/></g>
{xx(460,180,1)}
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('harmony', '音が重なって心地よく響く調和のイラスト。', f"""
<g transform="translate(300 210)">
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><circle cx="-90" cy="0" r="70"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><circle cx="0" cy="0" r="70"/></g>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4"><circle cx="90" cy="0" r="70"/></g>
  <g class="ink">
    <path d="M-118 30q-14 0-14-12t14-12q8 0 12 5v-45l30-9v14l-20 6v40q0 13-22 13z"/>
    <path d="M-28 30q-14 0-14-12t14-12q8 0 12 5v-45l30-9v14l-20 6v40q0 13-22 13z"/>
    <path d="M62 30q-14 0-14-12t14-12q8 0 12 5v-45l30-9v14l-20 6v40q0 13-22 13z"/>
  </g>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('harvest', '実った作物を刈り取って集める収穫のイラスト。', f"""
<g class="golds" stroke-width="5">{''.join(f'<path d="M{380+i*40} 330v-90"/>' for i in range(5))}</g>
<g class="gold o">{''.join(f'<ellipse cx="{380+i*40}" cy="228" rx="12" ry="26"/>' for i in range(5))}</g>
{person(200,346,1.1,1,'teal','blue','reach','bun','smile')}
<g transform="translate(120 300)">
  <path d="M-56 0h112l-16 56h-80z" class="goldp o"/>
  <path d="M-56 0h112" class="a"/>
  <g class="gold o"><ellipse cx="-24" cy="-12" rx="10" ry="20"/><ellipse cx="4" cy="-16" rx="10" ry="20"/><ellipse cx="30" cy="-10" rx="10" ry="20"/></g>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('hatred', '背を向け合って強く憎み合うイラスト。', f"""
{person(160,352,1.2,-1,'blue','blue','stand','short','sad')}
{person(440,352,1.2,1,'coral','gold','stand','bob','sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M250 200l40 34-30 24 40 32"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M110 190l-16-24M210 176v-26M390 176v-26M490 190l16-24"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('hazard', '足もとの危険を知らせる標識のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M0-130l140 240h-280z" class="gold o"/>
  <g fill="{INK}"><rect x="-14" y="-40" width="28" height="90" rx="14"/><circle cy="72" r="17"/></g>
</g>
<path d="M294 330v50" class="a"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M120 300q30-20 60 0M420 300q30-20 60 0"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
