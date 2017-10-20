# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def findIndex(l, target):
    d = {}
    for index, item in enumerate(l):
        compliment = target - item
        if compliment in d:
            return [d.get(compliment), index]
        d[item] = index
    raise Exception('No Solution Found.')


l = [3, 4, 2, 33, 36, 8, 7, -5, -9, -2, 6]
print(findIndex(l, 0))


