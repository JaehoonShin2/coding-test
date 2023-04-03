import sys
from collections import deque
import time

start = time.time()

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_10026.txt')

#   시간제한 1초
#   2중 for문

n = int(sys.stdin.readline().rstrip())
graph = [ list(str(sys.stdin.readline().rstrip())) for _ in range(n)]
visited_rgb = [[0 for _ in range(n)] for _ in range(n)]
visited_rg_b = [[0 for _ in range(n)] for _ in range(n)]

steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs_rgb(x, y, visited_):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        if visited_[x][y] == 1: continue
        visited_[x][y] = 1
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]

            # nx, ny는 0보다 작거나 n보다 같거나 크면 통과
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            # 최초 방문에 대해서 q에 추가하고, 방문처리
            if visited_[nx][ny] == 0 and graph[x][y] == graph[nx][ny]:
                visited_[nx][ny] == 1
                q.append([nx, ny])


def bfs_rg_b(x, y, visited_):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        if visited_[x][y] == 1: continue
        visited_[x][y] = 1
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]

            # nx, ny는 0보다 작거나 n보다 같거나 크면 통과
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            # 최초 방문에 대해서 q에 추가하고, 방문처리
            if visited_[nx][ny] == 0:
                if graph[x][y] != 'B' and graph[nx][ny] != 'B':
                    visited_[nx][ny] == 1
                    q.append([nx, ny])

cnt_rgb = 0
cnt_rg_b = 0

for i in range(n):
    for j in range(n):
        if visited_rgb[i][j] == 0:
            bfs_rgb(i, j, visited_rgb)
            cnt_rgb += 1
        
        if visited_rg_b[i][j] == 0:
            if graph[i][j] != 'B':
                bfs_rg_b(i, j, visited_rg_b)
                cnt_rg_b += 1
            else:
                bfs_rgb(i, j, visited_rg_b)
                cnt_rg_b += 1


print(cnt_rgb, cnt_rg_b)

end = time.time()
print('time = %0.7f'%(end-start))