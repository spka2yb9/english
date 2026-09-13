# 英単語の記憶イラスト

「覚えるヒント」の先頭に、単語ごとの静止画と記憶のための説明を表示する。
画像は回答後だけ表示し、未作成の単語では既存のヒントをそのまま表示する。
対応表は `src/content/vocabulary/illustrations.ts`。単語IDをキーにする。

## 作り方（現行の工程）

画像生成モデルは使わない。1単語1枚の**手書きSVG**を `public/images/vocabulary/<word>.svg` に置く。
文法レッスンの挿絵（`src/components/illustrations/primitives.tsx`）と同じ絵柄・同じ配色にそろえる。

0. 生成スクリプトは `scripts/vocab-illustrations/`。`lib.py` に共通部品（配色・人物・手・太陽・箱・一覧HTML）があり、
   回ごとに `batchNN.py` を作って `from lib import *` → `emit(word, alt, body)` で書き出す。
   第168回以降は `kit.py` を使う。`lib.py` に加えて、毎回書き写していた小物（表・矢印・記号・書類・棒グラフ・天秤・時計ほか）と
   `add(slug, alt, caption, body)` / `finish(__file__)` を持つ。`from kit import *` すれば一覧HTMLと
   `illustrations.ts` 追記用のJSONが `/tmp/batchNN.{html,json}` に出る。
1. 単語の語義を `src/content/vocabulary/` の該当エントリで確認する。語義とずれた場面は描かない。
2. 場面を1つに絞る。コラージュや複数コマにしない。「その語だけに当てはまる動き」を1つ選ぶ。
3. SVGを書く。規約は下記「SVGの規約」。図形は `primitives.tsx` のパスを流用してよい。
4. `sheet(words)` で一覧HTMLを作り、ブラウザで目視確認する（chrome-devtools MCP で `file://` を開く）。
   一発で読める絵はまず出ないので、読み取れない語は描き直して再確認する。ここが作業時間の大半。
   描き直しは `batchNNb.py` に分けて置く（`batchNN.py` を上から順に実行すると最終版になる）。
5. `illustrations.ts` に `src` / `alt` / `caption` を追加する。alt は絵の見た目の説明、caption は語義の説明。
   `kit.py` を使った回は `node scripts/vocab-illustrations/append-ts.mjs /tmp/batchNN.json ...` で追記できる。
   同じキーが複数の JSON にあれば、あとに渡したもの（描き直し）が採用される。
6. `npx tsc --noEmit` と `npx vitest run src/content/content.test.ts src/pages/Vocabulary.test.tsx` を通す。

### SVGの規約

- `viewBox="0 0 600 400"`（3:2。`VocabularyMemoryImage` が想定する比率）。
- `<img>` で読むので App.css は効かない。各ファイルの `<style>` に配色を直書きして自己完結させる。
- `role="img"` と `aria-label` に `illustrations.ts` の alt と同じ文を入れる。
- 配色は App.css の挿絵パレットに合わせる。背景 `#fffaf1`、線 `#2f4055`、地面 `#edf3ed`、
  teal `#238b83`/`#dff4ef`、blue `#4e86c6`/`#e1edfb`、gold `#d99a2b`/`#fff0c5`、
  green `#4e986a`/`#e1f3e5`、coral `#e86452`/`#fde9e3`、violet `#816eb2`/`#eee8fb`。
- 線は `stroke-width: 3`、`stroke-linecap`/`stroke-linejoin` は `round`。
- 文字は入れない（学習者の母語に依存させない）。矢印・点線は動きを示す最小限にとどめる。
- 単語間で意味が対になるもの（borrow / lend など）は、色と構図をそろえて対比が読めるようにする。

## 作成済み

**8,000語すべて**。`public/images/vocabulary/<word>.svg` に1語1枚あり、未作成の語はない。
対応表は `illustrations.ts`。

第6回以降は語の選定に `scripts/vocab-illustrations/candidates.py` を使う。
語義・品詞・レベルから具体度を推定して、描ける順に並べるだけの補助スクリプト。
未作成の語だけを出すので、`python3 scripts/vocab-illustrations/candidates.py 0 60` で次のバッチを選ぶ。

- 第1回: absorb、abandon、accept、achieve、adapt、avoid、borrow、lend、expand、protect、gather。
- 第2回: illusion、reflect、balance、connect、separate、attract、discover、escape、support、transform。
- 第3回: fluid、dissolve、melt、spill、leak、drift、fragile、shrink、fade、bend。
- 第4回: climb、crawl、dive、jump、throw、catch、push、pull、lift、hang、cut、dig、plant、mix、weigh、
  empty、rise、fall、wide、narrow、deep、heavy、straight、bridge、tunnel、ladder、nest、whisper、shout、swim。
  （`scripts/vocab-illustrations/batch04.py` → `batch04b.py`）
- 第5回: boil、stream、pump、tie、enter、exit、cross、block、lock、knock、press、burn、cool、dry、wet、
  thick、thin、flat、curved、mirror、gate、rope、wheel、spring、filter、seed、root、branch、leaf、path。
  （`scripts/vocab-illustrations/batch05.py` → `batch05b.py`）
- 第6回: blow、collect、cycle、fish、pick、receive、ship、smile、train、wind、bake、bite、divide、feed、fire、
  hand、pour、remove、shine、shut、soft、store、water、wooden、ankle、applaud、assemble、bin、bind、bury。
- 第7回: sink、strange、trick、airline、align、architect、athlete、blank、blast、blend、cartoon、carve、check、
  cloud、coast、collapse、dark、dip、drive、drop、erupt、fan、fly、furniture、gaze、glance、goal、grab、grin、headache。
- 第8回: close、cooker、distinguish、dressed、fail、handle、high、low、insect、knife、lab、lead、leap、lemon、
  listener、monkey、musician、observe、owner、painter、parking、patrol、plate、private、recognize、retreat、ride、
  seize、serve、breed、cheerful。
- 第9回: silver、size、sky、slap、soap、soar、sock、spark、split、spread、spy、stamp、stare、stir、stone、strip、
  stumble、tap、tear、tool、toss、tower、trail、truck、uniform、van、wash、weight、wood、bride。
- 第10回: assist、assistant、available、betray、compliment、conquer、convey、cope、covered、demonstrate、
  dominate、embark、ensure、entire、execute、grasp、historical、imaginary、indirect、intelligent、
  international、keen、local、obtain、organization、overlook、physical、practical、perceive、obsess。
- 第11回: donate、edit、foreign、helpful、pleased、rent、survive、united、appreciate、aspire、reasonable、
  sack、satisfied、smart、specific、speech、spoken、submit、suit、supplement、surrender、terminate、
  tolerate、use、vehicle、withdraw、witness、abroad、absent、act。
- 第12回: washing、actual、addition、affordable、allow、alternative、amount、appear、appearance、apply、
  arrangement、artistic、attack、awkward、beat、bilingual、blind、board、book、brief、broad、brush、camp、
  cap、care、celebrate、chain、chat、circle、clue。
- 第13回: bar、charity、climate、clumsy、coach、coal、community、competitor、complain、complaint、concrete、
  container、continue、control、copy、cottage、cry、deal、desert、destination、device、dirt、domestic、
  download、dream、dumb、elaborate、employment、entrance、place。
- 第14回: arrange、conduct、entry、ethical、exotic、expect、experience、experiment、experimental、expert、
  faithful、fear、fight、figure、fitness、flavor、formal、functional、fur、gap、garage、glove、greet、guide、
  handy、harsh、heat、hit、hold、hollow、homeless。
- 第15回: initial、innocent、instrument、internal、invent、invisible、invite、item、joke、junior、kill、
  laboratory、lack、land、level、liquid、loyal、magic、mail、marine、mark、marry、matter、medium、mention、
  may、humanitarian、infamous、instrumental、intended、legendary、disabled。
- 第16回: mixture、needle、notice、offer、operation、organize、overseas、own、pack、pass、perform、photograph、
  photographer、pile、pointed、population、pot、prayer、print、productive、program、promise、pronounce、
  prominent、noble、notable、notorious、municipal、naval、oral、mind。
- 第17回: purpose、question、race、random、reach、realistic、reality、record、recycle、refer、remarkable、
  reply、report、rest、ring、route、routine、ruin、sail、sailor、save、scan、scenery、script、seat、seem、
  shake、sincere、racial、renowned、number、need。
- 第18回: slice、smell、smoke、soil、sole、solid、sort、speed、stage、standard、star、state、steady、step、
  stiff、strength、stretch、striking、substantial、surgical、surprise、taste、tender、term、text、tip、tour、
  transport、trouble、verbal、view、track。
- 第19回: visible、vital、wave、weapon、wish、worry、yard、able、account、active、activist、admire、admit、
  adult、advise、age、aim、aircraft、alarm、alive、alone、ambulance、analyse、announce、annoy、apparatus、
  arms、arrest、asleep、assistance、association、attach。
- 第20回: auto、awful、back、balloon、base、based、bomb、breakthrough、breathe、bright、broken、bug、bush、
  calculate、cancel、careful、carriage、catalogue、centre、certain、chase、cheat、classical、clear、clever、
  click、closed、collector、combine、comfortable、communicate、compete。
- 第21回: composer、concentrate、confirm、confuse、connected、consider、consist、contain、content、convince、
  counterpart、coverage、crazy、critic、crowded、crystal、curly、currently、cutting、daily、dead、decorate、
  deficiency、deficit、delay、deliver、demonstration、depend、deposit、descent、describe、destroy。
- 第22回: disagree、disappear、dislike、divorced、dose、downstairs、earn、educate、electric、electronics、
  emergence、employ、encourage、entertain、enthusiast、equipment、establishment、estate、everyday、examine、
  exchange、execution、exist、expertise、explode、export、express、face、fair、fancy、fantasy、favour、
  feature、fee。
- 第23回: file、firearm、firework、fit、fix、flavour、fleet、flood、forward、foundation、freeze、fresh、fry、
  fun、further、gear、general、gig、grade、grocery、guard、head、heel、hide、highway、hire、historian、
  honesty、host、household、hunt、hurry、hydrogen。
- 第24回: ignore、ill、implementation、improve、include、included、increase、inform、informal、injure、insist、
  intend、intent、interrupt、introduce、involve、iron、jet、key、kick、kiss、labor、landlord、landmark、lane、
  later、lay、lazy、lie、limb、load、loud。
- 第25回: lovely、lucky、mainland、market、means、medical、missile、missing、monk、moral、morality、motorist、
  murder、navigation、necessary、nervous、noisy、note、novelist、obesity、objective、occur、operator、
  opponent、ordinary、organ、outfit、outlet、outsider、package、packet、ideology。
- 第26回: palm、participate、particular、persuade、pin、plot、poison、pray、prefer、pretend、prevent、
  procedure、provide、publish、punish、queue、quit、racism、react、realization、receiver、recommend、recover、
  reduce、refund、refuse、register、regret、rely、remain、point、ought、placement。
- 第27回: remains、remind、repair、repeat、replace、reporting、represent、require、resort、respond、retire、
  reunion、ritual、rival、roll、rose、safe、sake、satisfaction、scale、scary、set、share、shelter、shipping、
  shore、shortage、simple、simulation、sincerity、skull、slow、solve。
- 第28回: spare、specialist、species、spokesman、spokesperson、stall、steal、steam、stick、strain、stupid、
  submission、substance、succeed、suffer、suggest、suite、surgery、surprised、surprising、switch、tactic、tank、
  teenage、tenant、terminal、terror、texture、therapist、thread、threshold、tide、tidy。
- 第29回: timber、trade、trailer、translate、transportation、treat、troop、type、typical、underground、
  unhappy、unusual、update、upstairs、usual、vacuum、value、vessel、volunteer、vote、warm、warn、weak、wild、
  wonder、workforce、working、worm、worried、wrist、ability、abuse、accelerate、accident、accommodate。
- 第30回: accomplish、accumulate、accurate、activate、additional、address、adhere、administer、adventure、
  advertise、advertisement、advocate、afford、after、aged、allege、allocate、along、alter、amazed、amend、
  analyze、ancient、annoyed、annoying、annual、anticipate、anybody、anywhere、apologize、app、appoint、
  approach、architecture。
- 第31回: army、articulate、artificial、assault、assert、assess、assign、attain、attend、attention、attractive、
  attribute、author、average、await、background、baseball、basic、basketball、bean、beef、before、beg、behave、
  behaviour、belong、belt、best、bet、better、bid、birth、arm、academy、allowance。
- 第32回: biscuit、bit、blame、bleed、bless、blood、boast、bone、boost、boss、bother、bottom、bounce、bow、
  bowl、brain、brave、breach、briefly、broadcast、businessman、button、camping、carpet、case、cash、cast、
  castle、cater、cease、celebrity、central、chance、character、charge、chart。
- 第33回: cheer、chef、chip、choice、chop、church、cigarette、circulate、cite、claim、clarify、classify、cling、
  clothing、code、coincide、collaborate、coloured、column、combat、comfort、command、commence、commit、compel、
  compensate、compile、complement、complicated、comply、comprise、compromise、compute、conceal、concede、
  conceive、condemn、confess、confident、confine、confront、confused、congratulate、consent、conserve、constitute。
- 第34回: consult、contemplate、contend、continent、continuous、contract、convenient、convert、convict、cook、
  cooperate、coordinate、corner、correlate、correspond、count、couple、crack、crash、cream、creative、creep、
  criticize、crowd、cruel、cruise、crush、cultivate、cupboard、curious、current、curve、danger、dare、date、
  death、decision、decline、decrease、deem、defeat、defend、definite、dear。
- 第35回: defy、delete、denounce、dentist、depart、depict、deploy、deprive、derive、descend、deserve、
  designate、designer、detain、detect、detective、determine、determined、devastate、develop、devise、devote、
  diagnose、diary、dictate、differ、differentiate、digital、diminish、direction、director、disappoint、
  disappointed、disappointing、discard、discharge、disclose、discourage、displace、dispose、disrupt、distort。
- 第36回: distract、distress、distribute、disturb、divert、divorce、double、draft、drain、drama、drawing、
  driving、drown、drug、drunk、dub、dump、earth、ease、eastern、echo、educated、education、educational、
  effect、effective、either、elderly、elect、electricity、electronic、elevate、eliminate、embarrassed、
  embarrassing、embed、embody、embrace、emotional、emphasize、enact、encompass。
- 第37回: ending、endorse、endure、energy、enforce、engaged、engineer、enhance、enormous、enquire、enrich、
  enrol、ensue、enthusiastic、environmental、equal、equip、erect、essential、evacuate、evaluate、evoke、exact、
  exaggerate、exceed、excellent、except、exclude、excuse、exert、exhibit、expected、experienced、expire、
  exploit、expose、extend、extreme、facilitate、factory。
- 第38回: familiar、far、fascinating、fashion、fashionable、fasten、fat、fiction、field、final、financial、fine、
  finger、finish、first、fixed、flash、flee、float、flourish、flow、flu、flying、focus、fold、folk、following、
  forbid、forest、forge、forgive、fork、formulate、foster、free、fridge、frighten、frightened、frightening、frog。
- 第39回: frozen、fulfil、fulfill、furthermore、gallery、gas、generate、generous、gentle、gift、glad、global、
  god、gold、golf、good、grass、grateful、grind、grip、ground、guarantee、guest、guilty、gun、guy、habit、hail、
  hall、halt、haunt、heal、heart、height、heighten、hero、hers、herself、hesitate、hill。
- 第40回: himself、hint、his、historic、hockey、hole、homesick、honest、honour、hope、horrible、house、huge、
  human、hurt、ideal、identify、illness、illustrate、immediate、implement、import、impose、impress、imprison、
  inconvenience、incorporate、incredible、incur、indeed、independent、indicate、individual、indoor、induce、
  indulge、infect、inflict、inherit、inhibit。
- 第41回: initiate、inject、injured、insert、inside、inspect、inspire、install、instruct、instructor、insult、
  interact、interfere、interpret、intervene、introduction、invade、invention、invest、investigate、invoke、
  isolate、itself、jail、jam、jazz、jewellery、journalist、kid、kidnap、kind、king、knee、lake、lamp、laptop、
  last、latest、laughter、lawyer。
