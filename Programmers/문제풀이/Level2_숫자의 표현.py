def solution(n):
    answer = 0
    
    # 자연수 n을 연속한 자연수들로 표현 하는 방법
    # binary?
    # 원본/
    # 2로 나눴을 때 나머지가 1라면 가능
    # 15/2 == 7...1 -> 7,8
    # 3으로 나눴을 때 나머지가 0면 가능
    # 15/3 == 5...0 -> 4 5 6
    # 4로 나눴을 때 나머지가 1면 가능
    # 15/4 == 3...3 실패
    # 5로 나눴을 때 나머지가 0면 가능
    # 15/5 == 3...0  1 2 3 4 5
    # 6로 나눠 1
    # 15/6 == 2...2
    # 7로 나눠 0
    # 15/7 == 2...1
    # 8로 나눠 1
    
    # # 인풋값이 짝수라면
    # if n % 2 == 0:
    #     for i in range(n//2):
    #         # 만약 2,4,6,8 ... 와 같을 때
    #         if i % 2 == 1:
    #             if n % 2 == 0:
    #                 answer += 1
    #         elif i % 2 == 0:
    #             if n % 2 == 1:
    #                 answer += 1 

    # # 인풋값이 홀수라면
    # elif n % 2 == 1:
    #     for i in range(n//2+1):
    #         # 만약 2,4,6,8 ... 와 같을 때
    #         if i % 2 == 0:
    #             if n % 2 == 1:
    #                 answer += 1
    #         elif i % 2 == 1:
    #             if n % 2 == 0:
    #                 answer += 1 
    
    dp = ''
    if n % 2 == 0:
        dp = list([0]*(n//2+1) for i in range(n//2+1))
        
        for i in range(n//2, 0, -1):
            
        
    else:
        dp = list([0]*(n//2+2) for i in range(n//2+2))
    
    
    return answer

print(solution(16))