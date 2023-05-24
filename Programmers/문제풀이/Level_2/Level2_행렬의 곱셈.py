def solution(arr1, arr2):

    print(*arr2)
    
    l = []
    for a in zip(arr1):
        for b in zip(*arr2):
            for x, y in zip(a, b):
                l.append(sum(x*y))

    print(l)

# def solution(arr1, arr2):

#     row1, col1, row2, col2 = len(arr1), len(arr1[0]), len(arr2), len(arr2[0])
#     answer = [[0] * col2 for _ in range(row1)]

#     for i in range(row1):
#         for j in range(col2):
#             total = 0
#             for k in range(col1):
#                 total += arr1[i][k] * arr2[k][j]
#             answer[i][j] = total
        
#     return answer

arr1=[[2, 3, 2], 
      [4, 2, 4], 
      [3, 1, 4]]

arr2=[[5, 4, 3], 
      [2, 4, 1], 
      [3, 1, 1]]

arr1 = [[1,2,3,4], 
        [1,2,3,4]]
arr2 = [[1,2], 
        [1,2], 
        [1,2], 
        [1,2]]

# arr1=[[1, 4], 
#       [3, 2], 
#       [4, 1]]

# arr2=[[3, 3], 
#       [3, 3]]

print(solution(arr1, arr2))