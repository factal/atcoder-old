n = int(input())

satisfy = set()

for dig in range(0, 7): # digit
    for i in range(1 * 10 ** dig, 10 ** (dig + 1)):
        if i * 10 ** (dig+1) + i > n:
            break
        else:
            # print(i, dig)
            satisfy.add(i)

print(len(satisfy))