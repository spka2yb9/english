# 語彙データセットの増補（4,500語 → 7,500語）

## なぜ増やすか

CEFR B2 の運用には 6,500〜7,500 語の語彙が要るとされる。このアプリの語彙データは
4,500 語（A2 695 / B1 1,079 / B2 2,726）しかなく、B2 を名乗るには足りない。
重要度の高い語から順に約 3,000 語を足して 7,500 語にする。

## 何を足すか（優先順）

既存 4,500 語は Oxford 5000 系の抽象語・学術語に寄っていて、
**日常で毎日目にする具体語がごっそり抜けている**。そこを先に埋める。

1. 住まい・台所・道具・身の回りの品（第1弾で着手）
2. 食べ物・料理・食材
3. 体・健康・症状・医療
4. 動植物・自然・天気・地形
5. 服・買い物・お金・手続き
6. 交通・旅行・場所
7. 動作の細かい動詞（歩き方・見方・言い方・持ち方）
8. 感情・性格・態度の形容詞
9. 仕事・学校・IT・行政の実務語
10. 派生形（-ness / -ity / -ment / -ful / -less）と句動詞・慣用句の残り

`/tmp/miss.py` に語のリストを流し込むと、既存 4,500 語に無いものだけが返る。
候補出しはこれで足切りしてから書く。

## 1語に必要なもの

`src/content/types.ts` の `VocabularyEntry`。テストが通るには**必須項目に加えて次の2つ**が要る。

- `mnemonic`（覚えるヒント）— 全語必須。語源とは分けて、思い出す手がかりを書く。
- `collocations` — 全語必須。かつ**最低1件は見出し語の語幹を含む**こと
  （語幹 = 先頭語の先頭 `max(3, 長さ-3)` 文字）。
- `exampleSentence` も**同じ語幹を含む**こと。sting の例文を stung で書くと落ちる
  （語幹 sti が無いため）。不規則変化の語は原形が出る文にする。

書いたら `npx tsx scripts/check-vocab.mjs` で、足りない語と項目が一覧で出る。
英語で書く欄（例文・コロケーション・関連語）に日本語が紛れ込む事故も、このスクリプトが落とす。
café や £ は英文に出てよいので、検査は日本語（かな・漢字・全角）だけを見ている。
逆に「訳文に英単語が残る」事故（例: 彼女は politics から優雅に身を引いた）は自動判定できない。
hyphen・synonym のように訳文で英語を引くのが正しい語があるためで、スクリプトは
該当する数件を**目で確認する一覧**として出すだけにしてある。バッチごとに目を通すこと。

## 1バッチの手順

1. 候補を `/tmp/miss.py` に流して未収録語を取る。
   **突き合わせは id だけでなく見出し語でも行う**。既存データには `end-up`（id）／`end up`（word）の
   ように両者がずれる句動詞があり、id だけで見ると「未収録」に見えて重複を書いてしまう。
   `/tmp/dump.mjs` が id と word の両方を `/tmp/existing.txt` に出す。
   **英米つづり違いも重複扱いにする**。recognise は未収録に見えるが recognize が入っているので入れない。
   また `/tmp/miss.py` は**改行区切り**で読む（空白区切りにすると句動詞がばらける）。
2. `src/content/vocabulary/plusNN.ts` に書く（70語前後）。
3. `src/content/vocabulary/index.ts` に import と spread を足す。
4. `npx tsx scripts/check-vocab.mjs` → `bad 0` にする。
5. 件数を2か所直す。`src/content/summary.ts` の `vocabularyCount` と
   `src/content/content.test.ts` の `toHaveLength`。
   （summary.ts は `scripts/summary.mjs` でも生成できる）
6. `npx tsc --noEmit` と `npx vitest run src/content/content.test.ts src/pages/Vocabulary.test.tsx`。
7. このファイルの進捗に1行足す。

挿絵は語を入れ終えてから、`docs/vocabulary-illustrations.md` の手順で追いかける。
語が無ければページに出ないが、絵が無くても覚えるヒントの文は出るので、語を先に入れる。

## 進捗

- 4,500 → **7,500（目標に到達）**。内訳は B2 5,076 / B1 1,535 / A2 889。
  B2 に必要とされる 6,500〜7,500語の上限に達した。ここで語の追加はいったん終わり、
  次は増補した3,000語に挿絵をつける段階に移る（`docs/vocabulary-illustrations.md` の手順）。
  この回で **B2の下限とされる6,500語を超えた**。以降は上限7,500語に向けて厚みを足していく。
- 第1弾 plus01.ts（71語）住まい・台所・道具・身の回り:
  drawer、faucet、kettle、saucepan、frying pan、blender、toaster、microwave、stove、freezer、
  dishwasher、countertop、mattress、pillow、quilt、duvet、wardrobe、closet、bookshelf、stool、
  armchair、sofa、couch、rug、bulb、socket、cord、charger、clock、calendar、glue、stapler、
  hammer、screwdriver、drill、saw、bolt、wrench、pliers、toolbox、shovel、rake、hose、bucket、
  broom、mop、sponge、dustbin、shampoo、toothbrush、toothpaste、razor、comb、scissors、zipper、
  sleeve、collar、cuff、hem、apron、scarf、sandal、boot、slipper、sneaker、ribbon、wallet、purse、
  backpack、suitcase、umbrella
- 第2弾 plus02.ts（127語）食べ物・料理・味:
  simmer、roast、grill、dice、peel、whisk、knead、marinate、sprinkle、mash、grate、thaw、defrost、
  preheat、garnish、stew、rinse、edible、tasty、delicious、bland、sour、salty、greasy、crispy、
  crunchy、creamy、juicy、chewy、stale、ripe、rotten、serving、snack、dessert、appetizer、course、
  menu、teaspoon、tablespoon、ounce、pound、gram、pinch、dash、dough、yeast、crust、loaf、crumb、
  oat、barley、cereal、porridge、noodle、pasta、dumpling、tofu、pork、lamb、mutton、poultry、bacon、
  ham、sausage、steak、fillet、shrimp、prawn、crab、lobster、oyster、squid、tuna、salmon、cod、
  cabbage、lettuce、spinach、broccoli、cauliflower、celery、cucumber、pumpkin、eggplant、garlic、
  ginger、chili、mushroom、asparagus、pea、leek、radish、peach、pear、plum、cherry、grape、melon、
  watermelon、pineapple、mango、lime、grapefruit、berry、strawberry、raspberry、blueberry、coconut、
  walnut、almond、peanut、cinnamon、mint、parsley、basil、seasoning、vinegar、mustard、mayonnaise、
  ketchup、syrup、honey、marmalade、yoghurt、butter、margarine
