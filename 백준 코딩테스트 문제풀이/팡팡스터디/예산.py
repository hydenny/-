import sys

input = sys.stdin.readline

n = int(input().rstrip())

regions = list(map(int, input().split()))

budget = int(input().rstrip())

if sum(regions) <= budget:
    print(max(regions))
    exit()

start, end = 0, max(regions)
total = 0

while start <= end:
    result = (start + end) // 2
    
    for i in regions:
        total += min(result, i)
        
    if total > budget:
        end = result - 1
    else:
        start = result + 1

print(result)