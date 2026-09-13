import type { PronunciationEntry, MinimalPair, PronunciationTopic } from '../types'

// General American の発音リファレンス。A2レベルの日本語話者向け。

export const ipaEntries: PronunciationEntry[] = [
  // ─── 母音 ───
  {
    symbol: 'iː',
    type: 'vowel',
    examples: ['see', 'tea', 'green'],
    ja: '「イー」と長く伸ばす音です。日本語の「イー」より口を横に強く引きます。',
    tip: '口の両端を横に引いて笑顔の形を作り、「イー」と長めに言います。',
  },
  {
    symbol: 'ɪ',
    type: 'vowel',
    examples: ['sit', 'big', 'fish'],
    ja: '「イ」と「エ」の間の短い音です。日本語の「イ」より力の抜けた音になります。',
    tip: '口の力を抜き、横に引かずに短く「イ」と言います。「エ」に少し寄せるとそれらしくなります。',
  },
  {
    symbol: 'e',
    type: 'vowel',
    examples: ['bed', 'red', 'pen'],
    ja: '日本語の「エ」に近い短い音です。',
    tip: '日本語の「エ」とほぼ同じでかまいません。口をやや大きめに開いて短く言います。',
  },
  {
    symbol: 'æ',
    type: 'vowel',
    examples: ['cat', 'apple', 'hand'],
    ja: '「ア」と「エ」の中間の音です。日本語の「ア」より口を大きく横に開きます。',
    tip: '「エ」と言うときの口の形のまま、「ア」と声を出します。口を横に大きく開くのがポイントです。',
  },
  {
    symbol: 'ʌ',
    type: 'vowel',
    examples: ['cup', 'sun', 'love'],
    ja: '口をあまり開けずに短く出す「ア」です。日本語の「ア」に一番近い音です。',
    tip: '口を半分だけ開け、のどの奥から短くポンと「ア」と言います。æ のように口を横に開かないのが違いです。',
  },
  {
    symbol: 'ɑː',
    type: 'vowel',
    examples: ['father', 'hot', 'box'],
    ja: '口を縦に大きく開けて出す「アー」です。',
    tip: 'お医者さんにのどを見せるときのように口を縦に大きく開け、「アー」と言います。',
  },
  {
    symbol: 'ɔː',
    type: 'vowel',
    examples: ['talk', 'call', 'saw'],
    ja: '「オ」と「ア」の間の長めの音です。',
    tip: '唇を軽く丸め、口の奥から「オー」と「アー」の中間の音を出します。',
  },
  {
    symbol: 'ʊ',
    type: 'vowel',
    examples: ['book', 'good', 'put'],
    ja: '短くて力の抜けた「ウ」です。',
    tip: '唇をあまり丸めず、口の力を抜いて短く「ウ」と言います。uː のように伸ばしません。',
  },
  {
    symbol: 'uː',
    type: 'vowel',
    examples: ['food', 'blue', 'moon'],
    ja: '唇を丸めて長く伸ばす「ウー」です。',
    tip: '唇をしっかり丸めて前に突き出し、「ウー」と長く言います。',
  },
  {
    symbol: 'ɜːr',
    type: 'vowel',
    examples: ['bird', 'girl', 'work'],
    ja: '「アー」と言いながら舌を軽く反らせる、こもった音です。',
    tip: '舌先をどこにも付けずに軽く後ろへ反らせ、うなるように「アー」と言います。口はあまり開けません。',
  },
  {
    symbol: 'ə',
    type: 'vowel',
    examples: ['about', 'banana', 'lemon'],
    ja: 'あいまい母音です。弱く短い「ア」のような音で、英語で一番よく出てくる母音です。',
    tip: '口も舌も完全に脱力し、ため息をつくように短く「ア」と言います。はっきり発音しないのが正解です。',
  },

  // ─── 二重母音 ───
  {
    symbol: 'eɪ',
    type: 'diphthong',
    examples: ['day', 'rain', 'cake'],
    ja: '「エ」から「イ」へなめらかに移る音です。',
    tip: '「エィ」とひとつづきに言います。日本語式に「エー」と伸ばさないのがポイントです。',
  },
  {
    symbol: 'aɪ',
    type: 'diphthong',
    examples: ['my', 'time', 'five'],
    ja: '「ア」から「イ」へなめらかに移る音です。',
    tip: 'リラックスした状態で「アィ」と言います。最初の「ア」を強く、「ィ」は軽く添えます。',
  },
  {
    symbol: 'ɔɪ',
    type: 'diphthong',
    examples: ['boy', 'coin', 'enjoy'],
    ja: '「オ」から「イ」へなめらかに移る音です。',
    tip: '唇を丸めて「オ」から始め、「オィ」とひとつづきに言います。',
  },
  {
    symbol: 'aʊ',
    type: 'diphthong',
    examples: ['now', 'house', 'down'],
    ja: '「ア」から「ウ」へなめらかに移る音です。',
    tip: '口を大きく開けて「ア」から始め、唇を丸めながら「アゥ」と言います。',
  },
  {
    symbol: 'oʊ',
    type: 'diphthong',
    examples: ['go', 'home', 'boat'],
    ja: '「オ」から「ウ」へなめらかに移る音です。',
    tip: '「オー」と伸ばさず、「オゥ」と最後に軽く「ゥ」を添えます。',
  },

  // ─── 子音 ───
  {
    symbol: 'p',
    type: 'consonant',
    examples: ['pen', 'apple', 'stop'],
    ja: '唇を閉じてから息を破裂させる音です。',
    tip: '両唇をいったん閉じ、強い息とともにパッと開きます。語の最初では特に息を強く出します。',
  },
  {
    symbol: 'b',
    type: 'consonant',
    examples: ['big', 'baby', 'job'],
    ja: 'p と同じ口の形で、声を出す音です。',
    tip: '両唇を閉じ、のどを震わせながらパッと開きます。日本語の「バ行」の最初の音とほぼ同じです。',
  },
  {
    symbol: 't',
    type: 'consonant',
    examples: ['ten', 'time', 'cat'],
    ja: '舌先を上の歯ぐきに付けてから離す音です。',
    tip: '舌先を上の前歯のすぐ後ろの歯ぐきに付け、息とともにパッと離します。',
  },
  {
    symbol: 'd',
    type: 'consonant',
    examples: ['dog', 'ready', 'bed'],
    ja: 't と同じ口の形で、声を出す音です。',
    tip: '舌先を上の歯ぐきに付け、のどを震わせながら離します。日本語の「ダ」の最初の音に近いです。',
  },
  {
    symbol: 'k',
    type: 'consonant',
    examples: ['key', 'school', 'back'],
    ja: '舌の奥を上あごに付けてから離す音です。',
    tip: '舌の奥の部分を上あごに付け、息とともにパッと離します。日本語の「カ行」の最初の音に近いです。',
  },
  {
    symbol: 'g',
    type: 'consonant',
    examples: ['go', 'girl', 'bag'],
    ja: 'k と同じ口の形で、声を出す音です。',
    tip: '舌の奥を上あごに付け、のどを震わせながら離します。日本語の「ガ」の最初の音に近いです。',
  },
  {
    symbol: 'f',
    type: 'consonant',
    examples: ['fish', 'coffee', 'life'],
    ja: '上の前歯を下唇に当てて出す、息だけの音です。日本語の「フ」とは別の音です。',
    tip: '上の前歯を下唇の内側に軽く当て、そのすき間から息を出します。日本語の「フ」のように両唇を近づけて出す音ではありません。',
  },
  {
    symbol: 'v',
    type: 'consonant',
    examples: ['very', 'seven', 'love'],
    ja: 'f と同じ口の形で、声を出す音です。「ブ」とは別の音です。',
    tip: '上の前歯を下唇に軽く当てたまま声を出し、ふるえる感じを作ります。b と違って唇は閉じません。',
  },
  {
    symbol: 'θ',
    type: 'consonant',
    examples: ['think', 'three', 'bath'],
    ja: '舌先を前歯の間に軽くはさんで出す、息だけの音です。「ス」とは別の音です。',
    tip: '舌先を上下の前歯の間に軽くはさみ、そのすき間から息を出します。鏡で舌先が見えていれば正解です。',
  },
  {
    symbol: 'ð',
    type: 'consonant',
    examples: ['this', 'mother', 'they'],
    ja: 'θ と同じ口の形で、声を出す音です。「ズ」「ザ」とは別の音です。',
    tip: '舌先を前歯の間に軽くはさんだまま声を出します。舌先がふるえるくすぐったい感じがあれば正解です。',
  },
  {
    symbol: 's',
    type: 'consonant',
    examples: ['sun', 'city', 'bus'],
    ja: '鋭い「ス」の音です。',
    tip: '舌先を上の歯ぐきに近づけ、細いすき間から鋭く息を出します。唇は丸めず横に引きます。',
  },
  {
    symbol: 'z',
    type: 'consonant',
    examples: ['zoo', 'music', 'size'],
    ja: 's と同じ口の形で、声を出す音です。',
    tip: 's の口の形のまま声を出し、「ズー」とふるえる音にします。',
  },
  {
    symbol: 'ʃ',
    type: 'consonant',
    examples: ['she', 'shop', 'fish'],
    ja: '静かにさせるときの「シー」の音です。',
    tip: '唇を丸めて前に突き出し、「シュー」と息を出します。s より舌を少し奥に引くのがポイントです。',
  },
  {
    symbol: 'ʒ',
    type: 'consonant',
    examples: ['television', 'usual', 'measure'],
    ja: 'ʃ と同じ口の形で、声を出す音です。',
    tip: '唇を丸めて「シュ」の口の形を作り、そのまま声を出して「ジュ」に近い音にします。',
  },
  {
    symbol: 'h',
    type: 'consonant',
    examples: ['hat', 'hello', 'behind'],
    ja: 'のどの奥から出す、息だけの音です。',
    tip: 'ため息をつくように、のどから息だけを出します。唇や歯は使いません。「フ」にならないよう唇を丸めないことが大切です。',
  },
  {
    symbol: 'tʃ',
    type: 'consonant',
    examples: ['chair', 'teacher', 'watch'],
    ja: '「チ」に近い音です。',
    tip: '舌先を上の歯ぐきに付けてから、「チッ」と息を破裂させます。日本語の「チャ・チ・チュ」の最初の音に近いです。',
  },
  {
    symbol: 'dʒ',
    type: 'consonant',
    examples: ['job', 'juice', 'bridge'],
    ja: 'tʃ と同じ口の形で、声を出す音です。「ヂ」に近い音です。',
    tip: '舌先を上の歯ぐきに付け、声を出しながら「ヂッ」と離します。日本語の「ジャ・ジ・ジュ」の最初の音に近いです。',
  },
  {
    symbol: 'm',
    type: 'consonant',
    examples: ['man', 'summer', 'time'],
    ja: '唇を閉じて鼻から出す音です。',
    tip: '両唇をしっかり閉じ、「ンー」と鼻に響かせます。日本語の「マ行」の最初の音と同じです。',
  },
  {
    symbol: 'n',
    type: 'consonant',
    examples: ['no', 'dinner', 'sun'],
    ja: '舌先を歯ぐきに付けて鼻から出す音です。',
    tip: '舌先を上の歯ぐきに付けたまま、「ンー」と鼻に響かせます。語の最後でも舌先を付けたまま終わります。',
  },
  {
    symbol: 'ŋ',
    type: 'consonant',
    examples: ['sing', 'long', 'morning'],
    ja: '舌の奥を上げて鼻から出す「ン」です。ng のつづりでよく出てきます。',
    tip: '日本語で「マンガ」と言うときの「ン」と同じ音です。最後に「グ」をはっきり言わず、鼻に響かせて終わります。',
  },
  {
    symbol: 'l',
    type: 'consonant',
    examples: ['light', 'yellow', 'ball'],
    ja: '舌先を上の歯ぐきにしっかり付けて出す音です。',
    tip: '舌先を上の前歯のすぐ後ろの歯ぐきにしっかり付け、付けたまま声を出します。舌が付いていることが r との一番の違いです。',
  },
  {
    symbol: 'r',
    type: 'consonant',
    examples: ['right', 'sorry', 'car'],
    ja: '舌をどこにも付けずに出す、こもった音です。日本語の「ラ行」とは別の音です。',
    tip: '唇を軽く丸め、舌先を少し後ろに反らせて、口の中のどこにも触れないまま声を出します。舌が上あごに付いたら l になってしまいます。',
  },
  {
    symbol: 'w',
    type: 'consonant',
    examples: ['we', 'water', 'always'],
    ja: '唇を丸めた状態から次の母音へ素早く移る音です。',
    tip: '唇をしっかり丸めて「ウ」の形を作り、そこから素早く次の母音に移ります。',
  },
  {
    symbol: 'j',
    type: 'consonant',
    examples: ['yes', 'year', 'music'],
    ja: '日本語の「ヤ・ユ・ヨ」の最初の部分と同じ音です。',
    tip: '「イ」の口の形から素早く次の母音に移ります。「ヤ」と言うときの出だしの動きと同じです。',
  },
]

