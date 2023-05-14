def solution(n, lost, reserve):
    
    n_dict = dict.fromkeys(range(1, n+1), 1)
    
    for l in lost:
        n_dict[l] -= 1
    
    for r in reserve:
        n_dict[r] += 1
    
    for k, v in n_dict.items():
        if v == 2:
            if k > 1 and n_dict[k-1] == 0:
                n_dict[k-1] += 1
                n_dict[k] -= 1
            elif k < len(n_dict) and n_dict[k+1] == 0:
                n_dict[k+1] += 1
                n_dict[k] -= 1
    
    answer = n
    for k, v in n_dict.items():
        if v == 0:
            answer -= 1
    
    return answer
    
    
n=5	
lost=[2, 4]
reserve=[1, 3, 5]

print(solution(n, lost, reserve))