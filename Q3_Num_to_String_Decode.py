# set a = 1, b = 2, ..., z = 26
# given a number, find all possible string it represents
# eg: input 1123, the output should be aabc, kbc, alc, ...
# ask how long is the code?
# does this code contains 0?

# a list to store all the results
results = []
# a function to convert numeric string to charaters
def f(x):
    return chr(int(x) + 96)

# a recursive function to decode the code given as a string
def decode(code,  result = [], invalid=False):
    if invalid:
        print('Invalid input.')
        return
    if len(code) == 0:
        # result_char = [f(x) for x in result]
        # result_char = list(map(lambda x: chr(int(x) + 96), result))
        result_char=[chr(int(x) + 96) for x in result]
        print(''.join(result_char))
        results.append(''.join(result_char))
        return
    if code[-1] == '0':
        if len(code) > 1 and (code[-2] == '1' or code[-2] == '2'):
            # eat two digits
            decode(code[:-2], [code[-2:]] + result)
        else:
            decode(code, result, invalid=True)
            exit()

    else:
        decode(code[:-1], [code[-1]] + result)
        if len(code) >= 2 and code[-2] != '0' and int(code[-2:]) >=1 and int(code[-2:]) <= 26:
            decode(code[:-2], [code[-2:]] + result)

test = '810231523'
decode(test)
print(results)












