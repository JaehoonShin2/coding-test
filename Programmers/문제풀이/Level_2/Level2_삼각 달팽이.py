def solution(n):
    answer = [[0] * (n+1) for i in range(n+1)]
    
    x, y = -1, 0 # 좌표 초기화 => 처음 시작은 아래로 내려가기 때문에 x = -1
    num = 1
 
    for i in range(n): # 방향
        for _ in range(i, n): # 좌표 구하기
            if i % 3 == 0: # 하
                x += 1
            elif i % 3 == 1: # 우
                y += 1
            else: # 상
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
    
    ans = []
    for a in answer:
        for b in a:
            if b != 0:
                ans.append(b)
                
    return ans
n=5
print(solution(n))