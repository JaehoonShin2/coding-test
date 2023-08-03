def solution(t, p):
    answer = 0
    
    # 부분문자열의 제한 길이
    l = len(p)
    
    sub = ""
    for i in range(len(t)):
        # 만약 sub 의 길이가 l보다 작다면 추가
        if len(sub) < l:
            sub += t[i]
        # 만약 길이가 동일하다면 우선 크기 비교를 한 뒤 앞자리를 팝하기
        if len(sub) == l:
            if sub <= p:
                answer += 1
            sub = sub[1:]
    
    return answer