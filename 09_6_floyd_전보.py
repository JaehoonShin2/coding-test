import sys

n, m, c = map(int, sys.stdin.readline().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n+1)]
cnt = 0
max = 0

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b: graph[a][b] = 0

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x][y] = z

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in graph[1]:
    if i != INF and i != 0:
        cnt = cnt + 1
        if max < i:
            max = i

print(cnt, max)