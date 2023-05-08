def solution(priorities, location):
    
    p = []
    answer = 1
    
    for idx, value in enumerate(priorities):
        if idx == location:
            p.append((value, True))
        else:
            p.append((value, False))
    
    while p:
        max_num = max(p)[0]
        num = p.pop(0)
        
        if max_num == num[0]:
            if num[1]:
                return answer
            else:
                answer += 1
        else:
            p.append(num)