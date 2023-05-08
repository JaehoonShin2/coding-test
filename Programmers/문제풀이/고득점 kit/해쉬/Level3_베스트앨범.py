from collections import defaultdict as ad

def solution(genres, plays):
    
    answer = []
    d = ad(list)
    
    # 앨범의 종류를 key 로, value 에는 리스트로 횟수와 인덱스값을 튜플 형태로 담음
    for i in range(len(genres)):
        d[genres[i]].append((plays[i], i))
    
    # 하나의 key(앨범) 와 횟수의 총 합을 튜플 형태로 리스트에 담음
    l = []
    for k, v in d.items():
       l.append((k, sum(x[0] for x in v)))
    
    # 담긴 리스트에서 총합을 기준으로 내림차순 정렬
    l.sort(key= lambda x: x[1], reverse=True)

    # 리스트에서 한 개씩 뽑고
    for s in l:
        # 리스트의 앨범종류를 key로 맵의 value 를 꺼낸다
        m = d[s[0]]
        # 리스트에서 정렬을 하되, 튜플 중에서 횟수를 기준으로 내림차순 정렬을 함
        m.sort(key=lambda x: (-x[0], x[1]))
        
        for idx, v in enumerate(m):
        # 그 후 리스트에서 idx 2 이하, 즉 2개(혹은 1개)를 뽑은 뒤
            if idx < 2:
            # 튜플의 인덱스값을 answer 에 추가
                answer.append(v[1])
            else: 
                break
           
    return answer

genres=["classic", "pop", "classic", "classic", "pop"]	
plays=[500, 600, 150, 800, 2500]

print(solution(genres, plays))
