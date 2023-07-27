def solution(a, b, n):
    # 최종적으로 받을 수 있는 콜라의 갯수
    answer = 0
    # 현재 가진 콜라의 갯수가 a보다 크다면 반복
    while n >= a:
        # temp 는 n에서 a를 나눈 몫 * b개
        temp = (n // a) * b
        # answer 에 temp 를 더해줌
        answer += temp
        # 새로운 n는 돌려받은 temp 개 + 나누어떨어지지 않아 남은 갯수
        n = temp + (n % a)
    return answer
