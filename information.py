import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
# download nltk.download('punkt')
# download nltk.download('averaged_perceptron_tagger')

# Tokenizes the sentences and words.
def tokenize(raw):
    sent_tokenize_list = sent_tokenize(raw)
    word_tokenize_list = word_tokenize(raw)
    new_word_list = []
    for word in word_tokenize_list:
        if word != 'I' and word != 'Darren':
            word = word.lower()
            new_word_list += [word]
    new_word_list += ['I']
    new_word_list += ['Darren']

    # Gives information about the text.
    print("Amount of sentences:", len(sent_tokenize_list))
    print("length of text", len(word_tokenize_list))
    print("length of vocabulary:", len(sorted(set(word_tokenize_list))))
    return new_word_list

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

# counts how many times each word is used.
def word_count2(word_tokenize_list, raw):
    word_list = []
    for word in sorted(set(word_tokenize_list)):
        count = raw.count(word)
        word_list += [tuple((word, count))]
    return word_list

# strips the sentences from their punctuation marks.
def sentence_stripping(sent_tokenize_list):
    new_word_list = []
    #print(sent_tokenize_list)
    for word in sent_tokenize_list:
        word = word.strip('.')
        word = word.strip('?')
        word = word.strip('(')
        word = word.strip(')')
        word = word.strip('!')
        word = word.strip(':')
        word = word.strip('""')
        word = word.strip("''")
        word = word.strip(',')
        word = word.strip("``")
        #print(word)
        if word is not '':
            new_word_list += [word]
    return new_word_list
