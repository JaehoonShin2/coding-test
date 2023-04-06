def solution(answers):
    
    answer = []
    
    ans_1 = [1,2,3,4,5]
    ans_2 = [2,1,2,3,2,4,2,5]
    ans_3 = [3,3,1,1,2,2,4,4,5,5]
    
    ans_cnt = len(answers)
    
    r_ans_1 = ans_1 * ((ans_cnt//len(ans_1)) + 1)
    r_ans_2 = ans_2 * ((ans_cnt//len(ans_2)) + 1)
    r_ans_3 = ans_3 * ((ans_cnt//len(ans_3)) + 1)
    
    start = 0
    
    cor_1 = 0
    cor_2 = 0
    cor_3 = 0
    
    while start < ans_cnt:
        
        if answers[start] == r_ans_1[start]:
            cor_1 += 1
        if answers[start] == r_ans_2[start]:
            cor_2 += 1
        if answers[start] == r_ans_3[start]:
            cor_3 += 1
        
        start += 1
    
    cor_list = [cor_1, cor_2, cor_3]
    
    cnt_max = max(cor_list)
    
    for node in range(3):
        if cnt_max == cor_list[node]:
            answer.append(node+1)
    
    return answer


a = [1,3,2,4,2]

print(solution(a))