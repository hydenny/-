def solution(A):
    # write your code in Python 3.6
    even = 0
    odd = 0

    for i in A:
        if i % 2 == 0:
            even = max(even, i)
        else:
            odd = max(odd, i)

    return even + odd

A = list(map(int, input().split()))

print(solution(A))