def solution(board, moves):
    
    answer = 0
    result = []
    
    for move in moves:
        for b in board:
            if b[move-1] != 0:
                # 리스트가 빈 값일 경우(최초 인덱스값일 수도 있고, 있던 값을 빼면서 빈값이 되었을 수도 있고)
                if not result:
                    result.append(b[move-1])
                # 리스트의 직전 값과 move 로 꺼낸 인형 값이 같을 경우
                elif result[-1] == b[move-1]:
                    result = result[:-1]
                    answer += 2
                # 그 외의, 아무 관련성이 없는 경우
                else :
                    result.append(b[move-1])
                b[move-1] = 0
                break
            
    return answer

board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]

print(solution(board, moves))