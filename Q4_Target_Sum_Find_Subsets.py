# given a target sum, find all the possible subsets of positive integers that sums up to the target sum
# eg given a target sum 15, a possible subset is [4, 5, 6]

# question 1: 0 included?
# Let's first consider the case when 0 is not included
# question 2: limit of sum? if the limit is low, then we just generate all possible lists that sum up to the target sum
# then we find all those that are sets
# question 3: the subset is a set, or a list?

# first let's attack with exhaustive method, generating all sets(NOT the lists!)
results = []

def gen_list(ts, current_list=[]):
    if ts == 0:
        results.append(current_list)
        return
    for i in (range(1, ts+1)):
        # sets with out duplicates are returned
        if len(current_list) == 0 or (i not in current_list and i > current_list[-1]):
        # # subsets are returned
        # if len(current_list) == 0 or i >= current_list[-1]:
            gen_list(ts-i, current_list + [i])

gen_list(10)
print(results)

# now let's make this question a little bit harder
# let's say we would like to have all the subsets of an array with duplicates that sum up to the target
# the output can be a list with duplicates now as the array could contain duplicates as well


results = []
def gen_list(ts, current_array, current_list=[]):
    if ts == 0:
        print(current_list)
        results.append(current_list)
        return
    elif len(current_array) == 0:
        return
    for i in range(1, ts+1):
        if i in current_array and (len(current_list)== 0 or i >= current_list[-1]):
            gen_list(ts-i, [x for x in current_array if x >= i][1:], current_list + [i])

array = [5, 8, 2, 2, 9, 7, 4, 5, 7]
array.sort()
print(array)
gen_list(15, array)
print(results)