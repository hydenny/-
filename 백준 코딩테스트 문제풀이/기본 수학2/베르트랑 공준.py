import sys
MAX = 123456
array = [True] * (MAX * 2 + 1)

for i in range(2, int((2 * MAX) ** 0.5) + 1):
    if array[i] == True:
        for j in range(2 * i, 2 * MAX + 1, i):
            array[j] = False

while True:
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
       break
    
    result_array = array[n + 1: 2 * n + 1]
    print(result_array.count(True))