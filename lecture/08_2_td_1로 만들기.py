import sys

x = int(sys.stdin.readline().rstrip())

dp = [0] * 30001

def topdown(x):
    if x == 1:
        return 0
    if dp[x] != 0:
        return dp[x]
    dp[x] = topdown(x-1) + 1
    if x % 2 == 0:
        dp[x] = min(dp[x], topdown(x//2)+ 1)
    if x % 3 == 0:
        dp[x] = min(dp[x], topdown(x//3)+ 1)
    if x % 5 == 0:
        dp[x] = min(dp[x], topdown(x//5)+ 1)
    return dp[x]

#점화식 => An = min(An-1, An/2, An/3, An/5) + 1

print(topdown(x))