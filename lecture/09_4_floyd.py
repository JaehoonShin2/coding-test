import sys

#노드의 갯수
n = int(sys.stdin.readline().rstrip())
#간선의 갯수
m = int(sys.stdin.readline().rstrip())

INF = int(1e9)
#dp와 마찬가지
graph = [[INF] * (n+1) for i in range(n + 1)]

# 1,1과 같이 자기자신으로 이동하는 값에 대해서는 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b: graph[a][b] = 0

#a번 노드에서 b번 노드로 이동하는데 드는 간선크기(비용)을 c로 초기화
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[i][j] = min( graph[i][j], graph[i][k] + graph[k][j])
#점화식 dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF: print("INFINITY", end=' ')
        else: print(graph[a][b], end=' ')
    print("")




