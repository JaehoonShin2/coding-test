from collections import defaultdict as dd

def solution(keymap, targets):
    answer = []
    
    d = dd(list)
    
    for node in keymap:
        for idx, k in enumerate(node):
            d[k].append(idx+1)
    
    for t in targets:
        result = 0
        for i in t:
            if d[i] == []:
                result = -1
                break
            else:    
                result += min(d[i])    
        answer.append(result)
    
    return answer

keymap=["ABACD", "BCEFD"]	
targets=["ABCD","AABB"]

print(solution(keymap, targets))