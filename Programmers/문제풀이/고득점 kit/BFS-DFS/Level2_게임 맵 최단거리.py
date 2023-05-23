from collections import deque

def solution(maps):
    
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    n = len(maps)
    m = len(maps[0])
    
    q = deque()
    q.append([0, 0])
    
    while q:
        x, y = q.popleft()
        
        for k in move:
            nx = x + k[0]
            ny = y + k[1]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1:
                    maps[nx][ny] += maps[x][y]
                    if nx == n-1 and ny == m-1:
                        return maps[n-1][m-1]
                    q.append([nx, ny])
    
    return -1

maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))