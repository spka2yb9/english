# -*- coding: utf-8 -*-
"""第129回。台所と手仕事、速さを変える動詞。"""
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
def cross(x, y, s=1):
    return (f'<g fill="none" stroke="{TONES["coral"][0]}" stroke-width="{9*s}" stroke-linecap="round">'
            f'<path d="M{x-26*s} {y-26*s}l{52*s} {52*s}M{x+26*s} {y-26*s}l{-52*s} {52*s}"/></g>')
def tick(x, y, s=1):
    return (f'<g fill="none" stroke="{TONES["green"][0]}" stroke-width="{9*s}" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M{x-30*s} {y}l{22*s} {24*s} {42*s}-{52*s}"/></g>')
def head(x, y, r=22, shirt='teal', hair='short'):
    return (f'<g transform="translate({x} {y})">'
            f'<circle r="{r}" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>'
            f'<path d="{HAIRS[hair]}" transform="translate(0 108) scale({r/24:.2f})" fill="{HAIR}"/>'
            f'<circle cx="{-r*0.33:.0f}" cy="{-r*0.17:.0f}" r="2.4" fill="{INK}"/>'
            f'<circle cx="{r*0.33:.0f}" cy="{-r*0.17:.0f}" r="2.4" fill="{INK}"/>'
            f'<path d="M{-r*0.3:.0f} {r*0.35:.0f}q{r*0.3:.0f} {r*0.3:.0f} {r*0.6:.0f} 0" fill="none" stroke="{INK}" stroke-width="2"/>'
            f'<path d="M{-r*1.1:.0f} {r*1.5:.0f}q{r*1.1:.0f}-{r*0.6:.0f} {r*2.2:.0f} 0l-{r*0.3:.0f} {r*1.2:.0f}h-{r*1.6:.0f}z" fill="{TONES[shirt][0]}" class="o"/></g>')
def doc(x, y, w=100, h=130, lines=4):
    g = [f'<g transform="translate({x} {y})"><path d="M{-w/2} {-h/2}h{w}v{h}h{-w}z" class="paper"/>']
    for i in range(lines):
        g.append(f'<rect x="{-w/2+14}" y="{-h/2+22+i*(h-50)/max(lines,1):.0f}" width="{w-28-(i%3)*16}" height="8" rx="4" fill="{MUTED}"/>')
    g.append('</g>')
    return ''.join(g)

# --- 台所と食べ物 ------------------------------------------------------------
add('jar', 'ふた付きのガラス瓶にジャムが入っている', f'''
{table(340)}
<g transform="translate(300 250)">
  <path d="M-70-60h140v110q0 16-70 16t-70-16z" fill="#e8f0f6" class="o"/>
  <path d="M-70-60h140v-14h-140z" fill="#c8d0d8" class="o"/>
  <path d="M-78-74h156v-24h-156z" class="coral o"/>
  <path d="M-78-98q0-14 78-14t78 14z" class="corald o"/>
  <path d="M-60-30h120v78q0 12-60 12t-60-12z" class="corald"/>
  <path d="M-60-30h120" stroke="{TONES['coral'][2]}" stroke-width="3" fill="none"/>
  <path d="M-44 0h88v34h-88z" fill="#fffdf6" class="o"/>
  <rect x="-30" y="10" width="60" height="12" rx="6" fill="{MUTED}"/>
</g>''', ground=False)

add('ketchup', '赤いソースをボトルからしぼり出してかける', f'''
{table(340)}
<g transform="translate(230 220) rotate(150)">
  <path d="M-40-70h80v130q0 16-40 16t-40-16z" class="coral o"/>
  <path d="M-40-70q0-30 40-30t40 30z" class="coral o"/>
  <path d="M-14-100v-24h28v24z" class="corald o"/>
  <path d="M-30-30h60v60h-60z" fill="#fffdf6" class="o"/>
</g>
<path d="M300 230q30 30 34 60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="14" stroke-linecap="round"/>
<g transform="translate(400 290)">
  <ellipse rx="110" ry="28" fill="#fffdf6" class="o"/>
  <path d="M-110 0q0 34 110 34t110-34z" fill="#fffdf6" class="o"/>
  <g fill="{TONES['gold'][0]}" class="o">
''' + ''.join(f'<rect x="{-70+i*30}" y="-24" width="20" height="44" rx="6" transform="rotate({-12+i*8} {-60+i*30} 0)"/>' for i in range(5)) + f'''
  </g>
  <path d="M-50-10q60-20 110 6" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"/>
</g>''', ground=False)

add('honey', '瓶からとろりと流れ落ちる金色のはちみつ', f'''
{table(340)}
<g transform="translate(250 230)">
  <path d="M-56-50h112l-10 100q-2 14-46 14t-46-14z" fill="#e8f0f6" class="o"/>
  <path d="M-56-50h112v-14h-112z" class="goldd o"/>
  <path d="M-48-14h96l-8 62q-2 10-40 10t-40-10z" class="gold"/>
  <path d="M-48-14h96" stroke="{TONES['gold'][2]}" stroke-width="3" fill="none"/>
</g>
<path d="M300 230q26 40 20 90" fill="none" stroke="{TONES['gold'][0]}" stroke-width="16" stroke-linecap="round"/>
<g transform="translate(400 320)">
  <ellipse rx="80" ry="18" class="gold o"/>
</g>
<g transform="translate(470 180) scale(0.7)">
  <ellipse rx="40" ry="26" class="gold o"/>
  <g fill="{INK}"><path d="M-18-24q10 48 0 48zM6-26q10 52 0 52z"/></g>
  <circle cx="-34" cy="-4" r="16" fill="{INK}"/>
  <ellipse cx="4" cy="-30" rx="30" ry="14" fill="#fffefd" stroke="{INK}" stroke-width="3" opacity="0.85" transform="rotate(-22 4 -30)"/>
</g>''', ground=False)

