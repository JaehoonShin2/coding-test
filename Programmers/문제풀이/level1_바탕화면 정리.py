def solution(wallpaper):

    start_row, start_col, end_row , end_col = 50,50,0,0
    
    for row_idx, row in enumerate(wallpaper):
        for col_idx, col in enumerate(row):
            if wallpaper[row_idx][col_idx] == '#':
                
                if start_col > col_idx:
                    start_col = col_idx
                
                if end_col < col_idx + 1:
                    end_col = col_idx + 1
                
                if start_row > row_idx:
                    start_row = row_idx
                
                if end_row < row_idx + 1:
                    end_row = row_idx + 1
                
                print(row_idx, col_idx)
    
    
    answer = [start_row, start_col, end_row , end_col]
    
    return answer


wallpaper1 = [".#...", "..#..", "...#."]
wallpaper2 = ["..........", ".....#....", "......##..", "...##.....", "....#....."]

print(solution(wallpaper2))