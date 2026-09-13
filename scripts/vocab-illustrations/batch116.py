# -*- coding: utf-8 -*-
"""第116回。食べ物。実物を大きく一つ、切り口や中身が分かるように描く。"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib import *

W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))
BR = '#c99a63'; BRD = '#a0764a'; BRL = '#e8c391'

add('loaf', '切り分ける前のパンのかたまりと、切り離された一枚', f'''
<g>
  <path d="M150 260q-16-120 90-120h60q106 0 90 120z" fill="{BR}" class="o"/>
  <path d="M150 260h240v26H150z" fill="{BRD}" class="o"/>
  <g fill="none" stroke="{BRD}" stroke-width="4">
    <path d="M196 148q0 60 0 112M252 142v118M310 142v118M364 150v110"/>
  </g>
</g>
<g>
  <path d="M420 262q-8-96 44-96t44 96z" fill="{BRL}" class="o"/>
  <path d="M420 262h88v22h-88z" fill="{BRD}" class="o"/>
  <path d="M436 250q-6-72 28-72t28 72z" fill="#fff6e6" class="o"/>
</g>
<path d="M120 288h420" class="a"/>''', ground=False)

add('crust', 'パンの一枚が、かたい耳とやわらかい中身に分かれて見える', f'''
<g transform="translate(300 200)">
  <path d="M-130 90q-16-190 130-190t130 190z" fill="{BRD}" class="o"/>
  <path d="M-102 76q-14-160 102-160t102 160z" fill="#fff6e6" class="o"/>
  <g fill="{BRL}" opacity="0.8">
    <circle cx="-40" cy="0" r="9"/><circle cx="14" cy="-30" r="7"/><circle cx="50" cy="16" r="10"/>
    <circle cx="-14" cy="42" r="6"/><circle cx="-70" cy="40" r="7"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M96 130l64 20"/></g>
<g class="a" marker-end="url(#ar)"><path d="M504 130l-64 20"/></g>''', arrow=True, ground=False)

add('dough', 'こね台の上でパン生地が手でこねられている', f'''
<path d="M60 280h480v40H60z" fill="{BRL}" class="o"/>
<g>
  <path d="M170 280q-20-100 130-100t130 100z" fill="#fff2dc" class="o"/>
  <g fill="none" stroke="{BRL}" stroke-width="4">
    <path d="M230 250q30-24 70-6t70-14"/>
  </g>
</g>
{hand(226, 180, 1)}
{hand(378, 180, -1)}
<g fill="#fff2dc" stroke="{INK}" stroke-width="2">
  <circle cx="140" cy="300" r="9"/><circle cx="470" cy="302" r="7"/>
</g>''', ground=False)

add('noodle', 'どんぶりに入った汁そばから麺を箸で持ち上げている', f'''
<g>
  <path d="M150 220h300l-30 90q-6 20-120 20t-120-20z" class="bluep o"/>
  <ellipse cx="300" cy="220" rx="150" ry="34" class="blue o"/>
  <ellipse cx="300" cy="220" rx="126" ry="26" fill="#e0c48a"/>
</g>
<g fill="none" stroke="#f0d9a2" stroke-width="7" stroke-linecap="round">
  <path d="M254 216q26-70 66-96M282 220q18-74 58-100M312 218q14-70 50-98"/>
</g>
<g stroke="#8b6437" stroke-width="7" stroke-linecap="round" fill="none">
  <path d="M362 96l24-52M382 102l24-52"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M214 180q-10-20 2-34M186 190q-10-18 0-30"/>
</g>
<path d="M120 330h360" class="a"/>''', ground=False)

add('pasta', '皿に盛られた長い麺にソースがかかっている', f'''
<g>
  <ellipse cx="300" cy="250" rx="180" ry="58" fill="#fffefd" class="o"/>
  <ellipse cx="300" cy="244" rx="140" ry="42" fill="#f4efe6"/>
</g>
<g fill="none" stroke="#f0d9a2" stroke-width="9" stroke-linecap="round">
  <path d="M200 246q40-46 100-30t100 24"/>
  <path d="M206 258q46-30 96-14t96 12"/>
  <path d="M214 232q40-40 90-24t90 22"/>
</g>
<g class="coral o">
  <path d="M262 222q40-22 78 0 20 16-8 26-36 10-62 0-22-12-8-26z"/>
</g>
<circle cx="332" cy="228" r="7" class="green o"/>
<circle cx="284" cy="234" r="6" class="green o"/>
<path d="M100 308h400" class="a"/>''', ground=False)

add('dumpling', 'せいろに並んだ包み料理から湯気が上がっている', f'''
<g>
  <path d="M160 240h280v70q0 16-20 16H180q-20 0-20-16z" fill="{BR}" class="o"/>
  <ellipse cx="300" cy="240" rx="140" ry="30" fill="{BRL}" class="o"/>
</g>
<g fill="#fff6e6" stroke="{INK}" stroke-width="2.5">
  <path d="M226 246q0-34 34-34t34 34q-8 12-34 12t-34-12z"/>
  <path d="M306 246q0-34 34-34t34 34q-8 12-34 12t-34-12z"/>
  <path d="M266 216q0-30 34-30t34 30q-8 10-34 10t-34-10z"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="2.5">
  <path d="M240 214q8-6 14 0t14 0M320 214q8-6 14 0t14 0M280 186q8-6 14 0t14 0"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M256 158q10-20 0-36t8-28M344 158q10-20 0-36t8-28M300 140q10-20 0-36t8-26"/>
</g>
<path d="M130 326h340" class="a"/>''', ground=False)

add('tofu', '白い豆腐が一丁、切り分けられて皿にのっている', f'''
<g>
  <ellipse cx="300" cy="286" rx="170" ry="40" fill="#fffefd" class="o"/>
</g>
<g transform="translate(300 230)">
  <path d="M-90-40h180v66h-180z" fill="#fdfbf3" class="o"/>
  <path d="M-90-40l24-22h180l-24 22z" fill="#fffefd" class="o"/>
  <path d="M90-40l24-22v66l-24 22z" fill="#f2eee0" class="o"/>
  <path d="M-30-40v66M30-40v66" stroke="{MUTED}" stroke-width="2.5" fill="none"/>
  <path d="M-30-40l24-22M30-40l24-22" stroke="{MUTED}" stroke-width="2.5" fill="none"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M366 268h26M370 278h22"/>
</g>''', ground=False)

add('cereal', 'ボウルに入ったシリアルに牛乳が注がれている', f'''
<g>
  <path d="M170 200h260l-24 80q-6 22-106 22t-106-22z" fill="#fffefd" class="o"/>
  <ellipse cx="300" cy="200" rx="130" ry="30" fill="#f4efe6" class="o"/>
</g>
<g fill="{BRL}" stroke="{BRD}" stroke-width="2">
  <circle cx="248" cy="196" r="13"/><circle cx="288" cy="204" r="12"/><circle cx="330" cy="194" r="14"/>
  <circle cx="366" cy="204" r="11"/><circle cx="268" cy="212" r="11"/><circle cx="312" cy="216" r="12"/>
  <circle cx="352" cy="216" r="10"/>
</g>
<g transform="translate(452 120) rotate(28)">
  <path d="M-32-70h64v90q0 18-32 18t-32-18z" fill="#fffefd" class="o"/>
  <path d="M32-46h26q10 0 10 12t-10 12H32z" fill="#fffefd" class="o"/>
</g>
<g fill="none" stroke="#fffefd" stroke-width="10" stroke-linecap="round">
  <path d="M404 172q-20 12-24 26"/>
</g>
<path d="M140 306h320" class="a"/>''', ground=False)

add('porridge', 'とろりとした粥の椀にスプーンが差してある', f'''
<g>
  <path d="M180 210h240l-22 76q-6 20-98 20t-98-20z" fill="#fffefd" class="o"/>
  <ellipse cx="300" cy="210" rx="120" ry="28" fill="#f0e6cf" class="o"/>
  <path d="M212 206q26 16 88 16t88-16" fill="none" stroke="#dfd0ae" stroke-width="5"/>
</g>
<g transform="translate(370 168) rotate(22)">
  <ellipse rx="26" ry="17" fill="{MUTED}" stroke="{INK}" stroke-width="2.5"/>
  <path d="M18-6l70-44" stroke="{MUTED}" stroke-width="9" stroke-linecap="round" fill="none"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M244 176q10-18 0-32t8-24"/>
</g>
<path d="M150 306h300" class="a"/>''', ground=False)

add('pork', '骨つきの豚肉が一切れ', f'''
<g transform="translate(300 210)">
  <path d="M-120 30q-20-70 40-96 60-26 130-6 60 18 54 66-6 46-80 54-80 8-144-18z" fill="#f4b8b0" class="o"/>
  <path d="M-92 16q-12-50 36-68 48-18 104-2 46 14 40 44-6 30-62 36-62 6-118-10z" fill="#e88f88"/>
  <path d="M-124 22q-30-8-30-26t28-24l36 8-8 42z" fill="#fdf6ea" class="o"/>
  <path d="M-96 6q-20-4-20-14t18-14" fill="none" stroke="{MUTED}" stroke-width="3"/>
</g>
<path d="M130 288h340" class="a"/>''', ground=False)

add('bacon', '波打った薄いベーコンが数枚重なっている', f'''
<g stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
  <path d="M110 160q60-30 120 0t120 0 120 0v34q-60 30-120 30t-120-30-120 30z" fill="#f4b8b0"/>
  <path d="M110 194q60-30 120 0t120 0 120 0v22q-60 30-120 30t-120-30-120 30z" fill="#fdf6ea"/>
  <path d="M110 216q60-30 120 0t120 0 120 0v34q-60 30-120 30t-120-30-120 30z" fill="#e88f88"/>
  <path d="M110 250q60-30 120 0t120 0 120 0v22q-60 30-120 30t-120-30-120 30z" fill="#fdf6ea"/>
</g>
<path d="M90 320h420" class="a"/>''', ground=False)

add('ham', 'ハムの薄切りが皿に並んでいる', f'''
<ellipse cx="300" cy="240" rx="180" ry="56" fill="#fffefd" class="o"/>
<g stroke="{INK}" stroke-width="2.5">
  <ellipse cx="216" cy="228" rx="66" ry="34" fill="#f4b8b0"/>
  <ellipse cx="286" cy="234" rx="66" ry="34" fill="#f0a49c"/>
  <ellipse cx="356" cy="228" rx="66" ry="34" fill="#f4b8b0"/>
</g>
<g fill="#fdf6ea" opacity="0.9">
  <ellipse cx="200" cy="224" rx="10" ry="5"/><ellipse cx="300" cy="240" rx="9" ry="4"/>
  <ellipse cx="370" cy="222" rx="10" ry="5"/>
</g>
<path d="M110 302h380" class="a"/>''', ground=False)

add('sausage', '網の上で焼けているソーセージが数本', f'''
<g stroke="{INK}" stroke-width="2.5">
  <path d="M150 180q0-22 24-22h250q24 0 24 22t-24 22H174q-24 0-24-22z" fill="#c8705f"/>
  <path d="M150 226q0-22 24-22h250q24 0 24 22t-24 22H174q-24 0-24-22z" fill="#b45f4f"/>
  <path d="M150 272q0-22 24-22h250q24 0 24 22t-24 22H174q-24 0-24-22z" fill="#c8705f"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4">
  <path d="M120 300h360M120 316h360"/>
  <path d="M180 296v24M260 296v24M340 296v24M420 296v24"/>
</g>
{flame(230, 380, 0.3)}
{flame(360, 380, 0.3)}''', ground=False)

add('steak', '厚切りの肉が皿にのり、一部が切られている', f'''
<ellipse cx="300" cy="240" rx="190" ry="62" fill="#fffefd" class="o"/>
<g transform="translate(280 226)">
  <path d="M-110 22q-14-56 30-72 46-16 110-6 56 10 52 46-4 34-64 42-72 8-128-10z" fill="#8f4436" class="o"/>
  <path d="M-88 12q-8-38 26-50 36-12 88-4 44 8 40 30-4 22-52 28-58 6-102-4z" fill="#b05a48"/>
</g>
<g transform="translate(386 250) rotate(12)">
  <path d="M-38-16q30-14 64 0-12 22-64 20z" fill="#8f4436" class="o"/>
  <path d="M-30-10q26-10 52 0-10 14-52 12z" fill="#c96f5a"/>
</g>
<g stroke="{MUTED}" stroke-width="6" stroke-linecap="round" fill="none">
  <path d="M448 176l40-40"/>
</g>
<path d="M460 190l50-48-8-10-52 44z" fill="#cfd6dd" class="o"/>''', ground=False)

add('shrimp', '丸まった小エビが皿にのっている', f'''
<ellipse cx="300" cy="250" rx="170" ry="56" fill="#fffefd" class="o"/>
<g transform="translate(300 230)">
  <path d="M60 10q-6 60-70 60t-84-56q-14-52 34-72 40-16 62 10-34 4-42 30-10 34 26 44 40 10 54-16z" fill="#f0836a" class="o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="4">
    <path d="M-52-26q10 30 34 40M-30-46q6 34 30 46M-4-56q2 36 26 48"/>
  </g>
  <path d="M60 10l38-24-6 26 30 6-34 14z" class="coral o"/>
  <circle cx="-72" cy="-40" r="5" fill="{INK}"/>
  <g stroke="{TONES['coral'][2]}" stroke-width="3" fill="none" stroke-linecap="round">
    <path d="M-84-46l-30-24M-84-38l-34-12"/>
  </g>
</g>
<path d="M120 308h360" class="a"/>''', ground=False)

add('crab', '大きなはさみを持ったカニ', f'''
<g transform="translate(300 220)">
  <ellipse rx="110" ry="72" class="coral o"/>
  <path d="M-70-20q70-30 140 0" fill="none" stroke="{TONES['coral'][2]}" stroke-width="5"/>
  <g fill="{INK}"><circle cx="-34" cy="-44" r="9"/><circle cx="34" cy="-44" r="9"/></g>
  <g stroke="{TONES['coral'][2]}" stroke-width="4" fill="none">
    <path d="M-34-54v-20M34-54v-20"/>
  </g>
  <g stroke="{TONES['coral'][0]}" stroke-width="13" stroke-linecap="round" fill="none">
    <path d="M-96 30l-50 40M-88 54l-40 50M88 54l40 50M96 30l50 40"/>
  </g>
  <g class="corald o">
    <path d="M-108-36q-50-24-76 4-20 22 4 40l22-16-6 26 34-8z"/>
    <path d="M108-36q50-24 76 4 20 22-4 40l-22-16 6 26-34-8z"/>
  </g>
</g>
<path d="M90 330h420" class="a"/>''', ground=False)

add('lobster', '長い胴とはさみを持つロブスター', f'''
<g transform="translate(300 210)">
  <path d="M-30-70h60l14 130q2 26-44 26t-44-26z" class="coral o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="4">
    <path d="M-26-20h52M-22 12h44M-18 44h36"/>
  </g>
  <path d="M-30 84q-30 40 0 46 30-30 60 0 30-6 0-46z" class="corald o"/>
  <ellipse cy="-86" rx="34" ry="30" class="corald o"/>
  <g fill="{INK}"><circle cx="-14" cy="-96" r="6"/><circle cx="14" cy="-96" r="6"/></g>
  <g stroke="{TONES['coral'][2]}" stroke-width="3" fill="none" stroke-linecap="round">
    <path d="M-16-112l-24-46M16-112l24-46"/>
  </g>
  <g class="coral o">
    <path d="M-38-70q-60-10-76-56-8-26 16-32l14 34 14-30 18 34z"/>
    <path d="M38-70q60-10 76-56 8-26-16-32l-14 34-14-30-18 34z"/>
  </g>
  <g stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round" fill="none">
    <path d="M-40-20l-56 22M-38 16l-58 26M40-20l56 22M38 16l58 26"/>
  </g>
</g>''', ground=False)

add('oyster', '殻を開いたカキが氷の上にのっている', f'''
<g transform="translate(300 220)">
  <path d="M-160 40q-14-70 60-100 76-30 150 0 70 28 58 100z" fill="#dfe6ec" class="o"/>
  <path d="M-120 30q-10-52 46-74 58-22 114 0 52 20 44 74z" fill="#cfd8e2"/>
</g>
<g transform="translate(300 216)">
  <path d="M-92 24q-10-56 46-74 56-18 96 0 42 18 32 74z" fill="#e8e0cf" class="o"/>
  <path d="M-70 16q-6-40 36-52 42-12 72 0 32 12 24 52z" fill="#f6f0e2"/>
  <path d="M-30 6q30-22 62 0 12 16-14 24-34 8-52-4-14-10 4-20z" fill="#cfc4a8" class="o"/>
</g>
<g fill="#e6f0f6" stroke="{INK}" stroke-width="2">
  <path d="M140 268l24-14 24 14-24 14zM420 272l22-13 22 13-22 13z"/>
</g>
<path d="M110 292h380" class="a"/>''', ground=False)

add('squid', '長い足を持つイカ', f'''
<g transform="translate(300 180)">
  <path d="M-46-90h92l-6 130q-2 30-40 30t-40-30z" fill="#f0dfe2" class="o"/>
  <path d="M-46-90l-46 44 46 20zM46-90l46 44-46 20z" fill="#e6cfd4" class="o"/>
  <g fill="{INK}"><circle cx="-22" cy="46" r="7"/><circle cx="22" cy="46" r="7"/></g>
  <g stroke="#e6cfd4" stroke-width="11" stroke-linecap="round" fill="none">
    <path d="M-34 70q-20 60-4 108M-14 74q-8 62 2 112M14 74q8 62-2 112M34 70q20 60 4 108"/>
  </g>
  <g stroke="#dcc0c6" stroke-width="7" stroke-linecap="round" fill="none">
    <path d="M-48 66q-40 60-30 116M48 66q40 60 30 116"/>
  </g>
</g>''', ground=False)

add('tuna', '切り身にされたマグロの赤身', f'''
<ellipse cx="300" cy="250" rx="180" ry="56" fill="#fffefd" class="o"/>
<g stroke="{INK}" stroke-width="2.5">
  <path d="M188 208h96v66h-96z" fill="#b8394a"/>
  <path d="M188 208l22-20h96l-22 20z" fill="#cf5566"/>
  <path d="M284 208l22-20v66l-22 20z" fill="#9b2c3c"/>
  <path d="M318 216h96v58h-96z" fill="#c04255"/>
  <path d="M318 216l20-18h96l-20 18z" fill="#d76274"/>
  <path d="M414 216l20-18v58l-20 18z" fill="#a53042"/>
</g>
<g fill="none" stroke="#e08b96" stroke-width="3">
  <path d="M200 232h72M200 250h72M330 238h72M330 256h72"/>
</g>
<path d="M120 308h360" class="a"/>''', ground=False)

add('salmon', 'オレンジ色のサケの切り身に白い筋が入っている', f'''
<ellipse cx="300" cy="250" rx="180" ry="56" fill="#fffefd" class="o"/>
<g transform="translate(290 226)">
  <path d="M-120 30q-10-56 40-70 54-16 116 0 52 14 44 50-8 34-90 34-84 0-110-14z" fill="#f0855a" class="o"/>
  <g fill="none" stroke="#fdf0e4" stroke-width="7" stroke-linecap="round">
    <path d="M-92 18q60-24 190-6M-84 38q64-20 184-2M-96-2q54-24 176-8"/>
  </g>
  <path d="M78 12q26-6 42 8-16 18-42 12z" fill="#cfd6dd" class="o"/>
</g>
<path d="M120 308h360" class="a"/>''', ground=False)

add('cabbage', '葉が幾重にも巻いた丸いキャベツ', f'''
<g transform="translate(300 210)">
  <circle r="120" class="greenp o"/>
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="4">
    <path d="M-92-56q60 40 40 118M92-56q-60 40-40 118M0-118q-40 60 0 116M-116 20q70-20 116 40M116 20q-70-20-116 40"/>
  </g>
  <circle r="34" class="green o"/>
  <path d="M-20-10q20 20 40 0" fill="none" stroke="{TONES['green'][2]}" stroke-width="4"/>
</g>
<path d="M140 322h320" class="a"/>''', ground=False)

add('lettuce', '葉のふちが波打った軽いレタス', f'''
<g transform="translate(300 214)">
  <path d="M-120 60q-20-70 20-116 30-34 70-24 40-12 72 22 40 44 22 118z" class="greenp o"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="4">
    <path d="M-70 54q-14-70 30-104M0 58q-10-80 0-116M70 54q14-70-26-102"/>
  </g>
  <path d="M-120 60q30-20 60 0t60 0 60 0" fill="none" stroke="{TONES['green'][2]}" stroke-width="5"/>
</g>
<path d="M150 290h300" class="a"/>''', ground=False)

add('broccoli', '房が細かく分かれたブロッコリー', f'''
<g transform="translate(300 220)">
  <path d="M-20 90h40v-90h-40z" class="green o"/>
  <g class="greend o">
    <ellipse cx="-56" cy="-30" rx="46" ry="36"/><ellipse cx="56" cy="-30" rx="46" ry="36"/>
    <ellipse cx="0" cy="-62" rx="52" ry="40"/><ellipse cx="-30" cy="-6" rx="38" ry="30"/>
    <ellipse cx="30" cy="-6" rx="38" ry="30"/>
  </g>
  <g fill="{TONES['green'][0]}" opacity="0.5">
    <circle cx="-56" cy="-38" r="10"/><circle cx="52" cy="-40" r="10"/><circle cx="0" cy="-72" r="11"/>
    <circle cx="-24" cy="-14" r="8"/><circle cx="28" cy="-12" r="8"/>
  </g>
</g>
<path d="M170 312h260" class="a"/>''', ground=False)

add('cauliflower', '白い塊を緑の葉が包むカリフラワー', f'''
<g transform="translate(300 214)">
  <g class="greenp o">
    <path d="M-100 40q-40-70 4-104 20 60 46 76zM100 40q40-70-4-104-20 60-46 76z"/>
  </g>
  <g fill="#fdf8ec" stroke="{INK}" stroke-width="2.5">
    <ellipse cx="-46" cy="-16" rx="44" ry="36"/><ellipse cx="46" cy="-16" rx="44" ry="36"/>
    <ellipse cx="0" cy="-48" rx="50" ry="38"/><ellipse cx="-24" cy="16" rx="38" ry="30"/>
    <ellipse cx="24" cy="16" rx="38" ry="30"/>
  </g>
  <g fill="#eee7d4">
    <circle cx="-44" cy="-24" r="10"/><circle cx="44" cy="-24" r="10"/><circle cx="0" cy="-58" r="11"/>
    <circle cx="-20" cy="10" r="8"/><circle cx="22" cy="12" r="8"/>
  </g>
  <path d="M-20 44h40v42h-40z" class="green o"/>
</g>
<path d="M170 306h260" class="a"/>''', ground=False)

add('celery', '筋の通った長い茎が束になったセロリ', f'''
<g transform="translate(300 220)">
  <g stroke="{INK}" stroke-width="2.5">
    <path d="M-70 90q-14-100 10-160 8-20 24-20l6 180z" class="greenp"/>
    <path d="M-30 90q-8-110 6-170 6-22 24-22l4 192z" class="green"/>
    <path d="M14 90q8-110-2-170-4-22-22-22l-2 192z" class="greenp"/>
    <path d="M56 90q14-100-8-160-8-20-24-20l-6 180z" class="greend"/>
  </g>
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="3">
    <path d="M-52 80q-8-90 4-140M-12 82q-6-96 2-150M30 80q8-90-2-140"/>
  </g>
  <g class="greend o">
    <path d="M-34-90q-30-30-6-52 22 8 26 44zM10-92q30-30 6-52-22 8-26 44z"/>
  </g>
</g>
<path d="M190 312h220" class="a"/>''', ground=False)

add('cucumber', '細長いきゅうりと、その輪切り', f'''
<g transform="translate(260 210) rotate(-14)">
  <path d="M-150 0q0-34 34-34h230q34 0 34 34t-34 34H-116q-34 0-34-34z" class="greend o"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="4">
    <path d="M-120-16q40 10 0 32M-60-20q46 12 0 40M0-20q46 12 0 40M60-20q46 12 0 40"/>
  </g>
</g>
<g>
  <circle cx="450" cy="288" r="42" class="greenp o"/>
  <circle cx="450" cy="288" r="30" fill="#e9f4e6"/>
  <g fill="#cfe4c8"><circle cx="440" cy="280" r="5"/><circle cx="458" cy="284" r="5"/><circle cx="448" cy="298" r="5"/></g>
</g>''', ground=False)

add('pumpkin', '縦の筋が入ったオレンジ色のかぼちゃ', f'''
<g transform="translate(300 226)">
  <ellipse rx="140" ry="104" class="gold o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="5">
    <path d="M-90-72q-24 72 0 144M-44-92q-14 92 0 184M44-92q14 92 0 184M90-72q24 72 0 144"/>
  </g>
  <path d="M-14-104h28v-34h-28z" class="greend o"/>
  <path d="M14-130q40-20 44 12" fill="none" stroke="{TONES['green'][2]}" stroke-width="5" stroke-linecap="round"/>
</g>
<path d="M130 332h340" class="a"/>''', ground=False)

add('eggplant', 'つやのある濃い紫のなす', f'''
<g transform="translate(300 220) rotate(12)">
  <path d="M0-70q76 0 76 76t-76 82q-76-6-76-82t76-76z" class="violetd o"/>
  <path d="M-34-24q-18 40 0 70" fill="none" stroke="#c7b8e6" stroke-width="9" stroke-linecap="round"/>
  <path d="M-22-72q-14-16 0-30 12 12 26 10 12 16 0 26z" class="green o"/>
  <path d="M2-100v-26" stroke="{TONES['green'][2]}" stroke-width="7" stroke-linecap="round" fill="none"/>
</g>
<path d="M180 320h240" class="a"/>''', ground=False)

add('garlic', 'にんにくの球と、はがした一かけ', f'''
<g transform="translate(250 220)">
  <path d="M0-90q80 0 80 74t-80 76q-80-6-80-76 0-74 80-74z" fill="#f6f0e2" class="o"/>
  <g fill="none" stroke="#ddd4bd" stroke-width="4">
    <path d="M-46-58q-14 70 0 116M0-84q-10 78 0 132M46-58q14 70 0 116"/>
  </g>
  <path d="M-8-90h16v-30q0-8-8-8t-8 8z" fill="#ccc3a8" class="o"/>
</g>
<g transform="translate(430 250)">
  <path d="M0-56q40 0 40 34t-40 40q-40-6-40-40 0-34 40-34z" fill="#fdf8ec" class="o"/>
  <path d="M-14-24q-8 30 0 46" fill="none" stroke="#e2d9c2" stroke-width="5"/>
</g>
<path d="M140 324h340" class="a"/>''', ground=False)

add('ginger', 'ごつごつと枝分かれしたしょうがの根', f'''
<g transform="translate(300 220)">
  <path d="M-120 20q-16-46 26-56 40-10 62 6 26-40 70-24 40 14 32 50-8 34-56 34-40 0-64-14-30 20-70 4z" fill="#e0c48a" class="o"/>
  <path d="M60-46q30-40 62-20 26 16 6 44-20 26-52 8z" fill="#d8b878" class="o"/>
  <path d="M-96 34q-24 34 4 48 26 12 40-14z" fill="#d8b878" class="o"/>
  <g fill="none" stroke="#b89a5e" stroke-width="3.5">
    <path d="M-60-16q20 20 46 10M20-24q18 18 44 8M-40 30q26 12 50 0"/>
  </g>
</g>
<path d="M150 306h300" class="a"/>''', ground=False)

add('chili', '細長い赤いとうがらしが二本', f'''
<g transform="translate(270 210) rotate(-18)">
  <path d="M0-70q40 0 40 44 0 70-40 106-40-36-40-106 0-44 40-44z" class="coral o"/>
  <path d="M-14-30q-8 50 6 80" fill="none" stroke="#f7c7bd" stroke-width="7" stroke-linecap="round"/>
  <path d="M-16-70h32v-16h-32z" class="green o"/>
  <path d="M0-86q-20-24 4-32 18 14 8 32z" class="greend o"/>
</g>
<g transform="translate(390 246) rotate(16)">
  <path d="M0-56q32 0 32 36 0 56-32 86-32-30-32-86 0-36 32-36z" class="corald o"/>
  <path d="M-12-56h24v-14h-24z" class="green o"/>
</g>
<path d="M170 330h260" class="a"/>''', ground=False)

add('mushroom', 'かさと軸のあるきのこが二本', f'''
<g transform="translate(280 220)">
  <path d="M-22 80h44v-84h-44z" fill="#f2e9d6" class="o"/>
  <path d="M-100-4q0-76 100-76t100 76q-30 22-100 22t-100-22z" fill="#a0764a" class="o"/>
  <g fill="#8b6437">
    <circle cx="-46" cy="-30" r="13"/><circle cx="20" cy="-46" r="11"/><circle cx="60" cy="-20" r="10"/>
  </g>
  <path d="M-88 0q40 16 88 16t88-16" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>
<g transform="translate(430 260) scale(0.62)">
  <path d="M-22 80h44v-84h-44z" fill="#f2e9d6" class="o"/>
  <path d="M-100-4q0-76 100-76t100 76q-30 22-100 22t-100-22z" fill="#b5854f" class="o"/>
</g>
<path d="M140 312h360" class="a"/>''', ground=False)

add('asparagus', '穂先のとがったアスパラガスが束ねられている', f'''
<g transform="translate(300 216)">
''' + ''.join(f'<g transform="translate({-70+i*35} 0) rotate({-8+i*4})"><path d="M-11 96V-56q0-24 11-40 11 16 11 40V96z" class="green o"/><path d="M-9-52q9-14 18 0" fill="none" stroke="{TONES["green"][2]}" stroke-width="3"/><path d="M-8-20q8 10 16 0M-8 6q8 10 16 0M-8 32q8 10 16 0" fill="none" stroke="{TONES["green"][2]}" stroke-width="3"/></g>' for i in range(5)) + f'''
  <path d="M-92 34h184v22h-184z" class="coral o"/>
</g>
<path d="M170 320h260" class="a"/>''', ground=False)

add('pea', 'さやが開いて中に緑の豆が並んでいる', f'''
<g transform="translate(300 216) rotate(-10)">
  <path d="M-160 30q-20-70 60-84 100-18 190 6 60 16 54 48-6 30-100 34-140 6-204-4z" class="greenp o"/>
  <path d="M-140 6q40-30 130-24 90 6 150 30" fill="none" stroke="{TONES['green'][2]}" stroke-width="4"/>
  <g class="green o">
    <circle cx="-90" cy="14" r="28"/><circle cx="-24" cy="20" r="30"/>
    <circle cx="44" cy="22" r="29"/><circle cx="110" cy="18" r="27"/>
  </g>
  <g fill="#cfe4c8">
    <circle cx="-98" cy="4" r="8"/><circle cx="-32" cy="10" r="8"/><circle cx="36" cy="12" r="8"/><circle cx="102" cy="8" r="7"/>
  </g>
</g>
<path d="M110 296h380" class="a"/>''', ground=False)

add('leek', '白い根元から緑の葉が広がるねぎ', f'''
<g transform="translate(300 220)">
  <path d="M-26 110h52V-10h-52z" fill="#f6f2e4" class="o"/>
  <g fill="none" stroke="#ddd8c4" stroke-width="3"><path d="M-8 110V-10M10 110V-10"/></g>
  <path d="M-26-10h52v-30h-52z" fill="#e6efd8" class="o"/>
  <g class="greend o">
    <path d="M-24-40q-40-60-14-104 30 34 34 104zM24-40q40-60 14-104-30 34-34 104z"/>
    <path d="M-6-40q-8-74 8-108 16 34 10 108z"/>
  </g>
  <g stroke="#fffefd" stroke-width="6" stroke-linecap="round" fill="none">
    <path d="M-20 118l-16 20M0 118v22M20 118l16 20"/>
  </g>
</g>
<path d="M190 342h220" class="a"/>''', ground=False)

add('peach', '毛羽だった赤みのある桃と、その断面', f'''
<g transform="translate(250 216)">
  <circle r="104" fill="#f6b8a0" class="o"/>
  <path d="M-70-60q60-30 130 10" fill="none" stroke="#fbd8c8" stroke-width="12" stroke-linecap="round"/>
  <path d="M0-104q-6-40 30-46-6 34-30 46z" class="green o"/>
  <path d="M0-104q0 60 0 208" fill="none" stroke="#e08a70" stroke-width="5"/>
</g>
<g transform="translate(438 250)">
  <path d="M0-72q66 0 66 66t-66 66q-66 0-66-66 0-66 66-66z" fill="#f9c6b0" class="o"/>
  <path d="M0-56q52 0 52 50t-52 50q-52 0-52-50 0-50 52-50z" fill="#fbdccc"/>
  <ellipse ry="30" rx="20" fill="#8b6437" class="o"/>
</g>
<path d="M120 328h380" class="a"/>''', ground=False)

add('pear', '下がふくらんだ洋なし', f'''
<g transform="translate(300 220)">
  <path d="M0-112q22 0 22 26 0 26-14 44 44 22 44 76 0 62-52 62t-52-62q0-54 44-76-14-18-14-44 0-26 22-26z" class="greenp o"/>
  <path d="M-24 14q-16 34 4 60" fill="none" stroke="#dff0d8" stroke-width="8" stroke-linecap="round"/>
  <path d="M0-112v-26" stroke="#8b6437" stroke-width="7" stroke-linecap="round" fill="none"/>
  <path d="M4-130q34-16 40 12-30 10-40-12z" class="green o"/>
</g>
<path d="M200 320h200" class="a"/>''', ground=False)

add('plum', '濃い紫のすももが二つ', f'''
<g transform="translate(266 224)">
  <circle r="86" class="violetd o"/>
  <path d="M0-86v172" fill="none" stroke="#4a3b6e" stroke-width="5"/>
  <path d="M-46-52q30-22 60-6" fill="none" stroke="#c7b8e6" stroke-width="10" stroke-linecap="round"/>
  <path d="M0-86v-24" stroke="#8b6437" stroke-width="6" stroke-linecap="round" fill="none"/>
</g>
<g transform="translate(400 262)">
  <circle r="62" class="violet o"/>
  <path d="M0-62v124" fill="none" stroke="#4a3b6e" stroke-width="4"/>
  <path d="M0-62v-18" stroke="#8b6437" stroke-width="5" stroke-linecap="round" fill="none"/>
</g>
<path d="M150 326h320" class="a"/>''', ground=False)

add('cherry', '一本の柄から二つ下がったさくらんぼ', f'''
<g transform="translate(300 190)">
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="7" stroke-linecap="round">
    <path d="M0-90q-40 40-56 96M0-90q40 40 56 96"/>
  </g>
  <path d="M0-90q26-30 56-20-16 30-56 20z" class="green o"/>
  <circle cx="-56" cy="30" r="52" class="coral o"/>
  <circle cx="56" cy="30" r="52" class="corald o"/>
  <path d="M-76 8q16-14 32-6" fill="none" stroke="#fbd5cd" stroke-width="9" stroke-linecap="round"/>
</g>
<path d="M170 300h260" class="a"/>''', ground=False)

add('grape', '房になったぶどうと葉', f'''
<g transform="translate(300 210)">
  <path d="M0-120v34" stroke="#8b6437" stroke-width="7" stroke-linecap="round" fill="none"/>
  <path d="M4-114q40-30 66 0-34 30-66 0z" class="green o"/>
  <g class="violet o">
    <circle cx="-46" cy="-60" r="26"/><circle cx="0" cy="-70" r="26"/><circle cx="46" cy="-60" r="26"/>
    <circle cx="-70" cy="-14" r="26"/><circle cx="-24" cy="-20" r="26"/><circle cx="24" cy="-20" r="26"/><circle cx="70" cy="-14" r="26"/>
    <circle cx="-46" cy="28" r="26"/><circle cx="0" cy="32" r="26"/><circle cx="46" cy="28" r="26"/>
    <circle cx="-22" cy="72" r="26"/><circle cx="22" cy="72" r="26"/>
    <circle cx="0" cy="112" r="26"/>
  </g>
  <g fill="#c7b8e6" opacity="0.8">
    <circle cx="-52" cy="-68" r="7"/><circle cx="-6" cy="-78" r="7"/><circle cx="-30" cy="-28" r="7"/><circle cx="18" cy="24" r="7"/>
  </g>
</g>''', ground=False)

add('watermelon', '皮の縞模様が見えるすいかと、赤い切り身', f'''
<g transform="translate(232 218)">
  <circle r="106" class="greend o"/>
  <g fill="none" stroke="#dff0d8" stroke-width="12">
    <path d="M-64-84q-24 84 0 168M0-106v212M64-84q24 84 0 168"/>
  </g>
</g>
<g transform="translate(430 240) rotate(14)">
  <path d="M-92 40q0-92 92-92t92 92z" class="green o"/>
  <path d="M-76 40q0-78 76-78t76 78z" fill="#fffefd" class="o"/>
  <path d="M-64 40q0-66 64-66t64 66z" class="coral o"/>
  <g fill="{INK}">
    <ellipse cx="-26" cy="14" rx="5" ry="8"/><ellipse cx="8" cy="0" rx="5" ry="8"/><ellipse cx="34" cy="20" rx="5" ry="8"/>
  </g>
</g>
<path d="M100 328h420" class="a"/>''', ground=False)

add('pineapple', 'とげのある皮と冠の葉を持つパイナップル', f'''
<g transform="translate(300 232)">
  <ellipse rx="86" ry="112" class="gold o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="3.5">
''' + ''.join(f'<path d="M-86 {-84+i*28}L86 {-112+i*28}"/>' for i in range(8)) + ''.join(f'<path d="M-86 {-112+i*28}L86 {-84+i*28}"/>' for i in range(8)) + f'''
  </g>
  <g class="greend o">
    <path d="M-10-112q-30-50-6-84 22 34 22 84zM10-112q30-50 6-84-22 34-22 84z"/>
    <path d="M0-112q-8-64 0-96 8 32 0 96z"/>
    <path d="M-26-108q-44-30-42-64 34 20 50 62zM26-108q44-30 42-64-34 20-50 62z"/>
  </g>
</g>
<path d="M190 348h220" class="a"/>''', ground=False)

add('strawberry', 'つぶつぶのある赤いいちご', f'''
<g transform="translate(300 218)">
  <path d="M0 116q-96-30-96-114 0-40 40-46 26-16 56 0 40 6 40 46 0 84-40 114z" class="coral o"/>
  <g fill="#fdf0d0">
    <circle cx="-40" cy="-18" r="6"/><circle cx="-8" cy="-32" r="6"/><circle cx="26" cy="-20" r="6"/>
    <circle cx="-52" cy="16" r="6"/><circle cx="-18" cy="6" r="6"/><circle cx="16" cy="12" r="6"/><circle cx="48" cy="10" r="6"/>
    <circle cx="-34" cy="50" r="6"/><circle cx="4" cy="46" r="6"/><circle cx="36" cy="48" r="6"/>
    <circle cx="-14" cy="84" r="6"/><circle cx="18" cy="82" r="6"/>
  </g>
  <g class="greend o">
    <path d="M0-44q-34-6-46-30 30-6 46 12zM0-44q34-6 46-30-30-6-46 12zM0-44q-14-30 0-48 14 18 0 48z"/>
  </g>
  <path d="M0-92v-24" stroke="{TONES['green'][2]}" stroke-width="6" stroke-linecap="round" fill="none"/>
</g>''', ground=False)

add('coconut', '毛におおわれたココナッツと、割れて白い果肉が見える半分', f'''
<g transform="translate(232 224)">
  <circle r="96" fill="#8b6437" class="o"/>
  <g fill="none" stroke="#6b4c28" stroke-width="4">
    <path d="M-70-40q60 30 130 0M-70 30q60 30 130 0M-40-80q30 100 0 160"/>
  </g>
  <g fill="#5b4020"><circle cx="-24" cy="-40" r="9"/><circle cx="12" cy="-46" r="9"/><circle cx="-6" cy="-14" r="9"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-80 30q0-80 80-80t80 80z" fill="#8b6437" class="o"/>
  <path d="M-66 30q0-66 66-66t66 66z" fill="#fdf8ec" class="o"/>
  <path d="M-46 30q0-46 46-46t46 46z" fill="#f2ead6"/>
</g>
<path d="M110 322h400" class="a"/>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
