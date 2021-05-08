import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split())

if b == c:
    print(-1)
else:
    n = a // (c - b)

    if n >= 0:
        print(n + 1)
    else:
        print(-1)