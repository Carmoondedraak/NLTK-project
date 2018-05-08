import nltk

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

def tags(text, rules):
    #print(nltk.pos_tag(text))
    for tuplee in nltk.pos_tag(text):
        add_rule(rules, tuplee[1], tuplee[0])
    return rules

def add_rule(rules, left, right):
    # If the key does not already exist, initialize it with a list.
    if left not in rules:
        rules[left] = []
    rules[left].append(right)
