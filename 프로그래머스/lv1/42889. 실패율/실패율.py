from collections import Counter

def solution(N, stages):
    
    c = Counter(stages)
    stage_failure_rate = {}
    
    for i in range(1, N+1):
        stage_player = sum(v for k, v in c.items() if k >= i)
        if stage_player > 0:
            stage_failure_rate[i] = c[i]/stage_player
        else:
            stage_failure_rate[i] = 0
    
    answer = sorted(stage_failure_rate, key=lambda x:stage_failure_rate[x], reverse=True)
    return answer