- 第42回: leader、leading、learning、least、less、lifestyle、likely、line、linger、literally、live、lobby、
  located、log、lonely、look、loom、loose、lorry、lower、luck、mad、maintain、manage、manager、manifest、
  manipulate、manner、manufacture、map、march、master、mate、material、mathematics、maths、media、medicine、
  memory、mental。（literally、lonely、loose、lower、manager、manipulate は `batch42b.py` で描き直し）
- 第43回: merge、metal、middle、mild、minimize、mistake、mobile、mobilize、model、modify、monitor、moon、
  motivate、motorcycle、movement、multiply、musical、myself、national、neck、neglect、negotiate、network、
  nod、noise、nominate、normal、northern、notify、novel、nuclear、nut、obey、object、oblige、obvious、
  occupy、ocean、odd。（model、musical、obvious は `batch43b.py` で描き直し）
- 第44回: mount、offend、officer、oil、operate、opportunity、oppose、opt、option、original、originate、
  ourselves、outdoor、outline、outrage、outside、oven、overcome、overturn、overwhelm、owe、pace、pain、
  painful、palace、pale、pants、passenger、patient、pattern、pause、peace、peaceful、penny、permission、
  permit、persist、pet、petrol、physics。（peace は `batch44b.py` で描き直し）
- 第45回: picture、pilot、pioneer、plain、planet、plastic、platform、plead、pleasant、pledge、plug、plunge、
  pocket、poisonous、polite、portray、pose、poster、postpone、praise、preach、precede、predict、pregnant、
  prepared、prescribe、present、preserve、presume、prevail、previous、price、printer、prize、probe、proclaim、
  produce、professional、professor。（pilot、plead、polite、praise、precede、pregnant は `batch45b.py` で描き直し）
- 第46回: profile、prohibit、promote、proper、propose、prosecute、proud、prove、provoke、pub、public、punch、
  purchase、pure、pursue、queen、quote、railway、raise、rally、rank、rare、reassure、rebuild、recall、recent、
  reception、recipe、reckon、recording、recount、recruit、regain、regard、regional、regular、reign、reinforce、
  reject。（railway は `batch46b.py` で描き直し）
- 第47回: relaxed、relaxing、relieve、religious、remark、render、renew、repeated、reporter、reproduce、rescue、
  researcher、resemble、reserve、reside、resign、resist、resolve、restore、restrict、resume、retain、retired、
  retrieve、reveal、revise、revive、rid、rip、rob、rock、romantic、roof、rotate、royal、rub、rude、runner、
  running。（relaxing、rescue、reserve、rude は `batch47b.py` で描き直し。rude は `person()` に負のスケールを
  渡すと上下反転してしまうため、向きは `facing` で指定する）
- 第48回: round、run、rush、sacrifice、sailing、salary、sale、satisfy、sauce、scare、scared、scientific、
  scream、screw、search、season、secondary、secret、secretary、seek、select、serious、several、sharp、shatter、
  shed、sheet、shiny、shocked、shoot、shoulder、shrug、sigh、silent、silly、similar、simulate、singing、side。
  （secret、silly は `batch48b.py` で描き直し）
- 第49回: single、sir、ski、skiing、skin、slam、slash、sleep、slide、smartphone、smash、smoking、smooth、
  snap、soak、soccer、social、soldier、somewhere、southern、span、speaker、specifically、specify、speculate、
  spicy、spider、spin、spoil、sponsor、spoon、square、squeeze、stabilize、stair、start、starve、stay、
  steadily、steer。（skin は `batch49b.py` で描き直し）
- 第50回: stab、stem、stimulate、stomach、storm、strict、strive、struggle、stun、substantially、successful、
  such、suck、sudden、sue、suitable、summarize、supervise、suppose、suppress、surge、surround、suspect、
  suspend、sustain、swallow、swear、sweep、sweet、swing、tablet、tackle、tag、talented、talk、teaching、
  temperature、temporary、tempt、terrify、testify。（suitable、swallow は `batch50b.py` で描き直し）
- 第51回: themselves、thief、thinking、third、thought、threaten、thrive、tight、time、tiny、title、top、
  torture、towel、toy、trace、trainer、training、transfer、transmit、trap、traveller、trigger、trip、trust、
  twin、twist、ugly、unable、uncomfortable、undergo、undermine、understanding、undertake、unfair、unfold、
  unit、unite、unlikely、unnecessary、unpleasant。（trigger は銃の絵を避け、押しボタンに `batch51b.py` で描き直し）
- 第52回: unveil、upgrade、uphold、upset、urge、used、user、utilize、valley、valuable、vanish、variety、
  various、verify、violate、violent、virus、voice、vow、wait、wander、war、weaken、web、wedding、welcome、
  western、whip、whole、widen、winner、wipe、worldwide、worse、worship、worst、wound、wow、wrap。
  （worse は `face()` を translate 済みの `<g>` 内で絶対座標で呼び、顔が画面外に出ていたので `batch52b.py` で描き直し）
- 第53回（2周目・B1/B2中心）: written、yell、yield、zero、absolute、abstract、absurd、acceptable、accessible、
  accommodation、accompany、accuse、acknowledge、acute、ad、adequate、adjacent、adjust、advanced、adverse、
  aesthetic、against、agent、aggressive、agreement、album、alcohol、alike、allergic、almost、already、ambition、
  ambitious、among、amusing、anniversary、announcement、anonymous、apparent、application、appointment。描き直しなし。
  このバッチで `abstract` に絵がついたため、`Vocabulary.test.tsx` の「絵のない語」の2語目を固定文字列からデータセット
  から拾う形に変えた（今後どの語を描いてもテストが壊れない）。
- 第54回: accountable、administrative、applicable、appropriate、approve、arbitrary、architectural、argue、
  argument、armed、arrival、ashamed、assignment、associate、associated、assume、assure、astonishing、
  atmosphere、attitude、audience、audio、authentic、automatic、award、aware、badly、balanced、bare、battery、
  battle、beauty、bee、behavior、belief、bell、beloved、bent、between、billion。描き直しなし。
- 第55回: bizarre、bold、border、bound、brand、breath、breathing、brutal、bubble、budget、burst、calm、
  campus、candidate、capitalist、captain、capture、carefully、casual、category、cause、cautious、ceiling、
  celebration、cell、ceremony、certainly、challenging、champion、channel、chapter、charming、chest、childhood、
  chronic、citizen、civic、civil、clause、clearly、client、coin。（cause は `flame()` を translate 済みの `<g>` 内で
  絶対座標で呼んでいたため `batch55b.py` で描き直し。絶対座標をとるヘルパーは `<g transform>` の外で呼ぶ）
- 第56回: communication、comparable、comparison、compelling、competent、competition、competitive、completely、
  complex、compose、comprehensive、compulsory、concerned、confidence、confusing、conscious、consecutive、
  conservative、considerable、considerate、consistent、constant、construction、contact、contemporary、
  contribute、conventional、convinced、cooperative、correctly、corresponding、corridor、corrupt、costly、
  costume、cotton、countless、countryside、courageous、credible、crime、criminal。描き直しなし。
- 第57回: crude、curtain、custom、cute、cynical、damage、damaging、deadly、decent、decisive、dedicate、
  dedicated、defensive、definition、degree、deliberate、delighted、delivery、demand、dense、departure、
  dependable、dependent、depressed、depressing、description、desirable、destructive、detail、detailed、
  development、diagram、diamond、differently、difficulty、diplomatic、direct、disadvantage、disaster、
  disastrous、discount。（delivery と dependable は `box()` を translate 済みの `<g>` 内で絶対座標で呼んで
  箱が画面外に出ていたため `batch57b.py` で描き直し）
- 第58回: diverse、divine、dizzy、document、documentary、dominant、doubt、drag、drum、dual、due、dust、
  dynamic、eager、earthquake、easily、edge、editor、effort、election、elegant、elementary、emerge、emergency、
  emotion、employer、encounter、endless。描き直しなし。ここで **2,000語** に到達。
- 第59回（目標を3,000語に更新して再開）: dishonest、dismiss、display、distance、distant、distinct、distinctive、
  disturbing、ecological、editorial、electoral、encouraging、enemy、engage、engaging、engineering、enjoyable、
  entertaining、entertainment、enthusiasm、episode、equivalent、error、especially、establish、estimate、eternal、
  ethnic、even、everywhere、evidence、evident、evil、exactly、exceptional、excessive、excitement、exclusive、
  exhibition、expedition、explanation。描き直しなし。
- 第60回: explicit、explosion、expression、extensive、external、extra、extraordinary、fabulous、failed、failure、
  farm、fatal、fault、favourable、feasible、federal、fellow、fence、fever、fierce、fighting、film、finally、
  firstly、flag、flawed、flexible、flour、folding、fond、forgetful、former、forthcoming、fortunate、fortunately、
  found、frequent、friendship、frustrated、frustrating、fuel、function、fundamental。
  （film は `person()` を translate 済みの `<g>` 内で絶対座標で呼び人物が画面外に出ていたため `batch60b.py` で描き直し）
- 第61回: furious、generation、generic、genetic、gentleman、genuine、ghost、giant、glorious、go、golden、goods、
  gorgeous、grain、grand、grant、graphic、greeting、gross、half、happily、happiness、harmful、hate、headline、
  heating、helicopter、hidden、highlight、hilarious、holy、hopeful、hostile、humble、humor、humorous、hurricane、
  identical、identity、ideological、image、imagination、imaginative、immature、immense、imminent、immune。
  （generic（`box()` の絶対座標）と gentleman（帽子が浮いて見えた）は `batch61b.py` で描き直し）
- 第62回: impatient、impressed、impressive、improvement、inadequate、inappropriate、including、incorrect、
  indifferent、indigenous、inevitable、inherent、injury、inner、innovative、instant、instead、insufficient、
  insurance、intact、integrated、intense、intensive、intention、interactive、interim、intermediate、intimate、
  invitation、involved、ironic、isolated、journey、judge、just、keyboard、killing、knowledge、label、latter、
  laziness、lean、leather、lecture、leftover、length、lengthy。（killing は `flame()` の絶対座標ミスで `batch62b.py` で描き直し）
- 第63回: lesser、lethal、liable、license、lifelong、like、limit、limited、linear、lip、literary、literature、
  little、lively、living、locate、location、loss、loudly、luxury、magnetic、magnificent、major、mall、mandatory、
  marginal、marketing、marriage、martial、massive、matching、mathematical、mature、mechanical、medieval、
  memorable、mere、mess、minimal、minor、minute、miserable、misleading、misunderstanding、mixed、moderate、
  modest。描き直しなし。
- 第64回: monthly、mood、mostly、move、moving、mud、multiple、muscle、mutual、mystery、nail、naked、narrative、
  nasty、nation、nationwide、native、nearby、nearly、neat、neighbourhood、neighbouring、nervousness、net、
  neutral、next、nor、normally、nowhere、numerous、obedient、occasion、occasional、offensive、official、ongoing、
  operational、opposed、optical、organic、organizer、ours、outer、outgoing、outstanding、overall。
  （muscle は腕の形が読み取れず2回描き直し、ours は `box()` の絶対座標ミス。ともに `batch64b.py`）
- 第65回: overwhelming、pan、parental、partial、passion、passionate、passive、past、payment、peculiar、per、
  percentage、performance、perhaps、permanent、persistent、persuasive、pessimistic、philosophical、photography、
  pipe、pity、planning、pleasure、plenty、plus、poem、poet、poetry、politeness、politician、pollution、port、
  powder、power、precious、precise、predictable、preliminary、premier、preparation、presentation、priest、
  primary、prime、prince。（preparation の `box()` 絶対座標ミスと、port/poetry に残っていた no-op 呼び出しは
  `batch65.py` を直して再生成した）
- 第66回: princess、principal、printing、prior、prison、prisoner、probable、problematic、proceed、producer、
  production、profound、progress、progressive、promising、prompt、pronounced、prospective、protection、
  protective、provincial、psychological、punctual、punishment、quantity、quietly、quotation、racing、radical、
  rapid、raw、reaction、receipt、recommendation、reduction、region、regulatory、relation、relative、release、
  relevant、reliable、relieved、religion、reluctant。描き直しなし。
- 第67回: range、remote、request、research、reservation、residential、respective、response、responsibility、
  responsible、revolutionary、ridiculous、risk、risky、robot、robust、role、rough、row、rugby、rural、sacred、
  sadly、safety、sample、sand、satellite、scattered、scene、sceptical、schedule、score、scratch、screen、
  sculpture、seal、second、secondly、section、secular、security、selective、senior、sensible、sentence、serial。
  描き直しなし。
- 第68回: servant、setting、settle、severe、sexy、shadow、shallow、shaped、sheer、shelf、shell、shock、shocking、
  sight、sign、significant、silence、similarity、site、situated、skilled、slight、slip、slowly、sociable、society、
  software、solar、sophisticated、sound、source、spectacular、sporting、spot、stable、stadium、staff、standing、
  stark、statement、statue、sticky、stranger、strategic、stress、strike。（stress の `box()` 絶対座標ミスを直して再生成）
- 第69回: string、structural、stubborn、studio、stuff、stunning、subject、subsequent、subtle、suburban、success、
  successive、sufficient、suggestion、summary、super、superb、superior、supporter、supportive、supreme、sure、
  survey、suspicious、symbol、symbolic、sympathetic、system、systematic、tactical、tail、talent、tape、target、
  task、technical、technique、technological、technology、tent、terrific、theatrical、theirs、theme、theoretical、
  thorough。描き直しなし（superb に残った no-op 呼び出しだけ削って再生成）。ここで **2,500語**。
- 第70回: thoughtful、thrilled、throat、throughout、till、timely、tin、toe、tongue、touch、tough、towards、
  toxic、tragic、translation、transparent、tremendous、trend、tribal、troubled、trustworthy、truth、tube、tyre、
  ultimate、unacceptable、unconscious、underlying、underwear、unexpected、unfortunate、unfortunately、union、
  unique、universal、unknown、unprecedented、upcoming、upper、urban、urgent、useless、vague、valid、vast。
  （tube が注射器に見えたので歯みがき型に `batch70b.py` で描き直し）
- 第71回: version、vertical、very、viable、vibrant、vicious、victim、viewer、virtual、visual、vocal、voluntary、
  vulnerable、warning、waste、wealthy、weekly、weird、whatever、widespread、will、willing、win、wing、wise、wool、
  worth、worthwhile、worthy、wrong、young、youth、abortion、absence、absolutely、abundance、accent、acceptance、
  access、accordance、accountability、accountant、accumulation、accuracy、accusation。
  （worth は `box()` の絶対座標ミス＋天びんの配置が窮屈だったため `batch71b.py` で描き直し。ここで w- まで一巡し、
  以降は A から B1/B2 の未描画語を拾う三周目に入る）
- 第72回: accused、acid、acquisition、acre、adaptation、addiction、adjustment、administrator、admission、
  adolescent、adoption、advantage、affect、affection、agency、aid、aide、aids、alert、alien、alignment、
  allegation、alliance、allocation、ally、aluminium、amateur、ambassador、amendment、analogy、analysis、analyst、
  ancestor、anchor、angel、anger、angle、animation、anxiety、anxious、apart、apology、appetite、applicant、
  appreciation。描き直しなし。
- 第73回: approval、approximately、archive、arena、array、arrow、artwork、ash、aspect、aspiration、
  assassination、assertion、assumption、assurance、asylum、atrocity、attachment、attempt、attendance、attorney、
  auction、audit、automatically、availability、awareness、backdrop、backing、backup、backwards、bacteria、badge、
  bail、ballet、ballot、ban、banner、barrel、barrier、basement、basket、bass、bat、battlefield、bay、beam。
  （aspect は `box()` の絶対座標ミス、bat は暗い背景に `class="ink"` の黒シルエットを置いて見えなかったため
  `batch73b.py` で描き直し。夜背景では図形を明るい灰色にする）
