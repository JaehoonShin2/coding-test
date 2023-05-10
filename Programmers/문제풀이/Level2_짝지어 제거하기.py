def solution(s):
    
    # 전체 문자열의 갯수가 홀수라면 모두 제거할 수 없기 때문에 0 리턴
    if len(s) % 2 == 1: 
        return 0
    
    # 0번 인덱스 문자열을 스택에 담기
    stack = [s[0]]
    # 1번 인덱스 문자열부터 반복문 돌면서
    for v in s[1:]:
        # 만약 스택이 빈 값이 아니고, 스택의 가장 마지막 값과 현재의 문자열이 일치하면
        # 스택의 가장 마지막 값을 제거
        if len(stack) > 0 and v == stack[-1]:
            stack.pop()
        # 만약 일치하지 않는다면 스택에 추가
        else:
            stack.append(v)
    
    # 반복문 종료 후 스택이 빈 값이라면 1 리턴, 아니면 0 리턴
    if len(stack) == 0:
        return 1
    else: 
        return 0
    
print(solution('cdcd'))