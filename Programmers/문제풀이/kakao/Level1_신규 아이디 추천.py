def solution(new_id):
    
    # 1. 소문자치환
    new_id = new_id.lower()
    e_str = '-_.~!@#$%^&*()=+[{]}:?,<>/'
    avail_str = '-_.'
    remove_str = [x for x in e_str if x not in avail_str]
    # 2. 특정 특수문자 제거
    new_id = [x for x in new_id if x not in remove_str]
    # 3. .이 둘 이상 반복될 경우 제거
    temp = []
    for i in range(len(new_id)):
        temp.append(new_id[i])
        if i < 1:
            continue
        else:
            if temp[-1] == '.' and temp[-2] == '.':
                del temp[-1]
    new_id = temp     
    # 4. 처음 값이 . 이거나 마지막 값이 .일 경우 제거
    if new_id[0] == '.':
        new_id.pop(0)
    if len(new_id) ==  0:
        new_id.append('a')
    else:
        if new_id[-1] == '.':
            new_id.pop()
    # 5. 16 글자 이상일 경우 15글자로 쪼개고, 마지막이 . 이면 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id.pop()
    # 6. 2글자 이하일 경우, 마지막 글자를 3글자가 될 때까지 반복
    elif len(new_id) <= 2:
        while len(new_id) < 3:
            new_id.append(new_id[-1])
    return ''.join(new_id)
    

# new_id="...!@BaT#*..y.abcdefghijklm"
# new_id="z-+.^."
new_id="abcdefghijklmn.p"
new_id="123_.def"
new_id="=.="
print(solution(new_id))