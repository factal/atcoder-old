n = int(input())
a = 0
b = 0
for i in range(1, 39):
    for j in range(1, 27):
        if (3 ** i) + (5 ** j) == n:
            a = i
            b = j
            break
if a != 0 and b != 0:
    print(a, b)
else:
    print(-1)

