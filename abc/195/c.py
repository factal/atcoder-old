from bisect import bisect

n = int(input())

ans = 0

table = [10 ** (i * 3) for i in range(1, 6)]
comma = [999, 999999, 999999999, 999999999999, 999999999999999]

num = bisect(table, n)
for i in range(num):
    ans += n - comma[i]

print(ans)