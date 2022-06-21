def backtrack(depth, answer, m, n, end):
    if depth == m:
        for i in range(m):
            print(answer[i], end=' ')
        print()
        return
    
    for x in range(end,n):
        
        answer.append(x+1)
        
        backtrack(depth+1, answer, m, n, x)
        answer.pop()
    return

def solution():
    
    n, m = map(int, input().split())
    answer = []
    end = 0
    backtrack(0, answer, m, n, 0)
    
solution()