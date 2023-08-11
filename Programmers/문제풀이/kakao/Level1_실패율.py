
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

from collections import Counter

def solution(N, stages):
    
    c = Counter(stages)
    stage_failure_rate = {}
    
    for i in range(1, N+1):
        stage_player = sum(v for k, v in c.items() if k >= i)
        print(f"i : {i}, 미클리어 인원 : {c[i]}, 스테이지에 들어온 인원 : {stage_player}")
        if stage_player > 0:
            stage_failure_rate[i] = c[i]/stage_player
        else:
            stage_failure_rate[i] = 0
    
    answer = sorted(stage_failure_rate, key=lambda x:stage_failure_rate[x], reverse=True)
    return answer

# N, stage = 5, [2, 1, 2, 6, 2, 4, 3, 3]
N, stage = 4, [4,4,4,4,4]

if __name__ == "__main__":
    print(solution(N, stage))