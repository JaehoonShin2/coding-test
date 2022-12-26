import sys
from collections import deque

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_2667.txt')

t = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(t)]

visited = [[False] * t for _ in range(t)]

steps = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        if visited[x][y] == True: continue
        visited[x][y] = True
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]

            if nx < 0 or nx >= t or ny < 0 or ny >= t: continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
                cnt += 1
    return cnt

ans = []

for i in range(t):
    for j in range(t):
        if visited[i][j] == False and graph[i][j] == 1:
            ans.append(bfs(i, j))


ans.sort()
print(len(ans))
for a in ans:
    print(a)