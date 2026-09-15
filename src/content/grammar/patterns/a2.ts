import type { PatternFocusMap, PatternMap } from './types.ts'

// A2(U01–U06)の文型データ。例文の英文をそのままキーにする。

export const a2Patterns: PatternMap = {
  // u01-l1 be動詞の現在形
  'I am a nurse.': { pattern: 'SVC', note: 'be動詞のあとの名詞が主語を説明する補語(C)。' },
  'She is tired today.': { pattern: 'SVC', note: 'be動詞のあとの形容詞 tired が補語(C)。' },
  'They are in the kitchen.': { pattern: 'SV', note: 'be + 場所の副詞句。補語も目的語もない。' },
  'My brother is not busy now.': { pattern: 'SVC', note: 'be動詞のあとの形容詞 busy が補語(C)。' },
  'Are you hungry right now?': { pattern: 'SVC', note: '平叙文に戻すと hungry が補語(C)。' },
  'We are not late for the meeting.': { pattern: 'SVC', note: 'be動詞のあとの形容詞 late が補語(C)。' },
  'My parents are at the station.': { pattern: 'SV', note: 'at the station は場所の副詞句で要素に数えない。' },
  'This soup is too salty.': { pattern: 'SVC', note: 'be動詞のあとの形容詞 salty が補語(C)。' },
  'Are your keys in the front pocket?': { pattern: 'SV', note: '平叙文に戻すと be + 場所。補語も目的語もない。' },
  'I am not ready for the test.': { pattern: 'SVC', note: 'be動詞のあとの形容詞 ready が補語(C)。' },

  // u01-l2 一般動詞の現在形と三単現
  'I take the bus to work.': { pattern: 'SVO', note: 'take の対象 the bus が目的語(O)。' },
  'My sister works at a bank.': { pattern: 'SV', note: 'work は目的語を取らない。at 以下は副詞句。' },
  'He watches TV after dinner.': { pattern: 'SVO', note: 'watch の対象 TV が目的語(O)。' },
  'Emi studies English every day.': { pattern: 'SVO', note: 'study の対象 English が目的語(O)。' },
  'Water boils at 100 degrees.': { pattern: 'SV', note: 'boil は目的語を取らない。at 以下は副詞句。' },
  'My brother takes the train to work.': { pattern: 'SVO', note: 'take の対象 the train が目的語(O)。' },
  'Water boils at one hundred degrees Celsius.': { pattern: 'SV', note: 'boil は自動詞。at 以下は副詞句。' },
  'Aya studies English after dinner.': { pattern: 'SVO', note: 'study の対象 English が目的語(O)。' },
  'My father goes to the gym on Saturdays.': { pattern: 'SV', note: 'go は目的語を取らない。to 以下は副詞句。' },
  'Our teacher has two children.': { pattern: 'SVO', note: 'have の対象 two children が目的語(O)。' },
  'She likes music.': { pattern: 'SVO', note: 'like の対象 music が目的語(O)。' },
  'My dog sleeps a lot.': { pattern: 'SV', note: 'sleep は目的語を取らない。a lot は副詞。' },
  'I like music.': { pattern: 'SVO', note: 'like の対象 music が目的語(O)。' },
  'My dogs sleep a lot.': { pattern: 'SV', note: 'sleep は自動詞。a lot は副詞。' },

  // u01-l3 否定文と疑問文の作り方
  "I don't eat breakfast on weekdays.": { pattern: 'SVO', note: 'eat の対象 breakfast が目的語(O)。' },
  "My son doesn't like carrots.": { pattern: 'SVO', note: 'like の対象 carrots が目的語(O)。' },
  'Do you speak English?': { pattern: 'SVO', note: '平叙文に戻すと English が目的語(O)。' },
  'Does this bus go to the airport?': { pattern: 'SV', note: 'go は目的語を取らない。to 以下は副詞句。' },
  'Does the museum open on Mondays? No, it does not.': { pattern: 'SV', note: '主節 open は目的語を取らない。' },
  'Does your sister drive to work?': { pattern: 'SV', note: 'drive は目的語を取らない。to work は副詞句。' },
  "We don't need a reservation.": { pattern: 'SVO', note: 'need の対象 a reservation が目的語(O)。' },
  'Why does this machine make that noise?': { pattern: 'SVO', note: 'make の対象 that noise が目的語(O)。' },
  'Does your father cook on weekends?': { pattern: 'SV', note: 'cook は目的語を取らない。' },
  "They don't live near the station.": { pattern: 'SV', note: 'live は目的語を取らない。' },
  'She is not a teacher.': { pattern: 'SVC', note: 'be動詞のあとの名詞 a teacher が補語(C)。' },
  'Is she a teacher?': { pattern: 'SVC', note: '平叙文に戻すと a teacher が補語(C)。' },
  "She doesn't teach English.": { pattern: 'SVO', note: 'teach の対象 English が目的語(O)。' },
  'Does she teach English?': { pattern: 'SVO', note: '平叙文に戻すと English が目的語(O)。' },

  // u02-l1 現在進行形
  'I am cooking dinner now.': { pattern: 'SVO', note: 'cook の対象 dinner が目的語(O)。' },
  'She is talking on the phone.': { pattern: 'SV', note: 'talk は目的語を取らない。' },
  'The kids are playing in the yard.': { pattern: 'SV', note: 'play は目的語を取らない。' },
  "He isn't watching TV right now.": { pattern: 'SVO', note: 'watch の対象 TV が目的語(O)。' },
  'Are you waiting for the bus?': { pattern: 'SV', note: 'wait は目的語を取らない。' },
  'The customers are waiting outside.': { pattern: 'SV', note: 'wait は自動詞で目的語を取らない。' },
  'I am staying with my aunt this week.': { pattern: 'SV', note: 'stay は目的語を取らない。' },
  'Is the baby sleeping now?': { pattern: 'SV', note: 'sleep は自動詞で目的語を取らない。' },
  'They are building a new library near the park.': { pattern: 'SVO', note: 'build の対象 a new library が目的語(O)。' },
  'My phone is charging in the kitchen.': { pattern: 'SV', note: 'charge は目的語を取らない。' },

  // u02-l2 現在形 vs 現在進行形
  'My mother teaches math at a high school.': { pattern: 'SVO', note: 'teach の対象 math が目的語(O)。' },
  'She is teaching a class right now, so she cannot answer the phone.': { pattern: 'SVO', note: 'teach a class の a class が目的語(O)。' },
  'It rains a lot in June.': { pattern: 'SV', note: 'rain は目的語を取らない。' },
  'Take an umbrella. It is raining outside.': { pattern: 'SV', note: '中心の It is raining は目的語を取らない。' },
  "I am staying at my aunt's house this week.": { pattern: 'SV', note: 'stay は目的語を取らない。' },
  'I usually work from home, but I am working at the office today.': { pattern: 'SV', note: 'work は目的語を取らない。' },
  'Mina knows the answer.': { pattern: 'SVO', note: 'know の対象 the answer が目的語(O)。' },
  'We are thinking about moving closer to the station.': { pattern: 'SV', note: 'think about は目的語を取らない。' },
  'He usually walks to school, but today he is taking the bus.': { pattern: 'SVO', note: '後半 take the bus の bus が目的語(O)。' },
  'I want a cup of coffee right now.': { pattern: 'SVO', note: 'want の対象 a cup of coffee が目的語(O)。' },
  'He works in Nagoya.': { pattern: 'SV', note: 'work は目的語を取らない。' },
  'We usually eat dinner at seven.': { pattern: 'SVO', note: 'eat の対象 dinner が目的語(O)。' },
  'He is working from home today.': { pattern: 'SV', note: 'work は目的語を取らない。' },
  'We are eating dinner now. Can I call you back?': { pattern: 'SVO', note: 'eat の対象 dinner が目的語(O)。' },

  // u02-l3 過去形(規則・不規則)
  'I visited my grandparents last weekend.': { pattern: 'SVO', note: 'visit の対象 my grandparents が目的語(O)。' },
  'We went to a new ramen shop yesterday.': { pattern: 'SV', note: 'go は目的語を取らない。' },
  'She bought a nice jacket at the mall.': { pattern: 'SVO', note: 'buy の対象 a nice jacket が目的語(O)。' },
  "I didn't watch the game last night.": { pattern: 'SVO', note: 'watch の対象 the game が目的語(O)。' },
  'Did you finish your homework?': { pattern: 'SVO', note: '平叙文に戻すと homework が目的語(O)。' },
  'The movie was really good.': { pattern: 'SVC', note: 'be動詞のあとの形容詞 good が補語(C)。' },
  'We saw a beautiful rainbow after the storm.': { pattern: 'SVO', note: 'see の対象 a beautiful rainbow が目的語(O)。' },
  "Leo didn't bring his lunch yesterday.": { pattern: 'SVO', note: 'bring の対象 his lunch が目的語(O)。' },
  'Did you enjoy the concert last night?': { pattern: 'SVO', note: '平叙文に戻すと the concert が目的語(O)。' },
  'They built this bridge about fifty years ago.': { pattern: 'SVO', note: 'build の対象 this bridge が目的語(O)。' },

  // u02-l4 過去進行形
  'I was watching TV at nine last night.': { pattern: 'SVO', note: 'watch の対象 TV が目的語(O)。' },
  'They were playing soccer when it started to rain.': { pattern: 'SVO', note: '主節 play soccer の soccer が目的語(O)。' },
  'She was cooking dinner while I was doing my homework.': { pattern: 'SVO', note: 'cook の対象 dinner が目的語(O)。' },
  'What were you doing at noon yesterday?': { pattern: 'SVO', note: 'do の対象 what が目的語(O)。' },
  "I wasn't sleeping when you called me.": { pattern: 'SV', note: '主節 sleep は目的語を取らない。' },
  'I was cooking dinner when the phone rang.': { pattern: 'SVO', note: '主節 cook dinner の dinner が目的語(O)。' },
  'While Ken was washing the dishes, I was drying them.': { pattern: 'SVO', note: 'dry の対象 them が目的語(O)。' },
  'Were you sleeping when I sent the message?': { pattern: 'SV', note: '主節 sleep は目的語を取らない。' },
  'We were waiting at the gate when the announcement came.': { pattern: 'SV', note: 'wait は目的語を取らない。' },
  'The children were drawing pictures while their mother was cooking.': { pattern: 'SVO', note: '主節 draw pictures の pictures が目的語(O)。' },
  'I read a book last night.': { pattern: 'SVO', note: 'read の対象 a book が目的語(O)。' },
  'The phone rang.': { pattern: 'SV', note: 'ring は目的語を取らない。' },
  'I was reading a book at ten last night.': { pattern: 'SVO', note: 'read の対象 a book が目的語(O)。' },
  'The phone was ringing when I got home.': { pattern: 'SV', note: '主節 ring は目的語を取らない。' },

  // u02-l5 willによる未来
  'I think our team will win the game.': { pattern: 'SVO', note: 'think の that節が目的語(O)の1要素。' },
  "It's cold in here. I'll close the window.": { pattern: 'SVO', note: '後半 close の対象 the window が目的語(O)。' },
  "Don't worry. I'll call you tonight.": { pattern: 'SVO', note: '後半 call の対象 you が目的語(O)。' },
  'She will be twenty next month.': { pattern: 'SVC', note: 'be動詞のあとの twenty が補語(C)。' },
  "I won't be at home tomorrow morning.": { pattern: 'SV', note: 'be + 場所の副詞句。補語も目的語もない。' },
  'Will you be free this weekend?': { pattern: 'SVC', note: '平叙文に戻すと free が補語(C)。' },
  'I think the new café will be popular.': { pattern: 'SVO', note: 'think の that節が目的語(O)の1要素。' },
  'The doorbell is ringing. I will answer it.': { pattern: 'SVO', note: '後半 answer の対象 it が目的語(O)。' },
  'I will carry that box for you.': { pattern: 'SVO', note: 'carry の対象 that box が目的語(O)。' },
  'I will send you the file after this meeting.': { pattern: 'SVOO', note: 'you と the file の2つの目的語。' },

  // u02-l6 be going to
  'We are going to move to Sapporo next spring.': { pattern: 'SV', note: 'move は目的語を取らない。' },
  'I am going to start jogging next week.': { pattern: 'SVO', note: '動名詞 jogging が目的語(O)。' },
  "He isn't going to take the job.": { pattern: 'SVO', note: 'take の対象 the job が目的語(O)。' },
  'What are you going to do during the holidays?': { pattern: 'SVO', note: 'do の対象 what が目的語(O)。' },
  'Look at those clouds. It is going to rain.': { pattern: 'SV', note: '中心の It is going to rain は目的語なし。' },
  'We are going to repaint the kitchen this weekend.': { pattern: 'SVO', note: 'repaint の対象 the kitchen が目的語(O)。' },
  'Look at that glass. It is going to fall.': { pattern: 'SV', note: '中心の It is going to fall は目的語なし。' },
  'Are you going to apply for the job?': { pattern: 'SV', note: 'apply for は目的語を取らない。' },
  'They are going to open a bakery next month.': { pattern: 'SVO', note: 'open の対象 a bakery が目的語(O)。' },
  'I am not going to buy a new car this year.': { pattern: 'SVO', note: 'buy の対象 a new car が目的語(O)。' },
  "I'll have the pasta, please.": { pattern: 'SVO', note: 'have の対象 the pasta が目的語(O)。' },
  'I think he will pass the exam.': { pattern: 'SVO', note: 'think の that節が目的語(O)の1要素。' },
  'I am going to make curry tonight. I bought the ingredients yesterday.': { pattern: 'SVO', note: 'make の対象 curry が目的語(O)。' },
  'She is going to have a baby in June.': { pattern: 'SVO', note: 'have の対象 a baby が目的語(O)。' },

  // u03-l1 可算名詞と不可算名詞
  'There are three apples on the table.': { pattern: 'SV', note: 'there is/are 構文は第1文型。' },
  'I need some information about the hotel.': { pattern: 'SVO', note: 'need の対象 some information が目的語(O)。' },
  'She gave me two pieces of advice.': { pattern: 'SVOO', note: 'me と two pieces of advice の2つの目的語。' },
  'We bought some furniture for the new house.': { pattern: 'SVO', note: 'buy の対象 some furniture が目的語(O)。' },
  'Money is important, but it is not everything.': { pattern: 'SVC', note: 'be動詞のあとの形容詞・名詞が補語(C)。' },
  'She gave me two useful pieces of advice.': { pattern: 'SVOO', note: 'me と pieces of advice の2つの目的語。' },
  'We need more information before we decide.': { pattern: 'SVO', note: '主節 need の対象 more information が目的語(O)。' },
  'There are three apples in the basket.': { pattern: 'SV', note: 'there are 構文は第1文型。' },
  'Could you bring me a glass of water?': { pattern: 'SVOO', note: 'me と a glass of water の2つの目的語。' },
  'Our luggage is still at the airport.': { pattern: 'SV', note: 'be + 場所の副詞句。補語も目的語もない。' },
  'I ate two eggs this morning.': { pattern: 'SVO', note: 'eat の対象 two eggs が目的語(O)。' },
  'There is a chair in the corner.': { pattern: 'SV', note: 'there is 構文は第1文型。' },
  'I ate some rice this morning.': { pattern: 'SVO', note: 'eat の対象 some rice が目的語(O)。' },
  'There is some furniture in the corner.': { pattern: 'SV', note: 'there is 構文は第1文型。' },

  // u03-l2 a / an の使い方
  'She will arrive in an hour.': { pattern: 'SV', note: 'arrive は目的語を取らない。' },
  'He gave me an honest answer.': { pattern: 'SVOO', note: 'me と an honest answer の2つの目的語。' },
  'My cousin works at a university.': { pattern: 'SV', note: 'work は目的語を取らない。' },
  'They are planning a one-day trip.': { pattern: 'SVO', note: 'plan の対象 a one-day trip が目的語(O)。' },
  'I saw a dog in the park.': { pattern: 'SVO', note: 'see の対象 a dog が目的語(O)。' },
  'She is an engineer.': { pattern: 'SVC', note: 'be動詞のあとの名詞 an engineer が補語(C)。' },
  'The meeting starts in an hour.': { pattern: 'SV', note: 'start は目的語を取らない。' },
  'He goes to a university in Nagoya.': { pattern: 'SV', note: 'go は目的語を取らない。' },
  'Do you have an umbrella?': { pattern: 'SVO', note: '平叙文に戻すと an umbrella が目的語(O)。' },
  'We waited for an hour.': { pattern: 'SV', note: 'wait は目的語を取らない。' },
  'She studies at a university in Boston.': { pattern: 'SV', note: 'study は目的語を取らない。' },
  'My uncle is an honest person.': { pattern: 'SVC', note: 'be動詞のあとの名詞 an honest person が補語(C)。' },
  'He is an honest and careful driver.': { pattern: 'SVC', note: 'be動詞のあとの名詞 driver が補語(C)。' },
  'She wants to visit a European city this summer.': { pattern: 'SVO', note: 'to不定詞が目的語(O)。' },

  // u03-l3 the の使い方
  'I bought a shirt and a jacket. The shirt was on sale.': { pattern: 'SV', note: '後半の be + 句は補語でなく副詞句。' },
  'Could you open the window?': { pattern: 'SVO', note: 'open の対象 the window が目的語(O)。' },
  'The sun rises in the east.': { pattern: 'SV', note: 'rise は目的語を取らない。' },
  'Is this the key to the front door?': { pattern: 'SVC', note: '平叙文に戻すと the key が補語(C)。' },
  'I bought a lamp, and the lamp is beside my bed.': { pattern: 'SV', note: '後半は be + 場所の副詞句。' },
  'Please turn off the lights when you leave.': { pattern: 'SVO', note: 'turn off の対象 the lights が目的語(O)。' },
  'Books can take us to different worlds.': { pattern: 'SVO', note: 'take us の us が目的語(O)。to以下は副詞句。' },
  'We usually go to work by train.': { pattern: 'SV', note: 'go は目的語を取らない。' },
  'My daughter practices the violin every evening.': { pattern: 'SVO', note: 'practice の対象 the violin が目的語(O)。' },
  'The restaurant on the corner closes at ten.': { pattern: 'SV', note: 'close は目的語を取らない。' },
  'The coffee at that cafe is great.': { pattern: 'SVC', note: 'be動詞のあとの形容詞 great が補語(C)。' },
  'The children are playing outside.': { pattern: 'SV', note: 'play は目的語を取らない。' },
  'Coffee keeps me awake.': { pattern: 'SVOC', note: 'me = awake で awake が補語(C)。' },
  'Children learn languages quickly.': { pattern: 'SVO', note: 'learn の対象 languages が目的語(O)。' },

  // u03-l4 some / any / much / many
  'I bought some oranges at the market.': { pattern: 'SVO', note: 'buy の対象 some oranges が目的語(O)。' },
  'Would you like some tea?': { pattern: 'SVO', note: 'like の対象 some tea が目的語(O)。' },
  "We don't have any milk.": { pattern: 'SVO', note: 'have の対象 any milk が目的語(O)。' },
  'Do you have any questions?': { pattern: 'SVO', note: '平叙文に戻すと any questions が目的語(O)。' },
  'How many students are in your class?': { pattern: 'SV', note: 'be + 場所の副詞句。補語も目的語もない。' },
  "I don't have much time today.": { pattern: 'SVO', note: 'have の対象 much time が目的語(O)。' },
  'There are a lot of restaurants near here.': { pattern: 'SV', note: 'there are 構文は第1文型。' },
  'Can I have some water?': { pattern: 'SVO', note: 'have の対象 some water が目的語(O)。' },
  'Is there any coffee left?': { pattern: 'SV', note: 'there is 構文は第1文型。' },
  'Would you like some soup?': { pattern: 'SVO', note: 'like の対象 some soup が目的語(O)。' },
  "We don't have any clean towels.": { pattern: 'SVO', note: 'have の対象 any clean towels が目的語(O)。' },
  'How much time do we have?': { pattern: 'SVO', note: 'have の対象 how much time が目的語(O)。' },
  "There aren't any seats left on this train.": { pattern: 'SV', note: 'there are 構文は第1文型。' },
  'We invited a lot of friends to the party.': { pattern: 'SVO', note: 'invite の対象 a lot of friends が目的語(O)。' },

  // u04-l1 人称代名詞と格
  'She knows me very well.': { pattern: 'SVO', note: 'know の対象 me が目的語(O)。' },
  'This is my umbrella.': { pattern: 'SVC', note: 'be動詞のあとの名詞 my umbrella が補語(C)。' },
  'This umbrella is mine.': { pattern: 'SVC', note: 'be動詞のあとの所有代名詞 mine が補語(C)。' },
  'We invited them to the party.': { pattern: 'SVO', note: 'invite の対象 them が目的語(O)。' },
  'Can you help us with this?': { pattern: 'SVO', note: 'help us の us が目的語(O)。' },
  'I had dinner with him yesterday.': { pattern: 'SVO', note: 'have の対象 dinner が目的語(O)。' },
  'They invited us to dinner.': { pattern: 'SVO', note: 'invite の対象 us が目的語(O)。' },
  'This seat is hers, and that one is mine.': { pattern: 'SVC', note: 'be動詞のあとの所有代名詞が補語(C)。' },
  'Please send the photos to him.': { pattern: 'SVO', note: 'send の対象 the photos が目的語(O)。' },
  'His sister called her yesterday afternoon.': { pattern: 'SVO', note: 'call の対象 her が目的語(O)。' },

  // u04-l2 this / that / these / those
  'This is my favorite mug.': { pattern: 'SVC', note: 'be動詞のあとの名詞 my favorite mug が補語(C)。' },
  'These shoes are too small.': { pattern: 'SVC', note: 'be動詞のあとの形容詞 small が補語(C)。' },
  'That building is a museum.': { pattern: 'SVC', note: 'be動詞のあとの名詞 a museum が補語(C)。' },
  'Those clouds look like rain.': { pattern: 'SVC', note: 'look は連結動詞で like rain が主語を説明。' },
  'Who is that man by the door?': { pattern: 'SVC', note: '平叙文に戻すと that man が補語(C)。' },
  'These cookies are still warm.': { pattern: 'SVC', note: 'be動詞のあとの形容詞 warm が補語(C)。' },
  'Who is that man by the gate?': { pattern: 'SVC', note: '平叙文に戻すと that man が補語(C)。' },
  'That sounds like a good plan.': { pattern: 'SVC', note: 'sound は連結動詞で like以下が主語を説明。' },
  'Are these your gloves or mine?': { pattern: 'SVC', note: '平叙文に戻すと your gloves が補語(C)。' },
  'Those houses across the river look new.': { pattern: 'SVC', note: 'look + 形容詞 new は補語(C)。' },
  'This coffee smells great.': { pattern: 'SVC', note: 'smell + 形容詞 great は補語(C)。' },
  'These photos are from my trip.': { pattern: 'SV', note: 'be + 前置詞句 from my trip は副詞句。' },
  'That mountain is beautiful.': { pattern: 'SVC', note: 'be動詞のあとの形容詞 beautiful が補語(C)。' },
  'Those were good days.': { pattern: 'SVC', note: 'be動詞のあとの名詞 good days が補語(C)。' },

  // u04-l3 one / ones / it の使い分け
  'I lost my pen, so I bought a new one.': { pattern: 'SVO', note: 'bought の対象 a new one が目的語(O)。' },
  'Do you have a stapler? I need one.': { pattern: 'SVO', note: 'need の対象 one が目的語(O)。' },
  'I lost my pen, but Ken found it.': { pattern: 'SVO', note: '後半 found の対象 it が目的語(O)。' },
  'I bought a new phone. I really like it.': { pattern: 'SVO', note: 'like の対象 it が目的語(O)。' },
  'This cup is dirty. Can I have a clean one?': { pattern: 'SVO', note: 'have の対象 a clean one が目的語(O)。' },
  'I like these shoes better than the black ones.': { pattern: 'SVO', note: 'like の対象 these shoes が目的語(O)。' },
  'Which one is your bag? — The big one.': { pattern: 'SVC', note: '平叙文に戻すと Your bag is the big one。' },
  'My computer is old, so I want a new one.': { pattern: 'SVO', note: '後半 want の対象 a new one が目的語(O)。' },
  "Where is my key? I can't find it.": { pattern: 'SVO', note: '後半 find の対象 it が目的語(O)。' },
  'This chair is uncomfortable. Can I use that one?': { pattern: 'SVO', note: 'use の対象 that one が目的語(O)。' },
  'I like the blue shoes more than the black ones.': { pattern: 'SVO', note: 'like の対象 the blue shoes が目的語(O)。' },
  'I found my wallet, but I left it at home again.': { pattern: 'SVO', note: 'left の対象 it が目的語(O)。' },
  'My umbrella broke, so I bought a stronger one.': { pattern: 'SVO', note: 'bought の対象 a stronger one が目的語(O)。' },
  'She borrowed my dictionary and returned it this morning.': { pattern: 'SVO', note: 'borrow/return の対象が目的語(O)。' },

  // u05-l1 形容詞の位置と使い方
  'She has a beautiful voice.': { pattern: 'SVO', note: 'have の対象 a beautiful voice が目的語(O)。' },
  'This soup is delicious.': { pattern: 'SVC', note: 'be動詞のあとの形容詞 delicious が補語(C)。' },
  'I bought an expensive watch.': { pattern: 'SVO', note: 'buy の対象 an expensive watch が目的語(O)。' },
  'The children look sleepy.': { pattern: 'SVC', note: 'look + 形容詞 sleepy は補語(C)。' },
  'We stayed at a cheap hotel.': { pattern: 'SV', note: 'stay は目的語を取らない。' },
  'They live in a small wooden house.': { pattern: 'SV', note: 'live は目的語を取らない。' },
  'The children look tired after the trip.': { pattern: 'SVC', note: 'look + 形容詞 tired は補語(C)。' },
  'We watched an interesting documentary.': { pattern: 'SVO', note: 'watch の対象 a documentary が目的語(O)。' },
  'I would like something cold to drink.': { pattern: 'SVO', note: 'like の対象 something cold が目的語(O)。' },
  'They sell fresh bread at that little shop.': { pattern: 'SVO', note: 'sell の対象 fresh bread が目的語(O)。' },

  // u05-l2 副詞の形と位置
  'Please speak slowly during the announcement.': { pattern: 'SV', note: 'speak は目的語を取らない。' },
  'He passed the test easily.': { pattern: 'SVO', note: 'pass の対象 the test が目的語(O)。' },
  'My father works hard.': { pattern: 'SV', note: 'work は目的語を取らない。hard は副詞。' },
  'She sings very well.': { pattern: 'SV', note: 'sing は目的語を取らない。' },
  'The train arrived late.': { pattern: 'SV', note: 'arrive は目的語を取らない。' },
  'It rained heavily last night.': { pattern: 'SV', note: 'rain は目的語を取らない。' },
  'Nora explained the problem clearly.': { pattern: 'SVO', note: 'explain の対象 the problem が目的語(O)。' },
  'This train is incredibly fast.': { pattern: 'SVC', note: 'be動詞のあとの形容詞 fast が補語(C)。' },
  'The flowers smell sweet.': { pattern: 'SVC', note: 'smell + 形容詞 sweet は補語(C)。' },
  'He drives carefully on narrow streets.': { pattern: 'SV', note: 'drive は目的語を取らない。' },
  'She is a quiet person.': { pattern: 'SVC', note: 'be動詞のあとの名詞 a quiet person が補語(C)。' },
  'His English is good.': { pattern: 'SVC', note: 'be動詞のあとの形容詞 good が補語(C)。' },
  'She speaks quietly.': { pattern: 'SV', note: 'speak は目的語を取らない。' },
  'He speaks English well.': { pattern: 'SVO', note: 'speak の対象 English が目的語(O)。' },

  // u05-l3 頻度の副詞
  'I always brush my teeth before bed.': { pattern: 'SVO', note: 'brush の対象 my teeth が目的語(O)。' },
  'She is often late for meetings.': { pattern: 'SVC', note: 'be動詞のあとの形容詞 late が補語(C)。' },
  'We sometimes eat out on Fridays.': { pattern: 'SV', note: 'eat out は句動詞で目的語を取らない。' },
  'My father rarely watches TV.': { pattern: 'SVO', note: 'watch の対象 TV が目的語(O)。' },
  'I never drink coffee at night.': { pattern: 'SVO', note: 'drink の対象 coffee が目的語(O)。' },
  'Our team usually meets on Monday mornings.': { pattern: 'SV', note: 'meet は目的語を取らない。' },
  'Sam is rarely late for class.': { pattern: 'SVC', note: 'be動詞のあとの形容詞 late が補語(C)。' },
  'Our neighbors are never noisy at night.': { pattern: 'SVC', note: 'be動詞のあとの形容詞 noisy が補語(C)。' },
  'I often forget my umbrella at the office.': { pattern: 'SVO', note: 'forget の対象 my umbrella が目的語(O)。' },
  'My grandmother always walks to the market.': { pattern: 'SV', note: 'walk は目的語を取らない。' },

  // u06-l1 Wh疑問文
  'What time do you usually get up?': { pattern: 'SV', note: 'get up は句動詞で目的語を取らない。' },
  'Where did you buy that jacket?': { pattern: 'SVO', note: 'buy の対象 that jacket が目的語(O)。' },
  'When does the next bus leave?': { pattern: 'SV', note: 'leave は目的語を取らない。' },
  'Why is he angry?': { pattern: 'SVC', note: 'be動詞のあとの形容詞 angry が補語(C)。' },
  'Who is your favorite singer?': { pattern: 'SVC', note: '平叙文に戻すと singer が補語(C)。' },
  'How do I get to the station?': { pattern: 'SV', note: 'get to ~ は目的語を取らない。' },
  'Where did you put the spare key?': { pattern: 'SVO', note: 'put の対象 the spare key が目的語(O)。' },
  'Why is the store closed today?': { pattern: 'SV', note: 'be + 過去分詞の受動態。目的語を取らない。' },
  'What does this button do?': { pattern: 'SVO', note: 'do の対象 what が目的語(O)。' },
  'When did you move to this city?': { pattern: 'SV', note: 'move to ~ は目的語を取らない。' },

  // u06-l2 How + 形容詞/副詞
  'How much water do you drink every day?': { pattern: 'SVO', note: 'drink の対象 how much water が目的語(O)。' },
  'How much is this bag?': { pattern: 'SVC', note: '平叙文に戻すと This bag is how much の SVC。' },
  'How many eggs do we need?': { pattern: 'SVO', note: 'need の対象 how many eggs が目的語(O)。' },
  'How many people did you invite?': { pattern: 'SVO', note: 'invite の対象 how many people が目的語(O)。' },
  'How long does it take to get to the airport?': { pattern: 'SVO', note: 'take は時間を目的語に取る。' },
  'How often do you eat out?': { pattern: 'SV', note: 'eat out は句動詞で目的語を取らない。' },
  'How far is it from here to the beach?': { pattern: 'SVC', note: 'be動詞のあとの形容詞 far が補語(C)。' },
  'How old is your dog?': { pattern: 'SVC', note: 'be動詞のあとの形容詞 old が補語(C)。' },
  'How many languages does he speak?': { pattern: 'SVO', note: 'speak の対象 how many languages が目的語(O)。' },
  'How often do you call your grandparents?': { pattern: 'SVO', note: 'call の対象 your grandparents が目的語(O)。' },
  'How far is the hotel from the airport?': { pattern: 'SVC', note: 'be動詞のあとの形容詞 far が補語(C)。' },
  'How many guests are coming tonight?': { pattern: 'SV', note: 'come は目的語を取らない。' },
  'How much does a ticket cost?': { pattern: 'SVO', note: 'cost は値段を目的語に取る。' },
  'How long is the flight to Seoul?': { pattern: 'SVC', note: 'be動詞のあとの形容詞 long が補語(C)。' },

  // u06-l3 主語を尋ねる疑問文
  'Who called you?': { pattern: 'SVO', note: 'call の対象 you が目的語(O)。' },
  'What happened last night?': { pattern: 'SV', note: 'happen は目的語を取らない。' },
  'Who did you call?': { pattern: 'SVO', note: '平叙文に戻すと call の対象 who が目的語(O)。' },
  'What did you do last night?': { pattern: 'SVO', note: 'do の対象 what が目的語(O)。' },
  'Who made this cake?': { pattern: 'SVO', note: 'make の対象 this cake が目的語(O)。' },
  'Who wants some ice cream?': { pattern: 'SVO', note: 'want の対象 some ice cream が目的語(O)。' },
  'What happened to your leg?': { pattern: 'SV', note: 'happen は目的語を取らない。' },
  'Who teaches you English?': { pattern: 'SVOO', note: 'you と English の2つの目的語。' },
  'Which bus goes to the airport?': { pattern: 'SV', note: 'go は目的語を取らない。' },
  'Who left this note on my desk?': { pattern: 'SVO', note: 'leave の対象 this note が目的語(O)。' },
  'What caused the delay?': { pattern: 'SVO', note: 'cause の対象 the delay が目的語(O)。' },
  'Who wants the last slice of pizza?': { pattern: 'SVO', note: 'want の対象 the last slice が目的語(O)。' },
  'Who lives in that old house?': { pattern: 'SV', note: 'live は目的語を取らない。' },
  'What broke the window last night?': { pattern: 'SVO', note: 'break の対象 the window が目的語(O)。' },
}

