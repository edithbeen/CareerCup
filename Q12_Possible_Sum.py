# given a k side coin, print the the possible sums up to 1000

coin = [10, 25, 50]

s = 1000

result = []

def print_sums(coin, limit, current_s=0):
    if current_s > limit:
        return
    if current_s not in result:
        print(current_s)
        result.append(current_s)
        for value in coin:
            print_sums(coin, limit, current_s+value)

print_sums(coin, 100)
print('Break')


# now let's change the problem a little bit
# say, we have a bag of coins, each of which has one value and can only be used once

def print_sums(coin, limit, current_s=0):
    if current_s > limit:
        return
    if current_s not in result:
        print(current_s)
        result.append(current_s)
    if len(coin) > 0:
        for i in range(len(coin)):
            print_sums(coin[:i] + coin[i+1:], limit, coin[i] + current_s)

result = []
coin = [5, 10, 25, 25, 10, 50]
print_sums(coin, 200)