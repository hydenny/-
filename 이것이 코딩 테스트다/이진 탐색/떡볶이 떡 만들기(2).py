import sys

n, m = map(int, sys.stdin.readline().split())

ddeok = list(map(int, sys.stdin.readline().split()))

result = 0

start = 0
end = max(ddeok)

while start <= end:
    mid = (start + end) // 2

    total = 0

    for i in ddeok:
        if i > mid:
            total += i - mid

    if total > m:
        start = mid + 1

    elif total < m:
        end = mid - 1

    else:
        result = mid
        start = mid + 1

print(result)