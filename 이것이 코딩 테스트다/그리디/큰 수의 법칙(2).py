n, m, k = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

first = numbers[n - 1]
second = numbers[n - 2]

quotient = m // (k + 1)
remainder = m % (k + 1)

result = 0
result = quotient * (k * first + second) + remainder * first

print(result)