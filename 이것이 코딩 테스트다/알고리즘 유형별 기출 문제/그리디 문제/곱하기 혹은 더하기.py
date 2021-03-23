import sys

numbers = list(map(int, sys.stdin.readline().rstrip()))

numbers.sort()

result = 0

for i in numbers:
    if i == 0 or i == 1:
        result += i
    else:
        if result == 0:
            result += i
        else:
            result *= i

print(result)