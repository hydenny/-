N, M, K = map(int, input().split())

number = list(map(int, input().split()))

number.sort()

first = number[N - 1]
second = number[N - 2]

result = 0
count = 0

for i in range(M):
    if count < K:
        result += first
        count += 1
    else:
        result += second
        count = 0

print(result)
