# Reverse a list without using extra memory

# cheet with list comprehension

l = [3, 9, 'a', 0, 2, 5]

print([l[len(l)-i-1] for i in range(len(l))])

# switch the list symetrically

def switch(l):
    length = len(l)
    for i in range(length//2):
        temp = l[i]
        l[i] = l[length - i - 1]
        l[length - i - 1] = temp

    return l

print(switch(l))