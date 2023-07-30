# from collections import defaultdict as dd

# def solution(strings, n):
    
#     answer = []
    
#     temp_dic = dd(list)
    
#     for s in strings:
#         temp_dic[s[n]].append(s)
        
#     # 딕셔너리의 키 정렬
#     temp_key = [k for k in temp_dic.keys()]
#     temp_key.sort()
    
#     for tk in temp_key:
#         temp_dic[tk].sort()
#         answer += temp_dic[tk]
    
#     return answer

def solution(strings, n):
    
    return sorted(sorted(strings), key=lambda x: x[n])

strings = ["abce", "abcd", "cdx"]
n =  2

print(solution(strings, n))