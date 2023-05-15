def solution(name):

	# 조이스틱 조작 횟수 
    answer = 0
    
    # 문장의 총 길이
    l = len(name)
    
    # 횡 이동에 대한 초기화 값
    min_width_move = l - 1
    
    for i, char in enumerate(name):
        
        # 문자 하나 당 상 or 하 운동의 최소값을 answer 에 추가
        answer += min(ord(char)-ord('A'), ord('Z')-ord(char)+1)
        
        # 현재의 인덱스를 기준으로 반복되는 A의 여부를 확인
        # 만약 A가 반복된다면 A를 거치는 이동을 하는 것이 최소값인지 아닌지 구분하기 위함
        
        # next 는 현재 인덱스에서의 다음 문자를 의미
        next = i + 1
        # next 가 전체 문자열의 길이보다는 작으면서 다음 next(index) 의 값이 A 일 경우
        while next < l and name[next] == 'A':
            next += 1
        
        # 1) 기존의 최소 수평이동 값 == min_width_move
        # 2) A를 기준으로 왼쪽를 왕복하고 오른쪽으로 가는 값
        # 3) A를 기준으로 오른쪽을 왕복하고 왼쪽으로 가는 값 중
        # 3가지 경우의 수 중에서 최소값을 찾아 min_width_move 에 대입
        
        min_width_move = min(min_width_move, 
                             (i * 2) + l - next,
                             i + (2 * (l - next))
                             )        
    
    return answer + min_width_move


name="JAN"
print(solution(name))