import bisect

a, b = map(int, input().split())

table_solid = [3, 10, 15]
table_oil = [3, 8]

i = bisect.bisect(table_solid, a + b)
j = bisect.bisect(table_oil, b)

if (i, j) == (3, 2):
    print(1)
elif i >= 2 and j >= 1:
    print(2)
elif i >= 1:
    print(3)
else:
    print(4)