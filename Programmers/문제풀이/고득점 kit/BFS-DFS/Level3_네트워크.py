# def solution(n, computers):
#     temp = []
#     for i in range(n):
#         temp.append(i)
#     for i in range(n):
#         for j in range(n):
#             if computers[i][j]:
#                 for k in range(n):
#                     if temp[k] == temp[i]:
#                         print(temp[k], temp[i], temp[j])
#                         temp[k] = temp[j]
#     return len(set(temp))

from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [0] * n
    map = dict.fromkeys(range(n))
    for i in range(n):
        l = []
        for j in range(n):
            if i != j and computers[i][j] == 1:
                l.append(j)
            map[i] = l
    
    q = deque()
    
    for i in range(n):
        if visited[i] == 0:
            q.append(i)
            answer += 1
            while q:
                num = q.popleft()
                visited[num] = 1
                for nn in map[num]:
                    if visited[nn] != 1:
                        q.append(nn)
                
    return answer

n=3
computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(n, computers))