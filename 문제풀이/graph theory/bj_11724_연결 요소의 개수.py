import sys
sys.setrecursionlimit(10**6)

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_11724.txt')

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def dfs(v, visited):
    if visited[v] == True: 
        return
    visited[v] = True
    for node in graph[v]:
        if visited[node] == False:
            dfs(node, visited)
        else: continue
    return

cnt = 0

for i in range(1, n+1):
    if visited[i] == False:
        dfs(i, visited)
        cnt += 1
        
print(cnt)
