def index_Multi(List,liter):
    #Listはリスト本体・literは検索したい文字
    index_L = []
    for val in range(0,len(List)):
        if liter == List[val]:
            index_L.append(val)
    return index_L

n = int(input())
a = list(map(int, input().split()))

sum = [0]
temp = 0
ans = []

for i in a:
    temp += i
    sum.append(temp)

sum_move = []
temp = 0

for i in sum:
    temp += i
    sum_move.append(temp)

sum_move.pop()

m = max(sum_move)
ix = index_Multi(sum_move, m)
temp = max(ix)+2
print(max(sum[:temp]) + m)