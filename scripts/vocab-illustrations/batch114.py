# -*- coding: utf-8 -*-
"""第114回。既存4,500語の最後の7語。暴力に関わる語は、人が傷つく場面ではなく
物・記号・避難する人の動きで概念だけを示す。"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib import *

W = []

# rifle ライフル銃 --- 壁の銃架に置かれた一挺。物として静かに見せる。
W.append(emit('rifle', 'ライフル銃が壁の銃架に横向きに掛けられている', f'''
<g>
  <rect x="60" y="70" width="480" height="240" rx="10" fill="#f3ece1" stroke="{INK}" stroke-width="2.5"/>
  <path d="M60 150h480M60 232h480" stroke="{MUTED}" stroke-width="2" fill="none"/>
  <g transform="translate(300 196)">
    <path d="M-198-8h236v14h-236z" fill="{INK}"/>
    <path d="M-198-9h236v6h-236z" fill="{MUTED}"/>
    <path d="M38-14q34-4 54 6 24 12 34 30 6 12 2 22-4 10-18 8-16-2-30-12-16-12-24-28-6-12-18-16z" fill="#8b6437" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>
    <path d="M92 52q22 2 42 12 20 10 30 24 6 10 0 16-8 8-24 0-18-10-32-26-10-12-16-26z" fill="#a0764a" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>
    <path d="M30 6v26q0 10 10 10h16" fill="none" stroke="{INK}" stroke-width="3.5"/>
    <path d="M38 12v18" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
    <rect x="-96" y="-40" width="96" height="20" rx="10" fill="{INK}"/>
    <path d="M-84-20v12M-16-20v12" stroke="{INK}" stroke-width="5"/>
    <circle cx="-88" cy="-30" r="8" fill="{TONES['blue'][1]}" stroke="{INK}" stroke-width="2.5"/>
    <path d="M-198-4h-16v22h16z" fill="{MUTED}" stroke="{INK}" stroke-width="2"/>
  </g>
  <path d="M118 210q0 26 26 26h18q26 0 26-26" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <path d="M400 210q0 26 26 26h18q26 0 26-26" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
</g>''', ground=False))

# shot 発射音・発砲 --- 的の中心に一発。音の輪だけで「バン」を表す。
W.append(emit('shot', '的の中心に弾痕がひとつあき、そこから音の輪が広がっている', f'''
<g>
  <path d="M300 300v66" stroke="#8b6437" stroke-width="16" stroke-linecap="round"/>
  <circle cx="300" cy="182" r="112" class="paper"/>
  <circle cx="300" cy="182" r="86" fill="none" stroke="{INK}" stroke-width="3"/>
  <circle cx="300" cy="182" r="58" class="coralp o"/>
  <circle cx="300" cy="182" r="30" class="coral o"/>
  <circle cx="300" cy="182" r="13" fill="{INK}"/>
  <path d="M300 182l-26-30 34 14 8-38 10 38 32-16-24 32" fill="{TONES['gold'][0]}" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M150 108a170 170 0 0 0 0 148" class="a" opacity="0.85"/>
  <path d="M112 84a212 212 0 0 0 0 196" class="a" opacity="0.5"/>
  <path d="M450 108a170 170 0 0 1 0 148" class="a" opacity="0.85"/>
  <path d="M488 84a212 212 0 0 1 0 196" class="a" opacity="0.5"/>
</g>''', ground=False))

# shooting 銃撃・射撃 --- 壁の弾痕と規制テープ。人は遠くで見ているだけ。
W.append(emit('shooting', '壁にいくつも弾痕があき、その前に立入禁止のテープが張られている', f'''
<g>
  <rect x="40" y="60" width="520" height="246" fill="#e8e2d6" stroke="{INK}" stroke-width="2.5"/>
  <path d="M40 140h520M40 220h520M170 60v80M300 140v80M430 60v80M110 220v86M370 220v86" stroke="{MUTED}" stroke-width="2" fill="none"/>
  <g fill="{INK}">
    <circle cx="196" cy="112" r="11"/><circle cx="252" cy="168" r="9"/><circle cx="330" cy="104" r="12"/>
    <circle cx="398" cy="176" r="8"/><circle cx="288" cy="234" r="10"/>
  </g>
  <g stroke="{MUTED}" stroke-width="2" fill="none">
    <path d="M196 112l16-16M196 112l-18 14M252 168l-14 12M330 104l18-18M330 104l-16-16M398 176l14 12M288 234l-16 14"/>
  </g>
  <path d="M20 250l560-34v34l-560 34z" fill="{TONES['gold'][1]}" stroke="{INK}" stroke-width="2.5"/>
  <path d="M74 246l-8 36M164 240l-8 36M254 235l-8 36M344 229l-8 36M434 224l-8 36M524 218l-8 36" stroke="{TONES['gold'][2]}" stroke-width="7"/>
</g>
{person(120, 388, 0.5, 1, 'blue', 'violet', 'stand', 'bob', 'sad')}
{person(196, 390, 0.48, -1, 'green', 'blue', 'point', 'short', 'sad')}''', ground=True))

# militant 戦闘的な・過激な --- 旗を掲げてこぶしを突き上げる先頭の人。後ろは穏やかな二人。
W.append(emit('militant', 'こぶしを突き上げ旗を掲げる人が、穏やかな二人の前に立っている', f'''
{person(430, 316, 0.62, -1, 'blue', 'blue', 'stand', 'bob', 'neutral')}
{person(508, 318, 0.58, -1, 'green', 'violet', 'stand', 'short', 'neutral')}
<g>
  <path d="M150 300V96" stroke="#8b6437" stroke-width="9" stroke-linecap="round"/>
  <path d="M150 100h148l-26 32 26 32H150z" class="coral o"/>
  <path d="M198 116l18 18-18 18-18-18z" class="coralp"/>
</g>
{person(210, 314, 1.02, -1, 'coral', 'blue', 'up', 'short', 'sad')}
<g fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round">
  <path d="M262 178l22-14M266 200l26-4M256 158l14-22"/>
</g>''', ground=True))

# guerrilla ゲリラ・遊撃兵 --- 森の木陰に潜み、道を通る車をうかがう。
W.append(emit('guerrilla', '森の木の陰にひそんだ二人が、道を通る車をうかがっている', f'''
<path d="M0 250h600v56H0z" fill="#d9d2c4"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M30 278h60M130 278h60M230 278h60M330 278h60M430 278h60M530 278h50" stroke="#fffefd" stroke-width="6"/>
<g>
  <rect x="352" y="188" width="150" height="62" rx="8" fill="{TONES['green'][2]}" class="o"/>
  <path d="M352 188h-64l-24 30v32h88z" fill="{TONES['green'][0]}" class="o"/>
  <rect x="296" y="200" width="40" height="24" rx="4" fill="{TONES['blue'][1]}" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="322" cy="250" r="24" fill="{INK}"/><circle cx="322" cy="250" r="10" fill="{MUTED}"/>
  <circle cx="456" cy="250" r="24" fill="{INK}"/><circle cx="456" cy="250" r="10" fill="{MUTED}"/>
</g>
{tree(96, 250, 1.15)}
{tree(214, 244, 0.9)}
{tree(534, 250, 1.0)}
<g fill="#3d5142" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
  <path d="M120 250q0-38 26-38 24 0 26 30l6 8z"/>
  <path d="M146 212a15 15 0 1 1 0-1z" fill="#4c6350"/>
  <path d="M172 242l34-10 4 10-34 12z"/>
</g>
<g fill="#3d5142" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
  <path d="M232 250q0-34 23-34 21 0 23 27l5 7z"/>
  <path d="M255 216a13 13 0 1 1 0-1z" fill="#4c6350"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="2.5" stroke-dasharray="7 8" stroke-linecap="round">
  <path d="M186 226l104 4"/>
</g>''', ground=False))

# terrorism テロ --- 広場に閃光が起き、人々が外へ逃げる。加害者は描かない。
W.append(emit('terrorism', '広場の中央で爆発が起き、人々が両側へ逃げていく', f'''
{building(70, 306, 0.9, 'blue')}
{building(500, 306, 0.85, 'violet')}
<g transform="translate(300 190)">
  <path d="M0-104l24 44 46-32-22 50 52 8-48 26 36 40-52-16-6 54-26-46-40 36 10-52-54-2 42-34-34-42 52 14z" class="coral o"/>
  <path d="M0-64l16 28 28-20-14 32 32 6-30 16 22 24-32-10-4 32-16-28-24 22 6-32-32-2 24-20-20-26 32 8z" class="gold o"/>
</g>
{person(150, 336, 0.62, -1, 'green', 'blue', 'up', 'bob', 'sad')}
{person(230, 348, 0.58, -1, 'gold', 'violet', 'walk', 'short', 'sad')}
{person(400, 348, 0.58, 1, 'teal', 'blue', 'walk', 'bun', 'sad')}
{person(470, 336, 0.6, 1, 'violet', 'green', 'up', 'short', 'sad')}
<g fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round" marker-end="url(#ar)">
  <path d="M212 268l-52-16"/><path d="M388 268l52-16"/>
</g>''', ground=True, arrow=True))

# terrorist テロリスト --- 建物のわきに鞄を置いて立ち去る影。顔は描かない。
W.append(emit('terrorist', 'フードをかぶった人影が建物のわきに鞄を置いて立ち去ろうとしている', f'''
{building(470, 306, 1.0, 'blue')}
<g>
  <rect x="238" y="252" width="104" height="54" rx="9" fill="#5b4a3c" class="o"/>
  <path d="M262 252v-14q0-10 10-10h36q10 0 10 10v14" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M238 276h104" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="290" cy="290" r="9" class="coral o"/>
  <path d="M290 281v-6M283 296l-8 6M297 296l8 6" stroke="{TONES['coral'][2]}" stroke-width="3" stroke-linecap="round" fill="none"/>
</g>
<g fill="#3b4450" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
  <path d="M170 306q-14-96 12-124 10-10 24-10t24 10q26 28 12 124z"/>
  <path d="M182 190q-6-38 12-52 8-6 18-6t18 6q18 14 12 52-14-14-30-14t-30 14z" fill="#2c333d"/>
  <path d="M196 186q14-10 28 0 4 12-14 12t-14-12z" fill="{MUTED}" stroke="none"/>
  <path d="M226 232l36 24" stroke="#3b4450" stroke-width="14" stroke-linecap="round" fill="none"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 9" stroke-linecap="round" marker-end="url(#ar)">
  <path d="M148 254l-88-26"/>
</g>''', ground=True, arrow=True))

print(sheet(W, '/tmp/vocab-sheet.html', 4))
print(len(W))
