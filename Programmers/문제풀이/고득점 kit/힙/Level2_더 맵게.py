import heapq

def solution(scoville, K):
    answer = 0
    q = []
    
    for item in scoville:
        heapq.heappush(q, item)

    while q:
        first_q = heapq.heappop(q)
        if first_q >= K:
            break
        else:
            second_q = heapq.heappop(q)
            first_q = first_q + (second_q * 2)
            if not q and first_q < K:
                return -1
            heapq.heappush(q, first_q)
            answer += 1
            
            
    # 섞은 음식의 스코빌 지수 
    # = 가장 맵지 않은 음식의 스코빌 지수 
    # + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    
    return answer


scoville=[1, 2, 3, 9, 10, 12]	
K=7

print(solution(scoville, K))