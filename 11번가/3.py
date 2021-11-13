# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    numbers = set(A)
    
    count = 0

    for i in numbers:
        cal_count = min(A.count(i), abs(A.count(i) - i))
        count += cal_count
    return count