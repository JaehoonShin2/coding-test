from collections import deque

steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(i, j, row, col, v, visited):
        size = 1
        q = deque()
        q.append([i,j])
        while q:
            x, y = q.popleft()
            print(x, y)
            if v[x][y] == 0:
                return size
            
            for step in steps:
                nx = x + step[0]
                ny = y + step[1]
                
                if 0 <= nx < row and 0 <= ny < col:
                    if v[nx][ny] == 1 and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                        size += 1

        return size
    
def solution(v):

    answer = 0
    max_size = 0
    
    if not v: return [0,0]
    
    row = len(v)
    col = len(v[0])
    visited = [[0] * col for _ in range(row)]
        
    for i in range(row):
        for j in range(col):
            if visited[i][j] == 0 and v[i][j] == 1:
                visited[i][j] = 1
                max_size = max(max_size, bfs(i, j, row, col, v, visited))
                print('----')
                answer += 1
    
    return [answer, max_size]


v=[[1,1,0,1,1],[0,1,1,0,0],[0,0,0,0,0],
   [1,1,0,1,1],[1,0,1,1,1],[1,0,1,1,1]]

# v=[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],
#    [1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

# v=[[1,1,1,0,1,0,1], 
#    [1,0,0,0,1,0,0]]

print(solution(v))