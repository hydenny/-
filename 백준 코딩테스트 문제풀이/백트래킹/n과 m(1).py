# def backtrack(depth, visited, answer):
#     if depth == max_depth:
#         print(answer)
#         return
    
#     for x in range(len(array)):
#         if visited[x]:
#             continue
#         visited[x] = True
#         answer.append(x+1)
#         backtrack(depth + 1, visited, answer)
#         visited[x] = False
#         answer.pop(x+1)
#     return 

def backtrack(depth, visited, answer, m, n):
    if depth == m:
        for i in range(m):
            print(answer[i], end=' ')
        print()
        return
    
    for x in range(n):
        if visited[x]:
            continue
        visited[x] = True
        answer.append(x+1)
        backtrack(depth+1, visited, answer, m, n)
        visited[x] = False
        answer.pop()
    return

def solution():
    
    n, m = map(int, input().split())
    visited = [False] * n
    answer = []
    backtrack(0, visited, answer, m, n)
    
solution()