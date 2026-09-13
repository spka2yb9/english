# -*- coding: utf-8 -*-
"""第118回。生き物。横向きの輪郭＋その種だけの特徴（角・耳・しま・くちばし）で見分けられるようにする。"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib import *

W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))
GR = '#dfe8d8'
def grass(y=306):
    return (f'<path d="M0 {y}h600v{400-y}H0z" fill="{GR}"/><path d="M0 {y}h600" stroke="{INK}" stroke-width="2.5" fill="none"/>')

# --- 虫 ---------------------------------------------------------------------
add('snail', '渦を巻いた殻を背負ったカタツムリが葉の上をはっている', f'''
{grass(290)}
<g transform="translate(300 250)">
  <path d="M-130 36q-20-30 10-38l90-6q20-2 22 14t-18 20l-84 12q-14 2-20-2z" fill="#e8c391" class="o"/>
  <path d="M-130 36q-24 4-24 14t24 10h30v-24z" fill="#e8c391" class="o"/>
  <g stroke="#c9a464" stroke-width="4" stroke-linecap="round" fill="none">
    <path d="M-140 4l-16-40M-124 2l4-42"/>
  </g>
  <circle cx="-156" cy="-40" r="7" fill="{INK}"/><circle cx="-120" cy="-42" r="7" fill="{INK}"/>
  <g transform="translate(30 -6)">
    <path d="M0-58q58 0 58 56T0 54q-58 0-58-56 0-32 30-32t30 32q0 24-22 24" fill="#c99a63" stroke="{INK}" stroke-width="3"/>
  </g>
</g>''', ground=False)

add('beetle', '硬い前ばねが背中で二つに分かれた甲虫', f'''
{grass(300)}
<g transform="translate(300 210)">
  <ellipse rx="96" ry="76" fill="#3b4450" class="o"/>
  <path d="M0-76v152" stroke="{INK}" stroke-width="4" fill="none"/>
  <ellipse cy="-84" rx="46" ry="30" fill="#2c333d" class="o"/>
  <g stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none">
    <path d="M-22-104l-32-30M22-104l32-30"/>
    <path d="M-90-38l-56-24M-96 6l-62 6M-88 46l-52 34M90-38l56-24M96 6l62 6M88 46l52 34"/>
  </g>
  <g fill="#556070"><ellipse cx="-40" cy="-20" rx="20" ry="30"/><ellipse cx="40" cy="-20" rx="20" ry="30"/></g>
</g>''', ground=False)

add('ant', '三つの節に分かれた体と六本の脚を持つアリ', f'''
{grass(304)}
<g transform="translate(300 230)">
  <ellipse cx="86" rx="56" ry="42" fill="#5b3a2a" class="o"/>
  <ellipse rx="30" ry="26" fill="#5b3a2a" class="o"/>
  <circle cx="-58" r="34" fill="#5b3a2a" class="o"/>
  <circle cx="-70" cy="-8" r="6" fill="{INK}"/>
  <g stroke="#5b3a2a" stroke-width="5" stroke-linecap="round" fill="none">
    <path d="M-78-22l-26-36M-62-30l-6-42"/>
    <path d="M-10 22l-30 46M6 24l-4 50M20 20l32 44"/>
    <path d="M-10-22l-30-42M6-24l-4-46M20-20l32-40"/>
  </g>
</g>''', ground=False)

add('wasp', '腰がくびれ、黄と黒のしま模様を持つハチ', f'''
<g transform="translate(300 200) rotate(10)">
  <ellipse cx="70" rx="66" ry="44" class="gold o"/>
  <g fill="{INK}">
    <path d="M28-38q14 76 0 76zM66-44q14 88 0 88zM104-38q14 76 0 76z"/>
  </g>
  <path d="M136 0l30 14-30 10z" fill="{INK}"/>
  <path d="M0-14h20v28H0z" fill="{INK}"/>
  <circle cx="-40" r="34" fill="{INK}"/>
  <circle cx="-52" cy="-8" r="7" fill="#fffefd"/>
  <g stroke="{INK}" stroke-width="4" stroke-linecap="round" fill="none">
    <path d="M-58-26l-24-36M-42-32l-8-42"/>
    <path d="M20 40l-16 44M56 44l4 48M96 40l24 42"/>
  </g>
  <g fill="#fffefd" stroke="{INK}" stroke-width="2.5" opacity="0.85">
    <ellipse cx="46" cy="-52" rx="66" ry="26" transform="rotate(-18 46 -52)"/>
    <ellipse cx="86" cy="-46" rx="52" ry="20" transform="rotate(-8 86 -46)"/>
  </g>
</g>''', ground=False)

add('moth', 'ずんぐりした胴と地味な色の羽を持つガが明かりのそばにいる', f'''
<g transform="translate(300 220)">
  <g fill="#b5a48c" stroke="{INK}" stroke-width="2.5">
    <path d="M-14-30q-110-56-134 6-22 58 46 74 60 14 88-30z"/>
    <path d="M14-30q110-56 134 6 22 58-46 74-60 14-88-30z"/>
  </g>
  <g fill="#8f7d64">
    <ellipse cx="-84" cy="4" rx="26" ry="18"/><ellipse cx="84" cy="4" rx="26" ry="18"/>
  </g>
  <ellipse ry="52" rx="18" fill="#6b5b46" class="o"/>
  <circle cy="-56" r="18" fill="#6b5b46" class="o"/>
  <g stroke="#6b5b46" stroke-width="4" stroke-linecap="round" fill="none">
    <path d="M-8-70q-24-16-40-6M8-70q24-16 40-6"/>
  </g>
</g>
<g transform="translate(470 120)">
  <path d="M0-40q30 0 30 30 0 16-12 26-6 6-6 14h-24q0-8-6-14-12-10-12-26 0-30 30-30z" class="goldp o"/>
  <path d="M-14 30h28v10h-28z" fill="{MUTED}"/>
</g>
<g class="golds" stroke-width="4"><path d="M470 60v-16M420 96l-14-12M520 96l14-12"/></g>''', ground=False)

add('butterfly', '大きな四枚の羽に模様のあるチョウ', f'''
<g transform="translate(300 210)">
  <g class="violet o">
    <path d="M-12-20q-100-90-140-20-36 62 40 82 66 16 100-30z"/>
    <path d="M12-20q100-90 140-20 36 62-40 82-66 16-100-30z"/>
  </g>
  <g class="violetp o">
    <path d="M-12 20q-70 20-76 62-4 34 34 32 44-2 54-52z"/>
    <path d="M12 20q70 20 76 62 4 34-34 32-44-2-54-52z"/>
  </g>
  <g fill="{TONES['gold'][1]}">
    <circle cx="-76" cy="-30" r="16"/><circle cx="76" cy="-30" r="16"/>
    <circle cx="-44" cy="66" r="10"/><circle cx="44" cy="66" r="10"/>
  </g>
  <ellipse ry="72" rx="13" fill="{INK}"/>
  <circle cy="-78" r="15" fill="{INK}"/>
  <g stroke="{INK}" stroke-width="4" stroke-linecap="round" fill="none">
    <path d="M-6-90q-22-24-40-20M6-90q22-24 40-20"/>
  </g>
</g>''', ground=False)

add('mosquito', '細長い脚と針のような口を持つ蚊が腕にとまっている', f'''
<g transform="translate(300 300) rotate(-8)">
  <path d="M-220 30q-14-30 18-40l340-30q36-4 40 22t-34 30l-340 32q-16 2-24-14z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g transform="translate(300 190) rotate(14)">
  <ellipse cx="34" rx="52" ry="17" fill="#5b4a3c" class="o"/>
  <circle cx="-30" r="20" fill="#5b4a3c" class="o"/>
  <circle cx="-38" cy="-6" r="6" fill="{INK}"/>
  <path d="M-46 8l-56 46" stroke="#5b4a3c" stroke-width="5" stroke-linecap="round" fill="none"/>
  <g fill="#fffefd" stroke="{INK}" stroke-width="2" opacity="0.8">
    <ellipse cx="24" cy="-24" rx="56" ry="14" transform="rotate(-14 24 -24)"/>
    <ellipse cx="40" cy="-16" rx="48" ry="11" transform="rotate(-4 40 -16)"/>
  </g>
  <g stroke="#5b4a3c" stroke-width="3.5" stroke-linecap="round" fill="none">
    <path d="M-4 14l-30 60M22 16l-4 66M50 12l34 62M-4-14l-30-46M22-16l-4-52M50-12l34-46"/>
  </g>
</g>''', ground=False)

add('grasshopper', '後ろ脚が大きく曲がったバッタが草にとまっている', f'''
{grass(300)}
<g transform="translate(300 230)">
  <path d="M-70-16q0-34 70-34t80 34q6 34-70 40t-80-40z" class="green o"/>
  <path d="M-70-16q-40 4-40 20t40 20z" class="green o"/>
  <circle cx="-92" cy="-2" r="6" fill="{INK}"/>
  <g stroke="{TONES['green'][2]}" stroke-width="4" stroke-linecap="round" fill="none">
    <path d="M-100-16l-40-30M-96-8l-46-14"/>
  </g>
  <path d="M40 20q46-16 40-70-2-22-26-16-16 4-14 26 2 30-24 40z" class="greend o"/>
  <path d="M64 22l50 56" stroke="{TONES['green'][2]}" stroke-width="7" stroke-linecap="round" fill="none"/>
  <g stroke="{TONES['green'][2]}" stroke-width="4.5" stroke-linecap="round" fill="none">
    <path d="M-34 22l-24 52M-2 24l-6 56"/>
  </g>
  <path d="M-40-34q80-24 130 8" fill="none" stroke="{TONES['green'][2]}" stroke-width="4"/>
</g>''', ground=False)

add('caterpillar', '節がつながった毛のあるイモムシが葉を食べている', f'''
<g transform="translate(300 230)">
  <path d="M170-40q60-40 96 10-52 40-96-10z" class="greenp o"/>
  <path d="M170-40q-40 34-4 66" fill="none" stroke="{TONES['green'][2]}" stroke-width="4"/>
  <g class="green o">
''' + ''.join(f'<circle cx="{-150+i*38}" cy="{0 if i%2 else -10}" r="30"/>' for i in range(9)) + f'''
  </g>
  <circle cx="154" cy="-10" r="34" class="greend o"/>
  <circle cx="166" cy="-20" r="7" fill="{INK}"/>
  <g stroke="{TONES['green'][2]}" stroke-width="3.5" stroke-linecap="round" fill="none">
''' + ''.join(f'<path d="M{-150+i*38} {(-30 if i%2 else -40)}v-16"/>' for i in range(9)) + f'''
  </g>
</g>
<path d="M110 274h380" class="a"/>''', ground=False)

# --- 鳥 ---------------------------------------------------------------------
def bird(x, y, s, body, head, beak, extra=''):
    return (f'<g transform="translate({x} {y}) scale({s})">{body}{head}{beak}{extra}</g>')

add('sparrow', '小さくて茶色い、ずんぐりしたスズメが枝にとまっている', f'''
<path d="M120 300h360" stroke="#8b6437" stroke-width="12" stroke-linecap="round" fill="none"/>
<g transform="translate(300 240)">
  <ellipse rx="74" ry="60" fill="#a8825a" class="o"/>
  <path d="M20-20q60-16 84 30-56 26-84-30z" fill="#8b6437" class="o"/>
  <path d="M64 30l70 24-70 16z" fill="#8b6437" class="o"/>
  <circle cx="-56" cy="-42" r="34" fill="#c19a6e" class="o"/>
  <circle cx="-68" cy="-48" r="6" fill="{INK}"/>
  <path d="M-88-42l-26 8 26 10z" fill="{TONES['gold'][2]}" class="o"/>
  <g stroke="{TONES['gold'][2]}" stroke-width="5" stroke-linecap="round" fill="none">
    <path d="M-20 58v20M14 58v20"/>
  </g>
</g>''', ground=False)

add('pigeon', '灰色のハトが地面で餌をついばんでいる', f'''
{grass(300)}
<g transform="translate(300 234)">
  <ellipse rx="86" ry="62" fill="#8f9aa6" class="o"/>
  <path d="M16-20q66-14 90 34-60 28-90-34z" fill="#6f7b88" class="o"/>
  <path d="M70 34l76 22-76 20z" fill="#6f7b88" class="o"/>
  <circle cx="-66" cy="-46" r="34" fill="#a6b0bb" class="o"/>
  <path d="M-72-70q22-14 34 4-16 14-34-4z" class="violetp"/>
  <circle cx="-80" cy="-50" r="6" fill="{INK}"/>
  <path d="M-98-44l-24 8 24 8z" fill="{TONES['coral'][2]}" class="o"/>
  <g stroke="{TONES['coral'][2]}" stroke-width="6" stroke-linecap="round" fill="none">
    <path d="M-24 60v14M16 60v14"/>
  </g>
</g>''', ground=False)

add('crow', '真っ黒なカラスが電線にとまって鳴いている', f'''
<path d="M0 140h600" stroke="{INK}" stroke-width="4" fill="none"/>
<g transform="translate(300 210)">
  <ellipse rx="88" ry="60" fill="{INK}"/>
  <path d="M20-24q70-16 96 34-64 30-96-34z" fill="#1e2731"/>
  <path d="M76 30l88 30-88 22z" fill="{INK}"/>
  <circle cx="-70" cy="-48" r="36" fill="{INK}"/>
  <circle cx="-82" cy="-54" r="7" fill="#fffefd"/>
  <circle cx="-82" cy="-54" r="4" fill="{INK}"/>
  <path d="M-104-48l-42 10 42 12z" fill="#3b4450" class="o"/>
  <g stroke="{INK}" stroke-width="6" stroke-linecap="round" fill="none">
    <path d="M-26 58v14M16 58v14"/>
  </g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M144 148q-16-10-14-24M112 168q-20-8-20-24"/>
</g>''', ground=False)

add('eagle', 'かぎ形のくちばしと大きな翼を持つワシ', f'''
<g transform="translate(300 200)">
  <g fill="#7a5b3c" stroke="{INK}" stroke-width="2.5">
    <path d="M-30-20q-120-70-200 10 70 60 200 26z"/>
    <path d="M30-20q120-70 200 10-70 60-200 26z"/>
  </g>
  <g fill="#5b4029">
    <path d="M-120-16q-40 24-70 34M-90-4q-36 24-64 32M120-16q40 24 70 34M90-4q36 24 64 32" stroke="#5b4029" stroke-width="6" fill="none" stroke-linecap="round"/>
  </g>
  <ellipse ry="70" rx="42" fill="#7a5b3c" class="o"/>
  <circle cy="-74" r="36" fill="#fdf8ec" class="o"/>
  <circle cx="-14" cy="-82" r="7" fill="{INK}"/>
  <path d="M-34-72q-26 4-24 16 20 8 30-6z" class="gold o"/>
  <g stroke="{TONES['gold'][2]}" stroke-width="6" stroke-linecap="round" fill="none">
    <path d="M-20 66v22M20 66v22M-34 88h28M6 88h28"/>
  </g>
</g>''', ground=False)

add('owl', '大きな丸い目と耳のような羽角を持つフクロウ', f'''
<path d="M120 300h360" stroke="#8b6437" stroke-width="14" stroke-linecap="round" fill="none"/>
<g transform="translate(300 200)">
  <path d="M0-96q86 0 86 96t-86 100q-86 0-86-100t86-96z" fill="#a8825a" class="o"/>
  <path d="M-62-70q-16-40 8-46 20 14 26 40zM62-70q16-40-8-46-20 14-26 40z" fill="#8b6437" class="o"/>
  <g fill="#fdf8ec" stroke="{INK}" stroke-width="2.5">
    <circle cx="-34" cy="-30" r="34"/><circle cx="34" cy="-30" r="34"/>
  </g>
  <circle cx="-34" cy="-30" r="17" fill="{INK}"/><circle cx="34" cy="-30" r="17" fill="{INK}"/>
  <circle cx="-28" cy="-36" r="6" fill="#fffefd"/><circle cx="40" cy="-36" r="6" fill="#fffefd"/>
  <path d="M0-6l-14 22h28z" class="gold o"/>
  <g fill="#c19a6e">
    <path d="M-50 30q50-16 100 0-50 20-100 0zM-44 62q44-14 88 0-44 18-88 0z"/>
  </g>
  <g stroke="{TONES['gold'][2]}" stroke-width="6" stroke-linecap="round" fill="none">
    <path d="M-24 98v14M24 98v14"/>
  </g>
</g>''', ground=False)

add('swan', '首が長くS字に曲がった白いハクチョウが水に浮かんでいる', f'''
<path d="M0 280h600v120H0z" fill="#cfe0ec"/>
<g fill="none" stroke="#a8c4da" stroke-width="4">
  <path d="M60 320h120M300 336h140M120 360h180M400 300h120"/>
</g>
<g transform="translate(300 250)">
  <path d="M-140 30q-20-70 60-84 90-16 160 20 40 20 20 44-40 24-140 24-80 0-100-4z" fill="#fffefd" class="o"/>
  <path d="M-46-52q30-42 0-70-30-28-70-4-30 18-16 44" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-40-50q26-40-2-66-26-24-62-2-26 16-14 38 14-24 40-12 26 12 14 42z" fill="#fffefd" class="o"/>
  <circle cx="-122" cy="-108" r="6" fill="{INK}"/>
  <path d="M-136-102l-30 8 30 10z" class="gold o"/>
  <path d="M-138-108q-8-6 0-10" stroke="{INK}" stroke-width="3" fill="none"/>
</g>''', ground=False)

add('duck', '平たいくちばしと水かきを持つカモが泳いでいる', f'''
<path d="M0 288h600v112H0z" fill="#cfe0ec"/>
<g fill="none" stroke="#a8c4da" stroke-width="4">
  <path d="M60 324h120M320 344h140M140 366h160"/>
</g>
<g transform="translate(300 250)">
  <ellipse rx="110" ry="52" fill="#fdf8ec" class="o"/>
  <path d="M40-20q64-14 92 26-58 26-92-26z" fill="#e0d6c0" class="o"/>
  <path d="M-110 0q-40-6-44-30 30-14 52 4z" fill="#e0d6c0" class="o"/>
  <path d="M-70-26q0-46 42-46t42 46z" fill="#2f6b52" class="o"/>
  <circle cx="-46" cy="-52" r="6" fill="{INK}"/>
  <path d="M-70-40q-40 0-40 14t40 8z" class="gold o"/>
  <path d="M-104-30q10 6 0 10" stroke="{TONES['gold'][2]}" stroke-width="3" fill="none"/>
</g>''', ground=False)

add('goose', 'カモより首が長く体の大きいガンが草地を歩いている', f'''
{grass(300)}
<g transform="translate(300 230)">
  <ellipse cx="20" rx="116" ry="60" fill="#e8e0cf" class="o"/>
  <path d="M60-22q70-14 100 30-64 28-100-30z" fill="#c9bfa8" class="o"/>
  <path d="M-96-16q-16-70 20-100 20-16 40 2-30 24-24 60 4 24 20 40z" fill="#e8e0cf" class="o"/>
  <ellipse cx="-72" cy="-118" rx="34" ry="26" fill="#e8e0cf" class="o"/>
  <circle cx="-84" cy="-124" r="6" fill="{INK}"/>
  <path d="M-104-118l-34 8 34 12z" class="gold o"/>
  <g stroke="{TONES['gold'][2]}" stroke-width="7" stroke-linecap="round" fill="none">
    <path d="M-10 58v18M40 58v18"/>
  </g>
  <g fill="{TONES['gold'][1]}" stroke="{INK}" stroke-width="2">
    <path d="M-28 76h36l-8 12h-20z"/><path d="M22 76h36l-8 12h-20z"/>
  </g>
</g>''', ground=False)

add('rooster', 'とさかと長い尾を持つおんどりが朝に鳴いている', f'''
{grass(304)}
<g transform="translate(300 220)">
  <ellipse cx="10" rx="86" ry="66" fill="#b45f4f" class="o"/>
  <g class="coral o">
    <path d="M78 10q60-34 96-96 20 66-34 116-30 28-62 20z"/>
    <path d="M70 30q60-16 100-66 4 60-52 90-30 16-48-24z"/>
  </g>
  <path d="M-56-40q0-52 40-52t40 52z" fill="#b45f4f" class="o"/>
  <circle cx="-40" cy="-66" r="7" fill="{INK}"/>
  <path d="M-64-56l-34 12 34 12z" class="gold o"/>
  <g class="coral o">
    <path d="M-42-92q-6-26 12-26 4 14 14 6 6 16 20 8 4 22-18 22z"/>
    <path d="M-38-30q-14 24 4 30 20-6 8-30z"/>
  </g>
  <g stroke="{TONES['gold'][2]}" stroke-width="7" stroke-linecap="round" fill="none">
    <path d="M-16 62v22M28 62v22"/>
  </g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M170 138q-18-10-16-26M136 160q-22-8-22-26"/>
</g>''', ground=False)

add('turkey', '扇のように広げた尾と赤い肉垂れを持つ七面鳥', f'''
{grass(306)}
<g transform="translate(310 226)">
  <g fill="#8b6437" stroke="{INK}" stroke-width="2.5">
''' + ''.join(f'<path d="M40 20L{40+150*__import__("math").cos((200+i*17)*3.14159/180):.0f} {20+150*__import__("math").sin((200+i*17)*3.14159/180):.0f}l18 22z" transform="rotate({-8+i*2} 40 20)"/>' for i in range(9)) + f'''
  </g>
  <ellipse cx="10" cy="14" rx="76" ry="62" fill="#5b4029" class="o"/>
  <path d="M-56-24q0-42 34-42t34 42z" fill="#5b4029" class="o"/>
  <circle cx="-42" cy="-46" r="6" fill="{INK}"/>
  <path d="M-64-38l-26 8 26 10z" class="gold o"/>
  <path d="M-58-30q-10 34 6 40 18-8 8-40z" class="coral o"/>
  <path d="M-52-52q-16-18 0-26 14 10 6 26z" class="coral o"/>
  <g stroke="{TONES['gold'][2]}" stroke-width="7" stroke-linecap="round" fill="none">
    <path d="M-6 72v14M34 72v14"/>
  </g>
</g>''', ground=False)

add('parrot', '曲がったくちばしと鮮やかな羽を持つオウム', f'''
<path d="M300 60v90" stroke="{MUTED}" stroke-width="5" fill="none"/>
<path d="M200 150h200" stroke="#8b6437" stroke-width="12" stroke-linecap="round" fill="none"/>
<g transform="translate(300 210)">
  <ellipse rx="66" ry="70" class="green o"/>
  <path d="M20-20q56-10 74 30-52 24-74-30z" class="greend o"/>
  <path d="M40 44l40 96-58-46z" class="coral o"/>
  <path d="M40 44l64 78-70-30z" class="gold o"/>
  <circle cx="-32" cy="-58" r="42" class="coral o"/>
  <circle cx="-44" cy="-66" r="7" fill="{INK}"/>
  <path d="M-70-58q-32 0-32 16 0 20 24 20 4-18 8-24 6 22 26 12z" fill="#e8e0cf" class="o"/>
  <path d="M-14-96q26-24 44-6-20 18-44 6z" class="blue o"/>
  <g stroke="{TONES['gold'][2]}" stroke-width="5" stroke-linecap="round" fill="none">
    <path d="M-12-134v-4"/>
  </g>
</g>''', ground=False)

add('penguin', '白い腹と黒い背中を持つペンギンが氷の上に立っている', f'''
<path d="M0 300h600v100H0z" fill="#dfeaf2"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 200)">
  <path d="M0-110q76 0 76 106t-76 110q-76 0-76-110t76-106z" fill="{INK}"/>
  <path d="M0-72q46 0 46 70t-46 76q-46 0-46-76t46-70z" fill="#fdf8ec"/>
  <path d="M-72-10q-30 26-24 74 22 12 34-20z" fill="{INK}"/>
  <path d="M72-10q30 26 24 74-22 12-34-20z" fill="{INK}"/>
  <circle cx="-24" cy="-72" r="7" fill="{INK}"/><circle cx="24" cy="-72" r="7" fill="{INK}"/>
  <path d="M0-56l-16 18h32z" class="gold o"/>
  <g fill="{TONES['gold'][1]}" stroke="{INK}" stroke-width="2">
    <path d="M-46 106h40l-8 14h-24z"/><path d="M6 106h40l-8 14h-24z"/>
  </g>
</g>''', ground=False)

# --- は虫類・両生類 ---------------------------------------------------------
add('toad', '皮膚がざらついた、ずんぐりしたヒキガエル', f'''
{grass(300)}
<g transform="translate(300 240)">
  <ellipse rx="120" ry="70" fill="#7a7a4e" class="o"/>
  <path d="M-70-40q0-44 70-44t70 44z" fill="#8c8c5c" class="o"/>
  <g fill="#8c8c5c" stroke="{INK}" stroke-width="2.5">
    <circle cx="-40" cy="-52" r="22"/><circle cx="40" cy="-52" r="22"/>
  </g>
  <circle cx="-40" cy="-52" r="9" fill="{INK}"/><circle cx="40" cy="-52" r="9" fill="{INK}"/>
  <path d="M-56-8q56 22 112 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <g fill="#6b6b42">
    <circle cx="-70" cy="10" r="9"/><circle cx="-30" cy="30" r="8"/><circle cx="20" cy="24" r="9"/>
    <circle cx="70" cy="6" r="8"/><circle cx="-4" cy="-4" r="7"/><circle cx="52" cy="38" r="7"/>
  </g>
  <g fill="#7a7a4e" stroke="{INK}" stroke-width="2.5">
    <path d="M-116 46q-34 8-30 26h56z"/><path d="M116 46q34 8 30 26h-56z"/>
  </g>
</g>''', ground=False)

add('lizard', '細い体と長い尾を持つトカゲが石の上にいる', f'''
<g>
  <path d="M100 306h400v20H100z" fill="#cfd6dd" class="o"/>
</g>
<g transform="translate(300 250)">
  <path d="M-100-16q0-30 60-30h60q54 0 54 28t-54 28h-60q-60 0-60-26z" class="green o"/>
  <path d="M74-16q46-4 60-24 18-24-8-36-20-8-24 14 20-2 22 12 2 16-50 18z" class="greend o"/>
  <ellipse cx="-118" cy="-12" rx="34" ry="24" class="green o"/>
  <circle cx="-132" cy="-20" r="6" fill="{INK}"/>
  <path d="M-146-10q-14 4-2 8" stroke="{TONES['coral'][0]}" stroke-width="3" fill="none"/>
  <g stroke="{TONES['green'][2]}" stroke-width="7" stroke-linecap="round" fill="none">
    <path d="M-66 12l-32 34M-24 14l-14 40M30 12l30 36M64 8l40 32"/>
  </g>
  <g fill="{TONES['green'][2]}">
''' + ''.join(f'<path d="M{-80+i*22} -46l8-14 8 14z"/>' for i in range(8)) + f'''
  </g>
</g>''', ground=False)

add('snake', '体をくねらせたヘビが舌を出している', f'''
{grass(310)}
<g fill="none" stroke="{TONES['green'][2]}" stroke-width="42" stroke-linecap="round" stroke-linejoin="round">
  <path d="M470 280q-90 30-120-20t-110-20-70-40 100-40"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="24" stroke-linecap="round" stroke-linejoin="round">
  <path d="M470 280q-90 30-120-20t-110-20-70-40 100-40"/>
</g>
<g transform="translate(270 160)">
  <ellipse rx="42" ry="30" class="greend o"/>
  <circle cx="-16" cy="-8" r="7" fill="{INK}"/>
  <path d="M-42 4q-30 6-14 12" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round"/>
  <path d="M-56 16l-14-6M-56 16l-12 8" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round" fill="none"/>
</g>
<g fill="{TONES['green'][2]}" opacity="0.7">
  <circle cx="360" cy="256" r="10"/><circle cx="300" cy="228" r="9"/><circle cx="418" cy="272" r="9"/>
</g>''', ground=False)

add('turtle', '甲羅を背負ったカメが四本の足で歩いている', f'''
{grass(306)}
<g transform="translate(300 236)">
  <path d="M-130 40q-14-96 130-96t130 96z" fill="#5b7a4e" class="o"/>
  <g fill="none" stroke="#3f5a36" stroke-width="4">
    <path d="M-86 24q86-40 172 0M-60-14q60-24 120 0M-30-40q30-12 60 0"/>
    <path d="M-40 40v-70M40 40v-70"/>
  </g>
  <path d="M-130 40h260v18h-260z" fill="#7a9a68" class="o"/>
  <ellipse cx="-160" cy="26" rx="40" ry="28" fill="#7a9a68" class="o"/>
  <circle cx="-176" cy="18" r="6" fill="{INK}"/>
  <path d="M-186 32q10 6 18 0" stroke="{INK}" stroke-width="3" fill="none"/>
  <g fill="#7a9a68" stroke="{INK}" stroke-width="2.5">
    <path d="M-104 58h44v24h-44z"/><path d="M60 58h44v24h-44z"/>
  </g>
  <path d="M130 40q40 6 46 26-30 12-46-8z" fill="#7a9a68" class="o"/>
</g>''', ground=False)

add('crocodile', '長い口とごつごつした背中を持つワニが水辺にいる', f'''
<path d="M0 296h600v104H0z" fill="#cfe0ec"/>
<path d="M0 296h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(310 250)">
  <path d="M-180 20q0-34 60-34h150q60 0 60 30t-60 26h-150q-60 0-60-22z" fill="#5b7a4e" class="o"/>
  <path d="M90 8q60-6 96-26 30-16 4-30-24-10-24 12 22-4 20 10-4 12-96 18z" fill="#5b7a4e" class="o"/>
  <path d="M-180 6q-70 0-96 14 26 22 96 22z" fill="#5b7a4e" class="o"/>
  <path d="M-256 18h80v10h-80z" fill="#7a9a68" class="o"/>
  <g fill="#fffefd" stroke="{INK}" stroke-width="1.6">
''' + ''.join(f'<path d="M{-244+i*22} 18l7 12 7-12z"/>' for i in range(8)) + f'''
  </g>
  <circle cx="-166" cy="-6" r="7" fill="{INK}"/>
  <g fill="#3f5a36">
''' + ''.join(f'<path d="M{-120+i*36} -14l12-20 12 20z"/>' for i in range(7)) + f'''
  </g>
  <g stroke="#3f5a36" stroke-width="10" stroke-linecap="round" fill="none">
    <path d="M-100 46l-24 26M40 46l26 26"/>
  </g>
</g>''', ground=False)

# --- けもの -----------------------------------------------------------------
add('wolf', 'とがった耳と太い尾を持つオオカミが遠ぼえしている', f'''
{grass(308)}
<g transform="translate(300 230)">
  <path d="M-90-10q0-40 60-40h70q56 0 56 44v50q0 20-20 20h-146q-20 0-20-20z" fill="#8f9aa6" class="o"/>
  <path d="M96 0q46-14 62-56 20 40-16 76-24 24-46 8z" fill="#8f9aa6" class="o"/>
  <path d="M-90-10q-34-30-30-66 4-36 40-40 30-4 40 22l14 44z" fill="#a6b0bb" class="o"/>
  <path d="M-118-72l-14-46 40 20zM-58-90l14-44 20 40z" fill="#a6b0bb" class="o"/>
  <circle cx="-90" cy="-70" r="6" fill="{INK}"/>
  <path d="M-118-102l-40-24 34 42z" fill="#a6b0bb" class="o"/>
  <circle cx="-152" cy="-120" r="7" fill="{INK}"/>
  <g stroke="#6f7b88" stroke-width="13" stroke-linecap="round" fill="none">
    <path d="M-50 100v24M0 100v24M56 100v24M96 96v28"/>
  </g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M110 90q-18-10-16-26M78 116q-22-8-22-26"/>
</g>''', ground=False)

add('fox', '赤茶色の毛と白い先の太い尾を持つキツネ', f'''
{grass(308)}
<g transform="translate(300 236)">
  <path d="M-80-6q0-38 56-38h64q52 0 52 42v44q0 18-18 18h-136q-18 0-18-18z" fill="#c8703a" class="o"/>
  <path d="M92 4q56-6 84-52 22 46-20 84-28 26-64 6z" fill="#c8703a" class="o"/>
  <path d="M148-6q26-16 28-42 14 26-4 52z" fill="#fdf8ec" class="o"/>
  <path d="M-80-6q-30-24-26-56 4-32 36-34 28-2 36 20l12 40z" fill="#d88a54" class="o"/>
  <path d="M-104-62l-8-44 34 20zM-52-80l10-42 20 38z" fill="#c8703a" class="o"/>
  <path d="M-100-58l-4-24 18 12zM-56-70l6-22 12 20z" fill="#f0c0a0"/>
  <circle cx="-80" cy="-58" r="6" fill="{INK}"/>
  <path d="M-104-38l-26 6 26 10z" fill="{INK}"/>
  <path d="M-100-14q30 18 60 0" fill="none" stroke="#fdf8ec" stroke-width="10"/>
  <g stroke="#a85a2c" stroke-width="12" stroke-linecap="round" fill="none">
    <path d="M-44 92v26M4 92v26M54 92v26M88 88v30"/>
  </g>
</g>''', ground=False)

add('deer', '枝分かれした角を持つシカが森に立っている', f'''
{grass(310)}
{tree(80, 310, 0.8)}
{tree(530, 310, 0.7)}
<g transform="translate(300 220)">
  <path d="M-70 10q0-40 56-40h60q52 0 52 44v52q0 18-18 18h-132q-18 0-18-18z" fill="#b5854f" class="o"/>
  <path d="M98 14q20 0 20 14t-20 10z" fill="#fdf8ec" class="o"/>
  <path d="M-70 10q-26-26-24-62 2-34 34-36 28-2 34 22l12 44z" fill="#c99a63" class="o"/>
  <path d="M-96-40l-18-24 34 8z" fill="#c99a63" class="o"/>
  <circle cx="-74" cy="-56" r="6" fill="{INK}"/>
  <path d="M-96-34l-24 6 24 8z" fill="{INK}"/>
  <g fill="none" stroke="#8b6437" stroke-width="7" stroke-linecap="round">
    <path d="M-82-90q-8-40 6-58M-76-124l-24-18M-70-108l-28-6M-40-92q4-40-8-58M-46-124l24-18M-52-108l28-6"/>
  </g>
  <g stroke="#8b6437" stroke-width="12" stroke-linecap="round" fill="none">
    <path d="M-36 104v34M8 104v34M56 104v34M92 100v38"/>
  </g>
  <g fill="#e8c391"><circle cx="0" cy="20" r="7"/><circle cx="40" cy="34" r="7"/><circle cx="24" cy="56" r="6"/></g>
</g>''', ground=False)

add('rabbit', '長い耳と丸い尾を持つウサギが草の上にいる', f'''
{grass(304)}
<g transform="translate(300 240)">
  <ellipse cx="20" rx="86" ry="62" fill="#e0d6c0" class="o"/>
  <circle cx="98" cy="-10" r="26" fill="#fdf8ec" class="o"/>
  <circle cx="-64" cy="-44" r="46" fill="#e8e0cf" class="o"/>
  <path d="M-86-84q-16-72 6-78 22 6 14 76zM-46-88q-6-74 16-78 20 10-4 78z" fill="#e8e0cf" class="o"/>
  <path d="M-82-86q-10-52 2-58 14 6 8 56zM-48-90q-4-54 10-56 12 8-2 56z" fill="#f2c8c8"/>
  <circle cx="-84" cy="-50" r="6" fill="{INK}"/>
  <path d="M-102-32l-14 4 14 6z" fill="#e08a80"/>
  <g stroke="{INK}" stroke-width="2.5" fill="none">
    <path d="M-108-24l-24-6M-108-16l-24 4"/>
  </g>
  <g stroke="#c9bfa8" stroke-width="12" stroke-linecap="round" fill="none">
    <path d="M-20 56v14M40 56v14"/>
  </g>
</g>''', ground=False)

add('squirrel', 'ふさふさの尾を立てたリスが木の実を持っている', f'''
{grass(306)}
<g transform="translate(300 230)">
  <path d="M60 60q60-30 66-110 6-70-42-76-34-4-34 32 30-6 34 30 6 66-46 92z" fill="#c8703a" class="o"/>
  <ellipse cx="-10" cy="30" rx="60" ry="52" fill="#d88a54" class="o"/>
  <circle cx="-56" cy="-22" r="40" fill="#d88a54" class="o"/>
  <path d="M-78-52q-14-30 6-30 16 4 12 30zM-38-56q-8-30 12-28 14 8-2 30z" fill="#d88a54" class="o"/>
  <circle cx="-72" cy="-28" r="6" fill="{INK}"/>
  <path d="M-90-14l-16 4 16 6z" fill="{INK}"/>
  <path d="M-30 34q26-20 46 0-20 22-46 0z" fill="#8b6437" class="o"/>
  <g stroke="#a85a2c" stroke-width="10" stroke-linecap="round" fill="none">
    <path d="M-30 78v18M20 78v18"/>
  </g>
</g>''', ground=False)

add('mouse', '大きな丸い耳と細い尾を持つ小さなネズミ', f'''
{grass(308)}
<g transform="translate(300 254)">
  <ellipse cx="10" rx="76" ry="46" fill="#a6b0bb" class="o"/>
  <circle cx="-58" cy="-16" r="36" fill="#b8c1ca" class="o"/>
  <circle cx="-72" cy="-52" r="26" fill="#b8c1ca" class="o"/>
  <circle cx="-72" cy="-52" r="15" fill="#f2c8c8"/>
  <circle cx="-30" cy="-56" r="22" fill="#b8c1ca" class="o"/>
  <circle cx="-30" cy="-56" r="12" fill="#f2c8c8"/>
  <circle cx="-76" cy="-18" r="6" fill="{INK}"/>
  <path d="M-92-6l-12 4 12 4z" fill="#e08a80"/>
  <g stroke="{INK}" stroke-width="2" fill="none">
    <path d="M-104 0l-26-8M-104 6l-26 6"/>
  </g>
  <path d="M86 4q60 4 70 46" fill="none" stroke="#8f9aa6" stroke-width="7" stroke-linecap="round"/>
  <g stroke="#8f9aa6" stroke-width="8" stroke-linecap="round" fill="none">
    <path d="M-16 44v10M40 44v10"/>
  </g>
</g>''', ground=False)

add('hedgehog', '背中がとげにおおわれたハリネズミ', f'''
{grass(306)}
<g transform="translate(300 250)">
  <path d="M-120 40q-16-90 96-90t100 90z" fill="#8b6437" class="o"/>
  <g stroke="#5b4029" stroke-width="5" stroke-linecap="round" fill="none">
''' + ''.join(f'<path d="M{-104+i*22} {28-abs(i-5)*7}l{-8+ (i-5)*2} -{34-abs(i-5)*4}"/>' for i in range(11)) + f'''
  </g>
  <path d="M-120 40q-46-4-52-24 20-24 56-14z" fill="#e0c48a" class="o"/>
  <circle cx="-142" cy="16" r="6" fill="{INK}"/>
  <path d="M-166 22l-14 4 14 6z" fill="{INK}"/>
  <g stroke="#c9a464" stroke-width="9" stroke-linecap="round" fill="none">
    <path d="M-60 42v14M10 42v14M70 40v16"/>
  </g>
</g>''', ground=False)

add('whale', '潮を吹きながら泳ぐ大きなクジラ', f'''
<path d="M0 260h600v140H0z" fill="#cfe0ec"/>
<g fill="none" stroke="#a8c4da" stroke-width="4"><path d="M40 300h140M340 320h160M120 350h200"/></g>
<g transform="translate(300 250)">
  <path d="M-190 20q0-70 100-70t150 40q60 32 30 60-70 24-180 8-100-14-100-38z" fill="#5b7a9e" class="o"/>
  <path d="M-190 20q-40 10-46-34 40-16 76 4z" fill="#5b7a9e" class="o"/>
  <path d="M-170-4q-30-26-8-46 26 12 34 40z" fill="#5b7a9e" class="o"/>
  <path d="M60 42q46 16 96 4-30 34-96 14z" fill="#3f5a76" class="o"/>
  <path d="M-120 26q100 26 200 6" fill="none" stroke="#c7dbea" stroke-width="10"/>
  <circle cx="-152" cy="-2" r="7" fill="{INK}"/>
</g>
<g fill="none" stroke="#a8c4da" stroke-width="7" stroke-linecap="round">
  <path d="M172 196q-14-42 6-70M186 196q10-44 34-64"/>
</g>''', ground=False)

add('dolphin', '背びれととがった口を持つイルカが水面から跳ねている', f'''
<path d="M0 300h600v100H0z" fill="#cfe0ec"/>
<g fill="none" stroke="#a8c4da" stroke-width="4"><path d="M40 336h160M360 356h180"/></g>
<g transform="translate(300 200) rotate(-14)">
  <path d="M-180 30q0-64 90-70 90-6 150 22 56 26 26 52-70 26-166 12-100-16-100-16z" fill="#7a9ec0" class="o"/>
  <path d="M-180 30q-46 0-56-30 44-14 84 4z" fill="#7a9ec0" class="o"/>
  <path d="M-186 6q-40-6-52-24 34-10 62 6z" fill="#7a9ec0" class="o"/>
  <path d="M0-40q10-60 44-64-10 42-16 62z" fill="#5b7a9e" class="o"/>
  <path d="M76 44q46 20 90-2-30 40-96 18z" fill="#5b7a9e" class="o"/>
  <path d="M-130 22q90 26 190 6" fill="none" stroke="#d6e6f0" stroke-width="12"/>
  <circle cx="-150" cy="-2" r="7" fill="{INK}"/>
  <path d="M-170 12q18 8 32 2" stroke="{INK}" stroke-width="3" fill="none"/>
</g>
<g fill="none" stroke="#fffefd" stroke-width="6" stroke-linecap="round">
  <path d="M120 316q30-16 60 0M440 330q30-16 60 0"/>
</g>''', ground=False)

add('shark', '三角の背びれを水面に出して泳ぐサメ', f'''
<path d="M0 210h600v190H0z" fill="#cfe0ec"/>
<path d="M0 210h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 290)">
  <path d="M-190 10q0-56 90-64 96-8 156 26 54 30 20 52-76 24-176 6-90-16-90-20z" fill="#8f9aa6" class="o"/>
  <path d="M-190 10q-46 4-56-26 44-16 84 2z" fill="#8f9aa6" class="o"/>
  <path d="M-196-12q-40-8-50-28 34-8 62 10z" fill="#8f9aa6" class="o"/>
  <path d="M-10-52q20-80 50-88-4 52-14 86z" fill="#6f7b88" class="o"/>
  <path d="M70 40q50 22 96 0-30 40-100 16z" fill="#6f7b88" class="o"/>
  <path d="M-130 4q94 24 190 6" fill="none" stroke="#d6dde4" stroke-width="12"/>
  <circle cx="-152" cy="-16" r="7" fill="{INK}"/>
  <path d="M-176 6q34 14 62 4" fill="none" stroke="{INK}" stroke-width="3"/>
  <g fill="#fffefd" stroke="{INK}" stroke-width="1.4">
''' + ''.join(f'<path d="M{-172+i*18} 6l6 12 6-12z"/>' for i in range(6)) + f'''
  </g>
  <g stroke="#6f7b88" stroke-width="4" fill="none">
    <path d="M-70-20v26M-52-22v28M-34-22v28"/>
  </g>
</g>''', ground=False)

add('goat', 'あごひげと後ろに反った角を持つヤギ', f'''
{grass(306)}
<g transform="translate(300 232)">
  <path d="M-70 6q0-38 56-38h64q52 0 52 42v46q0 18-18 18h-136q-18 0-18-18z" fill="#e0d6c0" class="o"/>
  <path d="M102 8q26-4 30-24 16 22-6 40z" fill="#e0d6c0" class="o"/>
  <path d="M-70 6q-30-22-28-52 2-30 32-32 26-2 32 20l10 42z" fill="#e8e0cf" class="o"/>
  <circle cx="-72" cy="-52" r="6" fill="{INK}"/>
  <path d="M-94-30l-22 4 22 8z" fill="{SKINL}"/>
  <path d="M-92-14q-10 34 6 40 16-10 6-40z" fill="#e8e0cf" class="o"/>
  <path d="M-88-78q-30-40-2-52 12 22 24 40zM-52-84q-26-42 2-52 10 24 20 44z" fill="none" stroke="#c9bfa8" stroke-width="9" stroke-linecap="round"/>
  <g stroke="#c9bfa8" stroke-width="12" stroke-linecap="round" fill="none">
    <path d="M-36 96v28M8 96v28M56 96v28M92 92v32"/>
  </g>
</g>''', ground=False)

add('donkey', '長い耳と灰色の毛を持つロバが荷を背負っている', f'''
{grass(308)}
<g transform="translate(300 226)">
  <path d="M-70 10q0-40 58-40h68q54 0 54 44v54q0 18-18 18h-144q-18 0-18-18z" fill="#a6b0bb" class="o"/>
  <path d="M104 20q24 24 20 64-24 8-32-28z" fill="#8f9aa6" class="o"/>
  <path d="M-70 10q-28-26-26-62 2-34 34-36 28-2 34 22l12 44z" fill="#b8c1ca" class="o"/>
  <path d="M-92-52q-20-58-2-64 18 8 16 62zM-56-60q-10-60 10-62 16 10 4 60z" fill="#b8c1ca" class="o"/>
  <circle cx="-74" cy="-54" r="6" fill="{INK}"/>
  <path d="M-98-28q-14 6 0 12" fill="#8f9aa6" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-24-30h96v22h-96z" class="coral o"/>
  <g stroke="#8f9aa6" stroke-width="13" stroke-linecap="round" fill="none">
    <path d="M-34 100v28M10 100v28M58 100v28M94 96v32"/>
  </g>
</g>''', ground=False)

add('camel', '背中にこぶのあるラクダが砂漠を歩いている', f'''
<path d="M0 300h600v100H0z" fill="#f0dfb8"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 210)">
  <path d="M-60 30q0-30 50-30h100q46 0 46 34v40q0 16-16 16h-164q-16 0-16-16z" fill="#d8b878" class="o"/>
  <path d="M-30 4q0-48 34-48t34 48zM50 4q0-42 30-42t30 42z" fill="#d8b878" class="o"/>
  <path d="M136 34q22 22 18 56-22 8-30-24z" fill="#c9a464" class="o"/>
  <path d="M-60 30q-36-14-46-54-10-42 22-56 26-10 36 16l16 62z" fill="#e0c48a" class="o"/>
  <ellipse cx="-100" cy="-74" rx="34" ry="26" fill="#e0c48a" class="o"/>
  <circle cx="-112" cy="-84" r="6" fill="{INK}"/>
  <path d="M-128-68q-14 6-2 12" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-106-104q-16-24 4-24 12 12 8 24z" fill="#e0c48a" class="o"/>
  <g stroke="#c9a464" stroke-width="13" stroke-linecap="round" fill="none">
    <path d="M-30 90v40M14 90v40M66 90v40M110 86v44"/>
  </g>
</g>''', ground=False)

add('elephant', '長い鼻と大きな耳を持つゾウ', f'''
{grass(312)}
<g transform="translate(300 220)">
  <path d="M-40 20q0-50 70-50h70q60 0 60 56v54q0 20-20 20h-160q-20 0-20-20z" fill="#9aa5b0" class="o"/>
  <path d="M158 34q26 22 22 62-26 8-34-30z" fill="#8f9aa6" class="o"/>
  <path d="M-40 20q-46-16-56-64-10-46 26-60 30-12 42 16l18 66z" fill="#a6b0bb" class="o"/>
  <ellipse cx="-40" cy="-64" rx="52" ry="56" fill="#8f9aa6" class="o"/>
  <circle cx="-92" cy="-70" r="7" fill="{INK}"/>
  <path d="M-108-48q-24 40-16 80 4 28 30 22 22-6 12-28-10-20 8-38z" fill="#a6b0bb" class="o"/>
  <path d="M-84-30q-24 8-16 40" fill="none" stroke="#fdf8ec" stroke-width="8" stroke-linecap="round"/>
  <g stroke="#8f9aa6" stroke-width="16" stroke-linecap="round" fill="none">
    <path d="M-4 96v34M50 96v34M104 96v34M146 92v38"/>
  </g>
</g>''', ground=False)

add('lion', 'たてがみに囲まれた顔を持つライオン', f'''
{grass(310)}
<g transform="translate(300 226)">
  <path d="M-30 10q0-38 60-38h60q50 0 50 42v48q0 18-18 18h-134q-18 0-18-18z" fill="#d8b878" class="o"/>
  <path d="M138 26q40 10 44 50-34 14-48-20z" fill="#d8b878" class="o"/>
  <path d="M176 66q22 4 20 24-22 6-26-14z" fill="#8b6437" class="o"/>
  <circle cx="-52" cy="-24" r="78" fill="#a0764a" class="o"/>
  <g fill="#8b6437">
''' + ''.join(f'<path d="M-52 -24l{86*__import__("math").cos(i*3.14159/6):.0f} {86*__import__("math").sin(i*3.14159/6):.0f}" transform="translate(0 0)"/>' for i in range(12)) + f'''
  </g>
  <circle cx="-52" cy="-24" r="52" fill="#e0c48a" class="o"/>
  <circle cx="-72" cy="-38" r="6" fill="{INK}"/><circle cx="-32" cy="-38" r="6" fill="{INK}"/>
  <path d="M-52-16l-12 10h24z" fill="{INK}"/>
  <path d="M-52-6q-14 14-26 4M-52-6q14 14 26 4" fill="none" stroke="{INK}" stroke-width="3"/>
  <g stroke="#c9a464" stroke-width="13" stroke-linecap="round" fill="none">
    <path d="M0 98v28M50 98v28M100 98v28M136 94v32"/>
  </g>
</g>''', ground=False)

add('tiger', '黒いしま模様を持つトラ', f'''
{grass(310)}
<g transform="translate(300 226)">
  <path d="M-50 10q0-38 60-38h74q52 0 52 42v48q0 18-18 18h-150q-18 0-18-18z" fill="#e08a3a" class="o"/>
  <path d="M136 26q44 8 50 48-36 16-52-18z" fill="#e08a3a" class="o"/>
  <g fill="{INK}">
    <path d="M-14-24l10 46-16-2zM26-26l10 50-16-2zM66-24l10 46-16-2zM106-20l10 42-16-2z"/>
    <path d="M0 60l12 30h-18zM52 62l12 30h-18zM104 58l12 30h-18z"/>
    <path d="M150 40h30v8h-30zM158 58h30v8h-30z"/>
  </g>
  <circle cx="-64" cy="-20" r="60" fill="#e08a3a" class="o"/>
  <path d="M-104-64q-16-26 0-32 14 8 16 30zM-24-66q16-26 0-32-14 8-16 30z" fill="#e08a3a" class="o"/>
  <path d="M-64 4q-40 0-52-24 34-18 52-6 18-12 52 6-12 24-52 24z" fill="#fdf8ec"/>
  <circle cx="-84" cy="-34" r="6" fill="{INK}"/><circle cx="-44" cy="-34" r="6" fill="{INK}"/>
  <path d="M-64-14l-12 10h24z" fill="{INK}"/>
  <g fill="{INK}"><path d="M-96-60l6 22-12-2zM-64-68l6 24-12-2zM-32-60l6 22-12-2z"/></g>
  <g stroke="#c07028" stroke-width="13" stroke-linecap="round" fill="none">
    <path d="M-10 98v28M40 98v28M92 98v28M134 94v32"/>
  </g>
</g>''', ground=False)

add('giraffe', '首が非常に長く、まだら模様のあるキリン', f'''
{grass(316)}
{tree(510, 316, 0.9)}
<g transform="translate(280 250)">
  <path d="M-50 20q0-34 54-34h64q48 0 48 40v30q0 16-16 16h-134q-16 0-16-16z" fill="#e0c48a" class="o"/>
  <path d="M-50 20q-24-140-6-176 14-26 44-16 26 10 12 44l-18 148z" fill="#e0c48a" class="o"/>
  <ellipse cx="-8" cy="-180" rx="40" ry="26" fill="#e0c48a" class="o" transform="rotate(-16 -8 -180)"/>
  <circle cx="-24" cy="-196" r="6" fill="{INK}"/>
  <path d="M-40-176q-16 4-4 10" fill="none" stroke="{INK}" stroke-width="3"/>
  <g stroke="#c9a464" stroke-width="7" stroke-linecap="round" fill="none">
    <path d="M-16-206v-24M4-202v-22"/>
  </g>
  <g fill="#c9a464"><circle cx="-16" cy="-206" r="8"/><circle cx="4" cy="-202" r="8"/></g>
  <g fill="#b5854f">
    <ellipse cx="-20" cy="-120" rx="12" ry="10"/><ellipse cx="-32" cy="-80" rx="12" ry="10"/>
    <ellipse cx="-40" cy="-40" rx="12" ry="10"/><ellipse cx="10" cy="10" rx="16" ry="13"/>
    <ellipse cx="60" cy="0" rx="16" ry="13"/><ellipse cx="100" cy="20" rx="15" ry="12"/>
    <ellipse cx="40" cy="40" rx="14" ry="11"/>
  </g>
  <g stroke="#c9a464" stroke-width="12" stroke-linecap="round" fill="none">
    <path d="M-16 72v46M30 72v46M84 72v46M124 68v50"/>
  </g>
</g>''', ground=False)

add('zebra', '白と黒のしま模様を持つシマウマ', f'''
{grass(310)}
<g transform="translate(300 224)">
  <path d="M-60 10q0-38 60-38h74q52 0 52 42v48q0 18-18 18h-150q-18 0-18-18z" fill="#fdf8ec" class="o"/>
  <path d="M136 24q34 20 34 58-30 12-42-24z" fill="#fdf8ec" class="o"/>
  <path d="M-60 10q-28-26-26-62 2-34 34-36 28-2 34 22l12 44z" fill="#fdf8ec" class="o"/>
  <g fill="{INK}">
    <path d="M-20-24l10 92h-18zM16-26l10 96h-18zM52-24l10 92h-18zM88-20l10 88h-18zM120-14l10 82h-18z"/>
    <path d="M-66-38l24 8-24 10zM-72-14l30 8-30 10zM-58-58l22 8-22 10z"/>
    <path d="M138 30l30 10-30 8zM146 52l28 10-28 8z"/>
  </g>
  <path d="M-84-52q-14-26 2-30 12 10 12 30zM-52-62q10-28 24-24-2 14-12 30z" fill="#fdf8ec" class="o"/>
  <circle cx="-72" cy="-48" r="6" fill="{INK}"/>
  <path d="M-96-24q-14 6 0 12" fill="{INK}"/>
  <g stroke="{MUTED}" stroke-width="13" stroke-linecap="round" fill="none">
    <path d="M-16 98v28M32 98v28M84 98v28M124 94v32"/>
  </g>
</g>''', ground=False)

add('paw', '肉球のある動物の足あと', f'''
<g transform="translate(300 220)">
  <ellipse cy="46" rx="76" ry="60" fill="#8b6437" class="o"/>
  <g fill="#a0764a" stroke="{INK}" stroke-width="2.5">
    <ellipse cx="-72" cy="-24" rx="26" ry="32" transform="rotate(-20 -72 -24)"/>
    <ellipse cx="-26" cy="-56" rx="24" ry="32"/>
    <ellipse cx="26" cy="-56" rx="24" ry="32"/>
    <ellipse cx="72" cy="-24" rx="26" ry="32" transform="rotate(20 72 -24)"/>
  </g>
</g>
<g fill="#c9a464" opacity="0.5">
  <ellipse cx="140" cy="330" rx="30" ry="24"/><ellipse cx="120" cy="298" rx="12" ry="15"/>
  <ellipse cx="148" cy="288" rx="11" ry="14"/><ellipse cx="172" cy="300" rx="12" ry="15"/>
</g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
