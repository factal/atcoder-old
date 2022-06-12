from collections import deque

n , m = map(int, input().split())
a = list(map(int, input().split()))

zero_exist = []

a_m = a[:m]

temp_nums = set(a_m)
q_nums = dict(zip([i for i in range(n)], [0] * n))
for i in a_m:
    q_nums[i] += 1
for i in q_nums.items():
    if i[1] == 0:
        zero_exist.append(i[0])


q = deque(a_m, maxlen=m) # init


for i in a[m:]:
    q_nums[q[0]] -= 1
    q_nums[i] += 1
    if q_nums[q[0]] == 0:
        zero_exist.append(q[0])

    q.append(i)
    if q_nums[i] == 0:
        zero_exist.append(i)
    
#print(zero_exist)
    
try:
    print(min(zero_exist))
except:
    if min(a) - 1 >= 0:
        print(min(a)-1)
    else:
        print(max(a)+1)