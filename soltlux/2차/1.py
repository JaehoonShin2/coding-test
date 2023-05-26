def solution(num):
    i = [x for x in range(1, num+1)]
    d = dict.fromkeys(i)

    answer = 0
    for kk in d:
        k = str(kk)
        if '3' in k:
            answer += 1
        elif '6' in k:    
            answer += 1
        elif '9' in k:
            answer += 1
    
    return answer

num=33
print(solution(num))