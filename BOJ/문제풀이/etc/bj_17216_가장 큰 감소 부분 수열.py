import sys

sys.stdin = open("C:/Users/R/Desktop/python_input/bj_17216.txt")

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

dp = [0] * (n)
dp[len(data)-1] = data[len(data)-1]

for i in reversed(range(n)):
    for j in reversed(range(i+1, n)):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + data[i])
        else:
            dp[i] = max(dp[i], data[i])

print(max(dp))