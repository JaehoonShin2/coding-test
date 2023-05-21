import math

def solution(n,a,b):
    answer = 0
    while True:
        answer += 1
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        if a == b or a == 0 or b == 0:
            break
    return answer    
    
    
    
    
n,a,b = 8, 4, 7
print(solution(n,a,b))