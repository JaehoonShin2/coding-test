import sys

sys.stdin = open("C:/Users/R/Desktop/python_input/bj_11052.txt")

n = int(sys.stdin.readline().rstrip())
arr = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0] * (n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j]+arr[j])

print(dp)