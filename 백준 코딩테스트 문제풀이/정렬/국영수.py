import sys

input = sys.stdin.readline

n = int(input())

array = []

for i in range(n):
    array.append(input().split())

array.sort(key=lambda array: (-int(array[1]), int(array[2]), -int(array[3]), array[0]))

for i in array:
    print(i[0])