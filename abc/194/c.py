n = int(input())
a = list(map(int, input().split()))

a_power = [i ** 2 for i in a]

ans = n * sum(a_power) - (sum(a) ** 2)

print(ans)