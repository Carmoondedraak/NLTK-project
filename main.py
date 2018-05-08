# ----------------------------------------------------------------------------
# Carmen Veenker & Sven Boogmans
# NLTK project
#
#-----------------------------------------------------------------------------
import nltk
import PCF as p
import information as info
from nltk import CFG
from nltk.grammar import FeatureGrammar
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.parse import RecursiveDescentParser, FeatureEarleyChartParser

def main():
    raw = read()
    rules = dict()
    sent_tokenize_list = sent_tokenize(raw)
    word_tokenize_list = info.tokenize(raw)
    sent_tokenize_list = info.sentence_stripping(sent_tokenize_list)

    rules = p.tags(list(set(word_tokenize_list)), rules)
    print(rules)
    print(sent_tokenize_list[0].split())
    mem_list = p.shift_reduce(rules, sent_tokenize_list[1].split(), ['s'] )
    print(mem_list)

def read():
    f = open('DarrenShan.txt', 'rU')
    raw = f.read()
    sent_tokenize_list = sent_tokenize(raw)
    word_tokenize_list = info.tokenize(raw)
    word_dict = info.word_count(word_tokenize_list, raw)
    word_list = info.word_count2(word_tokenize_list, raw)

    #print(new_word_list)
    #print(sent_tokenize_list)
    most_used = (sorted(list(set(word_list)), key=lambda word: word[1]))

    info.word_usage(word_dict)
    return raw
    #Cfg(new_word_list)


# def Cfg(sent_tokenize_list):
#     cfg_1 = CFG.fromstring("""
#       S -> NP VP
#       NP -> Pro
#       VP -> V Adv Vt Vtt PP
#       PP -> Prep N
#       NP -> D N
#       VP -> V NP
#       VP -> V PP CC
#       PP -> Prep V Pro
#       CC -> Conj NP VP
#       VP -> V Adj
#       D -> 'the'
#       Pro -> 'I' | 'them'
#       Prep -> 'to' | 'by'
#       N -> 'spiders.'
#       V -> 'have' | 'used' | 'collect' | 'was'
#       Adv -> 'always'
#       Vt -> 'been'
#       Vtt -> 'fascinated'
#       Conj -> 'when'
#       Adj -> 'younger'
#       C -> 'and' | 'or'
#     """)
#     cfg_1_parser = RecursiveDescentParser(cfg_1)
#     check_sentence(cfg_1_parser, sent_tokenize_list[1])

main()
