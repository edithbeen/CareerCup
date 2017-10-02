# given a string and a hash map with all possible mapping for some characters in the string
# find all possible mappings, including it self

s = 'fab'
m = {'f':['M', '8'], 'b':['4', 'c', 't']}

l = []

def find_mapping(s):
    l = []
    for i in range(len(s)):
        temp = [s[i]]
        if m.get(s[i]) is not None:
            temp += m[s[i]]
        if len(l) == 0:
            l = temp
        else:
            new_l = l
            l = []
            for x in new_l:
                for y in temp:
                    l += [x+y]
    return l

print(find_mapping(s))