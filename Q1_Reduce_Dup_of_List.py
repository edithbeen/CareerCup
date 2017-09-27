# I'm glad that eventually, I am going to start this.
# I'll grab random interview coding questions from Careercup.com, and write my own solution in Python.
# Here is the first one.

# Q1 for a list with duplicated values, how can you find the duplicates?

# I try to solve this with hash table. In Python, we can use dictionary.

# first, we create a random list with duplicates. WLOG, we create a list of non-negative integers
# package for random integer creation
from random import randint
# here it is, a list of 200 integers
l = [randint(0, 100) for i in range(200)]

# a function to find the duplicates of a given list
def find_dup(l):
    # create a dictionary to store the unique values of the list as keys, and the position of those values as values
    dict = {}
    for i in range(len(l)):
        if l[i] in dict.keys():
            dict[l[i]] = dict[l[i]] + [i]
        else:
            dict[l[i]] = [i]
    dup = {k:v for (k, v) in dict.items() if len(dict[k])>1 }
    return dup

# another function that requires more code but more efficient as it only loop once
def find_dup_eff(l):
    dict = {}
    dup = {}
    for i in range(len(l)):
        if l[i] in dup.keys():
            dup[l[i]] = dup[l[i]] + [i]
        elif l[i] in dict.keys():
            dup[l[i]] = dict[l[i]] + [i]
            dict.pop(l[i])
        else:
            dict[l[i]] = [i]
    return dup


# test:
dup = find_dup(l)
dup_eff = find_dup_eff(l)
print(dup)
print(dup_eff)

