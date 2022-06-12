n, c = map(int, input().split())
events = []
for i in range(n):
    a, b, cost = map(int, input().split())
    a -= 1
    events.append((a, cost))
    events.append((b, -cost))
events.sort()

ans = 0
current = 0
pointer = 0

for x, cost in events:
    if x != pointer:
        ans += min(c, current) * (x - pointer)
        pointer = x
    current += cost

print(ans)