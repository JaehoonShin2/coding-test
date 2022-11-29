import sys

n, m = map(int, sys.stdin.readline().split())
arrA = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

m, k = map(int, sys.stdin.readline().split())
arrB = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

arr = [[0 for _ in range(k)] for i in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            arr[i][j] += (arrA[i][l] * arrB[l][j])

for row in arr:
    for num in row:
        print(num, end=" ")
    print()
