import sys

n, k = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

temp = sum(arr[:k])
result = temp

for i in range(k, n):
    temp += arr[i] - arr[i-k]
    result = max(result, temp)

print(result)