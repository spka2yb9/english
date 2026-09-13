"""第104回: 句動詞45語。ファイル名は id の空白をハイフンに置き換えたもの。"""
from lib import *
W=[]
def add(slug,a,b,**k): W.append(emit(slug,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'
def phone(x,y,s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-70-20h140v40h-140z" class="ink"/>'
            f'<path d="M-90-40h40v50h-40zM50-40h40v50H50z" class="ink"/></g>')
def bus(x,y,s=1,cls='teal',facing=1):
    return (f'<g transform="translate({x} {y}) scale({s*facing} {s})">'
            f'<path d="M-140 0v-110h280V0z" class="{cls} o"/>'
            f'<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5">'
            f'<rect x="-120" y="-96" width="70" height="46"/><rect x="-40" y="-96" width="70" height="46"/>'
            f'<rect x="40" y="-96" width="70" height="46"/></g>'
            f'<g fill="{INK}"><circle cx="-80" cy="6" r="24"/><circle cx="80" cy="6" r="24"/></g></g>')

add('call-back', '電話をかけ直すイラスト。', f"""
{phone(200,240,1.2)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" marker-end="url(#ar)">
  <path d="M330 190q90-60 150 20"/>
</g>
{phone(470,300,1)}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"><path d="M120 170q-20-20 0-40M80 190q-40-40 0-80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('check-in', '窓口で手続きを済ませるイラスト。', f"""
<g transform="translate(390 300)">
  <path d="M-170-30h340v20h-340z" class="goldd o"/>
  <path d="M-140-10v46M140-10v46" class="a"/>
  <path d="M-150-90h180v60h-180z" class="paper"/>
</g>
{person(140,352,1.1,1,'teal','blue','carry','short','smile')}
<g transform="translate(230 300)"><path d="M-36-28h72v56h-72z" class="goldd o"/></g>
<g transform="translate(300 230)">
  <path d="M-44-30h88v60h-88z" class="paper"/>
  <g fill="none" stroke="{GRN}" stroke-width="7"><path d="M-20 0l10 12 22-26"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('clean-up', '散らかった部屋をきれいに片づけるイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-90-90h180v180h-180z" fill="#fffdf6" class="o"/>
  <g class="goldp o"><path d="M-60-20l40-16 12 34-40 14z"/><path d="M10 20l36 14-12 34-36-14z"/></g>
  <g class="coralp o"><circle cx="30" cy="-40" r="20"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 240h60"/></g>
<g transform="translate(460 240)">
  <path d="M-90-90h180v180h-180z" fill="#fffdf6" class="o"/>
  <path d="M-60 20h120v50h-120z" class="tealp o"/>
</g>
<g transform="translate(340 330) rotate(20)">
  <path d="M-6-90h12v90h-12z" fill="{TONES['gold'][2]}"/>
  <path d="M-30 0h60l-10 40h-40z" class="goldp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('get-up', 'ベッドから起き上がるイラスト。', f"""
<g transform="translate(180 320)">
  <path d="M-120 20h240v16h-240z" class="ink"/>
  <path d="M-120-14h240v34h-240z" fill="#fffdf6" class="o"/>
  <path d="M-120-50h50v36h-50z" class="bluep o"/>
</g>
{person(430,352,1.25,1,'teal','blue','stand','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M280 240q60-60 100-30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('go-down', '下へさがっていくイラスト。', f"""
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="22" stroke-linecap="round" marker-end="url(#ar)"><path d="M300 90v210"/></g>
<g transform="translate(140 240)">
  <path d="M-70-110h140v220h-140z" fill="#dfe6ea" class="o"/>
  <path d="M-50-30h100v100h-100z" class="tealp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('go-up', '上へあがっていくイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="22" stroke-linecap="round" marker-end="url(#ar)"><path d="M300 340V120"/></g>
<g transform="translate(140 240)">
  <path d="M-70-110h140v220h-140z" fill="#dfe6ea" class="o"/>
  <path d="M-50-100h100v100h-100z" class="tealp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('hang-up', '受話器を置いて電話を切るイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-90-20h180v90h-180z" class="ink"/>
  <path d="M-70-40h140v20h-140z" class="ink"/>
</g>
<g transform="translate(300 190)">
  <path d="M-70-16h140v32h-140z" class="ink"/>
  <path d="M-90-36h40v46h-40zM50-36h40v46H50z" class="ink"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 130v40"/></g>
{xx(470,180,1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('wake-up', '目覚まし時計で目を覚ますイラスト。', f"""
<g transform="translate(200 320)">
  <path d="M-120 20h240v16h-240z" class="ink"/>
  <path d="M-120-14h240v34h-240z" fill="#fffdf6" class="o"/>
  <path d="M-120-50h50v36h-50z" class="bluep o"/>
  <circle cx="-86" cy="-64" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <g fill="{INK}"><circle cx="-94" cy="-68" r="3"/><circle cx="-78" cy="-68" r="3"/></g>
</g>
<g transform="translate(450 250)">
  <circle r="66" fill="#fffdf6" class="o"/>
  <path d="M0 0v-42M0 0l28 16" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle r="7" class="ink"/>
  <path d="M-48-52l-22-22M48-52l22-22" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <path d="M-44-54q-22-28 6-44M44-54q22-28-6-44" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round"><path d="M360 200l-20-20M360 300l-20 20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('come-up', '底から浮かび上がってくるイラスト。', f"""
<path d="M0 160h600v240H0z" class="bluep"/>
<path d="M0 160h600" class="a"/>
<circle cx="300" cy="330" r="20" class="teal o"/>
<circle cx="300" cy="260" r="26" class="teal o"/>
<circle cx="300" cy="180" r="34" class="teal o"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M420 340V150"/></g>
""", ground=False, arrow=True)

add('look-through', 'ページをざっとめくって目を通すイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-200-130h400v240h-400z" class="paper"/>
  <path d="M0-130v240" class="a"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-170 {-90+i*36}h150M30 {-90+i*36}h150"/>' for i in range(5))}</g>
  <g class="paper" opacity="0.7"><path d="M0-130q80 20 60 120T0 110z"/></g>
</g>
<g transform="translate(160 130)">
  <ellipse rx="46" ry="28" fill="#fffdf6" class="o"/>
  <circle r="16" class="blue o"/><circle r="7" class="ink"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M200 170l60 40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('pass-on', '次の人へ手渡していくイラスト。', f"""
{person(130,352,1,1,'teal','blue','give','short','smile')}
{person(300,352,1,1,'gold','violet','give','bob','smile')}
{person(470,352,1,-1,'coral','gold','reach','short','smile')}
<g transform="translate(215 270)"><path d="M-26-20h52v40h-52z" class="goldp o"/></g>
<g class="a" marker-end="url(#ar)"><path d="M190 200h60M360 200h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('pick-out', 'たくさんの中から選び出すイラスト。', f"""
<g class="tealp o">
  {''.join(f'<circle cx="{140+c*80}" cy="{250+r*70}" r="30"/>' for r in range(2) for c in range(5))}
</g>
<circle cx="300" cy="250" r="30" class="coral o"/>
{hand(300,120,1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M300 170v40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('sell-out', '棚の品が売り切れるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" fill="#fffdf6" class="o"/>
  <path d="M-200-40h400M-200 60h400" class="a"/>
</g>
{xx(300,230,2)}
{person(520,352,0.9,-1,'coral','gold','carry','bob','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('stand-out', 'ひとつだけ抜きん出て目立つイラスト。', f"""
<g transform="translate(300 300)">
  <g class="tealp o">{''.join(f'<rect x="{-220+i*70}" y="-60" width="50" height="60"/>' for i in range(7) if i!=3)}</g>
  <path d="M-25-180h50v180h-50z" class="coral o"/>
</g>
<g class="golds"><path d="M300 90v-24M220 120l-20-20M380 120l20-20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('take-back', '買った品を店に返すイラスト。', f"""
{person(150,352,1.15,1,'teal','blue','give','short','neutral')}
<g transform="translate(300 260)"><path d="M-40-30h80v60h-80z" class="goldp o"/></g>
<g transform="translate(470 290)">
  <path d="M-100-30h200v20h-200z" class="teal o"/>
  <path d="M-100-30l-10-40h220l-10 40z" class="tealp o"/>
  <path d="M-90-10h180v70h-180z" class="goldd o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 180h150"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('carry-out', '決めた計画を実際にやり遂げるイラスト。', f"""
<g transform="translate(160 230)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-56 {-60+i*44}h112"/>' for i in range(4))}</g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 230h50"/></g>
{person(420,352,1.2,1,'teal','blue','reach','cap','neutral')}
{box(520,300,90,60,18,'gold')}
{ck(430,150,1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('cut-down', '木を切り倒すイラスト。', f"""
{tree(380,340,1.5)}
{person(160,352,1.15,1,'gold','green','reach','cap','neutral')}
<g transform="translate(250 260) rotate(40)">
  <path d="M-8-10h16v120h-16z" fill="{TONES['gold'][2]}"/>
  <path d="M-40-30q40-20 70 10-34 26-70-10z" fill="#b9c2c9" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M430 200q60 60 90 120"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('hand-over', '手から手へ引き渡すイラスト。', f"""
{hand(140,240,1)}
{hand(460,240,-1)}
<g transform="translate(300 250)">
  <path d="M-60-40h120v80h-120z" class="goldp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 150h140"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('make-out', '目をこらしてやっと見分けるイラスト。', f"""
{face(180,220,84,'flat')}
<g fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"><path d="M132 180q22-12 42 0M198 180q22-12 42 0"/></g>
<g opacity="0.35">
  <path d="M400 170h140v140H400z" class="teal o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M280 230h90"/></g>
{ck(470,120,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('pick-up', '落ちている物を拾い上げるイラスト。', f"""
{person(250,352,1.25,1,'teal','blue','reach','short','neutral')}
<g transform="translate(420 350)">
  <path d="M-36-26h72v52h-72z" class="goldp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M420 300q0-60-60-80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('pull-over', '車を道路のわきに寄せるイラスト。', f"""
<path d="M0 200h600v120H0z" fill="#dfe6ea" class="o"/>
<g fill="none" stroke="#fffdf6" stroke-width="5" stroke-dasharray="26 22"><path d="M0 260h600"/></g>
<g transform="translate(400 330)">
  <path d="M-110 0v-40l40-50h150l40 50V0z" class="teal o"/>
  <g fill="#fffdf6" class="o"><rect x="-60" y="-80" width="56" height="34"/><rect x="10" y="-80" width="56" height="34"/></g>
  <g fill="{INK}"><circle cx="-60" cy="6" r="22"/><circle cx="80" cy="6" r="22"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M120 240q120 30 200 60"/></g>
""", ground=False, arrow=True)

add('sort-out', 'ごちゃ混ぜを分けて整理するイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-90-90h180v180h-180z" fill="#fffdf6" class="o"/>
  <g class="tealp o"><circle cx="-40" cy="-40" r="20"/><circle cx="30" cy="20" r="20"/></g>
  <g class="coralp o"><rect x="-10" y="-60" width="36" height="36"/><rect x="-60" y="20" width="36" height="36"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 240h60"/></g>
<g transform="translate(460 240)">
  <path d="M-90-90h180v180h-180z" fill="#fffdf6" class="o"/>
  <path d="M-90 0h180" class="a"/>
  <g class="tealp o"><circle cx="-45" cy="-45" r="20"/><circle cx="20" cy="-45" r="20"/></g>
  <g class="coralp o"><rect x="-64" y="26" width="36" height="36"/><rect x="10" y="26" width="36" height="36"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('speak-up', '声を大きくしてはっきり言うイラスト。', f"""
{person(180,352,1.3,1,'coral','blue','point','short','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M290 200q26 30 0 60M340 170q56 60 0 120M390 140q86 90 0 180"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('check-out', '精算して宿を出るイラスト。', f"""
<g transform="translate(200 300)">
  <path d="M-140-30h280v20h-280z" class="goldd o"/>
  <path d="M-110-10v46M110-10v46" class="a"/>
  <path d="M-60-80h120v50h-120z" class="paper"/>
</g>
<g transform="translate(200 250)">
  <circle r="20" fill="none" stroke="{TONES['gold'][2]}" stroke-width="8"/>
  <path d="M18 0h50v10h-12v12h-10v-12h-10v12h-10v-12h-8z" fill="{TONES['gold'][2]}"/>
</g>
{person(430,352,1.15,1,'teal','blue','carry','short','smile')}
<g class="a" marker-end="url(#ar)"><path d="M330 200h150"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('come-back', 'いったん出た人が戻ってくるイラスト。', f"""
<g transform="translate(160 260)">
  <path d="M-90 90v-140h180v140z" fill="#fffdf6" class="o"/>
  <path d="M-104-50L0-110l104 60z" class="teal o"/>
  <path d="M-30 90V20h60v70z" class="teald o"/>
</g>
{person(430,352,1.2,-1,'coral','blue','walk','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M470 180q-40-60-190-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('come-out', '中から外へ出てくるイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-130-150h260v300h-260z" fill="#dfe6ea" class="o"/>
  <path d="M-70-110h190v260H-70z" fill="#fffaf1" class="o"/>
  <circle cx="100" cy="20" r="8" class="ink"/>
</g>
{person(420,352,1.2,1,'teal','blue','walk','short','smile')}
<g class="a" marker-end="url(#ar)"><path d="M320 250h100"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('eat-out', '店で食事をするイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-160-30h320v20h-320z" class="goldd o"/>
  <path d="M-130-10v46M130-10v46" class="a"/>
  <ellipse cx="0" cy="-44" rx="60" ry="18" fill="#fffdf6" class="o"/>
  <path d="M-100-60v40M-108-60v20h16v-20M100-60v40" fill="none" stroke="{MUTED}" stroke-width="5"/>
</g>
{sit(160,352,1,1,'teal','blue','short','smile','lap')}
{sit(440,352,1,-1,'coral','gold','bob','smile','lap')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('get-back', '貸したものを取り戻すイラスト。', f"""
{person(150,352,1.2,1,'teal','blue','reach','short','smile')}
{person(470,352,1.15,-1,'coral','gold','give','bob','neutral')}
<g transform="translate(310 260)"><path d="M-40-30h80v60h-80z" class="goldp o"/></g>
<g class="a" marker-end="url(#ar)"><path d="M390 180H240"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('get-off', 'バスから降りるイラスト。', f"""
{bus(220,340,0.9,'teal',1)}
{person(460,352,1.15,1,'coral','blue','walk','short','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M340 250h80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('get-on', 'バスに乗り込むイラスト。', f"""
{bus(400,340,0.9,'teal',-1)}
{person(150,352,1.15,1,'coral','blue','walk','short','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M210 250h80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('get-out', '車から外へ出るイラスト。', f"""
<g transform="translate(210 320)">
  <path d="M-130 0v-40l40-50h150l40 50V0z" class="teal o"/>
  <g fill="#fffdf6" class="o"><rect x="-70" y="-80" width="56" height="34"/><rect x="0" y="-80" width="56" height="34"/></g>
  <g fill="{INK}"><circle cx="-70" cy="6" r="22"/><circle cx="70" cy="6" r="22"/></g>
</g>
{person(470,352,1.15,1,'coral','blue','walk','short','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M360 250h70"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('break-down', '車が動かなくなるイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-130 0v-40l40-50h150l40 50V0z" class="teal o"/>
  <g fill="#fffdf6" class="o"><rect x="-70" y="-80" width="56" height="34"/><rect x="0" y="-80" width="56" height="34"/></g>
  <g fill="{INK}"><circle cx="-70" cy="6" r="22"/><circle cx="70" cy="6" r="22"/></g>
</g>
{cloud(300,150,1.1,'blue')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round"><path d="M160 200l-20-24M440 200l20-24"/></g>
{xx(490,300,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('break-out', 'ふいに火が起こるイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-160 60v-120h320V60z" fill="#fffdf6" class="o"/>
  <path d="M-180-60L0-150l180 90z" class="teal o"/>
</g>
{flame(300,290,1.1)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M180 150l-20-24M420 150l20-24M300 110V80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('break-up', 'まとまりが分かれて散るイラスト。', f"""
{person(160,352,1.1,-1,'teal','blue','walk','short','sad')}
{person(440,352,1.1,1,'coral','gold','walk','bob','sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linejoin="round"><path d="M300 150l24 40-24 40 24 40"/></g>
<g class="a" marker-end="url(#ar)"><path d="M230 320H130M370 320h100"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('bring-up', '子どもを育てるイラスト。', f"""
{person(200,352,1.3,1,'violet','violet','give','bun','smile')}
{person(360,354,0.65,-1,'gold','coral','up','short','smile')}
{person(470,354,0.85,-1,'teal','blue','stand','bob','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M380 250q60-30 80 0"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('build-up', '少しずつ積み上げて大きくするイラスト。', f"""
<g transform="translate(300 340)">
  <g class="tealp o"><rect x="-230" y="-50" width="60" height="50"/></g>
  <g class="tealp o"><rect x="-140" y="-100" width="60" height="100"/></g>
  <g class="tealp o"><rect x="-50" y="-160" width="60" height="160"/></g>
  <g class="teal o"><rect x="40" y="-230" width="60" height="230"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M90 300q140-140 300-190"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('calm-down', '荒れた気持ちが静まるイラスト。', f"""
{person(160,352,1.15,1,'coral','blue','up','short','sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round"><path d="M110 190l-16-22M210 180v-24"/></g>
<g class="a" marker-end="url(#ar)"><path d="M290 250h60"/></g>
{person(460,352,1.15,1,'teal','blue','stand','short','smile')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><path d="M400 200q30-16 60 0t60 0"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('carry-on', '止まらずそのまま続けるイラスト。', f"""
{person(180,352,1.2,1,'teal','blue','walk','short','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="16 12" marker-end="url(#ar)"><path d="M260 320h280"/></g>
<g opacity="0.35">{person(120,352,1.2,1,'teal','blue','walk','short','neutral')}</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('catch-up', '遅れを取り戻して追いつくイラスト。', f"""
{person(400,352,1.15,1,'coral','blue','walk','short','neutral')}
{person(230,352,1.15,1,'teal','blue','walk','short','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M290 240h60"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"><path d="M170 300h-40M180 330h-50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('cheer-up', '元気のない人を励ますイラスト。', f"""
{person(160,352,1.15,1,'teal','blue','give','short','smile')}
{person(440,352,1.15,-1,'coral','gold','reach','bob','smile')}
<g transform="translate(300 270)">
  <path d="M-40-30h80v60h-80z" class="coral o"/>
  <path d="M0-30q-26-26-36-6 18 10 36 6zM0-30q26-26 36-6-18 10-36 6z" class="coralp o"/>
</g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2">
  <path d="M440 170l10 22 24 3-17 17 4 24-21-12-21 12 4-24-17-17 24-3z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('come-along', 'いっしょについて来るイラスト。', f"""
{person(220,352,1.2,1,'teal','blue','walk','short','smile')}
{person(340,354,1.1,1,'coral','gold','walk','bob','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M420 320h120"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M280 230h30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('come-across', '思いがけず出くわすイラスト。', f"""
{person(200,352,1.2,1,'teal','blue','walk','short','surprised')}
<g transform="translate(430 300)">
  <path d="M-60-40h120v80h-120z" class="goldp o"/>
</g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2.5">
  <path d="M430 170h26l-6 70h-14zM443 262a13 13 0 1 0 0 26 13 13 0 1 0 0-26z"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M270 330h90"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('count-on', '頼れる人に寄りかかるイラスト。', f"""
{person(360,352,1.3,1,'violet','violet','stand','bun','smile')}
{person(250,352,1.15,-1,'teal','blue','reach','short','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M180 220h100"/></g>
{ck(490,200,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('cut-off', '線をはさみで断ち切るイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="18" stroke-linecap="round"><path d="M60 250h180M360 250h180"/></g>
<g transform="translate(300 250) rotate(-16)">
  <path d="M-60-40L40-6" fill="none" stroke="#b9c2c9" stroke-width="9" stroke-linecap="round"/>
  <path d="M-60 40L40 6" fill="none" stroke="#b9c2c9" stroke-width="9" stroke-linecap="round"/>
  <circle cx="-74" cy="-48" r="18" fill="none" stroke="{TONES['blue'][0]}" stroke-width="8"/>
  <circle cx="-74" cy="48" r="18" fill="none" stroke="{TONES['blue'][0]}" stroke-width="8"/>
</g>
{xx(300,140,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('drop-off', '荷物を届けて置いていくイラスト。', f"""
{person(180,352,1.2,1,'teal','blue','reach','short','smile')}
<g transform="translate(400 340)">
  <path d="M-50-40h100v80h-100z" class="goldd o"/>
</g>
<g transform="translate(470 250)">
  <path d="M-60 60v-70h120v70z" fill="#fffdf6" class="o"/>
  <path d="M-72-10L0-56l72 46z" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M260 250q70-30 110 40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

print(len(W), ' '.join(W))
print(sheet(W))
