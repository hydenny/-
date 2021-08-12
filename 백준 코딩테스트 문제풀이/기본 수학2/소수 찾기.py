import sys

n = int(sys.stdin.readline().rstrip())

numbers = list(map(int, sys.stdin.readline().split()))

prime_number = set()

prime_number.add(2)
for i in range(3, 1000):
    count = 0
    for j in range(2, i + 1):
        if i % j == 0:
            count += 1
    if count > 1:
        continue
    prime_number.add(i)

count = 0
for i in numbers:
    if i in prime_number:
        count += 1

print(count)