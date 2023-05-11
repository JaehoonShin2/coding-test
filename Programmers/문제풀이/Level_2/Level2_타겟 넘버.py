from collections import deque

# def solution(numbers, target):
        
#     list = [0]
#     for idx, number in enumerate(numbers):
        
#         q = deque()
#         for n in list: 
#             q.append(n) 

#         list = []
#         while q:
#             num = q.popleft()
#             list.append(num + number)
#             list.append(num - number)
        
#         if idx == (len(numbers)-1):
#             return list.count(target)

def solution(numbers, target):
    answer = 0
    q = deque()
    
    # (current_sum, idx) 를 tuple 로 담기
    q.append((0, 0))
    
    while q:
        current_sum, idx = q.popleft()
        
        # 모든 값을 다 더했을 시점에서 q에 담긴 target 값의 갯수를 세기
        if idx == len(numbers):
            if current_sum == target:
                answer += 1
        
        else:
            q.append((current_sum+numbers[idx], idx+1))
            q.append((current_sum-numbers[idx], idx+1))
            
    return answer
        

numbers	=[1, 1, 1, 1, 1]
target=3

print(solution(numbers, target))
    
            