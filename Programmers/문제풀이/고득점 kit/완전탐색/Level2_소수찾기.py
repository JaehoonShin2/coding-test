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


# def solution(numbers):
#     answer = 0
    
    # numbers_list = []
    
    # for n in numbers:
    #     numbers_list.append(n)
    
    # num_arr = set()
    # for idx in range(1, len(numbers_list)+1):
    #     for p in pt(numbers_list, idx):
    #         num_arr.add(int(''.join(p)))
    
    # num_arr = set()
    
    # for idx in range(1, len(numbers)+1):
    #     for p in pt(range(len(numbers)), idx):
    #         num_str = ''
    #         for num in p:
    #             num_str += numbers[int(num)]
    #         num_arr.add(int(num_str))
            
    # isFalse = [False] * (max(num_arr)+1)

    # for i in range(2, (max(num_arr)+1)):

    #     if i in num_arr:
    #         if i > 1 and isFalse[i] == False:
    #             answer += 1

    #     for j in range(i, max(num_arr)+1, i):
    #         isFalse[j] = True
    
    # return answer