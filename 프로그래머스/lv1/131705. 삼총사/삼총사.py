from itertools import combinations as cb

def solution(number):
    
    answer = 0
    l = len(number)
    c = list(cb(range(l), 3))
    for arr in c:
        if sum(number[x] for x in arr) == 0:    
            answer += 1
    return answer