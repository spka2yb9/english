"""第9回: 身の回りのもの・動作の30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('silver', '銀色に光るスプーンとフォークが並んでいるイラスト。', f"""
<circle cx="470" cy="100" r="56" class="bluep"/>
<g transform="translate(230 240) rotate(-8)">
  <ellipse cy="-90" rx="30" ry="42" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <ellipse cy="-96" rx="18" ry="26" fill="#f7fbfe"/>
  <path d="M-9-50h18v170h-18z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(360 240) rotate(8)">
  <path d="M-26-130v56q0 20 12 24v170h28V-50q12-4 12-24v-56h-10v50h-8v-50h-8v50h-8v-50h-8v50h-10z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
</g>
<g class="golds" style="stroke-width:4" opacity=".8"><path d="M180 130l-24-20M420 140l24-20"/></g>
""", ground=True)

add('size', '大・中・小の三つの丸を並べて、大きさの違いを示したイラスト。', f"""
<circle cx="150" cy="220" r="100" class="tealp o"/>
<circle cx="340" cy="250" r="66" class="teal o"/>
<circle cx="470" cy="276" r="38" class="teald o"/>
<path d="M50 350h200" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
<path d="M274 350h132" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
<path d="M432 350h76" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('sky', '雲がうかぶ広い青空を描いたイラスト。地平線の下に地面が見える。', f"""
<rect width="600" height="400" rx="20" fill="#dbeaf8"/>
{sun(480,90,48)}
{cloud(160,140,1.6)}
{cloud(390,210,1.1)}
<path d="M0 330h600v70H0z" class="ground"/>
<path d="M0 330h600" class="a"/>
{tree(90,330,0.7)}
""", ground=False)

add('slap', '開いた手のひらで、ぴしゃりと平たく打つイラスト。', f"""
<circle cx="120" cy="100" r="56" class="coralp"/>
{hand(240,210,1)}
<path d="M330 210h80" class="a" marker-end="url(#ar)"/>
<path d="M450 120v180" fill="none" stroke="{TONES['gold'][2]}" stroke-width="26" stroke-linecap="round"/>
<g class="corals" style="stroke-width:5"><path d="M400 140l-26-20M420 280l-30 22M470 130v-26"/></g>
""", ground=True, arrow=True)

add('soap', '泡立った石けんで手を洗っているイラスト。', f"""
<circle cx="470" cy="100" r="56" class="tealp"/>
{hand(230,240,1)}
<g transform="translate(330 250) rotate(-10)">
  <path d="M-60-30h120q14 0 14 14v32q0 14-14 14h-120q-14 0-14-14v-32q0-14 14-14z" class="tealp o"/>
  <path d="M-30-14q30-10 60 0" fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"/>
</g>
<g class="o" fill="#ffffff"><circle cx="380" cy="180" r="20"/><circle cx="420" cy="150" r="14"/><circle cx="350" cy="140" r="11"/><circle cx="290" cy="170" r="15"/><circle cx="440" cy="200" r="10"/></g>
""", ground=True)

