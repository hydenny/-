import sys

N, M = map(int, sys.stdin.readline().split())

box = []

for i in range(N):
    box.append(list(map(int, sys.stdin.readline().rstrip())))

#DFS로 특정 노드 방문 후 연결된 모든 노드 방문
def dfs(x, y):
    #주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    #현재 노드를 아직 방문하지 않은 경우
    if box[x][y] == 0:
        #해당 노드 방문 처리
        box[x][y] = 1
        #상, 하, 좌, 우 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

#모든 노드(위치)에 대해 음료수 채우기
result = 0
for i in range(N):
    for j in range(M):

        if dfs(i, j) == True:
            result += 1

print(result)