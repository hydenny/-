import sys
input = sys.stdin.readline
INF = int(1e9)  #무한을 의미하는 값으로 10억을 설정

#노드 개수, 간선 개수
n, m = map(int, input().split())
#시작 노드 번호 입력
start = int(input())
#각 노드에 연결되어 있는 노드 정보 담는 리스트 생성
graph = [[] for i in range(n + 1)]
#방문한 적 있는지 체크하는 리스트 생성
visited = [False] * (n + 1)
#최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (n + 1)

#모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

#방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    #시작 노드 0으로 초기화(시작노드에서 자신으로 가는 경우는 거리 0으로 함)
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    #시작 노드 제외 전체 n - 1개 노드에 대해 반복
    for i in range(n - 1):
        #현재 최단 거리 가장 짧은 노드 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        #현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            #현재 노드 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

#모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    #도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    #도달할 수 있는 경우 거리 출력
    else:
        print(distance[i])