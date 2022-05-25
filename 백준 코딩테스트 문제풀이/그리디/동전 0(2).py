n, k = map(int, input().split())
coins = []
for i in range(n):
    coin = int(input())
    coins.append(coin)
    
result = 0
    
for i in range(n):
    coin = coins.pop()
    if k // coin == 0:
        continue
    else:
        result += k // coin
        k -= coin * (k // coin)

print(result)