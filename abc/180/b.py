import math

n = int(input())
x = map(int, input().split())

temp = list(map(abs, x))

m = sum(temp)
e = 0
for i in temp:
    e += i ** 2
c = max(temp)
print(m)
print(math.sqrt(e))
print(c)