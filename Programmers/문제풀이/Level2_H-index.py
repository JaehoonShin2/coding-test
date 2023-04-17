from collections import Counter

def solution(citations):
    answer = 0
    
    # 10000번 이상 인용
    # => 10000편 이상이어야 한다
    # h의 최대값은 1000
    # 왜냐하면 논문의 최대값이 1000이기 때문
    counter_cit = Counter(citations)
    sort_cit = sorted(counter_cit.items(), key= lambda x: x[0]  ,reverse=True)

    for i in range(1000, 0, -1):
        temp_h = 0
        for idx, node in sort_cit:
            if idx >= i:
                temp_h += node
            else:
                break
        
        if temp_h >= i:
            answer = i
            break
        

    return answer

citations = [3, 0, 6, 1, 5]

print(solution(citations))

def solution_2(citations):
    # 인용 횟수를 내림차순으로 정렬
    sorted_cit = sorted(citations, reverse=True)
    # idx == h 이상의 인용된 논문
    # value == h
    
    answer = max(map(min, enumerate(sorted_cit, start=1)))
    
    return answer

print(solution_2(citations))
    
    
    

