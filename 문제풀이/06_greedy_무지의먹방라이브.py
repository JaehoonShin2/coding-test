import heapq

def solution(food_times, k):

    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1)) #우선순위 큐에 음식의 시간과 음식 번호 순으로 입력

    sum_val = 0 #먹기 위해 사용한 시간
    prev = 0 #직전에 다 먹은 음식 시간 
    length = len(food_times) #남은 음색의 갯수

    while sum_val + ( (q[0][0] - prev) * length) <= k:
        now = heapq.heappop(q)[0] #우선순위 큐에 담긴 q 중에서 음싣의 시간 값을 now로 저장
        sum_val = (now - prev) * length
        length -= 1
        prev = now
    
    result = sorted(q, key=lambda x:x[1])
    return result[k-sum_val % length][1]