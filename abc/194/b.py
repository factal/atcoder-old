import itertools

n = int(input())
a, b, c = [], [], []
for i in range(n):
    temp_a , temp_b = map(int, input().split())
    a.append(temp_a)
    b.append(temp_b)
    c.append(temp_a + temp_b)

cost = []

for i in itertools.product(range(n), repeat=2):
    if i[0] == i[1]:
        cost.append(a[i[0]] + b[i[1]])
    else:
        cost.append(max(a[i[0]], b[i[1]]))

print(min(cost))