import type { PatternFocusMap, PatternMap } from './types.ts'

// B1(U11–U16)の文型データ。例文の英文をそのままキーにする。

export const b1Patterns: PatternMap = {
  // u11-l1 現在完了の基本概念
  'I have lost my key.': { pattern: 'SVO', note: 'my key が目的語の SVO。' },
  'She has broken her arm.': { pattern: 'SVO', note: 'her arm が目的語の SVO。' },
  'We have sold our car.': { pattern: 'SVO', note: 'our car が目的語の SVO。' },
  "The bus hasn't arrived.": { pattern: 'SV', note: 'arrive は目的語を取らない SV。' },
  'Have you seen my glasses?': { pattern: 'SVO', note: '平叙文 You have seen my glasses. の SVO。' },
  'The rain has stopped, so we can go outside now.': { pattern: 'SV', note: '主節 go outside は目的語なしの SV。' },
  'Have you seen my glasses anywhere?': { pattern: 'SVO', note: '平叙文 You have seen my glasses. の SVO。' },
  "I haven't finished this chapter yet.": { pattern: 'SVO', note: 'this chapter が目的語の SVO。' },
  'They have moved to a bigger apartment.': { pattern: 'SV', note: 'move は自動詞で to 句は副詞の SV。' },
  'Has the delivery arrived at the office?': { pattern: 'SV', note: 'arrive は自動詞。at 句は副詞の SV。' },

  // u11-l2 経験を表す現在完了
  'I have visited Kyoto three times.': { pattern: 'SVO', note: 'Kyoto が目的語の SVO。回数は数えない。' },
  'Have you ever tried natto?': { pattern: 'SVO', note: '平叙文 You have tried natto. の SVO。' },
  'She has never driven a car.': { pattern: 'SVO', note: 'a car が目的語の SVO。' },
  'I have seen this movie before.': { pattern: 'SVO', note: 'this movie が目的語の SVO。' },
  'We have been to that restaurant once.': { pattern: 'SV', note: 'be + 場所は SV。to 句は数えない。' },
  'My parents have never traveled abroad.': { pattern: 'SV', note: 'travel は自動詞で abroad は副詞の SV。' },
  'Have you ever ridden a horse?': { pattern: 'SVO', note: '平叙文 You have ridden a horse. の SVO。' },
  'I have been to Singapore three times.': { pattern: 'SV', note: 'be + 場所は SV。回数は数えない。' },
  'My parents have never seen snow.': { pattern: 'SVO', note: 'snow が目的語の SVO。' },
  'She has never eaten Indian food before.': { pattern: 'SVO', note: 'Indian food が目的語の SVO。' },

  // u11-l3 継続を表す現在完了
  'I have lived in Tokyo for three years.': { pattern: 'SV', note: 'live は自動詞。in 句は副詞の SV。' },
  'She has worked at this hospital since 2021.': { pattern: 'SV', note: 'work は自動詞。at 句は副詞の SV。' },
  'We have known each other since we were in high school.': { pattern: 'SVO', note: '主節は each other を目的語に取る SVO。' },
  "I haven't seen him for a month.": { pattern: 'SVO', note: 'him が目的語の SVO。' },
  'How long have you had that phone?': { pattern: 'SVO', note: '平叙文 You have had that phone. の SVO。' },
  'We have owned this house for twelve years.': { pattern: 'SVO', note: 'this house が目的語の SVO。' },
  'Sara has known him since elementary school.': { pattern: 'SVO', note: 'him が目的語の SVO。' },
  'How long have you been a member of this club?': { pattern: 'SVC', note: 'be + a member で主語を説明する SVC。' },
  'My uncle has taught at that school for twenty years.': { pattern: 'SV', note: 'teach は目的語なし。at 句は副詞の SV。' },
  'They have been friends since their first year of college.': { pattern: 'SVC', note: 'be + friends で主語を説明する SVC。' },

  // u11-l4 完了・結果を表す現在完了
  'I have just finished my homework.': { pattern: 'SVO', note: 'my homework が目的語の SVO。' },
  'The train has just left.': { pattern: 'SV', note: 'leave は目的語を取らない SV。' },
  'She has already eaten lunch.': { pattern: 'SVO', note: 'lunch が目的語の SVO。' },
  "I haven't sent the email yet.": { pattern: 'SVO', note: 'the email が目的語の SVO。' },
  'Have you packed your bag yet?': { pattern: 'SVO', note: '平叙文 You have packed your bag. の SVO。' },
  'The guests have just arrived.': { pattern: 'SV', note: 'arrive は自動詞の SV。' },
  'I have already sent the invoice.': { pattern: 'SVO', note: 'the invoice が目的語の SVO。' },
  'Have the repairs finished yet?': { pattern: 'SV', note: '平叙文 The repairs have finished. の SV。' },
  'We have already booked a table for six.': { pattern: 'SVO', note: 'a table が目的語の SVO。' },
  'The manager has just approved my request.': { pattern: 'SVO', note: 'my request が目的語の SVO。' },

  // u11-l5 現在完了 vs 過去形
  'I lost my key yesterday.': { pattern: 'SVO', note: 'my key が目的語の SVO。' },
  'She lived in Paris for two years.': { pattern: 'SV', note: 'live は自動詞。in 句は副詞の SV。' },
  'When did you buy that bike?': { pattern: 'SVO', note: '平叙文 You bought that bike. の SVO。' },
  'She has lived in Paris for two years.': { pattern: 'SV', note: 'live は自動詞で in 句は副詞の SV。' },
  'How long have you had that bike?': { pattern: 'SVO', note: '平叙文 You have had that bike. の SVO。' },
  'I saw that movie last weekend.': { pattern: 'SVO', note: 'that movie が目的語の SVO。' },
  'I have seen that movie three times.': { pattern: 'SVO', note: 'that movie が目的語の SVO。' },
  'My grandfather worked at a bank for 40 years.': { pattern: 'SV', note: 'work は自動詞。at 句は副詞の SV。' },
  'Emi has worked at the bank since April.': { pattern: 'SV', note: 'work は自動詞。at 句は副詞の SV。' },
  'When did you arrive in Japan?': { pattern: 'SV', note: '平叙文 You arrived in Japan. の SV。' },
  'I have lost my key, so I cannot open the door.': { pattern: 'SVO', note: '主節 I cannot open the door の SVO。' },
  'I dropped it on the bus this morning.': { pattern: 'SVO', note: 'it が目的語の SVO。' },
  'Did you call Maya yesterday?': { pattern: 'SVO', note: '平叙文 You called Maya. の SVO。' },
  'I finished the report an hour ago.': { pattern: 'SVO', note: 'the report が目的語の SVO。' },
  'She has finished the report, so we can send it now.': { pattern: 'SVO', note: '主節 we can send it now の SVO。' },

  // u11-l6 現在完了 総合練習
  'I have never eaten oysters.': { pattern: 'SVO', note: 'oysters が目的語の SVO。' },
  'We have been busy since Monday.': { pattern: 'SVC', note: 'be + busy が主語を説明する SVC。' },
  'She has already booked the tickets.': { pattern: 'SVO', note: 'the tickets が目的語の SVO。' },
  'Have you two met before?': { pattern: 'SV', note: '平叙文 You two have met. の SV。' },
  "My phone has died, so I can't check the map.": { pattern: 'SVO', note: '主節 check the map を目的語に取る SVO。' },
  'Our team has won five games this season.': { pattern: 'SVO', note: 'five games が目的語の SVO。' },
  'She has worked at the clinic since she graduated.': { pattern: 'SV', note: '主節 work は自動詞。at 句は副詞の SV。' },
  "We haven't received a reply yet.": { pattern: 'SVO', note: 'a reply が目的語の SVO。' },
  'Have you ever worked with this software before?': { pattern: 'SV', note: 'work は自動詞。with 句は副詞の SV。' },
  'The store has been closed since the typhoon.': { pattern: 'SV', note: 'be closed は受動態。目的語なしの SV。' },

  // u12-l1 現在進行形で表す予定
  'I am meeting Emi for lunch tomorrow.': { pattern: 'SVO', note: 'Emi が目的語の SVO。' },
  'We are flying to Okinawa next Friday.': { pattern: 'SV', note: 'fly は自動詞。to 句は副詞の SV。' },
  'She is seeing the dentist at three.': { pattern: 'SVO', note: 'the dentist が目的語の SVO。' },
  'What are you doing this weekend?': { pattern: 'SVO', note: '平叙文 You are doing what. の SVO。' },
  'I am not working next Monday.': { pattern: 'SV', note: 'work は目的語を取らない SV。' },
  'I am meeting the dentist at three tomorrow.': { pattern: 'SVO', note: 'the dentist が目的語の SVO。' },
  'We are flying to Fukuoka on Friday morning.': { pattern: 'SV', note: 'fly は自動詞。to 句は副詞の SV。' },
  'What are you doing after work?': { pattern: 'SVO', note: '平叙文 You are doing what. の SVO。' },
  'They are moving into the new office next month.': { pattern: 'SV', note: 'move は自動詞。into 句は副詞の SV。' },
  'I am taking my parents to the airport tonight.': { pattern: 'SVO', note: 'my parents が目的語の SVO。' },

  // u12-l2 will vs be going to vs 現在進行形
  "The phone is ringing. I'll get it.": { pattern: 'SVO', note: '後半の get it が目的語を取る SVO。' },
  "I'll have the salmon, please.": { pattern: 'SVO', note: 'the salmon が目的語の SVO。' },
  "I'm going to sell my car. I decided last month.": { pattern: 'SVO', note: '前半の sell my car が目的語を取る SVO。' },
  "We're going to visit my parents this summer.": { pattern: 'SVO', note: 'my parents が目的語の SVO。' },
  "It's hot in here. I'll open the window.": { pattern: 'SVO', note: '後半の open the window が SVO。' },
  "I'm going to start jogging next month.": { pattern: 'SVO', note: 'jogging を目的語に取る SVO。' },
  "I'm playing tennis with Aya on Sunday.": { pattern: 'SVO', note: 'tennis が目的語の SVO。' },
  'I think our team will win.': { pattern: 'SVO', note: 'that 節を目的語に取る SVO。' },
  "Slow down! We're going to miss the exit.": { pattern: 'SVO', note: '後半の miss the exit が SVO。' },
  'I forgot to call Leo. I will do it now.': { pattern: 'SVO', note: '後半の I will do it now が SVO。' },
  'We are going to replace the old computer.': { pattern: 'SVO', note: 'the old computer が目的語の SVO。' },
  'The technician is coming at ten on Tuesday.': { pattern: 'SV', note: 'come は自動詞。at 句は副詞の SV。' },
  'The phone is ringing. I will get it.': { pattern: 'SVO', note: '後半の I will get it が SVO。' },
  'We are having dinner with the client on Thursday.': { pattern: 'SVO', note: 'dinner が目的語の SVO。' },

  // u12-l3 時・条件の副詞節と未来
  'When he arrives, I will call you.': { pattern: 'SVO', note: '主節 I will call you の SVO。' },
  "If it rains tomorrow, we'll cancel the picnic.": { pattern: 'SVO', note: '主節 cancel the picnic の SVO。' },
  "I'll wait here until the store opens.": { pattern: 'SV', note: '主節 I will wait here の SV。' },
  "As soon as I get home, I'm going to take a shower.": { pattern: 'SVO', note: '主節の take a shower が SVO。' },
  'Before you leave, please turn off the lights.': { pattern: 'SVO', note: '命令文。the lights を目的語に取る SVO。' },
  'I will lock the door before I leave.': { pattern: 'SVO', note: '主節の lock the door が SVO。' },
  'If the weather improves, we will eat outside.': { pattern: 'SV', note: '主節 eat は自動詞の SV。' },
  'I do not know when the results will arrive.': { pattern: 'SVO', note: 'wh 節を目的語に取る SVO。' },
  'Call me when you get to the hotel.': { pattern: 'SVO', note: '命令文。me が目的語の SVO。' },
  'We will start as soon as everyone is ready.': { pattern: 'SV', note: '主節 start は自動詞の SV。' },

  // u13-l1 受動態の基本(現在・過去)
  'This temple was built in 1603.': { pattern: 'SV', note: '受動態 be built を1動詞とみなす SV。' },
  'These cookies are made with rice flour.': { pattern: 'SV', note: '受動態 are made の SV。' },
  'The song was written by a high school student.': { pattern: 'SV', note: '受動態。by 句は数えない SV。' },
  "The office isn't cleaned on weekends.": { pattern: 'SV', note: '受動態の否定。目的語なしの SV。' },
  'Was this photo taken in Okinawa?': { pattern: 'SV', note: '受動態の疑問文。平叙文に戻して SV。' },
  'These rooms are cleaned every morning.': { pattern: 'SV', note: '受動態 are cleaned の SV。' },
  'The bridge was damaged in the storm.': { pattern: 'SV', note: '受動態 was damaged の SV。' },
  'Was this photograph taken in Hokkaido?': { pattern: 'SV', note: '受動態の疑問文。平叙文に戻して SV。' },
  'These vegetables are grown on a local farm.': { pattern: 'SV', note: '受動態 are grown の SV。' },
  'The windows were washed last Thursday.': { pattern: 'SV', note: '受動態 were washed の SV。' },

  // u13-l2 by句と行為者の省略
  'My passport was stolen during the trip.': { pattern: 'SV', note: '受動態。during 句は副詞で SV。' },
  'The game was canceled because of the rain.': { pattern: 'SV', note: '受動態。because of 句は数えない SV。' },
  'This portrait was painted by Picasso.': { pattern: 'SV', note: '受動態。by 句は数えない SV。' },
  'The winning goal was scored by a sixteen-year-old.': { pattern: 'SV', note: '受動態。by 句は数えない SV。' },
  'I was invited to the wedding.': { pattern: 'SV', note: '受動態 was invited の SV。' },
  'Portuguese is spoken in Brazil.': { pattern: 'SV', note: '受動態 is spoken の SV。' },
  'This bridge was designed by a French engineer.': { pattern: 'SV', note: '受動態。by 句は数えない SV。' },
  'The meeting room is cleaned every morning.': { pattern: 'SV', note: '受動態 is cleaned の SV。' },
  'The missing child was found early this morning.': { pattern: 'SV', note: '受動態 was found の SV。' },
  'The mural was painted by local high school students.': { pattern: 'SV', note: '受動態。by 句は数えない SV。' },
  'The package was opened with a small knife.': { pattern: 'SV', note: '受動態。with 句は数えない SV。' },
  'Our flight was delayed for three hours.': { pattern: 'SV', note: '受動態 was delayed の SV。' },
  'This novel was translated by a famous poet.': { pattern: 'SV', note: '受動態。by 句は数えない SV。' },

  // u13-l3 助動詞・未来・完了の受動態
  'The results will be announced tomorrow morning.': { pattern: 'SV', note: 'will be announced を1動詞とみなす SV。' },
  'This medicine must be kept in the refrigerator.': { pattern: 'SV', note: 'must be kept を1動詞とみなす SV。' },
  "Smartphones can't be used during the exam.": { pattern: 'SV', note: 'can be used の受動態で SV。' },
  'The meeting has been moved to Friday.': { pattern: 'SV', note: 'has been moved を1動詞とみなす SV。' },
  'A new bridge is going to be built here.': { pattern: 'SV', note: 'is going to be built の受動態で SV。' },
  'My order has just been shipped.': { pattern: 'SV', note: 'has been shipped の受動態で SV。' },
  'The final decision will be announced tomorrow.': { pattern: 'SV', note: 'will be announced の受動態で SV。' },
  'All applications must be submitted online.': { pattern: 'SV', note: 'must be submitted の受動態で SV。' },
  'The broken elevator has already been repaired.': { pattern: 'SV', note: 'has been repaired の受動態で SV。' },
  'The road can be closed during heavy snow.': { pattern: 'SV', note: 'can be closed の受動態で SV。' },

  // u13-l4 受動態を使う場面
  'Kenta broke the window.': { pattern: 'SVO', note: 'the window が目的語の SVO。' },
  'I made this cake myself.': { pattern: 'SVO', note: 'this cake が目的語の SVO。' },
  'The window was broken during the night.': { pattern: 'SV', note: '受動態 was broken の SV。' },
  'This cake is sold only in Kyoto.': { pattern: 'SV', note: '受動態 is sold の SV。' },
  'The new stadium will be completed in 2027.': { pattern: 'SV', note: 'will be completed の受動態で SV。' },
  'The suspect was arrested on Tuesday morning.': { pattern: 'SV', note: '受動態 was arrested の SV。' },
  'Your order has been shipped.': { pattern: 'SV', note: 'has been shipped の受動態で SV。' },
  'The data was collected over six months.': { pattern: 'SV', note: '受動態 was collected の SV。' },
  'The museum opened a new gallery last month.': { pattern: 'SVO', note: 'a new gallery が目的語の SVO。' },
  'The new gallery was opened last month.': { pattern: 'SV', note: '受動態 was opened の SV。' },
  'The samples are stored at a constant temperature.': { pattern: 'SV', note: '受動態 are stored の SV。' },
  'The bridge was inspected by city engineers last week.': { pattern: 'SV', note: '受動態。by 句は数えない SV。' },
  'Our proposal has been accepted by the committee.': { pattern: 'SV', note: '受動態。by 句は数えない SV。' },
  'The city built a new library near the river.': { pattern: 'SVO', note: 'a new library が目的語の SVO。' },

  // u14-l1 主格の関係代名詞 who/which/that
  'I have a friend who lives in Canada.': { pattern: 'SVO', note: '関係詞節を除くと have a friend の SVO。' },
  'The bus that goes to the airport leaves every twenty minutes.': { pattern: 'SV', note: '関係詞節を除くと leaves の SV。' },
  'Do you know anyone who can speak Chinese?': { pattern: 'SVO', note: '平叙文 You know anyone. の SVO。' },
  'I want a phone which has a better camera.': { pattern: 'SVO', note: 'a phone が目的語の SVO。' },
  'The people who live next door are very friendly.': { pattern: 'SVC', note: 'be + friendly の SVC。関係詞節は数えない。' },
  'I know a mechanic who repairs electric cars.': { pattern: 'SVO', note: 'a mechanic が目的語の SVO。' },
  'The app that tracks my expenses is free.': { pattern: 'SVC', note: 'be + free の SVC。関係詞節は数えない。' },
  'Students who arrive late must sign in.': { pattern: 'SV', note: 'sign in は自動詞の SV。' },
  'The company that makes these bicycles is based in Osaka.': { pattern: 'SV', note: 'be based in を1動詞とみなす SV。' },
  'We hired an editor who has worked on medical journals.': { pattern: 'SVO', note: 'an editor が目的語の SVO。' },

  // u14-l2 目的格の関係代名詞と省略
  'The man who called you is my boss.': { pattern: 'SVC', note: 'be + my boss の SVC。関係詞節は数えない。' },
  'I like songs that make me happy.': { pattern: 'SVO', note: 'songs が目的語の SVO。関係詞節は数えない。' },
  'The man you met yesterday is my boss.': { pattern: 'SVC', note: 'be + my boss の SVC。' },
  'This is the best pizza I have ever eaten.': { pattern: 'SVC', note: 'This = the best pizza の SVC。' },
  'The movie that we watched last night was really good.': { pattern: 'SVC', note: 'be + good の SVC。関係詞節は数えない。' },
  'The cake she made was delicious.': { pattern: 'SVC', note: 'be + delicious の SVC。' },
  'Is this the umbrella you were looking for?': { pattern: 'SVC', note: '平叙文 This is the umbrella. の SVC。' },
  'He is a person everyone trusts.': { pattern: 'SVC', note: 'be + a person の SVC。' },
  'The shoes which I ordered online were too small.': { pattern: 'SVC', note: 'be + too small の SVC。' },
  'The movie we watched last night was excellent.': { pattern: 'SVC', note: 'be + excellent の SVC。' },
  'Is this the document that you need?': { pattern: 'SVC', note: '平叙文 This is the document. の SVC。' },
  'The colleague I sit next to is from Canada.': { pattern: 'SV', note: 'be from は前置詞句を伴う SV。' },
  'The songs my father loved are still popular today.': { pattern: 'SVC', note: 'be + popular の SVC。' },
  'This is the recipe that my grandmother taught me.': { pattern: 'SVC', note: 'This = the recipe の SVC。' },

  // u14-l3 whose / where / when
  'I have a friend whose father is a chef.': { pattern: 'SVO', note: 'whose 節を除くと have a friend の SVO。' },
  'She is the writer whose books sell millions of copies.': { pattern: 'SVC', note: 'be + the writer の SVC。' },
  'This is the town where I grew up.': { pattern: 'SVC', note: 'This = the town の SVC。' },
  'We stayed at a hotel where you can see the ocean from every room.': { pattern: 'SV', note: 'stay は自動詞。at 句は副詞の SV。' },
  'Do you remember the day when we first met?': { pattern: 'SVO', note: '平叙文 You remember the day. の SVO。' },
  'Winter is the season when this town is at its best.': { pattern: 'SVC', note: 'Winter = the season の SVC。' },
  'We met a chef whose restaurant has won several awards.': { pattern: 'SVO', note: 'a chef が目的語の SVO。' },
  'This is the park where my parents first met.': { pattern: 'SVC', note: 'This = the park の SVC。' },
  'I remember the day when our puppy came home.': { pattern: 'SVO', note: 'the day が目的語の SVO。' },
  'I work with a designer whose office is in Kobe.': { pattern: 'SV', note: 'work with は自動詞の SV。' },
  'This is a restaurant which serves great sushi.': { pattern: 'SVC', note: 'This = a restaurant の SVC。' },
  'This is the restaurant where we had our wedding party.': { pattern: 'SVC', note: 'This = the restaurant の SVC。' },

  // u14-l4 制限用法と非制限用法
  'My brother who lives in Osaka is a doctor.': { pattern: 'SVC', note: 'be + a doctor の SVC。関係詞節は数えない。' },
  'My brother, who lives in Osaka, is a doctor.': { pattern: 'SVC', note: '非制限用法でも主節は be + a doctor の SVC。' },
  'Kyoto, which was the capital of Japan for over a thousand years, attracts millions of tourists.': { pattern: 'SVO', note: '主節 attracts millions of tourists の SVO。' },
  'My mother, who is seventy, still works in her garden.': { pattern: 'SV', note: '主節 work は自動詞の SV。' },
  'The students who handed in their homework late lost points.': { pattern: 'SVO', note: 'lost points の SVO。関係詞節は数えない。' },
  'Mr. Ito, who teaches us math, is retiring next month.': { pattern: 'SV', note: 'retire は目的語を取らない SV。' },
  'The train was delayed again, which made everyone angry.': { pattern: 'SV', note: '主節の受動態 was delayed の SV。' },
  'Employees who work remotely join the meeting online.': { pattern: 'SVO', note: 'the meeting が目的語の SVO。' },
  'My brother, who works remotely, lives in Nagano.': { pattern: 'SV', note: '主節 live は自動詞の SV。' },
  'The library, which was renovated last year, is very bright.': { pattern: 'SVC', note: 'be + bright の SVC。' },
  'Our new manager, who joined in April, speaks three languages.': { pattern: 'SVO', note: 'three languages が目的語の SVO。' },
  'The report that we submitted yesterday needs one correction.': { pattern: 'SVO', note: 'one correction が目的語の SVO。' },

  // u14-l5 関係詞 総合練習
  'This is the factory that makes car parts.': { pattern: 'SVC', note: 'This = the factory の SVC。' },
  'The restaurant that we chose was very quiet.': { pattern: 'SVC', note: 'be + quiet の SVC。' },
  'This is the factory where my father works.': { pattern: 'SVC', note: 'This = the factory の SVC。' },
  'The restaurant where we had lunch was very quiet.': { pattern: 'SVC', note: 'be + quiet の SVC。' },
  'The woman who designed this building won an international prize.': { pattern: 'SVO', note: 'an international prize が目的語の SVO。' },
  'Is there anything I can do to help?': { pattern: 'SV', note: 'there is 構文は SV。' },
  'We visited the village where my grandfather was born.': { pattern: 'SVO', note: 'the village が目的語の SVO。' },
  'I have a coworker whose desk is always perfectly clean.': { pattern: 'SVO', note: 'have a coworker の SVO。' },
  'The cafe, which opened only last month, is already popular.': { pattern: 'SVC', note: 'be + popular の SVC。' },
  'The hotel that we booked has a view of the lake.': { pattern: 'SVO', note: 'a view が目的語の SVO。' },
  'The hotel where we stayed had a view of the lake.': { pattern: 'SVO', note: 'a view が目的語の SVO。' },
  'Mr. Hall, whose daughter is in my class, teaches science.': { pattern: 'SVO', note: 'science が目的語の SVO。' },
  'The engineer whose team built this system now works abroad.': { pattern: 'SV', note: '主節 work は自動詞の SV。' },
  'Tuesday is the day when our department holds its weekly meeting.': { pattern: 'SVC', note: 'Tuesday = the day の SVC。' },

  // u15-l1 ゼロ条件文と第1条件文
  'If you press this button, the door opens.': { pattern: 'SV', note: '主節 the door opens は目的語なしの SV。' },
  "If I drink coffee at night, I can't sleep.": { pattern: 'SV', note: '主節 I cannot sleep の SV。' },
  'If it snows tonight, the roads will be dangerous.': { pattern: 'SVC', note: '主節は be + dangerous の SVC。' },
  "If you hurry, you'll catch the bus.": { pattern: 'SVO', note: '主節 catch the bus の SVO。' },
  'If you heat ice, it melts.': { pattern: 'SV', note: '主節 it melts は自動詞の SV。' },
  'If I miss the last train, I take a taxi.': { pattern: 'SVO', note: '主節 take a taxi の SVO。' },
  'If it rains tomorrow, we will cancel the barbecue.': { pattern: 'SVO', note: '主節 cancel the barbecue の SVO。' },
  "If you don't leave now, you'll miss your flight.": { pattern: 'SVO', note: '主節 miss your flight の SVO。' },
  'I will call you if the package arrives.': { pattern: 'SVO', note: '主節 I will call you の SVO。' },
  'If you mix blue and yellow, you get green.': { pattern: 'SVC', note: '主節の get + green は SVC。' },
  'If the train is delayed, I will send you a message.': { pattern: 'SVOO', note: '主節は you と a message を取る SVOO。' },
  'Call me if you need any help.': { pattern: 'SVO', note: '命令文。call me の SVO。' },
  'If you press this button, the machine stops immediately.': { pattern: 'SV', note: '主節 the machine stops の SV。' },
  'If the meeting finishes early, we can catch the express.': { pattern: 'SVO', note: '主節 catch the express の SVO。' },

  // u15-l2 第2条件文
  'If I have time tomorrow, I will clean my room.': { pattern: 'SVO', note: '主節 clean my room の SVO。' },
  'If she studies hard, she will pass the exam.': { pattern: 'SVO', note: '主節 pass the exam の SVO。' },
  'If I had time, I would clean my room.': { pattern: 'SVO', note: '主節 clean my room の SVO。' },
  'If I were a bird, I would fly to you.': { pattern: 'SV', note: '主節 fly は自動詞の SV。' },
  'If I had more money, I would travel around the world.': { pattern: 'SV', note: '主節 travel は自動詞の SV。' },
  'If I were you, I would see a doctor.': { pattern: 'SVO', note: '主節 see a doctor の SVO。' },
  'If we lived closer, we would see each other more often.': { pattern: 'SVO', note: '主節 see each other の SVO。' },
  "She would be happier if she didn't work so much.": { pattern: 'SVC', note: '主節 be + happier の SVC。' },
  'If I could speak Chinese, I would work in Shanghai.': { pattern: 'SV', note: '主節 work は自動詞の SV。' },
  'If I lived closer, I would visit more often.': { pattern: 'SV', note: '主節 visit は目的語を取らない SV。' },
  'What would you do if you found a wallet?': { pattern: 'SVO', note: '平叙文 You would do what. の SVO。' },
  'If I were you, I would keep a copy of the receipt.': { pattern: 'SVO', note: '主節 keep a copy の SVO。' },
  'If she had a car, she would drive to the coast every weekend.': { pattern: 'SV', note: '主節 drive は自動詞の SV。' },
  'I would take the job if the office were closer to my home.': { pattern: 'SVO', note: '主節 take the job の SVO。' },

  // u15-l3 unless / in case / as long as
  "I'll call a taxi if it rains.": { pattern: 'SVO', note: '主節 call a taxi の SVO。' },
  "I'll take medicine if I feel sick.": { pattern: 'SVO', note: '主節 take medicine の SVO。' },
  "I'll take some cash in case the shop doesn't accept cards.": { pattern: 'SVO', note: '主節 take some cash の SVO。' },
  'Take some medicine in case you feel sick.': { pattern: 'SVO', note: '命令文。take some medicine の SVO。' },
  "Unless you have a ticket, you can't get in.": { pattern: 'SV', note: '主節 get in は自動詞の SV。' },
  "I won't go unless you come with me.": { pattern: 'SV', note: '主節 go は目的語を取らない SV。' },
  "You'll be fine as long as you follow the instructions.": { pattern: 'SVC', note: '主節 be + fine の SVC。' },
  'We can sit outside as long as it stays warm.': { pattern: 'SV', note: '主節 sit は自動詞の SV。' },
  'Write down the address in case you forget it.': { pattern: 'SVO', note: '命令文。the address を目的語に取る SVO。' },
  'We will miss the bus unless we leave now.': { pattern: 'SVO', note: '主節 miss the bus の SVO。' },
  'You can use my desk as long as you keep it tidy.': { pattern: 'SVO', note: '主節 use my desk の SVO。' },
  'Write down the address in case your phone loses its signal.': { pattern: 'SVO', note: '命令文。the address を目的語に取る SVO。' },
  'Take a jacket in case the temperature drops tonight.': { pattern: 'SVO', note: '命令文。take a jacket の SVO。' },
  'Unless the weather changes, the ferry will leave on time.': { pattern: 'SV', note: '主節 leave は自動詞の SV。' },

  // u15-l4 条件文 練習(1型 vs 2型)
  'If I get the job, I will move to Nagoya.': { pattern: 'SV', note: '主節 move は自動詞の SV。' },
  'If the bus is late, we will take the train.': { pattern: 'SVO', note: '主節 take the train の SVO。' },
  'If I got a job like that, I would move anywhere.': { pattern: 'SV', note: '主節 move は自動詞の SV。' },
  'If I were the mayor, I would build more parks.': { pattern: 'SVO', note: '主節 build more parks の SVO。' },
  'If it snows tonight, the trains will probably stop.': { pattern: 'SV', note: '主節 stop は自動詞の SV。' },
  'If I won the lottery, I would quit my job.': { pattern: 'SVO', note: '主節 quit my job の SVO。' },
  "If you leave now, you'll be home by nine.": { pattern: 'SV', note: '主節の be + home は場所を表す SV。' },
  'If I knew her number, I would call her right now.': { pattern: 'SVO', note: '主節 call her の SVO。' },
  'If our apartment had a balcony, we would grow vegetables.': { pattern: 'SVO', note: '主節 grow vegetables の SVO。' },
  'If our budget is approved, we will start in April.': { pattern: 'SV', note: '主節 start は自動詞の SV。' },
  'If our office were larger, we would add a meeting room.': { pattern: 'SVO', note: '主節 add a meeting room の SVO。' },
  'I would accept the offer if it included remote work.': { pattern: 'SVO', note: '主節 accept the offer の SVO。' },
  'If the client agrees, we will sign the contract on Monday.': { pattern: 'SVO', note: '主節 sign the contract の SVO。' },
  'If I spoke fluent Spanish, I would apply for that position.': { pattern: 'SV', note: '主節 apply for は自動詞の SV。' },

  // u16-l1 because / so / although
  'I went to bed early because I was tired.': { pattern: 'SV', note: '主節 go to bed は自動詞の SV。' },
  'It started to rain, so we went inside.': { pattern: 'SV', note: '主節 we went inside の SV。' },
  'Although the restaurant was expensive, the food was disappointing.': { pattern: 'SVC', note: '主節 be + disappointing の SVC。' },
  'Because the train was delayed, I missed the meeting.': { pattern: 'SVO', note: '主節 missed the meeting の SVO。' },
  'He kept working although he was sick.': { pattern: 'SVO', note: '主節 kept working は目的語を取る SVO。' },
  'We canceled the picnic because the wind was too strong.': { pattern: 'SVO', note: '主節 canceled the picnic の SVO。' },
  'The road was closed, so we took another route.': { pattern: 'SVO', note: '主節 took another route の SVO。' },
  'Although the task was difficult, everyone stayed calm.': { pattern: 'SVC', note: '主節の stay + calm は SVC。' },
  'Although we started late, we finished the project on time.': { pattern: 'SVO', note: '主節 finished the project の SVO。' },
  'The elevator was broken, so we walked up five floors.': { pattern: 'SV', note: '主節 walk up は自動詞の SV。' },
  'I took a taxi because I was late.': { pattern: 'SVO', note: '主節 took a taxi の SVO。' },
  'I was late, so I took a taxi.': { pattern: 'SVO', note: '主節 took a taxi の SVO。' },

  // u16-l2 when / while / until / as soon as
  'When I opened the door, the cat ran out.': { pattern: 'SV', note: '主節 the cat ran out の SV。' },
  'Someone knocked on the door while I was taking a shower.': { pattern: 'SV', note: '主節 knock on は自動詞の SV。' },
  "Let's wait here until the rain stops.": { pattern: 'SVOC', note: 'Let us wait で us と wait が O=C の SVOC。' },
  "I'll send you a message as soon as the tickets go on sale.": { pattern: 'SVOO', note: '主節は you と a message を取る SVOO。' },
  'He listened to music while he cooked dinner.': { pattern: 'SV', note: '主節 listen to は自動詞の SV。' },
  'Please stay here until the doctor calls your name.': { pattern: 'SV', note: '命令文。stay は自動詞の SV。' },
  'While I was printing the tickets, the computer froze.': { pattern: 'SV', note: '主節 the computer froze の SV。' },
  'I will let you know as soon as I hear anything.': { pattern: 'SVOC', note: 'let + you + know で O=C の SVOC。' },
  'I did not notice the mistake until the report was printed.': { pattern: 'SVO', note: '主節 noticed the mistake の SVO。' },
  'While the guests were arriving, the chef finished the dessert.': { pattern: 'SVO', note: '主節 finished the dessert の SVO。' },
  'When the movie ended, we left.': { pattern: 'SV', note: '主節 we left の SV。' },
  'I was cooking when the phone rang.': { pattern: 'SV', note: '主節 was cooking の SV。' },
  'The phone rang while I was cooking.': { pattern: 'SV', note: '主節 the phone rang の SV。' },
  'While we were in Kyoto, we visited three temples.': { pattern: 'SVO', note: '主節 visited three temples の SVO。' },

  // u16-l3 both A and B / either / neither
  'Both my brother and my sister live in Nagoya.': { pattern: 'SV', note: 'live は目的語を取らない SV。' },
  'You can pay by either cash or card.': { pattern: 'SV', note: 'pay by は自動詞の SV。' },
  'Neither the bus nor the train runs after midnight.': { pattern: 'SV', note: 'run は自動詞の SV。' },
  'This app is both free and easy to use.': { pattern: 'SVC', note: 'be + free and easy の SVC。' },
  'Either you or your brother has to stay home.': { pattern: 'SV', note: 'stay home は目的語なしの SV。' },
  'Both the manager and the assistant are attending the conference.': { pattern: 'SVO', note: 'the conference が目的語の SVO。' },
  'You can either call me or send me a message.': { pattern: 'SVO', note: 'either の前半 call me を SVO とみなす。' },
  'Neither the kitchen nor the bathroom has a window.': { pattern: 'SVO', note: 'a window が目的語の SVO。' },
  'Neither of the applicants has sent a portfolio yet.': { pattern: 'SVO', note: 'a portfolio が目的語の SVO。' },
  'Both the design and the price impressed our customers.': { pattern: 'SVO', note: 'our customers が目的語の SVO。' },
  'We can take either the bus or the subway.': { pattern: 'SVO', note: 'take が the bus を目的語に取る SVO。' },
  'We can take neither the bus nor the subway at this hour.': { pattern: 'SVO', note: 'take が the bus を目的語に取る SVO。' },
}

