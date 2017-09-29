# WAP to re-arrange an array and make arr[l] = arr[arr[l]]
# do in place w/0 using extra memeory
# the array contains 0 to n-1 integers

array = [1, 3, 2, 4, 0, 5]

# result preview, list expression, haha
print([array[x] for x in array])

# smart approach: we need to store the original arr[i] and arr[arr[i]] information in the ithe position with one value
# and later extract it
def arg_arr(array, size):
    for i in range(size):
        array[i] += size*(array[array[i]]%size)
    for i in range(size):
        array[i] = int(array[i]/size)
    return array

print(arg_arr(array, len(array)))