- 第3弾 plus03.ts（113語）体・症状・医療:
  jaw、chin、forehead、eyebrow、eyelid、eyelash、nostril、gum、tonsil、collarbone、fingernail、waist、
  thigh、shin、rib、pelvis、tendon、ligament、cartilage、marrow、artery、capillary、intestine、bowel、
  bladder、womb、gland、thyroid、pancreas、sneeze、cough、sniff、yawn、hiccup、shiver、sweat、itch、
  ache、sting、swell、bruise、limp、faint、scar、blister、rash、ulcer、nauseous、sore、numb、swollen、
  feverish、exhausted、breathless、drowsy、contagious、infectious、sterile、germ、hygiene、sanitation、
  immunity、allergy、asthma、diabetes、tumour、inflammation、fracture、sprain、dosage、capsule、
  ointment、bandage、plaster、stitch、vaccine、vaccination、syringe、nurse、midwife、stretcher、
  wheelchair、crutch、transplant、antibiotic、painkiller、aspirin、pharmacy、pharmacist、optician、
  checkup、heartbeat、posture、stamina、exercise、massage、diet、calorie、carbohydrate、overweight、
  underweight、newborn、toddler、puberty、adolescence、menopause、ageing、deaf、mute、addict、
  overdose、sober、intoxicated
- 第4弾 plus04.ts（119語）動物・植物・地形・天気:
  mammal、reptile、amphibian、rodent、snail、slug、beetle、ant、wasp、moth、butterfly、mosquito、
  grasshopper、cricket、cockroach、termite、caterpillar、sparrow、pigeon、crow、eagle、hawk、owl、swan、
  duck、goose、chicken、rooster、turkey、parrot、penguin、toad、lizard、snake、turtle、tortoise、
  crocodile、alligator、wolf、fox、deer、rabbit、squirrel、mouse、hedgehog、otter、whale、dolphin、
  shark、bull、calf、goat、donkey、camel、elephant、lion、tiger、ape、gorilla、giraffe、zebra、hoof、
  paw、claw、beak、tusk、fin、burrow、herd、flock、swarm、oak、pine、maple、birch、willow、bamboo、
  cactus、fern、moss、vine、shrub、hedge、trunk、twig、bud、blossom、petal、thorn、pollen、sap、bark、
  meadow、pasture、swamp、marsh、dune、canyon、plateau、ridge、creek、waterfall、glacier、iceberg、
  breeze、gale、thunder、lightning、sleet、frost、dew、mist、fog、drizzle、downpour、sunrise、sunset、
  dusk、twilight
- 第5弾 plus05.ts（115語）買い物・お金・手続き・交通・動作の細かい動詞:
  warranty、voucher、coupon、clearance、checkout、cashier、trolley、aisle、inventory、invoice、
  overdraft、instalment、repayment、interest、savings、deduction、exchange rate、banknote、change、
  debit、repay、spend、bankrupt、bankruptcy、insolvent、creditor、debtor、collateral、lease、
  receptionist、form、passport、linen、denim、nylon、polyester、velvet、sew、knit、mend、baggy、
  fitted、shabby、trendy、commuter、timetable、luggage、baggage、porter、boarding、duty-free、
  layover、itinerary、sightseeing、souvenir、guidebook、hostel、excursion、detour、shortcut、
  roundabout、intersection、crossroads、pavement、sidewalk、kerb、motorway、ferry、dock、pier、wharf、
  diesel、brake、clutch、steering、windscreen、bonnet、dashboard、puncture、tow、stroll、stride、
  roam、ramble、hike、trek、stagger、tiptoe、sprint、jog、trot、gallop、hop、glare、squint、blink、
  wink、peek、mutter、mumble、murmur、shriek、groan、moan、chuckle、giggle、smirk、frown、scowl、
  sob、weep、snatch、fling、hurl、shove
- 第6弾 plus06.ts（118語）感情・性格の形容詞＋仕事・IT・大学:
  gloomy、discontented、ecstatic、elated、irritated、enraged、resentful、jealous、envious、uneasy、
  apprehensive、panicky、terrified、petrified、startled、composed、serene、laid-back、easygoing、tense、
  edgy、restless、self-assured、arrogant、conceited、timid、bashful、obstinate、adaptable、rigid、
  lenient、tolerant、stingy、mean、selfish、selfless、inconsiderate、frank、blunt、tactful、tactless、
  hypocritical、treacherous、diligent、industrious、hardworking、idle、sloppy、meticulous、inquisitive、
  nosy、apathetic、witty、shrewd、cunning、naive、gullible、thankful、ungrateful、compassionate、
  ruthless、merciful、remorseful、smug、nostalgic、melancholy、cheerless、idealistic、impulsive、
  reckless、prudent、vacancy、shortlist、interviewee、probation、internship、apprenticeship、
  subordinate、staffing、rota、roster、sabbatical、redundancy、demotion、appraisal、minutes、briefing、
  brainstorm、keynote、spreadsheet、server、upload、bandwidth、firewall、encryption、plugin、cursor、
  folder、username、login、logout、malware、phishing、hacker、glitch、debug、algorithm、dataset、
  analytics、automation、dormitory、syllabus、tutorial、coursework、dissertation、plagiarism、diploma、
  postgraduate
