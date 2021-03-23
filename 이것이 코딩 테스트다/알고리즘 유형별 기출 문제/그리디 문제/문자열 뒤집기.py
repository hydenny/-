import sys

string = list(map(int, sys.stdin.readline().rstrip()))

order = [string[0]]

index = 0

for i in range(len(string)):
    if string[i] != order[index]:
        order.append(string[i])
        index += 1

if order.count(1) >= order.count(0):
    print(order.count(0))
else:
    print(order.count(1))