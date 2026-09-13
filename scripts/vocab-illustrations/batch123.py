# -*- coding: utf-8 -*-
"""第123回。建物のまわり・体の中・un-/non- の形容詞。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))
BRN='#8b6437'
def table(y=300):
    return (f'<path d="M40 {y}h520v20H40z" fill="#c9a464" class="o"/>'
            f'<path d="M80 {y+20}v60M520 {y+20}v60" stroke="#a0764a" stroke-width="14" stroke-linecap="round" fill="none"/>')
def split():
    return f'<path d="M300 20v360" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9" fill="none"/>'
def coin(x, y, r=20):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" class="gold o"/>'
            f'<circle cx="{x}" cy="{y}" r="{r*0.62}" fill="none" stroke="{TONES["gold"][2]}" stroke-width="2.5"/>')
def cross(x, y, s=1, c=None):
    c = c or TONES['coral'][0]
    return (f'<g fill="none" stroke="{c}" stroke-width="{9*s}" stroke-linecap="round">'
            f'<path d="M{x-26*s} {y-26*s}l{52*s} {52*s}M{x+26*s} {y-26*s}l{-52*s} {52*s}"/></g>')
def tick(x, y, s=1):
    return (f'<g fill="none" stroke="{TONES["green"][0]}" stroke-width="{9*s}" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M{x-30*s} {y}l{22*s} {24*s} {42*s}-{52*s}"/></g>')

# --- 建物と物 ---------------------------------------------------------------
add('attic', '屋根裏部屋に古い箱がしまわれている', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<path d="M300 30l260 200H40z" fill="#c8b8a0" class="o"/>
<path d="M300 30l260 200H40z" fill="none" stroke="{INK}" stroke-width="3"/>
<path d="M40 230h520v50H40z" fill="#8b6437" class="o"/>
<path d="M40 280h520v120H40z" fill="#f0eee6" class="o"/>
<g fill="none" stroke="{BRN}" stroke-width="7">
  <path d="M300 60v170M170 150l130 80M430 150L300 230"/>
</g>
<g transform="translate(300 120)">
  <path d="M-40-30h80v60h-80z" fill="#fde39a" class="o"/>
  <path d="M0-30v60M-40 0h80" stroke="{BRN}" stroke-width="4" fill="none"/>
</g>
{box(150, 200, 90, 56, 18, 'gold')}
{box(440, 200, 80, 50, 16, 'teal')}
<g transform="translate(230 208)">
  <path d="M-34-24h68v48h-68z" fill="#a0764a" class="o"/>
  <path d="M-34 0h68" stroke="#6b4c28" stroke-width="4" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M520 330l-100-100"/></g>''', arrow=True, ground=False)

add('bungalow', '二階のない、平屋建ての家', f'''
{split()}
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
<path d="M0 300h600v100H0z" fill="#dfe8d8"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(150 300)">
  <path d="M-100 0v-90h200V0z" fill="#fffdf6" class="o"/>
  <path d="M-116-90L0-160l116 70z" class="coral o"/>
  <path d="M-70-70h50v34h-50zM24-70h50v34h-50z" class="bluep o"/>
  <path d="M-16-40h34V0h-34z" class="corald o"/>
</g>
<g transform="translate(450 300)">
  <path d="M-90 0v-180h180V0z" fill="#fffdf6" class="o"/>
  <path d="M-104-180L0-240l104 60z" class="teal o"/>
  <path d="M-62-160h44v34h-44zM20-160h44v34h-44zM-62-100h44v34h-44zM20-100h44v34h-44z" class="bluep o"/>
  <path d="M-16-40h34V0h-34z" class="teald o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M150 190h-60"/></g>
<g class="a" marker-end="url(#ar)"><path d="M150 190h60"/></g>''', arrow=True, ground=False)

add('boiler', '湯を沸かして家じゅうに送る給湯器', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<path d="M0 350h600v50H0z" fill="#c9a464" class="o"/>
<g transform="translate(240 210)">
  <path d="M-100-140h200v290h-200z" fill="#e0e6ea" class="o"/>
  <path d="M-80-120h160v100h-160z" fill="#3b4450" class="o"/>
  <g fill="{TONES['green'][0]}"><rect x="-60" y="-100" width="16" height="30"/><rect x="-36" y="-100" width="16" height="30"/></g>
  <circle cx="30" cy="-70" r="20" class="coral o"/>
  <g fill="#9aa5b0" class="o"><circle cx="-50" cy="30" r="24"/><circle cx="20" cy="30" r="24"/></g>
  <path d="M-50 30v-14M20 30v-14" stroke="{INK}" stroke-width="4" fill="none"/>
  <path d="M-80 80h160v40h-160z" fill="#c8d0d8" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="16" stroke-linecap="round">
  <path d="M340 120h140v200"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="16" stroke-linecap="round">
  <path d="M340 250h90v70"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M510 250q16-20 0-36M540 260q20-26 0-52"/>
</g>
{flame(240, 340, 0.55)}''', ground=False)

add('bonnet', '車のボンネットを開けてエンジンを見ている', f'''
{table(360)}
<g transform="translate(320 300)">
  <path d="M-190 30h380v-50q0-20-20-20h-90l-40-40h-120l-30 40h-60q-20 0-20 20z" fill="{TONES['teal'][0]}" class="o"/>
  <path d="M-96-40h130l30 40h-190z" fill="#dceaf4" class="o"/>
  <circle cx="-110" cy="30" r="24" fill="{INK}"/><circle cx="110" cy="30" r="24" fill="{INK}"/>
</g>
<g transform="translate(200 250) rotate(-36)">
  <path d="M-100-10h200v20h-200z" fill="{TONES['teal'][2]}" class="o"/>
  <path d="M-100-10h200v6h-200z" fill="{TONES['teal'][1]}"/>
</g>
<g transform="translate(180 288)">
  <path d="M-50-24h100v40h-100z" fill="#5a6270" class="o"/>
  <g fill="#8f9aa6"><rect x="-40" y="-18" width="20" height="28"/><rect x="-12" y="-18" width="20" height="28"/><rect x="16" y="-18" width="20" height="28"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 150l60 60"/></g>''', arrow=True, ground=False)

add('brake', 'ブレーキを踏んで車が止まる', f'''
<path d="M0 250h600v150H0z" fill="#8f9aa6"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="#fffefd" stroke-width="6" stroke-dasharray="34 30"><path d="M0 340h600"/></g>
<g transform="translate(380 300)">
  <path d="M-130 30h260v-46q0-16-16-16h-60l-34-38h-84l-24 38h-42q-16 0-16 16z" class="coral o"/>
  <path d="M-84-32h84l24 38h-132z" fill="#dceaf4" class="o"/>
  <circle cx="-76" cy="30" r="22" fill="{INK}"/><circle cx="76" cy="30" r="22" fill="{INK}"/>
  <circle cx="130" cy="0" r="14" class="corald o"/>
  <g fill="{TONES['coral'][0]}" opacity="0.5"><circle cx="130" cy="0" r="30"/></g>
</g>
<g fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round">
  <path d="M120 330h130M150 300h100M170 270h80"/>
</g>
<g transform="translate(120 180)">
  <path d="M-60-40h120v80h-120z" fill="#e0e6ea" class="o"/>
  <path d="M-26-24h52v40q0 12-26 12t-26-12z" fill="{INK}"/>
  <path d="M-14 30h28v14h-28z" fill="#8f9aa6"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 240v40"/></g>''', arrow=True, ground=False)

add('cage', '鉄の格子のおりに鳥が入っている', f'''
{table(340)}
<g transform="translate(300 220)">
  <path d="M-110 100h220v20h-220z" fill="#8f9aa6" class="o"/>
  <path d="M-110-70h220v170h-220z" fill="#fffdf6" opacity="0.4"/>
  <g fill="none" stroke="{INK}" stroke-width="5">
''' + ''.join(f'<path d="M{-104+i*26} -70v170"/>' for i in range(9)) + f'''
    <path d="M-110-70h220M-110 20h220"/>
  </g>
  <path d="M-110-70q110-70 220 0z" fill="#c8d0d8" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="4">
''' + ''.join(f'<path d="M0-108L{-104+i*35} -70"/>' for i in range(7)) + f'''
  </g>
  <path d="M0-108v-24" stroke="{INK}" stroke-width="5" fill="none"/>
  <circle cy="-140" r="14" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g transform="translate(290 250)">
  <ellipse rx="40" ry="30" class="gold o"/>
  <circle cx="30" cy="-22" r="20" class="gold o"/>
  <path d="M46-26l22 6-22 8z" class="corald o"/>
  <circle cx="34" cy="-26" r="3.5" fill="{INK}"/>
  <path d="M-46 4l-24-14 26-8z" class="goldd o"/>
  <g stroke="{TONES['gold'][2]}" stroke-width="5" stroke-linecap="round" fill="none"><path d="M-10 30v14M14 30v14"/></g>
</g>''', ground=False)

add('claw', '猫の前足から鋭いつめが出ている', f'''
{table(340)}
<g transform="translate(300 240)">
  <ellipse cy="20" rx="110" ry="80" fill="#c8b8a0" class="o"/>
  <g fill="#c8b8a0" class="o">
''' + ''.join(f'<ellipse cx="{-72+i*48}" cy="-46" rx="26" ry="30"/>' for i in range(4)) + f'''
  </g>
  <g fill="#a89880">
    <ellipse cy="34" rx="46" ry="34"/>
''' + ''.join(f'<ellipse cx="{-72+i*48}" cy="-46" rx="14" ry="16"/>' for i in range(4)) + f'''
  </g>
  <g fill="#fffdf6" class="o">
''' + ''.join(f'<path d="M{-72+i*48} -76q-8-40 6-56 16 22 8 56z" transform="rotate({-18+i*12} {-72+i*48} -76)"/>' for i in range(4)) + f'''
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M120 120l40-30M470 110l-40-24"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 200l-90-40"/></g>''', arrow=True, ground=False)

add('beehive', '木の枠の巣箱にミツバチが出入りしている', f'''
<path d="M0 0h600v300H0z" fill="#dceaf4"/>
<path d="M0 300h600v100H0z" fill="#dfe8d8"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(280 300)">
  <path d="M-100 0h200v-40h-200zM-94-40h188v-56h-188zM-94-96h188v-56h-188zM-94-152h188v-56h-188z" fill="#d9b877" class="o"/>
  <path d="M-110-208h220v-24h-220z" fill="#c8703a" class="o"/>
  <path d="M-110-232L0-262l110 30z" fill="#c8703a" class="o"/>
  <path d="M-40-14h80v14h-80z" fill="{INK}"/>
</g>
<g>
''' + ''.join(f'''<g transform="translate({380+i*44} {150+(i%3)*54}) scale(0.5)">
  <ellipse rx="40" ry="26" class="gold o"/>
  <g fill="{INK}"><path d="M-18-24q10 48 0 48zM6-26q10 52 0 52z"/></g>
  <circle cx="-34" cy="-4" r="16" fill="{INK}"/>
  <ellipse cx="4" cy="-30" rx="30" ry="14" fill="#fffefd" stroke="{INK}" stroke-width="3" opacity="0.85" transform="rotate(-22 4 -30)"/>
</g>''' for i in range(4)) + f'''
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7">
  <path d="M370 200q-40 40-90 70"/>
</g>''', ground=False)

add('alligator', '幅の広いU字の口を持つアリゲーターが水辺にいる', f'''
<path d="M0 0h600v230H0z" fill="#cfe0d4"/>
<path d="M0 230h600v170H0z" fill="#7d9a80"/>
<path d="M0 230h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="#6b8a70" stroke-width="4"><path d="M40 300h160M400 340h170"/></g>
<g transform="translate(300 250)">
  <path d="M-230 20q40-40 120-40h100q60 0 90 20 40 26-10 40-90 16-190 6-90-8-110-26z" fill="#5f7a4f" class="o"/>
  <path d="M80-16q80 0 116 20-36 22-116 18-40-4-40-20t40-18z" fill="#5f7a4f" class="o"/>
  <path d="M80 22q80 4 116-2-36 22-116 18-40-4-40-16z" fill="#728f60"/>
  <circle cx="86" cy="-16" r="12" fill="#728f60" class="o"/>
  <circle cx="86" cy="-18" r="5" fill="{INK}"/>
  <g fill="#4e6641">
''' + ''.join(f'<path d="M{-200+i*30} -22l14-22 14 22z"/>' for i in range(9)) + f'''
  </g>
  <path d="M-230 20q-70-6-100 20 76 26 110 4z" fill="#5f7a4f" class="o"/>
  <g stroke="#4e6641" stroke-width="12" stroke-linecap="round" fill="none">
    <path d="M-120 44l-24 26M20 48l24 26"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M480 130l-90 70"/></g>''', arrow=True, ground=False)

# --- 体と学問 ---------------------------------------------------------------
add('antibody', 'Y字形の抗体がウイルスにくっついて働かなくする', f'''
<path d="M0 0h600v400H0z" fill="#eef4f8"/>
<g transform="translate(220 220)">
  <circle r="80" class="corald o"/>
  <g fill="{TONES['coral'][0]}">
''' + ''.join(f'<g transform="rotate({i*30})"><rect x="-7" y="-104" width="14" height="26" rx="7"/><circle cy="-108" r="11"/></g>' for i in range(12)) + f'''
  </g>
  <circle r="40" fill="{TONES['coral'][1]}" opacity="0.5"/>
</g>
<g>
''' + ''.join(f'''<g transform="translate({390+ (i%2)*90} {130+i*80}) rotate({-30+i*30}) scale(1.1)">
  <path d="M0 0v34" stroke="{TONES['blue'][0]}" stroke-width="13" stroke-linecap="round" fill="none"/>
  <path d="M0 0l-30-34M0 0l30-34" stroke="{TONES['blue'][0]}" stroke-width="13" stroke-linecap="round" fill="none"/>
  <circle cx="-30" cy="-34" r="9" class="blued"/><circle cx="30" cy="-34" r="9" class="blued"/>
</g>''' for i in range(3)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M390 220h-70"/></g>''', arrow=True, ground=False)

add('appendix', '本の最後についた付録のページ', f'''
{table(350)}
<g transform="translate(300 200)">
  <path d="M-200-140h400v290h-400z" fill="#fffefd" class="o"/>
  <path d="M-200-140h30v290h-30z" fill="#c8b8a0" class="o"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-140" y="{-110+i*30}" width="{300-(i%3)*40}" height="9" rx="4.5"/>' for i in range(6)) + f'''
  </g>
  <path d="M-150 90h340" stroke="{INK}" stroke-width="3" fill="none"/>
  <rect x="-140" y="106" width="110" height="14" rx="7" class="coral"/>
  <g fill="{TONES['coral'][1]}">
''' + ''.join(f'<rect x="-140" y="{130+i*16}" width="{260-i*40}" height="8" rx="4"/>' for i in range(2)) + f'''
  </g>
</g>
<g transform="translate(470 340) rotate(-8)">
  <path d="M-30-40h60v40h-60z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 290l-90 20"/></g>''', arrow=True, ground=False)

add('applause', '観客がいっせいに拍手を送っている', f'''
<path d="M0 0h600v400H0z" fill="#3b3550"/>
<path d="M0 250h600v150H0z" fill="#2b2740"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 240)">
  <path d="M-140 10h280v-14q0-30-140-30t-140 30z" class="coral o"/>
  <g fill="{TONES['gold'][1]}" opacity="0.3"><path d="M0-40l-160 170h320z"/></g>
</g>
{person(300, 250, 0.9, 1, 'gold', 'violet', 'up', 'bun', 'smile')}
<g>
''' + ''.join(f'''<g transform="translate({50+ (i%6)*100} {330+(i//6)*40})">
  <circle cy="-40" r="20" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS[["short","bob","bun","cap"][i%4]]}" transform="translate(0 68) scale(0.8)" fill="{HAIR}"/>
  <path d="M-34-14q34-16 68 0l-6 54h-56z" fill="{TONES[["teal","coral","blue","violet","green","gold"][i%6]][0]}" class="o"/>
  <g><path d="M-40-30l-16-24" stroke="{SKIN}" stroke-width="9" stroke-linecap="round" fill="none"/>
     <path d="M40-30l16-24" stroke="{SKIN}" stroke-width="9" stroke-linecap="round" fill="none"/>
     <ellipse cx="-58" cy="-58" rx="13" ry="16" fill="{SKIN}" stroke="{SKINL}" stroke-width="2"/>
     <ellipse cx="58" cy="-58" rx="13" ry="16" fill="{SKIN}" stroke="{SKINL}" stroke-width="2"/></g>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="3" stroke-linecap="round">
    <path d="M-74-72l-10-12M74-72l10-12"/></g>
</g>''' for i in range(8)) + f'''
</g>''', ground=False)

add('artefact', '発掘された古い壺が土の中から出てくる', f'''
<path d="M0 0h600v170H0z" fill="#dceaf4"/>
<path d="M0 170h600v230H0z" fill="#a8845c"/>
<path d="M0 158h600v14H0z" fill="#dfe8d8"/>
<path d="M0 158h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="#8f6f4a" stroke-width="3">
  <path d="M0 230h600M0 300h600"/>
</g>
<path d="M180 172q0 130 130 130t130-130z" fill="#6b4c28" class="o"/>
<g transform="translate(310 250)">
  <path d="M-56-40q0-30 56-30t56 30q10 60-6 76-50 14-100 0-16-16-6-76z" fill="#c8703a" class="o"/>
  <path d="M-40-46h80v-14q0-10-40-10t-40 10z" fill="#a8552c" class="o"/>
  <g fill="none" stroke="#8b3a1c" stroke-width="4"><path d="M-52-10h104M-48 18h96"/></g>
  <g fill="#8b3a1c">
''' + ''.join(f'<circle cx="{-36+i*24}" cy="4" r="5"/>' for i in range(4)) + f'''
  </g>
</g>
<g transform="translate(440 190) rotate(28)">
  <path d="M-8-70h16v90h-16z" fill="#c9a464" class="o"/>
  <path d="M-26 20h52l-8 40h-36z" fill="#8f9aa6" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 100q60 60 120 110"/></g>''', arrow=True, ground=False)

add('algorithm', '手順の箱と分岐がつながった流れ図', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(300 60)">
  <path d="M-70-26h140q14 0 14 26t-14 26h-140q-14 0-14-26t14-26z" class="tealp o"/>
  <rect x="-40" y="-7" width="80" height="14" rx="7" fill="{INK}"/>
</g>
<g transform="translate(300 170)">
  <path d="M0-46l70 46-70 46-70-46z" class="goldp o"/>
  <rect x="-30" y="-7" width="60" height="14" rx="7" fill="{INK}"/>
</g>
<g transform="translate(140 290)">
  <path d="M-80-30h160v60h-160z" class="coralp o"/>
  <rect x="-52" y="-7" width="104" height="14" rx="7" fill="{INK}"/>
</g>
<g transform="translate(460 290)">
  <path d="M-80-30h160v60h-160z" class="violetp o"/>
  <rect x="-52" y="-7" width="104" height="14" rx="7" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)">
  <path d="M300 90v34"/>
  <path d="M230 170H140v90"/>
  <path d="M370 170h90v90"/>
  <path d="M140 320v40h320v-40"/>
</g>''', arrow=True, ground=False)

# --- 動作 -------------------------------------------------------------------
add('blaze', '建物が赤々と燃え上がっている', f'''
<path d="M0 0h600v400H0z" fill="#3b2a28"/>
<path d="M0 350h600v50H0z" fill="#2b201e" class="o"/>
<g transform="translate(300 350)">
  <path d="M-140 0v-190h280V0z" fill="#5a4a44" class="o"/>
  <path d="M-140-190L0-260l140 70z" fill="#4a3a34" class="o"/>
  <g fill="#e8983a" class="o">
    <rect x="-100" y="-160" width="60" height="50"/><rect x="-20" y="-160" width="60" height="50"/>
    <rect x="60" y="-160" width="50" height="50"/><rect x="-60" y="-80" width="60" height="50"/><rect x="30" y="-80" width="60" height="50"/>
  </g>
</g>
{flame(200, 180, 1.4)}
{flame(330, 130, 1.7)}
{flame(430, 190, 1.2)}
<g fill="{MUTED}" opacity="0.5">
  <circle cx="180" cy="60" r="40"/><circle cx="290" cy="34" r="50"/><circle cx="400" cy="60" r="42"/>
</g>
<g fill="{TONES['gold'][0]}">
''' + ''.join(f'<circle cx="{120+i*52}" cy="{110+(i%4)*40}" r="{5-(i%3)}"/>' for i in range(9)) + f'''
</g>''', ground=False)

add('brighten', 'うす暗かった部屋が明るくなる', f'''
{split()}
<path d="M0 0h300v400H0z" fill="#4a5560"/>
<path d="M300 0h300v400H300z" fill="#fff6e0"/>
<g transform="translate(150 200)">
  <path d="M0-160v40" stroke="{MUTED}" stroke-width="5" fill="none"/>
  <path d="M-50-120h100l-18 40h-64z" fill="#6f7b88" class="o"/>
  <circle cy="-66" r="20" fill="#8f9aa6" class="o"/>
  <path d="M-90 130h180v20h-180z" fill="#5a6270"/>
  <path d="M-60 70h120v60h-120z" fill="#5a6270" class="o"/>
</g>
<g transform="translate(450 200)">
  <path d="M0-160v40" stroke="{INK}" stroke-width="5" fill="none"/>
  <path d="M-50-120h100l-18 40h-64z" fill="#c8d0d8" class="o"/>
  <circle cy="-66" r="22" class="gold o"/>
  <g fill="{TONES['gold'][1]}" opacity="0.55"><path d="M0-66l-140 216h280z"/></g>
  <g class="golds"><path d="M-46-56l-24 12M46-56l24 12M0-96v-16"/></g>
  <path d="M-90 130h180v20h-180z" fill="#c9a464"/>
  <path d="M-60 70h120v60h-120z" class="coralp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M264 340h72"/></g>''', arrow=True, ground=False)

add('chirp', '小鳥が枝でチッチッと短く鳴いている', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
<path d="M0 330q140 40 300 20t300-30" fill="none" stroke="{BRN}" stroke-width="16" stroke-linecap="round"/>
<g class="greenp o">
  <path d="M120 320q-40-30-20-52 34 12 20 52zM420 300q40-30 62-8-30 30-62 8z"/>
</g>
<g transform="translate(250 280)">
  <ellipse rx="46" ry="36" class="gold o"/>
  <circle cx="34" cy="-28" r="24" class="gold o"/>
  <path d="M52-34l24 8-24 8z" class="corald o"/>
  <circle cx="38" cy="-32" r="3.5" fill="{INK}"/>
  <path d="M-50 6l-28-16 30-8z" class="goldd o"/>
  <path d="M-6-10q30-16 44 4-28 22-44-4z" class="goldd o"/>
  <g stroke="{TONES['gold'][2]}" stroke-width="5" stroke-linecap="round" fill="none"><path d="M-10 34v14M14 34v14"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M340 200q26 30 0 60M386 176q40 54 0 108M432 152q54 78 0 156"/>
</g>
<g fill="{TONES['coral'][0]}"><circle cx="330" cy="180" r="6"/><circle cx="360" cy="140" r="5"/></g>''', ground=False)

add('chuckle', '本を読みながら声を殺して含み笑いをしている', f'''
{table(360)}
{sit(280, 360, 1.15, 1, 'teal', 'blue', 'short', 'smile', 'lap')}
{chair(280, 360, 1.05, 'gold', 1)}
<g transform="translate(320 250) rotate(-12)">
  <path d="M-70-50h140v100h-140z" fill="#fffefd" class="o"/>
  <path d="M0-50v100" stroke="{INK}" stroke-width="3" fill="none"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="{-58+ (i%2)*62}" y="{-34+(i//2)*22}" width="46" height="7" rx="3.5"/>' for i in range(6)) + f'''
  </g>
</g>
<g transform="translate(280 250)">
  <path d="M-14 10q16 8 30-2" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M200 210q-16-14 0-26M180 250l-22-10"/>
</g>
<g transform="translate(140 170)">
  <path d="M-34-24h68q10 0 10 10v28q0 10-10 10h-46l-18 14v-14q-14 0-14-10v-28q0-10 10-10z" fill="#fffefd" class="o"/>
  <g fill="{TONES['gold'][0]}"><circle cx="-14" cy="0" r="5"/><circle cx="2" cy="0" r="5"/><circle cx="18" cy="0" r="5"/></g>
</g>''', ground=False)

# --- 形容詞 -------------------------------------------------------------------
add('unarmed', '武器を持った人と、両手を開いた武器のない人', f'''
{split()}
{table(370)}
{person(150, 370, 1.15, 1, 'blue', 'blue', 'reach', 'cap', 'neutral')}
<g transform="translate(196 268) rotate(-24)">
  <path d="M-70-8h130v16h-130z" fill="#5a6270" class="o"/>
  <path d="M-70-12h-30v24h30z" fill="{INK}"/>
  <path d="M20 8h30v34h-30z" fill="#8b6437" class="o"/>
</g>
{person(450, 370, 1.15, 1, 'coral', 'blue', 'up', 'short', 'smile')}
{hand(404, 236, -1)}
{hand(496, 236, 1)}
{cross(150, 120, 0.9)}
{tick(450, 120, 0.9)}''', ground=False)

add('understaffed', 'たくさんの客に対して店員がひとりしかいない', f'''
{table(360)}
<g transform="translate(300 300)">
  <path d="M-230-40h460v40h-460z" fill="#c9a464" class="o"/>
  <path d="M-230-40h460v-14h-460z" fill="#a0764a"/>
</g>
{person(300, 280, 0.9, 1, 'teal', 'blue', 'reach', 'bun', 'sad')}
<g>
''' + ''.join(person(60+ (i%7)*82, 380+ (i//7)*0, 0.72, -1 if i%2 else 1, ['coral','gold','violet','green','blue','coral','gold'][i%7], 'blue', 'stand', ['short','bob','bun','cap'][i%4], 'neutral') for i in range(7)) + f'''
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M256 190q-16-14 0-26M344 186q16-14 0-26"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 250q80-40 150-10"/></g>''', arrow=True, ground=False)

add('underweight', '体重計の針が標準より下を指している', f'''
{table(370)}
{person(250, 330, 1.05, 1, 'coral', 'blue', 'stand', 'bob', 'sad')}
<g transform="translate(250 350)">
  <path d="M-90-24h180v24q0 12-16 12h-148q-16 0-16-12z" fill="#c8d0d8" class="o"/>
  <path d="M-90-24q0-16 90-16t90 16z" fill="#e0e6ea" class="o"/>
</g>
<g transform="translate(450 220)">
  <circle r="90" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
''' + ''.join(f'<path d="M{72*math.cos(math.pi*(0.75+i*0.083)):.0f} {72*math.sin(math.pi*(0.75+i*0.083)):.0f}L{86*math.cos(math.pi*(0.75+i*0.083)):.0f} {86*math.sin(math.pi*(0.75+i*0.083)):.0f}"/>' for i in range(19)) + f'''
  </g>
  <path d="M-62-62A88 88 0 0 1 62-62" fill="none" stroke="{TONES['green'][0]}" stroke-width="8" transform="rotate(0)"/>
  <path d="M0 0l-58-40" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round" fill="none"/>
  <circle r="9" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M450 330v-40"/></g>''', arrow=True, ground=False)

add('unfit', '息切れして走れない人と、軽々と走る人', f'''
{split()}
{table(370)}
{person(150, 370, 1.1, 1, 'gold', 'blue', 'stand', 'short', 'sad')}
<g fill="{TONES['blue'][0]}"><path d="M120 220q10 12 10 20t-10 8-10-8 10-20z"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M196 244q20-10 34 2M204 268q22-8 36 6"/>
</g>
{person(450, 370, 1.1, 1, 'teal', 'coral', 'walk', 'cap', 'smile', 'walk')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M370 240h50M356 280h40"/>
</g>
{cross(150, 110, 0.85)}
{tick(450, 110, 0.85)}''', ground=False)

add('unidentified', '顔がぼかされ、誰なのか分からない人物', f'''
{table(370)}
{person(300, 370, 1.3, 1, 'violet', 'blue', 'stand', 'short', 'neutral')}
<g transform="translate(300 230)">
  <circle r="46" fill="{MUTED}"/>
  <circle r="34" fill="#9aa5b0"/>
  <circle r="22" fill="#b0b8c0"/>
</g>
<g transform="translate(300 226)">
  <path d="M-16-28q0-28 16-28t16 28-16 22v14" fill="none" stroke="#fffefd" stroke-width="8" stroke-linecap="round"/>
  <circle cy="26" r="5" fill="#fffefd"/>
</g>
<g transform="translate(470 150)">
  <path d="M-56-40h112v80h-112z" class="paper"/>
  <circle cy="-10" r="18" fill="{MUTED}"/>
  <g fill="{MUTED}"><rect x="-36" y="16" width="72" height="8" rx="4"/></g>
  {cross(0, -10, 0.7)}
</g>''', ground=False)

add('unrealistic', '一晩で山を動かすという、ありえない計画', f'''
{table(370)}
<g transform="translate(430 370)">
  <path d="M-180 0l90-160 60 60 70-100 100 200z" fill="#8f9aa6" class="o"/>
  <path d="M50-200l-24 40h48z" fill="#fffefd" class="o"/>
</g>
{person(140, 370, 1.05, 1, 'coral', 'blue', 'reach', 'cap', 'smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8">
  <path d="M200 260q80-80 200-60"/>
</g>
<g transform="translate(180 130)">
  <path d="M-56-40h112q12 0 12 12v44q0 12-12 12h-76l-24 18v-18q-12 0-12-12v-44q0-12 12-12z" fill="#fffefd" class="o"/>
  <path d="M-30 10l60-46M-30-36l60 46" stroke="{MUTED}" stroke-width="4" fill="none"/>
  <g fill="{MUTED}"><rect x="-40" y="-30" width="60" height="7" rx="3.5"/></g>
</g>
{cross(470, 130, 1.2)}''', ground=False)

add('upbeat', 'うつむいた顔と、顔を上げて前向きな顔', f'''
{split()}
{table(370)}
{person(150, 370, 1.15, 1, 'blue', 'blue', 'stand', 'bob', 'sad')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M200 210l24-14M100 210l-24-14"/>
</g>
<g fill="{MUTED}" opacity="0.4"><ellipse cx="150" cy="150" rx="70" ry="34"/></g>
{person(450, 370, 1.15, 1, 'coral', 'gold', 'up', 'bob', 'smile')}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{450+120*math.cos(3.14+i*0.5):.0f} {230+120*math.sin(3.14+i*0.5):.0f}l{20*math.cos(3.14+i*0.5):.0f} {20*math.sin(3.14+i*0.5):.0f}"/>' for i in range(7)) + f'''
</g>''', ground=False)

add('upright', '傾いた柱と、まっすぐ立った柱', f'''
{split()}
{table(370)}
<g transform="translate(150 370) rotate(-18)">
  <path d="M-30-220h60v220h-60z" fill="#c9a464" class="o"/>
  <g fill="none" stroke="#a0764a" stroke-width="3"><path d="M0-220v220"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M150 370V140"/></g>
<g transform="translate(450 370)">
  <path d="M-30-220h60v220h-60z" fill="#c9a464" class="o"/>
  <g fill="none" stroke="#a0764a" stroke-width="3"><path d="M0-220v220"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="4"><path d="M420 340h30v-30" /></g>
{cross(150, 90, 0.8)}
{tick(450, 90, 0.8)}''', ground=False)

add('versatile', '一本の道具がねじにもナットにも栓抜きにも使える', f'''
{table(340)}
<g transform="translate(300 220)">
  <path d="M-30-90h60v190h-60z" class="coral o"/>
  <path d="M-30-90q0-24 30-24t30 24z" class="corald o"/>
  <circle cy="-70" r="9" fill="{INK}"/>
</g>
<g transform="translate(180 190) rotate(-40)">
  <path d="M-10-70h20v90h-20z" fill="#c8d0d8" class="o"/>
  <path d="M-16-70l6-16h20l6 16z" fill="#9aa5b0" class="o"/>
</g>
<g transform="translate(420 190) rotate(40)">
  <path d="M-10-70h20v90h-20z" fill="#c8d0d8" class="o"/>
  <path d="M-24-70h48l-10 22h-28z" fill="#9aa5b0" class="o"/>
  <path d="M-8-52h16v14h-16z" fill="#e8e2d6"/>
</g>
<g transform="translate(170 300) rotate(-70)">
  <path d="M-10-60h20v80h-20z" fill="#c8d0d8" class="o"/>
  <path d="M-20-60h40v20h-40z" fill="#9aa5b0" class="o"/>
  <circle cy="-50" r="7" fill="#e8e2d6"/>
</g>
<g transform="translate(430 300) rotate(70)">
  <path d="M-8-60h16v80h-16z" fill="#c8d0d8" class="o"/>
  <path d="M-16-64h32v18h-32z" fill="#9aa5b0" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 130q50-30 100 0"/></g>''', arrow=True, ground=False)

add('volcanic', '火山灰と溶岩でできた黒い岩の大地', f'''
<path d="M0 0h600v400H0z" fill="#6b4a52"/>
<path d="M0 240h600v160H0z" fill="#3b3238" class="o"/>
<path d="M0 400l180-200 60 60 100-120 120 130 140 130z" fill="#2b2429" class="o"/>
<path d="M240 200l-24 30h48z" class="coral o"/>
<g class="coral o">
  <path d="M340 140q40 60 60 200h-40q-20-130-40-170z"/>
</g>
<g fill="{MUTED}" opacity="0.6">
  <circle cx="300" cy="70" r="46"/><circle cx="380" cy="50" r="38"/><circle cx="230" cy="60" r="34"/>
</g>
<g fill="#1e1a1e" class="o">
  <path d="M80 340l40-20 30 30-40 20z"/><path d="M470 320l44-16 24 34-46 14z"/><path d="M200 370l36-14 22 26-38 12z"/>
</g>
<g fill="{TONES['coral'][0]}">
  <circle cx="140" cy="240" r="7"/><circle cx="470" cy="220" r="6"/><circle cx="90" cy="290" r="5"/>
</g>''', ground=False)

add('tangible', '約束の言葉と、手で持てる契約書', f'''
{split()}
{table(370)}
<g transform="translate(150 190)">
  <path d="M-80-50h160q14 0 14 14v56q0 14-14 14h-110l-30 22v-22q-14 0-14-14v-56q0-14 14-14z" fill="#fffefd" class="o" opacity="0.5"/>
  <g fill="{MUTED}" opacity="0.6"><rect x="-60" y="-28" width="110" height="9" rx="4.5"/><rect x="-60" y="-8" width="80" height="9" rx="4.5"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><circle cx="150" cy="190" r="120"/></g>
<g transform="translate(450 210) rotate(-6)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-66" y="{-84+i*26}" width="{132-(i%3)*30}" height="8" rx="4"/>' for i in range(5)) + f'''
  </g>
  <path d="M-60 60q40-24 66 0t50-10" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"/>
  <circle cx="56" cy="82" r="20" class="coral o"/>
</g>
{hand(370, 300, 1)}''', ground=False)

add('territorial', '犬が自分の縄張りに線を引いて他を寄せつけない', f'''
{table(370)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="16 12">
  <path d="M300 30v340"/>
</g>
<g transform="translate(180 320)">
  <ellipse rx="70" ry="44" fill="#c8a070" class="o"/>
  <circle cx="60" cy="-40" r="34" fill="#c8a070" class="o"/>
  <path d="M40-62q-10-40 6-42 16 6 12 42zM74-62q10-38 26-32 8 12-10 34z" fill="#a8804c" class="o"/>
  <path d="M84-32l24 8-24 10z" fill="#a8804c" class="o"/>
  <circle cx="70" cy="-42" r="3.5" fill="{INK}"/>
  <path d="M78-24q14 16 0 18t-10-18z" class="corald o"/>
  <path d="M-70-6q-40-30-54 0 34 26 54 8z" fill="#c8a070" class="o"/>
  <g stroke="#a8804c" stroke-width="10" stroke-linecap="round" fill="none"><path d="M-30 42v22M20 42v22"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M266 250q-16-14 0-26M250 200l-20-14"/>
</g>
{person(460, 370, 0.9, -1, 'teal', 'blue', 'walk', 'bob', 'sad', 'walk')}
<g class="a" marker-end="url(#ar)"><path d="M400 200h130"/></g>''', arrow=True, ground=False)

add('treacherous', '見た目は平らだが、薄い氷の下が割れている道', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v170H0z" fill="#cfe0ec"/>
<path d="M0 230h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M0 260h600v140H0z" fill="#e8f0f6" class="o"/>
<g fill="none" stroke="#9fc4dd" stroke-width="3">
  <path d="M60 300q60 30 130 10t130 20 140-30"/>
  <path d="M40 356q80-20 160 6t180-16 180 20"/>
</g>
<g fill="#4d7fa4" class="o">
  <path d="M300 290l50 20-14 50-60-14-6-40z"/>
</g>
<g fill="none" stroke="{TONES['blue'][2]}" stroke-width="4">
  <path d="M300 290l-40-20M350 310l50-16M336 360l30 34M276 346l-50 26"/>
</g>
{person(140, 260, 0.9, 1, 'coral', 'blue', 'walk', 'bob', 'smile', 'walk')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M420 140v70M420 240v14"/>
</g>
<circle cx="420" cy="180" r="60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>''', ground=False)

add('truthful', 'うそをつく人と、事実をそのまま話す人', f'''
{split()}
{table(370)}
{person(150, 370, 1.1, 1, 'blue', 'blue', 'stand', 'short', 'neutral')}
<g transform="translate(174 246)">
  <path d="M0 0q40 10 66 0" stroke="{SKIN}" stroke-width="16" stroke-linecap="round" fill="none"/>
  <path d="M0 0q40 10 66 0" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
</g>
{cross(150, 120, 0.8)}
{person(450, 370, 1.1, 1, 'coral', 'blue', 'stand', 'bob', 'smile')}
<g transform="translate(450 180)">
  <path d="M-56-36h112q12 0 12 12v40q0 12-12 12h-80l-22 16v-16q-10 0-10-12v-40q0-12 10-12z" fill="#fffefd" class="o"/>
  <g fill="{INK}"><rect x="-38" y="-16" width="76" height="9" rx="4.5"/><rect x="-38" y="2" width="56" height="9" rx="4.5"/></g>
</g>
{tick(450, 120, 0.8)}''', ground=False)

add('steadfast', '強い風の中でも旗を持って動かず立ち続ける', f'''
<path d="M0 0h600v400H0z" fill="#c8d2da"/>
{table(370)}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M20 120q90-26 170 0t170-8M20 200q90-26 170 0t170-8M20 280q80-24 150 0"/>
</g>
{person(330, 370, 1.3, 1, 'teal', 'blue', 'hold', 'cap', 'neutral')}
<g transform="translate(356 210)">
  <path d="M0 130V-90" stroke="{BRN}" stroke-width="9" stroke-linecap="round" fill="none"/>
  <path d="M4-90q60 10 100-10 6 40-4 60-50 16-96 4z" class="coral o"/>
</g>
<g transform="translate(330 370)">
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6"><path d="M-60 0h120"/></g>
</g>
<g fill="{MUTED}" opacity="0.5"><ellipse cx="330" cy="374" rx="60" ry="10"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}"><path d="M470 300v-70"/></g>''', arrow=True, ground=False)

add('shrewd', 'カードの裏を読み切って有利な手を選ぶ', f'''
{table(340)}
{sit(300, 340, 1.1, 1, 'violet', 'blue', 'short', 'smile', 'lap')}
<g transform="translate(300 250)">
''' + ''.join(f'<g transform="translate({-70+i*35} {(abs(i-2))*8}) rotate({-24+i*12})"><path d="M-26-40h52v80h-52z" fill="#fffefd" class="o"/><circle cy="-16" r="8" class="coral"/></g>' for i in range(5)) + f'''
</g>
<g transform="translate(300 218)">
  <path d="M-24-10q10-10 22 0M2-10q10-10 22 0" fill="none" stroke="{HAIR}" stroke-width="5" stroke-linecap="round"/>
  <path d="M-14 14q16 8 30-4" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
</g>
<g transform="translate(460 170)">
  <path d="M-56-40h112q12 0 12 12v40q0 12-12 12h-80l-24 18v-18q-8 0-8-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <g fill="{INK}"><path d="M-30-12l16 20 30-36" fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></g>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M190 170l-24-16M170 220l-28-6"/>
</g>''', ground=False)

add('resourceful', '道具がなくても身近な物で代わりを作って直す', f'''
{table(340)}
<g transform="translate(300 250)">
  <path d="M-120-40h240v90h-240z" fill="#c8d0d8" class="o"/>
  <path d="M-40-40v90" stroke="{INK}" stroke-width="4" fill="none"/>
  <path d="M-40-16h-60" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round" fill="none"/>
</g>
<g transform="translate(210 226) rotate(-20)">
  <path d="M-40-8h80v16h-80z" fill="#c9a464" class="o"/>
</g>
<g transform="translate(150 300)">
  <path d="M-40-30h80v60h-80z" fill="#8f9aa6" class="o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M-30 0h60"/></g>
</g>
{person(470, 340, 1.0, -1, 'gold', 'blue', 'reach', 'bun', 'smile')}
<g transform="translate(430 190)">
  <path d="M-40-30h80q10 0 10 10v34q0 10-10 10h-56l-16 14v-14q-18 0-18-10v-34q0-10 10-10z" fill="#fffefd" class="o"/>
  <g fill="{TONES['gold'][0]}"><path d="M0-20q22 0 22 20t-12 20v8h-20v-8q-12 0-12-20t22-20z"/></g>
</g>''', ground=False)

add('reactive', '火が出てから消す人と、先に消火器を備える人', f'''
{split()}
{table(370)}
{flame(150, 250, 1.0)}
{person(150, 370, 0.95, 1, 'coral', 'blue', 'up', 'short', 'sad')}
<g transform="translate(450 250)">
  <path d="M-30-60h60v120q0 14-30 14t-30-14z" class="coral o"/>
  <path d="M-14-60v-20h28v20z" fill="{INK}"/>
  <path d="M14-70q30 0 30 20" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
{person(500, 370, 0.9, -1, 'teal', 'blue', 'stand', 'bob', 'smile')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M150 130v40"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}"><path d="M450 130v40"/></g>''', ground=False)

add('prohibitive', '値札の金額が高すぎて手が出ない', f'''
{table(340)}
<g transform="translate(230 240)">
  <path d="M-80-60h160v130h-160z" class="tealp o"/>
  <path d="M-80-60l24-24h160l-24 24z" fill="{TONES['teal'][1]}" class="o"/>
  <path d="M80-60l24-24v130l-24 24z" class="teal o"/>
</g>
<g transform="translate(390 190) rotate(-14)">
  <path d="M-70-46h110l30 46-30 46H-70z" fill="#fffdf6" class="o"/>
  <circle cx="40" r="10" fill="none" stroke="{INK}" stroke-width="4"/>
  <g fill="{INK}"><rect x="-56" y="-22" width="78" height="14" rx="7"/><rect x="-56" y="4" width="88" height="14" rx="7"/></g>
</g>
{person(500, 340, 0.95, -1, 'coral', 'blue', 'reach', 'bob', 'sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M436 280l40 40M476 280l-40 40"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M330 110l20-24M400 96l6-26M460 116l24-22"/>
</g>''', ground=False)

add('pragmatic', '理想の完璧な図面と、実際に作れる簡素な形', f'''
{split()}
{table(370)}
<g transform="translate(150 200)">
  <path d="M-110-120h220v240h-220z" fill="#e1edfb" class="o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3">
    <path d="M-70 90V-40l70-50 70 50v130z"/>
    <path d="M-40 90V20h30v70M20 20h40v40H20z"/>
''' + ''.join(f'<path d="M{-100+i*24} -110v220"/>' for i in range(9)) + f'''
  </g>
</g>
<g transform="translate(450 300)">
  <path d="M-90 0v-90h180V0z" fill="#fffdf6" class="o"/>
  <path d="M-104-90L0-150l104 60z" class="coral o"/>
  <path d="M-20-50h40V0h-40z" class="corald o"/>
  <path d="M-60-64h34v28h-34z" class="bluep o"/>
</g>
{tick(450, 100, 0.9)}
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('petty', 'ささいな汚れひとつを大げさに言い立てている', f'''
{table(340)}
<g transform="translate(340 250)">
  <path d="M-140-70h280v140h-280z" fill="#fffdf6" class="o"/>
  <circle cx="60" cy="30" r="5" class="coral"/>
  <circle cx="60" cy="30" r="34" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
  <path d="M84 54l40 40" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round" fill="none"/>
</g>
{person(130, 340, 1.0, 1, 'violet', 'blue', 'point', 'bun', 'sad')}
<g transform="translate(200 180)">
  <path d="M-40-30h80q10 0 10 10v30q0 10-10 10h-56l-18 14v-14q-16 0-16-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <g fill="{TONES['coral'][0]}"><rect x="-26" y="-12" width="52" height="9" rx="4.5"/><rect x="-26" y="4" width="34" height="9" rx="4.5"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M96 200l-24-18M80 250l-28-6"/>
</g>''', ground=False)

add('outlandish', 'そろいの服の中に、とんでもなく奇抜な格好の人がいる', f'''
{table(370)}
''' + ''.join(person(80+i*90, 370, 0.9, 1, 'blue', 'blue', 'stand', 'short', 'neutral') for i in [0,1,3,4]) + f'''
{person(350, 370, 1.0, 1, 'coral', 'green', 'up', 'bun', 'smile')}
<g transform="translate(350 230)">
  <path d="M-70 0h140v12h-140z" class="gold o"/>
  <path d="M-40-90q40-40 80 0-14 60-40 60t-40-60z" class="violet o"/>
  <g fill="{TONES['gold'][0]}">
''' + ''.join(f'<circle cx="{-40+ i*20}" cy="{-100 - (i%3)*20}" r="10"/>' for i in range(5)) + f'''
  </g>
  <path d="M0-150v-26" stroke="{INK}" stroke-width="4" fill="none"/>
  <circle cy="-182" r="12" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M270 200l-26-20M440 190l26-22"/>
</g>''', ground=False)

add('nonverbal', '言葉を使わず、身ぶりだけで伝えている', f'''
{table(370)}
{person(180, 370, 1.1, 1, 'teal', 'blue', 'up', 'bob', 'smile')}
{hand(120, 236, -1)}
{hand(240, 236, 1)}
{person(440, 370, 1.05, -1, 'coral', 'violet', 'stand', 'short', 'smile')}
<g transform="translate(300 130)">
  <path d="M-70-40h140q12 0 12 12v44q0 12-12 12h-96l-24 18v-18q-12 0-12-12v-44q0-12 12-12z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}"><rect x="-46" y="-16" width="90" height="9" rx="4.5"/><rect x="-46" y="4" width="60" height="9" rx="4.5"/></g>
  {cross(0, -4, 0.85)}
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M260 250q40-30 110-20"/></g>''', ground=False)

add('nonprofit', '売上を配当せず、すべて活動に回す団体', f'''
{table(370)}
<g transform="translate(300 210)">
  <circle r="86" fill="none" stroke="{TONES['green'][0]}" stroke-width="10"/>
  <path d="M0-46q40 0 40 34T0 40q-40-18-40-52 0-34 40-34z" class="coral o"/>
  <path d="M-24-16q30-30 48 0-24 34-48 0z" fill="#fffefd" opacity="0.5"/>
</g>
<g transform="translate(120 300)">
  <path d="M-50-30h100v60h-100z" class="greenp o"/>
  <circle r="18" fill="none" stroke="{TONES['green'][2]}" stroke-width="3"/>
</g>
<g transform="translate(480 300)">
  <path d="M-50-30h100v60h-100z" class="greenp o"/>
  <circle r="18" fill="none" stroke="{TONES['green'][2]}" stroke-width="3"/>
  {cross(0, 0, 0.8)}
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}"><path d="M170 270q60-50 120-30"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M370 250q60-20 90 20"/></g>''', ground=False)

add('negligible', '山ほどの粒の横にある、数えるほどの粒', f'''
{split()}
{table(370)}
<g fill="{TONES['teal'][0]}" class="o">
''' + ''.join(f'<circle cx="{60+ (i%13)*16}" cy="{360-(i//13)*24}" r="9"/>' for i in range(78)) + f'''
</g>
<g fill="{TONES['coral'][0]}" class="o">
  <circle cx="440" cy="356" r="9"/><circle cx="462" cy="358" r="9"/><circle cx="452" cy="338" r="9"/>
</g>
<circle cx="452" cy="350" r="60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"/>
<g class="a" marker-end="url(#ar)"><path d="M452 200v70"/></g>''', arrow=True, ground=False)

add('measurable', 'ものさしを当てて長さをはっきり数値で示す', f'''
{table(340)}
<g transform="translate(300 240)">
  <path d="M-200-30h400v60h-400z" class="goldp o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">
''' + ''.join(f'<path d="M{-190+i*20} -30v{20 if i%5 else 34}"/>' for i in range(20)) + f'''
  </g>
</g>
<g transform="translate(230 170)">
  <path d="M-90-40h180v70h-180z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M140 130h180"/></g>
<g class="a" marker-end="url(#ar)"><path d="M320 130H140"/></g>
<g transform="translate(450 130)">
  <path d="M-56-30h112v60h-112z" class="paper"/>
  <g fill="{INK}"><rect x="-36" y="-8" width="72" height="16" rx="8"/></g>
</g>''', arrow=True, ground=False)

add('lucrative', '小さな店から大きな利益が上がっている', f'''
{table(370)}
<g transform="translate(180 370)">
  <path d="M-90 0v-110h180V0z" fill="#fffdf6" class="o"/>
  <path d="M-104-110h208v-24h-208z" class="teal o"/>
  <path d="M-60-90h56v50h-56z" class="bluep o"/>
  <path d="M20-70h40V0H20z" class="teald o"/>
</g>
<g transform="translate(420 250)">
  <path d="M-110 100h220v20h-220z" fill="{MUTED}"/>
  <g class="green o">
    <rect x="-96" y="50" width="44" height="50"/><rect x="-44" y="10" width="44" height="90"/>
    <rect x="8" y="-40" width="44" height="140"/><rect x="60" y="-100" width="44" height="200"/>
  </g>
  <g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M-100 70L96-90"/></g>
</g>
{coin(300, 320, 22)}
{coin(340, 350, 18)}
{coin(266, 356, 16)}''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
