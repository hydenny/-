#N, K = map(int, input().split('\n'))
N = int(input())
K = int(input())

if K >= N:
    print(0)
    #집중국 수가 센서 수 이상일 경우

else:
    pos = list(map(int, input().split()))

    pos.sort()
    interval = []
    interval_length = []
    #print(pos)

    for i in range(len(pos) - 1):
        interval.append([pos[i], pos[i + 1]])
        #좌표 순으로 정렬한 리스트에서 각 구간 좌표(처음과 끝 구간은 일부러 배제함)

        interval_length.append(pos[i + 1] - pos[i])
        #처음과 끝 구간을 제외한 구간별 길이
        #interval과 interval_length의 index관계 활용
        #interval[n] 구간의 길이는 interval_length[n]

    #print(interval)
    interval_length.sort()
    interval_length.reverse()

    total = 0
    excluding = 0

    for i in range(len(pos) - 1):
        total += pos[i + 1] - pos[i]

    for i in range(K - 1):
        excluding += (interval_length[i])

    print(total - excluding)