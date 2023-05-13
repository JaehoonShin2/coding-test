def solution(n, lost, reserve):
    
    n_dict = dict.fromkeys(range(1, n+1), 1)
    
    print(n_dict)   
    
    for l in lost:
        n_dict[l] -= 1
    
    print(n_dict)
    
n=5	
lost=[2, 4]
reserve=[1, 3, 5]

print(solution(n, lost, reserve))