from itertools import permutations as pt

def solution(numbers):
    answer = 0
    numbers_list = []
    
    for n in numbers:
        numbers_list.append(n)
    
    num_arr = set()
    for idx in range(1, len(numbers_list)+1):
        for p in pt(numbers_list, idx):
            num_arr.add(int(''.join(p)))

    minus = 0
    for num in num_arr:
        if num > 1:
            for i in range(2, num//2+1):
                if num%i == 0:
                    minus += 1
                    break
        else:
            minus += 1        
                
    return len(num_arr)-minus

numbers = "011"
print(solution(numbers))