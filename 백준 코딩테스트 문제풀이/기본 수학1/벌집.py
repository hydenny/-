n = int(input())
floor = 0

while n - 1 > 3 * floor * (floor + 1):
    floor += 1

print(floor + 1)