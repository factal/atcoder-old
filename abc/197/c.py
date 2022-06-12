import itertools

n = int(input())
a = list(map(int, input().split()))

cnt = []


for i in itertools.product(range(2), repeat=n-1):
    value_temp = []
    sections = []
    pointer = 0
    for j in range(n):
        if j == 0:
            sections.append([a[j]])
        else:
            if i[j-1] == 1:
                sections.append([a[j]])
                pointer += 1
            else: # i.e. i[j-1] == 0
                sections[pointer].append(a[j])
    for splited in sections:
        temp = 0b0
        for j in splited:
            temp = temp | j
        value_temp.append(temp)
    temp = 0b0
    for evaluated in value_temp:
        temp = temp ^ evaluated
    cnt.append(temp)

print(min(cnt))