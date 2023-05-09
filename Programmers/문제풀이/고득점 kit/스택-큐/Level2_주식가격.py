def solution(prices):
    answer = []

# range는 iterator 등을 호출하여 메모리에 적재하지 않고 순회
# for i in prices 같은 경우 새로운 공간을 만들어서 할당
# 그래서 range를 이용한 구문이 속도면에서 더 빠름
 
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
                
        answer.append(cnt)
        
    return answer

prices=[1, 2, 3, 2, 3]


def solution2(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        
        while stack != [] and  \
            stack[-1][1] > prices[i]:
            print(stack[-1][1])
            past, _ = stack.pop()
            answer[past] = i - past
            
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer

print(solution2(prices))