// 3分間English の会話に登場する文法用語のやさしい辞典。
// 会話の途中で急に用語だけが出てこないよう、各話の最後に「今日の用語メモ」として表示する。
// 定義は1〜2文。例を入れて、その場で意味がつかめることを優先する。

export type GlossaryEntry = {
  term: string
  /** やさしい説明。1〜2文。 */
  plain: string
  /** タイトルや本文で探すときの別表記。 */
  aliases?: string[]
}

export const GRAMMAR_GLOSSARY: GlossaryEntry[] = [
  {
    term: 'be動詞',
    plain: 'am / is / are のこと。「〜です」「〜にいます」のように、主語と後ろの言葉をつなぐ動詞です。',
  },
  {
    term: '一般動詞',
    plain: 'be動詞以外の動詞。eat, play, like など、動作や状態を表します。',
  },
  {
    term: '主語',
    plain: '文の「だれが・何が」にあたる部分。英語では動詞の前に置きます。',
  },
  {
    term: '動詞',
    plain: '動作や状態を表す語。文の中心になります。',
  },
  {
    term: '目的語',
    plain: '動詞の動作の対象。「〜を・〜に」にあたる語で、O と書きます。',
  },
  {
    term: '補語',
    plain: '主語や目的語を説明する語。「S = C」「O = C」の関係になるときの C です。',
  },
  {
    term: '修飾語',
    plain: '文の骨格に情報を足す飾り。場所・時・様子などを表し、M と書きます。外しても文は成り立ちます。',
  },
  {
    term: '文型',
    plain: '文を S・V・O・C の並びで分類した型。第1〜第5文型があります。',
  },
  {
    term: '第1文型',
    plain: '主語 + 動詞だけで成り立つ文。Birds fly. など。SV と書きます。',
  },
  {
    term: '第2文型',
    plain: '主語 + 動詞 + 補語の文。She is a nurse. のように S = C の関係になります。SVC と書きます。',
  },
  {
    term: '第3文型',
    plain: '主語 + 動詞 + 目的語の文。I like music. など。SVO と書きます。',
  },
  {
    term: '第4文型',
    plain: '主語 + 動詞 + 人 + 物の文。I gave him a book. など。SVOO と書きます。',
  },
  {
    term: '第5文型',
    plain: '主語 + 動詞 + 目的語 + 補語の文。They named the baby Emma. のように O = C の関係になります。SVOC と書きます。',
  },
  {
    term: '自動詞',
    plain: '目的語を取らない動詞。sleep, arrive, happen など。',
  },
  {
    term: '他動詞',
    plain: '目的語を取る動詞。make, invite, break など。',
  },
  {
    term: '助動詞',
    plain: '動詞の前に置いて、できる・義務・推量などの気持ちを足す語。can, must, will など。',
  },
  {
    term: '原形',
    plain: '辞書に載っている基本の形。動詞なら eat, go, play など。',
  },
  {
    term: '過去分詞',
    plain: 'have + 過去分詞や be + 過去分詞で使う形。played, gone, written など。',
  },
  {
    term: '現在分詞',
    plain: '動詞の -ing 形。進行形や、名詞を説明する分詞で使います。',
  },
  {
    term: '動名詞',
    plain: '動詞の -ing 形を名詞のように使うもの。Swimming is fun. の swimming です。',
  },
  {
    term: '不定詞',
    plain: 'to + 動詞の原形。「〜すること」「〜するために」などを表します。',
  },
  {
    term: 'to不定詞',
    plain: 'to + 動詞の原形のかたまり。「〜すること」「〜するために」などを表します。',
  },
  {
    term: '冠詞',
    plain: '名詞の前に付く a / an / the のこと。日本語にはないので、初出か既知かを意識して選びます。',
  },
  {
    term: '不定冠詞',
    plain: 'a / an のこと。聞き手がまだ特定できない1つの名詞に付けます。',
    aliases: ['a / an'],
  },
  {
    term: '定冠詞',
    plain: 'the のこと。話し手と聞き手が「どれのことか」分かっている名詞に付けます。',
    aliases: ['the の使い方'],
  },
  {
    term: '数量詞',
    plain: 'some / any / much / many / few / little など、数量を表す語。',
    aliases: ['some / any / much / many'],
  },
  {
    term: '指示詞',
    plain: 'this / that / these / those のように、近く・遠くのものや人を指す語。',
    aliases: ['this / that / these / those'],
  },
  {
    term: '可算名詞',
    plain: '1つ、2つと数えられる名詞。apple, book など。複数形と a / an が使えます。',
  },
  {
    term: '不可算名詞',
    plain: '区切って数えられない名詞。water, advice など。a / an や複数形は使いません。',
  },
  {
    term: '人称代名詞',
    plain: 'I / you / he / she / it / we / they のように、人や物を指す代名詞。',
  },
  {
    term: '所有格',
    plain: 'my / your / his のように「〜の」を表す形。',
  },
  {
    term: '目的格',
    plain: 'me / him / them のように、動詞や前置詞のあとで使う形。',
  },
  {
    term: 'Wh疑問文',
    plain: 'what / where / when / why / who / how で始まる疑問文。',
  },
  {
    term: '疑問詞',
    plain: 'Wh語のこと。what, where, when, why, who, how など。',
  },
  {
    term: '比較級',
    plain: '2つを比べて「〜より…」と言う形。taller, more expensive など。',
    aliases: ['as ... as'],
  },
  {
    term: 'too / enough',
    plain: '「〜すぎる」「十分〜」のように程度を表す表現。too は行きすぎ、enough は足りている状態です。',
  },
  {
    term: '最上級',
    plain: '3つ以上の中で「一番…」と言う形。the tallest, the most expensive など。',
  },
  {
    term: '前置詞',
    plain: '名詞の前に置いて、場所・時・方向などを表す語。at, on, in, to など。',
  },
  {
    term: '接続詞',
    plain: '文と文、語と語をつなぐ語。because, although, and など。',
    aliases: ['because / so / although'],
  },
  {
    term: '逆接',
    plain: '前の内容と反対のことをつなぐこと。however / although / despite などで表します。',
    aliases: ['however / despite / although'],
  },
  {
    term: '現在形',
    plain: '今の習慣・事実を表す形。I work. / He works. など。',
  },
  {
    term: '過去形',
    plain: '終わった過去の出来事を表す形。worked, went など。',
  },
  {
    term: '現在進行形',
    plain: '今している最中を表す形。be動詞 + -ing。I am reading. など。',
  },
  {
    term: '過去進行形',
    plain: '過去のある時点で進行中だった動作。was / were + -ing。',
  },
  {
    term: '現在完了',
    plain: 'have / has + 過去分詞。過去の出来事を「今」とつなげて伝える形です。',
  },
  {
    term: '現在完了進行形',
    plain: 'have been + -ing。過去に始まった動作が今も続いていることを表す形です。',
  },
  {
    term: '過去完了',
    plain: 'had + 過去分詞。過去のある時点よりさらに前に起きたことを表す形です。',
  },
  {
    term: '未来進行形',
    plain: 'will be + -ing。未来のある時点で進行中の動作を表します。',
  },
  {
    term: '未来完了',
    plain: 'will have + 過去分詞。未来のある時点までに完了していることを表します。',
  },
  {
    term: '未来表現',
    plain: 'will / be going to / 現在進行形など、これからのことを表す形の総称。',
    aliases: ['will vs be going to', '過去から見た未来'],
  },
  {
    term: '受動態',
    plain: '「〜される」という文。be動詞 + 過去分詞で作ります。',
  },
  {
    term: '能動態',
    plain: '「〜する」という普通の文。主語が動作をする側に立ちます。',
  },
  {
    term: '名詞',
    plain: '人・物・場所・考えなど、名前を表す語。apple, book, idea など。',
  },
  {
    term: '代名詞',
    plain: '名詞の代わりに使う語。I, you, it, they など。',
  },
  {
    term: '形容詞',
    plain: '人や物の様子・性質を説明する語。big, happy, delicious など。',
  },
  {
    term: '副詞',
    plain: '動詞・形容詞・他の副詞を説明する語。quickly, very, always など。',
  },
  {
    term: '関係詞',
    plain: '名詞のあとで説明を続ける who / which / that / where / when などの総称。',
    aliases: ['whose / where / when', 'what / whatever / whoever'],
  },
  {
    term: '関係代名詞',
    plain: '名詞のあとで説明を続ける who / which / that。the man who lives next door など。',
  },
  {
    term: '関係副詞',
    plain: 'where / when / why で名詞の説明を続ける語。',
  },
  {
    term: '先行詞',
    plain: '関係代名詞の前に置かれ、説明される名詞。the book which I read の the book です。',
  },
  {
    term: '制限用法',
    plain: 'カンマなしの関係詞節。名詞を「〜する人・物」と絞り込みます。',
  },
  {
    term: '非制限用法',
    plain: 'カンマ付きの関係詞節。すでに特定できる名詞に補足情報を足します。',
  },
  {
    term: '条件文',
    plain: 'if などで「もし〜なら」という条件を表す文。',
    aliases: ['unless / in case / as long as', 'provided / suppose / on condition that'],
  },
  {
    term: '願望',
    plain: '「〜ならいいのに」という願い。wish / if only などで表します。',
    aliases: ['wish / if only'],
  },
  {
    term: '後悔',
    plain: '過去の選択を振り返って「〜すべきだった」と残念に思うこと。should have / could have などで表します。',
    aliases: ['should have / could have'],
  },
  {
    term: '仮定法',
    plain: '現実と違うことを想像して言う形。If I had time, I would go. など。',
    aliases: ["would rather / it's time"],
  },
  {
    term: '伝聞',
    plain: '人から聞いたことやうわさを伝えること。「〜と言われている」は It is said that ... で表します。',
    aliases: ['It is said that'],
  },
  {
    term: '分詞',
    plain: '動詞を形容詞のように使う形。現在分詞(-ing)と過去分詞(played / written など)があります。',
  },
  {
    term: '分詞構文',
    plain: '接続詞と主語を省き、-ing で始める文。Walking home, I saw... など。',
  },
  {
    term: '省略',
    plain: '繰り返しになる語を落として短くすること。',
  },
  {
    term: '代用',
    plain: '繰り返しを避けて、so / not / 助動詞などで受けること。',
  },
  {
    term: '倒置',
    plain: '強調のために語順を入れ替えること。Never have I seen... など。',
  },
  {
    term: '強調構文',
    plain: 'It is ... that で伝えたい部分を際立たせる文。',
  },
  {
    term: '句動詞',
    plain: 'turn off のように、動詞 + 副詞 / 前置詞で1つの意味になる表現。',
  },
  {
    term: '間接疑問',
    plain: 'Do you know where he lives? のように、疑問の内容を文の中に入れた形。',
  },
  {
    term: '形式主語',
    plain: 'It is important to study. の It のように、長い主語の代わりに置く仮の主語。',
  },
  {
    term: '仮主語',
    plain: '形式主語と同じ。本当の主語を後ろに回すための It。',
  },
  {
    term: '副詞句',
    plain: '場所・時・様子などを表す句。文の骨格には数えず、M として扱います。',
  },
  {
    term: '前置詞句',
    plain: '前置詞から始まる句。in the box, at seven など。',
  },
  {
    term: '名詞句',
    plain: '名詞と同じ働きをする語のまとまり。',
  },
  {
    term: '関係詞節',
    plain: '関係代名詞・関係副詞が導く節。名詞を説明します。',
  },
  {
    term: 'that節',
    plain: 'that + 主語 + 動詞 のまとまり。「〜ということ」という名詞のように使います。',
  },
  {
    term: 'wh節',
    plain: 'what / where / why などで始まる節。「何を〜したか」という内容を表します。',
  },
  {
    term: 'whether節',
    plain: '「〜かどうか」という内容を表す節。whether + 主語 + 動詞 の形です。',
  },
  {
    term: '同格',
    plain: '名詞のあとに that節などを置いて、その名詞の中身を説明すること。the news that ... など。',
  },
  {
    term: '副詞節',
    plain: 'when / if / because などが導く節。時・条件・理由などを表し、文の骨格には数えません。',
  },
  {
    term: '名詞節',
    plain: '文の中で名詞のように働く節。that節・wh節・whether節などです。',
  },
  {
    term: '相関接続詞',
    plain: 'both ... and、either ... or、neither ... nor のように、2語がペアで働く接続詞。',
  },
  {
    term: '義務',
    plain: '「〜しなければならない」という意味。must / have to などで表します。',
    aliases: ['must / have to'],
  },
  {
    term: '助言',
    plain: '「〜したほうがいい」とアドバイスすること。should / had better などで表します。',
    aliases: ['should / had better'],
  },
  {
    term: '禁止',
    plain: "「〜してはいけない」という意味。mustn't などで表します。",
  },

  {
    term: '話法',
    plain: '人の発言をそのまま伝える直接話法と、自分の言葉に直す間接話法の総称。',
    aliases: ['人が言ったことを伝える', '質問・お願いを人に伝える'],
  },
  {
    term: '伝達動詞',
    plain: 'say / tell / promise / suggest / warn など、人の発言や意図を伝える動詞。',
    aliases: ['「約束した」「提案した」を使い分ける'],
  },
  {
    term: '主節',
    plain: '文の中心になる節。if節や関係詞節に対して、それ以外の主要部分です。',
  },
  {
    term: '従属節',
    plain: '主節を支える節。if節、when節、関係詞節など。',
  },
  {
    term: '等位節',
    plain: 'and / but / or などで対等につながれた節。',
  },
  {
    term: '平叙文',
    plain: '疑問文・命令文ではない、普通の文。',
  },
  {
    term: '否定文',
    plain: 'not / never などで否定を表す文。',
  },
  {
    term: '疑問文',
    plain: '質問する文。Yes / No で答える疑問文と、Wh語で始まる疑問文があります。',
  },
  {
    term: '肯定文',
    plain: '否定していない普通の文。',
  },
  {
    term: '三単現',
    plain: '三人称・単数・現在の略。he / she / it が主語で現在形のとき、動詞に -s を付けるルールです。',
  },
  {
    term: '3人称',
    plain: '話し手(I / we)でも聞き手(you)でもない人・物。he / she / it / they です。',
    aliases: ['三人称'],
  },
  {
    term: '単数',
    plain: '1人・1つのこと。',
  },
  {
    term: '複数',
    plain: '2人・2つ以上のこと。',
  },
  {
    term: '推量',
    plain: '根拠から「〜だろう」と推測すること。',
  },
  {
    term: 'have + 物 + 過去分詞',
    plain: '「(お金を払って)〜してもらう」「〜される」を表す形。have / get + 物 + 過去分詞で作ります。',
    aliases: ['have / get something done'],
  },
  {
    term: '使役動詞',
    plain: 'make / let / have / get のように「人に〜させる」を表す動詞。',
    aliases: ['使役', 'make / let / have / get'],
  },
  {
    term: '知覚動詞',
    plain: 'see / hear / feel など、見る・聞く・感じるを表す動詞。',
    aliases: ['知覚'],
  },
  {
    term: '後置修飾',
    plain: '名詞の後ろから説明を足すこと。the man standing there など。',
  },
  {
    term: '談話標識',
    plain: 'however / therefore など、文と文の関係を示す語。',
    aliases: ['therefore / moreover / such as', '順序・要約・言い換え'],
  },
  {
    term: 'コロケーション',
    plain: '語と語の自然な組み合わせ。listen to music など。',
  },
  {
    term: '頻度の副詞',
    plain: 'always / usually / sometimes / never など、どのくらいよくするかを表す副詞。',
  },
  {
    term: '時制',
    plain: '過去・現在・未来のいつを表すか、という文法の区別。',
  },
]

