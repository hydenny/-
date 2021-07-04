n = int(input())

plan = list(map(str, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x = 1
y = 1

for word in plan:
    px = x
    py = y
    
    if word == 'L':
        px = px + dx[0]
        py = py + dy[0]

    elif word == 'R':
        px = px + dx[1]
        py = py + dy[1]

    elif word == 'U':
        px = px + dx[2]
        py = py + dy[2]

    else:
        px = px + dx[3]
        py = py + dy[3]    

    if px < 1 or px > n or py < 1 or py > n:
        continue
    else:
        x = px
        y = py

print(y, x, end=' ')