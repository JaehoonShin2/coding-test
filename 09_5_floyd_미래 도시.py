import sys

n, m = map(int, sys.stdin.readline().split())

INF = int(1e9)
graph = [[INF] * (n+1) for i in range(n+1) ]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b: graph[a][b] = 0

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, sys.stdin.readline().split())

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

distance = graph[1][k] + graph[k][x]

if distance >= INF: print(-1)
else: print(distance)
