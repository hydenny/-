import sys

count = 1

while True:
    l, p, v = map(int, sys.stdin.readline().split())

    if l == 0 and p == 0 and v == 0:
        break
    quotient = v // p
    remainder = v % p

    if remainder < l:
        result = l * quotient + remainder
    else:
        result = l * quotient + l

    print("Case " + str(count) + ": " + str(result))
    count += 1