# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 
# 소수가 되는 경우의 개수
from itertools import combinations

def solution(nums):
    
    answer = 0
    c = [sum(node) for node in combinations(nums, 3)]
    
    for num in c:
        isCheck = False
        for i in range(2, num//2+1):
            if num%i == 0:
                isCheck = True
                break
        if not isCheck:
            answer += 1
        
    return answer

nums=[1,2,7,6,4]
print(solution(nums))