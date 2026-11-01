// イングバードの着せかえ。見た目だけの設定なので、学習の進み具合には影響しない。
// アイテムは学習日のトータルで解放される。休んでも解放済みのものが消えることはない。

export type OutfitSlot = 'glasses' | 'hat' | 'effect' | 'accessory' | 'shoes'

export type OutfitItem = {
  id: string
  label: string
  description: string
  /** 解放に必要な学習日トータル。0は最初から使える。 */
  unlockDays: number
  /** ダークファンタジー系。300日以降で解放する。 */
  theme?: 'dark'
}

export const GLASSES = [
  { id: 'none', label: 'なし', description: 'メガネをかけない。', unlockDays: 0 },
  { id: 'round', label: '丸メガネ', description: '勉強家の丸メガネ。', unlockDays: 1 },
  { id: 'square', label: '四角メガネ', description: 'きりっとした四角フレーム。', unlockDays: 3 },
  { id: 'sunglasses', label: 'サングラス', description: '決めポーズのサングラス。', unlockDays: 7 },
  { id: 'star', label: 'スターグラス', description: '星がきらめくレンズ。', unlockDays: 12 },
  { id: 'heart', label: 'ハートグラス', description: 'ハート型のレンズ。', unlockDays: 18 },
  { id: 'monocle', label: '片眼鏡', description: '紳士の片眼鏡。', unlockDays: 25 },
  { id: 'oval', label: 'オーバル', description: 'やわらかい楕円フレーム。', unlockDays: 35 },
  { id: 'pixel', label: 'ピクセルグラス', description: 'ゲーム風の角ばったフレーム。', unlockDays: 60 },
  { id: 'sport', label: 'スポーツサングラス', description: '走るときのワイドな一枚レンズ。', unlockDays: 90 },
  { id: 'reading', label: '読書メガネ', description: '手元が見やすいハーフリム。', unlockDays: 120 },
  { id: 'rainbow', label: 'レインボーグラス', description: '虹色にふちどられたレンズ。', unlockDays: 180 },
  { id: 'visor', label: 'バイザー', description: 'ひさしのあるスポーツバイザー。', unlockDays: 240 },
  { id: 'goggles', label: 'ゴーグル', description: '冒険者のゴーグル。', unlockDays: 320 },
  { id: 'cat_eye', label: 'キャットアイ', description: '目尻が上がったキャットアイ。', unlockDays: 9 },
  { id: 'aviator', label: 'アビエイター', description: 'パイロットの定番サングラス。', unlockDays: 17 },
  { id: 'rimless', label: 'リムレス', description: 'ふちの細いリムレスメガネ。', unlockDays: 27 },
  { id: 'diamond', label: 'ダイヤグラス', description: 'ダイヤ型のレンズ。', unlockDays: 42 },
  { id: 'spiral', label: 'ぐるぐる眼鏡', description: '見ているだけで目が回る。', unlockDays: 58 },
  { id: '3d', label: '3Dメガネ', description: '赤と青のレンズ。', unlockDays: 78 },
  { id: 'ski', label: 'スキーゴーグル', description: '雪の日もへっちゃら。', unlockDays: 105 },
  { id: 'flower', label: 'フラワーグラス', description: '花びらがついた丸メガネ。', unlockDays: 165 },
  { id: 'cyber', label: 'サイバーゴーグル', description: 'ネオンが光る未来のゴーグル。', unlockDays: 280 },
  { id: 'star_legend', label: '星のレンズ', description: '星が宿る伝説のレンズ。', unlockDays: 600 },
  { id: 'crimson_gaze', label: '紅い眼光', description: '赤く光る目。', unlockDays: 340, theme: 'dark' },
  { id: 'cursed_lens', label: '呪眼のレンズ', description: '紫の光を宿すレンズ。', unlockDays: 460, theme: 'dark' },
  { id: 'skull_goggles', label: '骸骨ゴーグル', description: '骨の意匠のゴーグル。', unlockDays: 600, theme: 'dark' },
  { id: 'abyss_mask', label: '深淵の面', description: '目元を覆う黒い面。', unlockDays: 750, theme: 'dark' },
  { id: 'demon_eyes', label: '悪魔の瞳', description: '縦長の瞳が光る。', unlockDays: 900, theme: 'dark' },
  { id: 'tinted', label: '色付き丸メガネ', description: 'うすい色の丸メガネ。', unlockDays: 6 },
  { id: 'butterfly', label: 'ちょうちょグラス', description: '羽のようなレンズ。', unlockDays: 15 },
  { id: 'tulip', label: 'チューリップグラス', description: '花びらの形のレンズ。', unlockDays: 30 },
  { id: 'halo', label: 'ハローグラス', description: '光の輪がついたレンズ。', unlockDays: 48 },
  { id: 'swirl', label: '星の渦メガネ', description: '星が渦を巻くレンズ。', unlockDays: 75 },
  { id: 'neon', label: 'ネオングラス', description: 'ネオンが光るフレーム。', unlockDays: 150 },
  { id: 'mirror', label: 'ミラーサングラス', description: '空を映すミラーレンズ。', unlockDays: 210 },
] as const satisfies readonly OutfitItem[]

