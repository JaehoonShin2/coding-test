from collections import defaultdict as dd
def solution(s):
    answer = []
    
    map = dd(list)
    
    for k, v in zip(s, range(len(s))):
        if len(map[k]) > 0:
            gap = v-map[k][-1][0]
            map[k].append([v, gap])
            answer.append(gap)     
        else:
            map[k].append([v, -1])
            answer.append(-1)

    return answer