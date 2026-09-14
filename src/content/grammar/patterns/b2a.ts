import type { PatternFocusMap, PatternMap } from './types.ts'

// B2 前半(U23–U28)の文型データ。例文の英文をそのままキーにする。

export const b2aPatterns: PatternMap = {
  // u23-l1 混合条件文
  'If I had taken that job, I would be living in New York now.': {
    pattern: 'SV',
    note: '主節は would be living。場所の副詞句は数えず SV。',
  },
  'If she had studied medicine, she would be a doctor today.': {
    pattern: 'SVC',
    note: '主節は be + 名詞。S = C の SVC。',
  },
  "If we hadn't missed our flight, we would be on the beach right now.": {
    pattern: 'SV',
    note: '所在の be + 場所は SV。if節は仮定法過去完了。',
  },
  "If he had saved more money, he wouldn't be so worried now.": {
    pattern: 'SVC',
    note: 'be + 形容詞 worried。S = C の SVC。',
  },
  "If I weren't so shy, I would have introduced myself at the party.": {
    pattern: 'SVO',
    note: '主節は introduced myself で SVO。at 句は数えない。',
  },
  'If I had accepted that job, I would live in Berlin now.': {
    pattern: 'SV',
    note: 'live は自動詞。場所の副詞句は数えず SV。',
  },
  'If she had charged her phone, we could contact her now.': {
    pattern: 'SVO',
    note: 'could contact her で SVO。if節は仮定法過去完了。',
  },
  'If I were more careful, I would not have deleted the file.': {
    pattern: 'SVO',
    note: 'would have deleted + O の SVO。if節は仮定法過去。',
  },
  'If we had bought the apartment last year, we would not be paying rent now.': {
    pattern: 'SVO',
    note: 'be paying + rent(O) の SVO。',
  },
  'If he had studied engineering, he would be working at a design firm today.': {
    pattern: 'SV',
    note: 'work は自動詞。場所の副詞句は数えず SV。',
  },

  // u23-l2 provided / suppose / on condition that
  'You may leave early provided that you finish the report first.': {
    pattern: 'SV',
    note: 'leave early で SV。条件は provided that 節。',
  },
  'They agreed to the deal on condition that the price stayed the same.': {
    pattern: 'SV',
    note: 'agree to は自動詞用法。前置詞句は数えず SV。',
  },
  'Suppose the train was cancelled. How would you get to the airport?': {
    pattern: 'SV',
    note: '疑問文を戻すと get to。get は自動詞で SV。',
  },
  'Supposing nobody replies, should we send the message again?': {
    pattern: 'SVO',
    note: 'send + the message(O) の SVO。',
  },
  'You can borrow my car this weekend provided you fill up the tank before you return it.': {
    pattern: 'SVO',
    note: 'borrow + my car(O) の SVO。',
  },
  "We'll sign the contract on condition that the price stays the same.": {
    pattern: 'SVO',
    note: 'sign + the contract(O) の SVO。',
  },
  'Suppose you lost your phone while travelling abroad. What would you do first?': {
    pattern: 'SVO',
    note: '疑問文を戻し do + what(O) の SVO。',
  },
  'Supposing he refuses to sign the contract, who will explain the situation to the client?': {
    pattern: 'SVO',
    note: 'explain + O。to 句は数えない SVO。',
  },
  'Providing that everyone agrees, we will start the project next week.': {
    pattern: 'SVO',
    note: 'start + the project(O) の SVO。',
  },
  'What if we miss the last train and there are no taxis outside the station?': {
    pattern: 'SVO',
    note: 'if節の miss + the last train(O) で SVO。',
  },
  'You may work remotely on Fridays provided that your manager agrees in advance.': {
    pattern: 'SV',
    note: 'work は自動詞。provided that 節は条件の SV。',
  },
  'The landlord agreed on condition that we paid a larger deposit.': {
    pattern: 'SV',
    note: 'agree は自動詞で SV。条件は on condition that 節。',
  },
  'Suppose the client rejected both designs. What would we do next?': {
    pattern: 'SVO',
    note: '疑問文を戻し do + what(O) の SVO。',
  },
  'Supposing the supplier raised the price next month, how would we explain that to our customers?': {
    pattern: 'SVO',
    note: 'explain + that(O)。to 句は数えない SVO。',
  },

  // u23-l3 would rather / it's time
  "I'd rather stay home tonight.": {
    pattern: 'SV',
    note: 'would rather + 原形。stay は自動詞で SV。',
  },
  "I'd rather not go out in this rain.": {
    pattern: 'SV',
    note: 'go out は句動詞。in 句は数えず SV。',
  },
  "I'd rather you stayed home tonight.": {
    pattern: 'SVO',
    note: 'would rather + 節を O とみなす SVO。',
  },
  "I'd rather you didn't go out in this rain.": {
    pattern: 'SVO',
    note: 'would rather + 節を O とみなす SVO。',
  },
  "I'd rather walk to the office than squeeze onto a crowded morning train.": {
    pattern: 'SV',
    note: 'would rather + walk。to 句は数えず SV。',
  },
  "I'd rather not talk about the results until everyone has had time to read them.": {
    pattern: 'SV',
    note: 'talk は自動詞。about 句は数えず SV。',
  },
  "I'd rather you told me the truth now, even if it is bad news.": {
    pattern: 'SVO',
    note: 'would rather + 節を O とみなす SVO。',
  },
  'Would you rather work from home or come to the office?': {
    pattern: 'SV',
    note: '疑問文を戻す。work は自動詞で SV。',
  },
  "It's time we left. The last train leaves at eleven.": {
    pattern: 'SVC',
    note: 'It is time + 節。関係詞節は数えず SVC。',
  },
  "It's high time you cleaned your room, because your guests arrive tomorrow morning.": {
    pattern: 'SVC',
    note: 'It is high time + 節。関係詞節は数えず SVC。',
  },
  'I would rather take the train than drive in the snow.': {
    pattern: 'SVO',
    note: 'take + the train(O) の SVO。',
  },
  'We would rather you did not mention the delay yet.': {
    pattern: 'SVO',
    note: 'would rather + 節を O とみなす SVO。',
  },
  'It is about time we replaced this old printer with a faster and quieter model.': {
    pattern: 'SVC',
    note: 'It is about time + 節。関係詞節は数えず SVC。',
  },
  'I would rather finish the report tonight than start the week with unfinished work.': {
    pattern: 'SVO',
    note: 'finish + the report(O) の SVO。',
  },

  // u24-l1 have / get something done
  'I had my hair cut yesterday because I have a job interview on Friday.': {
    pattern: 'SVOC',
    note: 'have + O + 過去分詞。O が「切られる」状態の SVOC。',
  },
  'We got the kitchen repainted last month and it looks much brighter now.': {
    pattern: 'SVOC',
    note: 'get + O + 過去分詞。前の節で判定し SVOC。',
  },
  'I need to have this suit cleaned before the wedding.': {
    pattern: 'SVOC',
    note: 'have + O + 過去分詞。to不定詞の内部で SVOC。',
  },
  'Where do you get your car serviced when the warranty has already expired?': {
    pattern: 'SVOC',
    note: '疑問文を戻し get + O + 過去分詞の SVOC。',
  },
  'He had his bag stolen at the airport while he was checking the departure board.': {
    pattern: 'SVOC',
    note: 'have + O + 過去分詞。被害を表す SVOC。',
  },
  'We are having the roof inspected next week before the rainy season begins.': {
    pattern: 'SVOC',
    note: 'have + O + 過去分詞。O = the roof の SVOC。',
  },
  'I finally got my laptop repaired after waiting almost three weeks for the parts.': {
    pattern: 'SVOC',
    note: 'get + O + 過去分詞。O = my laptop の SVOC。',
  },
  'A tourist had her passport stolen on the train.': {
    pattern: 'SVOC',
    note: 'have + O + 過去分詞。被害を表す SVOC。',
  },
  'We should have the air conditioner serviced before the summer heat arrives in earnest.': {
    pattern: 'SVOC',
    note: 'have + O + 過去分詞。O の状態を変える SVOC。',
  },
  'She got her documents translated by a certified agency before submitting the application.': {
    pattern: 'SVOC',
    note: 'get + O + 過去分詞。by 句は数えない SVOC。',
  },
  'I fixed my bike.': {
    pattern: 'SVO',
    note: 'fix は他動詞。my bike が O の SVO。',
  },
  'She painted the fence.': {
    pattern: 'SVO',
    note: 'paint は他動詞。the fence が O の SVO。',
  },
  'I had my bike fixed.': {
    pattern: 'SVOC',
    note: 'have + O + 過去分詞。O = my bike の SVOC。',
  },
  'She got the fence painted.': {
    pattern: 'SVOC',
    note: 'get + O + 過去分詞。O = the fence の SVOC。',
  },

  // u24-l2 make / let / have / get + 人 + 動詞
  'The teacher made us clean the classroom before we were allowed to go home.': {
    pattern: 'SVOC',
    note: 'make + O + 原形。us が O の SVOC。',
  },
  'My parents let me stay out late on weekends.': {
    pattern: 'SVOC',
    note: 'let + O + 原形。me が O の SVOC。',
  },
  "I'll have my assistant send you the file as soon as the meeting is over.": {
    pattern: 'SVOC',
    note: 'have + O + 原形。my assistant が O の SVOC。',
  },
  'How did you get your kids to eat vegetables?': {
    pattern: 'SVOC',
    note: '疑問文を戻し get + O + to不定詞の SVOC。',
  },
  'He was made to wait outside for an hour before anyone came to explain the delay.': {
    pattern: 'SV',
    note: '受動態は be + 過去分詞で1動詞。SV とみなす。',
  },
  'The funny video made everyone in the meeting room laugh for a full minute.': {
    pattern: 'SVOC',
    note: 'make + O + 原形。laugh が C の SVOC。',
  },
  'My supervisor had me rewrite the introduction three times before she approved it.': {
    pattern: 'SVOC',
    note: 'have + O + 原形。me が O の SVOC。',
  },
  'We finally got the supplier to lower the price.': {
    pattern: 'SVOC',
    note: 'get + O + to不定詞。to lower が C の SVOC。',
  },
  'The new policy lets employees choose their own working hours within a fixed range.': {
    pattern: 'SVOC',
    note: 'let + O + 原形。choose が C の SVOC。',
  },
  'It took three phone calls to get the landlord to fix the broken heater.': {
    pattern: 'SVO',
    note: 'It は形式主語。took + O の SVO。',
  },
  'My mother makes me practice the piano every day.': {
    pattern: 'SVOC',
    note: 'make + O + 原形。practice が C の SVOC。',
  },
  'The movie made me cry.': {
    pattern: 'SVOC',
    note: 'make + O + 原形。cry が C の SVOC。',
  },
  'My mother lets me play games after dinner.': {
    pattern: 'SVOC',
    note: 'let + O + 原形。play が C の SVOC。',
  },
  'Let me carry that for you.': {
    pattern: 'SVOC',
    note: '命令文で You を補う。let + O + 原形の SVOC。',
  },

  // u24-l3 知覚動詞 + 原形 / -ing
  'I felt the floor shake twice during the night and could not get back to sleep.': {
    pattern: 'SVOC',
    note: 'feel + O + 原形。the floor が O の SVOC。',
  },
  'Did you hear the phone ring while I was taking a shower this morning?': {
    pattern: 'SVOC',
    note: '疑問文を戻し hear + O + 原形の SVOC。',
  },
  'She noticed a man standing by the gate and quietly asked him what he wanted.': {
    pattern: 'SVOC',
    note: 'notice + O + 分詞。a man が O の SVOC。',
  },
  'We watched the children playing in the pool for a while.': {
    pattern: 'SVOC',
    note: 'watch + O + 分詞。the children が O の SVOC。',
  },
  'I heard my name called from behind just as I was leaving the building.': {
    pattern: 'SVOC',
    note: 'hear + O + 過去分詞。my name が O の SVOC。',
  },
  'I heard someone knock three times and then walk quickly down the corridor.': {
    pattern: 'SVOC',
    note: 'hear + O + 原形。someone が O の SVOC。',
  },
  'We watched the children building a shelter out of branches and old blankets.': {
    pattern: 'SVOC',
    note: 'watch + O + 分詞。the children が O の SVOC。',
  },
  'The suspect was seen to enter the building at midnight.': {
    pattern: 'SV',
    note: '受動態の知覚構文。be + 過去分詞で SV。',
  },
  'I saw the technician replace the entire panel and test every switch afterwards.': {
    pattern: 'SVOC',
    note: 'see + O + 原形。the technician が O の SVOC。',
  },
  'From my desk I could hear the rain hitting the windows all afternoon.': {
    pattern: 'SVOC',
    note: 'hear + O + 分詞。the rain が O の SVOC。',
  },
  'I saw him cross the street.': {
    pattern: 'SVOC',
    note: 'see + O + 原形。him が O の SVOC。',
  },
  'We watched the plane take off.': {
    pattern: 'SVOC',
    note: 'watch + O + 原形。take off が C の SVOC。',
  },
  'I saw him crossing the street.': {
    pattern: 'SVOC',
    note: 'see + O + 分詞。crossing が C の SVOC。',
  },
  'I heard the baby crying in the next room.': {
    pattern: 'SVOC',
    note: 'hear + O + 分詞。crying が C の SVOC。',
  },

  // u25-l1 分詞形容詞 -ing / -ed
  'This puzzle game is really interesting once you understand the basic rules.': {
    pattern: 'SVC',
    note: 'be + 形容詞。主節で判定し SVC。',
  },
  "I'm interested in Japanese history, especially the period before the Meiji Restoration.": {
    pattern: 'SVC',
    note: 'be + 分詞形容詞 interested。in 句は数えず SVC。',
  },
  'The long flight was tiring, and everyone was tired.': {
    pattern: 'SVC',
    note: 'be + 分詞形容詞。前半の節で判定し SVC。',
  },
  'His explanation was so confusing that nobody dared to ask a follow up question.': {
    pattern: 'SVC',
    note: 'so ... that 構文でも be + 形容詞で SVC。',
  },
  'The test results were disappointing, but the teacher encouraged us to try again next month.': {
    pattern: 'SVC',
    note: '前の節が be + 形容詞の SVC。',
  },
  'The instructions were misleading, so several users were confused.': {
    pattern: 'SVC',
    note: 'be + 分詞形容詞。前の節で判定し SVC。',
  },
  'I was amazed by the detail in the painting, especially the reflections on the water.': {
    pattern: 'SVC',
    note: 'be + 分詞形容詞 amazed。by 句は数えず SVC。',
  },
  'Waiting several weeks for the final decision is exhausting for everyone involved.': {
    pattern: 'SVC',
    note: '動名詞が S。be + 形容詞で SVC。',
  },
  'The opening ceremony was surprisingly moving, and several guests were moved to tears.': {
    pattern: 'SVC',
    note: 'be + 分詞形容詞。前半の節で判定し SVC。',
  },
  'Reading the same instructions three times was frustrating for everyone in the workshop.': {
    pattern: 'SVC',
    note: '動名詞が S。be + 形容詞で SVC。',
  },
  'The lecture was boring.': {
    pattern: 'SVC',
    note: 'be + 分詞形容詞 boring。S = C の SVC。',
  },
  'The news was surprising.': {
    pattern: 'SVC',
    note: 'be + 分詞形容詞 surprising。S = C の SVC。',
  },
  'The students were bored.': {
    pattern: 'SVC',
    note: 'be + 分詞形容詞 bored。S = C の SVC。',
  },
  'We were surprised at the news.': {
    pattern: 'SVC',
    note: 'be + 分詞形容詞 surprised。at 句は数えず SVC。',
  },

  // u25-l2 分詞による後置修飾
  'The woman wearing a red coat near the ticket gate is my aunt from Sapporo.': {
    pattern: 'SVC',
    note: '分詞句は修飾語。is + 名詞で SVC。',
  },
  'Do you know the boy talking to the teacher outside the staff room right now?': {
    pattern: 'SVO',
    note: '疑問文を戻し know + O。分詞句は修飾語。',
  },
  'They live in a house built over a hundred years ago.': {
    pattern: 'SV',
    note: 'live は自動詞。場所句と分詞は数えず SV。',
  },
  'Most of the emails sent to this address during the night turn out to be spam.': {
    pattern: 'SVC',
    note: 'turn out to be ~。S = C の SVC。',
  },
  'There were many people waiting in line outside the store.': {
    pattern: 'SV',
    note: 'there is/are は SV。waiting は修飾語。',
  },
  'The woman speaking at the front is our new director.': {
    pattern: 'SVC',
    note: 'is + 名詞。分詞句は修飾語で SVC。',
  },
  'Please review the changes highlighted in yellow before you sign the final version.': {
    pattern: 'SVO',
    note: '命令文で You を補う。review + O の SVO。',
  },
  'Passengers traveling with small children may board first through the priority gate.': {
    pattern: 'SV',
    note: 'board は自動詞。分詞句は修飾語で SV。',
  },
  'The documents attached to this email explain the new procedure in detail.': {
    pattern: 'SVO',
    note: 'explain + O。過去分詞句は修飾語で SVO。',
  },
  'The team leading the investigation will publish its findings early next spring.': {
    pattern: 'SVO',
    note: 'publish + O。分詞句は修飾語で SVO。',
  },
  'The dog barking next door kept me awake.': {
    pattern: 'SVOC',
    note: 'keep + O + 形容詞。awake が C の SVOC。',
  },
  'The girl singing on stage is my cousin.': {
    pattern: 'SVC',
    note: 'is + 名詞。分詞句は修飾語で SVC。',
  },
  'The windows broken in the storm were replaced.': {
    pattern: 'SV',
    note: '受動態は be + 過去分詞で1動詞。SV。',
  },
  'I love the pictures taken by my grandfather.': {
    pattern: 'SVO',
    note: 'love + O。過去分詞句は修飾語で SVO。',
  },

  // u25-l3 分詞構文
  'Walking home along the riverside path, I saw an old friend from high school.': {
    pattern: 'SVO',
    note: '分詞構文は修飾語。saw + O の SVO。',
  },
  'Feeling tired after a long day of meetings, she went to bed much earlier than usual.': {
    pattern: 'SV',
    note: 'went to bed は自動詞。分詞構文は数えない。',
  },
  'Not knowing what to say to the grieving family, I just stayed silent for a while.': {
    pattern: 'SVC',
    note: 'stay + 形容詞。silent が C の SVC。',
  },
  'Seen from the plane, the island looks like a heart.': {
    pattern: 'SVC',
    note: 'look like ~ を補語とみなす SVC。',
  },
  'She sat by the window, listening to the rain.': {
    pattern: 'SV',
    note: 'sat は自動詞。by 句と分詞構文は数えず SV。',
  },
  'Not knowing the answer to the final question, I politely asked for more time.': {
    pattern: 'SV',
    note: 'ask for は自動詞用法。前置詞句は数えず SV。',
  },
  'Surrounded by mountains on all four sides, the village is difficult to reach in winter.': {
    pattern: 'SVC',
    note: 'be + 形容詞 difficult。分詞構文は数えず SVC。',
  },
  'Having completed the survey in three cities, we analyzed the results over two weeks.': {
    pattern: 'SVO',
    note: 'analyze + O。分詞構文は数えず SVO。',
  },
  'Having checked every entrance twice, the guard finally locked the main gate for the night.': {
    pattern: 'SVO',
    note: 'lock + O。分詞構文は数えず SVO。',
  },
  'Written in plain language, the new manual is far easier for beginners to follow.': {
    pattern: 'SVC',
    note: 'be + 形容詞 easier。分詞構文は数えず SVC。',
  },

  // u26-l1 It is said that / He is said to
  'It is said that this temple is over a thousand years old.': {
    pattern: 'SV',
    note: '受動態 It is said that ~。be + 過去分詞で SV。',
  },
  'He is said to be one of the best chefs in the city, though he never gives interviews.': {
    pattern: 'SV',
    note: 'is said は受動で1動詞。SV とみなす。',
  },
  'It is believed that the painting was stolen in the 1970s.': {
    pattern: 'SV',
    note: '受動態。be + 過去分詞で1動詞の SV。',
  },
  'The company is expected to announce a new product next week.': {
    pattern: 'SV',
    note: 'is expected が受動。1動詞で SV。',
  },
  'She is said to have lived in Paris when she was young.': {
    pattern: 'SV',
    note: 'is said to have lived で受動の SV。',
  },
  'It is believed that the painting is authentic, although no documents have survived.': {
    pattern: 'SV',
    note: '主節は It is believed の受動で SV。',
  },
  'The company is expected to announce the quarterly results tomorrow morning in Tokyo.': {
    pattern: 'SV',
    note: 'is expected が受動。1動詞で SV。',
  },
  'The hikers are reported to have reached the village safely.': {
    pattern: 'SV',
    note: 'are reported to have ~ の受動で SV。',
  },
  'It is reported that the new railway line will open ahead of the original schedule.': {
    pattern: 'SV',
    note: 'It is reported that ~。受動で SV。',
  },
  'The author is known to have written most of the novel while living abroad.': {
    pattern: 'SV',
    note: 'is known to have written。受動で SV。',
  },

  // u26-l2 受動の不定詞・動名詞
  'Everyone wants to be respected at work, regardless of age or job title.': {
    pattern: 'SVO',
    note: 'want + to不定詞。to be respected が O の SVO。',
  },
  'This form needs to be signed by a parent before the school trip next month.': {
    pattern: 'SVO',
    note: 'need + to不定詞。to be signed が O の SVO。',
  },
  'He hates being treated like a child, even though he is only nineteen.': {
    pattern: 'SVO',
    note: 'hate + 動名詞。being treated が O の SVO。',
  },
  'She left the office early without being noticed.': {
    pattern: 'SVO',
    note: 'leave + O。without 句は数えない SVO。',
  },
  'I remember being taken to this park by my father almost every Sunday when I was little.': {
    pattern: 'SVO',
    note: 'remember + 動名詞。being taken が O の SVO。',
  },
  'Every applicant wants to be treated fairly, whatever the outcome of the interview is.': {
    pattern: 'SVO',
    note: 'want + to不定詞。to be treated が O の SVO。',
  },
  'The actor left through a side door to avoid being recognized.': {
    pattern: 'SV',
    note: 'leave は自動詞。前置詞句は数えず SV。',
  },
  'She was proud to have been selected for the national team at the age of seventeen.': {
    pattern: 'SVC',
    note: 'be + 形容詞 proud。to不定詞は修飾で SVC。',
  },
  'All the equipment has to be checked carefully before the first performance on Friday.': {
    pattern: 'SV',
    note: 'has to be checked が受動の述部。SV とみなす。',
  },
  'Nobody enjoys being interrupted while explaining something complicated to a large audience.': {
    pattern: 'SVO',
    note: 'enjoy + 動名詞。being interrupted が O の SVO。',
  },
  'I want to invite them to the party.': {
    pattern: 'SVO',
    note: 'want + to不定詞。invite them で SVO。',
  },
  'She avoided answering the question.': {
    pattern: 'SVO',
    note: 'avoid + 動名詞。answering ... が O の SVO。',
  },
  'I want to be invited to the party.': {
    pattern: 'SVO',
    note: 'want + to be invited。受動の不定詞が O の SVO。',
  },
  'She avoided being asked about it.': {
    pattern: 'SVO',
    note: 'avoid + 動名詞。being asked が O の SVO。',
  },

  // u26-l3 get受動態と受動の慣用表現
  'The road is closed for repairs.': {
    pattern: 'SV',
    note: '受動態は be + 過去分詞で1動詞。SV。',
  },
  'This cheese is made in France.': {
    pattern: 'SV',
    note: 'is made の受動態。1動詞とみなし SV。',
  },
  'My bike got stolen last night.': {
    pattern: 'SV',
    note: 'get + 過去分詞の受動態。SV。',
  },
  'He got caught cheating on the test.': {
    pattern: 'SV',
    note: 'get + 過去分詞の受動態。SV。',
  },
  'Be careful not to get hurt when you are carrying those heavy boxes downstairs.': {
    pattern: 'SVC',
    note: '命令文で You を補う。be + 形容詞で SVC。',
  },
  'We get paid on the twenty-fifth of every month, or on the previous Friday if it falls on a weekend.': {
    pattern: 'SV',
    note: 'get + 過去分詞の受動態。SV。',
  },
  'They got married in a small wooden church in Nagano with only twelve guests.': {
    pattern: 'SV',
    note: 'get + 過去分詞の受動態。SV。',
  },
  'The meeting is supposed to start at ten, but the projector still is not working.': {
    pattern: 'SV',
    note: 'be supposed to ~ は受動表現。SV とみなす。',
  },
  'My grandfather was born in a small fishing town.': {
    pattern: 'SV',
    note: 'be born は受動表現。SV とみなす。',
  },
  'The hotel is located within walking distance of the station.': {
    pattern: 'SV',
    note: 'is located の受動態。SV とみなす。',
  },
  'Two windows on the north side got broken during the storm last Tuesday night.': {
    pattern: 'SV',
    note: 'get + 過去分詞の受動態。SV。',
  },
  'Maya got promoted to team leader after only six months with the company.': {
    pattern: 'SV',
    note: 'get + 過去分詞の受動態。SV。',
  },
  'The delivery was supposed to arrive before noon.': {
    pattern: 'SV',
    note: 'be supposed to ~ は受動表現。SV とみなす。',
  },
  'My bicycle got stolen from the station car park sometime last Wednesday afternoon.': {
    pattern: 'SV',
    note: 'get + 過去分詞の受動態。SV。',
  },

  // u27-l1 前置詞 + 関係代名詞
  'This is the small wooden house in which I grew up before we moved to Kobe.': {
    pattern: 'SVC',
    note: 'This is + 名詞。関係詞節は数えず SVC。',
  },
  'The person to whom you should send the report is Ms. Hayashi.': {
    pattern: 'SVC',
    note: '関係詞節は修飾語。is + 名詞で SVC。',
  },
  'The project on which we are working is almost finished.': {
    pattern: 'SVC',
    note: 'is + finished。関係詞節は数えず SVC。',
  },
  'She asked a question to which no one in the entire room knew the answer.': {
    pattern: 'SVO',
    note: 'ask + O。関係詞節は数えず SVO。',
  },
  'The company for which he works is based in Nagoya but has offices across Asia.': {
    pattern: 'SV',
    note: 'is based in は受動。前置詞句は数えず SV。',
  },
  'The person to whom you should speak is Ms. Evans.': {
    pattern: 'SVC',
    note: '関係詞節は修飾語。is + 名詞で SVC。',
  },
  'This is the process by which the data is encrypted before it leaves the server.': {
    pattern: 'SVC',
    note: '主節は This is the process。SVC。',
  },
  'The apartment we moved into last month needs quite a few repairs before winter.': {
    pattern: 'SVO',
    note: 'need + O。関係詞節は数えず SVO。',
  },
  'The conference at which she presented her research attracted specialists from twelve countries.': {
    pattern: 'SVO',
    note: 'attract + O。関係詞節は数えず SVO。',
  },
  'These are the colleagues with whom I shared an office for almost five years.': {
    pattern: 'SVC',
    note: 'These are + 名詞。関係詞節は数えず SVC。',
  },
  'This is the house I grew up in.': {
    pattern: 'SVC',
    note: 'This is + 名詞。関係詞節は数えず SVC。',
  },
  'The person you should talk to is the manager.': {
    pattern: 'SVC',
    note: '関係詞節は修飾語。is + 名詞で SVC。',
  },
  'This is the house in which I grew up.': {
    pattern: 'SVC',
    note: 'This is + 名詞。関係詞節は数えず SVC。',
  },
  'The person to whom you should talk is the manager.': {
    pattern: 'SVC',
    note: '関係詞節は修飾語。is + 名詞で SVC。',
  },

  // u27-l2 what / whatever / whoever
  'Everything that he said was true.': {
    pattern: 'SVC',
    note: 'that節は修飾語。S = Everything, C = true。',
  },
  'I believed the story that she told us.': {
    pattern: 'SVO',
    note: 'believe + O。that節は修飾語で SVO。',
  },
  'What he said was true.': {
    pattern: 'SVC',
    note: 'what節が S。C = true の SVC。',
  },
  'I believed what she told us.': {
    pattern: 'SVO',
    note: 'what節が O。believe は他動詞で SVO。',
  },
  'What I need right now is a strong cup of coffee and about twenty minutes of silence.': {
    pattern: 'SVC',
    note: 'what節が S。is + 名詞の SVC。',
  },
  'You can order whatever you like, because the company is paying for this dinner.': {
    pattern: 'SVO',
    note: 'order + 節(O)。複数節は主節で判定し SVO。',
  },
  'Whoever arrives first should unlock the office and turn on the air conditioning.': {
    pattern: 'SVO',
    note: 'whoever節が S。unlock + O の SVO。',
  },
  'Whatever happens, stay calm and follow the plan.': {
    pattern: 'SVC',
    note: '命令文で You を補う。stay + 形容詞で SVC。',
  },
  'You can sit wherever you like, but please leave the front row for the speakers.': {
    pattern: 'SV',
    note: 'sit は自動詞。wherever 節は数えず SV。',
  },
  'What the witness described in her statement matched the photograph almost exactly.': {
    pattern: 'SVO',
    note: 'what節が S。match + O の SVO。',
  },
  'You may choose whichever option suits your schedule.': {
    pattern: 'SVO',
    note: 'choose + whichever option(O) の SVO。',
  },
  'Whoever left this package at reception forgot to write a name or a phone number.': {
    pattern: 'SVO',
    note: 'whoever節が S。forgot + to不定詞の SVO。',
  },
  'Whatever the committee decides tonight, we will need to inform the staff by Monday.': {
    pattern: 'SVO',
    note: 'need + to不定詞。inform the staff で SVO。',
  },
  'What worries me most is the lack of a clear deadline for the second phase.': {
    pattern: 'SVC',
    note: 'what節が S。is + 名詞の SVC。',
  },

  // u27-l3 非制限用法の which(文全体を受ける)
  'My brother who lives in Osaka is a doctor.': {
    pattern: 'SVC',
    note: '関係詞節は修飾語。is + 名詞で SVC。',
  },
  'The students who had finished the test left the room.': {
    pattern: 'SVO',
    note: 'leave + O。関係詞節は数えず SVO。',
  },
  'My brother, who lives in Osaka, is a doctor.': {
    pattern: 'SVC',
    note: '非制限用法も修飾語。is + 名詞で SVC。',
  },
  'The students, who had finished the test, left the room.': {
    pattern: 'SVO',
    note: '非制限用法も修飾語。leave + O で SVO。',
  },
  'The train was delayed for two hours, which meant we missed the opening ceremony.': {
    pattern: 'SV',
    note: '受動態 was delayed で SV。which節は数えない。',
  },
  'She answered every question calmly, which impressed the interviewers.': {
    pattern: 'SVO',
    note: 'answer + O。which節は数えず SVO。',
  },
  "He didn't reply to any of my messages all day, which is very unusual for him.": {
    pattern: 'SV',
    note: 'reply to は自動詞用法。which節は数えず SV。',
  },
  'Our flight to Sapporo was canceled, which is why we ended up taking the night train.': {
    pattern: 'SV',
    note: '受動態 was canceled で SV。which節は数えない。',
  },
  'It rained heavily all weekend, which completely ruined our camping plans in the mountains.': {
    pattern: 'SV',
    note: 'rain は自動詞。which節は数えず SV。',
  },
  'The server went offline, which prevented us from saving our work.': {
    pattern: 'SVC',
    note: 'go + 形容詞 offline。S = C の SVC。',
  },
  "Riku remembered every single guest's name that evening, which greatly impressed the host.": {
    pattern: 'SVO',
    note: 'remember + O。which節は数えず SVO。',
  },
  'The committee changed the deadline again, which nobody had expected.': {
    pattern: 'SVO',
    note: 'change + O。which節は数えず SVO。',
  },
  'The supplier raised its prices without warning, which forced us to revise the whole budget.': {
    pattern: 'SVO',
    note: 'raise + O。which節は数えず SVO。',
  },
  'She speaks three languages fluently, which is why the company sent her to Singapore.': {
    pattern: 'SVO',
    note: 'speak + O。which節は数えず SVO。',
  },

  // u28-l1 逆接・譲歩 however / despite / although
  'The restaurant is expensive. However, the food is worth every yen.': {
    pattern: 'SVC',
    note: '二文とも be 動詞。S = C の SVC。',
  },
  'Although it was raining steadily all afternoon, the outdoor concert went ahead as planned.': {
    pattern: 'SV',
    note: 'go ahead は自動詞。although節は数えない。',
  },
  'Despite the heavy traffic on the expressway, we still arrived at the airport on time.': {
    pattern: 'SV',
    note: 'arrive at は自動詞用法。despite 句は数えず SV。',
  },
  'In spite of feeling sick all morning, she finished the presentation without a single mistake.': {
    pattern: 'SVO',
    note: 'finish + O。in spite of 句は数えず SVO。',
  },
  'Working from home saves time. On the other hand, it can feel lonely.': {
    pattern: 'SVO',
    note: '動名詞が S。saves time で SVO。後半は SVC。',
  },
  'Although demand increased, the company kept its prices unchanged.': {
    pattern: 'SVOC',
    note: 'keep + O + 形容詞。unchanged が C の SVOC。',
  },
  'Despite receiving several written complaints, the store changed nothing about its refund policy.': {
    pattern: 'SVO',
    note: 'change + nothing(O)。despite 句は数えず SVO。',
  },
  'The mountain route is about ten kilometres longer. However, it is much safer at night.': {
    pattern: 'SVC',
    note: '二文とも be + 形容詞。S = C の SVC。',
  },
  'Despite the short notice, almost every member of the committee attended the emergency meeting.': {
    pattern: 'SVO',
    note: 'attend + O。despite 句は数えず SVO。',
  },
  'The software is powerful and flexible. However, new users often find it confusing at first.': {
    pattern: 'SVC',
    note: '前半の be + 形容詞で SVC。後半の find は SVOC。',
  },
  'The plan sounded great. However, it had one serious problem.': {
    pattern: 'SVC',
    note: 'sound + 形容詞で SVC。後半の had は SVO。',
  },
  'The plan sounded great, but it had one serious problem.': {
    pattern: 'SVC',
    note: 'sound + 形容詞で SVC。後半の had は SVO。',
  },

  // u28-l2 因果・追加・例示 therefore / moreover / such as
  'The demand for the product doubled within three months. Therefore, we increased production at both factories.': {
    pattern: 'SV',
    note: 'double は自動詞。後半の increased は SVO。',
  },
  'The new model is noticeably lighter. Moreover, the battery lasts almost twice as long.': {
    pattern: 'SVC',
    note: '前半の be + 形容詞で SVC。後半の lasts は SV。',
  },
  'In addition to English, she speaks Portuguese and Korean well enough to work in both.': {
    pattern: 'SVO',
    note: 'speak + O。in addition to 句は数えず SVO。',
  },
  'I like winter sports such as skiing and snowboarding, but I have never tried skating.': {
    pattern: 'SVO',
    note: 'like + O、tried + O でどちらも SVO。',
  },
  'Some habits are hard to change. For example, I still check my phone before bed.': {
    pattern: 'SVC',
    note: '前半の be + 形容詞で SVC。後半は SVO。',
  },
  'It snowed heavily all night in the north. As a result, most of the morning trains were delayed.': {
    pattern: 'SV',
    note: 'snow は自動詞。後半の受動も SV。',
  },
  'The coastal road was flooded again. Therefore, all the buses were diverted through the hills.': {
    pattern: 'SV',
    note: '二文とも受動態。be + 過去分詞で SV。',
  },
  'The plan is affordable for a small town. Moreover, it can be implemented within a single year.': {
    pattern: 'SVC',
    note: '前半の be + 形容詞で SVC。後半は受動で SV。',
  },
  'For this bridge we need durable materials such as steel and reinforced concrete.': {
    pattern: 'SVO',
    note: 'need + O。such as 以下は例示で数えない。',
  },
  'The old boiler failed three times last winter. As a result, the school replaced it in March.': {
    pattern: 'SV',
    note: 'fail は自動詞。後半の replaced は SVO。',
  },
  'She enjoys quiet hobbies such as reading and knitting.': {
    pattern: 'SVO',
    note: 'enjoy + O。such as 以下は例示で数えない。',
  },
  'She enjoys quiet hobbies. For example, she reads and knits every evening.': {
    pattern: 'SVO',
    note: '前半の enjoy + O で SVO。後半は SV。',
  },

  // u28-l3 順序・要約・言い換え
  'First of all, let me thank everyone for coming here on such a cold morning.': {
    pattern: 'SVOC',
    note: 'let + O + 原形。thank が C の SVOC。',
  },
  'Chop the onions finely. Then add them to the hot pan with a little olive oil.': {
    pattern: 'SVO',
    note: '命令文で You を補う。chop / add とも SVO。',
  },
  'Finally, let the soup simmer gently for twenty minutes without putting the lid on.': {
    pattern: 'SVOC',
    note: 'let + O + 原形。simmer が C の SVOC。',
  },
  'The flight was delayed, the hotel lost our booking, and it rained all week. In short, the trip was a disaster.': {
    pattern: 'SV',
    note: '最初の節が受動で SV。後半のまとめは SVC。',
  },
  'The offer expires on Friday. In other words, you need to decide this week.': {
    pattern: 'SV',
    note: 'expire は自動詞。後半の need は SVO。',
  },
  'To sum up, the new system is faster, cheaper, and considerably easier for beginners to use.': {
    pattern: 'SVC',
    note: 'be + 形容詞。to sum up は副詞句で SVC。',
  },
  'First of all, we need to identify the source of the error.': {
    pattern: 'SVO',
    note: 'need + to不定詞。identify the source で SVO。',
  },
  'The device is not backward compatible. In other words, it will not work with older software.': {
    pattern: 'SVC',
    note: '前半の be + 形容詞で SVC。後半は SV。',
  },
  'In short, the benefits of the new procedure clearly outweigh the remaining risks.': {
    pattern: 'SVO',
    note: 'outweigh は他動詞。O を取る SVO。',
  },
  'At first the software felt slow, but it became much faster after the second update.': {
    pattern: 'SVC',
    note: 'feel + 形容詞で SVC。後半の became も SVC。',
  },
  'First, preheat the oven to 200 degrees.': {
    pattern: 'SVO',
    note: '命令文で You を補う。preheat + O の SVO。',
  },
  'First of all, I want to explain the schedule.': {
    pattern: 'SVO',
    note: 'want + to不定詞。explain the schedule で SVO。',
  },
  'At first, the job seemed boring, but now I love it.': {
    pattern: 'SVC',
    note: 'seem + 形容詞で SVC。後半の love は SVO。',
  },
}

