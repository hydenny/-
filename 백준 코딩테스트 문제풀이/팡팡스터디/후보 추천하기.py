import sys

n = int(input())
recommend = int(input())
number = list(map(int, input().split()))

sets = set(number[-(n + 1):])
sets = list(sets)
sets.sort()
for i in range(n):
    print(sets[i], end=" ")