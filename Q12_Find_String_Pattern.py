# 1
# 11
# 21
# 1211
# 111221
# 312211

# exhaustive method
def find_pattern(s):
    if (len(s) == 1):
        return '1' + s
    output = ''
    current_chr = previous_chr = s[0]
    count = 1
    for i in range(1, len(s)):
        current_chr = s[i]
        if current_chr == previous_chr:
            count += 1
        else:
            output += str(count) + previous_chr
            previous_chr = current_chr
            count = 1
    return output + str(count) + previous_chr


print(find_pattern('1233323444'))

# recursive method
def find_pattern2(s, p=''):
    if len(s) == 0:
        return p
    current_chr = previous_chr = s[0]
    count = 1
    for i in range(1, len(s)):
        current_chr = s[i]
        if current_chr == previous_chr:
            count += 1
            if i == len(s) - 1:
                return p + str(count) + previous_chr
        else:
            return find_pattern2(s[i:], p + str(count) + previous_chr)

print(find_pattern2('332122444'))
