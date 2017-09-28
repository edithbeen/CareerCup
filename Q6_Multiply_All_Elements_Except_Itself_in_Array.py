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

# list expression, easier eay
ls = [prod(array[:i] + array[i+1:]) for i in range(len(array))]


