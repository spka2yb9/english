"""第28回: 予備・盗む・蒸気・切り替えなど30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('spare', '使っているタイヤの横に、予備のタイヤが置かれているイラスト。', f"""
<g transform="translate(200 250)">
  <circle r="90" fill="none" stroke="{INK}" stroke-width="24"/>
  <circle r="40" class="ink"/>
</g>
<g transform="translate(430 280)" opacity=".85">
  <circle r="66" fill="none" stroke="{MUTED}" stroke-width="20"/>
  <circle r="28" fill="{MUTED}"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><circle cx="430" cy="280" r="86"/></g>
<path d="M120 360h380" class="a"/>
""", ground=True)

add('specialist', '一つの分野の道具だけを扱う、専門家のイラスト。', f"""
{person(170,346,1.15,1,'teal','teal','point','cap','neutral')}
<g transform="translate(420 260)">
  <path d="M-120-60h240v120h-240z" class="bluep o"/>
  <path d="M-120-60h240" class="a"/>
  <g fill="none" stroke="{INK}" stroke-width="3">
    <path d="M-90-20h60l20 8-20 8h-60z"/><path d="M0-20h60l20 8-20 8H0z"/><path d="M-90 20h150"/>
  </g>
</g>
<g transform="translate(170 190)"><path d="M0-26l9 18 20 4-15 14 4 20-18-10-18 10 4-20-15-14 20-4z" class="gold o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('species', '形の違う三種類の動物を並べたイラスト。', f"""
<g transform="translate(150 300)">
  <ellipse cy="-20" rx="60" ry="34" class="goldp o"/>
  <path d="M-40 10v22M0 12v20M36 8v24" fill="none" stroke="{TONES['gold'][2]}" stroke-width="11" stroke-linecap="round"/>
  <circle cx="58" cy="-44" r="22" class="goldp o"/>
</g>
<g transform="translate(320 280)">
  <path d="M-46 0c26-40 90-40 116 0-26 40-90 40-116 0z" class="teal o"/>
  <path d="M-46 0l-36-26v52z" class="teal o"/>
</g>
<g transform="translate(480 270)">
  <ellipse rx="46" ry="26" class="violet o"/>
  <path d="M-46 0l-30 12 22 12z" class="violet o"/>
  <ellipse cx="36" cy="-14" rx="20" ry="17" class="violet o"/>
  <path d="M-14-10q-6-34 28-32 26 2 22 22z" class="violetp o"/>
