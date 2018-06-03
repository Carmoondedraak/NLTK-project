# ----------------------------------------------------------------------------
# Carmen Veenker & Sven Boogmans
# NLTK project
#
#-----------------------------------------------------------------------------
import nltk
import PCF as p
import CFG as c
import onzecfg as cc
import information as info
import THE_PARSER as pars
from nltk import CFG
from nltk.grammar import FeatureGrammar
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.parse import RecursiveDescentParser, FeatureEarleyChartParser, ChartParser, ShiftReduceParser

def main():
    raw = read()
    rules = dict()
    sent_tokenize_list = sent_tokenize(raw)
    word_tokenize_list = info.tokenize(raw)
    #print(word_tokenize_list)

    word_tokenize_list = info.sentence_stripping(word_tokenize_list)
    sent_tokenize_list = info.sentence_stripping(sent_tokenize_list)
    print(word_tokenize_list)
    rules = p.tags(list(set(word_tokenize_list)), rules)
    cfgg = c.add_lexicons_to_cfg(rules)
    cfgg = c.add_rules_to_cfg(cfgg,cfg_1)
    c.write_to_doc(cfgg)
    #
    # #print(rules)
    # #pos_tags = [pos for (token,pos)  in nltk.pos_tag(raw)]
    # #print(pos_tags)
    # mem_list = p.shift_reduce(rules, sent_tokenize_list[0].split(), ['S'] )
    #print(sent_tokenize_list[0])
    #grammar = nltk.parse_cfg(cfgg)
    #grammar = cfgg
    print(sent_tokenize_list[2])
    parser = ShiftReduceParser(pars.cfg_1)
    #print(cc.cfg_1)
    #print(parser)
    print(nltk.pos_tag([I],[have],[always],[been],[fascinated], [by], [spiders]))
    p.check_sentence(parser, "I have always been fascinated by spiders")
    #p.shift_reduce(cc.cfg_1, ['I','have'] , 'S')

cfg_1 = ["S -> NP VP", "NP -> Pro", "NP -> NP PP", "NP -> D N","NP -> Adj NP",
"NP -> CC NP", "VP -> V PP", "VP -> V N", "VP -> V Adv Vt Vtt PP", "VP -> V PP",
  "VP -> V NP", "VP -> V PP CC", "VP -> V Adj", "VP -> V Prep Vt N Vtt", "V -> V Vt N V",
   "V -> V Vt NP", "V -> V Vt Pro Prep C Vt Pro Vtt", "N -> Adj N", "PP -> Prep NP",
 "PP -> Prep N", "PP -> Prep V Pro", "Adj -> Adj Adj", "CC -> Conj NP VP"]

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
#cfg_1_parser = RecursiveDescentParser(cfg_1)
#check_sentence(cfg_1_parser, sent_tokenize_list[1])

main()
