# -*- coding: utf-8 -*-
"""第126回。表情・音・歩き方。似た音の語(squeak/squeal/screech)は音源そのものを変えて描き分ける。"""
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
def cross(x, y, s=1):
    return (f'<g fill="none" stroke="{TONES["coral"][0]}" stroke-width="{9*s}" stroke-linecap="round">'
            f'<path d="M{x-26*s} {y-26*s}l{52*s} {52*s}M{x+26*s} {y-26*s}l{-52*s} {52*s}"/></g>')
def tick(x, y, s=1):
    return (f'<g fill="none" stroke="{TONES["green"][0]}" stroke-width="{9*s}" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M{x-30*s} {y}l{22*s} {24*s} {42*s}-{52*s}"/></g>')
def sound(x, y, n=3, c=None, s=1, f=1):
    """音を表す弧。f=-1 で左向き。"""
    c = c or TONES['coral'][0]
    return (f'<g fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round" transform="translate({x} {y}) scale({f} 1)">'
            + ''.join(f'<path d="M0 {-30*s*(i+1)/1.6:.0f}q{34*s*(i+1)/1.6:.0f} {30*s*(i+1)/1.6:.0f} 0 {60*s*(i+1)/1.6:.0f}"/>' for i in range(n)) + '</g>')

# --- 表情 -------------------------------------------------------------------
add('scowl', '眉を強く下げ、口を曲げてにらみつけている', f'''
<g transform="translate(300 200)">
  <circle r="140" fill="{SKIN}" stroke="{SKINL}" stroke-width="4"/>
  <path d="M-104-42q44-34 76 6M104-42q-44-34-76 6" fill="none" stroke="{HAIR}" stroke-width="16" stroke-linecap="round"/>
  <circle cx="-50" cy="6" r="11" fill="{INK}"/><circle cx="50" cy="6" r="11" fill="{INK}"/>
  <path d="M-52 76q52-30 104 0" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>
  <path d="M-24-58q-14-16-34-18M24-58q14-16 34-18" fill="none" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-14 30q14 10 28 0" fill="none" stroke="{SKINL}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M120 60l-30-24M480 60l30-24M100 320l-30 22M500 320l30 22"/>
</g>''', ground=False)

add('smirk', '片方の口角だけを上げて、したり顔で笑っている', f'''
<g transform="translate(300 200)">
  <circle r="140" fill="{SKIN}" stroke="{SKINL}" stroke-width="4"/>
  <path d="M-100-52q40-20 70-4M100-52q-40-20-70-4" fill="none" stroke="{HAIR}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-70 0q20-16 40 0M30 0q20-16 40 0" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
  <path d="M-40 74q46 10 84-26" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>
  <path d="M50 44q14 4 18 12" fill="none" stroke="{SKINL}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M470 100l30-24M500 200h34M470 300l30 24"/>
</g>''', ground=False)

add('sob', '肩をふるわせて声を上げてすすり泣く', f'''
{table(380)}
{sit(300, 380, 1.25, 1, 'blue', 'blue', 'bob', 'sad', 'up')}
<g transform="translate(300 232)">
  <path d="M-26-8q12-14 24 0M2-8q12-14 24 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
</g>
<g fill="{TONES['blue'][0]}" stroke="{TONES['blue'][2]}" stroke-width="2">
  <path d="M258 260q10 12 10 20t-10 8-10-8 10-20z"/><path d="M254 306q9 11 9 18t-9 7-9-7 9-18z"/>
  <path d="M344 264q10 12 10 20t-10 8-10-8 10-20z"/><path d="M348 310q9 11 9 18t-9 7-9-7 9-18z"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M180 260q-18 12-18 30M420 256q18 12 18 30"/>
</g>
{sound(470, 200, 3, TONES['blue'][0], 0.9, 1)}
{sound(130, 200, 3, TONES['blue'][0], 0.9, -1)}''', ground=False)

add('tasty', 'ひと口食べて、おいしさに満足してうなずく', f'''
{table(350)}
<g transform="translate(220 210)">
  <circle r="96" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-84-28q6-70 84-70t84 70q-40-32-84-32t-84 32z" fill="{HAIR}"/>
  <path d="M-56 6q18-16 34 0M22 6q18-16 34 0" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <path d="M-26 48q26 24 52 0" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M350 130l24-24M366 210h30M350 290l24 24"/>
</g>
<g transform="translate(470 300)">
  <ellipse rx="80" ry="22" fill="#fffdf6" class="o"/>
  <path d="M-80 0q0 28 80 28t80-28z" fill="#fffdf6" class="o"/>
  <path d="M-40-14q40-26 80-2 4 22-24 26-48 4-56-24z" class="gold o"/>
</g>
<g transform="translate(300 300) rotate(-30)">
  <path d="M-6-70h12v100h-12z" fill="#c8d0d8" class="o"/>
  <path d="M-20-70q0 26 8 26M0-70v26M20-70q0 26-8 26" fill="none" stroke="#c8d0d8" stroke-width="6" stroke-linecap="round"/>
</g>''', ground=False)

add('under-the-weather', '毛布にくるまり熱をはかって、なんとなく体調が悪い', f'''
<path d="M0 0h600v400H0z" fill="#dfe4ea"/>
{table(380)}
{sit(280, 380, 1.2, 1, 'violet', 'blue', 'bob', 'sad', 'lap')}
<g transform="translate(280 330)">
  <path d="M-90-56q90-30 180 0 10 60-16 84-70 20-148 0-24-24-16-84z" class="violetp o"/>
  <g fill="none" stroke="{TONES['violet'][0]}" stroke-width="3"><path d="M-74-16h150M-70 20h142"/></g>
</g>
{thermometer(430, 260, 0.85, 0.55)}
{cloud(280, 96, 1.1, 'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
''' + ''.join(f'<path d="M{224+i*34} {150+(i%3)*18}l-10 26"/>' for i in range(5)) + f'''
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M180 230q-16 12-16 28M382 226q16 12 16 28"/>
</g>''', ground=False)

