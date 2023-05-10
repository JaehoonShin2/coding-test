def solution(array, commands):
    
    answer = []
    
    while commands:
        start, end, k = commands.pop(0)
        new_array = array[start-1:end]
        new_array.sort()
        answer.append(new_array[k-1])
        
    return answer


array=[1, 5, 2, 6, 3, 7, 4]	
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))