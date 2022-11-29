import sys

a = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0] * 1001

lis = 1
dp[0] = 1

for i in range(a):
    for j in range(i):
        if arr[i] > arr[j]:
            print(arr[i], arr[j])
            dp[i] = dp[j] + 1
    lis = max(lis, dp[i])
    print(lis)    
