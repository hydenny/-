import sys


def solution(n, k):
    answer = 0
    print(bin(n))
    while bin(n).count('1') > k:
        plus = 2 ** (bin(n)[::-1].index('1'))
        answer += plus
        n += plus
    print(answer)


n, k = map(int, input().split())

solution(n, k)