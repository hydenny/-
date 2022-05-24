n, m = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]

element = 0
for i in range(n):
    if element == 0:
        element = min(board[i])
    else:
        element = max(element, min(board[i]))

print(element)