import sys

input = sys.stdin.readline

n = int(input())

array = [['*'] * n for i in range(n)]

def hole(n):
    for i in range(n):
        for j in range(n):
            if n // 3 <= i < 2 * n // 3 and n // 3 <= j < 2 * n // 3:
                array[i][j] = ' '
            else:
                part = hole(n // 3)
                
                
    return array

hole(n)
    

for i in range(n):
    strArray = "".join(array[i])
    print(strArray)