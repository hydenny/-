pos = str(input())

x = pos[0]
y = int(pos[1])

step = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]

result = 0

for i in step:
    dx = ord(x) + i[0]
    dy = y + i[1]

    if dx < 97 or dx > 104 or dy < 1 or dy > 8:
        continue
    else:
        result += 1

print(result)