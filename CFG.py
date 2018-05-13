import nltk
from nltk import CFG
from nltk.grammar import FeatureGrammar
from nltk.parse import RecursiveDescentParser, FeatureEarleyChartParser, ChartParser

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

# I would hunt the cobwebs for lurking eight-legged predators
# TOEGEVOEGD : zin gesplit, eerst: .... ,hunting the  cobwebs....

cfg_1 = CFG.fromstring("""
 S -> NP VP
 NP -> Pro
 NP -> NP PP
 NP -> D N
 NP -> Adj NP
 NP -> CC NP
 VP -> V PP
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


 D -> 'the'
 Pro -> 'I' | 'them' | 'it' | 'It'
 Prep -> 'to' | 'by' | 'through' | 'at' | 'of' | 'for' | 'in'
 N -> 'spiders' | 'hours' | 'shed' | 'bottom' | 'garden' | 'cobwebs' | 'predators' | 'one' | 'bedroom' | 'mom'
 V -> 'have' | 'used' | 'collect' | 'was' | 'would' | 'rooting' | 'found'
 Adv -> 'always'
 Vt -> 'been' | 'spend' | 'hunt' | 'bring' | 'let' | 'drive'
 Vtt -> 'fascinated' | 'loose' | 'crazy'
 Conj -> 'when' | 'When'
 Adj -> 'younger' | 'dusty' | 'old' | 'our' | 'lurking' | 'eight-legged' | 'my'
 C -> 'and' | 'or'
""")

cfg_1_parser = ChartParser(cfg_1)
sentence = 'It used to drive my mom crazy'
check_sentence(cfg_1_parser, sentence)
