import sys

while True:
    array = list(map(int, sys.stdin.readline().split()))

    array.sort()

    if array == [0, 0, 0]:
        break
    maximum = array.pop()

    sum = array[0] ** 2 + array[1] ** 2

    if maximum ** 2 == sum:
        print("right")
        continue
    print("wrong")