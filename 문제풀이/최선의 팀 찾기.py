import sys
sys.setrecursionlimit(10**9)

sys.stdin = open('/Users/s/Desktop/C/dev_study/coding-test/python_input/codingtest_2.txt')

def solution():
    T = int(sys.stdin.readline().rstrip())

    for i in range(T):
        
        N = int(sys.stdin.readline().rstrip())
        arr = list(map(int, sys.stdin.readline().split()))
        
        # 배열 내에서 가장 큰 값을 찾는다.
        arr.sort()
        
        answerN = 0
        
        max_1 = abs(sum(arr))

        if(len(arr) == 1) : 
            print("#"+str(i+1)+" "+str(abs(arr[0])%10000007))
        else:
            for node in range(len(arr)):
                data_1 = arr.copy()
                data_2 = arr.copy()
                # node 가 0번이라면
                if(node == 0):
                    data_1.pop(1)
                    data_2.pop(-1)
                    max_2 = abs(sum(data_1))
                    max_3 = abs(sum(data_2))
                    answerN += max(max_1, max_2, max_3)
                # node 가 가장 마지막이라면
                elif (node == len(arr)):
                    data_1.pop(0)
                    data_2.pop(node-1)
                    max_2 = abs(sum(data_1))
                    max_3 = abs(sum(data_2))
                    answerN += max(max_1, max_2, max_3)
                else:
                    data_1.pop(0)
                    data_2.pop(-1)
                    max_2 = abs(sum(data_1))
                    max_3 = abs(sum(data_2))
                    answerN += max(max_1, max_2, max_3)
                
            print("#"+str(i+1)+" "+str(answerN%10000007))

solution()
            
# def solution_1():
#     T = int(input())

#     for i in range(T):
#         N = int(input())
#         arr = list(map(int, input().split()))

#         answer = []
#         for i in range(N):
#             max_sum = float('-inf')
#             for s in range(N):
#                 for t in range(s, N):
#                     if s <= i <= t:
#                         temp_sum = sum(arr[s:t+1])
#                         max_sum = max(max_sum, temp_sum)
#                         for j in range(s, t+1):
#                             if j != i:
#                                 temp_sum -= arr[j]
#                                 max_sum = max(max_sum, temp_sum)
#                                 temp_sum += arr[j]
#             answer.append(max_sum)

#         print(' '.join(map(str, answer)))
        
        
# solution_1()

