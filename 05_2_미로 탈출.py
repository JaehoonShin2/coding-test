from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

print(graph)

#상, 하, 좌, 우의 움직임
steps=[(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]
            #공간을 벗어났는지 확인
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m: continue
            #진행한 좌표가 괴물이 있는 곳인지 확인
            if graph[nx][ny] == 0: continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0,0))



