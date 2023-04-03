import sys
from collections import deque

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_4963.txt')

# 1 = 땅 / 0 : 바다
# 가로, 세로, 대각선으로 이어져있다면 하나의 섬

def func(h, w):
    
    maps = [ list(map(int, sys.stdin.readline().split())) for _ in range(h) ]
    
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        while q:
            x, y = q.popleft()
            if maps[x][y] == 0: continue
            maps[x][y] = 0
            for step in steps:
                nx = x + step[0]
                ny = y + step[1]

                if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == 1 :
                    q.append((nx, ny))
                else: continue
        return

    cnt = 0

    # 행
    for i in range(h):
        # 열
        for j in range(w):
            if maps[i][j] == 1:
                bfs(i, j)
                cnt += 1

    answer.append(cnt)
    cnt = 0

steps = [(-1, 0),(1, 0),(0, -1),(0, 1),(-1, -1),(-1, 1),(1, -1),(1, 1)]

answer = []

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        for ans in answer:
            print(ans)

        break
    else:
        func(h, w)
