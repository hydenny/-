n, k = map(int, input().split())

result = 0

while True:
    # n = ak + b로 시작
    
    target = (n // k) * k
    # target = ak
    
    result += (n - target)
    # result = b
    
    n = target
    # n = ak
    
    if n < k:
        break

    result += 1
    n //= k

result += (n - 1)
print(result)