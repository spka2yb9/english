"""第61回: 世代・本物・見出し・免疫など42語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('furious', '顔を真っ赤にして激しく怒るイラスト。', f"""
{face(270,200,100,'flat')}
<g fill="none" stroke="{INK}" stroke-width="8"><path d="M210 148l46 18M330 148l-46 18"/></g>
<g transform="translate(270 250)"><ellipse rx="34" ry="24" fill="#8b4a3e"/></g>
<circle cx="180" cy="234" r="26" class="coralp"/><circle cx="360" cy="234" r="26" class="coralp"/>
<g class="corals" opacity=".9" style="stroke-width:6"><path d="M410 130q30 30 30 60t-30 60M460 110q40 44 40 80t-40 80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('generation', '祖父・親・子と世代が続くイラスト。', f"""
{person(150,346,1.15,1,'violet','blue','stand','short','smile')}
{person(300,346,1.2,1,'teal','blue','stand','bob','smile')}
{person(440,346,0.8,1,'coral','gold','stand','cap','smile')}
<g class="a" marker-end="url(#ar)"><path d="M200 180h60M350 180h50"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('generic', '銘柄の印がない、ふつうの品のイラスト。', f"""
<g transform="translate(170 250)">
  {box(170,250,140,110,26,'teal')}
</g>
<g transform="translate(430 250)">
  <path d="M-70-60h140v130h-140z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-40-20h80M-40 0h60"/></g>
</g>
<path d="M300 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('genetic', '二重らせんの遺伝子を示したイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-60-160q120 80 0 160t0 160" fill="none" stroke="{TONES['teal'][0]}" stroke-width="12"/>
  <path d="M60-160q-120 80 0 160t0 160" fill="none" stroke="{TONES['coral'][0]}" stroke-width="12"/>
  <g fill="none" stroke="{MUTED}" stroke-width="6">{''.join(f'<path d="M-40 {-130+i*44}h80"/>' for i in range(7))}</g>
</g>
""", ground=False)

add('gentleman', '帽子をとって礼を示す紳士のイラスト。', f"""
<g transform="translate(250 346) rotate(14)">{person(0,0,1.3,1,'blue','blue','give','short','smile')}</g>
<g transform="translate(390 190)">
  <path d="M-46-10h92v14h-92z" class="ink"/>
  <path d="M-30-60h60v50h-60z" class="ink"/>
</g>
<g transform="translate(250 240)"><path d="M-14-10h28v10h-28z" class="coral o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('genuine', '刻印のある本物と、印のない偽物を比べたイラスト。', f"""
<g transform="translate(170 240)">
  <circle r="80" class="goldd o"/>
  <circle r="60" fill="#e5b56b" stroke="{INK}" stroke-width="3"/>
  <path d="M0-26l8 16 18 2-13 13 3 18-16-9-16 9 3-18-13-13 18-2z" class="ink"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M50-110l20 20 34-40"/></g>
</g>
<g transform="translate(430 240)">
  <circle r="80" fill="#cfc9a8" stroke="{INK}" stroke-width="3"/>
  <circle r="60" fill="#ddd7bb" stroke="{INK}" stroke-width="2"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M50-110l30 30M80-110l-30 30"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('ghost', '白い布のような姿で浮かぶ幽霊のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#2b3a52"/>
<g transform="translate(300 210)">
  <path d="M-90 120q-10-60-10-100 0-100 100-100t100 100q0 40-10 100l-30-26-30 26-30-26-30 26z" fill="#f2f6fa" opacity=".92"/>
  <g fill="{INK}"><ellipse cx="-30" cy="-30" rx="10" ry="14"/><ellipse cx="30" cy="-30" rx="10" ry="14"/></g>
  <ellipse cy="10" rx="16" ry="12" fill="{INK}"/>
</g>
<g fill="#fdf6e0"><circle cx="90" cy="100" r="4"/><circle cx="520" cy="140" r="4"/></g>
""", ground=False)

add('giant', '人の何倍もある巨大なもののイラスト。', f"""
<g transform="translate(380 230)">
  <path d="M-120-160h240v320h-240z" class="teal o"/>
</g>
{person(140,346,1.0,1,'coral','blue','up','short','surprised')}
<g class="a" marker-end="url(#ar)"><path d="M180 70h80"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M120 70h140"/></g>
<path d="M60 396h480" class="a"/>
""", ground=True, arrow=True)

add('glorious', '朝日が輝いて、見事に晴れたイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#fdf3dc"/>
{sun(300,150,60)}
<g fill="#f7e6bd" opacity=".6"><path d="M300 150L60 400h480z"/></g>
<g class="green o" opacity=".85"><path d="M0 340q150-50 300-20t300-10v90H0z"/></g>
{person(150,340,1.0,1,'coral','blue','up','short','smile')}
""", ground=False)

