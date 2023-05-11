# def solution(babbling):
        
#     answer = 0
#     token = ["aya", "ye", "woo", "ma" ]
    
#     for b in babbling:
#         for t in token:
#             b = b.replace(t, ' ')
#         # print(b)
#         if b.lstrip() == '':
#             answer += 1

    
#     return answer


# 순열/조합을 이용해서 푸는 방법
# 옹알이로 만들 수 있는 모든 순열을 만든 뒤에,
# 순열과 token 이 일치할 경우 1씩 증가

from itertools import permutations as p

def solution(babbling):
        
    answer = 0
    token = ["aya", "ye", "woo", "ma" ]
    p_token = []
    for j in range(1, 5):
        p_list = p([i for i in range(4)], j)
        for node in p_list:
            b_p = ''
            for n in node:
                b_p += token[n]
            p_token.append(b_p)
    
    for b in babbling:
        if b in p_token:
            answer += 1
    
    return answer 

# babbling=["aya", "yee", "u", "maa", "wyeoo"]	
babbling=["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]	

print(solution(babbling))