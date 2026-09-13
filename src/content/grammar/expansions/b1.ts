import type { LessonExpansionMap } from './types'

export const b1Expansions = {
  'u11-l1': {
    explanationTitle: '過去の事実ではなく、現在への報告',
    explanationBody:
      '現在完了は過去の出来事を述べながら、その経験・継続・結果が **今の状況に関係する** と伝える形です。出来事の時点より、今どうなのかに焦点があります。そのため、終わった時を指定する yesterday や last year とは原則一緒に使いません。\n\n形は have / has + 過去分詞で、主語に合わせて変わるのは have の部分です。疑問文では Have you ...?、否定文では have not ... とします。不規則な過去分詞は過去形と異なることがあるため、go–went–gone のように3つの形で覚えましょう。',
    examples: [
      { en: 'The rain has stopped, so we can go outside now.', ja: '雨がやんだので、今は外へ出られます。', highlight: 'has stopped', note: '過去の変化が今の状況につながっています。' },
      { en: 'Have you seen my glasses anywhere?', ja: '私の眼鏡をどこかで見ませんでしたか。', highlight: 'Have you seen' },
      { en: "I haven't finished this chapter yet.", ja: '私はまだこの章を読み終えていません。', highlight: "haven't finished" },
    ],
  },
  'u11-l2': {
    explanationTitle: '経験の有無を人生の範囲で捉える',
    explanationBody:
      '経験用法は、「これまで」という現在まで続く期間の中で、その出来事が一度でもあったかを伝えます。具体的にいつ起きたかは問題にしないため、ever・never・before・once などと相性がよく、時点を尋ねる When did you ...? には過去形を使います。\n\nhave been to は行って戻った経験、have gone to は行って今ここにいない状態を表します。回数は once / twice / three times のように置けます。経験を話したあと、いつ・どこでという詳細へ進むときは過去形へ切り替えるのが自然な会話の流れです。',
    examples: [
      { en: 'Have you ever ridden a horse?', ja: 'これまでに馬に乗ったことがありますか。', highlight: 'Have you ever ridden' },
      { en: 'I have been to Singapore three times.', ja: '私はシンガポールへ3回行ったことがあります。', highlight: 'have been to' },
      { en: 'My parents have never seen snow.', ja: '私の両親は雪を見たことが一度もありません。', highlight: 'have never seen' },
    ],
  },
  'u11-l3': {
    explanationTitle: '始点と長さを正確に言い分ける',
    explanationBody:
      '継続用法では、過去に始まった状態が今も続いています。since は開始地点を指し、since Monday / since I moved here のように時点や節を置きます。for は期間の長さを示し、for three days / for a long time とします。\n\nknow・live・own・be など状態を表す動詞は現在完了とよく組み合わさります。日本語の「3年前から」に引かれて since three years ago とするより、通常は for three years が簡潔です。How long have you ...? への答えが開始点なら since、長さなら for と整理しましょう。',
    examples: [
      { en: 'We have owned this house for twelve years.', ja: '私たちはこの家を12年間所有しています。', highlight: 'have owned' },
      { en: 'Sara has known him since elementary school.', ja: 'サラは小学校のころから彼を知っています。', highlight: 'since elementary school' },
      { en: 'How long have you been a member of this club?', ja: 'このクラブの会員になってどのくらいですか。', highlight: 'How long have you been' },
    ],
  },
  'u11-l4': {
    explanationTitle: '副詞の位置と話し手の期待を読む',
    explanationBody:
      'just は「たった今」、already は予想より早く「もう」、yet は「今までのところ」を表します。just / already は通常 have と過去分詞の間、yet は疑問文・否定文の文末に置くのが基本です。位置ごとまとまりで覚えましょう。\n\nHave you finished yet? には、そろそろ終わっているかもしれないという期待があります。I have not finished yet. は今後終える可能性を残します。already を疑問文で使う Have you finished already? は「もう終わったのですか」という驚きを表すため、単純な確認とはニュアンスが異なります。',
    examples: [
      { en: 'The guests have just arrived.', ja: 'お客さんたちはちょうど到着したところです。', highlight: 'have just arrived' },
      { en: 'I have already sent the invoice.', ja: '請求書はもう送りました。', highlight: 'have already sent' },
      { en: 'Have the repairs finished yet?', ja: '修理作業はもう終わりましたか。', highlight: 'finished yet' },
    ],
  },
  'u11-l5': {
    explanationTitle: '「いつ」より「今どうか」を先に問う',
    explanationBody:
      '過去形と現在完了の違いは、出来事の古さではありません。昨日起きたことでも今への結果を述べるなら現在完了が使われることがあり、何十年前でも完結した歴史上の事実なら過去形です。判断の中心は、話す時間枠が終わっているか、今を含んでいるかです。\n\nthis morning は午前中なら今を含み得ますが、夜に振り返れば終わった時間です。このように同じ表現でも発話時点で選択が変わります。現在完了でニュースを導入し、その後の詳細を過去形で説明する I have lost my key. I dropped it on the bus. という切り替えも自然です。',
    examples: [
      { en: 'I have lost my key, so I cannot open the door.', ja: '鍵をなくしてしまったので、ドアを開けられません。', highlight: 'have lost' },
      { en: 'I dropped it on the bus this morning.', ja: '今朝バスの中で落としました。', highlight: 'dropped', note: '落とした時点を述べる詳細は過去形です。' },
      { en: 'Did you call Maya yesterday?', ja: '昨日マヤに電話しましたか。', highlight: 'Did you call' },
    ],
  },
  'u11-l6': {
    explanationTitle: '4つの質問で用法を判定する',
    explanationBody:
      '現在完了を選んだら、次に文脈を4方向から確認します。「一度でもあるか」なら経験、「いつから続くか」なら継続、「もう終わったか」なら完了、「過去の出来事で今どうなったか」なら結果です。用法名を暗記する目的は、適切な時間表現を選ぶためです。\n\nただし1つの文が複数の意味を帯びることもあります。I have lived here for ten years. は継続であると同時に、10年の経験を背景として示します。試験では ever / since / yet などを手がかりにしつつ、実際の会話では「今との接点が何か」を説明できるかを最終判断にしましょう。',
    examples: [
      { en: 'Our team has won five games this season.', ja: '私たちのチームは今季5試合に勝っています。', highlight: 'has won', note: 'まだ続いている今季の実績です。' },
      { en: 'She has worked at the clinic since she graduated.', ja: '彼女は卒業して以来、その診療所で働いています。', highlight: 'has worked' },
      { en: "We haven't received a reply yet.", ja: '私たちはまだ返事を受け取っていません。', highlight: "haven't received" },
    ],
  },
  'u12-l1': {
    explanationTitle: '予定を「進行中の手配」として見せる',
    explanationBody:
      '未来を表す現在進行形は、相手との約束、予約、切符など、実現に向けた具体的な手配がある予定に使います。単なる希望ではなく、カレンダーに書けるほど輪郭がはっきりした予定だと考えると分かりやすいです。\n\n未来だと分かるよう tomorrow / this weekend / at six などを伴うことが多く、go・come・meet・leave・fly など移動や約束の動詞とよく使われます。What are you doing tonight? は今この瞬間の動作ではなく今夜の予定を尋ねています。文脈の時間表現を必ず確認しましょう。',
    examples: [
      { en: 'I am meeting the dentist at three tomorrow.', ja: '明日3時に歯医者に会う予定です。', highlight: 'am meeting', note: '予約済みの予定です。' },
      { en: 'We are flying to Fukuoka on Friday morning.', ja: '私たちは金曜の朝に福岡へ飛ぶ予定です。', highlight: 'are flying' },
      { en: 'What are you doing after work?', ja: '仕事のあと、何をする予定ですか。', highlight: 'are you doing' },
    ],
  },
  'u12-l2': {
    explanationTitle: '場面に合う未来表現を選ぶ',
    explanationBody:
      '場面から選ぶ練習をしましょう。電話が鳴って「私が出るよ」と今決めたなら I will answer it.、以前からの意図なら I am going to visit Kyoto.、日時を決めた約束なら I am meeting Aya at six. が自然です。**実現する確率ではなく、伝えたい情報**を見ます。\n\n予測なら、will は話し手の見通し、be going to は現在の状況から読み取る見込みを表します。現在進行形は通常、天気などの単なる予測には使いません。使える表現が重なることもあるので、会話の目的と前後の文脈で選びましょう。',
    examples: [
      { en: 'I forgot to call Leo. I will do it now.', ja: 'レオに電話するのを忘れていました。今します。', highlight: 'will do', note: '発話時に決めた行動です。' },
      { en: 'We are going to replace the old computer.', ja: '私たちは古いコンピューターを買い替えるつもりです。', highlight: 'are going to replace' },
      { en: 'The technician is coming at ten on Tuesday.', ja: '技術者は火曜の10時に来る予定です。', highlight: 'is coming' },
    ],
  },
  'u12-l3': {
    explanationTitle: '未来の意味と未来形を分けて考える',
    explanationBody:
      'when / after / before / until / as soon as で時を示す節、if / unless で条件を示す節では、未来の内容でも現在形を使います。未来であることは主節の will や文脈が示すため、従属節の中に will を重ねる必要がありません。\n\nただし when が「いつ〜するのか」という疑問内容を導く名詞節なら will を使えます。I do not know when he will arrive. では when節が know の目的語で、時を条件として示す節ではありません。節が「いつ起きたら主節が起きる」という関係か、「何を知らないか」という内容かを見分けましょう。',
    examples: [
      { en: 'I will lock the door before I leave.', ja: '出かける前にドアの鍵をかけます。', highlight: 'before I leave' },
      { en: 'If the weather improves, we will eat outside.', ja: '天気がよくなれば、外で食べます。', highlight: 'If the weather improves' },
      { en: 'I do not know when the results will arrive.', ja: '結果がいつ届くのか分かりません。', highlight: 'when the results will arrive', note: '疑問内容を表す名詞節なので will を使えます。' },
    ],
  },
  'u13-l1': {
    explanationTitle: '目的語を主役へ移し、時制は be動詞で示す',
    explanationBody:
      '受動態では、能動態の目的語を主語の位置へ移し、その主語が受けた行為に焦点を当てます。過去分詞は行為の内容を保ち、現在・過去などの時制は be動詞が担当します。is cleaned と was cleaned の違いは be動詞の時制です。\n\n受動態にできるのは基本的に目的語を取る他動詞です。happen や arrive には受け身にする目的語がないため、was happened とはしません。また主語が複数なら are / were と、受動態でも主語とbe動詞を一致させる必要があります。',
    examples: [
      { en: 'These rooms are cleaned every morning.', ja: 'これらの部屋は毎朝清掃されます。', highlight: 'are cleaned' },
      { en: 'The bridge was damaged in the storm.', ja: 'その橋は嵐で損傷しました。', highlight: 'was damaged' },
      { en: 'Was this photograph taken in Hokkaido?', ja: 'この写真は北海道で撮られましたか。', highlight: 'Was this photograph taken' },
    ],
  },
  'u13-l2': {
    explanationTitle: '行為者を言う価値があるか判断する',
    explanationBody:
      '受動態の by + 行為者は必須ではありません。行為者が不明、一般の人々、文脈上明らか、または重要でない場合は省略するのが自然です。My bike was stolen. では盗んだ人が分からないため、by someone を足しても情報が増えません。\n\n一方、作品の作者、発見者、意外な実行者などが新しく重要な情報なら by句を付けます。The song was written by a twelve-year-old student. では誰が書いたかに価値があります。道具・材料は by ではなく with を使うことがある点も区別しましょう。',
    examples: [
      { en: 'The missing child was found early this morning.', ja: '行方不明の子どもは今朝早く発見されました。', highlight: 'was found' },
      { en: 'The mural was painted by local high school students.', ja: 'その壁画は地元の高校生によって描かれました。', highlight: 'by local high school students' },
      { en: 'The package was opened with a small knife.', ja: 'その荷物は小さなナイフで開けられました。', highlight: 'with a small knife', note: '道具は通常 with で示します。' },
    ],
  },
  'u13-l3': {
    explanationTitle: '最初の動詞だけを時制・助動詞に合わせる',
    explanationBody:
      '複雑な受動態でも中心は常に be + 過去分詞です。助動詞の後ろでは be を原形にして must be checked、未来なら will be delivered、現在完了なら have been repaired と組み立てます。後ろから「過去分詞 → be → 時制・助動詞」の順に作ると安定します。\n\n現在完了の受動態では been を落としやすいので注意してください。has repaired は能動、has been repaired が受動です。疑問・否定の操作は最初の助動詞に対して行い、Has it been sent? / It has not been sent. とします。',
    examples: [
      { en: 'The final decision will be announced tomorrow.', ja: '最終決定は明日発表されます。', highlight: 'will be announced' },
      { en: 'All applications must be submitted online.', ja: 'すべての申請書はオンラインで提出しなければなりません。', highlight: 'must be submitted' },
      { en: 'The broken elevator has already been repaired.', ja: '故障したエレベーターはすでに修理されました。', highlight: 'has already been repaired' },
    ],
  },
  'u13-l4': {
    explanationTitle: '文法より先に話題の中心を選ぶ',
    explanationBody:
      '能動態と受動態は同じ出来事を異なる視点で見せます。行為者が話題の中心なら能動態、影響を受けたものや結果を中心に話を続けたいなら受動態が自然です。前の文で登場した名詞を次の文の主語に保つと、文章の流れも滑らかになります。\n\n科学・報道・手順では、個人より事実や工程を前面に出すため受動態がよく使われます。ただし受動態を多用すると、責任主体が曖昧で重い文章になることもあります。行為者が重要なら能動態で明示する、という選択も含めて考えましょう。',
    examples: [
      { en: 'The museum opened a new gallery last month.', ja: 'その美術館は先月、新しい展示室を開設しました。', highlight: 'The museum opened', note: '行為者である美術館を話題の中心にしています。' },
      { en: 'The new gallery was opened last month.', ja: 'その新しい展示室は先月開設されました。', highlight: 'was opened' },
      { en: 'The samples are stored at a constant temperature.', ja: '試料は一定の温度で保管されます。', highlight: 'are stored' },
    ],
  },
  'u14-l1': {
    explanationTitle: '2つの文で重なる名詞を接着点にする',
    explanationBody:
      '主格の関係代名詞は、2つの文に共通する名詞を1回にまとめ、その名詞の直後から説明を続ける仕組みです。I know a woman. She repairs clocks. の she を who に変えれば I know a woman who repairs clocks. になります。\n\nwho は人、which は物、that はどちらにも使えます。関係代名詞が節の主語なので省略できず、直後に別の主語を重ねません。また先行詞が単数なら works、複数なら work のように、関係節の動詞を先行詞の数に一致させます。',
    examples: [
      { en: 'I know a mechanic who repairs electric cars.', ja: '私は電気自動車を修理する整備士を知っています。', highlight: 'who repairs electric cars' },
      { en: 'The app that tracks my expenses is free.', ja: '私の支出を記録するそのアプリは無料です。', highlight: 'that tracks my expenses' },
      { en: 'Students who arrive late must sign in.', ja: '遅刻した生徒は署名して入室しなければなりません。', highlight: 'who arrive late' },
    ],
  },
  'u14-l2': {
    explanationTitle: '関係節の中の空席を探す',
    explanationBody:
      '目的格かどうかは、関係詞の後ろだけを見て「主語と動詞がすでにそろっているか」を確認します。the book that I bought では I bought のあとに目的語の空席があり、that がその役割をしています。主語の空席なら主格なので省略できません。\n\n目的格の who / which / that は、制限用法では省略できます。前置詞が文末に残る the person I spoke to も自然な会話表現です。ただし関係詞の直前に前置詞を移した to whom の形では省略できません。まず節を元の文に戻して、どの席が空いているかを確認しましょう。',
    examples: [
      { en: 'The movie we watched last night was excellent.', ja: '昨夜見た映画は素晴らしかったです。', highlight: 'we watched last night', note: '目的格の関係代名詞が省略されています。' },
      { en: 'Is this the document that you need?', ja: 'これはあなたが必要としている書類ですか。', highlight: 'that you need' },
      { en: 'The colleague I sit next to is from Canada.', ja: '私の隣に座る同僚はカナダ出身です。', highlight: 'I sit next to' },
    ],
  },
  'u14-l3': {
    explanationTitle: '所有・場所・時を元の文へ戻して確認する',
    explanationBody:
      'whose / where / when を選ぶときは、説明部分を元の独立した文に戻します。his roof のような所有格が必要なら whose、in that town のような場所の前置詞句なら where、on that day のような時の表現なら when です。\n\nwhere は in / at which、when は on / in which に近い働きをします。そのため the place where I work は自然ですが、the place where I work there のように場所表現を重ねません。whose は人だけでなく the company whose products ... のように組織や物にも使えます。',
    examples: [
      { en: 'We met a chef whose restaurant has won several awards.', ja: '私たちは、店がいくつもの賞を受賞したシェフに会いました。', highlight: 'whose restaurant' },
      { en: 'This is the park where my parents first met.', ja: 'ここは私の両親が初めて出会った公園です。', highlight: 'where my parents first met' },
      { en: 'I remember the day when our puppy came home.', ja: '子犬が家に来た日のことを覚えています。', highlight: 'when our puppy came home' },
    ],
  },
  'u14-l4': {
    explanationTitle: 'カンマは情報の必要性を示す',
    explanationBody:
      '制限用法の関係節は、どの人・物かを特定するために不可欠です。非制限用法は、すでに特定できる名詞へ補足情報を挿入し、話すときも前後に間を置きます。カンマを外すだけで対象範囲が変わることがあるため、飾りではなく意味の記号です。\n\n非制限用法では that を使わず、人には who、物には which を使います。また目的格でも関係代名詞を省略できません。固有名詞や my father のようにすでに一人に決まる表現には、補足ならカンマを付けるのが自然です。',
    examples: [
      { en: 'Employees who work remotely join the meeting online.', ja: '在宅勤務をする従業員はオンラインで会議に参加します。', highlight: 'who work remotely', note: '該当する従業員だけに絞っています。' },
      { en: 'My brother, who works remotely, lives in Nagano.', ja: '私の兄は在宅勤務をしており、長野に住んでいます。', highlight: 'who works remotely' },
      { en: 'The library, which was renovated last year, is very bright.', ja: 'その図書館は昨年改装され、とても明るいです。', highlight: 'which was renovated last year' },
    ],
  },
  'u14-l5': {
    explanationTitle: '先行詞と空席の2段階で選ぶ',
    explanationBody:
      '関係詞を総合的に選ぶときは、まず先行詞が人・物・場所・時・所有のどれかを見ます。次に、関係節の中で不足している役割が主語・目的語・所有格・副詞句のどれかを確認します。この2段階なら、先行詞が place だから必ず where、という早合点を防げます。\n\nthe place that we visited では visited の目的語が空いているので that、the place where we stayed では stayed in the place という場所句が必要なので where です。最後に、カンマの有無と省略可能性を確認すれば、形だけでなく意味まで正確に選べます。',
    examples: [
      { en: 'The hotel that we booked has a view of the lake.', ja: '私たちが予約したホテルからは湖が見えます。', highlight: 'that we booked' },
      { en: 'The hotel where we stayed had a view of the lake.', ja: '私たちが泊まったホテルからは湖が見えました。', highlight: 'where we stayed' },
      { en: 'Mr. Hall, whose daughter is in my class, teaches science.', ja: '娘さんが私と同じクラスのホール先生は、理科を教えています。', highlight: 'whose daughter is in my class' },
    ],
  },
  'u15-l1': {
    explanationTitle: '一般法則か、1回の未来かを見分ける',
    explanationBody:
      'ゼロ条件文は、条件が起きるたび同じ結果になる習慣・法則を表し、if節も主節も現在形です。第1条件文は、これから実際に起こり得る1回の条件と結果を表し、if節は現在形、主節は will / can / 命令文などになります。\n\nif節の位置は前後どちらでもよく、文頭に置くと通常カンマで区切ります。未来の意味でも if節に will を入れないことが基本です。「いつもそうなる」と言い換えられるか、「今回そうなれば」と言っているかで型を選びましょう。',
    examples: [
      { en: 'If you mix blue and yellow, you get green.', ja: '青と黄色を混ぜると緑になります。', highlight: 'If you mix' },
      { en: 'If the train is delayed, I will send you a message.', ja: '電車が遅れたら、メッセージを送ります。', highlight: 'If the train is delayed' },
      { en: 'Call me if you need any help.', ja: '助けが必要なら電話してください。', highlight: 'if you need', note: '主節は命令文にもできます。' },
    ],
  },
  'u15-l2': {
    explanationTitle: '過去形で現実から距離を取る',
    explanationBody:
      '第2条件文の過去形は過去の時間ではなく、現在・未来の現実から距離があることを示します。実現不可能な想像だけでなく、可能性が低いこと、控えめな提案にも使えます。If I had more time, I would learn Italian. は実際には時間が十分でないという含みです。\n\nbe動詞は、特に丁寧・正式な英語ではすべての主語に were を使い、If I were you は定型表現です。結果節には would のほか could / might も置けます。if節に would を入れず、「仮の条件」と「その結果」の役割を分けましょう。',
    examples: [
      { en: 'If I lived closer, I would visit more often.', ja: 'もっと近くに住んでいたら、もっと頻繁に訪ねるのですが。', highlight: 'If I lived closer' },
      { en: 'What would you do if you found a wallet?', ja: '財布を拾ったらどうしますか。', highlight: 'would you do if you found' },
      { en: 'If I were you, I would keep a copy of the receipt.', ja: '私があなたなら、領収書のコピーを取っておきます。', highlight: 'If I were you' },
    ],
  },
  'u15-l3': {
    explanationTitle: '似た条件表現を目的で区別する',
    explanationBody:
      'unless は「〜でない限り」、as long as は「〜という条件なら」です。You can stay as long as you are quiet. は、静かにすることを条件に滞在を認めています。unless you hurry は「急がない限り」で、ここに not を足すと意図した意味が逆になります。\n\nin case は、ある出来事に**備えて先に行動する理由**を示します。Take an umbrella in case it rains. では、雨に備えて傘を持ちます。if it rains なら「雨が降るなら」という条件です。まず「条件を示しているか、備えの理由か」を見分けましょう。',
    examples: [
      { en: 'We will miss the bus unless we leave now.', ja: '今出発しないと、バスに乗り遅れます。', highlight: 'unless we leave now' },
      { en: 'You can use my desk as long as you keep it tidy.', ja: 'きれいに使うなら、私の机を使っても構いません。', highlight: 'as long as' },
      { en: 'Write down the address in case your phone loses its signal.', ja: '携帯の電波が切れた場合に備えて、住所を書き留めておいてください。', highlight: 'in case', note: '問題が起きる前に備える行動です。' },
    ],
  },
  'u15-l4': {
    explanationTitle: '話し手が可能性をどう見ているかを読む',
    explanationBody:
      '第1条件文と第2条件文は、客観的な確率だけでなく、話し手の見方を示します。If she calls, I will tell her. は連絡があり得ると見ており、If she called, I would tell her. は今のところ可能性が低い、または純粋な仮の話として距離を置いています。\n\n時間表現だけで判断せず、現実的な計画・警告なら第1型、事実に反する想像・控えめな仮定なら第2型を選びます。主節の will / would を先に見つけ、if節の現在形 / 過去形との組み合わせがそろっているか確認すると、混合ミスを防げます。',
    examples: [
      { en: 'If our budget is approved, we will start in April.', ja: '予算が承認されれば、4月に開始します。', highlight: 'If our budget is approved' },
      { en: 'If our office were larger, we would add a meeting room.', ja: 'オフィスがもっと広ければ、会議室を追加するのですが。', highlight: 'If our office were larger' },
      { en: 'I would accept the offer if it included remote work.', ja: '在宅勤務が含まれているなら、その申し出を受けるのですが。', highlight: 'if it included' },
    ],
  },
  'u16-l1': {
    explanationTitle: '節どうしの論理関係を明示する',
    explanationBody:
      'because は原因を導き、so はその原因から生じた結果を導きます。同じ関係を反対方向から述べるため、because ... so ... を1つの文で二重に使う必要はありません。although は予想に反する事実を導き、主節との対比を作ります。\n\nalthough と but も同じ文で重ねないのが標準です。従属節を文頭に置く場合は、Although it was late, we continued. のようにカンマで区切ります。接続詞を選ぶ前に、2つの内容が「理由→結果」なのか「予想と反対」なのかを言葉で説明しましょう。',
    examples: [
      { en: 'We canceled the picnic because the wind was too strong.', ja: '風が強すぎたので、ピクニックを中止しました。', highlight: 'because' },
      { en: 'The road was closed, so we took another route.', ja: '道路が閉鎖されていたので、別の道を通りました。', highlight: 'so' },
      { en: 'Although the task was difficult, everyone stayed calm.', ja: '課題は難しかったものの、全員が落ち着いていました。', highlight: 'Although' },
    ],
  },
  'u16-l2': {
    explanationTitle: '出来事の長さと順序を接続詞で示す',
    explanationBody:
      'when はある時点や出来事、while は同時に続く期間、until はある時点までの継続、as soon as は直後を示します。接続詞の意味と動詞の性質を合わせると、2つの出来事の時間関係を細かく描けます。\n\n未来についても、これらが時を示す副詞節を導くなら現在形を使います。until は「〜までずっと」であり、by の「〜までに」とは異なります。また not ... until は「〜して初めて」という遅い開始を表します。どの動作が続き、どの出来事が境界になるかを時間線で考えましょう。',
    examples: [
      { en: 'Please stay here until the doctor calls your name.', ja: '医師が名前を呼ぶまで、ここにいてください。', highlight: 'until the doctor calls' },
      { en: 'While I was printing the tickets, the computer froze.', ja: 'チケットを印刷している間に、コンピューターが動かなくなりました。', highlight: 'While I was printing' },
      { en: 'I will let you know as soon as I hear anything.', ja: '何か分かり次第、すぐにお知らせします。', highlight: 'as soon as I hear' },
    ],
  },
  'u16-l3': {
    explanationTitle: '左右の形を平行にそろえる',
    explanationBody:
      'both A and B、either A or B、neither A nor B では、AとBに同じ文法形式を置く「平行構造」が大切です。reading and writing のように名詞同士、to call or to email のように不定詞同士をそろえると読みやすくなります。\n\nboth は2つともなので複数扱いです。either / neither で単数名詞を結ぶと、正式な文法では動詞を近いほうの主語に一致させる考え方がありますが、複雑なら文を言い換えると安全です。neither 自体が否定なので、not neither と二重にしないことも確認しましょう。',
    examples: [
      { en: 'Both the manager and the assistant are attending the conference.', ja: 'マネージャーとアシスタントの両方が会議に出席します。', highlight: 'Both the manager and the assistant' },
      { en: 'You can either call me or send me a message.', ja: '私に電話するか、メッセージを送ることができます。', highlight: 'either call me or send me a message' },
      { en: 'Neither the kitchen nor the bathroom has a window.', ja: 'キッチンにも浴室にも窓がありません。', highlight: 'Neither the kitchen nor the bathroom' },
    ],
  },
} satisfies LessonExpansionMap
