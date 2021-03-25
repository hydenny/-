import sys

S = str(sys.stdin.readline().rstrip())

result = 0

for i in S:
    if i == ('0' or '1'):
        result += int(i)
    else:
        if result == 0:
            result += int(i)
        else:
            result *= int(i)

print(result)