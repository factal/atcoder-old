n, m = map(int, input().split())

section = []
d = 1
pointer = 1

if m > 0 and m <= n - 2:
    section.append([1, 10 ** 8])
    pointer = 2
    for i in range(m + 1):
        section.append([pointer, pointer + d])
        pointer += d + 1
    
    pointer = 10 ** 8 + 1

    for i in range(n - m - 2):
        section.append([pointer, pointer + d])
        pointer += d + 1

    for i in section:
        print(i[0], i[1])

elif m == 0:
    pointer = 1
    for i in range(n):
        section.append([pointer, pointer + d])
        pointer += d + 1
    
    for i in section:
        print(i[0], i[1])

else:
    print(-1)