from itertools import combinations as cb

def solution(number):
    
    cnt = 0
    for i in cb(number, 3):
        if sum(i) == 0:    
            cnt += 1
    return cnt

number=[-3, -2, -1, 0, 1, 2, 3]
print(solution(number))