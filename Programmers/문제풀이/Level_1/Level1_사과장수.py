def solution(k, m, score):
    answer = 0
    cnt = len(score)//m
    # print(cnt)
    list = [[] for _ in range(cnt)]
    score_sort = sorted(score, reverse=True)
    # print(score_sort)
    a = 0
    for i in range(0, len(score_sort), m):
        if i+m <= len(score_sort):
            for j in range(i, i+m):
                list[a].append(score_sort[j])
            a += 1
    
    for node in list:
        answer += min(node) * m
        
    return answer

# k=4
# m=3	
# score=	[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]

k=3
m=4	
score=	[1, 2, 3, 1, 2, 3, 1]

print(solution(k, m, score))