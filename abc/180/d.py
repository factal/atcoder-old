import math
 
x, y , a, b = map(int, input().split())
cnt = 0
 
n = math.floor(math.log((x + b)/x) / math.log(a))
k = math.floor(math.log(y/x) / math.log(a))
N = min(n, k)
cnt += N
x = x * (a ** n)
m = (y - 1 - x) // b
cnt += m
x += m * b
print(max(0, cnt))
