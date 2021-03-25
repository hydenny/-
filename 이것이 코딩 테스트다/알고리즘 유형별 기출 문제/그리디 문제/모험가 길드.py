import sys

N = int(sys.stdin.readline())

members = list(map(int, sys.stdin.readline().split()))

start = 0
team = members[start]
count = 0

members.sort()

while members:
    start += team
    if start <= N - 1:
        team = members[start]
        count += 1
    else:
        break

print(count)