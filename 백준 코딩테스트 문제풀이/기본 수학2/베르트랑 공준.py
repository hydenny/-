import sys

while True:
    n = int(sys.stdin.readline())
    array = [True for i in range(n + 1, 2 * n + 1)]

    for i in range(2, int((2 * n) ** 0.5) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    print(array.count(True))