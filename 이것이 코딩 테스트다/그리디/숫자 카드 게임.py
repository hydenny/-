N, M = map(int, input().split())

#grid = [list(map(int, input())) for _ in range(N)]

grid = [[0] * M for x in range(N)]
#위의 주석 식을 활용해 아래 for문과 어울러 더 간단하게 코드를 구현할 수 있음.
#행렬 생성하기 위한 기본 공식처럼 알고 있으면 좋을 듯함.

for i in range(N):
    grid[i] = list(map(int, input().split()))

minimum = []

for i in range(len(grid)):
    minimum.append(min(grid[i]))

print(max(minimum))