import sys

n = int(sys.stdin.readline().rstrip())
k = list(map(int, sys.stdin.readline().split()))

dp = [0] * 1001

dp[1] = k[0]

for i in range(2, n+1):
    if dp[i] == 0:
        dp[i] = max(dp[i-1], dp[i-2] + k[i-1])

#점화식 => An = max( An-1, An-2 + Ki)

print(dp[n])