"""第26回: 参加・拒否・回復・減らすなど30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('palm', '開いた手のひらの内側を示したイラスト。', f"""
<circle cx="470" cy="96" r="54" class="coralp"/>
<g transform="translate(280 250)">
  <path d="M-70 90q-30-90 0-130 10-50 30-50t18 44v26q6-38 24-38t18 44v14q8-30 24-28t12 34q8-20 20-14t8 30q0 54-34 64z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <g fill="none" stroke="{SKINL}" stroke-width="2.5"><path d="M-46 40q40-20 76 0M-40 66q36-16 66 0"/></g>
</g>
<circle cx="290" cy="290" r="52" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
""", ground=True)

add('participate', '輪の中に加わって、一緒に活動しているイラスト。', f"""
<circle cx="320" cy="230" r="140" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" stroke-dasharray="16 12"/>
{person(250,320,0.85,1,'teal','blue','stand','short','smile')}
{person(390,320,0.85,-1,'gold','violet','stand','bob','smile')}
{person(110,346,0.9,1,'coral','gold','walk','cap','smile')}
<path d="M170 250h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('particular', '並んだ品の中から、特定の一つを選び出すイラスト。', f"""
<g class="tealp o">
  {''.join(f'<rect x="{80+i*82}" y="200" width="62" height="80"/>' for i in range(6))}
