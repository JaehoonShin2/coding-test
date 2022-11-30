import sys

n = int(sys.stdin.readline().rstrip())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr.sort(key=lambda x: x[0])
a = [ i[1] for i in arr ]

cnts = a[0]
dp = [1] * len(a)

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

result = len(a) - max(dp)

print(result)































# import sys

# n = int(sys.stdin.readline().rstrip())

# a = []
# b = []

# for i in range(n):
#     x, y = map(int, sys.stdin.readline().split())
#     a.append((x, y))

# a.sort( key= lambda x : x[0])

# minA = a[0][1]
# cntA = 0
# for i in range(1, n):
#     if minA > a[i][1]:
#         cntA += 1    

# a.sort( key= lambda x : x[1])
# for i in range(n):
#     b.append( ( a[i][1], a[i][0] ) ) 

# minB = b[0][1]
# cntB = 0
# for i in range(1, n):
#     if minB > b[i][1]:
#         cntB += 1

# print(min( cntA, cntB))