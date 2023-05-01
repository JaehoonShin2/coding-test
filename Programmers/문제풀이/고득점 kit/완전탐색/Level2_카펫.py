# 브라운의 갯수를 2로 나눈 뒤에 가로 세로의 값을 구한다.
# 정사각형에서부터 가로로 긴 직사각형으로 변형시키면서 내부에 들어가는
# 옐로우 박스의 크기와 맞는지 확인하기.

def solution(brown, yellow):
    answer = []
    
    # row * col = brown + yellow
    #           = brown + (row - 2) * (col -2)
    #           = brown + row*col -2(row+col) + 4
    # row + col = (brown + 4) / 2    
    
    sum_row_col = ( brown + 4 ) // 2
    
    # 초기 값으로 열은 무조건 3 이상이어야 함
    row, col = sum_row_col - 3, 3
    
    for i in range(1, brown):
    
        predict_yellow = (row-2)*(col-2)
    
        if predict_yellow == yellow: 
            break
    
        row -= 1
        col += 1
    answer.append(row)
    answer.append(col)
    
    return answer

print(solution(24, 24))