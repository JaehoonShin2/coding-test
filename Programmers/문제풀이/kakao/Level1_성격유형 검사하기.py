from collections import defaultdict

def solution(survey, choices):
    answer = ''
    
    test_model = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    # test_model = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
        
    test_model_dict = defaultdict(int)
    
    for idx, sur in enumerate(survey):
        left, right = sur[0], sur[1]
        if choices[idx] > 4:
            test_model_dict[right] += abs(choices[idx]-4)
        elif choices[idx] < 4:
            test_model_dict[left] += abs(choices[idx]-4)
    
    for t in test_model:
        l, r = t
        if test_model_dict[l] < test_model_dict[r]:
            answer += r
        else:
            answer += l
    
    return answer
    
    
survey=["AN", "CF", "MJ", "RT", "NA"]
choices=[5, 3, 2, 7, 5]

print(solution(survey, choices))