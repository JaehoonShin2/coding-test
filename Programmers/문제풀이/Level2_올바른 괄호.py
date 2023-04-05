def solution(s):
    
    answer = True

    # 처음으로 들어오는 값은 '(' 이어야 한다.
    # ')' 값이 들어올 경우 큐 안에 '(' 값이 존재해야 한다.
    # 마지막 값은 반드시 ')' 이어야만 한다.
    o = 0
    for i in s:
        if o < 0:
            return False
        
        if i == '(':
            o += 1
        elif i == ')':
            o -= 1

    if o == 0: 
        return True
    else: 
        return False
    
def solution(s):
    
    answer = True

    # 처음으로 들어오는 값은 '(' 이어야 한다.
    # ')' 값이 들어올 경우 큐 안에 '(' 값이 존재해야 한다.
    # 마지막 값은 반드시 ')' 이어야만 한다.
    o = 0
    for i in s:
        if o < 0:
            return False
        else:
            o =  o + 1 if i == '(' else o - 1

    return True if o == 0 else False