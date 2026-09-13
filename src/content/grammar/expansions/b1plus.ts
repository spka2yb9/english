import type { LessonExpansionMap } from './types'

export const b1PlusExpansions = {
  'u17-l1': {
    explanationTitle: '継続時間だけでなく活動の手触りを伝える',
    explanationBody:
      '現在完了進行形は、過去から今まで続く活動を have / has been + -ing で表します。単に期間を述べるだけでなく、「その活動にずっと取り組んでいる」という動きや一時性を感じさせます。How long ...?、for、since とよく組み合わさります。\n\n動作がたった今終わっていても、汗・濡れた地面など現在に証拠が残る場合に使えます。一方 know・own・belong など状態動詞は通常進行形にせず現在完了を使います。have been の been を落とさず、疑問文では Have you been waiting? と最初の have を前へ出しましょう。',
    examples: [
      { en: 'I have been learning sign language since January.', ja: '私は1月から手話を学び続けています。', highlight: 'have been learning' },
      { en: 'How long has the dog been barking?', ja: 'その犬はどのくらい吠え続けていますか。', highlight: 'has the dog been barking' },
      { en: 'Your clothes are wet. Have you been walking in the rain?', ja: '服が濡れていますね。雨の中を歩いていたのですか。', highlight: 'Have you been walking', note: '活動は終わっていても、今に証拠が残っています。' },
    ],
  },
  'u17-l2': {
    explanationTitle: '完成量か、活動の継続かを選ぶ',
    explanationBody:
      '現在完了は完成した結果・回数・量に焦点を当て、現在完了進行形は活動の長さ・途中経過・一時性を前面に出します。I have written three pages. は完成量、I have been writing for two hours. は執筆という活動の継続が中心です。\n\nlive・work・teach などは両方が可能で、長く安定した事実には現在完了、継続中の活動を強調するなら進行形が選ばれやすい傾向があります。know のような状態動詞や、finish のように完了点そのものを表す場合は進行形にしません。目的語の数量や still などの文脈も判断材料にしましょう。',
    examples: [
      { en: 'Nora has answered twenty emails this morning.', ja: 'ノラは今朝、メールに20通返信しました。', highlight: 'has answered', note: '完了した量に焦点があります。' },
      { en: 'Nora has been answering emails all morning.', ja: 'ノラは午前中ずっとメールに返信しています。', highlight: 'has been answering' },
      { en: 'We have known each other for more than a decade.', ja: '私たちは10年以上の知り合いです。', highlight: 'have known' },
    ],
  },
  'u18-l1': {
    explanationTitle: '過去の基準点を先に見つける',
    explanationBody:
      '過去完了は、単に「かなり昔」を表す形ではなく、過去の基準点より前の出来事や、その時点までの経験・継続を示します。when we arrived / by then や前後の文脈から「どの過去を基準にしているか」を探しましょう。\n\n形はすべての主語で had + 過去分詞です。副詞は had already left / had never seen のように had と過去分詞の間に置くのが基本です。一方、「以前に」の before は I had seen it before. のように文末に置きます。語の位置まで含めて覚えると、文を組み立てやすくなります。',
    examples: [
      { en: 'The guests had already left when we reached the restaurant.', ja: '私たちがレストランに着いたとき、客はすでに帰っていました。', highlight: 'had already left' },
      { en: 'I had never driven in snow before that trip.', ja: 'その旅行以前、私は雪道を運転したことがありませんでした。', highlight: 'had never driven' },
      { en: 'Had the meeting started by the time you arrived?', ja: 'あなたが到着するまでに会議は始まっていましたか。', highlight: 'Had the meeting started' },
    ],
  },
  'u18-l2': {
    explanationTitle: '順序が明白なら過去完了を使いすぎない',
    explanationBody:
      '過去完了は前後関係を明確にする道具ですが、すべての古い出来事に付ける必要はありません。after / before が順序を十分示す場合や、出来事を発生順に並べる場合は過去形だけでも自然です。過去完了を連続させると、物語の基準点が見えにくくなります。\n\n語る順序が実際の発生順と逆になるとき、過去完了の価値が高まります。When I opened the door, I realized someone had entered. では、侵入が気づきより前だと示します。一度時間関係を確立したあとは、必要に応じて過去形へ戻して物語を進められます。',
    examples: [
      { en: 'After we checked the map, we continued our journey.', ja: '地図を確認してから、旅を続けました。', highlight: 'checked', note: 'after が順序を示すため、両方とも過去形で自然です。' },
      { en: 'When I opened the file, I saw that someone had changed it.', ja: 'ファイルを開くと、誰かが変更していたことに気づきました。', highlight: 'had changed' },
      { en: 'She apologized because she had misunderstood my message.', ja: '彼女は私のメッセージを誤解していたので謝りました。', highlight: 'had misunderstood' },
    ],
  },
  'u18-l3': {
    explanationTitle: '前景・背景・さらに前を時制で描き分ける',
    explanationBody:
      '物語では、過去形が出来事を順に進める前景、過去進行形がその場で続いていた背景、過去完了が基準より前の経緯を担当します。すべてを同じ時制にせず、読者にどこへカメラを向けるかを時制で示します。\n\nまず過去形で基準となる場面を置き、必要なときだけ過去完了で回想し、再び過去形へ戻ると読みやすくなります。突然の出来事には過去形、すでに進行していた活動には過去進行形を選びます。接続詞だけに頼らず、時制そのものが作る時間関係を意識しましょう。',
    examples: [
      { en: 'The wind was blowing hard when our lights went out.', ja: '風が激しく吹いていたとき、家の明かりが消えました。', highlight: 'was blowing' },
      { en: 'I reached for my phone, but I had left it upstairs.', ja: '携帯に手を伸ばしましたが、2階に置いてきていました。', highlight: 'had left' },
      { en: 'We found some candles and waited for the power to return.', ja: '私たちはろうそくを見つけ、電気が戻るのを待ちました。', highlight: 'found' },
    ],
  },
  'u19-l1': {
    explanationTitle: '発言時から報告時へ視点を移す',
    explanationBody:
      '人の発言をあとから伝えるときは、時制だけでなく、人称・場所・時間の視点も報告する立場に合わせます。I は話した人に応じて he / she に、here は there、tomorrow は the next day などに変わる可能性があります。機械的な置換ではなく、今どこから誰が報告しているかを考えます。\n\nsaid が過去なら現在形を過去形、過去形を過去完了へずらすのが基本です。ただし今も変わらない事実は The teacher said water boils at one hundred degrees. のように現在形を保つことがあります。that は会話では省略できますが、長い文では残すと境界が明確です。',
    examples: [
      { en: 'Mika said that she was working from home that day.', ja: 'ミカは、その日は在宅勤務をしていると言いました。', highlight: 'she was working' },
      { en: 'Leo told me that he had lost his ticket.', ja: 'レオは切符をなくしたと私に言いました。', highlight: 'he had lost' },
      { en: 'The guide said that the museum opens at nine.', ja: 'ガイドは、その美術館は9時に開くと言いました。', highlight: 'the museum opens', note: '今も有効な時刻表なので現在形を保っています。' },
    ],
  },
  'u19-l2': {
    explanationTitle: '質問の形をやめて、内容として埋め込む',
    explanationBody:
      '質問を人に伝えるとき、元の疑問文は reported question という文の一部になります。そのため語順は疑問文ではなく主語 + 動詞へ戻し、do / does / did は消えます。Yes / No疑問文には if / whether、Wh疑問文には元の疑問詞を残します。\n\n指示・依頼は told / asked + 人 + to do、否定は told / asked + 人 + not to do です。say は直接人を目的語に取らないため said me to とはしません。質問を伝えているのか、行動を求めた発言を伝えているのかを先に分類しましょう。',
    examples: [
      { en: 'She asked me whether I needed a receipt.', ja: '彼女は私に領収書が必要か尋ねました。', highlight: 'whether I needed' },
      { en: 'The officer asked where we were staying.', ja: '係員は私たちがどこに滞在しているか尋ねました。', highlight: 'where we were staying' },
      { en: 'Dad told us not to leave the door unlocked.', ja: '父は私たちにドアの鍵を開けたままにしないよう言いました。', highlight: 'told us not to leave' },
    ],
  },
  'u19-l3': {
    explanationTitle: '伝達動詞ごとの文型まで覚える',
    explanationBody:
      'reporting verb は発言内容だけでなく、約束・提案・警告など話し手の意図を伝えます。ただし後ろの形は動詞ごとに異なります。promise / offer / refuse は to do、suggest / recommend は doing または that節、warn は warn 人 not to do などの型を取ります。\n\n日本語の「〜することを提案した」から suggest to do としないよう注意してください。tell は聞き手を必要としますが、say は内容を直接続けます。新しい伝達動詞は意味だけでなく、誰を目的語に置けるか、次が不定詞・動名詞・that節のどれかまで例文で記録しましょう。',
    examples: [
      { en: 'The airline offered to change our seats.', ja: '航空会社は座席を変更すると申し出ました。', highlight: 'offered to change' },
      { en: 'Mina suggested taking an earlier train.', ja: 'ミナはもっと早い電車に乗ることを提案しました。', highlight: 'suggested taking' },
      { en: 'The doctor warned him not to drive.', ja: '医師は彼に運転しないよう警告しました。', highlight: 'warned him not to drive' },
    ],
  },
  'u19-l4': {
    explanationTitle: '文全体だけを疑問文の語順にする',
    explanationBody:
      '間接疑問では、Do you know ...? / Could you tell me ...? という外側だけが疑問文です。内側の疑問内容は where the station is のように肯定文の語順へ戻します。疑問詞の直後に動詞を置く where is the station は直接疑問の語順です。\n\nYes / Noの内容なら if / whether を使い、Do you know whether the shop is open? とします。文末の疑問符は外側が質問のときだけ必要です。I wonder where he lives. は丁寧な疑問内容を述べる平叙文なのでピリオドです。do-support を消したあとの動詞の時制・三単現も忘れずに戻しましょう。',
    examples: [
      { en: 'Could you tell me where platform six is?', ja: '6番線がどこか教えていただけますか。', highlight: 'where platform six is' },
      { en: 'Do you know whether this bus stops at City Hall?', ja: 'このバスが市役所に止まるか知っていますか。', highlight: 'whether this bus stops' },
      { en: 'I wonder why the lights are still on.', ja: 'なぜまだ明かりがついているのでしょう。', highlight: 'why the lights are still on' },
    ],
  },
  'u20-l1': {
    explanationTitle: '証拠からの結論と単なる事実を区別する',
    explanationBody:
      '推量の must / might / cannot は、目に見える手がかりや知っている事実から話し手が導いた結論を示します。must はほぼ確信、might / may / could は可能性、cannot は論理的にあり得ないという判断です。義務の must や能力の can とは文脈で区別します。\n\n現在進行中のことなら must be doing、状態なら must be + 形容詞・名詞を使えます。否定の強い推量は cannot で、must not は通常禁止です。確信のない否定は might not とし、「あり得ない」と「そうでない可能性がある」の強さを分けましょう。',
    examples: [
      { en: 'The kitchen smells wonderful. Kai must be cooking.', ja: 'キッチンからいい香りがします。カイが料理をしているに違いありません。', highlight: 'must be cooking' },
      { en: 'This cannot be the right address because the number is different.', ja: '番号が違うので、ここが正しい住所のはずはありません。', highlight: 'cannot be' },
      { en: 'Rina might not be available this afternoon.', ja: 'リナは今日の午後、都合がつかないかもしれません。', highlight: 'might not be' },
    ],
  },
  'u20-l2': {
    explanationTitle: '助動詞の確信度を過去へそのまま移す',
    explanationBody:
      '過去の推量は、現在の確信度を表す助動詞の後ろに have + 過去分詞を置きます。must have done は強い肯定、might have done は可能性、cannot have done は強い否定です。推量している時点は今でも、判断対象が過去なので完了形を使います。\n\n語順は助動詞 + have + 過去分詞で固定され、must had や must have went とはしません。must have done は過去の義務ではなく「したに違いない」で、義務は had to do です。現在に残る証拠と、そこから推測する過去の出来事を分けて読み取りましょう。',
    examples: [
      { en: 'The door was unlocked. Someone must have entered the office.', ja: 'ドアの鍵が開いていました。誰かがオフィスに入ったに違いありません。', highlight: 'must have entered' },
      { en: 'Nora might have misunderstood the instructions.', ja: 'ノラは指示を誤解したのかもしれません。', highlight: 'might have misunderstood' },
      { en: 'They cannot have finished already because I can still hear them working.', ja: 'まだ作業する音が聞こえるので、彼らがもう終えたはずはありません。', highlight: 'cannot have finished' },
    ],
  },
  'u20-l3': {
    explanationTitle: '現実に起きなかった側まで読み取る',
    explanationBody:
      'should have done は望ましい行動をしなかった、should not have done は望ましくない行動をしてしまった、という現実を含みます。could have done は可能だったのに実現しなかった選択肢、または起こり得た危険を表します。形だけでなく暗示される事実まで読みましょう。\n\n相手に You should have ... と言うと非難に響くことがあるため、I wish we had ... や Next time, could we ...? のほうが協力的な場面もあります。could not have done は「どうしてもできなかったはず」で、I could not have done it without you. は強い感謝に使われます。',
    examples: [
      { en: 'I should have checked the opening hours first.', ja: '最初に営業時間を確認しておくべきでした。', highlight: 'should have checked' },
      { en: "We shouldn't have ignored that warning.", ja: '私たちはあの警告を無視すべきではありませんでした。', highlight: "shouldn't have ignored" },
      { en: 'A helmet could have prevented the injury.', ja: 'ヘルメットがあれば、そのけがを防げたかもしれません。', highlight: 'could have prevented' },
    ],
  },
  'u20-l4': {
    explanationTitle: '過去の状態には used to、反復動作には would',
    explanationBody:
      'used to は今とは違う過去の習慣・状態を表します。used to live のような状態にも、used to walk のような反復動作にも使え、通常は「今はそうではない」という対比を含みます。would は物語の中で繰り返した動作を回想するときに使います。\n\nwould は know・be・have のような状態には原則使えず、過去の時期を示す文脈も必要です。否定・疑問は did not use to / Did ... use to? と、did の後ろを原形 use にするのが標準です。be used to doing の「〜に慣れている」とも形・意味を区別してください。',
    examples: [
      { en: 'This building used to be a post office.', ja: 'この建物は以前、郵便局でした。', highlight: 'used to be' },
      { en: 'Every summer, our grandfather would take us fishing.', ja: '毎年夏になると、祖父は私たちを釣りに連れていってくれたものです。', highlight: 'would take' },
      { en: "Did you use to wear glasses?", ja: '以前は眼鏡をかけていましたか。', highlight: 'Did you use to wear' },
    ],
  },
  'u21-l1': {
    explanationTitle: 'to はこれから、-ing は経験済みの行為へ向く',
    explanationBody:
      '形で意味が変わる動詞には共通する感覚があります。to不定詞はこれから行う目的・必要、動名詞はすでに行ったことや活動そのものを指しやすい形です。remember to lock はこれから忘れず施錠する、remember locking は施錠した記憶がある、という違いです。\n\nstop to do は別の目的のために今の動作を止め、stop doing はその活動自体をやめます。try to do は達成を試み、try doing は方法として試してみる意味です。ただし感覚だけに頼らず、各ペアを対照例文で覚え、文脈の時間順序を図にすると確実です。',
    examples: [
      { en: 'Remember to attach the file before you send the email.', ja: 'メールを送る前にファイルを添付するのを忘れないでください。', highlight: 'Remember to attach' },
      { en: 'I remember meeting her at a conference in Seoul.', ja: 'ソウルの会議で彼女に会ったことを覚えています。', highlight: 'remember meeting' },
      { en: 'If the screen freezes, try restarting the computer.', ja: '画面が固まったら、コンピューターを再起動してみてください。', highlight: 'try restarting', note: '解決方法として試す意味です。' },
    ],
  },
  'u21-l2': {
    explanationTitle: '行動する人を目的語で明示する',
    explanationBody:
      'want / ask / tell / expect / allow + 人 + to do では、目的語の人が to不定詞の動作主になります。I want to leave. は私が去る、I want him to leave. は彼に去ってほしい、という違いです。代名詞は me / him / them など目的格を使います。\n\n否定は ask someone not to do のように not を to の直前に置きます。make / let のように原形を取る使役動詞とは型が異なります。また allow は受動態になると be allowed to do と to が残ります。誰が最初の動詞を行い、誰が不定詞の動作を行うかを矢印で分けましょう。',
    examples: [
      { en: 'The coach encouraged us to keep practicing.', ja: 'コーチは私たちに練習を続けるよう励ましました。', highlight: 'encouraged us to keep' },
      { en: 'Please remind me to buy some batteries.', ja: '電池を買うよう私に念を押してください。', highlight: 'remind me to buy' },
      { en: 'Visitors are not allowed to take photographs here.', ja: 'ここでは訪問者は写真を撮ることを許可されていません。', highlight: 'are not allowed to take' },
    ],
  },
  'u21-l3': {
    explanationTitle: '評価する内容を後ろに置いて読みやすくする',
    explanationBody:
      'It is + 形容詞 + to do は、長い行動内容を文末へ置き、最初に easy / important / dangerous などの評価を伝える構文です。誰にとっての評価かを示すなら for + 人を加え、It is difficult for me to choose. とします。\n\n名詞 + be + 形容詞 + to do の形では、主語の名詞が不定詞内の目的語として解釈されることがあります。This bag is easy to carry. は「このバッグを運ぶのが簡単」で、carry it と it を重ねません。人の性質を評価する It was kind of you to help. の of + 人との違いも文脈で押さえましょう。',
    examples: [
      { en: 'It is essential to keep your contact details up to date.', ja: '連絡先情報を最新に保つことが不可欠です。', highlight: 'It is essential to keep' },
      { en: 'This form is difficult to complete on a phone.', ja: 'この用紙は携帯電話では記入しにくいです。', highlight: 'difficult to complete' },
      { en: 'It was thoughtful of you to bring extra umbrellas.', ja: '予備の傘を持ってきてくれるとは、気が利いていました。', highlight: 'thoughtful of you to bring' },
    ],
  },
  'u22-l1': {
    explanationTitle: '事実を反転させて過去の別世界を描く',
    explanationBody:
      '第3条件文は、実際には起きなかった過去の条件と結果を想像します。If I had set an alarm, I would have woken up. なら現実は「アラームを設定しなかったので起きられなかった」です。英文を理解するときは、仮定文を現実の文へ反転させて確認しましょう。\n\nif節は had + 過去分詞、結果節は would / could / might have + 過去分詞です。had と would はどちらも apostrophe d に短縮されるため、後ろが過去分詞なら had、原形なら would と見分けます。if節に would have を入れないことも重要です。',
    examples: [
      { en: 'If we had booked earlier, we would have paid less.', ja: 'もっと早く予約していれば、支払いは少なく済んだでしょう。', highlight: 'If we had booked earlier' },
      { en: 'She might have caught the train if she had taken a taxi.', ja: 'タクシーに乗っていれば、彼女は電車に間に合ったかもしれません。', highlight: 'might have caught' },
      { en: 'If you had not called, I would have missed the deadline.', ja: 'あなたが電話してくれなかったら、締め切りに間に合わなかったでしょう。', highlight: 'had not called' },
    ],
  },
  'u22-l2': {
    explanationTitle: '願いの時間を動詞の形で示す',
    explanationBody:
      'wish の後ろでは、現実との距離を時制を1段階戻して示します。現在の事実と違う願いは過去形、過去への後悔は過去完了です。I wish I knew. は今知らない、I wish I had known. はそのとき知らなかった、という現実を含みます。\n\nwish + could は能力・可能性への願い、wish + would は他人や状況が変わってほしいという不満・要望に使います。自分の意志的行動に I wish I would ... は通常使いません。if only は wish より感情が強く、同じ時制の規則に従います。',
    examples: [
      { en: 'I wish our apartment had a balcony.', ja: '私たちのアパートにバルコニーがあればいいのに。', highlight: 'wish our apartment had' },
      { en: 'If only I had saved a copy of the document.', ja: 'その書類のコピーを保存しておけばよかったのに。', highlight: 'If only I had saved' },
      { en: 'I wish the neighbors would turn down the music.', ja: '近所の人が音楽の音量を下げてくれればいいのですが。', highlight: 'wish the neighbors would turn down' },
    ],
  },
  'u22-l3': {
    explanationTitle: '条件と結果が属する時間を別々に決める',
    explanationBody:
      '条件文を総合的に選ぶときは、型の番号より先に、条件が一般・未来・現在・過去のどこにあるかを決めます。一般法則はゼロ、現実的な未来は第1、現在の非現実は第2、過去の非現実は第3です。その後でif節と結果節の形をそろえます。\n\n第2・第3条件文は現実の裏返しなので、文が暗示する事実も確認します。If I were free は今は暇でない、If I had been free はそのとき暇でなかった、です。時間を示す now / tomorrow / yesterday と、結果が will / would / would have のどれかを手がかりに、両方の節を個別に点検しましょう。',
    examples: [
      { en: 'If you heat ice, it melts.', ja: '氷を温めると溶けます。', highlight: 'If you heat ice' },
      { en: 'If I finish early tomorrow, I will pick you up.', ja: '明日早く終われば、迎えに行きます。', highlight: 'If I finish early tomorrow' },
      { en: 'If we had checked the forecast, we would have changed our plans.', ja: '天気予報を確認していれば、予定を変更していたでしょう。', highlight: 'would have changed' },
    ],
  },
} satisfies LessonExpansionMap
