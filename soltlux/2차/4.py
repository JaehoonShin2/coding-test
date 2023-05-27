import heapq as h

def solution(n):
    
    cnt = 0
    q = []
    h.heappush(q,'4')
    h.heappush(q,'13')
    l = []
    
    while True:
        if cnt >= n:
            break
        
        num = h.heappop(q)
        if num+'4' not in q:
            h.heappush(q,num+'4')
        if num+'13' not in q:
            h.heappush(q,num+'13')
        l.append(int(num))
        cnt += 1
    
    return l[n-1]
    
n=5000
print(solution(n))
