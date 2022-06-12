import math

r, x, y = map(int, input().split())

d = math.sqrt(x ** 2 + y ** 2)

if d < r:
    cnt = 2
else:
    cnt = d // r
    if d % r != 0:
        cnt += 1

print(int(cnt))