export const HATS = [
  { id: 'grad', label: '学帽', description: 'おなじみの学帽。', unlockDays: 0 },
  { id: 'none', label: 'なし', description: '帽子をかぶらない。', unlockDays: 0 },
  { id: 'beanie', label: 'ニット帽', description: 'あったかいニット帽。', unlockDays: 2 },
  { id: 'cap', label: 'キャップ', description: 'ひさしのあるキャップ。', unlockDays: 5 },
  { id: 'beret', label: 'ベレー帽', description: 'おしゃれなベレー帽。', unlockDays: 10 },
  { id: 'headband', label: 'ヘッドバンド', description: 'やる気を出すヘッドバンド。', unlockDays: 14 },
  { id: 'flower', label: '花かんむり', description: '春の花かんむり。', unlockDays: 20 },
  { id: 'party', label: 'パーティーハット', description: '今日はお祝いの日。', unlockDays: 30 },
  { id: 'crown', label: '王冠', description: '積み上げた人に似合う王冠。', unlockDays: 50 },
  { id: 'wizard', label: '魔法使い帽', description: '英語の魔法をかける帽子。', unlockDays: 75 },
  { id: 'santa', label: 'サンタ帽', description: '冬の定番。', unlockDays: 100 },
  { id: 'chef', label: 'コック帽', description: '英語を料理するコック帽。', unlockDays: 150 },
  { id: 'pirate', label: '海賊帽', description: '七つの海を渡る海賊帽。', unlockDays: 200 },
  { id: 'cowboy', label: 'カウボーイハット', description: '西部のカウボーイハット。', unlockDays: 250 },
  { id: 'mushroom', label: 'きのこ帽', description: '森のきのこ帽。', unlockDays: 300 },
  { id: 'top', label: 'シルクハット', description: '格式高いシルクハット。', unlockDays: 365 },
  { id: 'crown_gold', label: '黄金の王冠', description: '黄金に輝く王冠。', unlockDays: 500 },
  { id: 'halo', label: '天使の輪', description: '頭の上で光る輪。', unlockDays: 730 },
  { id: 'straw', label: '麦わら帽子', description: '夏の日差しに似合う麦わら帽子。', unlockDays: 6 },
  { id: 'propeller', label: 'プロペラ帽', description: '風を受けて回るプロペラ。', unlockDays: 13 },
  { id: 'cat_ears', label: 'ねこみみ', description: 'かわいい猫の耳。', unlockDays: 21 },
  { id: 'bunny_ears', label: 'うさみみ', description: 'ぴんと立ったうさぎの耳。', unlockDays: 33 },
  { id: 'turban', label: 'ターバン', description: '宝石つきのターバン。', unlockDays: 45 },
  { id: 'sombrero', label: 'ソンブレロ', description: 'つばの広いソンブレロ。', unlockDays: 65 },
  { id: 'viking', label: 'ヴァイキングヘルム', description: 'つのの生えた兜。', unlockDays: 85 },
  { id: 'knight', label: '騎士の兜', description: '騎士のシルバーヘルム。', unlockDays: 115 },
  { id: 'jester', label: '道化師の帽子', description: '三つの先に鈴がついた帽子。', unlockDays: 145 },
  { id: 'helmet', label: 'ヘルメット', description: '安全第一のヘルメット。', unlockDays: 190 },
  { id: 'tiara', label: 'ティアラ', description: '宝石のついた小さな王冠。', unlockDays: 260 },
  { id: 'antenna', label: 'アンテナ', description: 'ぴこぴこ光るアンテナ。', unlockDays: 380 },
  { id: 'demon_horns', label: '悪魔の角', description: '闇から生えた2本の角。', unlockDays: 320, theme: 'dark' },
  { id: 'cursed_crown', label: '呪いの王冠', description: '紫に輝く呪いの王冠。', unlockDays: 400, theme: 'dark' },
  { id: 'skull_helm', label: '骸骨の兜', description: '骨でできた不気味な兜。', unlockDays: 520, theme: 'dark' },
  { id: 'dark_hood', label: '闇のフード', description: '顔に影を落とすフード。', unlockDays: 650, theme: 'dark' },
  { id: 'dragon_horns', label: '竜の角', description: 'ぎざぎざの竜の角。', unlockDays: 800, theme: 'dark' },
  { id: 'abyss_crown', label: '深淵の冠', description: '深淵から生まれた冠。', unlockDays: 950, theme: 'dark' },
  { id: 'sun_hat', label: 'つば広ハット', description: '日差しをよける広いつば。', unlockDays: 7 },
  { id: 'sailor', label: 'セーラー帽', description: '白いセーラー帽。', unlockDays: 18 },
  { id: 'beanie_stripe', label: 'ボーダーニット', description: 'しましまのニット帽。', unlockDays: 26 },
  { id: 'graduation_gold', label: '金の学帽', description: '金色に輝く学帽。', unlockDays: 55 },
  { id: 'witch_black', label: '黒い魔女帽', description: '星を散らした黒い魔女帽。', unlockDays: 95 },
  { id: 'flower_crown', label: '花の王冠', description: '花と宝石の王冠。', unlockDays: 140 },
  { id: 'samurai', label: '侍の兜', description: '前立てが光る侍の兜。', unlockDays: 230 },
  { id: 'phoenix', label: '不死鳥の羽', description: '炎のようにゆれる羽飾り。', unlockDays: 400 },
] as const satisfies readonly OutfitItem[]

