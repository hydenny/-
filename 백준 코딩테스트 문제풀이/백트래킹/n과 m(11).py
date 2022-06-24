result = []

def backtrack(depth, answer, m, n, numbers, end):
    if depth == m:
        for i in range(m):
            print(answer[i], end=' ')
        print()
        return
    
    overlap = 0
    for x in range(end, n):
        if overlap != numbers[x]:
            answer.append(numbers[x])
            overlap = numbers[x]
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