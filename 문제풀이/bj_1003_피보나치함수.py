import sys

t = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(t)]

dp = [[0] * 2 for _ in range(41)]

dp[0][0] = 1
dp[0][1] = 0
dp[1][0] = 0
dp[1][1] = 1


for a in arr:
    if a < 2: 
        print(dp[a][0], dp[a][1])
    else:
        for i in range(2, a+1):
            for j in range(2):
                dp[i][j] = dp[i-1][j] + dp[i-2][j]
        print(dp[a][0], dp[a][1])

        