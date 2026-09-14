import type { PatternFocusMap, PatternMap } from './types.ts'

// B1+(U17–U22)の文型データ。例文の英文をそのままキーにする。
//
// 補足の判定方針(types.ts の規約に加えて):
// - 複数の節が並ぶ文は、主節(従属節を除いた中心の節)だけで判定する。
//   等位接続(and / but / so)で主節が2つ並ぶ場合は、先に立つ節を中心とみなす。
// - 例文が2文でできている場合は、先に立つ文を中心とみなす。

export const b1PlusPatterns: PatternMap = {
  // u17-l1 現在完了進行形の基本
  'I have been waiting for the bus for twenty minutes.': {
    pattern: 'SV',
    note: '目的語なし。forの句は副詞句で数えない。',
  },
  'She has been studying English since April.': {
    pattern: 'SVO',
    note: 'studyingのあとに目的語English。SVO。',
  },
  'It has been raining all day.': {
    pattern: 'SV',
    note: '天候のItを主語にしたSV。all day は副詞句。',
  },
  'How long have you been working here?': {
    pattern: 'SV',
    note: '平叙文に戻すと You have been working here のSV。',
  },
  "They haven't been sleeping well lately.": {
    pattern: 'SV',
    note: 'well は副詞。目的語がなくSV。',
  },
  'I have been learning sign language since January.': {
    pattern: 'SVO',
    note: 'learningのあとに目的語。SVO。',
  },
  'How long has the dog been barking?': {
    pattern: 'SV',
    note: '平叙文に戻すと The dog has been barking のSV。',
  },
  'Your clothes are wet. Have you been walking in the rain?': {
    pattern: 'SVC',
    note: '前半が be + 形容詞のSVC。',
  },
  'We have been living in this neighborhood since our son was born.': {
    pattern: 'SV',
    note: 'live は自動詞。inの句は副詞句でSV。',
  },
  'The engineers have been testing the new system all week.': {
    pattern: 'SVO',
    note: 'testingの目的語が the new system。SVO。',
  },

  // u17-l2 現在完了 vs 現在完了進行形
  'I have painted the kitchen.': {
    pattern: 'SVO',
    note: 'paintedの目的語が the kitchen。SVO。',
  },
  'She has fixed her bike.': {
    pattern: 'SVO',
    note: 'her bike が目的語のSVO。',
  },
  'I have been painting the kitchen all afternoon.': {
    pattern: 'SVO',
    note: '進行形でも目的語を取ればSVO。',
  },
  'She has been fixing her bike since noon.': {
    pattern: 'SVO',
    note: 'fixingの目的語が her bike。SVO。',
  },
  "I've written five emails this morning.": {
    pattern: 'SVO',
    note: 'five emails が目的語のSVO。',
  },
  "I've been writing emails all morning.": {
    pattern: 'SVO',
    note: 'emails が目的語のSVO。',
  },
  'Your eyes are red. Have you been crying?': {
    pattern: 'SVC',
    note: '前半が be + 形容詞のSVC。',
  },
  'Someone has eaten my cake!': {
    pattern: 'SVO',
    note: 'my cake が目的語のSVO。',
  },
  'We have lived in Nagoya for ten years.': {
    pattern: 'SV',
    note: 'live は自動詞。in Nagoya は副詞句でSV。',
  },
  'Nora has answered twenty emails this morning.': {
    pattern: 'SVO',
    note: 'twenty emails が目的語のSVO。',
  },
  'Nora has been answering emails all morning.': {
    pattern: 'SVO',
    note: 'answeringの目的語が emails。SVO。',
  },
  'We have known each other for more than a decade.': {
    pattern: 'SVO',
    note: 'each other が目的語のSVO。',
  },
  'He has read three books since the holiday started.': {
    pattern: 'SVO',
    note: 'three books が目的語のSVO。',
  },
  'He has been reading in the garden since breakfast.': {
    pattern: 'SV',
    note: '目的語がなく in the garden は副詞句。SV。',
  },

  // u18-l1 過去完了の基本
  'When I arrived at the station, the train had already left.': {
    pattern: 'SV',
    note: '主節 the train had already left は自動詞でSV。',
  },
  'She had worked at a bank before she became a teacher.': {
    pattern: 'SV',
    note: '主節 she had worked は自動詞でSV。',
  },
  "I couldn't open the door because I had left my key at the office.": {
    pattern: 'SVO',
    note: '主節 I couldn\'t open the door がSVO。',
  },
  'By the time the guests arrived, we had finished all the preparations.': {
    pattern: 'SVO',
    note: '主節 we had finished は目的語を取るSVO。',
  },
  "He hadn't eaten sushi until he visited Japan.": {
    pattern: 'SVO',
    note: '主節 He hadn\'t eaten sushi がSVO。',
  },
  'The guests had already left when we reached the restaurant.': {
    pattern: 'SV',
    note: '主節 The guests had already left は自動詞でSV。',
  },
  'I had never driven in snow before that trip.': {
    pattern: 'SV',
    note: 'drive は自動詞。in snow は副詞句でSV。',
  },
  'Had the meeting started by the time you arrived?': {
    pattern: 'SV',
    note: '疑問文を戻すと The meeting had started のSV。',
  },
  'By the time we found the venue, the concert had begun.': {
    pattern: 'SV',
    note: '主節 the concert had begun は自動詞でSV。',
  },
  'She had never used a rice cooker before she moved to Japan.': {
    pattern: 'SVO',
    note: '主節は使用の目的語 a rice cooker を取るSVO。',
  },

  // u18-l2 過去完了 vs 過去形
  'She checked the report and sent it to her boss.': {
    pattern: 'SVO',
    note: '先に立つ She checked the report がSVO。',
  },
  'When the phone rang, I answered it right away.': {
    pattern: 'SVO',
    note: '主節 I answered it がSVO。',
  },
  'When I turned on the TV, the show had ended.': {
    pattern: 'SV',
    note: '主節 the show had ended は自動詞でSV。',
  },
  'He realized that he had sent the email to the wrong person.': {
    pattern: 'SVO',
    note: 'that節が目的語。SVO。',
  },
  'When we arrived, the concert started.': {
    pattern: 'SV',
    note: '主節 the concert started は自動詞でSV。',
  },
  'When we arrived, the concert had started.': {
    pattern: 'SV',
    note: '主節 the concert had started は自動詞でSV。',
  },
  'After the guests had left, we cleaned the kitchen.': {
    pattern: 'SVO',
    note: '主節 we cleaned the kitchen がSVO。',
  },
  'I lost the watch that my grandfather had given me.': {
    pattern: 'SVO',
    note: '関係詞節は数えず、I lost the watch のSVO。',
  },
  'Last night I watched a movie and went to bed early.': {
    pattern: 'SVO',
    note: '先に立つ I watched a movie がSVO。',
  },
  'After we checked the map, we continued our journey.': {
    pattern: 'SVO',
    note: '主節 we continued our journey がSVO。',
  },
  'When I opened the file, I saw that someone had changed it.': {
    pattern: 'SVO',
    note: '主節 I saw that ... は that節を目的語に取るSVO。',
  },
  'She apologized because she had misunderstood my message.': {
    pattern: 'SV',
    note: '主節 She apologized は自動詞でSV。',
  },
  'We took a taxi because we had missed the last bus.': {
    pattern: 'SVO',
    note: '主節 We took a taxi がSVO。',
  },
  'He finished the presentation and answered every question calmly.': {
    pattern: 'SVO',
    note: '先に立つ He finished the presentation がSVO。',
  },

  // u18-l3 物語の時制
  'It was raining hard when I left home this morning.': {
    pattern: 'SV',
    note: 'was raining は目的語を取らない進行形でSV。',
  },
  'I ran to the station and jumped on a train.': {
    pattern: 'SV',
    note: 'run も jump on も自動詞。SV。',
  },
  'A few minutes later, I realized that I had taken the wrong train.': {
    pattern: 'SVO',
    note: 'that節が目的語に入るSVO。',
  },
  'While I was looking at the route map, an old man kindly spoke to me.': {
    pattern: 'SV',
    note: '主節 an old man spoke to me は自動詞でSV。',
  },
  'In the end, I got to work only ten minutes late.': {
    pattern: 'SV',
    note: 'get to は自動詞相当。toの句は副詞句でSV。',
  },
  'The wind was blowing hard when our lights went out.': {
    pattern: 'SV',
    note: '主節 The wind was blowing hard は自動詞でSV。',
  },
  'I reached for my phone, but I had left it upstairs.': {
    pattern: 'SV',
    note: '先に立つ I reached for my phone は自動詞でSV。',
  },
  'We found some candles and waited for the power to return.': {
    pattern: 'SVO',
    note: '先に立つ We found some candles がSVO。',
  },
  'While we were putting the candles away, my sister was making hot tea.': {
    pattern: 'SVO',
    note: '主節 my sister was making hot tea がSVO。',
  },
  'The power came back an hour later, and the house felt warm again.': {
    pattern: 'SV',
    note: '先に立つ The power came back は自動詞でSV。',
  },

  // u19-l1 人が言ったことを伝える
  'Emi said she was tired.': {
    pattern: 'SVO',
    note: 'that節が目的語に入るSVO。',
  },
  'Ken said he had lost his umbrella.': {
    pattern: 'SVO',
    note: 'that節を目的語に取るSVO。',
  },
  'She said she would call me the next day.': {
    pattern: 'SVO',
    note: 'that節が目的語のSVO。',
  },
  "He told me he couldn't come to the party.": {
    pattern: 'SVOO',
    note: 'tell + 人 + that節のSVOO。',
  },
  'My coworker said she had to leave early that day.': {
    pattern: 'SVO',
    note: 'that節を目的語に取るSVO。',
  },
  'Mika said that she was working from home that day.': {
    pattern: 'SVO',
    note: 'that節が目的語のSVO。',
  },
  'Leo told me that he had lost his ticket.': {
    pattern: 'SVOO',
    note: 'tell + 人 + that節のSVOO。',
  },
  'The guide said that the museum opens at nine.': {
    pattern: 'SVO',
    note: 'that節を目的語に取るSVO。',
  },
  'She said that she had already sent the invoice the day before.': {
    pattern: 'SVO',
    note: 'that節が目的語のSVO。',
  },
  'They told us that the shop would reopen the next day.': {
    pattern: 'SVOO',
    note: 'tell + 人 + that節のSVOO。',
  },

  // u19-l2 質問・お願いを人に伝える
  'She asked me if I was busy that day.': {
    pattern: 'SVOO',
    note: 'ask + 人 + if節のSVOO。',
  },
  'He asked me where I had bought my jacket.': {
    pattern: 'SVOO',
    note: 'ask + 人 + wh節のSVOO。',
  },
  'The staff asked us what time we would arrive.': {
    pattern: 'SVOO',
    note: 'ask + 人 + wh節のSVOO。',
  },
  'My doctor told me to get more sleep.': {
    pattern: 'SVOC',
    note: 'tell + 人 + to不定詞のSVOC。',
  },
  'I asked the driver to slow down.': {
    pattern: 'SVOC',
    note: 'ask + 人 + to不定詞のSVOC。',
  },
  'She told the kids not to run in the hallway.': {
    pattern: 'SVOC',
    note: 'tell + 人 + not to do のSVOC。',
  },
  'She asked me whether I needed a receipt.': {
    pattern: 'SVOO',
    note: 'ask + 人 + whether節のSVOO。',
  },
  'The officer asked where we were staying.': {
    pattern: 'SVO',
    note: '人を取らずwh節だけが目的語。SVO。',
  },
  'Dad told us not to leave the door unlocked.': {
    pattern: 'SVOC',
    note: 'tell + 人 + not to do のSVOC。',
  },
  'The receptionist asked if we had made a reservation.': {
    pattern: 'SVO',
    note: '人を取らずif節だけが目的語。SVO。',
  },

  // u19-l3 「約束した」「提案した」を使い分ける
  'She promised to email me the details.': {
    pattern: 'SVO',
    note: 'to不定詞が目的語のSVO。',
  },
  'He suggested meeting at the station at nine.': {
    pattern: 'SVO',
    note: '動名詞 meeting が目的語のSVO。',
  },
  'The doctor advised her to take a few days off.': {
    pattern: 'SVOC',
    note: 'advise + 人 + to不定詞のSVOC。',
  },
  'They warned us not to leave our bags unattended.': {
    pattern: 'SVOC',
    note: 'warn + 人 + not to do のSVOC。',
  },
  'He refused to answer the question.': {
    pattern: 'SVO',
    note: 'to不定詞が目的語のSVO。',
  },
  'She admitted that she had made a mistake.': {
    pattern: 'SVO',
    note: 'that節が目的語のSVO。',
  },
  'The airline offered to change our seats.': {
    pattern: 'SVO',
    note: 'to不定詞を目的語に取るSVO。',
  },
  'Mina suggested taking an earlier train.': {
    pattern: 'SVO',
    note: '動名詞 taking が目的語のSVO。',
  },
  'The doctor warned him not to drive.': {
    pattern: 'SVOC',
    note: 'warn + 人 + not to do のSVOC。',
  },
  'My colleague recommended booking the hotel well in advance.': {
    pattern: 'SVO',
    note: '動名詞 booking が目的語のSVO。',
  },

  // u19-l4 文の中に質問を入れる
  'Where does he live?': {
    pattern: 'SV',
    note: '平叙文に戻すと He lives のSV。',
  },
  'What time is it?': {
    pattern: 'SVC',
    note: 'be動詞の補語が what time。SVC。',
  },
  'Do you know where he lives?': {
    pattern: 'SVO',
    note: 'wh節全体が目的語に入るSVO。',
  },
  'Could you tell me what time it is?': {
    pattern: 'SVOO',
    note: 'tell + 人 + wh節のSVOO。',
  },
  'Do you know where the nearest ATM is?': {
    pattern: 'SVO',
    note: 'wh節が目的語に入るSVO。',
  },
  'Could you tell me how much this costs?': {
    pattern: 'SVOO',
    note: 'tell + 人 + wh節のSVOO。',
  },
  "I'm not sure if the museum is open today.": {
    pattern: 'SVC',
    note: 'be + 形容詞 sure のSVC。',
  },
  'I wonder why the train stopped.': {
    pattern: 'SVO',
    note: 'wh節が目的語に入るSVO。',
  },
  'Do you remember what time the meeting starts?': {
    pattern: 'SVO',
    note: 'wh節が目的語に入るSVO。',
  },
  'Could you tell me where platform six is?': {
    pattern: 'SVOO',
    note: 'tell + 人 + wh節のSVOO。',
  },
  'Do you know whether this bus stops at City Hall?': {
    pattern: 'SVO',
    note: 'whether節が目的語に入るSVO。',
  },
  'I wonder why the lights are still on.': {
    pattern: 'SVO',
    note: 'wh節を目的語に取るSVO。',
  },
  'Could you tell me when the next tour begins?': {
    pattern: 'SVOO',
    note: 'tell + 人 + wh節のSVOO。',
  },
  'I am not sure whether the office is open on Saturdays.': {
    pattern: 'SVC',
    note: 'be + 形容詞 sure のSVC。',
  },

  // u20-l1 現在の推量 must / can't / might
  'He must be tired after that long flight.': {
    pattern: 'SVC',
    note: 'be + 形容詞 tired のSVC。',
  },
  "He can't be tired. He slept for ten hours.": {
    pattern: 'SVC',
    note: '先に立つ He can\'t be tired が be + 形容詞のSVC。',
  },
  'You must wear a helmet on this site.': {
    pattern: 'SVO',
    note: 'wearの目的語が a helmet。SVO。',
  },
  "You mustn't park in front of the gate.": {
    pattern: 'SV',
    note: 'park は自動詞。前置詞句は数えずSV。',
  },
  "You've been working since this morning. You must be hungry.": {
    pattern: 'SV',
    note: '先に立つ You\'ve been working は自動詞でSV。',
  },
  'The lights are off. They might be out for dinner.': {
    pattern: 'SV',
    note: '先に立つ The lights are off は be + 副詞でSV。',
  },
  "That can't be Ken. He's in Osaka this week.": {
    pattern: 'SVC',
    note: '先に立つ That can\'t be Ken は be + 名詞のSVC。',
  },
  'She knows every street around here. She must live in this neighborhood.': {
    pattern: 'SVO',
    note: '先に立つ She knows every street がSVO。',
  },
  "He isn't answering his phone. He may be in a meeting.": {
    pattern: 'SVO',
    note: '先に立つ He isn\'t answering his phone がSVO。',
  },
  'The kitchen smells wonderful. Kai must be cooking.': {
    pattern: 'SVC',
    note: '先に立つ The kitchen smells wonderful はSVC。',
  },
  'This cannot be the right address because the number is different.': {
    pattern: 'SVC',
    note: '主節は be + 名詞のSVC。',
  },
  'Rina might not be available this afternoon.': {
    pattern: 'SVC',
    note: 'be + 形容詞 available のSVC。',
  },
  'His car is in the driveway, so he must be at home.': {
    pattern: 'SV',
    note: '先に立つ be + 場所の句がSV。',
  },
  'She has three meetings today, so she could be very busy.': {
    pattern: 'SVO',
    note: '先に立つ She has three meetings がSVO。',
  },

  // u20-l2 過去の推量 must have / can't have
  'The ground is wet. It must have rained last night.': {
    pattern: 'SVC',
    note: '先に立つ The ground is wet は be + 形容詞のSVC。',
  },
  "She can't have taken your umbrella. She wasn't here yesterday.": {
    pattern: 'SVO',
    note: '前半 can\'t have taken + 目的語でSVO。',
  },
  'I might have left my keys in the car.': {
    pattern: 'SVO',
    note: 'leftの目的語が my keys。SVO。',
  },
  "He didn't come to the party. He may have been busy.": {
    pattern: 'SV',
    note: '先に立つ He didn\'t come は自動詞でSV。',
  },
  "They're an hour late. They must have gotten lost.": {
    pattern: 'SVC',
    note: '先に立つ They\'re an hour late はSVC。',
  },
  'The door was unlocked. Someone must have entered the office.': {
    pattern: 'SV',
    note: '先に立つ was unlocked は受動態でSV。',
  },
  'Nora might have misunderstood the instructions.': {
    pattern: 'SVO',
    note: 'misunderstoodの目的語が the instructions。SVO。',
  },
  'They cannot have finished already because I can still hear them working.': {
    pattern: 'SV',
    note: '主節 They cannot have finished は自動詞でSV。',
  },
  'The window was broken, so someone must have thrown a stone.': {
    pattern: 'SV',
    note: '先に立つ受動態 was broken でSV。',
  },
  'He cannot have written this report alone in one evening.': {
    pattern: 'SVO',
    note: 'writtenの目的語が this report。SVO。',
  },

  // u20-l3 should have / could have
  'I should have studied harder for the test.': {
    pattern: 'SV',
    note: 'study は自動詞。目的語がなくSV。',
  },
  "You shouldn't have said that to her.": {
    pattern: 'SVO',
    note: 'saidの目的語が that。SVO。',
  },
  'We could have won the game, but we made too many mistakes.': {
    pattern: 'SVO',
    note: '先に立つ wonの目的語が the game。SVO。',
  },
  'You could have told me you were coming.': {
    pattern: 'SVOO',
    note: 'tell + 人 + 節のSVOO。',
  },
  "I couldn't have done this without your support.": {
    pattern: 'SVO',
    note: 'doneの目的語が this。SVO。',
  },
  'I should have checked the opening hours first.': {
    pattern: 'SVO',
    note: 'checkedの目的語が the opening hours。SVO。',
  },
  "We shouldn't have ignored that warning.": {
    pattern: 'SVO',
    note: 'ignoredの目的語が that warning。SVO。',
  },
  'A helmet could have prevented the injury.': {
    pattern: 'SVO',
    note: 'preventedの目的語が the injury。SVO。',
  },
  'We should have reserved a table before the holiday weekend.': {
    pattern: 'SVO',
    note: 'reservedの目的語が a table。SVO。',
  },
  'They could have finished sooner with one more helper.': {
    pattern: 'SV',
    note: 'finish は自動詞。目的語がなくSV。',
  },
  'I should have brought an umbrella.': {
    pattern: 'SVO',
    note: 'broughtの目的語が an umbrella。SVO。',
  },
  "You shouldn't have spent so much.": {
    pattern: 'SVO',
    note: 'spentの目的語が so much。SVO。',
  },
  'We could have taken an earlier train.': {
    pattern: 'SVO',
    note: 'takenの目的語が an earlier train。SVO。',
  },
  'You could have hurt yourself.': {
    pattern: 'SVO',
    note: 'hurtの目的語が yourself。SVO。',
  },

  // u20-l4 used to / would(過去の習慣)
  'I used to play soccer every weekend.': {
    pattern: 'SVO',
    note: 'used to + play。目的語が soccer でSVO。',
  },
  'There used to be a movie theater on this street.': {
    pattern: 'SV',
    note: 'there is 構文なのでSV。',
  },
  "She didn't use to like coffee, but now she drinks it every day.": {
    pattern: 'SVO',
    note: '先に立つ like の目的語が coffee でSVO。',
  },
  'When we were kids, we would swim in the river all summer.': {
    pattern: 'SV',
    note: '主節 we would swim は自動詞でSV。',
  },
  'My grandmother would always bake cookies on Sundays.': {
    pattern: 'SVO',
    note: 'bakeの目的語が cookies。SVO。',
  },
  'This building used to be a post office.': {
    pattern: 'SVC',
    note: 'be + 名詞 a post office のSVC。',
  },
  'Every summer, our grandfather would take us fishing.': {
    pattern: 'SVOC',
    note: 'take + 目的語 + 分詞のSVOC。',
  },
  'Did you use to wear glasses?': {
    pattern: 'SVO',
    note: '疑問文を戻すと wearの目的語が glasses でSVO。',
  },
  'We used to walk to school together every morning.': {
    pattern: 'SV',
    note: 'walk は自動詞。toの句は副詞句でSV。',
  },
  'On rainy afternoons, my father would read to us for hours.': {
    pattern: 'SV',
    note: 'read to us は自動詞扱いでSV。',
  },
  'I used to have long hair.': {
    pattern: 'SVO',
    note: 'haveの目的語が long hair。SVO。',
  },
  'We used to live near the beach.': {
    pattern: 'SV',
    note: 'live は自動詞。nearの句は副詞句でSV。',
  },
  'Every summer, we would visit our grandparents in Nagano.': {
    pattern: 'SVO',
    note: 'visitの目的語が our grandparents。SVO。',
  },
  'My grandfather would tell us stories before bed.': {
    pattern: 'SVOO',
    note: 'tell + 人 + もの のSVOO。',
  },

  // u21-l1 意味が変わる動詞
  'Please remember to bring your passport tomorrow.': {
    pattern: 'SVO',
    note: '命令文。to不定詞が目的語のSVO。',
  },
  'I remembered to send the invoice this morning.': {
    pattern: 'SVO',
    note: 'to不定詞を目的語に取るSVO。',
  },
  'I remember visiting this town as a child.': {
    pattern: 'SVO',
    note: '動名詞 visiting が目的語のSVO。',
  },
  "I don't remember saying that.": {
    pattern: 'SVO',
    note: '動名詞 saying が目的語のSVO。',
  },
  "Don't forget to take your medicine after dinner.": {
    pattern: 'SVO',
    note: '命令文。to不定詞が目的語のSVO。',
  },
  "I'll never forget seeing the northern lights in Canada.": {
    pattern: 'SVO',
    note: '動名詞 seeing が目的語のSVO。',
  },
  'She stopped working at six and went home.': {
    pattern: 'SVO',
    note: '先に立つ stopped working は動名詞目的語でSVO。',
  },
  'On the way home, we stopped to look at the ocean.': {
    pattern: 'SV',
    note: 'stop は自動詞。to look は目的の副詞句でSV。',
  },
  'I tried to open the window, but it was stuck.': {
    pattern: 'SVO',
    note: '先に立つ tried to open は to不定詞目的語でSVO。',
  },
  'Try adding a little salt if the soup tastes flat.': {
    pattern: 'SVO',
    note: '命令文。動名詞が目的語のSVO。',
  },
  'Remember to attach the file before you send the email.': {
    pattern: 'SVO',
    note: '命令文。to不定詞が目的語のSVO。',
  },
  'I remember meeting her at a conference in Seoul.': {
    pattern: 'SVO',
    note: '動名詞 meeting が目的語のSVO。',
  },
  'If the screen freezes, try restarting the computer.': {
    pattern: 'SVO',
    note: '主節は命令文。動名詞が目的語のSVO。',
  },
  'She forgot to lock the back door last night.': {
    pattern: 'SVO',
    note: 'to不定詞が目的語のSVO。',
  },

  // u21-l2 動詞 + 目的語 + to不定詞
  'I want you to check this report by Friday.': {
    pattern: 'SVOC',
    note: 'want + 人 + to不定詞のSVOC。',
  },
  'She asked the staff to bring another chair.': {
    pattern: 'SVOC',
    note: 'ask + 人 + to不定詞のSVOC。',
  },
  'My boss told me to take a day off.': {
    pattern: 'SVOC',
    note: 'tell + 人 + to不定詞のSVOC。',
  },
  "My parents didn't allow me to have a smartphone until high school.": {
    pattern: 'SVOC',
    note: 'allow + 人 + to不定詞のSVOC。',
  },
  'Please remind me to buy milk on the way home.': {
    pattern: 'SVOC',
    note: '命令文。remind + 人 + to do のSVOC。',
  },
  'The coach encouraged us to keep practicing.': {
    pattern: 'SVOC',
    note: 'encourage + 人 + to不定詞のSVOC。',
  },
  'Please remind me to buy some batteries.': {
    pattern: 'SVOC',
    note: 'remind + 人 + to不定詞のSVOC。',
  },
  'Visitors are not allowed to take photographs here.': {
    pattern: 'SV',
    note: '受動態。目的語を取らないのでSV。',
  },
  'The teacher expects every student to submit the essay online.': {
    pattern: 'SVOC',
    note: 'expect + 人 + to不定詞のSVOC。',
  },
  'I asked my neighbor not to park in front of my gate.': {
    pattern: 'SVOC',
    note: 'ask + 人 + not to do のSVOC。',
  },

  // u21-l3 形容詞 + 不定詞 / It is ... to do
  'It is important to back up your files regularly.': {
    pattern: 'SVC',
    note: 'Itは形式主語。be + 形容詞のSVC。',
  },
  'It was hard for me to explain the problem in English.': {
    pattern: 'SVC',
    note: 'Itは形式主語。was + hard のSVC。',
  },
  "It's dangerous to use your phone while driving.": {
    pattern: 'SVC',
    note: 'Itは形式主語。be + 形容詞のSVC。',
  },
  'It was kind of you to carry my bags.': {
    pattern: 'SVC',
    note: 'Itは形式主語。was + kind のSVC。',
  },
  'This app is easy to use on a small screen.': {
    pattern: 'SVC',
    note: 'be + 形容詞 easy のSVC。to以下は副詞的。',
  },
  'It is essential to keep your contact details up to date.': {
    pattern: 'SVC',
    note: 'Itは形式主語。be + 形容詞のSVC。',
  },
  'This form is difficult to complete on a phone.': {
    pattern: 'SVC',
    note: 'be + 形容詞 difficult のSVC。',
  },
  'It was thoughtful of you to bring extra umbrellas.': {
    pattern: 'SVC',
    note: 'Itは形式主語。was + thoughtful のSVC。',
  },
  'It is difficult for beginners to hear the difference between these sounds.': {
    pattern: 'SVC',
    note: 'Itは形式主語。be + 形容詞のSVC。',
  },
  'We were glad to hear that your surgery went well.': {
    pattern: 'SVC',
    note: 'be + 形容詞 glad のSVC。',
  },

  // u22-l1 第3条件文
  'If I had known about the meeting, I would have attended.': {
    pattern: 'SV',
    note: '主節 I would have attended は自動詞でSV。',
  },
  'If we had left ten minutes earlier, we would have caught the train.': {
    pattern: 'SVO',
    note: '主節 would have caught the train がSVO。',
  },
  'She would have passed the exam if she had studied a little harder.': {
    pattern: 'SVO',
    note: '主節 would have passed the exam がSVO。',
  },
  "If it hadn't rained, we would have had the barbecue in the garden.": {
    pattern: 'SVO',
    note: '主節 would have had the barbecue がSVO。',
  },
  'If you had asked me, I could have lent you the money.': {
    pattern: 'SVOO',
    note: '主節 lend + 人 + もの のSVOO。',
  },
  'If we had booked earlier, we would have paid less.': {
    pattern: 'SVO',
    note: '主節 would have paid less はSVO。',
  },
  'She might have caught the train if she had taken a taxi.': {
    pattern: 'SVO',
    note: '主節 might have caught the train がSVO。',
  },
  'If you had not called, I would have missed the deadline.': {
    pattern: 'SVO',
    note: '主節 would have missed the deadline がSVO。',
  },
  'If they had checked the schedule, they would have noticed the change.': {
    pattern: 'SVO',
    note: '主節 would have noticed the change がSVO。',
  },
  'I would have joined you if I had finished my work earlier.': {
    pattern: 'SVO',
    note: '主節 I would have joined you がSVO。',
  },
  'If I had her number, I would call her.': {
    pattern: 'SVO',
    note: '主節 I would call her がSVO。',
  },
  "If I weren't so busy, I would help you.": {
    pattern: 'SVO',
    note: '主節 I would help you がSVO。',
  },
  'If I had had her number, I would have called her.': {
    pattern: 'SVO',
    note: '主節 would have called her がSVO。',
  },
  "If I hadn't been so busy, I would have helped you.": {
    pattern: 'SVO',
    note: '主節 would have helped you がSVO。',
  },

  // u22-l2 wish / if only
  'I wish I had more time for my hobbies.': {
    pattern: 'SVO',
    note: 'wishのあとの節が目的語。SVO。',
  },
  'I wish I were better at explaining things.': {
    pattern: 'SVO',
    note: 'wishのあとの節が目的語。SVO。',
  },
  'I wish I had taken more photos on that trip.': {
    pattern: 'SVO',
    note: 'wish + 節の目的語でSVO。',
  },
  'I wish you had told me about the change earlier.': {
    pattern: 'SVO',
    note: 'wishのあとの節が目的語。SVO。',
  },
  'I wish this printer would stop jamming.': {
    pattern: 'SVO',
    note: 'wish + 節の目的語でSVO。',
  },
  'If only I had brought my camera.': {
    pattern: 'SVO',
    note: 'If only のあとは節で、broughtの目的語が続くSVO。',
  },
  'I wish our apartment had a balcony.': {
    pattern: 'SVO',
    note: 'wishのあとの節が目的語。SVO。',
  },
  'If only I had saved a copy of the document.': {
    pattern: 'SVO',
    note: 'If only のあとの節は目的語を取るSVO。',
  },
  'I wish the neighbors would turn down the music.': {
    pattern: 'SVO',
    note: '句動詞 turn down が目的語を取るSVO。',
  },
  'I wish I had asked more questions during the interview.': {
    pattern: 'SVO',
    note: 'wishのあとの節が目的語。SVO。',
  },
  'I hope you pass the exam.': {
    pattern: 'SVO',
    note: 'hopeのあとの節が目的語。SVO。',
  },
  "I hope it doesn't rain tomorrow.": {
    pattern: 'SVO',
    note: 'hope + 節の目的語でSVO。',
  },
  'I wish you lived closer to us.': {
    pattern: 'SVO',
    note: 'wishのあとの節が目的語。SVO。',
  },
  "I wish it weren't raining right now.": {
    pattern: 'SVO',
    note: 'wish + 節の目的語でSVO。',
  },

  // u22-l3 条件文 総合練習(1〜3型)
  // ※「If you mix blue and yellow, you get green.」は B1 の u15-l1 と共通の例文。
  //   同一英文なので patterns/b1.ts の SVC(get + green)をそのまま使う。
  "If the weather is nice this weekend, we'll go hiking.": {
    pattern: 'SV',
    note: '主節 go hiking は自動詞でSV。',
  },
  'If I won the lottery, I would travel around the world.': {
    pattern: 'SV',
    note: '主節 travel は自動詞でSV。',
  },
  'If I had taken that flight, I would have been stuck at the airport all night.': {
    pattern: 'SV',
    note: '主節は受動態 would have been stuck でSV。',
  },
  'If you heat ice, it melts.': {
    pattern: 'SV',
    note: '主節 it melts は自動詞でSV。',
  },
  'If I finish early tomorrow, I will pick you up.': {
    pattern: 'SVO',
    note: '主節 pick up は句動詞で目的語を取るSVO。',
  },
  'If we had checked the forecast, we would have changed our plans.': {
    pattern: 'SVO',
    note: '主節 would have changed our plans がSVO。',
  },
  'If the delivery arrives before noon, we will start the setup.': {
    pattern: 'SVO',
    note: '主節 we will start the setup がSVO。',
  },
  'If I lived in that city, I would go to concerts every month.': {
    pattern: 'SV',
    note: '主節 go to concerts は自動詞でSV。',
  },
  'If we had hired one more designer, the launch would have gone smoothly.': {
    pattern: 'SV',
    note: '主節 go は自動詞。smoothly は副詞でSV。',
  },
  "If I finish work early, I'll join you for dinner.": {
    pattern: 'SVO',
    note: '主節 I\'ll join you がSVO。',
  },
  'If you press this button, the machine will stop.': {
    pattern: 'SV',
    note: '主節 the machine will stop は自動詞でSV。',
  },
  'If I spoke French, I would apply for that job.': {
    pattern: 'SV',
    note: '主節 apply for は自動詞でSV。',
  },
  'If you had pressed that button, the machine would have stopped.': {
    pattern: 'SV',
    note: '主節 stop は自動詞でSV。',
  },
}

