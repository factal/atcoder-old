n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

for i in a:
    cnt += (i[1]**2+i[1])//2 - (i[0]**2-i[0])//2

print(cnt)