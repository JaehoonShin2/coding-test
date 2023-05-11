
def solution(babbling):
    answer = 0
    speak = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        for s in speak:
            if s*2 not in b:
                b = b.replace(s, ' ')
        if b.lstrip() == '':
            answer += 1
    return answer

babbling=["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babbling))


# 순열로 풀 수가 없는 문재였음
# 왜냐하면 4가지 발음을 조합해 만들 수 있는 발음밖에 못하는데,
# 1,2,3,2,1.. 과 같이 4개 이상의 발음도 가능하기 때문

# permutations = set()

# def perm(temp, avail, count, k):
    
#     if count == k:
#         permutations.add(''.join(temp))
#         return

#     else:
#         for i in range(len(avail)):
#             if len(temp) > 0:
#                 if avail[i] != temp[-1]:
#                     temp.append(avail[i])
#                     perm(temp, avail, count+1, k)
#                     temp.pop()
#             else:
#                 temp.append(avail[i])
#                 perm(temp, avail, count+1, k)
#                 temp.pop()

# def solution(babbling):
    
#     if not babbling: # 빈 문자열("")일 경우 0을 반환
#         return 0
    
#     avail = ["aya", "ye", "woo", "ma"]
    
#     for cnt in range(1, len(avail)+1):
#         temp = []
#         perm(temp, avail, 0, cnt)
        
#     answer = 0
#     for b in babbling:
#         if b in permutations:
#             answer += 1    
            
#     return answer
