import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# Tokenizes the sentences and words.
def tokenize(raw):
    sent_tokenize_list = sent_tokenize(raw)
    word_tokenize_list = word_tokenize(raw)

    # Gives information about the text.
    print("Amount of sentences:", len(sent_tokenize_list))
    print("length of text", len(word_tokenize_list))
    print("length of vocabulary:", len(sorted(set(word_tokenize_list))))
    return word_tokenize_list

# Counts how many times each word is used.
def word_count(word_tokenize_list, raw):
    word_dict = {}
    for word in sorted(set(word_tokenize_list)):
        count = raw.count(word)
        word_dict[word] = count
    return word_dict


# The most usual word is 'a', it comes up 325 times.
# The code underneath counts the word that is used mostly.
def word_usage(word_dict):
    listy = set([])
    dicty = word_dict
    for i in range(5):
        count = 0
        for key in dicty:
            if word_dict[key] > count:
                count = word_dict[key]
                listy = (tuple((key, count)))
    print(listy)

def word_count2(word_tokenize_list, raw):
    word_list = []
    for word in sorted(set(word_tokenize_list)):
        count = raw.count(word)
        word_list += [tuple((word, count))]
    return word_list