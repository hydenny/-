from itertools import combinations_with_replacement
import sys

Rome = [1, 5, 10, 50]

n = int(sys.stdin.readline().rstrip())

result = set(combinations_with_replacement(Rome, n))

answer = set()
for i in result:
    answer.add(sum(i))

print(len(answer))