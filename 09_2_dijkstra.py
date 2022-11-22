import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline().rstrip())
graph = [[] for i in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        #꺼낸 노드와 최단거리를 가지고 거리 비교
        #만약 꺼낸 dist, 즉 거리가 INF가 아니라면 무시
        if distance[now] < dist:
            continue
        #아니라면, 꺼낸 노드에서 이어지는 다음 노드와 간선값을 더하기
        for i in graph[now]:
            #간선의 합을 더하기
            cost = dist + i[1]
            #만약 새로 더한 간선의 합이 기존의 distance[i]보다 작다면 교체
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF: print("INF")
    else: print(distance[i])