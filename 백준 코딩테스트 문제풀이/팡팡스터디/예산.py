import sys

input = sys.stdin.readline

n = int(input().rstrip())

regions = list(map(int, input().split()))

budget = int(input().rstrip())

if sum(regions) <= budget:
    print(max(regions))
    exit()

pivot = budget // n

remainder = []

for i in regions:
    if i <= pivot:
        budget -= i
    else:
        remainder.append(i)
if remainder:
    print(budget // len(remainder))
else:
    print(pivot)