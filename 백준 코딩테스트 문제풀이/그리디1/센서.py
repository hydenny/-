#N, K = map(int, input().split('\n'))
N = int(input())
K = int(input())

pos = list(map(int, input().split()))

pos.sort()
interval = []
interval_length = []
print(pos)
for i in range(1, len(pos) - 2):
    interval.append([pos[i], pos[i + 1]])
    #좌표 순으로 정렬한 리스트에서 각 구간 좌표(처음과 끝 구간은 일부러 배제함)
print(interval)
interval_length = sorted(interval, key=lambda x: -(x[1] - x[0]))
#구간별 길이 내림차순으로 정렬
print(interval_length)
count = 0

max_length = []

for i in range(len(interval_length) - 1):
    if count == K - 1:
        break
    else:
        if interval_length[i][1] == interval_length[i+1][0] or interval_length[i][0] == interval_length[i+1][1]:
                max_length.append(interval_length[i])
        else:
            max_length.append(interval_length[i])
            count += 1
print(max_length)

total = 0

for i in range(len(pos) - 2):
    total = total + pos[i + 1] - pos[i]
print(total)
exclude = 0

for i in range(len(max_length)):
    exclude = exclude + max_length[i][1] - max_length[i][0]
print(exclude)
print(total - exclude)
