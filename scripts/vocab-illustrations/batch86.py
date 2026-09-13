"""第86回: l〜m の名詞を中心に45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'
def gear(x,y,r=60,cls='teal',teeth=8):
    import math
    t=''.join(f'<rect x="-12" y="{-r-22}" width="24" height="26" transform="rotate({i*360//teeth})"/>' for i in range(teeth))
    return (f'<g transform="translate({x} {y})"><g class="{cls} o">{t}</g>'
            f'<circle r="{r}" class="{cls} o"/><circle r="{r*0.35:.0f}" fill="#fffdf6" stroke="{INK}" stroke-width="3"/></g>')
def note(x,y,s=1,cls='ink'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 30q-14 0-14-12t14-12q8 0 12 5v-45l30-9v14l-20 6v40q0 13-22 13z" '
            f'fill="{INK if cls=="ink" else TONES[cls][0]}"/></g>')

add('loyalty', '旗の前で胸に手を当て変わらぬ忠誠を示すイラスト。', f"""
{person(240,352,1.3,1,'teal','blue','hold','short','neutral')}
<g transform="translate(470 250)">
  <path d="M-6 130V-110" class="a"/>
  <path d="M-6-110h110v74H-6z" class="coral o"/>
</g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M258 250q-22-28 0-40 22-12 22 16 0-28 22-16 22 12 0 40l-22 22z"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('lung', '息を吸い込む二つの肺のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-120 150v-110q0-90 120-90t120 90v110z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-10-90h20v60h-20z" fill="{MUTED}" class="o"/>
  <path d="M-10-40q-30 0-46 30-18 34-10 80 6 30 34 30 26 0 26-30v-110z" class="coralp o"/>
  <path d="M10-40q30 0 46 30 18 34 10 80-6 30-34 30-26 0-26-30v-110z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"><path d="M-24-20v90M24-20v90"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 60v44"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('lyric', '曲にのせて歌われる歌詞のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-140h380v280h-380z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-150 {-40+i*44}h300"/>' for i in range(4))}</g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4">{''.join(f'<path d="M-150 {-20+i*44}h230"/>' for i in range(4))}</g>
