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
    for tuplee in nltk.pos_tag(text):
        add_rule(rules, tuplee[1], [tuplee[0]])
    return rules

def add_rule(rules, left, right):
    # If the key does not already exist, initialize it with a list.
    if left not in rules:
        rules[left] = []
    rules[left].append(right)

def reduce(rules, mem_list):
    reduced = True
    while reduced == True:
        reduced = False
        for key in rules:
            if [mem_list[-1]] in rules[key]:
                mem_list[-1] = key
                reduced = True
        for key in rules:
            if len(mem_list) >= 2:
                if [mem_list[-2], mem_list[-1]] in rules[key]:
                    mem_list = mem_list[:-1]
                    mem_list[-1] = key
                    reduced = True
        for key in rules:
            if len(mem_list) >= 3:
                if [mem_list[-3], mem_list[-2], mem_list[-1]] in rules[key]:
                    mem_list = mem_list[:-2]
                    mem_list[-1] = key
                    reduced = True
    return mem_list

## Actual Function

def shift_reduce(rules, atoms_list, goal):
    mem_list = []
    for atom in atoms_list:
        mem_list.append(atom)
        mem_list = reduce(rules, mem_list)
        print(mem_list)
        if mem_list == goal:

            return True
    return False
