# -*- coding: utf-8 -*-
"""第117回の描き直し。線が顔からずれた jaw と、形が読めない3点。"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))

def bighead(x=250, y=210, r=130):
    return (f'<g transform="translate({x} {y})">'
            f'<path d="M0-{r}q{r*0.82} 0 {r*0.82} {r*0.72}q0 {r*0.86}-{r*0.82} {r*0.86}'
            f'q-{r*0.82} 0-{r*0.82}-{r*0.86}q0-{r*0.72} {r*0.82}-{r*0.72}z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>'
            f'<path d="M-{r*0.86}-{r*0.3}q4-{r*0.86} {r*0.86}-{r*0.86}t{r*0.86} {r*0.86}q-{r*0.3}-{r*0.24}-{r*0.86}-{r*0.1}'
            f'q-{r*0.4}-{r*0.2}-{r*0.86} {r*0.1}z" fill="{HAIR}" stroke="{INK}" stroke-width="2.5"/>'
            f'<circle cx="-{r*0.34}" cy="-{r*0.1}" r="{r*0.075}" fill="{INK}"/>'
            f'<circle cx="{r*0.34}" cy="-{r*0.1}" r="{r*0.075}" fill="{INK}"/>'
            f'<path d="M-{r*0.3} {r*0.36}q{r*0.3} {r*0.2} {r*0.6} 0" fill="none" stroke="{INK}" stroke-width="{r*0.05}" stroke-linecap="round"/>'
            f'</g>')

def point(x1, y1, x2, y2):
    return f'<g class="a" marker-end="url(#ar)"><path d="M{x1} {y1}L{x2} {y2}"/></g>'

add('jaw', '顔の下半分、あごの輪郭が太い線でなぞられている', f'''
{bighead(250, 210)}
<path d="M144 202q0 122-38 122t-70-42q-32-42-32-80"
      fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"
      transform="translate(140 0) scale(-1 1) translate(-390 0)"/>
<path d="M356 202q0 42-32 84-34 42-74 42t-74-42q-32-42-32-84"
      fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"/>
{point(490, 254, 380, 232)}''', arrow=True, ground=False)

add('eyelid', '片目だけまぶたが下りて閉じている', f'''
{bighead(250, 210)}
<g>
  <ellipse cx="207" cy="197" rx="34" ry="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M173 197q34 24 68 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <g fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round">
    <path d="M182 210l-8 12M200 216v14M220 214l6 14M238 206l12 10"/>
  </g>
</g>
<ellipse cx="207" cy="197" rx="46" ry="38" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
{point(470, 128, 252, 176)}''', arrow=True, ground=False)

add('collarbone', '首の下を左右に走る二本の鎖骨がはっきり示されている', f'''
<g transform="translate(300 200)">
  <path d="M0-150q48 0 48 46 0 32-22 46 76 22 76 86v78h-204v-78q0-64 76-86-22-14-22-46 0-46 48-46z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <ellipse cy="-16" rx="16" ry="10" fill="{SKINL}" opacity="0.5"/>
</g>
<g fill="none" stroke="#e8e0cf" stroke-width="16" stroke-linecap="round">
  <path d="M292 194q-34 22-86 16M308 194q34 22 86 16"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round">
  <path d="M292 194q-34 22-86 16M308 194q34 22 86 16"/>
</g>
<circle cx="300" cy="192" r="10" fill="#e8e0cf" stroke="{INK}" stroke-width="2.5"/>
{point(510, 148, 406, 196)}''', arrow=True, ground=False)

add('gauze', '目の粗い白いガーゼが四つ折りにされ、傷に当てられている', f'''
<g transform="translate(300 210) rotate(-12)">
  <path d="M-190 34q-16-36 20-48l320-30q40-4 44 26t-38 34l-320 34q-18 2-26-16z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g transform="translate(280 186) rotate(-12)">
  <rect x="-90" y="-64" width="180" height="128" rx="6" fill="#fffefd" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#c8d2da" stroke-width="2.5">
''' + ''.join(f'<path d="M{-82+i*15} -64v128"/>' for i in range(12)) + ''.join(f'<path d="M-90 {-56+i*15}h180"/>' for i in range(8)) + f'''
  </g>
  <path d="M-90-64h180v128h-180z" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-90 0h180M0-64v128" stroke="#9fb0bd" stroke-width="4" fill="none"/>
</g>
{point(500, 96, 396, 148)}''', arrow=True, ground=False)

print(sheet(W, '/tmp/vocab-sheet2.html', 4))
