n, m, k = map(int, input().split())
array = list(map(int, input().split()))

first = max(array)
array.remove(first)
second = max(array)

if first == second:
    print(first * m)

else:
    answer = 0
    count = 1

    for num in range(m):
        if count == k:
            answer += second
            count = 1
        else:
            answer += first
            count += 1
    print(answer)