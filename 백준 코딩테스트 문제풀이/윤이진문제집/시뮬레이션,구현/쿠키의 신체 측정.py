import sys
dx = [-1, 1, 0, 0]
dy = [0, 0, 1]

def heart(n):
    for i in range(n):
        for j in range(n):
            if array[j][i] == '*':
                heart = array[j][i + dy[2]]
                return [j][i + dy[2]]

def left_arm(n):
    length = 1
    arm = array(heart(n)) + [dx[0]][dy[0]]
    while True:       
        if arm == '*':
            arm += [dx[0]][dy[0]]
            length += 1
        else:
            break
    return length

def right_arm(heart):
    length = 1
    arm = heart(n) + (0, 1)
    while True:       
        if arm == '*':
            arm += (0, 1)
            length += 1
        else:
            break
    return length

def waist(n):
    length = 1
    waist = heart(n) + (1, 0)
    while True:       
        if waist == '*':
            waist += (1, 0)
            length += 1
        else:
            break
    return length

def left_leg(n):
    return
def right_leg(n):
    return

n = int(sys.stdin.readline())

global array
array = [list(map(str, sys.stdin.readline())) for i in range(n)]

print(heart(n), left_arm(n))
#print(str(heart(n)), str(left_arm(n)), str(right_arm(n)), str(waist(n)), end=" ")