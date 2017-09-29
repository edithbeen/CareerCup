# given a numeric integer as input, return a array with the multiplication of all values in this array except itself

# question: null value and na values?
from numpy import prod

def multi_others(array):
    ls = []
    for i in range(len(array)):
        value_i = prod(array[:i] + array[i+1:])
        ls = ls + [value_i]
    return ls

array = [3, 3, 5, 7]
print(multi_others(array))

# list expression, check
ls = [prod(array[:i] + array[i+1:]) for i in range(len(array))]

# we can also implement our own function of prod
def prod(l):
    result = 1
    for item in l:
        result *= item
    return result

# define a function to implemnt our own function of pow
def pow(n, p):
    result = n
    if p == 0:
        return 1
    else:
        for i in range(p-1):
            result *= n

    return result

print(pow(2, 5))

