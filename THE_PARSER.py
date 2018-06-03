from nltk.grammar import FeatureGrammar
from nltk import CFG
from nltk.parse.generate import generate, demo_grammar
from nltk.parse import RecursiveDescentParser, FeatureEarleyChartParser, ChartParser
from nltk.tokenize import sent_tokenize
import nltk
from random import choice

# Function that works for multiple types of parsers
def check_sentence(parser, sentence):
    print("--------------------------------------------------")
    print("Checking if provided sentence matches the grammar:")
    print(sentence)
    if isinstance(sentence, str):
        sentence = sentence.split()
    tree_found = False
    results = parser.parse(sentence)
    for tree in results:
        tree_found = True
        print(tree)
    if not tree_found:
        print(sentence, "Does not match the provided grammar.")
    print("--------------------------------------------------")
    return tree_found

###################### THE CFG #############################

from nltk import ChartParser
from random import choice
grammar = CFG.fromstring("""

    S -> NP VP
    S -> NP
    NP -> PRP
    NP -> NP PP
    NP -> Pro
    NP -> N
    NP -> D Adj N
    NP -> D N
    NP -> CCC NP
    V -> V V N V
    V -> V V NP
    V -> V V Pro Prep C V Pro V
    VP -> VP VP
    VP -> V VP
    VP -> Adv V
    VP -> V PP
    VP -> V Adj
    VP -> V Im V
    VP -> V V NP
    VP -> VP NP
    VP -> VP PP
    VP -> V N
    VP -> V PP CC
    VP -> V NP
    VP -> V Adv V V PP
    VP -> V Prep V N V
    VP -> V V
    PP -> Prep NP
    PP -> Prep N
    PP -> PP PP
    PP -> Prep V Pro
    N -> Adj N
    N -> D Adj
    CC -> Conj NP VP


    N -> NN
    N -> NNS
    Adj -> JJ
    Adj -> JJR
    Adj -> JJS
    V -> VBG
    V -> VBD
    V -> VBP
    V -> VB
    V -> VBZ
    V -> VBN
    V -> MD
    Adv -> RB
    Adv -> WRB
    Pro -> PRP
    Pro -> WP
    D -> DT
    D -> WDT
    Prep -> IN
    C -> CC

    NNS -> 'calls'
    NNS -> 'noises'
    NNS -> 'pants'
    NNS -> 'names'
    NNS -> 'sorts'
    NNS -> 'prizes'
    NNS -> 'tantrums'
    NNS -> 'stores'
    NNS -> 'works'
    NNS -> 'cleaners'
    NNS -> 'people'
    NNS -> 'spiders'
    NNS -> 'loads'
    NNS -> 'predators'
    NNS -> 'hours'
    NNS -> 'cockroaches'
    NNS -> 'costs'
    NNS -> 'treats'
    NNS -> 'mistakes'
    NNS -> 'parents'
    NNS -> 'tears'
    NNS -> 'pieces'
    NNS -> 'things'
    NNS -> 'books'
    NNS -> 'teachers'
    NNS -> 'reasons'
    NNS -> 'heroes'
    NNS -> 'wins'
    NNS -> 'characters'
    NNS -> 'bones'
    NNS -> 'tale'
    NNS -> 'eggs'
    NNS -> 'knows'
    NNS -> 'women'
    NNS -> 'friends'
    NN -> 'mine'
    NN -> 'vacuum'
    NN -> 'begin'
    NN -> 'friend'
    NN -> 'throat'
    NN -> 'because…'
    NN -> 'watch'
    NN -> 'fault'
    NN -> 'car'
    NN -> 'make'
    NN -> 'shan'
    NN -> 'dusty'
    NN -> 'humming'
    NN -> 'guy'
    NN -> 'reason'
    NN -> 'child'
    NN -> 'book'
    NN -> 'storm'
    NN -> 'story'
    NN -> 'day'
    NN -> 'nothing'
    NN -> 'dalton'
    NN -> 'sliding'
    NN -> 'tell'
    NN -> 'way'
    NN -> 'road'
    NN -> 'stroller'
    NN -> 'laying'
    NN -> 'join'
    NN -> 'thing'
    NN -> 'night'
    NN -> 'slip'
    NN -> 'time'
    NN -> 'name'
    NN -> 'kill'
    NN -> 'everything'
    NN -> 'end'
    NN -> 'money'
    NN -> 'sleep'
    NN -> 'fall'
    NN -> 'garden'
    NN -> 'head'
    NN -> 've'
    NN -> 'nobody'
    NN -> 'drive'
    NN -> 'something'
    NN -> 'hunt'
    NN -> 'month'
    NN -> 'cost'
    NN -> 'matter'
    NN -> 'd'
    NN -> 'eat'
    NN -> 'bed'
    NN -> 'ripped'
    NN -> 'everyone'
    NN -> 'lunch'
    NN -> 'threw'
    NN -> 'bag'
    NN -> 'introduction'
    NN -> 'life'
    NN -> 'baby'
    NN -> 'country'
    NN -> 'describe'
    NN -> 'school'
    NN -> 'bottom'
    NN -> 'lot'
    NN -> 'town'
    NN -> 'get'
    NN -> 'toilet'
    NN -> 'song'
    NN -> 'hatch'
    NN -> 'collect'
    NN -> 'care'
    NN -> 'guard'
    NN -> 'stick'
    NN -> 'hand'
    NN -> 'bedroom'
    NN -> 'hour'
    NN -> 'everybody'
    NN -> 'bathroom'
    NN -> 'sound'
    NN -> 'someone'
    NN -> 'look'
    NN -> 'crazy'
    NN -> 'imagine'
    NN -> 'class'
    NN -> 'gift'
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
    IN -> 'by'
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
    MD -> 'have'
    JJS -> 'greatest'
    CC -> 'and'
    CC -> 'but'
""")

def produce(grammar, symbol):
    words = []
    productions = grammar.productions(lhs = symbol)
    if productions != None:
        production = choice(productions)
        for sym in production.rhs():
            if isinstance(sym, str):
                words.append(sym)
            else:
                words.extend(produce(grammar, sym))
        return words
    else:
        print("hey")
        produce(gr, gr.start())


parser = ChartParser(grammar)
gr = parser.grammar()
result = None
while result == None:
    try:
        result = ' '.join(produce(gr, gr.start()))
    except:
        pass

print(result)


#for sentence in generate(cfg_1, depth=5):
#    print(' '.join(sentence))

#parser = ChartParser(cfg_1)
#check_sentence(parser, 'I kill leonard in his bedroom')
