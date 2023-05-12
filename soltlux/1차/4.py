def solution(s):
    answer = 0
    stack = []
    for node in s:
        if node == 'z' or node == 'a':
            stack.append(node)
            if len(stack) > 1:
                if stack[-1] == 'z' and stack[-2] == 'a':
                    stack.pop(-2)
                    answer += 1
                elif stack[-1] == 'a' and stack[-2] == 'z':
                    stack.pop(-2)
                    answer += 1
    
    return answer

s="zabzczxa"
print(solution(s))