export const ACCESSORIES = [
  { id: 'none', label: 'なし', description: '小物なし。', unlockDays: 0 },
  { id: 'scarf', label: 'マフラー', description: '首まわりがあったかい。', unlockDays: 2 },
  { id: 'bowtie', label: '蝶ネクタイ', description: 'きちんと感のある蝶ネクタイ。', unlockDays: 4 },
  { id: 'necktie', label: 'ネクタイ', description: 'びしっと決まるネクタイ。', unlockDays: 8 },
  { id: 'bell', label: '鈴の首輪', description: 'ちりんと鳴る鈴の首輪。', unlockDays: 12 },
  { id: 'medal', label: 'メダル', description: '努力の証のメダル。', unlockDays: 20 },
  { id: 'pendant', label: 'ペンダント', description: '小さな宝石のペンダント。', unlockDays: 30 },
  { id: 'bandana', label: 'バンダナ', description: '元気なバンダナ。', unlockDays: 40 },
  { id: 'headphones', label: 'ヘッドホン', description: '英語を聴くヘッドホン。', unlockDays: 60 },
  { id: 'sash', label: 'たすき', description: 'やる気のたすき。', unlockDays: 90 },
  { id: 'scarf_red', label: 'あかマフラー', description: 'あざやかな赤のマフラー。', unlockDays: 120 },
  { id: 'bell_gold', label: '金の鈴', description: '金色に輝く鈴。', unlockDays: 160 },
  { id: 'cape', label: 'マント', description: '風を切るマント。', unlockDays: 220 },
  { id: 'wings', label: '小さな羽', description: '背中に生えた小さな羽。', unlockDays: 300 },
  { id: 'medal_legend', label: '伝説のメダル', description: '伝説の金色メダル。', unlockDays: 1000 },
  { id: 'mustache', label: 'ちょびひげ', description: 'りりしいちょびひげ。', unlockDays: 11 },
  { id: 'whistle', label: 'ホイッスル', description: 'ピピッと鳴るホイッスル。', unlockDays: 24 },
  { id: 'camera', label: 'カメラ', description: '思い出を残すカメラ。', unlockDays: 38 },
  { id: 'badge', label: 'バッジ', description: '小さな星のバッジ。', unlockDays: 55 },
  { id: 'flower_pin', label: '花のブローチ', description: '春を感じる花のブローチ。', unlockDays: 80 },
  { id: 'bell_blue', label: '青い鈴', description: '澄んだ音の青い鈴。', unlockDays: 100 },
  { id: 'scarf_green', label: '緑のマフラー', description: '森の色のマフラー。', unlockDays: 130 },
  { id: 'backpack', label: 'リュック', description: '冒険のリュック。', unlockDays: 175 },
  { id: 'bowtie_gold', label: '金の蝶ネクタイ', description: 'ぴかぴかの蝶ネクタイ。', unlockDays: 230 },
  { id: 'wings_angel', label: '天使の羽', description: '背中に生えた天使の羽。', unlockDays: 420 },
  { id: 'dark_cape', label: '黒いマント', description: '闇に溶ける黒いマント。', unlockDays: 300, theme: 'dark' },
  { id: 'demon_wings', label: '悪魔の翼', description: 'こうもり型の翼。', unlockDays: 360, theme: 'dark' },
  { id: 'bone_pendant', label: '骨のペンダント', description: '骨のかけらのペンダント。', unlockDays: 420, theme: 'dark' },
  { id: 'cursed_bell', label: '呪いの鈴', description: '紫に光る鈴。', unlockDays: 500, theme: 'dark' },
  { id: 'chain_collar', label: '冥界の鎖', description: '冥界の鎖の首輪。', unlockDays: 700, theme: 'dark' },
  { id: 'dark_orb', label: '闇のオーブ', description: '闇を宿す宝玉。', unlockDays: 850, theme: 'dark' },
  { id: 'spiked_collar', label: '棘の首輪', description: '棘のついた首輪。', unlockDays: 950, theme: 'dark' },
  { id: 'ribbon', label: 'リボン', description: '小さな赤いリボン。', unlockDays: 6 },
  { id: 'cravat', label: 'クラバット', description: 'ひらひらのクラバット。', unlockDays: 16 },
  { id: 'lanyard', label: '名札', description: '首から下げる名札。', unlockDays: 28 },
  { id: 'compass', label: 'コンパス', description: '旅のコンパス。', unlockDays: 46 },
  { id: 'lei', label: 'レイ', description: '花のレイ。', unlockDays: 70 },
  { id: 'scarf_blue', label: '青マフラー', description: '空の色のマフラー。', unlockDays: 110 },
  { id: 'medal_silver', label: '銀メダル', description: '銀色に輝くメダル。', unlockDays: 180 },
  { id: 'backpack_gold', label: '金のリュック', description: '金色のリュック。', unlockDays: 260 },
] as const satisfies readonly OutfitItem[]

