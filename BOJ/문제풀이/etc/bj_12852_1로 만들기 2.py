import sys

sys.stdin = open("C:/Users/R/Desktop/python_input/bj_12852.txt")

n = int(sys.stdin.readline().rstrip())

# 시간제한 0.5초
# o(n) -> 5천만 개
# o(n^2) -> 5천 개

dp = [int(1e9)] * (n+1)
arr = [[] for _ in range(n+1)]

dp[1] = 0
arr[1] = [1]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    arr[i] = arr[i-1] + [i]
    if i % 2 == 0 and dp[i // 2] + 1 < dp[i] :
        dp[i] = dp[i//2] + 1
        arr[i] = arr[i//2] + [i]
    if i % 3 == 0 and dp[i // 3] + 1 < dp[i] :
        dp[i] = dp[i//3] + 1
        arr[i] = arr[i//3] + [i]


print(dp[n])
print(*reversed(arr[n]))