export const a2Focus: PatternFocusMap = {
  'u01-l1':
    'be動詞の文は第2文型(SVC)が中心です。be動詞のあとの名詞や形容詞が補語(C)の席に入り、主語を説明します。場所を表す句が続くときは補語ではなく副詞句なので、第1文型(SV)になります。',
  'u01-l2':
    '一般動詞の現在形は、動作の対象があれば第3文型(SVO)、なければ第1文型(SV)です。works や goes、sleeps のように目的語を取らない動詞は、前置詞句が続いても SV のままです。',
  'u01-l3':
    '否定文・疑問文も平叙文に戻して考えると文型は同じです。do/does のあとの動詞が目的語を取れば SVO、取らなければ SV、be動詞なら補語(C)をとって SVC です。',
  'u02-l1':
    '現在進行形は be + -ing で「〜している最中」を表します。動作の対象があれば第3文型(SVO)、なければ第1文型(SV)です。talk や wait は目的語を取らないので SV になります。',
  'u02-l2':
    '現在形は習慣や事実、進行形は今起きていることを表しますが、文型は動詞のあとに何が続くかで決まります。work や rain は目的語を取らず SV、take the bus のように対象があれば SVO です。',
  'u02-l3':
    '過去形も文型の作りは現在形と同じです。動詞のあとの名詞が動作の対象なら目的語(O)で第3文型(SVO)、be動詞なら補語(C)で第2文型(SVC)です。',
  'u02-l4':
    '過去進行形は was/were + -ing です。when や while の節が付いても、中心となる主節の動詞で文型を決めます。主節が目的語を取れば SVO、取らなければ SV です。',
  'u02-l5':
    'will は「〜だろう / 〜するつもり」を表す助動詞で、文型は後ろの動詞で決まります。be動詞なら補語(C)をとる SVC、目的語があれば SVO、2つの目的語なら SVOO です。',
  'u02-l6':
    'be going to は「〜する予定」を表し、文型は to のあとの動詞で決まります。目的語を取らない move や rain、fall は SV、目的語を取れば SVO です。',
  'u03-l1':
    '可算・不可算にかかわらず、文型は動詞のあとに何が続くかで決まります。there is/are は第1文型(SV)で、名詞は補語ではなく存在を表す要素として続きます。',
  'u03-l2':
    'a / an は後ろの名詞の発音で選びますが、文型の判定には関係しません。be動詞のあとの名詞なら補語(C)で SVC、動詞の対象となる名詞なら目的語(O)で SVO です。',
  'u03-l3':
    'the の有無は文型に影響しません。動詞の対象となる名詞が続けば SVO、be動詞のあとに名詞や形容詞が来れば SVC、場所や状態の前置詞句なら SV です。',
  'u03-l4':
    'some / any / much / many は名詞の数量を表します。数量表現は1つの目的語(O)として数えるので、動詞のあとに続けば第3文型(SVO)です。there is/are は SV のままです。',
  'u04-l1':
    '代名詞は名詞と同じように、主語(S)・目的語(O)・補語(C)の席に入ります。動詞の対象になる目的格の代名詞は目的語(O)で、be動詞のあとの所有代名詞は補語(C)です。',
  'u04-l2':
    'this / that / these / those は主語や補語になります。be動詞のあとに名詞や形容詞が続く文は第2文型(SVC)で、look や smell、sound のような連結動詞も補語(C)をとります。',
  'u04-l3':
    'one / ones / it も名詞の席に入ります。動詞の対象なら目的語(O)で第3文型(SVO)、be動詞のあとなら補語(C)で第2文型(SVC)です。',
  'u05-l1':
    '形容詞は名詞を修飾するか、補語(C)の席に入ります。be動詞や look のあとの形容詞は補語(C)で第2文型(SVC)、名詞の前の形容詞は要素に数えません。',
  'u05-l2':
    '副詞は動詞や形容詞を修飾し、文型の要素には数えません。speak slowly は SV、explained the problem clearly は目的語をとって SVO、be + 形容詞は SVC です。',
  'u05-l3':
    '頻度の副詞は一般動詞の前、be動詞の後ろに置かれますが、文型には数えません。動詞の対象となる名詞があれば SVO、be動詞のあとの形容詞なら SVC です。',
  'u06-l1':
    'Wh疑問文も平叙文に戻して文型を判定します。疑問詞が目的語の働きをすれば SVO、場所や時を尋ねる副詞なら SV、be動詞のあとに補語があれば SVC です。',
  'u06-l2':
    'How + 形容詞/副詞の疑問文も、平叙文に戻すと文型が見えます。is のあとの old や far、long は補語(C)で SVC、How many/much が名詞の対象なら SVO です。',
  'u06-l3':
    '主語を尋ねる疑問文では、疑問詞そのものが主語(S)になります。動作の対象が続けば SVO、happen のように目的語を取らない動詞なら SV です。',
}
