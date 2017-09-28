# Excel usually have column name A, B, ..., AA, AB, ...
# convert them to numbers and vice versa
from math import pow

# first, let's write 2 simple functions to convert single letter to number and vice versa
def letter_to_number(letter):
    if len(letter) != 1:
        print('Invalid Letter Input')
    return ord(letter) - 64

def number_to_letter(number):
    if number not in range(1, 27):
        print('Invalid Number Input')
    return chr(number + 64)

# now, the recursive function to convert letter to number
def to_num(letters, current_num=0, current_position=0):
    if len(letters) == 0:
        print(current_num)
        return current_num
    temp_num = letter_to_number(letters[-1])
    to_num(letters[:-1], int(pow(26, current_position))*temp_num + current_num, current_position+1)

print(to_num('AA'))

