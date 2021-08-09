import sys

n = int(sys.stdin.readline().rstrip())

three, five = 0, 0

while n:
    if n % 3 == 0:
        n -= 3
        three += 1

    elif n % 5 == 0:
        n -= 5
        five += 1

    else:
        break

if n != 0:
    print(-1)

else:
    if three >= 5:
        five += 3 * three // 5
        three = three % 5

    print(three + five)