add('soar', '鳥が上昇気流に乗って、高く舞い上がっていくイラスト。', f"""
{cloud(140,300,1.2)}{cloud(430,330,1.0)}
<g transform="translate(320 150) scale(1.2) rotate(-24)">
  <ellipse rx="56" ry="26" class="teal o"/>
  <path d="M-56 0l-42 12 10-26z" class="teal o"/>
  <ellipse cx="42" cy="-16" rx="24" ry="20" class="teal o"/>
  <path d="M60-20l26-8-16 20z" class="gold o"/>
  <circle cx="48" cy="-22" r="3.4" class="ink"/>
  <path d="M-16-12q-6-42 34-40 32 2 28 28-4 22-62 12z" class="tealp o"/>
</g>
<path d="M180 380q60-120 160-190" class="muted" marker-end="url(#ar)"/>
<path d="M120 340v-40M480 300v-40" class="teals" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('sock', '足にはく短い靴下を、二枚並べたイラスト。', f"""
<circle cx="470" cy="100" r="56" class="violetp"/>
<g transform="translate(220 230) rotate(-8)">
  <path d="M-40-90h80v110q0 30 30 40l30 10v40h-70q-70 0-70-60z" class="violetp o"/>
  <path d="M-40-60h80" fill="none" stroke="{TONES['violet'][0]}" stroke-width="6"/>
</g>
<g transform="translate(370 250) rotate(10)">
  <path d="M-40-90h80v110q0 30 30 40l30 10v40h-70q-70 0-70-60z" class="coralp o"/>
  <path d="M-40-60h80" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
""", ground=True)

add('spark', '金属を打ち合わせて、小さな火花が飛び散っているイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-160 40h120l30-30" fill="none" stroke="#cfd8de" stroke-width="18" stroke-linecap="round"/>
  <path d="M160 40H40L10 10" fill="none" stroke="#cfd8de" stroke-width="18" stroke-linecap="round"/>
  <g class="golds" style="stroke-width:5">
    <path d="M0-10v-50M-30 0l-40-30M30 0l40-30M-20-30l-24-40M20-30l24-40M0-20l0 0"/>
  </g>
  <g class="gold o"><circle cx="-70" cy="-70" r="7"/><circle cx="70" cy="-64" r="6"/><circle cx="0" cy="-96" r="8"/><circle cx="-30" cy="-104" r="5"/><circle cx="34" cy="-110" r="5"/></g>
</g>
""", ground=True)

add('split', '一本のまるたにくさびを打ち込んで、二つに割っているイラスト。', f"""
<circle cx="470" cy="100" r="56" class="goldp"/>
<g transform="translate(280 280)">
  <path d="M-140-60h120l-14 60-16 60h-90z" class="goldp o"/>
  <path d="M140-60H20l14 60 16 60h90z" class="goldp o"/>
  <path d="M-140-60h120M140-60H20" class="a"/>
</g>
<g transform="translate(280 190)">
  <path d="M-20-90h40v90l-20 30-20-30z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M160 250h-60"/><path d="M400 250h60"/></g>
""", ground=True, arrow=True)

