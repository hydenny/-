import sys


def check_zero(x, y):
    #상,하,좌,우,왼아래,왼위,오른아래,오른위
    dx = [0, 0, -1, 1, -1, -1, 1, 1]
    dy = [-1, 1, 0, 0, 1, -1, 1, -1]
    
    if board[y][x] == '0':
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx < n - 1 and 0 < ny < n - 1:
                flag_board[ny][nx] = False
                

def solution(n):
    if n <= 2:
        print(0)
        return
    for y in range(n):
        for x in range(n):
            if y == 0 or y == n - 1 or x == 0 or x == n - 1:
                check_zero(x, y)
    zeros = 0
    for i in range(n):
        zeros += flag_board[i].count(False)
    for i in range(n):
        print(flag_board[i])    
    print((n - 2) ** 2 - zeros)


n = int(input())
board = []
for _ in range(n):
    board.append(list(map(str, input().rstrip())))
  
flag_board = [[True] * n for _ in range(n)]

solution(n)