</g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('spokesman', '団体を代表して、報道の場で話している人のイラスト。', f"""
{person(220,346,1.2,1,'blue','violet','point','short','neutral')}
<g transform="translate(280 250)">
  <path d="M-16-14h32v28h-32z" class="ink"/>
  <path d="M16-4l50-24v48z" class="ink" opacity=".8"/>
</g>
<g opacity=".55">{person(450,346,0.8,1,'teal','gold','stand','bob','neutral')}{person(520,346,0.8,1,'violet','teal','stand','cap','neutral')}</g>
<g transform="translate(390 170)">
  <path d="M-60-30h120q12 0 12 12v28q0 12-12 12h-80l-18 16 4-16q-12 0-12-12v-28q0-12 12-12z" class="paper"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('spokesperson', '団体の代弁として、公の場で発言している人のイラスト。', f"""
{person(220,346,1.2,1,'blue','violet','point','bun','neutral')}
<g transform="translate(280 250)">
  <path d="M-16-14h32v28h-32z" class="ink"/>
  <path d="M16-4l50-24v48z" class="ink" opacity=".8"/>
</g>
<g class="corals" opacity=".85" style="stroke-width:4"><path d="M370 220q26 26 26 40M400 200q34 34 34 56"/></g>
<g opacity=".55">{person(500,346,0.8,-1,'teal','gold','stand','short','neutral')}</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('stall', '通りに出された屋台で、品物を売っているイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-180-20h360v20h-360z" class="goldp o"/>
  <path d="M-160 0v70M160 0v70" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-200-70h400l-30-40h-340z" class="coral o"/>
  <g class="green o"><circle cx="-110" cy="-42" r="18"/><circle cx="-70" cy="-42" r="18"/></g>
  <g class="goldp o"><rect x="20" y="-60" width="40" height="40"/><rect x="70" y="-60" width="40" height="40"/></g>
</g>
{person(140,346,0.9,1,'teal','blue','give','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('steal', '人目を避けて、他人の物をこっそり持ち去るイラスト。', f"""
{person(200,346,1.1,1,'violet','blue','carry','cap','neutral')}
{box(200,266,80,60,0,'gold')}
<g transform="translate(430 300)">
  <path d="M-100-20h200v20h-200z" class="goldp o"/>
  <path d="M-40-20h80v-40h-80z" class="muted"/>
</g>
<path d="M340 250h-60" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:7"><path d="M140 200l30 30M170 200l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('steam', 'やかんの口から、白い蒸気が噴き出しているイラスト。', f"""
<g transform="translate(260 280)">
  <path d="M-90-40h180l-14 100h-152z" fill="#dfe6ea" class="o"/>
  <path d="M-90-40h180" class="a"/>
  <path d="M90-30h50l30-20-84-6z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-90-30q-46 0-46 30t46 30" fill="none" stroke="{INK}" stroke-width="9"/>
</g>
<g fill="#e7eef4" stroke="{MUTED}" stroke-width="2.5">
  <circle cx="400" cy="180" r="24"/><circle cx="436" cy="132" r="18"/><circle cx="466" cy="96" r="14"/>
</g>
{flame(260,352,0.8)}
""", ground=True)

add('stick', '棒の先に付いた粘着テープで、紙をくっつけているイラスト。', f"""
<g transform="translate(320 250) rotate(-8)">
  <path d="M-100-90h200v180h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-50h140M-70-20h140"/></g>
</g>
<g transform="translate(320 130)">
  <path d="M-50-14h100v28h-100z" class="goldp o" opacity=".85"/>
</g>
{hand(180,150,1)}
<path d="M320 170v30" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('strain', 'ロープが強く引かれて、張りつめているイラスト。', f"""
<path d="M80 250h440" fill="none" stroke="{TONES['gold'][0]}" stroke-width="18" stroke-linecap="round"/>
<g class="a" marker-end="url(#ar)"><path d="M200 180h-120"/><path d="M400 180h120"/></g>
<g class="corals" style="stroke-width:5"><path d="M290 220v-24M310 220v-24M300 290v24"/></g>
<path d="M80 360h440" class="muted"/>
""", ground=False, arrow=True)

add('stupid', '簡単な計算を大きく間違えているイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-150-110h300v220h-300z" class="paper"/>
  <g fill="{INK}"><rect x="-90" y="-40" width="40" height="8"/><rect x="-30" y="-44" width="8" height="16"/><rect x="-34" y="-40" width="16" height="8"/><rect x="10" y="-40" width="40" height="8"/></g>
  <g fill="{INK}"><rect x="70" y="-40" width="46" height="8"/></g>
  <g class="corals" style="stroke-width:8"><path d="M60 20l60 60M120 20l-60 60"/></g>
</g>
""", ground=True)

add('submission', '書類を窓口の箱に提出しているイラスト。', f"""
{person(180,346,1.1,1,'teal','blue','give','short','neutral')}
<g transform="translate(300 240) rotate(-6)">
  <path d="M-60-70h120v140h-120z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-36-40h72M-36-16h72"/></g>
</g>
<g transform="translate(450 300)">
  <path d="M-80-50h160v100h-160z" class="tealp o"/>
  <path d="M-40-50h80v-12h-80z" class="ink"/>
</g>
<path d="M370 200h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('substance', 'びんの中に入った物質そのものを示したイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-80-100h160l-12 200h-136z" fill="#f4fbff" class="o"/>
  <path d="M-40-120h80v20h-80z" class="ink"/>
  <path d="M-70-10h140l-8 110h-124z" class="violetp o"/>
  <path d="M-70-10h140" class="a"/>
</g>
<g fill="{TONES['violet'][0]}"><circle cx="420" cy="200" r="12"/><circle cx="456" cy="230" r="9"/><circle cx="404" cy="248" r="7"/></g>
<path d="M370 220h30" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('succeed', '高い所に登りきって、旗を立てるイラスト。', f"""
<g class="tealp o">
  <rect x="100" y="300" width="80" height="60"/><rect x="200" y="250" width="80" height="110"/>
  <rect x="300" y="200" width="80" height="160"/><rect x="400" y="140" width="80" height="220"/>
</g>
{person(440,140,0.55,1,'coral','blue','up','short','smile')}
<path d="M520 130V80" class="a"/>
<path d="M520 80l50 14-50 14z" class="coral o"/>
<path d="M130 260q120-70 260-100" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('suffer', 'けがの痛みに耐えて、うつむいている人のイラスト。', f"""
{person(280,346,1.25,1,'violet','blue','hold','short','sad')}
<g class="corals" opacity=".95" style="stroke-width:5">
  <path d="M240 200q-26-10-30-34M320 200q26-10 30-34"/>
</g>
<g transform="translate(266 306)">
  <path d="M-22-14h44v28h-44z" fill="#fffdf6" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-22-4h44M-22 6h44" fill="none" stroke="{MUTED}" stroke-width="2.5"/>
</g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('suggest', '案を書いた紙を示して、提案しているイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','give','short','smile')}
{person(450,346,1.1,-1,'coral','gold','think','bob','neutral')}
<g transform="translate(300 240)">
  <path d="M-60-60h120v120h-120z" class="paper"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><path d="M-36-30h72M-36-6h60"/></g>
  <circle cx="30" cy="34" r="12" class="goldp o"/>
</g>
<path d="M250 180h100" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('suite', '続き間になった二つの部屋を、上から見たイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-200-120h400v240h-400z" fill="#fffdf6" class="o"/>
  <path d="M0-120v90M0 30v90" class="a"/>
  <g class="tealp o"><rect x="-160" y="-80" width="120" height="60"/></g>
  <g class="goldp o"><rect x="40" y="20" width="120" height="70"/></g>
  <path d="M-200 20h60" fill="none" stroke="#fffdf6" stroke-width="8"/>
</g>
<path d="M300 130v-40" class="a" marker-end="url(#ar)" transform="rotate(180 300 110)"/>
""", ground=True, arrow=True)

add('surgery', '手術室で、器具を使って処置を行っているイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-200-30h400v26h-400z" fill="#dfe6ea" class="o"/>
  <path d="M-130-56h260v26h-260z" class="bluep o"/>
  <path d="M-160-4v70M160-4v70" fill="none" stroke="{MUTED}" stroke-width="10"/>
</g>
{person(210,240,0.85,1,'teal','teal','point','cap','neutral')}
{person(390,240,0.85,-1,'teal','teal','point','cap','neutral')}
<g transform="translate(300 120)">
  <circle r="40" class="goldp o"/>
  <path d="M0 40v20" fill="none" stroke="{INK}" stroke-width="8"/>
</g>
""", ground=True)

add('surprised', '目を大きく開けて、驚いた表情の顔のイラスト。', f"""
<g transform="translate(280 200)">
  <circle r="130" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="-48" cy="-24" r="26" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <circle cx="48" cy="-24" r="26" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <circle cx="-48" cy="-24" r="11" class="ink"/><circle cx="48" cy="-24" r="11" class="ink"/>
  <circle cy="54" r="24" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M-62-64q22-16 40-6M62-64q-22-16-40-6" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g class="golds" style="stroke-width:5"><path d="M450 130l24-24M470 210h30M450 290l24 24"/></g>
""", ground=False)

add('surprising', '思いがけない結果が出て、驚きを呼ぶイラスト。', f"""
<g transform="translate(400 220)">
  <path d="M-140 0l60-30-30-56 70 24 24-70 30 68 62-30-20 60 74 12-60 40 44 46-70-6-10 62-44-52-52 42 10-62z" class="goldp o"/>
  <path d="M-8-40h16v50h-16zM-8 22h16v16h-16z" class="coral o"/>
</g>
{person(150,346,1.1,1,'teal','blue','up','short','surprised')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('switch', 'スイッチを切り替えて、明かりを点けるイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-60-90h120v180h-120z" fill="#fffdf6" class="o"/>
  <path d="M-30-60h60v50h-60z" class="muted"/>
  <path d="M-30 10h60v50h-60z" class="coral o"/>
</g>
<g transform="translate(430 230)">
  <circle r="46" class="goldp o"/>
  <path d="M-18 46h36v16h-36z" class="ink"/>
  <g class="golds" style="stroke-width:4"><path d="M0-62v-16M-48-32l-16-10M48-32l16-10"/></g>
</g>
<path d="M280 250h80" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('tactic', '盤上の駒の動かし方を、矢印で示した戦術のイラスト。', f"""
<g transform="translate(300 240)">
  <g>{''.join(f'<rect x="{-160 + (i%8)*40}" y="{-160 + (i//8)*40}" width="40" height="40" fill="{"#fffdf6" if (i + i//8)%2 else "#dfe6ea"}"/>' for i in range(64))}</g>
  <circle cx="-100" cy="60" r="16" class="teal o"/>
  <circle cx="60" cy="-60" r="16" class="coral o"/>
  <path d="M-100 60L40-40" fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="10 8" marker-end="url(#ar)"/>
</g>
""", ground=True, arrow=True)

add('tank', 'キャタピラのついた戦車のイラスト。', f"""
<g transform="translate(300 270)">
  <path d="M-160 20h320v40h-320z" fill="#5d6b78" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{INK}" stroke-width="3">{''.join(f'<circle cx="{-130+i*52}" cy="40" r="16"/>' for i in range(6))}</g>
  <path d="M-110-20h220v40h-220z" fill="#7a8794" stroke="{INK}" stroke-width="3"/>
  <path d="M-50-60h100v40h-100z" fill="#7a8794" stroke="{INK}" stroke-width="3"/>
  <path d="M40-46h150v14H40z" fill="#7a8794" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('teenage', '10代の少年と少女が並んでいるイラスト。', f"""
{person(220,346,1.05,1,'coral','blue','stand','short','smile')}
{person(390,346,1.05,1,'violet','gold','stand','bob','smile')}
<g transform="translate(300 150)">
  <path d="M-60-30h120v60h-120z" class="paper"/>
  <g fill="{INK}"><rect x="-40" y="-14" width="8" height="28"/><path d="M-16-14h30v10h-20v6h20v12h-30z"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('tenant', '家主から鍵を受け取って、部屋を借りる人のイラスト。', f"""
{building(160,300,0.85,'teal')}
{person(430,346,1.15,-1,'coral','blue','hold','bob','smile')}
<g transform="translate(320 250)">
  <circle cx="-30" r="16" fill="none" stroke="{TONES['gold'][0]}" stroke-width="7"/>
  <path d="M-14 0h60v10h-14v10h-10v-10h-36z" class="goldd o"/>
</g>
<path d="M370 200h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('terminal', 'バスや飛行機の発着場に、乗り物が並ぶイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-220-80h440v120h-440z" fill="#dfe6ea" class="o"/>
  <path d="M-190-50h380v70h-380z" class="bluep o"/>
</g>
<g transform="translate(180 320) scale(0.4)">
  <path d="M-200-60h400v100h-400z" class="goldp o"/>
  <g class="bluep o"><rect x="-170" y="-40" width="60" height="40"/><rect x="-90" y="-40" width="60" height="40"/><rect x="-10" y="-40" width="60" height="40"/></g>
  <circle cx="-120" cy="46" r="26" class="ink"/><circle cx="120" cy="46" r="26" class="ink"/>
</g>
<g transform="translate(430 330) scale(0.35)">{plane(0,0,1.0,0,'teal')}</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('terror', '大きな影に追われて、逃げ出す恐怖のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#2b3a4a"/>
{person(180,350,1.15,1,'coral','blue','walk','short','sad')}
<g fill="#1e2a36" stroke="#4a5c6e" stroke-width="3"><path d="M360 350q-40-120 50-160 70-30 120 30 44 60-30 130z"/></g>
<g fill="#f7e6a8"><circle cx="430" cy="220" r="10"/><circle cx="490" cy="220" r="10"/></g>
<g class="muted"><path d="M120 260h-40M130 300h-50"/></g>
""", ground=False)

add('texture', '布の表面の細かい織り目を、拡大して示したイラスト。', f"""
<g transform="translate(220 240)">
  <path d="M-120-100h240v200h-240z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3">
    {''.join(f'<path d="M-120 {-80+i*24}h240"/>' for i in range(8))}
    {''.join(f'<path d="M{-100+i*24} -100v200"/>' for i in range(9))}
  </g>
</g>
<g transform="translate(430 230)">
  <circle r="76" fill="#fffdf6" stroke="{INK}" stroke-width="7"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6">
    <path d="M-60-30h120M-60 0h120M-60 30h120M-30-60v120M0-60v120M30-60v120"/>
  </g>
  <path d="M54 54l50 50" fill="none" stroke="{INK}" stroke-width="13" stroke-linecap="round"/>
</g>
""", ground=True)

add('therapist', '患者の体をほぐして、治療している人のイラスト。', f"""
<g transform="translate(330 300)">
  <path d="M-160-20h320v30h-320z" class="tealp o"/>
  <path d="M-140 10v50M140 10v50" fill="none" stroke="{MUTED}" stroke-width="10"/>
  <ellipse cx="20" cy="-46" rx="110" ry="26" class="coral o"/>
  <circle cx="-110" cy="-56" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
{person(150,346,1.05,1,'teal','teal','point','short','neutral')}
<path d="M220 250h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('thread', '針に通した一本の細い糸のイラスト。', f"""
<g transform="translate(300 200) rotate(-12)">
  <path d="M-160 0h300" fill="none" stroke="#dfe6ea" stroke-width="10"/>
  <path d="M110-5l50 5-50 5z" fill="#cfd8de" stroke="{INK}" stroke-width="2"/>
  <ellipse cx="-140" cy="0" rx="14" ry="7" fill="#fffaf1" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M120 240q80 60 180 0t180 40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<path d="M140 210q30 20 20 40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
""", ground=True)

add('threshold', '部屋の入口の境目にある敷居を示したイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-200-140h130v280h-130zM70-140h130v280H70z" fill="#e0d6c2" stroke="{INK}" stroke-width="3"/>
  <path d="M-70-140h140v280h-140z" fill="#fffaf1"/>
  <path d="M-70 120h140v20h-140z" class="goldd o"/>
</g>
<path d="M300 380v-20" class="a" marker-end="url(#ar)" transform="rotate(180 300 370)"/>
""", ground=True, arrow=True)

add('tide', '潮が引いて、岸の水位が下がっているイラスト。', f"""
<path d="M0 250h600v150H0z" class="bluep"/>
<path d="M0 300q120 20 240-10t360 10v100H0z" fill="#efdcb8" stroke="{INK}" stroke-width="3"/>
<path d="M0 220h600" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-dasharray="14 10"/>
<path d="M480 230v50" class="blues" marker-end="url(#ar)" style="stroke-width:6"/>
<g class="blues" opacity=".7"><path d="M40 250q50-14 100 0t100 0"/></g>
""", ground=False, arrow=True)

add('tidy', '散らかった机を片づけて、きちんと整えたイラスト。', f"""
<g transform="translate(160 250)">
  <path d="M-110-20h220v20h-220z" class="goldp o"/>
  <g class="tealp o" transform="rotate(-14 -60 -40)"><rect x="-80" y="-60" width="50" height="40"/></g>
  <g class="coralp o" transform="rotate(20 20 -40)"><rect x="0" y="-56" width="46" height="36"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-110-20h220v20h-220z" class="goldp o"/>
  <g class="tealp o"><rect x="-80" y="-60" width="50" height="40"/><rect x="-20" y="-60" width="50" height="40"/><rect x="40" y="-60" width="50" height="40"/></g>
</g>
<path d="M280 250h60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 150l18 18 30-36"/></g>
""", ground=True, arrow=True)
print(' '.join(W)); print(sheet(W))
