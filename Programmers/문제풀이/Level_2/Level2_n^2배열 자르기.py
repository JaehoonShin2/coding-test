def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        row = i // n  # 현재 위치의 숫자가 몇 번째 행에 속하는지 계산
        col = i % n   # 현재 위치의 숫자가 행 내에서 몇 번째 열에 속하는지 계산
        num = max(row, col) + 1  # 행과 열 중 큰 값에 1을 더한 것이 현재 위치의 숫자
        answer.append(num)
    return answer

n, left, right = 3, 2, 5
n, left, right = 4,7,14	
print(solution(n, left, right))