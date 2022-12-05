import sys


sys.stdin = open('C:/Users/R/Desktop/python_input/bj_24479.txt')


n, m, start = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

    graph[a].sort()

    path = [0] * (n+1)
    result = []

def dfs(graph, v, visited):
    visited[v] = True
    result.append(v)

    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)
    return

dfs(graph, 1, visited)

for idx, node in zip(range(1, len(result)+1), result):
    path[node] = idx
    
print(*path[1:], sep="\n")
