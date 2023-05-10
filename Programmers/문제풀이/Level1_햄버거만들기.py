def solution(ingredient):
    answer = 0
    temp = []
    
    for node in ingredient:
        temp.append(node)
        print('temp before : {}'.format(temp))
        if temp[-4:] == [1,2,3,1]:
            answer += 1
            del temp[-4:]
            print('temp after : {}'.format(temp))
    
    return answer
    


ingredient=[2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))