def solution(numbers):
    # answer = []
    result = [-1] * len(numbers)
    stack = []
    l = len(numbers)
    # 스택을 활용해서 numbers 의 가장 오른쪽 값부터 역순으로 뽑아서 비교
    for i in range(l - 1, -1, -1):
        while True:
            # 만약 스택에 값이 없다면, answer 에는 -1를 추가하고
            # 현재에는 numbers[i] 를 추가
            if not stack:
                # answer.append(-1)
                stack.append(numbers[i])
                break
            else:
                # 만약 스택의 가장 마지막 값
                # == 현재 nubmers[i]를 기준으로 오른쪽에 있는 값 
                # 중에서 현재 numbers[i]보다 값이 크다면
                # answer 에 스택의 마지막 값을 추가해준 뒤
                # stack 에는 현재 nubmers[i] 를 추가
                if stack[-1] > numbers[i]:
                    # answer.append(stack[-1])
                    result[i] = stack[-1]
                    stack.append(numbers[i])
                    break
                # 반면에 스택의 가장 마지막 값이 numbers[i]보다 같거나 작다면
                # 스택에서 해당 값을 제거
                else:
                    stack.pop()
    
    # reverse 를 통해 뒤집는 연산을 하는 것 보다 
    # 차라리 처음부터 해당 갯수 만큼의 리스트를 만든 뒤,
    # 값의 변동이 있을 때마다 변동을 주는 것이 좋다.
    # answer.reverse()         
    # return answer
    return result


numbers = [9, 1, 5, 3, 6, 2]
print(solution(numbers))
