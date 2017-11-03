# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#
# The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

def reverseInt(n):
    sign = 1
    if n < 0:
        sign = -1
        n = - n
    rev = 0
    while n >= 10:
        rev = rev*10 + n%10
        n = n//10
    try:
        rev = (rev*10 + n%10)*sign
    except:
        return 0
    return rev
