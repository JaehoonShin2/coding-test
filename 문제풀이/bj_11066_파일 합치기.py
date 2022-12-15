import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_11066.txt')

t = int(sys.stdin.readline().rstrip())

for _ in range(t):

    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().split()))

    dp = [[0 for i in range(n+1)] for _ in range(n+1)]

    sum = [0 for _ in range(n+1)]

    for i in range(n):
        sum[i+1] = sum[i] + arr[i]
    
    for i in range(2, n+1):
        for j in range(1, n+2-i):
            dp[j][j+i-1] = min([dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)]) + (sum[j+i-1] - sum[j-1])

    print(dp[1][n])