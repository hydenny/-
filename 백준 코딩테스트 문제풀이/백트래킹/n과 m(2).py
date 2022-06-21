def backtrack(depth, visited, answer, m, n, end):
    if depth == m:
        for i in range(m):
            print(answer[i], end=' ')
        print()
        return
    
    for x in range(end,n):
        if visited[x]:
            continue
        visited[x] = True
        # if end > x+1:
        #     continue
        answer.append(x+1)
         
        backtrack(depth+1, visited, answer, m, n, x+1)
        #print(end)
        visited[x] = False
        answer.pop()
    return

def solution():
    
    n, m = map(int, input().split())
    visited = [False] * n
    answer = []
    end = 0
    backtrack(0, visited, answer, m, n, 0)
    
solution()