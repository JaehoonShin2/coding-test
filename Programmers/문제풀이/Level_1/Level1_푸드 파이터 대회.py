def solution(food):
    answer = ['0']
    for i in reversed(range(len(food))):
        f = food[i] // 2
        if f > 0:
            new_f = f * str(i)
            answer.insert(0, new_f)
            answer.append(new_f)
        
    return ''.join(answer)
    
food =[1, 7, 1, 2]
print(solution(food))