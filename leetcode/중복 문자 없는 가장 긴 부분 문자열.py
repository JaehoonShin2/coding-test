def solution(s):
    
    # 문자열의 인덱스값을 담을 map
    map = dict()
    # 맥스 길이
    max_length = 0
    # 시작 인덱스
    start = 0
    for idx, str in enumerate(s):
        # 만약 map 에 현재 문자열이 존재하고, 시작 인덱스가 현재 문자열의 값보다 작을 경우
        if str in map and start <= map[str]:
            start = map[str]+1
        else:   
            max_length = max(max_length, idx+1-start)
        map[str] = idx
    
    return max_length

s="abcabcbb"
s="ntmttmmzuxt"
print(solution(s))