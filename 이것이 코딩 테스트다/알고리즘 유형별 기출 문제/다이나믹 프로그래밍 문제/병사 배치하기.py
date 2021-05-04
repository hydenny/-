import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    array = list(map(int, sys.stdin.readline().rstrip().split()))

check = [0] * len(array)

for i in range(len(array) - 1):
    if array[i + 1] >= array[i]:
        check[i + 1] = 1

if array.count(1) > array.count(0):
    print(array.count(0))
else:
    print(array.count(1))