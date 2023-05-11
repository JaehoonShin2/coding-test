def solution(ingredient):
    answer = 0
    temp = []
    for node in ingredient:
        temp.append(node)
        if temp[-4:] == [1,2,3,1]:
            answer += 1
            del temp[-4:]
    
    return answer
    


ingredient=[2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))