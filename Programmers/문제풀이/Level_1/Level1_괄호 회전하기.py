from collections import deque

def check(s):
    # 스택 생성
    stack = []
    # s_q 만큼 반복을 돌기
    for k, v in enumerate(s):
        # 만약 k(index) 가 0 이 아니고, stack 에 빈 값이 아니라면
        if k != 0 and len(stack) > 0:
        # 스택의 마지막 값을 기준으로 괄호의 페어 확인
            if stack[-1] == '[' and v == ']':
                stack.pop()
            elif stack[-1] == '{' and v == '}':           
                stack.pop()
            elif stack[-1] == '(' and v == ')':
                stack.pop()
        # 페어가 안맞으면 스택에 추가
            else:
                stack.append(v)
        # k == 0 (초기값) 혹은 stack 이 빈 값이면 스택에 추가
        else:
            stack.append(v)
    return len(stack)


def solution(s):
    answer = 0
    
    # 문자열을 큐로 변환
    s_q = deque(s)
    
    # 리스트의 갯수만큼 반복을 돌면서
    for _ in range(len(s_q)):
        # 만약 짝이 안맞는게 0이라면 answer += 1
        if check(s_q) == 0:
            answer += 1
        # 큐의 가장 앞 요소를 pop 하고
        f = s_q.popleft()
        # 큐에 다시 추가
        s_q.append(f)
    return answer

s="}]()[{"
print(solution(s))