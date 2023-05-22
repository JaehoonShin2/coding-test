# def solution(numbers):
#     d = dict()
#     a =  dict()
#     for idx, node in enumerate(numbers):
#         d[idx] = node

#     for i in range(len(d)-1):
#         for j in range(i+1, len(d)):
#             s = d[i] + d[j]
#             a[s] = 0
    
#     l = list(dict.fromkeys(a))
#     l.sort(key=lambda x: x) 
#     return [k for k in l]
from itertools import combinations as c

def solution(numbers):
    answer = []
    l = list(c(numbers, 2))
    
    for i in l:
        answer.append(i[0] + i[1])
    answer = list(set(answer))
    answer.sort()

    return answer

numbers=[2,1,3,4,1]
print(solution(numbers))