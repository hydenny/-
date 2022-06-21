def backtrack(depth, answer, m, n, numbers, end):
    if depth == m:
        for i in range(m):
            print(answer[i], end=' ')
        print()
        return
    
    for x in range(end, n):
        answer.append(numbers[x])
        backtrack(depth+1, answer, m, n, numbers, x)
        answer.pop()
    return

def solution():
    
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()
    answer = []
    backtrack(0, answer, m, n, numbers, 0)
    
solution()