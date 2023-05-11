def solution(n):
    
    answer = 0
    for i in range(n):
        sum = 0
        for j in range(i+1, n+1):
            sum += j
            if n == sum:
                answer += 1
                break
            elif n < sum:
                break
            
    return answer

print(solution(15))