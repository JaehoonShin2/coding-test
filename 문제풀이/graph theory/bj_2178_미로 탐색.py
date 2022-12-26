import sys
from collections import deque

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_2178.txt')

# 1초
# 이중 for문 10000개

n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(x, y):
    q = deque()
    q.append( (x, y) )
    while q:
        print(q)
        x, y = q.popleft()
        visited[x][y] = True
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    return graph[n-1][m-1]

print(bfs(0, 0))

for i in graph:
    print(*i, end=' ')
    print()