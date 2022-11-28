import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

dp = [0] * 11
dp[0] = arr[0]
max1 = dp[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]+arr[i], arr[i])
    if max1 < dp[i]:
        max1 = dp[i]

print(max1)
print(dp)
