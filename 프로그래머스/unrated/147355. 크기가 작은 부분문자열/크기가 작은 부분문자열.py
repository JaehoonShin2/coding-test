def solution(t, p):
    answer = 0
    
    # 전체 문자열의 길이
    n = len(t)
    # 부분문자열의 길이
    k = len(p)

    # 반복문을 돌면서 t[i:i+k] 의 값이 p보다 작을 경우 answer에 1을 더한다.
    for i in range(n+1-k):
        if t[i:i+k] <= p:
            answer += 1
    
    return answer