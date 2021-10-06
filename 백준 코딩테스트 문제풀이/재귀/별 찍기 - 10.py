import sys

input = sys.stdin.readline

n = int(input())

array = [['*'] * n for i in range(n)]

def pattern(n):
    for i in range(n // 3):
        for j in range(n // 3):
            pattern(n // 3)
    for i in range(n // 3):
        for j in range(n // 3,2 * n // 3):
            pattern(n // 3)
    for i in range(n // 3):
        for j in range(2 * n // 3, n):
            pattern(n // 3)

    for i in range(n // 3, 2 * n // 3):
        for j in range(n // 3):
            pattern(n // 3)
    for i in range(n // 3, 2 * n // 3):
        for j in range(n // 3, 2 * n // 3):
            array[i][j] = ' '
    for i in range(n // 3, 2 * n // 3):
        for j in range(2 * n // 3, n):
            pattern(n // 3)

    for i in range(2 * n // 3, n):
        for j in range(n // 3):
            pattern(n // 3)
    for i in range(2 * n // 3, n):
        for j in range(n // 3,2 * n // 3):
            pattern(n // 3)
    for i in range(2 * n // 3, n):
        for j in range(2 * n // 3, n):
            pattern(n // 3)

    return array
pattern(n)

for i in range(n):
    strArray = "".join(array[i])
    print(strArray)