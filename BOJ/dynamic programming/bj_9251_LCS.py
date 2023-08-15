
def solution():
    from sys import stdin
    
    # 두 개의 문자열 받기
    # str1 = stdin.readline().rstrip()
    # str2 = stdin.readline().rstrip()
    
    str1, str2 = "ACAYKP", "CAPCAK"
    
    # 두 개의 문자열에 대한 LCS 를 구하기 위한 DP 그래프 만들기
    m, n = len(str1), len(str2)
    
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            # 만약 str1[i-1] 과 str2[i-1] 의 문자열이 동일하다면 부분수열 가능
            # 따라서 현재까지의 부분수열의 합 +1 을 dp[i][j] 에 추가
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            
            # 일치하지 않는다면 부분수열 대상이 아님. 
            # 이 경우 현재까지의 부분수열의 최대합을 dp[i][j] 에 추가
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    print(dp[m][n])
    

if __name__ == "__main__":
    solution()