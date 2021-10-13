import sys

input = sys.stdin.readline

n, m = map(int, input().split())

BW = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
WB = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']

black_first = [BW, WB, BW, WB, BW, WB, BW, WB]
white_first = [WB, BW, WB, BW, WB, BW, WB, BW]

Min = int(1e9)

array = [list(map(str, input().rstrip())) for i in range(n)]

new_array = [[''] * 8 for i in range(8)]

for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        for a in range(8):
            for b in range(8):
                new_array[a][b] = array[a + i][b + j]
                
        b_count = 0
        w_count = 0

        for j in range(8):
            for k in range(8):
                if new_array[j][k] != black_first[j][k]:
                    b_count += 1
                if new_array[j][k] != white_first[j][k]:
                    w_count += 1

        Min = min(b_count, Min)
        Min = min(w_count, Min)

print(Min)