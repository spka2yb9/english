"""第73回: 承認・側面・障壁・かごなど45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('approval', '書類に承認の印が押されるイラスト。', f"""
<g transform="translate(280 240)">
  <path d="M-150-130h300v260h-300z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-110-80h220M-110-40h220M-110 0h180"/></g>
  <g transform="translate(50 60) rotate(-12)">
    <circle r="50" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
    <path d="M-24 0l18 20 32-38" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"/>
  </g>
</g>
<g transform="translate(490 160)"><path d="M-40-30h80v40h-80z" class="ink"/><path d="M-16-80h32v50h-32z" class="ink"/></g>
""", ground=True)

add('approximately', 'ぴたりでなく、およその数を示すイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-170-80h340v160h-340z" class="paper"/>
  <g fill="{INK}"><rect x="-80" y="-20" width="160" height="26"/></g>
  <g fill="none" stroke="{INK}" stroke-width="7"><path d="M-140-20q26-20 52 0M-140 14q26-20 52 0"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><rect x="120" y="120" width="360" height="200" rx="14"/></g>
""", ground=True)

add('archive', '古い記録をまとめて保管する棚のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-210-140h420v20h-420zM-210-40h420v20h-420zM-210 60h420v20h-420zM-210 160h420v20h-420z" class="goldd o"/>
  <path d="M-220-140h20v320h-20zM200-140h20v320h-20z" class="goldd o"/>
  <g class="tealp o">{''.join(f'<rect x="{-180+c*44}" y="-120" width="34" height="80"/>' for c in range(4))}</g>
  <g class="coralp o">{''.join(f'<rect x="{-180+c*44}" y="-20" width="34" height="80"/>' for c in range(5))}</g>
  <g class="goldp o">{''.join(f'<rect x="{-180+c*44}" y="80" width="34" height="80"/>' for c in range(3))}</g>
</g>
<path d="M60 416h480" class="a"/>
""", ground=True)

add('arena', '観客に囲まれた円い競技場のイラスト。', f"""
<g transform="translate(300 230)">
  <ellipse rx="230" ry="140" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <ellipse rx="160" ry="90" fill="#e6dcc9" stroke="{INK}" stroke-width="3"/>
  <g fill="{MUTED}">{''.join(f'<circle cx="{int(200*__import__("math").cos(i*3.14159/8))}" cy="{int(120*__import__("math").sin(i*3.14159/8))}" r="8"/>' for i in range(16))}</g>
  <g transform="translate(0 30) scale(0.6)">{person(0,0,1.0,1,'coral','blue','up','short','smile')}</g>
</g>
""", ground=False)

add('array', '同じものがずらりと並ぶイラスト。', f"""
<g class="teal o">{''.join(f'<rect x="{100+c*70}" y="{160+r*60}" width="52" height="46"/>' for r in range(3) for c in range(6))}</g>
<g class="a" marker-end="url(#ar)"><path d="M100 360h430"/></g>
""", ground=False, arrow=True)

add('arrow', '向きを示す矢印のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-160-30h200v-50l120 80-120 80v-50h-200z" class="coral o"/>
</g>
<path d="M120 350h360" class="a"/>
""", ground=False)

