import heapq as h

def solution(n):
    
    cnt = 0
    q = [4, 13]
    l = []
    
    while cnt < n:
        
        num = h.heappop(q)
        print('heapq 의 num : {}'.format(num))
        nw = int(str(num)+'4')
        if nw not in q:
            print(nw)
            h.heappush(q, nw)
        nw = int(str(num)+'13')
        if nw not in q:
            print(nw)
            h.heappush(q, nw)
        l.append(int(num))
        cnt += 1
        print('q의 변경 이후 상태값 : {}'.format(q))
            
    print(l)
    return l[n-1]
    
n=3
print(solution(n))
