from collections import defaultdict as dd, Counter

def solution(topping):
    answer = 0
    toppings_1 = dd(int)
    toppings_2 = Counter(topping)
    
    for i in topping:
        toppings_1[i] += 1
        toppings_2[i] -= 1
        if toppings_2[i] == 0: 
            toppings_2.pop(i)
        
        a = len(toppings_1.keys())
        b = len(toppings_2.keys())
        
        if a == b: answer += 1
        elif a > b: break
        
        print(f'철수의 토핑의 총 갯수 : {len(toppings_1)}')
        print(f'동생의 토핑의 총 갯수 : {len(toppings_2)}')
          
    return answer


topping=[1, 2, 1, 3, 1, 4, 1, 2]
print(solution(topping))

# from collections import deque

# def solution(topping):
#     answer = 0
#     l = len(topping)
#     q = deque(topping)
#     toppings_1 = dict()
#     # toppings_2 = dict()
#     for i in range(1, l):
#         toppings_1[q.popleft()] = 0
#         toppings_2 = dict.fromkeys(q)
#         print(f'철수의 토핑의 총 갯수 : {len(toppings_1)}')
#         print(f'동생의 토핑의 총 갯수 : {len(toppings_2)}')

#         if len(toppings_1) == len(toppings_2):
#             answer += 1
            
#     return answer