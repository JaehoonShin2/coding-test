from collections import Counter

def solution(k, tangerine):
    
    answer = 0
    tangerine_dict = Counter(tangerine)

    sorted_dict = sorted(tangerine_dict.items(), key= lambda item : item[1], reverse=True)

    for key, value in sorted_dict:
        
        k -= value
        answer += 1
        
        if k <= 0:
            break
    
    return answer

k1=6
tangerine1= [1, 3, 2, 5, 4, 5, 2, 3]	

print(solution(k1, tangerine1))