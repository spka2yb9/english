"""第90回: pr〜re の名詞を中心に45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'
def star(x,y,r=30,cls='gold'):
    import math
    pts=[]
    for i in range(10):
        rr = r if i%2==0 else r*0.45
        a = math.radians(-90+i*36)
        pts.append(f'{x+rr*math.cos(a):.0f} {y+rr*math.sin(a):.0f}')
    return f'<path d="M{"L".join(pts)}z" class="{cls} o"/>'

add('project', 'みんなで進める計画のイラスト。', f"""
<g transform="translate(340 200)">
  <path d="M-200-150h400v240h-400z" class="paper"/>
  <g class="teal o"><rect x="-170" y="-120" width="120" height="30"/><rect x="-170" y="-70" width="200" height="30"/><rect x="-170" y="-20" width="290" height="30"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 8"><path d="M-50-130v210M30-130v210M120-130v210"/></g>
</g>
{person(140,356,0.85,1,'coral','blue','up','short','smile')}
{person(230,356,0.85,1,'gold','violet','up','bob','smile')}
{person(320,356,0.85,1,'green','blue','up','short','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('proposition', '真か偽かを問う言い分のイラスト。', f"""
<g transform="translate(300 180)">
  <path d="M-210-100h420v200h-420z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="6"><path d="M-170-50h340M-170 0h340M-170 50h240"/></g>
</g>
{ck(200,330,1.1)}
{xx(400,330,1.1)}
""", ground=False)

add('prosecution', '法廷で罪を問い立てる起訴のイラスト。', f"""
<g transform="translate(300 150)">
  <path d="M-140 60h280v40h-280z" class="teald o"/>
  <path d="M-110-40h220v100h-220z" fill="#fffdf6" class="o"/>
  <path d="M-124-40L0-100l124 60z" class="teal o"/>
</g>
{person(140,356,1.05,1,'violet','blue','point','short','neutral')}
{person(460,356,1.05,-1,'coral','gold','stand','bob','sad')}
<g class="a" marker-end="url(#ar)"><path d="M240 280h140"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('prosecutor', '書類を手に罪を追及する検察官のイラスト。', f"""
{person(240,352,1.4,1,'violet','blue','carry','short','neutral')}
<g transform="translate(370 270)">
  <path d="M-44-60h88v120h-88z" class="paper"/>
  <path d="M-44-60h88v22h-88z" class="ink"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-26-16h52M-26 8h52M-26 32h34"/></g>
</g>
<g transform="translate(180 250)">
  <circle r="28" class="gold o"/>
  <path d="M0-16l6 12 14 2-10 10 2 14-12-7-12 7 2-14-10-10 14-2z" class="goldd"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('prosperity', '町がにぎわい実りが増える繁栄のイラスト。', f"""
{tower(130,330,0.6,'teal',4)}
{tower(260,330,0.75,'teal',5)}
{tower(400,330,0.6,'teal',4)}
<g transform="translate(510 290)">
  <path d="M-60 60h120v20h-120z" class="goldd o"/>
  <path d="M-50-10h100v70h-100z" class="gold o"/>
  <g class="gold o"><ellipse cx="0" cy="-26" rx="34" ry="14"/><ellipse cx="0" cy="-44" rx="34" ry="14"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M100 250q160-120 400-160"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('protein', '体をつくるもとになる蛋白質のイラスト。', f"""
<g transform="translate(190 260)">
  <ellipse rx="80" ry="50" class="corald o"/>
  <ellipse rx="46" ry="26" class="coralp o"/>
</g>
<g transform="translate(340 290)">
  <ellipse rx="44" ry="54" fill="#fffdf6" class="o"/>
  <circle r="20" class="gold o"/>
</g>
<g transform="translate(470 220)">
  <path d="M-40 90l10-60q-30-16-30-50 0-40 40-40t40 40q0 34-30 50l10 60z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="0" cy="-2" r="26" class="coralp o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('protocol', '取り決めた手順を定めた文書のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-190-150h380v300h-380z" class="paper"/>
  <g class="tealp o">{''.join(f'<circle cx="-150" cy="{-90+i*56}" r="18"/>' for i in range(4))}</g>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-116 {-90+i*56}h270"/>' for i in range(4))}</g>
  <circle cx="120" cy="110" r="32" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
""", ground=False)

add('province', '国の中のひとつの州のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-240-130q80-40 180-10t190 0v250q-120 40-220 0t-150 10z" class="greenp o"/>
  <path d="M-40-100q60-20 110 10t50 90-70 60-110-20-40-80 60-60z" class="coral o"/>
  <circle cx="40" cy="10" r="12" class="ink"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M540 340l-90-80"/></g>
""", ground=False, arrow=True)

add('provision', '必要な物を蓄えて配る供給のイラスト。', f"""
{box(170,280,140,100,28,'gold')}
{box(170,180,100,70,20,'gold')}
{person(470,352,1.15,-1,'teal','blue','reach','bob','smile')}
<g transform="translate(360 300)">
  <path d="M-50-30h100v60h-100z" class="coralp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 240h60"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('psychologist', '話を聞いて心を診る心理学者のイラスト。', f"""
<g transform="translate(200 330)">
  <path d="M-130 30v-40q0-20 20-20h220v60z" class="coral o"/>
  <path d="M-130-10q0-40 34-40h30v40z" class="corald o"/>
</g>
<g transform="translate(180 290)">
  <circle cx="0" cy="-20" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-27-23q4-28 25-28 24 0 28 25-13-10-27-4-12-10-26 7z" fill="{HAIR}" stroke="{HAIR}" stroke-width="2"/>
  <path d="M20-6h130v22H20z" class="teal o"/>
</g>
{sit(470,352,1.2,-1,'violet','violet','bun','smile','lap')}
<g transform="translate(410 300)"><path d="M-30-24h60v48h-60z" class="paper"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('psychology', '心の働きを調べる心理学のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-30 130v-40q-70-16-70-90 0-90 90-90 92 0 92 86 0 44-36 62v72z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2.5">
  <path d="M300 140q-30-38 0-54 30-16 30 22 0-38 30-22 30 16 0 54l-30 30z"/>
</g>
<g transform="translate(160 190)">
  <circle r="54" fill="none" stroke="{INK}" stroke-width="8"/>
  <circle r="46" fill="#fffdf6" opacity="0.4"/>
  <path d="M40 40l44 44" fill="none" stroke="{INK}" stroke-width="13" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('publication', '刷り上がって世に出る出版物のイラスト。', f"""
<g transform="translate(180 240)">
  <path d="M-110-100h220v160h-220z" class="bluep o"/>
  <path d="M-70-70h140v60h-140z" class="ink"/>
  <path d="M110-20h40v40h-40z" class="blued o"/>
</g>
<g transform="translate(410 250)">
  <path d="M-110-90h220v180h-220z" class="paper" transform="rotate(-6)"/>
  <path d="M-110-90h220v180h-220z" class="paper" transform="rotate(4) translate(16 10)"/>
  <g transform="rotate(4) translate(16 10)">
    <path d="M-80-60h160v60h-160z" class="tealp o"/>
    <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-80 20h160M-80 46h120"/></g>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 250h30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('publicity', 'スポットライトを当てて広く知らせる宣伝のイラスト。', f"""
<path d="M300 60l150 300H150z" fill="{TONES['gold'][1]}" opacity="0.7"/>
{box(300,300,170,110,30,'coral')}
{person(120,352,0.9,1,'teal','blue','hold','short','smile')}
{person(500,352,0.9,-1,'violet','gold','hold','bob','smile')}
<g fill="{INK}">
  <rect x="96" y="228" width="52" height="34" rx="6"/><rect x="452" y="228" width="52" height="34" rx="6"/>
</g>
<g class="golds"><path d="M120 200l-16-20M500 200l16-20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('pulse', '手首で打つ脈のイラスト。', f"""
{hand(160,260,1)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><circle cx="200" cy="250" r="26"/><circle cx="200" cy="250" r="44"/></g>
<g transform="translate(400 220)">
  <path d="M-160-90h320v180h-320z" class="paper"/>
  <path d="M-130 0h50l16-40 24 80 20-60 16 20h60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linejoin="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('pupil', 'かばんを持って机に向かう生徒のイラスト。', f"""
{sit(250,352,1.3,1,'teal','blue','short','smile','lap')}
{chair(260,356,1.2,'gold',1)}
<g transform="translate(400 320)">
  <path d="M-90-30h180v20h-180z" class="goldd o"/>
  <path d="M-70-10v46M70-10v46" class="a"/>
  <path d="M-56-70h100v40h-100z" class="paper"/>
</g>
<g transform="translate(120 340)">
  <path d="M-40-30h80v60h-80z" class="corald o"/>
  <path d="M-40-30q40-30 80 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('pursuit', '逃げる相手を追いかける追跡のイラスト。', f"""
{person(180,352,1.15,1,'violet','blue','walk','cap','neutral')}
{person(450,352,1.15,1,'coral','gold','walk','short','surprised')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M260 300h110"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"><path d="M110 300H70M120 330H80"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('puzzle', 'ひと片だけ足りないジグソーのイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-210-140h420v280h-420z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4">
    <path d="M-70-140v280M70-140v280M-210-46h420M-210 46h420"/>
  </g>
  <path d="M-70-46h140v92H-70z" fill="#fffaf1" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"/>
</g>
<g transform="translate(520 350) rotate(20)">
  <path d="M-40-34h80v68h-80z" class="teal o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('query', '知りたいことを投げて答えを引き出すイラスト。', f"""
<g transform="translate(420 230)">
  <ellipse cy="-90" rx="100" ry="30" class="bluep o"/>
  <path d="M-100-90v130q0 30 100 30t100-30V-90" class="bluep o"/>
  <path d="M-100-40q0 30 100 30t100-30M-100 10q0 30 100 30t100-30" fill="none" stroke="{TONES['blue'][2]}" stroke-width="3"/>
</g>
<g transform="translate(160 200)">
  <path d="M-40-50q0-40 42-40t42 38q0 30-42 40v16" fill="none" stroke="{TONES['coral'][0]}" stroke-width="16" stroke-linecap="round"/>
  <circle cx="2" cy="42" r="11" class="coral"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 290h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('quest', '遠い目当てを目指して旅するイラスト。', f"""
<path d="M0 340q150-40 300 0t300-30v90H0z" class="greenp o"/>
{person(160,346,1.2,1,'violet','blue','walk','short','neutral')}
<path d="M206 240v130" fill="none" stroke="{TONES['gold'][2]}" stroke-width="8" stroke-linecap="round"/>
<g transform="translate(500 250)">
  <path d="M-6 60V-70" class="a"/>
  <path d="M-6-70h80l-16 24 16 24H-6z" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M260 320h180"/></g>
""", ground=False, arrow=True)

add('questionnaire', '印をつけて答えるアンケートのイラスト。', f"""
<g transform="translate(280 200)">
  <path d="M-170-150h340v300h-340z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-80 {-100+i*56}h220"/>' for i in range(5))}</g>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="3">{''.join(f'<rect x="-140" y="{-116+i*56}" width="32" height="32"/>' for i in range(5))}</g>
  <g fill="none" stroke="{GRN}" stroke-width="6"><path d="M-132-104l10 12 20-24M-132 8l10 12 20-24M-132 120l10 12 20-24"/></g>
</g>
<g transform="translate(500 260)">
  <path d="M-14-120h28l10 120-24 40-24-40z" class="gold o"/>
</g>
""", ground=False)

add('quota', '決められた割当量まで満たすイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-110-140h220v280h-220z" fill="#fffdf6" class="o"/>
  <path d="M-110 20h220v120h-220z" class="teal o"/>
  <path d="M-130-40h260v14h-260z" class="coral o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-110 {100-i*40}h34"/>' for i in range(6))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M500 340v-130"/></g>
<path d="M60 390h480" class="a"/>
""", ground=True, arrow=True)

add('radar', '回る光線で物を捉えるレーダーのイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="150" fill="#0f2b24" class="o"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="3"><circle r="50"/><circle r="100"/><path d="M-150 0h300M0-150v300"/></g>
  <path d="M0 0L130-70A150 150 0 0 0 0-150z" fill="{TONES['green'][0]}" opacity="0.45"/>
  <path d="M0 0l130-70" fill="none" stroke="{TONES['green'][0]}" stroke-width="5"/>
  <circle cx="70" cy="-60" r="12" class="green"/>
  <circle cx="-60" cy="60" r="9" class="green" opacity="0.6"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('radiation', '見えない線を出す放射のイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="34" class="gold o"/>
  <g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2.5">
    <path d="M0-40A130 130 0 0 1 64-24L20-8A40 40 0 0 0 0-12z" transform="rotate(0)"/>
    <path d="M0-40A130 130 0 0 1 64-24L20-8A40 40 0 0 0 0-12z" transform="rotate(120)"/>
    <path d="M0-40A130 130 0 0 1 64-24L20-8A40 40 0 0 0 0-12z" transform="rotate(240)"/>
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="300" cy="220" r="170"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('rage', '顔を真っ赤にして激しく怒るイラスト。', f"""
<g transform="translate(300 200)">
  <circle r="100" class="coral o"/>
  <g fill="{INK}"><path d="M-66-30q30-20 54-4-28 6-54 4zM12-34q24-16 54 4-26 2-54-4z"/></g>
  <circle cx="-38" cy="-8" r="7" class="ink"/><circle cx="38" cy="-8" r="7" class="ink"/>
  <path d="M-40 46q40-30 80 0z" fill="{INK}"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M150 90l-20-30M300 70V36M450 90l20-30M120 200H84M480 200h36"/>
</g>
<g class="o" fill="#dfe6ea"><circle cx="170" cy="140" r="18"/><circle cx="430" cy="140" r="18"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('rail', 'まくら木の上に伸びるレールのイラスト。', f"""
<g fill="{TONES['gold'][2]}">
  {''.join(f'<rect x="{120-i*8}" y="{360-i*30}" width="{360+i*16}" height="16" rx="4"/>' for i in range(7))}
</g>
<g fill="none" stroke="#b9c2c9" stroke-width="14" stroke-linecap="round">
  <path d="M170 390L270 150M430 390L330 150"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="3">
  <path d="M170 390L270 150M430 390L330 150"/>
</g>
""", ground=False)

add('ranking', '上から順に並べた順位のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-60-140h120v140h-120z" class="gold o"/>
  <path d="M-190-90h120v90h-120z" class="tealp o"/>
  <path d="M70-50h120v50H70z" class="tealp o"/>
</g>
{star(300,130,34,'gold')}
{star(170,180,24,'teal')}
{star(430,220,24,'teal')}
<path d="M60 320h480" class="a"/>
""", ground=True)

add('rarely', 'ごくまれにしか起きないイラスト。', f"""
<g class="a" marker-end="url(#ar)"><path d="M60 240h480"/></g>
<g class="coral"><circle cx="200" cy="240" r="14"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M200 220v-60"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 10"><path d="M70 300h460"/></g>
{xx(430,180,0.9)}
""", ground=False, arrow=True)

add('rat', '長いしっぽのネズミのイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-100 40q-30-50 10-80 50-36 110-14 50 18 44 56-6 36-74 40-60 4-90-2z" fill="#9aa3ab" class="o"/>
  <circle cx="86" cy="-24" r="30" fill="#9aa3ab" class="o"/>
  <path d="M112-44l30 8-30 12z" class="corald o"/>
  <circle cx="96" cy="-30" r="5" class="ink"/>
  <circle cx="70" cy="-56" r="18" fill="#c3cad0" class="o"/>
  <path d="M-100 20q-70 10-90 60" fill="none" stroke="#9aa3ab" stroke-width="10" stroke-linecap="round"/>
  <path d="M-40 40v28M30 42v26" fill="none" stroke="#9aa3ab" stroke-width="9" stroke-linecap="round"/>
  <g fill="none" stroke="{INK}" stroke-width="2"><path d="M112-32h40M112-24h38"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('rating', '星の数で表す評価のイラスト。', f"""
{star(130,210,44,'gold')}
{star(235,210,44,'gold')}
{star(340,210,44,'gold')}
<g opacity="0.35">{star(445,210,44,'gold')}</g>
<g opacity="0.35">{star(550,210,44,'gold')}</g>
<path d="M60 320h480" class="a"/>
""", ground=True)

add('ray', 'すきまから差しこむ一筋の光のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-260-160h220v320h-220zM40-160h220v320H40z" fill="#dfe6ea" class="o"/>
</g>
<path d="M280 40h40v320h-40z" fill="{TONES['gold'][1]}"/>
<path d="M282 40l60 320h-84z" fill="{TONES['gold'][1]}" opacity="0.8"/>
<g class="golds"><path d="M300 30v-20"/></g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M300 90v90"/></g>
""", ground=False, arrow=True)

add('realm', '王のおさめる領域のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-240-120q100-40 240 0t240-20v240q-140 40-240 0t-240 20z" class="greenp o"/>
</g>
<g transform="translate(300 150)">
  <path d="M-60 20l-12-56 34 22 38-44 38 44 34-22-12 56z" class="gold o"/>
  <circle cx="0" cy="-50" r="9" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="16 12"><path d="M60 220q120-30 240 0t240-16"/></g>
""", ground=False)

add('rear', '乗り物の後ろ側を示すイラスト。', f"""
<g transform="translate(300 270)">
  <path d="M-180 0v-50l50-64h200l60 64V0z" class="teal o"/>
  <g fill="#fffdf6" class="o"><rect x="-110" y="-104" width="70" height="40"/><rect x="-20" y="-104" width="70" height="40"/></g>
  <g fill="{INK}"><circle cx="-110" cy="6" r="26"/><circle cx="100" cy="6" r="26"/></g>
  <path d="M-180-50h-30v50h30z" class="tealp o"/>
  <path d="M-206-40h-20v30h20z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><rect x="60" y="180" width="80" height="130" rx="14"/></g>
<g class="a" marker-end="url(#ar)"><path d="M100 150v40"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('rebel', 'ひとりだけ流れに逆らう反抗者のイラスト。', f"""
{person(140,352,0.95,1,'teal','blue','walk','short','neutral')}
{person(250,352,0.95,1,'teal','blue','walk','bob','neutral')}
{person(360,352,0.95,1,'teal','blue','walk','short','neutral')}
{person(500,352,1.1,-1,'coral','gold','walk','cap','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M110 200h300"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M540 250h-90"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('rebellion', '大勢が支配に立ち向かう反乱のイラスト。', f"""
{chair(480,340,1.3,'gold',-1)}
{person(120,352,1,1,'coral','blue','up','short','sad')}
{person(210,352,1,1,'gold','violet','up','bob','sad')}
{person(300,352,1,1,'coral','gold','up','cap','sad')}
<g class="coral o"><path d="M146 200h70l-14 22 14 22h-70z"/><path d="M236 200h70l-14 22 14 22h-70z"/></g>
<g class="a"><path d="M146 260v-70M236 260v-70"/></g>
<g class="a" marker-end="url(#ar)"><path d="M360 150h70"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('recession', '景気が落ちこんで店が閉まる不況のイラスト。', f"""
<g transform="translate(200 200)">
  <path d="M-140-120h280v240h-280z" class="paper"/>
  <path d="M-110 80l50-40 40 30 60-80" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
  <path d="M-110-90v190h250" class="a"/>
</g>
<g transform="translate(460 300)">
  <path d="M-90 60v-120h180V60z" fill="#fffdf6" class="o"/>
  <path d="M-90-60h180v20h-180z" class="teald o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="7">{''.join(f'<path d="M-70 {-20+i*20}h140"/>' for i in range(4))}</g>
</g>
{xx(460,160,1)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('recipient', '贈られたものを受け取る人のイラスト。', f"""
{person(420,352,1.3,-1,'teal','blue','reach','bob','smile')}
{box(230,270,140,100,28,'coral')}
{hand(90,260,1)}
<g class="a" marker-end="url(#ar)"><path d="M170 180h120"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('recognition', '見て「あの人だ」と気づくイラスト。', f"""
{person(180,352,1.2,1,'teal','blue','point','short','surprised')}
{face(450,210,80,'smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M260 240h100"/></g>
<g transform="translate(250 150)">
  <g fill="{TONES['gold'][0]}"><rect x="-11" y="-40" width="22" height="52" rx="11"/><circle cy="30" r="12"/></g>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('reconstruction', 'こわれた建物を組み直す再建のイラスト。', f"""
<g transform="translate(200 300)">
  <path d="M-80 0v-90h60l-10 40 20-40h10v90z" fill="#dfe6ea" class="o"/>
  <path d="M-94-90l40-30 30 20" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M310 240h50"/></g>
<g transform="translate(460 300)">
  <path d="M-80 0v-90h160V0z" fill="#fffdf6" class="o"/>
  <path d="M-94-90L0-146l94 56z" class="teal o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="6"><path d="M-100 0v-160h200V0M-100-80h200M-40-160V0M40-160V0"/></g>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('recruitment', '人を募って迎え入れる採用のイラスト。', f"""
<g transform="translate(400 190)">
  <path d="M-130-110h260v200h-260z" class="paper"/>
  <path d="M-100-80h200v50h-200z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-100-10h200M-100 20h200M-100 50h140"/></g>
</g>
<path d="M400 280v40" class="a"/>
{person(110,356,0.85,1,'coral','blue','carry','short','smile')}
{person(190,356,0.85,1,'gold','violet','carry','bob','smile')}
<g class="a" marker-end="url(#ar)"><path d="M250 330h70"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('referee', 'ホイッスルを吹いて裁く審判のイラスト。', f"""
{person(300,352,1.3,1,'violet','violet','point','cap','neutral')}
<g transform="translate(262 250)">
  <path d="M-30-14h50v28h-50z" class="ink"/>
  <path d="M20-8h26v16H20z" class="ink"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M210 220q-24 20 0 40M170 200q-40 40 0 80"/>
</g>
{person(120,356,0.8,1,'teal','blue','walk','short','neutral')}
{person(490,356,0.8,-1,'coral','gold','walk','bob','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('reference', '出どころの本を指し示す参照のイラスト。', f"""
<g transform="translate(200 220)">
  <path d="M-130-120h260v240h-260z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-96 {-80+i*40}h190"/>' for i in range(5))}</g>
  <g fill="{TONES['coral'][0]}"><circle cx="106" cy="-80" r="9"/></g>
</g>
<g transform="translate(460 230)">
  <path d="M-90-110h180v220h-180z" class="teal o"/>
  <path d="M-70-90h140v180h-140z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-40-50h80M-40-20h80M-40 10h60"/></g>
  <path d="M60-110h24v70l-12-16-12 16z" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M320 160h40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('referendum', 'みんなが票を入れて決める国民投票のイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-110-40h220v130h-220z" class="tealp o"/>
  <path d="M-60-50h120v14h-120z" class="ink"/>
</g>
<g transform="translate(300 150)">
  <path d="M-56-50h112v70h-112z" class="paper"/>
  <g fill="none" stroke="{GRN}" stroke-width="7"><path d="M-30-20l14 16 26-30"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 230v20"/></g>
{person(120,356,0.85,1,'coral','blue','give','short','smile')}
{person(490,356,0.85,-1,'gold','violet','give','bob','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('reflection', '水面にうつる山かげのイラスト。', f"""
<path d="M0 0h600v220H0z" fill="#e6f0fb"/>
<path d="M0 220l160-140 110 100 90-70 240 110z" class="greenp o"/>
<circle cx="490" cy="80" r="36" class="goldp o"/>
<path d="M0 220h600v180H0z" class="bluep"/>
<path d="M0 220h600" class="a"/>
<g opacity="0.55"><path d="M0 220l160 140 110-100 90 70 240-110z" class="green"/></g>
<circle cx="490" cy="300" r="36" class="gold" opacity="0.5"/>
<g fill="none" stroke="#fffdf6" stroke-width="3"><path d="M40 270h120M300 320h140M120 360h180"/></g>
""", ground=False)

add('reform', '古い仕組みを作り変える改革のイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-90-80h180v160h-180z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="6"><path d="M-60-40h120M-60 0h120M-60 40h120"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 240h50"/></g>
<g transform="translate(450 240)">
  <path d="M-90-80h180v160h-180z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="8"><path d="M-60-30l40 40 80-80"/></g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"><path d="M-60 40h120"/></g>
</g>
<g transform="translate(330 340) rotate(-28)">
  <path d="M-8-40h16v80h-16z" fill="{MUTED}" class="o"/>
  <path d="M-18-52h36v20h-36z" fill="{MUTED}" class="o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('refuge', '嵐をよけて身を寄せる避難所のイラスト。', f"""
{cloud(140,90,1.5,'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
  {''.join(f'<path d="M{70+i*30} {170+(i%3)*16}l-14 46"/>' for i in range(5))}
</g>
<g transform="translate(400 300)">
  <path d="M-130 60v-120h260V60z" fill="#fffdf6" class="o"/>
  <path d="M-150-60L0-140l150 80z" class="teal o"/>
  <path d="M-40 0h80v60h-80z" class="teald o"/>
</g>
{person(340,356,0.85,1,'coral','blue','stand','short','smile')}
{person(450,356,0.85,-1,'gold','violet','stand','bob','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
