n = int(input())
c = list(input())

r = 0
temp = 0

for i in c:
    if i == 'R':
        r += 1
    
w = n - r

for i in range(r):
    if c[i] == 'R':
        temp += 1

print(r - temp)