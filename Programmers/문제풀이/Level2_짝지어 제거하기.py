def solution(s):
    
    if len(s) % 2 == 1: return 0
    
    # 1000000개 => 시간복잡도 상 1개의 for 문
    
    stack = [s[0]]
    for v in s[1:]:
        if len(stack) > 0 and v == stack[-1]:
            stack.pop()
        else:
            stack.append(v)
    
    if len(stack) == 0:
        return 1
    else: return 0
    
    
print(solution('cdcd'))