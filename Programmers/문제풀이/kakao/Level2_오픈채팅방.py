# 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태

def solution(record):
    
    name_dict = dict()
    answer = []
    for r in record:
        rr = r.split(' ')
        if rr[0] != 'Leave':
            name_dict[rr[1]] = rr[2]
    
    for r in record:
        rr = r.split(' ')
        if rr[0] == 'Enter':
            answer.append(name_dict[rr[1]] + '님이 들어왔습니다.')    
        elif rr[0] == 'Leave':
            answer.append(name_dict[rr[1]] + '님이 나갔습니다.')    
    
    return answer

record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))