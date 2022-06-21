def backtrack(depth, answer, m, n, numbers):
    if depth == m:
        for i in range(m):
            print(answer[i], end=' ')
        print()
        return
    
    for x in range(n):
        answer.append(numbers[x])
        backtrack(depth+1, answer, m, n, numbers)
        answer.pop()
    return

def solution():
    
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()
    answer = []
    backtrack(0, answer, m, n, numbers)
    
solution()