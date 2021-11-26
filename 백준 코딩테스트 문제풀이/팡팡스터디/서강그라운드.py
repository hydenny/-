def dijkstra(start):
    global dist
    pq = [(0,start)]
    dist[start][start] = 0
    while pq:
        now_cost,now = heapq.heappop(pq)

        for nxt,nxt_cost in adj_list[now]:
            if dist[start][nxt] > now_cost+nxt_cost:
                dist[start][nxt] = now_cost + nxt_cost
                heapq.heappush(pq,(dist[start][nxt],nxt))

def solv():
    for start in range(1,n+1):
        dijkstra(start)

    answer = 0
    for row in dist:
        total = 0
        for idx in range(1,n+1):
            if row[idx] <= m:
                total += items[idx]
        answer = max(answer,total)
    print(answer)

import sys
import heapq
input = sys.stdin.readline
INF = 1e9

n,m,r = map(int, input().split())
items = [0]+list(map(int, input().split()))

adj_list = [[] for _ in range(n+1)]
dist = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(r):
    a,b,l = map(int, input().split())
    adj_list[a].append((b,l))
    adj_list[b].append((a,l))

solv()