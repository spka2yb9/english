"""第110回: 副詞・句動詞45語。"""
from lib import *
W=[]
def add(slug,a,b,**k): W.append(emit(slug,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'
def qmark(x,y,s=1,cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-24-26q0-28 26-28t26 26q0 22-26 28v12" fill="none" stroke="{TONES[cls][0]}" stroke-width="10" stroke-linecap="round"/>'
            f'<circle cy="36" r="7" class="{cls}"/></g>')
def clock(x,y,r=60,hand=-90):
    import math
    ex, ey = x+r*0.55*math.cos(math.radians(hand)), y+r*0.55*math.sin(math.radians(hand))
    return (f'<g><circle cx="{x}" cy="{y}" r="{r}" fill="#fffdf6" class="o"/>'
            f'<path d="M{x} {y}v-{r*0.6:.0f}" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M{x} {y}L{ex:.0f} {ey:.0f}" fill="none" stroke="{TONES["coral"][0]}" stroke-width="5" stroke-linecap="round"/>'
            f'<circle cx="{x}" cy="{y}" r="6" class="ink"/></g>')

add('fundamentally', '根っこの土台まで掘り下げるイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-160-140h320v100h-320z" class="tealp o"/>
  <path d="M-200-40h400v60h-400z" class="teal o"/>
</g>
<g transform="translate(300 330)">
  <circle r="56" fill="none" stroke="{INK}" stroke-width="9"/>
  <path d="M40 40l40 40" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>
</g>
<path d="M60 390h480" class="a"/>
""", ground=True)

add('genuinely', '心の底からそう思うイラスト。', f"""
{person(200,352,1.3,1,'teal','blue','hold','short','smile')}
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2.5">
  <path d="M420 200q-34-44 0-62 34-18 34 24 0-42 34-24 34 18 0 62l-34 34z"/>
</g>
{ck(420,330,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('get-across', '言いたいことが相手に伝わるイラスト。', f"""
{person(140,352,1.15,1,'teal','blue','point','short','neutral')}
<g transform="translate(300 190)">
  <path d="M-80-50h160v80h-160zM-50 30l-12 26 34-26z" fill="#fffdf6" class="o"/>
  <circle r="20" class="coral o"/>
</g>
{person(470,352,1.15,-1,'coral','gold','stand','bob','smile')}
<g class="a" marker-end="url(#ar)"><path d="M240 280h150"/></g>
{ck(470,180,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('get-around', 'じゃまを回りこんで進むイラスト。', f"""
{person(130,352,1.1,1,'teal','blue','walk','short','neutral')}
<g transform="translate(300 300)">
  <path d="M-80 60q-20-70 10-100 40-34 100-10 46 22 30 110z" fill="#8b98a6" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M200 300q60-160 200-120t130 100"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('get-by', 'ぎりぎりの分でなんとかやっていくイラスト。', f"""
<g transform="translate(240 250)">
  <path d="M-100-120h200v240h-200z" fill="#fffdf6" class="o"/>
  <path d="M-100 60h200v60h-200z" class="teal o"/>
  <path d="M-120 50h240v10h-240z" class="coral o"/>
</g>
{person(470,352,1.15,1,'teal','blue','stand','short','neutral')}
{ck(470,200,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('get-over', '病から立ち直って元気になるイラスト。', f"""
<g transform="translate(170 320)">
  <path d="M-100 20h200v14h-200z" class="ink"/>
  <path d="M-100-12h200v32h-200z" fill="#fffdf6" class="o"/>
  <path d="M-100-46h44v34h-44z" class="bluep o"/>
</g>
{person(450,352,1.25,1,'teal','blue','up','short','smile')}
<g fill="none" stroke="{GRN}" stroke-width="6" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M280 250q80-90 150-40"/></g>
{ck(360,140,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('hence', 'だからこうすると続けるイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-100-100h200v200h-200z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="12" marker-end="url(#ar)"><path d="M300 230h60"/></g>
{person(470,352,1.15,1,'coral','blue','walk','short','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('hopefully', 'うまくいくといいなと願うイラスト。', f"""
{person(210,352,1.25,1,'teal','blue','hold','short','smile')}
{sun(460,150,44)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M290 240q80-60 120-50"/></g>
{ck(300,340,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('however', 'ところが一方こうだと折り返すイラスト。', f"""
<g transform="translate(160 220)">
  <path d="M-90-90h180v180h-180z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linejoin="round" marker-end="url(#ar)">
  <path d="M280 160h60v130h60"/>
</g>
<g transform="translate(470 290)">
  <path d="M-80-80h160v160h-160z" class="coralp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('in-terms-of', 'あるものさしで見たときの姿のイラスト。', f"""
<g transform="translate(430 240)">
  <path d="M-110-110h220v220h-220z" class="teal o"/>
</g>
<g transform="translate(180 240)">
  <path d="M-70-120h140v240h-140z" class="goldp o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">{''.join(f'<path d="M-70 {-100+i*40}h{26 if i%2==0 else 16}"/>' for i in range(6))}</g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M260 240h50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('in-the-meantime', 'ふたつの用事のあいだの時間のイラスト。', f"""
<g transform="translate(300 160)">
  <circle cx="-200" cy="0" r="40" class="teal o"/>
  <circle cx="200" cy="0" r="40" class="teal o"/>
  <path d="M-200 0h400" class="a"/>
  <path d="M-140 60h280v40h-280z" class="goldp o"/>
</g>
{sit(300,376,0.9,1,'coral','blue','short','neutral','lap')}
<g transform="translate(360 330)"><path d="M-40-14h80v28h-80z" class="paper"/></g>
""", ground=False)

add('keep-up-with', '動く相手に遅れずついていくイラスト。', f"""
{person(230,352,1.2,1,'teal','blue','walk','short','neutral')}
{person(370,352,1.2,1,'coral','gold','walk','bob','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M450 250h90"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M300 190v190"/></g>
{ck(140,200,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('let-down', '当てにしていたのに裏切られるイラスト。', f"""
{person(170,352,1.2,1,'coral','blue','reach','short','sad')}
{person(450,352,1.15,-1,'teal','gold','stand','bob','neutral')}
<g transform="translate(320 330) rotate(24)">
  <path d="M-44-30h88v56h-88z" class="paper"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M380 220l-60 60"/></g>
{xx(300,150,1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('live-up-to', '求められた線にきちんと届くイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-200-60h400v10h-400z" class="coral o"/>
  <path d="M-110 100V-50h220v150z" class="teal o"/>
</g>
{ck(500,150,1.1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('look-down-on', '高い所から相手を見くだすイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-100 110h200v20h-200z" class="goldd o"/>
  <path d="M-70 90h140v20h-140z" class="gold o"/>
</g>
{person(180,340,1.15,1,'violet','violet','point','bun','neutral')}
{person(450,352,1,-1,'teal','blue','stand','short','sad')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M270 250l120 60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('look-into', '中身を細かく調べるイラスト。', f"""
<g transform="translate(340 300)">
  <path d="M-130-40h260v100h-260z" class="goldd o"/>
  <path d="M-130-40l-16-50h292l-16 50z" class="goldp o"/>
</g>
<g transform="translate(300 170)">
  <circle r="76" fill="none" stroke="{INK}" stroke-width="10"/>
  <circle r="66" fill="#fffdf6" opacity="0.4"/>
  <path d="M54 54l50 50" fill="none" stroke="{INK}" stroke-width="14" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('look-up-to', '高い所の人を仰ぎ見るイラスト。', f"""
<g transform="translate(420 250)">
  <path d="M-90 110h180v20h-180z" class="goldd o"/>
  <path d="M-60 90h120v20h-120z" class="gold o"/>
</g>
{person(420,340,1.2,-1,'violet','violet','stand','bun','smile')}
{person(160,352,1.1,1,'teal','blue','up','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M240 260l100-40"/></g>
{ck(300,140,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('make-up-for', '足りない分を埋め合わせるイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-160-120h320v240h-320z" fill="#fffdf6" class="o"/>
  <path d="M-160 0h320v120h-320z" class="teal o"/>
  <path d="M-160-80h320v80h-320z" class="coralp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M520 300V200"/></g>
{ck(120,160,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('nonetheless', 'よくない点があってもやはりこうなるイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
</g>
{xx(170,240,1.4)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M290 240h60"/></g>
<g transform="translate(460 240)">
  <path d="M-80-80h160v160h-160z" class="teal o"/>
</g>
{ck(460,240,1.4,'#fffdf6')}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('on-behalf-of', 'みんなを代表して前に立つイラスト。', f"""
{person(180,352,1.3,1,'violet','blue','point','bun','neutral')}
<g transform="translate(180 330)">
  <path d="M-56-40h112l16 60h-144z" class="goldd o"/>
</g>
{person(400,356,0.8,1,'teal','blue','stand','short','neutral')}
{person(470,356,0.8,1,'coral','gold','stand','bob','neutral')}
{person(540,356,0.8,-1,'green','blue','stand','short','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M350 220h-90"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('predominantly', '混じりの大半がひとつで占められるイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="150" class="teal o"/>
  <path d="M0 0v-150A150 150 0 0 1 75 130z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M540 340L360 260"/></g>
""", ground=False, arrow=True)

add('presumably', 'たぶんこうだろうと当たりをつけるイラスト。', f"""
{person(170,352,1.2,1,'teal','blue','think','short','neutral')}
<g transform="translate(430 230)" opacity="0.55">
  <path d="M-90-90h180v180h-180z" class="teal o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M260 250h70"/></g>
{qmark(330,140,1)}
{ck(500,340,0.7)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('put-up-with', 'うるさくても黙って耐えるイラスト。', f"""
{person(200,352,1.25,1,'teal','blue','stand','short','neutral')}
<g transform="translate(440 250)">
  <path d="M-50-40h50v80h-50z" class="ink"/>
  <path d="M0-70l70-40v220L0 40z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M330 210q-24 30 0 60M290 180q-46 60 0 120"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"><path d="M120 200l-16-22M280 190v-24"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('rather', 'かなりの程度まで来ているイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-160 0a160 160 0 0 1 320 0z" fill="#fffdf6" class="o"/>
  <path d="M-160 0h320" class="a"/>
  <path d="M0 0l110-90" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"/>
  <circle r="10" class="ink"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M0 -140v-16" transform="rotate({-90+i*45})"/>' for i in range(5))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('regardless-of', '事情がどうであれ変わらず進むイラスト。', f"""
{cloud(150,110,1.3,'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
  {''.join(f'<path d="M{100+i*32} {180+(i%3)*16}l-14 44"/>' for i in range(5))}
</g>
<g transform="translate(340 320)">
  <path d="M-70 40q-16-50 8-74 34-28 84-8 40 18 24 82z" fill="#8b98a6" class="o"/>
</g>
{person(480,352,1.2,1,'coral','blue','walk','short','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M120 250q140-110 300-60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('reportedly', '報じられたところではそうらしいイラスト。', f"""
<g transform="translate(280 220)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <path d="M-140-110h280v40h-280z" class="ink"/>
  <path d="M-140-50h120v90h-120z" class="tealp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M0-50h140M0-20h140M0 10h100M-140 70h280M-140 100h220"/></g>
</g>
{qmark(500,320,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('still', '今もなお続いているイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M60 300h480"/></g>
<g class="teal o"><rect x="120" y="230" width="330" height="60"/></g>
{clock(490,180,54,60)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M450 230v-20"/></g>
""", ground=False, arrow=True)

add('supposedly', '確かめてはいないがそういうことになっているイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-130-110h260v220h-260z" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" stroke-dasharray="14 12"/>
  <circle r="60" class="tealp o" opacity="0.6"/>
</g>
{qmark(480,150,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('take-off', '飛行機が地面を離れて飛び立つイラスト。', f"""
{plane(360,150,0.85,-18,'teal')}
<path d="M40 320h520v50H40z" fill="#dfe6ea" class="o"/>
<g fill="none" stroke="#fffdf6" stroke-width="5" stroke-dasharray="26 22"><path d="M40 345h520"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M100 300q160-40 220-130"/></g>
""", ground=False, arrow=True)

add('take-over', '別の会社が引き継いで手に入れるイラスト。', f"""
{tower(170,320,0.65,'teal',4)}
{tower(450,320,0.65,'coral',4)}
<g class="a" marker-end="url(#ar)"><path d="M370 170H250"/></g>
<g transform="translate(310 260)">
  <circle r="22" fill="none" stroke="{TONES['gold'][2]}" stroke-width="9"/>
  <path d="M20 0h56v10h-14v14h-12v-14h-12v14h-12v-14h-6z" fill="{TONES['gold'][2]}"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('terribly', '目盛りが振り切れるほどひどいイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-160 0a160 160 0 0 1 320 0z" fill="#fffdf6" class="o"/>
  <path d="M-160 0h320" class="a"/>
  <path d="M80-139A160 160 0 0 1 160 0h-80z" class="coralp"/>
  <path d="M0 0l152-40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"/>
  <circle r="11" class="ink"/>
</g>
{face(120,150,60,'sad')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('thankfully', 'うまくいってほっと感謝するイラスト。', f"""
{person(250,352,1.3,1,'teal','blue','hold','short','smile')}
<g class="o" fill="#e1edfb"><circle cx="360" cy="230" r="18"/><circle cx="392" cy="200" r="12"/></g>
{ck(470,200,1.2)}
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M150 180q-18-24 0-34 18-10 18 14 0-24 18-14 18 10 0 34l-18 18z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('thereafter', 'その時から後ずっとを指すイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M60 250h480"/></g>
<circle cx="220" cy="250" r="24" class="coral o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="14" stroke-linecap="round"><path d="M240 250h280"/></g>
<g class="ink">{''.join(f'<circle cx="{300+i*70}" cy="250" r="9"/>' for i in range(4))}</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M220 290v40"/></g>
""", ground=False, arrow=True)

add('thereby', 'それによってこうなると示すイラスト。', f"""
<g transform="translate(180 240)">
  <circle r="70" fill="none" stroke="{MUTED}" stroke-width="18"/>
  <g fill="{MUTED}">{''.join(f'<rect x="-10" y="-92" width="20" height="24" transform="rotate({a})"/>' for a in range(0,360,45))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" marker-end="url(#ar)"><path d="M300 240h60"/></g>
<g transform="translate(460 240)">
  <path d="M-70-70h140v140h-140z" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('thus', 'こうしてこの結びに至るイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-230-50h110v100h-110z" class="tealp o"/>
  <path d="M-100-50h110v100h-110z" class="tealp o"/>
  <path d="M30-70h140v140H30z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M190 240h30M320 240h30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('truly', 'まぎれもなく本物だと示すイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-140-130h280v260h-280z" class="paper"/>
  <circle cx="0" cy="20" r="60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
  <path d="M-30 20l20 24 46-54" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-100-90h200M-100-60h150"/></g>
</g>
{ck(500,150,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('undoubtedly', '疑いの余地なく確かなイラスト。', f"""
{qmark(180,220,1.8)}
{xx(180,220,1.8,MUTED)}
<g class="a" marker-end="url(#ar)"><path d="M290 230h60"/></g>
{ck(460,220,2.2)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('use-up', '残らず使い切るイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-90-120h180v240h-180z" fill="#fffdf6" class="o"/>
  <path d="M-90-110h180v230h-180z" class="teal o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M310 250h60"/></g>
<g transform="translate(470 250)">
  <path d="M-90-120h180v240h-180z" fill="#fffdf6" class="o"/>
</g>
{xx(470,250,1.4)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('wear-out', '履きつぶして穴があくイラスト。', f"""
<g transform="translate(180 300)">
  <path d="M-90 40q0-40 30-50l20-50h50v50l40 20q20 10 20 30z" class="teal o"/>
  <path d="M-90 40h150" class="a"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 260h60"/></g>
<g transform="translate(460 300)">
  <path d="M-90 40q0-40 30-50l20-50h50v50l40 20q20 10 20 30z" class="tealp o"/>
  <g fill="#fffaf1" stroke="{INK}" stroke-width="2.5"><circle cx="-30" cy="10" r="14"/><circle cx="40" cy="24" r="10"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('whatsoever', 'まったく何ひとつないイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-150-130h300v260h-300z" fill="#fffdf6" class="o"/>
</g>
{xx(300,240,3)}
""", ground=False)

add('whereby', 'その仕組みによって結果が出るイラスト。', f"""
<g transform="translate(200 240)">
  <path d="M-120-110h240v220h-240z" fill="#fffdf6" class="o"/>
  <circle cx="-30" cy="-20" r="46" fill="none" stroke="{MUTED}" stroke-width="14"/>
  <circle cx="46" cy="40" r="32" fill="none" stroke="{MUTED}" stroke-width="12"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M340 240h50"/></g>
<g transform="translate(470 240)">
  <path d="M-60-60h120v120h-120z" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('whilst', '一方が続くあいだにもう一方も進むイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-230-70h320v56h-320z" class="teal o"/>
  <path d="M-90 14h320v56H-90z" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M210 120v220M390 120v220"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" marker-end="url(#ar)"><path d="M300 360h-90M300 360h90"/></g>
""", ground=False, arrow=True)

add('wholly', 'すみずみまで一色に染まるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" class="teal o"/>
</g>
{ck(300,380,1)}
""", ground=False)

add('congressional', '議会にかかわることを示すイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-220 0h440v20h-440z" class="teald o"/>
  <path d="M-170-130h340v130h-340z" fill="#fffdf6" class="o"/>
  <g class="tealp o">{''.join(f'<rect x="{-150+i*60}" y="-120" width="40" height="120"/>' for i in range(5))}</g>
  <path d="M-190-130h380l-70-60h-240z" class="teal o"/>
  <path d="M-70-190q70-90 140 0z" class="teal o"/>
  <path d="M-6-206h12v20h-12z" class="gold o"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('profession', '専門の技を持って働く職のイラスト。', f"""
{person(190,352,1.25,1,'violet','blue','stand','bun','smile')}
<g fill="none" stroke="{INK}" stroke-width="5"><path d="M166 250q-16 40 14 56M214 250q16 40-14 56"/></g>
<circle cx="190" cy="312" r="15" fill="{MUTED}" stroke="{INK}" stroke-width="3"/>
<g transform="translate(430 230)">
  <path d="M-110-120h220v240h-220z" class="paper"/>
  <path d="M-80-90h160v40h-160z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-80-20h160M-80 10h120"/></g>
  <circle cx="60" cy="70" r="28" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
