# given a dictionary of key words, and and a key, if the key is the concatenation of arbitrary number of key words, return True, else return False
# question: can the key words be used more than once?

def is_Key_Words(words, key):
    if len(key) == 0:
        return True
    b = False
    for word in words:
        if key.startswith(word):
            b = is_Key_Words(words, key[len(word):])
        else:
            next
    return b

words = ['super', 'star', 'hello']
print(is_Key_Words(words, 'hellostar'))
print(is_Key_Words(words, 'helloworsld'))