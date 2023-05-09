import heapq

def solution(jobs):
    q = []
    n = len(jobs)
    current_time = 0  # 현재 시간
    total_time = 0  # 작업 소요시간의 총합
    
    jobs.sort(key=lambda x: x[0])
    
    # 전체 다 탐색해야 하기 때문에, 두 개의 리스트가 모두 빈 값이 되기 전까지는 반복
    while jobs or q:
        
        # 현재 거리보다 jobs 의 거리가 같거나 작다면, 해당 거리만큼 이동한 후, 현재거리를 변경. 이것을 반복
        while jobs and current_time >= jobs[0][0]:
            start, time = jobs.pop(0)
            heapq.heappush(q, (time, start))
        
        # while 에서 탈출 => jobs 가 모두 pop 되었거나 혹은 현재 거리가 jobs[0] 의 거리보다 작을 때
        # q이 비어있지 않으면, 가장 소요시간이 짧은 작업부터 처리
        if q:
            time, start = heapq.heappop(q)
            current_time += time
            total_time += current_time - start
            
        # q이 비어있다면, 다음 작업의 시작시간으로 시간을 이동
        else:
            current_time = jobs[0][0]
    
    return total_time // n        



# jobs=[[1, 9], [0, 3], [2, 6]]
# jobs=[[0, 9], [1, 1], [1, 1], [1, 1], [1, 1]]
jobs=[[0, 3], [1, 9], [500, 6]]
print(solution(jobs))
