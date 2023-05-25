def solution(land):
    dp = [[0] * 4 for _ in range(len(land))]

    for i, l in enumerate(land):
        for j, ll in enumerate(l):
            for k in range(4):
                if j == k: continue
                dp[i][j] = max(dp[i][j], ll + dp[i-1][k])
    
    return max(dp[len(land)-1])

land=[[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))


# def solution(land):

#     for i in range(1, len(land)):
#         for j in range(len(land[0])):
#             land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

#     return max(land[-1])