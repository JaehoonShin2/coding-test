# def solution(n):
#     ans = 0
    
#     dp = [1e9] * (n+1)
    
#     dp[0] = 0
    
#     for i in range(1, n+1):
#         if i%2 == 0:
#             dp[i] = dp[i//2]
        
#         dp[i] = min(dp[i], dp[i-1]+1)
        
#     return dp[n]


def solution(n):
    
    ans = 0
    
    while n > 0:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            ans += 1
    
    return ans
    

def solution(n):
    print(bin(n))
    return bin(n).count('1')

print(solution(10))