- 第74回: beast、behalf、being、bench、benchmark、benefit、besides、beyond、bias、biography、bishop、blade、
  blanket、blessing、bombing、bond、bonus、booking、boom、boundary、breakdown、breast、brick、broadband、
  broadcaster、browser、buck、buddy、buffer、bulk、bullet、bunch、burden、bureaucracy、burial、by、cabin、
  cabinet、cable、calculation、canal、cancer、candle、canvas、capability。描き直しなし。
- 第75回: capable、capacity、carbon、cargo、casino、casualty、cattle、caution、cave、cemetery、certainty、
  certificate、chamber、championship、chaos、charm、charter、cheap、cheek、chief、choir、chunk、circuit、
  circulation、civilian、civilization、clarity、clash、classic、classification、clerk、cliff、clinic、clip、
  closure、cluster、coalition、cocktail、coincidence、collision、columnist、comic、commander、commentator、
  commitment。描き直しなし。
- 第76回: commodity、commute、companion、compassion、compensation、competence、completion、complexity、
  complication、composition、concentration、concession、confession、configuration、confirmation、confrontation、
  confusion、congregation、conscience、consciousness、consensus、conservation、consideration、conspiracy、
  constantly、constituency、constitution、constraint、consultant、contempt、contender、contention、contrary、
  contribution、contributor、convenience、convention、conversion、conviction、coordination、coordinator、cop、
  copper、core、correction。描き直しなし。
- 第77回: correlation、correspondence、correspondent、corruption、counselling、counsellor、counter、county、
  coup、courage、courtesy、craft、creation、creativity、creator、creature、credit、crisis、criterion、criticism、
  critique、crop、crown、cue、cult、curiosity、currency、curriculum、dairy、dam、darkness、database、dawn、
  deadline、debris、debt、debut、decade、deck、declaration、decoration、dedication、deed、default、defect。
  描き直しなし。
- 第78回: discovery、disease、defence、defender、definitely、delegation、delicate、delight、demon、denial、
  density、deny、dependence、deployment、depression、depth、deputy、desire、desktop、despite、destruction、
  detection、detention、determination、devil、diagnosis、dictator、dignity、dilemma、diplomat、directly、
  directory、disagreement、disappointment、disc、discipline、disclosure、discomfort、discretion、
  discrimination、disk、dismissal、disorder、disposal、disruption、distinction、distribution。
  （distribution の `box()` 絶対座標ミスを直して再生成）
- 第79回: district、domain、dominance、donation、donor、dot、downside、downtown、dozen、drawback、drought、
  dull、duo、duration、edition、educator、effectively、ego、elbow、electrical、elite、embarrassment、embassy、
  emission、emphasis、empire、encouragement、endeavour、endorsement、endurance、enforcement、engagement、
  enquiry、entity、entrepreneur、envelope、environment、epidemic、equality、equally、equation、era、essence、
  ethic、evaluation、eventually、evolution。（dull に残った no-op 呼び出しを直して再生成）
- 第80回: comparative、constitutional、convincing、critical、crucial、examination、excellence、exception、
  excess、exclusion、executive、exile、existence、expansion、expectation、exploitation、exploration、explore、
  explosive、exposure、extension、extent、extract、extremely、eyesight、facility、faction、faculty、fairly、
  fairness、faith、fake、fame、fare、fate、favor、feather、feedback、fibre、finding、firefighter、fixture、
  flame、flaw、flesh、fool、footage、forecast、foreigner。（描き直しなし）
- 第81回: cover、realize、brilliant、raid、actually、appealing、empirical、light、home、pay、pop、shy、
  attraction、biological、biology、bitter、clinical、cloth、coastal、cognitive、colleague、collection、
  collective、colonial、colourful、combination、feel、force、forever、format、formation、fortune、forum、
  fossil、founder、fraction、fragment、framework、fraud、freedom、frequency、frequently、frustration、
  funeral、future。（fraud の仮面・forever の∞・fossil の化石・freedom の鳥を描き直し）
- 第82回: gallon、gambling、gaming、gang、gathering、gene、generally、generosity、genius、genre、gesture、
  glimpse、globalization、globe、glory、goodness、governor、grace、gradually、graduate、graphics、gratitude、
  grave、gravity、greenhouse、grid、grief、growth、guidance、guideline、guilt、gut、habitat、handful、
  handling、harassment、harbour、hardly、hardship、hardware、harm、harmony、harvest、hatred、hazard。
  （glimpse・gaming・gut・handling・guilt を描き直し。handling の「壊れ物」印は稲妻だと箱が割れて見えたのでグラス印に変更）
- 第83回: headquarters、healthcare、hearing、heaven、heavily、hell、helmet、herb、hesitation、hierarchy、hip、
  homeland、honor、hook、horizon、horn、horror、hostage、hostility、housing、humour、hunger、hunting、
  hypothesis、icon、id、identification、idiot、ignorance、illustration、imagery、immediately、immigrant、
  immigration、impossible、impression、imprisonment、inability、incentive、inch、incident、inclusion、income、
  independence、index。（hip・hunger・honor・horn を描き直し。horn は角がウサギ耳に見えたので稜のある湾曲した角に変更）
- 第84回: indication、indicator、indoors、inequality、infant、infection、inflation、info、infrastructure、
  inhabitant、injection、injustice、ink、innovation、input、inquiry、insertion、insider、insight、inspection、
  inspector、inspiration、installation、instance、instinct、institution、intake、integrity、intensity、
  interaction、interface、interference、interior、interpretation、interval、intervention、invasion、
  investigation、investigator、involvement、irony、isolation、jealousy、joint、journal。
  （injustice・inflation を描き直し。窓の並んだ高い建物 `tower()` を lib.py に移動）
- 第85回: journalism、joy、judgement、judgment、junction、jury、kidney、kingdom、kit、labour、lad、landing、
  landscape、lap、laser、lately、lawn、lawsuit、layer、layout、leadership、leaflet、league、legacy、legend、
  leisure、lens、liberation、liberty、licence、lifetime、limitation、link、listing、literacy、litre、litter、
  liver、loan、logic、logo、loneliness、loop、lord、lottery。
  （lap・loop・legend・kidney を描き直し。いすに座った人 `sit()` を lib.py に追加）
- 第86回: loyalty、lung、lyric、machinery、magnitude、mainly、mainstream、maintenance、majority、making、
  management、manipulation、manuscript、marathon、margin、marker、marketplace、mask、mass、maximum、mayor、
  meantime、meanwhile、measure、mechanic、mechanism、medal、medication、meditation、melody、membership、memo、
  memoir、memorial、mentor、merchant、mercy、merger、merit、metaphor、methodology、midst、migration、military、
  mill。（mask・metaphor・meantime・manipulation を描き直し。歯車 `gear()` と音符 `note()` はバッチ内に定義）
- 第87回: miner、mineral、minimum、minister、ministry、minority、miracle、misery、mission、mob、mode、
  modification、momentum、monopoly、monster、monument、mortgage、mosque、motion、motivation、motive、motor、
  myth、naturally、necessarily、necessity、negative、negotiation、nerve、newsletter、niche、nightmare、
  nomination、nominee、noon、norm、nostalgia、notebook、nursery、nursing、nutrition、obligation、observation、
  observer、obsession。（描き直しなし）
- 第88回: obstacle、occurrence、offence、offender、offering、offspring、opening、opera、opposition、orchestra、
  orientation、origin、outbreak、outcome、outdoors、outing、outlook、output、oxygen、pad、panel、panic、
  paperwork、parade、parallel、parameter、parish、participant、participation、partnership、passage、password、
  pastor、patch、patent、pathway、patience、patron、peak、peasant、peer、penalty、pension、perception、
  personnel。（opening のはさみ・oxygen の分子・peasant のくわを描き直し）
- 第89回: petition、phase、phenomenon、philosopher、philosophy、physician、pill、pipeline、pirate、pit、pitch、
  plea、pole、pond、popularity、portion、portrait、possession、poverty、practitioner、precedent、precision、
  predator、predecessor、prediction、pregnancy、prejudice、premise、premium、prescription、presence、
  preservation、prevalence、prevention、prey、pride、priority、privacy、proceeding、processing、programming、
  projection、promotion、proof、propaganda、proposal。
  （pill・predator・prey・plea・predecessor・presence を描き直し。いす `chair()` と四つ足のけもの `beast()` を lib.py に追加）
- 第90回: project、proposition、prosecution、prosecutor、prosperity、protein、protocol、province、provision、
  psychologist、psychology、publication、publicity、pulse、pupil、pursuit、puzzle、query、quest、
  questionnaire、quota、radar、radiation、rage、rail、ranking、rarely、rat、rating、ray、realm、rear、rebel、
  rebellion、recession、recipient、recognition、reconstruction、recruitment、referee、reference、referendum、
  reflection、reform、refuge。（prosperity・protein・radiation・rail を描き直し。放射線の三つ扇は内外半径を
  離さないと一塊に見える。まくら木は奥へ行くほど細くする）
- 第91回: refugee、refusal、regime、registration、regulation、regulator、rehabilitation、rejection、
  reliability、relief、reluctance、remainder、reminder、removal、rental、replacement、representation、
  representative、reproduction、republic、reputation、resemblance、resentment、residence、resident、residue、
  resignation、resistance、resolution、respect、restoration、restraint、restriction、result、retail、
  retirement、revelation、revenge、reverse、review、revision、revival、revolution、reward、rhythm。
  （resentment で `person()` を `<g transform>` の内側に書く例のミスをやり直し。revolution の王冠を180度回して×を添えた）
- 第92回: rhetoric、riot、rocket、rod、romance、rotation、rubber、rubbish、ruling、rumour、saint、sanction、
  saving、scandal、scenario、scholar、scholarship、scope、screening、scrutiny、seeker、segment、selection、
  self、seminar、sensation、sensitivity、sentiment、separation、sequence、series、settlement、settler、shade、
  shareholder、sibling、signal、signature、silk、sin、sketch、slave、slavery、slogan、slope。（描き直しなし）
- 第93回: secure、sensitive、shape、slot、solicitor、solidarity、solo、soul、spam、specification、specimen、
  spectacle、spectator、spectrum、speculation、spell、sphere、spice、spine、spotlight、spouse、squad、stance、
  steel、stereotype、stock、storage、strand、stroke、structure、subscriber、subscription、subsidy、substitute、
  substitution、suburb、succession、successor、suffering、superiority、supervision、supervisor、supply、
  surface、surgeon。（描き直しなし）
- 第94回: surplus、surveillance、survival、survivor、suspension、suspicion、sword、sympathy、symptom、
  syndrome、tale、teens、temple、tension、terrain、territory、testimony、testing、textbook、theft、theology、
  therapy、threat、thumb、timing、tobacco、toll、ton、tone、tournament、trademark、trading、traditional、
  transaction、transcript、transit、transition、transmission、trauma、treasure、treaty、trial、tribe、tribute、
  trophy。（thumb を2回描き直し。拳は縦長だと頭＋胴に見えるので横長にし、親指を左脇から立てた）
- 第95回: trio、triumph、trustee、tsunami、tune、uncertainty、undergraduate、unity、universe、utility、
  variable、vein、venue、verdict、verse、veteran、vice、victory、viewpoint、villager、violation、violence、
  virtue、visa、vision、vitamin、volume、voting、wage、ward、warehouse、warfare、warmth、warrior、weakness、
  wealth、weed、welfare、well、wheat、widow、tonne、trillion、robbery、spite。
  （violence を描き直し。拳だけでは読めないので袖と腕をつけた）
- 第96回: abolish、academic、acquire、adopt、advance、advertising、ahead、alcoholic、alongside、arise、
  authorize、barely、bargain、basis、beneath、beside、careless、chair、chemistry、colony、comedy、commission、
  conclude、conflict、consolidate、construct、consume、contrast、cultural、data、declare、define、
  deteriorate、discussion、dispute、downwards、elsewhere、empower、enable、entitle、escalate、evolve、
  farming、female、firm。（ここから名詞が尽きて動詞・副詞が中心になる。cultural を描き直し）
- 第97回: fishing、formerly、forth、freely、fully、gain、govern、greatly、halfway、highly、illegal、imply、
  increasingly、infer、initially、instantly、integrate、intensify、justify、lady、law、legal、likewise、male、
  maximize、merely、method、nature、newly、notably、nowadays、occasionally、openly、organized、otherwise、
  overly、overnight、oversee、partially、partly、permanently、political、positive、possess、powerful。
  （maximize・powerful を描き直し。四隅の矢印は中心を通すと×印に見えるので隅から外へ向ける）
- 第98回: incredibly、inevitably、ironically、largely、moreover、namely、nevertheless、precisely、presently、
  preside、president、primarily、purely、qualified、qualify、rapidly、readily、reasonably、regardless、
  regulate、relate、related、relatively、remarkably、respectively、roughly、seemingly、seldom、severely、
  shame、shortly、significantly、similarly、simultaneously、solely、somehow、sometime、somewhat、specialize、
  strengthen、strictly、subsequently、sufficiently、temporarily、thoroughly。（描き直しなし）
  副詞は「基準線＋そこからのズレ」「二枚並べて対比」「目盛りの振れ」の三型でほぼ描ける。
- 第99回: tighten、tourism、tradition、ultimately、unemployed、unify、upwards、utterly、vary、venture、
  versus、via、warrant、way、weave、whereas、wherever、widely、achievement、agricultural、bear、beneficial、
  bill、career、challenge、characteristic、chemical、comment、commercial、committee、communist、conclusion、
  condition、conference、connection、controversial、corporate、court、crew、customs、democratic、dramatic、
  duty、economic、economy。（tourism・versus を描き直し。文字は `text{display:none}` で出ないので
  「VS」のような字を図に置いてはいけない）
- 第100回: efficient、element、eligible、employee、engine、essay、evolutionary、factor、government、
  importance、inclined、industrial、industry、influence、influential、informative、ingredient、
  institutional、instruction、integral、intellectual、intriguing、irrelevant、judicial、launch、
  legislative、legitimate、logical、magical、meaningful、mysterious、optimistic、organizational、overtime、
  parliamentary、personality、policy、politics、position、possibility、potential、presidential、pressure、
  prestigious、process。（描き直しなし。登録 3,904 件＝SVG 3,904 ファイルで一致を確認）
- 第101回: publishing、qualification、ratio、reasoning、recovery、relevance、remedy、requirement、resource、
  revenue、say、scheme、sector、senator、sense、session、significance、sovereignty、spirit、sponsorship、
  stability、stake、statistic、status、stimulus、strategy、summit、surrounding、synthesis、taxpayer、
  tendency、tenure、terms、thesis、tissue、tolerance、tragedy、trait、transformation、transparency、
  tribunal、tuition、turnout、turnover、usage。
  （tuition を描き直し。taxpayer と「人→金→建物」の同じ構図になっていたので黒板と先生の場面に変更）
- 第102回: institute、integration、intelligence、investment、investor、issue、jurisdiction、justice、
  justification、legislation、legislature、liberal、lighting、likelihood、mandate、manufacturing、
  measurement、mining、mobility、nonsense、notion、objection、occupation、odds、optimism、ownership、
  parliament、perspective、poll、portfolio、preference、presidency、principle、privatization、privilege、
  probability、proceeds、processor、productivity、proportion、prospect、protest、protester、validity、
  variation。（描き直しなし）
- 第103回: have、might、please、shall、ah、as、can、mine、none、neither、since、while、whose、yet、yours、
  all、although、any、anyway、onto、though、now、obviously、once、originally、particularly、passing、
  perfectly、personally、possibly、previously、properly、recently、regularly、seriously、simply、skip、
  slightly、stand、strongly、successfully、suddenly、surely、tend、that。（描き直しなし）
  機能語は「時間軸上の点と範囲」「二択に○×」「破線で囲んだ所有」「薄く描いた別案」で表せる。
  ここで `candidates.py` が `[a-z]+` の id しか拾っておらず、句動詞やハイフン付きの語（take off、
  put up with、long-term など223語）を残数から取りこぼしていたことに気づいた。フィルタを外して修正。
  正しい残数は461語で、うち223語が句動詞・熟語。句動詞はむしろ絵にしやすいので次から着手する。