add('fillet', '魚から骨を取り除いて切り身にする', f'''
{split()}
{table(340)}
<g transform="translate(150 250)">
  <path d="M-90 0q30-50 90-50t70 50q-10 50-70 50t-90-50z" fill="#b8c8d4" class="o"/>
  <path d="M70 0l40-30v60z" fill="#b8c8d4" class="o"/>
  <circle cx="-56" cy="-10" r="6" fill="{INK}"/>
  <g fill="none" stroke="#8fa4b4" stroke-width="3">
''' + ''.join(f'<path d="M{-40+i*24} -26v52"/>' for i in range(5)) + f'''
  </g>
</g>
<g transform="translate(450 240)">
  <path d="M-90-24q80-30 180 0 6 30-70 34-90 4-110-34z" fill="#f0c8c0" class="o"/>
  <g fill="none" stroke="#dba89e" stroke-width="3"><path d="M-60-10q60 16 130 0"/></g>
</g>
<g transform="translate(450 320)">
  <path d="M-70 0h140" stroke="#dde3e8" stroke-width="5" fill="none"/>
  <g stroke="#dde3e8" stroke-width="3" fill="none">
''' + ''.join(f'<path d="M{-60+i*24} -14v28"/>' for i in range(6)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 240h60"/></g>''', arrow=True, ground=False)

add('knead', 'パン生地を手のひらで押してこねる', f'''
{table(340)}
<g transform="translate(300 290)">
  <path d="M-190-16h380v16h-380z" fill="#e8d8b4" class="o"/>
</g>
<g transform="translate(290 254)">
  <path d="M-100 20q-16-50 20-64 60-24 120-4 40 14 34 44-8 26-90 28-70 2-84-4z" fill="#f0e0b8" class="o"/>
  <g fill="none" stroke="#d8c498" stroke-width="3"><path d="M-60 6q60 14 120-4"/></g>
</g>
<g>
  <path d="M240 230q-40-40-80-30" stroke="{SKINL}" stroke-width="34" stroke-linecap="round" fill="none"/>
  <path d="M240 230q-40-40-80-30" stroke="{SKIN}" stroke-width="29" stroke-linecap="round" fill="none"/>
  <path d="M340 224q40-40 84-26" stroke="{SKINL}" stroke-width="34" stroke-linecap="round" fill="none"/>
  <path d="M340 224q40-40 84-26" stroke="{SKIN}" stroke-width="29" stroke-linecap="round" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 170v40"/></g>
<g class="a" marker-end="url(#ar)"><path d="M350 170v40"/></g>
<g fill="#f0e0b8"><circle cx="180" cy="300" r="8"/><circle cx="430" cy="304" r="7"/></g>''', arrow=True, ground=False)

# --- 手仕事 -----------------------------------------------------------------
add('knit', '二本の棒針で毛糸を編んでいく', f'''
{table(350)}
<g transform="translate(300 240)">
  <path d="M-120-20h240v100h-240z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4">
''' + ''.join(f'<path d="M{-110+i*24} -20q6 24 0 48t0 52"/>' for i in range(10)) + f'''
''' + ''.join(f'<path d="M-120 {4+i*30}q24-14 48 0t48 0 48 0 48 0 48 0"/>' for i in range(3)) + f'''
  </g>
</g>
<g transform="translate(240 190) rotate(-24)">
  <path d="M-6-90h12v130h-12z" fill="#c9a464" class="o"/>
  <circle cy="-96" r="10" class="coral o"/>
</g>
<g transform="translate(360 190) rotate(24)">
  <path d="M-6-90h12v130h-12z" fill="#c9a464" class="o"/>
  <circle cy="-96" r="10" class="coral o"/>
</g>
<g transform="translate(480 320)">
  <circle r="46" class="coral o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"><path d="M-40-16q40 26 80 0M-40 16q40-26 80 0"/></g>
  <path d="M-46 0q-40-20-80 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
</g>''', ground=False)

add('inscribe', '石碑に文字を彫り込む', f'''
{table(380)}
<g transform="translate(300 230)">
  <path d="M-130-140h260v280h-260z" fill="#b8bfc8" class="o"/>
  <path d="M-110-120h220v240h-220z" fill="#a8afb8"/>
  <g fill="#8f959e">
''' + ''.join(f'<rect x="-84" y="{-88+i*46}" width="{168-(i%3)*40}" height="16" rx="8"/>' for i in range(4)) + f'''
  </g>
  <g fill="none" stroke="#cdd4dc" stroke-width="2">
''' + ''.join(f'<path d="M-84 {-90+i*46}h{168-(i%3)*40}"/>' for i in range(4)) + f'''
  </g>
</g>
<g transform="translate(430 130) rotate(40)">
  <path d="M-10-70h20v90h-20z" fill="#c8d0d8" class="o"/>
  <path d="M-10 20l10 22 10-22z" fill="#8f9aa6" class="o"/>
</g>
<g transform="translate(500 90) rotate(-20)">
  <path d="M-16-40h32v70q0 12-16 12t-16-12z" fill="#c9a464" class="o"/>
</g>
<g fill="#a8afb8"><circle cx="200" cy="380" r="5"/><circle cx="230" cy="386" r="4"/></g>''', ground=False)

add('imprint', '柔らかい土に足あとがはっきり残る', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v170H0z" fill="#c8a878"/>
<path d="M0 230h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="#a88a58" class="o">
''' + ''.join(f'''<g transform="translate({80+i*84} {310+(i%2)*40}) rotate({-8+i*4})">
  <path d="M-22-30q22-14 44 0 6 40-8 54-14 8-28 0-14-14-8-54z"/>
  <circle cx="-16" cy="-40" r="8"/><circle cx="0" cy="-46" r="9"/><circle cx="16" cy="-42" r="8"/>
</g>''' for i in range(6)) + f'''
</g>
<g transform="translate(300 200)">
  <path d="M-40-90h80v70l40 20v20h-120v-20l40-20z" fill="#5b4a3c" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 190l-70 90"/></g>''', arrow=True, ground=False)

add('intertwine', '二本の綱がより合わさって一本になる', f'''
{table(380)}
<g transform="translate(300 200)">
''' + ''.join(f'<path d="M{-260+i*52} 0q26-48 52 0" fill="none" stroke="{TONES["coral"][0]}" stroke-width="24" stroke-linecap="round"/>' for i in range(10)) + f'''
''' + ''.join(f'<path d="M{-260+i*52} 0q26 48 52 0" fill="none" stroke="{TONES["teal"][0]}" stroke-width="24" stroke-linecap="round"/>' for i in range(10)) + f'''
  <path d="M-270 0h-30M270 0h30" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="24" stroke-linecap="round"><path d="M40 260q40-30 80-52"/></g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="24" stroke-linecap="round"><path d="M40 320q40-40 90-70"/></g>
<g class="a" marker-end="url(#ar)"><path d="M300 320v-70"/></g>''', arrow=True, ground=False)

add('interconnect', '離れていた機械が線でつながって一つの網になる', f'''
{split()}
{table(380)}
<g>
''' + ''.join(f'<g transform="translate({80+ (i%2)*110} {180+(i//2)*90})"><path d="M-38-28h76v56h-38z" fill="#3b4450" class="o"/><path d="M-38-28h76v56h-76z" fill="#3b4450" class="o"/><path d="M-30-20h60v40h-60z" fill="#dceaf4"/></g>' for i in range(4)) + f'''
</g>
<g>
''' + ''.join(f'<g transform="translate({390+ (i%2)*110} {180+(i//2)*90})"><path d="M-38-28h76v56h-76z" fill="#3b4450" class="o"/><path d="M-30-20h60v40h-60z" fill="#dceaf4"/></g>' for i in range(4)) + f'''
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6">
    <path d="M390 180h110M390 270h110M390 180v90M500 180v90M390 180l110 90M500 180l-110 90"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 230h60"/></g>''', arrow=True, ground=False)

# --- 速さを変える -----------------------------------------------------------
add('hinder', '重い荷を引かされて前に進みにくくなる', f'''
{table(380)}
{person(280, 380, 1.15, 1, 'coral', 'blue', 'walk', 'cap', 'sad', 'walk')}
<g>
  <path d="M250 330q-70 20-120 34" fill="none" stroke="{BRN}" stroke-width="7"/>
  <g transform="translate(100 372)">
    <path d="M-60-40h120v40h-120z" fill="#9aa5b0" class="o"/>
    <g fill="none" stroke="#7d8894" stroke-width="3"><path d="M-60-20h120M0-40v40"/></g>
  </g>
</g>
<g class="a" marker-end="url(#ar)" stroke-width="5"><path d="M360 260h90"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M240 260h-90"/></g>
<g fill="{TONES['blue'][0]}"><path d="M256 216q9 10 9 17t-9 8-9-8 9-17z"/></g>''', ground=False)

add('impede', '道が狭くなって車の流れが滞る', f'''
<path d="M0 250h600v150H0z" fill="#6f7b88"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M300 250h300v60H300zM300 340h300v60H300z" fill="#dfe8d8" class="o"/>
<g fill="none" stroke="#fffefd" stroke-width="5" stroke-dasharray="26 22"><path d="M0 326h300"/></g>
<g transform="translate(120 330) scale(0.55)">
  <path d="M-120 40h240v-56q0-20-20-20h-70l-40-40h-70q-20 0-20 20v76z" class="coral o"/>
  <circle cx="-70" cy="40" r="26" fill="{INK}"/><circle cx="70" cy="40" r="26" fill="{INK}"/>
</g>
<g transform="translate(260 330) scale(0.5)">
  <path d="M-120 40h240v-56q0-20-20-20h-70l-40-40h-70q-20 0-20 20v76z" class="teal o"/>
  <circle cx="-70" cy="40" r="26" fill="{INK}"/><circle cx="70" cy="40" r="26" fill="{INK}"/>
</g>
<g transform="translate(400 326) scale(0.4)">
  <path d="M-120 40h240v-56q0-20-20-20h-70l-40-40h-70q-20 0-20 20v76z" class="gold o"/>
  <circle cx="-70" cy="40" r="26" fill="{INK}"/><circle cx="70" cy="40" r="26" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M330 180l-60 40"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M330 180l-60 100"/></g>''', ground=False)

add('hasten', '締め切りが迫って作業を急がせる', f'''
{table(380)}
{sit(220, 380, 1.05, 1, 'coral', 'blue', 'bun', 'sad', 'lap')}
{chair(220, 380, 1.0, 'gold', 1)}
<g transform="translate(300 290)">
  <path d="M-180-20h360v20h-360z" fill="#c9a464" class="o"/>
</g>
<g>
''' + ''.join(f'<g transform="translate({300+ (i%3)*44} {250+(i//3)*0}) rotate({-14+i*10})">{doc(0, 0, 60, 78, 2)}</g>' for i in range(3)) + f'''
</g>
<g transform="translate(470 160)">
  <circle r="58" fill="#fffdf6" class="o"/>
  <path d="M0 0v-40M0 0l30 18" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round" fill="none"/>
  <circle r="8" fill="{INK}"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
    <path d="M62-42q20 20 20 42M-62-42q-20 20-20 42"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M400 230l-100 30"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M140 220h50M120 260h40"/>
</g>''', ground=False)

add('hoist', '滑車で重い荷を高く引き上げる', f'''
{table(380)}
<g>
  <path d="M60 60h480v20H60z" fill="#8f9aa6" class="o"/>
  <circle cx="380" cy="110" r="30" fill="#c8d0d8" class="o"/>
  <circle cx="380" cy="110" r="10" fill="{INK}"/>
  <path d="M380 80v-20" stroke="{INK}" stroke-width="6" fill="none"/>
  <path d="M352 118v140M408 118v100" fill="none" stroke="{BRN}" stroke-width="6"/>
</g>
{box(352, 300, 110, 74, 24, 'gold')}
{person(490, 380, 1.0, -1, 'teal', 'blue', 'up', 'cap', 'neutral')}
<path d="M408 218q30 20 44 40" fill="none" stroke="{BRN}" stroke-width="6"/>
<g class="a" marker-end="url(#ar)" stroke-width="6"><path d="M240 300v-120"/></g>''', ground=False)

add('flatten', '丸めた生地をめん棒で平らにのばす', f'''
{split()}
{table(340)}
<g transform="translate(150 250)">
  <circle r="66" fill="#f0e0b8" class="o"/>
  <path d="M-40-20q40-24 80 0" fill="none" stroke="#d8c498" stroke-width="4"/>
</g>
<g transform="translate(450 290)">
  <ellipse rx="120" ry="22" fill="#f0e0b8" class="o"/>
  <g fill="none" stroke="#d8c498" stroke-width="3"><path d="M-90-4q90 16 180 0"/></g>
</g>
<g transform="translate(450 200)">
  <path d="M-90-14h180v28h-180z" fill="#c9a464" class="o"/>
  <path d="M-120-8h30v16h-30zM90-8h30v16H90z" fill="#a0764a" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>
<g class="a" marker-end="url(#ar)"><path d="M450 130v40"/></g>''', arrow=True, ground=False)

add('fluctuate', '値が上がったり下がったりを繰り返す', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(300 220)">
  <path d="M-250 140h500v6h-500z" fill="{INK}"/>
  <path d="M-250-160v300h6v-300z" fill="{INK}"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="7 7">
''' + ''.join(f'<path d="M-244 {-120+i*60}h490"/>' for i in range(5)) + f'''
  </g>
  <path d="M-230 40l40-70 40 90 40-120 40 100 40-60 40 80 40-110 40 90 40-50" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linejoin="round"/>
  <g fill="{TONES['coral'][2]}">
''' + ''.join(f'<circle cx="{-230+i*40}" cy="{[40,-30,60,-60,40,-20,60,-50,40,-10][i]}" r="6"/>' for i in range(10)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M96 330v-40"/></g>
<g class="a" marker-end="url(#ar)"><path d="M96 290v40"/></g>''', arrow=True, ground=False)

add('lengthen', '短かったズボンのすそを足して長くする', f'''
{split()}
{table(370)}
<g transform="translate(150 200)">
  <path d="M-60-90h120v50l-10 110h-40l-10-60-10 60h-40l-10-110z" class="bluep o"/>
  <path d="M-60-40h120" fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"/>
</g>
<g transform="translate(450 200)">
  <path d="M-60-90h120v50l-16 180h-40l-8-120-8 120h-40l-16-180z" class="bluep o"/>
  <path d="M-60-40h120" fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-dasharray="12 8"><path d="M-46 130h92"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>
<g class="a" marker-end="url(#ar)"><path d="M540 300v60"/></g>''', arrow=True, ground=False)

# --- 予測と決定 --------------------------------------------------------------
add('foresee', 'これから来る嵐を前もって見通す', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
{table(380)}
<g fill="#4a5560" stroke="{INK}" stroke-width="2.5">
  <path d="M340 150q-8-56 44-56 14-44 68-28 34-26 68 12 44-8 52 44 30 8 26 40H374q-30-2-34-12z"/>
</g>
<g fill="none" stroke="#fdf0d0" stroke-width="6" stroke-linecap="round">
  <path d="M400 210q-20 24-6 40M480 214q-22 26-6 44"/>
</g>
{person(140, 380, 1.05, 1, 'teal', 'blue', 'point', 'cap', 'neutral')}
<g transform="translate(220 250) rotate(-20)">
  <path d="M-70-16h100q30 0 30 16t-30 16H-70z" fill="#5a6270" class="o"/>
  <circle cx="66" r="18" fill="#e8f0f6" class="o"/>
  <circle cx="-76" r="14" fill="#e8f0f6" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M300 230h50"/></g>
{sun(80, 90, 26)}''', ground=False)

add('forewarn', '前もって危険を知らせて備えさせる', f'''
{table(380)}
<g transform="translate(430 260)">
  <path d="M-90 120l90-190 90 190z" class="gold o"/>
  <path d="M-6 20h12v50h-12z" fill="{INK}"/>
  <circle cy="94" r="7" fill="{INK}"/>
</g>
{person(140, 380, 1.05, 1, 'coral', 'blue', 'point', 'bun', 'neutral')}
<g transform="translate(230 180)">
  <path d="M-60-40h120q12 0 12 12v40q0 12-12 12h-84l-22 16v-16q-14 0-14-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <path d="M-26 6l26-46 26 46z" class="gold o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M300 180h60"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M40 340h520"/></g>''', ground=False)

add('decree', '王が正式な布告を読み上げて命じる', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-160-100h320v200h-320z" class="paper"/>
  <path d="M-160-100q-30 0-30 20t30 20M160-100q30 0 30 20t-30 20" fill="#f0eee6" class="o"/>
  <rect x="-110" y="-60" width="150" height="16" rx="8" fill="{INK}"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-110" y="{-20+i*30}" width="{220-(i%3)*50}" height="10" rx="5"/>' for i in range(3)) + f'''
  </g>
  <circle cx="110" cy="60" r="26" class="coral o"/>
</g>
{person(140, 380, 1.0, 1, 'violet', 'gold', 'up', 'bun', 'neutral')}
<g transform="translate(140 254)">
  <path d="M-32 10h64v10h-64z" class="gold o"/>
  <path d="M-32 10l-6-40 20 18 18-28 18 28 20-18-6 40z" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M230 200q26 30 0 60"/>
</g>''', ground=False)

add('defer', '会議の日を先の日付へ延ばす', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-190-140h380v280h-380z" class="paper"/>
  <path d="M-190-140h380v50h-380z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5">
''' + ''.join(f'<path d="M{-190+i*54} -90v230"/>' for i in range(8)) + ''.join(f'<path d="M-190 {-40+i*44}h380"/>' for i in range(5)) + f'''
  </g>
  <rect x="-176" y="-24" width="26" height="12" rx="6" fill="{MUTED}"/>
  <path d="M-186-18h46" stroke="{MUTED}" stroke-width="6" stroke-linecap="round" fill="none"/>
  <rect x="122" y="68" width="26" height="12" rx="6" class="coral"/>
  <circle cx="135" cy="74" r="24" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M130 200q160-90 300 70"/></g>''', arrow=True, ground=False)

add('dissuade', '危ないと説いて相手に思いとどまらせる', f'''
{table(380)}
{person(180, 380, 1.05, 1, 'teal', 'blue', 'reach', 'bun', 'neutral')}
{person(400, 380, 1.05, 1, 'coral', 'blue', 'stand', 'short', 'sad')}
<g transform="translate(540 300)">
  <path d="M-40 80l40-140 40 140z" class="gold o"/>
  <path d="M-4 10h8v34h-8z" fill="{INK}"/>
</g>
<g>
  <path d="M226 250q60-10 100 0" stroke="{SKIN}" stroke-width="20" stroke-linecap="round" fill="none"/>
  <path d="M226 250q60-10 100 0" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M440 210h-90"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M440 210h90"/></g>
<g transform="translate(150 200)">
  <path d="M-40-30h80q10 0 10 10v30q0 10-10 10h-52l-18 14v-14q-10 0-10-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M-18 6l18-32 18 32z" class="gold o"/>
</g>''', ground=False)

add('deregulate', 'びっしりあった規制の札が減って自由になる', f'''
{split()}
{table(380)}
<g>
''' + ''.join(f'''<g transform="translate({70+ (i%3)*70} {200+(i//3)*90})">
  <circle r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
  <path d="M-20 20L20-20" stroke="{TONES['coral'][0]}" stroke-width="7" fill="none"/>
</g>''' for i in range(6)) + f'''
</g>
<g transform="translate(450 250)">
  <circle r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
  <path d="M-20 20L20-20" stroke="{TONES['coral'][0]}" stroke-width="7" fill="none"/>
</g>
{person(520, 380, 0.85, 1, 'teal', 'blue', 'up', 'cap', 'smile')}
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('augment', '手持ちの量に足して総量を増やす', f'''
{split()}
{table(340)}
<g transform="translate(150 290)">
''' + ''.join(f'{coin(-40+ (i%3)*40, -20-(i//3)*36, 20)}' for i in range(3)) + f'''
</g>
<g transform="translate(450 290)">
''' + ''.join(f'{coin(-40+ (i%3)*40, -20-(i//3)*36, 20)}' for i in range(9)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>
<g transform="translate(300 130)">
  <path d="M-8-30h16v20h20v16h-20v20h-16v-20h-20v-16h20z" class="green o"/>
</g>''', arrow=True, ground=False)

add('apportion', '一つのパイを人数分に等しく切り分ける', f'''
{table(340)}
<g transform="translate(300 240)">
  <circle r="120" fill="#e8c98d" class="o"/>
  <circle r="100" fill="#f0dcae" class="o"/>
  <g fill="none" stroke="#c9a464" stroke-width="4">
''' + ''.join(f'<path d="M0 0l{100*math.cos(i*1.047):.0f} {100*math.sin(i*1.047):.0f}"/>' for i in range(6)) + f'''
  </g>
  <g fill="none" stroke="{INK}" stroke-width="3" stroke-dasharray="8 6">
''' + ''.join(f'<path d="M0 0l{112*math.cos(i*1.047):.0f} {112*math.sin(i*1.047):.0f}"/>' for i in range(6)) + f'''
  </g>
</g>
{head(90, 340, 20, 'coral', 'bob')}
{head(160, 350, 20, 'teal', 'short')}
{head(450, 348, 20, 'gold', 'bun')}
{head(520, 340, 20, 'violet', 'cap')}
<g class="a" marker-end="url(#ar)"><path d="M180 300l60-20"/></g>
<g class="a" marker-end="url(#ar)"><path d="M430 300l-60-20"/></g>''', arrow=True, ground=False)

add('bestow', '功績をたたえて勲章を授ける', f'''
{table(380)}
{person(180, 380, 1.05, 1, 'violet', 'gold', 'give', 'bun', 'smile')}
{person(430, 380, 1.05, -1, 'teal', 'blue', 'stand', 'short', 'smile')}
<g transform="translate(310 230)">
  <path d="M-24 26h48l-6 40-18-14-18 14z" class="coral o"/>
  <circle cy="0" r="30" class="gold o"/>
  <path d="M0-18l7 14 15 2-11 12 3 16-14-8-14 8 3-16-11-12 15-2z" class="goldd"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 170q70-40 120 10"/></g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M480 200l24-20M500 260h26"/>
</g>''', arrow=True, ground=False)

# --- 句動詞 -----------------------------------------------------------------
add('fall-out', '仲のよかった二人が言い争って仲たがいする', f'''
{split()}
{table(380)}
{person(110, 380, 0.95, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(200, 380, 0.95, -1, 'coral', 'blue', 'stand', 'bun', 'smile')}
<g fill="{TONES['coral'][0]}">
  <path d="M155 250q-16-22 0-30 16-8 20 10 4-18 20-10 16 8 0 30l-20 22z"/>
</g>
{person(380, 380, 0.95, -1, 'teal', 'blue', 'stand', 'short', 'sad')}
{person(520, 380, 0.95, 1, 'coral', 'blue', 'stand', 'bun', 'sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M424 240l52 40M476 240l-52 40"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M420 320l-40 30"/></g>
<g class="a" marker-end="url(#ar)"><path d="M480 320l40 30"/></g>''', arrow=True, ground=False)

add('get-round-to', 'ずっと後回しにしていた仕事にやっと手をつける', f'''
{table(380)}
<g>
''' + ''.join(f'<g transform="translate({140+i*8} {280-i*12}) rotate({-8+i*4})">{doc(0, 0, 130, 160, 4)}</g>' for i in range(4)) + f'''
</g>
{person(420, 380, 1.05, -1, 'teal', 'blue', 'reach', 'bun', 'smile')}
<g transform="translate(300 190)">
  <circle r="52" fill="#fffdf6" class="o"/>
  <path d="M0 0v-34M0 0l24 16" stroke="{INK}" stroke-width="6" stroke-linecap="round" fill="none"/>
  <circle r="7" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M360 120q-120-40-200 60"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M360 300h-100"/></g>''', ground=False)

add('hold-off', '決めるのを待って、あとに回す', f'''
{table(380)}
{sit(240, 380, 1.1, 1, 'violet', 'blue', 'bun', 'neutral', 'lap')}
{chair(240, 380, 1.0, 'gold', 1)}
<g transform="translate(400 270)">
  {doc(0, 0, 150, 180, 4)}
  <path d="M-50 60h100" stroke="{MUTED}" stroke-width="3" fill="none"/>
</g>
<g>
  <path d="M300 250q-30-14-46 4" stroke="{SKINL}" stroke-width="30" stroke-linecap="round" fill="none"/>
  <path d="M300 250q-30-14-46 4" stroke="{SKIN}" stroke-width="25" stroke-linecap="round" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M340 190h90"/></g>
<g transform="translate(140 180)">
  <circle r="46" fill="#fffdf6" class="o"/>
  <path d="M0 0v-30M0 0l20 14" stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M190 180h40"/></g>''', arrow=True, ground=False)

# --- 物・人 -----------------------------------------------------------------
add('folder', '書類をはさんでまとめる紙ばさみ', f'''
{table(340)}
<g transform="translate(300 250)">
  <path d="M-140-30h130l24-30h126v140h-280z" class="gold o"/>
  <path d="M-130 0h270v110h-270z" fill="#fffdf6" class="o"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-104" y="{22+i*26}" width="{218-(i%3)*50}" height="9" rx="4.5"/>' for i in range(3)) + f'''
  </g>
  <path d="M-140 20h280v100q0 12-14 12h-252q-14 0-14-12z" class="goldd o"/>
  <rect x="-40" y="46" width="80" height="14" rx="7" fill="{TONES['gold'][1]}"/>
</g>''', ground=False)

add('invoice', '品目と金額が並んだ請求書', f'''
{table(370)}
<g transform="translate(300 200) rotate(-3)">
  <path d="M-160-150h320v300h-320z" class="paper"/>
  <rect x="-124" y="-124" width="130" height="18" rx="9" fill="{INK}"/>
  <path d="M-124-90h248" stroke="{INK}" stroke-width="3" fill="none"/>
  <g>
''' + ''.join(f'''<g transform="translate(0 {-60+i*36})">
  <rect x="-124" y="-6" width="{130-(i%3)*30}" height="11" rx="5.5" fill="{MUTED}"/>
  <rect x="{60+(i%2)*20}" y="-6" width="{64-(i%2)*20}" height="11" rx="5.5" fill="{MUTED}"/>
</g>''' for i in range(4)) + f'''
  </g>
  <path d="M-124 96h248" stroke="{INK}" stroke-width="3" fill="none"/>
  <rect x="-124" y="112" width="80" height="14" rx="7" fill="{INK}"/>
  <rect x="40" y="110" width="84" height="18" rx="9" class="coral"/>
</g>
<g transform="translate(490 320)">
  <path d="M-40-24h80v48h-80z" class="greenp o"/>
  <circle r="13" fill="none" stroke="{TONES['green'][2]}" stroke-width="3"/>
</g>''', ground=False)

add('gram', 'はかりの目盛りが小さな重さを示す', f'''
{table(370)}
<g transform="translate(300 300)">
  <path d="M-120-40h240v50q0 16-24 16h-192q-24 0-24-16z" fill="#c8d0d8" class="o"/>
  <path d="M-140-40q0-30 140-30t140 30z" fill="#e0e6ea" class="o"/>
</g>
<g transform="translate(300 180)">
  <circle r="76" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
''' + ''.join(f'<path d="M{60*math.cos(math.pi*(0.75+i*0.05)):.0f} {60*math.sin(math.pi*(0.75+i*0.05)):.0f}L{72*math.cos(math.pi*(0.75+i*0.05)):.0f} {72*math.sin(math.pi*(0.75+i*0.05)):.0f}"/>' for i in range(31)) + f'''
  </g>
  <path d="M0 0l-40-42" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round" fill="none"/>
  <circle r="8" fill="{INK}"/>
</g>
<g transform="translate(300 250)">
  <path d="M-30-16h60v16h-60z" class="gold o"/>
  <path d="M-14-16q0-14 14-14t14 14" fill="none" stroke="{TONES['gold'][2]}" stroke-width="5"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 180l-100 10"/></g>''', arrow=True, ground=False)

add('guitar', '六本の弦を指ではじいて弾く', f'''
{table(380)}
<g transform="translate(280 250) rotate(-16)">
  <path d="M-40 20q-70 0-70-60t70-60q40 0 46 30 6 30 0 60-6 30-46 30z" fill="#c8934a" class="o"/>
  <path d="M40 20q70 0 70-70t-70-70q-44 0-50 34-6 36 0 72 6 34 50 34z" fill="#c8934a" class="o"/>
  <circle cx="30" cy="-38" r="28" fill="#5b4a3c" class="o"/>
  <path d="M-40-16h120v34h-120z" fill="#8b6437" class="o"/>
  <path d="M-110-14h-90v22h90z" fill="#5b4a3c" class="o"/>
  <path d="M-200-24h-40v42h40z" fill="#c8934a" class="o"/>
  <g fill="none" stroke="#e8dcc0" stroke-width="2">
''' + ''.join(f'<path d="M76 {-10+i*6}H-196"/>' for i in range(6)) + f'''
  </g>
  <g fill="none" stroke="#8f9aa6" stroke-width="3">
''' + ''.join(f'<path d="M{-190+i*22} -14v22"/>' for i in range(8)) + f'''
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M430 170q26 30 0 60M460 146q40 52 0 104"/>
</g>''', ground=False)

add('hairdresser', '美容師がはさみで客の髪を切る', f'''
{table(380)}
{sit(300, 380, 1.15, 1, 'coral', 'blue', 'bob', 'smile', 'lap')}
{chair(300, 380, 1.05, 'gold', 1)}
<g transform="translate(300 320)">
  <path d="M-70-60q70-30 140 0 10 60-16 74-54 12-108 0-26-14-16-74z" class="tealp o"/>
</g>
{person(140, 380, 1.05, 1, 'teal', 'teal', 'reach', 'bun', 'smile')}
<g transform="translate(230 226) rotate(-24)">
  <g stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
    <path d="M-6-6l-70-26q-10-4-6-12t14-4L8-24z" fill="#cfd6dd"/>
    <path d="M-6 6l-70 26q-10 4-6 12t14 4L8 24z" fill="#8f9aa6"/>
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round">
    <path d="M12-12q36-14 50 4t-12 24"/><path d="M12 12q36 14 50-4t-12-24"/>
  </g>
</g>
<g fill="{HAIR}">
''' + ''.join(f'<path d="M{330+i*30} {330+(i%3)*20}q14-10 22 4-14 10-22-4z"/>' for i in range(5)) + f'''
</g>''', ground=False)

add('hashtag', '投稿の下に # のついた語が並んでいる', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-180-150h360v300h-360z" fill="#fffefd" class="o"/>
  <path d="M-180-150h360v50h-360z" class="teal o"/>
  <g fill="#fffefd"><circle cx="-152" cy="-125" r="14"/><rect x="-126" y="-133" width="110" height="16" rx="8"/></g>
  <path d="M-150-80h300v110h-300z" class="bluep o"/>
  <g fill="{TONES['blue'][0]}"><circle cx="-90" cy="-40" r="22"/><path d="M-40 30l50-70 40 44 30-30 60 56z"/></g>
  <g>
''' + ''.join(f'''<g transform="translate({-140+i*116} 70)">
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5">
    <path d="M-6-14v28M6-14v28M-14-6h28M-14 6h28"/>
  </g>
  <rect x="22" y="-7" width="{70-i*14}" height="14" rx="7" fill="{TONES['teal'][0]}"/>
</g>''' for i in range(3)) + f'''
  </g>
</g>''', ground=False)

add('holiday', 'カレンダーの赤い日に浜辺で休んでいる', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v70H0z" fill="#7aa8c4"/>
<path d="M0 300h600v100H0z" fill="#f0dfb8"/>
<path d="M0 230h600M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
{sun(500, 80, 40)}
<g transform="translate(200 300)">
  <path d="M-6 0v-70h12V0z" fill="{BRN}"/>
  <path d="M-90-70h180q-30-44-90-44t-90 44z" class="coralp o"/>
  <path d="M-90-70h180" fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"/>
</g>
<g transform="translate(230 350) rotate(-8)">
  <path d="M-70-16h140v32h-140z" class="tealp o"/>
  <path d="M-70-16h140" fill="none" stroke="{TONES['teal'][0]}" stroke-width="3"/>
</g>
<g transform="translate(470 330)">
  <path d="M-60-70h120v140h-120z" class="paper"/>
  <path d="M-60-70h120v30h-120z" class="coral o"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="{-48+ (i%4)*28}" y="{-28+(i//4)*26}" width="18" height="16" rx="3"/>' for i in range(12)) + f'''
  </g>
  <rect x="8" y="24" width="18" height="16" rx="3" class="coral"/>
</g>''', ground=False)

add('honeymoon', '結婚したばかりの二人が旅先で写真を撮る', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v70H0z" fill="#7aa8c4"/>
<path d="M0 300h600v100H0z" fill="#f0dfb8"/>
<path d="M0 230h600M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
{sun(500, 70, 34)}
{person(250, 360, 1.05, 1, 'coral', 'coral', 'stand', 'bun', 'smile')}
{person(340, 360, 1.05, -1, 'teal', 'blue', 'stand', 'short', 'smile')}
<g fill="{TONES['coral'][0]}">
  <path d="M295 216q-14-20 0-28 14-6 18 10 4-16 18-10 14 8 0 28l-18 20z"/>
</g>
<g transform="translate(120 300)">
  <path d="M-6 0v-60h12V0z" fill="{BRN}"/>
  <path d="M-50-60q-30-20-40-44 40 4 50 40zM6-64q30-24 60-6-30 30-60 6zM0-64q-14-40 4-52 20 14 6 52z" class="greenp o"/>
</g>
<g transform="translate(480 250)">
  <path d="M-40-26h80v52h-80z" fill="#3b4450" class="o"/>
  <circle cx="6" r="16" fill="#8f9aa6" class="o"/><circle cx="6" r="8" fill="{INK}"/>
  <path d="M-36-26h22v-8h-22z" fill="#3b4450"/>
</g>''', ground=False)

add('fuse', '切れたヒューズを新しいものに替える', f'''
{split()}
{table(340)}
<g transform="translate(150 250)">
  <path d="M-90-24h180v48h-180z" fill="#e8dcc0" class="o"/>
  <path d="M-90-24h24v48h-24zM66-24h24v48H66z" fill="#b8bfc8" class="o"/>
  <path d="M-60 0q30-30 60 0" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M10 0q20-20 44 0" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M-8-12l14 24" stroke="{TONES['coral'][0]}" stroke-width="5" fill="none"/>
</g>
{cross(150, 130, 0.7)}
<g transform="translate(450 250)">
  <path d="M-90-24h180v48h-180z" fill="#e8dcc0" class="o"/>
  <path d="M-90-24h24v48h-24zM66-24h24v48H66z" fill="#b8bfc8" class="o"/>
  <path d="M-64 0q64-30 128 0" fill="none" stroke="{TONES['gold'][0]}" stroke-width="5"/>
</g>
{tick(450, 130, 0.7)}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M450 330h-40M450 330h40"/>
</g>''', ground=False)

add('fracture', 'レントゲンに骨のひびが写っている', f'''
<path d="M0 0h600v400H0z" fill="#1e2430"/>
<g transform="translate(300 200)">
  <path d="M-180-160h360v320h-360z" fill="#2c3542" class="o"/>
  <g fill="#c8d4dc" opacity="0.9">
    <path d="M-34-130h68v40q0 20-20 26v130q0 20 20 26v40h-68v-40q20-6 20-26V-64q0-20-20-26z"/>
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5">
    <path d="M-30 30l60 16M-24 46l50-30"/>
  </g>
  <circle cx="0" cy="36" r="52" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M500 320l-140-70"/></g>''', arrow=True, ground=False)

add('glimmer', '真っ暗な中に、遠くの小さな明かりがかすかに光る', f'''
<path d="M0 0h600v400H0z" fill="#181d2a"/>
<path d="M0 340h600v60H0z" fill="#111520" class="o"/>
<g transform="translate(400 200)">
  <circle r="14" fill="#fdf0d0"/>
  <circle r="30" fill="#fdf0d0" opacity="0.28"/>
  <circle r="56" fill="#fdf0d0" opacity="0.12"/>
  <g fill="none" stroke="#fdf0d0" stroke-width="3" opacity="0.6" stroke-linecap="round">
    <path d="M-40 0h-16M40 0h16M0-40v-16M0 40v16"/>
  </g>
</g>
{person(150, 340, 1.05, 1, 'teal', 'blue', 'point', 'cap', 'neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M230 240h130"/></g>
<g fill="#2b3242"><path d="M0 300h600v40H0z"/></g>''', ground=False)

add('inhabit', '洞穴を家にして動物が住んでいる', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v170H0z" fill="#c9d8c0"/>
<path d="M0 230h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M180 230q0-160 160-160t160 160z" fill="#8f9aa6" class="o"/>
<path d="M260 230q0-90 80-90t80 90z" fill="#2c333d" class="o"/>
<g transform="translate(340 200) scale(0.75)">
  <ellipse rx="60" ry="40" fill="#a0764a" class="o"/>
  <circle cx="54" cy="-26" r="30" fill="#a0764a" class="o"/>
  <path d="M40-50q-8-38 8-38 14 6 10 38zM70-50q8-36 24-30 6 12-10 32z" fill="#a0764a" class="o"/>
  <circle cx="64" cy="-30" r="4" fill="{INK}"/>
  <circle cx="80" cy="-20" r="6" fill="{SKINL}"/>
  <g stroke="#8b6437" stroke-width="10" stroke-linecap="round" fill="none"><path d="M-24 38v14M22 38v14"/></g>
</g>
{tree(80, 260, 0.9)}
{tree(540, 270, 1.0)}
<g class="a" marker-end="url(#ar)"><path d="M120 120q100 20 160 70"/></g>''', arrow=True, ground=False)

add('easygoing', 'こまかいことを気にせず、のんびり構えている', f'''
{split()}
{table(380)}
{sit(150, 380, 1.1, 1, 'blue', 'blue', 'short', 'sad', 'up')}
{chair(150, 380, 1.0, 'gold', 1)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M100 230l-24-18M200 224l24-18"/>
</g>
<g transform="translate(150 290)">{doc(0, 0, 80, 50, 2)}</g>
<g transform="translate(450 380)">
  <path d="M-70-30h140v30h-140z" class="gold o"/>
  <path d="M-70-30q0-40 70-40t70 40z" class="goldp o"/>
  <path d="M-30-6l-40 24M30-6l40 24" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-30-110q30-16 60 0l-8 80h-44z" class="coral o"/>
  <path d="M-28-100l-46 30M28-100l46 30" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cy="-140" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['bun']}" transform="translate(0 -32) scale(1.08)" fill="{HAIR}"/>
  <path d="M-16-142q10-8 18 0M-2-142q10-8 18 0" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <path d="M-10-126q10 10 20 0" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M540 210l-24-18M550 260h-26"/>
</g>''', ground=False)

add('fluent', 'よどみなく言葉が流れ出てくる', f'''
{table(380)}
{person(160, 380, 1.15, 1, 'teal', 'blue', 'up', 'bun', 'smile')}
<g>
''' + ''.join(f'''<g transform="translate({280+ (i%3)*110} {150+(i//3)*80})">
  <path d="M-50-30h100q10 0 10 10v30q0 10-10 10h-66l-18 14v-14q-16 0-16-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <rect x="-34" y="-8" width="{68-(i%3)*14}" height="14" rx="7" fill="{INK}"/>
</g>''' for i in range(6)) + f'''
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="12 8">
  <path d="M230 240q60-100 160-80t180 40"/>
</g>''', ground=False)

add('fluffy', '空気を含んでふわふわにふくらんだタオル', f'''
{split()}
{table(340)}
<g transform="translate(150 260)">
  <path d="M-70-16h140v40h-140z" class="bluep o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"><path d="M-60 4h120"/></g>
</g>
<g transform="translate(450 250)">
  <path d="M-84 40q-30-50 0-76 40-34 90-16 60 20 62 60 0 38-70 42-70 4-82-10z" fill="#e1edfb" class="o"/>
  <g fill="#c8dcf4">
''' + ''.join(f'<circle cx="{-56+ (i%4)*38}" cy="{-14+(i//4)*30}" r="16"/>' for i in range(8)) + f'''
  </g>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"><path d="M-70 20q70 20 140 0"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('foolish', '傘を持たずに大雨の中へ出ていく', f'''
<path d="M0 0h600v400H0z" fill="#c8d2da"/>
{table(380)}
{cloud(300, 90, 1.5, 'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{50+i*40} {170+(i%3)*40}l-14 44"/>' for i in range(13)) + f'''
</g>
{person(380, 380, 1.15, 1, 'coral', 'blue', 'up', 'short', 'smile', 'walk')}
<g transform="translate(140 330)">
  <path d="M-50 0q0-50 50-50t50 50q-16-14-32-14t-18 8q-16-12-32-8T-50 0z" class="teal o"/>
  <path d="M0 0v60q0 14 16 14" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
</g>
{cross(140, 220, 0.7)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M470 200l24-20M490 260h26"/>
</g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
