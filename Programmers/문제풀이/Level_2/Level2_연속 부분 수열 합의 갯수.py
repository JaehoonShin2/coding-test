def solution(elements):
    
    answer = set()
    length = len(elements)
    for i in range(1, length+1):
        for j in range(1, length+1):
            sum_num = sum(elements[j:j+i])
            if j+i > length:
                k = j+i-length
                elements[0:k]
                sum_num += sum(elements[0:k])
            answer.add(sum_num)
    
    return len(answer)

elements = [7,9,1,1,4]

print(solution(elements))