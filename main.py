# ----------------------------------------------------------------------------
# Carmen Veenker & Sven Boogmans
# NLTK project
#
#-----------------------------------------------------------------------------
import nltk
import information as info
from nltk import CFG
from nltk.grammar import FeatureGrammar
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.parse import RecursiveDescentParser, FeatureEarleyChartParser

def main():
    read()

def read():
    f = open('DarrenShan.txt', 'rU')
    raw = f.read()
    sent_tokenize_list = sent_tokenize(raw)
    word_tokenize_list = info.tokenize(raw)
    word_dict = info.word_count(word_tokenize_list, raw)
    word_list = info.word_count2(word_tokenize_list, raw)
    new_word_list = []
    for word in sent_tokenize_list:
        word = word.strip('.')
        new_word_list += [word]
    print(new_word_list)

    print(sent_tokenize_list)
    #print(sorted(word_list, key=lambda word: word[1]))
    info.word_usage(word_dict)
    Cfg(new_word_list)

# Function that works for multiple types of parsers (You are free to use something else if you want.)
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
        #tree.draw()
    if not tree_found:
        print(sentence, "Does not match the provided grammar.")
    print("--------------------------------------------------")
    return tree_found

def Cfg(sent_tokenize_list):
    cfg_1 = CFG.fromstring("""
      S -> NP VP
      NP -> Pro
      VP -> V Adv Vt Vtt PP
      PP -> Prep N
      NP -> D N
      VP -> V NP
      VP -> V PP CC
      PP -> Prep V Pro
      CC -> Conj NP VP
      VP -> V Adj
      D -> 'the'
      Pro -> 'I' | 'them'
      Prep -> 'to' | 'by'
      N -> 'spiders.'
      V -> 'have' | 'used' | 'collect' | 'was'
      Adv -> 'always'
      Vt -> 'been'
      Vtt -> 'fascinated'
      Conj -> 'when'
      Adj -> 'younger'
      C -> 'and' | 'or'
    """)
    cfg_1_parser = RecursiveDescentParser(cfg_1)
    check_sentence(cfg_1_parser, sent_tokenize_list[1])



main()
