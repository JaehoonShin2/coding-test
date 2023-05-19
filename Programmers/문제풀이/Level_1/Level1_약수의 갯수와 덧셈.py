def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        
        isCheck = [0] * (i+1)
        isCheck[1] = 1
        
        for j in range(2, i+1):
            if isCheck[j] == 0 and i % j == 0:
                k = j
                while k <= i:
                    isCheck[k] = 1
                    k *= i

        if isCheck.count(1) % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer

left, right = 13, 17
print(solution(left, right))