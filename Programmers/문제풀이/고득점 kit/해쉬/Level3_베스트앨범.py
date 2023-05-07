from collections import defaultdict as ad

def solution(genres, plays):
    answer = []
    
    d = ad(list)
    
    for i in range(len(genres)):
        d[genres[i]].append((plays[i], i))
    
    l = []
    for k, v in d.items():
       l.append((k, sum(v[0])))
    
    l.sort(key= lambda x: x[1], reverse=True)

    for s in l:
        m = d[s[0]]
        m.sort(reverse=True)
        print(m)
        for idx, v in enumerate(m):
            if idx < 2:
                answer.append(v[1])
            else: 
                break
           
    return answer

genres=["classic", "pop", "classic", "classic", "pop"]	
plays=[500, 600, 150, 800, 2500]

print(solution(genres, plays))