- 第7弾 plus07.ts（122語）論説・学術の動詞＋法律・行政＋抽象名詞:
  ascertain、corroborate、substantiate、refute、rebut、contradict、reconcile、delineate、elucidate、
  stipulate、postulate、hypothesise、scrutinise、appraise、collate、tabulate、quantify、extrapolate、
  entail、necessitate、presuppose、ascribe、apportion、mitigate、alleviate、exacerbate、aggravate、
  curtail、truncate、abridge、condense、streamline、augment、amplify、proliferate、dwindle、degenerate、
  stagnate、fluctuate、conform、deviate、diverge、converge、supersede、supplant、relegate、vindicate、
  exonerate、absolve、impede、hinder、hamper、thwart、obstruct、forestall、instigate、incite、spur、
  galvanise、withhold、relinquish、forfeit、divulge、censor、ratify、authorise、accredit、certify、
  plaintiff、defendant、barrister、parole、acquittal、litigation、injunction、subpoena、statute、decree、
  manifesto、diplomacy、embargo、ceasefire、armistice、census、demographic、deportation、bribery、remand、
  scarcity、onset、outset、repercussion、ramification、rationale、yardstick、paradox、anomaly、
  discrepancy、inconsistency、dissent、backlash、outcry、deterrent、leverage、inertia、nuance、
  connotation、hallmark、prerequisite、precondition、caveat、setback、shortcoming、pitfall、loophole、
  turmoil、upheaval、unrest、disarray、consolation、reparation、philanthropy
- 第8弾 plus08.ts（90語）句動詞:
  bail out、bank on、barge in、bear out、boil down to、branch out、brush up on、bump into、burn out、
  cash in on、catch on、chip in、clamp down on、come by、come down to、crack down on、cut back、
  cut down on、dawn on、die down、do away with、draw up、ease off、face up to、fall back on、
  fall through、fend for、fit in、follow through、get away with、get on with、get round to、go about、
  go along with、grow on、head for、hold off、hold on to、iron out、jot down、kick off、lash out、
  lead to、let off、make do with、miss out、mull over、nail down、opt for、opt out、pass out、
  phase out、pick on、pin down、play down、pull off、pull through、put across、put aside、put forward、
  rely on、scale back、see through、set back、settle for、shake off、shrug off、single out、sink in、
  size up、stand up for、step down、step in、stick out、sum up、switch off、take to、talk into、
  tear down、tell off、think over、tip off、tone down、touch on、track down、turn to、wear off、
  weigh up、wind up、wipe out
  （end up / get over / keep up with / rule out / run out of は既存と重複したので取り下げた）
- 第9弾 plus09.ts（125語）派生名詞（-ness / -ity / -ment）＋描写の形容詞:
  awkwardness、bitterness、bluntness、boldness、brightness、clumsiness、coldness、dullness、eagerness、
  emptiness、fondness、gentleness、greatness、harshness、idleness、likeness、madness、neatness、
  openness、readiness、richness、rudeness、shyness、sickness、smoothness、softness、stiffness、
  stillness、sweetness、tenderness、thickness、tiredness、vagueness、wilderness、absurdity、ambiguity、
  authenticity、brevity、durability、familiarity、feasibility、fertility、formality、humidity、
  legitimacy、longevity、maturity、modesty、neutrality、novelty、obscurity、originality、plausibility、
  proximity、purity、rarity、rigidity、secrecy、severity、simplicity、uniformity、versatility、
  visibility、vitality、amusement、astonishment、bewilderment、concealment、confinement、detachment、
  discouragement、embodiment、empowerment、enrichment、enrolment、entitlement、fulfilment、impairment、
  impeachment、nourishment、reinforcement、shipment、postponement、refinement、sturdy、flimsy、bulky、
  compact、spacious、cramped、cosy、messy、slippery、fluffy、soggy、brittle、glossy、blurred、vivid、
  dim、murky、opaque、quiet、deafening、shrill、piercing、muffled、fragrant、cumbersome、portable、
  disposable、durable、scarce、plentiful、ample、meagre、lavish、brisk、sluggish、hasty、gradual、
  abrupt、erratic、deserted、bustling
  この回から、規則的な派生語は「訳・例文・ヒントを1語ずつ手で書いた表」を Python で組み立てる形にした。
  文言はすべて個別に書いており、テンプレ文の使い回しはしていない。
- 第10弾 plus10.ts（125語）文章・文学・芸術＋理科＋宗教・歴史・スポーツ:
  apostrophe、comma、semicolon、colon、bracket、parenthesis、hyphen、asterisk、paragraph、phrase、
  syllable、vowel、consonant、prefix、suffix、synonym、antonym、grammar、punctuation、spelling、
  handwriting、footnote、bibliography、citation、appendix、glossary、preface、foreword、prose、
  nonfiction、narrator、simile、satire、publisher、proofread、paperback、hardback、readership、
  bestseller、mural、palette、conductor、symphony、chorus、soloist、rehearsal、encore、violin、cello、
  flute、trumpet、guitar、tempo、chord、playwright、rehearse、audition、friction、velocity、
  acceleration、atom、molecule、particle、electron、proton、neutron、nucleus、solvent、catalyst、
  oxidation、combustion、voltage、insulator、magnet、magnetism、telescope、microscope、chromosome、
  organism、mutation、photosynthesis、respiration、digestion、ecosystem、food chain、orbit、galaxy、
  comet、asteroid、eclipse、ozone、sediment、erosion、volcano、renewable、fossil fuel、sustainability、
  recycling、landfill、shrine、monastery、cathedral、chapel、altar、pilgrimage、folklore、superstition、
  prophecy、scripture、sermon、monarchy、dynasty、conquest、revolt、siege、feudal、archaeology、
  excavation、artefact、relic、ruins、descendant、umpire、qualifier、draw
