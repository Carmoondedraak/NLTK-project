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

def tags(text, rules):
    for tuplee in nltk.pos_tag(text):
        add_rule(rules, tuplee[1], [tuplee[0]])
    return rules


 # D -> 'the'
 # Pro -> 'I' | 'them' | 'it' | 'It'
 # Prep -> 'to' | 'by' | 'through' | 'at' | 'of' | 'for' | 'in'
 # N -> 'spiders' | 'hours' | 'shed' | 'bottom' | 'garden' | 'cobwebs' | 'predators' | 'one' | 'bedroom' | 'mom'
 # V -> 'have' | 'used' | 'collect' | 'was' | 'would' | 'rooting' | 'found'
 # Adv -> 'always'
 # Vt -> 'been' | 'spend' | 'hunt' | 'bring' | 'let' | 'drive'
 # Vtt -> 'fascinated' | 'loose' | 'crazy'
 # Conj -> 'when' | 'When'
 # Adj -> 'younger' | 'dusty' | 'old' | 'our' | 'lurking' | 'eight-legged' | 'my'
 # C -> 'and' | 'or'

cfg_2 = CFG.fromstring("""

S -> NP VP
S -> S Conj S
Adj -> Adj Adj
NP -> Adj N
NP -> Pro
NP -> N
NP -> D Adj N
NP -> D N
VP -> V VP
V -> V V N V
VP -> VP VP
VP -> Adv V
VP -> V PP
VP -> V Adj
VP -> V Im V
VP -> V V NP
VP -> VP NP
VP -> VP PP
PP -> Prep NP
PP -> PP PP



 Pro -> 'I' | 'them'
 D -> 'the'
 N -> 'spiders' | 'hours' | 'shed' | 'bottom' | 'garden' | 'cobwebs' | 'predators'
 V -> 'have' | 'been' | 'fascinated' | 'used' | 'collect' | 'was' | 'would' | 'spend' | 'rooting'| 'hunt'
 Im -> 'to'
 Adv -> 'always'
 Prep -> 'by' | 'through' | 'at' | 'of' | 'for'
 Conj -> 'when'
 Adj -> 'younger' | 'dusty' | 'old' | 'our' | 'lurking' | 'eight-legged'


""")

# adds the lexicons to our CFG's.
def add_lexicons_to_cfg(words_rules):
    CFG_string = ""

    # for key in words_rules:
    #     rule = key
    #     lexicons = words_rules[key]
    #     CFG_string = CFG_string + '\n' + rule + ' -> '
    #     #file.write(CFG_string + '\n' + rule + ' -> ')
    #     for i in range(len(lexicons)-1):
    #         #file.write( CFG_string + "'{}'".format(lexicons[i][0]) + '|')
    #         CFG_string = CFG_string + "'{}'".format(lexicons[i][0]) + '|'
    #     CFG_string = CFG_string + "'{}'".format(lexicons[len(lexicons)-1][0]) + '\n'
    #     #file.write( CFG_string + "'{}'".format(lexicons[len(lexicons)-1][0]) + '\n')
    # print(CFG_string)
    # return CFG_string

    for key in words_rules:
        rule = key
        lexicons = words_rules[key]
        #CFG_string = CFG_string + '\n' + rule + ' -> '
        #file.write(CFG_string + '\n' + rule + ' -> ')
        for i in range(len(lexicons)-1):
            #file.write( CFG_string + "'{}'".format(lexicons[i][0]) + '|')
            CFG_string = CFG_string + '\n' + rule + ' -> ' + "'{}'".format(lexicons[i][0])    #print(CFG_string)
    return CFG_string

def write_to_doc(cfg):
    file = open("tryall.py", "w")
    lines = file.readlines()
    line[2] = file.write(cfg)

    file.close()



def add_rules_to_cfg(CFG_string, cfg_1):
    for i in cfg_1:
        CFG_string = CFG_string + '\n' + "{}".format(i)
    return CFG_string

#word_rules = nltk.pos_tag(['When', 'I', 'found', 'one', 'I', 'would', 'bring', 'it', 'in', 'and', 'let', 'it', 'loose', 'in', 'my', 'bedroom'])
#cfg_3 = add_lexicons_to_cfg(word_rules)
#cfg_3 = add_rules_to_cfg(cfg_3, cfg_1)
#print( add_lexicons_to_cfg(word_rules))
