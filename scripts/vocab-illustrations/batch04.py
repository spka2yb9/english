"""第4回: 動作・形状・場所の30語。"""
from lib import *

W = []
def add(word, alt, body, **kw):
    W.append(emit(word, alt, body, **kw))

# --- 動作 --------------------------------------------------------------------
add('climb', 'はしごのような急な岩場を、手足を使って上へ登っていく人のイラスト。', f"""
<circle cx="120" cy="90" r="56" class="goldp"/>
<path d="M300 400V60q0-30 60-30h240v370z" fill="#e7dcc9" stroke="{INK}" stroke-width="3"/>
<path d="M330 120h60M420 190h70M340 250h70M430 320h60" fill="none" stroke="#cbbda3" stroke-width="6" stroke-linecap="round"/>
{person(258,330,1.05,1,'coral','blue','up','cap','neutral')}
<path d="M200 260q-8-70 30-120" class="muted" marker-end="url(#ar)"/>
""", arrow=True)

add('crawl', '赤ちゃんが両手と両ひざを床につけて、ゆっくり前へはっていくイラスト。', f"""
<circle cx="470" cy="120" r="70" class="violetp"/>
<g transform="translate(280 300)">
  <path d="M-70-40q70-24 140 0l-6 40h-128z" class="coral o"/>
  <path d="M-64 0v34M-24 0v34M40 0v34M76 0v34" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
  <circle cx="-96" cy="-58" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-124-72q6-24 30-24 22 0 26 22-14-8-30-2-10-6-26 4z" fill="{HAIR}"/>
  <circle cx="-108" cy="-54" r="2.6" class="ink"/>
  <path d="M-112-42q10 6 18 0" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
<path d="M150 250q-40 10-56 34" class="muted" marker-end="url(#ar)"/>
<path d="M120 356h360" class="muted"/>
""", arrow=True)

add('dive', 'プールの飛び込み台から、頭を下にして水面へ飛び込む人のイラスト。', f"""
<path d="M0 260h600v140H0z" class="bluep"/>
<path d="M0 260h600" class="a"/>
<g class="blues" opacity=".8"><path d="M60 300q60-16 120 0t120 0"/><path d="M340 340q60-16 120 0t120 0"/></g>
<path d="M40 120h150v16H40z" class="goldp o"/>
<path d="M60 136v70M170 136v70" fill="none" stroke="{TONES['gold'][2]}" stroke-width="9"/>
<g transform="translate(330 190) rotate(52)">
  <path d="M-25-78q25-13 50 0l-8 72h-34z" class="coral o"/>
  <path d="M-12-8l-7 35M12-8l7 35" fill="none" stroke="{TONES['blue'][2]}" stroke-width="11" stroke-linecap="round"/>
  <path d="M-22-70l-26-35-5-17M22-70l26-35 5-17" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
  <circle cx="0" cy="-108" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-24-109q3-28 25-28 24 0 28 25-13-10-27-4-12-11-26 7z" fill="{HAIR}"/>
</g>
<path d="M214 158q60 20 92 58" class="muted" marker-end="url(#ar)"/>
<ellipse cx="404" cy="262" rx="40" ry="12" fill="#ffffff" stroke="{TONES['blue'][0]}" stroke-width="3"/>
""", ground=False, arrow=True)

add('jump', '両足で地面をけって空中へ跳び上がった人と、足元に残った影のイラスト。', f"""
<circle cx="470" cy="100" r="62" class="tealp"/>
{person(280,240,1.05,1,'teal','blue','up','short','smile')}
<ellipse cx="280" cy="330" rx="52" ry="12" fill="#cfd8d2" stroke="none"/>
<g class="teals" marker-end="url(#ar)"><path d="M170 262V190"/><path d="M392 262V190"/></g>
<path d="M120 330h360" class="a"/>
""", ground=True, arrow=True)

add('throw', '振りかぶった腕からボールが弧を描いて飛んでいくイラスト。', f"""
<circle cx="150" cy="100" r="60" class="coralp"/>
{person(160,336,1.0,1,'coral','blue','up','cap','neutral')}
<path d="M250 200q120-60 250 30" class="muted" marker-end="url(#ar)"/>
<circle cx="286" cy="176" r="17" class="gold o" opacity=".35"/>
<circle cx="360" cy="164" r="17" class="gold o" opacity=".6"/>
<circle cx="470" cy="204" r="20" class="gold o"/>
<path d="M462 188q16 12 16 32" fill="none" stroke="{TONES['gold'][2]}" stroke-width="2.5"/>
""", ground=True, arrow=True)

