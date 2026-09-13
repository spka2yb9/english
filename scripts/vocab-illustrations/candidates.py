"""描ける語の候補を並べる。語義・品詞から具体度を推定して並べ替えるだけの補助。"""
import json, re, sys, os
V = json.load(open('/tmp/vocab.json'))
done = set(re.findall(r"^  '?([^':\n]+?)'?: \{", open('src/content/vocabulary/illustrations.ts').read(), re.M))
ABSTRACT = '主義 性 政策 制度 経済 政治 法 権 論 概念 傾向 状況 可能 事実 意味 影響 関係 過程 方針 要素 傾 率 議 策 化 性格 精神 理論 対象 条件 資 益 業 額 費 税 統 織 機関 委員'.split()
CONCRETE = ('動物 鳥 魚 虫 花 木 葉 実 種 川 山 海 空 雲 雨 雪 風 火 水 土 石 道 家 部屋 窓 扉 台 机 椅子 皿 器 服 靴 帽子 袋 箱 車 船 列車 橋 塔 店 畑 庭 手 足 目 口 耳 頭 顔 体 '
            'つかむ 押す 引く 投げる 運ぶ 落ちる 上がる 下がる 開ける 閉める 切る 折る 曲げる 回す 結ぶ 縫う 塗る 洗う 焼く 煮る 注ぐ 積む 並べる 掘る 植える 集める 分ける 混ぜる 包む 縛る 磨く 叩く 蹴る 走る 歩く 跳ぶ 泳ぐ 飛ぶ 座る 立つ 寝る 食べる 飲む 見る 聞く 話す 笑う 泣く 触る 指す 渡す 受け取る '
            '広い 狭い 高い 低い 長い 短い 太い 細い 重い 軽い 丸い 四角 鋭い 硬い 柔らか 明るい 暗い 暖かい 寒い 熱い 冷たい 濡れ 乾い 汚れ きれい 満 空').split()
def score(e):
    txt = ' '.join(e['m'])
    s = 0
    if any(k in txt for k in CONCRETE): s += 3
    if any(k in txt for k in ABSTRACT): s -= 3
    if e['pos'] in ('動詞', '名詞・動詞'): s += 2
    if e['pos'] in ('形容詞', '形容詞・動詞', '形容詞・副詞'): s += 1
    if e['pos'] in ('副詞', '接続詞', '前置詞', '句動詞'): s -= 1
    if e['lv'] == 'A2': s += 2
    elif e['lv'] == 'B1': s += 1
    if len(txt) > 26: s -= 1
    return s
rows = [e for e in V if e['id'] not in done]  # ハイフン・スペースを含む id（句動詞など）も対象
rows.sort(key=lambda e: (-score(e), e['id']))
start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
n = int(sys.argv[2]) if len(sys.argv) > 2 else 60
for e in rows[start:start+n]:
    print(f"{e['id']:16}{e['pos']:10}{e['lv']:4}{' / '.join(e['m'])[:60]}")
print(f"--- {len(rows)} 語が未作成（{len(done)} 語作成済み）", file=sys.stderr)
