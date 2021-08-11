import sys

t = int(sys.stdin.readline().rstrip())

def getcount(x, y):
    dist = y - x
    
    count = 0
    number = 1
    sum = 0
    while True:
        if dist >= 2 * (sum + number):
            number += 1
            sum += number
            count += 1
        else:
            sum -= number
            number -= 1
            break

    spare = (dist - (2 * sum - number)) // (number - 1)
    result = count * 2 + spare
    return result

for i in range(t):
    x, y = map(int, sys.stdin.readline().split())
    print(getcount(x, y))
