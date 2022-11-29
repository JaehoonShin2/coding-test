import sys

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

dp = [0] * 100001
dp[0] = arr[0]

for i in range(1, len(arr)):
    dp[i] = dp[i-1] + arr[i]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    print(dp[y-1] - dp[x-2])

