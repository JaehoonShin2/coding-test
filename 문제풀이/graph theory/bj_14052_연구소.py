from collections import deque
import sys
import copy
import time

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_14502.txt')

start = time.time()

steps = [(-1,0), (1,0), (0,-1), (0,1) ]
# n은 세로, m은 가로
n, m = map(int, sys.stdin.readline().split())
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 현재 2의 위치를 찾고, 바이러스의 전파를 확인하는 함수
def virus():
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
# 만약 그래프에서 해당 좌표가 2일 경우 q에 저장
                q.append((i, j))

    copy_graph = copy.deepcopy(graph)

# 2가 담긴 q에 아직 값이 담겨있을 때
    while q:
        x, y = q.popleft()
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]
# nx, ny가 각각 0부터 해당 행, 열의 값에 해당할 때           
            if (0 <= nx < n) and (0 <= ny < m):
# 그래프 노드의 값이 0 이라면 바이러스 전염, 2로 변경
                if(copy_graph[nx][ny] == 0):
                    copy_graph[nx][ny] = 2
                    q.append((nx, ny))

# 모든 바이러스 전파가 끝난 뒤, 여전히 생존해있는 0의 가짓수를 센다.
    global cnt
    result = 0
    for i in range(n):
        for j in range(m):
            if (copy_graph[i][j] == 0):
                result += 1
# 글로벌로 선언한 cnt와 반복문으로 형성된 안전지역 중 더 큰 값을 cnt에 담는다.
    cnt = max(cnt, result)

cnt = 0

def make_wall(count):
    if(count == 3):
        virus()
        return
    for i in range(n):
        for j in range(m):
            if(graph[i][j] == 0):
                graph[i][j] = 1
                make_wall(count+1)
# 재귀함수가 종료되면 다시 해당 노드를 0으로 변경
                graph[i][j] = 0

make_wall(0)
print(cnt)

end = time.time()

print('time = %0.7f'%(end-start))
