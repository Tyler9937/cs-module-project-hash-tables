import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

words = words.split()
cache = {}

for index, word in enumerate(words):
    if word not in cache:
        cache[word] = []

    if index != len(words) - 1:
        cache[word].append(words[index + 1])



def isupper_func(word, dict):
    while word.isupper() is False:
        word = random.choice(list(dict))
    return word

def islower_func(word, dict):
    if word.isupper() is True:
        word = random.choice(list(dict))
    return word

def make_sent(num_sentences):
    for i in range(num_sentences):
        word = random.choice(list(cache))
        word = isupper_func(word, cache)
        string = word

        last_word_switch = True
        
        while last_word_switch is True:
            next_list = cache[word]
            word = random.choice(next_list)
            word = islower_func(word, next_list)

            string = string + " " + word
        
            
            if '.' in word:
                last_word_switch = False

        string = string.replace('"', '')

        print(string)
        print(' ')
        print(' ')

make_sent(5)
            
                
        



# TODO: construct 5 random sentences
# Your code here

