import sys

n = int(sys.stdin.readline().rstrip())

three, five = 0, 0

if n == 4 or n == 7:
    print(-1)
    quit()

while n % 5:
    n -= 3
    three += 1

five = n // 5

if three % 5 == 0:
    five += three // 5
    three -= three // 5 * 3

print(three + five)