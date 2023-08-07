from collections import defaultdict as dd
def solution(s):
    answer = []
    
    map = dd(list)
    
    for k, v in zip(s, range(len(s))):
        answer.append(-1) if len(map[k]) == 0 else answer.append(v-map[k][-1])
        map[k].append(v)
    return answer