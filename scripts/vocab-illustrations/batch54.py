"""第54回: 承認・態度・観客・境界など40語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('accountable', '自分の仕事について、数字で説明する責任を負うイラスト。', f"""
{person(160,346,1.2,1,'blue','blue','point','short','neutral')}
<g transform="translate(420 220)">
  <path d="M-120-110h240v220h-240z" fill="#f7fbfe" class="o"/>
  <g fill="{TONES['teal'][0]}"><rect x="-90" y="20" width="40" height="70"/><rect x="-30" y="-20" width="40" height="110"/><rect x="30" y="-60" width="40" height="150"/></g>
  <g fill="{INK}"><rect x="-90" y="-90" width="100" height="14"/></g>
</g>
<path d="M240 200h40" class="a" marker-end="url(#ar)"/>
<g transform="translate(160 240)"><path d="M-40-30h80v10h-80z" class="paper"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('administrative', '書類と印で事務を回すイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-220-30h440v40h-440z" class="goldd o"/>
</g>
<g transform="translate(180 220)">
  <path d="M-80-60h160v90h-160z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-50-30h100M-50-10h100M-50 10h70"/></g>
</g>
<g transform="translate(330 230)" opacity=".9">
  <path d="M-80-50h160v80h-160z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-50-20h100M-50 0h80"/></g>
</g>
<g transform="translate(470 200)"><path d="M-40-30h80v40h-80z" class="ink"/><path d="M-16-80h32v50h-32z" class="ink"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><circle cx="470" cy="250" r="26"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('applicable', 'その決まりが当てはまる場合と、当てはまらない場合のイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-90-70h180v140h-180z" class="tealp o"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M-30 0l20 20 40-46"/></g>
</g>
<g transform="translate(430 240)">
  <circle r="80" class="mutedfill" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M-30-30l60 60M30-30l-60 60"/></g>
</g>
<g transform="translate(300 110)"><path d="M-60-40h120v70h-120z" class="paper"/><g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-36-16h72M-36 4h50"/></g></g>
<path d="M270 160L200 190M330 160l70 30" class="a" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('appropriate', '場にふさわしい服装を選ぶイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-70-90h140v60h-140z" class="bluep o"/>
  <path d="M-70-30h60l10 130h-60zM10-30h60l-10 130h-60z" class="blue o"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M60-110l20 20 34-40"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-70-70h140v90h-140z" class="coralp o"/>
  <path d="M-40 20h80v70h-80z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M60-110l30 30M90-110l-30 30"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('approve', '計画書に承認の印を出して、よしと認めるイラスト。', f"""
{person(150,346,1.15,1,'blue','blue','give','short','smile')}
<g transform="translate(360 230)">
  <path d="M-110-110h220v220h-220z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-80-60h160M-80-20h160M-80 20h120"/></g>
  <g transform="translate(50 60) rotate(-12)">
    <circle r="46" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
    <path d="M-22 0l16 18 30-36" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"/>
  </g>
</g>
<path d="M230 200h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('arbitrary', 'さいころ任せで、気ままに決めるイラスト。', f"""
{person(160,346,1.15,1,'violet','blue','reach','short','flat')}
<g transform="translate(320 200) rotate(-12)">
  <path d="M-50-50h100v100h-100z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><circle cx="-22" cy="-22" r="8"/><circle cx="22" cy="22" r="8"/><circle cx="0" cy="0" r="8"/></g>
</g>
<g class="tealp o"><rect x="420" y="240" width="60" height="90"/><rect x="500" y="240" width="60" height="90"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M370 250h70"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('architectural', '建物の設計図と定規のイラスト。', f"""
<g transform="translate(280 220)">
  <path d="M-180-140h360v280h-360z" fill="#e8f2fb" class="o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4">
    <path d="M-120 110h240v-160h-240z"/><path d="M-140-50l140-90 140 90"/><path d="M-40 110V30h80v80z"/><path d="M-100-20h60v50h-60zM40-20h60v50H40z"/>
  </g>
</g>
<g transform="translate(480 330) rotate(-20)"><path d="M-90-16h180v32h-180z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('argue', '意見をぶつけ合って議論するイラスト。', f"""
{person(150,346,1.15,1,'teal','blue','point','short','flat')}
{person(450,346,1.15,-1,'coral','gold','point','bob','flat')}
<g fill="#fffdf6" stroke="{INK}" stroke-width="3">
  <path d="M210 120h130v60H210z"/><path d="M255 180l-14 26 34-26z"/>
  <path d="M260 210h130v60H260z"/><path d="M330 270l14 26-34-26z"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M355 150h40M245 240h-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('argument', '主張を書き並べて、根拠を示すイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <g fill="{INK}"><rect x="-140" y="-110" width="160" height="18"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-100-50h240M-100 0h240M-100 50h200"/></g>
  <g class="teal o"><circle cx="-130" cy="-44" r="10"/><circle cx="-130" cy="6" r="10"/><circle cx="-130" cy="56" r="10"/></g>
</g>
""", ground=True)

add('armed', '盾を構えて、身がまえているイラスト。', f"""
{person(280,346,1.3,1,'green','green','carry','cap','neutral')}
<g transform="translate(360 250)">
  <path d="M0-70q50 20 50 60 0 50-50 70-50-20-50-70 0-40 50-60z" fill="#8b98a6" stroke="{INK}" stroke-width="3"/>
  <path d="M0-40v90" fill="none" stroke="#c9d3dc" stroke-width="6"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('arrival', '駅に着いて、到着を告げるイラスト。', f"""
<g transform="translate(360 250)">
  <path d="M-40 60h280v-140H-40z" class="bluep o"/>
  <g fill="#e8f4fb" stroke="{INK}" stroke-width="3"><rect x="0" y="-60" width="70" height="50"/><rect x="100" y="-60" width="70" height="50"/></g>
</g>
<g transform="translate(180 280)"><path d="M-120 30h240v-20h-240z" fill="#dfe6ea" class="o"/></g>
{person(150,280,0.85,1,'teal','gold','stand','bob','smile')}
<path d="M300 160h-100" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M110 190l18 18 30-36"/></g>
<path d="M60 320h480" class="a"/>
""", ground=True, arrow=True)

add('ashamed', '顔を伏せて、恥ずかしがっているイラスト。', f"""
<g transform="translate(280 346) rotate(10)">{person(0,0,1.35,1,'coral','blue','stand','short','sad')}</g>
{hand(220,210,1)}
<g class="coralp"><circle cx="330" cy="215" r="22"/></g>
{drop(360,240,0.7)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('assignment', '出された課題の用紙のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <g fill="{INK}"><rect x="-130" y="-110" width="140" height="16"/></g>
  <g fill="none" stroke="{INK}" stroke-width="3"><rect x="-130" y="-60" width="30" height="30"/><rect x="-130" y="-10" width="30" height="30"/><rect x="-130" y="40" width="30" height="30"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-80-46h200M-80 4h200M-80 54h160"/></g>
</g>
<g transform="translate(500 330) rotate(24)"><path d="M-10-80h20v110h-20z" class="coral o"/><path d="M-10 30h20l-10 24z" class="ink"/></g>
""", ground=True)

add('associate', '一方を見て、もう一方を思い浮かべるイラスト。', f"""
<g transform="translate(160 230)">
  <circle r="70" class="coral o"/>
</g>
<g transform="translate(440 230)">
  <path d="M-70-60h140v120h-140z" fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="11 9"/>
  <g class="tealp o"><circle r="40"/></g>
</g>
<path d="M250 230h100" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('associated', '二つの輪が線でつながって、関わりがあるイラスト。', f"""
<g transform="translate(180 230)"><circle r="70" class="tealp o"/></g>
<g transform="translate(420 230)"><circle r="70" class="coralp o"/></g>
<path d="M250 230h100" fill="none" stroke="{INK}" stroke-width="10"/>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('assume', '確かめないまま、そうだと決めてかかるイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','think','short','neutral')}
<g transform="translate(430 190)">
  <path d="M-130-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-166q-38-4-26-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g opacity=".8"><path d="M-40-30h80v60h-80z" class="coralp o"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"><path d="M60 0l14 14 24-30"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M300 300h120"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M340 330l30 30M370 330l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('assure', '大丈夫だと請け合って、安心させるイラスト。', f"""
{person(200,346,1.2,1,'blue','blue','give','short','smile')}
{person(400,346,1.2,-1,'coral','gold','stand','bob','neutral')}
<path d="M270 250h30" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<g transform="translate(320 150)">
  <path d="M-70-50h140v70h-140z" fill="#fffdf6" class="o"/>
  <path d="M-40 20l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M-24-16l16 18 32-38"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('astonishing', '思わず目をみはる、驚くべきものを見るイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','up','short','surprised')}
<g transform="translate(430 220)">
  <path d="M0-140l34 80 84-20-56 68 56 68-84-20-34 80-34-80-84 20 56-68-56-68 84 20z" class="gold o"/>
  <circle r="34" fill="#fffdf6"/>
</g>
<g class="golds" style="stroke-width:6"><path d="M280 140l-26-20M290 190h-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('atmosphere', '灯りのやわらかい、その場の雰囲気のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#3c3b52"/>
<g fill="#f7e6bd" opacity=".18"><circle cx="180" cy="150" r="120"/><circle cx="430" cy="200" r="110"/></g>
<g transform="translate(180 130)"><path d="M-30-40h60l20 50h-100z" fill="#f3e3ae" stroke="#d9c286" stroke-width="2"/><path d="M-4-70h8v30h-8z" fill="#d9c286"/></g>
<g transform="translate(430 180)"><circle r="24" fill="#f3e3ae"/></g>
<g transform="translate(300 320)"><path d="M-160-16h320v24h-320z" fill="#5a5470"/></g>
<g transform="translate(230 300) scale(0.8)">{person(0,0,1.0,1,'teal','blue','stand','bob','smile')}</g>
""", ground=False)

add('attitude', '同じ場面に、前向きな構えと投げやりな構えを並べたイラスト。', f"""
{person(170,346,1.2,1,'teal','blue','up','short','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M100 170l20 20 34-40"/></g>
<g transform="translate(430 346) rotate(-10)">{person(0,0,1.2,1,'coral','gold','stand','bob','sad')}</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M510 170l30 30M540 170l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('audience', '舞台を見つめる観客席のイラスト。', f"""
<g transform="translate(300 140)">
  <path d="M-180-60h360v120h-360z" fill="#41506a"/>
  <g transform="translate(0 40) scale(0.5)">{person(0,20,1.0,1,'coral','gold','up','bob','smile')}</g>
</g>
{person(120,340,0.8,1,'teal','blue','stand','short','smile')}
{person(230,340,0.8,1,'gold','blue','stand','bob','smile')}
{person(340,340,0.8,1,'violet','gold','stand','cap','smile')}
{person(450,340,0.8,1,'coral','blue','stand','short','smile')}
<path d="M60 360h480" class="a"/>
""", ground=True)

add('audio', '音声の波形とヘッドホンのイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-90 40q0-110 90-110t90 110" fill="none" stroke="{INK}" stroke-width="14"/>
  <path d="M-110 40h40v70h-40zM70 40h40v70H70z" fill="#41506a" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(430 230)">
  <g fill="{TONES['teal'][0]}">{''.join(f'<rect x="{-90+i*22}" y="{-int(60*[0.3,0.8,1,0.5,0.9,0.4,0.7,0.6][i])}" width="12" height="{int(120*[0.3,0.8,1,0.5,0.9,0.4,0.7,0.6][i])}"/>' for i in range(8))}</g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('authentic', '本物と偽物を見分けるイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-70-70h140v140h-140z" class="gold o"/>
  <g transform="translate(0 0)"><path d="M0-30l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" fill="#fffdf6"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M40-110l20 20 34-40"/></g>
</g>
<g transform="translate(430 240)">
  <path d="M-70-70h140v140h-140z" fill="#d5cfa8" class="o"/>
  <path d="M0-30l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" fill="#eee9d0"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M40-110l30 30M70-110l-30 30"/></g>
</g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('automatic', '人が触らなくても、機械がひとりで動くイラスト。', f"""
<g transform="translate(360 240)">
  <path d="M-140-120h280v240h-280z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="12"><circle cx="-50" cy="-30" r="44"/><circle cx="50" cy="40" r="34"/></g>
  <g class="green o"><circle cx="90" cy="-80" r="14"/></g>
</g>
<g transform="translate(150 250)">
  {hand(150,250,1)}
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M110 90l40 40M150 90l-40 40"/></g>
</g>
<g class="corals" style="stroke-width:4"><path d="M280 130q26-14 50 4"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('award', '賞状を授けられるイラスト。', f"""
{person(160,346,1.1,1,'blue','blue','give','short','smile')}
<g transform="translate(320 230) rotate(-6)">
  <path d="M-100-70h200v140h-200z" class="paper"/>
  <g fill="{INK}"><rect x="-60" y="-40" width="120" height="14"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-10h120M-60 10h90"/></g>
  <g transform="translate(60 40)"><circle r="20" class="gold o"/><path d="M-10 20h20v20h-20z" class="coral o"/></g>
</g>
{person(490,346,1.1,-1,'coral','gold','reach','bob','smile')}
<path d="M400 300h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('aware', '背後の変化にちゃんと気づいているイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','think','short','neutral')}
<g transform="translate(450 220)">
  <path d="M-70-70h140v140h-140z" class="coralp o"/>
  <g class="corals" style="stroke-width:5"><path d="M0-100v-24M-80-70l-24-16M80-70l24-16"/></g>
</g>
<path d="M280 250h90" fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="12 9" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M120 180l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('badly', 'ひどく壊れて、状態が悪いイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-80-70h160v140h-160z" class="tealp o"/>
</g>
<g transform="translate(430 250)">
  <g fill="#b6bfc9" stroke="{INK}" stroke-width="3">
    <path d="M-80-70h70l-10 60-60-20z"/><path d="M0-70h80v50l-70 10z"/><path d="M-80 20l70-10 10 60h-80z"/><path d="M20 20l60-10v60H10z"/>
  </g>
</g>
<path d="M280 250h50" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:5"><path d="M430 130v-26M350 150l-20-20M510 150l20-20"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('balanced', '左右の重さがつり合っているイラスト。', f"""
<g transform="translate(300 180)">
  <path d="M-6-40h12v70h-12z" class="ink"/>
  <path d="M-160 30h320" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-160 30v50M160 30v50" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(140 270)"><g class="teal o"><circle r="30"/><circle cx="40" r="30"/></g></g>
<g transform="translate(440 270)"><g class="coral o"><circle r="30"/><circle cx="-40" r="30"/></g></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M290 350l20 20 34-40"/></g>
""", ground=False)

add('bare', '何も置かれていない、むき出しの台のイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-90-20h180v30h-180z" class="goldd o"/>
  <path d="M-70 10h14v70h-14zM56 10h14v70H56z" class="goldd o"/>
  <g class="tealp o"><rect x="-60" y="-70" width="50" height="50"/></g>
  <g class="coralp o"><circle cx="40" cy="-46" r="24"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-90-20h180v30h-180z" class="goldd o"/>
  <path d="M-70 10h14v70h-14zM56 10h14v70H56z" class="goldd o"/>
</g>
<path d="M290 240h50" class="a" marker-end="url(#ar)"/>
<path d="M60 336h480" class="a"/>
""", ground=True, arrow=True)

add('battery', '＋と−の端子がついた電池のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-90-120h180v240h-180z" class="teal o"/>
  <path d="M-40-140h80v20h-80z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <g fill="#fffdf6"><rect x="-60" y="-60" width="120" height="24"/><rect x="-60" y="0" width="120" height="24"/><rect x="-60" y="60" width="80" height="24"/></g>
</g>
<g fill="{INK}" transform="translate(300 90)"><rect x="-30" y="-6" width="60" height="12"/><rect x="-6" y="-30" width="12" height="60"/></g>
<g fill="{INK}" transform="translate(300 390)"><rect x="-30" y="-6" width="60" height="12"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('battle', '盾と旗を構えて、ぶつかり合う戦いのイラスト。', f"""
{person(180,346,1.15,1,'green','green','carry','cap','flat')}
{person(430,346,1.15,-1,'violet','violet','carry','cap','flat')}
<g transform="translate(250 250)">
  <path d="M0-60q40 16 40 50 0 44-40 60-40-16-40-60 0-34 40-50z" fill="#8b98a6" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(360 250)">
  <path d="M0-60q40 16 40 50 0 44-40 60-40-16-40-60 0-34 40-50z" fill="#8b98a6" stroke="{INK}" stroke-width="3"/>
</g>
<g class="corals" style="stroke-width:6"><path d="M300 170v-30M270 190l-24-20M330 190l24-20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('beauty', '花の美しさに見入るイラスト。', f"""
<g transform="translate(400 260)">
  <path d="M0 90V0" fill="none" stroke="{TONES['green'][2]}" stroke-width="7"/>
  <g class="coral o"><circle cx="-40" cy="-30" r="30"/><circle cx="40" cy="-30" r="30"/><circle cx="0" cy="-70" r="30"/><circle cx="-24" cy="10" r="30"/><circle cx="24" cy="10" r="30"/></g>
  <g class="gold o"><circle cy="-24" r="22"/></g>
</g>
{person(150,346,1.05,1,'violet','blue','think','bob','smile')}
<g class="golds" style="stroke-width:5"><path d="M250 160l26-20M260 200h30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('bee', '花のまわりを飛ぶミツバチのイラスト。', f"""
<g transform="translate(300 200)">
  <ellipse rx="70" ry="50" fill="#f3c94f" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><path d="M-20-46h20v92h-20zM20-46h20v92h-20z"/></g>
  <circle cx="-76" cy="-14" r="30" class="ink"/>
  <g fill="none" stroke="{INK}" stroke-width="4"><path d="M-90-40l-16-30M-70-44l-4-34"/></g>
  <g fill="#e8f4fb" opacity=".85" stroke="{INK}" stroke-width="2"><ellipse cx="-10" cy="-70" rx="44" ry="26" transform="rotate(-20 -10 -70)"/><ellipse cx="40" cy="-64" rx="36" ry="22" transform="rotate(20 40 -64)"/></g>
</g>
<g transform="translate(470 330)">
  <path d="M0 40V-10" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
  <g class="coralp o"><circle cx="-24" cy="-30" r="20"/><circle cx="24" cy="-30" r="20"/><circle cy="-56" r="20"/></g>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('behavior', '人の目の前でのふるまいを示したイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','give','short','smile')}
{person(400,346,1.1,-1,'coral','gold','stand','bob','smile')}
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="10 8"><path d="M200 170q100-40 200 0"/></g>
<g transform="translate(300 250)"><path d="M-20 0h40" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M480 200l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('belief', '胸の中に、固く信じるものを抱くイラスト。', f"""
{person(280,346,1.35,1,'violet','blue','carry','short','neutral')}
<g transform="translate(280 250)">
  <circle r="46" class="goldp o"/>
  <g class="golds" style="stroke-width:4"><path d="M0-64v-16M-46-46l-14-10M46-46l14-10"/></g>
</g>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="11 9"><circle cx="280" cy="250" r="76"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('bell', 'つり下がって鳴る鐘のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-6-140h12v40h-12z" class="ink"/>
  <path d="M-100 80q0-160 100-160t100 160z" class="gold o"/>
  <path d="M-110 80h220v26h-220z" class="goldd o"/>
  <circle cy="120" r="20" class="goldd o"/>
</g>
<g class="corals" opacity=".9" style="stroke-width:5"><path d="M450 200q26 26 26 50M490 170q40 40 40 80M150 200q-26 26-26 50M110 170q-40 40-40 80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('beloved', 'たいせつに思う相手を、そっと抱きしめるイラスト。', f"""
{person(250,346,1.2,1,'coral','gold','give','bob','smile')}
{person(360,346,1.2,-1,'teal','blue','give','short','smile')}
<path d="M290 250h30" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<g transform="translate(305 160)">
  <path d="M0 44c-44-32-60-48-60-72a32 32 0 0 1 60-16 32 32 0 0 1 60 16c0 24-16 40-60 72z" class="coral o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('bent', 'まっすぐな棒と、折れ曲がった棒を比べたイラスト。', f"""
<path d="M100 180h400" fill="none" stroke="{TONES['teal'][0]}" stroke-width="20" stroke-linecap="round"/>
<path d="M100 300h180l100 60h120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M300 380v-30" class="a" marker-end="url(#ar)" transform="rotate(180 300 365)"/>
""", ground=False, arrow=True)

add('between', '二つのものの間にあることを示したイラスト。', f"""
<g class="tealp o"><rect x="90" y="200" width="110" height="120"/><rect x="400" y="200" width="110" height="120"/></g>
<g transform="translate(300 260)"><circle r="40" class="coral o"/></g>
<g class="a" marker-end="url(#ar)"><path d="M210 260h40M390 260h-40"/></g>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('billion', '同じ束が膨大に積み上がるイラスト。', f"""
<g class="teal o">
  {''.join(f'<rect x="{100+c*40}" y="{300-r*40}" width="34" height="34"/>' for r in range(5) for c in range(10))}
</g>
<g class="tealp o">{''.join(f'<rect x="{100+c*40}" y="{100}" width="34" height="34"/>' for c in range(10))}</g>
<g class="muted"><path d="M300 90V60"/></g>
<path d="M60 350h480" class="a"/>
""", ground=True)
print(len(W), ' '.join(W)); print(sheet(W))
