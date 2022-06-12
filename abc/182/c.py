n = input()
k = len(n)

pattern = []

for i in range(2 ** k):
    tmp = [False] * k
    for j in range(k):
        if i >> j & 1:
            tmp[j] = True
    pattern.append(tmp)

pattern.pop(0)

sum = []
cnt = []
ans = []

for i in pattern:
    temp = 0
    for j in range(k):
        if i[j]:
            temp += int(n[j])
    sum.append(temp)
    cnt.append(i.count(True))

for i in range(len(sum)):
    if sum[i] % 3 == 0:
        ans.append(cnt[i])

if len(ans) == 0:
    print(-1)
else:
    print(k - max(ans))