# --- 音 ---------------------------------------------------------------------
add('squeak', 'ネズミがチューッと小さく高い声で鳴く', f'''
{table(360)}
<g transform="translate(240 320)">
  <ellipse rx="66" ry="42" fill="#b0b8c0" class="o"/>
  <circle cx="58" cy="-22" r="28" fill="#b0b8c0" class="o"/>
  <circle cx="42" cy="-52" r="22" fill="#b0b8c0" class="o"/>
  <circle cx="42" cy="-52" r="12" class="coralp"/>
  <circle cx="70" cy="-26" r="4" fill="{INK}"/>
  <circle cx="86" cy="-14" r="5" fill="{SKINL}"/>
  <g fill="none" stroke="{SKINL}" stroke-width="2.5"><path d="M86-20l24-10M86-8l26 4M84-14h26"/></g>
  <path d="M-66 6q-56-16-70 22 50 20 70-6z" fill="none" stroke="{MUTED}" stroke-width="6"/>
  <g stroke="{MUTED}" stroke-width="7" stroke-linecap="round" fill="none"><path d="M-20 40v14M20 40v14"/></g>
</g>
{sound(360, 250, 3, TONES['coral'][0], 0.8, 1)}
<g transform="translate(500 250)">
  <path d="M-40-60h80v120h-80z" fill="{BRN}" class="o"/>
  <circle cx="-24" r="8" class="gold o"/>
</g>''', ground=False)

add('squeal', 'ブタがキーッと甲高い声を上げる', f'''
{table(340)}
<g transform="translate(230 290)">
  <ellipse rx="96" ry="62" fill="#f0c8c8" class="o"/>
  <circle cx="86" cy="-30" r="42" fill="#f0c8c8" class="o"/>
  <ellipse cx="124" cy="-18" rx="22" ry="17" fill="#e0a8a8" class="o"/>
  <g fill="#c88a8a"><circle cx="118" cy="-18" r="4"/><circle cx="130" cy="-18" r="4"/></g>
  <circle cx="92" cy="-42" r="4" fill="{INK}"/>
  <path d="M66-62q-6-34 10-34 14 6 8 34zM106-64q8-32 22-26 6 10-10 28z" fill="#f0c8c8" class="o"/>
  <path d="M-96 0q-40-6-42 22 34 16 42-4z" fill="none" stroke="#e0a8a8" stroke-width="8"/>
  <g stroke="#e0a8a8" stroke-width="12" stroke-linecap="round" fill="none"><path d="M-40 58v18M20 58v18"/></g>
</g>
{sound(400, 240, 4, TONES['coral'][0], 1.2, 1)}''', ground=False)

add('screech', '急ブレーキでタイヤがキーッと路面をこする', f'''
<path d="M0 250h600v150H0z" fill="#6f7b88"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round" opacity="0.7">
  <path d="M40 330h250M40 372h250"/>
</g>
<g transform="translate(400 320)">
  <path d="M-130 30h260v-46q0-16-16-16h-64l-34-38H-84l-24 38h-22q-16 0-16 16z" class="coral o"/>
  <path d="M-80-32h96l30 38h-136z" fill="#dceaf4" class="o"/>
  <circle cx="-70" cy="30" r="24" fill="{INK}"/><circle cx="70" cy="30" r="24" fill="{INK}"/>
</g>
{sound(310, 160, 4, TONES['coral'][0], 1.1, -1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" opacity="0.8">
  <path d="M320 320q-30 20-40 40M356 330q-26 22-30 40"/>
</g>''', ground=False)

add('shove', '人の背中を乱暴に押しのけている', f'''
{table(370)}
{person(190, 370, 1.15, 1, 'blue', 'blue', 'reach', 'short', 'sad')}
{person(400, 370, 1.15, 1, 'coral', 'blue', 'walk', 'bob', 'surprised', 'walk')}
<g>
  <path d="M226 250q60-8 90 4" stroke="{SKIN}" stroke-width="22" stroke-linecap="round" fill="none"/>
  <path d="M226 250q60-8 90 4" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g class="a" marker-end="url(#ar)" stroke-width="6"><path d="M330 200h100"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M470 240l24-18M480 290l26-6"/>
</g>''', ground=False)

add('snatch', '通りすがりにかばんをひったくって走り去る', f'''
{table(370)}
{person(180, 370, 1.05, 1, 'gold', 'blue', 'reach', 'bob', 'surprised')}
{person(420, 370, 1.1, 1, 'violet', 'blue', 'walk', 'cap', 'neutral', 'walk')}
<g transform="translate(370 250) rotate(-16)">
  <path d="M-46-28h92v56h-92z" class="coral o"/>
  <path d="M-20-28q0-16 20-16t20 16" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g class="a" marker-end="url(#ar)" stroke-width="5"><path d="M250 210q90-50 200 20"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M140 220l-24-18M200 200l4-26"/>
</g>''', ground=False)

# --- 歩き方 ------------------------------------------------------------------
add('stride', '大股で力強くまっすぐ歩いていく', f'''
{table(370)}
<g transform="translate(300 370)">
  <path d="M-12-8l-56 40M12-8l58 36" fill="none" stroke="{TONES['blue'][2]}" stroke-width="14" stroke-linecap="round"/>
  <path d="M-28-84q28-14 56 0l-8 78h-40z" class="teal o"/>
  <path d="M-24-76l-42 34M24-76l44 26" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
  <circle cy="-116" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['cap']}" transform="translate(0 -8) scale(1.08)" fill="{TONES['blue'][0]}"/>
  <circle cx="-9" cy="-112" r="2.4" fill="{INK}"/><circle cx="9" cy="-112" r="2.4" fill="{INK}"/>
  <path d="M-8-100q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M232 384h136"/></g>
<g class="a" marker-end="url(#ar)"><path d="M232 340v40"/></g>
<g class="a" marker-end="url(#ar)"><path d="M368 340v40"/></g>''', arrow=True, ground=False)

add('stroll', '公園をゆっくりぶらぶらと歩いている', f'''
<path d="M0 0h600v250H0z" fill="#dceaf4"/>
<path d="M0 250h600v150H0z" fill="#dfe8d8"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M0 360q160-30 300 0t300-14v54H0z" fill="#d9c9a8"/>
{person(300, 350, 1.05, 1, 'coral', 'blue', 'stand', 'bob', 'smile')}
{tree(100, 280, 1.0)}
{tree(500, 300, 1.2)}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 8"><path d="M120 380q80-14 160 0"/></g>
{sun(500, 70, 30)}
<g class="o"><circle cx="180" cy="330" r="7" class="coralp"/><circle cx="420" cy="340" r="7" class="violetp"/></g>''', ground=False)

