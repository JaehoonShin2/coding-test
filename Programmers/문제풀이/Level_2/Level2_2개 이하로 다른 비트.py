def solution(numbers):
    result = []
    for number in numbers:
        print(bin(number))
        b_n = ['0'] + list(bin(number)[2:])
        l = len(b_n)
        check = False
        for i in range(l - 1, 0, -1):
            if b_n[i] == '0':
                check = True
                b_n[i] = '1'
                break
            elif b_n[i] == '1':
                if b_n[i - 1] == '0':
                    check = True
                    b_n[i] = '0'
                    b_n[i - 1] = '1'
                    break
        
        a = ''.join(b_n)
        result.append(int(a, 2))
    
    return result
    
numbers = [2, 7]
print(solution(numbers))
