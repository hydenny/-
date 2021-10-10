def divide_sum(n):
    result = n

    while n:
        result += n % 10
        n //= 10

    return result

n = int(input())

for i in range(n // 2, n):
    if divide_sum(i) == n:
        print(i)
        exit()
print(0)