def solution(n):
    answer = 0
    
    one_cnt = bin(n).count('1')
    
    # n 에서 부터 1000001 이하 까지의 반복
    for num in range(n+1, 1000001):
        
        new_one_cnt = bin(num).count('1')
    
        if one_cnt == new_one_cnt:
            answer = num
            break
        
    return answer