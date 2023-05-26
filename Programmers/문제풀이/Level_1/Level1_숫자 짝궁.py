from collections import Counter

def solution(X, Y):
    
    x_c = Counter(X)
    y_c = Counter(Y)
    n_list = []
    for i in range(10):
        ii = str(i)
        if x_c[ii] > 0 and y_c[ii] > 0:
            min_cnt = min(x_c[ii], y_c[ii])
            for _ in range(min_cnt):
                n_list.append(ii)
                
    n_list.sort(reverse=True)
    if not n_list: return '-1'
    else: 
        # 이 코드의 시간 복잡도는 n_list의 길이에 선형적으로 비례합니다. 
        # 리스트의 길이에 따라 문자열 결합과 정수 변환의 연산이 수행되기 때문에, 
        # 리스트의 길이가 길수록 연산에 걸리는 시간도 증가합니다. 
        # 따라서 시간 복잡도는 O(n)입니다. 여기서 n은 n_list의 길이입니다.
        # return str(int(''.join(n_list)))
        if n_list[0] == '0':
            return '0'
        else: return ''.join(n_list)
X,Y="12321", "42531"
X,Y='2444556', '2244567'
print(solution(X, Y))