import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

dpUp = [1] * n
dpDown = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dpUp[i] = max(dpUp[i], dpUp[j]+1)

arr.reverse()

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dpDown[i] = max(dpDown[i], dpDown[j] + 1)
dpDown.reverse()

dp = []

for i in range(n):
    dp.append( dpUp[i]+dpDown[i]- 1 )

print(max(dp))
