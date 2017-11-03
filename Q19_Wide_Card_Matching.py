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

# def isMatch(s, p):
#     if len(p) == 0:
#         if len(s) == 0:
#             return True
#         else:
#             return False
#     if len(p) == 1:
#         if p == '*':
#             return True
#         elif p == '?' and len(s) == 1:
#             return True
#         else:
#             return p == s
#     first_char = p[0]
#     if len(s) == 0:
#         if first_char != '*':
#             return False
#         else:
#             for i in range(1, len(p)):
#                 if p[i] != '*':
#                     return False
#             return True
#     if first_char == '?':
#         return isMatch(s[1:], p[1:])
#     elif first_char != '*':
#         return s.startswith(p[0]) and isMatch(s[1:], p[1:])
#     else:
#         for k in range(1, len(p)):
#             if p[k] != '*':
#                 p = p[k:]
#                 break
#             if k == len(p) - 1:
#                 return True
#         for i in range(len(s)):
#             if isMatch(s[i:], p):
#                 return True
#         return False


def isMatch(text, pattern):
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '?'}

    if len(pattern) >= 1 and pattern[0] == '*':
        if len(pattern) >=2 and pattern[1] == '*':
            return isMatch(text, pattern[1:])
        else:
            return (isMatch(text, pattern[1:]) or
                    isMatch(text[1:], pattern))
    else:
        return first_match and isMatch(text[1:], pattern[1:])



print(isMatch("aa", "*"))
print(isMatch('ho', 'ho**'))
print(isMatch('', '?*'))
# print(isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", "***bba**a*bbba**aab**b"))
#
