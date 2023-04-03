import sys
from collections import deque

#  높이는 1이상 100 이하의 정수
#  시간제한 1 초

n = int(sys.stdin.readline().rstrip())
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]


max = 0

steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(h, i, j):
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.popleft()
        # 일단 한 번이라도 방문한 노드는 방문처리
        safety[x][y] = 2
        # 만약 graph[x][y] 가 물의 높이보다 낮다면 잠겼기 때문에 safety를 1로
        if graph[x][y] <= h:
            safety[x][y] = 1
            
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]

            # nx, ny는 0보다 크고 n보다 작아야만 한다.
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            # safety[nx][ny] 가 0, 초기상태면 q에 담기
            if safety[nx][ny] == 0 and graph[nx][ny] > h:
                if [nx, ny] not in q:
                    q.append([nx, ny])


max = 1

for h in range(1, 101):
    cnt = 0
    safety = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] <= h and safety[i][j] == 0:
                safety[i][j] = 1
            if safety[i][j] == 0:
                bfs(h, i, j)
                cnt += 1
    if max < cnt:
        max = cnt
    
    if cnt == 0: 
        print(max)
        exit()