add('tiptoe', 'つま先立ちで音を立てずに歩く', f'''
{table(370)}
<g transform="translate(300 370)">
  <path d="M-14-10l-30 26 14 10 20-22M14-10l30 22-12 12-22-20" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-26-84q26-14 52 0l-8 78h-36z" class="violet o"/>
  <path d="M-24-76l-26 40M24-76l26 40" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cy="-112" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['bob']}" transform="translate(0 -4)" fill="{HAIR}"/>
  <circle cx="-8" cy="-108" r="2.2" fill="{INK}"/><circle cx="8" cy="-108" r="2.2" fill="{INK}"/>
  <path d="M-7-96h14" fill="none" stroke="{INK}" stroke-width="2"/>
  <path d="M-40-88l-30-30" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
</g>
<g transform="translate(240 240)">
  <path d="M-10-30h20v34h-20z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M40 374h520"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M430 200q26 30 0 60M470 176q40 46 0 108"/>
</g>
{cross(470 , 300, 0.6)}''', ground=False)

add('trot', '馬が速足でリズムよく走る', f'''
<path d="M0 0h600v250H0z" fill="#dceaf4"/>
<path d="M0 250h600v150H0z" fill="#dfe8d8"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 290)">
  <path d="M-120 0q-10-56 40-66h110q50 6 60 50-40 26-110 26-80 0-100-10z" fill="#a0764a" class="o"/>
  <path d="M100-56q40-40 60-70 24 16 10 60l-26 44z" fill="#a0764a" class="o"/>
  <path d="M156-124q-8-34 6-36 14 8 8 36zM178-130q10-30 22-24 4 12-10 30z" fill="#a0764a" class="o"/>
  <path d="M162-88l30 8-30 12z" fill="#8b6437" class="o"/>
  <circle cx="150" cy="-104" r="4" fill="{INK}"/>
  <path d="M124-120q40-18 56 10-36 8-56-10z" fill="#6b4c28" class="o"/>
  <path d="M-120 0q-46-16-56-58 46 6 64 44z" fill="#6b4c28" class="o"/>
  <g stroke="#8b6437" stroke-width="14" stroke-linecap="round" fill="none">
    <path d="M-70 16l-40 44M-30 20l14 50M40 18l40 44M80 14l-14 52"/>
  </g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M80 220h50M60 260h40M100 300h50"/>
</g>
<g fill="{MUTED}"><ellipse cx="300" cy="348" rx="120" ry="12" opacity="0.4"/></g>''', ground=False)

add('tumble', '階段から足をすべらせて転がり落ちる', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<g fill="#c9a464" class="o">
''' + ''.join(f'<path d="M{40+i*80} {160+i*48}h{560-i*80}v48h-{560-i*80}z"/>' for i in range(5)) + f'''
</g>
<g transform="translate(330 230) rotate(120)">
  <path d="M-12-8l-26 33M12-8l28 28" fill="none" stroke="{TONES['blue'][2]}" stroke-width="11" stroke-linecap="round"/>
  <path d="M-25-78q25-13 50 0l-8 72h-34z" class="coral o"/>
  <path d="M-22-70l-30 24M22-70l32 20" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
  <circle cy="-108" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" fill="{HAIR}"/>
  <circle cx="-8" cy="-104" r="2.2" fill="{INK}"/><circle cx="8" cy="-104" r="2.2" fill="{INK}"/>
  <circle cx="0" cy="-91" r="4" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
<g class="a" marker-end="url(#ar)" stroke-width="5"><path d="M180 140q80 40 200 200"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M420 170l24-18M450 230l26 6"/>
</g>''', arrow=True, ground=False)

add('trickle', '蛇口から水がちょろちょろとしか出ない', f'''
{split()}
<path d="M0 0h600v400H0z" fill="#e8eef2"/>
<g transform="translate(150 180)">
  <path d="M-14-60h28v40h-28z" fill="#b8bfc8" class="o"/>
  <path d="M-14-60q0-34 50-34h44v24h-36q-36 0-36 26z" fill="#c8d0d8" class="o"/>
  <path d="M-40-20h52q10 0 10 12t-10 12h-52q-10 0-10-12t10-12z" fill="#9aa5b0" class="o"/>
</g>
<g fill="{TONES['blue'][1]}" stroke="{TONES['blue'][0]}" stroke-width="2"><path d="M124 184h52v170h-52z"/></g>
<g transform="translate(450 180)">
  <path d="M-14-60h28v40h-28z" fill="#b8bfc8" class="o"/>
  <path d="M-14-60q0-34 50-34h44v24h-36q-36 0-36 26z" fill="#c8d0d8" class="o"/>
  <path d="M-40-20h52q10 0 10 12t-10 12h-52q-10 0-10-12t10-12z" fill="#9aa5b0" class="o"/>
</g>
<g fill="{TONES['blue'][0]}">
  <path d="M424 200q9 10 9 17t-9 8-9-8 9-17z"/><path d="M422 256q8 9 8 15t-8 7-8-7 8-15z"/>
  <path d="M424 310q8 9 8 15t-8 7-8-7 8-15z"/>
</g>
<g transform="translate(300 380)"><path d="M-280-30h560v40h-560z" fill="#c8d0d8" class="o"/></g>''', ground=False)

# --- 物 ---------------------------------------------------------------------
add('semiconductor', '基板の上に黒い四角のチップが載っている', f'''
<path d="M0 0h600v400H0z" fill="#1e2d24"/>
<g transform="translate(300 200)">
  <path d="M-250-150h500v300h-500z" fill="#1f6b4a" class="o"/>
  <g fill="none" stroke="#c9a464" stroke-width="4">
    <path d="M-220-110h140v60h100v80h-120M120-120v90h100M-200 100h180v-40h120v60"/>
  </g>
  <g fill="#c9a464">
''' + ''.join(f'<circle cx="{-210+ (i%8)*60}" cy="{-120+(i//8)*70}" r="7"/>' for i in range(24)) + f'''
  </g>
  <g transform="translate(0 0)">
    <path d="M-90-56h180v112h-180z" fill="#1c1f26" class="o"/>
    <circle cx="-64" cy="-32" r="8" fill="#4a5560"/>
    <g fill="#8f9aa6">
''' + ''.join(f'<rect x="{-84+i*22}" y="-70" width="12" height="14" rx="2"/><rect x="{-84+i*22}" y="56" width="12" height="14" rx="2"/>' for i in range(8)) + f'''
''' + ''.join(f'<rect x="-104" y="{-42+i*22}" width="14" height="12" rx="2"/><rect x="90" y="{-42+i*22}" width="14" height="12" rx="2"/>' for i in range(4)) + f'''
    </g>
  </g>
</g>''', ground=False)

add('stocking', 'ひざ上まである長い靴下', f'''
{table(340)}
<g transform="translate(230 210)">
  <path d="M-34-110h68v170q0 26-20 34l-56 20q-18 6-24-12t10-24l34-16q-12-20-12-42z" class="violetp o"/>
  <path d="M-34-110h68v-16h-68z" class="violet o"/>
  <g fill="none" stroke="{TONES['violet'][0]}" stroke-width="2.5">
''' + ''.join(f'<path d="M-32 {-84+i*30}h64"/>' for i in range(5)) + f'''
  </g>
</g>
<g transform="translate(400 210)">
  <path d="M-34-110h68v170q0 26-20 34l-56 20q-18 6-24-12t10-24l34-16q-12-20-12-42z" class="violetp o"/>
  <path d="M-34-110h68v-16h-68z" class="violet o"/>
  <g fill="none" stroke="{TONES['violet'][0]}" stroke-width="2.5">
''' + ''.join(f'<path d="M-32 {-84+i*30}h64"/>' for i in range(5)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 90v220"/></g>''', arrow=True, ground=False)

