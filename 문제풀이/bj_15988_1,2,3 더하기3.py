import sys

sys.stdin = open("C:/Users/R/Desktop/python_input/bj_15988.txt")

dp = [0] * (n+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])
    dp[i] %= 1000000009

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    
    n = int(sys.stdin.readline().rstrip())
    print(dp[n])