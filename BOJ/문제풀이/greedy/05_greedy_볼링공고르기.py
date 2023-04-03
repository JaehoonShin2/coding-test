import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(n-1):
    for j in range(i, n):
        if arr[i] != arr[j]: 
            cnt += 1
print(cnt)