- 第11弾 plus11.ts（125語）論説・実務の動詞の残り＋人・職業:
  affirm、approximate、avert、bestow、bolster、broaden、crave、defer、denote、deter、discern、dispatch、
  disperse、dwell、elicit、emit、emphasise、enlarge、entrust、envisage、equate、exempt、expel、
  fabricate、falter、furnish、gauge、harness、hoist、ignite、immerse、inhabit、inscribe、instil、
  intrigue、legislate、lessen、liberate、lodge、magnify、marginalise、mediate、memorise、minimise、
  narrate、navigate、negate、normalise、nurture、offset、omit、optimise、orchestrate、outweigh、
  overlap、penetrate、permeate、pertain、pinpoint、populate、prioritise、procure、prolong、propel、
  quench、radiate、reap、reclaim、reconstruct、rectify、redeem、refrain、rehabilitate、reinstate、
  reiterate、rejoice、renounce、reorganise、repel、replicate、restrain、revoke、safeguard、scatter、
  soothe、sprout、stabilise、subscribe、suffice、surpass、swap、sway、symbolise、sympathise、
  synthesise、tally、uncover、underline、underpin、utilise、validate、withstand、bystander、eyewitness、
  newcomer、breadwinner、caretaker、babysitter、apprentice、trainee、intern、negotiator、mediator、
  auditor、technician、plumber、electrician、carpenter、butcher、baker、tailor、hairdresser、gardener、
  farmer、labourer
- 第12弾 plus12.ts（115語）論説・報道の抽象名詞:
  adversity、affinity、allegiance、allure、anguish、apathy、ardour、aversion、backbone、bearing、
  blueprint、bout、brink、calibre、chore、cohesion、condolence、conjunction、contour、curb、deadlock、
  delusion、destiny、detriment、disgrace、disguise、distraction、downfall、eligibility、envy、
  equilibrium、esteem、euphoria、famine、fatigue、fervour、flair、fluctuation、foresight、fortitude、
  frenzy、fringe、fusion、gist、glimmer、grievance、gulf、haven、hindrance、hoax、hub、hunch、hurdle、
  impetus、imprint、impulse、inclination、influx、intuition、jargon、jeopardy、juncture、knack、
  liability、lull、lure、manoeuvre、mindset、mishap、misconception、nuisance、omen、onslaught、ordeal、
  overhaul、oversight、panorama、paradigm、peril、pinnacle、plight、poise、polarity、predicament、
  prestige、presumption、prowess、quirk、radius、rapport、reassurance、rebuke、reckoning、recourse、
  reliance、remnant、renown、respite、reverence、rift、rigour、rivalry、rubble、sanctuary、shortfall、
  snag、standpoint、stigma、strife、stronghold、subtlety、token、uproar、vantage、verge
  この帯の語は「決まった形」で出ることが多いので、on the brink of / in jeopardy / a quirk of fate /
  by the same token のような定型をコロケーションと覚えるヒントに必ず入れた。
- 第13弾 plus13.ts（123語）論説・実務の形容詞:
  adept、akin、aloof、ambivalent、amiable、analogous、apt、astute、audible、autonomous、barren、benign、
  bleak、blatant、candid、coherent、cohesive、commonplace、compatible、complacent、conceivable、concise、
  concurrent、condescending、confidential、conscientious、conspicuous、contentious、contradictory、
  courteous、cumulative、deficient、definitive、derogatory、desolate、detrimental、devious、devoid、
  discreet、disparate、dormant、drastic、dubious、eccentric、elusive、eminent、erroneous、exhaustive、
  feeble、fertile、finite、fluent、formidable、frantic、frugal、futile、glaring、graceful、grim、
  hazardous、hectic、ignorant、immaculate、impartial、impeccable、imperative、implicit、incessant、
  incidental、inclusive、incompatible、indispensable、inferior、infinite、innate、intermittent、
  intricate、intrinsic、invaluable、irreversible、lucrative、lucid、literal、lukewarm、malicious、
  manual、mediocre、merciless、methodical、mundane、negligible、nominal、noticeable、obscure、obsolete、
  ominous、optimal、overt、painstaking、paramount、perpetual、pertinent、petty、picturesque、plausible、
  potent、pragmatic、precarious、prevalent、prone、prosperous、provisional、rampant、redundant、
  relentless、repetitive、reputable、resilient、rigorous、scenic、secluded、simultaneous、sleek
  取り違えやすい対は覚えるヒントで区別した: definitive と definite、eminent と imminent、
  discreet と discrete、exhaustive と exhausted、invaluable（値がつかないほど貴重）と valueless、
  finite と infinite（アクセント位置も違う）。
  （mandatory は既存と重複したので取り下げた）
- 第14弾 plus14.ts（112語）形容詞の残り＋論説文をつなぐ副詞:
  solitary、sparse、spontaneous、sporadic、stagnant、staple、static、steadfast、stern、stringent、
  succinct、superficial、superfluous、susceptible、tangible、tedious、tentative、thrifty、tranquil、
  transient、turbulent、ubiquitous、unanimous、unavoidable、unbiased、uncanny、unconditional、undue、
  unequivocal、unforeseen、unilateral、unparalleled、unrelenting、unsettling、untenable、upbeat、
  upright、utmost、versatile、vigorous、void、wary、wasteful、weary、wholesome、wilful、archaic、
  belated、corrosive、heterogeneous、illegible、incoherent、inconceivable、lofty、retrospective、
  rudimentary、alternatively、chiefly、collectively、conversely、crucially、decidedly、drastically、
  duly、eagerly、evidently、exceedingly、harshly、henceforth、hereby、hitherto、ideally、implicitly、
  indefinitely、informally、intentionally、invariably、jointly、markedly、mistakenly、mutually、
  narrowly、noticeably、notwithstanding、overwhelmingly、perpetually、persistently、plainly、promptly、
  proportionally、purposely、reluctantly、repeatedly、routinely、scarcely、sensibly、sharply、
  sincerely、successively、swiftly、unanimously、undeniably、uniformly、unnecessarily、unwittingly、
  urgently、vastly、vigorously、virtually、visibly、voluntarily、willingly
  副詞は「文頭に置いて話の向きを変える」型を厚めに入れた（conversely, crucially, notwithstanding,
  hitherto ↔ henceforth, alternatively）。wary と weary のような紛らわしい対も注記した。
