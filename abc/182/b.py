n = int(input())
a = list(map(int, input().split()))

cnt = [0] * 1001
number = [0] * 1001

for i in range(2, 1001):
    for j in a:
        if j % i == 0:
            cnt[i] += 1

print(cnt.index(max(cnt)))