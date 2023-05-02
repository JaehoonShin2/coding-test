from collections import Counter

def solution(participant, completion):
    
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    
    for p in p_counter:
        if p_counter[p] != c_counter[p]:
            return p

participant=["leo", "kiki", "eden"]
completion=["eden", "kiki"]

print(solution(participant, completion))