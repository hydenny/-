import sys

t = int(sys.stdin.readline().rstrip())

dp = [[0] * 15 for i in range(15)]

def living_number(k, n):
    if dp[k][n] == 0:
        if k == 0:
            dp[k][n] = n
            return n
        
        else:
            sum = 0
            for i in range(1, n + 1):
                sum += living_number(k - 1, i)
            dp[k][n] = sum
            return sum

    else:
        return dp[k][n]

for i in range(t):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    print(living_number(k, n))