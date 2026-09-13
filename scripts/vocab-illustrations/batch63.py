"""第63回: 免許・限界・場所・誤解など45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('lesser', '二つのうち、小さいほう・劣るほうを示したイラスト。', f"""
<path d="M60 340h480" class="a"/>
<rect x="140" y="140" width="130" height="200" class="teal o"/>
<rect x="340" y="240" width="130" height="100" class="coral o"/>
<path d="M405 190v30" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M120 240h360"/></g>
""", ground=False, arrow=True)

add('lethal', 'ひと口で命を落とす、どくろ印の毒のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-80-80h160l-16 180h-128z" fill="#e2eee2" stroke="{INK}" stroke-width="3"/>
  <path d="M-34-110h68v30h-68z" class="ink"/>
  <g transform="translate(0 30)">
    <circle r="44" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
    <g fill="{INK}"><circle cx="-15" cy="-8" r="9"/><circle cx="15" cy="-8" r="9"/><rect x="-5" y="8" width="10" height="14"/></g>
    <path d="M-22 28h44" fill="none" stroke="{INK}" stroke-width="4"/>
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10"><circle cx="300" cy="230" r="150"/></g>
""", ground=False)

add('liable', 'こわしたぶんの責任を負って払うイラスト。', f"""
<g transform="translate(190 300)">
  <g fill="#cfe0ea" stroke="{INK}" stroke-width="3"><path d="M-70 40l30-50 24 30z"/><path d="M10 40l30-30 20 30z"/></g>
</g>
{person(400,346,1.2,1,'teal','blue','give','short','sad')}
<g transform="translate(320 250)">
  <path d="M-50-24h100v40h-100z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <circle r="12" class="goldd o"/>
</g>
<path d="M290 300h-60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('license', '顔写真と印のついた免許証のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-170-110h340v220h-340z" class="paper"/>
  <g transform="translate(-100 -10)">
    <path d="M-50-60h100v120h-100z" class="tealp o"/>
    <circle cy="-16" r="20" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <path d="M-32 40q0-30 32-30t32 30z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  </g>
  <g fill="{INK}"><rect x="-10" y="-70" width="130" height="18"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-10-20h130M-10 20h100"/></g>
  <g transform="translate(90 60)"><circle r="26" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/><path d="M-12 0l10 10 18-20" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('lifelong', '子どものころから年老いるまで続くイラスト。', f"""
{person(140,346,0.75,1,'coral','gold','stand','cap','smile')}
{person(300,346,1.2,1,'teal','blue','stand','short','smile')}
{person(460,346,1.1,1,'violet','blue','stand','bob','smile')}
<path d="M120 170h360" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('like', '二つがよく似ていて、同じようだと示すイラスト。', f"""
<g transform="translate(180 230)"><path d="M0-80l80 80-80 80-80-80z" class="teal o"/></g>
<g transform="translate(430 230)"><path d="M0-76l76 76-76 76-76-76z" class="tealp o"/></g>
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M290 210q20-14 40 0M290 250q20-14 40 0"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('limit', 'ここまでという線が引かれているイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-220-40h440v80h-440z" fill="#dfe6ea" class="o"/>
  <path d="M-220-40h300v80h-300z" class="teal o"/>
  <path d="M80-90v180" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 150h70"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M440 130l30 30M470 130l-30 30"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('limited', '数がわずかしか用意されていないイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8">
  {''.join(f'<rect x="{300+i*70}" y="220" width="60" height="90"/>' for i in range(3))}
</g>
<g class="teal o"><rect x="120" y="220" width="60" height="90"/><rect x="200" y="220" width="60" height="90"/></g>
<g fill="{INK}" transform="translate(500 170)">
  <path d="M0 0q0-24 18-24t18 24q0 12-12 16v10h-10v-18q12-4 12-12t-7-8-7 12z"/><rect x="11" y="38" width="10" height="10"/>
</g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('linear', '点が一直線に並ぶイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" fill="#f7fbfe" class="o"/>
  <path d="M-170 100L170-90" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"/>
  <g fill="{INK}"><circle cx="-170" cy="100" r="8"/><circle cx="-85" cy="52" r="8"/><circle cx="0" cy="5" r="8"/><circle cx="85" cy="-43" r="8"/><circle cx="170" cy="-90" r="8"/></g>
</g>
""", ground=True)

add('lip', '口のふちのくちびるを示したイラスト。', f"""
{face(280,200,110,'flat')}
<g transform="translate(280 250)">
  <path d="M-60 0q30-26 60 0 30-26 60 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="0" transform="translate(-30 0)"/>
  <path d="M-56 0q28-30 56 0 28-30 56 0 -28 34-56 34-28 0-56-34z" transform="translate(-28 0)" class="coral o"/>
</g>
<circle cx="280" cy="252" r="56" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M450 252h-60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('literary', '古い装丁の文学書が並ぶイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-200 90h400v20h-400z" class="goldd o"/>
  <g class="violet o"><rect x="-180" y="-60" width="50" height="150"/></g>
  <g class="coral o"><rect x="-120" y="-80" width="50" height="170"/></g>
  <g class="teald o"><rect x="-60" y="-50" width="50" height="140"/></g>
  <g class="goldd o"><rect x="0" y="-70" width="50" height="160"/></g>
  <g class="violetp o"><rect x="60" y="-40" width="50" height="130"/></g>
  <g fill="{TONES['gold'][2]}"><rect x="-172" y="-30" width="34" height="8"/><rect x="-112" y="-50" width="34" height="8"/><rect x="8" y="-40" width="34" height="8"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('literature', '物語の本と、それを読む人のイラスト。', f"""
<g transform="translate(390 230)">
  <path d="M-140-100h280v200h-280z" class="violet o"/>
  <path d="M-120-80h240v160h-240z" fill="#fffdf6" class="o"/>
  <path d="M0-80v160" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-100 {-50+i*30}h80"/>' for i in range(4))}{''.join(f'<path d="M20 {-50+i*30}h80"/>' for i in range(4))}</g>
</g>
{person(140,346,1.05,1,'teal','blue','think','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('little', '器の中身がほんの少しだけのイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-90-110h180l-20 220h-140z" fill="#f7fbfe" class="o"/>
  <path d="M-62 70h124l-6 40h-112z" class="bluep o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M450 320v-30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('lively', '音楽に合わせて元気に飛びはねるイラスト。', f"""
<g transform="translate(200 340) rotate(-10)">{person(0,0,1.2,1,'coral','gold','up','bob','smile')}</g>
<g transform="translate(380 340) rotate(10)">{person(0,0,1.2,1,'teal','blue','up','short','smile')}</g>
<g fill="{INK}"><ellipse cx="300" cy="150" rx="16" ry="11" transform="rotate(-18 300 150)"/><rect x="311" y="106" width="6" height="40"/></g>
<g class="golds" style="stroke-width:5"><path d="M120 200l-24-18M480 200l24-18"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('living', '人が暮らしている部屋のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-140h440v280h-440z" fill="#fffdf6" class="o"/>
  <path d="M-220 60h440v80h-440z" class="goldp o"/>
  <g class="tealp o"><rect x="-190" y="-20" width="150" height="80"/></g>
  <path d="M-180-100h100v70h-100z" fill="#cfe6f5" stroke="{INK}" stroke-width="3"/>
  <g class="goldd o"><rect x="60" y="0" width="140" height="20"/><rect x="70" y="20" width="14" height="40"/><rect x="176" y="20" width="14" height="40"/></g>
</g>
{person(200,320,0.7,1,'coral','gold','stand','bob','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('locate', '探して、その位置を突き止めるイラスト。', f"""
<g transform="translate(280 240)">
  <path d="M-190-140h380v280h-380z" class="paper"/>
  <path d="M-190 40q100-40 190 0t190-20" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"/>
</g>
<g transform="translate(400 200)">
  <circle r="64" fill="#e7f6fb" opacity=".85" stroke="{INK}" stroke-width="8"/>
  <path d="M0 30c-24-32-32-44-32-56a32 32 0 0 1 64 0c0 12-8 24-32 56z" class="coral o"/>
  <path d="M0 64v70" fill="none" stroke="{INK}" stroke-width="14" transform="rotate(24)"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('location', '地図上のどこであるかを示したイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-200-40h400M-200 50h400M-70-140v280M70-140v280"/></g>
</g>
<g transform="translate(360 200)">
  <path d="M0 46c-34-46-46-64-46-82a46 46 0 0 1 92 0c0 18-12 36-46 82z" class="coral o"/>
  <circle cy="-38" r="15" fill="#fffdf6"/>
</g>
""", ground=True)

add('loss', '手にしていたものを失うイラスト。', f"""
{person(170,346,1.2,1,'teal','blue','reach','short','sad')}
<g opacity=".3" transform="translate(250 250)"><path d="M-40-40h80v80h-80z" class="muted"/></g>
<path d="M300 250q90-40 140 40" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><rect x="210" y="210" width="80" height="80"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('loudly', '大声で叫んで、音が大きく響くイラスト。', f"""
{person(160,346,1.2,1,'coral','blue','up','short','flat')}
<g transform="translate(210 200)"><ellipse rx="20" ry="16" fill="#8b4a3e"/></g>
<g class="corals" opacity=".9" style="stroke-width:8"><path d="M280 150q34 50 34 90t-34 90M350 120q46 70 46 120t-46 120M420 90q60 90 60 150t-60 150"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('luxury', '宝石と金の器で、ぜいたくを示したイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-70-70h140l-16 140h-108z" class="gold o"/>
  <path d="M-50-40h100l-10 90h-80z" fill="#f7e6bd"/>
</g>
<g transform="translate(420 250)">
  <path d="M0-70l50 30v50L0 70l-50-30v-50z" class="violet o"/>
  <path d="M0-70v140" fill="none" stroke="#fffdf6" stroke-width="3"/>
</g>
<g class="golds" style="stroke-width:5"><path d="M300 150l-10-26M340 170l26-20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('magnetic', '磁石が金属を引きつけるイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-70-60a70 70 0 0 1 140 0v40h-46v-40a24 24 0 0 0-48 0v40h-46z" class="coral o"/>
  <path d="M-70-20h46v50h-46z" class="ink"/>
  <path d="M24-20h46v50H24z" fill="#c9d3dc" stroke="{INK}" stroke-width="2"/>
</g>
<g fill="#c9d3dc" stroke="{INK}" stroke-width="2"><rect x="380" y="200" width="40" height="14"/><rect x="430" y="240" width="40" height="14"/><rect x="390" y="280" width="40" height="14"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M370 210h-60M420 250h-90M380 290h-70"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('magnificent', '見上げるほど壮大な山と城のイラスト。', f"""
<g fill="#b9c8d6"><path d="M300 60l200 240H100z"/></g>
<g fill="#a8bacb"><path d="M300 60l70 240h-140z"/></g>
<g transform="translate(300 300)">
  <path d="M-90 40h180v-70h-180z" fill="#f4ead2" class="o"/>
  <path d="M-90-30h30v-40h-30zM-15-30h30v-50h-30zM60-30h30v-40h-30z" class="teal o"/>
</g>
{person(120,346,0.6,1,'coral','blue','up','short','surprised')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('major', 'いくつもある中で、いちばん主要なものを示したイラスト。', f"""
<path d="M60 346h480" class="a"/>
<g class="tealp o"><rect x="110" y="270" width="70" height="76"/><rect x="200" y="290" width="70" height="56"/><rect x="440" y="280" width="70" height="66"/></g>
<rect x="300" y="140" width="120" height="206" class="coral o"/>
<path d="M360 100v30" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('mall', '店が並ぶショッピングモールのイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-240-120h480v240h-480z" fill="#fffdf6" class="o"/>
  <path d="M-240-120h480v40h-480z" class="teal o"/>
  <g class="tealp o"><rect x="-210" y="-40" width="120" height="90"/><rect x="-70" y="-40" width="120" height="90"/><rect x="70" y="-40" width="120" height="90"/></g>
  <g fill="{INK}"><rect x="-200" y="-30" width="60" height="12"/><rect x="-60" y="-30" width="60" height="12"/><rect x="80" y="-30" width="60" height="12"/></g>
</g>
{person(180,330,0.7,1,'coral','gold','walk','bob','smile')}
{person(400,330,0.7,-1,'teal','blue','walk','short','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('mandatory', 'やらねばならないと、印がついているイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-140-120h280v240h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-90-60h180M-90-20h180M-90 20h140"/></g>
  <g fill="{TONES['coral'][0]}"><path d="M-120-108h26v66h-26zM-120-30h26v26h-26z"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><rect x="-134" y="-118" width="268" height="120"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M520 160h-40"/></g>
""", ground=True, arrow=True)

add('marginal', 'ほんのわずかしか差がないイラスト。', f"""
<path d="M60 340h480" class="a"/>
<rect x="170" y="160" width="120" height="180" class="teal o"/>
<rect x="330" y="150" width="120" height="190" class="coral o"/>
<g class="a" marker-end="url(#ar)"><path d="M300 120v40M300 160v-40"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M150 160h330M150 150h330"/></g>
""", ground=False, arrow=True)

add('marketing', '商品を売り込む看板と客のイラスト。', f"""
<g transform="translate(400 230)">
  <path d="M-130-120h260v190h-260z" fill="#fffdf6" class="o"/>
  <path d="M-100-90h200v90h-200z" class="coralp o"/>
  <g fill="{INK}"><rect x="-80" y="20" width="160" height="20"/></g>
  <path d="M-14 70h28v100h-28z" class="ink"/>
</g>
{person(140,346,1.05,1,'blue','blue','point','short','smile')}
<g class="corals" style="stroke-width:5"><path d="M230 190q26-16 50 0M230 230h50"/></g>
{person(250,346,0.8,-1,'coral','gold','walk','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('marriage', '指輪を交わして夫婦になるイラスト。', f"""
{person(230,346,1.2,1,'blue','blue','give','short','smile')}
{person(380,346,1.2,-1,'coral','gold','give','bob','smile')}
<g transform="translate(305 250)">
  <circle cx="-16" r="20" fill="none" stroke="{TONES['gold'][0]}" stroke-width="7"/>
  <circle cx="16" r="20" fill="none" stroke="{TONES['gold'][0]}" stroke-width="7"/>
</g>
<g transform="translate(305 150)">
  <path d="M0 36c-36-28-50-40-50-58a26 26 0 0 1 50-14 26 26 0 0 1 50 14c0 18-14 30-50 58z" class="coralp o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('martial', '構えを取って武術の型を示すイラスト。', f"""
{person(220,346,1.3,1,'blue','blue','point','short','flat')}
<g transform="translate(220 250)"><path d="M-70-10h140v14h-140z" class="ink"/></g>
{person(420,346,1.3,-1,'coral','blue','point','bob','flat')}
<g class="corals" style="stroke-width:5"><path d="M320 200v-26M280 220l-24-18M360 220l24-18"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('massive', 'どっしりと重い巨大な岩塊のイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-200 100l30-140 80-50 130 20 70 80-20 90z" fill="#8b98a6" stroke="{INK}" stroke-width="4"/>
  <g fill="none" stroke="#6d7c8c" stroke-width="5"><path d="M-100-60l40 80-30 80M60-70l-20 80 70 60"/></g>
</g>
{person(100,346,0.6,1,'coral','blue','up','short','surprised')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('matching', 'おそろいの色と形をそろえたイラスト。', f"""
{person(220,346,1.2,1,'coral','gold','stand','bob','smile')}
{person(380,346,1.2,1,'coral','gold','stand','short','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M280 170l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('mathematical', '式と記号でできた数学的なイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-140h380v280h-380z" class="paper"/>
  <g fill="{INK}">
    <rect x="-150" y="-90" width="60" height="12"/><rect x="-70" y="-96" width="12" height="24"/><rect x="-76" y="-90" width="24" height="12"/>
    <rect x="-30" y="-90" width="60" height="12"/><rect x="50" y="-96" width="30" height="8"/><rect x="50" y="-80" width="30" height="8"/>
    <rect x="100" y="-90" width="60" height="12"/>
  </g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><circle cx="-100" cy="40" r="50"/><path d="M20 90h120V-10H20z"/></g>
</g>
""", ground=True)

add('mature', '青い実が熟して色づくイラスト。', f"""
<g transform="translate(170 250)">
  <circle r="66" class="green o"/>
  <path d="M0-66v-26" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
</g>
<g transform="translate(430 250)">
  <circle r="76" class="coral o"/>
  <path d="M0-76v-26" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
</g>
<path d="M280 250h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 360l20 20 34-40"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('mechanical', '歯車とレバーで動く機械仕掛けのイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-180-130h360v260h-360z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="12"><circle cx="-70" cy="-30" r="50"/><circle cx="40" cy="40" r="36"/></g>
  <g fill="{INK}">{''.join(f'<rect x="-78" y="-98" width="16" height="20" transform="rotate({i*60} -70 -30)"/>' for i in range(6))}</g>
  <g transform="translate(120 -60)"><path d="M-8-50h16v70h-16z" class="coral o"/><circle cy="-56" r="14" class="coral o"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('medieval', '城と旗のある中世のイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-160 80h320v-140h-320z" fill="#c8c2b0" stroke="{INK}" stroke-width="3"/>
  <g fill="#c8c2b0" stroke="{INK}" stroke-width="3"><rect x="-190" y="-100" width="60" height="180"/><rect x="130" y="-100" width="60" height="180"/></g>
  <g fill="{INK}"><rect x="-150" y="-70" width="20" height="26"/><rect x="-40" y="-70" width="20" height="26"/><rect x="60" y="-70" width="20" height="26"/></g>
  <path d="M-40 80V10h80v70z" class="goldd o"/>
  <path d="M-164-100h8v-40h-8zM156-100h8v-40h-8z" class="ink"/>
  <path d="M-156-138h40v24h-40zM164-138h40v24h-40z" class="coral o"/>
</g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('memorable', '心に残って忘れられない場面のイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','think','short','smile')}
<g transform="translate(430 200)">
  <path d="M-130-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-166q-38-4-26-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 -6) scale(0.55)">
    <path d="M-90-50h180v110h-180z" class="paper"/>
    <path d="M-60 50l50-70 34 34 30-44 30 80z" class="green o"/>
  </g>
  <g transform="translate(90 20)"><path d="M0-20l8 16 18 2-13 13 3 18-16-9-16 9 3-18-13-13 18-2z" class="gold o"/></g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="280" cy="300" r="12"/><circle cx="256" cy="324" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('mere', 'ほんの一つだけしかないイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><rect x="90" y="180" width="420" height="170" rx="14"/></g>
<g transform="translate(300 265)"><circle r="26" class="coral o"/></g>
<g class="a" marker-end="url(#ar)"><path d="M300 130v30"/></g>
""", ground=False, arrow=True)

add('mess', '物が散らかって、雑然としているイラスト。', f"""
<g transform="translate(300 300)"><path d="M-240-20h480v40h-480z" class="goldd o"/></g>
<g class="tealp o" transform="translate(150 250) rotate(24)"><rect x="-40" y="-30" width="80" height="60"/></g>
<g class="coralp o" transform="translate(260 240) rotate(-18)"><rect x="-50" y="-24" width="100" height="48"/></g>
<g class="goldp o" transform="translate(380 250) rotate(40)"><rect x="-36" y="-30" width="72" height="60"/></g>
<g fill="none" stroke="{INK}" stroke-width="4"><path d="M440 260q30-30 60 0"/></g>
<g fill="{MUTED}"><circle cx="200" cy="200" r="8"/><circle cx="330" cy="180" r="6"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('minimal', '飾りを削って、必要最小限にしたイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-90-90h180v180h-180z" fill="#fffdf6" class="o"/>
  <g class="tealp o"><circle cx="-40" cy="-40" r="20"/><rect x="10" y="-60" width="50" height="40"/><circle cx="30" cy="40" r="24"/><rect x="-70" y="20" width="50" height="40"/></g>
</g>
<g transform="translate(430 240)">
  <path d="M-90-90h180v180h-180z" fill="#fffdf6" class="o"/>
  <g class="teal o"><circle r="26"/></g>
</g>
<path d="M290 240h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('minor', '主要なものに比べて、小さいほうを示したイラスト。', f"""
<path d="M60 346h480" class="a"/>
<rect x="140" y="130" width="150" height="216" class="teal o"/>
<rect x="360" y="270" width="90" height="76" class="coral o"/>
<path d="M405 220v30" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('minute', '虫めがねでしか見えない極小の粒のイラスト。', f"""
<g transform="translate(240 260)">
  <path d="M-160-100h320v200h-320z" fill="#fffdf6" class="o"/>
  <g class="coral o"><circle cx="20" cy="10" r="4"/></g>
</g>
<g transform="translate(400 200) rotate(24)">
  <circle r="76" fill="#e7f6fb" opacity=".85" stroke="{INK}" stroke-width="8"/>
  <g class="coral o"><circle r="16"/></g>
  <path d="M0 76v70" fill="none" stroke="{INK}" stroke-width="16"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('miserable', '雨に濡れて、みじめに落ち込むイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#8b98a6"/>
<g fill="none" stroke="#cfd8e0" stroke-width="4" stroke-linecap="round">{''.join(f'<path d="M{90+i*50} 90l-16 50"/>' for i in range(10))}</g>
<g transform="translate(300 340) rotate(6)">{person(0,0,1.15,1,'blue','blue','stand','short','sad')}</g>
{drop(360,240,0.8)}
""", ground=False)

add('misleading', '矢印が実際とちがう方を指して、誤解させるイラスト。', f"""
<g transform="translate(200 220)">
  <path d="M-70-50h140v100h-140z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="7" marker-end="url(#ar)"><path d="M-40 0h60"/></g>
  <path d="M-14 50h28v90h-28z" class="ink"/>
</g>
<path d="M300 220h120" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"/>
<g transform="translate(470 220)">
  <path d="M0-60l60 120h-120z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-6" y="-14" width="12" height="40"/><rect x="-6" y="36" width="12" height="12"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M190 320l30 30M220 320l-30 30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('misunderstanding', '同じ言葉を、互いに別の意味で受け取るイラスト。', f"""
{person(150,346,1.15,1,'teal','blue','point','short','neutral')}
{person(450,346,1.15,-1,'coral','gold','think','bob','flat')}
<g transform="translate(230 170)">
  <path d="M-60-40h120v60h-120z" fill="#fffdf6" class="o"/>
  <g class="teal o"><circle r="16" transform="translate(0 -10)"/></g>
</g>
<g transform="translate(390 170)">
  <path d="M-60-40h120v60h-120z" fill="#fffdf6" class="o"/>
  <g class="coral o"><rect x="-18" y="-28" width="36" height="36"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M295 140l30 30M325 140l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('mixed', '別々の色が混ざり合うイラスト。', f"""
<g transform="translate(160 240)"><circle r="60" class="teal o"/></g>
<g transform="translate(300 240)"><circle r="60" class="coral o"/></g>
<g transform="translate(460 240)">
  <circle r="70" class="violet o"/>
  <path d="M-70 0a70 70 0 0 1 140 0z" class="teal o" opacity=".5"/>
</g>
<path d="M370 240h30" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('moderate', '強すぎず弱すぎない、ほどよい目盛りのイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-170 40a170 170 0 0 1 340 0z" fill="#f7fbfe" class="o"/>
  <path d="M-170 40a170 170 0 0 1 60-130l40 46a110 110 0 0 0-40 84z" class="tealp o"/>
  <path d="M170 40a170 170 0 0 0-60-130l-40 46a110 110 0 0 1 40 84z" class="coralp o"/>
  <path d="M0 40V-120" fill="none" stroke="{INK}" stroke-width="8"/>
  <circle cy="40" r="12" class="ink"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 200l20 20 34-40"/></g>
<path d="M60 320h480" class="a"/>
""", ground=True)

add('modest', '実績はあるのに、控えめに構えるイラスト。', f"""
<g transform="translate(220 346) rotate(16)">{person(0,0,1.2,1,'teal','gold','stand','short','smile')}</g>
<g transform="translate(430 230)">
  <path d="M-70-70h140v140h-140z" class="paper"/>
  <g transform="translate(0 -10)"><path d="M0-30l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" class="gold o"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-40 40h80"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M320 250h30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)
print(len(W), ' '.join(W)); print(sheet(W))
