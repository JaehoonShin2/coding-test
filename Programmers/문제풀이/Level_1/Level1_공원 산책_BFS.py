from collections import deque

def solution(park, routes):
    
    # 주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
    # 주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
    # 위 두 가지중 어느 하나라도 해당된다면, 로봇 강아지는 해당 명령을 무시하고 다음 명령을 수행합니다.
    
    row, col = 0, 0
    max_row, max_col = len(park), len(park[0])
    for i in range(max_row):
        for j in range(max_col):
            if park[i][j] == 'S':
                row, col = i, j

    # print(row, col)
    
    q = deque()
    
    for route in routes:
        locate, num = route.split(' ')
        n = int(num)
        q.append([locate, n])
    
    while q:
        locate, n = q.popleft()
        print(locate, n)

        # 현재의 위치에서 n을 더하거나 뺀 값이 0~len 사이
        if (locate == 'E' ) & (col+n < max_col):
            
            if park[row][col+n] != 'X':
                col += n
        
        if (locate == 'W') & (col-n >= 0):
            if park[row][col-n] != 'X':
                col -= n
            
        if (locate == 'N') & (row-n >= 0):
            if park[row-n][col] != 'X':
                row -= n
            
        if (locate == 'S') & (row+n < max_row): 
            if park[row+n][col] != 'X':
                row += n            

        i = 0
        print('{}번째 실행'.format(i), row, col)
        i += 1
         
    answer = [row, col]

    
    return answer

park1 = ["SOO","OOO","OOO"]
routes1 = ["E 2","S 2","W 1"]
park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]


print(solution(park, routes))