export const SHOES = [
  { id: 'none', label: 'なし', description: '靴をはかない。', unlockDays: 0 },
  { id: 'sneakers', label: 'スニーカー', description: '白いスニーカー。', unlockDays: 4 },
  { id: 'boots', label: 'ブーツ', description: 'しっかりした茶色のブーツ。', unlockDays: 9 },
  { id: 'sandals', label: 'サンダル', description: '風通しのいいサンダル。', unlockDays: 14 },
  { id: 'rain_boots', label: '長靴', description: '雨の日も安心の長靴。', unlockDays: 21 },
  { id: 'slippers', label: 'スリッパ', description: 'おうち時間のスリッパ。', unlockDays: 30 },
  { id: 'dress_shoes', label: '革靴', description: 'きちんと感のある革靴。', unlockDays: 42 },
  { id: 'roller_skates', label: 'ローラースケート', description: '車輪のついたスケート。', unlockDays: 60 },
  { id: 'ice_skates', label: 'アイススケート', description: '銀の刃がきらり。', unlockDays: 85 },
  { id: 'sports', label: 'スポーツシューズ', description: '走りやすいスポーツシューズ。', unlockDays: 115 },
  { id: 'geta', label: '下駄', description: 'かっこいい木の下駄。', unlockDays: 150 },
  { id: 'star_boots', label: '星のブーツ', description: '星がかがやくブーツ。', unlockDays: 200 },
  { id: 'rocket_boots', label: 'ロケットブーツ', description: '炎を吹くロケットブーツ。', unlockDays: 300 },
  { id: 'glass_slippers', label: 'ガラスの靴', description: '透きとおったガラスの靴。', unlockDays: 450 },
  { id: 'cloud_shoes', label: '雲の靴', description: '雲みたいにふかふかの靴。', unlockDays: 700 },
  { id: 'cursed_boots', label: '呪いのブーツ', description: '赤く光るブーツ。', unlockDays: 330, theme: 'dark' },
  { id: 'shadow_shoes', label: '影の靴', description: '影がまとわりつく靴。', unlockDays: 480, theme: 'dark' },
  { id: 'dragon_boots', label: '竜鱗のブーツ', description: '竜の鱗のブーツ。', unlockDays: 620, theme: 'dark' },
  { id: 'underworld_boots', label: '冥界の靴', description: '紫の炎をまとう靴。', unlockDays: 880, theme: 'dark' },
  { id: 'loafers', label: 'ローファー', description: '革のローファー。', unlockDays: 7 },
  { id: 'boat_shoes', label: 'ボートシューズ', description: 'デッキシューズ。', unlockDays: 18 },
  { id: 'jelly_shoes', label: 'ジェリーシューズ', description: '透けるジェリー素材。', unlockDays: 35 },
  { id: 'rain_shoes', label: 'レインシューズ', description: '雨の日も弾む靴。', unlockDays: 55 },
  { id: 'moon_boots', label: '月のブーツ', description: '月あかりのブーツ。', unlockDays: 130 },
  { id: 'sun_sneakers', label: '太陽のスニーカー', description: '太陽のように明るい。', unlockDays: 240 },
  { id: 'fire_boots', label: '炎のブーツ', description: '炎をまとうブーツ。', unlockDays: 380 },
] as const satisfies readonly OutfitItem[]

