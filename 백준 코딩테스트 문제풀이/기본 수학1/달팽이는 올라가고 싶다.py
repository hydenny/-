a, b, v = map(int, input().split())

count = 0

v -= a

if v % (a - b) > 0:
    count = 2 + v // (a - b)
else:
    count = 1 + v // (a - b)

print(count)