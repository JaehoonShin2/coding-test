import sys

sys.stdin = open("C:/Users/R/Desktop/python_input/bj_12865.txt")

n, k = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]


for i in range(1, n + 1):

    for j in range(1, k+1):

        weight = arr[i-1][0] 
        value = arr[i-1][1]

        if j < weight:
            dp[i][j] = dp[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])

print(dp[n][k])


# for i in arr:
#     if(dp[i[0]] == 0 ):
#         dp[i[0]] = i[1]
#     else:
#         if(dp[i[1]] < i[1]):
#             dp[i[0]] = i[0]

# for i in range(2, k+1):
#     dp[i] = max([dp[l] + dp[i-l] for l in range(i-1)])

# print(dp[k])