export const EFFECTS = [
  { id: 'none', label: 'なし', description: 'エフェクトなし。', unlockDays: 0 },
  { id: 'sparkle', label: 'きらきら', description: '星がまたたく。', unlockDays: 1 },
  { id: 'bubble', label: 'あわ', description: 'しゃぼん玉が浮かぶ。', unlockDays: 3 },
  { id: 'sakura', label: 'さくら', description: '花びらが舞う。', unlockDays: 5 },
  { id: 'snow', label: 'ゆき', description: '雪がふる。', unlockDays: 8 },
  { id: 'leaves', label: 'はっぱ', description: '木の葉が舞いおちる。', unlockDays: 12 },
  { id: 'notes', label: 'おんぷ', description: '音符が浮かぶ。', unlockDays: 16 },
  { id: 'hearts', label: 'ハート', description: 'ハートが漂う。', unlockDays: 22 },
  { id: 'stars', label: 'ほしぞら', description: '小さな星がまたたく。', unlockDays: 28 },
  { id: 'confetti', label: 'こんぺいとう', description: '紙吹雪が舞う。', unlockDays: 40 },
  { id: 'rain', label: 'あめ', description: '雨がしとしと降る。', unlockDays: 55 },
  { id: 'fireflies', label: 'ほたる', description: 'ほたるが光る。', unlockDays: 70 },
  { id: 'lightning', label: 'いなずま', description: '小さな雷が走る。', unlockDays: 85 },
  { id: 'rainbow', label: 'にじ', description: '虹がかかる。', unlockDays: 110 },
  { id: 'bigbubbles', label: '大きなあわ', description: '大きなしゃぼん玉。', unlockDays: 140 },
  { id: 'goldsparkle', label: '金のきらめき', description: '金色の光がまたたく。', unlockDays: 200 },
  { id: 'meteor', label: '流星', description: '流れ星が走る。', unlockDays: 280 },
  { id: 'aurora', label: 'オーロラ', description: '空にオーロラがゆれる。', unlockDays: 400 },
  { id: 'galaxy', label: '銀河', description: '銀河の星々がひかる。', unlockDays: 1000 },
  { id: 'butterfly', label: 'ちょうちょ', description: 'ひらひら舞うちょうちょ。', unlockDays: 15 },
  { id: 'balloons', label: 'ふうせん', description: 'ふわふわ浮かぶ風船。', unlockDays: 26 },
  { id: 'bubblestars', label: '星あわ', description: '星が入ったしゃぼん玉。', unlockDays: 48 },
  { id: 'fireworks', label: '花火', description: '小さな花火がはじける。', unlockDays: 95 },
  { id: 'heart_rain', label: 'ハートの雨', description: 'ハートが降ってくる。', unlockDays: 135 },
  { id: 'gold_leaves', label: '金のはっぱ', description: '金色に色づいた葉。', unlockDays: 155 },
  { id: 'stardust', label: '星くず', description: 'きらきら舞う星くず。', unlockDays: 210 },
  { id: 'comet', label: 'すい星', description: '尾を引いて走るすい星。', unlockDays: 330 },
  { id: 'sunlight', label: '木もれ日', description: '木のあいだから差す光。', unlockDays: 450 },
  { id: 'thunderstorm', label: '雷雨', description: '雨と雷がいっしょに来る。', unlockDays: 550 },
  { id: 'aurora_borealis', label: '極光', description: '夜空にゆれる極光。', unlockDays: 700 },
  { id: 'stardust_legend', label: '伝説の星くず', description: '伝説の輝きを放つ星くず。', unlockDays: 900 },
  { id: 'dark_mist', label: '黒い霧', description: '足元に漂う黒い霧。', unlockDays: 310, theme: 'dark' },
  { id: 'bats', label: 'コウモリ', description: '羽音を立てて飛ぶ。', unlockDays: 350, theme: 'dark' },
  { id: 'purple_flame', label: '紫の炎', description: 'ゆらめく紫の炎。', unlockDays: 430, theme: 'dark' },
  { id: 'cursed_glow', label: '呪いの光', description: '不気味に光る玉。', unlockDays: 530, theme: 'dark' },
  { id: 'blood_moon', label: '血の月', description: '赤く染まった月。', unlockDays: 640, theme: 'dark' },
  { id: 'ghosts', label: '亡霊', description: 'ふわふわ漂う亡霊。', unlockDays: 760, theme: 'dark' },
  { id: 'abyss', label: '深淵', description: '闇が渦を巻く。', unlockDays: 900, theme: 'dark' },
  { id: 'void_rift', label: '虚空の裂け目', description: '空寂に走る紫の裂け目。', unlockDays: 1000, theme: 'dark' },
  { id: 'drizzle', label: '小雨', description: 'しとしと降る小雨。', unlockDays: 2 },
  { id: 'sunshower', label: '天気雨', description: '太陽ときらめく雨。', unlockDays: 11 },
  { id: 'raindrops', label: '雨だれ', description: 'ぽとぽと落ちるしずく。', unlockDays: 25 },
  { id: 'rainbow_rain', label: '虹雨', description: '色とりどりの雨粒。', unlockDays: 44 },
  { id: 'sleet', label: 'みぞれ', description: '雨と雪がいっしょに。', unlockDays: 90 },
  { id: 'storm', label: '嵐', description: '風と雨と雷。', unlockDays: 170 },
  { id: 'bubble_rain', label: 'あわ雨', description: 'あわが雨のように降る。', unlockDays: 290 },
  { id: 'star_rain', label: '星の雨', description: '星が降ってくる。', unlockDays: 360 },
  { id: 'gold_rain', label: '金の雨', description: '金色の雨。', unlockDays: 520 },
  { id: 'reverse_rain', label: '逆さ雨', description: '空へ登っていく雨。', unlockDays: 780 },
] as const satisfies readonly OutfitItem[]