export const b2aFocus: PatternFocusMap = {
  'u23-l1':
    'if節と主節で時のずれる混合条件文でも、文型は主節の動詞のあとに何が続くかで決まる。be + 名詞や形容詞なら SVC、live や進行形の自動詞なら SV になり、条件の if節は要素に数えない。',
  'u23-l2':
    '条件を表す provided that / on condition that などの節は要素に数えないので、判定は主節で行う。leave / work / agree のような自動詞は SV、send / explain / start のような他動詞は SVO になる。',
  'u23-l3':
    'would rather のあとに動詞原形が続けば SV か SVO、節が続けばその節を O とみなして SVO。It is time + S + 過去形は time が補語なので SVC となり、we left の部分は関係詞節として数えない。',
  'u24-l1':
    'have / get + O + 過去分詞は「O を〜してもらう・〜される」で、O と過去分詞の間に主述関係がある SVOC。I fixed my bike. のような能動の文は SVO で、視点の違いを文型の違いとして比べられる。',
  'u24-l2':
    'make / let / have + O + 原形と get + O + to不定詞は、どれも O と C が主述関係になる SVOC。同じ内容を受動態にすると be + 過去分詞を1動詞とみなすので、SV に変わる点も押さえたい。',
  'u24-l3':
    '知覚動詞も使役動詞と同じ SVOC。原形は行為の全体を、-ing は進行中の一場面を表すが、O + C の関係は変わらない。受動態の was seen to enter では be + 過去分詞が1動詞になり SV になる。',
  'u25-l1':
    'be + 分詞形容詞は補語を取る SVC。主語が「〜させる」側なら -ing、人や物が「〜させられる」側なら -ed を選び、補語が主語を説明する S = C の関係になる。前置詞句は要素に数えない。',
  'u25-l2':
    '分詞句は名詞を後ろから修飾するだけで、S / V / O / C のどれにもならない。数えるのは主節の要素だけなので、be + 名詞や形容詞なら SVC、他動詞なら SVO、受動態なら SV になる。',
  'u25-l3':
    '分詞構文は副詞句として文全体を修飾するので要素に数えない。判定はあとに残る主節で行い、be + 形容詞なら SVC、analyze / lock のような他動詞なら SVO、go to bed のような自動詞なら SV になる。',
  'u26-l1':
    'be + 過去分詞は1つの動詞とみなし、目的語を取らないので SV。It is said that ~ も He is said to ~ も同じで、that節や to不定詞、by句は要素に数えない。',
  'u26-l2':
    'to be 〜 / being 〜 は受動の準動詞で、動詞の目的語の席をそのまま占める。want / need / hate / avoid / remember / enjoy はどれも他動詞なので SVO になる。be proud to ~ のように形容詞が補語なら SVC。',
  'u26-l3':
    'get + 過去分詞も be + 過去分詞と同じ受動態で SV。be supposed to ~、be born、be located in ~ のような慣用表現も述部を1つの動詞としてとらえ、SV として扱う。',
  'u27-l1':
    '前置詞 + 関係代名詞の節は名詞を修飾するだけなので要素に数えない。This is the house ~ なら be + 名詞の SVC、ask / need / attract が残れば SVO、is based のような受動なら SV になる。',
  'u27-l2':
    'what / whatever / whoever の節は名詞の席(S / O / C)に入るので1要素として数える。S なら SVC や SVO、O なら SVO になる。一方 that 節が名詞を修飾するだけのときは数えない。',
  'u27-l3':
    '関係詞節は制限用法でも非制限用法でも修飾語なので要素に数えない。文全体を受ける which 節も同じで、判定は主節だけを見て、be + 名詞の SVC、leave / answer / change などの SVO、受動の SV とする。',
  'u28-l1':
    'although 節や despite / in spite of の句は譲歩を表す副詞要素なので数えない。文が二つ並ぶ場合も、話題を提示する先の文で文型を判定する。keep + O + 形容詞や sound + 形容詞にも注目したい。',
  'u28-l2':
    'therefore / moreover / for example などは文と文の関係を示す標識で、文型には影響しない。such as の例示は名詞句の一部なので数えず、二文あるときは先に出た文の動詞で判定する。',
  'u28-l3':
    '接続副詞は前後の文の関係を示すだけで要素にはならない。let + O + 原形は SVOC、命令文は You を補って SVO、まとめの文は be + 形容詞や名詞の SVC と、それぞれもとの形に戻して判定する。',
}
