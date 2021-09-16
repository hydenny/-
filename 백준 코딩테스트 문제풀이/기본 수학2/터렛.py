import sys

def get_number(x_1, y_1, r_1, x_2, y_2, r_2):
    dist = ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5

    if dist == 0:
        if r_1 == r_2:
            return -1
        return 0
    
    if dist == r_1 + r_2 or dist == abs(r_1 - r_2):
        return 1
    
    if dist < r_1 + r_2 and dist > abs(r_1 - r_2):
        return 2
    return 0

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, sys.stdin.readline().split())

    print(get_number(x_1, y_1, r_1, x_2, y_2, r_2))