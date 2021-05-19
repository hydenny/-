n = int(input())

if n == 1:
    print(1)
else:
    r = n - 1
    
    floor = 1

    while r > 6 * floor:
        r -= 6 * floor
        floor += 1


print(floor + 1)