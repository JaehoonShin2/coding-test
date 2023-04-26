from collections import deque

keypad = [[1,2,3], [4,5,6], [7,8,9], ['*',0,'#']]
move = [(0,1), (0, -1), (1, 0), (-1, 0)]
    
def bfs(number, current):

    current_row, current_col = 0, 0
    
    for r in range(4):
        for c in range(3):
            if keypad[r][c] == current:
                current_row, current_col = r, c
    
    q = deque()
    q.append((current_row, current_col))
    visited = [[0] * 3 for _ in range(4)]
    while q:
        row, col = q.popleft()
        
        if keypad[row][col] == number:
            return visited[row][col]
        
        for m in move:
            nrow, ncol = row + m[0], col + m[1]
            # 0 에서 로우&컬럼 사이의 값 중에서
            if nrow >= 0 and nrow < 4 and ncol >= 0 and ncol < 3:
                # 미방문한 노드 중에서
                if not visited[nrow][ncol]:
                    visited[nrow][ncol] = visited[row][col] + 1
                    if keypad[nrow][ncol] == number:
                        return visited[nrow][ncol]
                    else:
                        q.append((nrow, ncol))

def solution(numbers, hand):
    
    answer = ''
    l, r = '*', '#'
                        
    for number in numbers:

        if number in [1,4,7]:
            l = number
            answer += 'L'
        elif number in [3,6,9]:
            r = number
            answer += 'R'
        else:
            l_dist = bfs(number, l)
            r_dist = bfs(number, r)
            
            if l_dist < r_dist :
                l = number
                answer += 'L'
            elif l_dist > r_dist :
                r = number
                answer += 'R'
            else :
                if hand == 'right' :
                    r = number
                    answer += 'R'
                else :
                    l = number
                    answer += 'L'
                    
    return answer

                    

# numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand= "right"

numbers=[4, 3, 2, 8]
hand= "right"
    
print(solution(numbers, hand))