add('strap', 'かばんのひもを肩にかけ、金具で長さを調節する', f'''
{table(380)}
{person(280, 380, 1.2, 1, 'teal', 'blue', 'stand', 'bob', 'smile')}
<g transform="translate(280 300)">
  <path d="M-32-108q16-10 30 0l70 130q-30 12-56 4z" class="corald o"/>
  <g transform="translate(30 -10)">
    <path d="M-20-16h40v32h-40z" fill="#c8d0d8" class="o"/>
    <path d="M-6-16v32" stroke="{INK}" stroke-width="4" fill="none"/>
  </g>
</g>
<g transform="translate(360 350)">
  <path d="M-56-36h112v72h-112z" class="coral o"/>
  <path d="M-56 0h112" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 180l-140 40"/></g>''', arrow=True, ground=False)

add('subtitle', '画面の下に訳のせりふが出ている', f'''
{table(380)}
<g transform="translate(300 210)">
  <path d="M-250-160h500v320h-500z" fill="#3b4450" class="o"/>
  <path d="M-230-140h460v280h-460z" fill="#dceaf4"/>
  {person(-80, 100, 0.7, 1, 'coral', 'blue', 'point', 'bun', 'smile')}
  {person(80, 100, 0.7, -1, 'teal', 'violet', 'stand', 'short', 'smile')}
  <path d="M-230 60h460v80h-460z" fill="{INK}" opacity="0.45"/>
  <g fill="#fffefd">
    <rect x="-160" y="78" width="320" height="16" rx="8"/>
    <rect x="-110" y="106" width="220" height="16" rx="8"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 340l-100-40"/></g>''', arrow=True, ground=False)

add('switch-off', 'スイッチを下げて明かりを消す', f'''
{split()}
<path d="M0 0h300v400H0z" fill="#fff6e0"/>
<path d="M300 0h300v400H300z" fill="#4a5560"/>
<g transform="translate(150 130)">
  <path d="M0-70v30" stroke="{INK}" stroke-width="5" fill="none"/>
  <path d="M-46-40h92l-16 36h-60z" fill="#c8d0d8" class="o"/>
  <circle cy="10" r="20" class="gold o"/>
  <g fill="{TONES['gold'][1]}" opacity="0.55"><path d="M0 10l-120 200h240z"/></g>
</g>
<g transform="translate(150 320)">
  <path d="M-40-50h80v100h-80z" fill="#fffdf6" class="o"/>
  <path d="M-20-34h40v40h-40z" fill="{TONES['green'][0]}" class="o"/>
</g>
<g transform="translate(450 130)">
  <path d="M0-70v30" stroke="{MUTED}" stroke-width="5" fill="none"/>
  <path d="M-46-40h92l-16 36h-60z" fill="#6f7b88" class="o"/>
  <circle cy="10" r="20" fill="#8f9aa6" class="o"/>
</g>
<g transform="translate(450 320)">
  <path d="M-40-50h80v100h-80z" fill="#c8d0d8" class="o"/>
  <path d="M-20 -4h40v40h-40z" fill="{MUTED}" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 320h60"/></g>''', arrow=True, ground=False)

