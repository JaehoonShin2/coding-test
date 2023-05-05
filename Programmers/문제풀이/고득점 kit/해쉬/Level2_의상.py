from collections import Counter

def solution(clothes):
    answer = 1
    counter = Counter([type for clothe, type in clothes])
    for k, cnt in counter.items():
        answer *= (cnt+1)
    return answer-1        
    

# clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes=[['동그란 안경', '얼굴'], ['검정 선글라스','얼굴'], ['파란색 티셔츠', '상의'], ['청바지', '하의'], ['긴 코트', '겉옷']]
clothes=[["yellow_hat", "headgear"],
        ["green_turban", "headgear"],
        ["blue_sunglasses", "eyewear"],
        ["red_shirt", "top"],
        ["blue_jeans", "bottoms"]]
print(solution(clothes))

