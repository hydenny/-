def backtrack(depth, answer, m, n):
    if depth == m:
        for i in range(m):
            print(answer[i], end=' ')
        print()
        return
    
    for x in range(n):
        # if visited[x]:
            # continue
        # visited[x] = True
        answer.append(x+1)
        backtrack(depth+1, answer, m, n)
        # visited[x] = False
        answer.pop()
    return

def solution():
    
    n, m = map(int, input().split())
    # visited = [False] * n
    answer = []
    backtrack(0, answer, m, n)
    
solution()