def solution(s):
    
    answer = ''
    idx = 0
    for node in s:
        if node == ' ':
            idx = 0
            answer += node
        else:
            if idx%2 == 0:
                answer += node.upper()
            else:
                answer += node.lower()
            idx += 1
    
    return answer
    
    
s="try hello world"
print(solution(s))