def solution(priorities, location):
    
    p = []
    answer = 1
    
    for idx, value in enumerate(priorities):
        if idx == location:
            p.append((value, True))
        else:
            p.append((value, False))
    
    while p:
        # print('최대값 : {}'.format(max(p)[0]))
        max_num = max(p)[0]
        num = p.pop(0)
        
        # pop 한 뒤 최대값이라면
        if max_num == num[0]:
            # 만약 true 일 때는 answer 리턴
            if num[1]:
                return answer
            # 최대값인데 false 라면 answer += 1
            else:
                answer += 1
        # 최대값이 아니라면
        else:
            p.append(num)

priorities=[2, 1, 3, 2]
location= 2

print(solution(priorities, location))