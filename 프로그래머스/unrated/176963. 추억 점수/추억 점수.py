def solution(name, yearning, photo):
    answer = []
    # name 을 키로, 그리움 점수를 value 로 가지는 dictionary 를 만들고, key로 찾기.
    map = dict(zip(name, yearning))
    for p in photo:
        answer.append(sum(map.get(pp) for pp in p if map.get(pp) != None))
    return answer