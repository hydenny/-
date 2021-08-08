def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

import sys

input = sys.stdin.readline

n = int(input())

array = list(map(int, input().rstrip().split()))

m = int(input())

tofind = list(map(int, input().rstrip().split()))

array.sort()

result = []

for i in range(m):
    if binary_search(array, 0, n - 1, tofind[i]) == None:
        result.append("no")
    else:
        result.append("yes")

for i in range(m):
    print(result[i], end=" ")