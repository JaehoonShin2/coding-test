def solution(n):
    dp = [0] * (n+1)
    
    dp[1]=1
    dp[2]=2
    d = 1000000007
    
    for i in range(3, n+1):
        dp[i] = (dp[i-1]+dp[i-2])%d
    
    return dp[i]

n=4
print(solution(n))