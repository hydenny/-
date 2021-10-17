n = int(input())

count = 0
number = "666"

while True:
    if "666" not in number:
        number = str(int(number) + 1)
    else:
        count += 1
        if count == n:
            break
        else:
            number = str(int(number) + 1)

print(number)