</g>
<rect x="326" y="200" width="62" height="80" class="coral o"/>
<circle cx="357" cy="240" r="58" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="11 9"/>
{hand(200,340,1)}
<path d="M270 340h40" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('persuade', '相手に話して、考えを変えてもらうイラスト。', f"""
{person(160,346,1.15,1,'teal','blue','point','short','neutral')}
{person(450,346,1.1,-1,'coral','gold','stand','bob','smile')}
<g transform="translate(300 200)">
  <path d="M-70-40h140q16 0 16 16v44q0 16-16 16h-90l-26 22 6-22h-30q-16 0-16-16v-44q0-16 16-16z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-40-14h80M-40 8h56"/></g>
</g>
<g class="corals" style="stroke-width:5"><path d="M400 260h-40" marker-end="url(#ar)"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M490 180l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('pin', '紙を壁にピンで留めているイラスト。', f"""
<g transform="translate(300 240) rotate(-6)">
  <path d="M-110-110h220v220h-220z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-60h140M-70-20h140M-70 20h110"/></g>
</g>
<g transform="translate(300 130)">
  <circle r="18" class="coral o"/>
  <path d="M-4 18h8v30h-8z" class="ink"/>
</g>
<path d="M420 130q-40 0-70 10" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('plot', '物語の筋を、山と谷のある線で示したイラスト。', f"""
<path d="M60 340h480" class="a"/>
<path d="M60 300q80-20 130-120t150 60 200-100" fill="none" stroke="{TONES['violet'][0]}" stroke-width="8" stroke-linecap="round"/>
<g fill="{INK}"><circle cx="60" cy="300" r="9"/><circle cx="190" cy="180" r="9"/><circle cx="340" cy="240" r="9"/><circle cx="540" cy="140" r="9"/></g>
""", ground=False)

add('poison', 'どくろ印のついた瓶を示したイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-60-70h120l-10 150h-100z" fill="#e1f3e5" stroke="{INK}" stroke-width="3"/>
  <path d="M-30-90h60v20h-60z" class="ink"/>
  <path d="M-40-20h80v70h-80z" class="paper"/>
  <g transform="translate(0 14)">
    <circle r="18" fill="{INK}"/>
    <g fill="#fffdf6"><circle cx="-7" cy="-4" r="4"/><circle cx="7" cy="-4" r="4"/></g>
    <path d="M-12 18h24v6h-24z" fill="{INK}"/>
  </g>
</g>
<g class="corals" style="stroke-width:7"><path d="M440 160l40 40M480 160l-40 40"/></g>
""", ground=True)

add('pray', '手を合わせて、静かに祈っているイラスト。', f"""
<circle cx="300" cy="140" r="86" class="goldp" opacity=".5"/>
{person(300,346,1.3,1,'violet','blue','hold','bob','neutral')}
<g transform="translate(300 252)">
  <path d="M-8-30q-14 30 0 60M8-30q14 30 0 60" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
</g>
<path d="M254 218h14M332 218h14" class="a"/>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('prefer', '二つのうち、片方を選んで手に取るイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-70-60h140v120h-140z" class="tealp o"/>
</g>
<g transform="translate(430 230)">
  <path d="M-70-60h140v120h-140z" class="muted"/>
</g>
{hand(170,120,1)}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M140 330l18 18 30-36"/></g>
<g class="corals" style="stroke-width:7"><path d="M410 330l30 30M440 330l-30 30"/></g>
""", ground=True)

add('pretend', '面をつけて、別の人のふりをしているイラスト。', f"""
{person(280,346,1.25,1,'violet','blue','hold','short','neutral')}
<g transform="translate(280 232)">
  <ellipse rx="34" ry="40" fill="#fff0c5" stroke="{INK}" stroke-width="3"/>
  <circle cx="-12" cy="-8" r="4" class="ink"/><circle cx="12" cy="-8" r="4" class="ink"/>
  <path d="M-12 16q12 10 24 0" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M34 0h30" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"><circle cx="430" cy="230" r="50"/></g>
<path d="M370 230h-40" class="muted" marker-end="url(#ar)"/>
<path d="M80 366h440" class="a"/>
""", ground=True, arrow=True)

add('prevent', 'さくを立てて、進んでくるものを止めるイラスト。', f"""
<path d="M60 300h480" fill="none" stroke="#e6dcc9" stroke-width="50" stroke-linecap="round"/>
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="11" stroke-linecap="round">
  <path d="M310 200v160M370 200v160M280 240h120M280 300h120"/>
</g>
<path d="M110 260h120" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:8"><path d="M240 220l40 40M280 220l-40 40"/></g>
""", ground=True, arrow=True)

add('procedure', '番号のついた手順を、順に進めていくイラスト。', f"""
<g class="tealp o">
  {''.join(f'<circle cx="{110+i*95}" cy="230" r="42"/>' for i in range(5))}
</g>
<g fill="{INK}">
  {''.join(f'<rect x="{104+i*95}" y="216" width="{10+i*3}" height="28"/>' for i in range(5))}
</g>
<g class="a" marker-end="url(#ar)">{''.join(f'<path d="M{158+i*95} 230h30"/>' for i in range(4))}</g>
<path d="M60 320h480" class="muted"/>
""", ground=False, arrow=True)

add('provide', '必要な物を用意して、相手に渡しているイラスト。', f"""
{person(160,346,1.1,1,'teal','blue','give','short','smile')}
{person(450,346,1.1,-1,'coral','gold','give','bob','smile')}
{box(300,250,110,80,0,'gold')}
<path d="M250 180h100" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('publish', '原稿が本になって、世に出るイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-80-100h160v200h-160z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-56 {-70+i*30}h112"/>' for i in range(6))}</g>
</g>
<g transform="translate(430 250)">
  <path d="M-90-110h180v220h-180z" class="tealp o"/>
  <path d="M-70-110h20v220h-20z" class="teal o"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"><path d="M-30-60h100M-30-30h80"/></g>
</g>
<path d="M270 240h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('punish', '規則を破った人に、罰の札が示されるイラスト。', f"""
{person(200,346,1.15,1,'coral','blue','hold','short','sad')}
{person(440,346,1.1,-1,'blue','violet','point','cap','neutral')}
<g transform="translate(330 220)">
  <path d="M-50-30h100v60h-100z" class="coral o"/>
  <path d="M-6-18h12v22h-6z" fill="#fffdf6"/>
  <circle cy="14" r="5" fill="#fffdf6"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('queue', '順番を待つ人が、一列に並んでいるイラスト。', f"""
{person(150,346,0.9,1,'teal','blue','stand','short','neutral')}
{person(250,346,0.9,1,'coral','gold','stand','bob','neutral')}
{person(350,346,0.9,1,'violet','teal','stand','cap','neutral')}
{person(450,346,0.9,1,'gold','blue','stand','short','neutral')}
<path d="M120 250h380" class="muted"/>
<path d="M100 300h-40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('quit', '机の物を片づけて、職場を去っていくイラスト。', f"""
<g transform="translate(150 260)">
  <path d="M-100-14h200v16h-200z" class="goldp o"/>
  <path d="M-86 2v84M86 2v84" fill="none" stroke="{TONES['gold'][2]}" stroke-width="11" stroke-linecap="round"/>
</g>
{person(340,346,1.05,1,'coral','blue','carry','short','neutral')}
{box(340,276,90,60,0,'gold')}
<path d="M420 240h80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('racism', '肌の色で扱いを分ける、差別の線を示したイラスト。', f"""
{person(180,346,1.05,1,'teal','blue','stand','short','sad')}
<g fill="#8a5a3c" stroke="#5f3d28" stroke-width="2.5"><circle cx="180" cy="238" r="24"/></g>
<path d="M156 226q4-26 26-26 22 0 26 24-14-8-28-2-10-6-24 4z" fill="{HAIR}"/>
{person(430,346,1.05,-1,'coral','gold','point','bob','neutral')}
<path d="M300 130v240" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="16 12"/>
<g class="corals" style="stroke-width:7"><path d="M280 170l40 40M320 170l-40 40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('react', '押されたボタンに応じて、明かりがつくイラスト。', f"""
{hand(160,220,1)}
<g transform="translate(300 250)">
  <path d="M-70-60h140v120h-140z" fill="#dfe6ea" class="o"/>
  <circle r="34" class="coral o"/>
</g>
<g transform="translate(470 230)">
  <circle r="40" class="goldp o"/>
  <path d="M-16 40h32v14h-32z" class="ink"/>
  <g class="golds" style="stroke-width:4"><path d="M0-56v-16M-44-28l-16-10M44-28l16-10"/></g>
</g>
<path d="M240 220h20" class="a" marker-end="url(#ar)"/>
<path d="M380 230h40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('realization', '思い浮かべていた計画が、実物になって完成するイラスト。', f"""
<g transform="translate(160 200)">
  <path d="M-110 40q-14-54 40-66 16-40 76-28 34 6 44 40 56-6 60 44 4 40-46 44h-134q-34-4-30-34z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 8)">{building(0,20,0.4,'teal')}</g>
</g>
{building(430,320,0.9,'teal')}
<path d="M280 220h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('receiver', '受話器を手に取って、耳に当てているイラスト。', f"""
{person(240,346,1.2,1,'teal','blue','hold','bob','neutral')}
<g transform="translate(268 230) rotate(-20)">
  <path d="M-40-14q40-20 80 0 10 16-10 20l-60 4q-20-4-10-24z" class="ink"/>
  <circle cx="-44" cy="-4" r="14" class="ink"/><circle cx="44" cy="-4" r="14" class="ink"/>
</g>
<g transform="translate(450 290)">
  <path d="M-80-40h160v80h-160z" fill="#dfe6ea" class="o"/>
  <g class="ink">{''.join(f'<circle cx="{-50 + (i%3)*40}" cy="{-20 + (i//3)*36}" r="10"/>' for i in range(6))}</g>
</g>
<path d="M340 250h60" fill="none" stroke="{MUTED}" stroke-width="5"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('recommend', '相手におすすめの品を示して、勧めているイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','point','short','smile')}
<g transform="translate(400 250)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <path d="M-50-50h100v100h-100z" class="coralp o"/>
</g>
<g transform="translate(400 130)"><path d="M0-30l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" class="gold o"/></g>
<path d="M250 240h70" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('recover', '病後に体調が戻り、元気になっていくイラスト。', f"""
<g opacity=".5">{person(160,346,1.0,1,'teal','blue','stand','short','sad')}</g>
{person(420,346,1.2,1,'teal','blue','up','short','smile')}
<path d="M240 220h100" class="a" marker-end="url(#ar)"/>
<g class="greens" style="stroke-width:4"><path d="M500 220l24-24M330 300h-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('reduce', '同じ器の中身が、だんだん減っていくイラスト。', f"""
<g transform="translate(140 280)">
  <path d="M-50-90h100l-8 150h-84z" fill="#f7fbfe" class="o"/>
  <path d="M-49-70h98l-7 130h-84z" class="bluep o"/>
</g>
<g transform="translate(300 280)">
  <path d="M-50-90h100l-8 150h-84z" fill="#f7fbfe" class="o"/>
  <path d="M-46-20h92l-6 80h-80z" class="bluep o"/>
</g>
<g transform="translate(460 280)">
  <path d="M-50-90h100l-8 150h-84z" fill="#f7fbfe" class="o"/>
  <path d="M-42 30h84l-4 30h-76z" class="bluep o"/>
</g>
<path d="M100 150h400" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('refund', '返品して、支払ったお金が戻ってくるイラスト。', f"""
{person(160,346,1.1,1,'coral','blue','give','bob','neutral')}
{person(450,346,1.1,-1,'teal','violet','give','short','smile')}
{box(250,220,70,50,0,'gold')}
<g transform="translate(360 290)">
  <path d="M-40-20h80v40h-80z" class="greenp o"/>
  <circle r="10" class="green o"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="4">
  <path d="M300 180q60-20 90 20" marker-end="url(#ar)"/>
  <path d="M300 320q-60 20-90-20" marker-end="url(#ar)"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('refuse', '差し出された物を、手で断って受け取らないイラスト。', f"""
{person(430,346,1.15,-1,'teal','blue','give','bob','neutral')}
{box(320,250,70,50,0,'gold')}
{hand(200,250,-1)}
<g class="corals" style="stroke-width:8"><path d="M240 180l40 40M280 180l-40 40"/></g>
<path d="M270 320h-40" class="a" marker-end="url(#ar)" transform="rotate(180 250 320)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('register', '名簿に名前を書き入れて、登録しているイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-150-120h300v240h-300z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-110 {-80+i*40}h220"/>' for i in range(5))}</g>
  <g fill="{INK}"><rect x="-100" y="-96" width="70" height="8"/><rect x="-100" y="-56" width="90" height="8"/></g>
</g>
{hand(160,180,1)}
<path d="M230 200h30" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('regret', '過去の選択を思い返して、悔やんでいるイラスト。', f"""
{person(190,346,1.2,1,'violet','blue','think','short','sad')}
<g transform="translate(410 200)">
  <path d="M-110-70h220v140h-220z" class="paper" opacity=".8"/>
  <g class="corals" style="stroke-width:7"><path d="M-30-30l60 60M30-30l-60 60"/></g>
</g>
<path d="M300 240h-40" class="muted" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('rely', 'つえに体重をかけて、頼って歩いているイラスト。', f"""
{person(260,346,1.2,1,'teal','blue','point','short','neutral')}
<path d="M340 250v110" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
<path d="M340 250q20-20 40-10" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
<g class="a" marker-end="url(#ar)"><path d="M420 250v70"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('remain', '多くが去ったあと、一つだけその場に残るイラスト。', f"""
<g opacity=".25">{box(150,300,80,60,0,'gold')}{box(260,300,80,60,0,'gold')}</g>
{box(420,300,80,60,0,'gold')}
<g class="muted" marker-end="url(#ar)"><path d="M180 200h-100M290 200h-100"/></g>
<circle cx="420" cy="300" r="66" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('point', '指を伸ばして、ある一点を差し示しているイラスト。', f"""
{person(190,346,1.2,1,'teal','blue','point','short','neutral')}
<circle cx="300" cy="230" r="15" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="10 8"><path d="M330 226h130" marker-end="url(#ar)"/></g>
<circle cx="490" cy="222" r="20" class="coral o"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('ought', 'すべきことを示す矢印が、正しい道を指しているイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','stand','short','neutral')}
<path d="M270 230h140" class="a" marker-end="url(#ar)" style="stroke-width:7"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M440 220l20 20 34-40"/></g>
<path d="M270 320h140" class="muted" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:7"><path d="M440 300l30 30M470 300l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('placement', '実習先の職場に、配置されて働き始めるイラスト。', f"""
{building(440,300,0.9,'teal')}
{person(170,346,1.05,1,'coral','blue','walk','short','smile')}
<g transform="translate(280 250)">
  <path d="M-44-30h88v60h-88z" class="paper"/>
  <circle cx="-18" cy="-6" r="12" class="tealp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M4-10h30M4 4h24"/></g>
</g>
<path d="M340 200h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(' '.join(W)); print(sheet(W))