/** 長い用語から先に照合し、部分一致の重複を避ける。 */
const GLOSSARY_BY_LENGTH = [...GRAMMAR_GLOSSARY].sort((a, b) => b.term.length - a.term.length)

export function findTermsInText(text: string): GlossaryEntry[] {
  let remaining = text
  const found: GlossaryEntry[] = []
  for (const entry of GLOSSARY_BY_LENGTH) {
    const candidates = [entry.term, ...(entry.aliases ?? [])]
    const hit = candidates.find((candidate) => remaining.includes(candidate))
    if (!hit) continue
    found.push(entry)
    for (const candidate of candidates) {
      remaining = remaining.split(candidate).join('　')
    }
  }
  return found
}

/** 複数の文字列から用語を集め、最初に現れた順に返す。 */
export function collectTerms(texts: string[], limit = 8): GlossaryEntry[] {
  const joined = texts.join('\n')
  const candidates = findTermsInText(joined)
  return candidates
    .map((entry) => {
      const candidates = [entry.term, ...(entry.aliases ?? [])]
      const indices = candidates.map((candidate) => joined.indexOf(candidate)).filter((index) => index >= 0)
      return { entry, index: indices.length > 0 ? Math.min(...indices) : -1 }
    })
    .filter(({ index }) => index >= 0)
    .sort((a, b) => a.index - b.index)
    .slice(0, limit)
    .map(({ entry }) => entry)
}