export type GlassesId = (typeof GLASSES)[number]['id']
export type HatId = (typeof HATS)[number]['id']
export type EffectId = (typeof EFFECTS)[number]['id']
export type AccessoryId = (typeof ACCESSORIES)[number]['id']
export type ShoeId = (typeof SHOES)[number]['id']

export type IngbirdOutfit = {
  glasses: GlassesId
  hat: HatId
  effect: EffectId
  accessory: AccessoryId
  shoes: ShoeId
}

export const DEFAULT_OUTFIT: IngbirdOutfit = {
  glasses: 'none',
  hat: 'grad',
  effect: 'none',
  accessory: 'none',
  shoes: 'none',
}

/** 画面に出す順番。 */
export const OUTFIT_SLOT_ORDER: readonly OutfitSlot[] = ['glasses', 'hat', 'effect', 'accessory', 'shoes']

export const OUTFIT_SLOT_LABELS: Record<OutfitSlot, string> = {
  glasses: 'メガネ',
  hat: '帽子',
  effect: 'エフェクト',
  accessory: '小物',
  shoes: '靴',
}

export const OUTFIT_ITEMS: Record<OutfitSlot, readonly OutfitItem[]> = {
  glasses: GLASSES,
  hat: HATS,
  effect: EFFECTS,
  accessory: ACCESSORIES,
  shoes: SHOES,
}

