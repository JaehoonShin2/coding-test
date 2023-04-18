from collections import Counter

# def solution(want, number, discount):
#     answer = 0
    
#     want_dict = {}
#     number_sum = sum(number)
        
#     for i in range(len(want)):
#         want_dict[want[i]] = number[i]
            
#     for idx in range(len(discount)-len(number)):
#         discount_dict = Counter(discount[idx:number_sum+idx])
        
#         isCount = True
        
#         for k, v in want_dict.items():
#             if discount_dict[k] != v:
#                 isCount = False
#                 break
        
#         if isCount: answer += 1
    
#     return answer

def solution(want, number, discount):
    answer = 0
    
    want_dict = {}
    number_sum = sum(number)
        
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
            
    for idx in range(len(discount)-len(number)):
        if want_dict ==  Counter(discount[idx:number_sum+idx]):
            answer += 1
        
    return answer


want=["banana", "apple", "rice", "pork", "pot"]
number=[3, 2, 2, 2, 1]
discount=["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

print(solution(want, number, discount))