export const b1Focus: PatternFocusMap = {
  'u11-l1':
    '現在完了は have + 過去分詞をまとめて1つの動詞とみなす。あとに目的語があれば SVO (I have lost my key.)、なければ SV (The bus has not arrived.) になる。',
  'u11-l2':
    '経験の現在完了でも文型は同じで、動詞が目的語を取るかどうかで SVO と SV に分かれる。have been to ~ は be + 場所なので SV とみなす。',
  'u11-l3':
    '継続を表す for / since の句は副詞なので数えない。have been a member のように be + 名詞なら SVC、know / have のように目的語を取れば SVO になる。',
  'u11-l4':
    'just / already / yet は副詞で文型には数えない。finished my homework のように目的語があれば SVO、arrived / left のように自動詞なら SV で判定する。',
  'u11-l5':
    '過去形と現在完了は時制が違うだけで文型の見方は同じ。目的語の有無で SVO と SV を分ける。so で結ばれた文は後ろの節を主節として判定する。',
  'u11-l6':
    'have been busy / friends のように be + 形容詞・名詞は SVC。know / receive / win などは目的語を取って SVO になる。been closed は受動態なので SV。',
  'u12-l1':
    '現在進行形は be + -ing を1つの動詞とみなす。meeting Emi のように目的語があれば SVO、flying / moving のように自動詞なら SV になる。',
  'u12-l2':
    'will / be going to / 現在進行形のどれも、あとに動詞が続く述部の形で文型が決まる。目的語を取れば SVO、自動詞なら SV と読む。',
  'u12-l3':
    'when / if / until / before などの副詞節は要素に数えず、主節で判定する。主節が wait / eat / start なら SV、call / cancel / lock なら SVO。',
  'u13-l1':
    '受動態は be + 過去分詞を1つの動詞とみなす。目的語は主語に移っているので、行為者を表す by 句があっても数えず、すべて SV になる。',
  'u13-l2':
    'by 句の有無は文型を変えない。be + 過去分詞を1動詞とみなすので、by / with / during などの句は数えず、すべて SV で判定する。',
  'u13-l3':
    'will be / must be / has been + 過去分詞はまとめて1つの動詞とみなす。助動詞や完了が付いても目的語は続かないので SV になる。',
  'u13-l4':
    '能動態なら目的語が動詞のあとに続いて SVO (Kenta broke the window.)、受動態にすると目的語が主語に移って SV になる。この対比で文型が変わる。',
  'u14-l1':
    '関係詞節は直前の名詞を修飾するだけで要素に数えない。who / that / which を外して主節の骨格 (I have a friend なら SVO) で判定する。',
  'u14-l2':
    '目的格の関係代名詞も名詞を修飾するので数えない。外したときに残る主節が "This is the ~" なら SVC、like / met のように目的語を取れば SVO。',
  'u14-l3':
    'whose / where / when の節も名詞を修飾するので要素に数えない。主節が be 動詞なら SVC、stay / work / remember / met なら SV や SVO になる。',
  'u14-l4':
    'カンマの有無は文型に影響しない。非制限用法の節も修飾なので数えず、主節の is a doctor / works / attracts で SVC・SV・SVO を決める。',
  'u14-l5':
    'there is 構文は目的語を取らない SV。関係詞節は修飾として数えず、外した主節の骨格 (This is the factory なら SVC、visited the village なら SVO) で判定する。',
  'u15-l1':
    'if 節は副詞節なので要素に数えず、主節で判定する。主節が opens / melts / stops なら SV、catch / cancel なら SVO、be + dangerous なら SVC。',
  'u15-l2':
    'if 節の仮定法も副詞節なので数えない。主節の would + 原形が目的語を取れば SVO、drive / travel / work / visit のように自動詞なら SV になる。',
  'u15-l3':
    'unless / in case / as long as の節は副詞節で数えない。主節の動詞が take / call / miss / use なら SVO、go / sit / leave なら SV、be + fine なら SVC。',
  'u15-l4':
    '1型でも2型でも文型は主節の動詞で決まる。move / stop / start なら SV、build / take / sign なら SVO、be home は場所を表す SV とみなす。',
  'u16-l1':
    'because / although の節は副詞節で数えず、so で結ばれた等位節は後ろを中心とみなす。主節の動詞で SV・SVC・SVO を判定する。',
  'u16-l2':
    '接続詞 when / while / until / as soon as が導く節は副詞節なので数えない。主節は rang / left / wait なら SV、finished / visited なら SVO、let は SVOC になる。',
  'u16-l3':
    'both A and B / either A or B / neither A nor B の相関接続詞は主語や目的語の一部で、要素を増やさない。主節の動詞で SV・SVO を判定する。',
}
