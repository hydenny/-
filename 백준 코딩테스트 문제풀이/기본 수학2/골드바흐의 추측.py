import sys

array = [True for i in range(10001)]

for i in range(2, 101):
    if array[i] == True:
        j = 2
        while i * j <= 10000:
            array[i * j] = False
            j += 1

t = int(sys.stdin.readline().rstrip())

def find(number):
    i = number // 2
    if array[i] == True:
        return [i, i]
    while True:
        i -= 1
        if array[i]:
            if array[number - i]:
                break
    return [i, number - i]

for i in range(t):
    n = int(sys.stdin.readline().rstrip())

    print(find(n)[0], end=" ")
    print(find(n)[1])