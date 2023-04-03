# 시간 제한 1초
# 인풋데이터 100개*100 = 1만 개

import sys

sys.stdin = open("C:/Users/R/Desktop/python_input/bj_1890.txt")

n = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp =[[0 for _ in range(n+1)] for _ in range(n+1)]

# dp[0][0] 의 각 노드에 올 수 있는 경우의 수를 담는다.
dp[0][0] = 1

for i in range(n):
    for k in range(n):
        # 만약 i와 k, 행과 열이 그래프의 가장 오른쪽 노드에 도착하면
        # dp[n][n] 에 1을 추가해준다.
        if i == n-1 and k == n-1:
            print(dp[i][k])
            break
        # 현재 dp에서 움직일 수 있는 값
        move_cnt = graph[i][k]
        # 아래로 이동
        if i + move_cnt < n:    
            dp[i+move_cnt][k] += dp[i][k]
        # 오른쪽으로 이동
        if k + move_cnt < n:
            dp[i][k+move_cnt] += dp[i][k]
        






# 시간제한이 1초 일 때, 빅O를 기준으로 시간복잡도를 계산해보면
# o(n) -> 인풋데이터 1억 개.
# ex) 1차원 for문,,,
# o(n^2) -> 인풋데이터 1만 개
# ex) 2차원 for문,,,
# o(n^3) -> 인풋데이터 500개...
# o(2^n) -> 20개






# case1 => 기본 입력값 출력은 되지만 시간 초과

# result = 0

# def func(x, y):
#     global result

#     if x == n-1 and y == n-1:
#         result += 1
#         return
#     elif x >= n or y >= n:
#         return
#     else:
#         num = graph[x][y]
#         func(x+num, y)
#         func(x, y+num)
#         return

# func(0, 0)
# print(result)