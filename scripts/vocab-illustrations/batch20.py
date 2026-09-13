"""第20回: 明暗・破損・計算・追跡など30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('auto', '一台の自動車を横から見たイラスト。', f"""
<circle cx="470" cy="96" r="54" class="coralp"/>
<g transform="translate(300 270)">
  <path d="M-180 50h360l-20-70h-60l-40-66h-140l-40 66h-74z" class="coral o"/>
  <path d="M-130-20h96v-52h-70zM-14-72h88l32 52H-14z" class="bluep o"/>
  <circle cx="-100" cy="58" r="36" class="ink"/><circle cx="100" cy="58" r="36" class="ink"/>
  <circle cx="-100" cy="58" r="14" fill="#dfe6ea"/><circle cx="100" cy="58" r="14" fill="#dfe6ea"/>
</g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('awful', '腐った料理を前にして、顔をしかめているイラスト。', f"""
{person(200,346,1.2,1,'coral','blue','hold','short','sad')}
<g transform="translate(410 300)">
  <ellipse rx="80" ry="28" fill="#fffdf6" class="o"/>
  <g fill="#9aa88f" stroke="{INK}" stroke-width="2.5"><circle cx="-24" cy="-14" r="20"/><circle cx="14" cy="-8" r="20"/></g>
  <g class="muted"><path d="M-20-44q-14-30 4-52M22-40q-14-34 6-56"/></g>
</g>
<g class="corals" style="stroke-width:6"><path d="M290 200l-26-26M264 200l26-26"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('back', '人物の後ろ姿を、正面の姿と並べて示したイラスト。', f"""
{person(190,346,1.2,1,'teal','blue','stand','short','smile')}
<g transform="translate(410 346)">
  <path d="M-12-8l-7 35M12-8l7 35" fill="none" stroke="{TONES['blue'][2]}" stroke-width="13" stroke-linecap="round"/>
  <path d="M-30-94q30-16 60 0l-10 86h-40z" class="teal o"/>
  <path d="M-26-84l-20 54M26-84l20 54" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
  <circle cx="0" cy="-130" r="29" fill="{HAIR}"/>
</g>
<path d="M300 130v220" class="muted"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('balloon', 'ひもの付いた風船が、空へ浮かんでいるイラスト。', f"""
<g transform="translate(300 180)">
  <ellipse rx="90" ry="106" class="coralp o"/>
  <path d="M0 106l-16 26h32z" class="coral o"/>
  <path d="M0 132q30 60 0 120q-30 60 0 88" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M-40-40q20-30 46-30" fill="none" stroke="#ffffff" stroke-width="8" stroke-linecap="round" opacity=".8"/>
</g>
<path d="M420 200v-60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('base', '建物の土台となる基礎の部分を示したイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-120-120h240v180h-240z" fill="#fffdf6" class="o"/>
  <path d="M-136-120L0-200l136 80z" class="teal o"/>
  <g class="bluep o"><rect x="-80" y="-90" width="60" height="50"/><rect x="20" y="-90" width="60" height="50"/></g>
</g>
<path d="M140 300h320v50H140z" class="goldd o"/>
<path d="M140 300h320" class="a"/>
<path d="M480 326h60" class="a" marker-end="url(#ar)" transform="rotate(180 510 326)"/>
""", ground=True, arrow=True)

add('based', '土台の上に、その上の部分が乗って支えられているイラスト。', f"""
<path d="M120 320h360v50H120z" class="goldd o"/>
<g transform="translate(300 250)">
  <path d="M-110-60h220v120h-220z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"><path d="M-110 0h220M0-60v120"/></g>
</g>
<path d="M540 300v40" class="a" marker-end="url(#ar)" transform="rotate(180 540 320)"/>
<path d="M60 370h480" class="a"/>
""", ground=True, arrow=True)

add('bomb', '落下してきた爆弾が、地上で大きく爆発するイラスト。', f"""
<g transform="translate(180 150) rotate(20)">
  <ellipse rx="34" ry="46" class="ink"/>
  <path d="M0-46v-20" class="a"/>
  <path d="M-20 46l-14 24h68l-14-24z" class="ink"/>
</g>
<g transform="translate(400 280)">
  <path d="M-140 0l60-30-30-56 70 24 24-70 30 68 62-30-20 60 74 12-60 40 44 46-70-6-10 62-44-52-52 42 10-62z" class="coral o"/>
  <path d="M-70 0l36-16-16-32 40 14 14-40 18 40 34-16-12 34 42 8-34 22 26 26-40-4-6 36-26-30-30 24 6-36z" class="goldp o"/>
</g>
<path d="M230 200q60 20 110 50" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('breakthrough', '行き止まりの壁を破って、向こう側へ進み出るイラスト。', f"""
<g transform="translate(320 240)">
  <path d="M-60-140h60v90l-40 30 40 30v90h-60z" class="goldp o"/>
  <path d="M60-140h60v280H60v-90l40-30-40-30z" class="goldp o"/>
</g>
<path d="M120 240h130" class="a" marker-end="url(#ar)"/>
<path d="M400 240h100" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:5"><path d="M300 140l-20-30M340 140l20-30M300 340l-20 30M340 340l20 30"/></g>
""", ground=True, arrow=True)

add('breathe', '胸をふくらませて息を吸い、空気が出入りしているイラスト。', f"""
{person(240,346,1.3,1,'teal','blue','stand','short','neutral')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-dasharray="12 8">
  <path d="M330 220q60-30 120-20" marker-end="url(#ar)"/>
  <path d="M450 270q-60 20-120 10" marker-end="url(#ar)"/>
</g>
<g transform="translate(240 268)">
  <ellipse rx="46" ry="34" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('bright', '強い光を放つ電球が、周りを明るく照らしているイラスト。', f"""
<circle cx="300" cy="200" r="150" class="goldp" opacity=".55"/>
<g transform="translate(300 190)">
  <circle r="60" class="gold o"/>
  <path d="M-24 60h48v22h-48z" class="ink"/>
  <path d="M-18 82h36v14h-36z" class="ink"/>
</g>
<g class="golds" style="stroke-width:5">
  <path d="M300 90V50M180 150l-34-24M420 150l34-24M170 250h-40M430 250h40M300 320v40"/>
</g>
""", ground=False)

add('broken', 'ひもが切れて、二つに分かれてしまったイラスト。', f"""
<circle cx="470" cy="96" r="54" class="coralp"/>
<path d="M60 220q80-30 160 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="18" stroke-linecap="round"/>
<path d="M380 220q80-30 160 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="18" stroke-linecap="round"/>
<path d="M220 215l30 10-30 10z" class="coral"/>
<path d="M380 215l-30 10 30 10z" class="coral"/>
<g class="corals" style="stroke-width:5"><path d="M300 160v-30M262 176l-24-24M338 176l24-24"/></g>
<path d="M60 330h480" class="a"/>
""", ground=True)

add('bug', '画面のプログラムに紛れ込んだ不具合の虫のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-170-130h340v260h-340z" fill="#dfe6ea" class="o"/>
  <path d="M-140-100h280v200h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M-110 {-70+i*30}h{140 - (i%3)*40}"/>' for i in range(6))}
  </g>
</g>
<g transform="translate(360 260) scale(0.6)">
  <ellipse cy="40" rx="50" ry="66" class="coral o"/>
  <circle cy="-30" r="30" class="coralp o"/>
  <g fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"><path d="M-40 20l-60-20M40 20l60-20M-40 70l-60 30M40 70l60 30"/></g>
  <path d="M-12-54q-20-30-40-34M12-54q20-30 40-34" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
</g>
""", ground=True)

add('bush', '背の低い木がこんもりと茂った茂みのイラスト。', f"""
<g transform="translate(280 300)">
  <circle cx="-70" cy="-20" r="52" class="greenp o"/>
  <circle cx="0" cy="-46" r="62" class="greenp o"/>
  <circle cx="70" cy="-16" r="50" class="greenp o"/>
  <path d="M-120 0h240" class="a"/>
</g>
{tree(480,300,0.8)}
<path d="M60 300h480" class="a"/>
""", ground=True)

add('calculate', '数式を書いて、電卓で答えを出しているイラスト。', f"""
<g transform="translate(200 230)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <g fill="{INK}"><rect x="-60" y="-50" width="40" height="8"/><rect x="-10" y="-54" width="8" height="16"/><rect x="-14" y="-50" width="16" height="8"/><rect x="20" y="-50" width="40" height="8"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60 0h120M-60 30h100"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-80-110h160v220h-160z" fill="#dfe6ea" class="o"/>
  <path d="M-60-90h120v50h-120z" class="tealp o"/>
  <g class="ink">
    {''.join(f'<rect x="{-56 + (i%3)*40}" y="{-20 + (i//3)*40}" width="28" height="28" rx="5"/>' for i in range(9))}
  </g>
</g>
<path d="M310 220h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('cancel', '予定表の項目に線を引いて、取り消しているイラスト。', f"""
<g transform="translate(280 230)">
  <path d="M-140-140h280v280h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-100-90h200M-100-30h200M-100 30h200M-100 90h160"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M-110-30h220"/></g>
</g>
<g class="corals" style="stroke-width:8"><path d="M440 170l40 40M480 170l-40 40"/></g>
""", ground=True)

add('careful', '割れやすい品を、両手でそっと運んでいるイラスト。', f"""
<circle cx="470" cy="96" r="54" class="greenp"/>
{person(280,346,1.25,1,'teal','blue','carry','short','neutral')}
<g transform="translate(280 258)">
  <path d="M-50-40h100l-14 76h-72z" fill="#fffdf6" class="o"/>
  <path d="M-50-40h100" class="a"/>
</g>
<g fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"><circle cx="210" cy="286" r="15"/><circle cx="350" cy="286" r="15"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="4" stroke-dasharray="9 8"><circle cx="280" cy="250" r="76"/></g>
<path d="M80 366h420" class="a"/>
""", ground=True)

add('carriage', '連結された客車が、線路の上に並んでいるイラスト。', f"""
<path d="M0 330h600v40H0z" fill="#d8d3ca"/>
<g fill="none" stroke="{INK}" stroke-width="4"><path d="M0 336h600M0 356h600"/></g>
<g transform="translate(180 270)">
  <path d="M-140-60h280v100h-280z" class="tealp o"/>
  <g class="bluep o"><rect x="-110" y="-40" width="60" height="44"/><rect x="-30" y="-40" width="60" height="44"/><rect x="50" y="-40" width="60" height="44"/></g>
  <circle cx="-90" cy="52" r="18" class="ink"/><circle cx="90" cy="52" r="18" class="ink"/>
</g>
<g transform="translate(470 270)">
  <path d="M-120-60h240v100h-240z" class="tealp o"/>
  <g class="bluep o"><rect x="-90" y="-40" width="60" height="44"/><rect x="-10" y="-40" width="60" height="44"/></g>
  <circle cx="-70" cy="52" r="18" class="ink"/><circle cx="70" cy="52" r="18" class="ink"/>
</g>
<path d="M320 280h30" fill="none" stroke="{INK}" stroke-width="8"/>
""", ground=False)

add('catalogue', '商品が写真つきで並んだ冊子のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M0 40q-80-40-160-20v-160q80-20 160 20z" class="paper"/>
  <path d="M0 40q80-40 160-20v-160q-80-20-160 20z" class="paper"/>
  <path d="M0-120v160" class="a"/>
  <g class="tealp o"><rect x="-130" y="-90" width="44" height="44"/><rect x="-70" y="-90" width="44" height="44"/></g>
  <g class="coralp o"><rect x="30" y="-90" width="44" height="44"/><rect x="90" y="-90" width="44" height="44"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-130-30h100M-130-10h80M30-30h100M30-10h80"/></g>
</g>
<path d="M120 350h360" class="a"/>
""", ground=True)

add('centre', '円の中心にある点を示したイラスト。', f"""
<circle cx="300" cy="210" r="140" fill="none" stroke="{TONES['teal'][0]}" stroke-width="10"/>
<circle cx="300" cy="210" r="14" class="coral o"/>
<g class="muted"><path d="M160 210h130M300 70v130M440 210H310M300 350V220"/></g>
""", ground=False)

add('certain', '答えに丸をつけて、はっきり確信しているイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','point','short','smile')}
<g transform="translate(400 230)">
  <path d="M-110-110h220v220h-220z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-60h140M-70 0h140M-70 60h110"/></g>
  <circle cx="0" cy="0" r="46" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M240 180l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('chase', '前を走る相手を、後ろから追いかけているイラスト。', f"""
{person(400,346,1.1,1,'coral','gold','walk','short','surprised')}
{person(200,346,1.1,1,'teal','blue','walk','cap','neutral')}
<path d="M270 240q60-30 100-10" class="a" marker-end="url(#ar)"/>
<g class="muted"><path d="M140 300h-40M150 340h-50"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('cheat', '答案をこっそり見て、不正をしているイラスト。', f"""
{person(200,346,1.1,1,'coral','blue','point','short','neutral')}
<g transform="translate(360 280)">
  <path d="M-80-70h160v140h-160z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-50-40h100M-50-10h100M-50 20h70"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="8 7"><path d="M250 230h60" marker-end="url(#ar)"/></g>
<g class="corals" style="stroke-width:7"><path d="M440 170l30 30M470 170l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('classical', '古い様式の柱が並んだ建物のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-200 90h400v20h-400z" class="goldd o"/>
  <g class="goldp o">
    {''.join(f'<rect x="{-170+i*70}" y="-40" width="40" height="130"/>' for i in range(5))}
  </g>
  <path d="M-210-40h420v-26h-420z" class="goldd o"/>
  <path d="M-210-66L0-150l210 84z" class="gold o"/>
</g>
<path d="M60 360h480" class="a"/>
""", ground=True)

add('clear', 'くもったガラスをふいて、向こうがはっきり見えるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" fill="#dbeaf8" stroke="{INK}" stroke-width="4"/>
  <path d="M-200 60L-60-60l90 90 70-60 100 90z" class="tealp o"/>
  <path d="M-200-140h190v280h-190z" fill="#ffffff" opacity=".65"/>
</g>
{hand(160,180,1)}
<path d="M210 300h80" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('clever', '難しい仕掛けを、うまい方法で解いているイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','think','short','smile')}
<g transform="translate(400 240)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <path d="M-60-60h60v60h-60zM0 0h60v60H0z" class="tealp o"/>
  <path d="M-60 0h60v60h-60z" class="goldp o"/>
  <path d="M0-60h60v60H0z" class="coralp o"/>
</g>
<g transform="translate(240 160)">
  <circle r="30" class="goldp o"/>
  <path d="M-12 30h24v12h-24z" class="ink"/>
  <g class="golds" style="stroke-width:4"><path d="M0-44v-16M-34-22l-14-8M34-22l14-8"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('click', 'マウスのボタンを押して、カチッと反応するイラスト。', f"""
<g transform="translate(300 270)">
  <path d="M-70 60q-20-120 70-120t70 120q-30 24-70 24t-70-24z" fill="#dfe6ea" class="o"/>
  <path d="M-4-58v50" class="a"/>
  <path d="M-70-10q0-50 66-50" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>
{hand(300,140,1)}
<path d="M300 180v30" class="a" marker-end="url(#ar)"/>
<g class="golds" style="stroke-width:4"><path d="M180 200l-26-16M420 200l26-16"/></g>
""", ground=True, arrow=True)

add('closed', '店の扉が閉まり、閉店の札が下がっているイラスト。', f"""
{building(300,300,1.1,'teal')}
<path d="M280 300v-52h40v52z" class="goldd o"/>
<g transform="translate(300 180) rotate(-6)">
  <path d="M-60-24h120v48h-120z" class="paper"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M-36 0h72"/></g>
</g>
<g class="corals" style="stroke-width:8"><path d="M450 200l40 40M490 200l-40 40"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('collector', '集めた切手を並べて眺めている収集家のイラスト。', f"""
{person(160,346,1.15,1,'violet','blue','point','bun','smile')}
<g transform="translate(400 240)">
  <path d="M-130-100h260v200h-260z" class="violetp o"/>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="2.5">
    {''.join(f'<rect x="{-108 + (i%4)*56}" y="{-76 + (i//4)*68}" width="44" height="52"/>' for i in range(8))}
  </g>
</g>
<path d="M240 220h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('combine', '二つの部品を合わせて、一つの形にするイラスト。', f"""
<g transform="translate(140 240)"><path d="M-60-60h120v120h-120z" class="teal o"/></g>
<g transform="translate(460 240)"><circle r="60" class="coral o"/></g>
<g transform="translate(300 250)">
  <path d="M-56-56h112v112h-112z" class="teal o"/>
  <circle cx="30" cy="30" r="46" class="coral o" opacity=".9"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M210 180q40 20 46 40"/><path d="M390 180q-40 20-46 40"/></g>
""", ground=True, arrow=True)

add('comfortable', 'やわらかいソファに深く座って、くつろいでいるイラスト。', f"""
<circle cx="470" cy="96" r="54" class="violetp"/>
<g transform="translate(290 300)">
  <path d="M-150-40h300v90h-300z" class="violetp o"/>
  <path d="M-150-40q0-70 60-70h180q60 0 60 70z" class="violetp o"/>
  <path d="M-190-20h40v70h-40zM150-20h40v70h-40z" class="violetd o"/>
</g>
<g transform="translate(290 290)">
  <path d="M-30-70q30-14 60 0l-8 68h-44z" class="teal o"/>
  <path d="M-24-8l-56 16M20-8l50 12" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <circle cx="0" cy="-96" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-24-98q3-28 25-28 24 0 28 25-13-10-27-4-12-11-26 7z" fill="{HAIR}"/>
  <path d="M-12-92h8M4-92h8" class="a"/>
  <path d="M-8-80q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
<path d="M60 360h480" class="a"/>
""", ground=True)

add('communicate', '二人が言葉をやりとりして、意思を伝え合うイラスト。', f"""
{person(170,346,1.1,1,'teal','blue','stand','short','smile')}
{person(430,346,1.1,-1,'coral','gold','stand','bob','smile')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5">
  <path d="M240 200h120" marker-end="url(#ar)"/>
  <path d="M360 250H240" marker-end="url(#ar)"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('compete', '二人が同じ的を目指して、競い合っているイラスト。', f"""
<g transform="translate(300 130)">
  <circle r="52" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <circle r="34" class="goldp o"/><circle r="14" class="gold o"/>
</g>
{person(170,346,1.1,1,'teal','blue','up','short','neutral')}
{person(430,346,1.1,-1,'coral','gold','up','cap','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M220 250q30-40 50-56"/><path d="M380 250q-30-40-50-56"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(' '.join(W)); print(sheet(W))
