x = int(input())

count = 1

while True:
    if x > count:
        x -= count
        count += 1
    else:
        break
if count % 2 != 0:
    print(str(count - (x - 1)) + "/" + str(x))
else:
    print(str(x) + "/" + str(count - (x - 1)))