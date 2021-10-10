from itertools import permutations
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

cards = list(map(int, input().rstrip().split()))

max = 0

for i in permutations(cards, 3):
    if max < sum(i) and sum(i) <= m:
        max = sum(i)

print(max)