import sys
from collections import deque
import time

start = time.time()

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_14502.txt')

m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
virusList = []

g = []

for i in range(n):
    for j in range(m):
        g.append((i, j))
        if graph[i][j] == 2:
            virusList.append([i, j])

steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 바이러스가 완전히 퍼지게 되는 bfs 함수
def virus(temp_):
    q = deque()
    while len(virusList) != 0:
        q.append(virusList.pop())

    while q:
        x, y = q.popleft()
        # 만약 temp[x[y] 가 2, 바이러스가 아니라면 통과
        if temp_[x][y] != 2: continue
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]

            # nx, ny는 0보다 작거나 n,m보다 같거나 클 수 없다
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            # temp[nx][ny] 가 0이라면 2로 바꾸고, q에 담는다.
            if temp_[nx][ny] == 0:
                temp_[nx][ny] = 2
                q.append([nx, ny])

def safety_seacrh(temp_):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp_[i][j] == 0:
                cnt += 1
    return cnt


def search():
    ans = 0
    for i in range(len(g)):
        for j in range(i+1, len(g)):
            for k in range(j+1, len(g)):
                cnt = 0
                temp_ = [row[:] for row in graph[:]]

                if temp_[g[i][0]][g[i][1]] == 0:
                    temp_[g[i][0]][g[i][1]] = 1
                    cnt += 1
                if temp_[g[j][0]][g[j][1]] == 0 : 
                    temp_[g[j][0]][g[j][1]] = 1
                    cnt += 1
                if temp_[g[k][0]][g[k][1]] == 0: 
                    temp_[g[k][0]][g[k][1]] = 1
                    cnt += 1
                
                if cnt != 3: 
                    continue
                    
                virus(temp_)
                count = safety_seacrh(temp_)
                ans = max(ans, count)
    print(ans)

search()

end = time.time()
print('time = %0.7f'%(end-start))