def solution(arr, n):
    nums_dict = {}
    for i in range(len(arr)):
        if n - arr[i] in nums_dict:
            return True
        nums_dict[arr[i]] = i
    return False

arr=[5,3,9,13]  
n=8
print(solution(arr, n))



# def solution(arr, n):
#     answer = False
#     cnt=len(arr)
#     dp=[[0] * (cnt+1) for _ in range(cnt+1)]
    
#     for i in range(cnt):
#         if arr[i] == n:
#             return True
#         dp[i+1][0] = arr[i]
#         dp[0][i+1] = arr[i]
    
#     for i in range(1, cnt+1):
#         for j in range(1, cnt+1):
#             if i == j:
#                 dp[i][j] = dp[i][0]
#             else:
#                 dp[i][j] = dp[i][0] + dp[0][j]
#                 if dp[i][j] == n:
#                     return True
#     return False