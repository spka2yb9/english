"""第34回: 相談・契約・協力・減少など45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('consult', '専門家に向かい合って、相談しているイラスト。', f"""
{person(170,346,1.1,1,'coral','blue','point','bob','neutral')}
{person(440,346,1.15,-1,'blue','violet','point','short','neutral')}
<g transform="translate(300 300)">
  <path d="M-100-20h200v20h-200z" class="goldp o"/>
  <path d="M-40-46h80v26h-80z" class="paper"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="4"><path d="M240 190h120" marker-end="url(#ar)"/><path d="M360 230H240" marker-end="url(#ar)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('contemplate', '一点を見つめて、じっくり考え込んでいるイラスト。', f"""
{person(200,346,1.2,1,'violet','blue','think','short','neutral')}
<g transform="translate(430 210)">
  <circle r="90" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4"><circle r="60"/><circle r="30"/></g>
  <circle r="10" class="violet o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M280 220h60" marker-end="url(#ar)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('contend', '互いに主張をぶつけ合って、争っているイラスト。', f"""
{person(180,346,1.15,1,'coral','blue','point','short','neutral')}
{person(430,346,1.15,-1,'teal','gold','point','bob','neutral')}
<g transform="translate(250 190)"><path d="M-46-26h92q12 0 12 12v26q0 12-12 12h-60l-16 14 4-14q-12 0-12-12v-26q0-12 12-12z" class="paper"/><path d="M-6-12h12v20h-6z" class="coral"/></g>
<g transform="translate(370 240)"><path d="M46-26H-46q-12 0-12 12v26q0 12 12 12h60l16 14-4-14q12 0 12-12v-26q0-12-12-12z" class="paper"/><path d="M-6-12h12v20h-6z" class="teal"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('continent', '海に囲まれた大きな陸地を、上から見たイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#dbeaf8"/>
<path d="M120 90q160-40 260 20t80 140-140 110-220-40-40-150 60-80z" fill="#e4efe2" stroke="{INK}" stroke-width="3"/>
{building(240,220,0.4,'teal')}{tree(340,250,0.5)}{tree(180,280,0.45)}
<g class="blues" opacity=".6"><path d="M40 60q40-12 80 0M480 320q40-12 80 0"/></g>
""", ground=False)

add('continuous', 'とぎれずにつながった一本の線と、切れた線を比べたイラスト。', f"""
<path d="M60 170h480" fill="none" stroke="{TONES['teal'][0]}" stroke-width="14" stroke-linecap="round"/>
<path d="M60 300h480" fill="none" stroke="{MUTED}" stroke-width="14" stroke-linecap="round" stroke-dasharray="40 30"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M520 100l18 18 30-36"/></g>
""", ground=False)

add('contract', '二人が署名した契約書に、印が入るイラスト。', f"""
{person(150,346,1.05,1,'blue','violet','give','short','neutral')}
{person(450,346,1.05,-1,'coral','gold','give','bob','neutral')}
<g transform="translate(300 240)">
  <path d="M-90-100h180v200h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-60h120M-60-30h120M-60 0h90"/></g>
  <path d="M-60 50q30-16 50 0t50-8" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
  <circle cx="50" cy="70" r="14" class="coral o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('convenient', 'すぐ手の届く場所に道具があって、使いやすいイラスト。', f"""
{hand(180,240,1)}
<g transform="translate(340 250)">
  <path d="M-90-60h180v120h-180z" class="goldp o"/>
  <g class="tealp o"><rect x="-70" y="-40" width="40" height="80"/><rect x="-20" y="-40" width="40" height="80"/><rect x="30" y="-40" width="40" height="80"/></g>
</g>
<path d="M240 240h20" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 150l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('convert', '四角い形が、丸い形に変換されるイラスト。', f"""
<g transform="translate(170 230)"><path d="M-70-70h140v140h-140z" class="teal o"/></g>
<g transform="translate(430 230)"><circle r="70" class="coral o"/></g>
<path d="M270 230h60" class="a" marker-end="url(#ar)" style="stroke-width:7"/>
<path d="M120 350h360" class="a"/>
""", ground=True, arrow=True)

add('convict', '法廷で有罪が告げられ、罪が確定するイラスト。', f"""
{person(200,346,1.1,1,'coral','blue','hold','short','sad')}
{person(430,346,1.1,-1,'blue','violet','point','cap','neutral')}
<g transform="translate(430 230)"><path d="M-40-10h60v20h-60z" class="goldd o"/></g>
<g transform="translate(310 200)">
  <path d="M-46-26h92v52h-92z" class="paper"/>
  <g class="corals" style="stroke-width:6"><path d="M-16-10l32 22M16-10l-32 22"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('cook', 'なべの前で、料理を作っている人のイラスト。', f"""
{person(200,346,1.2,1,'coral','blue','point','bob','smile')}
<g transform="translate(380 280)">
  <path d="M-90-30h180l-14 60h-152z" fill="#dfe6ea" class="o"/>
  <path d="M-104-30h208" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
</g>
{flame(380,340,0.7)}
<g class="muted" opacity=".8"><path d="M350 200q-14-30 4-52M400 196q-14-34 6-56"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('cooperate', '二人が同じ荷物を両側から持って運ぶイラスト。', f"""
{person(170,346,1.1,1,'teal','blue','give','short','smile')}
{person(430,346,1.1,-1,'coral','gold','give','bob','smile')}
{box(300,250,130,80,0,'gold')}
<path d="M240 250h30M330 250h30" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<path d="M300 160h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('coordinate', 'ばらばらの動きを、中央でそろえてまとめるイラスト。', f"""
<g class="tealp o"><circle cx="120" cy="150" r="30"/><circle cx="120" cy="300" r="30"/><circle cx="480" cy="150" r="30"/><circle cx="480" cy="300" r="30"/></g>
<circle cx="300" cy="225" r="46" class="coral o"/>
<g class="a" marker-end="url(#ar)">
  <path d="M160 165l90 40"/><path d="M160 285l90-40"/><path d="M440 165l-90 40"/><path d="M440 285l-90-40"/>
</g>
""", ground=False, arrow=True)

add('corner', '部屋の二つの壁が出会う角を示したイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-200-140h400v280h-400z" fill="#fffdf6" class="o"/>
  <path d="M-200 60h400" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M-60-140v200" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M-60 60h-140v80h140z" fill="#f0ece3"/>
</g>
<circle cx="240" cy="300" r="46" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
""", ground=True)

add('correlate', '二つの折れ線が、同じ向きに動いているイラスト。', f"""
<path d="M60 340h480M100 340V100" fill="none" stroke="{INK}" stroke-width="4"/>
<path d="M110 300l80-40 90-60 100-40 110-30" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"/>
<path d="M110 330l80-36 90-56 100-38 110-28" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="12 8"/>
<path d="M420 200h60" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('correspond', '二つの表の項目が、一つずつ対応しているイラスト。', f"""
<g transform="translate(160 230)">
  <path d="M-80-110h160v220h-160z" class="paper"/>
  <g fill="{INK}">{''.join(f'<rect x="-50" y="{-80+i*50}" width="60" height="10"/>' for i in range(4))}</g>
</g>
<g transform="translate(440 230)">
  <path d="M-80-110h160v220h-160z" class="paper"/>
  <g fill="{INK}">{''.join(f'<rect x="-10" y="{-80+i*50}" width="60" height="10"/>' for i in range(4))}</g>
</g>
<g class="a" marker-end="url(#ar)">{''.join(f'<path d="M250 {155+i*50}h100"/>' for i in range(4))}</g>
""", ground=True, arrow=True)

add('count', '並んだ品を一つずつ数えているイラスト。', f"""
<g class="tealp o">
  {''.join(f'<circle cx="{130+i*70}" cy="250" r="26"/>' for i in range(6))}
</g>
<g fill="{INK}">{''.join(f'<rect x="{126+i*70}" y="310" width="{6+i}" height="20"/>' for i in range(6))}</g>
{hand(130,170,1)}
<path d="M180 190h40" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('couple', '二人が並んで、一組になっているイラスト。', f"""
<circle cx="300" cy="150" r="76" class="coralp"/>
<g transform="translate(300 186)"><path d="M0 24l-28-34 14-16 14 14 14-14 14 16z" class="coral o"/></g>
{person(240,346,1.15,1,'violet','blue','give','bob','smile')}
{person(360,346,1.15,-1,'teal','gold','give','short','smile')}
<circle cx="300" cy="258" r="14" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('crack', '皿の表面に細いひびが走っているイラスト。', f"""
<g transform="translate(300 250)">
  <ellipse rx="150" ry="50" fill="#fffdf6" class="o"/>
  <path d="M-90-20l30 24-24 20 36 22" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"/>
  <path d="M20-24l26 26-20 22" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"/>
</g>
<circle cx="230" cy="250" r="66" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M120 340h360" class="a"/>
""", ground=True)

add('crash', '車が壁にぶつかって、衝突しているイラスト。', f"""
<g transform="translate(200 290) scale(0.55)">
  <path d="M-150 40h300l-16-56h-50l-34-56h-120l-34 56h-62z" class="coral o"/>
  <circle cx="-84" cy="48" r="30" class="ink"/><circle cx="84" cy="48" r="30" class="ink"/>
</g>
<path d="M410 130h60v240h-60z" class="goldp o"/>
<g transform="translate(370 260)">
  <path d="M-60 0l30-16-16-28 36 12 12-36 16 36 30-16-10 30 38 6-30 20 22 24-36-4-6 34-22-28-26 22 4-32z" class="goldp o"/>
</g>
<path d="M60 350h480" class="a"/>
""", ground=True)

add('cream', 'びんに入った乳白色のクリームのイラスト。', f"""
<g transform="translate(280 260)">
  <path d="M-70-90h140l-10 160h-120z" fill="#f4fbff" class="o"/>
  <path d="M-62-20h124l-8 90h-108z" fill="#fff8e6" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-34-110h68v20h-68z" class="ink"/>
</g>
<g transform="translate(440 290)">
  <path d="M0 0q-30-30 0-60 30 30 0 60z" fill="#fff8e6" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-30 0h60v10h-60z" fill="#fff8e6" stroke="{INK}" stroke-width="2.5"/>
</g>
<path d="M120 350h380" class="a"/>
""", ground=True)

add('creative', '同じ材料から、思いがけない形を作り出すイラスト。', f"""
<g transform="translate(140 250)">
  <g class="tealp o"><rect x="-40" y="-40" width="36" height="36"/><rect x="4" y="-40" width="36" height="36"/><rect x="-40" y="4" width="36" height="36"/></g>
</g>
<g transform="translate(410 240)">
  <path d="M0-90l70 50v100l-70 40-70-40V-40z" class="coral o"/>
  <path d="M0-90v230M-70-40l140 100M70-40L-70 60" fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"/>
</g>
<path d="M230 250h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(290 140)">
  <circle r="26" class="goldp o"/>
  <path d="M-10 26h20v12h-20z" class="ink"/>
  <g class="golds" style="stroke-width:4"><path d="M0-38v-14M-30-20l-12-8M30-20l12-8"/></g>
</g>
""", ground=True, arrow=True)

add('creep', '身を低くして、そっと忍び寄っているイラスト。', f"""
<g transform="translate(300 300)">
  <ellipse cx="0" cy="-30" rx="86" ry="40" class="violet o"/>
  <path d="M-56 6v20M-16 10v16M28 10v16M60 4v22" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
  <circle cx="-104" cy="-52" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-134-56q4-30 30-30 26 0 30 28-16-10-30-4-12-8-30 6z" fill="{HAIR}"/>
  <circle cx="-114" cy="-48" r="3" class="ink"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M140 220h100" marker-end="url(#ar)"/></g>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('criticize', '相手の作品を指して、欠点を述べているイラスト。', f"""
{person(160,346,1.15,1,'coral','blue','point','short','neutral')}
<g transform="translate(430 240)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <path d="M-60 50l50-80 40 46 40-56 26 90z" class="tealp o"/>
  <g class="corals" style="stroke-width:6"><path d="M-40-70l40 40M0-70l-40 40"/></g>
</g>
<g transform="translate(280 190)">
  <path d="M-40-26h80q12 0 12 12v26q0 12-12 12h-56l-16 14 4-14q-12 0-12-12v-26q0-12 12-12z" class="paper"/>
  <path d="M-6-12h12v20h-6z" class="coral"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('crowd', '広場に大勢の人が集まっているイラスト。', f"""
<g class="tealp o">
  {''.join(f'<g transform="translate({70+ (i%8)*68} {200 + (i//8)*72})"><circle cy="-24" r="17"/><path d="M-21 32q0-32 21-32t21 32z"/></g>' for i in range(24))}
</g>
<path d="M60 380h480" class="a"/>
""", ground=False)

add('cruel', '弱い立場の相手に、冷たく当たっているイラスト。', f"""
{person(180,346,1.15,1,'coral','blue','point','cap','neutral')}
<g transform="translate(420 320)">
  <ellipse cx="0" cy="-20" rx="60" ry="34" class="goldp o"/>
  <path d="M-40 12v20M-10 14v18M20 14v18M44 8v24" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10" stroke-linecap="round"/>
  <g transform="translate(64 -42)">
    <ellipse rx="26" ry="22" class="goldp o"/>
    <path d="M-14-18q-12-26 6-26 14 0 14 20z" class="goldd o"/>
    <circle cx="6" cy="-2" r="3" class="ink"/>
    <path d="M0 12q10 6 18-2" fill="none" stroke="{INK}" stroke-width="2"/>
  </g>
</g>
<g class="corals" style="stroke-width:7"><path d="M290 200l40 40M330 200l-40 40"/></g>
<path d="M250 280h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('cruise', '客船が海の上を、ゆったり進んでいくイラスト。', f"""
<path d="M0 270h600v130H0z" class="bluep"/>
<path d="M0 270q60-14 120 0t120 0 120 0 120 0 120 0" class="a"/>
<g transform="translate(300 250)">
  <path d="M-180 0h360l-30 40h-300z" fill="#fffdf6" class="o"/>
  <path d="M-140 0v-40h280v40z" fill="#fffdf6" class="o"/>
  <path d="M-100-40v-36h200v36z" fill="#fffdf6" class="o"/>
  <g class="bluep o">{''.join(f'<rect x="{-120+i*46}" y="-32" width="30" height="24"/>' for i in range(6))}</g>
  <path d="M40-76v-30h30v30z" class="coral o"/>
</g>
{sun(500,90,40)}
<path d="M120 160h140" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('crush', '上から強い力を受けて、缶が押しつぶされるイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-60-40h120l-10 40-20 20 30 20h-120l30-20-20-20z" fill="#dfe6ea" class="o"/>
  <path d="M-60-40h120" class="a"/>
</g>
<g transform="translate(300 170)">
  <path d="M-110-30h220v50h-220z" fill="#8f9aa5" stroke="{INK}" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 120v50"/><path d="M420 120v50"/></g>
<path d="M120 340h360" class="a"/>
""", ground=True, arrow=True)

add('cultivate', '畑を耕して、作物を育てているイラスト。', f"""
<path d="M0 250h600v150H0z" fill="#e7d9c4"/>
<path d="M0 250h600" class="a"/>
<g fill="none" stroke="#c9a97c" stroke-width="4"><path d="M0 300q120-20 240 0t360-10M0 350q120-20 240 0t360-10"/></g>
{''.join(f'<g transform="translate({140+i*90} 260)"><path d="M0 0v-40" fill="none" stroke="{TONES["green"][2]}" stroke-width="6"/><path d="M0-24c-24-6-32-22-32-22 22-6 32 22 32 22z" class="green o"/><path d="M0-40c24-6 32-22 32-22-22-6-32 22-32 22z" class="green o"/></g>' for i in range(4))}
{person(120,250,0.8,1,'gold','blue','point','cap','neutral')}
""", ground=False)

add('cupboard', '扉のついた戸棚に、食器が入っているイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-140-140h280v280h-280z" class="goldp o"/>
  <path d="M0-140v280" class="a"/>
  <path d="M-120-110h100v100h-100z" fill="#fffdf6" stroke="{INK}" stroke-width="2.5"/>
  <g class="bluep o"><ellipse cx="-70" cy="-30" rx="34" ry="12"/><ellipse cx="-70" cy="-50" rx="34" ry="12"/></g>
  <circle cx="-14" cy="0" r="8" class="goldd"/><circle cx="14" cy="0" r="8" class="goldd"/>
</g>
<path d="M120 380h360" class="a"/>
""", ground=True)

add('curious', '箱の中をのぞき込んで、知りたがっているイラスト。', f"""
{box(400,300,140,100,0,'gold')}
<g transform="translate(400 240)"><path d="M-70-14h140v20h-140z" class="gold o" transform="rotate(-16)"/></g>
{person(200,346,1.15,1,'teal','blue','reach','short','surprised')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="9 8"><path d="M270 240h80" marker-end="url(#ar)"/></g>
<g fill="{INK}"><path d="M150 180q0-22 22-22t22 22q0 15-17 20v10h-10v-17q17-2 17-13 0-10-12-10t-12 10z"/><circle cx="172" cy="236" r="6"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('current', '川の流れの向きを、矢印で示したイラスト。', f"""
<path d="M0 200h600v200H0z" class="bluep"/>
<path d="M0 200h600" class="a"/>
<g class="blues" marker-end="url(#ar)" style="stroke-width:6">
  <path d="M80 250q120-30 220 0t200-10"/>
  <path d="M60 310q120-30 220 0t220-10"/>
  <path d="M80 360q120-30 220 0t200-10"/>
</g>
""", ground=False, arrow=True)

add('curve', 'まっすぐな点線に対して、なめらかに曲がった線のイラスト。', f"""
<path d="M70 200h460" class="muted"/>
<path d="M70 280q230-190 460 0" fill="none" stroke="{TONES['violet'][0]}" stroke-width="14" stroke-linecap="round"/>
<circle cx="70" cy="280" r="13" class="violetd"/><circle cx="530" cy="280" r="13" class="violetd"/>
<path d="M300 190v-40" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('danger', '崖のふちに、危険を知らせる標識が立つイラスト。', f"""
<path d="M0 250h300v150H0z" class="ground"/>
<path d="M0 250h300" class="a"/>
<g transform="translate(230 190)">
  <path d="M0-70l70 116h-140z" class="goldp o"/>
  <path d="M-6-26h12v40h-12zM-6 22h12v12h-12z" class="ink"/>
  <path d="M-4 46h8v70h-8z" class="goldd o"/>
</g>
<g class="corals" style="stroke-width:6"><path d="M340 300l40 40M380 300l-40 40"/></g>
""", ground=False)

add('dare', '高い所から、思いきって飛び込もうとするイラスト。', f"""
<path d="M0 300h600v100H0z" class="bluep"/>
<path d="M0 300q60-14 120 0t120 0 120 0 120 0 120 0" class="a"/>
<path d="M60 120h160v16H60z" class="goldp o"/>
<path d="M80 136v60M200 136v60" fill="none" stroke="{TONES['gold'][2]}" stroke-width="9"/>
{person(200,120,0.9,1,'coral','blue','up','short','neutral')}
<path d="M260 160q120 60 160 140" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('date', 'カレンダーの一日に丸をつけて、日付を示すイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <path d="M-180-140h360v50h-360z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5">
    {''.join(f'<rect x="{-160 + (i%7)*46}" y="{-70 + (i//7)*54}" width="42" height="48"/>' for i in range(21))}
  </g>
  <circle cx="26" cy="8" r="24" class="coral o"/>
</g>
""", ground=True)

add('death', 'ろうそくの火が消えて、命が終わったことを示すイラスト。', f"""
<g transform="translate(240 280)">
  <path d="M-24-90h48v90h-48z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0-90v-16" class="a"/>
  <g class="muted"><path d="M0-110q-14-26 4-44"/></g>
</g>
<g transform="translate(430 270)" opacity=".85">
  <path d="M-10-90h20v50h-20zM-30-70h60v20h-60z" fill="#cfc7b8" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-50 40q50-40 100 0z" fill="#cfc7b8" stroke="{INK}" stroke-width="2.5"/>
</g>
<path d="M120 340h380" class="a"/>
""", ground=True)

add('decision', '二つの案のうち一つに印をつけて、決めるイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-80-70h160v140h-160z" class="tealp o"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M-30 0l20 20 34-40"/></g>
</g>
<g transform="translate(430 230)">
  <path d="M-80-70h160v140h-160z" class="muted"/>
  <g class="corals" style="stroke-width:8"><path d="M-30-30l60 60M30-30l-60 60"/></g>
</g>
{hand(170,110,1)}
<path d="M120 350h360" class="a"/>
""", ground=True)

add('decline', '右下がりに落ちていく線と、断る手のイラスト。', f"""
<path d="M60 340h480M100 340V100" fill="none" stroke="{INK}" stroke-width="4"/>
<path d="M110 140l90 50 90 40 100 60 100 40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" marker-end="url(#ar)"/>
{hand(480,170,-1)}
""", ground=False, arrow=True)

add('decrease', '棒の高さが順に低くなっていくイラスト。', f"""
<path d="M60 340h480" class="a"/>
<g class="tealp o">
  <rect x="100" y="140" width="70" height="200"/><rect x="200" y="190" width="70" height="150"/>
  <rect x="300" y="240" width="70" height="100"/><rect x="400" y="280" width="70" height="60"/>
</g>
<path d="M120 110h340" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('deem', '品物を見て、これは合格だと判断しているイラスト。', f"""
{person(160,346,1.15,1,'blue','violet','point','short','neutral')}
<g transform="translate(400 250)">
  <path d="M-90-70h180v140h-180z" class="tealp o"/>
</g>
<g transform="translate(400 130)">
  <path d="M-40-24h80v48h-80z" class="paper"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round"><path d="M-18 0l14 14 24-28"/></g>
</g>
<path d="M250 200h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('defeat', '相手を打ち負かして、勝ち残っているイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','up','short','smile')}
<g transform="translate(430 350)">
  <ellipse cx="0" cy="-16" rx="70" ry="24" class="coralp o"/>
  <circle cx="-60" cy="-40" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-84-44q4-26 26-26 22 0 26 24-14-8-28-2-10-6-24 4z" fill="{HAIR}"/>
  <path d="M-70-36h6M-52-36h6" class="a"/>
</g>
<path d="M280 250h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(200 160)"><path d="M0-30l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" class="gold o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('defend', '盾を構えて、飛んでくるものから身を守るイラスト。', f"""
{person(360,346,1.15,-1,'teal','blue','point','cap','neutral')}
<g transform="translate(270 260)">
  <path d="M-50-70h100v80q0 60-50 90-50-30-50-90z" class="tealp o"/>
  <path d="M0-70v170M-50 0h100" fill="none" stroke="{TONES['teal'][0]}" stroke-width="5"/>
</g>
<g class="corals" marker-end="url(#ar)" style="stroke-width:6">
  <path d="M60 200h120"/><path d="M60 260h120"/><path d="M60 320h120"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('definite', 'あいまいな点線の形が、はっきりした実線になるイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-80-70h160v140h-160z" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
</g>
<g transform="translate(430 230)">
  <path d="M-80-70h160v140h-160z" class="teal o"/>
</g>
<path d="M280 230h60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 130l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('crowded' if False else 'continent2' if False else 'chip2' if False else 'cook2' if False else 'consult2' if False else 'convey2' if False else 'dear', '手紙の書き出しに、あて名を書き入れているイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-150-140h300v280h-300z" class="paper"/>
  <g fill="{INK}"><rect x="-110" y="-100" width="120" height="10"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-110-50h220M-110-20h220M-110 10h180M-110 40h200"/></g>
</g>
<g transform="translate(430 160) rotate(34)">
  <path d="M-10-80h20v110h-20z" class="coral o"/>
  <path d="M-10 30h20l-10 26z" class="ink"/>
</g>
""", ground=True)
print(len(W), ' '.join(W)); print(sheet(W))
