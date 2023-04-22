from itertools import permutations as ps

def solution(k, dungeons):
    answer = 0

    d_l = len(dungeons)
    for p in ps(range(d_l)):
        print('p : {}'.format(p))
        tk = k
        for idx, v in enumerate(p):
            
            if tk < dungeons[idx][0]:
                answer = max(answer, idx)
                break
            
            tk -= dungeons[v][1]
            
        else: 
            return d_l
            
    return answer
    

k=80
dungeons=[[80,20],[50,40],[30,10]]

print(solution(k, dungeons))