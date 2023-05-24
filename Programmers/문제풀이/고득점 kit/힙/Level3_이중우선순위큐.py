import heapq

def solution(operations):

    hq = []
    
    for operation in operations:
        order, n = operation.split(' ')
        num = int(n)
        if order == 'I':
            heapq.heappush(hq, num)
        else:
            if hq:
                if num < 0:
                    heapq.heappop(hq)
                elif num > 0:
                    hq.remove(max(hq))
                    heapq.heapify(hq)
        
    if not hq:
        return [0, 0]
    else:
        # 의도 : 최소값
        pop_num = heapq.heappop(hq)
        if hq:
            return [max(hq), pop_num]
        else:
            if pop_num >= 0:
                return [pop_num, 0]
            else:
                return [0, pop_num]
    
operations=["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
# operations=["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
operations=["I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1", "I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1"]
print(solution(operations))