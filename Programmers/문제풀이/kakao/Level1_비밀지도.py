def bin_change(arr, n):
    bin_list = []
    for x in arr:
        x = bin(x)[2:]
        while len(x) < n:
            x = '0'+x
        bin_list.append(x)
    return bin_list

def solution(n, arr1, arr2):
    answer = []
    bin_arr1 = bin_change(arr1, n)
    bin_arr2 = bin_change(arr2, n)
    
    key = [['#'] * n for _ in range(n)]
    
    answer = []
    
    for i in range(n):
        for j in range(n):
            if bin_arr1[i][j] == '0' and bin_arr2[i][j] == '0':
                key[i][j] = ' '
        answer.append(''.join(key[i]))
        
    return answer

n=6
arr1=[46, 33, 33 ,22, 31, 50]
arr2=[27 ,56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))