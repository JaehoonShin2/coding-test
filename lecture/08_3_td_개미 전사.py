import sys

n = int(sys.stdin.readline().rstrip())
k = list(map(int, sys.stdin.readline().split()))

dp = [0] * 101

#점화식 => An = max( An-1, An-2 + Ki)

def td(n):
    if n == 0:
        return dp[0]
    if n == 1:
        dp[1] = k[0]
        return dp[1]
    if dp[n] != 0:
        return dp[n]
    dp[n] = max(td(n-1), td(n-2) + k[n-1])
    return dp[n]

print(td(n))