import heapq

def solution(k, score):
    answer = []
    
    q = []
    for i in score:
        # q 의 갯수가 k보다 적다면, q에 넣고 최소값을 answer에 반영
        heapq.heappush(q, i)
        if len(q) > k:
            heapq.heappop(q)
        answer.append(q[0])
        
    return answer