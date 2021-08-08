import sys

input = sys.stdin.readline

n = int(input())

array = []

for i in range(n):
    array.append(list(map(int, input().split())))

array.sort(key=lambda x: (x[1], x[2]))
count = 0

while array:
    x = array.pop(0)
    for y in array:
        if x[2] <= y[1]:
            x = y
            array.remove(y)
        else:
            continue
    count += 1

print(count)