add('thermostat', '室温の設定つまみを回して温度を決める', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<g transform="translate(300 200)">
  <circle r="150" fill="#fffdf6" class="o"/>
  <circle r="124" fill="#e0e6ea" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">
''' + ''.join(f'<path d="M{104*math.cos(math.pi*(0.7+i*0.081)):.0f} {104*math.sin(math.pi*(0.7+i*0.081)):.0f}L{122*math.cos(math.pi*(0.7+i*0.081)):.0f} {122*math.sin(math.pi*(0.7+i*0.081)):.0f}"/>' for i in range(21)) + f'''
  </g>
  <path d="M-88-88A124 124 0 0 1 0-124" fill="none" stroke="{TONES['blue'][0]}" stroke-width="12"/>
  <path d="M0-124A124 124 0 0 1 88-88" fill="none" stroke="{TONES['coral'][0]}" stroke-width="12"/>
  <circle r="60" fill="#c8d0d8" class="o"/>
  <path d="M0 0v-46" stroke="{INK}" stroke-width="9" stroke-linecap="round" fill="none"/>
  <circle r="12" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M420 100q60 40 40 90"/></g>
{flame(500, 350, 0.35)}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M100 340v-30M86 322h28M92 314l16 16M108 314l-16 16"/>
</g>''', arrow=True, ground=False)

add('tusk', 'ゾウの口から長く曲がったきばが二本出ている', f'''
<path d="M0 0h600v290H0z" fill="#dceaf4"/>
<path d="M0 290h600v110H0z" fill="#dfe8d8"/>
<path d="M0 290h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(300 260)">
  <ellipse rx="130" ry="100" fill="#9aa5b0" class="o"/>
  <path d="M-130-30q-90-20-100 40 80 40 108 0z" fill="#8f9aa6" class="o"/>
  <path d="M130-30q90-20 100 40-80 40-108 0z" fill="#8f9aa6" class="o"/>
  <circle cx="-46" cy="-30" r="7" fill="{INK}"/><circle cx="46" cy="-30" r="7" fill="{INK}"/>
  <path d="M-22 50q-16 90 30 84 26-6 12-84z" fill="#9aa5b0" class="o"/>
  <g fill="#fffdf6" class="o">
    <path d="M-58 40q-24 60-6 96 26-12 24-92z"/>
    <path d="M58 40q24 60 6 96-26-12-24-92z"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 380l100-50"/></g>
<g class="a" marker-end="url(#ar)"><path d="M480 380l-100-50"/></g>''', arrow=True, ground=False)

add('vacancy', '満室の札と、空室ありの札', f'''
{split()}
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<g transform="translate(150 200)">
  <path d="M-100-140h200v280h-200z" fill="#c8d0d8" class="o"/>
  <g class="o">
''' + ''.join(f'<rect x="{-80+ (i%3)*56}" y="{-116+(i//3)*70}" width="40" height="46" fill="{TONES["gold"][1]}"/>' for i in range(12)) + f'''
  </g>
  <path d="M-70 170h140v-56h-140z" class="coral o"/>
  <rect x="-46" y="132" width="92" height="16" rx="8" fill="#fffefd"/>
</g>
<g transform="translate(450 200)">
  <path d="M-100-140h200v280h-200z" fill="#c8d0d8" class="o"/>
  <g class="o">
''' + ''.join(f'<rect x="{-80+ (i%3)*56}" y="{-116+(i//3)*70}" width="40" height="46" fill="{TONES["gold"][1] if i not in (4, 7, 10) else "#5a6270"}"/>' for i in range(12)) + f'''
  </g>
  <path d="M-70 170h140v-56h-140z" class="green o"/>
  <rect x="-46" y="132" width="92" height="16" rx="8" fill="#fffefd"/>
</g>
{cross(150, 60, 0.7)}
{tick(450, 60, 0.7)}''', ground=False)

add('vaccination', '小びんのワクチンと、接種の記録カード', f'''
{table(340)}
<g transform="translate(200 250)">
  <path d="M-32-60h64v96q0 14-32 14t-32-14z" fill="#e8f0f6" class="o"/>
  <path d="M-32-60h64v-14h-64z" fill="#8f9aa6" class="o"/>
  <path d="M-14-74v-10h28v10z" class="coral o"/>
  <path d="M-26-20h52v56q0 10-26 10t-26-10z" fill="{TONES['blue'][1]}"/>
</g>
<g transform="translate(330 190) rotate(30)">
  <path d="M-50-12h96v24h-96z" fill="#e8f0f6" class="o"/>
  <path d="M-50-14h26v28h-26z" class="bluep"/>
  <path d="M46-5h26v10H46z" fill="#8f9aa6" class="o"/>
  <path d="M72-2h30v4H72z" fill="{INK}"/>
</g>
<g transform="translate(450 290) rotate(-6)">
  <path d="M-80-56h160v112h-160z" class="paper"/>
  <rect x="-60" y="-40" width="90" height="12" rx="6" fill="{INK}"/>
  <g fill="{MUTED}"><rect x="-60" y="-14" width="120" height="9" rx="4.5"/><rect x="-60" y="6" width="100" height="9" rx="4.5"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
    <path d="M-56 34l10 12 22-26"/><path d="M4 34l10 12 22-26"/>
  </g>
</g>''', ground=False)

add('vandalism', '壁に落書きされ、ベンチが壊されている', f'''
<path d="M0 0h600v400H0z" fill="#d6cec0"/>
<g fill="none" stroke="#c0b8a8" stroke-width="3">
''' + ''.join(f'<path d="M0 {50+i*60}h600"/>' for i in range(5)) + f'''
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="14" stroke-linecap="round">
  <path d="M80 120q40-50 80 0t80-40 70 60"/>
</g>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="12" stroke-linecap="round">
  <path d="M360 90q60 30 20 80t60 30"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="10" stroke-linecap="round">
  <path d="M120 210q90-30 160 20"/>
</g>
<path d="M0 320h600v80H0z" fill="#8f9aa6" class="o"/>
<g transform="translate(300 320)">
  <path d="M-140-16h130v16h-130z" fill="#c9a464" class="o"/>
  <path d="M20-10h110v16H20z" fill="#c9a464" class="o" transform="rotate(18 20 -10)"/>
  <path d="M-120 0v40M-40 0v40" stroke="#8b6437" stroke-width="10" stroke-linecap="round" fill="none"/>
  <path d="M60 20l30 20" stroke="#8b6437" stroke-width="10" stroke-linecap="round" fill="none"/>
</g>
<g transform="translate(500 250) rotate(20)">
  <path d="M-16-46h32v76q0 12-16 12t-16-12z" class="coral o"/>
  <path d="M-8-46v-12h16v12z" fill="{INK}"/>
</g>''', ground=False)

add('ventilation', '換気扇が回って室内の空気を外へ出す', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<path d="M0 350h600v50H0z" fill="#c9a464" class="o"/>
<g transform="translate(400 160)">
  <path d="M-90-90h180v180h-180z" fill="#c8d0d8" class="o"/>
  <circle r="70" fill="#5a6270" class="o"/>
  <g fill="#8f9aa6" class="o">
''' + ''.join(f'<path d="M0 0q40-20 60 10-30 34-60-10z" transform="rotate({i*90})"/>' for i in range(4)) + f'''
  </g>
  <circle r="14" fill="{INK}"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M60 120q80-24 150 0t100-10M40 200q80-24 150 0t110-8M60 280q80-24 150 0t100-6"/>
</g>
<g class="a" marker-end="url(#ar)" stroke-width="5"><path d="M480 240q60 40 60 100"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M400 250q40 30 30 60"/></g>''', ground=False)

