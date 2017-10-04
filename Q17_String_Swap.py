# given a string, you can swap only adjacent characters and every charcater can swap atmost once
# give the # of possible output after the swap

# Question: every character in the string is unique?

# let's deal with strings that contains unique elements

s = '123456'

def swap_unique(s):
    l = []
    if len(s) == 0:
        return ['']
    if len(s) == 1:
        return [s]
    l = [s[1]+s[0]+x for x in swap_unique(s[2:])] + [s[0]+x for x in swap_unique(s[1:])]
    return l

def swap_count_unique(s):
    count = 0
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    if len(s) == 2:
        return 2
    count = swap_count_unique(s[2:]) + swap_count_unique(s[1:])
    return count

print(swap_unique(s))
print(len(swap_unique(s)))
print(swap_count_unique(s))

# now deal with string with duplicates
# remember, if a character is the same as its adjacent character, it doesn't matter whether it swaps or not
def swap(s):
    l = []
    if len(s) == 0:
        return ['']
    if len(s) == 1:
        return [s]
    char_0 = s[0]
    char_1 = s[1]
    if char_0 == char_1:
        l = [s[0]+x for x in swap_unique(s[1:])]
    else:
        l = [s[1]+s[0]+x for x in swap_unique(s[2:])] + [s[0]+x for x in swap_unique(s[1:])]
    return l

def swap_count(s):
    count = 0
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 2
    if s[0] == s[1]:
        count = swap_count(s[1:])
    else:
        count = swap_count_unique(s[2:]) + swap_count_unique(s[1:])
    return count


s = '113433564335'

print(swap(s))
print(len(swap(s)))
print(swap_count(s))