export const b1PlusFocus: PatternFocusMap = {
  'u17-l1':
    'have been doing も1つの動詞(V)と見る。目的語を取れば SVO、取らなければ SV。for / since の句は副詞句なので文型には数えない。',
  'u17-l2':
    '完了と進行形の違いは型には表れない。have + 過去分詞 / have been doing をまとめて1つの動詞とし、あとに目的語があれば SVO、なければ SV になる。',
  'u18-l1':
    '主節と従属節が並ぶと型は迷いやすいが、判定は主節だけで行う。when / before / by the time の節や、主節のあとの副詞句は数えない。',
  'u18-l2':
    'had + 過去分詞も1つの動詞として扱う。that節は目的語の席に入るので SVO になり、関係詞節は名詞を修飾するだけで要素に数えない。',
  'u18-l3':
    '過去の出来事を並べた文は、中心となる最初の節で判定すると安定する。was doing は1つの動詞で、目的語がなければ SV。',
  'u19-l1':
    'say は that節を目的語に取る SVO。tell は「人 + that節」と続けるので SVOO になり、ここが say との分かれ目になる。',
  'u19-l2':
    'ask / tell + 人 + if・wh節 は SVOO、ask / tell + 人 + to do は SVOC。「人」が入るかどうかで型が変わる。',
  'u19-l3':
    'promise / refuse / suggest / admit は to不定詞や動名詞・that節を目的語に取り SVO。advise / warn は「人 + to do」を取るので SVOC。',
  'u19-l4':
    '間接疑問の wh節・whether節は目的語の席に入るので、文全体は SVO。tell me が加われば「人 + 節」で SVOO になる。',
  'u20-l1':
    '推量の助動詞は文型を変えない。must / might + be + 形容詞・名詞なら SVC、be + 場所や off のような副詞なら SV。',
  'u20-l2':
    'must have / might have + 過去分詞も1つの動詞と見る。目的語を取れば SVO、受動態の be + 過去分詞なら SV、be + 形容詞なら SVC。',
  'u20-l3':
    'should have / could have + 過去分詞を1つの動詞として扱う。あとに目的語があれば SVO、なければ SV になる。',
  'u20-l4':
    'used to / would + 動詞も1つの動詞として扱う。There used to be ... は there is 構文なので SV、be + 名詞なら SVC。',
  'u21-l1':
    'remember / forget / try のあとの動名詞・to不定詞は目的語の席に入るので SVO。目的を表す副詞的な to は数えない。',
  'u21-l2':
    'want / ask / tell / allow + 人 + to do は「人」が目的語、「to do」が補語で SVOC。O と C の間に「人が〜する」の関係がある。',
  'u21-l3':
    'It is hard to do ... の It は形式主語で、真の主語は to以下。文型は be + 形容詞の SVC として数える。',
  'u22-l1':
    'if節は従属節なので数えず、主節だけで判定する。would have + 過去分詞を1つの動詞と見ると、主節は SV か SVO、lend なら SVOO になる。',
  'u22-l2':
    'wish / hope はあとに節を続け、その節がひとまとまりの目的語になるので SVO。If only も同じく願望を表す。',
  'u22-l3':
    '1〜3型が混ざっても、判定は if節を外した主節だけで行う。go / travel / apply for などの自動詞は SV、目的語を取れば SVO。',
}
