import sys
sys.setrecursionlimit(10**6)

sys.stdin = open("C:/Users/R/Desktop/python_input/bj_11722.txt")

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))


dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if data[j] > data[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# def binory(start, end, target):
#     mid = (start+end)//2
#     if mid == 0:
#         return 0
#     elif dp[mid-1] > target and dp[mid] < target:
#         return mid
#     elif target < dp[mid]:
#         return binory(mid+1, end, target)
#     else:
#         return binory(start, mid-1, target)

# dp = [0]

# for data in dataes :
#     if dp[len(dp)-1] > data:
#         dp.append(data)
#     elif dp[len(dp)-1] < data :
#         idx = binory(0, len(dp), data)
#         dp[idx] = data

# print(len(dp))