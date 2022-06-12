n = int(input())

# can be expressed: p_1^k p_2^k ... p_m^k (k >= 2)

unexpressed = set()

for i in range(2, int(n ** 0.5) + 1): # 2 <= i <= n
    for j in range(2, 34): # 2<= j <= n
        if i ** j > n:
            break
        unexpressed.add(i ** j)
        
print(n - len(unexpressed))