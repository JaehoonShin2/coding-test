def solution(park, routes):
    
    # 주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
    # 주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
    # 위 두 가지중 어느 하나라도 해당된다면, 로봇 강아지는 해당 명령을 무시하고 다음 명령을 수행합니다.
    
    answer = []
    
    arr_map = []
    h = 0
    w = 0
    row, col = len(park), len(park[0])
                
    for i in range(row):
        for j in range(len(park[i])):
            arr_map.append(park[i][j])
            if park[i][j] == 'S':
                w = j
                h = i

    # w = 가로
    # h = 세로
    
    for route in routes:
        op, nn = route.split(' ')
        n = int(nn)
        
        isContinue = True
        if (op == 'W') & (w-n >= 0):
            for node in range(w-n, w+1):
                if park[h][node] == 'X':
                    isContinue = False
            
            if isContinue:
                w -= n
        
        if (op == 'E') & (w+n < col):
            for node in range(w, w+n+1):
                if park[h][node] == 'X':
                    isContinue = False
            
            if isContinue:
                w += n
                
        
        if (op == 'S') & (h+n < row):
            for node in range(h, h+n+1):
                if park[node][w] == 'X':
                    isContinue = False
            
            if isContinue:
                h += n
        
        if (op == 'N') & (h-n >= 0):
            for node in range(h-n, h+1):
                if park[node][w] == 'X':
                    isContinue = False
            
            if isContinue:
                h -= n
                
    answer.append(h)
    answer.append(w)
    
    return answer

park1 = ["SOO","OOO","OOO"]
routes1 = ["E 2","S 2","W 1"]
park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]


print(solution(park, routes))