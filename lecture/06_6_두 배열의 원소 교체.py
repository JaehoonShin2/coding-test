import sys

n, k = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort()
b.sort()

for i in range(k):
    if a[i] < b[n-1-i]:
        a[i], b[n-1-i] = b[n-1-i], a[i]
    else: break

print(sum(a))