export const minimalPairs: MinimalPair[] = [
  {
    focus: 'R と L',
    a: { word: 'right', ipa: '/raɪt/' },
    b: { word: 'light', ipa: '/laɪt/' },
    tip: 'right は舌をどこにも付けず、light は舌先を上の歯ぐきに付けます。舌が付くかどうかだけが違いです。',
  },
  {
    focus: 'R と L',
    a: { word: 'read', ipa: '/riːd/' },
    b: { word: 'lead', ipa: '/liːd/' },
    tip: 'read の r は唇を軽く丸めて始めます。lead の l は舌先を歯ぐきに付けたまま「リー」と言います。',
  },
  {
    focus: 'θ と S',
    a: { word: 'think', ipa: '/θɪŋk/' },
    b: { word: 'sink', ipa: '/sɪŋk/' },
    tip: 'think は舌先を前歯の間にはさみます。sink は舌先を歯の内側に置いて鋭く「ス」と言います。聞くときは、息のこもった柔らかい音なら think です。',
  },
  {
    focus: 'ð と D',
    a: { word: 'they', ipa: '/ðeɪ/' },
    b: { word: 'day', ipa: '/deɪ/' },
    tip: 'they は舌先を前歯の間にはさんだまま声を出します。day は舌先を歯ぐきに付けてパッと離します。they のほうが柔らかくこすれる音になります。',
  },
  {
    focus: 'æ と ʌ',
    a: { word: 'cap', ipa: '/kæp/' },
    b: { word: 'cup', ipa: '/kʌp/' },
    tip: 'cap は口を横に大きく開いて「エ」寄りの「ア」、cup は口をあまり開けず短くポンと「ア」と言います。cap のほうが音が長めに聞こえます。',
  },
  {
    focus: 'V と B',
    a: { word: 'very', ipa: '/ˈveri/' },
    b: { word: 'berry', ipa: '/ˈberi/' },
    tip: 'very は上の前歯を下唇に当てたまま声を出します。berry は両唇をいったん閉じます。唇を閉じるかどうかが違いです。',
  },
  {
    focus: 'V と B',
    a: { word: 'vote', ipa: '/voʊt/' },
    b: { word: 'boat', ipa: '/boʊt/' },
    tip: 'vote はふるえるようなこすれた音で始まり、boat は唇の破裂音で始まります。鏡で唇が閉じていなければ v です。',
  },
  {
    focus: 'F と H',
    a: { word: 'fat', ipa: '/fæt/' },
    b: { word: 'hat', ipa: '/hæt/' },
    tip: 'fat は上の前歯を下唇に当てて息を出します。hat はのどの奥からのため息だけです。日本語の「フ」はどちらでもないので、歯と唇を使うかどうかで区別します。',
  },
  {
    focus: 'S と ʃ',
    a: { word: 'sea', ipa: '/siː/' },
    b: { word: 'she', ipa: '/ʃiː/' },
    tip: 'sea は唇を横に引いて鋭く「スィー」、she は唇を丸めて「シー」と言います。日本語の「シ」は she に近いので、sea のときは意識して「スィ」にします。',
  },
  {
    focus: 'ɪ と iː',
    a: { word: 'sit', ipa: '/sɪt/' },
    b: { word: 'seat', ipa: '/siːt/' },
    tip: '長さだけでなく音の質も違います。sit は口の力を抜いた短い「イ」、seat は口を横に引いてはっきり「イー」と言います。',
  },
  {
    focus: 'ɜːr と ɑːr',
    a: { word: 'hurt', ipa: '/hɜːrt/' },
    b: { word: 'heart', ipa: '/hɑːrt/' },
    tip: 'hurt は口をあまり開けず、こもった「アー」で舌を反らせます。heart は口を縦に大きく開けて「アー」と言ってから舌を反らせます。口の開き方が違いです。',
  },
  {
    focus: 'ɔː と ɜːr',
    a: { word: 'walk', ipa: '/wɔːk/' },
    b: { word: 'work', ipa: '/wɜːrk/' },
    tip: 'walk は唇を丸めて「ウォーク」、r の音はありません。work は口をあまり開けず、舌を反らせてこもった「ワーク」と言います。',
  },
  {
    focus: 'J の有無',
    a: { word: 'year', ipa: '/jɪr/' },
    b: { word: 'ear', ipa: '/ɪr/' },
    tip: 'year は「イ」の口から「ィヤ」と始まる動きがあります。ear は最初からそのまま「イ」で始まります。year のほうが出だしに動きがあると覚えます。',
  },
]

