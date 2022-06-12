# WA!

h, w, m = map(int, input().split())
bomb = [list(map(int, input().split())) for _ in range(m)]

cnt_x = [0] * h
cnt_y = [0] * w
bomb_cnt = 0

for i in bomb:
    cnt_x[i[0]-1] += 1
    cnt_y[i[1]-1] += 1

max_x = max(cnt_x)
max_y = max(cnt_y)
ans = max_x + max_y
ans_index_x = [i for i, v in enumerate(cnt_x) if v == max_x]
ans_index_y = [i for i, v in enumerate(cnt_y) if v == max_y]

for i in bomb:
    if i[0]-1 in ans_index_x and i[1]-1 in ans_index_y:
        bomb_cnt += 1

if bomb_cnt >= len(ans_index_x) * len(ans_index_y):
    print(ans - 1)
else:
    print(ans)