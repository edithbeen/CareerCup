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
print(len(set(swap_unique(s))))
print(swap_count_unique(s))



# now deal with string with duplicates

# remember, if there are n consecutive characters are the same, then, we can just treat them as one character

def swap(s):
    l = []
    if len(s) == 0:
        return ['']
    if len(s) == 1:
        return [s]
    if s[0] == s[1]:
        j = len(s)
        for i in range(2, len(s)):
            if s[i] != s[0]:
                j = i
                break
        l = [s[:j-1] + x for x in swap(s[j-1:])]
    else:
        l = [s[1] + s[0] + x for x in swap(s[2:])] + [s[0] + x for x in swap(s[1:])]
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
        j = len(s)
        for i in range(2, len(s)):
            if s[i] != s[0]:
                j = i
                count = swap_count(s[j - 1:])
                break
        if j == len(s):
            count = 1

    else:
        count = swap_count(s[2:]) + swap_count(s[1:])
    return count


s = '1777667577'

swap_l = swap(s)
swap_set = set(swap_l)
print(swap_l)
print(len(swap_l))
print(swap_count(s))
print(len(swap_set))