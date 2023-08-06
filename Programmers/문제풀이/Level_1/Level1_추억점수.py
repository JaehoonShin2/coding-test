def solution(name, yearning, photo):
    answer = []
    
    # name 을 키로, 그리움 점수를 value 로 가지는 dictionary 를 만들고, key로 찾기.
    map = dict(zip(name, yearning))
    for p in photo:
        answer.append(sum(map.get(pp) for pp in p if map.get(pp) != None))
    return answer

name, yearning, photo = ["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
print(solution(name, yearning, photo))