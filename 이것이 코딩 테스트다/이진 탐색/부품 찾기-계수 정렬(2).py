import sys

input = sys.stdin.readline

n = int(input().rstrip())

check_list = [0] * 1000000

array = list(map(int, input().split()))

for i in range(n):
    check_list[array[i]] = 1

m = int(input().rstrip())

tofind = list(map(int, input().split()))

for i in tofind:
    if check_list[i] == 1:
        print('yes', end=" ")

    else:
        print('no', end=" ")