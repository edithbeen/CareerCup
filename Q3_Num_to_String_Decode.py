# set a = 1, b = 2, ..., z = 26
# given a number, find all possible string it represents
# eg: input 1123, the output should be aabc, kbc, alc, ...
# ask how long is the code?
# does this code contains 0?
# a list to store all the results
results = []
def f(x):
    return chr(int(x) + 96)
def decode(code,  result = []):
    # recursively eat one or two digit of the code
    if len(code) == 0:
        # result_char = [f(x) for x in result]
        result_char = list(map(lambda x: chr(int(x) + 96), result))
        print(''.join(result_char))
        results.append(result)
        return
    if code[-1] == '0':
        if len(code) > 1 and (code[-2] == '1' or code[-2] == '2'):
            # eat two digits
            decode(code[:-2], [code[-2:]] + result)
        else:
            print('Invalid input')
            exit()

    else:
        decode(code[:-1], [code[-1]] + result)
        if len(code) >= 2 and code[-2] != '0' and int(code[-2:]) >=1 and int(code[-2:]) <= 26:
            decode(code[:-2], [code[-2:]] + result)


test = '20231523'
decode(test)












