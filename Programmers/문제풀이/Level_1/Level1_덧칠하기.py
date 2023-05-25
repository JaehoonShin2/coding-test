def solution(n, m, section):
    answer = 1
    start = section[0]
    for i in range(1, len(section)):
        if section[i] - start + 1 > m:
            start = section[i]
            answer += 1
    
    return answer

n, m, section=4,1,[1, 2, 3, 4]
print(solution(n, m, section))