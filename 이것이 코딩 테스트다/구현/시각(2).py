n = int(input())

hour = 0
result = 0

for i in range(n + 1):
    if hour == (3 or 13 or 23):
        result += 3600

    else:
        result += (900 + 675)

    hour += 1

print(result)