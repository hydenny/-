N, K = map(int, input().split())

if N == K:
    print(1)

else:
    count = 0
    while N >= K:
        N = N//K
        count += 1

    while N > 1:
        N -= 1
        count += 1

    print(count)