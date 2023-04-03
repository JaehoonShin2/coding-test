import sys

n = int(sys.stdin.readline().rstrip())

arr = [0] * (n+1)

for i in range(1, n+1):
    arr[i] = int(sys.stdin.readline().rstrip())

dp = [0] * 301

if n > 2:
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-2], dp[i-3]+arr[i-1]) +arr[i]
    
    print(dp[n])
elif n == 2:
    print(arr[1]+arr[2])
elif n == 1:
    print(arr[1])