- 第15弾 plus15.ts（102語）連語・慣用句・接続表現:
  at all costs、at first glance、at large、at odds with、at stake、at the expense of、at the mercy of、
  by and large、by virtue of、for the sake of、in accordance with、in due course、in favour of、
  in light of、in line with、in place of、in principle、in retrospect、in the event of、in the long run、
  in the wake of、in vain、on the contrary、on the grounds that、out of the question、to some extent、
  with regard to、with respect to、without fail、a far cry from、all the same、as a rule、be bound to、
  be liable to、be subject to、be supposed to、cannot help but、come to terms with、get to grips with、
  have a say in、have no choice but to、keep track of、lose sight of、make sense of、make the most of、
  pay attention to、take account of、take advantage of、take for granted、take into account、
  take issue with、take part in、throw light on、turn a blind eye to、break the ice、bite the bullet、
  call it a day、cut corners、draw the line、face the music、get the hang of、go the extra mile、
  hit the nail on the head、jump to conclusions、keep an eye on、learn the ropes、
  let the cat out of the bag、miss the point、on the same page、play it by ear、pull your weight、
  put your foot down、read between the lines、see eye to eye、set the record straight、sit on the fence、
  stand your ground、steal the show、take the plunge、the tip of the iceberg、think outside the box、
  under the weather、up in the air、as a result of、as opposed to、given that、in contrast to、
  in so far as、no sooner than、on condition that、provided that、so as to、so long as、such as、
  aside from、along with、instead of、other than、owing to、prior to、subsequent to、thanks to
  **連語の例文は語幹が消えやすい**。be bound to の語幹は "be" なので "are bound to" では落ちる。
  take part in / stand your ground / steal the show も過去形にすると落ちる。原形が出る文にすること。
  この回、目視一覧が実際に1件（訳文に good weather が残っていた）を拾った。
- 第16弾 plus16.ts（108語）ビジネス・金融／住まいと不動産／報道とネット:
  ledger、overhead、markup、dividend、stakeholder、equity、broker、valuation、takeover、buyout、cartel、
  antitrust、tariff、procurement、logistics、distributor、retailer、wholesaler、supplier、vendor、
  royalty、licensing、infringement、counterfeit、whistleblower、downturn、deflation、austerity、bailout、
  profitability、solvency、liquidity、depreciation、freelance、self-employed、payroll、severance、perk、
  attic、balcony、porch、hallway、staircase、floorboard、doorstep、doorway、windowsill、shutter、
  chimney、fireplace、radiator、boiler、thermostat、insulation、draught、damp、mould、plumbing、wiring、
  fuse、gutter、patio、driveway、tenancy、sublet、eviction、estate agent、surveyor、outskirts、borough、
  terrace、semi-detached、bungalow、mansion、penthouse、byline、scoop、tabloid、broadsheet、bulletin、
  presenter、pundit、press release、censorship、libel、slander、defamation、retraction、disclaimer、
  ratings、viewership、prime time、livestream、podcast、blog、influencer、hashtag、viral、trending、
  moderation、troll、clickbait、paywall、misinformation、disinformation、fact-check、verification、framing
  **和製英語との食い違いは覚えるヒントに必ず書く**: mansion は集合住宅ではなく大邸宅、
  「ゴールデンタイム」は prime time、「マンション」は flat / apartment。
  libel（文書）と slander（口頭）、misinformation（過失）と disinformation（故意）も書き分けた。
- 第17弾 plus17.ts（101語）音と動きの動詞／家族と人生の出来事／時を表す語:
  growl、howl、purr、hiss、chirp、buzz、croak、roar、squeak、bang、clatter、clang、rattle、rustle、
  creak、squeal、screech、thud、thump、splash、trickle、gush、drip、ooze、seep、spurt、spray、swirl、
  ripple、flicker、blaze、glow、gleam、sparkle、glitter、shimmer、dazzle、crumble、flake、dent、flatten、
  wobble、tilt、topple、crumple、bob、whirl、revolve、tumble、uncle、aunt、nephew、niece、cousin、
  stepmother、stepfather、in-laws、fiancé、fiancée、widower、orphan、guardian、heir、teenager、bachelor、
  newlywed、acquaintance、comrade、foe、courtship、honeymoon、cremation、tomb、mourning、bereavement、
  inheritance、upbringing、parenting、curfew、ancestry、lineage、kinship、clan、extended family、
  nuclear family、midday、midnight、fortnight、century、millennium、epoch、weekday、weekend、holiday、
  vacation、semester、quarter、overdue、lasting、momentary、recurrence
  音の語は「どんな音か」を覚えるヒントで書き分けた: thud（響かない鈍い一発）と thump（打つ動作寄り）、
  squeak（油切れの高い音）と squeal（もっと長く大きい）と screech（耳障り）、
  trickle（ちょろちょろ）と gush（どっと）、ooze（粘って出る）と seep（静かにしみる）。
  光の語も同様に: flicker（明滅）、glow（炎なしに光る）、gleam（なめらかな面の反射）、
  sparkle（点々と瞬く）、shimmer（ゆらめく）、dazzle（強すぎて見えない）。
- 第18弾 plus18.ts（80語）句動詞の残り:
  add up、back down、blow over、bottom out、break away、break off、bring forward、brush aside、buy out、
  call in、clear up、close down、come about、come apart、come off、come round、cool down、cover up、
  crop up、die out、draw on、dress up、drop in、drum up、dwell on、eat into、even out、fall out、
  fend off、fill up、fire up、fizzle out、flare up、fork out、gear up、get ahead、give rise to、
  go under、grind to a halt、keep back、knock out、lay down、let on、level off、live off、map out、
  mark down、measure up、narrow down、pass off、piece together、press ahead、reel off、ring up、
  round up、rule over、run down、sail through、seize on、set in、shore up、sign up、slip up、spell out、
  stamp out、step up、stir up、strike out、sweep aside、tail off、team up、tie in with、trickle down、
  usher in、wade through、ward off、water down、whittle down、wriggle out of、zoom in
  紛らわしい対を注記した: rule over（統治する）と rule out（除外する）、set in（悪い状態が居座る）と
  set out（出発する）、die out（絶滅する）と die down（静まる）、fill up（満タン）と fill in（記入）。
