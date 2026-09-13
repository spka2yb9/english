# -*- coding: utf-8 -*-
"""第120回。台所・道具・体の動作。動詞は「前と後」か「手と物」で見せる。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))
BRN='#8b6437'
def table(y=300):
    return (f'<path d="M40 {y}h520v20H40z" fill="#c9a464" class="o"/>'
            f'<path d="M80 {y+20}v60M520 {y+20}v60" stroke="#a0764a" stroke-width="14" stroke-linecap="round" fill="none"/>')
def pot(x, y, s=1, lid=True):
    l = f'<ellipse cx="0" cy="-84" rx="80" ry="14" fill="#b8bfc8" class="o"/><rect x="-12" y="-104" width="24" height="20" rx="10" fill="{INK}"/>' if lid else ''
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-76-80h152l-12 80q-4 12-64 12t-64-12z" fill="#9aa5b0" class="o"/>'
            f'<path d="M-76-70h-26q-14 0-14 16t14 16h20M76-70h26q14 0 14 16t-14 16h-20" fill="none" stroke="{INK}" stroke-width="7"/>'
            f'{l}</g>')

# --- 台所と食べ物 ------------------------------------------------------------
add('butter', 'パンにナイフでバターを塗っている', f'''
{table(304)}
<g transform="translate(190 260)">
  <path d="M-84 44q-14-64 20-72 60-14 130 6 16 6 12 66z" fill="#e8c98d" class="o"/>
  <path d="M-70 20q60-20 140 0" fill="none" stroke="#c9a464" stroke-width="4"/>
  <path d="M-70-16q54-14 128 2 8 22 4 30-70-18-136 4-2-24 4-36z" fill="#fde39a" class="o"/>
</g>
<g transform="translate(400 250) rotate(28)">
  <path d="M-70-8h96q30 0 30 10t-30 10h-96z" fill="#c8d0d8" class="o"/>
  <path d="M-124-9h58v20h-58q-10 0-10-10t10-10z" fill="{INK}"/>
  <path d="M-30-20h50v-10h-56z" fill="#fde39a" class="o"/>
</g>
<g transform="translate(486 292)">
  <path d="M-56-30h112v30h-112z" fill="#fde39a" class="o"/>
  <path d="M-56-30l16-16h112l-16 16z" fill="#fff2b8" class="o"/>
  <g fill="none" stroke="#e0c48a" stroke-width="3"><path d="M-30-24v24M0-24v24M30-24v24"/></g>
</g>''', ground=False)

add('snack', 'ポテトチップスとクッキーの皿をつまんでいる', f'''
{table(300)}
<g transform="translate(220 250)">
  <path d="M-90 50q-10-70 90-70t90 70z" fill="#fffdf6" class="o"/>
  <g class="gold o">
''' + ''.join(f'<ellipse cx="{-56+i*28}" cy="{6+(i%3)*14}" rx="26" ry="16" transform="rotate({-20+i*14} {-56+i*28} {6+(i%3)*14})"/>' for i in range(5)) + f'''
  </g>
</g>
<g transform="translate(430 268)">
  <circle r="42" fill="#c9a464" class="o"/>
  <g fill="#6b4c28"><circle cx="-14" cy="-10" r="7"/><circle cx="14" cy="-2" r="6"/><circle cx="-4" cy="18" r="6"/><circle cx="18" cy="-22" r="5"/></g>
</g>
{hand(470, 150, -1)}
<g class="a" marker-end="url(#ar)"><path d="M462 196v34"/></g>''', arrow=True)

add('stew', '肉と野菜がごろごろ入った煮込みが深い皿に盛られている', f'''
{table(310)}
<g transform="translate(300 264)">
  <path d="M-120 0q0 56 120 56T120 0z" fill="#fffdf6" class="o"/>
  <ellipse rx="120" ry="24" fill="#c8703a" class="o"/>
  <g class="o">
    <path d="M-58-14q18-16 40-2t-6 24-42-8z" fill="#8b4a2c"/>
    <path d="M18-18q22-12 38 6t-20 20-24-14z" fill="#8b4a2c"/>
    <circle cx="-16" cy="8" r="14" fill="#e8983a"/>
    <circle cx="62" cy="-2" r="12" fill="#e8983a"/>
    <circle cx="-84" cy="0" r="11" class="green"/>
    <circle cx="30" cy="10" r="10" class="green"/>
  </g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" opacity="0.8">
  <path d="M240 208q14-24 0-44M300 196q14-26 0-48M360 208q14-24 0-44"/>
</g>''', ground=False)

add('simmer', 'なべの中がぐつぐつと弱火で煮えている', f'''
{table(320)}
{pot(300, 300, 1, False)}
<path d="M224 250h152v-6q-76-14-152 0z" fill="#c8703a"/>
<g fill="#e8983a" stroke="{INK}" stroke-width="2">
  <circle cx="252" cy="242" r="11"/><circle cx="292" cy="234" r="14"/><circle cx="334" cy="244" r="10"/><circle cx="362" cy="236" r="8"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3.5" stroke-linecap="round" opacity="0.8">
  <path d="M258 210q12-20 0-36M300 200q12-22 0-40M344 210q12-20 0-36"/>
</g>
<g>
  <path d="M230 340h140" stroke="{INK}" stroke-width="5" fill="none"/>
  <g class="coral o">
    <path d="M256 340q-6-24 8-32 2 12 10 6 2 14-4 26zM300 340q-6-26 8-34 2 12 10 6 2 16-4 28zM344 340q-6-24 8-32 2 12 10 6 2 14-4 26z"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M448 356h-56"/></g>''', arrow=True, ground=False)

add('grate', 'おろし金でチーズをすりおろしている', f'''
{table(320)}
<g transform="translate(280 200)">
  <path d="M-46-90h92l24 190h-140z" fill="#c8d0d8" class="o"/>
  <g fill="{INK}">
''' + ''.join(f'<path d="M{-44+c*22} {-50+r*26}l10 8-10 4z"/>' for r in range(6) for c in range(5)) + f'''
  </g>
  <path d="M-30-90q30-24 60 0" fill="none" stroke="{INK}" stroke-width="7"/>
</g>
<g transform="translate(392 176) rotate(-24)">
  <path d="M-40-26h80v52h-80z" fill="#fde39a" class="o"/>
  <g fill="#e8c98d"><circle cx="-16" cy="-6" r="6"/><circle cx="14" cy="8" r="5"/><circle cx="6" cy="-14" r="4"/></g>
</g>
<g fill="#fde39a" stroke="#e0c48a" stroke-width="2">
''' + ''.join(f'<path d="M{230+i*24} {318-(i%4)*8}q10-14 20 0-10 8-20 0z"/>' for i in range(8)) + f'''
</g>''', ground=False)

add('sprinkle', '料理の上に塩をふりかけている', f'''
{table(320)}
<g transform="translate(300 274)">
  <ellipse rx="110" ry="26" fill="#fffdf6" class="o"/>
  <path d="M-110 0q0 34 110 34T110 0z" fill="#fffdf6" class="o"/>
  <g class="o"><circle cx="-40" cy="-6" r="20" class="green"/><circle cx="12" cy="-10" r="18" class="coral"/><circle cx="60" cy="-2" r="16" class="gold"/></g>
</g>
<g transform="translate(340 130) rotate(38)">
  <path d="M-24 0h48l-6 70q-2 12-18 12t-18-12z" fill="#fffdf6" class="o"/>
  <path d="M-24 0q0-20 24-20t24 20z" fill="#b8bfc8" class="o"/>
  <g fill="{INK}"><circle cx="-8" cy="-10" r="2.5"/><circle cx="8" cy="-10" r="2.5"/><circle cx="0" cy="-16" r="2.5"/></g>
</g>
<g fill="#fffefd" stroke="{MUTED}" stroke-width="1.5">
''' + ''.join(f'<circle cx="{288+i*13}" cy="{170+(i%5)*18}" r="3.5"/>' for i in range(12)) + f'''
</g>''', ground=False)

add('peanut', '殻の入ったピーナッツと、殻を割って出た豆', f'''
{table(316)}
<g transform="translate(220 250) rotate(-14)">
  <path d="M-70 0q0-40 34-40t32 26q6-30 40-28 36 2 36 40t-36 40q-34 2-40-28-2 28-32 26T-70 0z" fill="#d9b877" class="o"/>
  <g fill="none" stroke="#a0764a" stroke-width="3">
    <path d="M-54-18q10 40 0 38M-24-24q10 48 0 46M28-26q10 52 0 50M60-20q10 42 0 40"/>
  </g>
</g>
<g transform="translate(410 262)">
  <ellipse cx="-24" rx="28" ry="34" fill="#e8c9a0" class="o"/>
  <ellipse cx="34" cy="10" rx="28" ry="34" fill="#e8c9a0" class="o" transform="rotate(20 34 10)"/>
  <path d="M-24-34v68" stroke="#c9a464" stroke-width="3" fill="none"/>
</g>
<g fill="#d9b877" class="o">
  <path d="M470 300q26-18 40 0-14 18-40 0z"/><path d="M500 320q24-16 38 0-12 16-38 0z"/>
</g>''', ground=False)

add('pinch', '指先で塩をひとつまみしている', f'''
{table(330)}
<g transform="translate(280 170)">
  <path d="M-70 0q-20-40 6-56 30-18 52 2 12-30 40-16 24 12 10 44" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M38-26q30 10 22 40-10 34-70 34-56 0-58-40" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-70 0q-16 16-4 30" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-64 6l-14 20" stroke="{SKIN}" stroke-width="16" stroke-linecap="round" fill="none"/>
  <path d="M-52 14l-4 26" stroke="{SKIN}" stroke-width="15" stroke-linecap="round" fill="none"/>
</g>
<g fill="#fffefd" stroke="{MUTED}" stroke-width="1.5">
''' + ''.join(f'<circle cx="{216+ (i%4)*10}" cy="{224+i*16}" r="3"/>' for i in range(7)) + f'''
</g>
<g transform="translate(230 300)">
  <ellipse cy="-6" rx="60" ry="18" fill="#f0e6d0" class="o"/>
  <path d="M-60-6q0 30 60 30t60-30z" fill="#fffdf6" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M400 190l-70 4"/></g>''', arrow=True, ground=False)

add('quench', '汗をかいた人がコップの水を一気に飲んでかわきをいやす', f'''
{person(200, 320, 1.0, 1, 'coral', 'blue', 'hold', 'short', 'sad')}
<g fill="{TONES['blue'][0]}">
  <path d="M170 190q8 8 8 13t-8 5-8-5 8-13zM238 184q8 8 8 13t-8 5-8-5 8-13z"/>
</g>
<g transform="translate(430 300)">
  <path d="M-46-100h92l-12 100q-2 12-34 12t-34-12z" fill="#e8f0f6" class="o"/>
  <path d="M-40-56h80l-8 56q-2 10-32 10t-32-10z" fill="{TONES['blue'][1]}"/>
  <path d="M-40-56h80" stroke="{TONES['blue'][0]}" stroke-width="3" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M366 200q-40 20-80 22"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M250 148q-10 14 0 24"/>
</g>''', arrow=True)

# --- 道具と作業 --------------------------------------------------------------
add('sew', '針と糸で布を縫っている', f'''
{table(320)}
<g transform="translate(280 250) rotate(-8)">
  <path d="M-150-60h300v110h-300z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="3"><path d="M-150-20h300M-150 14h300"/></g>
</g>
<g transform="translate(320 220) rotate(-40)">
  <path d="M0 0l-6 -70 6-10 6 10z" fill="#c8d0d8" class="o"/>
  <ellipse cy="-58" rx="4" ry="8" fill="{INK}"/>
</g>
<path d="M290 172q40-30 90-10 46 18 76-14" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M170 250h20M212 250h20M254 250h20M296 250h20M338 250h20M380 250h20"/>
</g>
<g transform="translate(490 260)">
  <path d="M-24-40h48v80h-48z" class="coralp o"/>
  <path d="M-24-40q24-12 48 0M-24 40q24 12 48 0" fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"/>
  <path d="M-16-30h32v60h-32z" class="coral"/>
</g>''', ground=False)

add('hem', '布のすそを折り返して縫っている', f'''
{table(330)}
<g transform="translate(300 200)">
  <path d="M-160-90h320v190h-320z" class="bluep o"/>
  <path d="M-160 60h320v40h-320z" class="blue o"/>
  <path d="M-160 60h320" stroke="{INK}" stroke-width="2.5" fill="none"/>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
''' + ''.join(f'<path d="M{-150+i*30} 80h18"/>' for i in range(11)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M460 330l0-40"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 6"><path d="M140 260h320"/></g>''', arrow=True, ground=False)

add('sharpen', '砥石で包丁の刃をといでいる', f'''
{table(320)}
<g transform="translate(300 290)">
  <path d="M-130-14h260v22q0 10-16 10h-228q-16 0-16-10z" fill="#8f9aa6" class="o"/>
  <path d="M-130-14q40-14 130-14t130 14z" fill="#b8bfc8" class="o"/>
</g>
<g transform="translate(290 232) rotate(-10)">
  <path d="M-110-22h150l40 22-40 12h-150z" fill="#dde3e8" class="o"/>
  <path d="M-110 12h190" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M80-6h96q14 0 14 10t-14 10H80z" fill="{INK}"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M140 250l-24-14M164 262l-26-8M120 274l-26 4"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M400 180h-140"/></g>
<g class="a" marker-end="url(#ar)"><path d="M260 160h140"/></g>''', arrow=True, ground=False)

add('knot', 'ロープの端が固く結ばれて結び目になっている', f'''
<g transform="translate(300 200)">
  <path d="M-260 40q120 0 160-40" fill="none" stroke="#c9a464" stroke-width="26" stroke-linecap="round"/>
  <path d="M260 40q-120 0-160-40" fill="none" stroke="#c9a464" stroke-width="26" stroke-linecap="round"/>
  <path d="M-100 0q40-70 100-70t100 70" fill="none" stroke="#c9a464" stroke-width="26" stroke-linecap="round"/>
  <path d="M-60-40q60 90 120 0" fill="none" stroke="#b08c50" stroke-width="26" stroke-linecap="round"/>
  <g fill="none" stroke="#a0764a" stroke-width="3">
    <path d="M-240 40h60M180 40h60M-40-56h80"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 316v-70"/></g>''', arrow=True, ground=False)

add('stitch', '布に糸で一針ずつ縫い目が並んでいる', f'''
{table(330)}
<g transform="translate(300 210)">
  <path d="M-180-80h360v170h-360z" fill="#f0e6d0" class="o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
''' + ''.join(f'<path d="M{-160+i*36} -20h22"/>' for i in range(9)) + f'''
  </g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="7" stroke-linecap="round">
''' + ''.join(f'<path d="M{-160+i*36} 40l22 20"/>' for i in range(9)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 130l-70 56"/></g>''', arrow=True, ground=False)

add('zip', 'ファスナーのスライダーを引き上げて閉じている', f'''
<g transform="translate(300 210)">
  <path d="M-140-160h100v340h-100zM40-160h100v340H40z" class="tealp o"/>
  <g fill="{INK}">
''' + ''.join(f'<path d="M-40 {-150+i*22}h14v12h-14zM26 {-140+i*22}h14v12h-14z"/>' for i in range(9)) + f'''
  </g>
  <path d="M-40 20h80v160h-80z" fill="{TONES['teal'][2]}"/>
  <g transform="translate(0 26)">
    <path d="M-26-16h52v34h-52z" fill="#b8bfc8" class="o"/>
    <path d="M-10 18h20v26h-20z" fill="#8f9aa6" class="o"/>
    <ellipse cy="56" rx="16" ry="22" fill="none" stroke="{INK}" stroke-width="6"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M420 260v-160"/></g>''', arrow=True, ground=False)

add('bolt', '六角の頭を持つ太いボルトとナット', f'''
{table(320)}
<g transform="translate(270 260)">
  <path d="M-140-40l24-24h60l24 24-24 24h-60z" fill="#9aa5b0" class="o"/>
  <path d="M-56-58h190v36h-190z" fill="#b8bfc8" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="2.5">
''' + ''.join(f'<path d="M{-40+i*20} -58l12 36"/>' for i in range(9)) + f'''
  </g>
  <path d="M-140-40l24-24h60l24 24-24 24h-60z" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>
<g transform="translate(440 296)">
  <path d="M-46 0l22-38h44l22 38-22 38h-44z" fill="#9aa5b0" class="o"/>
  <circle r="20" fill="#f0e6d0" class="o"/>
</g>''', ground=False)

add('dismantle', '棚を工具でばらばらに分解している', f'''
{table(340)}
<g transform="translate(220 260) rotate(-6)">
  <path d="M-90-100h20v200h-20zM70-100h20v200h-20z" fill="#c9a464" class="o"/>
</g>
<g transform="translate(400 200) rotate(24)">
  <path d="M-90-12h180v24h-180z" fill="#c9a464" class="o"/>
</g>
<g transform="translate(430 300) rotate(-40)">
  <path d="M-80-12h160v24h-160z" fill="#c9a464" class="o"/>
</g>
<g transform="translate(300 130) rotate(52)">
  <path d="M-70-10h140v20h-140z" fill="#c9a464" class="o"/>
</g>
<g transform="translate(500 130) rotate(30)">
  <path d="M-10-70h20v100h-20z" fill="#8f9aa6" class="o"/>
  <path d="M-26 30h52v46q0 12-26 12t-26-12z" fill="{INK}"/>
  <path d="M-10-70l-14-16h48l-14 16z" fill="#b8bfc8" class="o"/>
</g>
<g fill="{TONES['gold'][0]}">
  <circle cx="180" cy="150" r="7"/><circle cx="330" cy="250" r="7"/><circle cx="150" cy="300" r="7"/><circle cx="500" cy="250" r="7"/>
</g>''', ground=False)

add('crumble', '古い壁がぼろぼろに崩れて破片が落ちている', f'''
{table(350)}
<g>
  <path d="M120 350V110h280v70l-30 20 26 24-40 24 30 30-40 20 24 22-30 30z" fill="#d9cfbc" class="o"/>
  <g fill="none" stroke="#b8ad98" stroke-width="3">
    <path d="M150 160h240M150 210h200M150 260h180M150 310h140"/>
  </g>
  <g fill="#b8ad98">
    <path d="M300 150l30 26-34 12z"/><path d="M220 240l26 18-30 14z"/>
  </g>
</g>
<g fill="#d9cfbc" class="o">
''' + ''.join(f'<path d="M{420+i*22} {200+i*26}l{14+i*2} {10+i}l-{10+i} {14+i}z"/>' for i in range(6)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 170q40 60 40 140"/></g>''', arrow=True, ground=False)

add('ignite', 'マッチをすって火をつけた瞬間', f'''
<g transform="translate(240 260) rotate(-30)">
  <path d="M-140-8h180v16h-180z" fill="#c9a464" class="o"/>
  <ellipse cx="46" rx="22" ry="16" class="corald o"/>
</g>
{flame(300, 190, 1.1)}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M370 130l30-26M392 190l38-4M366 246l32 26"/>
</g>
<g transform="translate(140 340)">
  <path d="M-70-30h140v50h-140z" class="teald o"/>
  <path d="M-70-30h140v14h-140z" fill="#8f9aa6"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 250l60-30"/></g>''', arrow=True)

add('flake', '塗装が薄い破片になってはがれ落ちている', f'''
<path d="M0 0h600v400H0z" fill="#5c86ad"/>
<g fill="#c9a464">
  <path d="M300 60q60 40 40 120t-90 60-100-70 40-100 110-10z"/>
  <path d="M120 220q50 30 30 90t-90 40-40-80 100-50z"/>
  <path d="M440 200q60 20 50 90t-100 50-40-90 90-50z"/>
</g>
<g fill="#5c86ad" stroke="{INK}" stroke-width="2" opacity="0.95">
  <path d="M300 100q30 20 14 46t-40 8 26-54z"/>
</g>
<g fill="#5c86ad" class="o">
  <path d="M470 300l30 20-14 30-30-14z"/><path d="M180 330l34 12-8 32-32-10z"/><path d="M330 340l26 22-20 24-24-20z"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 250q30 40 20 100"/></g>''', arrow=True, ground=False)

add('underline', '文の一行に下線が引かれて強調されている', f'''
<g transform="translate(300 200)">
  <path d="M-220-150h440v300h-440z" class="paper"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-180" y="{-110+i*46}" width="{300-(i%3)*50}" height="10" rx="5"/>' for i in range(6)) + f'''
  </g>
  <rect x="-180" y="-18" width="250" height="10" rx="5" fill="{INK}"/>
  <path d="M-184 10h258" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round" fill="none"/>
</g>
<g transform="translate(430 250) rotate(30)">
  <path d="M0-90l14 30v90h-28V-60z" class="gold o"/>
  <path d="M-14 30h28v40l-14 24-14-24z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-6 70h12l-6 24z" fill="{INK}"/>
</g>''', ground=False)

add('swab', '綿棒で口の中の検体を取っている', f'''
{face(200, 200, 92, 'grin')}
<g transform="translate(390 200) rotate(-24)">
  <path d="M-90-5h180v10h-180z" fill="#e8e2d6" class="o"/>
  <ellipse cx="-100" rx="24" ry="16" fill="#fffefd" class="o"/>
  <ellipse cx="96" rx="18" ry="12" fill="#fffefd" class="o"/>
</g>
<g transform="translate(510 320)">
  <path d="M-24-70h48v70q0 14-24 14t-24-14z" fill="#e8f0f6" class="o"/>
  <path d="M-24-70h48v-14h-48z" fill="{TONES['blue'][0]}" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M330 150q60-30 130-10"/></g>''', arrow=True)

# --- 動きと体 ----------------------------------------------------------------
add('hurl', '石を力いっぱい投げつけている', f'''
{person(180, 330, 1.1, 1, 'coral', 'blue', 'up', 'short', 'sad')}
<circle cx="207" cy="180" r="18" fill="{MUTED}" class="o"/>
<g fill="{MUTED}" class="o">
  <path d="M320 150l22 12-6 24-24-8z"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 172q120-40 250 40"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M158 176l-24-20M186 148l-8-28"/>
</g>
<g fill="{MUTED}" class="o">
  <ellipse cx="520" cy="290" rx="30" ry="22"/>
</g>''', arrow=True)

add('jog', '軽い足取りでゆっくり走っている', f'''
{person(280, 330, 1.15, 1, 'teal', 'coral', 'walk', 'cap', 'smile', 'walk')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M120 220h60M100 260h50M130 300h44"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M420 240q14-16 0-30M448 246q20-22 0-42"/>
</g>
{tree(500, 306, 0.8)}''')

add('squint', 'まぶしくて目を細めて遠くを見ている', f'''
{sun(490, 90, 46)}
<g transform="translate(240 210)">
  <circle r="100" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-70-24q30-16 56 0M14-24q30-16 56 0" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <path d="M-70-46q30-14 56 0M14-46q30-14 56 0" fill="none" stroke="{HAIR}" stroke-width="8" stroke-linecap="round"/>
  <path d="M-30 44h60" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <g fill="none" stroke="{SKINL}" stroke-width="3">
    <path d="M-92-10l-16-10M-90 8l-18 4M92-10l16-10M90 8l18 4"/>
  </g>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M400 150l-40 30M410 200l-46 10M396 250l-40 22"/>
</g>''')

add('weep', '静かに涙を流して泣いている', f'''
{face(260, 200, 100, 'sad')}
<g fill="{TONES['blue'][0]}" stroke="{TONES['blue'][2]}" stroke-width="2">
  <path d="M226 200q10 12 10 20t-10 8-10-8 10-20z"/>
  <path d="M224 250q9 11 9 18t-9 7-9-7 9-18z"/>
  <path d="M294 206q10 12 10 20t-10 8-10-8 10-20z"/>
  <path d="M296 256q9 11 9 18t-9 7-9-7 9-18z"/>
</g>
<g transform="translate(470 250) rotate(-16)">
  <path d="M-56-46h112v92h-112z" fill="#fffefd" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-56-16h112M-56 14h112"/></g>
</g>''')

add('mumble', 'うつむいて口の中でもごもごと話している', f'''
{person(220, 330, 1.15, 1, 'violet', 'blue', 'stand', 'bob', 'neutral')}
<g transform="translate(380 170)">
  <path d="M-70-50h140q16 0 16 16v52q0 16-16 16h-96l-34 26v-26q-16 0-16-16v-52q0-16 16-16z" fill="#fffefd" class="o" opacity="0.9"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="{-50+ (i%3)*36}" y="{-30+ (i//3)*24}" width="28" height="10" rx="5" opacity="0.5"/>' for i in range(6)) + f'''
  </g>
  <path d="M-60-40l120 100" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 6" fill="none"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-linecap="round">
  <path d="M256 210q14 8 26 0M262 226q14 8 26 0"/>
</g>''')

add('overhear', '壁のむこうの話を思わず耳にしてしまう', f'''
<path d="M300 0h20v400h-20z" fill="#c9a464" class="o"/>
{person(150, 340, 1.0, 1, 'coral', 'blue', 'stand', 'bun', 'smile')}
{person(450, 340, 1.0, -1, 'teal', 'violet', 'point', 'short', 'smile')}
<g transform="translate(430 190)">
  <path d="M-60-40h140q14 0 14 14v44q0 14-14 14h-100l-28 22v-22q-12 0-12-14v-44q0-14 12-14z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}"><rect x="-44" y="-22" width="80" height="9" rx="4.5"/><rect x="-44" y="0" width="60" height="9" rx="4.5"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M272 190q-20 14 0 30M250 178q-34 26 0 54"/>
</g>
<ellipse cx="176" cy="222" rx="9" ry="13" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>''')

add('deaf', '耳が聞こえず、手話で話している', f'''
{person(200, 340, 1.05, 1, 'teal', 'blue', 'up', 'bob', 'smile')}
<g transform="translate(228 228)">
  <ellipse rx="12" ry="17" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-24-26l48 52M24-26l-48 52" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round" fill="none"/>
</g>
{hand(400, 200, 1)}
{hand(490, 250, -1)}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 6">
  <path d="M420 160q40-30 80 0"/>
</g>''')

add('immerse', '布をバケツの水にすっかり浸している', f'''
{table(340)}
<g transform="translate(300 260)">
  <path d="M-100-90h200l-20 130q-2 14-80 14t-80-14z" fill="#b8bfc8" class="o"/>
  <path d="M-96-60h192l-16 100q-2 12-80 12t-80-12z" fill="{TONES['blue'][1]}"/>
  <path d="M-96-60h192" stroke="{TONES['blue'][0]}" stroke-width="3" fill="none"/>
  <path d="M-100-90q0-40 100-40t100 40" fill="none" stroke="{INK}" stroke-width="6"/>
  <g class="coral o" opacity="0.85">
    <path d="M-56-40q40-20 90 0 20 40-10 60-50 14-84-14-14-26 4-46z"/>
  </g>
  <path d="M-40-70q30 16 60 0" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 100v90"/></g>''', arrow=True, ground=False)

add('paddle', 'カヌーをパドルでこいでいる', f'''
<path d="M0 250h600v150H0z" fill="#8fb8d4"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="#c7dbea" stroke-width="4"><path d="M40 300h150M380 330h180M60 350h140"/></g>
<g transform="translate(300 280)">
  <path d="M-170 0q0 34 170 34T170 0q-30-24-170-24T-170 0z" class="gold o"/>
  <path d="M-170 0q40-14 170-14T170 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"/>
</g>
{sit(290, 268, 0.72, 1, 'coral', 'blue', 'cap', 'smile', 'lap')}
<g transform="translate(330 190) rotate(38)">
  <path d="M-8-90h16v190h-16z" fill="#c9a464" class="o"/>
  <path d="M-30 100q0-40 30-40t30 40q0 30-30 34t-30-34z" fill="#b8bfc8" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M440 190q40 40 20 90"/></g>''', arrow=True, ground=False)

add('hike', 'リュックを背負って山道を歩いている', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
<path d="M0 300l140-160 90 90 110-140 120 130 140-60v240z" fill="#9aa5b0" class="o"/>
<path d="M0 300h600v100H0z" fill="#dfe8d8"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M40 400q160-70 260-100t300-0" fill="none" stroke="#c9a464" stroke-width="30"/>
{person(280, 356, 1.05, 1, 'coral', 'green', 'walk', 'cap', 'smile', 'walk')}
<g transform="translate(250 300)">
  <path d="M-30-40h60v70q0 12-30 12t-30-12z" class="teal o"/>
  <path d="M-30-40q30-14 60 0" fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"/>
</g>
<path d="M326 260v110" stroke="#a0764a" stroke-width="8" stroke-linecap="round" fill="none"/>
{sun(510, 70, 34)}''', ground=False)

add('detour', '工事で道がふさがれ、矢印が回り道を示す', f'''
{table(400)}
<path d="M0 240h600v120H0z" fill="#8f9aa6"/>
<g fill="none" stroke="#fffefd" stroke-width="6" stroke-dasharray="34 30"><path d="M0 300h600"/></g>
<g transform="translate(300 250)">
  <path d="M-110 40h220v20h-220z" class="coral o"/>
  <path d="M-110 40h220v20h-220z" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <g fill="#fffefd">
''' + ''.join(f'<path d="M{-100+i*40} 40l20 20h-20z"/>' for i in range(6)) + f'''
  </g>
  <path d="M-90 60v40M90 60v40" stroke="{INK}" stroke-width="8" stroke-linecap="round" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)" stroke-width="7"><path d="M60 300q60 0 80-90t150-70 130 60"/></g>
<g transform="translate(140 130)">
  <path d="M-40-30h80v60h-80z" class="gold o"/>
  <path d="M-24 0h48" stroke="{INK}" stroke-width="7" fill="none"/>
</g>''', ground=False)

add('sidewalk', '車道の横に一段高い歩道があり、人が歩いている', f'''
<path d="M0 250h600v150H0z" fill="#8f9aa6"/>
<g fill="none" stroke="#fffefd" stroke-width="6" stroke-dasharray="34 30"><path d="M0 330h600"/></g>
<path d="M0 220h600v40H0z" fill="#c8d0d8" class="o"/>
<path d="M0 250h600v14H0z" fill="#a8b2bc"/>
<g fill="none" stroke="{MUTED}" stroke-width="3">
''' + ''.join(f'<path d="M{60+i*80} 220v34"/>' for i in range(7)) + f'''
</g>
{person(200, 244, 0.75, 1, 'coral', 'blue', 'walk', 'bob', 'smile', 'walk')}
{person(400, 244, 0.75, -1, 'teal', 'violet', 'walk', 'short', 'smile', 'walk')}
<g transform="translate(480 300)">
  <path d="M-90 30h180v-40q0-14-14-14h-152q-14 0-14 14z" fill="#6f7b88" class="o"/>
  <circle cx="-56" cy="30" r="18" fill="{INK}"/><circle cx="56" cy="30" r="18" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M100 160v50"/></g>''', arrow=True, ground=False)

add('luggage', '空港でスーツケースとかばんをまとめて運んでいる', f'''
{table(330)}
<g transform="translate(200 240)">
  <path d="M-70-60h140v130h-140z" class="teal o"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"><path d="M-70 0h140M0-60v130"/></g>
  <path d="M-8-60v-30h16v30" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle cx="-44" cy="76" r="10" fill="{INK}"/><circle cx="44" cy="76" r="10" fill="{INK}"/>
</g>
<g transform="translate(370 280)">
  <path d="M-60-40h120v70h-120z" class="coral o"/>
  <path d="M-30-40q0-24 30-24t30 24" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
{box(490, 280, 90, 60, 20, 'gold')}''', ground=False)

add('umbrella', '雨の中でかさをさしている', f'''
<path d="M0 0h600v400H0z" fill="#cfd8e0"/>
{table(360)}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
''' + ''.join(f'<path d="M{40+i*44} {60+(i%3)*40}l-14 40"/>' for i in range(13)) + f'''
</g>
<g transform="translate(300 190)">
  <path d="M-150 0q0-110 150-110T150 0q-38-30-75-30T0-6q-38-24-75-24T-150 0z" class="coral o"/>
  <path d="M0-110v-20" stroke="{INK}" stroke-width="6" stroke-linecap="round" fill="none"/>
  <path d="M0 0v130q0 24 26 24" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
</g>
{person(300, 360, 0.95, 1, 'teal', 'blue', 'hold', 'bob', 'smile')}''', ground=False)

add('boot', 'すねまで覆う長靴が並んでいる', f'''
{table(320)}
<g transform="translate(230 300)">
  <path d="M-40-140h70v100l50 20q16 6 16 20H-40z" fill="#4a5560" class="o"/>
  <path d="M-40-140h70v20h-70z" fill="#6f7b88"/>
  <path d="M-42 0h140v-14H-42z" fill="{INK}"/>
</g>
<g transform="translate(400 300)">
  <path d="M-40-140h70v100l50 20q16 6 16 20H-40z" fill="#4a5560" class="o"/>
  <path d="M-40-140h70v20h-70z" fill="#6f7b88"/>
  <path d="M-42 0h140v-14H-42z" fill="{INK}"/>
</g>''', ground=False)

# --- 生き物と自然 -------------------------------------------------------------
add('chicken', 'とさかのあるニワトリが庭で餌をついばんでいる', f'''
{table(320)}
<g transform="translate(300 250)">
  <ellipse rx="80" ry="60" fill="#fffdf6" class="o"/>
  <path d="M60-30q46-30 60 4 8 26-20 34" fill="#fffdf6" class="o"/>
  <circle cx="94" cy="-42" r="30" fill="#fffdf6" class="o"/>
  <path d="M78-64q4-24 16-16 6-18 18-4 8-14 14 6-4 22-24 22z" class="coral o"/>
  <path d="M118-38l24 8-24 10z" class="gold o"/>
  <circle cx="102" cy="-46" r="3.5" fill="{INK}"/>
  <path d="M104-16q14 22 0 24t-12-24z" class="coral o"/>
  <path d="M-80-10q-40-30-46 10 30 24 46 18z" fill="#f0e6d0" class="o"/>
  <path d="M-20-20q40 8 44 44-40 8-58-24z" fill="#f0e6d0" class="o"/>
  <g stroke="{TONES['gold'][2]}" stroke-width="7" stroke-linecap="round" fill="none">
    <path d="M-20 58v14M20 58v14M-30 72h20M10 72h20"/>
  </g>
</g>
<g fill="#c9a464"><circle cx="430" cy="322" r="6"/><circle cx="452" cy="330" r="5"/><circle cx="412" cy="334" r="5"/></g>''', ground=False)

add('flock', '空を鳥の群れが並んで飛んでいる', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
{table(360)}
<g fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{110+i*46} {90+abs(i-5)*24}q14-16 26 0q12-16 26 0"/>' for i in range(10)) + f'''
</g>
<g fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round">
''' + ''.join(f'<path d="M{160+i*52} {200+abs(i-4)*20}q11-13 20 0q9-13 20 0"/>' for i in range(8)) + f'''
</g>
{tree(80, 360, 1.0)}
{tree(530, 360, 0.9)}''', ground=False)

add('herd', '牛の群れが草地に集まっている', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
<path d="M0 240h600v160H0z" fill="#dfe8d8"/>
<path d="M0 240h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g>
''' + ''.join(f'''<g transform="translate({100+i*100} {270+(i%3)*44}) scale({0.7+(i%3)*0.12})">
  <ellipse rx="72" ry="46" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><ellipse cx="-24" cy="-10" rx="22" ry="16"/><ellipse cx="34" cy="14" rx="18" ry="13"/></g>
  <circle cx="-76" cy="-30" r="30" fill="#fffdf6" class="o"/>
  <path d="M-96-52q-16-16-4-22 12-2 14 16zM-58-54q14-18 24-10 4 12-14 20z" fill="#e8c9a0" class="o"/>
  <circle cx="-86" cy="-32" r="3.5" fill="{INK}"/>
  <g stroke="#c9a464" stroke-width="8" stroke-linecap="round" fill="none"><path d="M-34 44v26M22 44v26"/></g>
</g>''' for i in range(5)) + f'''
</g>''', ground=False)

add('swarm', '虫の大群がかたまりになって飛んでいる', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
{table(350)}
<g fill="{INK}">
''' + ''.join(f'<ellipse cx="{300+130*math.cos(i*0.7)*(0.4+0.09*(i%7)):.0f}" cy="{180+100*math.sin(i*1.3)*(0.4+0.08*(i%6)):.0f}" rx="7" ry="5" transform="rotate({i*29} {300+130*math.cos(i*0.7)*(0.4+0.09*(i%7)):.0f} {180+100*math.sin(i*1.3)*(0.4+0.08*(i%6)):.0f})"/>' for i in range(34)) + f'''
</g>
<g fill="none" stroke="{MUTED}" stroke-width="2">
''' + ''.join(f'<path d="M{300+130*math.cos(i*0.7)*(0.4+0.09*(i%7)):.0f} {180+100*math.sin(i*1.3)*(0.4+0.08*(i%6)):.0f}l{-9+(i%3)*9} -8"/>' for i in range(0, 34, 2)) + f'''
</g>
{person(90, 350, 0.85, 1, 'coral', 'blue', 'up', 'short', 'sad')}''', ground=False)

add('burrow', '地面の下に掘られた巣穴とその中の動物', f'''
<path d="M0 0h600v190H0z" fill="#dceaf4"/>
<path d="M0 190h600v210H0z" fill="#c9a464"/>
<path d="M0 190h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="#dfe8d8"><path d="M0 178h600v14H0z"/></g>
<path d="M180 190q0 90 120 90t120-60" fill="none" stroke="#8b6437" stroke-width="52" stroke-linecap="round"/>
<path d="M180 190q0 90 120 90t120-60" fill="none" stroke="#f0e6d0" stroke-width="38" stroke-linecap="round"/>
<g transform="translate(300 272) scale(0.8)">
  <ellipse rx="56" ry="36" fill="#a0764a" class="o"/>
  <circle cx="52" cy="-16" r="26" fill="#a0764a" class="o"/>
  <path d="M44-40q-6-34 10-34 12 6 8 34zM70-40q6-32 20-28 6 10-8 32z" fill="#a0764a" class="o"/>
  <circle cx="62" cy="-20" r="3.5" fill="{INK}"/>
  <circle cx="76" cy="-10" r="5" fill="{SKINL}"/>
</g>
<g fill="#a0764a" class="o">
  <path d="M150 190q30-30 70-16-30 22-70 16z"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 120q40 40 46 60"/></g>''', arrow=True, ground=False)

add('volcano', '火山が噴煙と溶岩を噴き上げている', f'''
<path d="M0 0h600v400H0z" fill="#6b5570"/>
<path d="M0 400l180-260h60l180 260z" fill="#5b4a3c" class="o"/>
<path d="M180 140h60l-30-30z" fill="#5b4a3c"/>
<path d="M186 140q30-18 54 0-6 60-30 120-24-60-24-120z" class="coral o"/>
<path d="M196 140q20-12 34 0-4 44-18 90-16-46-16-90z" class="gold o"/>
<g fill="{MUTED}" opacity="0.85">
  <circle cx="210" cy="70" r="38"/><circle cx="270" cy="44" r="46"/><circle cx="340" cy="60" r="38"/><circle cx="160" cy="46" r="32"/>
</g>
<g class="coral o">
  <path d="M240 200q60 60 100 200h-40q-30-130-80-180z"/>
</g>
<g fill="{TONES['coral'][0]}">
  <circle cx="120" cy="180" r="9"/><circle cx="330" cy="150" r="8"/><circle cx="90" cy="250" r="7"/><circle cx="390" cy="220" r="8"/>
</g>''', ground=False)

add('orbit', '惑星のまわりを衛星がだ円の軌道で回っている', f'''
<path d="M0 0h600v400H0z" fill="#2c3550"/>
<g fill="#fffefd"><circle cx="70" cy="60" r="4"/><circle cx="520" cy="50" r="3"/><circle cx="140" cy="330" r="3"/><circle cx="470" cy="340" r="4"/><circle cx="300" cy="30" r="3"/></g>
<ellipse cx="300" cy="200" rx="230" ry="120" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9"/>
<circle cx="300" cy="200" r="76" class="blue o"/>
<g fill="{TONES['green'][0]}" opacity="0.9">
  <path d="M262 158q40-8 50 14t-30 30-40-20 20-24z"/><path d="M320 216q40 4 34 30t-44 6 10-36z"/>
</g>
<g transform="translate(524 216)">
  <path d="M-20-20h40v40h-40z" fill="#c8d0d8" class="o"/>
  <path d="M-70-12h44v24h-44zM26-12h44v24H26z" class="blue o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['gold'][0]}"><path d="M500 320q60-50 62-104"/></g>''', arrow=True, ground=False)

add('horizontal', '水平な線と垂直な線が並べて示されている', f'''
<g transform="translate(300 130)">
  <path d="M-220-40h440v80h-440z" class="tealp o"/>
  <path d="M-190 0h380" stroke="{TONES['teal'][2]}" stroke-width="12" stroke-linecap="round" fill="none"/>
  <g fill="none" stroke="{INK}" stroke-width="3" stroke-dasharray="7 7"><path d="M-190-30v60M190-30v60"/></g>
</g>
<g transform="translate(300 300)">
  <path d="M-220-70h440v140h-440z" fill="#f0eee6" class="o"/>
  <g stroke="{MUTED}" stroke-width="12" stroke-linecap="round" fill="none">
    <path d="M-120-50v100M0-50v100M120-50v100"/>
  </g>
  <path d="M-180 0h-30M180 0h30" stroke="{MUTED}" stroke-width="4" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 60h120"/></g>
<g class="a" marker-end="url(#ar)"><path d="M300 60H180"/></g>''', arrow=True, ground=False)

add('gardener', '庭師が花壇の手入れをしている', f'''
{table(320)}
<g fill="#8b6437"><path d="M300 320h280v-40q0-14-16-14H316q-16 0-16 14z"/></g>
<g>
''' + ''.join(f'<g transform="translate({340+i*52} {258})"><path d="M0 20v-30" stroke="{TONES["green"][2]}" stroke-width="6" fill="none"/><circle r="8" class="gold o"/>' + ''.join(f'<ellipse cx="{16*math.cos(j*1.2566):.0f}" cy="{16*math.sin(j*1.2566):.0f}" rx="10" ry="8" class="{"coralp" if i%2 else "violetp"} o"/>' for j in range(5)) + '</g>' for i in range(5)) + f'''
</g>
{person(160, 320, 1.05, 1, 'green', 'gold', 'reach', 'cap', 'smile')}
<g transform="translate(230 250) rotate(30)">
  <path d="M-30-8h60v16h-60z" fill="{INK}"/>
  <path d="M30-14h40l14 22-14 22H30z" fill="#8f9aa6" class="o"/>
</g>
<g transform="translate(90 300)">
  <path d="M-34-30h68l-8 60h-52z" class="teal o"/>
  <path d="M34-20q40 0 40 30h-40z" class="teal o"/>
</g>''', ground=False)

add('ferry', '車と人を乗せた渡し船が対岸へ向かう', f'''
<path d="M0 0h600v250H0z" fill="#dceaf4"/>
<path d="M0 250h600v150H0z" fill="#8fb8d4"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="#c7dbea" stroke-width="4"><path d="M20 320h150M400 340h180M60 370h120"/></g>
<g transform="translate(290 250)">
  <path d="M-190 0h380l-40 60q-6 12-150 12T-150 60z" class="blue o"/>
  <path d="M-160-70h320v70h-320z" fill="#fffdf6" class="o"/>
  <g class="bluep o">
    <rect x="-140" y="-56" width="50" height="34"/><rect x="-70" y="-56" width="50" height="34"/>
    <rect x="20" y="-56" width="50" height="34"/><rect x="90" y="-56" width="50" height="34"/>
  </g>
  <path d="M-40-130h90v60h-90z" fill="#fffdf6" class="o"/>
  <path d="M120-130h20v60h-20z" fill="{TONES['coral'][0]}" class="o"/>
</g>
<g transform="translate(240 176) scale(0.5)">
  <path d="M-90 30h180v-40q0-14-14-14h-152q-14 0-14 14z" fill="#6f7b88" class="o"/>
  <circle cx="-56" cy="30" r="18" fill="{INK}"/><circle cx="56" cy="30" r="18" fill="{INK}"/>
</g>
<g fill="#4a4436"><path d="M520 250V180h10v70zM540 250V200h10v50z"/></g>''', ground=False)

add('shampoo', '髪にシャンプーの泡を立てて洗っている', f'''
{table(360)}
<g transform="translate(280 250)">
  <circle r="90" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-84-24q6-70 84-70t84 70q-40-30-84-30t-84 30z" fill="{HAIR}"/>
  <path d="M-30-6q-8 14 0 22M30-6q8 14 0 22" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <path d="M-24 44q24 16 48 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
</g>
<g fill="#fffefd" stroke="{MUTED}" stroke-width="2">
''' + ''.join(f'<circle cx="{200+ (i%6)*32}" cy="{120+ (i//6)*30 - (i%3)*12}" r="{16-(i%4)*3}"/>' for i in range(15)) + f'''
</g>
{hand(190, 190, 1)}
{hand(390, 180, -1)}
<g transform="translate(500 300)">
  <path d="M-32-70h64v70q0 12-32 12t-32-12z" class="tealp o"/>
  <path d="M-14-70v-16h28v16z" class="teal o"/>
  <path d="M-24-46h48v26h-48z" class="teal"/>
</g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
