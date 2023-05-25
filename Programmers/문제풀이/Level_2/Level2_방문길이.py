def solution(dirs):
    
    visited = set()
    move = {'U':(-1, 0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
    r, c = 5, 5
    
    for dir in dirs:
        row, col = move[dir]
        nr, nc = r + row, c+col
        if 0 <= nr <= 10 and 0 <= nc <= 10:
            visited.add((r, c, nr, nc))
            visited.add((nr, nc, r, c))
            r, c = nr, nc
            
    return len(visited)//2

dirs="ULURRDLLU"
dirs="LULLLLLLU"
dirs="LULULULULU"
print(solution(dirs))