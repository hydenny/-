import sys

t, w = map(int, sys.stdin.readline().split())

array = []
change = []
count = 1

for i in range(t):
    array.append(int(sys.stdin.readline()))

for i in range(1, t):
    number = array[i - 1]
    if array[i - 1] != array[i]:
        change.append((number, count))
        count = 1
    else:
        count += 1
change.append((number, count))

print(change)

if change[0][0] == 1:
    total_change = len(change) - 1
else:
    total_change = len(change)

newChange= []

for i in change:
    newChange.append(i[1])

if w >= total_change:
    print(sum(newChange))