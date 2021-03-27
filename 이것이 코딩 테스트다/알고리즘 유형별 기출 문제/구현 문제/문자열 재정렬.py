import sys

string = list(map(str, sys.stdin.readline().rstrip()))

sum = 0

string.sort()

for i in string:
    if ord(i) >= 65:
        result = string[string.index(i):]
        numbers = string[:string.index(i)]
        break

for i in numbers:
    sum += int(i)

print(''.join(result) + str(sum))