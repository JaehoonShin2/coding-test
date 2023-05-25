import math 

def solution(number, limit, power):
    
    n_list = [0] * (number+1)
    n_list[1] = 1
    
    for i in range(2, number+1):
        print('제곱근 : {}'.format(int(math.sqrt(i))+1))
        cd = 0
        for j in range(1, int(math.sqrt(i))+1):
            print(i, j)
            if i % j == 0:
                cd += 1
                if j != math.sqrt(i):
                    cd += 1
            
        n_list[i] = cd
        
    result = sum(x if x <= limit else power for x in n_list)
    return result

number, limit, power = 10, 3, 2
print(solution(number, limit, power))