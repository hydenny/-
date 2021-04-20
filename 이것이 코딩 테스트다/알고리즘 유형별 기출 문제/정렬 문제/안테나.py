import sys

N = int(sys.stdin.readline().rstrip())

array = list(map(int, sys.stdin.readline().rstrip().split()))

array.sort()

print(array[N//2 - 1])