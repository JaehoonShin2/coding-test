def solution(number, k):
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            print(stack.pop())
            k -= 1
        stack.append(n)
        print(stack)

    # 아직 제거되지 못 한 숫자를 뒤에서 삭제
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)
    

number="1231234"
k=3
number="1924"
k=2
number="4177252841"
k=4
# number='9998887776665554443332221110009'
# k=30
print(solution(number, k))


# def solution(number, k):
    
#     max_list = []
#     l = len(number)
#     max_l = k + 1
#     start = 0
    
#     max_value = number[start]
#     max_index = start
    
#     # 0 부터 k + 1 만큼 중에서 가장 큰 값을 추출
#     for i in range(1, max_l):
#         print(number[i])
#         if number[i] == '9':
#             # 가장 큰 값을 max_value 로 넣고,
#             # 해당 인덱스를 max_index 로 지정
#             max_value = number[i]
#             max_index = i
#             break
#         if number[i] > max_value:
#             max_value = number[i]
#             max_index = i
#     # max_value 를 리스트에 넣고
#     max_list.append(str(max_value))
    
#     while len(max_list) < l-k :
#         # 시작점을 max_index + 1 로 변경
#         start = max_index + 1
#         max_value = number[start]
#         max_index = start
#         max_l += 1
#         print("----")
#         for i in range(start, max_l):
#             print('test : {}'.format(i))
#             if number[i] == '9':
#             # 가장 큰 값을 max_value 로 넣고,
#             # 해당 인덱스를 max_index 로 지정
#                 max_value = number[i]
#                 max_index = i
#                 break
#             if number[i] > max_value:
#                 max_value = number[i]
#                 max_index = i
#         # max_value 를 리스트에 넣고
#         max_list.append(str(max_value))
        
#     return ''.join(max_list)


# def solution(number, k):
    
#     max_list = []
#     l = len(number)
#     max_l = k + 1
#     start = 0
#     while len(max_list) < l-k :
#         d = max(number[start:max_l])
#         d_index = number[start:max_l].index(d) + start
#         max_list.append(str(d))
#         start = d_index + 1
#         max_l += 1
    
#     return ''.join(max_list)