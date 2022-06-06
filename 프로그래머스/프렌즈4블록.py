def erase(board):
    to_erase = set()
    for x in range(m-1):
        for y in range(n-1):
            if board[x][y] == board[x+1][y] == board[x][y+1] == board[x+1][y+1]:
                to_erase.add((x, y))
                to_erase.add((x+1, y))
                to_erase.add((x, y+1))
                to_erase.add((x+1, y+1))
    return to_erase

def clean(board):
    x, y = m - 1, n - 1
    while y != -1:
        if x == -1:
            x = m - 1
            y -= 1
        else:
            if board[x][y] == '':
                
            

def solution(m, n, board):
    answer = 0
    while True:
        erase_list = list(erase(board))
        if erase_list == None:
            break
        else:
            for x, y in erase_list:
                board[x][y] = ''
            clean(board)
    print(board)
    return answer

m, n = map(int, input().split())
board = [list(map(str, input())) for _ in range(m)]

solution(m, n, board)