add('go', 'その場を離れて出発するイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','walk','short','smile')}
<g opacity=".3">{person(120,346,1.0,1,'teal','blue','stand','short','neutral')}</g>
<path d="M290 250h200" class="a" marker-end="url(#ar)"/>
<g transform="translate(520 300)"><path d="M-40 46h80V-20h-80z" fill="#f4ead2" class="o"/><path d="M-54-20l54-40 54 40z" class="coral o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('golden', '金色に輝く器のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-90-90h180l-20 120a70 40 0 0 1-140 0z" class="gold o"/>
  <path d="M-40 60h80v40h-80z" class="goldd o"/>
  <path d="M-80 100h160v24h-160z" class="goldd o"/>
  <path d="M-60-70q30 30 0 60" fill="none" stroke="#fffdf6" stroke-width="10" opacity=".7"/>
</g>
<g class="golds" style="stroke-width:6"><path d="M160 130l-26-20M440 130l26-20M300 110V80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('goods', '売り物の品が箱で積まれたイラスト。', f"""
{box(180,300,150,110,30,'teal')}
{box(180,180,150,110,30,'teal')}
{box(400,300,150,110,30,'gold')}
<g transform="translate(400 200)">
  <path d="M-60-40h120l20 30-20 30h-120z" class="coral o"/>
  <g fill="#fffdf6"><rect x="-40" y="-10" width="70" height="16"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('gorgeous', '飾り立てた豪華な広間のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-140h440v280h-440z" fill="#f4ead2" class="o"/>
  <path d="M-220-140h440v-24h-440z" class="goldd o"/>
  <g class="goldp o"><rect x="-190" y="-100" width="60" height="240"/><rect x="130" y="-100" width="60" height="240"/></g>
  <g transform="translate(0 -60)"><path d="M-60 0h120l-20 40h-80z" class="gold o"/><path d="M-6-70h12v70h-12z" class="goldd o"/></g>
  <path d="M-80 60h160v80h-160z" class="coralp o"/>
</g>
<g class="golds" style="stroke-width:5"><path d="M140 130l-24-18M460 130l24-18"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('grain', '穂と、こぼれた粒の穀物のイラスト。', f"""
<g transform="translate(200 260)">
  <path d="M0 100V-40" fill="none" stroke="{TONES['gold'][2]}" stroke-width="6"/>
  <g class="gold o">{''.join(f'<ellipse cx="{-16 if i%2 else 16}" cy="{-40-i*22}" rx="16" ry="10" transform="rotate({-25 if i%2 else 25} {-16 if i%2 else 16} {-40-i*22})"/>' for i in range(5))}</g>
</g>
<g class="gold o"><ellipse cx="400" cy="340" rx="16" ry="10"/><ellipse cx="440" cy="330" rx="16" ry="10" transform="rotate(20 440 330)"/><ellipse cx="470" cy="345" rx="16" ry="10" transform="rotate(-15 470 345)"/><ellipse cx="420" cy="356" rx="16" ry="10"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('grand', '見上げるほど壮大な建物のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-200 110h400v-180h-400z" fill="#f4ead2" class="o"/>
  <path d="M-230-70l230-120 230 120z" class="teal o"/>
  <g class="goldp o"><rect x="-170" y="-30" width="60" height="140"/><rect x="-80" y="-30" width="60" height="140"/><rect x="20" y="-30" width="60" height="140"/><rect x="110" y="-30" width="60" height="140"/></g>
</g>
{person(120,346,0.6,1,'coral','blue','up','short','surprised')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('grant', '正式に認めて、助成の書面を渡すイラスト。', f"""
{person(150,346,1.1,1,'blue','blue','give','short','smile')}
<g transform="translate(320 240)">
  <path d="M-90-60h180v120h-180z" class="paper"/>
  <g fill="{INK}"><rect x="-60" y="-30" width="80" height="14"/></g>
  <g transform="translate(50 20)"><circle r="24" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/><path d="M-12 0l10 10 16-18" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round"/></g>
</g>
{person(480,346,1.1,-1,'teal','gold','reach','bob','smile')}
<path d="M240 300h140" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('graphic', '数字を図に起こしたグラフのイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-140h380v280h-380z" fill="#f7fbfe" class="o"/>
  <path d="M-150 100h340M-150-110v210" fill="none" stroke="{INK}" stroke-width="4"/>
  <g fill="{TONES['teal'][0]}"><rect x="-120" y="20" width="50" height="80"/><rect x="-50" y="-30" width="50" height="130"/><rect x="20" y="-80" width="50" height="180"/><rect x="90" y="-50" width="50" height="150"/></g>
</g>
""", ground=True)

add('greeting', '手を挙げてあいさつを交わすイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','up','short','smile')}
{person(400,346,1.2,-1,'coral','gold','up','bob','smile')}
<g transform="translate(300 160)">
  <path d="M-70-40h140v60h-140z" fill="#fffdf6" class="o"/>
  <path d="M-30 20l-14 26 34-26z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-50" y="-20" width="100" height="14"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('gross', 'すべてを合わせた総計を示すイラスト。', f"""
<g class="tealp o"><rect x="90" y="240" width="70" height="80"/><rect x="170" y="220" width="70" height="100"/><rect x="250" y="260" width="70" height="60"/></g>
<g transform="translate(450 230)">
  <path d="M-70-90h140v180h-140z" class="teal o"/>
  <g fill="#fffdf6"><rect x="-40" y="-30" width="80" height="20"/><rect x="-40" y="10" width="80" height="20"/></g>
</g>
<path d="M340 260h40" class="a" marker-end="url(#ar)"/>
<g fill="{INK}" transform="translate(200 170)"><rect x="-24" y="-6" width="48" height="12"/><rect x="-6" y="-24" width="12" height="48"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('half', '一つを二等分した片方を示したイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="130" fill="#fffdf6" class="o"/>
  <path d="M0-130A130 130 0 0 1 0 130z" class="coral o"/>
  <path d="M0-130v260" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
<path d="M480 210h-60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('happily', 'にこにこ笑いながら歩くイラスト。', f"""
{person(280,346,1.35,1,'coral','gold','walk','bob','smile')}
<g class="golds" style="stroke-width:5"><path d="M170 190l-26-20M180 230h-30M400 190l26-20M410 230h30"/></g>
<g fill="{TONES['coral'][1]}"><circle cx="220" cy="230" r="14"/><circle cx="330" cy="230" r="14"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('happiness', '笑顔とハートで満たされた幸福のイラスト。', f"""
{face(220,200,90,'smile')}
<g transform="translate(420 210)">
  <path d="M0 60c-56-42-76-60-76-92a40 40 0 0 1 76-22 40 40 0 0 1 76 22c0 32-20 50-76 92z" class="coral o"/>
</g>
<g class="golds" style="stroke-width:5"><path d="M320 140l26-20M330 180h30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('harmful', 'その煙が体に悪くはたらくイラスト。', f"""
<g transform="translate(180 300)">
  <path d="M-60 60h120l-14-100h-92z" fill="#8b8161" stroke="{INK}" stroke-width="3"/>
  <g class="muted" opacity=".9"><path d="M-20-50q20-40 0-70M20-50q20-40 0-70"/></g>
</g>
{person(440,346,1.15,-1,'coral','gold','stand','bob','sad')}
<path d="M270 220h80" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M500 170l30 30M530 170l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('hate', '差し出されたものを、嫌って突き返すイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-60-40h120v80h-120z" fill="#8b8161" stroke="{INK}" stroke-width="3"/>
</g>
{person(150,346,1.15,1,'teal','blue','give','short','neutral')}
{person(460,346,1.25,-1,'coral','gold','point','bob','flat')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"><path d="M360 170l40 40M400 170l-40 40"/></g>
<path d="M400 300h-60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('headline', '新聞の一面に大きく出る見出しのイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-150h400v300h-400z" class="paper"/>
  <g fill="{INK}"><rect x="-160" y="-120" width="320" height="34"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-160 {-50+i*34}h150"/>' for i in range(6))}</g>
  <g class="tealp o"><rect x="20" y="-50" width="140" height="120"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="130" y="90" width="340" height="50"/></g>
<path d="M520 115h-40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('heating', '暖房の器から暖かさが出るイラスト。', f"""
<g transform="translate(240 260)">
  <path d="M-110-70h220v140h-220z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="6">{''.join(f'<path d="M{-80+i*40}-50v120"/>' for i in range(5))}</g>
</g>
<g class="corals" opacity=".9" style="stroke-width:5"><path d="M380 240q26-26 0-52M420 260q26-26 0-52M460 240q26-26 0-52"/></g>
{thermometer(520,260,0.8,0.9)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('helicopter', '回転翼で飛ぶヘリコプターのイラスト。', f"""
<g transform="translate(300 230)">
  <ellipse rx="90" ry="60" class="tealp o"/>
  <path d="M70-10h140v24H70z" class="tealp o"/>
  <path d="M190-40h16v60h-16z" class="tealp o"/>
  <path d="M-40-20h60v40h-60z" fill="#e8f4fb" stroke="{INK}" stroke-width="3"/>
  <path d="M-6-100h12v40h-12z" class="ink"/>
  <path d="M-200-108h400v14h-400z" class="ink"/>
  <path d="M-60 60h120v14h-120z" class="ink"/>
</g>
<g class="muted"><path d="M120 100q40-20 60 0M420 100q40-20 60 0"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('hidden', '布の下に隠れて見えないイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-120 90q0-160 120-160t120 160z" fill="#dfe6ea" class="o"/>
  <g opacity=".25"><circle cy="20" r="50" class="teal o"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="300" cy="270" r="70"/></g>
<g transform="translate(480 150)">
  <ellipse rx="46" ry="30" fill="#fffdf6" class="o"/>
  <circle r="14" class="ink"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"><path d="M-50-30l100 60"/></g>
</g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('highlight', '大事な一行に色をかぶせて目立たせるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-140 {-90+i*45}h280"/>' for i in range(5))}</g>
  <path d="M-146-20h292v40h-292z" class="goldp o" opacity=".85"/>
</g>
<g transform="translate(500 300) rotate(28)"><path d="M-14-80h28v100h-28z" class="gold o"/><path d="M-14 20h28l-14 24z" class="ink"/></g>
""", ground=True)

add('hilarious', 'おかしくて笑い転げるイラスト。', f"""
<g transform="translate(220 346) rotate(-18)">{person(0,0,1.3,1,'coral','gold','up','bob','smile')}</g>
<g fill="none" stroke="{INK}" stroke-width="5"><path d="M170 210q16-16 32 0M216 206q16-16 32 0"/></g>
{drop(300,200,0.7)}
<g class="golds" style="stroke-width:6"><path d="M400 180l26-20M410 220h30M400 260l26 20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('holy', '光を放つ聖なる書のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#f6f0dc"/>
<g fill="#f7e6bd" opacity=".7"><circle cx="300" cy="220" r="170"/></g>
<g transform="translate(300 230)">
  <path d="M-140-100h280v200h-280z" class="violet o"/>
  <path d="M-120-80h240v160h-240z" fill="#fffdf6" class="o"/>
  <g fill="{TONES['gold'][2]}"><rect x="-10" y="-50" width="20" height="100"/><rect x="-50" y="-20" width="100" height="20"/></g>
</g>
<g fill="none" stroke="#d9c286" stroke-width="5"><circle cx="300" cy="110" r="0"/></g>
""", ground=False)

add('hopeful', '暗がりの先に明かりを見て、希望をもつイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#3b4a63"/>
{person(180,346,1.2,1,'teal','blue','up','short','smile')}
<g transform="translate(450 200)">
  <circle r="60" fill="#f7e6bd"/>
  <g opacity=".4" fill="#f7e6bd"><circle r="100"/></g>
</g>
<path d="M260 250h100" fill="none" stroke="#f7e6bd" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('hostile', 'にらみつけて、敵意を向けるイラスト。', f"""
{person(190,346,1.2,1,'violet','blue','point','short','flat')}
{person(430,346,1.2,-1,'teal','gold','stand','bob','sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M270 200h80M280 250h70"/></g>
<g class="corals" style="stroke-width:5"><path d="M130 180q-24 16-24 40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('humble', '腰を低くして、へりくだるイラスト。', f"""
<g transform="translate(230 346) rotate(28)">{person(0,0,1.2,1,'teal','gold','stand','short','smile')}</g>
{person(450,346,1.3,-1,'blue','blue','stand','bob','neutral')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M110 190l18 18 30-36"/></g>
<path d="M320 260h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('humor', '笑いを誘う話で、その場がほどけるイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','point','short','smile')}
<g transform="translate(340 170)">
  <path d="M-80-50h160v80h-160z" fill="#fffdf6" class="o"/>
  <path d="M-40 30l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{INK}" stroke-width="5"><path d="M-40-20q20 20 40 0M10-20q20 20 40 0"/></g>
</g>
{person(480,346,1.15,-1,'coral','gold','up','bob','smile')}
<g class="golds" style="stroke-width:5"><path d="M420 250l26-20M430 290h30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('humorous', '冗談を言って、まわりを笑わせるイラスト。', f"""
{person(200,346,1.25,1,'gold','blue','up','short','smile')}
<g transform="translate(200 180)">
  <path d="M-44-24h88v20h-88z" class="coralp o"/>
  <circle cx="0" cy="-40" r="16" class="coral o"/>
</g>
{face(430,200,70,'smile')}
<g fill="none" stroke="{INK}" stroke-width="4"><path d="M400 190q14-12 28 0M436 186q14-12 28 0"/></g>
<path d="M290 220h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('hurricane', '渦を巻いて吹き荒れる大あらしのイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#5b6b80"/>
<g fill="none" stroke="#cfd8e0" stroke-width="16" stroke-linecap="round">
  <path d="M300 210q-120-60-40-120 60-44 120 10"/>
  <path d="M300 210q120 60 40 120-60 44-120-10"/>
  <path d="M300 210q-60-90 40-70M300 210q60 90-40 70"/>
</g>
<circle cx="300" cy="210" r="26" fill="#41506a"/>
<g fill="none" stroke="#cfd8e0" stroke-width="4"><path d="M70 340q40-20 80 0M450 340q40-20 80 0"/></g>
""", ground=False)

add('identical', '寸分たがわず同じ形が二つ並ぶイラスト。', f"""
<g transform="translate(180 230)"><path d="M-80-80h160v160h-160z" class="teal o"/><circle r="40" fill="#fffdf6"/></g>
<g transform="translate(430 230)"><path d="M-80-80h160v160h-160z" class="teal o"/><circle r="40" fill="#fffdf6"/></g>
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M290 210h40M290 250h40"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('identity', '身分証で、その人が誰かを示すイラスト。', f"""
<g transform="translate(320 230)">
  <path d="M-160-110h320v220h-320z" class="paper"/>
  <g transform="translate(-90 -10)">
    <circle r="54" class="tealp o"/>
    <circle cy="-16" r="20" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <path d="M-32 40q0-30 32-30t32 30z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  </g>
  <g fill="{INK}"><rect x="0" y="-70" width="120" height="18"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M0-20h120M0 20h100"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('ideological', '相反する二つの考えが向かい合うイラスト。', f"""
<g transform="translate(160 230)">
  <path d="M-90-90h180v180h-180z" class="tealp o"/>
  <g fill="{TONES['teal'][2]}"><rect x="-50" y="-10" width="100" height="20"/></g>
</g>
<g transform="translate(440 230)">
  <path d="M-90-90h180v180h-180z" class="coralp o"/>
  <g fill="{TONES['coral'][2]}"><rect x="-10" y="-50" width="20" height="100"/><rect x="-50" y="-10" width="100" height="20"/></g>
</g>
<g fill="none" stroke="{INK}" stroke-width="5" marker-end="url(#ar)"><path d="M270 230h40M330 230h-40"/></g>
""", ground=False, arrow=True)

add('image', '画面に映った一枚の像のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-140h380v280h-380z" fill="#dfe6ea" class="o"/>
  <path d="M-160-110h320v220h-320z" fill="#fffdf6" class="o"/>
  <path d="M-130 90l90-110 60 60 70-90 90 140z" class="green o"/>
  {sun(0,-60,26)}
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('imagination', '頭の中に、ないものを思い描くイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','think','short','smile')}
<g transform="translate(420 190)">
  <path d="M-130-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-166q-38-4-26-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="9 8"><path d="M-60 20l50-70 40 40 40-50 30 80z"/></g>
  <g class="violetp o"><circle cx="60" cy="-40" r="18"/></g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="280" cy="290" r="12"/><circle cx="256" cy="314" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('imaginative', 'ありふれた形から、思いがけない絵を作るイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-60-60h120v120h-120z" class="tealp o"/>
</g>
<g transform="translate(430 240)">
  <path d="M-90-70h180v140h-180z" fill="#fffdf6" class="o"/>
  <path d="M-60 50l40-70 30 30 40-50 40 90z" class="violetp o"/>
  <g class="gold o"><circle cx="50" cy="-40" r="18"/></g>
  <g class="golds" style="stroke-width:4"><path d="M-70-50l-20-16"/></g>
</g>
<path d="M260 240h60" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('immature', 'まだ実が青くて、熟していないイラスト。', f"""
<g transform="translate(180 250)">
  <circle r="70" class="green o"/>
  <path d="M0-70v-30" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
</g>
<g transform="translate(430 250)">
  <circle r="70" class="coral o"/>
  <path d="M0-70v-30" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
</g>
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M120 150l30 30M150 150l-30 30"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('immense', '人が小さく見えるほど、計り知れない大きさのイラスト。', f"""
<g fill="#b9c8d6"><path d="M300 60l260 300H40z"/></g>
<g fill="#a8bacb"><path d="M300 60l100 300h-200z"/></g>
{person(100,346,0.7,1,'coral','blue','up','short','surprised')}
<g class="a" marker-end="url(#ar)"><path d="M540 340V90"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('imminent', '雲がすぐ頭上まで迫っているイラスト。', f"""
{cloud(300,120,1.8)}
{person(300,346,1.15,1,'teal','blue','up','short','surprised')}
<path d="M300 190v40" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">{''.join(f'<path d="M{200+i*40} 200l-10 26"/>' for i in range(6))}</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('immune', '盾がはたらいて、病がはね返されるイラスト。', f"""
{person(180,346,1.2,1,'teal','blue','carry','short','smile')}
<g transform="translate(280 240)">
  <path d="M0-80q56 22 56 66 0 56-56 78-56-22-56-78 0-44 56-66z" fill="#cfe6d6" stroke="{TONES['green'][2]}" stroke-width="4"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M-20 10l14 16 28-34"/></g>
</g>
<g transform="translate(470 230)">
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="5">{''.join(f'<path d="M0 0L{int(50*__import__("math").cos(i*3.14159/4))} {int(50*__import__("math").sin(i*3.14159/4))}"/>' for i in range(8))}</g>
  <circle r="26" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M400 200h-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
