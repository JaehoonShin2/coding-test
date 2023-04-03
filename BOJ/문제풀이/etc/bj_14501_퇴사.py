import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_14501.txt')

n = int(sys.stdin.readline().rstrip())
d = [0]
p = [0]

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    d.append(x)
    p.append(y)

dp = [0] * (n+2)

for i in reversed(range(1, n+1)):
    day = d[i]
    if i-1 + day <= n:
        value = p[i]
        dp[i] = max(dp[i+1], dp[i+day] + value)
    else:
        dp[i] = dp[i+1]

print(dp[1])