import math

def change_10_to_n(n, value):
    
    n_dic1 = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'
}
    result = ''
    q, r = divmod(n, value)
    while q > 0:
        result += n_dic1[r]
        q, r = divmod(q, value)

    result += n_dic1[r]
    return result[::-1]

def solution(n, k):
    n_list = ''
    if k < 10:
        n_list = change_10_to_n(n, k)
    else:
        n_list = str(n)
    nn_list = n_list.split('0')
    num_list = [x for x in nn_list if x != '']
    answer = 0
    
    for nnn in num_list:
        nn = int(nnn)
        if nn > 1:
            is_check = False
            for i in range(2, int( math.sqrt(nn) ) + 1):
                if nn%i == 0:
                    is_check = True
                    break
            if not is_check:
                answer += 1
    
    return answer

n, k=437674, 3
n, k=110011, 10
print(solution(n, k))