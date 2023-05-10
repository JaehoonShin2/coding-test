def solution(numbers):

    numbers=list(map(str, numbers))
    
    # numbers.sort(key=lambda x: (x*3)[:4], reverse=True)
    # x*3 이 가능한 이유
    # 문자열은 아스키값으로 치환되서 정렬되기 때문에 
    # 첫번째 인덱스값으로 비교를 합니다. 
    # (666,101010,222)여기서는 아스키값으로 보면 
    # 1: 81, 2: 82, 6:86 이기 때문에 위와 같은 결과가 나옵니다
    # 666을 문자치환 후 정렬하면 868686 vs 818081808180 vs 828282
    # 로 치환 후 비교가 되게 된다는 것
    
    numbers.sort(key=lambda x: (x*4)[:4], reverse=True)

    answer = ''.join(numbers)
    
    # 만약 answer 의 최초값이 0이라면, 그냥 0을 리턴
    if answer[0] == '0':
        return '0'
    else:
        return answer
    
numbers=[3, 30, 34, 5, 9]
numbers=[0, 0, 0, 0, 0]
print(solution(numbers))