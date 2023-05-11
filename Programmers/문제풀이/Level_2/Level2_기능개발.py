def solution(progresses, speeds):
    
    answer = []
    cnt_answer = []
        
    for idx in range(len(progresses)):
        p = progresses[idx]
        s = speeds[idx]   
        
        cnt = 0
        while p < 100:
            p += s
            cnt += 1
        cnt_answer.append(cnt)
    
     
    start_num = cnt_answer[0]
    result_cnt = 1
    
    idx = 1
    while idx < len(cnt_answer):
       
        if start_num >= cnt_answer[idx]:
            result_cnt += 1
        
        else:
            answer.append(result_cnt)
            start_num = cnt_answer[idx]
            result_cnt = 1
            
        idx += 1
    
    answer.append(result_cnt)
         
    return answer


progresses1=[93, 30, 55]
speeds1=[1, 30, 5]
progresses2=[95, 90, 99, 99, 80, 99]
speeds2=[1, 1, 1, 1, 1, 1]

print(solution(progresses2, speeds2))