- 第19弾 plus19.ts（88語）派生名詞（-tion / -ment / -ance / -ity など）:
  abolition、adherence、admiration、advancement、affiliation、affirmation、alteration、anticipation、
  appliance、applause、apprehension、approximation、arbitration、ascent、assimilation、attainment、
  authorisation、avoidance、betrayal、cancellation、captivity、cessation、clarification、coercion、
  coexistence、colonisation、commemoration、commencement、compilation、comprehension、compression、
  condemnation、conformity、congestion、consolidation、containment、contamination、contemplation、
  continuation、contraction、cultivation、defiance、degradation、deliberation、demolition、depiction、
  deprivation、desertion、designation、desperation、devastation、deviation、devotion、differentiation、
  diffusion、disappearance、discontent、dispersal、displacement、dissatisfaction、dissolution、distortion、
  disturbance、diversion、domination、elaboration、elevation、elimination、emigration、enactment、
  enhancement、enlargement、enlightenment、eruption、escalation、estimation、evacuation、exaggeration、
  exemption、exhaustion、experimentation、extinction、extraction、fabrication、facilitation、fascination、
  formulation、fragmentation
  取り違えやすい対を注記: tax avoidance（合法の節税）と tax evasion（脱税）、
  emigration（出ていく）と immigration（入ってくる）、ascent と assent（同音・別語）、
  condemn は n を読まないが condemnation では読む。
- 第20弾 plus20.ts（90語）派生名詞の続き（G-R）:
  generalisation、germination、gratification、hibernation、humiliation、illumination、imitation、immersion、
  impersonation、imposition、impoverishment、inception、incorporation、indignation、induction、indulgence、
  infestation、infiltration、informant、infusion、inhalation、inhibition、initiation、inoculation、
  inscription、insistence、insurgency、intensification、interception、interrogation、intimidation、
  intoxication、intrusion、inversion、irrigation、irritation、iteration、legalisation、liquidation、
  lubrication、magnification、manifestation、mediation、mobilisation、modernisation、multiplication、
  nationalisation、naturalisation、negation、neutralisation、notification、obstruction、omission、
  oppression、optimisation、partition、penetration、perfection、persecution、persistence、persuasion、
  pollination、portrayal、precaution、precipitation、predominance、privatisation、proclamation、
  proliferation、pronunciation、propagation、provocation、purification、ratification、realisation、
  recollection、reconciliation、rectification、redemption、reformation、relaxation、relocation、
  remembrance、renewal、renovation、repatriation、repetition、repression、retention、reversal
  **動詞からつづりが変わる名詞は必ず注意を促す**: pronounce → pronunciation（o が消える）、
  omit → omission、persuade → persuasion、induction（帰納）と deduction（演繹）、
  persecution（迫害）と prosecution（起訴）。
  この回、CJK 検査が関連語欄に混入した日本語（改革）を1件拾った。
- 第21弾 plus21.ts（103語）派生名詞の残り（R-Z）＋ -ive 形容詞:
  revocation、salvation、saturation、seclusion、secretion、sedation、segregation、simplification、
  specialisation、stabilisation、standardisation、starvation、sterilisation、stimulation、stipulation、
  subordination、subsidence、suffocation、suppression、sustenance、symbolism、termination、turbulence、
  unification、urbanisation、utilisation、validation、ventilation、victimisation、vindication、
  visualisation、expensive、abrasive、adhesive、affirmative、appreciative、argumentative、assertive、
  attentive、authoritative、captive、coercive、communicative、compulsive、conclusive、conducive、
  constructive、contemplative、corrective、deductive、demonstrative、depressive、derivative、descriptive、
  digestive、disruptive、divisive、emotive、evasive、evocative、expansive、expressive、figurative、
  formative、furtive、illustrative、immersive、indicative、inductive、inflammatory、instinctive、
  instructive、interpretive、intrusive、intuitive、inventive、investigative、manipulative、normative、
  obsessive、operative、perceptive、permissive、pervasive、possessive、predictive、prescriptive、
  preventive、primitive、prohibitive、provocative、punitive、reactive、receptive、reflective、
  regenerative、repressive、reproductive、restorative、restrictive、speculative、subjective、submissive
  **expensive のような基本語が既存4,500語から抜けていた**。派生形を機械的にたどる作業でも、
  途中で基本語の穴が見つかることがあるので、候補は必ず未収録判定に通すこと。
  取り違えやすい対: authoritative（信頼できる）と authoritarian（権威主義の）、
  compulsive（やめられない）と compulsory（義務の）、descriptive と prescriptive、
  deductive（演繹）と inductive（帰納）、emotional（人が感情的）と emotive（ものが感情を呼ぶ）。
- 第22弾 plus22.ts（100語）-ous / -able / -ful / -less の形容詞:
  dangerous、famous、deceptive、ambiguous、arduous、atrocious、audacious、boisterous、ferocious、
  frivolous、gracious、hideous、homogeneous、ingenious、innocuous、laborious、ludicrous、luminous、
  luxurious、marvellous、miraculous、mischievous、momentous、monotonous、mountainous、noxious、
  obnoxious、outrageous、perilous、pompous、populous、porous、pretentious、rebellious、illustrious、
  admirable、advisable、agreeable、arguable、attainable、avoidable、bearable、believable、changeable、
  charitable、commendable、curable、debatable、despicable、dispensable、enviable、equitable、excusable、
  flammable、honourable、hospitable、identifiable、imaginable、impenetrable、impressionable、improbable、
  incomparable、incurable、indefensible、inexcusable、interchangeable、irreplaceable、irresistible、
  justifiable、knowledgeable、laughable、manageable、measurable、boastful、deceitful、disgraceful、
  doubtful、dreadful、eventful、forceful、fruitful、insightful、joyful、mournful、pitiful、regretful、
  resourceful、respectful、rightful、scornful、skilful、spiteful、tasteful、truthful、watchful、aimless、
  boundless、effortless、fearless、flawless
  **ここでも基本語 dangerous と famous が既存4,500語から抜けていた**。
  一字違いで意味が変わる対を注記: ingenious（巧妙な）と ingenuous（純朴な）、
  momentous（重大な）と momentary（一瞬の）、enviable（うらやまれる）と envious（うらやむ）、
  tasteful（品がよい）と tasty（おいしい）、respectful / respectable / respective、
  flammable と inflammable は同じ意味（in- を否定と誤解させるため flammable が推奨）。
  なお目視一覧を meaningsJa まで広げたら140件になり、その大半が
  「(be absorbed in で)」のような正当な英語だったので、訳文だけを見る形に戻した。
