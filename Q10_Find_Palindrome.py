# Given a Palindrome, find the counts of Palindrome substrings.

# question: how do we count duplicates?
# let's consider duplicates, using a hash table to store all the duplicates
# the key of the dictionary will be the length of the palindrome, and the values will be the patterns of the palindrome

# first define a function to determine if a string is a palindrome
def isPalindrome(s):
    l = len(s)
    for i in range(l//2):
        if s[i] != s[l-i-1]:
            return False
    return True

# now, recursive funciton to determine the count of palindromes
# a dictionary to record all the patterns
s = 'abccbaabccba'

def countPalindrome(s):
    patterns = [None for i in range(len(s))]
    count = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if isPalindrome(s[i:j]):
                if patterns[j-i-1] is None:
                    patterns[j-i-1] = [s[i:j]]
                    count += 1
                elif s[i:j] not in patterns[j-i-1]:
                    patterns[j-i-1] += [s[i:j]]
                    count += 1
    print(patterns)
    return count

print(countPalindrome(s))

