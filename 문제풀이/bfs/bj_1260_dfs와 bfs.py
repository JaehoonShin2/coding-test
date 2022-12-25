import sys
from collections import deque

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_1260.txt')

n, m, start = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

D_visited = [False] * (n+1)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

dfs(graph, start, D_visited)

print()

B_visited = [False] * (n+1)

def bfs(graph, v, visited):
    q = deque([v])
    visited[v] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True

bfs(graph, start, B_visited)