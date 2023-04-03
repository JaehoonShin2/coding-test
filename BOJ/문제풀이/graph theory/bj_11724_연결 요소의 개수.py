import sys
sys.setrecursionlimit(10**6)
from collections import deque

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_11724.txt')

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

D_visited = [False] * (n+1)

## dfs 해결법
def dfs(v, visited):
    if visited[v] == True: 
        return
    visited[v] = True
    for node in graph[v]:
        if visited[node] == False:
            dfs(node, visited)
        else: continue
    return

D_cnt = 0

for i in range(1, n+1):
    if D_visited[i] == False:
        dfs(i, D_visited)
        D_cnt += 1
        
print(D_cnt)

B_visited = [False] * (n+1)

def bfs(v, visited):
    q = deque()
    visited[v] = True
    q.append(graph[v])
    while q:
        print(q)
        now = q.popleft()
        for node in now:
            if visited[node] == False:
                visited[node] = True
                q.append(graph[node])
            else: continue
        return

B_cnt = 0

for i in range(1, n+1):
    if B_visited[i] == False:
        bfs(i, B_visited)
        B_cnt += 1
        
print(B_cnt)

