import type { GrammarExample } from '../../types'

/**
 * 全セクションの例文を10文へそろえるための追加分。
 * 既存の教材ファイルは書き換えず、語彙の notes.ts / collocations.ts と同じ方式でここへ合流させる。
 * 例文10文がそのままセクション内の並べ替え10問の母集団になるため、すべて4語以上にする。
 */
export const extraExamples: Record<string, GrammarExample[]> = {
  'u01-l1': [
    { en: 'I am not ready for the test.', ja: '私はそのテストの準備ができていません。', highlight: 'am not' },
  ],
  'u01-l2': [
    { en: 'My father goes to the gym on Saturdays.', ja: '父は土曜日にジムへ行きます。', highlight: 'goes' },
    { en: 'Our teacher has two children.', ja: '私たちの先生には子どもが2人います。', highlight: 'has', note: 'have は三単現で has になります。' },
  ],
  'u01-l3': [
    { en: 'Does your father cook on weekends?', ja: 'お父さんは週末に料理をしますか。', highlight: 'Does' },
    { en: "They don't live near the station.", ja: '彼らは駅の近くには住んでいません。', highlight: "don't live" },
  ],
  'u02-l1': [
    { en: 'They are building a new library near the park.', ja: '公園の近くに新しい図書館が建てられています。', highlight: 'are building' },
    { en: 'My phone is charging in the kitchen.', ja: '私の携帯は台所で充電中です。', highlight: 'is charging' },
  ],
  'u02-l2': [
    { en: 'He usually walks to school, but today he is taking the bus.', ja: '彼はふだん歩いて学校へ行きますが、今日はバスに乗っています。', highlight: 'is taking' },
    { en: 'I want a cup of coffee right now.', ja: '今すぐコーヒーが1杯ほしいです。', highlight: 'want', note: 'want は状態を表すため、通常は進行形にしません。' },
  ],
  'u02-l3': [
    { en: 'They built this bridge about fifty years ago.', ja: 'この橋は約50年前に造られました。', highlight: 'built' },
  ],
  'u02-l4': [
    { en: 'We were waiting at the gate when the announcement came.', ja: 'アナウンスが流れたとき、私たちはゲートで待っていました。', highlight: 'were waiting' },
    { en: 'The children were drawing pictures while their mother was cooking.', ja: '母親が料理をしている間、子どもたちは絵を描いていました。', highlight: 'were drawing' },
  ],
  'u02-l5': [
    { en: 'I will send you the file after this meeting.', ja: 'この会議のあとでファイルをお送りします。', highlight: 'will send' },
  ],
  'u02-l6': [
    { en: 'They are going to open a bakery next month.', ja: '彼らは来月パン屋を開く予定です。', highlight: 'are going to open' },
    { en: 'I am not going to buy a new car this year.', ja: '今年は新しい車を買うつもりはありません。', highlight: 'am not going to buy' },
  ],
  'u03-l1': [
    { en: 'Could you bring me a glass of water?', ja: 'お水を1杯持ってきてもらえますか。', highlight: 'a glass of water' },
    { en: 'Our luggage is still at the airport.', ja: '私たちの荷物はまだ空港にあります。', highlight: 'luggage is', note: 'luggage は不可算なので動詞は is です。' },
  ],
  'u03-l2': [
    { en: 'He is an honest and careful driver.', ja: '彼は正直で慎重な運転手です。', highlight: 'an honest' },
    { en: 'She wants to visit a European city this summer.', ja: '彼女はこの夏ヨーロッパの都市を訪れたがっています。', highlight: 'a European city', note: 'European は「ユ」という子音の音で始まります。' },
  ],
  'u03-l3': [
    { en: 'We usually go to work by train.', ja: '私たちはふだん電車で通勤します。', highlight: 'by train', note: '交通手段の by train は無冠詞です。' },
    { en: 'My daughter practices the violin every evening.', ja: '娘は毎晩バイオリンを練習します。', highlight: 'the violin', note: '楽器には the を付けます。' },
    { en: 'The restaurant on the corner closes at ten.', ja: '角のレストランは10時に閉まります。', highlight: 'The restaurant on the corner' },
  ],
  'u03-l4': [
    { en: "There aren't any seats left on this train.", ja: 'この電車には空いている席がまったくありません。', highlight: "aren't any" },
    { en: 'We invited a lot of friends to the party.', ja: '私たちはパーティーにたくさんの友人を招待しました。', highlight: 'a lot of' },
  ],
  'u04-l1': [
    { en: 'His sister called her yesterday afternoon.', ja: '彼のお姉さんが昨日の午後、彼女に電話しました。', highlight: 'His sister called her', note: 'his は名詞の前なので所有格、her は動詞のあとなので目的格です。' },
  ],
  'u04-l2': [
    { en: 'Are these your gloves or mine?', ja: 'これらはあなたの手袋ですか、それとも私のですか。', highlight: 'these' },
    { en: 'Those houses across the river look new.', ja: '川の向こうのあの家々は新しく見えます。', highlight: 'Those houses' },
  ],
  'u04-l3': [
    { en: 'My umbrella broke, so I bought a stronger one.', ja: '傘が壊れたので、もっと丈夫なものを買いました。', highlight: 'a stronger one' },
    { en: 'She borrowed my dictionary and returned it this morning.', ja: '彼女は私の辞書を借りて、今朝それを返してくれました。', highlight: 'it', note: '話に出たまさにその辞書なので it です。' },
  ],
  'u05-l1': [
    { en: 'I would like something cold to drink.', ja: '何か冷たい飲み物がほしいです。', highlight: 'something cold', note: 'something のあとでは形容詞を後ろに置きます。' },
    { en: 'They sell fresh bread at that little shop.', ja: 'あの小さな店では焼きたてのパンを売っています。', highlight: 'fresh bread' },
  ],
  'u05-l2': [
    { en: 'He drives carefully on narrow streets.', ja: '彼は狭い道では慎重に運転します。', highlight: 'carefully' },
  ],
  'u05-l3': [
    { en: 'I often forget my umbrella at the office.', ja: '私はよく会社に傘を忘れます。', highlight: 'often forget' },
    { en: 'My grandmother always walks to the market.', ja: '祖母はいつも市場まで歩いて行きます。', highlight: 'always walks' },
  ],
  'u06-l1': [
    { en: 'When did you move to this city?', ja: 'いつこの街へ引っ越してきたのですか。', highlight: 'When did' },
  ],
  'u06-l2': [
    { en: 'How much does a ticket cost?', ja: 'チケットはいくらしますか。', highlight: 'How much' },
    { en: 'How long is the flight to Seoul?', ja: 'ソウルまでの飛行時間はどのくらいですか。', highlight: 'How long' },
  ],
  'u06-l3': [
    { en: 'Who lives in that old house?', ja: 'あの古い家には誰が住んでいるのですか。', highlight: 'Who lives', note: '疑問詞の主語は3人称単数扱いなので lives です。' },
    { en: 'What broke the window last night?', ja: '昨夜、何が窓を割ったのですか。', highlight: 'What broke' },
  ],
  'u07-l1': [
    { en: 'The new office is closer to the station than the old one.', ja: '新しいオフィスは古いオフィスより駅に近いです。', highlight: 'closer to the station than' },
  ],
  'u07-l2': [
    { en: 'This is the longest bridge in the country.', ja: 'これはこの国で最も長い橋です。', highlight: 'the longest bridge in' },
    { en: 'That was the most difficult question of the exam.', ja: 'あれは試験で最も難しい問題でした。', highlight: 'the most difficult question of' },
  ],
  'u07-l3': [
    { en: 'This chair is not as comfortable as the old one.', ja: 'この椅子は古い椅子ほど快適ではありません。', highlight: 'not as comfortable as' },
    { en: 'She speaks English as naturally as her teacher.', ja: '彼女は先生と同じくらい自然に英語を話します。', highlight: 'as naturally as' },
  ],
  'u07-l4': [
    { en: 'The suitcase was too heavy for me to lift.', ja: 'そのスーツケースは重すぎて、私には持ち上げられませんでした。', highlight: 'too heavy for me to lift' },
  ],
  'u08-l1': [
    { en: 'The library closes at nine on weekdays.', ja: '図書館は平日は9時に閉まります。', highlight: 'at nine on weekdays' },
  ],
  'u08-l2': [
    { en: 'She was reading a book on the train.', ja: '彼女は電車で本を読んでいました。', highlight: 'on the train', note: '電車・バス・飛行機は on、乗用車は in です。' },
  ],
  'u08-l3': [
    { en: 'They arrived in Osaka late at night.', ja: '彼らは夜遅くに大阪に着きました。', highlight: 'arrived in', note: '都市・国には arrive in を使います。' },
  ],
  'u08-l4': [
    { en: 'I always listen to music while I run.', ja: '走っている間はいつも音楽を聴きます。', highlight: 'listen to music' },
  ],
  'u09-l1': [
    { en: 'Can I leave my bag here for a moment?', ja: '少しの間、ここにかばんを置いていいですか。', highlight: 'Can I leave' },
    { en: 'My father could read music when he was six.', ja: '父は6歳のときに楽譜が読めました。', highlight: 'could read' },
  ],
  'u09-l2': [
    { en: "You mustn't use your phone during the exam.", ja: '試験中は携帯電話を使ってはいけません。', highlight: "mustn't use" },
    { en: "She doesn't have to work on Saturdays.", ja: '彼女は土曜日に働かなくてもよいのです。', highlight: "doesn't have to work" },
  ],
  'u09-l3': [
    { en: 'You should ask your doctor about that medicine.', ja: 'その薬については医師に相談したほうがいいですよ。', highlight: 'should ask' },
    { en: "We'd better book the tickets before they sell out.", ja: '売り切れる前にチケットを予約したほうがいいです。', highlight: "'d better book" },
  ],
  'u09-l4': [
    { en: 'Maybe the shop is closed on Mondays.', ja: 'もしかすると、その店は月曜が休みかもしれません。', highlight: 'Maybe', note: 'maybe は副詞なので文頭に置きます。' },
    { en: 'The traffic will be heavy after the concert.', ja: 'コンサートのあとは道路が混むでしょう。', highlight: 'will be' },
  ],
  'u10-l1': [
    { en: 'They need to leave before eight tomorrow.', ja: '彼らは明日8時前に出発する必要があります。', highlight: 'need to leave' },
    { en: 'She stopped by the store to buy some bread.', ja: '彼女はパンを買うために店に寄りました。', highlight: 'to buy' },
  ],
  'u10-l2': [
    { en: 'He gave up smoking three years ago.', ja: '彼は3年前に喫煙をやめました。', highlight: 'gave up smoking' },
    { en: 'Learning a new language takes patience.', ja: '新しい言語を学ぶには忍耐が必要です。', highlight: 'Learning a new language', note: '動名詞のかたまりが主語なので単数扱いです。' },
  ],
  'u10-l3': [
    { en: 'We stopped to look at the map.', ja: '私たちは地図を見るために立ち止まりました。', highlight: 'stopped to look', note: 'stop to do は「するために立ち止まる」です。' },
    { en: 'My brother loves collecting old stamps.', ja: '兄は古い切手を集めるのが大好きです。', highlight: 'loves collecting' },
  ],
  'u10-l4': [
    { en: 'She apologized for arriving so late.', ja: '彼女はとても遅れて到着したことを謝りました。', highlight: 'for arriving' },
    { en: 'I am used to working with a small team.', ja: '私は少人数のチームで働くことに慣れています。', highlight: 'to working', note: 'be used to の to は前置詞なので -ing が続きます。' },
  ],
  'u11-l1': [
    { en: 'They have moved to a bigger apartment.', ja: '彼らはもっと広いアパートへ引っ越しました。', highlight: 'have moved' },
    { en: 'Has the delivery arrived at the office?', ja: '配達物はオフィスに届きましたか。', highlight: 'Has the delivery arrived' },
  ],
  'u11-l2': [
    { en: 'She has never eaten Indian food before.', ja: '彼女はインド料理を食べたことが一度もありません。', highlight: 'has never eaten' },
  ],
  'u11-l3': [
    { en: 'My uncle has taught at that school for twenty years.', ja: 'おじはその学校で20年間教えています。', highlight: 'for twenty years' },
    { en: 'They have been friends since their first year of college.', ja: '彼らは大学1年のときから友人です。', highlight: 'since their first year' },
  ],
  'u11-l4': [
    { en: 'We have already booked a table for six.', ja: '私たちはすでに6人分の席を予約しました。', highlight: 'have already booked' },
    { en: 'The manager has just approved my request.', ja: '部長はちょうど私の申請を承認しました。', highlight: 'has just approved' },
  ],
  'u11-l5': [
    { en: 'I finished the report an hour ago.', ja: '私は1時間前に報告書を仕上げました。', highlight: 'finished', note: 'ago は特定の過去の時点を表すので過去形です。' },
    { en: 'She has finished the report, so we can send it now.', ja: '彼女は報告書を仕上げたので、今すぐ送れます。', highlight: 'has finished' },
  ],
  'u11-l6': [
    { en: 'Have you ever worked with this software before?', ja: 'このソフトを使って仕事をしたことがありますか。', highlight: 'Have you ever worked' },
    { en: 'The store has been closed since the typhoon.', ja: 'その店は台風以来ずっと閉まっています。', highlight: 'has been closed since' },
  ],
  'u12-l1': [
    { en: 'They are moving into the new office next month.', ja: '彼らは来月、新しいオフィスへ移ります。', highlight: 'are moving' },
    { en: 'I am taking my parents to the airport tonight.', ja: '今夜、両親を空港まで送ります。', highlight: 'am taking' },
  ],
  'u12-l2': [
    { en: 'The phone is ringing. I will get it.', ja: '電話が鳴っています。私が出ます。', highlight: 'will get', note: 'その場で決めたことなので will です。' },
    { en: 'We are having dinner with the client on Thursday.', ja: '木曜日にクライアントと会食する予定です。', highlight: 'are having' },
  ],
  'u12-l3': [
    { en: 'Call me when you get to the hotel.', ja: 'ホテルに着いたら電話してください。', highlight: 'when you get' },
    { en: 'We will start as soon as everyone is ready.', ja: '全員の準備ができたらすぐに始めます。', highlight: 'as soon as everyone is' },
  ],
  'u13-l1': [
    { en: 'These vegetables are grown on a local farm.', ja: 'これらの野菜は地元の農場で育てられています。', highlight: 'are grown' },
    { en: 'The windows were washed last Thursday.', ja: '窓は先週の木曜日に洗われました。', highlight: 'were washed' },
  ],
  'u13-l2': [
    { en: 'Our flight was delayed for three hours.', ja: '私たちの便は3時間遅れました。', highlight: 'was delayed', note: '誰が遅らせたかは重要でないので by句を付けません。' },
    { en: 'This novel was translated by a famous poet.', ja: 'この小説は有名な詩人によって翻訳されました。', highlight: 'by a famous poet' },
  ],
  'u13-l3': [
    { en: 'The road can be closed during heavy snow.', ja: '大雪の間、その道路は閉鎖されることがあります。', highlight: 'can be closed' },
  ],
  'u13-l4': [
    { en: 'The bridge was inspected by city engineers last week.', ja: 'その橋は先週、市の技術者によって点検されました。', highlight: 'was inspected' },
    { en: 'Our proposal has been accepted by the committee.', ja: '私たちの提案は委員会に受理されました。', highlight: 'has been accepted' },
    { en: 'The city built a new library near the river.', ja: '市は川の近くに新しい図書館を建てました。', highlight: 'The city built', note: '話題の中心が「する側」なので能動態が自然です。' },
  ],
  'u14-l1': [
    { en: 'The company that makes these bicycles is based in Osaka.', ja: 'これらの自転車を作っている会社は大阪にあります。', highlight: 'that makes' },
    { en: 'We hired an editor who has worked on medical journals.', ja: '私たちは医学雑誌を手がけたことのある編集者を雇いました。', highlight: 'who has worked' },
  ],
  'u14-l2': [
    { en: 'The songs my father loved are still popular today.', ja: '父が好きだった歌は今でも人気があります。', highlight: 'my father loved', note: '目的格の関係代名詞が省略されています。' },
    { en: 'This is the recipe that my grandmother taught me.', ja: 'これは祖母が教えてくれたレシピです。', highlight: 'that my grandmother taught' },
  ],
  'u14-l3': [
    { en: 'I work with a designer whose office is in Kobe.', ja: '私はオフィスが神戸にあるデザイナーと働いています。', highlight: 'whose office' },
  ],
  'u14-l4': [
    { en: 'Our new manager, who joined in April, speaks three languages.', ja: '4月に入社した新しい部長は3か国語を話します。', highlight: 'who joined in April' },
    { en: 'The report that we submitted yesterday needs one correction.', ja: '昨日提出した報告書には1か所の訂正が必要です。', highlight: 'that we submitted yesterday' },
  ],
  'u14-l5': [
    { en: 'The engineer whose team built this system now works abroad.', ja: 'このシステムを作ったチームの技術者は、今は海外で働いています。', highlight: 'whose team built' },
    { en: 'Tuesday is the day when our department holds its weekly meeting.', ja: '火曜日は私たちの部署が週次会議を開く日です。', highlight: 'when our department holds' },
  ],
  'u15-l1': [
    { en: 'If you press this button, the machine stops immediately.', ja: 'このボタンを押すと、機械はすぐに止まります。', highlight: 'If you press' },
    { en: 'If the meeting finishes early, we can catch the express.', ja: '会議が早く終われば、特急に乗れます。', highlight: 'If the meeting finishes' },
  ],
  'u15-l2': [
    { en: 'If she had a car, she would drive to the coast every weekend.', ja: '車があれば、彼女は毎週末海岸までドライブするでしょう。', highlight: 'would drive' },
    { en: 'I would take the job if the office were closer to my home.', ja: 'オフィスが自宅にもっと近ければ、その仕事を引き受けるのですが。', highlight: 'were closer' },
  ],
  'u15-l3': [
    { en: 'Take a jacket in case the temperature drops tonight.', ja: '今夜気温が下がる場合に備えて、上着を持って行きなさい。', highlight: 'in case' },
    { en: 'Unless the weather changes, the ferry will leave on time.', ja: '天候が変わらない限り、フェリーは定刻に出発します。', highlight: 'Unless the weather changes' },
  ],
  'u15-l4': [
    { en: 'If the client agrees, we will sign the contract on Monday.', ja: 'クライアントが同意すれば、月曜日に契約を結びます。', highlight: 'will sign' },
    { en: 'If I spoke fluent Spanish, I would apply for that position.', ja: 'スペイン語が流暢に話せたら、その職に応募するのですが。', highlight: 'would apply' },
  ],
  'u16-l1': [
    { en: 'Although we started late, we finished the project on time.', ja: '開始は遅れましたが、私たちはプロジェクトを予定どおり終えました。', highlight: 'Although' },
    { en: 'The elevator was broken, so we walked up five floors.', ja: 'エレベーターが故障していたので、私たちは5階分歩いて上がりました。', highlight: 'so' },
  ],
  'u16-l2': [
    { en: 'I did not notice the mistake until the report was printed.', ja: '報告書が印刷されるまで、私はその誤りに気づきませんでした。', highlight: 'until the report was printed' },
    { en: 'While the guests were arriving, the chef finished the dessert.', ja: '客が到着している間に、シェフはデザートを仕上げました。', highlight: 'While the guests were arriving' },
  ],
  'u16-l3': [
    { en: 'Neither of the applicants has sent a portfolio yet.', ja: '応募者のどちらも、まだ作品集を送ってきていません。', highlight: 'Neither of the applicants has' },
    { en: 'Both the design and the price impressed our customers.', ja: 'デザインも価格も、私たちの顧客を感心させました。', highlight: 'Both the design and the price' },
  ],
  'u17-l1': [
    { en: 'We have been living in this neighborhood since our son was born.', ja: '息子が生まれてから、私たちはこの地域に住んでいます。', highlight: 'have been living' },
    { en: 'The engineers have been testing the new system all week.', ja: '技術者たちは今週ずっと新しいシステムを検証しています。', highlight: 'have been testing' },
  ],
  'u17-l2': [
    { en: 'He has read three books since the holiday started.', ja: '休暇が始まってから、彼は3冊の本を読み終えました。', highlight: 'has read three books', note: '冊数という結果を報告しているので現在完了です。' },
    { en: 'He has been reading in the garden since breakfast.', ja: '彼は朝食のあとからずっと庭で読書をしています。', highlight: 'has been reading' },
  ],
  'u18-l1': [
    { en: 'By the time we found the venue, the concert had begun.', ja: '会場を見つけたときには、コンサートはもう始まっていました。', highlight: 'had begun' },
    { en: 'She had never used a rice cooker before she moved to Japan.', ja: '日本へ来る前、彼女は炊飯器を使ったことがありませんでした。', highlight: 'had never used' },
  ],
  'u18-l2': [
    { en: 'We took a taxi because we had missed the last bus.', ja: '最終バスに乗り遅れていたので、私たちはタクシーに乗りました。', highlight: 'had missed' },
    { en: 'He finished the presentation and answered every question calmly.', ja: '彼は発表を終え、すべての質問に落ち着いて答えました。', highlight: 'finished', note: '起きた順に語るので、過去形を並べるだけで足ります。' },
  ],
  'u18-l3': [
    { en: 'While we were putting the candles away, my sister was making hot tea.', ja: 'ろうそくを片付けている間、姉は熱いお茶を入れていました。', highlight: 'were putting' },
    { en: 'The power came back an hour later, and the house felt warm again.', ja: '1時間後に電気が復旧し、家は再び暖かく感じられました。', highlight: 'came back' },
  ],
  'u19-l1': [
    { en: 'She said that she had already sent the invoice the day before.', ja: '彼女は前日にすでに請求書を送ったと言いました。', highlight: 'had already sent' },
    { en: 'They told us that the shop would reopen the next day.', ja: '彼らは、その店は翌日に再開すると私たちに言いました。', highlight: 'would reopen' },
  ],
  'u19-l2': [
    { en: 'The receptionist asked if we had made a reservation.', ja: '受付係は、私たちが予約をしているかどうか尋ねました。', highlight: 'asked if' },
  ],
  'u19-l3': [
    { en: 'My colleague recommended booking the hotel well in advance.', ja: '同僚は、ホテルをかなり前もって予約することを勧めました。', highlight: 'recommended booking' },
  ],
  'u19-l4': [
    { en: 'Could you tell me when the next tour begins?', ja: '次のツアーがいつ始まるか教えていただけますか。', highlight: 'when the next tour begins' },
    { en: 'I am not sure whether the office is open on Saturdays.', ja: 'オフィスが土曜日に開いているかどうか、私には分かりません。', highlight: 'whether the office is' },
  ],
  'u20-l1': [
    { en: 'His car is in the driveway, so he must be at home.', ja: '車が私道にあるので、彼は家にいるに違いありません。', highlight: 'must be' },
    { en: 'She has three meetings today, so she could be very busy.', ja: '彼女は今日3つ会議があるので、とても忙しいのかもしれません。', highlight: 'could be' },
  ],
  'u20-l2': [
    { en: 'The window was broken, so someone must have thrown a stone.', ja: '窓が割れていたので、誰かが石を投げたに違いありません。', highlight: 'must have thrown' },
    { en: 'He cannot have written this report alone in one evening.', ja: '彼が一晩でこの報告書を1人で書いたはずはありません。', highlight: 'cannot have written' },
  ],
  'u20-l3': [
    { en: 'We should have reserved a table before the holiday weekend.', ja: '連休の前に席を予約しておくべきでした。', highlight: 'should have reserved' },
    { en: 'They could have finished sooner with one more helper.', ja: 'もう1人手伝いがいれば、彼らはもっと早く終えられたでしょう。', highlight: 'could have finished' },
  ],
  'u20-l4': [
    { en: 'We used to walk to school together every morning.', ja: '私たちは毎朝一緒に歩いて学校へ通ったものです。', highlight: 'used to walk' },
    { en: 'On rainy afternoons, my father would read to us for hours.', ja: '雨の午後には、父は何時間も私たちに本を読んでくれたものです。', highlight: 'would read' },
  ],
  'u21-l1': [
    { en: 'She forgot to lock the back door last night.', ja: '彼女は昨夜、裏口の鍵をかけ忘れました。', highlight: 'forgot to lock' },
  ],
  'u21-l2': [
    { en: 'The teacher expects every student to submit the essay online.', ja: '先生は全生徒に、小論文をオンラインで提出することを求めています。', highlight: 'expects every student to submit' },
    { en: 'I asked my neighbor not to park in front of my gate.', ja: '私は隣人に、門の前に駐車しないようお願いしました。', highlight: 'not to park' },
  ],
  'u21-l3': [
    { en: 'It is difficult for beginners to hear the difference between these sounds.', ja: '初心者がこれらの音の違いを聞き分けるのは難しいです。', highlight: 'for beginners to hear' },
    { en: 'We were glad to hear that your surgery went well.', ja: '手術がうまくいったと聞いて、私たちはうれしく思いました。', highlight: 'glad to hear' },
  ],
  'u22-l1': [
    { en: 'If they had checked the schedule, they would have noticed the change.', ja: '予定表を確認していれば、彼らは変更に気づいていたでしょう。', highlight: 'would have noticed' },
    { en: 'I would have joined you if I had finished my work earlier.', ja: '仕事をもっと早く終えていたら、私も参加したのですが。', highlight: 'had finished' },
  ],
  'u22-l2': [
    { en: 'I wish I had asked more questions during the interview.', ja: '面接中にもっと質問しておけばよかったと思います。', highlight: 'had asked' },
  ],
  'u22-l3': [
    { en: 'If the delivery arrives before noon, we will start the setup.', ja: '配達が正午前に届けば、私たちは設営を始めます。', highlight: 'will start' },
    { en: 'If I lived in that city, I would go to concerts every month.', ja: 'その街に住んでいたら、私は毎月コンサートへ行くでしょう。', highlight: 'would go' },
    { en: 'If we had hired one more designer, the launch would have gone smoothly.', ja: 'デザイナーをもう1人雇っていたら、公開は順調に進んだでしょう。', highlight: 'would have gone' },
  ],
  'u23-l1': [
    { en: 'If we had bought the apartment last year, we would not be paying rent now.', ja: '昨年そのマンションを買っていたら、今は家賃を払っていないでしょう。', highlight: 'would not be paying' },
    { en: 'If he had studied engineering, he would be working at a design firm today.', ja: '工学を学んでいたら、彼は今日、設計事務所で働いているでしょう。', highlight: 'would be working' },
  ],
  'u23-l2': [
    { en: 'Supposing the supplier raised the price next month, how would we explain that to our customers?', ja: '仮に来月、仕入先が値上げしたら、それを顧客にどう説明しますか。', highlight: 'Supposing the supplier raised' },
  ],
  'u23-l3': [
    { en: 'I would rather finish the report tonight than start the week with unfinished work.', ja: '週の初めに未処理の仕事を残すより、今夜のうちに報告書を仕上げたいです。', highlight: 'would rather finish' },
  ],
  'u24-l1': [
    { en: 'We should have the air conditioner serviced before the summer heat arrives in earnest.', ja: '本格的な夏の暑さが来る前に、エアコンを点検してもらうべきです。', highlight: 'have the air conditioner serviced' },
    { en: 'She got her documents translated by a certified agency before submitting the application.', ja: '彼女は申請書を提出する前に、認定機関で書類を翻訳してもらいました。', highlight: 'got her documents translated' },
  ],
  'u24-l2': [
    { en: 'The new policy lets employees choose their own working hours within a fixed range.', ja: '新しい方針では、決められた範囲内で従業員が自分の勤務時間を選べます。', highlight: 'lets employees choose' },
    { en: 'It took three phone calls to get the landlord to fix the broken heater.', ja: '大家に壊れた暖房を修理してもらうには、3回の電話が必要でした。', highlight: 'to get the landlord to fix' },
  ],
  'u24-l3': [
    { en: 'I saw the technician replace the entire panel and test every switch afterwards.', ja: '技術者がパネル全体を交換し、その後すべてのスイッチを点検するのを見ました。', highlight: 'saw the technician replace' },
    { en: 'From my desk I could hear the rain hitting the windows all afternoon.', ja: '自分の机から、午後の間ずっと雨が窓に当たる音が聞こえていました。', highlight: 'hear the rain hitting' },
  ],
  'u25-l1': [
    { en: 'The opening ceremony was surprisingly moving, and several guests were moved to tears.', ja: '開会式は思いがけず感動的で、何人かの招待客は涙を流していました。', highlight: 'moving' },
    { en: 'Reading the same instructions three times was frustrating for everyone in the workshop.', ja: '同じ手順書を3回読むのは、研修の参加者全員にとって苛立たしいことでした。', highlight: 'frustrating' },
  ],
  'u25-l2': [
    { en: 'The documents attached to this email explain the new procedure in detail.', ja: 'このメールに添付した書類が、新しい手順を詳しく説明しています。', highlight: 'attached to this email' },
    { en: 'The team leading the investigation will publish its findings early next spring.', ja: '調査を主導しているチームは、来春早くに調査結果を公表します。', highlight: 'leading the investigation' },
  ],
  'u25-l3': [
    { en: 'Having checked every entrance twice, the guard finally locked the main gate for the night.', ja: 'すべての入口を2度確認したあと、警備員はようやく夜のために正門を施錠しました。', highlight: 'Having checked' },
    { en: 'Written in plain language, the new manual is far easier for beginners to follow.', ja: '平易な言葉で書かれているため、新しいマニュアルは初心者にとってずっと分かりやすいです。', highlight: 'Written in plain language' },
  ],
  'u26-l1': [
    { en: 'It is reported that the new railway line will open ahead of the original schedule.', ja: '新しい鉄道路線は当初の予定より早く開業すると報じられています。', highlight: 'It is reported that' },
    { en: 'The author is known to have written most of the novel while living abroad.', ja: 'その作家は、小説の大半を海外に住みながら書いたことで知られています。', highlight: 'is known to have written' },
  ],
  'u26-l2': [
    { en: 'All the equipment has to be checked carefully before the first performance on Friday.', ja: '金曜日の初演の前に、すべての機材を入念に点検しなければなりません。', highlight: 'to be checked' },
    { en: 'Nobody enjoys being interrupted while explaining something complicated to a large audience.', ja: '大勢の前で複雑なことを説明している最中に割り込まれるのは、誰も好みません。', highlight: 'being interrupted' },
  ],
  'u26-l3': [
    { en: 'My bicycle got stolen from the station car park sometime last Wednesday afternoon.', ja: '私の自転車は先週水曜の午後のいつかに、駅の駐輪場から盗まれました。', highlight: 'got stolen' },
  ],
  'u27-l1': [
    { en: 'The conference at which she presented her research attracted specialists from twelve countries.', ja: '彼女が研究を発表した学会には、12か国から専門家が集まりました。', highlight: 'at which she presented' },
    { en: 'These are the colleagues with whom I shared an office for almost five years.', ja: 'この人たちは、私が5年近くオフィスを共有した同僚です。', highlight: 'with whom I shared' },
  ],
  'u27-l2': [
    { en: 'Whatever the committee decides tonight, we will need to inform the staff by Monday.', ja: '委員会が今夜何を決めても、月曜までに職員へ知らせる必要があります。', highlight: 'Whatever the committee decides' },
    { en: 'What worries me most is the lack of a clear deadline for the second phase.', ja: '私が最も心配しているのは、第2段階の期限が明確でないことです。', highlight: 'What worries me most' },
  ],
  'u27-l3': [
    { en: 'The supplier raised its prices without warning, which forced us to revise the whole budget.', ja: '仕入先が予告なく値上げしたため、私たちは予算全体を見直さざるを得なくなりました。', highlight: 'which forced us' },
    { en: 'She speaks three languages fluently, which is why the company sent her to Singapore.', ja: '彼女は3か国語を流暢に話すので、会社は彼女をシンガポールへ派遣しました。', highlight: 'which is why' },
  ],
  'u28-l1': [
    { en: 'Despite the short notice, almost every member of the committee attended the emergency meeting.', ja: '急な連絡にもかかわらず、委員会のほぼ全員が緊急会議に出席しました。', highlight: 'Despite the short notice' },
    { en: 'The software is powerful and flexible. However, new users often find it confusing at first.', ja: 'そのソフトは高機能で柔軟です。しかし、新規の利用者は最初とまどうことが多いです。', highlight: 'However' },
  ],
  'u28-l2': [
    { en: 'The old boiler failed three times last winter. As a result, the school replaced it in March.', ja: '古いボイラーは昨冬3回故障しました。その結果、学校は3月にそれを交換しました。', highlight: 'As a result' },
  ],
  'u28-l3': [
    { en: 'At first the software felt slow, but it became much faster after the second update.', ja: '最初はソフトが遅く感じられましたが、2回目の更新後はずっと速くなりました。', highlight: 'At first', note: 'at first は「最初は〜だった(が後で変わった)」を表します。' },
  ],
  'u29-l1': [
    { en: 'Everyone agrees that the current filing system wastes far too much of our time.', ja: '今の書類管理の仕組みは私たちの時間を浪費しすぎている、と全員が同意しています。', highlight: 'that the current filing system' },
    { en: 'The possibility that the shipment will arrive late worries the whole production team.', ja: '出荷が遅れるかもしれないという可能性が、生産チーム全体を不安にさせています。', highlight: 'The possibility that' },
  ],
  'u29-l2': [
    { en: 'Nobody could explain how the two files ended up with exactly the same name.', ja: '2つのファイルがまったく同じ名前になった経緯を、誰も説明できませんでした。', highlight: 'how the two files ended up' },
    { en: "Whether we hire another translator or not depends entirely on next year's budget.", ja: 'もう1人翻訳者を雇うかどうかは、来年度の予算に完全に左右されます。', highlight: 'Whether we hire another translator or not' },
  ],
  'u29-l3': [
    { en: 'It is important that every visitor sign the register before entering the laboratory.', ja: '来訪者は全員、実験室に入る前に記録簿へ署名することが重要です。', highlight: 'sign', note: 'important that の節では動詞は原形になります。' },
    { en: 'It turned out that the missing file had been saved in the wrong folder.', ja: '見つからなかったファイルは、間違ったフォルダに保存されていたことが分かりました。', highlight: 'It turned out that' },
  ],
  'u30-l1': [
    { en: 'What the customers appreciated most was the speed of our reply to their complaint.', ja: '顧客が最も評価したのは、苦情への返信の速さでした。', highlight: 'What the customers appreciated most' },
  ],
  'u30-l2': [
    { en: 'Not only did the printer jam repeatedly, but it also smudged every color page.', ja: 'プリンターは何度も紙詰まりしただけでなく、カラーページをすべて汚しました。', highlight: 'Not only did the printer jam' },
    { en: 'Seldom have I read a report as carefully organized as the one you submitted.', ja: 'あなたが提出したものほど丁寧に構成された報告書を、私はめったに読んだことがありません。', highlight: 'Seldom have I read' },
  ],
  'u30-l3': [
    { en: 'Will the supplier accept our revised terms? I am afraid not, judging by their reply.', ja: '仕入先は修正した条件を受け入れるでしょうか。返信を見る限り、残念ながら受け入れないでしょう。', highlight: 'I am afraid not' },
  ],
  'u31-l1': [
    { en: 'The shop closed two years ago, and nothing has opened in its place since.', ja: 'その店は2年前に閉店し、それ以来その場所には何も開いていません。', highlight: 'closed two years ago' },
    { en: 'She had already left the building when the security guard came to lock up.', ja: '警備員が施錠に来たとき、彼女はすでに建物を出ていました。', highlight: 'had already left' },
  ],
  'u31-l2': [
    { en: 'The exhibition runs until the end of August, but tickets must be bought by Friday.', ja: '展覧会は8月末まで開催されますが、チケットは金曜までに購入する必要があります。', highlight: 'until the end of August' },
  ],
  'u31-l3': [
    { en: 'It was such a long meeting that half of us forgot the original question.', ja: 'とても長い会議だったので、私たちの半分は最初の議題を忘れてしまいました。', highlight: 'such a long meeting that' },
  ],
  'u32-l1': [
    { en: 'By this time next month we will have moved all the files to the new server.', ja: '来月の今ごろまでには、すべてのファイルを新しいサーバーへ移し終えているでしょう。', highlight: 'will have moved' },
  ],
  'u32-l2': [
    { en: 'He was going to apply for the transfer, but the position was filled internally.', ja: '彼は異動に応募するつもりでしたが、その職は社内で埋まってしまいました。', highlight: 'was going to apply' },
  ],
  'u32-l3': [
    { en: 'Had the supplier warned us earlier, we could have found another source of parts.', ja: '仕入先がもっと早く知らせてくれていれば、別の部品の調達先を見つけられたでしょう。', highlight: 'Had the supplier warned' },
  ],
  'u32-l4': [
    { en: 'The more people join the tour, the lower the price per person becomes.', ja: 'ツアーに参加する人が多いほど、1人あたりの料金は安くなります。', highlight: 'The more people join' },
  ],
  'u33-l1': [
    { en: 'Her son goes to school by bus, but she drives to the school for meetings.', ja: '息子はバスで通学していますが、彼女は面談のときは車で学校へ行きます。', highlight: 'to school', note: '機能を指す go to school は無冠詞、建物を指すときは the school です。' },
  ],
  'u33-l2': [
    { en: 'Little progress has been made since the last inspection, according to the latest report.', ja: '最新の報告によれば、前回の点検以降ほとんど進展がありません。', highlight: 'Little progress' },
  ],
  'u33-l3': [
    { en: 'The heater is still on, so please remember to turn it off before you leave.', ja: '暖房がまだ入っているので、出る前に忘れずに消してください。', highlight: 'turn it off' },
  ],
}
