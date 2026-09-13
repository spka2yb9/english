import type { LessonExpansionMap } from './types'

export const b2Expansions = {
  'u23-l1': {
    explanationTitle: '条件と結果の時間がずれる理由を読む',
    explanationBody:
      '混合条件文は、条件と結果が同じ時間に属さない因果関係を表します。最も多いのは「過去の選択が違っていれば、現在の状態も違う」という If + had done, would + 原形です。now / today / still などが現在の結果を見分ける手がかりになります。\n\n逆に、現在の性質が過去の結果へ影響したと考える If I were more organized, I would not have missed the deadline. もあります。型を丸暗記せず、条件と結果それぞれに時間線を引き、過去の非現実には過去完了、現在の非現実には過去形相当を割り当てましょう。\n\n**日本語ではこう考える。** 日本語の「あのとき〜していたら、今ごろ…なのに」は、前半と後半で時間がずれていることを「あのとき」「今ごろ」という副詞だけで示し、動詞の形はほとんど変えません。英語は動詞の形そのものにこの時間差を刻むため、前半 had done と後半 would do を別々に決める必要があります。日本語文を読むときに「あのとき」「今ごろ」に相当する語へ印を付け、それぞれに時制を割り当てるという二段構えで訳すと、型を暗記しなくても正しく組み立てられます。',
    examples: [
      { en: 'If I had accepted that job, I would live in Berlin now.', ja: 'あの仕事を引き受けていたら、今ごろベルリンに住んでいるでしょう。', highlight: 'would live in Berlin now' },
      { en: 'If she had charged her phone, we could contact her now.', ja: '彼女が携帯を充電していたら、今連絡できるのですが。', highlight: 'could contact her now' },
      { en: 'If I were more careful, I would not have deleted the file.', ja: '私がもっと注意深ければ、そのファイルを削除しなかったでしょう。', highlight: 'would not have deleted', note: '現在の性質が過去の結果に影響する逆方向の混合です。' },
    ],
  },
  'u23-l2': {
    explanationTitle: '条件の強さと場面の格式を調整する',
    explanationBody:
      'provided / providing that は「この条件を満たす限り」と必要条件を強く示し、許可や合意に向きます。on condition that はさらに契約的・フォーマルです。suppose / supposing は条件を課すのではなく、仮の状況を会話へ持ち込んで相手に考えさせます。\n\nこれらの節も if節と同様、現実的な未来条件には現在形、非現実の想像には過去形を使います。条件節の中へ不用意に will を置きません。what if は心配にも提案にも使えるため、声調と後続文脈から「もし困ったことが起きたら」か「こうしてみたら」を読み分けます。\n\n**日本語ではこう考える。** 日本語の「〜すれば」「〜する限り」「〜としたら」は、ほとんど同じ軽さで使い分けられます。英語では provided that が契約に近い硬さ、suppose が雑談での仮の持ちかけ、in case が備えの理由と、場面の格式と役割がはっきり分かれています。訳語で選ばず、「これは条件を課しているのか、仮の話を持ちかけているのか、備えの理由を述べているのか」と役割を先に決めてから語を選びましょう。',
    examples: [
      { en: 'You may work remotely on Fridays provided that your manager agrees in advance.', ja: '上司が事前に同意するという条件で、金曜日は在宅勤務をしても構いません。', highlight: 'provided that' },
      { en: 'The landlord agreed on condition that we paid a larger deposit.', ja: 'より多くの保証金を払うという条件で、家主は同意しました。', highlight: 'on condition that' },
      { en: 'Suppose the client rejected both designs. What would we do next?', ja: '顧客が両方のデザインを却下したとしましょう。次にどうしますか。', highlight: 'Suppose the client rejected' },
    ],
  },
  'u23-l3': {
    explanationTitle: '過去形が表す対人距離を理解する',
    explanationBody:
      'would rather の主語自身が行動するなら原形ですが、別の人にしてほしいことは would rather + 人 + 過去形で表します。この過去形は時間ではなく、相手の行動を直接命令せず距離を置いて望む仮定法です。否定は人 + did not + 原形になります。\n\nIt is time + 人 + 過去形も、現在すでに実行すべきなのにまだしていないという現実とのずれを示します。It is time to leave は中立的な時刻の案内、It is time we left は軽い催促です。high time は不満が強くなり得るため、相手との関係に配慮して使いましょう。\n\n**日本語ではこう考える。** 日本語は「〜してほしいのですが」と語尾をぼかして距離を作ります。英語の would rather + 人 + 過去形は、この距離を過去形で作っています。過去形なのに現在や未来の話だという点が日本語話者にはつまずきどころですが、「時間の過去ではなく、心理的な遠慮の距離だ」と捉え直すと納得しやすくなります。仮定法の過去形はすべてこの発想でつながっています。',
    examples: [
      { en: 'I would rather take the train than drive in the snow.', ja: '雪の中を運転するより、電車に乗りたいです。', highlight: 'would rather take' },
      { en: 'We would rather you did not mention the delay yet.', ja: '遅延のことはまだ話さないでいただきたいです。', highlight: 'would rather you did not mention' },
      { en: 'It is about time we replaced this old printer with a faster and quieter model.', ja: 'そろそろこの古いプリンターを、もっと速くて静かな機種に買い替える時です。', highlight: 'time we replaced' },
    ],
  },
  'u24-l1': {
    explanationTitle: '手配したサービスか、受けた出来事かを文脈で読む',
    explanationBody:
      'have / get + 物 + 過去分詞は、主語自身が作業したのではなく、誰かに手配して実施してもらったことを表します。get は have より会話的で、手配に少し努力した響きを持つことがあります。作業者を言う必要があれば by + 人を加えられます。\n\n同じ形が、My phone was stolen に近い「望まない出来事を受けた」という経験も表します。She had her bag stolen. は盗ませたのではありません。意図的なサービスか被害かは、動詞と状況から判断します。時制は have / get の部分で示し、過去分詞は変えません。',
    examples: [
      { en: 'We are having the roof inspected next week before the rainy season begins.', ja: '梅雨が始まる前に、来週屋根を点検してもらう予定です。', highlight: 'are having the roof inspected' },
      { en: 'I finally got my laptop repaired after waiting almost three weeks for the parts.', ja: '部品を3週間近く待って、ようやくノートパソコンを修理してもらいました。', highlight: 'got my laptop repaired' },
      { en: 'A tourist had her passport stolen on the train.', ja: '旅行者が電車内でパスポートを盗まれました。', highlight: 'had her passport stolen', note: '意図した手配ではなく被害を表します。' },
    ],
  },
  'u24-l2': {
    explanationTitle: '働きかけの種類と後ろの形をセットにする',
    explanationBody:
      'make は強制・強い原因、let は許可、have は立場を利用した依頼・手配、get は説得や工夫の結果を表します。意味だけでなく、make / let / have + 人 + 原形に対し、get + 人 + to不定詞という形の差を同時に覚えます。\n\n受動態では make の形が be made to do となり、能動態にはなかった to が現れます。let の受動は一般に be allowed to do で言い換えます。help は help someone do / to do の両方が可能です。目的語の人が後ろの動作を行うという共通構造を保ちながら、働きかけのニュアンスを選びましょう。',
    examples: [
      { en: 'The funny video made everyone in the meeting room laugh for a full minute.', ja: 'その面白い動画は、会議室にいた全員をまるまる1分間笑わせました。', highlight: 'made everyone in the meeting room laugh' },
      { en: 'My supervisor had me rewrite the introduction three times before she approved it.', ja: '上司は承認するまでに、私に序文を3回書き直させました。', highlight: 'had me rewrite' },
      { en: 'We finally got the supplier to lower the price.', ja: '私たちはついに仕入れ先を説得して価格を下げてもらいました。', highlight: 'got the supplier to lower' },
    ],
  },
  'u24-l3': {
    explanationTitle: '知覚した範囲を原形と -ing で描き分ける',
    explanationBody:
      'see / hear / watch / feel + 人・物 + 原形は、始まりから終わりまでの出来事を1つのまとまりとして捉えます。-ing は進行中の一場面を捉え、完了したかどうかには焦点を当てません。知覚そのものが過去でも、後ろの原形を過去形にはしません。\n\nI saw him cross the street は渡り切る一連を見た、I saw him crossing the street は渡っているところを見かけた、という視点の差です。受動態では He was seen to cross ... のように原形の前に to が現れます。また smell / find などでも目的語 + -ing により進行中の状況を描けます。\n\n**日本語ではこう考える。** 日本語は「彼が渡るのを見た」と「彼が渡っているのを見た」で、原形と -ing の差にきれいに対応しています。ところが日本語では「〜のを」で受けるため、英語でも to不定詞や that節を使いたくなりがちです。知覚動詞の後ろは to を付けない原形か -ing、というルールだけは日本語の発想から切り離して覚えてください。ただし受動態にすると to が現れる点も併せて押さえておくと混乱しません。',
    examples: [
      { en: 'I heard someone knock three times and then walk quickly down the corridor.', ja: '誰かが3回ノックして、それから廊下を足早に歩いていくのが聞こえました。', highlight: 'heard someone knock' },
      { en: 'We watched the children building a shelter out of branches and old blankets.', ja: '子どもたちが枝と古い毛布で避難所を作っているところを見ていました。', highlight: 'watched the children building' },
      { en: 'The suspect was seen to enter the building at midnight.', ja: '容疑者が真夜中に建物へ入るところを目撃されました。', highlight: 'was seen to enter', note: '受動態では原形の前に to が現れます。' },
    ],
  },
  'u25-l1': {
    explanationTitle: '感情の原因と受け手を矢印で結ぶ',
    explanationBody:
      '-ing 形容詞は感情を引き起こす側の性質、-ed 形容詞はその感情を受けた人・生き物の状態を表します。The lecture was confusing, so the students were confused. のように、原因から受け手へ矢印を描くと選びやすくなります。\n\n人でも a boring speaker のように原因側なら -ing、物でも the damaged machine のような一般の過去分詞形容詞は受け身・完了の状態を表します。感情を表す interested は通常 very interested、原因側の interesting は really interesting などと強めます。主語が人か物かだけで機械的に決めないことが重要です。\n\n**日本語ではこう考える。** 日本語は「退屈な映画」「退屈している私」と、修飾する名詞によって形容詞の形を変えません。どちらも「退屈」で通じてしまいます。英語の -ing と -ed は、この区別を語形そのものに背負わせています。I am boring と言ってしまう誤りが後を絶たないのは、日本語に対応する形がないからです。主語が感情を「起こす側」か「受ける側」かを、和訳ではなく場面の絵で判断する習慣をつけましょう。',
    examples: [
      { en: 'The instructions were misleading, so several users were confused.', ja: '説明が紛らわしかったので、何人かの利用者が混乱しました。', highlight: 'were confused' },
      { en: 'I was amazed by the detail in the painting, especially the reflections on the water.', ja: '私はその絵の細部、とくに水面の反射に驚きました。', highlight: 'was amazed' },
      { en: 'Waiting several weeks for the final decision is exhausting for everyone involved.', ja: '最終決定を何週間も待つのは、関係者全員にとって疲れることです。', highlight: 'exhausting' },
    ],
  },
  'u25-l2': {
    explanationTitle: '名詞と分詞の能動・受動関係を確認する',
    explanationBody:
      '名詞と分詞の関係を先に確認します。the people waiting outside は「人々が待つ」、the documents attached to the email は「書類が添付される」です。過去分詞を見たら、単に「過去」と訳す前に、名詞が行為を受ける側かを考えましょう。\n\n日本語の「外で待っている人々」に対して、英語は the people を先に置き、waiting outside を後ろへ続けます。長い説明をひとかたまりとして読むのがコツです。いつの出来事かを明示したい場合は、関係節を残したほうが分かりやすくなることもあります。',
    examples: [
      { en: 'The woman speaking at the front is our new director.', ja: '前で話している女性が私たちの新しい部長です。', highlight: 'speaking at the front' },
      { en: 'Please review the changes highlighted in yellow before you sign the final version.', ja: '最終版に署名する前に、黄色で強調された変更点を確認してください。', highlight: 'highlighted in yellow' },
      { en: 'Passengers traveling with small children may board first through the priority gate.', ja: '小さなお子様連れの乗客は、優先ゲートから先に搭乗できます。', highlight: 'traveling with small children' },
    ],
  },
  'u25-l3': {
    explanationTitle: '省略された主語が主節と一致するか点検する',
    explanationBody:
      '分詞構文では、通常、分詞の意味上の主語と主節の主語が同じです。Walking into the room, I noticed ... なら歩いて入ったのは I です。この一致が崩れると、意図しない主語が動作したように読める dangling participle になります。\n\n-ing は同時・理由・連続動作、過去分詞は受動・状態を表しやすいですが、正確な論理関係は文脈に依存します。曖昧なら when / because / although を残すほうが安全です。主節より前に完了したことを明示するには Having finished ...、否定は Not knowing ... の形が使えます。\n\n**日本語ではこう考える。** 分詞構文は、日本語の連用中止「〜て、」「〜ので、」にかなり近い働きをします。「家に歩いて帰る途中、旧友に会った」は Walking home, I saw an old friend. とほぼ一対一で対応します。ただし決定的な違いが一つあり、英語では分詞の主語が主節の主語と必ず一致しなければなりません。日本語は主語が違っても「〜て、」でつなげてしまうため、Walking along the river, the old bridge came into view. のような誤りが起きます。書いたあとに主語をそろえて読み返す癖をつけてください。',
    examples: [
      { en: 'Not knowing the answer to the final question, I politely asked for more time.', ja: '最後の質問の答えが分からなかったので、私は丁寧にもう少し時間を求めました。', highlight: 'Not knowing the answer' },
      { en: 'Surrounded by mountains on all four sides, the village is difficult to reach in winter.', ja: '四方を山に囲まれているため、その村へは冬に行くのが困難です。', highlight: 'Surrounded by mountains' },
      { en: 'Having completed the survey in three cities, we analyzed the results over two weeks.', ja: '3つの都市で調査を終えたあと、私たちは2週間かけて結果を分析しました。', highlight: 'Having completed the survey' },
    ],
  },
  'u26-l1': {
    explanationTitle: '伝聞内容の時制を不定詞の形で示す',
    explanationBody:
      'It is said that S + V は内容全体を提示し、S is said to do は内容の主語を文頭に出す簡潔な報道表現です。現在・同時の内容なら to do、伝聞より前の内容なら to have done を使います。He is believed to have left は、去ったことが信じられているという時間差を示します。\n\nsay 以外にも believe・think・report・expect・know などが使え、情報源を断定せず客観的な調子を作ります。ただし責任主体を不必要に隠す効果もあるため、情報源が重要なら According to ... や能動態で明示する選択も考えましょう。',
    examples: [
      { en: 'It is believed that the painting is authentic, although no documents have survived.', ja: '書類は一切残っていませんが、その絵は本物だと考えられています。', highlight: 'It is believed that' },
      { en: 'The company is expected to announce the quarterly results tomorrow morning in Tokyo.', ja: 'その会社は明日の朝、東京で四半期の結果を発表すると予想されています。', highlight: 'is expected to announce' },
      { en: 'The hikers are reported to have reached the village safely.', ja: 'ハイカーたちは無事に村へ到着したと報じられています。', highlight: 'are reported to have reached', note: '到着が報道より前なので完了不定詞です。' },
    ],
  },
  'u26-l2': {
    explanationTitle: '名詞的な位置でも受動の向きを保つ',
    explanationBody:
      '不定詞・動名詞が表す行為でも、主語や対象が行為を受ける側なら受動形が必要です。want to be invited は招待されたい、avoid being seen は見られるのを避ける、というように to be + 過去分詞 / being + 過去分詞を使います。\n\n完了した受動を表す to have been done / having been done もあります。能動か受動かを決めたあと、時制関係を決めるという順序が有効です。need doing が「〜される必要がある」を表す用法もありますが、need to be done のほうが形が明示的で広く使えます。',
    examples: [
      { en: 'Every applicant wants to be treated fairly, whatever the outcome of the interview is.', ja: '面接の結果がどうであれ、応募者は誰もが公平に扱われることを望んでいます。', highlight: 'to be treated' },
      { en: 'The actor left through a side door to avoid being recognized.', ja: 'その俳優は気づかれるのを避けるため、脇の扉から出ました。', highlight: 'being recognized' },
      { en: 'She was proud to have been selected for the national team at the age of seventeen.', ja: '彼女は17歳で代表チームに選ばれたことを誇りに思いました。', highlight: 'to have been selected' },
    ],
  },
  'u26-l3': {
    explanationTitle: 'get受動が示す変化と当事者性',
    explanationBody:
      'get + 過去分詞は、安定した状態より、予期せぬ出来事や状態の変化を生き生きと伝えます。get hurt・get lost・get promoted など会話でよく使われ、主語がその出来事に関わった印象を伴うこともあります。正式な報告では be受動のほうが中立的です。\n\nbe supposed to は形は受動でも、「〜することになっている」「〜のはずだ」という決まり・期待を表す1つのまとまりです。was supposed to do は、しばしば予定が実現しなかった含みを持ちます。get married / be married のように、変化と状態の対比にも注目しましょう。\n\n**日本語ではこう考える。** 日本語の「〜された」は状態にも出来事にも使え、「窓が割れている」と「窓が割れた」を助詞や文脈で区別します。英語では be受動態が状態にも出来事にも読めるのに対し、get受動態は出来事に限られます。予期しない被害や急な変化を語るときは get を選ぶ、と覚えておくと自然さが一段上がります。ただし be located や be born のように get と組めない決まり文句もあるので、そこは形ごと覚えます。',
    examples: [
      { en: 'Two windows on the north side got broken during the storm last Tuesday night.', ja: '先週火曜日の夜の嵐で、北側の窓が2枚割れました。', highlight: 'got broken' },
      { en: 'Maya got promoted to team leader after only six months with the company.', ja: 'マヤは入社わずか6か月でチームリーダーに昇進しました。', highlight: 'got promoted' },
      { en: 'The delivery was supposed to arrive before noon.', ja: '配達は正午前に届くことになっていました。', highlight: 'was supposed to arrive' },
    ],
  },
  'u27-l1': {
    explanationTitle: 'フォーマルさと前置詞の位置を選ぶ',
    explanationBody:
      '前置詞 + whom / which は、前置詞を関係詞の前へ移したフォーマルな形です。the colleague to whom I wrote に対し、会話では the colleague who I wrote to や the colleague I wrote to が自然です。前置詞を前へ出した場合、that や関係詞の省略は使えません。\n\nどの前置詞かは元の動詞・名詞との結びつきから決まります。the reason for which、the method by which のように、元の文へ戻して確認します。場所の in which は where に言い換えられることがありますが、すべての前置詞関係を where だけで表せるわけではありません。\n\n**日本語ではこう考える。** 日本語は「私が育った家」のように、助詞「で」「に」を関係節の中に残したまま名詞の前へ置きます。英語では前置詞を後ろに残す the house I grew up in と、前へ出す the house in which I grew up の二通りがあり、後者だけが硬い書き言葉になります。日本語には語順で格式を変える仕組みがないため、この差は意識的に覚える必要があります。読むときは前置詞 + which を見たら、その前置詞を節の中の元の位置へ戻して意味を取ると分かりやすくなります。',
    examples: [
      { en: 'The person to whom you should speak is Ms. Evans.', ja: 'あなたが話すべき相手はエバンズさんです。', highlight: 'to whom you should speak' },
      { en: 'This is the process by which the data is encrypted before it leaves the server.', ja: 'これが、データがサーバーを出る前に暗号化される工程です。', highlight: 'by which' },
      { en: 'The apartment we moved into last month needs quite a few repairs before winter.', ja: '先月入居したアパートは、冬までにかなりの数の修理が必要です。', highlight: 'we moved into', note: '会話的な前置詞残置で、目的格は省略されています。' },
    ],
  },
  'u27-l2': {
    explanationTitle: '先行詞を含む関係詞を名詞のかたまりとして扱う',
    explanationBody:
      'what は the thing that に近く、それ自体に先行詞を含みます。そのため the thing what や everything what のように別の先行詞を重ねません。what節全体は主語・目的語・補語など、名詞が入る位置に置けます。\n\nwhatever / whoever / whichever は「何であっても・誰であっても・どれであっても」と選択を限定しない意味、または文脈によって「〜するものは何でも」を表します。whatever と no matter what は副詞節では近い意味ですが、名詞節の目的語には whatever が必要です。節内で関係詞が果たす役割も確認しましょう。',
    examples: [
      { en: 'What the witness described in her statement matched the photograph almost exactly.', ja: '目撃者が供述で説明したことは、写真とほぼ完全に一致しました。', highlight: 'What the witness described' },
      { en: 'You may choose whichever option suits your schedule.', ja: '予定に合う選択肢をどれでも選べます。', highlight: 'whichever option suits your schedule' },
      { en: 'Whoever left this package at reception forgot to write a name or a phone number.', ja: '受付にこの荷物を置いた人は誰であれ、名前も電話番号も書き忘れました。', highlight: 'Whoever left this package' },
    ],
  },
  'u27-l3': {
    explanationTitle: 'which の先行詞が名詞か出来事全体かを判定する',
    explanationBody:
      '非制限用法の which は、直前の名詞だけでなく、前の節が表す出来事・事実全体を受けて話し手のコメントを加えられます。The flight was canceled, which caused a long delay. では caused の主語は「欠航したという事実」です。\n\n文全体を受ける which の前にはカンマが必要で、that には置き換えられません。どこまでを受けるか曖昧な場合は This fact ... や This decision ... と新しい文に分けるほうが明確です。which節の動詞は、受けた内容全体を単数の事実として扱うため通常単数形になります。\n\n**日本語ではこう考える。** 日本語は「電車が遅れて、そのせいで式に間に合わなかった」のように、前の文全体を「そのせい」「それ」で受け直します。英語の非制限用法の which はこの「そのこと」に対応します。日本語話者が誤りやすいのは、ここで that を使ってしまう点です。カンマのあとで前の文全体を受けられるのは which だけで、that は使えません。また it を置いてカンマでつなぐと二文が接続詞なしで並ぶことになり、これも誤りになります。',
    examples: [
      { en: 'The server went offline, which prevented us from saving our work.', ja: 'サーバーが停止し、そのため作業を保存できませんでした。', highlight: 'which prevented us' },
      { en: "Riku remembered every single guest's name that evening, which greatly impressed the host.", ja: 'リクはその晩、客一人ひとりの名前を覚えており、そのことが主催者をたいそう感心させました。', highlight: 'which greatly impressed the host' },
      { en: 'The committee changed the deadline again, which nobody had expected.', ja: '委員会は締め切りをまた変更しましたが、それは誰も予想していませんでした。', highlight: 'which nobody had expected' },
    ],
  },
  'u28-l1': {
    explanationTitle: '意味だけでなく文法上の接続方法を選ぶ',
    explanationBody:
      'although は接続詞なので主語 + 動詞の節を導き、despite / in spite of は前置詞表現なので名詞・代名詞・動名詞を取ります。however は接続副詞で、独立した文どうしの対比を示すため、ピリオドやセミコロンのあとに置き、通常カンマで区切ります。\n\n日本語ではすべて「しかし・〜にもかかわらず」と訳せても、文法上の接続力が異なります。however を but と同じように2節の間へカンマだけで置く comma splice は避けましょう。譲歩部分を文頭・文末のどちらに置くかで、先に背景を示すか結論を強調するかも調整できます。',
    examples: [
      { en: 'Although demand increased, the company kept its prices unchanged.', ja: '需要は増えましたが、その会社は価格を据え置きました。', highlight: 'Although demand increased' },
      { en: 'Despite receiving several written complaints, the store changed nothing about its refund policy.', ja: '書面で苦情を何件も受けたにもかかわらず、その店は返金方針を何一つ変えませんでした。', highlight: 'Despite receiving several written complaints' },
      { en: 'The mountain route is about ten kilometres longer. However, it is much safer at night.', ja: '山側の道は10キロほど長いです。しかし、夜間はずっと安全です。', highlight: 'However' },
    ],
  },
  'u28-l2': {
    explanationTitle: '論理標識が結ぶ単位と役割をそろえる',
    explanationBody:
      'therefore は前の内容を原因として結果を導き、moreover / in addition は同じ方向の情報を追加します。これらは文と文を論理的に結ぶ接続副詞で、although のように従属節を直接作る接続詞ではありません。句読点とともに使いましょう。\n\nsuch as は一般的な集合の中から具体例を挙げ、後ろには名詞・名詞句を置きます。for example は文全体の例示にも使えます。標識を多く入れれば良い文章になるわけではなく、前後の関係が読者に明白なところでは省く判断も必要です。因果・追加・例示のどれを示すかを先に決めてください。\n\n**日本語ではこう考える。** 日本語の「そのため」「さらに」「たとえば」は、文頭に置けば読点だけで前の文とつなげます。英語の therefore / moreover / for example は副詞なので、カンマだけで二つの文をつなぐことはできません。The road was icy, therefore we left early. は誤りで、ピリオドかセミコロンで区切る必要があります。接続詞 so / but と接続副詞 therefore / however を、つなぎ方が違うものとして分けて覚えてください。',
    examples: [
      { en: 'The coastal road was flooded again. Therefore, all the buses were diverted through the hills.', ja: '海沿いの道路がまた冠水しました。そのため、バスはすべて丘を回る道に迂回しました。', highlight: 'Therefore' },
      { en: 'The plan is affordable for a small town. Moreover, it can be implemented within a single year.', ja: 'その計画は小さな町にも手が届く費用です。さらに、1年以内に実施できます。', highlight: 'Moreover' },
      { en: 'For this bridge we need durable materials such as steel and reinforced concrete.', ja: 'この橋には鉄や鉄筋コンクリートなどの耐久性のある材料が必要です。', highlight: 'such as steel and reinforced concrete' },
    ],
  },
  'u28-l3': {
    explanationTitle: '標識で読者の現在地を示す',
    explanationBody:
      'first of all / next / finally は手順や論点の順序、in short / to sum up は要約、in other words は同じ内容の言い換えを予告します。これらは情報そのものではなく、文章の中で読者が今どこにいるかを示す案内標識です。\n\nin other words の後ろでは新しい理由を追加せず、前の内容をより明確な表現で言い直します。in short は細部を削って中心結論を残します。機械的に各文頭へ置くと文章が途切れるため、段落の転換点や誤解しやすい箇所に絞り、同じ標識の繰り返しを避けましょう。',
    examples: [
      { en: 'First of all, we need to identify the source of the error.', ja: 'まず最初に、エラーの原因を特定する必要があります。', highlight: 'First of all' },
      { en: 'The device is not backward compatible. In other words, it will not work with older software.', ja: 'その機器には後方互換性がありません。つまり、古いソフトウェアでは動きません。', highlight: 'In other words' },
      { en: 'In short, the benefits of the new procedure clearly outweigh the remaining risks.', ja: '要するに、新しい手順の利点は残るリスクを明らかに上回ります。', highlight: 'In short' },
    ],
  },
  'u29-l1': {
    explanationTitle: 'that節が文中で占める席を確認する',
    explanationBody:
      'that節は「〜ということ」という内容を表し、動詞の目的語、主語、補語、名詞の説明などに使えます。think / say の目的語では that を省略しやすい一方、文頭の主語節や the fact that のように境界を明確にする必要がある場所では通常残します。\n\n関係代名詞の that と違い、名詞節の that は節内で主語・目的語の役割を持たず、後ろの文は要素がそろっています。the news that the store closed は「閉店したという知らせ」という同格、the store that closed は「閉店した店」という関係節です。節内の空席の有無で見分けましょう。\n\n**日本語ではこう考える。** 日本語は「〜ということ」という一つの形で、内容を名詞のように扱えます。英語はここを that節、what節、the fact that の同格節に分岐させるため、日本語から出発すると選べなくなります。判別の鍵は that の後ろが完全な文かどうかです。欠けがなければ同格の that節、主語や目的語が欠けていれば関係詞節になります。主語の位置に置いた that節の that は省略できない点も、日本語には対応がないので意識して覚えましょう。',
    examples: [
      { en: 'The survey shows that most residents support the proposal.', ja: '調査は、住民の大半が提案を支持していることを示しています。', highlight: 'that most residents support the proposal' },
      { en: 'The fact that nobody in the room objected to the proposal surprised me.', ja: '部屋にいた誰もその提案に反対しなかったという事実に驚きました。', highlight: 'The fact that nobody in the room objected' },
      { en: 'I assume the documents have already been sent to the client by courier.', ja: '書類はすでに宅配便で顧客へ送られたものと思います。', highlight: 'the documents have already been sent', note: '目的語の that が省略されています。' },
    ],
  },
  'u29-l2': {
    explanationTitle: '疑問の意味を保ち、語順は平叙文に戻す',
    explanationBody:
      'wh節は what / where / why などが導く「何を〜したか」という内容、whether節は二つ以上の可能性の間の「〜かどうか」を表します。どちらも名詞節なので、内部は疑問文ではなく主語 + 動詞の語順です。do-support も使いません。\n\nwhether は if より形式的で、whether or not、前置詞の後ろ、to不定詞の前、文頭の主語節では whether が必要または好まれます。what は節内で名詞の役割を持ちますが、that は接続だけを担当します。節全体が文のどの要素になっているかも確認しましょう。\n\n**日本語ではこう考える。** 日本語の「〜かどうか」は、主語でも目的語でも前置詞のあとでも同じ形で使えます。英語ではこれが whether と if に分かれ、if は動詞の目的語の位置にしか置けません。主語の位置、前置詞のあと、to不定詞の前ではすべて whether になります。もう一つ、日本語は「どの電車が行くのか教えて」と疑問の形を保ったまま文に埋め込めますが、英語では名詞節の中を平叙文の語順に戻す必要があります。この二点が名詞節での最頻出の誤りです。',
    examples: [
      { en: 'What the committee decides this afternoon will affect every department in the company.', ja: '委員会が今日の午後に決定することは、社内の全部署に影響します。', highlight: 'What the committee decides' },
      { en: 'We discussed whether the benefits justified the cost.', ja: '私たちは、その利点が費用に見合うかどうかを話し合いました。', highlight: 'whether the benefits justified the cost' },
      { en: 'I cannot decide whether to accept the offer or wait for a better one.', ja: 'その申し出を受けるべきか、もっとよい条件を待つべきか決められません。', highlight: 'whether to accept', note: 'to不定詞の前では whether を使います。' },
    ],
  },
  'u29-l3': {
    explanationTitle: '形式主語 it が重い内容を後ろへ運ぶ',
    explanationBody:
      'It is important that ... の it は具体的な物を指さず、長い that節を文末へ置くための形式主語です。英語は短く分かりやすい主語を好むため、That everyone understands the rule is important. より自然な情報配列を作れます。\n\nIt seems that S + V は S seems to do に書き換えられ、過去の内容なら seems to have done を使えます。要求・重要性を表す formal English では It is essential that every member be present. のように原形を使うことがあります。通常の事実を述べる that節と、提案・必要性を表す形を区別しましょう。\n\n**日本語ではこう考える。** 日本語は「〜のは明らかだ」と、内容を先に述べて評価を後ろに置けます。英語は評価を先に出し、長い内容を後ろへ回すために It を仮の主語に立てます。語順が正反対なので、日本語のまま組み立てると That the museum closes on Mondays is not widely known. のように頭でっかちな文になりがちです。文法的には誤りではありませんが、It is not widely known that ... のほうがはるかに自然です。長い主語を見たら It で始め直す、と手を動かして直す習慣をつけましょう。',
    examples: [
      { en: 'It is unlikely that the repairs will finish today, judging by the amount of work left.', ja: '残っている作業量から判断すると、修理が今日終わる可能性は低いです。', highlight: 'It is unlikely that' },
      { en: 'It appears that one page is missing from the middle of the contract.', ja: '契約書の途中から1ページ欠けているようです。', highlight: 'It appears that' },
      { en: 'The witness seems to have changed her account of the evening more than once.', ja: '目撃者はその晩の証言を、一度ならず変えたようです。', highlight: 'seems to have changed' },
    ],
  },
  'u30-l1': {
    explanationTitle: '何を強調するかを決めてから組み立てる',
    explanationBody:
      '強調構文は、元の文で特に伝えたい人物・物・場所などを取り出す形です。Maya found the key in the kitchen. から It was Maya who found the key. なら人物、It was in the kitchen that Maya found the key. なら場所に注目させられます。\n\nWhat I need is a cup of coffee. は、必要なものを後半で示します。日本語の「必要なのは〜だ」に近い流れです。英語の強調には声の強勢や副詞なども使えるので、強調構文が唯一の方法というわけではありません。**何を特に伝えたいか、何と対比しているか**が明確なときに使いましょう。',
    examples: [
      { en: 'It was Lena who noticed the calculation error just before the report was printed.', ja: '報告書が印刷される直前に計算ミスに気づいたのは、レナでした。', highlight: 'It was Lena who' },
      { en: 'It was after midnight that the power finally returned.', ja: '電気がようやく戻ったのは真夜中を過ぎてからでした。', highlight: 'It was after midnight that' },
      { en: 'What we need most at this stage is a clear decision from the head office.', ja: 'この段階で私たちに最も必要なのは、本社からの明確な決定です。', highlight: 'What we need most' },
    ],
  },
  'u30-l2': {
    explanationTitle: '前置した否定表現に疑問文型の語順で応じる',
    explanationBody:
      'never / rarely / only then / not until など否定・制限の表現を文頭へ出すと、主節では助動詞 + 主語 + 動詞という倒置が起きます。助動詞がなければ do / does / did を補い、Never I saw ではなく Never did I see とします。文体は強調的でフォーマルです。\n\nSo do I / Neither do I では、前文の時制・助動詞・be動詞に合わせます。I am tired. に So am I、I cannot swim. に Neither can I です。単なる同意の So I do は語順も意味も異なります。倒置を起こす範囲が前置した節ではなく主節になる Not until ... did ... の形にも注意しましょう。\n\n**日本語ではこう考える。** 日本語は「一度も見たことがない」の強さを、「一度も」という副詞と語尾で表します。語順は変わりません。英語の倒置は、否定語を文頭へ動かし、その代償として助動詞と主語を入れ替えます。つまり英語は語順そのものを強調の道具にしています。So do I / Neither do I も同じ仕組みで、日本語の「私も」が相手の文の形にかかわらず一定なのに対し、英語は相手が使った助動詞に合わせて do / am / can / have を選び直さなければなりません。ここは反射で出るまで音読で練習する価値があります。',
    examples: [
      { en: 'Rarely do we receive such detailed feedback from a first time customer.', ja: '初めてのお客様からこれほど詳しい意見をいただくことは、めったにありません。', highlight: 'Rarely do we receive' },
      { en: 'Not until the next morning did I notice the mistake in the second column.', ja: '翌朝になって初めて、2列目の間違いに気づきました。', highlight: 'did I notice' },
      { en: 'I have never visited Peru, and neither has my sister.', ja: '私はペルーを訪れたことがなく、妹も訪れたことがありません。', highlight: 'neither has my sister' },
    ],
  },
  'u30-l3': {
    explanationTitle: '省略後も復元できる手がかりを残す',
    explanationBody:
      '省略と代用は、前後から内容を一意に復元できるときにだけ自然です。I think so の so は肯定内容全体、I hope not の not は否定内容を代用します。do so は前に述べた動作をやや形式的に受け、助動詞だけを残す形は時制や主語の違いを保ちます。\n\nif necessary / when possible は主語 + be動詞を省いた定型的な節です。省略によって主語が曖昧になったり、時制・態が失われたりする場合は完全な形を使います。また hope so / think so は自然でも、know so などすべての動詞が so を同じように取るわけではないため、組み合わせで覚えましょう。\n\n**日本語ではこう考える。** 日本語は主語も目的語も省略できるため、「そう思います」「まだです」のように語をまるごと落とせます。英語は主語と助動詞を残さなければならず、落とせるのはその後ろだけです。I think so. の so、but I have not. の have がそれにあたります。日本語の感覚で I think. や but I not. としてしまう誤りが典型例です。何を残して何を落とすかが日本語と逆だと意識すると、省略が急に扱いやすくなります。',
    examples: [
      { en: 'Will the budget be approved before the end of the quarter? I certainly hope so.', ja: '四半期末までに予算は承認されますか。ぜひそう願っています。', highlight: 'hope so' },
      { en: 'Mina can solve the problem faster than I can.', ja: 'ミナは私より速くその問題を解けます。', highlight: 'than I can', note: 'can の後ろの solve the problem が省略されています。' },
      { en: 'Please revise the schedule in the shared folder if necessary.', ja: '必要であれば共有フォルダの予定表を修正してください。', highlight: 'if necessary' },
    ],
  },
  'u31-l1': {
    explanationTitle: '同じ期間でも、どこまでの期間かで形が変わる',
    explanationBody:
      '同じ「3年間住んだ」でも、どこまでの3年間かで時制が変わります。I lived there for three years. は終わった過去の期間、I have lived here for three years. は今まで、I had lived there for three years when I moved. は引っ越した時点までの期間です。\n\n**for や since は、現在完了だけの目印ではありません**。過去の基準点までを話すなら過去完了にも使います。また昨日の出来事も、途中を見せれば過去進行形になります。時間表現、基準となる時点、動作をどう見せるかの3つを合わせて判断しましょう。',
    examples: [
      { en: 'By the time the technician arrived, the system had restarted itself.', ja: '技術者が到着するまでに、システムは自動的に再起動していました。', highlight: 'had restarted' },
      { en: 'I have used this software almost every day since I joined the company in 2019.', ja: '2019年に入社して以来、このソフトウェアをほぼ毎日使っています。', highlight: 'have used' },
      { en: 'We were discussing the proposal when the chairperson interrupted us.', ja: '議長が話を遮ったとき、私たちは提案について話し合っていました。', highlight: 'were discussing' },
    ],
  },
  'u31-l2': {
    explanationTitle: '意味の軸と後続形式を別々に検査する',
    explanationBody:
      '紛らわしいペアは、最初に意味の違い、次に後ろに置ける文法形式を検査します。by は締め切りまでの完了、until は境界までの継続です。during + 名詞と while + 主語 + 動詞、despite + 名詞・動名詞と although + 主語 + 動詞は、意味が近くても接続方法が異なります。\n\n動詞との相性も有効な手がかりです。submit / arrive のような到達点を持つ動作は by、wait / remain open のような継続は until と結びつきます。ただし否定文の did not arrive until noon は「正午になって初めて到着した」という遅い開始なので、表面の動詞だけでなく否定を含む構造全体を読みましょう。\n\n**日本語ではこう考える。** 日本語の「まで」が by と until の両方を担っているために、この二つは日本語話者が最後まで間違え続ける組み合わせです。「5時までに出す」は期限なので by、「5時まで待つ」は継続の終点なので until です。訳語ではなく、動作が一回で終わるのか続くのかで判断してください。during と while も同様で、日本語の「〜の間」が名詞にも節にも付くのに対し、英語は during のあとが名詞、while のあとが節と形で決まっています。',
    examples: [
      { en: 'Please submit your expense report by Friday afternoon at the very latest.', ja: '遅くとも金曜日の午後までに経費報告書を提出してください。', highlight: 'by Friday' },
      { en: 'The reception desk remains open until eight on weekdays and until five on Saturdays.', ja: '受付は平日は8時まで、土曜日は5時まで開いています。', highlight: 'until eight' },
      { en: 'Although she felt nervous, she answered every question clearly.', ja: '彼女は緊張していましたが、すべての質問にはっきり答えました。', highlight: 'Although she felt nervous' },
    ],
  },
  'u31-l3': {
    explanationTitle: '直後の名詞と目的語の有無を手がかりにする',
    explanationBody:
      'so / such は程度を強めますが、so + 形容詞・副詞、such + 名詞句が基本です。形容詞と単数名詞が一緒なら such a difficult task または so difficult a task とします。another は不特定の単数を1つ追加し、other は複数名詞・不可算名詞、the other は残りの特定物を指します。\n\nrise は主語自身が上がる自動詞で目的語を取らず、raise は何かを上げる他動詞です。活用も rise–rose–risen と raise–raised–raised で異なります。日本語訳が同じでも、空所の直後に名詞があるか、誰・何が変化を起こすかという文の骨組みを確認すれば選べます。',
    examples: [
      { en: 'The instructions were so clear that nobody asked a question.', ja: '説明がとても明確だったので、誰も質問しませんでした。', highlight: 'so clear that' },
      { en: 'Could I have another copy of the form, because I made a mistake on this one?', ja: 'こちらを書き損じてしまったので、その用紙をもう1部いただけますか。', highlight: 'another copy' },
      { en: 'The central bank raised interest rates after prices rose sharply.', ja: '物価が急上昇したあと、中央銀行は金利を引き上げました。', highlight: 'raised interest rates' },
    ],
  },
  'u32-l1': {
    explanationTitle: '未来の場面を思い浮かべて選ぶ',
    explanationBody:
      'まず「明日の9時に自分は何をしているか」と場面を思い浮かべましょう。仕事の途中なら I will be working at nine.、それまでに仕事が終わる見込みなら I will have finished by nine. です。**進行中の様子か、その時点までの完了か**で形を選びます。\n\nat / by は手がかりですが、形を自動的に決めるスイッチではありません。I will finish by nine. も使えます。また Will you be using the room? は相手の予定を確認する言い方です。時間の形だけでなく、約束するのか、見通しを述べるのか、予定を尋ねるのかも確認しましょう。',
    examples: [
      { en: 'At this time tomorrow the committee will be discussing our proposal in Tokyo.', ja: '明日の今ごろ、委員会は東京で私たちの提案を審議している最中でしょう。', highlight: 'will be discussing' },
      { en: 'By the end of the week the team will have tested all fifty sample units.', ja: '週末までに、チームは50個の試作品すべてを検査し終えているでしょう。', highlight: 'will have tested' },
      { en: 'Will you be joining the online briefing, or would you prefer a written summary?', ja: 'オンラインの説明会には参加なさいますか、それとも書面の要約のほうがよろしいですか。', highlight: 'Will you be joining', note: '未来進行形なので、依頼ではなく予定の確認に響きます。' },
    ],
  },
  'u32-l2': {
    explanationTitle: '当時の予定と、実現したかどうかを分ける',
    explanationBody:
      '過去から見た未来では、「そのとき、これからどうなると思っていたか」を表します。was going to は当時の意図、was about to は直前の状況、would はその時点から先の予測・予定や、物語のその後の展開を伝えます。\n\nwas going to だけで「結局しなかった」とは決まりません。実現したかは but ... などの続きから読み取ります。人の発言を伝える場合も、She said she would come. が基本ですが、予定が今も有効なら She said she will come. とすることもあります。**過去形を見たら機械的にずらすのではなく、どの時点から伝えているか**を確認しましょう。',
    examples: [
      { en: 'We were going to repaint the whole office, but the budget was cut in half.', ja: '事務所全体を塗り直すつもりでしたが、予算が半分に削られました。', highlight: 'were going to repaint' },
      { en: 'I was about to reply when I noticed that she had already sent a correction.', ja: '返信しようとしたそのとき、彼女がすでに訂正を送っていたことに気づきました。', highlight: 'was about to reply' },
      { en: 'The doctor assured us that the treatment would take no more than three months.', ja: '医師は、治療は3か月以内で済むと請け合ってくれました。', highlight: 'would take', note: '主節が過去なので、その中の未来は would にします。' },
    ],
  },
  'u32-l3': {
    explanationTitle: '日本語ではこう考える: 語順で敬意を上げるという発想',
    explanationBody:
      '日本語は丁寧さを語尾で上げます。「知っていたら」を「存じておりましたら」にするように、単語を差し替えて敬意を作ります。英語の倒置条件文はこれと発想が違い、単語はそのままで語順だけを変えて格式を上げます。Had I known は If I had known と語も意味も同じで、変わるのは並べ方だけです。この「語順が敬意になる」という感覚は日本語にないため、初見では回りくどく見えます。\n\n読むときの手順は単純で、文頭に Had / Were / Should が来て、そのあとに主語が続いていたら、頭の中で if を補って読み直せば元の条件文に戻ります。書くときは、契約書やビジネスメールの結びなど改まった場面に限って使い、会話では素直に if を使いましょう。否定を Hadn\'t I known と縮約してしまう誤りだけは、日本語話者に非常に多いので注意してください。',
    examples: [
      { en: 'Had we been told about the change earlier, we could have adjusted the schedule.', ja: '変更をもっと早く知らされていたら、日程を調整できたでしょう。', highlight: 'Had we been told' },
      { en: 'Were the deadline to be moved forward, the whole team would have to work weekends.', ja: '万一締め切りが前倒しになれば、チーム全員が週末も働かなければならないでしょう。', highlight: 'Were the deadline to be moved' },
      { en: 'Should you decide to withdraw your application, please inform us in writing.', ja: '万一応募を取り下げることになりましたら、書面でお知らせください。', highlight: 'Should you decide', note: 'ビジネスメールの結びで非常によく使われる形です。' },
    ],
  },
  'u32-l4': {
    explanationTitle: '日本語ではこう考える: 「〜ほど…」の連動と、程度を表す副詞',
    explanationBody:
      '日本語の「読めば読むほど」は前半だけで連動を示せますが、英語は前半と後半の両方に the を置いて初めて構文が成立します。The more you read, better you understand のように後半の the を落とす誤りが非常に多いので、二つで一組と覚えてください。また日本語は「本をたくさん読むほど」と名詞を後ろに残せますが、英語は The more books you read のように名詞ごと前へ移します。\n\nもう一つの落とし穴が very です。日本語の「とても」は「とても大きい」にも「とても大きくなった」にも使えるため、very bigger と言ってしまいがちです。英語では比較級を強めるのは far / much / a lot / considerably で、very は原級専用だと割り切りましょう。差が小さいときの a little / slightly も合わせて覚えると、報告や説明で数値の変化を正確に伝えられます。',
    examples: [
      { en: 'The more detailed your notes are, the easier the revision becomes later on.', ja: 'メモが詳しいほど、あとの復習は楽になります。', highlight: 'The more detailed' },
      { en: 'The rent here is considerably higher than in the town where I grew up.', ja: 'ここの家賃は、私が育った町よりかなり高いです。', highlight: 'considerably higher' },
      { en: 'This version is only slightly slower, but it uses far less memory than before.', ja: 'この版はわずかに遅いだけですが、以前よりはるかに少ないメモリで動きます。', highlight: 'slightly slower', note: '差の大きさに応じて slightly と far を使い分けています。' },
    ],
  },
  'u33-l1': {
    explanationTitle: '聞き手と共有できるかを確かめる',
    explanationBody:
      '冠詞を選ぶときは、話し手だけでなく**聞き手がどれを指すか分かるか**を確認します。I bought a book. のあとに The book was expensive. と続けるのは、同じ本がすでに会話に登場したからです。初めて言う場合でも、部屋のドアが1つなら Please close the door. と言えます。\n\n日本語の「が」「は」と a / the は一対一には対応しません。また、複数・不可算名詞は、無冠詞で一般論を述べることも、some で不特定の数・量を表すこともできます。Dogs need water. と Some dogs are outside. を比べ、特定できるかに加えて、**種類全体か一部か**を考えましょう。',
    examples: [
      { en: 'I ordered a coffee and a sandwich, but the sandwich never arrived at our table.', ja: 'コーヒーとサンドイッチを注文しましたが、サンドイッチはとうとう来ませんでした。', highlight: 'the sandwich', note: '初出は a、既出は the。日本語の「が」と「は」に近い対立です。' },
      { en: 'Teachers in this country receive very little training in dealing with such cases.', ja: 'この国の教師は、そうした事例への対応についてほとんど研修を受けていません。', highlight: 'Teachers', note: '一般論なので無冠詞の複数にします。' },
      { en: 'The equipment in the older laboratory has not been replaced since the 1990s.', ja: '古い実験室の設備は、1990年代から交換されていません。', highlight: 'The equipment', note: 'equipment は不可算なので複数形にせず、限定されているので the を付けます。' },
    ],
  },
  'u33-l2': {
    explanationTitle: '少なさの捉え方と、of の形を分けて確認する',
    explanationBody:
      'few / little は「ほとんどない」と少なさに注目し、a few / a little は「少しある」と存在を伝えます。few / a few は可算名詞の複数形、little / a little は不可算名詞と組み合わせます。ただし、a が付いても十分な量とは限りません。I have a little time, but not enough. と続けることもできます。\n\nof は表現ごとに確認しましょう。most students に対して most of the students / most of them とします。一方 all the students は of がなくても正しい形です。**限定語があれば何でも of が必須**とまとめず、表の組み合わせで覚えましょう。',
    examples: [
      { en: 'Few of the residents we interviewed had even heard about the new regulation.', ja: '取材した住民のうち、新しい規則を耳にしたことがある人さえほとんどいませんでした。', highlight: 'Few of the residents' },
      { en: 'We still have a little money left, so we can afford one more night here.', ja: 'まだ少しお金が残っているので、もう一泊できます。', highlight: 'a little money' },
      { en: 'Most visitors to this island arrive by ferry rather than by small aircraft.', ja: 'この島を訪れる人の大半は、小型機ではなくフェリーで到着します。', highlight: 'Most visitors', note: '限定語がないので of は付けません。' },
    ],
  },
  'u33-l3': {
    explanationTitle: '日本語ではこう考える: 「それを消して」の語順',
    explanationBody:
      '分離できる句動詞では、turn off the light / turn the light off のどちらも使えます。しかし、目的語が it なら turn it off にします。日本語では「電気を消す」「それを消す」の語順が同じなので、英語では代名詞になったところを特に確認しましょう。\n\nこの規則は、look after のように分離できない表現には当てはまりません。look after them が正しい形です。**辞書で分離できるかを確認し、次に目的語が代名詞かを見る**のが手順です。分離できる表現でも、長い目的語は後ろに置いたほうが読みやすくなることがあります。',
    examples: [
      { en: 'I have printed the contracts, so could you check them over before lunch?', ja: '契約書を印刷したので、昼食前に目を通していただけますか。', highlight: 'check them over', note: '代名詞は動詞と副詞の間に入ります。' },
      { en: 'The committee will look into the complaint and report back within two weeks.', ja: '委員会は苦情を調査し、2週間以内に報告します。', highlight: 'look into the complaint', note: 'look into は分離できない型です。' },
      { en: 'Please write down the reference number before you close the booking page.', ja: '予約画面を閉じる前に、照会番号を書き留めておいてください。', highlight: 'write down the reference number' },
    ],
  },
} satisfies LessonExpansionMap