add('spread', 'パンにバターを塗り広げているイラスト。', f"""
<circle cx="470" cy="100" r="56" class="goldp"/>
<g transform="translate(280 290)">
  <path d="M-150-60h300v20l-16 80h-268l-16-80z" class="goldp o"/>
  <path d="M-150-60h300" class="a"/>
  <path d="M-120-40h240l-10 60h-220z" fill="#fff0c5" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-110-30h150l-6 40h-140z" class="gold o" opacity=".65"/>
</g>
<g transform="translate(340 200) rotate(24)">
  <path d="M-90-10h120l30 10-30 10H-90z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <path d="M-150-12h60v24h-60z" class="goldd o"/>
</g>
<path d="M200 210h140" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('spy', '物陰から双眼鏡でこっそり様子をうかがっている人のイラスト。', f"""
<path d="M380 60h220v300H380z" fill="#e0d6c2" stroke="{INK}" stroke-width="3"/>
{person(300,346,1.1,1,'violet','blue','hold','cap','neutral')}
<g transform="translate(300 236)">
  <rect x="-46" y="-18" width="40" height="40" rx="10" class="violetd o"/>
  <rect x="6" y="-18" width="40" height="40" rx="10" class="violetd o"/>
  <path d="M-6 2h12" class="a"/>
</g>
<path d="M350 220h70" class="muted" marker-end="url(#ar)"/>
<path d="M60 366h300" class="a"/>
""", ground=True, arrow=True)

add('stamp', '封筒のすみに切手をはっているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="coralp"/>
<g transform="translate(300 270)">
  <path d="M-170-90h340v180h-340z" class="paper"/>
  <path d="M-170-90L0 30l170-120" fill="none" class="a"/>
  <g transform="translate(108 -50)">
    <path d="M-46-30h92v60h-92z" fill="#fffdf6" stroke="{INK}" stroke-width="2.5" stroke-dasharray="6 4"/>
    <circle r="16" class="coral o"/>
  </g>
</g>
<path d="M470 130q-30 40-40 60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('stare', '目を大きく開いて、まっすぐじっと見つめている顔のイラスト。', f"""
<g transform="translate(280 200)">
  <circle r="140" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="-52" cy="-24" r="30" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <circle cx="52" cy="-24" r="30" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <circle cx="-52" cy="-24" r="13" class="ink"/><circle cx="52" cy="-24" r="13" class="ink"/>
  <path d="M-20 60h40" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4">
  <path d="M420 176h130" marker-end="url(#ar)"/><path d="M420 190h130" marker-end="url(#ar)"/>
</g>
""", ground=False, arrow=True)

add('stir', 'カップの中の液体をスプーンでかき回しているイラスト。うずが立っている。', f"""
<circle cx="470" cy="100" r="56" class="goldp"/>
<g transform="translate(280 270)">
  <path d="M-100-70h200l-20 140h-160z" fill="#fffdf6" class="o"/>
  <path d="M-100-70h200" class="a"/>
  <path d="M-92-30h184l-16 100h-152z" class="goldp o"/>
  <path d="M-70-20q46 26 90 0t76 6" fill="none" stroke="{TONES['gold'][2]}" stroke-width="5"/>
  <path d="M100-50q42 0 42 28t-42 28" fill="none" stroke="{INK}" stroke-width="9"/>
</g>
<path d="M300 240L390 110" fill="none" stroke="{TONES['gold'][2]}" stroke-width="11" stroke-linecap="round"/>
<ellipse cx="300" cy="244" rx="26" ry="9" fill="#f0dfc2" stroke="{INK}" stroke-width="2.5" transform="rotate(-38 300 244)"/>
<path d="M170 200a120 50 0 0 0 224 0" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('stone', '地面に転がった大小の石を描いたイラスト。', f"""
<circle cx="470" cy="100" r="56" class="tealp"/>
<g transform="translate(260 280)">
  <path d="M-90 50q-30-70 10-100 44-32 96-14 48 20 42 74-2 30-22 40z" fill="#b9b1a3" class="o"/>
  <path d="M-50-30q40-20 80 6" fill="none" stroke="#9a9284" stroke-width="3"/>
</g>
<g transform="translate(420 320)">
  <path d="M-46 20q-14-34 6-46 22-14 46-4 22 10 18 34-2 12-10 16z" fill="#c9c1b3" class="o"/>
</g>
<g transform="translate(120 330)">
  <path d="M-30 12q-10-22 4-30 14-8 30-2 14 6 12 22-2 8-6 10z" fill="#c9c1b3" class="o"/>
</g>
""", ground=True)

add('strip', '巻いた紙から細長い一片を切り取り、はぎ取っているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="bluep"/>
<g transform="translate(300 260)">
  <path d="M-180-90h360v180h-360z" class="paper"/>
  <path d="M-180-30h360M-180 20h360" fill="none" stroke="{MUTED}" stroke-width="2.5" stroke-dasharray="8 8"/>
</g>
<g transform="translate(300 130) rotate(-8)">
  <path d="M-180-24h360v48h-360z" class="bluep o"/>
</g>
<path d="M300 190v-24" class="a" marker-end="url(#ar)"/>
{hand(496,130,-1)}
""", ground=True, arrow=True)

add('stumble', '石につまずいて、前へよろけている人のイラスト。', f"""
<path d="M40 340h520" fill="none" stroke="#e6dcc9" stroke-width="46" stroke-linecap="round"/>
<g transform="translate(250 330)">
  <path d="M-40 12q-14-34 6-46 22-14 46-4 22 10 18 34-2 12-10 16z" fill="#b9b1a3" class="o"/>
</g>
<g transform="translate(340 316) rotate(24)">{person(0,0,1.05,1,'coral','blue','up','short','surprised')}</g>
<path d="M180 220q60-30 100 0" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('tap', '蛇口をひねって、水を出しているイラスト。', f"""
<g transform="translate(300 190)">
  <path d="M-10 0v-90h120" fill="none" stroke="#cfd8de" stroke-width="24" stroke-linecap="round"/>
  <path d="M-10 0v20" fill="none" stroke="#cfd8de" stroke-width="30"/>
  <path d="M96-90v-30" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
  <path d="M70-124h52v14H70z" class="coral o"/>
</g>
<path d="M290 230v110" fill="none" stroke="{TONES['blue'][0]}" stroke-width="14" stroke-linecap="round"/>
<path d="M290 230v110" fill="none" stroke="#9dc6ea" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="290" cy="350" rx="80" ry="16" class="bluep o"/>
""", ground=True)

add('tear', '一枚の紙を両手で引っぱって、二つに裂いているイラスト。', f"""
<circle cx="470" cy="100" r="56" class="coralp"/>
<g transform="translate(280 230)">
  <path d="M-160-100h150l-20 40 20 40-20 40 20 60h-150z" class="paper"/>
  <path d="M160-100H10l20 40-20 40 20 40-20 60h150z" class="paper"/>
</g>
{hand(90,230,1)}
{hand(470,230,-1)}
<g class="a" marker-end="url(#ar)"><path d="M170 340h-70"/><path d="M390 340h70"/></g>
""", ground=True, arrow=True)

add('tool', 'ハンマー・ドライバー・レンチなど、道具が並んだイラスト。', f"""
<g transform="translate(160 240) rotate(-12)">
  <path d="M-44-30h88v34h-88z" class="goldd o"/>
  <path d="M0 4v120" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"/>
</g>
<g transform="translate(300 250)">
  <path d="M-14-100h28v70h-28z" class="coral o"/>
  <path d="M-6-30h12v120h-12z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(440 250) rotate(14)">
  <path d="M-30-100q30-24 60 0-16 16-30 10-14 6-30-10z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-10-84h20v170h-20z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('toss', 'コインを指で軽く上へ放り上げているイラスト。', f"""
<circle cx="470" cy="100" r="56" class="goldp"/>
{hand(240,300,1)}
<path d="M280 260q40-120 120-160" class="muted" marker-end="url(#ar)"/>
<circle cx="300" cy="220" r="16" class="goldp o" opacity=".5"/>
<circle cx="340" cy="170" r="16" class="goldp o" opacity=".75"/>
<circle cx="390" cy="120" r="20" class="gold o"/>
""", ground=True, arrow=True)

add('tower', '細長く高くそびえる塔のイラスト。', f"""
<g transform="translate(300 0)">
  <path d="M-70 360V120h140v240z" class="tealp o"/>
  <path d="M-90 120L0 40l90 80z" class="teal o"/>
  <path d="M0 40V6" class="a"/>
  <g class="bluep o"><rect x="-30" y="160" width="60" height="50"/><rect x="-30" y="240" width="60" height="50"/></g>
  <path d="M-70 320h140" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"/>
</g>
<path d="M120 360h360" class="a"/>
{tree(120,360,0.55)}
""", ground=True)

add('trail', '森の中に細く続く小道と、地面に残った足跡のイラスト。', f"""
<path d="M0 220h600v180H0z" fill="#e4efe2"/>
<path d="M0 220h600" class="a" opacity=".4"/>
{tree(90,250,0.8)}{tree(520,240,0.7)}
<path d="M300 400q-40-110 20-160t-10-40" fill="none" stroke="#e6dcc9" stroke-width="40" stroke-linecap="round"/>
<g fill="#c9bda6">
  <ellipse cx="286" cy="360" rx="10" ry="16"/><ellipse cx="314" cy="330" rx="10" ry="16"/>
  <ellipse cx="292" cy="300" rx="9" ry="14"/><ellipse cx="316" cy="272" rx="8" ry="13"/>
  <ellipse cx="300" cy="248" rx="7" ry="11"/>
</g>
""", ground=False)

add('truck', '荷台に荷物を積んだトラックが走っているイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-200 40h130v-120h-130z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <path d="M-70 40h270v-90H-70z" class="coral o"/>
  <path d="M-190-60h100v40h-100z" class="bluep o"/>
  <circle cx="-150" cy="52" r="30" class="ink"/><circle cx="70" cy="52" r="30" class="ink"/><circle cx="150" cy="52" r="30" class="ink"/>
  <g class="goldp o"><rect x="-40" y="-90" width="70" height="40"/><rect x="40" y="-90" width="70" height="40"/></g>
</g>
<path d="M60 330h480" class="a"/>
<path d="M540 220h40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('uniform', '同じ制服を着た三人が並んでいるイラスト。', f"""
{person(160,346,1.1,1,'blue','violet','stand','short','smile')}
{person(300,346,1.1,1,'blue','violet','stand','bob','smile')}
{person(440,346,1.1,1,'blue','violet','stand','cap','smile')}
<g fill="none" stroke="{TONES['blue'][2]}" stroke-width="4"><path d="M140 250h40M280 250h40M420 250h40"/></g>
<path d="M100 200h400" class="muted"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('van', '小型の配送車が荷物を積んで走っているイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-180 40h360v-80q0-40-40-40h-260l-60 60z" class="tealp o"/>
  <path d="M-176-20h80v-46h-34z" class="bluep o"/>
  <path d="M-80-66h60v46h-60z" class="bluep o"/>
  <circle cx="-120" cy="52" r="30" class="ink"/><circle cx="110" cy="52" r="30" class="ink"/>
  <path d="M40-50h120v50H40z" fill="#fffdf6" stroke="{INK}" stroke-width="2.5"/>
  <path d="M60-30h80M60-14h60" fill="none" stroke="{MUTED}" stroke-width="3"/>
</g>
<path d="M60 330h480" class="a"/>
<path d="M540 220h40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('wash', '泡の立った水で、皿を洗っているイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-160-40h320l-24 110h-272z" fill="#eef4f8" class="o"/>
  <path d="M-160-40h320" class="a"/>
  <path d="M-140 0h280l-16 70h-248z" class="bluep o"/>
</g>
<g fill="#ffffff" class="o"><circle cx="200" cy="200" r="20"/><circle cx="250" cy="176" r="14"/><circle cx="350" cy="186" r="17"/><circle cx="400" cy="212" r="12"/></g>
<g transform="translate(300 210) rotate(-16)">
  <ellipse rx="60" ry="22" fill="#fffdf6" class="o"/>
  <ellipse rx="36" ry="12" class="bluep o"/>
</g>
{hand(180,250,1)}
""", ground=True)

add('weight', 'はかりの上に人が立ち、体重の目盛りが表示されているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="tealp"/>
{person(300,300,1.05,1,'teal','blue','stand','short','neutral')}
<g transform="translate(300 330)">
  <path d="M-110-30h220v40h-220z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <circle cx="0" cy="-8" r="0" />
  <path d="M-110 10h220v20h-220z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(450 250)">
  <circle r="46" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0l26-24" class="a"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5"><path d="M-32-32l-8-8M32-32l8-8M0-44v-10"/></g>
</g>
<path d="M400 290q-40 20-60 30" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('wood', '切り口の年輪が見える木材のイラスト。', f"""
<circle cx="120" cy="100" r="56" class="goldp"/>
<g transform="translate(320 250)">
  <path d="M-160-60h240l60 30v60l-60 30h-240z" class="goldp o"/>
  <path d="M-160-60l60-30h240l-60 30z" class="gold o"/>
  <ellipse cx="140" cy="0" rx="24" ry="60" fill="#f0d6a6" stroke="{INK}" stroke-width="2.5"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="2.5">
    <ellipse cx="140" cy="0" rx="15" ry="40"/><ellipse cx="140" cy="0" rx="7" ry="20"/>
    <path d="M-150-40h230M-150-14h220M-150 12h220M-150 38h230"/>
  </g>
</g>
""", ground=True)

add('bride', '白いドレスとブーケを持った花嫁のイラスト。', f"""
<circle cx="470" cy="100" r="56" class="coralp"/>
{person(280,346,1.25,1,'violet','violet','hold','bob','smile')}
<g transform="translate(280 300)">
  <path d="M-40-70q40-14 80 0l40 100h-160z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M-30-40q30 12 60 0" fill="none" stroke="{MUTED}" stroke-width="3"/>
</g>
<g transform="translate(280 208)">
  <path d="M-34-40q34-20 68 0l6 60q-40 24-80 0z" fill="#fffdf6" opacity=".6" stroke="{MUTED}" stroke-width="2"/>
</g>
<g transform="translate(360 300)">
  <g class="coral o"><circle cx="-14" cy="-10" r="14"/><circle cx="14" cy="-14" r="14"/><circle cx="0" cy="10" r="14"/></g>
  <path d="M0 20v30" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
</g>
<path d="M80 366h420" class="a"/>
""", ground=True)
print(' '.join(W)); print(sheet(W))
