from collections import *

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    field = [[-1] * 102 for i in range(102)]
    # field = [[5] * 22 for _ in range(22)]
    # 직사각형 그리기
    for r in rectangle:
        # 모든 좌표값 2배
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        # x1부터 x2, y1부터 y2까지 순회
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                # x1, x2, y1, y2는 테두리이므로 제외하고 내부만 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                # 다른 직사각형의 내부가 아니면서 테두리일 때 1로 채움
                elif field[i][j] != 0:
                    field[i][j] = 1
            
    
    for m in field:
        print(m, end=" ")
        print()

    
    q = deque()
    q.append([characterX * 2, characterY * 2])
    
    move = [[-1,0], [1,0], [0,-1], [0, 1]]
    visited = [[1] * 102 for i in range(102)]
    
    while q:
        x, y = q.popleft()
        if x == itemX * 2 and y == itemY * 2 :
            answer = visited[x][y] //2
            return answer
        
        for m in move:
            nx = x + m[0]
            ny = y + m[1]
           # 현재 좌표가 테두리이고 아직 방문하지 않은 곳이라면 q에 추가 후 visited 최단거리로 갱신
            if field[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
    print()

    
    return answer


rectangle, characterX, characterY, itemX, itemY = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3,7, 8

print(solution(rectangle, characterX, characterY, itemX, itemY))
