import sys

n = int(sys.stdin.readline().rstrip())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    if dp[i] == 0:
        dp[i] = (dp[i-1]% 796796) + ( 2*dp[i-2]% 796796)

#점화식 => An = ( An-1+ 2*An-2)

print(dp[n])