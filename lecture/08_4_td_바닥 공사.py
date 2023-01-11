import sys

n = int(sys.stdin.readline().rstrip())

dp = [0] * 1001

def td(n):
    if n == 1:
        dp[n] == 1
        return 1
    if n == 2:
        dp[n] == 3
        return 3
    if dp[n] == 0:
        dp[n] = ( td(n-1) % 796796) + ( 2 * td(n-2) % 796796)
    return dp[n]

#점화식 => An = ( An-1+ 2*An-2)

print(td(n))