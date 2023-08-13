def solution(msg):
    
    dic = dict(zip([chr(c) for c in range(ord('A'), ord('Z')+1)] ,range(1, 27)))
    
    answer = []
    
    m = list(msg)
    temp = m.pop(0)
    temp_idx = 0
    max_idx = 26
    
    while temp != "":
        if temp in dic:
            if m:
                temp_idx = dic[temp]
                temp += m.pop(0)
            else:
                answer.append(dic[temp])
                return answer
        else:
            answer.append(temp_idx)
            max_idx += 1
            dic[temp] = max_idx
            temp = temp[-1]

    
    return answer