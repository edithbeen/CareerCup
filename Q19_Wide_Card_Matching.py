# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false

def isMatch(s, p):
    if len(p) == 0:
        if len(s) == 0:
            return True
        else:
            return False
    if len(p) == 1:
        if p == '*':
            return True
        elif p == '?' and len(s) == 1:
            return True
        else:
            return p == s
    first_char = p[0]
    if len(s) == 0:
        if first_char != '*':
            return False
        else:
            return isMatch(s, p[1:])
    if first_char == '?':
        return isMatch(s[1:], p[1:])
    elif first_char != '*':
        return s.startswith(p[0]) and isMatch(s[1:], p[1:])
    else:
        for i in range(len(s)):
            if isMatch(s[i:], p[1:]):
                return True
        return False


print(isMatch("aa", "*"))
print(isMatch('ho', 'ho**'))
print(isMatch('', '?*'))
print(isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", "***bba**a*bbba**aab**b"))
