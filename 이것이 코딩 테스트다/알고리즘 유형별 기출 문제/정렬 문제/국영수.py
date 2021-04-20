import sys

N = int(sys.stdin.readline().rstrip())

array = []

for i in range(N):
    name, korean, english, math = map(str, sys.stdin.readline().rstrip().split())
    array.append([name, korean, english, math])

array.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in array:
    print(i[0])