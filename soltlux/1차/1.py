def solution(waiting):
    answer = []
    
    # for node in waiting:
    #     if node not in answer:
    #         answer.append(node)
            
    result = dict.fromkeys(waiting)
  
    return list(result)

waiting=[1,5,8,2,10,5,4,6,4,8]

print(solution(waiting))