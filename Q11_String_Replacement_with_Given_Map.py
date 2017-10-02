# given a string and a hash map with all possible mapping for some characters in the string
# find all possible mappings, including it self

s = 'fab'
m = {'f':['M', '8'], 'b':['4', 'c', 't']}

def find_mapping(s):
    l = None
    for i in range(len(s)):
        temp = [s[i]]
        if m.get(s[i]) is not None:
            temp += m[s[i]]
        if l is None:
            l = temp
        else:
            l = [x+y for x in l for y in temp]
    return l

print(find_mapping(s))