add('void', '内容が消され「無効」と大きく打たれた書類', f'''
{table(370)}
<g transform="translate(300 200) rotate(-4)">
  <path d="M-180-150h360v300h-360z" class="paper"/>
  <g fill="{MUTED}" opacity="0.5">
''' + ''.join(f'<rect x="-140" y="{-116+i*36}" width="{280-(i%3)*60}" height="10" rx="5"/>' for i in range(7)) + f'''
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round" opacity="0.8">
    <path d="M-150-100L150 110M150-100L-150 110"/>
  </g>
  <g transform="rotate(-16)">
    <path d="M-130-40h260v80h-260z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
    <g fill="{TONES['coral'][0]}">
''' + ''.join(f'<rect x="{-104+i*54}" y="-16" width="40" height="32" rx="6"/>' for i in range(4)) + f'''
    </g>
  </g>
</g>''', ground=False)

add('whisk', '泡立て器で卵をかき混ぜて泡立てる', f'''
{table(330)}
<g transform="translate(300 260)">
  <path d="M-110-40h220l-20 90q-2 16-90 16t-90-16z" fill="#e0e6ea" class="o"/>
  <path d="M-104-30h208" fill="none" stroke="#c8d0d8" stroke-width="3"/>
  <path d="M-90-30h180l-6 34q-40 16-84 16t-84-16z" fill="#fde39a"/>
  <g fill="#fff2b8" stroke="{TONES['gold'][2]}" stroke-width="2">
    <circle cx="-50" cy="-18" r="13"/><circle cx="-14" cy="-6" r="10"/><circle cx="30" cy="-16" r="12"/><circle cx="66" cy="-4" r="9"/>
  </g>
</g>
<g transform="translate(320 170) rotate(14)">
  <path d="M-10-100h20v70h-20z" fill="{INK}"/>
  <g fill="none" stroke="#c8d0d8" stroke-width="5">
''' + ''.join(f'<path d="M0-30q{-46+i*23} 50 0 96"/>' for i in range(5)) + f'''
  </g>
  <path d="M-12-34h24v10h-24z" fill="#8f9aa6" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M420 130q50 30 30 70"/></g>''', arrow=True, ground=False)

add('whisker', '猫の鼻の左右に長いひげが伸びている', f'''
{table(370)}
<g transform="translate(300 210)">
  <circle r="110" fill="#c8a070" class="o"/>
  <path d="M-96-56q-24-70 0-80 30 6 44 62zM96-56q24-70 0-80-30 6-44 62z" fill="#c8a070" class="o"/>
  <path d="M-78-62q-14-46 0-52 18 4 26 40zM78-62q14-46 0-52-18 4-26 40z" class="coralp"/>
  <g fill="{INK}"><ellipse cx="-42" cy="-14" rx="10" ry="14"/><ellipse cx="42" cy="-14" rx="10" ry="14"/></g>
  <path d="M-14 30h28l-14 14z" class="corald o"/>
  <path d="M0 44v10M-24 66q24 12 24-12M24 66q-24 12-24-12" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <g fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round">
    <path d="M-26 40q-90-16-140-40M-26 50q-90 4-140-2M-26 60q-90 22-134 46"/>
    <path d="M26 40q90-16 140-40M26 50q90 4 140-2M26 60q90 22 134 46"/>
  </g>
</g>''', ground=False)

add('wilderness', '道も家もない、手つかずの広大な自然', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
<path d="M0 250l110-110 90 70 100-100 110 110 90-70 100 90v160H0z" fill="#9aa5b0" class="o"/>
<path d="M0 300q120-20 300 10t300-20v110H0z" fill="#7d9a70" class="o"/>
''' + ''.join(f'''<g transform="translate({30+i*56} {330+(i%3)*22}) scale({0.7+(i%3)*0.14})">
  <path d="M-8 0h16v-40h-16z" fill="{BRN}"/>
  <path d="M0-140l-32 46h64zM0-114l-44 52h88zM0-84l-54 56h108z" fill="{TONES['green'][2]}" class="o"/>
</g>''' for i in range(10)) + f'''
<path d="M0 380q160-30 300 0t300-20v40H0z" fill="#5b8caa" opacity="0.6"/>
{sun(510, 70, 30)}''', ground=False)

add('terrace', '同じ形の家が壁を接して一列に並んでいる', f'''
<path d="M0 0h600v300H0z" fill="#dceaf4"/>
<path d="M0 300h600v100H0z" fill="#8f9aa6" class="o"/>
<g>
''' + ''.join(f'''<g transform="translate({70+i*115} 300)">
  <path d="M-58 0v-150h116V0z" fill="{["#d9b877","#c8a070","#d9b877","#c8a070","#d9b877"][i]}" class="o"/>
  <path d="M-64-150h128v-20h-128z" fill="#8b6437" class="o"/>
  <path d="M-40-130h34v40h-34zM8-130h34v40H8zM-40-70h34v40h-34z" class="bluep o"/>
  <path d="M8-60h34V0H8z" fill="#6b4c28" class="o"/>
  <path d="M22-46h6v6h-6z" fill="{TONES['gold'][0]}"/>
  <path d="M-30-170h14v-24h-14z" fill="#8f9aa6" class="o"/>
</g>''' for i in range(5)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M60 160h480"/></g>''', arrow=True, ground=False)

# --- 抽象 -------------------------------------------------------------------
add('the-tip-of-the-iceberg', '水面に出た氷山の先はごく一部で、下に大きな塊がある', f'''
<path d="M0 0h600v170H0z" fill="#dceaf4"/>
<path d="M0 170h600v230H0z" fill="#4d7fa4"/>
<path d="M0 170h600" stroke="{INK}" stroke-width="3" fill="none"/>
<path d="M244 170l56-90 70 90z" fill="#fffefd" class="o"/>
<path d="M130 170h340q40 90-16 150-60 64-166 56-104-8-152-78-32-52-6-128z" fill="#c7dbea" class="o" opacity="0.9"/>
<g fill="none" stroke="#9fc4dd" stroke-width="4">
  <path d="M180 230h260M158 300h300M200 356h200"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M470 60l-110 50"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M60 176v-90"/></g>
<g class="a" marker-end="url(#ar)"><path d="M60 190v170"/></g>''', arrow=True, ground=False)

