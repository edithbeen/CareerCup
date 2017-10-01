# a k-palindrome string is a string which transforms to a palindrome if at most k character is removed
# given a string s and an integer k, write a function that returns Yes if it is a k-palindrome, otherwise No
# S has at most 20,000 characters, 0<k<=30

# recursive method

def is_K_Palindrome(s, k):
    if k < 0:
        return False
    if len(s) == 0 or len(s) == 1:
        return True
    start_chr = s[0]
    end_chr = s[-1]
    if start_chr == end_chr:
        return is_K_Palindrome(s[1:-1], k)
    else:
        return is_K_Palindrome(s[1:], k-1) or is_K_Palindrome(s[:-1], k-1)



s = 'abbaabbsade'
print(is_K_Palindrome(s, 5))
