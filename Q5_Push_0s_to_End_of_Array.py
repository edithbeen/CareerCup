# push all the 0s of an array to the end of the array
# this question is easy in Python environment

# question: does the array contains null value and n/a value?
# W/O LOG, we assume we would like to push a value in an array to the end

def push_value(array, value):
    n_values = len([x for x in array if x == value])
    new_array = [x for x in array if x != value] + [value for i in range(n_values)]
    print(new_array)
    return new_array

# test
import numpy as np
array = [1, 33, 5, 65, 'a', None, 4, np.nan, 5, 9, 0, 4, 'aa', 7, 4, 2, 0, 44, 2, 9]
push_value(array, 0)