- 第23弾 plus23.ts（90語）-less / -al / -ic の形容詞:
  natural、personal、mindless、motionless、nameless、needless、odourless、painless、penniless、
  pointless、powerless、priceless、remorseless、seamless、senseless、shameless、sleepless、spotless、
  stainless、tasteless、thankless、timeless、tireless、toothless、valueless、weightless、worthless、
  accidental、ceremonial、consequential、continental、departmental、developmental、dimensional、
  elemental、factual、fictional、governmental、grammatical、habitual、horizontal、hypothetical、
  imperial、impersonal、intentional、maternal、medicinal、monumental、nutritional、optional、
  ornamental、paternal、pivotal、seasonal、sensational、sequential、situational、spatial、supplemental、
  temporal、territorial、topical、transitional、vocational、acidic、aerobic、analytic、apologetic、
  athletic、catastrophic、chaotic、climatic、cosmetic、cryptic、diagnostic、elastic、emphatic、
  energetic、fantastic、geographic、heroic、horrific、hygienic、hysterical、iconic、idiomatic、
  linguistic、majestic、metallic、microscopic
  **さらに基本語 natural と personal が抜けていた**（dangerous / famous / expensive に続いて）。
  一字違いの別語を注記: elemental（根源的な）と elementary（初歩の）、climatic（気候の）と
  climactic（クライマックスの）、topical（時事的な）と typical（典型的な）、
  medicinal（薬効のある）と medical（医学の）、temporal（時間の）と temporary（一時的な）、
  seasonal と seasoned、personal と personnel。
- 第24弾 plus24.ts（74語）-ic / -ish の形容詞、-en / -ify の動詞:
  patriotic、pathetic、periodic、phonetic、photographic、poetic、prehistoric、prolific、prophetic、
  rhetorical、rhythmic、robotic、sarcastic、schematic、seismic、semantic、simplistic、sonic、stylistic、
  synthetic、telescopic、therapeutic、thematic、traumatic、volcanic、bookish、childish、foolish、
  greenish、outlandish、peckish、reddish、sheepish、snobbish、squeamish、stylish、blacken、brighten、
  dampen、darken、deafen、deepen、enlighten、harden、hasten、lengthen、lighten、loosen、moisten、
  quicken、ripen、sharpen、shorten、soften、stiffen、straighten、sweeten、thicken、toughen、whiten、
  worsen、diversify、electrify、exemplify、falsify、gratify、horrify、pacify、personify、purify、
  signify、simplify、solidify、typify
  接尾辞の働きを覚えるヒントに明記した（-en は「〜にする」、-ify は「〜化する」、
  -ish は「〜っぽい／〜がかった」）。初見の語も分解して読めるようにするため。
  childish（幼稚な・悪い意味）と childlike（純真な・良い意味）、simplistic（単純すぎる・批判）と
  simple（単純な・中立）、stylish（おしゃれ）と stylistic（文体上の）も書き分けた。
  発音の落とし穴も: hasten・moisten・soften の t は読まない。
- 第25弾 plus25.ts（95語）接頭辞でできた語:
  antibody、antiseptic、antidote、antisocial、autobiography、autograph、automate、autopilot、bilateral、
  biannual、biodiversity、counterattack、counterbalance、counterproductive、decode、decompose、dehydrate、
  deregulate、devalue、disband、disbelief、discontinue、disembark、disengage、disinfect、dislodge、
  dismantle、disobey、disprove、disqualify、disregard、dissuade、distrust、exhale、extrovert、foresee、
  foreground、forewarn、hyperactive、hyperlink、hypersensitive、interconnect、interdependent、
  intermediary、interplay、intertwine、misbehave、miscalculate、misconduct、misguided、mishandle、
  misinterpret、misjudge、mislead、mismanage、mismatch、misplace、misread、misspell、mistrust、misuse、
  nonexistent、nonprofit、nonstop、nonverbal、outdated、outdo、outgrow、outlast、outlive、outnumber、
  outperform、outsmart、outsource、overcharge、overcrowded、overdo、overestimate、overhear、overload、
  overpower、overreact、overrule、overrun、overshadow、oversleep、overstate、overtake、overthrow、
  overwork、postwar、preconception、predispose、preoccupied、preschool
  接頭辞の働きを一語ずつ覚えるヒントに書いた（anti- 対抗 / auto- 自ら / bi- 二 / counter- 逆に /
  de- 取り除く / dis- 否定・分離 / fore- 前もって / hyper- 過度に / inter- 互いに / mis- 誤って /
  non- 否定 / out- 勝って・超えて / over- 過度に / post- 後 / pre- 前）。初見の語を分解して読むため。
  紛らわしい対: biannual（年2回）と biennial（2年に1回）、autograph（有名人のサイン）と
  signature（書類の署名）、overhear（意図せず耳に入る）と eavesdrop（盗み聞き）。
- 第26弾 plus26.ts（91語）re- / semi- / sub- / super- / sur- / trans- / un- / under- の語:
  reassemble、reassess、recapture、reconnect、reconsider、redefine、rediscover、redistribute、refuel、
  regroup、reignite、reinstall、reinterpret、reintroduce、relaunch、relive、remarry、rename、reopen、
  rephrase、reschedule、reshape、restate、restructure、resurface、retell、rethink、retrain、reunite、
  reuse、revisit、rewrite、semicircle、semiconductor、semifinal、subcommittee、subconscious、subculture、
  subdivide、subheading、submarine、subsection、subset、subtitle、supermarket、supernatural、superpower、
  surcharge、surname、transatlantic、transcribe、unambiguous、unarmed、unassuming、unattended、
  unauthorised、unavailable、unaware、unbeaten、uncommon、unconvincing、undecided、undeniable、
  underpaid、underrated、understaffed、understate、underway、undesirable、undisputed、uneven、
  unfamiliar、unfit、unhelpful、unidentified、uninterested、unjust、unlawful、unlimited、unlock、
  unofficial、unpaid、unpredictable、unqualified、unrealistic、unreasonable、unreliable、unresolved、
  unsafe、unsatisfactory、unsuccessful
  紛らわしい語を注記: **uninterested（関心がない）と disinterested（利害がなく公平な）**、
  unqualified は「資格がない」と「無条件の・文句なしの」という正反対に見える二義を持つ、
  not uncommon（わりとよくある）のような二重否定の控えめ表現。