</g>
{note(180,120,1.1,'coral')}
{note(300,90,1.1,'coral')}
{note(400,120,1.1,'coral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('machinery', '歯車の組み合わさった機械のイラスト。', f"""
{gear(210,220,70,'teal',9)}
{gear(370,170,50,'gold',8)}
{gear(400,300,42,'coral',7)}
<path d="M40 350h520v40H40z" fill="#dfe6ea" class="o"/>
""", ground=False)

add('magnitude', '小さいものと巨大なものの大きさの差のイラスト。', f"""
<circle cx="120" cy="300" r="26" class="tealp o"/>
<circle cx="400" cy="220" r="150" class="teal o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M560 370v-300"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M520 370h80M520 70h80"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('mainly', '大部分がひとつで占められているイラスト。', f"""
<g transform="translate(280 210)">
  <circle r="150" class="tealp o"/>
  <path d="M0 0v-150A150 150 0 1 1-106 106z" class="teal o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M540 150l-90 40"/></g>
""", ground=False, arrow=True)

add('mainstream', '大きな流れの本流とわきにそれた少数のイラスト。', f"""
<path d="M0 120h600v200H0z" class="bluep"/>
<path d="M0 120h600M0 320h600" class="a"/>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4">
  <path d="M40 170q60-20 120 0t120 0 120 0 120 0"/>
  <path d="M40 270q60-20 120 0t120 0 120 0 120 0"/>
</g>
<g class="teal o">{''.join(f'<path d="M{110+i*110} 210h70l-14 30h-42z"/>' for i in range(4))}</g>
<g class="coral o"><path d="M480 350h70l-14 30h-42z"/></g>
<g class="a" marker-end="url(#ar)"><path d="M60 210h40"/></g>
""", ground=False, arrow=True)

add('maintenance', '油をさして機械を保つ整備のイラスト。', f"""
{gear(400,220,80,'teal',9)}
{person(150,352,1.15,1,'violet','blue','reach','cap','neutral')}
<g transform="translate(250 200)">
  <path d="M-30 30h60v20h-60z" fill="{MUTED}" class="o"/>
  <path d="M-10-20h20v50h-20z" fill="{MUTED}" class="o"/>
  <path d="M10-10l50-30" fill="none" stroke="{MUTED}" stroke-width="7"/>
</g>
{drop(300,150,1.3,'gold')}
{ck(490,120,1)}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('majority', '半分を越える多数のイラスト。', f"""
{person(110,330,0.75,1,'teal','blue','up','short','smile')}
{person(190,330,0.75,1,'teal','blue','up','bob','smile')}
{person(270,330,0.75,1,'teal','blue','up','short','smile')}
{person(350,330,0.75,1,'teal','blue','up','bun','smile')}
{person(470,330,0.75,-1,'coral','gold','stand','short','neutral')}
{person(540,330,0.75,-1,'coral','gold','stand','bob','neutral')}
<g transform="translate(300 380)">
  <path d="M-250-12h420v24h-420z" class="teal o"/>
  <path d="M170-12h80v24h-80z" class="coralp o"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="10 8"><path d="M300 140v250"/></g>
<path d="M60 396h480" class="a"/>
""", ground=True)

add('making', '手を動かして物を作り上げるイラスト。', f"""
{hand(130,230,1)}
{hand(470,230,-1)}
<g transform="translate(300 250)">
  <path d="M-60-60h120v120h-120z" class="teal o"/>
  <path d="M-60-60h120v120h-120zM-60 0h120M0-60v120" class="a"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)">
  <path d="M200 230h30M400 230h-30"/>
</g>
<g class="golds"><path d="M300 140v-30M200 150l-16-20M400 150l16-20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('management', '全体を見て人と仕事を回す経営のイラスト。', f"""
{person(140,352,1.2,1,'violet','blue','point','bun','neutral')}
<g transform="translate(400 210)">
  <path d="M-170-130h340v260h-340z" fill="#fffdf6" class="o"/>
  <path d="M-130-90h90v60h-90zM-45-90h90v60h-90zM40-90h90v60H40z" class="tealp o"/>
  <path d="M-130 20h90v60h-90zM-45 20h90v60h-90zM40 20h90v60H40z" class="goldp o"/>
  <g class="a" marker-end="url(#ar)"><path d="M-85-24v36M0-24v36M85-24v36"/></g>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('manipulation', '糸で操られる人形のイラスト。', f"""
{hand(300,90,1)}
<g fill="none" stroke="{MUTED}" stroke-width="2.5">
  <path d="M270 130l-40 110M300 130v100M336 130l40 110"/>
</g>
<g transform="translate(300 290)">
  <circle cy="-80" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-34-46h68v70h-68z" class="teal o"/>
  <path d="M-34-40l-40 30M34-40l40 30" fill="none" stroke="{SKIN}" stroke-width="9" stroke-linecap="round"/>
  <path d="M-20 24l-16 60M20 24l16 60" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('manuscript', '手書きで書きためた原稿のイラスト。', f"""
<g transform="translate(260 220)">
  <path d="M-130-140h260v280h-260z" class="paper" transform="rotate(-5)"/>
  <path d="M-130-140h260v280h-260z" class="paper" transform="rotate(3) translate(14 10)"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4" transform="rotate(3) translate(14 10)">
    {''.join(f'<path d="M-96 {-96+i*40}h190"/>' for i in range(6))}
  </g>
</g>
<g transform="translate(470 240)">
  <path d="M-14-130h28l10 130-24 40-24-40z" class="gold o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('marathon', '長い道を走り続けるマラソンのイラスト。', f"""
<path d="M0 320h600v40H0z" fill="#dfe6ea" class="o"/>
{person(140,320,1,1,'coral','blue','walk','short','neutral')}
{person(250,320,1,1,'teal','gold','walk','bob','neutral')}
{person(350,320,1,1,'gold','violet','walk','short','neutral')}
<g transform="translate(500 250)">
  <path d="M-6 70V-60" class="a"/>
  <path d="M-6-60h90v50H-6z" class="teal o"/>
  <g fill="#fffdf6"><rect x="16" y="-46" width="40" height="10" rx="5"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="16 14"><path d="M60 300h420"/></g>
""", ground=False)

add('margin', 'ページのまわりに取られた余白のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-210-160h420v320h-420z" class="paper"/>
  <path d="M-210-160h420v320h-420zM-140-100h280v200h-280z" fill="{TONES['coral'][1]}" fill-rule="evenodd" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-120 {-70+i*40}h240"/>' for i in range(5))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M120 40h-30M120 40h30"/></g>
""", ground=False, arrow=True)

add('marker', '場所を示すために立てた目印のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-10 90V-90" class="a"/>
  <path d="M-10-90h100l-24 30 24 30H-10z" class="coral o"/>
  <ellipse cy="92" rx="60" ry="18" class="tealp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"><path d="M120 340q80-40 170-46M480 340q-80-40-170-46"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('marketplace', '店が並んで売り買いする市場のイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-110-40h220v20h-220z" class="coral o"/>
  <path d="M-110-40l-10-40h240l-10 40z" class="coralp o"/>
  <path d="M-100-20h200v70h-200z" class="goldd o"/>
  <g class="gold o"><circle cx="-60" cy="-36" r="14"/><circle cx="-20" cy="-36" r="14"/><circle cx="20" cy="-36" r="14"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-100-40h200v20h-200z" class="teal o"/>
  <path d="M-100-40l-10-40h220l-10 40z" class="tealp o"/>
  <path d="M-90-20h180v70h-180z" class="goldd o"/>
  <g class="greenp o"><circle cx="-40" cy="-36" r="14"/><circle cx="0" cy="-36" r="14"/><circle cx="40" cy="-36" r="14"/></g>
</g>
{person(300,360,0.85,1,'violet','blue','carry','bob','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('mask', '顔を覆い隠す仮面のイラスト。', f"""
{face(220,220,86,'flat')}
<g transform="translate(300 220)">
  <path d="M-70-60q70-40 140 0 0 100-70 100T-70-60z" class="goldp o"/>
  <g fill="{INK}"><path d="M-40-30q20-14 40 0-20 14-40 0zM20-30q20-14 40 0-20 14-40 0z"/></g>
  <path d="M0 30q20 14 40 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('mass', '同じものが山のように大量にあるイラスト。', f"""
<g class="tealp o">
  {''.join(f'<circle cx="{160+((i*53)%280)}" cy="{330-(i//6)*44}" r="26"/>' for i in range(30))}
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10"><path d="M110 360q190-230 380 0"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('maximum', 'これ以上は上がらない上限のイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-200-160h400v20h-400z" class="coral o"/>
  <g class="teal o">{''.join(f'<rect x="{-170+i*70}" y="{-40-i*25}" width="50" height="{80+i*25}"/>' for i in range(5))}</g>
  <path d="M-200 110h400" class="a"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M540 240v-130"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('mayor', '市庁舎の前に立つ市長のイラスト。', f"""
{person(200,352,1.3,1,'violet','blue','stand','short','smile')}
<g transform="translate(200 300)">
  <path d="M-30-70L30 30" fill="none" stroke="{TONES['gold'][0]}" stroke-width="14"/>
  <circle cx="30" cy="34" r="16" class="goldd o"/>
</g>
{building(450,330,0.9,'teal')}
<path d="M60 376h480" class="a"/>
""", ground=True)

add('meantime', 'ふたつの出来事のあいだの時間のイラスト。', f"""
<g transform="translate(300 200)">
  <circle cx="-200" cy="0" r="44" class="teal o"/>
  <circle cx="200" cy="0" r="44" class="teal o"/>
  <path d="M-200 0h400" class="a"/>
  <path d="M-140 70h280v40h-280z" class="goldp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M300 200h-90M300 200h90"/></g>
{person(300,380,0.7,1,'coral','blue','think','short','neutral')}
""", ground=False, arrow=True)

add('meanwhile', '同じ時刻に別の場所で起きていることのイラスト。', f"""
<g transform="translate(160 230)">
  <path d="M-120-110h240v220h-240z" fill="#fffdf6" class="o"/>
</g>
{person(160,300,0.85,1,'teal','blue','walk','short','smile')}
<g transform="translate(440 230)">
  <path d="M-120-110h240v220h-240z" fill="#fffdf6" class="o"/>
</g>
{person(440,300,0.85,-1,'coral','gold','stand','bob','smile')}
<g transform="translate(300 90)">
  <circle r="56" fill="#fffdf6" class="o"/>
  <path d="M0 0v-38M0 0l26 16" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <circle r="6" class="ink"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M250 110H180M350 110h70"/></g>
""", ground=False)

add('measure', 'ものさしで長さを量るイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-160-90h320v90h-320z" class="tealp o"/>
</g>
<g transform="translate(300 190)">
  <path d="M-200-40h400v60h-400z" class="goldp o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">
    {''.join(f'<path d="M{-180+i*40} -40v{26 if i%2==0 else 16}"/>' for i in range(10))}
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M300 130h-160M300 130h160"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('mechanic', '車を直す整備士のイラスト。', f"""
<g transform="translate(400 280)">
  <path d="M-130 0v-30l30-44h170l40 44V0z" class="teal o"/>
  <g fill="#fffdf6" class="o"><rect x="-80" y="-66" width="60" height="34"/><rect x="0" y="-66" width="60" height="34"/></g>
  <g fill="{INK}"><circle cx="-80" cy="6" r="22"/><circle cx="80" cy="6" r="22"/></g>
  <path d="M-130-30h-40v30h40z" class="tealp o"/>
</g>
{person(170,352,1.15,1,'violet','violet','reach','cap','neutral')}
<g transform="translate(250 230) rotate(30)">
  <path d="M-8-50h16v90h-16z" fill="{MUTED}" class="o"/>
  <path d="M-18-60h36v20h-36z" fill="{MUTED}" class="o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('mechanism', '内側の仕掛けが見える仕組みのイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" fill="#fffdf6" class="o"/>
  <path d="M-200-140h400v40h-400z" class="ink"/>
</g>
{gear(230,210,56,'teal',8)}
{gear(340,270,40,'gold',7)}
<g fill="none" stroke="{MUTED}" stroke-width="8" stroke-linecap="round"><path d="M400 240l70-50M470 190v-40"/></g>
<circle cx="470" cy="140" r="16" class="coral o"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('medal', '胸にさげられたメダルのイラスト。', f"""
{person(300,352,1.35,1,'teal','blue','stand','short','smile')}
<g transform="translate(300 250)">
  <path d="M-40-60l30 56h-30zM40-60l-30 56h30z" class="coral o"/>
  <circle cy="30" r="44" class="gold o"/>
  <circle cy="30" r="30" class="goldp o"/>
  <path d="M0 4l10 20 22 3-16 15 4 22-20-11-20 11 4-22-16-15 22-3z" class="goldd"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('medication', 'びんに入った薬とカプセルのイラスト。', f"""
<g transform="translate(220 270)">
  <path d="M-70 80v-120q0-20 20-24v-26h100v26q20 4 20 24v120z" fill="#fffdf6" class="o"/>
  <path d="M-70 80V0h140v80z" class="coralp o"/>
  <path d="M-40-90h80v20h-80z" class="corald o"/>
  <path d="M-40-40h80v40h-80z" class="paper"/>
</g>
<g transform="translate(420 300)">
  <path d="M-60-20h60v40h-60q-20 0-20-20t20-20z" class="coral o"/>
  <path d="M0-20h40q20 0 20 20t-20 20H0z" fill="#fffdf6" class="o"/>
</g>
<g class="goldp o"><circle cx="400" cy="220" r="22"/><circle cx="460" cy="240" r="22"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('meditation', '足を組んで静かに心を整える瞑想のイラスト。', f"""
<g transform="translate(300 330)">
  <path d="M-90 0q0-30 90-30t90 30z" class="bluep o"/>
  <path d="M-60-30q20-40 60-40t60 40z" class="teal o"/>
  <circle cy="-96" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-31-99q4-34 31-34 30 0 34 31-16-12-33-5-15-13-32 8z" fill="{HAIR}" stroke="{HAIR}" stroke-width="2"/>
  <g fill="none" stroke="{INK}" stroke-width="2.5"><path d="M-16-96q8 6 16 0M0-96q8 6 16 0"/></g>
  <path d="M-60-40l-30 34M60-40l30 34" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3" opacity="0.7">
  <circle cx="300" cy="230" r="140"/><circle cx="300" cy="230" r="180"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('melody', '上がり下がりしながら流れる旋律のイラスト。', f"""
<g transform="translate(300 230)">
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-240 {-60+i*30}h480"/>' for i in range(5))}</g>
</g>
{note(120,230,1,'teal')}
{note(200,200,1,'teal')}
{note(280,170,1,'teal')}
{note(360,200,1,'teal')}
{note(440,240,1,'teal')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8">
  <path d="M126 218q80-60 160-60t160 70"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('membership', '会員証を持つ仲間の一員のイラスト。', f"""
<g transform="translate(200 200)">
  <path d="M-130-90h260v180h-260z" class="paper"/>
  <path d="M-130-90h260v34h-260z" class="teal o"/>
  <g transform="translate(-70 20)">
    <circle cy="-24" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <path d="M-36 46v-12q0-24 36-24t36 24v12z" class="blue o"/>
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M10-20h100M10 10h100M10 40h70"/></g>
</g>
{person(400,356,0.8,1,'teal','blue','stand','short','smile')}
{person(470,356,0.8,1,'gold','violet','stand','bob','smile')}
{person(540,356,0.8,-1,'green','blue','stand','bun','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('memo', '要点を書きとめた小さなメモのイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-140-130h280v240l-40 40h-240z" class="goldp o"/>
  <path d="M100 110h40l-40 40z" class="gold o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-100 {-80+i*46}h200"/>' for i in range(4))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('memoir', '自分の来し方を書きつづる回想録のイラスト。', f"""
{sit(190,340,1.25,1,'violet','violet','bun','smile','lap')}
<g transform="translate(190 340)">
  <path d="M-90-20h40v20h-40z" class="goldd o"/>
  <path d="M-90-20v-130h30v130z" class="gold o"/>
</g>
<g transform="translate(250 292)">
  <path d="M-46-14h92v30h-92z" class="paper"/>
</g>
<g transform="translate(440 200)">
  <path d="M-90-100h180v80h-180z" class="paper"/>
  <path d="M-70-80h60v40h-60z" class="tealp o"/>
  <path d="M-90 10h180v80h-180z" class="paper"/>
  <path d="M-70 30h60v40h-60z" class="goldp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M300 200h40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('memorial', '花を供えて故人をしのぶ記念碑のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-100 80h200v30h-200z" class="teald o"/>
  <path d="M-60-140h120v220h-120z" fill="#dfe6ea" class="o"/>
  <g fill="{MUTED}"><rect x="-30" y="-100" width="60" height="12"/><rect x="-30" y="-70" width="60" height="12"/><rect x="-30" y="-40" width="44" height="12"/></g>
</g>
<g class="coral o"><circle cx="190" cy="350" r="16"/><circle cx="410" cy="350" r="16"/></g>
<g class="greens"><path d="M190 366v24M410 366v24"/></g>
<path d="M60 390h480" class="a"/>
""", ground=True)

add('mentor', '経験ある人が並んで教え導くイラスト。', f"""
{person(200,352,1.3,1,'violet','violet','point','bun','smile')}
{person(400,354,1,1,'teal','blue','stand','short','smile')}
<g transform="translate(400 250)">
  <path d="M-56-40h112v70h-112z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-34-20h68M-34 0h68M-34 20h44"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M280 250h50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('merchant', '品物を売って商いをする商人のイラスト。', f"""
<g transform="translate(340 280)">
  <path d="M-150-30h300v20h-300z" class="coral o"/>
  <path d="M-150-30l-14-40h328l-14 40z" class="coralp o"/>
  <path d="M-140-10h280v80h-280z" class="goldd o"/>
</g>
{person(340,250,1,-1,'gold','blue','give','short','smile')}
<g transform="translate(220 250)">
  <path d="M-40-20h80v40h-80z" class="greenp o"/>
  <circle r="12" class="gold o"/>
</g>
{person(140,352,0.9,1,'teal','blue','give','bob','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('mercy', '振り上げた手をおろして許す慈悲のイラスト。', f"""
{person(180,352,1.2,1,'teal','blue','reach','short','neutral')}
{person(440,352,1.1,-1,'coral','gold','think','bob','sad')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M250 190v60"/></g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M320 160q-22-28 0-40 22-12 22 16 0-28 22-16 22 12 0 40l-22 22z"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('merger', '二つの会社がひとつになる合併のイラスト。', f"""
{tower(150,300,0.6,'teal',4)}
{tower(300,300,0.6,'coral',4)}
<g class="a" marker-end="url(#ar)"><path d="M200 160h40M340 160h40"/></g>
{tower(480,300,0.85,'violet',5)}
<path d="M60 330h480" class="a"/>
""", ground=True, arrow=True)

add('merit', 'よい点として数え上げられる長所のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-190-150h380v300h-380z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-80 {-90+i*60}h230"/>' for i in range(4))}</g>
  <g fill="none" stroke="{GRN}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round">
    {''.join(f'<path d="M-150 {-96+i*60}l14 16 26-32"/>' for i in range(4))}
  </g>
</g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2">
  <path d="M540 90l10 22 24 3-17 17 4 24-21-12-21 12 4-24-17-17 24-3z"/>
</g>
""", ground=False)

add('metaphor', '別のものにたとえて言い表す隠喩のイラスト。', f"""
<g transform="translate(160 220)">
  <path d="M-90-70h180v140h-180z" class="paper"/>
  <path d="M-50 40q0-70 50-70t50 70z" class="coral o"/>
  <path d="M0-30q-20-30 0-40 20 10 0 40z" class="coralp o"/>
</g>
<g transform="translate(440 220)">
  <path d="M-90-70h180v140h-180z" class="paper"/>
  <ellipse cy="10" rx="70" ry="36" class="gold o"/>
  <circle cx="46" cy="-24" r="26" class="gold o"/>
  <path d="M66-30l26 10-26 10z" class="corald o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"><path d="M-40-14q20-20 40 0"/></g>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="7"><path d="M262 200h76M262 240h76"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('methodology', '決まった手順と道具で進める方法のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-230-40h120v120h-120z" class="tealp o"/>
  <path d="M-60-40h120v120H-60z" class="tealp o"/>
  <path d="M110-40h120v120H110z" class="tealp o"/>
</g>
<g transform="translate(170 250)"><circle r="26" fill="none" stroke="{INK}" stroke-width="7"/><path d="M18 18l24 24" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/></g>
<g transform="translate(300 250)"><path d="M-8-30h16v60h-16z" fill="{MUTED}" class="o"/><path d="M-20-40h40v16h-40z" fill="{MUTED}" class="o"/></g>
<g transform="translate(470 250)"><path d="M-30-26h60v56h-60z" class="paper"/><g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-16-10h32M-16 4h32"/></g></g>
<g class="a" marker-end="url(#ar)"><path d="M240 150h50M410 150h50"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('midst', '取り囲まれた真ん中にいるイラスト。', f"""
{person(120,330,0.75,1,'teal','blue','stand','short','neutral')}
{person(200,330,0.75,1,'gold','violet','stand','bob','neutral')}
{person(400,330,0.75,-1,'green','blue','stand','short','neutral')}
{person(480,330,0.75,-1,'violet','gold','stand','bun','neutral')}
{person(300,346,1.05,1,'coral','blue','stand','cap','surprised')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10"><circle cx="300" cy="240" r="90"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('migration', '群れが遠くへ渡っていく移住のイラスト。', f"""
<g fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round">
  <path d="M120 140q20-20 40 0M120 140q-20-20-40 0"/>
  <path d="M240 100q20-20 40 0M240 100q-20-20-40 0"/>
  <path d="M360 140q20-20 40 0M360 140q-20-20-40 0"/>
  <path d="M180 190q20-20 40 0M180 190q-20-20-40 0"/>
  <path d="M300 190q20-20 40 0M300 190q-20-20-40 0"/>
</g>
<path d="M0 280q150-40 300 0t300 0v120H0z" class="greenp o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M80 250q200 90 460-80"/></g>
""", ground=False, arrow=True)

add('military', '隊列を組んだ軍のイラスト。', f"""
{person(140,352,1,1,'green','green','stand','cap','neutral')}
{person(240,352,1,1,'green','green','stand','cap','neutral')}
{person(340,352,1,1,'green','green','stand','cap','neutral')}
{person(440,352,1,1,'green','green','stand','cap','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><path d="M100 380h400"/></g>
<g transform="translate(520 250)">
  <path d="M-6 130V-60" class="a"/>
  <path d="M-6-60h80v50H-6z" class="green o"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('mill', '穀物をひく水車小屋のイラスト。', f"""
<g transform="translate(360 280)">
  <path d="M-110 60v-140h220V60z" fill="#fffdf6" class="o"/>
  <path d="M-124-80L0-150l124 70z" class="coral o"/>
  <path d="M-30 0h60v60h-60z" class="corald o"/>
</g>
<g transform="translate(160 270)">
  <circle r="90" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="8">
    {''.join(f'<path d="M0 0l{int(90*__import__("math").cos(__import__("math").radians(a)))} {int(90*__import__("math").sin(__import__("math").radians(a)))}"/>' for a in range(0,360,45))}
  </g>
</g>
<path d="M0 340h600v60H0z" class="bluep"/>
<path d="M0 340h600" class="a"/>
""", ground=False)

print(len(W), ' '.join(W))
print(sheet(W))
