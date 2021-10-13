import sys

input = sys.stdin.readline

n = int(input())

student = []

for i in range(n):
    x, y = map(int, input().split())
    student.append([x, y])

for i in student:
    rate = 1
    for j in student:
        if i[0] < j[0]:
            if i[1] < j[1]:
                rate += 1

    print(rate, end=" ")