- 第104回: call back、check in、clean up、get up、go down、go up、hang up、wake up、come up、look through、
  pass on、pick out、sell out、stand out、take back、carry out、cut down、hand over、make out、pick up、
  pull over、sort out、speak up、check out、come back、come out、eat out、get back、get off、get on、get out、
  break down、break out、break up、bring up、build up、calm down、carry on、catch up、cheer up、come along、
  come across、count on、cut off、drop off。（描き直しなし）
  句動詞の id は空白やハイフンを含むので、`illustrations.ts` のキーは引用符で囲み（`'call back': {`）、
  SVG のファイル名は空白をハイフンに置き換える（`call-back.svg`）。登録は `/tmp/reg2.py` を使う。
  `candidates.py` の done 判定も引用符つきキーを拾うよう直した。
- 第105回: give back、go back、go on、go out、grow up、look out、look up、put away、put back、put on、
  slow down、stay up、take out、throw away、try on、turn off、turn on、write down、end up、fill in、fill out、
  get along、get away、get into、get through、get together、give away、give in、give off、give out、go ahead、
  go off、go over、go through、hand in、hand out、hang on、hang out、hold back、hold on、hold up、keep on、
  keep up、knock down、lay off。（描き直しなし。電球 `bulb()` とスイッチ `switch()` はバッチ内に定義）
- 第106回: back up、blow up、call off、come up with、cut out、deal with、find out、get rid of、give up、
  leave out、look back、look after、look forward to、make up、move in、move on、move out、pass away、
  pay back、pay off、pull out、put down、put out、put together、put up、rule out、run into、run over、
  set aside、set off、set out、settle down、shut down、stand by、stand for、stick to、take after、take down、
  take in、take on、take up、turn around、turn down、turn into、turn out。（描き直しなし）
  データセットの id は `find-out` のようにハイフンのものと `back up` のように空白のものが混在するので、
  登録時は id をそのままキーにする（勝手に正規化しない）。
- 第107回: high-profile、in fact、short-term、used to、line-up、all right、at random、old-fashioned、
  on the whole、out of date、per cent、up to date、according to、any more、as well as、at last、at least、
  full-time、large-scale、long-standing、long-term、long-time、non-profit、part-time、post-war、so-called、
  thought-provoking、apart from、as a result、as far as、as long as、decision-making、due to、film-maker、
  for instance、in addition to、in advance、in charge of、in common、in general、in particular、in return、
  in spite of、no longer、on average。（描き直しなし）
- 第108回: it、indictment、inmate、leave、lost、magistrate、on purpose、point out、punk、put off、rather than、
  run out of、self-esteem、set up、show up、therefore、this、totally、try、try out、turn up、typically、
  unless、unlike、upon、warm up、well-being、whenever、whether、whoever、whom、width、wildlife、willingness、
  wire、wisdom、wit、withdrawal、within、work out、workout、workplace、youngster、zone、accidentally。
  （描き直しなし）
- 第109回: accordingly、accurately、additionally、adequately、afterwards、albeit、allegedly、altogether、
  amid、annually、apparently、appeal、appropriately、aside、basically、break into、bring about、broadly、but、
  by no means、call for、characterize、closely、commonly、confer、consequently、considerably、consistently、
  continually、critically、deeply、deliberately、desperately、do without、dramatically、drop out、emotionally、
  entirely、essentially、exclusively、explicitly、extensively、fall apart、fall behind、firmly。（描き直しなし）
- 第110回: fundamentally、genuinely、get across、get around、get by、get over、hence、hopefully、however、
  in terms of、in the meantime、keep up with、let down、live up to、look down on、look into、look up to、
  make up for、nonetheless、on behalf of、predominantly、presumably、put up with、rather、regardless of、
  reportedly、still、supposedly、take off、take over、terribly、thankfully、thereafter、thereby、thus、truly、
  undoubtedly、use up、wear out、whatsoever、whereby、whilst、wholly、congressional、profession。（描き直しなし）
- 第111回: sexual、sex、gay、lesbian、profit、profitable、property、psychiatric、quality、rate、rational、
  relationship、rule、service、shift、situation、socialist、solution、specialized、spending、spiritual、
  statistical、steep、straightforward、sum、sustainable、tax、theory、total、treatment、tropical、
  unemployment、varied、accomplishment、activation、administration、aftermath、agenda、aggression、
  agriculture、assembly、assessment、asset、authority、autonomy。（描き直しなし）
  gay・lesbian は手をつなぐ二人とハートで、sex・sexual は♀♂の記号で描いた。茶化さず、記号と関係だけを示す。
- 第112回: beneficiary、campaign、capitalism、chairman、circumstance、citizenship、collaboration、
  commentary、commerce、commissioner、compliance、component、compound、concept、conception、consequence、
  consistency、consultation、consumer、consumption、contest、context、contractor、contradiction、
  controversy、copyright、corporation、council、councillor、credibility、cure、custody、dealer、debate、
  delegate、democracy、department、desperate、dimension、disability、discourse、diversity、division、
  doctrine、documentation。（disability を描き直し。車いすの記号は頭・座った体・車輪・足台を分けて描く）
- 第113回: affair、arguably、concern、earnings、economics、economist、effectiveness、efficiency、
  efficiently、enterprise、expenditure、expense、extremist、fabric、feat、feminist、figure out、finance、
  flexibility、formula、frame、franchise、frankly、fund、funding、fundraising、gender、governance、heritage、
  humanity、impact、implication、incidence、initiative、make、make-up、militia、potentially、sexuality、
  spokeswoman、vulnerability、warming、workload、workshop。（描き直しなし）
  これで既存4,500語のうち4,488語が完了。残り12語は暴力・性暴力に直結する語で、次回に扱い方を分けて決める。
- 第114回: rifle、shot、shooting、militant、guerrilla、terrorism、terrorist。
  暴力に関わる語は「人が傷つく場面」ではなく、物（銃）・跡（弾痕と規制テープ）・避難する人の動きだけで
  概念を示した。加害の主体は描かないか、顔のない影にとどめる。
  （rifle・guerrilla・terrorist を描き直し。銃は台尻を機関部に重ねないと浮いて見える。
  木陰の人影は幹より前に出して顔を見せないと茂みに見える）
  **描かないと決めた5語**: genocide、massacre、rape、suicide、racist。
  前4語は人が殺される場面そのもので、絵にしても記憶の助けにならない。racist は人種の描き分けが
  戯画になりやすい。いずれも登録しないので、アプリは既存の覚えるヒント文だけを表示する。
  **2026-09-12 追記**: このあと語彙データを 4,500語 → 7,500語 に増補したため、
  挿絵のない語が約3,000語ある（`docs/vocabulary-expansion.md` 参照）。
  第115回からはその3,000語を同じ手順で描いていく。
  **ファイル名の衝突に注意**: `make up`（句動詞・構成する）と `make-up`（名詞・化粧）は
  どちらも slug が `make-up` になり、あとから作ったほうが前の絵を上書きしていた。
  id からハイフンを作るときは、既存 slug と当たらないか `dup src` で必ず確かめる（化粧は `makeup.svg` に変えた）。

### 進捗

2026-09-12 時点で6,908語。第34回以降は抽象語が増えるため、矢印・対比・容器などの図式で意味の方向を示す絵が多い。第6回以降は `candidates.py` で描ける語を選び、1バッチ30〜46語で進めた。
第16回以降は目視での描き直しがほぼ不要になっている（人物・容器・建物・矢印などの共通部品が出そろったため）。

### 残りの進め方

目標は全4,500語。ただし一括生成はしない。1回30語前後のバッチで、1枚ずつ丁寧に描いて目視で直す。
機械的に量産した図は、意味とずれていても一見それらしく見えてしまい、覚え違いのもとになる。
その30語ぶんの手戻りを毎回受け入れるほうが、あとから全部見直すより安い。

- 1バッチ30語。うち3分の1程度は初回で読み取れないので描き直す前提で見積もる。
- 語の選び方は、まず具体物・動作・形状・位置関係。次に対になる語（push/pull、wide/narrow、
  enter/exit、whisper/shout、thick/thin、dry/wet）を必ずペアで作り、構図と色をそろえる。
- 抽象語は最後に回す。絵にしても記憶の助けにならないものは無理に作らず、
  `illustrations.ts` に載せない（未登録の語は既存の「覚えるヒント」がそのまま出る）。
- 共通部品は `lib.py` に足していく。人物・手・太陽・箱・炎・建物・温度計・木・水滴はすでにある。
  同じ絵柄を保つため、新しい小物も必ず lib 側へ足してから使う。

## 過去の経緯（画像生成モデル期）

第1〜3回は当初 imagegen スキルの `image_gen` で 3:2 のPNGを生成していた。
のちに全31語を手書きSVGへ差し替え、PNGは削除した。理由は、生成環境に依存せず、
差分レビューでき、拡大しても劣化せず、文法レッスンの挿絵と絵柄をそろえられること。

当時の生成プロンプトは記録として残してある。
alt と caption は流用できるので、新しい語を追加するときの下敷きに使える。

- [vocabulary-illustration-prompts.json](vocabulary-illustration-prompts.json)（第1回）
- [vocabulary-illustration-prompts-02.json](vocabulary-illustration-prompts-02.json)（第2回）
- [vocabulary-illustration-prompts-03.json](vocabulary-illustration-prompts-03.json)（第3回。この回のプロンプトは未使用）
- [vocabulary-illusion-refinement.json](vocabulary-illusion-refinement.json)（illusion の仕上げ）

## absorb の生成プロンプト（PNG期の記録）

```text
Use case: illustration-story. Asset type: one mnemonic illustration embedded in the '覚えるヒント' section of an English vocabulary learning app for Japanese adults. Primary request: illustrate ABSORB, meaning to take liquid into something, with a memorable image of plant roots absorbing water. One single coherent scene, not a collage, not panels. A small vivid green plant growing in a cutaway of warm brown soil; its pale branching roots visibly take in bright blue water droplets from the surrounding soil, with a few subtle directional blue strokes pointing INTO the roots. Above-ground leaves look fresh and healthy. Make the inward absorption unambiguous: droplets in soil approaching the roots, not falling out of the plant. Friendly polished editorial gouache illustration with clean silhouettes and soft paper texture, uncluttered warm ivory background, restrained teal, blue and warm ochre palette. Centered composition, generous margins, landscape 3:2 aspect ratio, clear enough at 400px wide. No text, letters, numbers, logo, or watermark. Save the generated image for use in the current workspace and return its artifact path.
```
- 第115回: 増補3,000語の挿絵の第1弾。台所・住まい・道具・身の回りの品45語。
  drawer、kettle、saucepan、frying pan、toaster、stove、freezer、mattress、pillow、wardrobe、
  bookshelf、stool、armchair、sofa、rug、bulb、socket、cord、charger、clock、calendar、glue、stapler、
  hammer、screwdriver、drill、saw、wrench、pliers、shovel、rake、hose、bucket、broom、mop、sponge、
  razor、comb、scissors、zipper、sleeve、collar、apron、scarf、sandal。
  （saucepan・mattress・pillow・stapler・pliers・scissors・zipper を描き直し。
  取っ手は本体から十分はみ出させないと見えない。まくらは真横から描くと皿に見えるので、
  少し傾けて厚みを出す。刃物は二枚の刃の交差が見えるように角度をつける）
  **多語の id はファイル名も両方でそろえる**: `emit('frying pan', ...)` と書くと
  `frying pan.svg`（空白入り）ができてしまい、登録側の `frying-pan.svg` と食い違った。
  emit の第1引数からハイフン形にすること。
