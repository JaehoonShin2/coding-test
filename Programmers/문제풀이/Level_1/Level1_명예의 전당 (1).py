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

k, score = 4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]

if __name__ == "__main__":
    print(solution(k, score))