h, w, x, y = map(int, input().split())
s = []
for i in range(h):
    s.append(input())

x -= 1
y -= 1

cnt = 1

def seeker(dire_x, dire_y):
    global cnt
    dist = 1

    while True:
        try:
           
            
            if x + dist * dire_x >= 0 and y + dist * dire_y >= 0 and s[x + dist * dire_x][y + dist * dire_y] == '.':
                cnt += 1
                dist += 1
            else:
                return
        except:
            return


seeker(1, 0)
seeker(-1, 0)
seeker(0, 1)
seeker(0, -1)
            
print(cnt)