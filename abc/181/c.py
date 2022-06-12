import itertools

n = int(input())
x = []
y = []
for i in range(n):
    temp, temp1 = map(int, input().split())
    x.append(temp)
    y.append(temp1)

flag = False

for i in itertools.combinations(range(n), 3):
    if x[i[1]]-x[i[0]] == 0:
        if x[i[0]] == x[i[1]] == x[i[2]]:
            flag = True
            break
    else:
        d = (y[i[1]]-y[i[0]])/(x[i[1]]-x[i[0]])
        if y[i[2]] == d*(x[i[2]]-x[i[0]])+y[i[0]]:
            flag = True
            break

if flag:
    print('Yes')
else:
    print('No')