def solution(s):
    
    if len(s) % 2 == 1: return 0
    
    # 1000000개 => 시간복잡도 상 1개의 for 문
    stack = [s[0]]
    for v in s[1:]:
        stack.pop() if len(stack) > 0 and v == stack[-1] else stack.append(v)
    
    return 1 if len(stack) == 0 else 0
    
    
print(solution('cdcd'))