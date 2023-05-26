from collections import deque

def solution(n):
    
    cnt = 0
    q = deque()
    q.append('4')
    q.append('13')
    l = []
    
    while True:
        if cnt >= n:
            break
        
        num = q.popleft()
        q.append(num+'4')
        q.append(num+'13')
        l.append(int(num))
        cnt += 1
    
    l.sort()
    
    for ll in range(1,len(l)-1):
        if l[ll] > l[ll-1]:
            continue
        else:
            print('error')
    
    return l[n-1]
    
n=5000
print(solution(n))
