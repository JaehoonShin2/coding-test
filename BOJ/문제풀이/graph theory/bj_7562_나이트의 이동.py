import sys
from collections import deque
import time

start = time.time()

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_7562.txt')

#   체스판의 길이는 4~300 max input date == 300^2 = 90000
#   시간제한 1 초
#   2차원 for문 불가


steps = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

def bfs(x, y):
    # 데큐 선언
    q = deque()
    # 초기 위치 q에 삽입
    q.append([x, y])
    # 만약 최초 값이 타겟값이라면 바로 리턴
    if graph[x][y] == -1: 
        print(0)
        return
    while q:
        x, y = q.popleft()

        for step in steps:
            nx = x + step[0]
            ny = y + step[1]

            # nx와 ny가 0보다 작거나, n보다 같거나 클 경우 패스
            if nx < 0 or nx >= n or ny < 0 or ny >= n: 
                continue
            # graph[nx][ny] 가 타겟값이라면 cnt를 리턴
            if graph[nx][ny] == -1: 
                print(graph[x][y] + 1)
                return 
            # graph[nx][my] 에 대해 처음 방문이며, 현재 q에 nx,ny에 대한 값이 없다면 큐에 추가            
            # if graph[nx][ny] == 0 and [nx, ny] not in q:
            # 처음에는 메모리를 위해 q를 돌며 [nx, ny]를 검사했으나 이로 인한 시간 초과가 발생해서
            # 코드를 수정하였더니 정답 처리가 됨
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])

t = int(sys.stdin.readline().rstrip())

for _ in range(t):

    n = int(sys.stdin.readline().rstrip())
    x, y = map(int, sys.stdin.readline().split())
    tx, ty = map(int, sys.stdin.readline().split())
    graph = [ [0 for _ in range(n)] for _ in range(n)]
    # 초기값 0, 방문처리 , 최종 목표 -1
    graph[tx][ty] = -1

    bfs(x, y)

end = time.time()
print('time = %0.7f'%(end-start))