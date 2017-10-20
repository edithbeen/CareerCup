# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
def getPalindrome(l, c, r):
    p = c
    len_l = len(l)
    len_r = len(r)
    for i in range(min(len_l, len_r)):
        if l[-i-1] == r[i]:
            p = r[i] + p + r[i]
        else:
            break
    return p

def longestPalindrome(s):
    n = len(s)
    long_p = ''
    for i in range(0, 2*n -1):
        candidate = ''
        if n - i//2 -1 < len(long_p)//2:
            break
        if i%2 == 0:
            candidate = getPalindrome(s[:i//2], s[i//2], s[i//2+1:])
        else:
            candidate = getPalindrome(s[:(i+1)//2], '', s[i//2+1:])
        if len(candidate) > len(long_p):
            long_p = candidate
    return long_p

s = 'abcacbade'
print(longestPalindrome(s))


