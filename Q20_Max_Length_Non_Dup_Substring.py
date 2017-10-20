#Given a string, find the length of the longest substring without repeating characters.

def findLongest(s):
    d = {}
    max_length = 0
    pos = -1
    for index, letter in enumerate(s):
        if letter in d:
            pos = max(d[letter], pos)
        max_length = max(max_length, index - pos)
        d[letter] = index
    return max_length

# now, find the longest substring, if same longest, return the first one
def findLongestSubstring(s):
    d = {}
    substring = ''
    pos = -1
    for index, letter in enumerate(s):
        if letter in d:
            pos = max(d[letter], pos)
        if index - pos > len(substring):
            substring = s[pos+1:index+1]
        d[letter] = index
    return substring
s = 'aaabbbc'
print(findLongest(s))
print(findLongestSubstring(s))