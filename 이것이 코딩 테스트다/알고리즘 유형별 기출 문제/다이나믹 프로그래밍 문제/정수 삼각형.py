import sys

n = int(sys.stdin.readline().rstrip())

sum = 0

for i in range(n):
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    if i == 0:
        num = array[0]
        index = 0
    else:
        num = max(array[index:index + 2])
        index = array.index(num)
    sum += num

print(sum)
