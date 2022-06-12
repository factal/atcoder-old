# WA!

n, m = map(int, input().split())
h = list(map(int, input().split()))
w = list(map(int, input().split()))

h.sort()
w.sort()

d_0 = [] # start at 0
d_1 = [] # start at 1
pointer = 0
ans = []

for i in range(n//2):
    d_0.append(h[2*i+1] - h[2*i])

for i in range(n//2):    
    d_1.append(h[2*(i+1)]-h[2*i+1])
    
sum_0 = 0
sum_1 = sum(d_1)

if n >= 2:
    for i in range(n):
            
        if i % 2 == 0 and i != 0:
            sum_1 -= d_1[i//2-1]
            sum_0 += d_0[i//2-1]
        
        if m-1 < pointer:
            break
        if w[pointer] <= h[i]:
            while w[pointer] <= h[i]:
                if i % 2 == 0:
                    ans.append(sum_0 + h[i] - w[pointer] + sum_1)
                else:
                    ans.append(sum_0 + w[pointer] - h[i-1] + sum_1)
                pointer += 1
                if m-1 < pointer:
                    break 

else:
    ans.append(abs(h[0]-w[0]))

if pointer <= m-1 and h[-1] < w[pointer]:
    ans.append(sum_0 + w[pointer] - h[-1])

print(min(ans))
