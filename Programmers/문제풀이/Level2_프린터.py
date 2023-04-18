from collections import deque

# def solution(priorities, location):
    
#     p = []
#     answer = 1
    
#     for idx, value in enumerate(priorities):
#         if idx == location:
#             p.append((value, True))
#         else:
#             p.append((value, False))
    
#     while p:
#         # print('최대값 : {}'.format(max(p)[0]))
#         max_num = max(p)[0]
#         num = p.pop(0)
        
#         # pop 한 뒤 최대값이라면
#         if max_num == num[0]:
#             # 만약 true 일 때는 answer 리턴
#             if num[1]:
#                 return answer
#             # 최대값인데 false 라면 answer += 1
#             else:
#                 answer += 1
#         # 최대값이 아니라면
#         else:
#             p.append(num)

def solution(priorities, location):
    
    # 기존 리스트에 있던 내용들의 key-value 를 tuple 형태로 새롭게 q에 담기
    q = deque([ (k, v) for k, v in enumerate(priorities)])
    ans = 0
    
    while q:
        value = q.popleft()
        
        # any : 하나라도 참이라면 True 리턴
        # q의 가장 왼쪽에서 뽑은 튜플의 값이
        # 전체 q에 들어 있는 노드를 반복돌면서 각 튜플의 값보다 하나라도 크면
        # pop 으로 뽑은 값을 다시 q 에 넣는다.
        if any( value[1] < item[1] for item in q):
            q.append(value)
        
        else:
            ans += 1
            if value[0] == location:
                return ans
    
    
priorities=[2, 1, 3, 2]
location= 2

print(solution(priorities, location))


    
    