export const pronunciationTopics: PronunciationTopic[] = [
  {
    id: 'schwa',
    title: 'あいまい母音(シュワー)',
    body:
      '英語で一番多く使われる母音は、実は「ア」でも「イ」でもなく、**あいまい母音 /ə/(シュワー)**です。口の力を完全に抜いて、ため息のように短く出す弱い音です。\n\n強く読まれない音節の母音は、つづりが a でも o でも u でも、多くがこのあいまい母音になります。つづりのとおりにはっきり読むと、かえって英語らしくなくなってしまいます。\n\n- about の最初の a は、はっきりした「ア」ではなく弱い /ə/ です\n- banana は真ん中だけ強く、前後の a はどちらも /ə/ です\n- 強い音節をしっかり、弱い音節を /ə/ で軽く言うと、英語のリズムが生まれます\n\nまずは知っている単語の中の「弱い部分」を探して、そこを脱力して言う練習をしてみましょう。',
    examples: [
      {
        en: 'about',
        ja: '〜について',
        highlight: 'a',
        note: '最初の a があいまい母音です。「ア」と弱く短く言います。',
      },
      {
        en: 'banana',
        ja: 'バナナ',
        note: '真ん中の音節だけ強く、前後の a は両方とも弱いあいまい母音です。',
      },
      {
        en: 'support',
        ja: '支える',
        highlight: 'su',
        note: '最初の su は弱く、「サ」ではなくあいまいな /ə/ になります。',
      },
      {
        en: 'camera',
        ja: 'カメラ',
        note: '強いのは最初の音節だけで、あとの母音は全部あいまい母音です。',
      },
      {
        en: 'today',
        ja: '今日',
        highlight: 'to',
        note: 'to の o は「トゥ」ではなく弱い /ə/ になります。',
      },
    ],
  },
  {
    id: 'word-stress',
    title: '単語の強勢(word stress)',
    body:
      '英語の単語には、必ず**強く読む場所(強勢)**があります。強勢の位置を間違えると、正しい音で言っていても通じにくくなります。\n\nさらに、同じつづりでも強勢の位置で意味が変わる単語があります。\n\n- **record**: 前を強く読むと名詞「記録」、後ろを強く読むと動詞「記録する」になります\n- **present**: 前を強く読むと名詞「プレゼント」、後ろを強く読むと動詞「発表する」になります\n\nまた、日本語のカタカナ語と強勢の位置が違う単語にも注意が必要です。hotel は「ホ」ではなく後ろの tel を強く読みます。辞書で単語を調べるときは、意味と一緒に強勢の位置も確認する習慣をつけましょう。',
    examples: [
      {
        en: 'She keeps a record of her spending.',
        ja: '彼女は支出の記録をつけています。',
        highlight: 'record',
        note: '名詞なので前を強く読みます(REcord)。',
      },
      {
        en: 'Please record the meeting.',
        ja: '会議を録音してください。',
        highlight: 'record',
        note: '動詞なので後ろを強く読みます(reCORD)。',
      },
      {
        en: 'I got a present from my friend.',
        ja: '友達からプレゼントをもらいました。',
        highlight: 'present',
        note: '名詞なので前を強く読みます(PREsent)。',
      },
      {
        en: 'They will present their plan tomorrow.',
        ja: '彼らは明日、計画を発表します。',
        highlight: 'present',
        note: '動詞なので後ろを強く読みます(preSENT)。',
      },
      {
        en: 'We stayed at a hotel near the station.',
        ja: '駅の近くのホテルに泊まりました。',
        highlight: 'hotel',
        note: 'カタカナの「ホテル」と違い、後ろを強く読みます(hoTEL)。',
      },
    ],
  },
  {
    id: 'sentence-stress',
    title: '文の強勢とリズム',
    body:
      '英語の文は、すべての単語を同じ強さで読みません。**意味の中心になる単語(内容語)を強く**、それ以外(機能語)を弱く読むことで、英語らしいリズムが生まれます。\n\n- **強く読む内容語**: 名詞・動詞・形容詞・副詞(例: bus, want, late)\n- **弱く読む機能語**: 冠詞・前置詞・代名詞・be動詞など(例: a, to, the, is)\n\n強い単語から次の強い単語までがほぼ同じ長さになるように、間の弱い単語は速く軽く言います。日本語のようにすべての音を同じ長さで読むと、単語は合っていても聞き取ってもらいにくくなります。\n\n文を練習するときは、まず強く読む単語に印をつけて、そこだけ大きくゆっくり言う練習から始めるのがおすすめです。',
    examples: [
      {
        en: 'I want to go to the beach.',
        ja: '海に行きたいです。',
        note: 'want と go と beach を強く、to や the は弱く速く読みます。',
      },
      {
        en: 'She bought some flowers for her mother.',
        ja: '彼女はお母さんに花を買いました。',
        note: 'bought と flowers と mother を強く読みます。',
      },
      {
        en: 'Can you help me with my homework?',
        ja: '宿題を手伝ってくれますか。',
        note: 'help と homework を強く、Can you は弱く短く読みます。',
      },
      {
        en: 'The bus was late this morning.',
        ja: '今朝バスは遅れました。',
        note: 'bus と late と morning を強く読みます。',
      },
    ],
  },
  {
    id: 'weak-forms',
    title: '弱形(weak forms)',
    body:
      'can, to, for, and などのよく使う短い単語には、**強い読み方と弱い読み方の2つ**があります。ふつうの文の中では、ほとんどの場合弱いほうで読まれます。\n\n- **can** は /kən/ となり、「クン」のように聞こえます\n- **to** は /tə/ となり、「タ」に近い音になります\n- **for** は /fər/ となり、「ファ」のように短くなります\n- **and** は /ən/ となり、「ン」だけのように聞こえることもあります\n\nこれを知らないと、リスニングで「can が聞こえなかった」「and がどこにあるかわからない」ということが起こります。弱形は省略ではなく、正しい発音です。\n\n逆に、弱い単語をわざと強く読むと強調の意味になります。I CAN swim. と can を強く言うと、「(できないと思われているけれど)泳げますよ」というニュアンスになります。',
    examples: [
      {
        en: 'I can swim.',
        ja: '私は泳げます。',
        highlight: 'can',
        note: 'can は「クン」のように弱く読みます。強く読むと「できる」を強調する意味になります。',
      },
      {
        en: 'I want to see it.',
        ja: 'それが見たいです。',
        highlight: 'to',
        note: 'to は「タ」に近い弱い音になります。',
      },
      {
        en: 'This present is for you.',
        ja: 'このプレゼントはあなたへのものです。',
        highlight: 'for',
        note: 'for は「ファ」のように弱く短く読みます。',
      },
      {
        en: 'I had bread and butter.',
        ja: 'パンとバターを食べました。',
        highlight: 'and',
        note: 'and は「ン」に近い音になり、全体が「ブレッドンバター」のように聞こえます。',
      },
    ],
  },
  {
    id: 'linking',
    title: '連結(linking)',
    body:
      '英語では、**前の単語の最後の子音と、次の単語の最初の母音がつながって**発音されます。これを連結(リンキング)といいます。\n\n- an apple は「アン・アップル」ではなく「アナポー」のようにつながります\n- turn on は「ターン・オン」ではなく「ターノン」のように聞こえます\n\nネイティブの英語が速く聞こえる大きな理由のひとつがこの連結です。単語を1つずつ覚えていても、つながった形を知らないと聞き取れません。\n\n練習のコツは、2語をひとつの単語のつもりで言ってみることです。turn on なら「turnon」という1語だと思って読むと、自然につながります。聞き取りでも「知っている単語がつながっただけ」と気づけるようになると、一気に楽になります。',
    examples: [
      {
        en: 'an apple',
        ja: 'りんご1個',
        note: 'n と a がつながり、「アナポー」のように聞こえます。',
      },
      {
        en: 'Turn on the light.',
        ja: '電気をつけてください。',
        highlight: 'Turn on',
        note: 'turn の n と on がつながり、「ターノン」のように聞こえます。',
      },
      {
        en: 'Check it out.',
        ja: '見てみてください。',
        note: '3語がつながり、「チェッキラウト」のように聞こえます。',
      },
      {
        en: 'Come in and sit down.',
        ja: '入って座ってください。',
        highlight: 'Come in',
        note: 'come in がつながり、「カミン」のように聞こえます。',
      },
    ],
  },
  {
    id: 'final-consonants',
    title: '語末の子音',
    body:
      '日本語の音は基本的に母音で終わるため、日本語話者は英語の**単語の最後の子音に、つい母音を足してしまい**がちです。cat が「キャット(catto)」、good が「グッド(guddo)」になってしまうパターンです。\n\n余分な母音が付くと、音節の数が増えて単語のリズムが変わるため、意外なほど通じにくくなります。\n\n語末の子音は、次のように「止める」のがコツです。\n\n- **t / d**: 舌先を上の歯ぐきに付けたところで止め、「ト」「ド」と言わない\n- **p / b**: 唇を閉じたところで止め、「プ」「ブ」と言わない\n- **k / g**: 舌の奥を上あごに付けたところで止める\n\n口の形は作るけれど、そのあとの母音を発音しない、というイメージです。単語の最後で一瞬だけ息を止める練習をすると、ぐっと英語らしくなります。',
    examples: [
      {
        en: 'cat',
        ja: '猫',
        note: '「キャット」ではなく、最後は t の口の形で息を止めるだけです。',
      },
      {
        en: 'good',
        ja: '良い',
        note: '最後の d のあとに「オ」を足さず、舌先を歯ぐきに付けたまま終わります。',
      },
      {
        en: 'stop',
        ja: '止まる',
        note: '最後の p は唇を閉じるだけです。「プ」と母音を足しません。',
      },
      {
        en: 'I like this book.',
        ja: '私はこの本が好きです。',
        note: 'like と book の最後に「ウ」や「オ」を足さないように注意します。',
      },
    ],
  },
]
