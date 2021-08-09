import sys

n = int(sys.stdin.readline().rstrip())

array = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().rstrip())

tofind = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    if tofind[i] in array:
        print("yes", end=" ")
    else:
        print("no", end=" ")