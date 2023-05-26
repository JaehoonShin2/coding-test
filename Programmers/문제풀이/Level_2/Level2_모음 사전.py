from math import pow

def solution(word):

    answer = []
    alpha = ['A', 'E', 'I', 'O', 'U', '']
    for i in alpha:
        for j in alpha:
            for k in alpha:
                for l in alpha:
                    for m in alpha:
                        nw = i+j+k+l+m 
                        if nw not in answer: answer.append(nw)
                        

    answer.sort()
    print(answer[:11])
    a = answer.index(word)
    
    return a


word='AAAE'
print(solution(word))



def solution(word):

    answer= 0
    
    l = len(word)
    max_l = sum(int(pow(5, x)) for x in range(1, 6))
    
    for idx, w in enumerate(word):
        if w == 'A': answer += 1
        elif w == 'E': answer += (int(max_l / pow(5, idx+1)) * 1) + 1
        elif w == 'I': answer += (int(max_l / pow(5, idx+1)) * 2) + 1
        elif w == 'O': answer += (int(max_l / pow(5, idx+1)) * 3) + 1
        else: answer += (int(max_l / pow(5, idx+1)) * 4) + 1

    return answer