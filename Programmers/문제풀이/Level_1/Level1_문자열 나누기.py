def recur(s, idx, target_cnt, e_cnt, target):
    if len(s)-1 == idx:
        return idx
    
    if target_cnt == e_cnt:
        return idx
    
    else:
        if s[idx+1] == target:
            return recur(s, idx+1, target_cnt+1, e_cnt, target)
        else:
            return recur(s, idx+1, target_cnt, e_cnt+1, target)

def solution(s):
    answer = 0
    
    index = 0
    while index < len(s):
        new_index = recur(s, index, 1, 0, s[index])
        print(s[index:new_index+1])
        answer += 1
        index = new_index+1
    
    return answer

s="banana"
s="abracadabra"
s="aaabbaccccabba"
print(solution(s))