import sys

input = sys.stdin.readline

n = int(input().rstrip())

regions = list(map(int, input().split()))

budget = int(input().rstrip())

if sum(regions) <= budget:
    print(max(regions))

if budget % n == 0:
    pivot = budget // n
else:
    pivot = budget // n + 1
    
for i in regions:
    if i <= pivot:
        