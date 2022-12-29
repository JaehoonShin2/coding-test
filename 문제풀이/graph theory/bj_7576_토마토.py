import sys
from collections import deque

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_7576.txt')

m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

steps = [(-1, 0),(1, 0),(0, -1),(0, 1)]

res = 0

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])


def bfs():
    while q:
        x, y = q.popleft()
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                q.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1

bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res - 1)
