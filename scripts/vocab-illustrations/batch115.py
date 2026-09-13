# -*- coding: utf-8 -*-
"""第115回。増補3,000語の挿絵の第1弾。台所・住まい・道具・身の回りの品。
物そのものを大きく一つ描き、使う手や場面を小さく添える。"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib import *

W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))

# --- 台所と住まい -----------------------------------------------------------
add('drawer', 'たんすの引き出しが一段だけ手前に引き出されている', f'''
<g>
  <path d="M150 90h300v216H150z" fill="#c99a63" class="o"/>
  <path d="M164 104h272v56H164zM164 232h272v58H164z" fill="#b5854f" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round">
    <path d="M270 132h60M270 261h60"/>
  </g>
  <path d="M120 172h330v66H120z" fill="#dcae72" class="o"/>
  <path d="M120 172l44-6h316l-30 6z" fill="#e8c391" class="o"/>
  <path d="M255 205h60" stroke="{INK}" stroke-width="5" fill="none" stroke-linecap="round"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M96 205h-40"/></g>''', arrow=True)

add('kettle', 'やかんが火にかけられ、注ぎ口から湯気が上がっている', f'''
<g>
  <path d="M240 306q-56 0-56-62 0-58 60-58h64q60 0 60 58 0 62-56 62z" class="teal o"/>
  <path d="M368 216q34-6 40 22 6 26-24 34l-8-26q16-2 12-14-4-10-18-6z" class="teald o"/>
  <path d="M264 186q0-26 40-26t40 26" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <ellipse cx="304" cy="184" rx="26" ry="9" class="tealp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round">
  <path d="M396 214q14-22 0-42t8-38"/>
  <path d="M424 226q12-18 0-34t6-32"/>
</g>
{flame(268, 372, 0.42)}
<path d="M170 306h270" class="a"/>''', ground=False)

add('saucepan', '取っ手が一本ついた片手鍋', f'''
<g>
  <path d="M150 200h220v70q0 38-40 38h-140q-40 0-40-38z" class="muted-none teal o"/>
  <ellipse cx="260" cy="200" rx="110" ry="24" class="tealp o"/>
  <ellipse cx="260" cy="200" rx="84" ry="16" fill="#cfe6df"/>
  <path d="M370 214h94q16 0 16 14t-16 14h-94z" fill="#5b4a3c" class="o"/>
</g>
<path d="M120 308h340" class="a"/>''', ground=False)

add('frying-pan', '浅くて平たいフライパンに卵が一つ焼けている', f'''
<g>
  <ellipse cx="250" cy="230" rx="130" ry="44" fill="#3b4450" class="o"/>
  <ellipse cx="250" cy="222" rx="120" ry="38" fill="#556070" class="o"/>
  <ellipse cx="238" cy="220" rx="46" ry="24" fill="#fffdf6" class="o"/>
  <circle cx="238" cy="220" r="15" class="gold o"/>
  <path d="M378 226h108q16 0 16 15t-16 15H378z" fill="#5b4a3c" class="o"/>
</g>
{flame(230, 330, 0.36)}
<path d="M100 306h400" class="a"/>''', ground=False)

add('toaster', 'トースターから焼けたパンが飛び出している', f'''
<g>
  <path d="M170 180h260v126H170z" rx="14" class="coral o"/>
  <path d="M170 180q0-16 20-16h220q20 0 20 16" class="corald o"/>
  <path d="M212 176h64v10h-64zM324 176h64v10h-64z" fill="{INK}"/>
  <circle cx="398" cy="260" r="16" class="goldp o"/>
  <path d="M398 252v16" stroke="{INK}" stroke-width="3" fill="none"/>
</g>
<g>
  <path d="M206 160v-64q0-14 18-14h34q18 0 18 14v64z" class="gold o"/>
  <path d="M320 160v-64q0-14 18-14h34q18 0 18 14v64z" class="gold o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M244 60v-24M356 60v-24"/></g>
<path d="M140 306h320" class="a"/>''', arrow=True, ground=False)

add('stove', '四つ口のコンロの上で鍋が煮えている', f'''
<g>
  <path d="M130 200h340v106H130z" fill="#8f9aa6" class="o"/>
  <path d="M130 200h340v22H130z" fill="#6f7b88" class="o"/>
  <g fill="#3b4450" stroke="{INK}" stroke-width="2.5">
    <circle cx="205" cy="256" r="30"/><circle cx="300" cy="256" r="30"/>
    <circle cx="395" cy="256" r="30"/>
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    <circle cx="205" cy="256" r="16"/><circle cx="300" cy="256" r="16"/><circle cx="395" cy="256" r="16"/>
  </g>
</g>
<g>
  <path d="M244 200h112v-42q0-30-56-30t-56 30z" class="teal o"/>
  <ellipse cx="300" cy="128" rx="56" ry="12" class="tealp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M282 112q10-18 0-32t6-26M320 112q10-16 0-28t6-24"/>
</g>
<path d="M100 306h400" class="a"/>''', ground=False)

add('freezer', '冷凍庫の扉が開いて中の霜と氷が見えている', f'''
<g>
  <path d="M180 70h230v240H180z" fill="#e6eef4" class="o"/>
  <path d="M196 86h198v92H196z" fill="#cfe0ec" class="o"/>
  <path d="M196 194h198v100H196z" fill="#cfe0ec" class="o"/>
  <g fill="#fffefd" stroke="{INK}" stroke-width="2">
    <rect x="216" y="106" width="42" height="30" rx="4"/>
    <rect x="272" y="106" width="42" height="30" rx="4"/>
    <rect x="328" y="106" width="42" height="30" rx="4"/>
    <rect x="240" y="216" width="46" height="34" rx="4"/>
    <rect x="302" y="216" width="46" height="34" rx="4"/>
  </g>
  <path d="M410 176h14v40h-14z" fill="{MUTED}" stroke="{INK}" stroke-width="2"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3.5" stroke-linecap="round">
  <path d="M460 120v52M434 146h52M442 128l36 36M478 128l-36 36"/>
  <path d="M470 240v34M453 257h34M458 245l24 24M482 245l-24 24"/>
</g>
<path d="M150 310h330" class="a"/>''', ground=False)

add('mattress', 'ベッド枠の上に厚いマットレスが載っている', f'''
<g>
  <path d="M110 260h380v46H110z" fill="#8b6437" class="o"/>
  <path d="M120 306v34M480 306v34" stroke="#8b6437" stroke-width="14" stroke-linecap="round" fill="none"/>
  <path d="M124 180h352q20 0 20 22v58H104v-58q0-22 20-22z" fill="#fffefd" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5">
    <path d="M104 220h392"/>
  </g>
  <g fill="{MUTED}">
    <circle cx="164" cy="200" r="5"/><circle cx="244" cy="200" r="5"/>
    <circle cx="324" cy="200" r="5"/><circle cx="404" cy="200" r="5"/>
    <circle cx="204" cy="242" r="5"/><circle cx="284" cy="242" r="5"/><circle cx="364" cy="242" r="5"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M76 182v76"/></g>''', arrow=True, ground=False)

add('pillow', 'ふっくらしたまくらが一つ置かれている', f'''
<g transform="translate(300 210)">
  <path d="M-150-62q30-18 150-18t150 18q18 28 0 62-30 20-150 20t-150-20q-18-34 0-62z" fill="#fffefd" class="o"/>
  <path d="M-124-46q26-12 124-12t124 12" fill="none" stroke="{MUTED}" stroke-width="2.5"/>
  <path d="M-124 40q26 12 124 12t124-12" fill="none" stroke="{MUTED}" stroke-width="2.5"/>
</g>
<path d="M110 300h380" class="a"/>''', ground=False)

add('wardrobe', '洋服だんすの扉が開いて服が掛かっている', f'''
<g>
  <path d="M160 60h280v250H160z" fill="#c99a63" class="o"/>
  <path d="M176 76h122v218H176z" fill="#b5854f" class="o"/>
  <path d="M302 76h122v218H302z" fill="#dcae72" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round">
    <path d="M288 176v28M312 176v28"/>
  </g>
  <path d="M312 104h100" stroke="{INK}" stroke-width="4" fill="none"/>
  <g>
    <path d="M332 104v16M362 104v16M392 104v16" stroke="{INK}" stroke-width="3" fill="none"/>
    <path d="M332 120l-16 22 10 60h12l10-60z" class="teal o"/>
    <path d="M362 120l-16 22 10 60h12l10-60z" class="coral o"/>
    <path d="M392 120l-16 22 10 60h12l10-60z" class="violet o"/>
  </g>
</g>
<path d="M130 310h340" class="a"/>''', ground=False)

add('bookshelf', '本棚に本が並び、一冊が引き出されかけている', f'''
<g>
  <path d="M140 60h320v250H140z" fill="#c99a63" class="o"/>
  <path d="M154 74h292v10H154zM154 158h292v10H154zM154 240h292v10H154z" fill="#8b6437"/>
  <g stroke="{INK}" stroke-width="2.5">
    <rect x="166" y="90" width="20" height="68" class="teal"/>
    <rect x="190" y="96" width="16" height="62" class="coral"/>
    <rect x="210" y="90" width="24" height="68" class="gold"/>
    <rect x="238" y="100" width="18" height="58" class="violet"/>
    <rect x="260" y="92" width="20" height="66" class="green"/>
    <rect x="166" y="176" width="22" height="64" class="violet"/>
    <rect x="192" y="182" width="18" height="58" class="teal"/>
    <rect x="214" y="176" width="20" height="64" class="coral"/>
    <rect x="238" y="184" width="24" height="56" class="gold"/>
  </g>
  <rect x="330" y="176" width="26" height="64" class="green o" transform="translate(0 -14) rotate(-8 343 208)"/>
</g>
<path d="M110 310h380" class="a"/>''', ground=False)

add('stool', '背もたれのない丸いすが一脚', f'''
<g>
  <ellipse cx="300" cy="150" rx="86" ry="24" class="gold o"/>
  <path d="M214 150v14q0 22 86 22t86-22v-14" class="goldd o"/>
  <g stroke="#8b6437" stroke-width="13" stroke-linecap="round" fill="none">
    <path d="M240 178l-32 128M360 178l32 128M264 184l-8 122M336 184l8 122"/>
  </g>
  <g stroke="#8b6437" stroke-width="8" fill="none">
    <path d="M226 244h148"/>
  </g>
</g>
<path d="M170 306h260" class="a"/>''', ground=False)

add('armchair', 'ひじ掛けのついた大きないす', f'''
<g>
  <path d="M180 300v-140q0-40 44-40h152q44 0 44 40v140z" class="teal o"/>
  <path d="M212 300v-92q0-16 18-16h140q18 0 18 16v92z" class="tealp o"/>
  <path d="M150 300v-96q0-26 26-26t26 26v96z" class="teald o"/>
  <path d="M398 300v-96q0-26 26-26t26 26v96z" class="teald o"/>
  <path d="M206 254h188v34H206z" class="tealp o"/>
  <g stroke="#5b4a3c" stroke-width="11" stroke-linecap="round" fill="none">
    <path d="M186 300v22M414 300v22"/>
  </g>
</g>
<path d="M130 322h340" class="a"/>''', ground=False)

add('sofa', '三人掛けの長いす', f'''
<g>
  <path d="M120 290v-108q0-30 34-30h292q34 0 34 30v108z" class="coral o"/>
  <path d="M152 290v-72q0-14 16-14h264q16 0 16 14v72z" class="coralp o"/>
  <path d="M96 290v-76q0-22 22-22t22 22v76z" class="corald o"/>
  <path d="M460 290v-76q0-22 22-22t22 22v76z" class="corald o"/>
  <path d="M148 246h304v34H148z" class="coralp o"/>
  <path d="M250 204v42M350 204v42" stroke="{INK}" stroke-width="2.5" fill="none"/>
  <g stroke="#5b4a3c" stroke-width="11" stroke-linecap="round" fill="none">
    <path d="M136 290v22M464 290v22"/>
  </g>
</g>
<path d="M80 312h440" class="a"/>''', ground=False)

add('rug', '板張りの床の一部だけを覆う敷物', f'''
<path d="M60 210h480v110H60z" fill="#dcae72"/>
<g stroke="#b5854f" stroke-width="2.5" fill="none">
  <path d="M60 240h480M60 270h480M60 300h480M180 210v110M300 210v110M420 210v110"/>
</g>
<g transform="translate(300 268)">
  <path d="M-150-44h300v88h-300z" class="violetp o"/>
  <path d="M-126-28h252v56h-252z" fill="none" stroke="{TONES['violet'][2]}" stroke-width="4"/>
  <path d="M-96-12h192v24h-192z" class="violet o"/>
  <g stroke="{TONES['violet'][2]}" stroke-width="4" stroke-linecap="round">
    <path d="M-150-44v-10M-130-44v-10M-110-44v-10M150-44v-10M130-44v-10M110-44v-10"/>
    <path d="M-150 44v10M-130 44v10M-110 44v10M150 44v10M130 44v10M110 44v10"/>
  </g>
</g>''', ground=False)

add('bulb', '電球が一つ、光を放っている', f'''
<g transform="translate(300 200)">
  <path d="M0-110q56 0 56 56 0 30-22 48-12 10-12 24h-44q0-14-12-24-22-18-22-48 0-56 56-56z" class="goldp o"/>
  <path d="M-26 22h52v12h-52zM-24 40h48v12h-48zM-22 58h44v14q0 10-22 10t-22-10z" fill="{MUTED}" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-18-26q10 26 18 34 8-8 18-34" fill="none" stroke="{TONES['gold'][2]}" stroke-width="4" stroke-linecap="round"/>
</g>
<g class="golds" stroke-width="5" stroke-linecap="round">
  <path d="M300 44v-26M186 104l-20-18M414 104l20-18M148 200h-28M452 200h28"/>
</g>''', ground=False)

add('socket', '壁のコンセントに差し込みプラグを近づけている', f'''
<path d="M0 0h600v400H0z" fill="#eef1f4"/>
<g>
  <rect x="150" y="130" width="150" height="150" rx="14" fill="#fffefd" class="o"/>
  <g fill="{INK}">
    <rect x="196" y="176" width="14" height="34" rx="6"/>
    <rect x="240" y="176" width="14" height="34" rx="6"/>
  </g>
  <circle cx="225" cy="238" r="7" fill="{MUTED}"/>
</g>
<g transform="translate(400 205)">
  <rect x="-40" y="-52" width="80" height="104" rx="14" fill="#fffefd" class="o"/>
  <g fill="{MUTED}" stroke="{INK}" stroke-width="2">
    <rect x="-70" y="-34" width="34" height="12" rx="6"/>
    <rect x="-70" y="22" width="34" height="12" rx="6"/>
  </g>
  <path d="M40 0h70" stroke="{INK}" stroke-width="9" fill="none" stroke-linecap="round"/>
  <path d="M110 0q40 0 40 40" stroke="{INK}" stroke-width="9" fill="none" stroke-linecap="round"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M336 205h-24"/></g>''', arrow=True, ground=False)

add('cord', 'とぐろを巻いた電気コードの先にプラグがついている', f'''
<g fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round">
  <path d="M120 250q60-90 130-40t120-20q50-32 96 18"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M120 250q60-90 130-40t120-20q50-32 96 18"/>
</g>
<g transform="translate(112 256)">
  <rect x="-46" y="-26" width="52" height="52" rx="10" fill="#fffefd" class="o"/>
  <g fill="{MUTED}" stroke="{INK}" stroke-width="2">
    <rect x="-74" y="-16" width="30" height="10" rx="5"/>
    <rect x="-74" y="6" width="30" height="10" rx="5"/>
  </g>
</g>
<g transform="translate(470 214)">
  <rect x="-8" y="-30" width="56" height="60" rx="10" class="teal o"/>
  <circle cx="20" cy="0" r="10" class="tealp o"/>
</g>''', ground=False)

add('charger', '充電器を差し込んだスマホの電池が満たされていく', f'''
<g>
  <rect x="200" y="70" width="150" height="250" rx="20" fill="#3b4450" class="o"/>
  <rect x="214" y="92" width="122" height="196" rx="8" fill="#e6eef4" class="o"/>
  <g transform="translate(275 190)">
    <rect x="-38" y="-22" width="72" height="44" rx="6" fill="none" stroke="{INK}" stroke-width="4"/>
    <rect x="34" y="-9" width="9" height="18" rx="3" fill="{INK}"/>
    <rect x="-32" y="-16" width="42" height="32" class="green"/>
    <rect x="10" y="-16" width="18" height="32" fill="#cfe0ec"/>
  </g>
  <path d="M275 320v20" stroke="{INK}" stroke-width="8" fill="none"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round">
  <path d="M275 344q0 30 60 30t60-30q0-40 70-40"/>
</g>
<g transform="translate(478 300)">
  <rect x="-8" y="-28" width="52" height="56" rx="9" fill="#fffefd" class="o"/>
  <g fill="{MUTED}" stroke="{INK}" stroke-width="2">
    <rect x="44" y="-16" width="26" height="10" rx="5"/><rect x="44" y="6" width="26" height="10" rx="5"/>
  </g>
</g>
<path d="M186 122l22-40-6 30h20l-26 44 6-34z" class="gold o"/>''', ground=False)

add('clock', '文字盤に長針と短針のある掛け時計', f'''
<g transform="translate(300 196)">
  <circle r="122" class="tealp o"/>
  <circle r="104" fill="#fffefd" class="o"/>
  <g stroke="{INK}" stroke-width="5" stroke-linecap="round">
    <path d="M0-96v-14"/><path d="M0 96v14"/><path d="M-96 0h-14"/><path d="M96 0h14"/>
  </g>
  <g stroke="{MUTED}" stroke-width="3" stroke-linecap="round">
    <path d="M52-88l6-12"/><path d="M88-52l12-6"/><path d="M88 52l12 6"/><path d="M52 88l6 12"/>
    <path d="M-52-88l-6-12"/><path d="M-88-52l-12-6"/><path d="M-88 52l-12 6"/><path d="M-52 88l-6 12"/>
  </g>
  <path d="M0 0v-62" stroke="{INK}" stroke-width="9" stroke-linecap="round" fill="none"/>
  <path d="M0 0l62 34" stroke="{INK}" stroke-width="7" stroke-linecap="round" fill="none"/>
  <circle r="9" class="coral o"/>
</g>''', ground=False)

add('calendar', '日付のますが並んだ壁掛けカレンダー、一日に丸がついている', f'''
<g>
  <rect x="130" y="80" width="340" height="240" rx="12" fill="#fffefd" class="o"/>
  <path d="M130 92q0-12 12-12h316q12 0 12 12v42H130z" class="coral o"/>
  <g stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none">
    <path d="M196 80V54M404 80V54"/>
  </g>
  <g stroke="{MUTED}" stroke-width="2.5" fill="none">
    <path d="M130 178h340M130 224h340M130 270h340"/>
    <path d="M178 134v186M226 134v186M274 134v186M322 134v186M370 134v186M418 134v186"/>
  </g>
  <g fill="{MUTED}">
    <circle cx="154" cy="156" r="5"/><circle cx="202" cy="156" r="5"/><circle cx="250" cy="156" r="5"/>
    <circle cx="298" cy="156" r="5"/><circle cx="346" cy="156" r="5"/><circle cx="394" cy="156" r="5"/><circle cx="442" cy="156" r="5"/>
    <circle cx="154" cy="202" r="5"/><circle cx="202" cy="202" r="5"/><circle cx="298" cy="202" r="5"/>
    <circle cx="346" cy="202" r="5"/><circle cx="394" cy="202" r="5"/><circle cx="442" cy="202" r="5"/>
    <circle cx="154" cy="248" r="5"/><circle cx="202" cy="248" r="5"/><circle cx="250" cy="248" r="5"/>
    <circle cx="298" cy="248" r="5"/><circle cx="346" cy="248" r="5"/><circle cx="394" cy="248" r="5"/>
  </g>
  <circle cx="250" cy="202" r="17" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>''', ground=False)

add('glue', 'のりのチューブから紙に接着剤を絞り出している', f'''
<g transform="translate(230 190) rotate(28)">
  <path d="M-34 0h68v100q0 24-34 24t-34-24z" class="gold o"/>
  <path d="M-34 0h68v-56q0-14-16-14h-36q-16 0-16 14z" class="goldd o"/>
  <path d="M-14-70h28v-24h-28z" fill="{MUTED}" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-18-94h36v-14h-36z" class="corald o"/>
</g>
<g class="paper"><path d="M300 250h190v90H300z"/></g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="9" stroke-linecap="round">
  <path d="M336 276q30 26 60 0t60 0"/>
</g>
<circle cx="312" cy="248" r="8" class="goldp o"/>
<circle cx="304" cy="222" r="5" class="goldp o"/>''', ground=False)

add('stapler', 'ホチキスが紙の束をとじている', f'''
<g class="paper"><path d="M150 230h250v80H150z"/><path d="M158 222h250v80H158z"/></g>
<g transform="translate(300 200)">
  <path d="M-140 22h250q22 0 22 18t-22 18h-250z" class="teald o"/>
  <path d="M-140-16h240q26 0 26 20t-26 20h-240q-16 0-16-20t16-20z" class="teal o"/>
  <path d="M-140-16v40" stroke="{INK}" stroke-width="3" fill="none"/>
  <circle cx="112" cy="4" r="8" class="tealp o"/>
</g>
<g fill="{MUTED}" stroke="{INK}" stroke-width="2">
  <path d="M186 216h26v6h-26zM186 216v10M212 216v10"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 130v-40"/></g>''', arrow=True, ground=False)

add('hammer', '金づちで板に釘を打ちつけている', f'''
<g transform="translate(300 150) rotate(-18)">
  <path d="M-70-34h96v66h-96z" fill="#3b4450" class="o"/>
  <path d="M-70-34q-34 4-34 34t34 32z" fill="#556070" class="o"/>
  <path d="M26-22h20l26 130h-30z" fill="#8b6437" class="o"/>
  <path d="M46 108h34l14 108h-40z" fill="#a0764a" class="o"/>
</g>
<g>
  <path d="M120 300h360v40H120z" fill="#dcae72" class="o"/>
  <path d="M262 300v-26h12v26z" fill="{MUTED}" stroke="{INK}" stroke-width="2"/>
  <path d="M252 274h32v8h-32z" fill="{INK}"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M226 258l-20-16M302 254l16-20M196 288l-24-4"/>
</g>''', ground=False)

add('screwdriver', 'ねじ回しがねじの頭に当てられている', f'''
<g transform="translate(280 200) rotate(34)">
  <path d="M-30-30h60v120q0 22-30 22t-30-22z" class="coral o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="4">
    <path d="M-30 10h60M-30 40h60M-30 70h60"/>
  </g>
  <path d="M-12-30h24v-96h-24z" fill="{MUTED}" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-16-126h32v-16h-32z" fill="#8f9aa6" stroke="{INK}" stroke-width="2.5"/>
</g>
<g>
  <path d="M120 290h360v40H120z" fill="#dcae72" class="o"/>
  <circle cx="360" cy="308" r="16" fill="{MUTED}" stroke="{INK}" stroke-width="2.5"/>
  <path d="M348 308h24" stroke="{INK}" stroke-width="4" fill="none"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round" marker-end="url(#ar)">
  <path d="M404 150a54 54 0 0 1-30 46"/>
</g>''', arrow=True, ground=False)

add('drill', '電動ドリルが壁に穴をあけている', f'''
<path d="M340 60h260v300H340z" fill="#e8e2d6"/>
<path d="M340 60v300" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(230 190)">
  <path d="M-90-40h130q26 0 26 34t-26 34h-130q-24 0-24-34t24-34z" class="teal o"/>
  <path d="M-70 28h56l14 96q2 16-16 16h-52q-18 0-16-16z" class="teald o"/>
  <path d="M-62 40h40v20h-40z" class="tealp o"/>
  <path d="M66-14h34v28H66z" fill="#8f9aa6" class="o"/>
  <path d="M100-6h48v12h-48z" fill="{MUTED}" stroke="{INK}" stroke-width="2.5"/>
  <g fill="none" stroke="{INK}" stroke-width="2.5"><path d="M104 6q10-6 20 0t20 0"/></g>
</g>
<circle cx="384" cy="190" r="11" fill="{INK}"/>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-linecap="round">
  <path d="M398 172l18-14M402 190h24M398 208l18 14"/>
</g>''', ground=False)

add('saw', 'のこぎりが丸太を切っている', f'''
<g>
  <path d="M110 260q0-56 56-56t56 56-56 56-56-56z" fill="#b5854f" class="o"/>
  <path d="M166 204h230v112H166z" fill="#c99a63" class="o"/>
  <ellipse cx="396" cy="260" rx="30" ry="56" fill="#b5854f" class="o"/>
  <g fill="none" stroke="#8b6437" stroke-width="3">
    <ellipse cx="166" cy="260" rx="26" ry="40"/><ellipse cx="166" cy="260" rx="13" ry="20"/>
  </g>
</g>
<g transform="translate(300 170) rotate(-8)">
  <path d="M-190 0h300v22h-300z" fill="#cfd6dd" class="o"/>
  <path d="M-190 22l14 20 14-20 14 20 14-20 14 20 14-20 14 20 14-20 14 20 14-20 14 20 14-20 14 20 14-20 14 20 14-20 14 20 14-20 14 20 14-20 14 20 14-20" fill="#cfd6dd" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M110-6h44q22 0 22 20t-22 20h-44z" fill="#8b6437" class="o"/>
</g>''', ground=False)

add('wrench', 'スパナがボルトの頭をくわえて締めている', f'''
<g transform="translate(300 200) rotate(-24)">
  <path d="M-150-16h190v32h-190z" fill="#8f9aa6" class="o"/>
  <path d="M-150-16q-40 0-40 32t40 32h30v-32h-30v-32z" fill="#8f9aa6" class="o"/>
  <path d="M40-46q46 0 46 46t-46 46h-6q-30 0-30-24h34q16 0 16-22t-16-22H4q0-24 30-24z" fill="#8f9aa6" class="o"/>
</g>
<g transform="translate(346 132)">
  <path d="M-30-17l30-17 30 17v34l-30 17-30-17z" fill="{MUTED}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>
  <circle r="13" fill="#6f7b88" stroke="{INK}" stroke-width="2.5"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round" marker-end="url(#ar)">
  <path d="M412 118a70 70 0 0 1 8 60"/>
</g>''', arrow=True, ground=False)

add('pliers', '二枚の柄が交差したペンチ', f'''
<g transform="translate(300 200)">
  <g stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
    <path d="M-14 6L-140 96q-16 12-6 26t28 6L20 30z" class="coral"/>
    <path d="M14 6L140 96q16 12 6 26t-28 6L-20 30z" class="corald"/>
    <path d="M-12 0l-72-96q-8-12 4-20t22 2L6-14z" fill="#8f9aa6"/>
    <path d="M12 0l72-96q8-12-4-20t-22 2L-6-14z" fill="#cfd6dd"/>
  </g>
  <circle r="12" fill="#6f7b88" stroke="{INK}" stroke-width="2.5"/>
</g>''', ground=False)

add('shovel', 'シャベルが土をすくい上げている', f'''
<path d="M0 280h600v120H0z" fill="#a0764a"/>
<path d="M0 280h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(320 210) rotate(24)">
  <path d="M-16-160h32v150h-32z" fill="#8b6437" class="o"/>
  <path d="M-26-160h52v-22q0-14-26-14t-26 14z" fill="none" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>
  <path d="M-46-10h92v60q0 40-46 40t-46-40z" fill="#8f9aa6" class="o"/>
</g>
<g>
  <path d="M392 224q34-14 56 4t-4 40-70-4z" fill="#8b6437" class="o"/>
</g>''', ground=False)

add('rake', 'くまでが落ち葉をかき集めている', f'''
<path d="M0 290h600v110H0z" fill="#dfe8d8"/>
<path d="M0 290h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 180) rotate(20)">
  <path d="M-10-150h20v190h-20z" fill="#8b6437" class="o"/>
  <path d="M-70 40h140v18h-140z" fill="#8f9aa6" class="o"/>
  <g stroke="{INK}" stroke-width="2.5" fill="#8f9aa6">
    <path d="M-66 58l-14 40h12l16-40zM-40 58l-8 42h12l10-42zM-14 58l-3 44h12l3-44zM14 58l3 44h12l-3-44zM40 58l8 42h12l-10-42zM66 58l14 40h-12l-16-40z"/>
  </g>
</g>
<g stroke="{INK}" stroke-width="2.5">
  <path d="M180 290q10-16 26-8t-4 20-30-4z" class="gold"/>
  <path d="M136 296q8-14 22-6t-4 18-26-4z" class="coralp"/>
  <path d="M226 300q9-14 22-6t-4 16-24-2z" class="corald"/>
</g>''', ground=False)

add('hose', 'とぐろを巻いたホースの先から水が出ている', f'''
<g fill="none" stroke="{TONES['green'][2]}" stroke-width="18" stroke-linecap="round">
  <path d="M120 300q-40-60 20-80t130 10q60 20 90-20t100 10"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round">
  <path d="M120 300q-40-60 20-80t130 10q60 20 90-20t100 10"/>
</g>
<g transform="translate(468 226)">
  <path d="M-8-12h44v24h-44z" fill="{MUTED}" stroke="{INK}" stroke-width="2.5"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M512 224q28 4 44 26M512 232q26 12 34 34M512 240q22 18 22 42"/>
</g>
{drop(556, 300, 1.2)}
{drop(534, 318, 1.0)}''', ground=False)

add('bucket', '取っ手つきのバケツに水が入っている', f'''
<g transform="translate(300 220)">
  <path d="M-96-70h192l-26 156q-2 20-70 20t-70-20z" class="blue o"/>
  <ellipse cy="-70" rx="96" ry="26" class="bluep o"/>
  <path d="M-84-36q30 14 84 14t84-14" fill="none" stroke="{TONES['blue'][2]}" stroke-width="5"/>
  <path d="M-96-76q0-70 96-70t96 70" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
</g>
<path d="M170 310h260" class="a"/>''', ground=False)

add('broom', 'ほうきが床のごみを掃いている', f'''
<g transform="translate(320 200) rotate(18)">
  <path d="M-11-160h22v190h-22z" fill="#a0764a" class="o"/>
  <path d="M-38 30h76v34h-76z" fill="#8b6437" class="o"/>
  <path d="M-40 64h80l16 84q2 12-14 12h-84q-16 0-14-12z" class="gold o"/>
  <g stroke="{TONES['gold'][2]}" stroke-width="3" fill="none">
    <path d="M-26 64l-10 96M-6 64l-4 96M14 64l4 96M34 64l10 96"/>
  </g>
</g>
<path d="M80 330h440" class="a"/>
<g fill="{MUTED}"><circle cx="176" cy="320" r="6"/><circle cx="148" cy="326" r="4"/><circle cx="200" cy="326" r="4"/></g>''', ground=False)

add('mop', 'モップが床の水をふいている', f'''
<g transform="translate(300 190) rotate(-12)">
  <path d="M-11-160h22v180h-22z" fill="#8f9aa6" class="o"/>
  <path d="M-30 20h60v22h-60z" class="teald o"/>
  <g stroke="{TONES['teal'][1]}" stroke-width="9" stroke-linecap="round" fill="none">
    <path d="M-26 42q-14 60-30 92M-10 42q-8 62-14 96M6 42q4 62 6 96M22 42q14 58 30 92"/>
  </g>
</g>
<path d="M80 330h440" class="a"/>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M172 316q26-10 46 0M404 316q26-10 46 0"/>
</g>''', ground=False)

add('sponge', '泡の立ったスポンジで面をこすっている', f'''
<g transform="translate(300 200)">
  <path d="M-110-56h220v112h-220z" rx="14" class="goldp o"/>
  <path d="M-110-56h220v34h-220z" class="gold o"/>
  <g fill="{TONES['gold'][2]}" opacity="0.6">
    <circle cx="-70" cy="10" r="9"/><circle cx="-30" cy="28" r="7"/><circle cx="6" cy="4" r="10"/>
    <circle cx="46" cy="30" r="7"/><circle cx="80" cy="6" r="9"/><circle cx="-50" cy="-6" r="6"/>
    <circle cx="26" cy="34" r="5"/><circle cx="66" cy="-8" r="6"/>
  </g>
</g>
<g fill="#fffefd" stroke="{INK}" stroke-width="2.5">
  <circle cx="200" cy="112" r="20"/><circle cx="246" cy="88" r="14"/><circle cx="290" cy="104" r="24"/>
  <circle cx="342" cy="84" r="16"/><circle cx="386" cy="106" r="20"/>
</g>
<path d="M140 300h320" class="a"/>''', ground=False)

add('razor', '泡のついた顔にかみそりを当てている', f'''
{face(220, 200, 96, 'flat')}
<g fill="#fffefd" stroke="{INK}" stroke-width="2.5">
  <circle cx="188" cy="256" r="26"/><circle cx="232" cy="266" r="22"/><circle cx="272" cy="248" r="18"/>
  <circle cx="160" cy="236" r="18"/>
</g>
<g transform="translate(376 236) rotate(-30)">
  <path d="M-14 0h28v110q0 16-14 16t-14-16z" class="violet o"/>
  <path d="M-26-34h52v34h-52z" fill="#cfd6dd" class="o"/>
  <path d="M-26-34h52v-8h-52z" fill="{INK}"/>
  <g stroke="{INK}" stroke-width="2" fill="none"><path d="M-14-26v20M0-26v20M14-26v20"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M348 224l-40 12"/></g>''', arrow=True, ground=False)

add('comb', '歯の並んだくしが髪をとかしている', f'''
<g transform="translate(320 190) rotate(14)">
  <path d="M-150-30h300v34h-300z" class="teald o"/>
  <g fill="{TONES['teal'][0]}" stroke="{INK}" stroke-width="2">
''' + ''.join(f'<rect x="{-146+i*15}" y="4" width="8" height="56" rx="4"/>' for i in range(20)) + f'''
  </g>
</g>
<g fill="none" stroke="{HAIR}" stroke-width="7" stroke-linecap="round">
  <path d="M150 300q30-70 90-96M186 312q26-72 86-100M222 320q24-70 84-100"/>
</g>''', ground=False)

add('scissors', '二枚の刃が交差したはさみが紙を切っている', f'''
<g class="paper"><path d="M60 170h240v130H60z"/></g>
<path d="M180 170v130" stroke="{MUTED}" stroke-width="2.5" stroke-dasharray="8 8" fill="none"/>
<g transform="translate(300 210)">
  <g stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
    <path d="M-8-6L-130-52q-14-6-8-18t22-6L14-24z" fill="#cfd6dd"/>
    <path d="M-8 6L-130 52q-14 6-8 18t22 6L14 24z" fill="#8f9aa6"/>
    <path d="M10-16l106-38q16-6 24 8t-8 22L26 6z" fill="none" stroke="none"/>
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="14" stroke-linecap="round">
    <path d="M16-14q60-24 84 4t-18 44"/>
    <path d="M16 14q60 24 84-4t-18-44"/>
  </g>
  <circle r="10" fill="#6f7b88" stroke="{INK}" stroke-width="2.5"/>
</g>''', ground=False)

add('zipper', '上着のファスナーが半分だけ閉まっている', f'''
<g>
  <path d="M170 60h120l-14 250H186z" class="blue o"/>
  <path d="M430 60H310l14 250h90z" class="blue o"/>
  <path d="M290 60h20l14 250h-48z" class="blued o"/>
</g>
<g>
  <g fill="{MUTED}" stroke="{INK}" stroke-width="2">
''' + ''.join(f'<rect x="{284 - (0 if i%2 else 12)}" y="{72+i*14}" width="12" height="8" rx="2"/>' for i in range(9)) + f'''
  </g>
  <g fill="{MUTED}" stroke="{INK}" stroke-width="2">
''' + ''.join(f'<rect x="{262}" y="{224+i*14}" width="12" height="8" rx="2"/><rect x="{326}" y="{224+i*14}" width="12" height="8" rx="2"/>' for i in range(6)) + f'''
  </g>
</g>
<g transform="translate(300 206)">
  <path d="M-24-14h48v28h-48z" fill="#8f9aa6" class="o"/>
  <path d="M-8 14h16v34q0 12-8 12t-8-12z" fill="#8f9aa6" class="o"/>
</g>''', ground=False)

add('sleeve', 'シャツのそでを腕まくりしている', f'''
<g>
  <path d="M180 90h240l30 70-56 24-18-30v146H224V154l-18 30-56-24z" class="tealp o"/>
  <path d="M250 90h100l-50 44z" fill="#fffefd" class="o"/>
</g>
<g>
  <path d="M420 160l40 16-14 44-44-18z" class="teal o"/>
  <path d="M402 202l44 18-8 26-46-20z" class="teald o"/>
  <path d="M392 226l46 20q-8 34-46 22z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 250l30-46"/></g>''', arrow=True, ground=False)

add('collar', 'シャツのえりが首まわりに立っている', f'''
<g>
  <path d="M170 130h260v190H170z" class="tealp o"/>
  <path d="M300 130v190" stroke="{MUTED}" stroke-width="2.5" fill="none"/>
  <g fill="{MUTED}"><circle cx="300" cy="190" r="7"/><circle cx="300" cy="240" r="7"/><circle cx="300" cy="290" r="7"/></g>
</g>
<g>
  <path d="M230 130q-4-52 26-64l44 58z" fill="#fffefd" class="o"/>
  <path d="M370 130q4-52-26-64l-44 58z" fill="#fffefd" class="o"/>
  <path d="M256 66q22-16 44-16t44 16" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M456 96l-70 8"/></g>''', arrow=True, ground=False)

add('apron', '首と腰でひもを結んだエプロン', f'''
<g>
  <path d="M240 110h120v56h-120z" class="coralp o"/>
  <path d="M232 166h136q34 0 34 40v100q0 40-34 40H232q-34 0-34-40V206q0-40 34-40z" class="coral o"/>
  <path d="M254 220h92v66h-92z" class="coralp o"/>
  <path d="M300 220v66" stroke="{TONES['coral'][2]}" stroke-width="3" fill="none"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round">
  <path d="M244 110q-30-46 56-46t56 46"/>
  <path d="M200 200l-64 20M400 200l64 20"/>
</g>''', ground=False)

add('scarf', '首に巻かれたマフラーが垂れている', f'''
{person(300, 340, 1.1, 1, 'blue', 'blue', 'stand', 'bob', 'smile')}
<g>
  <path d="M262 226q38 22 76 0 14 10 6 24-44 22-88 0-8-14 6-24z" class="coral o"/>
  <path d="M266 250l-12 96h34l6-88z" class="corald o"/>
  <path d="M334 250l12 96h-34l-6-88z" class="coral o"/>
  <g stroke="{TONES['coral'][2]}" stroke-width="4" fill="none">
    <path d="M258 288h32M254 316h32M312 288h32M316 316h32"/>
  </g>
</g>''', ground=True)

add('sandal', '甲があいた夏のサンダル', f'''
<g transform="translate(300 220)">
  <path d="M-140 30q0-40 40-44l180-16q60-6 60 26t-60 34l-180 12q-40 2-40-12z" fill="#a0764a" class="o"/>
  <path d="M-140 42q0-14 40-16l180-12q60-4 60 12t-60 18l-180 12q-40 2-40-14z" fill="#8b6437" class="o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="16" stroke-linecap="round">
    <path d="M-70 0q40-34 88-6"/>
    <path d="M40-14q40-28 78 2"/>
  </g>
</g>
<path d="M120 290h360" class="a"/>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