- 第27弾 plus27.ts（72語）人を表す -er / -ant、状態の -ship / -hood、性質の -ity / -ance、主義の -ism / -ist:
  carer、caregiver、dweller、examiner、interviewer、lodger、mourner、occupant、onlooker、organiser、
  pedestrian、performer、respondent、voter、accountancy、companionship、craftsmanship、dictatorship、
  fellowship、guardianship、workmanship、brotherhood、livelihood、motherhood、parenthood、adulthood、
  brutality、civility、disparity、elasticity、entirety、eternity、extremity、ferocity、fidelity、
  fragility、humility、ingenuity、insanity、intimacy、irregularity、locality、mentality、mortality、
  nationality、nobility、normality、parity、annoyance、elegance、fragrance、observance、perseverance、
  radiance、resonance、utterance、vengeance、vigilance、consumerism、feminism、heroism、idealism、
  liberalism、materialism、nationalism、patriotism、pessimism、realism、socialism、vandalism、
  vegetarianism、idealist
  接尾辞の対応を明記した（-er が「する側」／-ee が「される側」、-ism が主義／-ist がその人、
  -hood と -ship はどちらも「〜であること・集団」）。
  紛らわしい語: humility（謙虚さ）と humiliation（屈辱）、ingenuity（創意）と ingenuous（純朴）、
  observance（順守）と observation（観察）、carer（英）と caregiver（米）。
- 第28弾 plus28.ts（94語）動詞・形容詞と前置詞の結びつき、数量・理由の連語:
  account for、allow for、answer for、ask after、attend to、believe in、belong to、care for、
  come across as、concentrate on、consist of、cope with、depend on、dispose of、engage in、focus on、
  hear from、hear of、hope for、insist on、interfere with、invest in、lead up to、long for、
  look back on、look out for、object to、occur to、provide for、react to、refer to、relate to、
  resort to、result from、result in、stem from、stick with、succeed in、suffer from、think of、
  watch out for、work on、worry about、yearn for、aware of、capable of、conscious of、content with、
  critical of、curious about、dependent on、eligible for、essential to、familiar with、guilty of、
  immune to、inherent in、keen on、liable for、loyal to、notorious for、obsessed with、opposed to、
  proud of、relevant to、reliant on、responsible for、sensitive to、similar to、suitable for、
  superior to、suspicious of、typical of、vulnerable to、worthy of、a great deal of、a handful of、
  a number of、a range of、a series of、a variety of、an array of、in danger of、in need of、
  in search of、on account of、on the basis of、with the exception of、for the purpose of、
  by means of、in the absence of、in the course of、in the light of、with a view to
  **前置詞を間違えると通じないので、どれをとるかを一語ずつ覚えるヒントに書いた**。
  向きが逆になる対に注意: result from（〜が原因で生じる）と result in（結果として〜になる）、
  be familiar with（自分が知っている）と be familiar to（相手に知られている）、
  hear from（連絡をもらう）と hear of（うわさに聞く）、
  liable for + 名詞（責任がある）と liable to + 動詞（〜しがち）。
  than ではなく to をとる語: superior to、inferior to、similar to。
- 第29弾 plus29.ts（112語・最終）話をつなぐ慣用表現と、身のまわりの具体名詞:
  as a matter of fact、as far as I know、at any rate、in a nutshell、in other words、in short、
  in brief、needless to say、not to mention、so to speak、that is to say、to be honest、
  to put it simply、what is more、above all、after all、at most、at once、at present、by chance、
  by contrast、by far、for good、for now、for the time being、in detail、in effect、in practice、
  in public、in theory、in turn、of course、on time、once and for all、so far、sooner or later、
  to some degree、up to a point、without doubt、more or less、as such、if anything、let alone、
  no wonder、on the one hand、on the other hand、to say the least、acorn、antler、cocoon、gill、hive、
  beehive、mane、pouch、talon、whisker、clover、daffodil、daisy、ivy、lily、lotus、orchid、sunflower、
  tulip、cage、cushion、funnel、jar、jug、lantern、lever、mat、oar、paddle、pillar、plank、saddle、
  spade、bib、blouse、bracelet、brooch、cardigan、cloak、earring、gown、handkerchief、hood、jumper、
  knot、lace、necklace、pendant、robe、sash、stocking、strap、tights、trousers、veil、vest、waistcoat、
  wig、zip、gauze、sling、splint、swab、thermometer、tweezers
  英米差が大きい衣類の語を注記した: jumper（英セーター／米ジャンパースカート）、
  vest（英肌着／米ベスト）、waistcoat（英）= vest（米）、trousers（英）= pants（米、英では下着）、
  zip（英）= zipper（米）。読みの落とし穴も: knot の k、brooch は /broʊtʃ/、waistcoat は /ˈweskoʊt/。

## この増補で分かったこと

- 既存4,500語は Oxford 5000 系の抽象語・学術語に寄っていて、**日常の具体語と基本語に穴があった**。
  作業中に見つかった抜けの例: expensive、dangerous、famous、natural、personal、quiet、compact、
  scissors、drawer、wallet、kettle。派生形を機械的にたどる作業が、基本語の穴を掘り当てるのに有効だった。
- 候補の未収録判定は **id・見出し語・英米つづり**の三つで突き合わせないと重複が混ざる。
- 例文と語幹の検査（`scripts/check-vocab.mjs`）が最も多くのミスを拾った。とくに連語と不規則動詞。
- 英語欄への日本語混入は CJK 検査で自動的に落とせるが、**日本語欄への英語混入は自動判定できない**
  （hyphen や synonym は訳文で英語を引くのが正しい）。目視一覧として出す形に落ち着いた。
