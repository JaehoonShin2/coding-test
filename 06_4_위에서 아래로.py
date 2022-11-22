import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort(reverse=True)

print(arr)