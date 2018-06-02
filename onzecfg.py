from nltk.grammar import FeatureGrammar
from nltk import CFG
cfg_1 = CFG.fromstring("""
    S -> NP VP
    S -> NN
    NP -> PRP
    NP -> NP PP
    NP -> D NN
    NP -> Adj NP
    NP -> CC NP
    VP -> VB B BN
    VP -> V N
    VP -> V Adv Vt Vtt PP
    VP -> V PP
    VP -> V NP
    VP -> V PP CC
    VP -> V Adj
    VP -> V Prep Vt N Vtt
    V -> V Vt N V
    V -> V Vt NP
    V -> V Vt Pro Prep C Vt Pro Vtt
    N -> Adj N
    PP -> Prep NP
    PP -> Prep N
    PP -> Prep V Pro
    Adj -> Adj Adj
    CC -> Conj NP VP
    NN -> 'dirty'
    NN -> 'heard'
    NN -> 'hell'
    NN -> 'sound'
    NN -> 'day'
    NN -> 'understand'
    NN -> 'introduction'
    NN -> 'collect'
    NN -> 'fall'
    NN -> 'because'
    NN -> 'pet'
    NN -> 'temper'
    NN -> 'road'
    NN -> 'tarantula'
    NN -> 'guy'
    NN -> 'drive'
    NN -> 'class'
    NN -> 'drawn'
    NN -> 'smart'
    NN -> 'baby'
    NN -> 'cross'
    NN -> 'hand'
    NN -> 'mom'
    NN -> 'hey'
    NN -> 'car'
    NN -> 'lot'
    NN -> 'story'
    NN -> 'cobweb'
    NN -> 'town'
    NN -> 'll'
    NN -> 'month'
    NN -> 'stood'
    NN -> 'hour'
    NN -> 'toilet'
    NN -> 'tell'
    NN -> 'eat'
    NN -> 'cost'
    NN -> 'come'
    NN -> 'nobody'
    NN -> 'night'
    NN -> 'fault'
    NN -> 'bring'
    NN -> 'name'
    NN -> 'let'
    NN -> 'someone'
    NN -> 'break'
    NN -> 'beat'
    NN -> 'join'
    NN -> 'bathroom'
    NN -> 'bell'
    NN -> 'felt'
    NN -> 'guard'
    NN -> 'nothing'
    NN -> 'something'
    NN -> 'everyone'
    NN -> 'bottom'
    NN -> 'change'
    NN -> 'school'
    NN -> 'book'
    NN -> 'bedroom'
    NN -> 'sleep'
    NN -> 'stick'
    NN -> 'end'
    NN -> 'cool'
    NN -> 'hung'
    NN -> 'way'
    NN -> 'throat'
    NN -> 'life'
    NN -> 're'
    NN -> 'needless'
    NN -> 'care'
    NN -> 'dare'
    NN -> 'worse'
    NN -> 'time'
    NN -> 's'
    NN -> 'everything'
    NN -> 'reason'
    NN -> 'vacuum'
    NN -> 'thing'
    NN -> 'look'
    NN -> 'wildness'
    NN -> 'hunt'
    NN -> 'money'
    NN -> 'gift'
    NN -> 'country'
    NN -> 'sister'
    NN -> 'imagine'
    NN -> 'steve'
    NN -> 'watch'
    NN -> 'everybody'
    NN -> 'slip'
    NN -> 'cobwebs'
    NN -> 'hours'
    NN -> 'predators'
    NN -> 'rotten'
    NN -> 'women'
    NN -> 'characters'
    NN -> 'teachers'
    NN -> 'eggs'
    NN -> 'wins'
    NN -> 'fights'
    NN -> 'people'
    NN -> 'stores'
    NN -> 'bones'
    NN -> 'works'
    NN -> 'mistakes'
    NN -> 'names'
    NN -> 'sorts'
    NN -> 'parents'
    NN -> 'noises'
    NN -> 'calls'
    NN -> 'costs'
    NN -> 'kindergarten'
    NN -> 'cockroaches'
    NN -> 'books'
    NN -> 'tantrums'
    NN -> 'flies'
    NN -> 'things'
    NN -> 'spiders'
    NN -> 'pieces'
    NN -> 'endings'
    NN -> 'friends'
    NN -> 'reasons'
    NN -> 'pants'
    NN -> 'ends'
    NN -> 'prizes'
    NN -> 'tale'
    JJ -> 'crazy'
    JJ -> 'other'
    JJ -> 'ready'
    JJ -> 'past'
    JJ -> 'harm'
    JJ -> 'stayed'
    JJ -> 'feared'
    JJ -> 'speak'
    JJ -> 'big'
    JJ -> 'happy'
    JJ -> 'great'
    JJ -> 'busy'
    JJ -> 'last'
    JJ -> 'stole'
    JJ -> 'obvious'
    JJ -> 'stroller'
    JJ -> 'wild'
    JJ -> 'lunch'
    JJ -> 'storm'
    JJ -> 'die'
    JJ -> 'little'
    JJ -> 'worms'
    JJ -> 'describe'
    JJ -> 'sharp'
    JJ -> 'wish'
    JJ -> 'happen'
    JJ -> 'enough'
    JJ -> 'dusty'
    JJ -> 'clear'
    JJ -> 'english'
    JJ -> 'cruel'
    JJ -> 'dalton'
    JJ -> 'sick'
    JJ -> 'many'
    JJ -> 'garden'
    JJ -> 'tree'
    JJ -> 'made-up'
    JJ -> 'true'
    JJ -> 'first'
    JJ -> 'irresponsible'
    JJ -> 'mr'
    JJ -> 'shan'
    JJ -> 'started'
    JJ -> 'real'
    JJ -> 'eight-legged'
    JJ -> 'fierce'
    JJ -> 'nasty'
    JJ -> 'trick'
    JJ -> 'small'
    JJ -> 'queasy'
    JJ -> 'fascinated'
    JJ -> 'late'
    JJ -> 'evil'
    JJ -> 'old'
    JJ -> 'quiet'
    JJ -> 'scary'
    JJ -> 'mine'
    JJ -> 'loose'
    JJ -> 'angry'
    JJ -> 'guys'
    JJ -> 'leopard'
    JJ -> 'leonard'
    JJ -> 'bad'
    JJ -> 'cried'
    JJ -> 'mouth'
    JJ -> 'mad'
    JJ -> 'ordinary'
    JJ -> 'throw'
    JJ -> 'thought'
    JJ -> 'serious'
    VBG -> 'understanding'
    VBG -> 'creeping'
    VBG -> 'guessing'
    VBG -> 'blowing'
    VBG -> 'laying'
    VBG -> 'lurking'
    VBG -> 'going'
    VBG -> 'crawling'
    VBG -> 'watching'
    VBG -> 'rattling'
    VBG -> 'being'
    VBG -> 'humming'
    VBG -> 'calling'
    VBG -> 'looking'
    VBG -> 'making'
    VBG -> 'waking'
    VBG -> 'rooting'
    VBG -> 'faking'
    VBG -> 'sliding'
    VBG -> 'feeling'
    VBG -> 'passing'
    VBG -> 'sitting'
    VBG -> 'waiting'
    VBG -> 'ring'
    RB -> 'here'
    RB -> 'not'
    RB -> 'once'
    RB -> 'anyway'
    RB -> 'funny'
    RB -> 'soon'
    RB -> 'too'
    RB -> 'practically'
    RB -> 'everywhere'
    RB -> 'still'
    RB -> 'sometimes'
    RB -> 'normally'
    RB -> 'often'
    RB -> 'so'
    RB -> 'treats'
    RB -> 'well'
    RB -> 'almost'
    RB -> 'teacher'
    RB -> 'away'
    RB -> 'ever'
    RB -> 'then'
    RB -> 'always'
    RB -> 'really'
    RB -> 'quite'
    RB -> 'even'
    RB -> 'just'
    RB -> 've'
    RB -> 'before'
    RB -> 'yard'
    RB -> 'very'
    RB -> 'simply'
    RB -> 'back'
    RB -> 'up'
    RB -> 'again'
    RB -> 'stupid'
    RB -> 'not'
    RB -> 'right'
    RB -> 'belly'
    RB -> 'never'
    DT -> 'every'
    DT -> 'no'
    DT -> 'an'
    DT -> 'any'
    DT -> 'a'
    DT -> 'the'
    DT -> 'all'
    DT -> 'this'
    PRP -> 'them'
    PRP -> 'you'
    PRP -> 'we'
    PRP -> 'they'
    PRP -> 'I'
    PRP -> 'him'
    PRP -> 'he'
    PRP -> 'me'
    VBD -> 'ripped'
    VBD -> 'threw'
    VBD -> 'knew'
    VBD -> 'tried'
    VBD -> 'grinned'
    VBD -> 'calmed'
    VBD -> 'said'
    VBD -> 'took'
    VBD -> 'told'
    VBD -> 'had'
    VBD -> 'began'
    VBD -> 'came'
    VBD -> 'stuck'
    VBD -> 'was'
    VBD -> 'shed'
    VBD -> 'were'
    VBD -> 'gave'
    VBD -> 'hollered'
    VBD -> 'prodded'
    VBD -> 'got'
    VBD -> 'loved'
    VBD -> 'happened'
    VBD -> 'shouted'
    VBD -> 'despised'
    VBD -> 'received'
    VBD -> 'whacked'
    VBD -> 'went'
    VBD -> 'wanted'
    VBD -> 'did'
    VBD -> 'found'
    VBD -> 'nodded'
    VBD -> 'ran'
    RP -> 'out'
    IN -> 'd'
    IN -> 'like'
    IN -> 'around'
    IN -> 'with'
    IN -> 'because'
    IN -> 'through'
    IN -> 'for'
    IN -> 'at'
    IN -> 'of'
    IN -> 'near'
    IN -> 'except'
    IN -> 'as'
    IN -> 'while'
    IN -> 'since'
    IN -> 'under'
    IN -> 'into'
    IN -> 'without'
    IN -> 'above'
    IN -> 'behind'
    IN -> 'if'
    IN -> 'that'
    IN -> 'by'
    IN -> 'on'
    IN -> 'inside'
    IN -> 'put'
    IN -> 'after'
    IN -> 'in'
    IN -> 'than'
    IN -> 'from'
    VBP -> 'cartoon'
    VBP -> 'do'
    VBP -> 'matter'
    VBP -> 'dad'
    VBP -> 'poisonous'
    VBP -> 'child'
    VBP -> 'hatch'
    VBP -> 'expect'
    VBP -> 'cleaner'
    VBP -> 'spend'
    VBP -> 'head'
    VBP -> 'believe'
    VBP -> 'friend'
    VBP -> 'ill'
    VBP -> 'spider'
    VBP -> 'are'
    VBP -> 'begin'
    VBP -> 'kill'
    VBP -> 'am'
    VBP -> 'get'
    VBP -> 'say'
    VBP -> 'bag'
    VBP -> 'wherever'
    VB -> 'become'
    VB -> 'dead'
    VB -> 'alive'
    VB -> 'tears'
    VB -> 'be'
    VB -> 'rushing'
    VB -> 'make'
    VB -> 'more'
    VB -> 'go'
    VB -> 'have'
    VB -> 'myself'
    VBZ -> 'goes'
    VBZ -> 'unfolds'
    VBZ -> 'loads'
    VBZ -> 'heroes'
    VBZ -> 'says'
    VBZ -> 'is'
    VBZ -> 'does'
    WP -> 'what'
    WRB -> 'when'
    CD -> 'one'
    CD -> 'nine'
    VBN -> 'made'
    VBN -> 'done'
    VBN -> 'raised'
    VBN -> 'fallen'
    VBN -> 'spoiled'
    VBN -> 'called'
    VBN -> 'squeezed'
    VBN -> 'sucked'
    VBN -> 'played'
    VBN -> 'scared'
    VBN -> 'lost'
    VBN -> 'used'
    VBN -> 'been'
    VBN -> 'bed'
    VBN -> 'met'
    VBN -> 'seen'
    PRP -> 'their'
    PRP -> 'your'
    PRP -> 'our'
    PRP -> 'his'
    JJR -> 'younger'
    WDT -> 'which'
    MD -> 'wo'
    MD -> 'would'
    MD -> 'will'
    MD -> 'could'
    MD -> 'should'
    JJS -> 'greatest'
    CC -> 'and'
    CC -> 'but'
""")
