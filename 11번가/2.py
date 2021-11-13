# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    pivot = 0

    S = list(S)

    lengths = []
    length = 1

    while S:
        if len(S) >= 2:
            if S[-1] == S[-2]:
                length += 1
            else:
                lengths.append(length)
                length = 1
        else:
            lengths.append(length)
        S.pop()

    result = []
    for i in lengths:
        result.append(max(lengths) - i)
    return sum(result)