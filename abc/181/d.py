import itertools

s = input()

c = {}
ans = False
eight = []
eight_c = []
cnt = 0
for i in range(125):
    eight.append(str(cnt))
    cnt += 8

for i in eight:
    temp = {}
    for j in i:
        temp.setdefault(j, 0)
        temp[j] += 1
    eight_c.append(temp)

if len(s) >= 4:
    eight_c = eight_c[13:]
    for i in s:
        c.setdefault(i, 0)
        c[i] += 1
    
    for i in eight_c:
        flag = []
        for j, k in i.items():
            c.setdefault(j, -1)
            if c[j] >= k:
                flag.append(True)
            else:
                flag.append(False)
        if all(flag):
            ans = True
            break

elif len(s) == 3:
    for i in itertools.permutations(s, 3):
        if "".join(map(str, i)) in eight:
            ans = True
            

elif len(s) == 2:
    temp1 = s[0]+s[1]
    temp2 = s[1]+s[0]
    if temp1 in eight or temp2 in eight:
            ans = True

elif len(s) == 1:
    if s in eight:
        ans = True

if ans:
    print('Yes')
else:
    print('No')