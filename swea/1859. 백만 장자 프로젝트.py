T = int(input())
for test_case in range(1, T + 1):
    result = 0
    days = int(input())
    prices = list(map(int, input().split()))
    
    while prices:
        start = 0
        count = 0
        total = 0
        
        pivot = max(prices)
        pi = prices.index(pivot)
        sub_prices = prices[start:pi]
        count = len(sub_prices)
        total = sum(sub_prices)
        result += prices[pi] * count - total
        
        if pi == days - 1:
            break
        else:
            prices = prices[pi + 1:]
    print("#" + str(test_case), result)