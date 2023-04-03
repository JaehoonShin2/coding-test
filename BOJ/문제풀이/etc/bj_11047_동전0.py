import sys

n, k = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

cnt = 0

arr.reverse()

for i in arr:
    if k < i: continue
    else:
        cnt += k // i
        k = k % i

print(cnt)