add('artwork', '額に入った芸術作品のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-140h360v280h-360z" class="goldd o"/>
  <path d="M-150-110h300v220h-300z" fill="#fffdf6" class="o"/>
  <g class="coralp o"><circle cx="-70" cy="-30" r="50"/></g>
  <g class="tealp o"><path d="M0 60h120v-100H0z"/></g>
  <g class="goldp o"><path d="M-140 60l60-90 50 90z"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('ash', '燃えつきたあとに残る灰のイラスト。', f"""
{flame(170,250,0.9)}
<g transform="translate(430 320)">
  <path d="M-90 30q30-50 90-50t90 50z" fill="#c9c6b8" stroke="{MUTED}" stroke-width="3"/>
  <g class="muted"><path d="M-30-30q20-30 0-50M30-30q20-30 0-50"/></g>
</g>
<path d="M270 250h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('aspect', '立方体のうち、一つの面を示したイラスト。', f"""
<g transform="translate(280 240)">
  {box(280,240,200,150,40,'teal')}
</g>
<g transform="translate(280 240)"><path d="M-100-75h200v150h-200z" class="coral o" opacity=".85"/></g>
<path d="M480 300h-70" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('aspiration', '高い星を見上げて強く願うイラスト。', f"""
<g transform="translate(470 120)"><path d="M0-40l14 28 30 4-22 21 6 30-28-15-28 15 6-30-22-21 30-4z" class="gold o"/></g>
{person(180,346,1.25,1,'violet','blue','up','short','neutral')}
<g transform="translate(280 180)">
  <path d="M-70-40h140v60h-140z" fill="#fffdf6" class="o"/>
  <g transform="translate(0 -10)"><path d="M0-14l6 12 14 2-10 10 2 14-12-8-12 8 2-14-10-10 14-2z" class="gold o"/></g>
</g>
<path d="M330 200q80-40 110-60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('assassination', '要人が命をねらわれることを示したイラスト。', f"""
{person(400,346,1.25,1,'blue','blue','stand','short','sad')}
<g transform="translate(400 226)"><path d="M-16-16l6 14 16 2-12 11 3 16-13-8-13 8 3-16-12-11 16-2z" class="gold o"/></g>
<g transform="translate(180 250)">
  <path d="M-60 90q-16-140 60-140t60 140z" fill="#41506a"/>
  <g fill="{TONES['coral'][0]}"><path d="M-26-40l22 14-22 14zM26-40l-22 14 22 14z"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M260 230h70"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('assertion', '手を上げて、はっきり言い切るイラスト。', f"""
{person(180,346,1.25,1,'blue','blue','up','short','neutral')}
<g transform="translate(400 200)">
  <path d="M-100-60h200v90h-200z" fill="#fffdf6" class="o"/>
  <path d="M-60 30l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-70" y="-34" width="140" height="18"/><rect x="-70" y="-4" width="100" height="18"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('assumption', '確かめないまま前提として置くイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','think','short','neutral')}
<g transform="translate(430 190)">
  <path d="M-130-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-166q-38-4-26-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="9 8"><rect x="-60" y="-40" width="120" height="70"/></g>
  <g class="tealp o"><rect x="-40" y="-24" width="80" height="40"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M300 320h100"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M330 350l28 28M358 350l-28 28"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('assurance', '大丈夫だと保証の印をつけて渡すイラスト。', f"""
{person(160,346,1.15,1,'blue','blue','give','short','smile')}
<g transform="translate(340 240)">
  <path d="M-90-70h180v140h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-40h120M-60-10h120"/></g>
  <g transform="translate(40 40)"><circle r="26" fill="none" stroke="{TONES['green'][0]}" stroke-width="5"/><path d="M-12 0l10 10 18-20" fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"/></g>
</g>
{person(490,346,1.15,-1,'coral','gold','reach','bob','smile')}
<path d="M440 300h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('asylum', '逃れてきた人を受け入れて守るイラスト。', f"""
<g transform="translate(400 260)">
  <path d="M-110 80h220V-40h-220z" fill="#f4ead2" class="o"/>
  <path d="M-130-40l130-80 130 80z" class="teal o"/>
  <path d="M-30 80V20h60v60z" class="goldd o"/>
</g>
{person(160,340,1.05,1,'coral','gold','carry','bob','sad')}
<path d="M240 300h80" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 150l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('atrocity', 'むごい行いが行われた跡を示したイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#9b9683"/>
<g fill="#7d7a67" stroke="{INK}" stroke-width="3">
  <path d="M120 340v-110l60-30v140z" transform="rotate(-8 150 300)"/>
  <path d="M240 340v-80l60 20v60z"/>
  <path d="M360 340v-130l70 50v80z" transform="rotate(6 400 300)"/>
</g>
<g class="muted" opacity=".9"><path d="M200 190q30-40 0-70M420 170q30-40 0-70"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M480 90l34 34M514 90l-34 34"/></g>
""", ground=False)

add('attachment', 'メールに書類を添えて送るイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-150-100h300v200h-300z" class="paper"/>
  <path d="M-150-100l150 110 150-110" fill="none" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(90 60)">
    <path d="M-30-20h60v40h-60z" class="tealp o"/>
    <path d="M-10-40q30-20 30 20t-30 20" fill="none" stroke="{INK}" stroke-width="6"/>
  </g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('attempt', '一度はずしても、もう一度ためすイラスト。', f"""
{person(150,346,1.1,1,'teal','blue','reach','short','neutral')}
<g transform="translate(450 220)">
  <circle r="70" fill="#fffdf6" class="o"/>
  <circle r="44" class="coralp o"/>
  <circle r="18" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9" marker-end="url(#ar)"><path d="M230 250q100-70 160-90"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M230 280q110-20 190-50"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('attendance', '名簿に出席の印がつくイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <g fill="{MUTED}">{''.join(f'<rect x="-90" y="{-100+i*50}" width="150" height="14"/>' for i in range(4))}</g>
  <g fill="none" stroke="{INK}" stroke-width="3">{''.join(f'<rect x="-140" y="{-106+i*50}" width="28" height="28"/>' for i in range(4))}</g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round">
    <path d="M-134-96l10 10 18-22"/><path d="M-134-46l10 10 18-22"/><path d="M-134 54l10 10 18-22"/>
  </g>
</g>
""", ground=True)

add('attorney', '書類を手に法廷で代弁する弁護士のイラスト。', f"""
<g transform="translate(440 150)">
  <path d="M-80 40h160v20h-160z" class="goldd o"/>
  <path d="M-6-60h12v100h-12z" class="ink"/>
  <path d="M-60-60h120v10h-120z" class="ink"/>
  <g class="goldp o"><path d="M-60-50l-24 34h48z"/><path d="M60-50l-24 34h48z"/></g>
</g>
{person(180,346,1.25,1,'blue','blue','carry','short','neutral')}
<g transform="translate(180 250)"><path d="M-50-30h100v50h-100z" class="paper"/></g>
<path d="M280 250h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('auction', '札を上げて競り合うイラスト。', f"""
{person(160,346,1.05,1,'teal','blue','up','short','neutral')}
{person(280,346,1.05,1,'coral','gold','up','bob','neutral')}
<g transform="translate(160 200)"><path d="M-24-16h48v26h-48z" class="paper"/></g>
<g transform="translate(280 190)"><path d="M-24-16h48v26h-48z" class="paper"/></g>
<g transform="translate(460 260)">
  <path d="M-60-20h120v40h-120z" class="goldd o"/>
  <g transform="translate(0 -80) rotate(-24)"><path d="M-40-24h80v48h-80z" fill="#8b5e3c" stroke="{INK}" stroke-width="3"/><path d="M-10 24h20v70h-20z" class="goldd o"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('audit', '帳簿を細かく検査するイラスト。', f"""
<g transform="translate(260 250)">
  <path d="M-150-120h300v240h-300z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-110 {-80+i*40}h220"/>' for i in range(5))}</g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"><path d="M-130-86l12 12 20-24"/><path d="M-130-46l12 12 20-24"/></g>
</g>
<g transform="translate(430 200) rotate(24)">
  <circle r="70" fill="#e7f6fb" opacity=".85" stroke="{INK}" stroke-width="8"/>
  <path d="M0 70v70" fill="none" stroke="{INK}" stroke-width="16"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('automatically', '手を触れずとも自ずと動くイラスト。', f"""
<g transform="translate(380 240)">
  <path d="M-120-100h240v200h-240z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="10"><circle cx="-40" cy="-20" r="40"/><circle cx="40" cy="30" r="28"/></g>
  <g class="green o"><circle cx="80" cy="-70" r="12"/></g>
</g>
{hand(170,240,1)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M140 300l40 40M180 300l-40 40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('availability', '空きがあるかどうかを示す表のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-130h380v260h-380z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">{''.join(f'<path d="M{-190+c*95}-130v260"/>' for c in range(1,4))}{''.join(f'<path d="M-190 {-44+r*86}h380"/>' for r in range(2))}</g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round"><path d="M-150-100l14 14 24-30"/><path d="M40-14l14 14 24-30"/><path d="M-55 72l14 14 24-30"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round"><path d="M-50-100l30 30M-20-100l-30 30"/><path d="M135-14l30 30M165-14l-30 30"/></g>
</g>
""", ground=True)

add('awareness', 'まわりの様子に気づいているイラスト。', f"""
{person(200,346,1.25,1,'teal','blue','think','short','neutral')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="12 9"><circle cx="200" cy="260" r="140"/></g>
<g class="coralp o"><circle cx="430" cy="180" r="26"/></g>
<g class="goldp o"><rect x="400" y="290" width="60" height="50"/></g>
<path d="M330 200h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('backdrop', '人物の後ろに広がる背景幕のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-220-140h440v280h-440z" fill="#cfe6f5" class="o"/>
  <g fill="#b9c8d6"><path d="M-100 140l120-140 120 140z"/></g>
  {sun(-140,-80,26)}
</g>
{person(300,346,1.1,1,'coral','gold','stand','bob','smile')}
<path d="M470 100v60" class="a" marker-end="url(#ar)" transform="rotate(180 470 130)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('backing', '後ろから支えて後押しするイラスト。', f"""
{person(360,346,1.25,1,'coral','gold','walk','bob','smile')}
{person(200,346,1.15,1,'blue','blue','reach','short','smile')}
<path d="M270 250h40" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<path d="M440 250h80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('backup', '本体のほかに控えを用意しておくイラスト。', f"""
<g transform="translate(190 250)">
  <path d="M-80-70h160v140h-160z" class="teal o"/>
  <g class="green o"><circle cx="50" cy="-50" r="12"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-80-70h160v140h-160z" class="tealp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><rect x="-80" y="-70" width="160" height="140"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 250h50"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('backwards', '後ろ向きに下がって進むイラスト。', f"""
{person(320,346,1.2,-1,'teal','blue','walk','short','neutral')}
<path d="M250 250h-140" class="a" marker-end="url(#ar)"/>
<g fill="{MUTED}"><ellipse cx="400" cy="366" rx="22" ry="9"/><ellipse cx="460" cy="374" rx="20" ry="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('bacteria', '顕微鏡で見える細菌のイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="150" fill="#e7f6fb" opacity=".7" stroke="{INK}" stroke-width="3"/>
  <g class="green o"><ellipse cx="-60" cy="-30" rx="44" ry="22" transform="rotate(-20 -60 -30)"/><ellipse cx="40" cy="20" rx="44" ry="22" transform="rotate(24 40 20)"/><ellipse cx="-10" cy="80" rx="36" ry="18"/></g>
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="3"><path d="M-100-56q-20-20-40-10M84 34q20-20 40-10"/></g>
</g>
""", ground=False)

add('badge', '胸につける記章のイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="100" class="gold o"/>
  <circle r="76" fill="#f7e6bd" stroke="{INK}" stroke-width="3"/>
  <path d="M0-40l14 28 30 4-22 21 6 30-28-15-28 15 6-30-22-21 30-4z" class="goldd o"/>
  <path d="M-40 100h80l-20 60-20-30-20 30z" class="coralp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('bail', 'お金を積んで、いったん出してもらうイラスト。', f"""
<g transform="translate(200 240)">
  <path d="M-110-120h220v240h-220z" fill="#e4e9ee" class="o"/>
  <g fill="{INK}">{''.join(f'<rect x="{-90+i*46}" y="-100" width="14" height="200"/>' for i in range(4))}</g>
</g>
<g transform="translate(400 280)">
  <path d="M-60-30h120v50h-120z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <circle r="16" class="goldd o"/>
</g>
{person(490,346,1.0,1,'violet','violet','walk','cap','neutral')}
<path d="M330 200h100" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('ballet', 'つま先立ちで舞うバレエのイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-30-100q34-16 60 0l-6 60h-50z" class="coralp o"/>
  <path d="M-24-40h68l30 30h-128z" class="coralp o"/>
  <circle cy="-128" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-26-138q4-30 28-30t28 30q-28-14-56 0z" fill="{HAIR}"/>
  <path d="M-30-100q-40-40-30-70" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
  <path d="M30-100q40-40 30-70" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-10-10v60M10-10l50 40" fill="none" stroke="{SKIN}" stroke-width="13" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('ballot', '投票用紙を箱に入れるイラスト。', f"""
<g transform="translate(340 290)">
  <path d="M-100-60h200v120h-200z" fill="#dfe6ea" class="o"/>
  <path d="M-40-70h80v14h-80z" class="ink"/>
</g>
<g transform="translate(330 170) rotate(-10)">
  <path d="M-60-40h120v70h-120z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><rect x="-44" y="-24" width="20" height="20"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"><path d="M-40-16l10 10 18-22"/></g>
</g>
{hand(180,220,1)}
<path d="M240 220h40" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('ban', '赤い禁止の輪で、してはいけないと示すイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="24"/>
  <path d="M-86-86l172 172" fill="none" stroke="{TONES['coral'][0]}" stroke-width="24"/>
  <g opacity=".5"><path d="M-60-20h120v60h-120z" class="tealp o"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('banner', '横に長い横断幕を張るイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-240-10h480v14h-480z" class="ink"/>
  <path d="M-200 4h400v110h-400z" class="coralp o"/>
  <g fill="{INK}"><rect x="-140" y="40" width="280" height="24"/></g>
</g>
{person(140,346,0.8,1,'teal','blue','up','short','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('barrel', '木のたるのイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-80-110q-30 110 0 220h160q30-110 0-220z" fill="#c9a06b" stroke="{INK}" stroke-width="3"/>
  <ellipse cy="-110" rx="80" ry="22" fill="#d9b476" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#8b5e3c" stroke-width="8"><path d="M-92-40h184M-92 50h184"/></g>
  <g fill="none" stroke="#8b5e3c" stroke-width="3"><path d="M-30-108v216M30-108v216"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('barrier', '行く手をふさぐ柵のイラスト。', f"""
<g transform="translate(360 260)">
  <path d="M-20-140h40v280h-40z" fill="#c9d3dc" class="o"/>
  <path d="M-140-40h280v30h-280z" class="coral o"/>
  <path d="M-140-10h280v30h-280z" fill="#fffdf6" stroke="{INK}" stroke-width="2"/>
</g>
{person(150,346,1.05,1,'teal','blue','walk','short','flat')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M230 250h60"/></g>
<path d="M60 396h480" class="a"/>
""", ground=True, arrow=True)

add('basement', '建物の地下にある部屋のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-180-120h360v120h-360z" fill="#f4ead2" class="o"/>
  <path d="M-200-120l200-70 200 70z" class="coral o"/>
  <path d="M-180 0h360v120h-360z" fill="#dfe6ea" class="o"/>
  <path d="M-180 0h360" fill="none" stroke="{INK}" stroke-width="5"/>
  <g fill="#cfd8e0"><rect x="-60" y="30" width="120" height="60"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="120" y="210" width="360" height="120"/></g>
<path d="M520 270h-50" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('basket', '編んだかごのイラスト。', f"""
<g transform="translate(300 270)">
  <path d="M-110-40h220l-24 120h-172z" fill="#d9b476" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#b09274" stroke-width="3">{''.join(f'<path d="M{-90+i*36}-40l{6+i} 120"/>' for i in range(6))}<path d="M-104 0h208M-96 40h192"/></g>
  <path d="M-110-40q110-90 220 0" fill="none" stroke="#b09274" stroke-width="10"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('bass', '低い音を出す太い弦のイラスト。', f"""
<g transform="translate(300 250)">
  <ellipse rx="90" ry="110" class="goldd o"/>
  <path d="M-10-190h20v90h-20z" class="ink"/>
  <path d="M-30-206h60v20h-60z" class="goldd o"/>
  <circle cy="10" r="26" fill="#fffaf1" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{INK}" stroke-width="4"><path d="M-12-180v180M0-180v180M12-180v180"/></g>
</g>
<g class="corals" opacity=".8" style="stroke-width:6"><path d="M440 240q26 26 26 50M480 210q40 40 40 80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('bat', '夜に飛ぶコウモリのイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#2b3a52"/>
<g transform="translate(300 200)">
  <ellipse rx="40" ry="50" class="ink"/>
  <path d="M-30-30l-40-30-20-40-20 50-40 20 40 20 20 50 20-40 40-30z" class="ink"/>
  <path d="M30-30l40-30 20-40 20 50 40 20-40 20-20 50-20-40-40-30z" class="ink"/>
  <path d="M-20-46l-10-30 26 16zM20-46l10-30-26 16z" class="ink"/>
  <g fill="#f3c94f"><circle cx="-12" cy="-20" r="5"/><circle cx="12" cy="-20" r="5"/></g>
</g>
<g fill="#f3e3ae"><path d="M480 90a56 56 0 1 0 0 84 44 44 0 1 1 0-84z"/></g>
""", ground=False)

add('battlefield', '戦いのあとが残る野のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#c9c6b8"/>
<g class="green o" opacity=".5"><path d="M0 320q150-30 300-10t300-20v110H0z"/></g>
<g transform="translate(160 250)"><path d="M-4-70h8v100h-8z" class="ink"/><path d="M4-66h50v34H4z" class="coralp o"/></g>
<g transform="translate(430 250)"><path d="M-4-70h8v100h-8z" class="ink"/><path d="M-54-66h50v34h-50z" class="tealp o"/></g>
<g fill="#a9a396" stroke="{INK}" stroke-width="2"><path d="M250 330l40-30 30 30z"/><path d="M330 330l30-20 20 20z"/></g>
<g class="muted" opacity=".9"><path d="M300 250q30-40 0-70"/></g>
""", ground=False)

add('bay', '陸が湾のように入りこんだ海のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#dff0fa"/>
<g class="green o" opacity=".9"><path d="M0 400V180q120 0 150 60t120 20 130-60 200-40v240z" /></g>
<path d="M0 400v-120q140 20 180 80t170 20 150-100 100-40" fill="none" stroke="{TONES['blue'][2]}" stroke-width="0"/>
<g fill="none" stroke="{TONES['blue'][2]}" stroke-width="4" opacity=".7"><path d="M120 340q40-20 80 0M300 360q40-20 80 0"/></g>
{sun(500,80,26)}
""", ground=False)

add('beam', '一筋の光線が伸びるイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#33445c"/>
<g transform="translate(140 200)">
  <path d="M-50-40h60v80h-60z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <circle cx="14" r="24" fill="#f7e6bd"/>
</g>
<g fill="#f7e6bd" opacity=".5"><path d="M160 180L520 100v200L160 220z"/></g>
<g fill="#f7e6bd"><circle cx="520" cy="200" r="14"/></g>
""", ground=False)
print(len(W), ' '.join(W)); print(sheet(W))
