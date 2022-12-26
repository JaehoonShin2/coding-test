import sys
from collections import deque

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_1012.txt')

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    m, n, r = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(r):
        b, a = map(int, sys.stdin.readline().split())
        graph[a][b] = 1

    visited = [[False] * m for _ in range(n)]

    steps = [(1,0),(-1,0),(0,1),(0,-1)]

    def bfs(x, y):
        cnt = 0
        q = deque()
        q.append((x, y))
        while q:
            x, y = q.popleft()
            if visited[x][y] == True: continue
            visited[x][y] = True
            cnt += 1
            for step in steps:
                nx = x + step[0]
                ny = y + step[1]

                if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    q.append((nx,ny))
        return cnt

    ans = []

    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and graph[i][j] == 1:
                ans.append(bfs(i,j))

    print(len(ans))