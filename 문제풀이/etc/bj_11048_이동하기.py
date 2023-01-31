import sys

sys.stdin = open("C:/Users/R/Desktop/python_input/bj_11048.txt")

n, m  = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

dp[1][1] = graph[0][0]

for i in range(1, m+1):
    for j in range(1, n+1):
        dp[j][i] = dp[j-1][i] + graph[j-1][i-1]
        
        dp[j][i] = max(dp[j][i], dp[j-1][i-1]+graph[j-1][i-1])
        
        dp[j][i] = max(dp[j][i], dp[j][i-1]+graph[j-1][i-1])

print(dp[n][m])