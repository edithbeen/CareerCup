# Cound # of distinct words in a sequence

# question: how long is the sequence? Is it a stack, queue, or a stream?
# all elements in the sequence is a word? how do you define a word?

def count_distinct_words(l, dictionary):
    s = []
    for w in l:
        if w not in s and w in dictionary:
            s.append(s)
    return len(s)

l = ['wow', 'apple', 'pear', 'seie', 'seiw']
dictionary = ['fruit', 'apple', 'pear', 'sentence', 'hello', 'regular']

print(count_distinct_words(l, dictionary))
# count the number of words appear in a sentence using a harsh map
# question: sentence, assuming not too long?
# punctuation marks?
# capitalized, non_capitalized count as one word?

import re
def word_cleanser(w):
    result = w
    while result.startswith('\'') or result.startswith('-'):
        result = result[1:]
    while result.endswith('\'') or result.endswith('-'):
        result = result[:-1]
    return result

def count_words(s, word, dictionary):
    if not isinstance(s, str):
        print('Invalid Input')
        return
    s_list = re.split('[^a-z\'\-A-Z]', s)
    mytable = {}
    for w in s_list:
        w_clean = word_cleanser(w)
        if mytable.get(w_clean) is not None:
            mytable[w_clean] += 1
        elif mytable.get(w_clean.lower()) is not None:
            mytable[w_clean.lower()] += 1
        elif w_clean in dictionary:
            mytable[w_clean] = 1
        elif w_clean.lower() in dictionary:
            mytable[w_clean.lower()] = 1
    if mytable.get(word) is None:
        return 0
    else:
        return mytable[word]


s = 'I\'m a \'\'regular\' sentence!!!Haaha, you can-not see me!! Sentence, sentence, sentence'
print(count_words(s, 'regular', dictionary))
print(count_words(s, 'sentence', dictionary))

print(re.sub('[^A-Za-z\'\-]', ' ', s))
# count the occurance of a substring in a string
s = 'aababacababababa'
subs = 'aba'
# C_s = C_s[1:] + if s.startswith(subs)

def count_subs(s, subs):
    count = 0
    for i in range(len(s)- len(subs) + 1):
        if s[i:].startswith(subs):
            count += 1
    return count

def count_subs2(s, subs):
    if len(s) < len(subs):
        return 0
    if s.startswith(subs):
        return 1 + count_subs2(s[1:], subs)
    else:
        return count_subs2(s[1:],subs)


print(count_subs(s, subs))
print(count_subs2(s, subs))
