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
    word_tokenize_list = info.tokenize(raw)
    word_dict = info.word_count(word_tokenize_list, raw)
    word_list = info.word_count2(word_tokenize_list, raw)
    print(sorted(word_list, key=lambda word: word[1]))
    info.word_usage(word_dict)
    s



main()
