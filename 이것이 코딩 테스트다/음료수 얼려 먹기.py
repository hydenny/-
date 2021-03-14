import sys

N, M = map(int, sys.stdin.readline().split())

box = []
check = []

for i in range(N):
    box[i] = list(map(int, sys.stdin.readline().split()))
    check[i] = [0] * M

print(check)