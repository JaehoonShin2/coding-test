def solution(a, b, n):
    # 총 받을 수 있는 콜라의 갯수
    answer = 0
    # 해당 시점에서 남은 콜라의 갯수
    temp = 0
    # 돌려받은 콜라의 갯수+남은 콜라의 갯수가 a보다 작아질 때까지
    while (n + temp) >= a:
        # 만약 나누고 남은 콜라가 있고, n%a != 이라면
        if n % a != 0 and temp > 0 :
            n += temp
            temp = 0
        
        # 현재의 콜라에서의 남을 갯수
        temp = temp + (n % a)
        
        # c 는 n 개에서 a개만큼 나눈 값
        c = n // a
        
        # b개만큼 돌려줄 떄, c번 콜라를 가져다줌
        n = b*c
        
        answer += n
    
    return answer