# -*- coding: utf-8 -*-
"""第188回。plus36 の50語。marble / moose / mosaic の描き直しも含む。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

add('marble', '磨いた石の板に、うっすら筋の模様が走っている',
    '大理石、ビー玉＝marble。', f'''
{table(352)}
<g transform="translate(300 240)">
  <path d="M-230-120h460v230h-460z" fill="#f4f2ec" class="o"/>
  <path d="M-210-90q90 40 180-10t200 30" fill="none" stroke="#cfc9bd" stroke-width="7"/>
  <path d="M-220 10q120-30 210 20t180-10" fill="none" stroke="#dcd7cc" stroke-width="9"/>
  <path d="M-200 70q100 20 190-14t200 20" fill="none" stroke="#cfc9bd" stroke-width="5"/>
  <path d="M-230-120h460v230h-460z" fill="none" class="o"/></g>
{''.join(f'<g transform="translate({{}} 300)"><circle r="22" fill="#cfe4f0" stroke="{INK}" stroke-width="2.5"/><path d="M-13 4q13-20 26 0" fill="none" stroke="{{}}" stroke-width="8"/></g>'.format(200 + i * 90, c) for i, c in enumerate(['#e86452', '#4e986a', '#d99a2b']))}''')

add('moose', '手のひらのように広がった角をもつヘラジカが、森に立つ',
    'ヘラジカ＝moose。', f'''
<path d="M0 330h600v70H0z" class="greenp"/>
{tree(80, 330, 0.8)}{tree(540, 330, 0.7)}
<g transform="translate(290 250)">
  <ellipse rx="118" ry="62" fill="#7a5a3a" class="o"/>
  <path d="M96-30q26-56 58-36 24 16 6 52-14 24-42 22z" fill="#7a5a3a" class="o"/>
  <path d="M120-70q-50-6-56-40 30-6 46 10 6-24 26-26-4 22 10 34z" fill="#c8a05f" class="o"/>
  <path d="M172-74q50-6 56-40-30-6-46 10-6-24-26-26 4 22-10 34z" fill="#c8a05f" class="o"/>
  <circle cx="140" cy="-38" r="5" class="ink"/>
  <ellipse cx="168" cy="-12" rx="16" ry="12" fill="#4a3420"/>
  <path d="M120 20q6 34-14 48" fill="none" stroke="#7a5a3a" stroke-width="11" stroke-linecap="round"/>
  <path d="M-76 56v56M-18 60v52M40 60v52M92 54v58" stroke="#7a5a3a" stroke-width="17" fill="none" stroke-linecap="round"/></g>''')

add('mosaic', '小さな色タイルを寄せ集め、円の模様を描いている',
    'モザイク＝mosaic。', f'''
<g transform="translate(300 210)">
  <path d="M-230-140h460v280h-460z" fill="#e8ddc9" class="o"/></g>
{''.join(f'<rect x="{80 + (i % 21) * 21}" y="{80 + (i // 21) * 21}" width="17" height="17" rx="2" fill="{c}" stroke="#e8ddc9" stroke-width="1"/>' for i, c in enumerate([('#fffefd' if abs(((i % 21) * 21 + 88) - 300) ** 2 + abs(((i // 21) * 21 + 88) - 210) ** 2 < 5200 else ['#238b83', '#4e86c6', '#e86452', '#d99a2b', '#816eb2'][i % 5]) for i in range(273)]))}
<g transform="translate(300 210)"><path d="M-230-140h460v280h-460z" fill="none" class="o"/></g>''')

# --- plus36 ------------------------------------------------------------------

add('pastry', '伸ばした生地を型に敷き、ふちを指で押さえる',
    '練り生地(パイ皮)、焼き菓子＝pastry。', f'''
{table(352)}
<g transform="translate(300 280)">
  <path d="M-120-30q0 60 120 60t120-60z" fill="#c3cbd1" class="o"/>
  <ellipse cy="-30" rx="120" ry="30" fill="#dfe6ea" class="o"/>
  <ellipse cy="-28" rx="104" ry="24" fill="#f0e0b8"/>
  {''.join(f'<path d="M{int(-100*math.cos(math.radians(a)))} {int(-28-24*math.sin(math.radians(a)))}l{int(14*math.cos(math.radians(a)))} {int(10*math.sin(math.radians(a)))}" stroke="#d8c49a" stroke-width="4" fill="none"/>' for a in range(0, 181, 20))}</g>
<g transform="translate(280 180)">
  <path d="M-110-24h220v48h-220z" fill="#c9a464" class="o"/>
  <path d="M-146-12h36v24h-36zM110-12h36v24h-36z" fill="#a0764a" class="o"/></g>''')

add('peacock', '尾羽を扇のように広げたクジャクが、目玉模様を見せる',
    'クジャク(雄)＝peacock。', f'''
<path d="M0 330h600v70H0z" class="greenp"/>
<g transform="translate(300 250)">
  {''.join(f'<g transform="rotate({-80+i*16})"><path d="M0 0v-190" stroke="#3f8f6a" stroke-width="6" fill="none"/><ellipse cy="-196" rx="18" ry="24" class="teal o"/><circle cy="-196" r="9" class="violet"/></g>' for i in range(11))}
  <ellipse rx="44" ry="60" class="blue o"/>
  <circle cy="-80" r="26" class="blue o"/>
  <path d="M22-86l26 8-26 10z" class="gold o"/>
  <circle cx="10" cy="-88" r="4" class="ink"/>
  <path d="M0-106v-18M-10-118h20" stroke="{TEAD}" stroke-width="4" fill="none"/>
  <path d="M-16 60v24M16 60v24" stroke="{GLDD}" stroke-width="7" fill="none" stroke-linecap="round"/></g>''')

add('pearl', '貝の中の丸い真珠と、つないだネックレス',
    '真珠＝pearl。', f'''
{table(352)}
<g transform="translate(190 280)">
  <path d="M-80 0q0-60 80-60t80 60z" fill="#e8e4da" class="o"/>
  <path d="M-80 0q0 40 80 40t80-40z" fill="#d8d2c4" class="o"/>
  <circle cy="-16" r="26" fill="#fffefd" class="o"/>
  <circle cx="-8" cy="-24" r="7" fill="#ffffff"/></g>
<g transform="translate(430 240)">
  <path d="M-100 0q100 90 200 0" fill="none" stroke="{MUTED}" stroke-width="3"/>
  {''.join(f'<circle cx="{-100+i*22}" cy="{abs(math.sin(i/9*math.pi))*66:.0f}" r="12" fill="#fffefd" stroke="{MUTED}" stroke-width="2"/>' for i in range(10))}</g>''')

add('pebble', '波で角の取れた丸い小石が、浜辺に集まっている',
    '小石＝pebble。', f'''
<path d="M0 250h600v150H0z" fill="#e2ddd2"/>
<path d="M0 250h600v-40q-140 40-300 0T0 250z" class="bluep o"/>
{''.join(f'<ellipse cx="{{}}" cy="{{}}" rx="{{}}" ry="{{}}" fill="{{}}" stroke="{INK}" stroke-width="2" transform="rotate({{}} {{}} {{}})"/>'.format(70 + (i * 67) % 480, 280 + (i * 41) % 100, 20 + i % 12, 14 + i % 8, ['#b5bec4', '#dfe6ea', '#9aa7b1', '#cfd6db'][i % 4], (i * 31) % 60 - 30, 70 + (i * 67) % 480, 280 + (i * 41) % 100) for i in range(22))}''')

add('peg', '壁に打った掛けくぎに、上着と帽子が下がる',
    'くい、掛けくぎ＝peg。', f'''
<g transform="translate(300 200)"><path d="M-280-180h560v360h-560z" fill="#f6efe1" class="o"/></g>
<g transform="translate(300 160)">
  <path d="M-220-20h440v20h-440z" fill="#c9a464" class="o"/>
  {''.join(f'<g transform="translate({-150+i*100} 0)"><path d="M-9 0h18v34h-18z" fill="#a0764a" class="o"/><circle cy="40" r="14" fill="#a0764a" class="o"/></g>' for i in range(4))}</g>
<g transform="translate(150 210)">
  <path d="M-60 0l60-30 60 30 10 120h-140z" class="teal o"/></g>
<g transform="translate(350 206)">
  <path d="M-46 14q0-40 46-40t46 40z" class="coral o"/>
  <path d="M-60 14h120v16h-120z" class="corald o"/></g>''')

add('pencil', '先を削った鉛筆と、消しゴムのついた端',
    '鉛筆＝pencil。', f'''
{table(352)}
<g transform="translate(300 260) rotate(-14)">
  <path d="M-190-24h300v48h-300z" class="gold o"/>
  {''.join(f'<path d="M-190 {-24+i*16}h300" stroke="{GLDD}" stroke-width="2" fill="none"/>' for i in range(1, 3))}
  <path d="M110-24h50l40 24-40 24h-50z" fill="#e0c48c" class="o"/>
  <path d="M180-8l20 8-20 8z" class="ink"/>
  <path d="M-230-24h40v48h-40z" fill="#9aa7b1" class="o"/>
  <path d="M-270-20h40v40h-40z" class="coralp o"/></g>''')

add('penknife', '折りたたみ式の小刀の刃が、柄から開いている',
    '小型の折りたたみナイフ＝penknife。', f'''
{table(352)}
<g transform="translate(280 270) rotate(-10)">
  <path d="M-110-24h220v48h-220z" class="coral o"/>
  <path d="M-110-24h220v10h-220z" class="corald"/>
  <circle cx="90" cy="0" r="8" fill="{CRLD}"/></g>
<g transform="translate(380 230) rotate(-38)">
  <path d="M0-16h150l20 16-20 16H0z" fill="#c3cbd1" class="o"/>
  <path d="M0-10h140" fill="none" stroke="#9aa7b1" stroke-width="3"/></g>''')

add('pepper', 'こしょう挽きから黒い粒がふられ、隣にピーマンが置かれる',
    'こしょう／ピーマン＝pepper。', f'''
{table(352)}
<g transform="translate(220 250)">
  <path d="M-34 90q-14-110 6-140h56q20 30 6 140z" fill="#5b4636" class="o"/>
  <path d="M-30-50h60v-30h-60z" fill="#8a6a46" class="o"/>
  <circle cy="-90" r="14" fill="#8a6a46" class="o"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="4" fill="#2f2620"/>'.format(200 + (i * 23) % 60, 350 + (i * 17) % 16) for i in range(7))}
<g transform="translate(430 290)">
  <path d="M-60 10q-10-60 20-76 40-20 80 0 30 16 20 76-30 30-60 30t-60-30z" class="green o"/>
  <path d="M0-72v-24" stroke="#2a6b4c" stroke-width="7" fill="none"/>
  <path d="M-24-72q24-14 48 0" fill="none" stroke="#2a6b4c" stroke-width="6"/></g>''')

add('perfume', 'ガラスの小びんから、香りが霧になって広がる',
    '香水＝perfume。', f'''
{table(352)}
<g transform="translate(280 280)">
  <path d="M-60-50h120v90a20 20 0 0 1-20 20h-80a20 20 0 0 1-20-20z" fill="#f4dff0" opacity="0.9" stroke="{INK}" stroke-width="3"/>
  <path d="M-24-80h48v30h-48z" fill="#e0c48c" class="o"/>
  <path d="M-34-96h68v16h-68z" class="goldd o"/>
  <path d="M34-88h30v20H34z" fill="#c9a2c9" class="o"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="none" stroke="{VIO}" stroke-width="2.5"/>'.format(390 + (i * 31) % 120, 150 + (i * 43) % 90, 5 + i % 4) for i in range(9))}''')

add('pewter', '鈍い銀色の合金で作られた大ぶりのジョッキ',
    'しろめ(錫を主とする合金)＝pewter。', f'''
{table(352)}
<g transform="translate(290 270)">
  <path d="M-70-80h140v140a24 24 0 0 1-24 24h-92a24 24 0 0 1-24-24z" fill="#b8bcc0" class="o"/>
  <path d="M70-50q46 0 46 44t-46 44" fill="none" stroke="#b8bcc0" stroke-width="18"/>
  <ellipse cy="-80" rx="70" ry="18" fill="#cdd1d4" class="o"/>
  <path d="M-50-40h100v10h-100zM-50 30h100v10h-100z" fill="#9ba1a6"/></g>
{''.join(spark(150 + i * 300, 160, 0.6, 'gold') for i in range(2))}''')

add('piano', '黒鍵と白鍵の並んだ鍵盤を、指でたたく',
    'ピアノ＝piano。', f'''
<g transform="translate(300 250)">
  <path d="M-240-120h480v120h-480z" fill="#2f3542" class="o"/>
  <path d="M-250 0h500v40h-500z" fill="#1f2a38" class="o"/>
  {''.join(f'<rect x="{-236+i*34}" y="-88" width="30" height="88" fill="#fffefd" stroke="{INK}" stroke-width="2"/>' for i in range(14))}
  {''.join(f'<rect x="{-214+i*34+ (0 if i%7 in (0,1,3,4,5) else 0)}" y="-88" width="18" height="56" fill="#1f2a38"/>' for i in range(13) if i % 7 not in (2, 6))}
  <path d="M-250 40h500v40h-500z" fill="#2f3542" class="o"/></g>
{hand(200, 130, 1)}''')

add('piglet', '丸い鼻をもつ小さな子ブタが、わらの上に立つ',
    '子ブタ＝piglet。', f'''
<path d="M0 320h600v80H0z" class="ground"/>
<g transform="translate(150 330)"><ellipse rx="60" ry="16" fill="#e0c48c" class="o"/></g>
<g transform="translate(320 280)">
  <ellipse rx="90" ry="56" fill="#f0b8b8" class="o"/>
  <circle cx="80" cy="-24" r="42" fill="#f0b8b8" class="o"/>
  <ellipse cx="116" cy="-16" rx="20" ry="15" fill="#e09a9a" class="o"/>
  <circle cx="110" cy="-20" r="4" class="ink"/><circle cx="122" cy="-20" r="4" class="ink"/>
  <path d="M56-56l-6-26 26 14zM100-60l16-24 4 24z" fill="#f0b8b8" class="o"/>
  <circle cx="70" cy="-38" r="4.5" class="ink"/>
  <path d="M-60 46v34M-16 50v30M26 50v30M66 44v36" stroke="#f0b8b8" stroke-width="15" fill="none" stroke-linecap="round"/>
  <path d="M-90 0q-30-6-24-30" fill="none" stroke="#f0b8b8" stroke-width="9" stroke-linecap="round"/></g>''')

add('pillowcase', 'まくらに白いカバーがかけられ、口が開いている',
    'まくらカバー＝pillowcase。', f'''
{table(352)}
<g transform="translate(300 270)">
  <path d="M-150-60q150-40 300 0 20 60 0 110-150 34-300 0-20-50 0-110z" fill="#fffefd" class="o"/>
  <path d="M100-50q20 60 0 100" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>
  <path d="M100-50q40 0 50 10 10 50 0 84-14 10-50 6" fill="#f2f6f8" class="o"/></g>
{''.join(spark(140 + i * 320, 160, 0.6, 'gold') for i in range(2))}''')

add('pinecone', '松の枝についた、うろこ状の実が下を向く',
    '松かさ、松ぼっくり＝pinecone。', f'''
<g transform="translate(300 150)">
  <path d="M-220 0q120 40 220 0t220 0" fill="none" stroke="{BRN}" stroke-width="12"/>
  {''.join(f'<path d="M{-180+i*46} 6l-24 40M{-180+i*46} 6l-6 44M{-180+i*46} 6l16 42" stroke="#3f8f6a" stroke-width="4" fill="none" stroke-linecap="round"/>' for i in range(9))}</g>
<g transform="translate(300 250)">
  {''.join(f'<ellipse cx="{-28+ (i%3)*28}" cy="{i//3*22}" rx="20" ry="13" fill="#8a5c2b" stroke="{INK}" stroke-width="2"/>' for i in range(12))}
  <ellipse cy="94" rx="16" ry="12" fill="#8a5c2b" class="o"/>
  <path d="M0-30v-24" stroke="{BRN}" stroke-width="6" fill="none"/></g>''')

add('pitcher', '取っ手と注ぎ口のついた水差しから、水を注ぐ',
    '水差し＝pitcher。', f'''
{table(352)}
<g transform="translate(240 240) rotate(24)">
  <path d="M-60-80h120v150a24 24 0 0 1-24 24h-72a24 24 0 0 1-24-24z" fill="#fffefd" class="o"/>
  <path d="M-60-80h-30l20 26h10z" fill="#fffefd" class="o"/>
  <path d="M60-50q40 0 40 40t-40 40" fill="none" stroke="{INK}" stroke-width="10"/>
  <path d="M-52 0h104v66a20 20 0 0 1-20 20h-64a20 20 0 0 1-20-20z" class="bluep"/></g>
{''.join(drop(340 + i * 8, 210 + i * 26, 1.0, 'blue') for i in range(2))}
<g transform="translate(400 300)">
  <path d="M-40-50l6 90h68l6-90z" fill="#e6f2f6" opacity="0.9" stroke="{INK}" stroke-width="3"/>
  <path d="M-32 0h64l4 40h-72z" class="bluep"/></g>''')

add('placemat', '一人分の食器の下に、四角い敷物が置かれている',
    'ランチョンマット＝placemat。', f'''
{table(352)}
<g transform="translate(300 280) rotate(-2)">
  <path d="M-150-60h300v120h-300z" fill="#d8c4a0" class="o"/>
  <path d="M-132-44h264v88h-264z" fill="none" stroke="#b09a72" stroke-width="4"/></g>
<g transform="translate(300 270)"><ellipse rx="80" ry="24" fill="#fffefd" class="o"/><ellipse rx="52" ry="15" fill="none" stroke="{MUTED}" stroke-width="2.5"/></g>
<g transform="translate(190 272)"><path d="M-5-34h10v66h-10z" fill="#c3cbd1" class="o"/>
  {''.join(f'<path d="M{-8+i*8} -34v18" stroke="#c3cbd1" stroke-width="4" fill="none"/>' for i in range(3))}</g>
<g transform="translate(410 272)"><path d="M-5-34h10v66h-10z" fill="#c3cbd1" class="o"/>
  <ellipse cy="-40" rx="12" ry="18" fill="#dfe6ea" class="o"/></g>''')

add('platter', '取り分け用の大きな木の皿に、チーズが盛られている',
    '大皿、盛り合わせ＝platter。', f'''
{table(352)}
<g transform="translate(300 280)">
  <ellipse rx="200" ry="56" fill="#c9a464" class="o"/>
  <ellipse rx="170" ry="42" fill="#e0c48c" class="o"/>
  {''.join(f'<path d="M{-110+i*54} -10L{-80+i*54}-42l30 32z" fill="#f2dc8e" stroke="{INK}" stroke-width="2"/>' for i in range(4))}
  {''.join(f'<circle cx="{-90+i*60}" cy="10" r="12" class="coral o"/>' for i in range(3))}</g>''')

add('playground', 'ブランコとすべり台のある遊び場で、子どもが遊ぶ',
    '遊び場、校庭＝playground。', f'''
<path d="M0 320h600v80H0z" fill="#e8ddc9"/>
<g transform="translate(160 320)">
  <path d="M-70 0L0-140 70 0" fill="none" stroke="{MUTED}" stroke-width="11"/>
  <path d="M-60-120h120" stroke="{MUTED}" stroke-width="9" fill="none"/>
  {''.join(f'<path d="M{-30+i*60} -118v80" stroke="{BRN}" stroke-width="5" fill="none"/>' for i in range(2))}
  <path d="M-46-38h92v12h-92z" fill="{BRN}" class="o"/></g>
<g transform="translate(430 320)">
  <path d="M-70 0v-140h30V0z" fill="{MUTED}"/>
  <path d="M-40-140h30L90 0H60z" class="coral o"/>
  {''.join(f'<path d="M-70 {-30-i*30}h30" stroke="{BRN}" stroke-width="6" fill="none"/>' for i in range(3))}</g>
{person(290, 350, 0.8, 1, 'teal', 'blue', 'up', 'short', 'smile')}''')

add('plough', '刃のついたすきが土を掘り起こし、うねを作る',
    'すき、プラウ／耕す＝plough。', f'''
<path d="M0 250h600v150H0z" fill="#5b4636"/>
{''.join(f'<path d="M{{}} 400q30-70 0-140" fill="none" stroke="#3f3126" stroke-width="10"/>'.format(80 + i * 80) for i in range(4))}
<g transform="translate(380 250)">
  <path d="M-20-130h30v130h-30z" fill="#6b7680" class="o"/>
  <path d="M-20 0h30l50 50h-80z" fill="#8a97a3" class="o"/>
  <path d="M10-130l90-40" stroke="#6b7680" stroke-width="11" fill="none" stroke-linecap="round"/>
  <path d="M-50-90h70v20h-70z" fill="#6b7680" class="o"/></g>
{''.join(f'<path d="M{{}} 300q20 16 40 0" fill="none" stroke="#3f3126" stroke-width="4"/>'.format(60 + i * 90) for i in range(3))}''')

add('plywood', '薄い板を何層も貼り合わせた合板の断面が見える',
    '合板、ベニヤ板＝plywood。', f'''
{table(352)}
<g transform="translate(300 250)">
  <path d="M-200-60h400v90h-400z" fill="#e0c48c" class="o"/>
  <path d="M-200-60l40-30h400l-40 30z" fill="#f0dcb0" class="o"/>
  <path d="M200-60l40-30v90l-40 30z" fill="#c9a464" class="o"/>
  {''.join(f'<path d="M-200 {-46+i*22}h400" stroke="#c0a468" stroke-width="3" fill="none"/>' for i in range(4))}
  {''.join(f'<path d="M200 {-46+i*22}l40-30" stroke="#a88c50" stroke-width="3" fill="none"/>' for i in range(4))}</g>
{ring(420, 250, 0, True)}''')

add('policeman', '制帽をかぶった警察官が、手を挙げて交通を止める',
    '警察官(男性)＝policeman。', f'''
<path d="M0 340h600v60H0z" fill="#9aa7b1"/>
{''.join(f'<rect x="{{}}" y="350" width="46" height="50" fill="#fffefd"/>'.format(60 + i * 90) for i in range(6))}
<g transform="translate(300 340)">
  <path d="M-80 0v-160q80-34 160 0V0z" fill="#2f4a6b" class="o"/>
  <path d="M-80-160l-40 70M80-160q40 20 20 66" fill="none" stroke="#2f4a6b" stroke-width="24" stroke-linecap="round"/>
  <circle cx="0" cy="-206" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-42-212q6-26 42-26t42 26z" fill="#22364f" class="o"/>
  <path d="M-46-212h92v14h-92z" fill="#1a2a3d" class="o"/>
  <circle cx="-12" cy="-204" r="3.4" class="ink"/><circle cx="12" cy="-204" r="3.4" class="ink"/>
  <path d="M-10-186h20" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-50-120h34v34h-34z" class="goldp o"/></g>
{hand(400, 200, -1)}''')

add('polish', '布で靴をこすって磨き、つやが出る',
    '磨く、つや出し剤＝polish。', f'''
{table(352)}
<g transform="translate(300 290)">
  <path d="M-90 30q0-60 50-60h40l70 40v20z" fill="#5b3a20" class="o"/>
  <path d="M-90 30h160v14h-160z" fill="#3f2814"/>
  {''.join(spark(-20 + i * 40, -30 - (i % 2) * 20, 0.6, 'gold') for i in range(3))}</g>
<g transform="translate(180 220) rotate(-16)">
  <path d="M-40-30h80v60h-80z" class="goldp o"/>
  <path d="M-40 0h80" fill="none" stroke="{GLDD}" stroke-width="3"/></g>
<g transform="translate(470 300)">
  <path d="M-34-30h68v50a14 14 0 0 1-14 14h-40a14 14 0 0 1-14-14z" fill="#2f3542" class="o"/>
  <ellipse cy="-30" rx="34" ry="10" fill="#4e5a66" class="o"/></g>''')

add('postbox', '街角に立つ赤い円柱のポストに、手紙を入れる',
    '郵便ポスト＝postbox。', f'''
<path d="M0 340h600v60H0z" class="ground"/>
<g transform="translate(300 340)">
  <path d="M-70 0v-200h140V0z" class="coral o"/>
  <path d="M-70-200q70-50 140 0z" class="corald o"/>
  <path d="M-46-160h92v18h-92z" fill="#2f2620"/>
  <path d="M-50-60h100v40h-100z" class="corald o"/>
  <path d="M-70-20h140v20h-140z" class="corald o"/></g>
<g transform="translate(250 120) rotate(-16)">
  <path d="M-40-24h80v48h-80z" class="paper"/>
  <path d="M-40-24l40 26 40-26" fill="none" stroke="{MUTED}" stroke-width="3"/></g>
{line(270, 150, 292, 172, MUTED, True, 4)}''', arrow=True)

add('postcard', '片面に景色の写真、もう片面に切手と文面のあるはがき',
    'はがき、絵はがき＝postcard。', f'''
{table(352)}
<g transform="translate(180 260) rotate(-8)">
  <path d="M-100-70h200v140h-200z" class="paper"/>
  <path d="M-86-56h172v112h-172z" class="bluep o"/>
  <path d="M-86 30q60-60 100-10t72-20v56h-172z" class="green o"/>
  {sun(50, -24, 18)}</g>
<g transform="translate(410 250) rotate(6)">
  <path d="M-100-70h200v140h-200z" class="paper"/>
  <path d="M40-56h44v34H40z" class="coralp o"/>
  <path d="M0-56v112" fill="none" stroke="{MUTED}" stroke-width="3"/>
  {''.join(f'<rect x="-86" y="{-40+i*26}" width="{70-(i%2)*18}" height="8" rx="4" fill="{MUTED}"/>' for i in range(4))}
  {''.join(f'<rect x="16" y="{6+i*20}" width="68" height="8" rx="4" fill="{MUTED}"/>' for i in range(2))}</g>''')

add('postcode', '宛名書きの最後に、文字と数字の郵便番号が入る',
    '郵便番号＝postcode。', f'''
{table(352)}
<g transform="translate(300 250)">
  <path d="M-180-110h360v220h-360z" class="paper"/>
  <path d="M100-96h64v46h-64z" class="coralp o"/>
  {''.join(f'<rect x="-150" y="{-60+i*34}" width="{200-(i%3)*50}" height="12" rx="6" fill="{MUTED}"/>' for i in range(3))}
  <g transform="translate(-150 56)">
    {''.join(f'<rect x="{i*34}" y="0" width="26" height="34" rx="4" fill="none" stroke="{CRL}" stroke-width="4"/>' for i in range(6))}
    {''.join(f'<rect x="{i*34+6}" y="8" width="14" height="18" rx="3" fill="{CRL}"/>' for i in range(6))}</g></g>
{ring(240, 320, 0, True)}''')

add('postman', 'かばんを肩にかけた配達員が、家の郵便受けに手紙を入れる',
    '郵便配達員＝postman。', f'''
<path d="M0 340h600v60H0z" class="greenp"/>
{house(470, 340, 0.7, 'coral')}
<g transform="translate(390 320)">
  <path d="M-30-30h60v40h-60z" class="bluep o"/>
  <path d="M-30-30h60v10h-60z" class="blue"/></g>
{person(220, 350, 1.25, 1, 'blue', 'green', 'give', 'cap', 'smile')}
<g transform="translate(170 250)">
  <path d="M-50-30h100v70h-100z" fill="{BRN}" class="o"/>
  <path d="M-50-30q50-40 100 0" fill="none" stroke="#6a4020" stroke-width="6"/></g>
<g transform="translate(320 240) rotate(-10)">
  <path d="M-34-22h68v44h-68z" class="paper"/>
  <path d="M-34-22l34 22 34-22" fill="none" stroke="{MUTED}" stroke-width="3"/></g>''')

add('pothole', '舗装が抜けてできた道路の穴に、水がたまっている',
    '(道路の)くぼみ、穴＝pothole。', f'''
<path d="M0 200h600v200H0z" fill="#9aa7b1"/>
<path d="M0 190h600v14H0z" class="ground"/>
{''.join(f'<rect x="{{}}" y="290" width="60" height="12" fill="#fffefd"/>'.format(40 + i * 120) for i in range(5))}
<g transform="translate(300 260)">
  <path d="M-90 20q-30-50 20-64 70-20 120 6 40 22 10 58-70 26-150 0z" fill="#4e5a66" class="o"/>
  <path d="M-70 16q-16-30 20-38 56-14 96 4 26 14 4 34-52 18-120 0z" class="bluep"/></g>
{''.join(f'<path d="M{{}} {{}}l14-18" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(440 + i * 20, 200 - i * 16) for i in range(2))}''')

add('potter', '陶工が回るろくろの上で、粘土の器を形づくる',
    '陶芸家、陶工＝potter。', f'''
{table(352)}
<g transform="translate(320 300)">
  <path d="M-14 0v-60h28V0z" fill="#6b7680" class="o"/>
  <ellipse cy="-60" rx="90" ry="24" fill="#8a97a3" class="o"/>
  <path d="M-46-70q-6-70 46-84 52 14 46 84-46 22-92 0z" fill="#a2825e" class="o"/>
  <path d="M-30-120q30 16 60 0" fill="none" stroke="#8a6a46" stroke-width="4"/></g>
<g transform="translate(320 200)"><path d="M-90 0a90 30 0 1 0 40-26" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 9" marker-end="url(#ar)"/></g>
{hand(200, 230, 1)}
{hand(450, 230, -1)}''', arrow=True)

add('pottery', '焼き上がった陶器の器や皿が、棚に並んでいる',
    '陶器、陶芸＝pottery。', f'''
{table(352)}
<g transform="translate(300 300)">
  <path d="M-220-14h440v14h-440z" fill="#c9a464" class="o"/></g>
<g transform="translate(150 250)">
  <path d="M-46 36q-10-60 20-76 26-14 52 0 30 16 20 76z" fill="#b5744a" class="o"/>
  <path d="M-30-30q30 14 60 0" fill="none" stroke="#8a5232" stroke-width="4"/></g>
<g transform="translate(300 264)">
  <path d="M-56 22q0-50 56-50t56 50z" fill="#c8a05f" class="o"/>
  <ellipse cy="22" rx="56" ry="14" fill="#a8814a" class="o"/></g>
<g transform="translate(450 258)">
  <path d="M-40-40h80v60a20 20 0 0 1-20 20h-40a20 20 0 0 1-20-20z" fill="#8a9a7a" class="o"/>
  <path d="M40-24q30 0 30 22t-30 22" fill="none" stroke="#8a9a7a" stroke-width="10"/></g>''')

add('pram', '赤ん坊が横になれる深い乳母車を、押して歩く',
    '乳母車＝pram。', f'''
<path d="M0 340h600v60H0z" class="ground"/>
<g transform="translate(320 300)">
  <path d="M-110-40q0 70 110 70t110-70z" class="bluep o"/>
  <path d="M-110-40q0-70 110-70t110 70z" class="blue o"/>
  <path d="M-110-40h220" fill="none" stroke="{INK}" stroke-width="3"/>
  <circle cx="-70" cy="46" r="30" class="ink"/><circle cx="70" cy="46" r="30" class="ink"/>
  <circle cx="-70" cy="46" r="11" fill="#fffefd"/><circle cx="70" cy="46" r="11" fill="#fffefd"/>
  <path d="M110-40l60-50h50" fill="none" stroke="{MUTED}" stroke-width="9" stroke-linecap="round"/></g>
{person(490, 350, 1.05, -1, 'coral', 'green', 'reach', 'bun', 'smile')}
{head(300, 250, 18, 'coral', 'short')}''')

add('prune', 'はさみでバラの枝を切り、形を整える',
    '(枝を)刈りこむ、剪定する＝prune。', f'''
<path d="M0 330h600v70H0z" class="greenp"/>
<g transform="translate(300 330)">
  <path d="M-8 0v-90h16V0z" class="goldd"/>
  <path d="M0-80l-60-50M0-90l60-56M0-100v-50" fill="none" stroke="{BRN}" stroke-width="7"/>
  {''.join(flower(x, y, 0.5, 'coral') for x, y in [(-60, -140), (60, -152), (0, -158)])}
  <g opacity="0.3"><path d="M0-100l-100-40M0-110l106-20" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="9 8"/></g></g>
<g transform="translate(420 190) rotate(150)">
  <path d="M0 0l70-40M0 0l70 40" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <circle cx="84" cy="-48" r="14" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle cx="84" cy="48" r="14" fill="none" stroke="{INK}" stroke-width="7"/></g>''')

add('puddle', '雨上がりの道にできた浅い水たまりに、空が映る',
    '水たまり＝puddle。', f'''
<path d="M0 240h600v160H0z" fill="#9aa7b1"/>
<path d="M0 230h600v14H0z" class="ground"/>
<g transform="translate(300 310)">
  <path d="M-160 20q-40-50 20-64 90-22 170 4 60 20 20 60-100 22-210 0z" class="bluep o"/>
  <path d="M-120 10q-16-24 20-30 60-12 100 2" fill="none" stroke="#ffffff" stroke-width="5" opacity="0.8"/>
  {cloud(40, -4, 0.5, 'blue')}</g>
{''.join(f'<path d="M{{}} {{}}l-10 20" fill="none" stroke="{BLU}" stroke-width="4" stroke-linecap="round"/>'.format(120 + i * 90, 60 + (i % 2) * 30) for i in range(4))}''')

add('puppet', '糸で手足をつるした人形が、上の手で動かされる',
    'あやつり人形＝puppet。', f'''
{hand(300, 70, 1)}
<g transform="translate(300 120)">
  <path d="M-70-10h140v14h-140z" fill="{BRN}" class="o"/>
  <path d="M-10-40h20v34h-20z" fill="{BRN}" class="o"/></g>
{''.join(f'<path d="M{{}} 134L{{}} {{}}" fill="none" stroke="{MUTED}" stroke-width="2.5"/>'.format(240 + i * 40, 210 + i * 60, 220 + (i % 2) * 80) for i in range(4))}
<g transform="translate(300 290)">
  <circle cy="-70" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-34-78q4-38 34-38 30 0 34 36-18-16-34-8-18-10-34 10z" fill="{HAIR}"/>
  <circle cx="-11" cy="-70" r="3.4" class="ink"/><circle cx="11" cy="-70" r="3.4" class="ink"/>
  <path d="M-9-54q9 8 18 0" fill="none" stroke="{INK}" stroke-width="2.4"/>
  <path d="M-34-30h68v70h-68z" class="coral o"/>
  <path d="M-34-26l-40 20M34-26l40 20" stroke="{SKIN}" stroke-width="12" fill="none" stroke-linecap="round"/>
  <path d="M-20 40l-10 50M20 40l10 50" stroke="{BLUD}" stroke-width="13" fill="none" stroke-linecap="round"/></g>''')

add('puppy', '小さな子犬が、床の上でしっぽを振る',
    '子犬＝puppy。', f'''
<path d="M0 320h600v80H0z" class="ground"/>
<g transform="translate(310 290)">
  <ellipse rx="80" ry="50" fill="#c8a05f" class="o"/>
  <circle cx="70" cy="-36" r="42" fill="#c8a05f" class="o"/>
  <path d="M40-56q-24-20-14-46 26 8 34 32zM100-58q24-20 14-46-26 8-34 32z" fill="#a8814a" class="o"/>
  <circle cx="58" cy="-42" r="5" class="ink"/><circle cx="84" cy="-42" r="5" class="ink"/>
  <ellipse cx="72" cy="-22" rx="10" ry="7" fill="#5b4030"/>
  <path d="M62-10q10 10 20 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-50 42v30M-6 46v26M36 46v26" stroke="#c8a05f" stroke-width="14" fill="none" stroke-linecap="round"/>
  <path d="M-78-8q-40-10-40-44" fill="none" stroke="#c8a05f" stroke-width="11" stroke-linecap="round"/></g>
{''.join(f'<path d="M{{}} {{}}q14-14 0-28" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(200 + i * 20, 230 - i * 14) for i in range(2))}''')

add('quartz', '六角柱の先がとがった透明な水晶が、岩から伸びる',
    '石英、水晶＝quartz。', f'''
{table(352)}
<g transform="translate(300 300)">
  <path d="M-140 0q-20-50 30-60 90-20 160 6 50 20 20 54z" fill="#8a7a6a" class="o"/></g>
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><path d="M-26 0h52v-90l-26-40-26 40z" fill="#dff1f8" opacity="0.92" stroke="{INK}" stroke-width="3"/><path d="M0-130v130" stroke="#a8c8d8" stroke-width="3" fill="none"/></g>'.format(x, y, r) for x, y, r in [(250, 280, -12), (320, 270, 6), (380, 286, 20)])}
{''.join(spark(180 + i * 260, 150, 0.7, 'gold') for i in range(2))}''')

add('racket', '網を張った枠と柄のあるラケットと、ボール',
    'ラケット＝racket。', f'''
{table(352)}
<g transform="translate(280 230) rotate(24)">
  <ellipse rx="80" ry="100" fill="none" stroke="{TEAD}" stroke-width="14"/>
  {''.join(f'<path d="M{-58+i*24} -90v180" stroke="#fffefd" stroke-width="3" fill="none"/>' for i in range(6))}
  {''.join(f'<path d="M-74 {-72+i*24}h148" stroke="#fffefd" stroke-width="3" fill="none"/>' for i in range(7))}
  <ellipse rx="80" ry="100" fill="none" stroke="{TEAD}" stroke-width="14"/>
  <path d="M-14 100h28v110h-28z" fill="{BRN}" class="o"/></g>
<g transform="translate(470 300)">
  <circle r="30" class="green o"/>
  <path d="M-30 0q30-24 60 0M-30 0q30 24 60 0" fill="none" stroke="#fffefd" stroke-width="3"/></g>''')

add('raft', '板を並べて結んだいかだが、川を流れていく',
    'いかだ＝raft。', f'''
<path d="M0 250h600v150H0z" class="bluep"/>
{''.join(f'<path d="M{{}} 330q22-12 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(i * 88) for i in range(7))}
<g transform="translate(300 280)">
  {''.join(f'<rect x="{-160+i*40}" y="-16" width="34" height="32" rx="4" fill="#c9a464" stroke="{INK}" stroke-width="2.5"/>' for i in range(8))}
  <path d="M-166-6h332M-166 8h332" stroke="#8b6437" stroke-width="4" fill="none"/></g>
<g transform="translate(300 250)">{sit(0, 0, 0.85, 1, 'teal', 'blue', 'cap', 'smile', 'lap')}</g>
<g transform="translate(370 250) rotate(-30)">
  <path d="M-6-90h12v170h-6z" fill="{BRN}" class="o"/>
  <path d="M-6-90h12v170h-12z" fill="{BRN}" class="o"/>
  <path d="M-22 80q22 20 44 0-6-30-22-36-16 6-22 36z" fill="#c9a464" class="o"/></g>''')

add('railing', '並んだ縦の棒でできた柵が、道路ぞいに続く',
    '柵、手すり＝railing。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
<g transform="translate(300 300)">
  {''.join(f'<path d="M{-250+i*50} 0v-140" stroke="#6b7680" stroke-width="9" fill="none" stroke-linecap="round"/>' for i in range(11))}
  <path d="M-260-140h520M-260-80h520" stroke="#6b7680" stroke-width="11" fill="none" stroke-linecap="round"/>
  {''.join(f'<circle cx="{-250+i*50}" cy="-150" r="9" fill="#6b7680" class="o"/>' for i in range(11))}</g>
{hand(300, 140, 1)}''')

add('ramp', '段差をつなぐ斜めの通路を、車いすが上がる',
    '傾斜路、スロープ＝ramp。', f'''
<path d="M0 350h600v50H0z" class="ground"/>
<g transform="translate(420 350)">
  <path d="M-60 0v-90h180V0z" fill="{STONE}" class="o"/>
  <path d="M-60-90L-260 0h200z" fill="#b5bec4" class="o"/>
  <path d="M-260-14L-56-106" fill="none" stroke="{MUTED}" stroke-width="7"/></g>
<g transform="translate(230 290) rotate(-24)">
  <circle r="36" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle cx="36" cy="26" r="12" class="ink"/>
  <path d="M-10-30h34v40h-34z" class="teal o"/>
  <circle cx="6" cy="-52" r="18" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M24 4h30" stroke="{SKIN}" stroke-width="8" fill="none" stroke-linecap="round"/></g>
{arc(180, 240, 380, 190, 50, MUTED, True, 4)}''', arrow=True)

add('raven', '全身が黒く、太いくちばしをもつワタリガラスが枝に止まる',
    'ワタリガラス＝raven。', f'''
{''.join(cloud(120 + i * 340, 80, 1.0, 'blue') for i in range(2))}
<g transform="translate(300 270)">
  <path d="M-240 40h480v22h-480z" fill="{BRN}" class="o"/>
  <ellipse rx="80" ry="46" fill="#2f3542" class="o"/>
  <circle cx="64" cy="-40" r="32" fill="#2f3542" class="o"/>
  <path d="M92-48l44 10-44 14z" fill="#4e5a66" class="o"/>
  <circle cx="72" cy="-48" r="5" fill="#fffefd"/>
  <path d="M-80 6l-56-20 50 42z" fill="#2f3542" class="o"/>
  <path d="M-20 30q30 20 60 0" fill="none" stroke="#4e5a66" stroke-width="4"/>
  <path d="M-10 44v18M20 44v18" stroke="#4e5a66" stroke-width="7" fill="none" stroke-linecap="round"/></g>''')

add('reed', '水辺に細長いアシが群生し、穂が風に揺れる',
    'アシ、葦＝reed。', f'''
<path d="M0 280h600v120H0z" class="bluep"/>
{''.join(f'<g transform="translate({{}} 300) rotate({{}})"><path d="M0 60V-140" stroke="#7a9a4a" stroke-width="6" fill="none"/><ellipse cy="-160" rx="12" ry="34" fill="#8a6a46" class="o"/></g>'.format(70 + i * 50, -8 + (i % 3) * 6) for i in range(11))}
{''.join(f'<path d="M{{}} 330q22-12 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(i * 88) for i in range(7))}''')

add('reel', '糸を巻き取る円い道具が、釣りざおについている',
    '糸巻き、リール＝reel。', f'''
{table(352)}
<g transform="translate(300 250) rotate(-20)">
  <path d="M-200-6h400v12h-400z" fill="{BRN}" class="o"/></g>
<g transform="translate(240 268)">
  <circle r="56" fill="#8a97a3" class="o"/>
  <circle r="34" fill="#dfe6ea" class="o"/>
  <circle r="10" class="ink"/>
  <path d="M56 0h30" stroke="#8a97a3" stroke-width="9" fill="none"/>
  <circle cx="94" cy="0" r="12" fill="{BRN}" class="o"/></g>
<path d="M300 230q80 20 150 80" fill="none" stroke="{MUTED}" stroke-width="2.5"/>''')

add('reflector', '自転車の後ろの反射板が、光を受けて赤く輝く',
    '反射板＝reflector。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v400h-600z" fill="#2f3a4d"/></g>
<g transform="translate(330 300)">
  <circle cx="-130" cy="40" r="56" fill="none" stroke="#8a97a3" stroke-width="7"/>
  <path d="M-130 40L-30-30h80" fill="none" stroke="#4e6070" stroke-width="8" stroke-linecap="round"/>
  <path d="M-70-40h50l-10 20h-50z" fill="#4e6070"/></g>
<g transform="translate(210 300)">
  <rect x="-30" y="-18" width="60" height="36" rx="8" class="coral o"/>
  {''.join(f'<path d="M{-20+i*20} -14v28" stroke="{CRLD}" stroke-width="4" fill="none"/>' for i in range(3))}</g>
{''.join(f'<path d="M{int(210+52*math.cos(math.radians(a)))} {int(300+52*math.sin(math.radians(a)))}l{int(28*math.cos(math.radians(a)))} {int(28*math.sin(math.radians(a)))}" stroke="{CRL}" stroke-width="6" fill="none" stroke-linecap="round"/>' for a in (-150, -120, -90, -60, -30, 180))}''')

add('refrigerator', '扉を開けた冷蔵庫の中に、食品が段ごとに並ぶ',
    '冷蔵庫＝refrigerator。', f'''
<g transform="translate(300 210)">
  <path d="M-120-170h240v340h-240z" fill="#dfe6ea" class="o"/>
  <path d="M-96-146h192v90h-192z" fill="#eef4f7" class="o"/>
  <path d="M-96-40h192v186h-192z" fill="#eef4f7" class="o"/>
  {''.join(f'<path d="M-96 {10+i*50}h192" stroke="{MUTED}" stroke-width="4" fill="none"/>' for i in range(3))}
  {''.join(f'<rect x="{-80+ (i%4)*46}" y="{-26+(i//4)*50}" width="34" height="30" rx="4" fill="{c}" stroke="{INK}" stroke-width="2"/>' for i, c in enumerate(['#dff4ef','#fde9e3','#fff0c5','#e1edfb','#e1f3e5','#eee8fb','#dff4ef','#fde9e3']))}
  <path d="M104-140v70M104-30v80" stroke="{MUTED}" stroke-width="9" fill="none" stroke-linecap="round"/></g>''')

add('reindeer', '枝分かれした角をもつトナカイが、雪の上に立つ',
    'トナカイ＝reindeer。', f'''
<path d="M0 320h600v80H0z" fill="#eef4f7"/>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="3" fill="#ffffff" stroke="{MUTED}" stroke-width="1.2"/>'.format(60 + (i * 83) % 500, 60 + (i * 37) % 200) for i in range(9))}
<g transform="translate(300 260)">
  <ellipse rx="100" ry="52" fill="#8a6a46" class="o"/>
  <path d="M84-26q26-50 54-32 22 14 4 46-12 22-38 20z" fill="#8a6a46" class="o"/>
  <path d="M104-62q-36-14-36-48 24 2 36 20 4-22 22-26-6 20 6 32zM152-66q36-14 36-48-24 2-36 20-4-22-22-26 6 20-6 32z" fill="#c8a05f" class="o"/>
  <circle cx="124" cy="-32" r="5" class="ink"/>
  <circle cx="150" cy="-10" r="11" class="coral o"/>
  <path d="M-62 46v46M-14 50v42M32 50v42M76 44v48" stroke="#8a6a46" stroke-width="14" fill="none" stroke-linecap="round"/>
  <path d="M-100-8q-30-8-26-38" fill="none" stroke="#8a6a46" stroke-width="10" stroke-linecap="round"/></g>''')

add('reservoir', 'ダムでせき止められた広い水面が、山あいに広がる',
    '貯水池、ダム湖＝reservoir。', f'''
<path d="M0 200h600v200H0z" class="greenp"/>
<path d="M0 180L140 60l90 70 110-90 120 100" fill="#d8cdb6" class="o"/>
<path d="M0 200h380v130H0z" class="bluep o"/>
{''.join(f'<path d="M{{}} 250q22-12 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(i * 80) for i in range(5))}
<g transform="translate(400 260)">
  <path d="M-24-100q30 100 0 170h60q-30-70 0-170z" fill="{STONE}" class="o"/>
  <path d="M-24-100h60v14h-60z" fill="#9aa7b1"/></g>
{''.join(f'<path d="M{{}} 300q30 20 60 0" fill="none" stroke="{BLU}" stroke-width="0"/>'.format(x) for x in (0,))}''')

add('rhino', '鼻の上に太い角をもつサイが、厚い皮膚で立つ',
    'サイ＝rhino。', f'''
<path d="M0 320h600v80H0z" class="greenp"/>
<g transform="translate(300 260)">
  <ellipse rx="130" ry="64" fill="#9aa0a4" class="o"/>
  <path d="M110-30q30-44 58-26 24 16 4 48-14 22-40 20z" fill="#9aa0a4" class="o"/>
  <path d="M158-50q10-40 26-44-2 30-8 46z" fill="#d8d2c4" class="o"/>
  <path d="M138-38q6-22 16-26-2 18-6 28z" fill="#d8d2c4" class="o"/>
  <circle cx="130" cy="-26" r="5" class="ink"/>
  <path d="M100-56l-4-24 22 14z" fill="#9aa0a4" class="o"/>
  <path d="M-80 58v42M-26 62v38M28 62v38M80 56v44" stroke="#9aa0a4" stroke-width="19" fill="none" stroke-linecap="round"/>
  <path d="M-128-6q-34-8-32-38" fill="none" stroke="#9aa0a4" stroke-width="10" stroke-linecap="round"/></g>''')

add('rim', 'グラスの上のふちだけが、輪になって強調される',
    '(器や車輪の)縁、ふち＝rim。', f'''
{table(352)}
<g transform="translate(300 250)">
  <path d="M-70-90l14 190h112l14-190z" fill="#e6f2f6" opacity="0.9" stroke="{INK}" stroke-width="3"/>
  <path d="M-58-20h116l10 120h-136z" class="bluep"/>
  <path d="M-70-90l14 190h112l14-190z" fill="none" class="o"/>
  <ellipse cy="-90" rx="70" ry="18" fill="none" stroke="{CRL}" stroke-width="9"/></g>
{''.join(f'<path d="M{{}} {{}}h-60" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>'.format(490, 160) for _ in range(1))}''', arrow=True)

add('rind', 'チーズの外側のかたい皮が、中身と切り分けられる',
    '(果物・チーズなどの)厚い外皮＝rind。', f'''
{table(352)}
<g transform="translate(300 270)">
  <path d="M-130 40L-130-20 0-70v60z" fill="#f2dc8e" class="o"/>
  <path d="M0-10l130 30v40L0 40z" fill="#e0c86a" class="o"/>
  <path d="M-130-20L0-70l130 50L0 30z" fill="#f8ecb8" class="o"/>
  <path d="M-130-20L0-70l130 50" fill="none" stroke="#c8a440" stroke-width="12"/>
  <path d="M-130 40V-20" stroke="#c8a440" stroke-width="12" fill="none"/>
  <path d="M130 20v50" stroke="#c8a440" stroke-width="12" fill="none"/></g>
{''.join(f'<path d="M{{}} {{}}h-60" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>'.format(520, 180) for _ in range(1))}''', arrow=True)

add('roller', '塗料をつけたローラーで、壁を一気に塗っていく',
    'ローラー、転がす筒＝roller。', f'''
<g transform="translate(300 200)"><path d="M-280-180h560v360h-560z" fill="#e4dccb" class="o"/></g>
<path d="M60 40h200v320H60z" class="tealp"/>
<g transform="translate(300 200) rotate(-10)">
  <path d="M-80-30h160v60h-160z" fill="#c3cbd1" class="o"/>
  <path d="M-80-30h160v14h-160z" fill="#9aa7b1"/>
  <path d="M0 30v40h90" fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round"/>
  <path d="M90 70h60" stroke="{BRN}" stroke-width="16" fill="none" stroke-linecap="round"/></g>
{''.join(f'<path d="M{{}} {{}}h-60" fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"/>'.format(230, 120 + i * 40) for i in range(2))}''', arrow=True)

finish(__file__)
