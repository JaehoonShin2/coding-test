from collections import deque

def solution1(n):
    answer = 0
    
    moves = [1, 2]
    
    q = deque()
    q.append(n)
    
    while q:
        num = q.popleft()
        
        
        for move in moves:
            if num - move >= 0:
                print('num 값 : {}, move값 : {}, 움직인 후의 값 : {}'.format(num, move, num-move))
        
                if num-move == 0:
                    answer = answer%1234567 + 1
                else:
                    q.append(num - move)
                
    return answer

def solution(n):
    
    dp = [0] * (n+1)
    
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    for i in range(1, n+1):
        print('dp[{}] = {}'.format(i, dp[i]))
    
    answer = dp[n]
    return answer

print(solution(8))