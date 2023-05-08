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

print(solution(prices))