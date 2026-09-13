// A1相当の基本語・機能語。4,500見出し語(A2–B2の差分)には含まれないため、
// レベル逸脱の検査(未習語率)ではこれらを既習として扱う。
// 頻度の高い一般語のみを集めたもので、特定の商用語彙リストの複製ではない。

const WORDS = `
a about above across after afternoon again against age ago air all almost alone along already also always am
among an and angry animal another answer any anyone anything apartment apple april are area arm around arrive art as
ask at august aunt autumn away baby back bad bag ball banana bank bath bathroom be beach beautiful because become bed
bedroom been beer before begin behind believe below beside best better between bicycle big bike bird birthday bit black
blue boat body book boot bored boring born borrow both bottle bowl box boy bread break breakfast bring brother brown
build building bus business busy but butter buy by cake call camera can candy cap car card care careful carry cat catch
cd ceiling cent center centre century chair chance change cheap check cheese chicken child children chocolate choose
cinema city class classroom clean clear climb clock close clothes cloud club coat coffee cold college color colour come
company complete computer concert continue cook cool copy corner correct cost could country course cousin cover cow
crazy cream cross cry cup customer cut dad dance danger dangerous dark date daughter day dead dear december decide deep
delicious desk dictionary did die difference different difficult dinner dirty do doctor dog dollar door double down
draw dream dress drink drive driver drop dry during each ear early earth east easy eat egg eight eighteen eighty either
eleven else email empty end enjoy enough enter evening ever every everybody everyone everything everywhere exam example
excited exciting excuse exercise expensive explain eye face fact fall family famous fan far farm farmer fast fat father
favorite favourite february feel feeling festival few field fifteen fifth fifty fill film final finally find fine
finger finish fire first fish five fix flat floor flower fly follow food foot football for forget fork form forty four
fourteen free fresh friday friend friendly from front fruit full fun funny furniture future game garden gas gate get
gift girl give glass glasses go goal gold good goodbye grandfather grandmother grass gray great green grey ground group
grow guess guitar guy hair half hall hand happen happy hard hat hate have he head health hear heart heavy hello help
her here hers herself hey hi high hill him himself his history hit hobby hold holiday home homework hope horse hospital
hot hotel hour house how however hundred hungry hurry hurt husband i ice idea if ill important in inside instead
interest interested interesting internet into introduce invite is island it its itself january job join joke journey
juice july jump june just keep key kid kill kilometer kind king kitchen knife know lady lake lamp land language large
last late later laugh lazy lead learn leave left leg lemon less lesson let letter library lie life lift light like line
lion list listen little live living lonely long look lose lost lot loud love low lucky lunch machine magazine mail main
make man many map march market married match math maths matter may maybe me meal mean meat medicine meet member menu
message middle midnight might mile milk million mind mine minute miss mistake mobile modern moment monday money monkey
month moon more morning most mother mountain mouse mouth move movie mr mrs ms much mum music must my myself name near
nearly necessary neck need neighbor neighbour never new news newspaper next nice night nine nineteen ninety no nobody
noise none noon nor north nose not nothing notice november now number nurse ocean october of off offer office often oh
oil ok old on once one onion only open opposite or orange order other our ours out outside over own page pain paint
pair paper parent park part party pass past pay pen pencil people perfect perhaps person pet phone photo piano picture
piece pig pink pizza place plan plane plant plate play player please pocket point police pool poor popular possible
post potato pound practice practise prefer prepare present president pretty price print prize probably problem
program programme project public pull purple push put quarter queen question quick quickly quiet quite radio rain read
ready real really reason receive red remember rent repeat reply report restaurant rest return rice rich ride right ring
river road rock room round rule run sad safe salad salt same sand saturday save say school science scissors sea season
seat second see seem sell send sentence september serious seven seventeen seventy several shall she sheep shelf ship
shirt shoe shop short should shoulder shout show shower sick side sign silver simple since sing single sister sit six
sixteen sixty size skirt sky sleep slow slowly small smell smile smoke snow so soap soccer sock soft some somebody
someone something sometimes son song soon sorry sound soup south space speak special spell spend spoon sport spring
stand star start station stay steal still stone stop store storm story straight strange street strong student study
stupid subject sugar summer sun sunday supermarket sure surprise sweet swim table take talk tall taste taxi tea teach
teacher team teeth telephone television tell ten tennis terrible test than thank that the theater theatre their theirs
them themselves then there these they thing think third thirsty thirteen thirty this those though thousand three
through throw thursday ticket tidy tie time tired to today together toilet tomato tomorrow tonight too tooth top touch
town toy traffic train travel tree trip trousers true try tuesday turn twelve twenty twice two ugly umbrella uncle
under understand university until up us use useful usually vegetable very video village visit voice wait wake walk wall
want warm wash watch water way we wear weather wedding wednesday week weekend welcome well west wet what when where
which while white who whole whose why wide wife will win wind window wine winter wish with without woman women wonder
wonderful wood word work world worry worse worst would write wrong year yellow yes yesterday yet you young your yours
yourself zero zoo

am are is was were be been being have has had having do does did done doing go goes went gone going come came coming
get got gotten getting make made making take took taken taking see saw seen know knew known think thought say said
tell told give gave given find found feel felt keep kept leave left let put set sit sat stand stood understand
understood run ran win won lose lost buy bought bring brought teach taught catch caught fight fought seek sought
speak spoke spoken write wrote written ride rode ridden drive drove driven eat ate eaten fall fell fallen begin began
begun drink drank sing sang swim swam wake woke woken break broke broken choose chose chosen forget forgot forgotten
hold held hear heard read pay paid sell sold send sent spend spent build built meet met sleep slept feed fed lead led
grow grew grown throw threw thrown fly flew flown draw drew drawn wear wore worn tear tore lay laid lie lay hide hid
shut cut hurt cost hit quit let bet upset become became rise rose risen show showed shown mean meant

magazine magazines website websites aloud drill drills sewing sew gym locker lockers neighborhood neighborhoods
cannot employee employees commute commuting toaster toasters kettle screw screws torch midday
`

export const basicWords: Set<string> = new Set(WORDS.trim().split(/\s+/))
