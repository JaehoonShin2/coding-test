

def solution(dartResult):
    
    answer = 0
    
    area = {"S":1, "D":2, "T":3}
    option = {'*':2, '#':-1}
    num_list = []
    
    for idx, dart in enumerate(dartResult):
        if dart in ['S', 'D', 'T']:
            current_num = int(dartResult[idx-1])
            current_area = dartResult[idx]
            num_list.append(pow(current_num, area[current_area]))

        elif dart in ['*','#']:
            num_list.append(dart)
    
    nnn = []
    aaa = []
    
    print(num_list)
    
    for idx in range(len(num_list)-1):
        if num_list[idx] in range(0, 11):
            nnn.append(num_list[idx])
            if num_list[idx+1] in ['*', '#']:
                aaa.append(num_list[idx+1])
            else:
                aaa.append('')
    
    print(nnn)
    print(aaa)   
    
    
    return answer


dartResult="1D#2S*3S"
# dartResult="1T2D3D#"
print(solution(dartResult))