- 第116回: 食べ物45語。loaf、crust、dough、noodle、pasta、dumpling、tofu、cereal、porridge、pork、
  bacon、ham、sausage、steak、shrimp、crab、lobster、oyster、squid、tuna、salmon、cabbage、lettuce、
  broccoli、cauliflower、celery、cucumber、pumpkin、eggplant、garlic、ginger、chili、mushroom、
  asparagus、pea、leek、peach、pear、plum、cherry、grape、watermelon、pineapple、strawberry、coconut。
  （pasta・pork・ginger・pear・dough を描き直し）
  **食べ物は淡い色で描くと形が消える**。パスタの麺、洋なし、しょうがはいずれも
  背景の生成り色(#fffaf1)に沈んだ。実物より一段濃い色を選び、輪郭線も入れること。
  果物や野菜は「まるごと＋断面」を並べると、形と中身の両方が伝わって分かりやすい
  （watermelon、peach、coconut、cucumber、garlic でこの型を使った）。
- 第117回: 体の部位・症状・手当ての道具45語。jaw、chin、forehead、eyebrow、eyelid、eyelash、nostril、
  gum、collarbone、fingernail、waist、thigh、shin、rib、pelvis、artery、intestine、thyroid、sneeze、
  cough、sniff、yawn、hiccup、shiver、sweat、itch、ache、sting、swell、bruise、limp、scar、blister、
  bandage、plaster、syringe、stretcher、wheelchair、crutch、capsule、ointment、thermometer、gauze、
  sling、splint。（jaw を3回、eyelid・collarbone・gauze を1回ずつ描き直し）
  **体の部位は「大きな顔や体＋矢印」の型でそろえる**と、どの語も同じ読み方で伝わる。
  この回でその型を確立した。顔は使い回すのでバッチ内に `bighead()` を置いた。
  **輪郭をなぞる線は、なぞる相手の座標をそのまま使う**。jaw で顔の輪郭とは別に描いたら
  線が顔の外に浮き、左右反転の transform を足したらさらにずれた。
  顔が (250,210) 中心・幅±106・あご先 y=322 と分かっているなら、
  `M146 188 Q146 320 250 320 Q354 320 354 188` と直接その数値で書けば一度で合う。
  症状は「人＋印」で描ける（かゆみは波線、痛みは放射線、寒さは雪の結晶）。
  swell のように程度を示す語は、**普通の状態と並べて矢印でつなぐ**と一目で分かる。
- 第118回: 生き物45語。snail、beetle、ant、wasp、moth、butterfly、mosquito、grasshopper、caterpillar、
  sparrow、pigeon、crow、eagle、owl、swan、duck、goose、rooster、turkey、parrot、penguin、toad、lizard、
  snake、turtle、crocodile、wolf、fox、deer、rabbit、squirrel、mouse、hedgehog、whale、dolphin、shark、
  goat、donkey、camel、elephant、lion、tiger、giraffe、zebra、paw。
  （mosquito・swan・wolf・lion を描き直し）
  **生き物は「横向きの輪郭＋その種だけの特徴」で描き分ける**。
  角(deer/goat)、耳(rabbit/donkey/wolf)、しま(tiger/zebra)、こぶ(camel)、首(giraffe)、
  背びれ(shark)のように、一つの特徴を大きく強調すれば体は共通の輪郭で足りる。
  この回で足を止めた落とし穴を二つ:
  - **頭を二重に描かない**。wolf で「頭」と「鼻づら」を別々の楕円で足したら顔が二つに見えた。
    頭は一つの形にして、鼻づらはそこから伸ばす。
  - **`<g fill>` の中に線だけの `<path d="M..l..">` を置いても何も出ない**。
    lion のたてがみを線で放射させようとして消えた。塗りで描くなら楕円などの図形を並べる。
  - **白い動物は水色の背景に沈む**。swan は水を濃くし、輪郭線を 3.5 に太くして分けた。
- 第119回: 植物・地形・天気45語。oak、pine、maple、birch、willow、bamboo、cactus、fern、moss、vine、
  shrub、hedge、trunk、twig、bud、blossom、petal、thorn、pollen、sap、bark、meadow、swamp、dune、canyon、
  plateau、ridge、creek、waterfall、glacier、iceberg、breeze、gale、thunder、lightning、sleet、frost、
  dew、mist、fog、drizzle、downpour、sunrise、sunset、dusk。（sap・oak・bud を描き直し）
  **地形は横から見た断面、天気は空の色で描き分ける**。
  地形は「地平線をどう折るか」だけで canyon（両側を切り落とす）・plateau（頂を平らに）・
  ridge（背を一本の折れ線に）・dune（波形に重ねる）が描き分けられる。
  天気は背景色そのものが情報になる。thunder は暗い灰、lightning は紺、frost は淡い水色、
  sunrise は下からオレンジ、sunset は上から紫、dusk は青紫、と空を塗り分ければ主役の形は少なくて済む。
  この回の落とし穴:
  - **幹だけを描くと板に見える**。sap を幹の切り口だけにしたら木の扉になった。
    木の一部を見せる語（sap、bark、trunk）でも、枝と葉を小さく残して「木だ」と分かるようにする。
  - **対比する語は隣に並べる**。bud は開いた花を隣に置いて矢印でつないだ途端に「まだ開いていない」が伝わった。
    mist/fog、thunder/lightning のように紛らわしい組は、片方の絵に他方との差を描き込む。
- 第120回: 台所・道具・体の動作48語。butter、snack、stew、simmer、grate、sprinkle、peanut、pinch、quench、
  sew、hem、sharpen、knot、stitch、zip、bolt、dismantle、crumble、ignite、flake、swab、hurl、jog、squint、
  weep、mumble、overhear、deaf、immerse、paddle、hike、detour、sidewalk、luggage、umbrella、boot、chicken、
  flock、herd、swarm、burrow、volcano、orbit、horizontal、gardener、ferry、shampoo、underline。
  （pinch・knot・hem・flake・burrow を描き直し、pinch と knot はさらにもう一度）
  台所ものが続くので `table(y)` を局所ヘルパーにした。天板と脚2本だけの4行で、
  butter から grate まで同じ机の上に並ぶので一覧に統一感が出る。
  この回の落とし穴、どれも二度手間になったので残す:
  - **手のひらを形（path）で描くと雲になる**。pinch を輪郭で描いたら二度とも綿になった。
    指は**線**で描く。太い `SKINL` の線の上に少し細い `SKIN` の線を重ねれば、それだけで輪郭つきの指になる。
    `finger(d, w)` として関数にした。
  - **結び目は縄だけでは描けない**。knot を縄のこぶや交差で描いても、ただの波かXにしかならない。
    「何かを縛った縄」にして初めて結び目に見えた。抽象的な形の語は、使われている場面ごと描く。
  - **動物を横長のかたまり一つで描くとなめくじになる**。burrow の中身がそうなった。
    第118回の「頭は一つに」と裏表で、頭・耳・足・尾は分けて描く。
  - **「はがれる」は落下中のかけらで見せる**。flake を壁の斑点で描いたら模様に見えた。
    めくれ上がった縁と、宙にある薄片を足すと動きが出る。
- 第121回: 家の設備・書類・様子を表す形容詞45語。faucet、countertop、dishwasher、microwave、dustbin、jug、
  doorway、driveway、hood、magnet、aisle、motorway、boarding、baggage、conductor、form、handwriting、blog、
  internship、interviewer、diet、exercise、clutch、condense、dehydrate、marinate、obstruct、pound、
  transplant、hop、giggle、furnish、expel、barren、fertile、cosy、dim、gloomy、conspicuous、deafening、
  hectic、jealous、selfish、luminous、brisk。（transplant・gloomy・exercise・boarding を描き直し）
  **形容詞は反対の場面を左右に並べる**。画面の真ん中に破線を1本引く `split()` を足した。
  barren/fertile、dim の明暗、condense の長短、dehydrate の前後、furnish の空室と家具入り。
  一枚の絵で「どういう状態か」を言い切るより、隣に反対を置くほうが早く伝わる。
  この回の落とし穴:
  - **もやや影を全面にかけると主役が消える**。gloomy に灰色の楕円をかぶせたら人が見えなくなった。
    暗さは背景色そのものと窓の雨で出し、覆いはかけない。
  - **横向きの人体は肉のかたまりになる**。exercise の腕立て伏せがそうだった。
    運動は立ち姿＋道具（ダンベル）にすると一目で分かる。
  - **似た形の絵を同じ回に入れない**。boarding のボーディングブリッジが baggage のベルトコンベアと
    見分けられなかった。タラップと乗り込む列に描き替えた。一覧で隣り合う語ほど形を離す。
- 第122回: 身のまわりの物と程度の形容詞46語。lime、raspberry、prawn、roast、radiator、ribbon、sneaker、
  staircase、submarine、toolbox、trolley、tutorial、prefix、pavement、shortcut、nurse、peek、splash、spend、
  subdivide、instigate、resurface、aimless、bleak、eccentric、fitted、formidable、fruitful、furtive、grim、
  joyful、laborious、lofty、mountainous、populous、porous、potent、prehistoric、scarce、seamless、secluded、
  shrill、smug、soggy、tedious、thrifty。（fitted・secluded を描き直し）
  形容詞が半分を占める回。`split()` の左右比較が効いたのは scarce（棚いっぱい／ほぼ空）、
  seamless（縫い目あり／なし）、fitted（だぶだぶ／ぴったり）、subdivide（4分割／16分割）、
  aimless（的に当たる矢／さまよう足あと）。**同じ物を二つ並べて片方だけ変える**のがいちばん伝わる。
  この回の落とし穴:
  - **服だけを人と別に描くと宙に浮く**。fitted のだぶだぶ側がハンガーの服に見えた。
    人の胴に直接だぶつかせる。`person()` を使わず胴と袖を手で描けば、ゆとりの量を自由に変えられる。
  - **「隠れている」を木で埋めると本当に消える**。secluded で家が完全に隠れた。
    家は手前の空き地に出し、囲いのほうを厚くする。隠れている語ほど主役は見せる。
- 第123回: 建物まわり・体の中・un-/non- の形容詞45語。attic、bungalow、boiler、bonnet、brake、cage、claw、
  beehive、alligator、antibody、appendix、applause、artefact、algorithm、blaze、brighten、chirp、chuckle、
  unarmed、understaffed、underweight、unfit、unidentified、unrealistic、upbeat、upright、versatile、volcanic、
  tangible、territorial、treacherous、truthful、steadfast、shrewd、resourceful、reactive、prohibitive、
  pragmatic、petty、outlandish、nonverbal、nonprofit、negligible、measurable、lucrative。
  （claw・versatile・bonnet を描き直し）
  **un-/non- の語は、split() の左右に「無い側」と「有る側」を置いて ×と✓ を打つ**。
  そのための `cross(x,y,s)` と `tick(x,y,s)` を足した。unarmed、unfit、upright、truthful がこれで片づいた。
  記号を足すだけで「どちらがその語か」が迷わず決まる。
  この回の落とし穴:
  - **肉球を真上から描くとパン生地になる**。claw がそうなった。横から見た足先にして、
    つめを長く曲げて輪郭の外へ突き出す。つめは「外に出ている」ことが形の本体。
  - **抽象的な形容詞は物より場面を並べる**。versatile を「多機能な道具」として描いたら
    ただの赤い棒になった。一本の道具から線を四方に伸ばし、それぞれの仕事を小さく描いたら通じた。
  - **部品を本体の外に置くと別の物になる**。bonnet でエンジンを車の横に描いたら機械の絵になった。
    開いた蓋の下、車体の中に収める。
- 第124回: 家族・車まわり・慣用表現46語。ancestry、breadwinner、extended family、eyewitness、famous、
  dashboard、fill up、gutter、draught、firewall、insulator、grill、defrost、delicious、dice、gush、fragrance、
  hiss、howl、fling、hold on to、disobey、idle、dazzle、eruption、demolition、excursion、gown、cuff、cushion、
  dangerous、inoculation、infestation、ingenuity、gauge、envy、emptiness、conquest、calibre、chromosome、
  clumsiness、demographic、draw the line、get the hang of、go the extra mile、eternity。
  （chromosome・gown・cuff を描き直し）
  家系図や人数の比較のために、顔と肩だけの小さな人 `head(x,y,r,shirt,hair)` を足した。
  `person()` の縮小版では細部がつぶれるが、これなら半径16pxまで下げても顔が読める。
  ancestry、extended family、breadwinner、demographic がこれ一つで描けた。
  複数語の見出しは **emit の第1引数をハイフンでつなぐ**（`extended-family`）。
  第115回の frying pan と同じ落とし穴で、スペースのままだとファイル名にスペースが入る。
  この回の落とし穴:
  - **細い曲線を4本並べると葉になる**。chromosome がそうだった。
    Xの字は太い棒を2本交差させ、中央をくびれさせる。形の芯を太くする。
  - **すそが広い服を三角形で塗ると円すいになる**。gown で起きた。
    肩・腕・首を残したまま、すそだけを床まで伸ばす。人であることを先に成立させる。
  - **服の一部だけを切り出すと箱になる**。cuff がただの白い長方形になった。
    そで口には腕と手を通す。体の部位を表す語は、つながっている体ごと描く。
- 第125回: 店・水回り・re- の動詞46語。inventory、labourer、optician、narrator、playwright、monastery、
  plumbing、patio、pier、kerb、sanitation、rinse、ripple、precipitation、poultry、salty、puberty、organism、
  reptile、massage、navigate、ramble、oversleep、rehearse、memorise、phrase、satire、lantern、lace、sash、
  pouch、reconnect、reconsider、reinstall、rename、reopen、repay、reschedule、rift、livestream、lodge、
  natural、nonstop、nuclear family、personal、preheat。（labourer を描き直し）
  **re- の動詞は split() の左右に「一度目 → 二度目」を置く**。
  reconnect（切れている／つながっている）、reinstall（消えた／戻った）、rename（元の名／新しい名）、
  reopen（閉店／開店）、reschedule（消した日付／新しい日付）。矢印一本で「もう一度」が出る。
  画面を描く語が増えたので `screen(x,y,w,h)` を足した。枠・画面・台座の3要素だけ。
  この回の落とし穴:
  - **担いだ荷物が顔にかぶさると人が消える**。labourer で袋が顔の真上に来て、
    正体不明のかたまりになった。荷物は顔の高さを避け、斜め上か横に置く。
    人が主役の絵では、顔だけは必ず何にも隠されない位置に確保する。
  この回で語彙データ側の事故も一つ直した。plus02 の rinse の meaningsJa に
  「すすぐ、water で洗い流す」と英単語が残っていた。同じ形の混入がほかにないか
  「日本語に挟まれた3文字以上の英字（かっこ書きを除く）」で全件走査し、これ一件だけと確認した。
- 第126回: 表情・音・歩き方45語。scowl、smirk、sob、tasty、under the weather、squeak、squeal、screech、
  shove、snatch、stride、stroll、tiptoe、trot、tumble、trickle、semiconductor、stocking、strap、subtitle、
  switch off、thermostat、tusk、vacancy、vaccination、vandalism、ventilation、void、whisk、whisker、
  wilderness、terrace、the tip of the iceberg、throw light on、steal the show、paradox、novelty、dosage、
  extremity、maturity、shorten、soften、spur、stick out、unlock。（spur を描き直し）
  ここで5,000語を超えた。
  **似た音の語は「音の出どころ」を変えて描き分ける**。音そのものは弧で表すしかないので、
  弧の数や太さを変えても区別がつかない。squeak はネズミときしむドア、squeal はブタ、
  screech は急ブレーキのタイヤ。何が鳴っているかで決まる。音の弧は `sound(x,y,n,色,倍率,向き)` にまとめた。
  歩き方の4語（stride / stroll / tiptoe / trot）も同じ考えで、
  歩幅（大股・普通・つま先）と足の数（人2本・馬4本）と背景（何もない・公園・忍び足の点線）で分けた。
  この回の落とし穴:
  - **乗り物と乗り手が重なると両方読めなくなる**。spur で馬上の人を描いたら茶色いかたまりになった。
    道具が主役の語では、道具（拍車つきのブーツ）を大きく前に出し、馬は小さく脇に置く。
    「誰が何をしているか」より「その語が指す物はどれか」を優先する。
- 第127回: 家族・家の中・句動詞45語。aunt、cousin、babysitter、baker、backpack、balcony、closet、couch、
  windowsill、berry、blueberry、crispy、creamy、ape、athletic、audition、autograph、bob、crumple、blacken、
  broaden、cloak、converge、contradict、abridge、alleviate、amplify、appraise、bolster、certify、broker、
  collate、corroborate、conform、counterattack、accidental、childish、century、comma、branch out、call in、
  chip in、come by、crop up、work on。（cloak を描き直し）
  **句動詞は前置詞の向きをそのまま矢印にする**。branch out は外向きの2本、call in は内向き、
  chip in は中心へ集まる3本、crop up は下から上、come by は横切る線。
  意味を絵で言い換えるより、前置詞の空間の向きを矢印にしたほうが速く伝わる。
  親族語のために `doc(x,y,w,h,lines)` も足した。書類は今後もよく出る。
  この回の落とし穴:
  - **体をすっぽり覆う服は、覆いきると人でなくなる**。cloak が紫のおばけになった。
    頭・顔・足先は必ず外に出す。「覆う」語ほど、覆われている中身を見せる。
    第122回の secluded（隠れている家を見せる）と同じ形の失敗。
- 第128回: de-/dis- の動詞と日常の名詞44語。crunchy、dessert、earring、dock、darken、dampen、deepen、dent、
  deserted、deter、devalue、deviate、disband、disguise、disinfect、dislodge、disperse、disqualify、distrust、
  diverge、divulge、disprove、decode、debug、decompose、dwindle、die down、ease off、drum up、draw up、
  dreadful、doubtful、eclipse、emit、energetic、enlarge、exhale、exhausted、entrust、quirk、oversight、
  litigation、emphasise、curb。（dislodge・dwindle・quirk を描き直し、dislodge はさらにもう一度）
  **de-/dis- は「元の状態 → 取り除いた状態」を split() の左右に置く**。
  disband（輪の中／散った）、disperse（密集／四方へ）、disguise（素顔／変装）、
  decode（記号／読める文）、decompose（緑の葉／黒い土）。
  -en で終わる動詞（darken、dampen、deepen）も同じ形で、程度の差だけを変える。
  この回の落とし穴:
  - **薄い色で塗った中身は白い背景に溶ける**。dwindle の水位が5杯とも空に見えた。
    量の変化を見せる絵では、中身を淡色（`bluep`）ではなく原色（`blue`）で塗り、器の輪郭を太くする。
  - **口の中や歯並びは描いても口に見えない**。dislodge を歯にはさまった物にしたら白い塊になった。
    靴底の溝と小石に替えたら一発で通じた。**体の内側より、身近な物の隙間で見せる**。
  - **癖は一度の動作では癖にならない**。quirk が「ノックしている人」で終わっていた。
    音の弧を3本にし、吹き出しに点を3つ並べて「毎回三回」と分かるようにした。
    習慣を表す語は、くり返しの回数を絵に出す。
- 第129回: 台所と手仕事、速さを変える動詞45語。jar、ketchup、honey、fillet、knead、knit、inscribe、imprint、
  intertwine、interconnect、hinder、impede、hasten、hoist、flatten、fluctuate、lengthen、foresee、forewarn、
  decree、defer、dissuade、deregulate、augment、apportion、bestow、fall out、get round to、hold off、folder、
  invoice、gram、guitar、hairdresser、hashtag、holiday、honeymoon、fuse、fracture、glimmer、inhabit、
  easygoing、fluent、fluffy、foolish。（描き直しなし）
  この回は一枚も描き直さずに済んだ。効いたのは**似た語をあらかじめ別の場面に振り分けてから描き始めたこと**。
  hinder（重い荷を引かされて遅くなる）、impede（道が狭まって流れが滞る）、obstruct（第121回、
  倒木で完全にふさがる）は日本語では全部「妨げる」だが、
  「遅くする／狭める／ふさぐ」と場面を先に決めれば絵は自然に分かれる。
  hasten はその反対側に置いた。
  なお `head()` を書き忘れて `NameError` で落ちた。バッチ間で使い回すヘルパーが増えてきたので、
  新しい batchNN.py を書き始めるときは前回のヘルパー定義をまるごと写してから中身を書く。
- 第130回: mis- と out- の動詞46語。misspell、misread、misinterpret、misjudge、mislead、miscalculate、
  misplace、mishandle、mismatch、misbehave、misuse、mistrust、outdo、outlast、outnumber、outperform、
  outsmart、outsource、outweigh、outdated、login、logout、mat、melon、menu、midnight、necklace、nephew、
  niece、orphan、lever、lessen、lighten、loosen、lure、magnify、mediate、minimise、moisten、mutter、omit、
  ooze、overcharge、let off、level off、liberate。（描き直しなし）
  接頭辞ごとに描き方を固定できた回。
  **mis- は split() の左右に「正しい／誤った」を置いて ✓ と × を打つ**。
  **out- は「相手と自分を並べて、自分の側だけを大きく・高く・多くする」**。
  outdo（高さ）、outnumber（数）、outlast（残り）、outperform（線の位置）、outweigh（てんびんの傾き）。
  比較の語は、比べる相手を必ず同じ絵の中に描く。
  **文字は `text` が display:none なので描けない。語は四角の並びで表す**。
  そのための `word(x,y,n,w,色,bad)` を足した。bad の位置だけ傾けて色を変えれば
  misspell の「一字だけ違う」が出る。login のパスワード欄の●もこれで描いた。
  この回の事故を一つ。書きかけのダミー `add('misspell-check','','')` を `W.pop()` で
  一覧から外したが、**emit() はその時点で既にファイルを書き出していた**ので
  `public/images/vocabulary/` に孤児ファイルが残った。登録後の
  entries / files 突き合わせで orphan として検出できたので削除した。
  この突き合わせは毎回やる価値がある。
- 第131回: over- の動詞と身のまわりの語45語。overdo、overdose、overestimate、overhaul、overpower、
  overreact、overrule、overrun、overshadow、overstate、overtake、overweight、paragraph、passport、peel、
  podcast、portable、optional、messy、gradual、narrate、negate、orchestrate、pacify、penetrate、permeate、
  personify、pick on、pin down、pinpoint、populate、prioritise、proliferate、prolong、proofread、propel、
  puncture、marginalise、measure up、incite、horrify、galvanise、exonerate、fabricate、falsify。
  （overestimate を描き直し）
  **over- は「本来の線を越える」で描く**。基準の線や枠を破線で引き、そこを越えたところに主役を置く。
  overrun（時計の予定時間を過ぎる）、overweight（目盛りの緑帯を越える）、overtake（相手の車を越す）、
  overdo（適量を越えた塩）。**基準がないと「越えた」が出ない**ので、破線の基準を必ず一本描く。
  第129回に続いて前回のヘルパー定義をファイルごと写してから書き始めた。今回も NameError は出ていない。
  この回の落とし穴:
  - **「予想」と「実物」を左右に離すと、どちらがどちらか決まらない**。
    overestimate を split() で描いたら読めなかった。
    頭の中の大きさを**破線**、実物を**塗り**にして同じ場所に重ねたら一目で通じた。
    思い込みと現実を比べる語（overestimate、underestimate、unrealistic）は重ねて描く。
- 第132回: re- の動詞45語。reassemble、reassess、recapture、reconstruct、redefine、rediscover、
  redistribute、refuel、regroup、rehabilitate、reinstate、reintroduce、reiterate、remarry、reorganise、
  rephrase、replicate、reshape、retell、reunite、revisit、revoke、recycling、quantify、quicken、radiate、
  ratify、reap、rebuke、rectify、rejoice、relegate、relinquish、repel、restrain、elicit、envisage、equate、
  exemplify、instil、lull、purse、of course、on time、respectful。
  （reshape・relegate・equate を描き直し）
  第125回で決めた「re- は split() の左右に一度目 → 二度目」がそのまま25語に効いた。
  ばらけたものを集める語（reassemble、regroup、reunite、reorganise）は
  左を散らし、右を整列させるだけで描き分けが要らない。
  この回の落とし穴:
  - **`<g transform="translate(...)">` の中でヘルパーを呼ぶと座標が二重にずれる**。
    relegate で `translate(300 130)` の中に `head(150,130,...)` を書いたら、
    顔が枠の外（絶対座標 450,260）へ飛んだ。
    `head()` や `person()` は自分で `translate` を出すので、**必ず絶対座標で、group の外に置く**。
  - **記号のヘルパーに 0 を渡すと消える**。equate で `cross(x,y,0.0)` と書いて何も描かれなかった。
    倍率は必ず正の値にする。等号のように既製の記号がないものは、
    角丸の長方形を二本並べて自分で描く。
- 第133回: 状態の変化と句動詞46語。ripe、ripen、rotten、seasonal、roam、scatter、seep、solidify、stagger、
  stagnate、stiffen、stabilise、soothe、slippery、round up、run down、seize on、settle for、shake off、
  shortlist、scoop、saddle、scrutinise、ascertain、delineate、elucidate、enlighten、entail、extrapolate、
  hypothesise、affirm、absolve、aggravate、necessitate、predispose、esteem、poise、foreground、revolt、
  sightseeing、souvenir、slipper、spelling、so far、sterilisation、restate。
  （saddle を三度描き直し）
  **段階のある語は三つ並べる**。ripe は青い実・食べごろ・傷んだ実を横に並べ、まん中だけ丸で囲った。
  二つでは「どちらが」で終わるが、三つ並べると「まん中がその語」と決まる。
  seasonal も同じ木を四季で四つ並べた。
  この回の落とし穴、saddle で三度やり直したので詳しく残す:
  - **動物に物を載せると、載せた物が体の一部に見える**。
    鞍を大きく暗い色で背中いっぱいに描いたら、馬がカメになった。鞍は小さく、背の一点にだけ載せる。
  - **首と頭を一つのパスでつなぐと、頭が消える**。
    第126回の trot から首のパスをそのまま持ってきたが、あれは「首＋鼻づら」だけで
    **頭そのものを描いていなかった**。単体で走っている絵なら勢いでごまかせるが、
    背中に物を載せて視線が集まると頭がないことが分かる。
    体・首・**頭**・耳・鼻づら・目・たてがみ・尾・脚を、それぞれ独立した図形として置く。
  - 使い回すときは、**元の絵が何を省略していたか**まで確認してから持ってくる。
- 第134回: 身のまわりの名詞と、置き換え・裏づけの動詞46語。suitcase、sunflower、supermarket、surname、
  teaspoon、teenager、telescope、timetable、toothbrush、toothpaste、trousers、tulip、uncle、tailor、trek、
  thud、straighten、streamline、subscribe、substantiate、supersede、supplant、surpass、symbolise、
  sympathise、tabulate、thicken、thwart、toughen、transcribe、truncate、typify、uncover、underpin、
  reinterpret、presuppose、mismanage、ascribe、stylish、terrified、thankful、trendy、such as、take part in、
  similar to、trickle down。（描き直しなし）
  **「取って代わる」の三語は、取って代わられる側が何かで決める**。
  supersede は古い機種（物）、supplant は席にいた人（人）、surpass は追い越す線（数値）。
  日本語ではどれも「上回る・置き換わる」だが、主語と対象を変えれば絵が自然に分かれる。
  第129回・第133回と同じで、**似た語は描き始める前に場面を割り当てておくと描き直しが出ない**。
- 第135回: 画面まわりの語、un- の形容詞、量を表す連語45語。upload、username、troll、viral、trending、
  wallet、violin、yoghurt、almond、allergy、veil、vacation、weekday、weekend、subpoena、understate、
  utilise、vindicate、whiten、withhold、withstand、verge、unfamiliar、unhelpful、unlimited、unsafe、
  unsuccessful、ambiguous、abrupt、acidic、adept、admirable、advisable、aerobic、affirmative、agreeable、
  akin、aloof、visibly、instead of、pay attention to、proud of、responsible for、a variety of、above all。
  （veil を描き直し）
  **カレンダーは色を塗る範囲だけで語が変わる**。weekday は月〜金の列を、weekend は土日の列を塗り、
  見出しの行の色も入れ替えた。同じ枠を使い回して塗り分ければ、対になる語が一組で片づく。
  この回の落とし穴:
  - **半透明の布に格子を描くと鳥かごになる**。veil を布地の織り目のつもりで格子にしたら
    顔にかごをかぶせた絵になった。**顔を先に描き、その上に線のない半透明の面を一枚重ねる**。
    透けて見えることが veil の要点なので、覆いの模様より「下が見えている」ことを優先する。
- 第136回: 人柄を表す形容詞と、量・時を表す連語45語。appetizer、aspirin、atom、banknote、amusement、
  ambivalent、amiable、ample、analogous、analytic、antisocial、apathetic、apologetic、appreciative、
  apprehensive、approximate、apt、archaic、arduous、arrogant、assertive、atrocious、attentive、audacious、
  audible、autonomous、avoidable、baggy、bankrupt、bashful、bang、collectively、harshly、markedly、
  noticeably、a great deal of、a number of、a range of、a series of、after all、along with、as a result of、
  at most、at once、at present。（arrogant を描き直し）
  **量を表す連語は「並べ方」だけで描き分ける**。
  a great deal of は数えられない水を一つの器に、a number of は同じ箱を数えられる形で並べ、
  a range of は小から大へ大きさを変えて並べ、a series of は同じ形を矢印でつないで並べた。
  中身を変えずに並べ方だけ変えると、四語がひと組で片づく。
  この回の落とし穴:
  - **`person()` の上に手描きの腕を重ねるときは、顔の座標を計算してから置く**。
    arrogant で組んだ腕を顔の高さに置いてしまい、顔が腕で消えた。
    `person(x, y, s)` の**顔の中心は y - 108*s、胴の上端は y - 78*s**。
    腕は必ず胴の上端より下に置く。第125回の labourer（荷物が顔にかぶさった）と同じ失敗で、
    今度は座標の計算式そのものを書き残しておく。
- 第137回: 職業と身のまわりの物、b- の形容詞45語。butcher、carpenter、cashier、beak、bestseller、blender、
  blouse、cardigan、bracelet、cello、cathedral、bull、calf、calorie、change、blink、bearable、belated、
  biannual、bilateral、bland、blatant、blunt、blurred、boastful、boisterous、bookish、boundless、breathless、
  brittle、bulky、bustling、catastrophic、ceremonial、changeable、chaotic、brightness、buzz、discontent、
  as far as I know、aware of、be supposed to、belong to、by chance、capable of。（calf・cello を描き直し）
  **一語に二つの意味がある語は、両方を一枚に並べる**。calf は「ふくらはぎ」と「子牛」を左右に置き、
  ふくらはぎのほうを破線で囲った。どちらか一方だけ描くと、もう一方を引けなくなる。
  change（変化／おつり）も、おつりの場面を選んだうえで説明文で両方に触れた。
  この回の落とし穴:
  - **体の一部を筒で描くと肉の塊になる**。calf の脚がそうだった。
    太もも→ひざ→ふくらはぎ→足首→足と、**関節ごとに図形を分けて順に置く**。
    第133回の saddle（馬の頭がなかった）と同じで、輪郭一つで済ませようとすると必ず崩れる。
  - **弦楽器は「くびれ」がないと弦楽器にならない**。cello を円二つで描いたら雪だるまになった。
    第135回の violin で使ったくびれた輪郭を縦にしたら通じた。
- 第138回: c- の形容詞と身のまわりの名詞45語。checkout、checkup、chimney、chorus、cinnamon、comet、
  commuter、consonant、coupon、cricket、charitable、cheerless、chewy、coercive、coherent、cohesive、
  commendable、communicative、compact、compassionate、complacent、composed、compulsive、conceited、
  conceivable、concise、conclusive、concurrent、condescending、confidential、conscientious、constructive、
  contagious、contemplative、continental、contradictory、counterproductive、courteous、cramped、cryptic、
  cumbersome、cumulative、by and large、by means of、curious about。（consonant を描き直し）
  この回の落とし穴:
  - **口だけを角丸で描いても顔にならない**。consonant を唇の開閉だけで描いたら、ただの二つの塊になった。
    目のある丸い顔を描いてから、口の形だけを変える。**体の部位は必ず全体の中に置く**。
    第124回の cuff（そで口だけ切り出して箱になった）と同じ形の失敗。
  - **対にして描くとき、どちらが見出し語か分かる印を付ける**。
    はじめ「閉じた口に ×、開いた口に ✓」としたが、これでは consonant が否定されているように見えた。
    **見出し語の側を実線の丸で囲み、対比の側を破線の丸にする**。
    ✓と×は「正しい／誤り」の対にだけ使い、「これがその語／これは違う語」には丸の実線と破線を使う。
- 第139回: d-/e- の形容詞と身のまわりの名詞45語。cursor、daisy、denim、diesel、diploma、dormitory、
  ecosystem、electrician、duty-free、draw、drip、dash、deceitful、deceptive、definitive、derogatory、
  descriptive、desolate、despicable、detrimental、devious、devoid、diligent、disgraceful、dispensable、
  disposable、divisive、dormant、drastic、drowsy、dubious、ecstatic、elated、enraged、edgy、edible、
  effortless、elastic、eminent、emphatic、climatic、diagnostic、depend on、in brief、in practice。
  （dispensable を描き直し）
  **感情の語は「体のどこに出るか」で描き分ける**。
  ecstatic は跳び上がる足、elated は浮くような姿勢と光、enraged は赤い顔と耳から出る湯気、
  edgy は指をかむ手と細かい震え線、drowsy は半分閉じた目と Zzz。
  顔だけで描くと全部同じになるので、必ず体のどこかに出す。
  この回の落とし穴:
  - **第138回で決めた印の規則を、さっそく破って描いてしまった**。
    dispensable を ✓/× で描いたら「どちらが正しいか」に読めた。
    **見出し語＝実線の丸、対比＝破線の丸**の規則を適用して描き直した。
    規則を決めた次の回で忘れるくらいなので、split() を使う語では毎回この二つのどちらかを選ぶ、
    と手を動かす前に決めておく。
- 第140回: e-/f- の形容詞と身のまわりの名詞46語。fin、fireplace、flute、exchange rate、fossil fuel、
  freelance、alteration、enviable、envious、equitable、erratic、erroneous、evasive、eventful、evocative、
  excusable、exempt、exhaustive、expansive、expressive、factual、fearless、feeble、ferocious、feudal、
  feverish、figurative、finite、flammable、flawless、flimsy、forceful、formative、fragrant、frantic、
  deductive、departmental、dimensional、elemental、emotive、antitrust、consequential、essential to、
  familiar with、for now、in the long run。（描き直しなし）
  第138回の「見出し語＝実線の丸、対比＝破線の丸」を全語で徹底したら、描き直しがゼロになった。
  **-able / -ous のように「する側／される側」で対になる語は、丸をどちらに置くかだけで決まる**。
  enviable はうらやましがられる賞に丸、envious はうらやましがる人に丸。同じ場面を使い回せる。
- 第141回: g-/h- の形容詞と身のまわりの名詞47語。galaxy、germ、gorilla、grapefruit、guidebook、hacker、
  hallway、handkerchief、heartbeat、hostel、humidity、hyperlink、frown、glow、frivolous、frugal、futile、
  geographic、glossy、graceful、gracious、greasy、greenish、gullible、habitual、hasty、hazardous、heroic、
  heterogeneous、homogeneous、hideous、honourable、horrific、hospitable、hygienic、hyperactive、
  hypersensitive、hypocritical、hypothetical、iconic、idealistic、identifiable、spatial、supplemental、
  unsatisfactory、depressive、developmental。（hideous を描き直し）
  **反対語の対は同じ絵を二枚使い、丸の位置だけ入れ替える**。
  heterogeneous と homogeneous は、ばらばらの図形と同じ図形を並べた**まったく同じ絵**を使い、
  実線の丸をどちらに置くかだけ変えた。glossy（つや／つや消し）も同じやり方。
  対語は一枚描けば二枚できる。
  この回の落とし穴:
  - **「醜い」はごつごつした輪郭では出ない**。hideous を不定形の塊で描いたら茶色いしみになった。
    **ふつうの壺の形をまず作り、そこから色をけんかさせ、取っ手を左右で違う形にする**。
    何が壊れているか分かる形でないと「醜い」にならない。
- 第142回: in-/im- の形容詞45語。in-laws、intern、intersection、ignorant、illegible、illustrative、
  illustrious、imaginable、immaculate、immersive、impartial、impeccable、impenetrable、impersonal、
  implicit、improbable、impulsive、incessant、inclusive、incoherent、incomparable、inconceivable、
  inconsiderate、incurable、indefensible、indispensable、inductive、industrious、inexcusable、inferior、
  infinite、inflammatory、ingenious、innate、innocuous、inquisitive、insightful、instinctive、instructive、
  intentional、intermittent、intricate、intrusive、intuitive、invaluable。（描き直しなし）
  **否定接頭辞の語は、split() の「できない側」に実線の丸を置く**。
  ignorant、illegible、incoherent、inferior は左（できない側）に丸、
  indispensable、inclusive、intuitive、immaculate、impeccable は右（できる側）に丸。
  接頭辞が否定でも、語が指すのは必ず「その状態のほう」なので、
  **丸は接頭辞ではなく語の意味に合わせて置く**。
  inductive は第139回の deductive の**矢印を上下逆にしただけ**で描けた。
  対になる語は、先に描いたほうの図を上下または左右に反転すると早い。

### 第143回（45語）

i-/j-/l-/m- の形容詞と身のまわりの名詞。jumper, lamb, lily, mammal, mango, mayonnaise, microscope, midday, mint, manual, idiomatic, interdependent, intrinsic, inventive, investigative, irreplaceable, irresistible, irreversible, irritated, juicy, justifiable, knowledgeable, laid-back, lasting, laughable, lavish, lenient, linguistic, literal, lucid, ludicrous, lukewarm, luxurious, majestic, malicious, manageable, manipulative, marvellous, maternal, meagre, medicinal, mediocre, merciful, merciless, metallic。

- `literal` は第140回の `figurative` と同じ構図にして、本物の山のほうに実線の丸を置いた。対義語は同じ絵で丸の位置だけ変える。
- `lukewarm` は熱い・ぬるい・冷たいの三つのカップを並べ、真ん中を丸で囲む（第133回の三段階ルール）。
- 果物は「丸＋緑のへた」で描くとかぼちゃになる。`mango` は上がふくらんで下がとがる非対称の輪郭にし、切って種を見せた半分を添えて描き直した。

### 第144回（45語）

dis-/re- の動詞と、判断・態度をあらわす形容詞。fantastic, hardworking, avert, deafen, debit, discern, discontinue, disembark, disengage, disgrace, dwell, falter, forestall, gratify, noticeable, procure, reclaim, redeem, reignite, relive, slander, suffice, unavailable, astute, believable, course, deficient, discontented, discreet, disparate, elusive, fictional, glaring, hysterical, incidental, keep an eye on, loyal to, methodical, no wonder, rhetorical, stylistic, conducive, content with, cremation, dissatisfaction。

- `suffice` と `deficient` は同じビーカーの絵で、水面が破線に届くかどうかだけを変えた（対義語は同じ絵で一箇所だけ動かす）。
- 空白を含む id（keep an eye on など）は emit() の第1引数をハイフンにする。今回もそのまま渡してファイル名に空白が入ったので、`illustrations.ts` の src とあわせて付け直した。
- 破線＝実在しないもの。`fictional` は竜を破線で描くと形が読めず、城に替えた。輪郭が単純なものを選ぶ。
- 「まぶしい光から顔をそむける」だけでは fantastic と見分けがつかない。`avert` は転がる岩の進路を曲げる絵にして、避ける対象を危険なものにした。
- 虫めがねの白い円は opacity 0.5 だと下の線が消える。0.16 まで下げる。

### 第145回（45語）

-tion/-ance の抽象名詞と、in-/with- の連語、mi-/mo- の形容詞。as a matter of fact, as such, at large, entirety, experimentation, facilitation, fidelity, for the purpose of, formality, fulfilment, gratification, grievance, immersion, inception, indulgence, insanity, madness, make sense of, realisation, recourse, seclusion, severance, staffing, tenderness, utterance, with a view to, governmental, in danger of, in detail, in need of, in other words, in public, in short, insolvent, interpretive, intoxicated, keen on, meticulous, microscopic, mindless, miraculous, mischievous, misguided, molecule, momentary。

- 空白を含む id を毎回ハイフンにし忘れるので、`lib.py` の `emit()` の先頭で `word.replace(' ', '-')` するようにした。以後は id をそのまま渡してよい。
- ✗ は「間違い」専用。ふさがった扉は ✗ でなく板を打ちつけて表す（`recourse`）。`misguided` は mis- の右／誤りテンプレートなので ✓✗ を使う。
- 同じ「ごちそう」の絵は使い回せない。`gratification` は自分のケーキ、`indulgence` は与えすぎる山盛りに描き分けた。
- 目的をあらわす連語は視点を変える。`for the purpose of` は的、`with a view to` は遠くの旗を見すえる絵。

### 第146回（46語）

mo-/n-/o- の形容詞と、身のまわりの名詞。momentous, monumental, monotonous, more or less, motionless, mournful, muffled, mundane, murky, mustard, mute, naive, nosy, obnoxious, obsessive, obstinate, nameless, nonexistent, needless, odourless, painless, nationality, newborn, nonfiction, nutritional, nylon, oat, painkiller, paperback, nominal, normative, nostalgic, nauseous, noxious, numb, obscure, obsolete, ominous, on the other hand, opaque, optimal, ornamental, overcrowded, overdue, overt, painstaking。

- -less は「あるはずのものが破線で消えている」で統一した（needless, odourless, painless, motionless, nameless）。
- 「見えない」系は物を変えて描き分ける。`murky` は濁った水、`opaque` は透けない板、`obscure` は霧に隠れた山。
- `nonfiction` は第145回の `fictional` と同じ本の絵にして、出てくるものを破線から実線の山に変えた。
- 仮置きで `add(...)` してから `W.pop()` しても、`emit()` はすでにファイルを書いている。孤児 SVG になるので仮置き自体をやめる。

### 第147回（45語）

p- の形容詞と、職業をあらわす名詞。panicky, paramount, pathetic, peckish, petrified, powerless, preoccupied, prone, pompous, pretentious, perceptive, perilous, precarious, plausible, pertinent, pervasive, predictive, preventive, periodic, perpetual, permissive, prescriptive, prevalent, priceless, pharmacy, pharmacist, plumber, performer, presenter, pedestrian, penniless, preschool, postwar, paternal, patriotic, phonetic, photographic, picturesque, piercing, pitiful, pivotal, plentiful, poetic, primitive, prolific。

- 描き直しなし。似た語をあらかじめ振り分けたのが効いた。paramount は「いちばん高い棒＋冠」、pivotal は「シーソーの軸」、pathetic は「できそこないの雪だるま」、pitiful は「皿に一粒」。
- pompous は台の上でふんぞり返る人、pretentious はただの一品を飾り立てる皿。人がらは人、見せかけは物で描き分けた。
- 職業は「その人の道具と場所」で描く（pharmacist＝薬と白衣、plumber＝レンチと配管、presenter＝マイクと画面）。

### 第148回（45語）

re- の形容詞と動詞、pr-/r- の名詞。pronunciation, roar, rhythmic, repetition, repetitive, rewrite, regretful, remorseful, remorseless, resentful, restless, rebellious, receptive, reckless, reconcile, relentless, repressive, restrictive, rigid, punitive, rampant, resilient, restorative, regenerative, reuse, revolve, prophetic, prosperous, provisional, prudent, reputable, redundant, reddish, reflective, rigorous, rudimentary, publisher, receptionist, retailer, rehearsal, ruins, reproductive, robotic, rudeness, quarter。

- `person()` を回転させてお辞儀や土下座を作ろうとすると、頭と髪がずれて別物になる。姿勢で見せずに「吹き出しの中身」で見せるほうが読める（remorseful＝割れた皿の吹き出し）。
- 後悔・容赦の三語は場面を分けた。regretful＝逃した列車、remorseful＝自分が壊したもの、remorseless＝すがる相手と腕組み。
- 「押さえる」三語も対象を変えた。repressive＝上から押す大きな手、restrictive＝小さな枠、rigid＝曲がらない棒。

### 第149回（45語）

s- の形容詞と、学校・食事まわりの名詞。ruthless, sarcastic, scornful, snobbish, spiteful, sheepish, shameless, shyness, self-assured, selfless, sober, sluggish, sloppy, spotless, shabby, simplistic, simultaneous, sequential, serene, scenic, sensational, speculative, sparse, sporadic, spacious, solitary, sleek, sparkle, sleepless, sickness, sore, skilful, savings, semester, semi-detached, semifinal, server, serving, spinach, spray, spreadsheet, sprint, spontaneous, sooner or later, sonic。

- 見下す系の四語は道具立てを変えた。scornful＝払いのける手、sarcastic＝失敗を前の拍手、snobbish＝上を向いて安いほうを見ない、spiteful＝いすの画びょう。
- `sporadic` は第147回の `periodic` と同じ数直線で、間かくだけ不ぞろいにした。
- 「みんなで喜ぶ絵」は spontaneous には足りない。ひとりから他へ矢印で広がる形にし、予定表を空の破線にして「決めていない」を足した。

### 第150回（49語）

s-/t- の形容詞と、家族・道具の名詞。squeamish, startled, swollen, tiredness, stern, stringent, stingy, submissive, timid, tactful, tactless, take advantage of, superficial, superfluous, subjective, succinct, stagnant, sterile, stainless, sturdy, tasteful, tasteless, tentative, suffix, synonym, thematic, think of, thanks to, suitable for, temporal, timeless, thickness, steering, stepfather, stepmother, technician, trainee, toddler, tights, symphony, trumpet, syrup, tablespoon, synthetic, telescopic, therapeutic, thankless, swap, to be honest。

- -ful と -less の対は同じ場面で吹き出しの形だけ変えた（tactful＝丸い吹き出し、tactless＝とげのある吹き出し）。tasteful / tasteless も同じ部屋の飾りだけを変えた。
- `stern` は人の顔つき、`stringent` は規則の細さ。「厳しい」は人か仕組みかで描き分ける。
- `HAIRS['bun']` は小さく描くと short と見分けがつかない。母親役は 'bob' を使う（stepfather / stepmother）。
- 語が何を指すかを示す絵は、指される側を誰でも分かる物にする。`synonym` の指す先を人型アイコンからりんごに変えた。

### 第151回（45語）

t- の形容詞と un- の否定形容詞。tireless, tolerant, toothless, topical, tranquil, transatlantic, transient, transitional, traumatic, turbulent, typical of, ubiquitous, unambiguous, unequivocal, unanimous, unassuming, unattended, unauthorised, unavoidable, unaware, unbeaten, unbiased, unjust, uncanny, uncommon, unconvincing, undecided, undeniable, underpaid, underrated, underway, undesirable, undue, uneasy, uneven, unforeseen, ungrateful, unilateral, uninterested, unofficial, unpaid, unparalleled, unpredictable, unrelenting, unreliable。

- un- の定型を決めた。「あるはずのものを破線で描く」（unattended＝破線の人、unauthorised＝破線の通行証、ungrateful＝空の破線吹き出し）か、「肯定側を破線の丸、否定側を実線の丸で対比する」（unambiguous, unequivocal, uneven, unofficial）。
- 反対語は同じ絵を使い回した。unbiased＝水平なてんびん、unjust＝同じ仕事に不ぞろいな報酬。
- 人物の不在を白い四角で塗りつぶすと、ただの白い箱に見える。破線の人型で描く。

### 第152回（45語）

v-/w- の語と、a- で始まる抽象名詞。unresolved, unsettling, untenable, valueless, worthless, wary, watchful, weary, weightless, wholesome, wilful, wind up, wink, witty, worry about, wasteful, vigorous, vivid, vest, vinegar, vowel, walnut, a far cry from, a handful of, all the same, abolition, absurdity, acceleration, accountancy, acorn, acquaintance, acquittal, addict, adherence, admiration, adolescence, adulthood, advancement, adversity, affiliation, affirmation, allegiance, allure, altar, amphibian。

- 同義に近い二語は「なぜ価値がないか」で分けた。valueless＝値がつかない（ガラスと空の値札）、worthless＝役に立たない（こわれた道具とごみ箱）。
- `adolescence` と `adulthood` は同じ三段階の成長図で、丸を置く位置だけ変えた。
- 白や淡い色の上に白い物を置くと消える。`untenable` の氷を崩れる岩に替えた。
- ◯（丸）は日本語の「はい・正しい」の記号として使える。`affirmation` はうなずき＋緑の◯。

### 第153回（45語）

an-/ap-/ar-/as-/at-/au-/av- の抽象名詞と慣用表現。anguish, annoyance, apprehension, apathy, astonishment, aversion, awkwardness, ardour, anomaly, antonym, at odds with, as opposed to, at first glance, as a rule, aside from, at any rate, approximation, an array of, analytics, appraisal, apprentice, arbitration, archaeology, auditor, authorisation, austerity, attainment, antibiotic, antidote, asthma, antler, asteroid, apostrophe, asterisk, appliance, autobiography, autopilot, ascent, avoidance, at all costs, at stake, at the expense of, at the mercy of, armistice, anticipation。

- `antonym` は第150回の `synonym` と同じ「二語から線を下ろす」構図で、指す先を大小の対にした。
- 動物は正面より横向きのほうが読める。`antler` は正面のシカがクモに見えたので、横顔にして角を太い枝線で描き直した。
- caption に `'` をそのまま書くと `illustrations.ts` が構文エラーになる。全角の `’` を使う（apostrophe）。

### 第154回（46語）

b- の名詞と慣用表現。backbone, bladder, bowel, bib, bereavement, betrayal, bewilderment, bitterness, boldness, brutality, backlash, bailout, bandwidth, bankruptcy, buyout, bribery, borough, bulletin, briefing, bibliography, bracket, brevity, byline, brainstorm, brush up on, be bound to, be liable to, be subject to, believe in, bite the bullet, break the ice, bump into, by contrast, by far, by virtue of, call it a day, cancellation, barley, basil, blueprint, brooch, broadsheet, brotherhood, bystander, brink, bout。

- 描き直しなし。臓器は `torso()`（上半身の輪郭）を新設し、その中に器官を置いて実線の丸で囲む形に統一した（backbone, bladder, bowel）。
- be bound to / be liable to / be subject to は仕掛けで描き分けた。レール（決まった行き先）、ひび（もれやすい）、検査門（通されて変わる）。
- `barley` は第146回の `oat` と同じ穂の構図だが、長い芒（のぎ）を足して区別した。

### 第155回（45語）

ca-/ce-/ch-/cl-/co- の名詞と慣用表現。capillary, cartilage, carbohydrate, caregiver, carer, captive, captivity, ceasefire, cessation, coercion, concealment, censor, censorship, census, citation, caveat, clang, clatter, chord, chapel, clover, cockroach, cocoon, cod, civility, clan, comrade, companionship, coexistence, cohesion, coldness, commemoration, commonplace, compilation, comprehension, compression, come to terms with, cannot help but, clear up, clearance, clickbait, collateral, colon, combustion, chore。

- 米英で同義の語（caregiver / carer）は場面を変えて描き、caption で使い分けを書く。
- 人・行為・しくみを描き分ける。censor＝塗りつぶす人、censorship＝必ず削られる関門。
- お辞儀は `person()` の頭を回転させても読めない。`civility` は「扉を開けて先に通す」動作に替えた。
- 音は波の大きさと数で区別する。clang＝大きな波が少数、clatter＝小さな波が多数。

### 第156回（45語）

con-/cou-/cr-/cu-/d- の名詞と句動詞。condemnation, critical of, defamation, defiance, confinement, containment, contamination, conformity, conjunction, consist of, conscious of, consolation, dependent on, congestion, contemplation, continuation, contour, damp, deadlock, delusion, deflation, debtor, demotion, counterbalance, cut down on, counterfeit, coursework, craftsmanship, cultivation, dataset, creak, croak, crossroads, crumb, cunning, curfew, corrective, cut corners, cope with, concentrate on, cool down, condolence, defendant, courtship, daffodil。

- 描き直しなし。閉じこめ系は対象で分けた。confinement＝人を小部屋に、containment＝広がりを輪で囲う。
- `conscious of` は第151回の `unaware` と同じ「うしろで起きていること」の絵で、視線の破線をつなぐかどうかだけ変えた。
- 名誉を傷つける語は媒体で分ける。slander＝口（第144回）、defamation＝刷った紙。

### 第157回（45語）

de-/di-/do-/dr-/du- の名詞と句動詞。diffusion, dispersal, dissolution, disarray, deviation, discrepancy, disparity, distortion, deprivation, deportation, displacement, desertion, disregard, desperation, disbelief, discouragement, detachment, devotion, deterrent, domination, devastation, depreciation, dividend, downturn, downfall, distributor, dispatch, disinformation, disclaimer, depiction, designation, diplomacy, disappearance, disturbance, diversion, distraction, descendant, dweller, doorstep, duvet, dullness, diabetes, dress up, drop in, destiny。

- 描き直しなし。「散る」三語は動きで分けた。diffusion＝じわじわ均一に、dispersal＝外向きの矢印で四方へ、dissolution＝輪が切れて人が去る。
- 「ずれ」三語も分けた。deviation＝線から外れる道、discrepancy＝二つの記録の数字ちがい、disparity＝小屋と高層ビル。
- 「無視」は段階で分ける。unaware＝気づかない、uninterested＝関心がない、disregard＝見えていて押しのける。

### 第158回（45語）

e-/f- の抽象名詞と慣用表現。eagerly, eagerness, fervour, euphoria, exhaustion, fatigue, faint, fascination, ferocity, evacuation, eviction, emigration, extinction, famine, enlargement, elevation, expensive, electron, equilibrium, estimation, elimination, exemption, excavation, extraction, embargo, exaggeration, fabrication, fact-check, examiner, feasibility, enrolment, fellowship, empowerment, enlightenment, epoch, dynasty, encore, elegance, extrovert, flair, familiarity, fit in, flicker, face the music, embodiment。

- 描き直しなし。「疲れ」四語は絵を分けた。tiredness＝いすでうなだれる、weary＝長い道の果て、exhaustion＝地面に伸びる＋空のめもり、fatigue＝金属のひび。
- 「出ていく」三語も分けた。evacuation＝警報で建物から、eviction＝家財を出される、emigration＝国境を越える。
- ✓ は right/wrong 専用だが、fact-check と feasibility は「正しいか／できるか」の判定なので使ってよい。

### 第159回（46語）

f-/g-/h- の名詞と句動詞。gleam, glitter, glare, groan, growl, glitch, gallop, germination, food chain, gill, fusion, fluctuation, fortnight, for the time being, for good, folklore, footnote, foreword, glossary, gist, framing, fondness, gentleness, fragility, frenzy, greatness, foe, focus on, foresight, for the sake of, get on with, get to grips with, hamper, guardian, guardianship, guilty of, genocide, forfeit, gulf, hallmark, gland, floorboard, hardback, garnish, fringe, given that。

- 描き直しなし。光る語は粒の数で分ける。gleam＝ひとすじ、glitter＝細かい粒が多数、sparkle（第149回）＝水面。
- 人と制度は分けて描く。guardian＝子を守って立つ人（実線の丸）、guardianship＝判のある書面。
- `genocide` のような重い語は、暴力を描かずに「実線の人が破線に置きかわる＋追悼のろうそく」で表す。

### 第160回（45語）

h-/i- の名詞と、in- で始まる慣用表現。harness, haven, harshness, hibernation, hindrance, hurdle, have no choice but to, hit the nail on the head, impairment, immune to, immunity, hygiene, hoof, hoax, impersonation, imitation, illumination, humiliation, humility, heroism, idleness, hunch, impulse, impetus, heir, impeachment, hub, hive, head for, hear from, hear of, hope for, hyphen, in a nutshell, if anything, in accordance with, in line with, in contrast to, in place of, in favour of, in effect, in due course, in principle, in retrospect, in light of。

- 実線の丸は「見出し語そのもの」に置く。`imitation` は最初、本物のほうを実線で囲んでいたので、まがいもの側に入れ替えた。
- じゃま三語は形で分けた。hamper＝足のおもり、hindrance＝出口をふさぐ荷物、hurdle＝跳び越える枠。
- まねる二語も分けた。imitation＝ものの複製、impersonation＝人の面をかぶる。

### 第161回（45語）

in- の抽象名詞と慣用表現。inflammation, irritation, inhalation, infusion, infiltration, intrusion, influx, irrigation, inhibition, injunction, insulation, in vain, interception, informant, intermediary, interrogation, interviewee, insistence, infringement, inheritance, instalment, invest in, interest, indignation, intimidation, intimacy, intrigue, interplay, intuition, initiation, insurgency, induction, inherent in, inversion, irregularity, iteration, inscription, in search of, in so far as, in the absence of, in the event of, in the light of, in the wake of, in turn, intoxication。

- 描き直し1枚（inhibition）。抑える動きは、体をひねらせるより「⊖の標識＋手を戻す矢印」のほうが読める。
- 入りこむ三語は入り方で分けた。infiltration＝紛れこむ、intrusion＝押し開けて入る、influx＝四方から流れこむ。
- 炎症系は場所で分けた。inflammation＝関節の内側、irritation＝肌の表面。

### 第162回（51語）

j-/k-/l-/ma- の名詞と慣用表現。itinerary, layover, locality, marsh, landfill, mansion, lodger, ledger, markup, liquidation, livelihood, logistics, licensing, libel, ligament, marrow, mane, misinformation, misconception, malware, manifesto, manifestation, look back on, look out for, lose sight of, keep track of, jump to conclusions, jeopardy, juncture, massacre, mediator, mediation, midwife, magnetism, lubrication, longevity, make the most of, knack, mentality, mindset, let alone, let the cat out of the bag, learn the ropes, lead to, keynote, ivy, lotus, linen, margarine, marmalade, mash。

- 描き直しなし。名誉毀損は媒体と場面で三つに分けた。slander＝口、defamation＝刷った紙、libel＝記事＋法廷。
- `jump to conclusions` は第161回の `intuition` と同じ「途中を飛ばす」構図で、行き着く先を ✓ から ✗ に変えた。
- 仲立ちも役割で分けた。intermediary＝品を取り次ぐ、mediator＝あいだに立つ人、mediation＝握手にいたる過程、arbitration＝裁定を下す。

### 第163回（46語）

me-/mi-/mo-/mu-/n-/o- の名詞と慣用表現。melancholy, mourner, mourning, moan, mend, nurture, nourishment, mishap, miss out, misconduct, nuisance, obstruction, modesty, neutrality, nobility, neatness, obsessed with, moderation, mobilisation, newcomer, newlywed, negotiator, multiplication, negation, nuance, murmur, notification, millennium, monarchy, nationalism, menopause, mutation, nucleus, mural, likeness, obscurity, notorious for, observance, mould, mutton, oar, needless to say, not to mention, no sooner than, notwithstanding, normality。

- `head()` を `<g transform=...>` の中で呼ぶと二重に動いて画面外に出る（第132回と同じ失敗）。額縁は g で描き、顔は絶対座標で外に置く（likeness）。
- `nucleus` は第158回の `electron` と同じ原子の絵で、丸を中心に移しただけ。同じ絵で丸の位置を変える型。
- 悼む語は人と状態で分けた。mourner＝悼む人（実線の丸）、mourning＝黒い装いと喪の期間。

### 第164回（45語）

o-/ov-/pa- の名詞と慣用表現。overlap, overload, overwork, overthrow, overhead, overdraft, offset, onset, outset, once and for all, onslaught, onlooker, occupant, outskirts, organiser, oppression, ordeal, parole, on account of, owing to, on the basis of, on the grounds that, opposed to, on the contrary, on the one hand, on the same page, other than, out of the question, parenthesis, partition, parity, omission, pancreas, ozone, pasture, orchid, otter, parsley, palette, parenthood, parenting, paradigm, panorama, omen, ounce。

- 描き直しなし。`on the one hand` は第146回の `on the other hand` と同じ両手の絵で、片方を破線にして実線側に丸を置いた。
- 同義の連語は場面を変える。on account of＝雨で試合中止、owing to＝ストで列車遅延。
- 状態と行為も分けた。parenthood＝親という立場（実線の丸）、parenting＝食べさせ・教え・遊ぶ三場面。

### 第165回（48語）

pa-/pe-/ph-/pi-/pl-/po-/pr- の名詞。patriotism, perseverance, persistence, persecution, persuasion, philanthropy, peril, pitfall, plight, predicament, pinnacle, pillar, penthouse, perfection, perk, paywall, press release, prestige, porter, probation, postgraduate, preface, portrayal, plagiarism, postulate, preconception, presumption, photosynthesis, pollination, penetration, proliferation, propagation, proton, phishing, plausibility, proclamation, predominance, postponement, prior to, prime time, play it by ear, precaution, porch, pendant, polyester, plugin, pilgrimage, plaintiff。

- 描き直しなし。粘る二語は場面で分けた。perseverance＝風雨の坂を登り続ける、persistence＝一滴が石をうがつ。
- 困る二語も分けた。plight＝水につかった家（抜け出せない状況）、predicament＝両側が壁（どちらも選べない）。
- `plaintiff` は第156回の `defendant` と同じ法廷の絵で、丸を反対側の席に移した。
- `preface`（著者が書く）と第159回の `foreword`（他人が書く）は同じ本の絵で、書き手の色を変えて区別した。

### 第166回（45語）

pr-/q-/ra-/re- の名詞と句動詞。rely on, reliant on, reliance, prophecy, prose, provocation, prowess, proximity, radius, rarity, ratification, procurement, remand, rectification, recurrence, reformation, refinement, relaunch, reconciliation, redemption, redundancy, relocation, reassurance, readiness, reluctantly, refrain, put your foot down, pull your weight, react to, recollection, reckoning, put aside, readership, pundit, realism, qualifier, purr, rattle, radiance, purity, racist, quilt, radish, relic, relaxation。

- 描き直しなし。頼る三語は主語で分けた。rely on＝人が人に寄りかかる、reliant on＝機械が一本の電源に、reliance＝仕入れの円グラフ。
- `reconciliation` は第148回の `reconcile` と別の絵にした。動詞＝握手、名詞＝割れた皿がつながった状態。
- `racist` のように差別を扱う語は、線で分けて片側だけを ⊖ で締め出す図にとどめ、人物を醜く描かない。

### 第167回（45語）

re-/ri-/ro-/ru-/sa-/sc-/se- の名詞。remembrance, remnant, retention, retrospective, retraction, revocation, rethink, reversal, reparation, repayment, renewal, renovation, renown, reverence, rivalry, respiration, secretion, sedation, saturation, sediment, scarcity, repression, salvation, sanctuary, respite, resonance, rustle, ring up, rigidity, rigour, richness, respondent, roster, rota, repatriation, schematic, scripture, secrecy, seasoning, sabbatical, roundabout, rubble, rodent, robe, repeatedly。

- 描き直しなし。取り消す二語は対象で分けた。retraction＝出した記事の主張、revocation＝出した許可証。
- 名簿二語も分けた。roster＝役つきの顔ぶれ一覧、rota＝曜日ごとに回る当番表（循環の矢印つき）。
- 抑える語は場所で分けた。oppression＝上からの支配、repressive＝押さえる大きな手、repression＝体の中に押しこめた感情。

### 第168〜180回（590語）

残っていた未作成語をすべて描いた。1回あたり46〜49語、計590語。この13回で `rape` と `suicide` を除く全語に絵がついた。

- 共通部品を `kit.py` にまとめた。第167回までは回ごとに同じ小物（`table` / `coin` / `cross` / `tick` / `doc` / `head` / `word` ほか）を
  60行ほど書き写していた。13回ぶんで約800行の重複になるので、`lib.py` の上にもう一段だけ足した。
  `add()` が caption も受け取り、`finish()` が `illustrations.ts` 追記用のJSONを出す。
- 非ASCIIの見出し語はファイル名をASCIIにする。`fiancé` / `fiancée` は `fiance.svg` / `fiancee.svg` に置き、
  `add(..., key='fiancé')` で `illustrations.ts` のキーだけ元の綴りにした。URLで壊れやすいのを避けるため。
- 描き直しは各回とも `batchNNb.py`（2周目は `batchNNc.py`）。目視で読めなかったのは13回で20語。
  多かったのは「小物が小さすぎて何か分からない」（アイロン、靴、こぶし、かぎづめ）と
  「人体の内側の図が読めない」（digestion / digestive）。後者は器官を単体で描くのをやめ、
  体の輪郭の中に入れたら読めるようになった。
- 意味の近い語は、同じ絵にせず場面の要素で分けた。
  clamp down on＝万力で締める／crack down on＝柵と笛で止める。
  intentionally＝的を狙って当てる／purposely＝わざとコップを倒す。
  come off＝跳躍が決まる／pull off＝綱を渡りきる。
  fend off＝盾ではね返す／ward off＝傘で近寄らせない。
  brush aside＝手で紙を払う／sweep aside＝ほうきで山を払う。
  supplier＝工場から店へ／wholesaler＝大荷を複数の店へ分ける。
- 対になる語は構図をそろえた。fiancé / fiancée は同じ二人の絵で指輪の位置だけを変え、
  nationalisation / privatisation は同じ建物の旗を掛け替え、result from / result in は矢印の向きだけを反転した。
- 時を指す副詞は同じ数直線の上で塗る側を変えた。henceforth＝印より右、hitherto＝印より左、
  indefinitely＝右端の印がないまま伸びる、subsequent to＝印より後ろの出来事に丸。
- 程度を表す慣用表現も目盛りで分けた。to some degree＝つまみが途中、to some extent＝帯が途中まで、
  up to a point＝坂の途中に「ここまで」の旗、virtually＝上端のすぐ手前。

### 第181回（2語）

第114回で保留した `rape` と `suicide`。これで 7,500語すべてに絵がそろった。

- 第114回の方針（加害の場面を描かず、物・跡・制度の側から示す）を引き継いだ。
  rape は「本人の境界線と、それを越えさせない法」、suicide は「予防の相談窓口」で示し、
  被害・自傷の場面そのものは描かない。suicide の例文が helpline なので、絵もそこに合わせた。
- 2回描き直した。1周目は左端が見切れ、2周目は電話が「ダンベル」に見えた。
  受話器は輪郭を自作せず、広く使われている受話器アイコンの形をそのまま使ったら一度で読めた。

### 第182〜191回（500語）

語彙を 7,500語 → 8,000語 に増補したぶん。日常の具体名詞が中心で、1回50語、計500語。
これで 8,000語すべてに絵がついた。

- **曜日と月は「位置＋語源」で描き分けた**。文字が使えないので、
  月は12マス・曜日は7マスの帯を置いて何番目かを示し、その上に中身を足す。
  月は季節の景色（1月＝雪、4月＝花、8月＝浜辺、10月＝紅葉）、
  曜日は語源の印（Monday＝月、Tuesday＝軍神の剣、Wednesday＝オーディンのワタリガラス、
  Thursday＝トールの大づち、Friday＝愛の女神のハート、Saturday＝土星の環、Sunday＝太陽）。
  「覚えるヒント」の語源説明と絵が同じことを言うので、両方が支え合う。
- 具体物が多いので描き直しは少なく、500語で14語だけ。失敗の型は3つに絞られた。
  1つ目は**別の記号に見えてしまう**（hoop の輪＋犬が「犬の立入禁止」標識に見えた→バスケットのゴールに変更）。
  2つ目は**質感が意図と違って読める**（crate の横板が「ケーキの層」、flannel の格子が「れんが壁」、
  mosaic のタイルが「縦縞」→どれも板の向き・目地・形を変えた）。
  3つ目は**f-string の中で `.format()` を入れ子にして属性の引用符が落ちる**（lilac が空になった）。
  入れ子をやめて関数に切り出すのが確実。
- 対になる語は素材を共有した。frying pan は既存語だったので rolling pin に差し替え、
  chopping board・dustpan・sleeping bag も既存語との重複を避けて選び直した。
  重複は `scripts/vocab-illustrations/` ではなく語彙データ側の検証（`npm run validate:vocab -- <plusNN.ts>`）で先に落とす。
