"""第94回: su〜tr の名詞を中心に45語。"""
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

add('surplus', '必要な分を越えてあふれる余りのイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-120-100h240v190h-240z" fill="#fffdf6" class="o"/>
  <path d="M-120-40h240v130h-240z" class="teal o"/>
  <path d="M-140-40h280v12h-280z" class="coral o"/>
</g>
<g class="teal o">
  <circle cx="230" cy="120" r="24"/><circle cx="300" cy="100" r="24"/><circle cx="370" cy="120" r="24"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M500 250V150"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('surveillance', 'カメラで見張る監視のイラスト。', f"""
<g transform="translate(160 140)">
  <path d="M-60-30h90v60h-90z" class="ink"/>
  <path d="M30-20l40-16v72l-40-16z" class="ink"/>
  <circle cx="52" cy="0" r="12" class="coral"/>
  <path d="M-60 0v-40h-30" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M240 170l120 100"/></g>
{person(400,352,1.05,-1,'teal','blue','walk','short','neutral')}
<g transform="translate(510 200)">
  <path d="M-60-60h120v100h-120z" class="ink"/>
  <path d="M-48-48h96v76h-96z" fill="#26303f"/>
  <circle cx="0" cy="-10" r="16" fill="{TONES['green'][0]}"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('survival', '厳しい中でも生き残るイラスト。', f"""
<path d="M0 300h600v100H0z" fill="#e8ded2"/>
<g fill="none" stroke="#c9b79f" stroke-width="6"><path d="M0 340h600M0 370h600"/></g>
{sun(500,90,44)}
<g transform="translate(230 300)">
  <path d="M0 0v-90" class="greens"/>
  <path d="M0-50q-40-6-46-40 38-6 46 40zM0-70q40-6 46-40-38-6-46 40z" class="greenp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round">
  <path d="M120 300v-40M150 300l-14-30M390 300v-34M420 300l14-28"/>
</g>
{ck(330,200,1.1)}
<path d="M0 300h600" class="a"/>
""", ground=False)

add('survivor', 'がれきの中から生き残った人のイラスト。', f"""
<g fill="#c3cad0" class="o">
  <path d="M60 340l60-30 20 40-60 16z"/>
  <path d="M480 350l60-24 14 40-62 14z"/>
  <path d="M160 380l50-16 12 30-50 10z"/>
  <path d="M420 380l50-16 12 30-50 10z"/>
</g>
{person(300,350,1.3,1,'teal','blue','up','short','neutral')}
{ck(470,180,1.1)}
<path d="M60 390h480" class="a"/>
""", ground=True)

add('suspension', 'ひもでつり下げて動きを止めるイラスト。', f"""
<g transform="translate(300 130)">
  <path d="M-160-40h320v20h-320z" class="ink"/>
  <path d="M0-20v120" fill="none" stroke="{MUTED}" stroke-width="6"/>
</g>
{box(300,300,140,100,26,'gold')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10">
  <path d="M470 200v80M510 200v80"/>
</g>
<path d="M60 390h480" class="a"/>
""", ground=True)

add('suspicion', '横目でうかがって疑うイラスト。', f"""
{face(200,210,88,'flat')}
<g fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round">
  <path d="M140 172q24-12 46 0M216 172q24-12 46 0"/>
</g>
<g fill="{INK}"><circle cx="190" cy="196" r="8"/><circle cx="266" cy="196" r="8"/></g>
{person(470,352,1.1,-1,'coral','gold','stand','bob','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M300 230h110"/></g>
<g transform="translate(340 130)">
  <path d="M-26-26q0-28 28-28t28 26q0 22-28 28v12" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"/>
  <circle cy="36" r="7" class="coral"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('sword', '両刃のまっすぐな剣のイラスト。', f"""
<g transform="translate(300 220) rotate(-30)">
  <path d="M-10-170h20l6 190h-32z" fill="#c3cad0" class="o"/>
  <path d="M-16 20h32l-16 24z" fill="#c3cad0" class="o"/>
  <path d="M-60 20h120v20H-60z" class="goldd o"/>
  <path d="M-10 40h20v80h-20z" class="gold o"/>
  <circle cx="0" cy="130" r="14" class="goldd o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sympathy', '肩に手を置いて思いをくみ取るイラスト。', f"""
{person(220,352,1.2,1,'teal','blue','give','bun','smile')}
{person(400,352,1.15,-1,'blue','blue','think','short','sad')}
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2.5">
  <path d="M310 160q-24-32 0-44 24-12 24 18 0-30 24-18 24 12 0 44l-24 24z"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('symptom', '熱とせきに表れる症状のイラスト。', f"""
{person(220,352,1.25,1,'blue','blue','stand','short','sad')}
<g fill="{TONES['coral'][0]}"><circle cx="200" cy="228" r="6"/><circle cx="240" cy="236" r="6"/><circle cx="214" cy="252" r="5"/></g>
{thermometer(430,300,0.9,0.85)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M290 200q18-18 0-36M320 186q30-30 0-60"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('syndrome', 'いくつもの症状がまとまって現れる症候群のイラスト。', f"""
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="14 12"><circle cx="300" cy="210" r="170"/></g>
{thermometer(180,270,0.55,0.85)}
<g transform="translate(300 120)">
  <circle r="40" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-16 14q16 12 32 0" fill="none" stroke="{INK}" stroke-width="3" transform="translate(0 6) scale(1 -1)"/>
  <g fill="{INK}"><circle cx="-14" cy="-8" r="4"/><circle cx="14" cy="-8" r="4"/></g>
</g>
<g transform="translate(420 250)">
  <path d="M-40 40l10-60q-30-16-30-46 0-36 36-36t36 36q0 30-30 46l10 60z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M-20-40h40M-14-24h28"/></g>
</g>
<g class="coral"><circle cx="220" cy="330" r="8"/><circle cx="250" cy="350" r="7"/><circle cx="196" cy="352" r="6"/></g>
""", ground=False)

add('tale', '物語の世界が開く本のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-220-130h440v260h-440z" class="paper"/>
  <path d="M0-130v260" class="a"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M30-90h160M30-60h160M30-30h130M30 0h160M30 30h120"/></g>
  <path d="M-190 90h170v20h-170z" class="greenp o"/>
  <path d="M-160 90v-70h100v70z" fill="#fffdf6" class="o"/>
  <path d="M-170-20h40v-30h-40zM-90-20h40v-30h-40z" class="teal o"/>
  <path d="M-160-20h100v-20h-100z" class="teal o"/>
</g>
""", ground=False)

add('teens', '十代の若者のイラスト。', f"""
{person(180,352,1,1,'coral','blue','up','short','smile')}
{person(300,352,1.05,1,'gold','violet','up','bob','smile')}
{person(420,352,1,-1,'teal','gold','up','cap','smile')}
<g transform="translate(300 160)">
  <path d="M-230-16h460v32h-460z" fill="#dfe6ea" class="o"/>
  <path d="M-60-16h180v32H-60z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M300 200v-24"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('temple', '重なった屋根をもつ寺のイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-170 0h340v20h-340z" class="goldd o"/>
  <path d="M-120 0v-90h240V0z" fill="#fffdf6" class="o"/>
  <path d="M-180-90h360l-40-30h-280z" class="corald o"/>
  <path d="M-140-120h280l-36-30h-208z" class="coral o"/>
  <path d="M-100-150h200l-40-40h-120z" class="corald o"/>
  <path d="M-40 0v-60h80V0z" class="goldd o"/>
  <path d="M-6-190h12v-20h-12z" class="gold o"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('tension', '両側から引かれてぴんと張る緊張のイラスト。', f"""
{hand(110,220,1)}
{hand(490,220,-1)}
<g fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"><path d="M180 220h240"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M290 180v-24M310 180v-24M300 262v24"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M200 320H100M400 320h100"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('terrain', '高低のある地形のイラスト。', f"""
<path d="M0 400V250l100-90 90 70 110-140 90 110 100-40 110 70v170z" class="greenp o"/>
<path d="M0 250l100-90 90 70 110-140 90 110 100-40 110 70" fill="none" stroke="{INK}" stroke-width="4"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M40 400V250M40 250h30"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M310 400V90M310 90h30"/></g>
<path d="M0 396h600" class="a"/>
""", ground=False)

add('territory', '境を引いて自分の側とする領域のイラスト。', f"""
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="16 12"><path d="M300 60v320"/></g>
<g transform="translate(160 210)">
  <path d="M-130 90q0-120 130-120t130 120z" class="tealp o"/>
  <path d="M-20-30v-70h4l50 18-50 18" class="ink"/>
</g>
{person(440,352,1.1,-1,'coral','gold','point','short','neutral')}
{xx(360,200,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('testimony', '法廷で手を挙げて事実を述べる証言のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-120-40h240v90h-240z" class="goldd o"/>
  <path d="M-130-60h260v20h-260z" class="gold o"/>
</g>
{person(300,260,1.15,1,'teal','blue','up','short','neutral')}
<g transform="translate(470 190)">
  <path d="M-70-60h140v110h-140z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-44-30h88M-44-6h88M-44 18h60"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M360 190h40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('testing', '試して確かめる試験のイラスト。', f"""
<g transform="translate(200 240)">
  <path d="M-120-110h240v220h-240z" class="bluep o"/>
  <path d="M-70-70h140v100h-140z" class="ink"/>
  <path d="M-30 60h60v40h-60z" class="blued o"/>
</g>
<g transform="translate(450 240)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-20-60h80M-20-20h80M-20 20h60"/></g>
  <g fill="none" stroke="{GRN}" stroke-width="7"><path d="M-60-66l10 12 20-24M-60-26l10 12 20-24M-60 14l10 12 20-24"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M330 240h30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('textbook', '授業で使う教科書のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-170-150h340v300h-340z" class="teal o"/>
  <path d="M-150-130h300v260h-300z" fill="#fffdf6" class="o"/>
  <path d="M-100-100h200v70h-200z" class="tealp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-100 0h200M-100 34h200M-100 68h150"/></g>
  <path d="M120-150h34v90l-17-20-17 20z" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('theft', 'そっと持ち去ってしまう盗みのイラスト。', f"""
<g transform="translate(200 300)">
  <path d="M-90-40h180v100h-180z" class="goldd o"/>
  <path d="M-90-40q90-46 180 0z" class="gold o"/>
</g>
{hand(390,220,-1)}
<g transform="translate(300 230)">
  <path d="M-40-26h80v52h-80z" class="greenp o"/>
  <circle r="14" class="gold o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M240 180h100"/></g>
{xx(490,140,1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('theology', '神について論じる神学のイラスト。', f"""
<g transform="translate(260 220)">
  <path d="M-140-150h280v300h-280z" class="violet o"/>
  <path d="M-120-130h240v260h-240z" fill="#fffdf6" class="o"/>
  <path d="M-14-100h28v60h60v28h-60v60h-28v-60h-60v-28h60z" class="violetp o"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="8"><ellipse cx="490" cy="170" rx="46" ry="14"/></g>
{person(490,352,1.1,-1,'violet','violet','think','bun','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('therapy', '手当てを受けて調子を取り戻す治療のイラスト。', f"""
{sit(220,352,1.25,1,'teal','blue','short','smile','down')}
{chair(230,356,1.2,'gold',1)}
{person(430,352,1.15,-1,'violet','violet','reach','bun','smile')}
<g fill="none" stroke="{GRN}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M160 200q120-90 260-40"/></g>
{ck(300,140,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('threat', '力にものを言わせて脅すイラスト。', f"""
{person(170,352,1.25,1,'coral','blue','up','short','neutral')}
{person(460,352,1.15,-1,'teal','gold','stand','bob','sad')}
<g transform="translate(320 170)">
  <path d="M0-90l110 180h-220z" class="gold o"/>
  <g fill="{INK}"><rect x="-12" y="-30" width="24" height="66" rx="12"/><circle cy="58" r="13"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 300h120"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('thumb', '手の親指を示したイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-70 100v-70q0-40 40-46l70-10v40l-40 10h70q20 0 20 20t-20 20h-20q20 0 20 18t-20 18h-20q16 0 16 16t-16 16z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-70-16q-40-30-10-70 34-34 66 0l14 40" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"><ellipse cx="255" cy="180" rx="60" ry="46" transform="rotate(-30 255 180)"/></g>
<path d="M430 180h-90" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('timing', 'ちょうどよい瞬間をとらえるイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="140" fill="#fffdf6" class="o"/>
  <path d="M-20-166h40v26h-40z" class="ink"/>
  <path d="M0 0v-100" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"/>
  <circle r="10" class="ink"/>
  <path d="M-30-120h60v30h-60z" class="greenp o"/>
  <g fill="{INK}">{''.join(f'<rect x="-4" y="-128" width="8" height="16" transform="rotate({a})"/>' for a in range(0,360,30))}</g>
</g>
{ck(480,340,1)}
""", ground=False)

add('tobacco', '乾かした葉をつめたたばこのイラスト。', f"""
<g transform="translate(180 260)">
  <path d="M0 60V-40" class="greens"/>
  <path d="M0-10q-60-6-70-54 58-8 70 54z" fill="#a89a72" class="o"/>
  <path d="M0-40q60-6 70-54-58-8-70 54z" fill="#a89a72" class="o"/>
</g>
<g transform="translate(430 290)">
  <path d="M-60-90h120v130h-120z" class="corald o"/>
  <path d="M-60-90h120v30h-120z" class="coral o"/>
  <g fill="#fffdf6" class="o"><rect x="-40" y="-116" width="20" height="30"/><rect x="-12" y="-116" width="20" height="30"/><rect x="16" y="-116" width="20" height="30"/></g>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('toll', '通るために払う通行料のイラスト。', f"""
<path d="M0 320h600v80H0z" fill="#dfe6ea" class="o"/>
<g fill="none" stroke="#fffdf6" stroke-width="5" stroke-dasharray="24 20"><path d="M0 360h600"/></g>
<g transform="translate(420 260)">
  <path d="M-10-90h20v150h-20z" class="ink"/>
  <path d="M-10-80h-180v30h180z" class="coral o"/>
  <g fill="#fffdf6">{''.join(f'<rect x="{-170+i*40}" y="-80" width="20" height="30"/>' for i in range(4))}</g>
</g>
<g transform="translate(180 240)">
  <ellipse rx="34" ry="14" class="gold o"/>
  <ellipse rx="18" ry="7" class="goldd o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 270v30"/></g>
""", ground=False, arrow=True)

add('ton', '目盛りが振り切れるほど重いおもりのイラスト。', f"""
<g transform="translate(240 250)">
  <path d="M-110-80h220v170h-220z" class="ink"/>
  <path d="M-70-110h140v30h-140z" fill="{INK}"/>
  <path d="M-40-150h80v40h-80z" fill="{INK}"/>
</g>
<g transform="translate(240 360)">
  <path d="M-150-16h300v32h-300z" class="goldd o"/>
</g>
<g transform="translate(490 300)">
  <path d="M-80 0a80 80 0 0 1 160 0z" fill="#fffdf6" class="o"/>
  <path d="M-80 0h160" class="a"/>
  <path d="M0 0l60-42" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round"/>
  <circle r="8" class="ink"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tone', '言い方の調子が変わるイラスト。', f"""
{person(150,352,1.2,1,'teal','blue','point','short','neutral')}
<g transform="translate(360 180)">
  <path d="M-120-70h240v120h-240zM-80 50l-14 32 44-32z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
    <path d="M-80-30q30-30 60 0t60-20"/>
  </g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" stroke-linecap="round">
    <path d="M-80 10q30 30 60 0t60 20"/>
  </g>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('tournament', '勝ち上がりで決める大会のイラスト。', f"""
<g transform="translate(300 230)">
  <g fill="none" stroke="{INK}" stroke-width="4">
    <path d="M-230-120h60v60h-60M-230 0h60v-60h-60"/>
    <path d="M-170-60h50v60h-50"/>
    <path d="M230-120h-60v60h60M230 0h-60v-60h60"/>
    <path d="M170-60h-50v60h50"/>
    <path d="M-120 0h240"/>
  </g>
  <g class="tealp o">{''.join(f'<rect x="-290" y="{-136+i*120}" width="60" height="32"/>' for i in range(2))}</g>
  <g class="tealp o">{''.join(f'<rect x="230" y="{-136+i*120}" width="60" height="32"/>' for i in range(2))}</g>
</g>
{star(300,300,34,'gold')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('trademark', '自社の印として登録したマークのイラスト。', f"""
{box(240,270,180,130,34,'teal')}
<g transform="translate(240 250)">
  <circle r="46" fill="#fffdf6" class="o"/>
  <path d="M-22 18l22-42 22 42z" class="coral o"/>
</g>
<g transform="translate(450 190)">
  <circle r="42" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M-16 18v-36h20q14 0 14 12t-14 12h-20M4 6l14 12" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('trading', '品と金をやり取りする取引のイラスト。', f"""
{person(140,352,1.15,1,'teal','blue','give','short','smile')}
{person(460,352,1.15,-1,'coral','gold','give','bob','smile')}
{box(240,250,100,70,20,'gold')}
<g transform="translate(370 250)">
  <path d="M-50-26h100v52h-100z" class="greenp o"/>
  <circle r="14" class="gold o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 160h120M370 320H250"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('traditional', '昔から受け継がれてきた形のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-150 0h300v20h-300z" class="goldd o"/>
  <path d="M-110 0v-80h220V0z" fill="#fffdf6" class="o"/>
  <path d="M-160-80h320l-36-30h-248z" class="corald o"/>
  <path d="M-120-110h240l-34-34h-172z" class="coral o"/>
  <path d="M-30 0v-50h60V0z" class="goldd o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M80 360h60"/></g>
{person(500,352,0.9,-1,'violet','violet','stand','bun','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('transaction', 'レジでの一回のやり取りのイラスト。', f"""
<g transform="translate(330 290)">
  <path d="M-160-30h320v20h-320z" class="goldd o"/>
  <path d="M-130-10v46M130-10v46" class="a"/>
  <path d="M-80-100h160v70h-160z" class="bluep o"/>
  <g fill="#fffdf6" class="o"><rect x="-60" y="-90" width="120" height="30"/></g>
</g>
{person(140,352,1,1,'teal','blue','give','short','smile')}
<g transform="translate(220 250)">
  <path d="M-40-20h80v40h-80z" class="greenp o"/>
  <circle r="12" class="gold o"/>
</g>
<g transform="translate(490 250)">
  <path d="M-30-50h60v100h-60z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-18-30h36M-18-14h36M-18 2h24"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('transcript', '成績を記した証明書のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-190-150h380v300h-380z" class="paper"/>
  <path d="M-150-110h300v40h-300z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M-150 {-40+i*44}h300"/>' for i in range(5))}
    <path d="M60-70v220"/>
  </g>
  <g fill="{INK}">{''.join(f'<rect x="90" y="{-58+i*44}" width="22" height="10"/>' for i in range(4))}</g>
  <circle cx="120" cy="110" r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
""", ground=False)

add('transit', '荷が経由地を通って運ばれるイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-100-90h200v160h-200z" class="tealp o"/>
  <path d="M-60-50h120v80h-120z" class="teal o"/>
</g>
{box(110,280,90,60,18,'gold')}
{box(500,280,90,60,18,'gold')}
<g class="a" marker-end="url(#ar)"><path d="M170 180h60M370 180h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('transition', '少しずつ移り変わる過渡期のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-250-70h100v140h-100z" class="teal o"/>
  <path d="M-150-70h100v140h-100z" class="tealp o"/>
  <path d="M-50-70h100v140H-50z" class="goldp o"/>
  <path d="M50-70h100v140H50z" class="coralp o"/>
  <path d="M150-70h100v140H150z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M60 350h480"/></g>
""", ground=False, arrow=True)

add('transmission', '塔から電波を送って届けるイラスト。', f"""
<g transform="translate(140 280)">
  <path d="M-40 80l16-160h48L40 80M-30 20h60M-22-30h44" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M190 160q30 30 0 60M230 130q60 60 0 120M270 100q90 90 0 180"/>
</g>
<g transform="translate(470 260)">
  <path d="M-100-80h200v160h-200z" class="ink"/>
  <path d="M-86-66h172v132h-172z" fill="#26303f"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6"><path d="M-50-20h100M-50 10h70"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('trauma', '過去の傷が心に残るイラスト。', f"""
{person(180,352,1.2,1,'blue','blue','think','short','sad')}
<g transform="translate(430 210)">
  <path d="M0-50q-56-66-98-16-40 46 98 146 138-100 98-146-42-50-98 16z" fill="#fffdf6" class="o"/>
  <path d="M-10-40l24 40-30 26 20 40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
</g>
{cloud(180,100,1.2,'violet')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('treasure', '宝石があふれる宝箱のイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-140 10h280v90h-280z" class="goldd o"/>
  <path d="M-140 10q0-80 140-80t140 80z" class="gold o"/>
  <path d="M-140 10h280" class="a"/>
  <path d="M-20 30h40v40h-40z" class="goldp o"/>
</g>
<g transform="translate(240 200)">
  <path d="M-30-10h60l-30 40z" class="tealp o"/>
  <path d="M-30-10l14-20h32l14 20z" class="teal o"/>
</g>
<g transform="translate(360 190)">
  <path d="M-24-8h48l-24 34z" class="coralp o"/>
  <path d="M-24-8l12-16h24l12 16z" class="coral o"/>
</g>
<g class="golds"><path d="M150 130l-20-22M460 130l20-22M300 110V88"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('treaty', '国どうしが取り結ぶ条約のイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-6 120V-90" class="a"/>
  <path d="M-6-90h96v64H-6z" class="teal o"/>
</g>
<g transform="translate(440 240)">
  <path d="M6 120V-90" class="a"/>
  <path d="M6-90h-96v64H6z" class="coral o"/>
</g>
<g transform="translate(300 250)">
  <path d="M-90-70h180v140h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-56-40h112M-56-14h112M-56 12h80"/></g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><path d="M-56 44q20-16 40 0"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M10 44q20-16 40 0"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('trial', '何度も試して確かめる試行のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-230-60h120v120h-120z" class="tealp o"/>
  <path d="M-60-60h120v120H-60z" class="tealp o"/>
  <path d="M110-60h120v120H110z" class="teal o"/>
</g>
{xx(130,300,0.7)}
{xx(300,300,0.7)}
{ck(470,300,0.9)}
<g class="a" marker-end="url(#ar)"><path d="M180 220h50M350 220h50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('tribe', '火を囲んで結びつく族のイラスト。', f"""
{flame(300,320,1)}
{sit(150,340,0.9,1,'gold','coral','short','neutral','down')}
{sit(450,340,0.9,-1,'gold','coral','bun','neutral','down')}
{person(300,200,0.8,1,'gold','coral','up','cap','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10"><circle cx="300" cy="270" r="200"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tribute', '花をささげて讃える賛辞のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-90 80h180v26h-180z" class="teald o"/>
  <path d="M-50-140h100v220h-100z" fill="#dfe6ea" class="o"/>
  <g fill="{MUTED}"><rect x="-26" y="-100" width="52" height="12"/><rect x="-26" y="-70" width="52" height="12"/></g>
</g>
{person(150,352,1.1,1,'violet','blue','give','bun','smile')}
<g class="coral o"><circle cx="230" cy="320" r="16"/><circle cx="400" cy="320" r="16"/></g>
<g class="greens"><path d="M230 336v26M400 336v26"/></g>
{star(470,150,26,'gold')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('trophy', '優勝のしるしのトロフィーのイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-70-110h140v50q0 80-70 80t-70-80z" class="gold o"/>
  <path d="M-70-96q-50 0-50 34t50 34M70-96q50 0 50 34t-50 34" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12"/>
  <path d="M-16 20h32v46h-32z" class="goldd o"/>
  <path d="M-70 66h140v30h-140z" class="goldd o"/>
  <path d="M0-96l14 30 32 4-24 22 6 32-28-16-28 16 6-32-24-22 32-4z" class="goldp"/>
</g>
<g class="golds"><path d="M150 160l-20-22M450 160l20-22M300 110V88"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
