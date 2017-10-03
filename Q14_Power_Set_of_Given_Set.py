# given a set, please give its power set, which is the set of the empty set, itself, and all its subsets

s = [1, 3, 3, 5, 7, 9]

# for loop method
def find_power_set(s):
    p = [[]]
    if s == []:
        return p
    else:
        for i in range(len(s)):
            temp = [[], [s[i]]]
            p = [x+y for x in p for y in temp]
    return p

print(find_power_set(s))
# recursive method

def find_power_set2(s):
    p = [[]]
    if s == []:
        return p
    else:
        p = find_power_set2(s[1:])
        return p + [[s[0]] + x for x in p]
print(find_power_set2(s))