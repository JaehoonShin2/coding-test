import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

dp=[10001] * (m+1)

dp[0] = 0
# 동전의 종류만큼 반복
for i in range(n):
    # 하나의 동전 종류로 dp를 1~m까지 생성
    for j in range(arr[i], m+1):
        if dp[j - arr[i]] != 10001:
            dp[j] = min(dp[j], dp[j-arr[i]]+1)

if dp[m] == 10001: print(-1)
else: print(dp[m])

