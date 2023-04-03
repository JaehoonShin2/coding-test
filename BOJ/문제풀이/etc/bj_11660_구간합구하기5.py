import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_11660.txt')

n, m = map(int, sys.stdin.readline().split())

graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0] * (n+1) for _ in range(n+1)]

answer = []

for i in range(n):
    sum = 0
    for j in range(n):
        sum += graph[i][j]
        dp[i+1][j+1] = sum + dp[i][j+1]


for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    answer.append(result)

for a in answer:
    print(a)
    