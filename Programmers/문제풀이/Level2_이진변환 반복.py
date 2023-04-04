# def solution(s):
#     answer = []
    
#     bin_cnt = 0
#     zero_cnt = 0
    
#     # 문자를 1개씩 쪼개서 0일 경우 제거, 제거할 때마다 +1
#     # 모두 제거가 완료되면 1의 갯수를 세서 이진법으로 변환
#     isEnd = True
    
#     while isEnd:
#         one_cnt = 0
#         z_cnt = 0
#         for i in s:
#             # 1이면 1 증가
#             if i == '1':
#                 one_cnt += 1
#             else: 
#                 z_cnt += 1

#         zero_cnt += z_cnt
#         bin_cnt += 1
#         # 최종 1의 갯수를 이진으로 변환하고 다시 반복
#         s = bin(one_cnt)[2:]
        
#         if s == '1':
#             isEnd = False
    
#     answer = [bin_cnt, zero_cnt]
#     return answer


# python 에서 count 함수를 사용하면 리스트 내에서의 인자의 갯수를 알 수 있다.


def solution_re(s):
    a, b = 0, 0
    # s 가 '1' 이 아니라면 반복
    while s != '1':
        # 이진을 한 회수
        a += 1
        # '1' 의 갯수 세기
        num = s.count('1')
        # 전체 s의 갯수에서 1의 갯수를 빼기 == 0의 갯수
        b += len(s) - num
        # '1'의 갯수만큼 이진으로 변환
        s = bin(num)[2:]
    return [a, b]

print(solution_re('110011'))
        