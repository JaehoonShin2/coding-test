def solution(triangle):
    
    max_row = len(triangle)
    max_col = len(triangle[max_row-1])
    
    dp = [[0] * (max_col+1) for _ in range(max_row+1)]    
    
    for i in range(max_row):
        for j in range(len(triangle[i])):
            dp[i+1][j+1] = triangle[i][j] + max(dp[i][j], dp[i][j+1])
    
    return (max(dp[max_row]))    

triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))