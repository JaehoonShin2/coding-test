import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

dp=[10001] * (m+1)

dp[0] = 0

# An = min(An, An-k + 1)
def td(m, arr):
    if m <= 0: return 0
    for i in arr:
        dp[m] = min(td(m, arr), td(m - i, arr) + 1)
    return dp[m]

result = td(m, arr)
if  result == 10001: print(-1)
else: print(result)

