def solution(d, budget):
    answer = 0
    d.sort()
    for b in d:
        if budget - b >= 0:
            budget -= b
            answer += 1
        else:
            break
            
    return answer

d, budget = [1,3,2,5,4], 9

print(solution(d, budget))