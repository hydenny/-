import sys

input = sys.stdin.readline

n = int(input())

array = [['*'] * n for i in range(n)]

def hole(n, x, y):
    for i in range(n // 3 + y, 2 * n // 3 + y):
        for j in range(n // 3 + x, 2 * n // 3 + x):
            array[i][j] = ' '
    return

def pattern(n, x, y):
    if n < 3:
        return

    pattern(n // 3, x, y)
    pattern(n // 3, x + n // 3, y)
    pattern(n // 3, x + 2 * n // 3, y)

    pattern(n // 3, x, y + n // 3)
    hole(n, x, y)
    pattern(n // 3, x + 2 * n // 3, y + n // 3)

    pattern(n // 3, x, y + 2 * n // 3)
    pattern(n // 3, x + n // 3, y + 2 * n // 3)
    pattern(n // 3, x + 2 * n // 3, y + 2 * n // 3)

pattern(n, 0, 0)

for i in range(n):
    strArray = "".join(array[i])
    print(strArray)