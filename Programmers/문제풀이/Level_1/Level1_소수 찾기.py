def solution(n):
    answer = 0
    
    # 에라토스테네스의 체
    # 2, 3, 4, 5, 6, 7, 8, 9, ... n 
    # 2를 소수로 잡고 2의 배수를 모두 지움
    # 왜냐하면 2의 배수라는 것은 2가 해당 수의 약수로 존재한다는 의미이기 때문
    # 3, 5, 7, 9, ... n
    # 3를 소수로 잡고 3의 배수를 모두 지움
    # 5, 7, ... n
    
    isCheck = [False] * (n+1)
    
    for i in range(2, n+1):
        
        if isCheck[i] == False:
            answer += 1
        
        for j in range(i, n+1, i):
            isCheck[j] = True        
    
    
    return answer


print(solution(10))