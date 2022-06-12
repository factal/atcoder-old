a, b, w = map(int, input().split())

a /= 1000
b /= 1000

ans = []

for i in range(10 ** 6 + 1):
    if a * i <= w <= b * i:
        ans.append(i)

try:
    print(min(ans), max(ans))
except:
    print('UNSATISFIABLE')