add('throw-light-on', '手元のランプが暗がりの中の答えを照らし出す', f'''
<path d="M0 0h600v400H0z" fill="#2c3550"/>
{table(380)}
<g transform="translate(140 170)">
  <path d="M-46-30h92l-16 40h-60z" fill="#c8d0d8" class="o"/>
  <circle cy="24" r="22" class="gold o"/>
  <path d="M0-30v-40" stroke="{INK}" stroke-width="5" fill="none"/>
</g>
<g fill="{TONES['gold'][1]}" opacity="0.3"><path d="M140 194l280-100v220z"/></g>
<g transform="translate(400 200)">
  <path d="M-90-70h180v140h-180z" class="paper"/>
  <g fill="{INK}"><rect x="-66" y="-46" width="132" height="12" rx="6"/><rect x="-66" y="-20" width="100" height="12" rx="6"/><rect x="-66" y="6" width="120" height="12" rx="6"/></g>
  {tick(0, 46, 0.6)}
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['gold'][0]}"><path d="M200 190h100"/></g>''', ground=False)

add('steal-the-show', '主役の横で脇役が一番の注目を集める', f'''
<path d="M0 0h600v400H0z" fill="#3b3550"/>
<path d="M0 320h600v80H0z" fill="#5a4a3c" class="o"/>
<path d="M0 40h600v40H0z" class="corald o"/>
<path d="M0 80h60v240H0zM600 80h-60v240h60z" class="coral o"/>
{person(200, 320, 1.1, 1, 'blue', 'blue', 'stand', 'bun', 'sad')}
{person(400, 320, 1.15, 1, 'coral', 'gold', 'up', 'cap', 'smile')}
<g fill="{TONES['gold'][1]}" opacity="0.28"><path d="M400 60l-130 260h260z"/></g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{400+150*math.cos(3.5+i*0.42):.0f} {200+150*math.sin(3.5+i*0.42):.0f}l{22*math.cos(3.5+i*0.42):.0f} {22*math.sin(3.5+i*0.42):.0f}"/>' for i in range(8)) + f'''
</g>
<g fill="{MUTED}" opacity="0.35"><ellipse cx="200" cy="220" rx="70" ry="120"/></g>''', ground=False)

add('paradox', '進むほど元の場所に戻る、矛盾しているのに成り立つ階段', f'''
<path d="M0 0h600v400H0z" fill="#eef2f6"/>
<g fill="#c8d0d8" class="o">
  <path d="M160 300h90v-30h-90zM250 270h90v-30h-90zM340 240h90v-30h-90zM430 210h60v90h-60z"/>
  <path d="M160 300v-90h-60v90zM100 210h90v-30h-90zM190 180h90v-30h-90zM280 150h90v-30h-90z"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round" marker-end="url(#ar)">
  <path d="M170 268q120-10 240-70t-80-80-240 60"/>
</g>
{person(210, 268, 0.5, 1, 'teal', 'blue', 'walk', 'cap', 'neutral', 'walk')}
{person(390, 200, 0.5, 1, 'teal', 'blue', 'walk', 'cap', 'neutral', 'walk')}
<g transform="translate(500 90)">
  <path d="M-16-30q0-26 16-26t16 26-16 20v12" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="26" r="6" fill="{INK}"/>
</g>''', arrow=True, ground=False)

add('novelty', 'そろいの品の中に、初めて見る珍しい形の品がある', f'''
{table(340)}
<g>
''' + ''.join(f'<g transform="translate({100+i*80} 260)"><path d="M-30-50h60v100h-60z" class="tealp o"/><path d="M-30-50l10-14h60l-10 14z" fill="{TONES["teal"][1]}" class="o"/></g>' for i in [0,1,3,4,5]) + f'''
</g>
<g transform="translate(340 250)">
  <path d="M0-70l22 40 44 8-32 32 8 44-42-22-42 22 8-44-32-32 44-8z" class="coral o"/>
  <circle r="14" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{340+110*math.cos(3.5+i*0.5):.0f} {250+110*math.sin(3.5+i*0.5):.0f}l{20*math.cos(3.5+i*0.5):.0f} {20*math.sin(3.5+i*0.5):.0f}"/>' for i in range(7)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 120l-90 60"/></g>''', arrow=True, ground=False)

add('dosage', '一日に飲む錠剤の数が箱に指示されている', f'''
{table(330)}
<g transform="translate(200 240)">
  <path d="M-80-70h160v140h-160z" fill="#fffdf6" class="o"/>
  <path d="M-80-70l20-24h160l-20 24z" fill="#f0eee6" class="o"/>
  <path d="M80-70l20-24v140l-20 24z" fill="#e0dcd0" class="o"/>
  <rect x="-60" y="-46" width="90" height="14" rx="7" class="coral"/>
  <g fill="{MUTED}"><rect x="-60" y="-16" width="110" height="9" rx="4.5"/><rect x="-60" y="4" width="80" height="9" rx="4.5"/></g>
  <g class="coral o"><circle cx="-40" cy="40" r="12"/><circle cx="-6" cy="40" r="12"/><circle cx="28" cy="40" r="12"/></g>
</g>
<g>
''' + ''.join(f'<g transform="translate({390+i*54} 270)"><ellipse rx="26" ry="18" fill="#fffdf6" class="o"/><path d="M-26 0h52" stroke="{MUTED}" stroke-width="3" fill="none"/></g>' for i in range(3)) + f'''
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M330 270h30"/></g>
<g class="a" marker-end="url(#ar)"><path d="M360 180h150"/></g>
<g class="a" marker-end="url(#ar)"><path d="M510 180H360"/></g>''', arrow=True, ground=False)

add('extremity', '棒の両端が先端で、そこがいちばん外側になる', f'''
{table(370)}
<g transform="translate(300 200)">
  <path d="M-230-16h460v32h-460z" fill="#c9a464" class="o"/>
  <circle cx="-230" r="26" class="coral o"/>
  <circle cx="230" r="26" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M70 300l-0-70"/></g>
<g class="a" marker-end="url(#ar)"><path d="M530 300v-70"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M70 340h460"/></g>
{person(300, 370, 0.55, 1, 'teal', 'blue', 'up', 'cap', 'smile')}''', arrow=True, ground=False)

add('maturity', '青い実が時間をかけて熟して色づく', f'''
{split()}
{table(340)}
<g transform="translate(150 240)">
  <circle r="70" class="green o"/>
  <path d="M0-70q-14-30 6-38 20 8 8 38z" class="greend o"/>
  <ellipse cx="-24" cy="-24" rx="16" ry="11" fill="#fffefd" opacity="0.4" transform="rotate(-30 -24 -24)"/>
</g>
<g transform="translate(450 240)">
  <circle r="84" class="coral o"/>
  <path d="M0-84q-16-32 8-42 22 10 8 42z" class="greend o"/>
  <ellipse cx="-30" cy="-30" rx="18" ry="13" fill="#fffefd" opacity="0.4" transform="rotate(-30 -30 -30)"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 240h60"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M280 130q20 20 40 0"/></g>
<g transform="translate(300 110)">
  <circle r="26" fill="#fffdf6" class="o"/>
  <path d="M0 0v-16M0 0l10 8" stroke="{INK}" stroke-width="4" stroke-linecap="round" fill="none"/>
</g>''', arrow=True, ground=False)

add('shorten', '長いズボンのすそを切って短くする', f'''
{split()}
{table(370)}
<g transform="translate(150 200)">
  <path d="M-60-90h120v50l-16 190h-40l-8-130-8 130h-40l-16-190z" class="bluep o"/>
  <path d="M-60-40h120" fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M60 290h180"/></g>
<g transform="translate(450 200)">
  <path d="M-60-90h120v50l-10 120h-40l-10-70-10 70h-40l-10-120z" class="bluep o"/>
  <path d="M-60-40h120" fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"/>
</g>
<g transform="translate(250 290) rotate(20)">
  <g stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
    <path d="M-6-6l-70-26q-10-4-6-12t14-4L8-24z" fill="#cfd6dd"/>
    <path d="M-6 6l-70 26q-10 4-6 12t14 4L8 24z" fill="#8f9aa6"/>
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round">
    <path d="M12-12q36-14 50 4t-12 24"/><path d="M12 12q36 14 50-4t-12-24"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 130h60"/></g>''', arrow=True, ground=False)

add('soften', 'かたいバターが温まってやわらかくなる', f'''
{split()}
{table(340)}
<g transform="translate(150 260)">
  <path d="M-70-40h140v60h-140z" fill="#fde39a" class="o"/>
  <path d="M-70-40l18-18h140l-18 18z" fill="#fff2b8" class="o"/>
  <path d="M70-40l18-18v60l-18 18z" fill="#e8c98d" class="o"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M100 150v-30M86 132h28M92 124l16 16M108 124l-16 16"/>
</g>
<g transform="translate(450 270)">
  <path d="M-80-14q40-40 90-16 50 24 66 30-30 20-90 20t-66-34z" fill="#fde39a" class="o"/>
  <path d="M-40-22q40-20 70 4" fill="none" stroke="#e8c98d" stroke-width="4"/>
</g>
{flame(450, 150, 0.4)}
<g class="a" marker-end="url(#ar)"><path d="M270 260h60"/></g>''', arrow=True, ground=False)

add('spur', '拍車を当てて馬を一気に速く走らせる', f'''
<path d="M0 0h600v260H0z" fill="#dceaf4"/>
<path d="M0 260h600v140H0z" fill="#dfe8d8"/>
<path d="M0 260h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(320 280)">
  <path d="M-120 0q-10-52 40-62h100q46 6 56 48-40 24-104 24-76 0-92-10z" fill="#a0764a" class="o"/>
  <path d="M92-52q40-38 58-66 22 16 8 58l-24 42z" fill="#a0764a" class="o"/>
  <path d="M146-116q-8-32 6-34 12 8 6 34zM168-122q10-28 20-22 4 10-8 28z" fill="#a0764a" class="o"/>
  <path d="M152-82l28 8-28 10z" fill="#8b6437" class="o"/>
  <circle cx="140" cy="-98" r="4" fill="{INK}"/>
  <path d="M-120 0q-44-16-54-56 44 6 62 42z" fill="#6b4c28" class="o"/>
  <g stroke="#8b6437" stroke-width="13" stroke-linecap="round" fill="none">
    <path d="M-70 14l-50 34M-26 18l4 52M40 16l46 36M76 12l-8 54"/>
  </g>
</g>
{sit(300, 250, 0.72, 1, 'coral', 'blue', 'cap', 'neutral', 'lap')}
<g transform="translate(272 268)">
  <path d="M-20-8h30v16h-30z" fill="#8f9aa6" class="o"/>
  <circle cx="-26" r="16" fill="none" stroke="#8f9aa6" stroke-width="5"/>
  <g fill="#8f9aa6">
''' + ''.join(f'<rect x="-29" y="-24" width="6" height="12" rx="3" transform="rotate({i*45} -26 0)"/>' for i in range(8)) + f'''
  </g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M80 200h60M60 250h50M90 300h60"/>
</g>
<g class="a" marker-end="url(#ar)" stroke-width="5"><path d="M480 190h80"/></g>''', ground=False)

add('stick-out', '同じ長さの棒の中で一本だけ長く突き出ている', f'''
{table(370)}
<g fill="#c9a464" class="o">
''' + ''.join(f'<rect x="{80+i*72}" y="200" width="40" height="170"/>' for i in range(6)) + f'''
</g>
<path d="M296 100h40v270h-40z" class="coral o"/>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M40 200h520"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M440 130h-80"/></g>''', arrow=True, ground=False)

add('unlock', '鍵を差し込んで回し、錠を開ける', f'''
{split()}
{table(370)}
<g transform="translate(150 230)">
  <path d="M-60 0h120v90h-120z" class="gold o"/>
  <path d="M-36 0v-30q0-36 36-36t36 36V0" fill="none" stroke="#8f9aa6" stroke-width="16"/>
  <circle cy="40" r="14" fill="{INK}"/>
  <path d="M-4 46h8v22h-8z" fill="{INK}"/>
</g>
{cross(150, 120, 0.7)}
<g transform="translate(450 230)">
  <path d="M-60 0h120v90h-120z" class="gold o"/>
  <path d="M-36 0v-30q0-36 36-36t36 36v-10" fill="none" stroke="#8f9aa6" stroke-width="16"/>
  <circle cy="40" r="14" fill="{INK}"/>
</g>
<g transform="translate(450 270) rotate(30)">
  <circle cx="-40" r="18" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-22-5h60v10h-60z" fill="{INK}"/>
  <path d="M30 5h8v14h-8zM44 5h8v10h-8z" fill="{INK}"/>
</g>
{tick(450, 120, 0.7)}''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