add('catch', '発車間際の列車に、走ってきた人がちょうど間に合って乗り込むイラスト。', f"""
<g transform="translate(400 210)">
  <path d="M-90-90h250q30 0 30 30v170h-280z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <path d="M-60-60h80v60h-80zM50-60h80v60h-80z" class="bluep o"/>
  <path d="M-90 70h280" class="a"/>
  <circle cx="0" cy="106" r="20" class="ink"/><circle cx="120" cy="106" r="20" class="ink"/>
  <path d="M-90-20v90h-40q-14 0-14-14v-62q0-14 14-14z" class="paper"/>
</g>
<path d="M0 316h600" class="a"/>
{person(180,316,0.95,1,'coral','gold','walk','short','surprised')}
<path d="M110 250q60-24 120-6" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('push', '大きな箱の後ろに手をあて、前方へ押して動かしている人のイラスト。', f"""
<circle cx="120" cy="110" r="58" class="tealp"/>
{box(400,290,110,86,26,'gold')}
{person(230,340,1.0,1,'teal','blue','point','short','neutral')}
<path d="M300 240h90" class="a" marker-end="url(#ar)"/>
<path d="M470 340h80" class="muted" marker-end="url(#ar)"/>
<path d="M60 356h500" class="a"/>
""", ground=True, arrow=True)

add('pull', 'ロープを両手で握り、荷車を自分の方へ引っ張っている人のイラスト。', f"""
<circle cx="480" cy="110" r="58" class="coralp"/>
{box(430,282,104,74,22,'gold')}
<circle cx="392" cy="336" r="20" class="ink"/><circle cx="470" cy="336" r="20" class="ink"/>
<path d="M250 280q60 6 130 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="7"/>
{person(200,356,1.0,1,'coral','blue','walk','cap','neutral')}
<path d="M300 226h-90" class="a" marker-end="url(#ar)"/>
<path d="M60 376h500" class="a"/>
""", ground=True, arrow=True)

add('lift', '重そうな箱を、ひざを曲げた姿勢から両手で持ち上げている人のイラスト。', f"""
<circle cx="470" cy="110" r="58" class="goldp"/>
{box(300,150,104,74,22,'gold')}
<path d="M240 196l-40 40M360 196l40 40" fill="none" stroke="{SKIN}" stroke-width="18" stroke-linecap="round"/>
{person(300,336,1.05,1,'teal','blue','up','short','neutral')}
<g class="teals" marker-end="url(#ar)"><path d="M180 250V150"/><path d="M420 250V150"/></g>
<path d="M80 356h440" class="a"/>
""", ground=True, arrow=True)

add('hang', 'ドアのそばのフックに、コートを掛けてぶら下げているイラスト。', f"""
<path d="M60 40h180v340H60z" fill="#e7dcc9" stroke="{INK}" stroke-width="3"/>
<circle cx="210" cy="220" r="12" class="goldd"/>
<path d="M340 110h30v20h-30z" class="ink"/>
<path d="M356 130q0 16-16 16" class="a"/>
<g transform="translate(400 150)">
  <path d="M0-24q-20 6-30 26l-26 60 26 10 8-20v130h44V202l8 20 26-10-26-60q-10-20-30-26z" class="coral o"/>
  <path d="M0-24l-14 22 14 18 14-18z" class="coralp o"/>
</g>
<path d="M400 108v18" fill="none" stroke="{INK}" stroke-width="4"/>
<path d="M470 200q26 40 0 90" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('cut', '包丁がパンに刃を入れ、一枚が切り離されているイラスト。', f"""
<circle cx="470" cy="100" r="58" class="goldp"/>
<g transform="translate(300 290)">
  <path d="M-170 30h340l-16 26h-308z" class="paper"/>
  <path d="M-40-70q60-26 130 0 20 60 0 96h-130z" class="goldp o"/>
  <path d="M-130-64q46-20 84 0 16 56 0 90h-84z" class="goldp o"/>
  <path d="M-46-64v90" class="a"/>
</g>
<g transform="translate(258 150) rotate(14)">
  <path d="M-10-6h150l30 26h-180z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-90-4h84v22h-84z" class="ink"/>
</g>
<path d="M258 196v56" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('dig', 'シャベルで地面を掘り、掘った土が横に積まれているイラスト。', f"""
<circle cx="120" cy="100" r="58" class="greenp"/>
<path d="M0 240h600v160H0z" fill="#e7d9c4"/>
<path d="M0 240h240q30 60 90 60t90-60h180" fill="#fffaf1" stroke="{INK}" stroke-width="3"/>
<path d="M0 240h600" class="a" opacity=".4"/>
<path d="M430 240q30-56 76 0z" fill="#d8c3a2" stroke="{INK}" stroke-width="2.5"/>
<g transform="translate(300 250) rotate(24)">
  <path d="M-8-130h16v110h-16z" class="goldd"/>
  <path d="M-30-20h60l-8 56h-44z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-8-140h16v14h-16z" class="ink"/>
</g>
<path d="M180 200q40 40 42 80" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('plant', '土に植えられた若い植物が、葉を広げて育っているイラスト。', f"""
<circle cx="470" cy="100" r="60" class="goldp"/>
<path d="M0 270h600v130H0z" fill="#e7d9c4"/>
<path d="M0 270h600" class="a"/>
<path d="M300 270V150" fill="none" stroke="{TONES['green'][2]}" stroke-width="9" stroke-linecap="round"/>
<path d="M300 214c-46-10-60-38-60-38 42-10 60 38 60 38z" class="green o"/>
<path d="M300 186c46-10 60-38 60-38-42-10-60 38-60 38z" class="green o"/>
<path d="M300 150c-34-18-34-52-34-52 34 6 34 52 34 52z" class="green o"/>
<g fill="none" stroke="#c9a97c" stroke-width="6" stroke-linecap="round">
  <path d="M300 270v56"/><path d="M300 292l-40 30"/><path d="M300 300l44 26"/>
</g>
""", ground=False)

add('mix', 'ボウルの中で白と赤の材料が、かき混ぜられて一つになっていくイラスト。', f"""
<circle cx="470" cy="100" r="56" class="coralp"/>
<g transform="translate(280 250)">
  <path d="M-120-40h240q-14 96-120 96T-120-40z" fill="#fffdf6" class="o"/>
  <path d="M-120-40h240" class="a"/>
  <path d="M-96-30q40 20 96 6t92-6q-12 70-96 70t-92-70z" class="coralp o"/>
  <path d="M-50-10q30 40 80 10" fill="none" stroke="#ffffff" stroke-width="8" stroke-linecap="round"/>
</g>
<path d="M300 140l86-70" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10" stroke-linecap="round"/>
<path d="M180 190a110 46 0 0 0 200 0" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('weigh', 'はかりに載せた果物の重さを、目盛りが指し示しているイラスト。', f"""
<circle cx="120" cy="110" r="58" class="tealp"/>
<g transform="translate(300 300)">
  <path d="M-120-30h240v70h-240z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <circle cx="0" cy="6" r="30" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 6l20-16" class="a"/>
  <path d="M-140-40h280l-10-14h-260z" class="tealp o"/>
</g>
<g transform="translate(300 226)">
  <path d="M-70 0h140l-10 20h-120z" class="paper"/>
  <circle cx="-28" cy="-22" r="22" class="coral o"/>
  <circle cx="20" cy="-16" r="26" class="green o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M-70 0v30" transform="translate(160 200)"/><path d="M70 0v30" transform="translate(370 200)"/></g>
""", ground=True, arrow=True)

# --- 状態・形 ----------------------------------------------------------------
add('empty', '中身が何も入っていないコップと、点線で示された元の中身のイラスト。', f"""
<circle cx="470" cy="110" r="62" class="bluep"/>
<g transform="translate(250 220)">
  <path d="M-76-110h152l-16 226h-120z" fill="#f7fbfe" class="o"/>
  <path d="M-70-16h140" class="muted"/>
  <path d="M-76-110h152" class="a"/>
</g>
<path d="M420 220q-40 20-70 22" class="muted" marker-end="url(#ar)"/>
<path d="M100 340h300" class="a"/>
""", ground=True, arrow=True)

add('rise', '朝日が地平線から上へのぼっていくイラスト。上向きの矢印が動きを示す。', f"""
<path d="M0 300h600v100H0z" class="ground"/>
{sun(300,270,72)}
<path d="M0 300h600" class="a"/>
<path d="M300 160V60" class="golds" marker-end="url(#ar)"/>
<path d="M170 300q0-70 40-110M430 300q0-70-40-110" class="muted"/>
""", ground=False, arrow=True)

add('fall', '木の枝から葉が下へ落ちていくイラスト。下向きの矢印が動きを示す。', f"""
{tree(140,340,1.3)}
<g transform="translate(340 120) rotate(20)"><path d="M0 0c-30-24-26-60 6-60 26 0 40 20 40 38 0 18-22 36-46 22z" class="goldp o"/></g>
<g transform="translate(360 220) rotate(-30)" opacity=".8"><path d="M0 0c-30-24-26-60 6-60 26 0 40 20 40 38 0 18-22 36-46 22z" class="goldp o"/></g>
<g transform="translate(340 320) rotate(60)"><path d="M0 0c-30-24-26-60 6-60 26 0 40 20 40 38 0 18-22 36-46 22z" class="gold o"/></g>
<path d="M470 90v220" class="golds" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('wide', '幅の広い川に、端から端まで長くかかった橋のイラスト。両側に幅を示す矢印。', f"""
<path d="M60 200h480v130H60z" class="bluep"/>
<path d="M60 200h480M60 330h480" class="a"/>
<path d="M40 170h520" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"/>
<path d="M120 178v54M300 178v54M480 178v54" fill="none" stroke="{TONES['gold'][2]}" stroke-width="8"/>
<path d="M70 380h460" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('narrow', '幅の狭い小道を、両側の壁がすぐ近くまで迫っているイラスト。狭さを示す矢印。', f"""
<path d="M0 60h250v300H0z" fill="#e7dcc9" stroke="{INK}" stroke-width="3"/>
<path d="M350 60h250v300H350z" fill="#e7dcc9" stroke="{INK}" stroke-width="3"/>
<path d="M250 60h100v300H250z" fill="#fffaf1"/>
<path d="M250 360h100" class="a"/>
<path d="M262 210h76" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
<path d="M60 120h150M400 120h150M60 300h150M400 300h150" fill="none" stroke="#cbbda3" stroke-width="6" stroke-linecap="round"/>
""", ground=False, arrow=True)

add('deep', '水面から底までがとても深い湖を、縦の長い矢印で示したイラスト。', f"""
<path d="M0 110h600v290H0z" class="bluep"/>
<path d="M0 110h600" class="a"/>
<path d="M0 340q120-40 300-30t300 20v70H0z" fill="#c9ad86" stroke="{INK}" stroke-width="3"/>
<path d="M300 130v190" class="blues" marker-start="url(#ar)" marker-end="url(#ar)" style="stroke-width:5"/>
<g class="blues" opacity=".7"><path d="M60 170h120M400 210h140M80 260h110"/></g>
<g transform="translate(460 300)"><path d="M0 0c-30-14-30-34 0-46 26 10 26 34 0 46z" class="teal o"/><path d="M0-46l24-14-6 22z" class="teal o"/></g>
""", ground=False, arrow=True)

add('heavy', '持ち上げようとした人の腕がたわむほど重い箱のイラスト。下向きの矢印が重さを示す。', f"""
{box(300,210,140,110,30,'gold')}
<path d="M230 270l-30 40M370 270l30 40" fill="none" stroke="{SKIN}" stroke-width="18" stroke-linecap="round"/>
{person(300,360,1.05,1,'coral','blue','stand','short','sad')}
<g class="a" marker-end="url(#ar)"><path d="M170 190v90"/><path d="M430 190v90"/></g>
<path d="M100 380h400" class="a"/>
""", ground=True, arrow=True)

add('straight', '曲がらずまっすぐ目的地へ向かう道と、点線で示された回り道を比べたイラスト。', f"""
<circle cx="80" cy="200" r="24" class="teal o"/>
<circle cx="520" cy="200" r="24" class="coral o"/>
<path d="M110 200h380" fill="none" stroke="{TONES['teal'][0]}" stroke-width="12" stroke-linecap="round" marker-end="url(#ar)"/>
<path d="M100 230q60 120 200 110t190-120" class="muted"/>
<path d="M100 170q60-120 200-110t190 120" class="muted"/>
""", ground=False, arrow=True)

# --- 場所・もの --------------------------------------------------------------
add('bridge', '川の両岸をつなぐ橋を、人が渡っているイラスト。', f"""
<path d="M0 250h600v150H0z" class="bluep"/>
<path d="M0 250h140v150H0zM460 250h140v150H460z" class="ground"/>
<path d="M0 250h140M460 250h600" class="a"/>
<path d="M100 190h400" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"/>
<path d="M120 197v56M300 197v56M480 197v56" fill="none" stroke="{TONES['gold'][2]}" stroke-width="8"/>
<path d="M100 160q100-40 200-40t200 40" fill="none" stroke="{TONES['gold'][0]}" stroke-width="7"/>
{person(300,186,0.62,1,'coral','blue','walk','short','smile')}
""", ground=False)

add('tunnel', '山を貫いて向こう側へ通り抜ける、アーチ型のトンネルのイラスト。', f"""
<path d="M20 330L300 70l280 260z" class="tealp o"/>
<path d="M200 330v-64a100 100 0 0 1 200 0v64z" fill="#3d4c5c" stroke="{INK}" stroke-width="3"/>
<path d="M224 330v-56a76 76 0 0 1 152 0v56z" fill="#22303e"/>
<circle cx="300" cy="286" r="26" class="goldp"/>
<path d="M60 356h480" class="a"/>
<path d="M300 380V336" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('ladder', '壁に立てかけたはしごを、段に足をかけて登っていくイラスト。', f"""
<path d="M340 40h260v320H340z" fill="#e7dcc9" stroke="{INK}" stroke-width="3"/>
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="11" stroke-linecap="round">
  <path d="M160 360L250 60M240 360L330 60"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="9" stroke-linecap="round">
  <path d="M172 320h82M186 270h82M200 220h82M214 170h82M228 120h82"/>
</g>
<path d="M120 300q-16-90 30-160" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('nest', '木の枝の上に組まれた巣の中で、卵とひなが守られているイラスト。', f"""
<circle cx="130" cy="110" r="62" class="greenp"/>
<path d="M0 320q160-40 300-30t300 20" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"/>
<g transform="translate(300 268)">
  <path d="M-110 20a110 60 0 0 1 220 0q-30 30-110 30T-110 20z" class="goldp o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="3">
    <path d="M-96 22q100-26 196 0M-84 40q90-20 172 0"/>
  </g>
  <ellipse cx="-34" cy="10" rx="24" ry="20" fill="#fffdf6" class="o"/>
  <ellipse cx="20" cy="14" rx="24" ry="20" fill="#fffdf6" class="o"/>
  <g transform="translate(64 -4)">
    <circle r="20" class="gold o"/>
    <path d="M18-4l20-6-14 16z" class="gold o"/>
    <circle cx="6" cy="-6" r="2.6" class="ink"/>
  </g>
</g>
""", ground=True)

add('whisper', '手を口元に添えて、隣の人の耳もとに小さな声で話しかけているイラスト。', f"""
<circle cx="470" cy="110" r="62" class="violetp"/>
{person(210,336,1.05,1,'teal','blue','point','short','neutral')}
{person(380,336,1.05,-1,'violet','gold','stand','bob','smile')}
<g transform="translate(300 216)">
  <path d="M-56-30h112q14 0 14 14v30q0 14-14 14h-90l-24 20 6-20h-4q-14 0-14-14v-30q0-14 14-14z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-34-8h40M-34 6h60"/></g>
</g>
<path d="M340 250q20 14 22 30" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('shout', '大きく口を開け、両手を上げて遠くへ声を張り上げているイラスト。', f"""
<circle cx="440" cy="140" r="80" class="coralp"/>
{person(200,336,1.15,1,'coral','blue','up','short','surprised')}
<g class="corals" opacity=".9">
  <path d="M300 150q40 20 40 60t-40 60" style="stroke-width:6"/>
  <path d="M350 120q60 30 60 90t-60 90" style="stroke-width:6"/>
  <path d="M400 90q80 40 80 120t-80 120" style="stroke-width:6"/>
</g>
<path d="M100 356h400" class="a"/>
""", ground=True)

add('swim', '海の中で腕をかいて前へ進んでいる人のイラスト。水面に波が立っている。', f"""
<path d="M0 190h600v210H0z" class="bluep"/>
<path d="M0 190q60-16 120 0t120 0 120 0 120 0 120 0" class="a"/>
<g class="blues" opacity=".7"><path d="M40 250q60-14 120 0M400 300q60-14 120 0M120 330q60-14 120 0"/></g>
<g transform="translate(300 220)">
  <path d="M-70 0q70-26 150 0-10 34-80 34T-70 0z" class="coral o"/>
  <circle cx="-100" cy="-16" r="28" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-126-30q4-26 28-26 22 0 26 24-14-8-28-2-10-6-26 4z" fill="{HAIR}"/>
  <circle cx="-110" cy="-14" r="2.6" class="ink"/>
  <path d="M-116 0q10 6 18 0" fill="none" stroke="{INK}" stroke-width="2"/>
  <path d="M-70-6q-30-34-60-24" fill="none" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
  <path d="M76 18q40 8 60 30" fill="none" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
</g>
<path d="M180 170q-40-16-60 4" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

print(' '.join(W))
print(sheet(W))
