import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline().rstrip())
graph = [[] for i in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

def dijkstra(start):
    q= []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) #0, 1
        if distance[now] < dist: #이미 한 번 거리가 측정된 노드라면
            continue
        for i in graph[now]: #i[0] = 최단거리 i[1] = 연결된 노드
            # now노드 기준으로 다음 노드까지의 최단거리 합 계산
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

