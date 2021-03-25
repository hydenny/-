import sys

N = int(sys.stdin.readline())

fear = list(map(int, sys.stdin.readline().split()))

most = N - 1
spare = N
count = 0

fear.sort()

while spare:
    spare -= fear[most]
    most -= fear[most]
    count += 1

print(count)
#fail
