from itertools import permutations as pt

def solution(numbers):
    answer = 0
    
    numbers_list = []
    
    for n in numbers:
        numbers_list.append(n)
    
    # print(numbers_lsit)
    
    p_arr = []
    for idx in range(1, len(numbers_list)+1):
        p_arr.append(list(p(numbers_list, idx)))
    
    num_arr = set()

    for idx in range(1, len(numbers)+1):
        for p in pt(range(len(numbers)), idx):
            num_str = ''
            for num in p:
                num_str += numbers[int(num)]
            num_arr.add(int(num_str))
    
    # for idx in range(1, len(numbers)+1):
    #     for p in pt(range(len(numbers)), idx):
    #         num_str = ''
    #         for num in p:
    #             num_str += numbers[int(num)]
    #         num_arr.add(int(num_str))
            
    
    print(num_arr)
    
    isFalse = [False] * (max(num_arr)+1)

    for i in range(2, (max(num_arr)+1)):

        if i in num_arr:
            if i > 1 and isFalse[i] == False:
                answer += 1

        for j in range(i, max(num_arr)+1, i):
            isFalse[j] = True


    # numbers 를 순열로 해서 조합 가능한 모든 수를 찾고, 해당 숫자가 소수인지 확인하기
    
    
    return answer

numbers = "17"
print(solution(numbers))