/** アイテムの総数(「なし」も選択肢として数える)。 */
export const OUTFIT_TOTAL = OUTFIT_SLOT_ORDER.reduce((sum, slot) => sum + OUTFIT_ITEMS[slot].length, 0)

/** その学習日トータルで使えるか。 */
export function isOutfitUnlocked(item: OutfitItem, totalDays: number): boolean {
  return totalDays >= item.unlockDays
}

/** 解放済みのアイテム数。 */
export function unlockedOutfitCount(totalDays: number): number {
  return OUTFIT_SLOT_ORDER.reduce(
    (sum, slot) => sum + OUTFIT_ITEMS[slot].filter((item) => isOutfitUnlocked(item, totalDays)).length,
    0,
  )
}

/** 枠とアイテムの組。プレビューや通知で使う。 */
export type OutfitEntry = { slot: OutfitSlot; item: OutfitItem }

/** すべてのアイテムを、枠の表示順で並べる。 */
export function allOutfitEntries(): OutfitEntry[] {
  return OUTFIT_SLOT_ORDER.flatMap((slot) => OUTFIT_ITEMS[slot].map((item) => ({ slot, item })))
}

/** その学習日トータルで、ちょうど新しく解放されるアイテム。 */
export function itemsUnlockedAt(totalDays: number): OutfitEntry[] {
  return allOutfitEntries().filter(({ item }) => item.unlockDays === totalDays)
}

/** 次に解放されるアイテム。同じ日に複数あるときはまとめて返す。全部解放済みなら空。 */
export function nextOutfitUnlocks(totalDays: number): OutfitEntry[] {
  const locked = allOutfitEntries().filter(({ item }) => item.unlockDays > totalDays)
  if (locked.length === 0) return []
  const nextDays = Math.min(...locked.map(({ item }) => item.unlockDays))
  return locked.filter(({ item }) => item.unlockDays === nextDays)
}

/** 次に解放されるアイテムまでの残り日数。全部解放済みなら null。 */
export function daysToNextOutfitUnlock(totalDays: number): number | null {
  const next = nextOutfitUnlocks(totalDays)
  return next.length === 0 ? null : next[0].item.unlockDays - totalDays
}

/** 指定した枠の選択肢かどうか。保存データの検証にも使う。 */
export function isOutfitId(slot: OutfitSlot, id: string): boolean {
  return OUTFIT_ITEMS[slot].some((item) => item.id === id)
}

/** 1枠だけ着せかえる。知らないIDは無視して、今の姿をそのまま返す。 */
export function changeOutfit(outfit: IngbirdOutfit, slot: OutfitSlot, id: string): IngbirdOutfit {
  if (!isOutfitId(slot, id)) return outfit
  return { ...outfit, [slot]: id } as IngbirdOutfit
}
