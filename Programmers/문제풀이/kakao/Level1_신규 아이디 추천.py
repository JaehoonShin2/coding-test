def solution(new_id):
    
    new_id = new_id.lower()
    e_str = ['!', '@', '#', '$', '%', '^', '&', 
             '*', '(', ')', '=', '+', '[',
             '{', ']', '}', ':', '?', ',', '<', '>', '/']
    
    '[-_.~!@#$%^&*()=+[{]}:?,<>/]'
    
    # 특수문자 제거
    for e in e_str:
        if e in new_id:
            new_id = new_id.replace(e, '')

    # . 을 기준으로 나눈 뒤, 한 개의 .만 남기기
    id = ''
    string = new_id.split('.')
    for idx, s in enumerate(string):
        if s != '':
            if idx == 0:
                id += s
            else:
                id = id + '.' + s
    
    # 만약 id 가 빈값이 아니라면, 
    # 
    if id != '':
        if id[0] == '.':
            id = id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
        new_id = id
    else:
        new_id = 'a'
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[14] == '.':
            new_id = new_id[:14]
    
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id = new_id + new_id[-1]
    
    answer = new_id
    
    return answer

# new_id="...!@BaT#*..y.abcdefghijklm"
# new_id="z-+.^."
new_id="abcdefghijklmn.p"
new_id="123_.def"
new_id="=.="
print(solution(new_id))