import sys

h, w = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))

height = array[0]

result = 0

for i in range(1, w + 1):
    if array[i] < height:
        result += (height - array[i])
    else:
        