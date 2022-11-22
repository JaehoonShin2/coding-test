import sys
import heapq

n, m = map(int,sys.stdin.readline().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b, 1))

x, k = map(int, sys.stdin.readline().split())

INF = int(1e9)
distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
result1 = distance[k]

distance = [INF] * (n+1)

result2 = 0
if x < k:
    dijkstra(x)
    result2 = distance[k]
else:
    dijkstra(k)
    result2 = distance[x]

print(result1, result2)