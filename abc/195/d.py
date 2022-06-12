# WA!

from bisect import bisect_left

n, m, q = map(int, input().split())
goods = [list(map(int, input().split())) for _ in range(n)]
boxes = list(map(int, input().split()))
query = [list(map(int, input().split())) for _ in range(q)]

goods.sort(key=lambda i: i[1], reverse=True) # sorting on value
ans = []

for l, r in query:
    cnt = 0
    
    x = boxes[:l - 1] + boxes[r:]
    x.sort()

    for weight, value in goods:
        index = bisect_left(x, weight)
        if index < len(x):
            x.pop(index)
            cnt += value
        else:
            break
    ans.append(cnt)

for i in ans:
    print(i)