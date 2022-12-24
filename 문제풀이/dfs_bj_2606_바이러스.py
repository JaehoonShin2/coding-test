import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_2606.txt')

c = int(sys.stdin.readline().rstrip())

n = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(c+1)]

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (c+1)

def dfs(arr, x, visited):
    visited[x] = 1
    for i in graph[x]:
        if visited[i] == 0:
            dfs(arr, i, visited)
    return

dfs(graph, 1, visited)

result = 0

for i in visited:
    if i == 1: result += 1

print(result-1)