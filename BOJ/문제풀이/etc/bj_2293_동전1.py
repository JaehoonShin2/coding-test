import sys

#sys.stdin = open('C:/Users/R/Desktop/python_input/bj_2293.txt')

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

dp = [0] * (k+1)

dp[0] = 1

for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]

print(dp[k])