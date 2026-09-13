# -*- coding: utf-8 -*-
"""第189回。plus37 の50語。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

add('chopping board', '木のまな板の上で、包丁が野菜を切っている',
    'まな板＝chopping board。', f'''
{table(352)}
<g transform="translate(300 290)">
  <path d="M-160-40h300v80h-300z" fill="#c9a464" class="o"/>
  <path d="M140-20h40v40h-40z" fill="#c9a464" class="o"/>
  <circle cx="164" cy="0" r="9" fill="#fffaf1" class="o"/>
  {''.join(f'<path d="M{-130+i*60} -40v80" stroke="#a0764a" stroke-width="3" fill="none"/>' for i in range(5))}</g>
{''.join(f'<circle cx="{{}}" cy="262" r="18" class="green o"/>'.format(180 + i * 44) for i in range(3))}
<g transform="translate(360 200) rotate(-20)">
  <path d="M-80-18h160l14 18-14 18h-160z" fill="#c3cbd1" class="o"/>
  <path d="M80-18h70v36H80z" fill="{BRN}" class="o"/></g>''')

add('roommate', '同じ部屋の二つの机で、それぞれが自分のことをする',
    '同室の相手、ルームメイト＝roommate。', f'''
<g transform="translate(300 200)"><path d="M-280-170h560v340h-560z" fill="#f6efe1" class="o"/></g>
<path d="M300 40v300" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="12 10"/>
{''.join(f'<g transform="translate({{}} 330)"><path d="M-70-40h140v14h-140z" fill="#c9a464" class="o"/><path d="M-56-26v40M56-26v40" stroke="{BRN}" stroke-width="8" fill="none"/></g>'.format(160 + i * 280) for i in range(2))}
{sit(160, 290, 1.0, 1, 'teal', 'blue', 'short', 'smile', 'lap')}
{sit(440, 290, 1.0, 1, 'coral', 'green', 'bob', 'smile', 'lap')}
{''.join(f'<g transform="translate({{}} 200)"><path d="M-60-46h120v92h-120z" fill="#fffefd" class="o"/></g>'.format(160 + i * 280) for i in range(2))}''')

add('rosebush', 'とげのある枝にバラの花が咲いた茂みが、庭に立つ',
    'バラの木、バラの茂み＝rosebush。', f'''
<path d="M0 320h600v80H0z" class="greenp"/>
<g transform="translate(300 320)">
  <path d="M-6 0v-70h12V0z" class="goldd"/>
  <path d="M0-60l-80-60M0-70l80-64M0-80v-70" fill="none" stroke="#3f8f6a" stroke-width="7"/>
  {''.join(f'<path d="M{x} {y}l{dx} {dy}" stroke="#2a6b4c" stroke-width="4" fill="none"/>' for x, y, dx, dy in [(-40, -90, -8, -10), (40, -96, 8, -10), (-10, -120, -10, -6), (16, -110, 10, -6)])}
  {''.join(flower(x, y, 0.62, 'coral') for x, y in [(-84, -128), (84, -140), (0, -160)])}
  {''.join(f'<ellipse cx="{x}" cy="{y}" rx="20" ry="12" class="green o" transform="rotate({r} {x} {y})"/>' for x, y, r in [(-50, -70, -20), (50, -76, 20), (-16, -40, -10)])}</g>''')

add('rotor', 'ヘリコプターの上で、細長い回転翼が回る',
    '回転翼、ローター＝rotor。', f'''
{''.join(cloud(120 + i * 340, 90, 1.0, 'blue') for i in range(2))}
<g transform="translate(300 270)">
  <path d="M-100-40q0-50 100-50t100 50v50h-200z" class="teal o"/>
  <path d="M-100 10h200v34h-200z" class="teald o"/>
  <path d="M-60-56h80v40h-80z" fill="#dfeaf2" class="o"/>
  <path d="M100-10l110 26v20l-110-10z" class="teal o"/>
  <path d="M200 16v-50" stroke="{TEAD}" stroke-width="9" fill="none"/>
  <path d="M-70 44v30h140v-30" fill="none" stroke="{MUTED}" stroke-width="9"/>
  <path d="M-90 74h180" stroke="{MUTED}" stroke-width="9" fill="none" stroke-linecap="round"/></g>
<g transform="translate(300 180)">
  <path d="M0-10v-30" stroke="{MUTED}" stroke-width="10" fill="none"/>
  <path d="M-230-46h460v14h-460z" fill="#6b7680" class="o"/>
  <path d="M-180-70h360v12h-360z" fill="#8a97a3" class="o" opacity="0.6"/></g>
<g transform="translate(300 96)"><path d="M-70 0q70-26 140 0" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/></g>''', arrow=True)

add('rowboat', 'オールの二本ついた小舟を、湖の上でこぐ',
    '手こぎボート＝rowboat。', f'''
<path d="M0 260h600v140H0z" class="bluep"/>
{''.join(f'<path d="M{{}} 300q22-12 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(i * 88) for i in range(7))}
<g transform="translate(300 280)">
  <path d="M-160 0q0 40 160 40t160-40q-60-24-160-24T-160 0z" class="coral o"/>
  <path d="M-130-4q130-16 260 0" fill="none" stroke="{CRLD}" stroke-width="4"/>
  <path d="M-60-6h120v10h-120z" fill="{CRLD}"/></g>
{sit(300, 250, 0.85, 1, 'teal', 'blue', 'cap', 'smile', 'lap')}
{''.join(f'<g transform="translate(300 254) rotate({{}})"><path d="M-6-10h12v150h-12z" fill="{BRN}" class="o"/><path d="M-20 140q20 22 40 0-6-32-20-38-14 6-20 38z" fill="#c9a464" class="o"/></g>'.format(r) for r in (-56, 56))}''')

add('rowing', '二人がそろってオールを引き、細長い艇を進める',
    'ボートこぎ、ローイング＝rowing。', f'''
<path d="M0 250h600v150H0z" class="bluep"/>
{''.join(f'<path d="M{{}} 300q22-12 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(i * 88) for i in range(7))}
<g transform="translate(300 290)">
  <path d="M-250 0q0 26 250 26t250-26q-120-20-250-20T-250 0z" fill="#f6efe1" class="o"/></g>
{''.join(sit(240 + i * 110, 270, 0.78, 1, c, 'blue', 'cap', 'flat', 'up') for i, c in enumerate(['teal', 'coral']))}
{''.join(f'<g transform="translate({{}} 274) rotate(-40)"><path d="M-6-10h12v130h-12z" fill="{BRN}" class="o"/><path d="M-18 120q18 20 36 0-6-28-18-34-12 6-18 34z" fill="#c9a464" class="o"/></g>'.format(240 + i * 110) for i in range(2))}
{arc(120, 210, 300, 200, 50, MUTED, True, 5)}''', arrow=True)

add('ruby', '深い赤の宝石が、指輪の台にはめこまれている',
    'ルビー、紅玉＝ruby。', f'''
{table(352)}
<g transform="translate(300 270)">
  <ellipse cy="40" rx="90" ry="26" fill="none" stroke="{GLD}" stroke-width="14"/>
  <path d="M-56-40h112l-20-40h-72z" class="coral o"/>
  <path d="M-56-40h112l-30 60h-52z" class="corald o"/>
  <path d="M-36-40l14-40M36-40l-14-40M-22 20l10-60M22 20l-10-60" fill="none" stroke="#fdece8" stroke-width="3"/></g>
{''.join(spark(160 + i * 280, 140, 0.8, 'gold') for i in range(2))}''')

add('rucksack', '肩ひもと胸ベルトのついた大きなリュックが立つ',
    'リュックサック＝rucksack。', f'''
{table(352)}
<g transform="translate(300 250)">
  <path d="M-90-80h180v190h-180z" fill="#3f6b4a" class="o"/>
  <path d="M-90-80q90-46 180 0" fill="none" stroke="#2a5234" stroke-width="6"/>
  <path d="M-60-80q-34-56 0-76 22-14 44 0M60-80q34-56 0-76-22-14-44 0" fill="none" stroke="#2a5234" stroke-width="10"/>
  <path d="M-60 20h120v50h-120z" fill="#2a5234" class="o"/>
  <path d="M-16-40h32v24h-32z" class="goldd o"/>
  <path d="M-90 0h180" fill="none" stroke="#2a5234" stroke-width="5"/>
  <path d="M-30-110h60v14h-60z" fill="#2a5234" class="o"/></g>''')

add('ruler', '目盛りのついた直定規を当て、まっすぐな線を引く',
    '定規、ものさし＝ruler。', f'''
{table(352)}
<g transform="translate(300 260)">
  <path d="M-200-90h400v180h-400z" class="paper"/>
  <path d="M-160 40h320" fill="none" stroke="{INK}" stroke-width="5"/></g>
<g transform="translate(300 240)">
  <path d="M-200-26h400v52h-400z" fill="#f0e6d2" class="o"/>
  {''.join(f'<path d="M{-180+i*36} -26v{18 if i%2 else 26}" stroke="{INK}" stroke-width="3" fill="none"/>' for i in range(11))}</g>
<g transform="translate(420 190) rotate(34)">
  <path d="M-8-70h16v100l-8 20-8-20z" class="teal o"/></g>''')

add('rung', 'はしごの横木に足をかけて、一段ずつ上る',
    'はしごの横木、段＝rung。', f'''
<path d="M0 360h600v40H0z" class="ground"/>
<g transform="translate(300 360) rotate(-10)">
  <path d="M-70 0v-330M70 0v-330" stroke="{BRN}" stroke-width="16" fill="none" stroke-linecap="round"/>
  {''.join(f'<path d="M-70 {-40-i*56}h140" stroke="{BRN}" stroke-width="13" fill="none" stroke-linecap="round"/>' for i in range(5))}</g>
{ring(290, 260, 62, True)}
<g transform="translate(270 260)"><path d="M-40 20q0-40 34-40h18l30 24v16z" fill="{INK}"/></g>''')

add('runway', '空港の長い滑走路に、白い中心線が続き機体が並ぶ',
    '滑走路＝runway。', f'''
<path d="M0 200h600v200H0z" class="greenp"/>
<path d="M0 240h600v120H0z" fill="#6b7680"/>
{''.join(f'<rect x="{{}}" y="294" width="60" height="12" fill="#fffefd"/>'.format(30 + i * 100) for i in range(6))}
<g transform="translate(360 260) rotate(-4)">{plane(0, 0, 0.6, 0, 'teal')}</g>
{''.join(f'<path d="M{{}} 250v-24" stroke="#fffefd" stroke-width="5" fill="none"/>'.format(60 + i * 120) for i in range(5))}
{''.join(cloud(120 + i * 340, 90, 0.9, 'blue') for i in range(2))}''')

add('salt', 'ふたに穴のあいた容器から、白い粒がふりかけられる',
    '塩＝salt。', f'''
{table(352)}
<g transform="translate(280 260) rotate(24)">
  <path d="M-40-50h80v100a20 20 0 0 1-20 20h-40a20 20 0 0 1-20-20z" fill="#e6f2f6" opacity="0.9" stroke="{INK}" stroke-width="3"/>
  <path d="M-34-10h68v56a18 18 0 0 1-18 18h-32a18 18 0 0 1-18-18z" fill="#fffefd"/>
  <path d="M-34-72q34-16 68 0v22h-68z" fill="#9aa7b1" class="o"/>
  {''.join(f'<circle cx="{-18+i*18}" cy="-62" r="4" fill="#fffaf1"/>' for i in range(3))}</g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="4" fill="#fffefd" stroke="{MUTED}" stroke-width="1.5"/>'.format(360 + (i * 23) % 70, 210 + (i * 31) % 110) for i in range(12))}
<g transform="translate(420 320)"><ellipse rx="70" ry="16" fill="#fffefd" class="o"/></g>''')

add('sandpaper', 'ざらざらした紙で木の表面をこすり、なめらかにする',
    '紙やすり＝sandpaper。', f'''
{table(352)}
<g transform="translate(300 300)">
  <path d="M-210-30h420v50h-420z" fill="#e0c48c" class="o"/>
  <path d="M-210-30h180v50h-180z" fill="#f2e2c4"/></g>
<g transform="translate(340 240) rotate(-6)">
  <path d="M-90-30h180v60h-180z" fill="#b98a58" class="o"/>
  {''.join(f'<circle cx="{-76+ (i%9)*19}" cy="{-18+(i//9)*19}" r="2.6" fill="#6a4a2a"/>' for i in range(27))}</g>
{hand(340, 170, 1)}
{''.join(f'<path d="M{{}} {{}}h50" fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"/>'.format(450, 240) for _ in range(1))}''', arrow=True)

add('sandwich', 'パンに具をはさんで、斜めに切ったサンドイッチ',
    'サンドイッチ＝sandwich。', f'''
{table(352)}
<g transform="translate(230 280) rotate(-6)">
  <path d="M-90 40L0-60l90 100z" fill="#e0b872" class="o"/>
  <path d="M-64 14L0-58l64 72z" fill="#fdf3c8" class="o"/>
  <path d="M-50 0q50-14 100 0" fill="none" stroke="#4e986a" stroke-width="8"/>
  <path d="M-40 14q40-10 80 0" fill="none" stroke="#e86452" stroke-width="8"/></g>
<g transform="translate(410 300) rotate(10)">
  <path d="M-80 30L0-60l80 90z" fill="#e0b872" class="o"/>
  <path d="M-58 8L0-58l58 66z" fill="#fdf3c8" class="o"/>
  <path d="M-44-4q44-12 88 0" fill="none" stroke="#4e986a" stroke-width="7"/></g>''')

add('sapphire', '深い青の宝石が、まわりを小さな石に囲まれる',
    'サファイア＝sapphire。', f'''
{table(352)}
<g transform="translate(300 260)">
  <ellipse cy="54" rx="90" ry="26" fill="none" stroke="{GLD}" stroke-width="14"/>
  <path d="M-56-40h112l-20-40h-72z" class="blue o"/>
  <path d="M-56-40h112l-30 60h-52z" class="blued o"/>
  <path d="M-36-40l14-40M36-40l-14-40M-22 20l10-60M22 20l-10-60" fill="none" stroke="#e6f0fb" stroke-width="3"/>
  {''.join(f'<circle cx="{-90+i*180}" cy="-20" r="12" fill="#fffefd" stroke="{GLD}" stroke-width="3"/>' for i in range(2))}</g>
{''.join(spark(160 + i * 280, 140, 0.8, 'gold') for i in range(2))}''')

add('saucer', 'カップの下に受け皿が置かれ、そろって一組になる',
    '受け皿、ソーサー＝saucer。', f'''
{table(352)}
<g transform="translate(300 280)">
  <ellipse rx="120" ry="34" fill="#fffefd" class="o"/>
  <ellipse rx="76" ry="20" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M-56-90h112v58a30 30 0 0 1-30 30h-52a30 30 0 0 1-30-30z" fill="#fffefd" class="o"/>
  <path d="M56-70q40 0 40 32t-40 32" fill="none" stroke="{INK}" stroke-width="9"/>
  <path d="M-46-80h92v40a24 24 0 0 1-24 24h-44a24 24 0 0 1-24-24z" fill="#7a4a28"/></g>
{ring(300, 292, 130, True)}''')

add('sawdust', 'のこぎりで木を切ると、細かい木の粉が下にたまる',
    'おがくず＝sawdust。', f'''
{table(352)}
<g transform="translate(300 280)">
  <path d="M-180-30h360v40h-360z" fill="#c9a464" class="o"/></g>
<g transform="translate(320 190) rotate(-6)">
  <path d="M-110-16h220l-6 32h-214z" fill="#c3cbd1" class="o"/>
  {''.join(f'<path d="M{-100+i*22} 16l10 14 10-14z" fill="#c3cbd1" stroke="{INK}" stroke-width="1.5"/>' for i in range(10))}
  <path d="M110-20h60v40h-60z" fill="{BRN}" class="o"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="#e8d2a8" stroke="{INK}" stroke-width="1.2"/>'.format(200 + (i * 37) % 200, 320 + (i * 23) % 30, 4 + i % 3) for i in range(20))}''')

add('saxophone', '金色に曲がった管の楽器を、手で支えて吹く',
    'サクソフォン＝saxophone。', f'''
{table(352)}
<g transform="translate(300 240)">
  <path d="M20-140q40 40 20 120-16 66-70 66-56 0-56-56 0-40 40-50" fill="none" stroke="{GLD}" stroke-width="24" stroke-linecap="round"/>
  <path d="M-46 108q-40-6-40-40 0-30 30-34" fill="none" stroke="{GLD}" stroke-width="24" stroke-linecap="round"/>
  <path d="M-86 74q-40 10-40 40 0 36 50 36 60 0 76-40" fill="none" stroke="{GLD}" stroke-width="0"/>
  <path d="M20-140h30v-20H10z" fill="#2f3542" class="o"/>
  {''.join(f'<circle cx="{14-i*8}" cy="{-100+i*40}" r="9" class="goldd o"/>' for i in range(4))}
  <path d="M-56 130q-44 0-44-44" fill="none" stroke="{GLD}" stroke-width="24" stroke-linecap="round"/>
  <path d="M-100 86q0-40 44-44" fill="none" stroke="{GLD}" stroke-width="0"/>
  <path d="M-90 116q-50 26-30 60 20 30 70 6" fill="none" stroke="{GLD}" stroke-width="0"/>
  <ellipse cx="-60" cy="150" rx="54" ry="26" fill="{GLDP}" stroke="{INK}" stroke-width="3" transform="rotate(-20 -60 150)"/></g>''')

add('scaffold', '建物の外側に、金属の足場が組み上げられている',
    '足場、やぐら＝scaffold。', f'''
<path d="M0 360h600v40H0z" class="ground"/>
<g transform="translate(360 360)">
  <path d="M-110 0v-300h220V0z" fill="#fffdf6" class="o"/>
  {''.join(f'<rect x="{-80+ (i%3)*60}" y="{-270+(i//3)*70}" width="40" height="40" class="tealp o"/>' for i in range(9))}</g>
<g transform="translate(300 360)">
  {''.join(f'<path d="M{-150+i*100} 0v-320" stroke="#8a97a3" stroke-width="9" fill="none"/>' for i in range(4))}
  {''.join(f'<path d="M-150 {-60-i*70}h300" stroke="#8a97a3" stroke-width="9" fill="none"/>' for i in range(4))}
  {''.join(f'<path d="M-150 {-60-i*70}l100-70M-50 {-60-i*70}l100-70M50 {-60-i*70}l100-70" stroke="#b5bec4" stroke-width="4" fill="none"/>' for i in range(3))}
  {''.join(f'<path d="M-150 {-54-i*70}h300v10h-300z" fill="#c9a464"/>' for i in range(4))}</g>''')

add('scarecrow', '十字に組んだ棒に服を着せた案山子が、畑に立つ',
    'かかし＝scarecrow。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
{''.join(f'<g transform="translate({{}} 330)"><path d="M0 0v-50" stroke="{GLDD}" stroke-width="5" fill="none"/><ellipse cy="-58" rx="10" ry="18" class="gold o"/></g>'.format(60 + i * 60) for i in range(4))}
<g transform="translate(330 330)">
  <path d="M-8 0v-200h16V0z" fill="{BRN}" class="o"/>
  <path d="M-110-150h220v16h-220z" fill="{BRN}" class="o"/>
  <path d="M-70-140h140v130h-140z" class="coral o"/>
  <path d="M-70-140l-46 6 6 60 30-10M70-140l46 6-6 60-30-10" class="coral o"/>
  <circle cy="-190" r="34" fill="#e0c48c" class="o"/>
  <path d="M-40-200q40-40 80 0z" fill="#c9a464" class="o"/>
  <path d="M-50-198h100v12h-100z" fill="#c9a464" class="o"/>
  <circle cx="-12" cy="-190" r="4" class="ink"/><circle cx="12" cy="-190" r="4" class="ink"/>
  <path d="M-12-172q12 10 24 0" fill="none" stroke="{INK}" stroke-width="3"/>
  {''.join(f'<path d="M{-100+i*14} -128l-8 18" stroke="#e0c48c" stroke-width="4" fill="none"/>' for i in range(4))}</g>''')

add('scooter', 'ハンドルつきの板に片足を乗せ、もう片足で地面をける',
    'キックスケーター、スクーター＝scooter。', f'''
<path d="M0 350h600v50H0z" class="ground"/>
<g transform="translate(320 350)">
  <path d="M-110-20h180v16h-180z" fill="{TEA}" class="o"/>
  <circle cx="-110" cy="-6" r="22" class="ink"/>
  <circle cx="70" cy="-6" r="22" class="ink"/>
  <path d="M70-20v-140" stroke="{TEAD}" stroke-width="11" fill="none" stroke-linecap="round"/>
  <path d="M30-160h80" stroke="{INK}" stroke-width="11" fill="none" stroke-linecap="round"/></g>
{person(280, 330, 1.0, 1, 'coral', 'blue', 'reach', 'cap', 'smile')}''')

add('scorpion', '尾を持ち上げ、はさみを広げたサソリが砂の上にいる',
    'サソリ＝scorpion。', f'''
<path d="M0 250h600v150H0z" fill="#e8d8b0"/>
<g transform="translate(300 290)">
  <ellipse rx="60" ry="34" fill="#8a5c2b" class="o"/>
  <path d="M-56-10q-50-26-70-6-16 16 10 30 20 10 40-6z" fill="#8a5c2b" class="o"/>
  <path d="M-56 14q-50 26-70 6-16-16 10-30 20-10 40 6z" fill="#8a5c2b" class="o"/>
  <path d="M-120-16q-30-16-40 0 14 14 30 10zM-120 22q-30 16-40 0 14-14 30-10z" fill="#8a5c2b" class="o"/>
  <path d="M56 0q50 0 66-40 16-40-10-58-24-14-30 16" fill="none" stroke="#8a5c2b" stroke-width="18" stroke-linecap="round"/>
  <path d="M78-92l-8-26 26 12z" fill="#8a5c2b" class="o"/>
  {''.join(f'<path d="M{-30+i*24} 32l{-10+i*6} 34" stroke="#8a5c2b" stroke-width="6" fill="none" stroke-linecap="round"/>' for i in range(4))}
  {''.join(f'<path d="M{-30+i*24} -32l{-10+i*6}-34" stroke="#8a5c2b" stroke-width="6" fill="none" stroke-linecap="round"/>' for i in range(4))}</g>''')

add('scrapbook', '切り抜きと写真を貼り集めた帳面が開いている',
    'スクラップブック、切り抜き帳＝scrapbook。', f'''
{table(352)}
<g transform="translate(300 250)">
  <path d="M-180-110h170v220h-170zM10-110h170v220H10z" class="paper"/>
  <path d="M-14-116h28v232h-28z" class="corald o"/>
  <g transform="rotate(-8)"><path d="M-160-80h110v70h-110z" class="tealp o"/></g>
  {''.join(f'<rect x="-160" y="{10+i*26}" width="{110-(i%2)*30}" height="10" rx="5" fill="{MUTED}" transform="rotate(-4 -160 {10+i*26})"/>' for i in range(3))}
  <g transform="rotate(6)"><path d="M40-80h120v60H40z" class="goldp o"/></g>
  <g transform="rotate(-4)"><path d="M40 10h110v80H40z" class="violetp o"/></g></g>''')

add('scrub', 'ブラシに力を込めて、床の汚れをこすり落とす',
    'ごしごし洗う、こする＝scrub。', f'''
{table(352)}
<g transform="translate(300 300)">
  <path d="M-220-30h440v50h-440z" fill="#dfe6ea" class="o"/>
  <g opacity="0.5"><path d="M60-20q40 20 90 0" fill="none" stroke="#b5744a" stroke-width="12"/></g></g>
<g transform="translate(230 250) rotate(-10)">
  <path d="M-60-24h120v34h-120z" fill="{BRN}" class="o"/>
  {''.join(f'<path d="M{-50+i*14} 10v22" stroke="#8a97a3" stroke-width="5" fill="none"/>' for i in range(8))}</g>
{hand(230, 190, 1)}
{''.join(f'<path d="M{{}} {{}}h50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" marker-end="url(#ar)"/>'.format(320, 220 + i * 26) for i in range(2))}
{''.join(f'<path d="M{{}} {{}}h-50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" marker-end="url(#ar)"/>'.format(320, 233 + i * 26) for i in range(2))}''', arrow=True)

add('dustpan', 'ほうきで掃いたごみを、平たい受け皿に入れる',
    'ちり取り＝dustpan。', f'''
{table(352)}
<g transform="translate(340 300)">
  <path d="M-90 0h180v-40l-24-30h-132z" fill="{TEA}" class="o"/>
  <path d="M-90 0h180v14h-180z" class="teald o"/>
  <path d="M66-70h40v-16H66z" class="teald o"/></g>
<g transform="translate(180 220) rotate(24)">
  <path d="M-8-110h16v130h-16z" fill="{BRN}" class="o"/>
  <path d="M-34 20q34 46 68 0z" fill="#c9a464" class="o"/>
  {''.join(f'<path d="M{-26+i*13} 40v30" stroke="#c9a464" stroke-width="5" fill="none"/>' for i in range(5))}</g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="{MUTED}"/>'.format(250 + (i * 23) % 70, 290 + (i * 17) % 20, 4 + i % 3) for i in range(6))}''')

add('seagull', '白い体に灰色の翼のカモメが、浜辺で羽を広げる',
    'カモメ＝seagull。', f'''
<path d="M0 300h600v100H0z" fill="#f0e0b8"/>
<path d="M0 290h600v20H0z" class="bluep"/>
<g transform="translate(300 260)">
  <ellipse rx="76" ry="42" fill="#fffefd" class="o"/>
  <circle cx="64" cy="-34" r="30" fill="#fffefd" class="o"/>
  <path d="M90-38l34 8-34 12z" class="gold o"/>
  <circle cx="72" cy="-42" r="4" class="ink"/>
  <path d="M-20-20q60-56 120-20-50 4-80 34z" fill="#b5bec4" class="o"/>
  <path d="M-76 0l-60-16 54 34z" fill="#b5bec4" class="o"/>
  <path d="M-16 38v22M16 38v22" stroke="{GLDD}" stroke-width="7" fill="none" stroke-linecap="round"/></g>
{''.join(cloud(110 + i * 350, 80, 0.9, 'blue') for i in range(2))}''')

add('seahorse', '体を立てたタツノオトシゴが、尾で海藻につかまる',
    'タツノオトシゴ＝seahorse。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v400h-600z" fill="#cfe4f0"/></g>
{''.join(f'<path d="M{{}} 400q-20-120 10-200" fill="none" stroke="#3f8f6a" stroke-width="14" stroke-linecap="round"/>'.format(430 + i * 40) for i in range(3))}
<g transform="translate(280 220)">
  <path d="M0-120q40 0 44 40 4 46-24 70-30 26-20 60 8 26 34 18" fill="none" stroke="{GLD}" stroke-width="34" stroke-linecap="round"/>
  <path d="M0-120q-40 0-40 34 0 18 14 26" fill="none" stroke="{GLD}" stroke-width="34" stroke-linecap="round"/>
  <path d="M-34-136l-36 10 34 20z" class="gold o"/>
  <circle cx="-6" cy="-124" r="5" class="ink"/>
  {''.join(f'<path d="M{6+i*6} {-96+i*26}l18-8" stroke="{GLDD}" stroke-width="4" fill="none"/>' for i in range(4))}</g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="none" stroke="#9fc8dd" stroke-width="2.5"/>'.format(90 + (i * 97) % 300, 70 + (i * 53) % 200, 6 + i % 3) for i in range(6))}''')

add('seam', '二枚の布を縫い合わせた線が、縫い目として残る',
    '縫い目、継ぎ目＝seam。', f'''
{table(352)}
<g transform="translate(300 260)">
  <path d="M-200-90h200v180h-200z" class="tealp o"/>
  <path d="M0-90h200v180H0z" class="bluep o"/>
  <path d="M0-90v180" fill="none" stroke="{INK}" stroke-width="3"/>
  {''.join(f'<path d="M-12 {-80+i*22}h24" stroke="{CRL}" stroke-width="5" fill="none" stroke-linecap="round"/>' for i in range(9))}</g>
{ring(300, 260, 0, True)}
{''.join(f'<path d="M{{}} 150h-60" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>'.format(480) for _ in range(1))}''', arrow=True)

add('seatbelt', '座席の帯を斜めに掛け、留め具に差しこむ',
    'シートベルト＝seatbelt。', f'''
<g transform="translate(300 280)">
  <path d="M-120-40h240v100h-240z" class="tealp o"/>
  <path d="M-120-40v-120h240v120" fill="{TEA}" class="o"/>
  <path d="M-120-40h240v20h-240z" class="teald"/></g>
<g transform="translate(300 250)">
  <path d="M-90-110L60 70" stroke="#4e5a66" stroke-width="20" fill="none" stroke-linecap="round"/>
  <path d="M50 58h44v34H50z" fill="#2f3542" class="o"/>
  <path d="M100 66h50v20h-50z" fill="#8a97a3" class="o"/></g>
{ring(370, 320, 60, True)}''')

add('seaweed', '波に揺れる細長い海藻が、岩から伸びている',
    '海藻＝seaweed。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v400h-600z" fill="#cfe4f0"/></g>
<path d="M0 350h600v50H0z" fill="#d8cdb6"/>
{''.join(f'<path d="M{{}} 350q{{}} -80 0-160t{{}} -110" fill="none" stroke="#3f8f6a" stroke-width="{{}}" stroke-linecap="round"/>'.format(80 + i * 70, 30 if i % 2 else -30, -20 if i % 2 else 20, 12 + (i % 3) * 4) for i in range(8))}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="none" stroke="#9fc8dd" stroke-width="2.5"/>'.format(100 + (i * 87) % 420, 80 + (i * 53) % 180, 6 + i % 3) for i in range(7))}''')

add('seesaw', '板の中央が支点になり、両端が上下するシーソー',
    'シーソー＝seesaw。', f'''
<path d="M0 330h600v70H0z" fill="#e8ddc9"/>
<g transform="translate(300 330)">
  <path d="M-34 0l34-70 34 70z" fill="{MUTED}" class="o"/></g>
<g transform="translate(300 260) rotate(-14)">
  <path d="M-200-12h400v24h-400z" fill="#c9a464" class="o"/>
  <path d="M-170-30h30v18h-30zM140-30h30v18h-30z" fill="{BRN}" class="o"/></g>
{head(140, 240, 26, 'coral', 'bob')}
{head(460, 320, 26, 'teal', 'short')}
<g transform="translate(300 130)"><path d="M-60 0q60-24 120 0" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/></g>''', arrow=True)

add('sewer', '道路の下を走る太い下水管に、雨水が流れこむ',
    '下水道、下水管＝sewer。', f'''
<path d="M0 0h600v170H0z" class="ground"/>
<path d="M0 150h600v22H0z" fill="#9aa7b1"/>
<g transform="translate(220 160)">
  <path d="M-40-10h80v20h-80z" fill="#6b7680" class="o"/>
  {''.join(f'<path d="M{-30+i*20} -10v20" stroke="#4e5a66" stroke-width="4" fill="none"/>' for i in range(4))}</g>
<g transform="translate(300 290)">
  <path d="M-300-80h600v160h-600z" fill="#3f3830"/>
  <path d="M-300-50h600v110h-600z" fill="#5b5346"/>
  <path d="M-300-40h600v90h-600z" fill="#2f2a24"/>
  <path d="M-300 10h600v40h-600z" class="bluep" opacity="0.7"/></g>
{''.join(drop(220, 190 + i * 30, 1.0, 'blue') for i in range(2))}
{''.join(f'<path d="M{{}} 300q22-12 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(i * 90) for i in range(6))}''')

add('shack', '板を寄せ集めて建てた粗末な小屋が、川べりに立つ',
    '掘っ立て小屋、粗末な家＝shack。', f'''
<path d="M0 320h600v80H0z" class="greenp"/>
<path d="M0 360h600v40H0z" class="bluep"/>
<g transform="translate(300 320) rotate(-3)">
  <path d="M-100 0v-100h200V0z" fill="#a2825e" class="o"/>
  <path d="M-116-100h232l-10-30h-212z" fill="#8a6a46" class="o"/>
  <path d="M-30 0v-56h54V0z" fill="#6a4a2a" class="o"/>
  {''.join(f'<path d="M{-84+i*36} -100V0" stroke="#8a6a46" stroke-width="3" fill="none"/>' for i in range(5))}
  <path d="M40-76h34v26H40z" fill="#6a4a2a" class="o"/>
  <path d="M-100-60l-30 8v12l30-6" fill="#8a6a46" class="o"/></g>''')

add('shawl', '大判の布を肩から巻き、ふちに房が下がる',
    'ショール、肩掛け＝shawl。', f'''
<g transform="translate(300 250)">
  <circle cy="-130" r="46" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-44-166q4-50 44-50t44 48q-22-20-44-10-24-12-44 12z" fill="{HAIR}"/>
  <circle cx="-16" cy="-130" r="4" class="ink"/><circle cx="16" cy="-130" r="4" class="ink"/>
  <path d="M-12-108q12 10 24 0" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-120-70q120-46 240 0 20 100-120 130-140-30-120-130z" class="violet o"/>
  <path d="M-100-50q100-30 200 0" fill="none" stroke="{VIOD}" stroke-width="4"/>
  {''.join(f'<path d="M{-110+i*26} 58v26" stroke="{VIOD}" stroke-width="5" fill="none" stroke-linecap="round"/>' for i in range(9))}</g>''')

add('shears', '刃の長い大ばさみで、生け垣の枝を刈りそろえる',
    '大ばさみ、植木ばさみ＝shears。', f'''
<path d="M0 330h600v70H0z" class="greenp"/>
<g transform="translate(300 330)">
  <path d="M-220 0v-120h440V0z" class="green o"/>
  <path d="M-220-120q110-30 220 0t220 0" fill="none" stroke="#2a6b4c" stroke-width="5"/></g>
<g transform="translate(300 190) rotate(-10)">
  <path d="M-30-10L-160-40l6 20 124 20z" fill="#c3cbd1" class="o"/>
  <path d="M-30 10L-160 40l6-20 124-20z" fill="#c3cbd1" class="o"/>
  <circle r="9" class="ink"/>
  <path d="M10-10l120-40" stroke="{BRN}" stroke-width="16" fill="none" stroke-linecap="round"/>
  <path d="M10 10l120 40" stroke="{BRN}" stroke-width="16" fill="none" stroke-linecap="round"/></g>
{''.join(f'<ellipse cx="{{}}" cy="{{}}" rx="14" ry="8" class="green o" transform="rotate({{}} {{}} {{}})"/>'.format(150 + i * 70, 240 + (i % 2) * 30, -20 + i * 18, 150 + i * 70, 240 + (i % 2) * 30) for i in range(4))}''')

add('sheepdog', '毛の長い牧羊犬が、羊の群れを一方へ追いこむ',
    '牧羊犬＝sheepdog。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
{''.join(f'<g transform="translate({{}} {{}})"><ellipse rx="44" ry="30" fill="#f4f1ea" class="o"/><circle cx="36" cy="-18" r="18" fill="#4a4238" class="o"/><path d="M-24 26v18M12 28v16" stroke="#4a4238" stroke-width="7" fill="none"/></g>'.format(360 + i * 80, 280 + (i % 2) * 40) for i in range(3))}
<g transform="translate(160 300)">
  <ellipse rx="70" ry="40" fill="#5b4636" class="o"/>
  <circle cx="62" cy="-28" r="30" fill="#5b4636" class="o"/>
  <path d="M34-46q-18-22-6-42 20 12 26 34zM90-48q18-22 6-42-20 12-26 34z" fill="#3f3126" class="o"/>
  <circle cx="52" cy="-32" r="4" fill="#fffefd"/><circle cx="74" cy="-32" r="4" fill="#fffefd"/>
  <ellipse cx="64" cy="-14" rx="9" ry="6" fill="#2f2620"/>
  <path d="M-44 34v28M-6 38v24M32 36v26" stroke="#5b4636" stroke-width="12" fill="none" stroke-linecap="round"/>
  <path d="M-68-6q-40-10-40-40" fill="none" stroke="#5b4636" stroke-width="11" stroke-linecap="round"/></g>
{arc(250, 240, 340, 240, 46, MUTED, True, 4)}''', arrow=True)

add('shipyard', '造船所のドックで、大きな船体が組み立てられている',
    '造船所＝shipyard。', f'''
<path d="M0 300h600v100H0z" fill="#9aa7b1"/>
<path d="M0 340h600v60H0z" class="bluep"/>
<g transform="translate(300 300)">
  <path d="M-200 0h400l-40 40h-320z" fill="#6b7680" class="o"/>
  <path d="M-180-90h360v90h-360z" class="coral o"/>
  <path d="M-120-150h240v60h-240z" fill="#fffefd" class="o"/>
  {''.join(f'<rect x="{-90+i*46}" y="-136" width="30" height="24" class="bluep o"/>' for i in range(4))}</g>
<g transform="translate(120 300)">
  <path d="M-14 0v-240h28V0z" class="gold o"/>
  <path d="M0-240h200v22H0z" class="gold o"/>
  <path d="M160-218v60" stroke="{INK}" stroke-width="5" fill="none"/>
  <path d="M146-158h30v20h-30z" fill="{MUTED}" class="o"/></g>''')

add('shoelace', '靴のひもが穴を通って交差し、ちょう結びになる',
    '靴ひも＝shoelace。', f'''
{table(352)}
<g transform="translate(300 290)">
  <path d="M-120 40q0-70 50-70h50l90 50v20z" fill="#3f6b8a" class="o"/>
  <path d="M-120 40h190v16h-190z" fill="#2a4a64"/>
  <path d="M-60-30h60v50h-60z" fill="#dfeaf2" class="o"/>
  {''.join(f'<circle cx="{-46+i*20}" cy="{-16+(i%2)*20}" r="4" class="ink"/>' for i in range(4))}
  {''.join(f'<path d="M{-46+i*20} {-16+(i%2)*20}l20 20" stroke="#fffefd" stroke-width="5" fill="none"/>' for i in range(3))}
  <path d="M-40-40q-26-30 0-40 18-6 22 16M-10-40q26-30 50-20 18 8 0 26" fill="none" stroke="#fffefd" stroke-width="7"/>
  <path d="M-24-46l-30 18M-4-46l30 20" stroke="#fffefd" stroke-width="6" fill="none" stroke-linecap="round"/></g>''')

add('sideboard', '低い戸棚の上に器が並び、下に引き出しがある',
    '食器棚、サイドボード＝sideboard。', f'''
<g transform="translate(300 200)"><path d="M-280-170h560v340h-560z" fill="#f6efe1" class="o"/></g>
<g transform="translate(300 320)">
  <path d="M-180-90h360v110h-360z" fill="#a2825e" class="o"/>
  <path d="M-180-100h360v14h-360z" fill="#8a6a46" class="o"/>
  <path d="M-160-70h160v34h-160zM20-70h140v34H20z" fill="#8a6a46" class="o"/>
  <path d="M-160-24h160v34h-160zM20-24h140v34H20z" fill="#8a6a46" class="o"/>
  {''.join(f'<circle cx="{-80+i*160}" cy="{-52+(i%2)*0}" r="7" class="goldd"/>' for i in range(2))}
  <path d="M-160 20v26M160 20v26" stroke="#8a6a46" stroke-width="12" fill="none"/></g>
{''.join(f'<g transform="translate({{}} 212)"><ellipse rx="36" ry="10" fill="#fffefd" class="o"/></g>'.format(200 + i * 100) for i in range(3))}''')

add('sieve', '目の細かいふるいで小麦粉をこし、下に細かく落とす',
    'ふるい、こし器＝sieve。', f'''
{table(352)}
<g transform="translate(300 220)">
  <path d="M-90-30q0 50 90 50t90-50z" fill="#c3cbd1" class="o"/>
  <ellipse cy="-30" rx="90" ry="24" fill="#dfe6ea" class="o"/>
  <ellipse cy="-28" rx="74" ry="18" fill="#e8e2d4"/>
  <path d="M-124-30h34v14h-34zM90-30h34v14H90z" fill="#9aa7b1" class="o"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="3" fill="#f0e6d2" stroke="{MUTED}" stroke-width="1"/>'.format(250 + (i * 29) % 100, 260 + (i * 19) % 50) for i in range(18))}
<g transform="translate(300 320)">
  <path d="M-90-20q0 50 90 50t90-50z" fill="#fffefd" class="o"/>
  <ellipse cy="-20" rx="90" ry="22" fill="#fffefd" class="o"/>
  <ellipse cy="-18" rx="72" ry="16" fill="#f0e6d2"/></g>''')

add('sill', '窓の下枠に鉢植えが置かれ、日が差しこむ',
    '窓の下枠、敷居＝sill。', f'''
<g transform="translate(300 200)">
  <path d="M-240-180h480v360h-480z" fill="#e4dccb" class="o"/>
  <path d="M-160-140h320v220h-320z" fill="#dfeaf2" class="o"/>
  <path d="M0-140v220M-160-30h320" fill="none" stroke="{INK}" stroke-width="5"/></g>
<g transform="translate(300 290)">
  <path d="M-190-10h380v26h-380z" fill="#c9a464" class="o"/>
  <path d="M-190 16h380v10h-380z" fill="#a0764a"/></g>
{ring(300, 292, 0, True)}
<g transform="translate(380 260)">
  <path d="M-30-14h60l-8 34h-44z" class="coral o"/>
  <path d="M0-14v-26" stroke="{GRND}" stroke-width="5" fill="none"/>
  <ellipse cx="-14" cy="-44" rx="16" ry="9" class="green o"/>
  <ellipse cx="14" cy="-52" rx="16" ry="9" class="green o"/></g>''')

add('skateboard', '車輪のついた板の上に乗り、坂を滑り下りる',
    'スケートボード＝skateboard。', f'''
<path d="M0 350h600v50H0z" class="ground"/>
<g transform="translate(300 330) rotate(-10)">
  <path d="M-120-14h240q14 14 0 28h-240q-14-14 0-28z" fill="#c9a464" class="o"/>
  <path d="M-120-14q-30 0-30-14M120-14q30 0 30-14" fill="none" stroke="#a0764a" stroke-width="0"/>
  <circle cx="-70" cy="26" r="16" class="ink"/><circle cx="70" cy="26" r="16" class="ink"/>
  <path d="M-70 14h-16v-10h32v10zM70 14H54V4h32v10z" fill="#8a97a3"/></g>
{person(290, 300, 1.1, 1, 'coral', 'blue', 'up', 'cap', 'smile')}
{''.join(f'<path d="M{{}} {{}}h50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"/>'.format(80, 250 + i * 30) for i in range(2))}''')

add('skating', '氷の上を、刃のついた靴で滑る',
    'スケート＝skating。', f'''
<path d="M0 280h600v120H0z" fill="#e8f0f2"/>
{''.join(f'<path d="M{{}} {{}}q60-16 120 0" fill="none" stroke="#c8d8dc" stroke-width="4"/>'.format(60 + (i % 2) * 90, 320 + i * 26) for i in range(3))}
{person(300, 300, 1.35, 1, 'coral', 'blue', 'walk', 'cap', 'smile')}
{''.join(f'<g transform="translate({{}} 302)"><path d="M-24 0h48v8h-48z" fill="#8a97a3" class="o"/><path d="M-24 8h48v6h-48z" fill="#c3cbd1"/></g>'.format(276 + i * 50) for i in range(2))}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="3" fill="#ffffff" stroke="{MUTED}" stroke-width="1.2"/>'.format(60 + (i * 83) % 480, 60 + (i * 41) % 150) for i in range(8))}''')

add('skewer', '細い金串に肉と野菜を交互に刺して焼く',
    '串＝skewer。', f'''
{table(352)}
<g transform="translate(300 260) rotate(-10)">
  <path d="M-220-4h440v8h-440z" fill="#c3cbd1" class="o"/>
  <path d="M220-4l40 4-40 4z" fill="#c3cbd1" class="o"/>
  {''.join(f'<g transform="translate({-150+i*70} 0)"><rect x="-28" y="-28" width="56" height="56" rx="8" fill="{c}" stroke="{INK}" stroke-width="2.5"/></g>' for i, c in enumerate(['#b5744a', '#4e986a', '#b5744a', '#e86452', '#b5744a']))}</g>
{''.join(f'<path d="M{{}} {{}}q16-20 0-36" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(200 + i * 100, 170 - i * 10) for i in range(3))}''')

add('skillet', '厚い鉄のフライパンで、卵とベーコンを焼く',
    '厚手のフライパン＝skillet。', f'''
{table(352)}
<g transform="translate(280 280)">
  <ellipse rx="130" ry="46" fill="#4e5a66" class="o"/>
  <ellipse cy="-10" rx="114" ry="38" fill="#2f3542"/>
  <path d="M126-10h130v26h-130z" fill="#4e5a66" class="o"/>
  <ellipse cx="-30" cy="-14" rx="44" ry="24" fill="#fffefd" class="o"/>
  <circle cx="-30" cy="-14" r="16" class="gold"/>
  <path d="M40-24q40-10 60 6-30 16-60 4z" fill="#c96a5a" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}q16-20 0-36" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(220 + i * 60, 200 - i * 10) for i in range(3))}''')

add('skylight', '屋根に開けた窓から、光が斜めに差しこむ',
    '天窓＝skylight。', f'''
<g transform="translate(300 220)">
  <path d="M-280-140L0-220l280 80v300h-560z" fill="#e4dccb" class="o"/>
  <path d="M-280 180h560" fill="none" stroke="{INK}" stroke-width="0"/></g>
<g transform="translate(220 130) rotate(-16)">
  <path d="M-70-40h140v80h-140z" fill="#cfe4f0" class="o"/>
  <path d="M0-40v80M-70 0h140" fill="none" stroke="{INK}" stroke-width="4"/></g>
<path d="M170 165L60 380h230L300 160z" fill="#fff6d8" opacity="0.55"/>
{sun(470, 80, 32)}''')

add('slate', '灰色の薄い石を重ねてふいた屋根',
    '粘板岩、スレート＝slate。', f'''
<g transform="translate(300 300)">
  <path d="M-260 60L0-140l260 200z" fill="#6b7680" class="o"/>
  {''.join(f'<g>{"".join(f"<rect x={{}} y={{}} width=42 height=26 rx=2 fill={{}} stroke={INK} stroke-width=1.5/>" for _ in [0])}</g>' for i in range(0))}</g>
{''.join(f'<rect x="{int(300 - (row + 1) * 62 + (row % 2) * 22 + col * 44)}" y="{int(160 + row * 26)}" width="40" height="24" rx="2" fill="{"#7a8690" if (row + col) % 2 else "#616d77"}" stroke="{INK}" stroke-width="1.5"/>' for row in range(7) for col in range(row * 2 + 2))}
<path d="M0 360h600v40H0z" class="ground"/>''')

add('sledge', '木のそりに乗って、雪の坂を滑り下りる',
    'そり＝sledge。', f'''
<path d="M0 240q140 40 300 60t300 60v40H0z" fill="#eef4f7" class="o"/>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="3" fill="#ffffff" stroke="{MUTED}" stroke-width="1.2"/>'.format(60 + (i * 79) % 480, 40 + (i * 43) % 180) for i in range(9))}
<g transform="translate(300 300) rotate(10)">
  <path d="M-90-16h180v18h-180z" fill="#c9a464" class="o"/>
  {''.join(f'<path d="M{-70+i*46} 2v22" stroke="#a0764a" stroke-width="7" fill="none"/>' for i in range(4))}
  <path d="M-100 24h200q20 0 20-20" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/></g>
{sit(300, 280, 0.9, 1, 'coral', 'blue', 'cap', 'smile', 'lap')}
{''.join(f'<path d="M{{}} {{}}h50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"/>'.format(90, 230 + i * 30) for i in range(2))}''')

add('sleeping bag', 'ファスナーのついた袋の寝床に、人が入って眠る',
    '寝袋＝sleeping bag。', f'''
<path d="M0 330h600v70H0z" class="ground"/>
<g transform="translate(300 300)">
  <path d="M-200 30q-20-60 30-70 170-24 340 0 24 10 20 70z" class="teal o"/>
  <path d="M-200 30h390" fill="none" stroke="{TEAD}" stroke-width="4"/>
  <path d="M-150-34q160-22 320 0" fill="none" stroke="{TEAD}" stroke-width="5" stroke-dasharray="10 8"/>
  <path d="M-200-20q-40 0-40 24t40 26" fill="{TEA}" stroke="{INK}" stroke-width="2.5"/></g>
{head(180, 262, 26, 'coral', 'short')}
{''.join(f'<path d="M{{}} {{}}q12-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(140 + i * 20, 220 - i * 14) for i in range(2))}''')

add('snowflake', '六本の枝が対称に伸びた雪の結晶',
    '雪の結晶、雪片＝snowflake。', f'''
<g transform="translate(300 190)"><path d="M-300-190h600v400h-600z" fill="#dfeaf2"/></g>
<g transform="translate(300 190)">
  {''.join(f'<g transform="rotate({a})"><path d="M0 0v-130" stroke="#fffefd" stroke-width="12" fill="none" stroke-linecap="round"/><path d="M0-60l-34-30M0-60l34-30M0-100l-24-22M0-100l24-22" stroke="#fffefd" stroke-width="9" fill="none" stroke-linecap="round"/></g>' for a in range(0, 360, 60))}
  <circle r="18" fill="#fffefd"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="#fffefd"/>'.format(60 + (i * 83) % 500, 40 + (i * 47) % 320, 4 + i % 3) for i in range(10))}''')

finish(__file__)
