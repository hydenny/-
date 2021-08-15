import sys

m, n = map(int, sys.stdin.readline().split())

for i in range(m, n + 1):
    if i == 1:
        continue
    flag = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i)