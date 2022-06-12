n, k = map(int, input().split())

cnt = list(range(max(2, k + 2), min(2 * n, k + 2 * n) + 1))
ans = 0

for i in cnt:
    #a+b
    if i-1 <= n:
        ab=i-1
    else:
        ab=i-1-2*(i-1-n)
    
    #c+d
    if i-1-k <= n:
        cd=i-1-k
    else:
        cd=i-1-k-2 * (i-1-k-n)
    
    ans += ab * cd

print(ans)